// Intègre la bibliothèque vérifiée au backend IA (worker/src/kb.json) : même contenu que la base du site.
// Usage : node scripts/build-worker-kb.js   (lancé automatiquement par npm run worker:deploy)
import { writeFileSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT } from '../server/config.js';
import { loadLibrary } from '../server/library.js';
import { buildKb } from '../server/kbexport.js';

const { json, manifest } = buildKb(loadLibrary(undefined, console));
writeFileSync(join(ROOT, 'worker', 'src', 'kb.json'), json);
console.log(`worker/src/kb.json : ${manifest.nb_fiches} fiches (${Math.round(manifest.taille / 1024)} Ko), version ${manifest.version}`);
