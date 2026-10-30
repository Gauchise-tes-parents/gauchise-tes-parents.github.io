#!/usr/bin/env node
// Audit de cohérence : chaque affirmation suggérée (764, tous volets et sous-thèmes) est traitée comme le fait
// l'application (analyse argumentative, puis correspondance forte), et on vérifie que la fiche obtenue traite
// bien du même domaine. Usage : node scripts/audit-coherence.js [--json fichier] [--detail]
import { writeFileSync } from 'node:fs';
import { loadLibrary } from '../server/library.js';
import { conceptsFiche, resoudrePhrase } from '../public/js/analyse.js';
import { SG_BIBLIOTHEQUE } from '../public/js/suggestions.js';

export const resoudre = (texte, lib) => resoudrePhrase(texte, lib);

export function auditCoherence(lib) {
  const lignes = [];
  for (const [volet, sts] of Object.entries(SG_BIBLIOTHEQUE)) {
    for (const [st, liste] of Object.entries(sts)) {
      for (const brut of liste) {
        const texte = brut.split('|').slice(1).join('|');
        const { an, fiche, voie } = resoudre(texte, lib);
        let statut = 'lacune';
        if (fiche) {
          const cp = new Set(an.concepts.filter((c) => c.central).map((c) => c.id));
          const cf = conceptsFiche(fiche);
          const commun = [...cp].filter((c) => cf.includes(c));
          statut = (fiche.volet === volet || commun.length || fiche.sous_theme === st || (fiche.type === 'histoire' && /histoire/i.test(st))) ? 'coherent' : 'suspect';
        }
        lignes.push({ volet, sous_theme: st, texte, statut, voie, fiche: fiche?.id || null, fiche_volet: fiche?.volet || null, concepts: an.concepts.map((c) => c.id) });
      }
    }
  }
  return lignes;
}

if (process.argv[1]?.endsWith('audit-coherence.js')) {
  const lib = loadLibrary(undefined, { warn() {} });
  const l = auditCoherence(lib);
  const n = (s) => l.filter((x) => x.statut === s).length;
  console.log(`${l.length} affirmations — cohérentes : ${n('coherent')} · suspectes : ${n('suspect')} · sans fiche : ${n('lacune')}`);
  const parVolet = {};
  for (const x of l) { const v = (parVolet[x.volet] ||= { total: 0, coherent: 0, suspect: 0, lacune: 0 }); v.total++; v[x.statut]++; }
  console.table(parVolet);
  if (process.argv.includes('--detail')) for (const x of l.filter((y) => y.statut === 'suspect')) console.log(`SUSPECT [${x.volet} / ${x.sous_theme}] ${x.texte} → ${x.fiche} (${x.fiche_volet})`);
  const j = process.argv.indexOf('--json'); if (j > 0) writeFileSync(process.argv[j + 1], JSON.stringify(l, null, 1));
}
