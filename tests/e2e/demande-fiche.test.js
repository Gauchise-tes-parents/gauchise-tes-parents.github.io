// v15 — Questions sans réponse : le bouton « Envoyer anonymement ma question » n'existe que si un collecteur est
// configuré, rien ne part sans clic, et seul le texte de la question est envoyé.
import { test, describe, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, readFileSync, existsSync, statSync } from 'node:fs';
import { join, extname } from 'node:path';
import { tmpdir } from 'node:os';

let chromium = null;
try { ({ chromium } = await import('playwright')); } catch {
  for (const p of [process.env.PLAYWRIGHT_PATH, '/opt/npm-tools/node_modules/playwright/index.mjs'].filter(Boolean)) { try { ({ chromium } = await import(p)); break; } catch { /* suivant */ } }
}
const skip = chromium ? false : 'Playwright non installé';
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.woff': 'font/woff', '.png': 'image/png', '.webmanifest': 'application/manifest+json' };
const servir = (racine, gerer = null) => new Promise((ok) => {
  const srv = createServer((q, r) => {
    if (gerer && gerer(q, r)) return;
    let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html';
    const f = join(racine, p);
    if (!existsSync(f) || statSync(f).isDirectory()) { r.writeHead(404); r.end(); return; }
    r.writeHead(200, { 'content-type': TYPES[extname(f)] || 'application/octet-stream' }); r.end(readFileSync(f));
  }).listen(0, '127.0.0.1', () => ok(srv));
});

describe('demande de fiche (collecte opt-in)', { skip }, () => {
  let site, collecteur, browser; const recues = [];
  before(async () => {
    collecteur = await servir('/nonexistent', (q, r) => {
      const cors = { 'access-control-allow-origin': '*', 'access-control-allow-headers': 'content-type' };
      if (q.method === 'OPTIONS') { r.writeHead(204, cors); r.end(); return true; }
      let b = ''; q.on('data', (c) => { b += c; }); q.on('end', () => { recues.push({ url: q.url, body: b, cookie: q.headers.cookie || null }); r.writeHead(201, { ...cors, 'content-type': 'application/json' }); r.end('{"ok":true}'); });
      return true;
    });
    const base = `http://127.0.0.1:${collecteur.address().port}`;
    const out = mkdtempSync(join(tmpdir(), 'gtp-site-'));
    // l'URL https est exigée en production ; le test remplace ensuite la configuration générée par l'adresse locale
    execFileSync(process.execPath, ['scripts/build-static.js'], { env: { ...process.env, STATIC_OUT: out, GTP_QUESTIONS_BASE: 'https://collecteur.example' }, stdio: 'ignore' });
    for (const f of ['config.js', 'index.html']) {
      const p = join(out, f);
      const t = readFileSync(p, 'utf8').replaceAll('https://collecteur.example', base);
      (await import('node:fs')).writeFileSync(p, t);
    }
    site = await servir(out);
    browser = await chromium.launch();
  });
  after(async () => { await browser?.close(); site?.close(); collecteur?.close(); });

  test('rien ne part sans clic ; au clic, seul le texte de la question', async () => {
    const page = await browser.newPage();
    await page.goto(`http://127.0.0.1:${site.address().port}/#/express`);
    await page.locator('#express-text').fill('Les colonies de vacances sont devenues inabordables');
    await page.getByRole('button', { name: 'Sortir une réplique' }).click();
    await page.waitForFunction(() => location.hash === '#/introuvable');
    const bouton = page.getByRole('button', { name: 'Envoyer anonymement ma question' });
    await bouton.waitFor();
    assert.equal(recues.length, 0, 'aucune requête avant le clic');
    await bouton.click();
    await page.waitForFunction(() => /Merci/.test(document.querySelector('#demande-fiche-msg')?.textContent || ''));
    assert.equal(recues.length, 1);
    assert.equal(recues[0].url, '/questions');
    assert.deepEqual(JSON.parse(recues[0].body), { texte: 'Les colonies de vacances sont devenues inabordables' });
    assert.equal(recues[0].cookie, null);
    await page.close();
  });
});
