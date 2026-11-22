// v15.1 (affluence) : la base est téléchargée depuis le relais Cloudflare si son empreinte correspond au manifeste
// de GitHub Pages ; sinon (relais en retard, altéré ou en panne) depuis GitHub Pages. Une seule fois par visite.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { loadLibrary } from '../../server/library.js';
import { buildKb } from '../../server/kbexport.js';

const { json, manifest } = buildKb(loadLibrary(undefined, { warn() {} }).slice(0, 30));
const RELAIS = 'https://gauchise-direct.exemple.workers.dev/kb';

async function charger(relais) {
  const appels = [];
  globalThis.window = { GTP_CONFIG: { kbRelais: RELAIS } };
  globalThis.localStorage = { _m: {}, getItem(k) { return this._m[k] ?? null; }, setItem(k, v) { this._m[k] = v; } };
  globalThis.fetch = async (url) => {
    appels.push(String(url));
    if (String(url).startsWith(RELAIS)) return relais();
    if (String(url).startsWith('kb/manifest.json')) return new Response(JSON.stringify(manifest));
    if (String(url).startsWith('kb/base.json')) return new Response(json);
    throw new Error(url);
  };
  const { kb } = await import(`../../public/js/kbstore.js?t=${Math.random()}`);
  await kb.load();
  return { kb, appels };
}

test('relais à jour : la base vient du relais, GitHub Pages ne sert que le petit manifeste', async () => {
  const { kb, appels } = await charger(() => new Response(json));
  assert.equal(kb.fiches.length, 30);
  assert.ok(appels.some((u) => u === `${RELAIS}/base.json?v=${encodeURIComponent(manifest.version)}`));
  assert.ok(!appels.some((u) => u.startsWith('kb/base.json')), 'pas de double téléchargement');
});

test('relais en retard ou altéré : empreinte refusée, copie de GitHub Pages', async () => {
  const autre = json.replace('"format":3', '"format":3 ');
  assert.notEqual(createHash('sha256').update(autre).digest('hex'), manifest.sha256);
  const { kb, appels } = await charger(() => new Response(autre));
  assert.equal(kb.fiches.length, 30);
  assert.ok(appels.some((u) => u.startsWith('kb/base.json')));
});

test('relais en panne : copie de GitHub Pages, sans erreur visible', async () => {
  const { kb } = await charger(() => { throw new Error('réseau'); });
  assert.equal(kb.fiches.length, 30);
  const r = await charger(() => new Response('erreur 1027', { status: 429 }));
  assert.equal(r.kb.fiches.length, 30);
});
