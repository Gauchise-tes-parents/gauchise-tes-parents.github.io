// Prépare le dossier web des applications mobiles (Capacitor : App Store et Google Play) — v15 en préparation.
// Usage : node scripts/mobile/build-mobile.js [--plateforme ios|android] [--avec-soutien]
//   → dist/mobile/www : le même site autonome que GitHub Pages, base de fiches embarquée (fonctionne sans réseau),
//     sans service worker (les fichiers sont déjà dans l'appli) et, par défaut, sans lien de don Tipeee
//     (les règles des boutiques sur les dons externes sont à vérifier avant de l'activer : voir docs/MOBILE.md).
// Ensuite (une fois Capacitor installé, voir docs/MOBILE.md) : npx cap sync
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
const args = process.argv.slice(2);
const i = args.indexOf('--plateforme');
const plateforme = i >= 0 ? args[i + 1] : 'mobile';
if (!['ios', 'android', 'mobile'].includes(plateforme)) { console.error('Plateforme : ios, android ou mobile.'); process.exit(1); }
const soutien = args.includes('--avec-soutien');
const OUT = join(ROOT, 'dist', 'mobile', 'www');

// Pas de backend IA ni de serveur connecté dans l'appli : uniquement le mode autonome (aucune donnée personnelle transmise).
execFileSync(process.execPath, [join(ROOT, 'scripts', 'build-static.js')], { stdio: 'inherit', env: { ...process.env, STATIC_OUT: OUT, GTP_API_BASE: '', GTP_IA_BASE: '', GTP_QUESTIONS_BASE: process.env.GTP_QUESTIONS_BASE_MOBILE || 'aucun', GTP_KB_RELAIS: 'aucun' } });
// Base : celle embarquée dans l'appli (aucun téléchargement). Direct : seule la vérification « en live ou pas » est
// faite (détecteur du projet, sans donnée personnelle) ; le live s'ouvre dans l'appli Twitch ou YouTube, sans lecteur
// intégré (pas de contenu ni de traceur tiers dans l'appli, déclarations des boutiques plus simples).
const cfgPath = join(OUT, 'config.js');
const cfg = readFileSync(cfgPath, 'utf8').replace(/build: ("[^"]*")/, `build: $1, app: true, plateforme: ${JSON.stringify(plateforme)}, soutien: ${soutien}`);
writeFileSync(cfgPath, cfg + '// Version application mobile (scripts/mobile/build-mobile.js)\n');
// Le 404.html (astuce GitHub Pages) n'a pas de sens dans l'appli
try { execFileSync('rm', ['-f', join(OUT, '404.html'), join(OUT, '.nojekyll')]); } catch { /* facultatif */ }
console.log(`Dossier web mobile prêt : ${OUT}\n  plateforme : ${plateforme} · lien Tipeee : ${soutien ? 'affiché' : 'masqué'}\n  étape suivante : npx cap sync (voir docs/MOBILE.md)`);
