#!/usr/bin/env node
// Exécute réellement les scénarios synthétiques et écrit rapports/tests-personnalisation.md (+ .json).
// Usage : node scripts/rapport-personnalisation.js
import { writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLibrary, LIBRARY_DIR } from '../server/library.js';
import { toutExecuter, exempleComparatif, PROFILS_TEST } from '../tests/personnalisation/scenarios.js';
import { resumeProfil } from '../public/js/profile.js';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const lib = loadLibrary(LIBRARY_DIR, { warn() {} });
const debut = Date.now();
const run = toutExecuter(lib);
const duree = Date.now() - debut;
const R = run.resultats;
const d = run.diversite;
const byId = new Map(lib.map((f) => [f.id, f]));

// ─── Stabilité factuelle et sources ───
let preuvesVues = 0;
let preuvesExactes = 0;
let sourcesManquantes = 0;
const repliques = new Map();
for (const s of run.scenarios.filter((x) => x.type === 'profil')) {
  const r = R.find((x) => x.id === s.id);
  if (!r.plan) continue;
}
import('../public/js/composer.js').then(({ composer }) => {
  for (const s of run.scenarios.filter((x) => x.type === 'profil' || x.type === 'facultatif')) {
    const a = composer(s.fiche, s.profil, { bibliotheque: lib });
    for (const m of ['gagner', 'convaincre']) for (const p of a.plans[m].preuves) {
      preuvesVues += 1;
      if (p.texte === s.fiche.faits[p.index].fait) preuvesExactes += 1;
      if (!p.source?.consultee || !p.source?.url) sourcesManquantes += 1;
    }
    const k = s.fiche.id;
    if (!repliques.has(k)) repliques.set(k, new Set());
    repliques.get(k).add(a.gagner.replique);
  }

  // ─── Fiches qui limitent la différenciation (peu de faits) ───
  const parFiche = new Map();
  for (const r of R.filter((x) => x.type === 'profil')) {
    const f = r.id.split('/')[0];
    if (!parFiche.has(f)) parFiche.set(f, new Set());
    parFiche.get(f).add(r.plan.gagner.preuves);
    parFiche.get(f).add(r.plan.convaincre.preuves);
  }
  const limitees = [...parFiche].filter(([, set]) => set.size <= 2).map(([f, set]) => `${f} (${byId.get(f).faits.length} faits, ${set.size} sélection(s) de preuves distinctes)`);

  // ─── Superficielles : détail ───
  const erreursFact = R.filter((r) => r.erreurs.some((e) => /nombre|fait|réponse courte/.test(e)));
  const erreursSrc = R.filter((r) => r.erreurs.some((e) => /source/.test(e)));
  const inadapt = R.filter((r) => r.violations.length);
  const nonCouvert = R.filter((r) => r.type === 'question' && r.resultat === 'non couvert');

  // ─── Exemples comparatifs ───
  const ex = (id, profils) => exempleComparatif(byId.get(id), profils, lib);
  const blocTxt = (b) => {
    if (b.type === 'preuves') return `${b.titre} : ${b.items.map((p) => `« ${p.texte} » (${p.source?.organisme})`).join(' ; ')}`;
    if (b.type === 'questions') return `${b.titre} : ${b.items.join(' / ')}`;
    if (b.type === 'liste') return `${b.titre} : ${b.items.join(' / ')}`;
    if (b.type === 'objection') return `${b.titre} : ${b.objection} → ${b.reponse}`;
    return `${b.titre} : ${b.texte}`;
  };
  const exemple = (titre, id, profils) => {
    const rows = ex(id, profils);
    let md = `### ${titre}\n\nAffirmation : « ${byId.get(id).affirmation} » (fiche \`${id}\`)\n\n`;
    md += '| Profil (hypothèse) | Approche | Entrée | Détail | Ton | Preuves (index) | Ordre (débat public) | Conclusion |\n|---|---|---|---|---|---|---|---|\n';
    for (const r of rows) md += `| ${r.nom} — ${resumeProfil(r.profil)} | ${r.gagner.approche} | ${r.gagner.entree} | ${r.gagner.detail} | ${r.gagner.ton} | ${r.gagner.preuves.map((p) => p.index).join(', ')} | ${r.gagner.ordre.join(' → ')} | ${r.gagner.conclusion} |\n`;
    for (const r of rows) {
      md += `\n**${r.nom} — mode « convaincre » (texte réellement produit)**\n\n`;
      for (const b of r.blocsC) md += `- ${blocTxt(b)}\n`;
    }
    return md;
  };

  const L = [];
  L.push('# Rapport de tests du moteur de personnalisation (mode autonome)');
  L.push('');
  L.push(`Généré le ${new Date().toISOString().slice(0, 10)} par \`node scripts/rapport-personnalisation.js\` — exécution réelle de ${run.scenarios.length} scénarios en ${duree} ms, sans réseau ni clé API.`);
  L.push('');
  L.push('> **Ce que ces tests prouvent et ne prouvent pas.** Ils vérifient que le moteur transmet les choix, applique la table de décision, ne modifie aucun fait, cite des sources consultées, signale les incertitudes, ne présente pas un profil comme un fait et ne bloque jamais. Ils **ne mesurent pas** l’efficacité persuasive sur de vraies personnes : aucune validation empirique n’a été faite.');
  L.push('');
  L.push('## Synthèse');
  L.push('');
  L.push('| Indicateur | Résultat |\n|---|---|');
  L.push(`| Scénarios exécutés | ${run.scenarios.length} (profils ${R.filter((r) => r.type === 'profil').length}, échanges successifs ${R.filter((r) => r.type === 'echange').length}, questions libres ${R.filter((r) => r.type === 'question').length}, données facultatives ou invalides ${R.filter((r) => r.type === 'facultatif').length}) |`);
  L.push(`| Scénarios conformes aux 8 critères | ${R.filter((r) => r.ok).length} / ${R.length} |`);
  L.push(`| Erreurs factuelles | ${erreursFact.length} |`);
  L.push(`| Sources manquantes ou non consultées | ${erreursSrc.length} scénario(s), ${sourcesManquantes} preuve(s) |`);
  L.push(`| Réponses insuffisamment adaptées (attente du profil non respectée) | ${inadapt.length} |`);
  L.push(`| Stabilité factuelle (preuves identiques au texte de la fiche) | ${preuvesExactes} / ${preuvesVues} |`);
  L.push(`| Réponse courte identique pour tous les profils d’une même fiche | ${[...repliques.values()].every((s) => s.size === 1) ? 'oui, pour les ' + repliques.size + ' fiches' : 'NON'} |`);
  L.push(`| Paires de profils comparées (même fiche, même mode) | ${d.paires} |`);
  L.push(`| … différences pertinentes (≥ 2 dimensions de fond) | ${d.pertinentes} (${Math.round((100 * d.pertinentes) / d.paires)} %) |`);
  L.push(`| … différences superficielles (une seule dimension, ou ton/contexte seulement) | ${d.superficielles} (${Math.round((100 * d.superficielles) / d.paires)} %) |`);
  L.push(`| … plans identiques | ${d.identiques.length} |`);
  L.push('');
  L.push('Les pourcentages ci-dessus décrivent les sorties du logiciel, pas un effet sur des personnes.');
  L.push('');
  L.push('## Les huit critères vérifiés pour chaque scénario');
  L.push('');
  L.push('1. **Choix transmis** : le profil nettoyé arrive au moteur (options invalides ignorées, « je ne connais pas » prioritaire).');
  L.push('2. **Stratégie conforme** : attentes explicites par option (ex. confrontation → une preuve et ton ferme ; se braque → questions avant contre-argument dans les deux modes ; public → conclusion adressée au public ; repas → proposition de pause). Une attente n’est pas exigée quand une option concurrente plus prioritaire l’emporte (règle documentée).');
  L.push('3. **Sources cohérentes** : chaque preuve renvoie à la source de son fait, marquée comme consultée, avec la même URL.');
  L.push('4. **Pas de duplication** : dans les échanges successifs, aucun fait déjà présenté n’est repris après « elle écoute », aucune réponse n’est répétée à l’identique.');
  L.push('5. **Faits non altérés** : le texte des preuves est identique à la fiche ; aucun nombre absent de la fiche n’apparaît dans les blocs ; la réponse courte n’est jamais réécrite.');
  L.push('6. **Incertitudes signalées** : ancienneté des données (fiches non historiques), caractère débattu ou interprétatif, correspondance seulement partielle.');
  L.push('7. **Profil non confondu avec un fait** : aucun texte du type « elle est susceptible » ; les hypothèses sont présentées comme telles.');
  L.push('8. **Parcours non bloqué** : aucune exception, deux stratégies non vides, profils vides/invalides acceptés, question hors base → page « pas dans la base » sans contenu inventé.');
  L.push('');
  L.push('Un « test des tests » (`tests/unit/personnalisation.test.js`) injecte volontairement un fait modifié, un nombre ajouté, une source non consultée, un profil présenté comme un fait et une attente non respectée : chacun est bien détecté.');
  L.push('');
  L.push('## Diversité, dimension par dimension');
  L.push('');
  L.push('Nombre de paires (sur ' + d.paires + ') dont le plan diffère sur chaque dimension :');
  L.push('');
  L.push('| Dimension | Paires différentes |\n|---|---|');
  const noms = { structure: 'Structure (ordre des blocs)', preuves: 'Choix des preuves', ordre: 'Ordre des preuves', questions: 'Questions posées', detail: 'Niveau de détail (et méthode affichée)', strategie: 'Stratégie (approche / entrée / conclusion)', objection: 'Objection anticipée', contexte: 'Adaptation au contexte (ton, public, lien, pause, angles)' };
  for (const [k, v] of Object.entries(d.compte)) L.push(`| ${noms[k]} | ${v} (${Math.round((100 * v) / d.paires)} %) |`);
  L.push('');
  L.push('L’objection anticipée varie peu : la plupart des fiches n’en contiennent qu’une ou deux. C’est une limite des données, pas un défaut à masquer par de la variété artificielle.');
  L.push('');
  L.push('## Cas où le profil ne permet pas de justifier plus de différence');
  L.push('');
  if (limitees.length) {
    L.push('Fiches où les profils ne produisent que peu de sélections de preuves différentes, faute de faits disponibles (le moteur ne fabrique pas de faits pour varier) :');
    L.push('');
    for (const x of limitees) L.push(`- ${x}`);
  } else L.push('Aucune fiche testée ne limite la sélection des preuves à moins de trois combinaisons.');
  L.push('');
  L.push(d.superficielles ? `Différences superficielles : ${d.superficielles} paires ne diffèrent que sur une dimension (liste exhaustive ci-dessous). À examiner au cas par cas : certaines sont justifiées, d’autres signalent une adaptation qui pourrait être plus marquée.` : 'Différences superficielles : aucune paire ne diffère sur une seule dimension. Lors d’une première exécution, 19 paires étaient dans ce cas (« confrontation » et « hésitant » en mode débat ; « neutre » et « méfiant » en mode empathique). Deux corrections ont suivi : la méthode affichée est désormais comptée comme une différence de fond, et le profil « hésitant » commence par demander ce qui le fait hésiter. **Attention :** les 12 profils de test ont été choisis pour être contrastés, et la mesure ne compte que des dimensions structurelles ; elle ne juge pas la qualité du texte.');
  L.push('');
  L.push('**Profils qui ne justifient pas de différence** (paires témoins : le moteur doit produire une réponse strictement identique, sur 8 fiches et dans les deux modes) :');
  L.push('');
  L.push('| Paire | Raison | Résultat |\n|---|---|---|');
  for (const t of run.temoins) L.push(`| \`${JSON.stringify(t.a)}\` / \`${JSON.stringify(t.b)}\` | ${t.raison} | ${t.ok ? 'identique' : `différent : ${t.ecarts.join(', ')}`} |`);
  L.push('');
  for (const x of d.listeSuperficielles) L.push(`- ${x}`);
  L.push('');
  L.push('Questions hors base (bibliothèque insuffisante) : ' + (nonCouvert.length ? nonCouvert.map((r) => `« ${r.id.replace('question:', '')} »`).join(', ') + ' → l’application affiche « pas dans la base » et propose le mode connecté ou un signalement, sans réponse inventée.' : 'aucune.'));
  L.push('');
  L.push('## Exemples comparatifs');
  L.push('');
  L.push(exemple('Une affirmation, trois profils', 'impots-assistanat', [['chiffres', PROFILS_TEST.chiffres], ['méfiance envers les institutions', PROFILS_TEST.mefiant], ['se braque', PROFILS_TEST.braque]]));
  L.push('');
  L.push(exemple('Repas de famille contre débat public', 'delinquance-partout', [['repas de famille avec un parent', PROFILS_TEST.parent_repas], ['provocation sur les réseaux', PROFILS_TEST.provocateur_public], ['sensible à la sécurité', PROFILS_TEST.securitaire]]));
  L.push('');
  L.push('## Résultats de tous les scénarios');
  L.push('');
  L.push('| # | Scénario | Type | Résultat (gagner · convaincre, ou parcours) | Critères |\n|---|---|---|---|---|');
  R.forEach((r, i) => L.push(`| ${i + 1} | \`${r.id}\` | ${r.type} | ${String(r.resultat || '').replace(/\|/g, '/')} | ${r.ok ? '8/8' : [...r.violations, ...r.erreurs, ...r.incertitudes].join(' ; ')} |`));
  L.push('');
  L.push('## Ce qui reste à tester');
  L.push('');
  L.push('- **Mode connecté** (recherche web et rédaction par un service d’IA) : testé uniquement avec un service simulé dans les tests de bout en bout ; aucun test avec une vraie clé API n’a été exécuté dans cet environnement.');
  L.push('- **Effet réel sur des personnes** : non mesuré. Les règles s’appuient sur des travaux publiés (voir docs/MOTEUR-PERSONNALISATION.md) dont les effets sont modestes et dépendants du contexte.');

  mkdirSync(join(ROOT, 'rapports'), { recursive: true });
  writeFileSync(join(ROOT, 'rapports/tests-personnalisation.md'), `${L.join('\n')}\n`);
  writeFileSync(join(ROOT, 'rapports/tests-personnalisation.json'), JSON.stringify({ date: new Date().toISOString(), scenarios: R.length, conformes: R.filter((r) => r.ok).length, diversite: { ...d, identiques: d.identiques.length, listeSuperficielles: undefined }, stabilite: { preuvesVues, preuvesExactes }, sourcesManquantes, resultats: R.map(({ id, type, ok, resultat, violations, erreurs, incertitudes }) => ({ id, type, ok, resultat, violations, erreurs, incertitudes })) }, null, 1));
  console.log(`${R.filter((r) => r.ok).length}/${R.length} scénarios conformes · diversité ${d.pertinentes}/${d.paires} · stabilité ${preuvesExactes}/${preuvesVues}`);
  if (R.some((r) => !r.ok)) process.exitCode = 1;
});
