// Indique, pour une liste de questions (une par ligne), si l'application y répond déjà et par quelle fiche.
// Usage : node scripts/verifier-couverture.mjs questions.txt   (ou : echo "question" | node scripts/verifier-couverture.mjs -)
import { readFileSync } from 'node:fs';
import { loadLibrary } from '../server/library.js';
import { resoudrePhrase } from '../public/js/analyse.js';
const lib = loadLibrary(undefined, { warn() {} });
const src = process.argv[2] && process.argv[2] !== '-' ? readFileSync(process.argv[2], 'utf8') : readFileSync(0, 'utf8');
for (const q of src.split('\n').map((x) => x.trim()).filter(Boolean)) {
  const r = resoudrePhrase(q, lib);
  console.log(`${r.fiche ? 'COUVERTE' : 'LACUNE  '}\t${r.fiche?.id || '-'}\t${r.voie || ''}\t${q}`);
}
