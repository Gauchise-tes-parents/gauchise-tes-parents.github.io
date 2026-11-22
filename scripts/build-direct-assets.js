// Relais de la base de connaissances sur Cloudflare (v15.1, affluence).
// Exécuté par Cloudflare au déploiement du Worker « gauchise-direct » (worker-direct/wrangler.toml, [build]) :
// copie kb/base.json et kb/manifest.json dans worker-direct/public/, servis comme « static assets ».
// Le site (GitHub Pages) télécharge alors la base, son fichier le plus lourd, depuis ce relais ; il vérifie son
// empreinte SHA-256 avec le manifeste publié par GitHub Pages et, en cas d'écart ou de panne, reprend la copie
// de GitHub Pages. Aucun secret ; contenu identique à la base publique.
import { mkdirSync, writeFileSync, rmSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLibrary } from '../server/library.js';
import { buildKb } from '../server/kbexport.js';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const OUT = process.env.DIRECT_ASSETS_OUT || join(ROOT, 'worker-direct', 'public');
rmSync(OUT, { recursive: true, force: true });
mkdirSync(join(OUT, 'kb'), { recursive: true });
const { json, manifest } = buildKb(loadLibrary(undefined, console));
writeFileSync(join(OUT, 'kb', 'base.json'), json);
writeFileSync(join(OUT, 'kb', 'manifest.json'), JSON.stringify(manifest, null, 2));
// En-têtes des fichiers statiques : lecture autorisée depuis le site, cache court (une nouvelle base arrive
// à chaque publication ; le site la redemande avec ?v=<version>).
writeFileSync(join(OUT, '_headers'), ['/kb/*', '  Access-Control-Allow-Origin: *', '  Cache-Control: public, max-age=300', '  X-Content-Type-Options: nosniff', ''].join('\n'));
console.log(`Relais Cloudflare : base ${manifest.version} (${Math.round(manifest.taille / 1024)} Ko) écrite dans ${OUT}`);
