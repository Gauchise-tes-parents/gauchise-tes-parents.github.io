#!/usr/bin/env node
// Rapport des tests de compréhension (v8) : exécute réellement chaque phrase avec le nouveau moteur
// et avec l'ancienne correspondance par mots (v7), puis écrit rapports/tests-comprehension.md.
import { writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLibrary } from '../server/library.js';
import { analyserPhrase } from '../public/js/analyse.js';
import { CA_CONCEPTS, CA_ARGUMENTS, CA_EMOTIONS, CA_PROCEDES } from '../public/js/cartographie.js';
import { kbMatch } from '../public/js/kbsearch.js';
import { PHRASES } from '../tests/comprehension/phrases.js';
import { evaluer } from '../tests/comprehension/evaluer.js';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const lib = loadLibrary(undefined, { warn() {} });
const thema = lib.filter((f) => f.type !== 'science');
const V8 = ['immigration-emploi', 'immigration-salaires', 'chomage-penurie-recrutement'];
const libV7 = thema.filter((f) => !V8.includes(f.id));
const liste = (v) => (Array.isArray(v) ? v : [v]);
const md = (s) => String(s ?? '').replace(/\|/g, '\\|');

const ancien = (t, base) => { const m = kbMatch(base, t)[0]; return m ? m.fiche.id : null; };
const ancienOk = (it, id) => it.f === undefined || liste(it.f).includes(id);

let ok = 0; let okV7 = 0; let okAncienActuel = 0;
const lignes = []; const corrections = [];
const parCat = {};
for (const it of PHRASES) {
  const an = analyserPhrase(it.t, { bibliotheque: lib });
  const r = evaluer(it, an);
  const v7 = ancien(it.t, libV7); const va = ancien(it.t, thema);
  if (r.ok) ok += 1;
  if (ancienOk(it, v7)) okV7 += 1;
  if (ancienOk(it, va)) okAncienActuel += 1;
  const c = (parCat[it.cat] ||= { n: 0, ok: 0 }); c.n += 1; if (r.ok) c.ok += 1;
  if (!ancienOk(it, v7) && r.ok) corrections.push({ it, v7, an });
  lignes.push(`| ${md(it.t)} | ${md(it.cat)}${it.lot ? ' (validation)' : ''} | ${md(an.arguments.map((a) => a.label).join(' ; ') || '—')} | ${md(an.concepts.map((x) => x.label).join(', ') || '—')} | ${md(an.arguments.map((a) => a.fiche ? a.fiche.id : 'lacune reconnue').join(' ; ') || 'aucune')} | ${md(an.ecartees.map((e) => e.id).join(', ') || '—')} | ${md(v7 || 'aucune')} | ${r.ok ? 'réussi' : `échec : ${md(r.erreurs.join(' ; '))}`} |`);
}
const nMotifs = Object.values(CA_CONCEPTS).reduce((n, c) => n + c.motifs.length, 0);
const val = PHRASES.filter((p) => p.lot === 'validation');
const demo = analyserPhrase('Plus il y a d’immigrés, moins il y a de travail pour les Français.', { bibliotheque: lib });
const demoAvant = kbMatch(libV7, demo.texte).slice(0, 3);

const out = `# Tests de compréhension — moteur d'analyse argumentative (v8)

Rapport produit par \`npm run rapport:comprehension\` le ${new Date().toISOString().slice(0, 10)} : chaque phrase est réellement analysée ; rien n'est recopié à la main.

## Résultats

- **${PHRASES.length} phrases** testées, dont ${val.length} du lot de validation (écrites après les réglages).
- **Nouveau moteur : ${ok}/${PHRASES.length} réussies** (argument principal, fiche, arguments secondaires, fiches à exclure, émotions et procédés attendus).
- Ancienne correspondance par mots (v7), sur la bibliothèque v7 : ${okV7}/${PHRASES.length} phrases avec la bonne fiche (ou l'absence de fiche quand aucune ne répond).
- Ancienne correspondance par mots, sur la bibliothèque actuelle (avec les fiches emploi ajoutées en v8) : ${okAncienActuel}/${PHRASES.length}.

Critère « ancien moteur » : la première fiche proposée est l'une des fiches attendues ; quand aucune fiche ne répond, il est compté juste seulement s'il ne propose rien. L'ancien moteur ne repérait ni arguments secondaires, ni émotions, ni procédés : ces critères ne lui sont pas appliqués.

| Catégorie | Phrases | Réussies |
|---|---:|---:|
${Object.entries(parCat).map(([k, v]) => `| ${k} | ${v.n} | ${v.ok} |`).join('\n')}

## Cartographie

- ${Object.keys(CA_CONCEPTS).length} concepts, ${nMotifs} mots-clés, expressions, synonymes et fautes fréquentes ;
- ${CA_ARGUMENTS.length} arguments reliés aux fiches qui y répondent (dont ${CA_ARGUMENTS.filter((a) => !a.fiches.length).length} sans fiche, signalés comme lacunes) ;
- ${Object.keys(CA_EMOTIONS).length} émotions, ${Object.keys(CA_PROCEDES).length} procédés argumentatifs.

## Démonstration : « ${demo.texte} »

**Avant (v7)** : la correspondance par mots proposait ${demoAvant.map((m) => `\`${m.fiche.id}\` (${m.force}, score ${m.score})`).join(', ')}. Les mots « immigrés » et « Français » suffisaient à faire remonter la fiche sur les aides sociales, qui ne parle pas d'emploi.

**Après (v8)** :
1. Concepts repérés : ${demo.concepts.map((c) => `${c.label} (« ${c.mots.join(' », « ')} »)`).join(' ; ')}.
2. Lien de cause affirmé : ${demo.causalites.map((c) => `${c.cause} → ${c.effet} (${c.forme})`).join(' ; ')}.
3. Argument : **${demo.principal.label}** — sous-entendu : ${demo.principal.implicite}
4. Fiche retenue : \`${demo.principal.fiche.id}\` (« ${demo.principal.fiche.affirmation} »).
5. Fiches écartées :
${demo.ecartees.map((e) => `   - \`${e.id}\` : ${e.raison}.`).join('\n')}
6. Procédé possible : ${demo.procedes.map((p) => p.label).join(', ') || 'aucun'} ; question : « ${demo.question} »
7. Phrase marquante (mode « gagner ») : « ${demo.phrase} »

## Erreurs corrigées par rapport à la v7 (${corrections.length})

| Phrase | Avant (v7) | Après (v8) |
|---|---|---|
${corrections.map(({ it, v7, an }) => `| ${md(it.t)} | ${md(v7 || 'aucune fiche')} | ${md(an.arguments.map((a) => `${a.label} → ${a.fiche ? a.fiche.id : 'lacune reconnue'}`).join(' ; '))} |`).join('\n')}

## Détail des ${PHRASES.length} phrases

| Phrase | Catégorie | Arguments repérés | Concepts | Fiches retenues | Fiches écartées | Ancienne fiche (v7) | Résultat |
|---|---|---|---|---|---|---|---|
${lignes.join('\n')}
`;
mkdirSync(join(ROOT, 'rapports'), { recursive: true });
writeFileSync(join(ROOT, 'rapports', 'tests-comprehension.md'), out);
console.log(`Nouveau moteur : ${ok}/${PHRASES.length} · ancien (v7) : ${okV7}/${PHRASES.length} · ancien sur la base actuelle : ${okAncienActuel}/${PHRASES.length} · ${corrections.length} erreurs corrigées → rapports/tests-comprehension.md`);
