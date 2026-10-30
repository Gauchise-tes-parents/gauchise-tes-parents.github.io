// v12 — Rapport d'exécution des 20 questions de la demande (et variantes), dans les deux modes.
// Usage : node scripts/rapport-v12.js  → écrit rapports/tests-20-questions.md
import { writeFileSync, mkdirSync } from 'node:fs';
import { loadLibrary } from '../server/library.js';
import { resoudrePhrase } from '../public/js/analyse.js';
import { composer } from '../public/js/composer.js';
import { Q20 } from '../tests/v12-questions.js';

const lib = loadLibrary(undefined, { warn() {} });
const lignes = [];
let ok = 0;
for (const [q, attendu] of Q20) {
  const r = resoudrePhrase(q, lib);
  const f = r.fiche;
  const bon = f?.id === attendu;
  let modes = '—';
  if (f) {
    const a = composer(f, {}, { bibliotheque: lib });
    const prem = ['gagner', 'convaincre'].map((m) => a[m].blocs[0].type === 'replique');
    modes = prem.every(Boolean) ? 'réponse d’abord (2 modes)' : 'à revoir';
  }
  if (bon) ok += 1;
  lignes.push(`| ${q} | ${bon ? '✅' : '❌'} \`${f?.id || 'aucune'}\` | ${r.an.domaines.map((d) => d.label).join(' ; ')} | ${f ? f.sources.length : 0} | ${modes} |`);
  lignes.push(`| | ${(f?.argumentaires.court || '').replace(/\|/g, '/')} | | | |`);
}
const md = `# Tests v12 — les 20 questions de la demande

Généré par \`node scripts/rapport-v12.js\` le ${new Date().toISOString().slice(0, 10)} : **${ok}/${Q20.length}** questions reçoivent la fiche qui répond directement à leur sujet.

Pour chaque question, la deuxième ligne reproduit la réponse courte affichée en premier.

| Question | Fiche obtenue | Domaines mobilisés | Sources | Modes |
|---|---|---|---:|---|
${lignes.join('\n')}
`;
mkdirSync(new URL('../rapports/', import.meta.url), { recursive: true });
writeFileSync(new URL('../rapports/tests-20-questions.md', import.meta.url), md);
console.log(`${ok}/${Q20.length} — rapports/tests-20-questions.md écrit`);
