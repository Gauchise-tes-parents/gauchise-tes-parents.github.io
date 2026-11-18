// Génère les icônes PNG de l'application (site installable, App Store, Google Play) à partir de public/img/icon.svg.
// Usage : node scripts/mobile/generer-icones.mjs   (nécessite Playwright / Chromium ; à relancer si le logo change)
// - icon-192.png, icon-512.png : icônes « any » (coins arrondis, fond transparent)
// - icon-maskable-512.png : fond plein, logo dans la zone sûre (80 %) pour les icônes adaptatives Android
// - apple-touch-icon.png (180) : fond plein, sans transparence (iOS arrondit lui-même)
// - store/icon-1024.png : icône de l'App Store (carrée, sans transparence ni coins arrondis)
// - store/icon-play-512.png : icône haute définition de Google Play
import { readFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
let chromium;
try { ({ chromium } = await import('playwright')); } catch {
  for (const p of [process.env.PLAYWRIGHT_PATH, '/opt/npm-tools/node_modules/playwright/index.mjs'].filter(Boolean)) { try { ({ chromium } = await import(p)); break; } catch { /* suivant */ } }
}
if (!chromium) { console.error('Playwright est nécessaire : npm i -D playwright && npx playwright install chromium'); process.exit(2); }

const svg = readFileSync(join(ROOT, 'public', 'img', 'icon.svg'), 'utf8');
const FOND = '#2B1A5C';
// variante pleine : fond carré sur toute la surface ; échelle < 1 = logo resserré au centre (zone sûre)
function plein(echelle) {
  const corps = svg.replace(/<rect[^>]*\/>/, '').replace(/^<svg[^>]*>/, '').replace(/<\/svg>\s*$/, '');
  const d = (192 * (1 - echelle)) / 2;
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192"><rect width="192" height="192" fill="${FOND}"/><g transform="translate(${d} ${d}) scale(${echelle})">${corps}</g></svg>`;
}
const SORTIES = [
  ['public/img/icon-192.png', 192, svg, true],
  ['public/img/icon-512.png', 512, svg, true],
  ['public/img/icon-maskable-512.png', 512, plein(0.8), false],
  ['public/img/apple-touch-icon.png', 180, plein(0.92), false],
  ['mobile/store/icon-1024.png', 1024, plein(0.92), false],
  ['mobile/store/icon-play-512.png', 512, plein(0.92), false],
];
const browser = await chromium.launch();
const page = await browser.newPage();
for (const [chemin, taille, contenu, transparent] of SORTIES) {
  await page.setViewportSize({ width: taille, height: taille });
  await page.setContent(`<html><body style="margin:0;background:transparent">${contenu.replace('<svg ', `<svg width="${taille}" height="${taille}" `)}</body></html>`);
  mkdirSync(dirname(join(ROOT, chemin)), { recursive: true });
  await page.screenshot({ path: join(ROOT, chemin), omitBackground: transparent, clip: { x: 0, y: 0, width: taille, height: taille } });
  console.log(`${chemin} (${taille}×${taille})`);
}
await browser.close();
