// Publication statique (GitHub Pages, Cloudflare Pages…) : produit dist/site/, utilisable sans serveur.
// Le mode autonome y est complet et fonctionne hors ligne après la première visite (service worker).
// Le mode connecté n'y est actif que si GTP_API_BASE pointe vers un serveur Node déployé ailleurs.
//
// Usage : node scripts/build-static.js            (variables facultatives : GTP_API_BASE, WATCH_EXTERNAL_SCHEDULE)
import { cpSync, mkdirSync, rmSync, writeFileSync, readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT } from '../server/config.js';
import { loadLibrary } from '../server/library.js';
import { buildKb, assetManifest } from '../server/kbexport.js';
import { watchConfig, readState } from '../server/watch/veille.js';

const OUT = process.env.STATIC_OUT || join(ROOT, 'dist', 'site');
// Adresses publiques par défaut (deploiement.json, versionné, sans secret) ; les variables d'environnement ont priorité
let DEPLOIEMENT = {};
try { DEPLOIEMENT = JSON.parse(readFileSync(join(ROOT, 'deploiement.json'), 'utf8')); } catch { /* fichier facultatif */ }
const apiBase = process.env.GTP_API_BASE || DEPLOIEMENT.apiBase || '';
if (apiBase && !/^https:\/\/[^\s"'<>]+$/.test(apiBase)) { console.error('GTP_API_BASE doit être une URL https.'); process.exit(1); }
// Backend IA (Gemini) : URL publique du Worker, jamais de clé
const iaBase = (process.env.GTP_IA_BASE || DEPLOIEMENT.iaBase || '').replace(/\/+$/, '');
if (iaBase && !/^https:\/\/[^\s"'<>/]+(\/[^\s"'<>]*)?$/.test(iaBase)) { console.error('GTP_IA_BASE doit être une URL https.'); process.exit(1); }

rmSync(OUT, { recursive: true, force: true });
mkdirSync(OUT, { recursive: true });
cpSync(join(ROOT, 'public'), OUT, { recursive: true });
// CSP : sur GitHub Pages, pas d'en-têtes HTTP personnalisables ; la politique est dans une balise <meta>.
// Si un serveur du mode connecté est configuré, sa seule origine est ajoutée aux connexions autorisées.
const connexions = [apiBase, iaBase].filter(Boolean).map((u) => new URL(u).origin);
if (connexions.length) {
  const idx = join(OUT, 'index.html');
  writeFileSync(idx, readFileSync(idx, 'utf8').replace("connect-src 'self'", `connect-src 'self' ${[...new Set(connexions)].join(' ')}`));
}

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
// Identifiant unique de cette publication : l'application le compare à version.json pour se mettre à jour toute seule
const build = `${new Date().toISOString().replace(/\D/g, '').slice(0, 14)}-${Math.random().toString(36).slice(2, 8)}`;
writeFileSync(join(OUT, 'config.js'), `// Généré par scripts/build-static.js\nwindow.GTP_CONFIG = { apiBase: ${apiBase ? JSON.stringify(apiBase) : 'null'}, iaBase: ${iaBase ? JSON.stringify(iaBase) : 'null'}, build: ${JSON.stringify(build)} };\n`);
writeFileSync(join(OUT, 'version.json'), JSON.stringify({ build }));
// Noms de fichiers propres à chaque publication (?v=…) : GitHub Pages fait garder les fichiers 10 minutes par les
// navigateurs, qui ne revérifient que la page au rechargement. Sans ce suffixe, un visiteur pourrait recevoir un
// mélange d'ancienne et de nouvelle version juste après une mise à jour.
const v = `?v=${build}`;
const idxPath = join(OUT, 'index.html');
writeFileSync(idxPath, readFileSync(idxPath, 'utf8')
  .replace('src="config.js"', `src="config.js${v}"`)
  .replace('src="js/app.js"', `src="js/app.js${v}"`)
  .replace('href="css/styles.css"', `href="css/styles.css${v}"`));
for (const f of readdirSync(join(OUT, 'js')).filter((n) => n.endsWith('.js'))) {
  const p = join(OUT, 'js', f);
  writeFileSync(p, readFileSync(p, 'utf8').replace(/(from\s+['"]\.\/[\w-]+\.js)(['"])/g, `$1${v}$2`));
}
writeFileSync(join(OUT, '.nojekyll'), '');
writeFileSync(join(OUT, '404.html'), readFileSync(join(OUT, 'index.html')));
writeFileSync(join(OUT, 'asset-manifest.json'), JSON.stringify(assetManifest(OUT)));
if (!existsSync(join(OUT, 'sw.js'))) throw new Error('sw.js manquant');
console.log(`Site statique écrit : ${OUT}\n  ${library.length} fiches · base ${manifest.version} (${Math.round(manifest.taille / 1024)} Ko)\n  Mode connecté : ${apiBase ? apiBase : 'non configuré (mode autonome seul)'}\n  IA (Gemini) : ${iaBase || 'non configurée'}`);
