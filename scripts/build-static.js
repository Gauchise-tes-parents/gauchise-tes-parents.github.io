// Publication statique (GitHub Pages, Cloudflare Pages…) : produit dist/site/, utilisable sans serveur.
// Le mode autonome y est complet et fonctionne hors ligne après la première visite (service worker).
// Le mode connecté n'y est actif que si GTP_API_BASE pointe vers un serveur Node déployé ailleurs.
//
// Usage : node scripts/build-static.js            (variables facultatives : GTP_API_BASE, WATCH_EXTERNAL_SCHEDULE)
import { cpSync, mkdirSync, rmSync, writeFileSync, readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT } from '../server/config.js';
import { loadLibrary } from '../server/library.js';
import { buildKb, assetManifest } from '../server/kbexport.js';
import { watchConfig, readState } from '../server/watch/veille.js';

const OUT = process.env.STATIC_OUT || join(ROOT, 'dist', 'site');
const apiBase = process.env.GTP_API_BASE || '';
if (apiBase && !/^https:\/\/[^\s"'<>]+$/.test(apiBase)) { console.error('GTP_API_BASE doit être une URL https.'); process.exit(1); }

rmSync(OUT, { recursive: true, force: true });
mkdirSync(OUT, { recursive: true });
cpSync(join(ROOT, 'public'), OUT, { recursive: true });

const library = loadLibrary(undefined, console);
const wc = watchConfig(process.env, ROOT);
const st = readState(wc);
const { json, manifest } = buildKb(library, { veille: st });
mkdirSync(join(OUT, 'kb'), { recursive: true });
writeFileSync(join(OUT, 'kb', 'base.json'), json);
writeFileSync(join(OUT, 'kb', 'manifest.json'), JSON.stringify(manifest, null, 2));
const externe = process.env.WATCH_EXTERNAL_SCHEDULE || '';
writeFileSync(join(OUT, 'kb', 'veille.json'), JSON.stringify(st.derniere_tentative || externe ? {
  statut: externe ? 'actif' : 'inactif',
  planificateur: externe || null,
  intervalle_heures: externe ? wc.intervalHours : null,
  derniere_reussite: st.derniere_reussite,
  derniere_tentative: st.derniere_tentative,
  prochaine: null,
  dernier_rapport: st.dernier_rapport,
} : { statut: 'indisponible' }, null, 2));
writeFileSync(join(OUT, 'config.js'), `// Généré par scripts/build-static.js\nwindow.GTP_CONFIG = { apiBase: ${apiBase ? JSON.stringify(apiBase) : 'null'} };\n`);
writeFileSync(join(OUT, '.nojekyll'), '');
writeFileSync(join(OUT, '404.html'), readFileSync(join(OUT, 'index.html')));
writeFileSync(join(OUT, 'asset-manifest.json'), JSON.stringify(assetManifest(OUT)));
if (!existsSync(join(OUT, 'sw.js'))) throw new Error('sw.js manquant');
console.log(`Site statique écrit : ${OUT}\n  ${library.length} fiches · base ${manifest.version} (${Math.round(manifest.taille / 1024)} Ko)\n  Mode connecté : ${apiBase ? apiBase : 'non configuré (mode autonome seul)'}`);
