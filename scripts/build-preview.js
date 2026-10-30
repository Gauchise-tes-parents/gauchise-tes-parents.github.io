// Construit un aperçu en UN SEUL fichier HTML (base de connaissances intégrée) : le mode autonome y est
// complet (bibliothèque, compositeur, questionnaire) ; le mode connecté n'y est pas disponible.
// Pour une publication web réelle avec hors-ligne, utiliser plutôt : npm run build:static
//
// Usage : node scripts/build-preview.js [sortie.html]
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { ROOT } from '../server/config.js';
import { loadLibrary } from '../server/library.js';
import { buildKb } from '../server/kbexport.js';

const args = process.argv.slice(2);
const fragment = args.includes('--fragment'); // sortie sans <html>/<head>/<body> (pour un hébergement qui fournit déjà le squelette)
const out = args.find((a) => !a.startsWith('--')) || join(ROOT, 'dist', fragment ? 'apercu-fragment.html' : 'apercu-statique.html');
const pub = (p) => readFileSync(join(ROOT, 'public', p), 'utf8');

// Modules dans l'ordre des dépendances ; imports retirés, exports transformés en déclarations.
const ORDER = ['js/logo-data.js', 'js/taxonomy.js', 'js/kbsearch.js', 'js/kbstore.js', 'js/store.js', 'js/profile.js', 'js/composer.js', 'js/conversation.js', 'js/suggestions.js', 'js/copy.js', 'js/art.js', 'js/api.js', 'js/app.js'];
const bundle = ORDER.map((f) => `// ---- ${f}\n${pub(f)
  .replace(/^import[\s\S]*?from\s+['"][^'"]+['"];\s*$/gm, '')
  .replace(/^export\s+(?=(const|function|class|async)\b)/gm, '')}`).join('\n');

// Polices intégrées en data URI
let css = pub('css/styles.css');
css = css.replace(/url\('\.\.\/fonts\/([^']+)'\)/g, (_, f) => `url(data:font/woff;base64,${readFileSync(join(ROOT, 'public', 'fonts', f)).toString('base64')})`);

const kbLib = loadLibrary(undefined, console);
const { manifest } = buildKb(kbLib);
const library = JSON.parse(buildKb(kbLib).json).fiches;
const icon = `data:image/svg+xml;base64,${Buffer.from(pub('img/icon.svg')).toString('base64')}`;

let html = pub('index.html')
  .replace(/<link rel="manifest"[^>]*>\n?/, '')
  .replace(/<link rel="preload"[^>]*>\n?/, '')
  .replace(/<link rel="icon"[^>]*>/, `<link rel="icon" type="image/svg+xml" href="${icon}">`)
  .replace(/<link rel="stylesheet"[^>]*>/, () => `<style>\n${css}\n</style>`)
  .replace(/<script src="config.js"><\/script>\n?\s*/, '')
  .replace(/<script type="module" src="js\/app.js"><\/script>/, () => `<script>window.GTP_CONFIG = { apiBase: null }; window.__GTP_STATIC__ = ${JSON.stringify({ library, version: manifest.version, date: manifest.genere_le }).replace(/</g, '\\u003c')};</script>\n<script type="module">\n${bundle}\n</script>`);

if (fragment) {
  const head = html.match(/<head>([\s\S]*?)<\/head>/)[1]
    .replace(/<meta charset[^>]*>\s*/, '').replace(/<meta name="viewport"[^>]*>\s*/, '');
  const body = html.match(/<body>([\s\S]*?)<\/body>/)[1];
  html = `${head.trim()}\n${body.trim()}\n`;
}
mkdirSync(dirname(out), { recursive: true });
writeFileSync(out, html);
console.log(`Aperçu statique écrit : ${out} (${Math.round(html.length / 1024)} Ko, ${library.length} fiches)`);
