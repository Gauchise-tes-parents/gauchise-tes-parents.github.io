// v13 — Parcours dans le navigateur : réponse de l'IA (Gemini SIMULÉ derrière le vrai code du backend) et confidentialité.
// Le backend IA est le vrai gestionnaire du Worker (worker/src/handler.js) ; seule l'API Google est simulée.
import { test, describe, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { testConfig, startServer } from '../helpers.js';
import { createHandler } from '../../worker/src/handler.js';
import { loadLibrary } from '../../server/library.js';
import { buildKb } from '../../server/kbexport.js';

let chromium = null;
try { ({ chromium } = await import('playwright')); } catch {
  for (const p of [process.env.PLAYWRIGHT_PATH, '/opt/npm-tools/node_modules/playwright/index.mjs'].filter(Boolean)) { try { ({ chromium } = await import(p)); break; } catch { /* suivant */ } }
}
const skip = chromium ? false : 'Playwright non installé';
const PHONE = { width: 390, height: 844 };
const FICHES = JSON.parse(buildKb(loadLibrary(undefined, { warn() {} })).json).fiches;

function gemini() {
  const appels = [];
  const fn = async (url, init) => {
    const body = JSON.parse(init.body);
    appels.push(body);
    const mode = /COUP EXPRESS/.test(body.systemInstruction.parts[0].text) ? 'express' : 'autre';
    const court = /PLUS COURTE/.test(body.systemInstruction.parts[0].text);
    const obj = {
      sujet: 'Sujet repéré', reponse_directe: court ? 'Version courte de la réponse.' : mode === 'express' ? 'Réponse express à dire telle quelle.' : 'Réponse directe et argumentée. Plus de détails sur https://invente.example/x',
      arguments: [{ texte: 'Argument tiré de la fiche', statut: 'fait', sources: ['B1'] }, { texte: 'Argument tiré de la recherche', statut: 'estimation', sources: ['WEB'] }, { texte: 'Connaissance du modèle', statut: 'interpretation', sources: [] }],
      chiffres: [], replique: 'La formule qui marque.', contre_arguments: [{ objection: 'Mais pourtant…', reponse: 'Réponse à l’objection.' }], procedes: [{ nom: 'Généralisation abusive', explication: 'Un cas devient une règle.' }], limites: 'Données limitées.',
    };
    return { ok: true, status: 200, json: async () => ({ candidates: [{ content: { parts: [{ text: JSON.stringify(obj) }] }, finishReason: 'STOP', groundingMetadata: { webSearchQueries: ['recherche test'], groundingChunks: [{ web: { uri: 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/test', title: 'insee.fr' } }] } }] }) };
  };
  fn.appels = appels;
  return fn;
}

describe('interface — IA Gemini (simulée) et confidentialité', { skip }, () => {
  let s; let browser; let g; const errors = [];
  before(async () => {
    s = await startServer(testConfig({ liveMode: false, apiKey: '' }));
    browser = await chromium.launch();
  });
  after(async () => { await browser?.close(); await s?.close(); });

  async function page({ ia = true } = {}) {
    const ctx = await browser.newContext({ viewport: PHONE, isMobile: true, hasTouch: true, reducedMotion: 'reduce', serviceWorkers: 'block' });
    await ctx.addInitScript(() => { if (!localStorage.getItem('gtp-donnees-v1')) localStorage.setItem('gtp-donnees-v1', JSON.stringify({ reglages: { mode: 'autonome', majAuto: false } })); });
    const p = await ctx.newPage();
    p.on('pageerror', (e) => errors.push(e.message));
    p.on('console', (m) => { if (m.type() === 'error' && !/Failed to load resource/.test(m.text())) errors.push(m.text()); });
    const externes = [];
    p.on('request', (r) => { if (!r.url().startsWith(s.base) && !r.url().startsWith('data:')) externes.push(r.url()); });
    p.externes = externes;
    if (ia) {
      g = gemini();
      const handler = createHandler({ fiches: FICHES, fetchImpl: g, cache: null, journal: { log() {} } });
      const env = { GEMINI_API_KEY: 'cle-test', GEMINI_MODEL: 'gemini-test', ALLOWED_ORIGINS: s.base, LIMITE_PAR_VISITEUR: '100' };
      // le site déclare un backend IA à la même origine ; ses requêtes sont servies par le vrai gestionnaire du Worker
      await p.route('**/config.js', (r) => r.fulfill({ contentType: 'text/javascript', body: `window.GTP_CONFIG = { apiBase: null, iaBase: ${JSON.stringify(s.base)} };` }));
      await p.route('**/api/ia**', async (r) => {
        const req = r.request();
        const res = await handler(new Request(req.url(), { method: req.method(), headers: { ...req.headers(), origin: s.base }, body: req.method() === 'POST' ? req.postData() : undefined }), env);
        await r.fulfill({ status: res.status, headers: Object.fromEntries(res.headers), body: await res.text() });
      });
    }
    return p;
  }
  const express = async (p, t, mode = 'gagner') => {
    await p.goto(`${s.base}/#/express`);
    await p.locator(`[data-express-mode="${mode}"]`).click();
    await p.locator('#express-text').fill(t);
    await p.getByRole('button', { name: 'Sortir une réplique' }).click();
    await p.waitForFunction(() => ['#/argumentaire', '#/introuvable'].includes(location.hash));
  };

  test('sans fiche : l’IA répond automatiquement, origine et statut de chaque élément affichés, lien inventé retiré', async () => {
    const p = await page();
    await p.goto(`${s.base}/#/express`);
    await p.locator('.privacy-note[data-transmission="ia"]').waitFor();
    await express(p, 'Le prix du pain au Moyen Âge était-il régulé ?');
    await p.locator('.ia-contenu').waitFor();
    const txt = await p.locator('#ia-block').innerText();
    assert.match(txt, /Rédigé par Gemini/);
    assert.match(txt, /Recherche Google effectuée/);
    assert.match(txt, /Aucune fiche de la bibliothèque/);
    assert.match(txt, /Non vérifié/i, 'la connaissance du modèle sans source est marquée non vérifiée');
    assert.ok(!/invente\.example/.test(txt));
    assert.ok(await p.locator('#ia-block a[href^="https://vertexaisearch.cloud.google.com/"]').count(), 'page réellement consultée');
    assert.equal(g.appels.length, 1);
    // version plus courte : un nouvel appel, avec la variante
    await p.locator('[data-ia="plus_court"]').click();
    await p.getByText('Version courte de la réponse.').waitFor();
    assert.equal(g.appels.length, 2);
    assert.match(g.appels[1].systemInstruction.parts[0].text, /PLUS COURTE/);
    assert.ok((await p.evaluate(() => document.documentElement.scrollWidth - window.innerWidth)) <= 1);
    await p.context().close();
  });

  test('avec fiche : la bibliothèque répond d’abord, l’IA seulement à la demande (coup express)', async () => {
    const p = await page();
    await p.goto(`${s.base}/#/express`);
    await p.locator('.privacy-note[data-transmission="ia"]').waitFor();
    await express(p, 'Il y a des millions de cartes Vitale en trop.', 'gagner');
    await p.locator('#ia-block [data-ia="express"]').waitFor();
    assert.equal(g.appels.length, 0, 'pas d’appel automatique quand une fiche répond');
    await p.locator('#ia-block [data-ia="express"]').click();
    await p.getByText('Réponse express à dire telle quelle.').waitFor();
    const txt = await p.locator('#ia-block').innerText();
    assert.match(txt, /Bibliothèque : « Il y a des millions de cartes Vitale en trop/);
    assert.ok(await p.locator('#ia-block a[href="#/bibliotheque/cartes-vitale-en-trop"]').count());
    assert.equal(g.appels.length, 1);
    assert.match(g.appels[0].systemInstruction.parts[0].text, /COUP EXPRESS/);
    await p.context().close();
  });

  test('confidentialité : aucune requête vers un autre site, aucune question conservée dans le navigateur', async () => {
    const p = await page({ ia: false });
    const q = 'Mon voisin Gérard dit que les immigrés prennent le travail des Français.';
    await express(p, q);
    await p.goto(`${s.base}/#/confidentialite`);
    await p.getByRole('heading', { name: 'Confidentialité et sécurité' }).waitFor();
    const stockage = await p.evaluate(() => JSON.stringify({ l: { ...localStorage }, s: { ...sessionStorage }, c: document.cookie }));
    assert.ok(!stockage.includes('Gérard') && !stockage.includes('prennent le travail'), stockage.slice(0, 300));
    assert.equal(JSON.parse(stockage).c, '');
    assert.deepEqual(p.externes, [], 'aucun appel à un site tiers');
    // aucune autorisation demandée par la page
    const perms = await p.evaluate(async () => Promise.all(['geolocation', 'camera', 'microphone', 'notifications'].map(async (n) => { try { return (await navigator.permissions.query({ name: n })).state; } catch { return 'n/a'; } })));
    assert.ok(perms.every((x) => x !== 'granted'), perms.join(','));
    assert.match(await p.locator('main').innerText(), /Aucune géolocalisation/);
    assert.match(await p.locator('main').innerText(), /GitHub Pages indique enregistrer l’adresse IP/);
    await p.context().close();
  });

  test('aucune erreur JavaScript', () => { assert.deepEqual(errors, []); });
});
