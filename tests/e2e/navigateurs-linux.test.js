// v14.1 — Retours des premiers utilisateurs sous Linux : le site restait presque vide.
// Cause : Firefox en navigation privée, avec les cookies bloqués, ou durci (LibreWolf, Tor Browser…) annonce
// « serviceWorker » dans navigator mais renvoie undefined ou lève une SecurityError à l'accès ; l'exception
// arrêtait le démarrage avant le chargement de la base. On simule ici ces navigateurs (et d'autres API
// verrouillées) dans Chromium avec l'identité d'un Firefox Linux : l'accueil et la bibliothèque doivent s'afficher.
import { test, describe, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { testConfig, startServer } from '../helpers.js';

let chromium = null;
try { ({ chromium } = await import('playwright')); } catch {
  for (const p of [process.env.PLAYWRIGHT_PATH, '/opt/npm-tools/node_modules/playwright/index.mjs'].filter(Boolean)) { try { ({ chromium } = await import(p)); break; } catch { /* suivant */ } }
}
const skip = chromium ? false : 'Playwright non installé';
const UA = 'Mozilla/5.0 (X11; Linux x86_64; rv:115.0) Gecko/20100101 Firefox/115.0';
const insecure = "new DOMException('The operation is insecure.', 'SecurityError')";
const SCENARIOS = {
  'service worker absent (undefined)': "Object.defineProperty(Navigator.prototype, 'serviceWorker', { get() { return undefined; } });",
  'service worker interdit (SecurityError)': `Object.defineProperty(Navigator.prototype, 'serviceWorker', { get() { throw ${insecure}; } });`,
  'stockage interdit': `for (const k of ['localStorage', 'sessionStorage']) Object.defineProperty(window, k, { get() { throw ${insecure}; } });`,
  'Cache API interdite': `Object.defineProperty(window, 'caches', { get() { throw ${insecure}; } });`,
  'IndexedDB absente': "Object.defineProperty(window, 'indexedDB', { get() { return null; } });",
  'crypto.subtle absent': "Object.defineProperty(crypto, 'subtle', { get() { return undefined; } });",
};
SCENARIOS['tout verrouillé à la fois'] = Object.values(SCENARIOS).join('\n');

describe('navigateurs Linux verrouillés (Firefox privé, LibreWolf, Tor Browser)', { skip }, () => {
  let s, browser;
  before(async () => { s = await startServer(testConfig({ liveMode: false, apiKey: '' })); browser = await chromium.launch(); });
  after(async () => { await browser?.close(); await s?.close(); });

  for (const [nom, script] of Object.entries(SCENARIOS)) {
    test(nom, async () => {
      const ctx = await browser.newContext({ userAgent: UA });
      await ctx.addInitScript(script);
      const page = await ctx.newPage();
      const erreurs = [];
      page.on('pageerror', (e) => erreurs.push(e.message));
      await page.goto(`${s.base}/#/bibliotheque`, { waitUntil: 'networkidle' });
      await page.waitForSelector('a.fiche-card', { timeout: 15000 });
      assert.ok((await page.locator('a.fiche-card').count()) > 100, 'la bibliothèque doit afficher les fiches');
      assert.deepEqual(erreurs, []);
      await ctx.close();
    });
  }
});
