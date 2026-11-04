// Phase bêta : intègre à la bibliothèque publiée les fiches créées par l'IA (branche « fiches-ia », dossier
// data/propositions/). Chaque fiche est revalidée avec le validateur de la bibliothèque ; une fiche invalide, un
// identifiant déjà pris ou une fiche qui ne vient pas de l'IA sont écartés. Lancé par le flux de publication,
// APRÈS les tests (les fiches vérifiées restent la référence des tests).
// Usage : node scripts/integrer-fiches-ia.js <dossier contenant data/propositions>
import { readdirSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { validateEntry, LIBRARY_DIR } from '../server/library.js';

const base = process.argv[2] || '.';
const dir = join(base, 'data', 'propositions');
if (!existsSync(dir)) { console.log('Aucune fiche IA à intégrer.'); process.exit(0); }
const CIBLE = process.env.GTP_LIBRARY_DIR || LIBRARY_DIR;
const existants = new Set(readdirSync(CIBLE).filter((f) => f.endsWith('.json')).map((f) => f.replace(/\.json$/, '')));
let ok = 0; let ko = 0;
for (const f of readdirSync(dir).filter((n) => /^ia-[a-z0-9-]+\.json$/.test(n))) {
  try {
    const fiche = JSON.parse(readFileSync(join(dir, f), 'utf8'));
    const pb = validateEntry(fiche);
    if (fiche.origine !== 'ia' || fiche.relecture == null || !fiche.id.startsWith('ia-')) pb.push('pas une fiche IA');
    if (existants.has(fiche.id)) pb.push('identifiant déjà présent');
    if (pb.length) { ko += 1; console.log(`écartée ${f} : ${pb[0]}`); continue; }
    writeFileSync(join(CIBLE, `${fiche.id}.json`), `${JSON.stringify(fiche, null, 2)}\n`);
    existants.add(fiche.id); ok += 1;
  } catch (e) { ko += 1; console.log(`illisible ${f}`); }
}
console.log(`Fiches IA intégrées : ${ok} ; écartées : ${ko}.`);
