#!/usr/bin/env node
// Enrichit les métadonnées des fiches (data/library/*.json) à partir de la cartographie des arguments :
//   concepts      — concepts couverts (calculés sur l'affirmation, les mots-clés et le sous-thème) ;
//   repond_a      — arguments cartographiés auxquels la fiche répond (id + libellé) ;
//   ne_repond_pas — arguments voisins auxquels elle NE répond PAS (fiche explicitement écartée) ;
//   synonymes     — formulations courantes associées à ses concepts (aide à la reconnaissance).
// Ne touche à aucun fait, chiffre, source ou argumentaire. À relancer après les générateurs Python.
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { CA_CONCEPTS, CA_ARGUMENTS } from '../public/js/cartographie.js';
import { anConcepts } from '../public/js/analyse.js';
import { kbNormalize } from '../public/js/kbsearch.js';

const DIR = join(dirname(fileURLToPath(import.meta.url)), '..', 'data', 'library');
const norm = (t) => ` ${kbNormalize(t).replace(/[^a-z0-9%!? ]+/g, ' ').replace(/\s+/g, ' ').trim()} `;
const lisible = (m) => /^[a-z ]+$/.test(m) ? m : null; // motifs sans syntaxe d'expression régulière

let n = 0;
const bilan = { concepts: 0, repond: 0, exclusions: 0 };
for (const fichier of readdirSync(DIR).filter((f) => f.endsWith('.json'))) {
  const p = join(DIR, fichier);
  const f = JSON.parse(readFileSync(p, 'utf8'));
  delete f.concepts; // recalcul propre
  const concepts = anConcepts(norm(`${f.affirmation} ${(f.mots_cles || []).join(' ')} ${f.sous_theme || ''}`)).map((c) => c.id);
  const repond = CA_ARGUMENTS.filter((a) => a.fiches.includes(f.id));
  // un argument auquel la fiche répond ajoute ses concepts (ex. « travail des Français » → emploi)
  for (const a of repond) for (const c of a.tous) if (!concepts.includes(c)) concepts.push(c);
  const exclu = CA_ARGUMENTS.filter((a) => (a.exclues || []).includes(f.id));
  f.concepts = concepts;
  f.repond_a = repond.map((a) => ({ id: a.id, label: a.label, ...(a.partielle ? { partielle: true } : {}) }));
  f.ne_repond_pas = exclu.map((a) => ({ id: a.id, label: a.label }));
  f.synonymes = [...new Set(concepts.flatMap((c) => CA_CONCEPTS[c].motifs.map(lisible).filter(Boolean)))].slice(0, 12);
  writeFileSync(p, `${JSON.stringify(f, null, 2)}\n`);
  n += 1; bilan.concepts += concepts.length; bilan.repond += repond.length; bilan.exclusions += exclu.length;
}
console.log(`${n} fiches enrichies — ${bilan.concepts} rattachements à des concepts, ${bilan.repond} liens « répond à », ${bilan.exclusions} exclusions explicites.`);
