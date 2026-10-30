#!/usr/bin/env node
// Génère docs/MOTEUR-PERSONNALISATION.md à partir du code réel (EFFETS, REGLES, DECISIONS, fiches scientifiques).
// La documentation ne peut donc pas diverger de ce que le moteur fait. Usage : node scripts/doc-moteur.js
import { writeFileSync, mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLibrary, LIBRARY_DIR } from '../server/library.js';
import { EFFETS, composer, planifier, suite } from '../public/js/composer.js';
import { REGLES, DECISIONS, nettoyerProfil } from '../public/js/profile.js';
import { INTERLOCUTEUR, RETOURS } from '../public/js/taxonomy.js';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const lib = loadLibrary(LIBRARY_DIR, { warn() {} });
const fiches = lib.filter((f) => f.type !== 'science');
const sci = new Map(lib.filter((f) => f.type === 'science').map((f) => [f.id, f]));
const byId = (id) => lib.find((f) => f.id === id);
const fp = (a) => JSON.stringify({ g: a.gagner.blocs, c: a.convaincre.blocs });
const CONF = { elevee: 'élevée', moyenne: 'moyenne', faible: 'faible' };

const TESTS = {
  debat: { competitif: 'une seule preuve, ton ferme', provocateur: 'recentrage, réponse courte', susceptible: 'questions avant contre-argument (deux modes)', evite: 'questions avant contre-argument', hesitant: 'conclusion « plusieurs pistes »' },
  faits: { chiffres: 'preuve chiffrée en tête ou absence signalée', experience: 'entrée par le vécu' },
  autorite: { mefiance: 'méthode affichée pour chaque preuve', independantes: 'méthode affichée' },
  valeurs: { securite: 'angle sécurité', ordre: 'angle sécurité', justice_sociale: 'angle justice', souverainete: 'angle nation', tradition: 'angle nation' },
  cadre: { reseaux: 'conclusion adressée au public', plusieurs: 'conclusion adressée au public', repas: 'proposition de pause' },
  lien: { parent: 'conclusion sur le lien', conjoint: 'conclusion sur le lien', public: 'conclusion adressée au public' },
  connaissance: { faible: 'ton pédagogique ou nuancé', elevee: 'détail et méthode' },
  objectif: { corriger: 'entrée par la correction', riposter: 'phrase pour le public' },
  politique: { partisan: 'reconnaître d’abord un point fondé' },
};

function effetMesure(dim, k, multi) {
  const base = dim === 'debat' ? { faits: 'chiffres' } : { debat: 'calme' };
  const p = { ...base, [dim]: multi ? [k] : k };
  return fiches.filter((f) => fp(composer(f, p, { bibliotheque: lib })) !== fp(composer(f, base, { bibliotheque: lib }))).length;
}

const oui = (v) => (v === true ? 'oui' : v === false ? 'non' : v);
function diffPlan(fiche, base, avec, mode) {
  const a = planifier(fiche, { profil: base, mode, bibliotheque: lib });
  const b = planifier(fiche, { profil: avec, mode, bibliotheque: lib });
  const champs = { approche: 'approche', entree: 'point d’entrée', ton: 'ton', detail: 'niveau de détail', conclusion: 'conclusion', apaisement: 'proposition de pause', public: 'phrase pour le public', lien: 'phrase sur le lien' };
  const rows = [];
  for (const [k, lab] of Object.entries(champs)) if (JSON.stringify(a[k]) !== JSON.stringify(b[k])) rows.push(`| ${lab} | ${oui(a[k])} | ${oui(b[k])} |`);
  const pa = a.preuves.map((x) => `${x.index}${x.methode ? ' (avec méthode)' : ''}`).join(', ');
  const pb = b.preuves.map((x) => `${x.index}${x.methode ? ' (avec méthode)' : ''}`).join(', ');
  if (pa !== pb) rows.push(`| preuves (index des faits) | ${pa} | ${pb} |`);
  if (a.ordre.join() !== b.ordre.join()) rows.push(`| ordre des blocs | ${a.ordre.join(' → ')} | ${b.ordre.join(' → ')} |`);
  if (a.questions.join() !== b.questions.join()) rows.push(`| questions | ${a.questions.join(' / ') || '—'} | ${b.questions.join(' / ') || '—'} |`);
  if ((a.objection?.index ?? '-') !== (b.objection?.index ?? '-')) rows.push(`| objection anticipée | ${a.objection?.objection || '—'} | ${b.objection?.objection || '—'} |`);
  if (String(a.concordantes) !== String(b.concordantes)) rows.push(`| sources concordantes | ${a.concordantes || '—'} | ${b.concordantes?.join(', ') || '—'} |`);
  if (a.prochaine.map((x) => x.retour).join() !== b.prochaine.map((x) => x.retour).join()) rows.push(`| prochaine étape prévue | ${a.prochaine.map((x) => x.retour).join(', ')} | ${b.prochaine.map((x) => x.retour).join(', ')} |`);
  return `| Élément du plan | Sans l’information | Avec l’information |\n|---|---|---|\n${rows.join('\n')}`;
}

const L = [];
L.push('# Moteur de personnalisation — fonctionnement et table de décision');
L.push('');
L.push('_Document généré par `node scripts/doc-moteur.js` à partir du code (`public/js/composer.js`, `public/js/profile.js`) et des fiches scientifiques. Les effets « mesurés » sont recalculés à chaque génération sur les ' + fiches.length + ' fiches thématiques._');
L.push('');
L.push('## 1. Principe');
L.push('');
L.push('Le mode autonome n’utilise **aucun modèle d’IA** : c’est un moteur de règles déterministe (même contexte → même réponse). Il procède en trois temps :');
L.push('');
L.push('1. **Nettoyage du profil** (`nettoyerProfil`) : seules les options prévues sont gardées ; « je ne connais pas cette personne » annule toutes les autres hypothèses ; trois valeurs au plus.');
L.push('2. **Plan explicite** (`planifier`) : à partir de la fiche, du mode, du profil, des arguments déjà avancés, des objections et questions déjà traitées et des fiches récemment utilisées, le moteur choisit : l’approche (factuelle, historique ou institutionnelle, valeurs et conséquences), le point d’entrée, les preuves et leur ordre, le niveau de détail, la source mise en avant, l’objection à anticiper, les questions, le ton, la conclusion, l’ordre des blocs et la prochaine étape. Chaque choix est justifié (« Pourquoi cette stratégie » dans l’interface).');
L.push('3. **Rendu** (`blocs`) : les blocs sont assemblés dans l’ordre du plan. Les seuls textes ajoutés par le moteur sont des formules de liaison sans contenu factuel ; les faits, chiffres, sources et réponses courtes sont repris **tels quels** depuis la fiche.');
L.push('');
L.push('**Résolution des conflits entre options.** Les poids d’approche s’additionnent ; pour le point d’entrée, le ton et la conclusion, chaque mode a une liste de priorité (par exemple en « gagner un débat » : correction > fait > cadre > concession… ; en « convaincre » : reformulation > question > vécu…). Le nombre maximal de preuves est le plus petit demandé ; « méfiance » peut ajouter une source concordante d’un autre organisme (jusqu’à trois preuves). Le mode infléchit l’approche (+0,75 vers factuelle en « gagner », vers valeurs en « convaincre ») sans écraser le profil.');
L.push('');
L.push('**Ce qui ne change jamais selon le profil** : le texte des faits, les chiffres, les sources et leurs dates, la réponse courte, les limites de la fiche, les avertissements d’ancienneté et de débat.');
L.push('');
L.push('## 2. Table de décision');
L.push('');
L.push('Pour chaque option : l’information qu’elle apporte, les éléments du plan qu’elle influence, la consigne affichée (avec son fondement), les cas où elle ne doit rien changer, l’effet mesuré (nombre de fiches dont la réponse change quand on ajoute cette seule option) et le test automatisé qui la vérifie.');
L.push('');
L.push('### Mode');
L.push('');
for (const [k, v] of Object.entries(DECISIONS.mode)) L.push(`- **${k === 'gagner' ? 'Gagner un débat' : 'Convaincre'}** — ${v.info} Influence : ${v.influence.join(', ')}. Sans effet sur : ${v.neutre} Test : « le mode change le contenu, pas les faits ».`);
L.push(`- **Volet (thème)** — ${DECISIONS.volet.info} Influence : ${DECISIONS.volet.influence.join(', ')}. ${DECISIONS.volet.neutre}`);
L.push('');
for (const d of INTERLOCUTEUR) {
  L.push(`### ${d.label}${d.essentiel ? ' (question essentielle)' : ' (facultative)'}`);
  L.push('');
  L.push('| Option | Information apportée | Éléments influencés | Consigne affichée (fondement) | Ne change pas | Effet mesuré | Test |');
  L.push('|---|---|---|---|---|---|---|');
  for (const [k, lab] of d.options) {
    const e = EFFETS[d.id]?.[k] || {};
    const dec = DECISIONS[d.id]?.[k];
    const p = nettoyerProfil({ [d.id]: d.multi ? [k] : k });
    const regles = REGLES.filter((r) => r.id !== 'ethique' && r.quand(p));
    const consignes = regles.map((r) => `${r.consigne} (${r.fondement === 'recherche' ? 'recherche' : 'bonne pratique'} ; ${r.fiche})`).join(' ') || '—';
    const n = effetMesure(d.id, k, d.multi);
    L.push(`| ${lab} | ${dec?.info || lab} | ${(e.influence || []).join(', ') || '—'} | ${consignes} | ${e.neutre || dec?.neutre || 'Aucun fait, chiffre ni source n’est modifié.'} | ${e.neutre ? 'neutre par conception' : `${n} / ${fiches.length} fiches`} | ${TESTS[d.id]?.[k] ? `attente « ${TESTS[d.id][k]} »` : 'effet non nul (test de couverture)'} |`);
  }
  L.push('');
}
L.push('Le test « chaque option du questionnaire modifie le plan sur au moins une fiche, ou est documentée comme neutre » (`tests/unit/personnalisation.test.js`) échoue si une option devient décorative.');
L.push('');
L.push('## 3. Exemples imposés');
L.push('');
L.push('### « La personne se méfie des médias et des institutions »');
L.push('');
const fi = byId('impots-assistanat');
L.push(`Fiche « ${fi.affirmation} », mode « gagner un débat », profil de départ neutre-calme. Effet de l’ajout de « se méfie des institutions » :`);
L.push('');
L.push(diffPlan(fi, { debat: 'calme' }, { debat: 'calme', autorite: 'mefiance' }, 'gagner'));
L.push('');
L.push('Le moteur **ne remplace pas** les données publiques par d’autres : il affiche période, périmètre et organisme pour chaque preuve, ajoute une source d’un autre organisme quand la fiche en contient une, pose la question « Quelle source te paraîtrait fiable ? » et prépare la réponse au retour « elle dit que les chiffres sont truqués ».');
L.push('');
L.push('### « Repas de famille »');
L.push('');
const fd = byId('delinquance-partout');
L.push(`Fiche « ${fd.affirmation} », mode « convaincre », profil de départ neutre-calme. Effet de l’ajout de « repas de famille » :`);
L.push('');
L.push(diffPlan(fd, { debat: 'calme' }, { debat: 'calme', cadre: 'repas' }, 'convaincre'));
L.push('');
L.push('Même ajout en mode « gagner un débat » :');
L.push('');
L.push(diffPlan(fd, { debat: 'calme' }, { debat: 'calme', cadre: 'repas' }, 'gagner'));
L.push('');
L.push('Et avec, en plus, « c’est un parent » (mode « convaincre ») :');
L.push('');
L.push(diffPlan(fd, { debat: 'calme', cadre: 'repas' }, { debat: 'calme', cadre: 'repas', lien: 'parent' }, 'convaincre'));
L.push('');
L.push('## 4. Échanges successifs');
L.push('');
L.push('Après chaque réponse, l’utilisateur peut indiquer ce qui s’est passé (boutons ou texte libre interprété localement par mots-clés). Le moteur garde en mémoire, pour la durée de la discussion seulement, les faits déjà présentés, les objections déjà traitées et les questions déjà posées : rien n’est répété. Les hypothèses du profil peuvent être corrigées à tout moment.');
L.push('');
L.push('| Retour | Réponse proposée (exemple sur « ' + fi.affirmation + ' », retours enchaînés dans cet ordre) | Conseil | Fondement |');
L.push('|---|---|---|---|');
const session = { utilises: [], objectionsVues: [], questionsPosees: [], retours: [] };
for (const [k, lab] of RETOURS) {
  const x = suite(fi, { inconnu: true }, k, session, { bibliotheque: lib });
  session.retours.push(k);
  if (x.utilise != null) session.utilises.push(x.utilise);
  if (x.objection != null) session.objectionsVues.push(x.objection);
  if (x.question) session.questionsPosees.push(x.question);
  L.push(`| ${lab} | **${x.titre}** — ${String(x.texte).replace(/\n/g, ' ').replace(/\|/g, '/')} | ${x.conseil} | ${x.fiche_science} |`);
}
L.push('');
L.push('Chaque proposition rappelle qu’elle repose uniquement sur ce que l’utilisateur a observé et qu’elle est approximative.');
L.push('');
L.push('## 5. Référentiel scientifique');
L.push('');
L.push('Chaque consigne renvoie à une fiche scientifique de la bibliothèque (rubrique « Science du dialogue »). Aucune de ces notions n’est une loi universelle : les effets mesurés sont généralement modestes et dépendent du contexte. Les consignes marquées « bonne pratique » ne reposent pas directement sur une étude ; elles sont présentées comme telles.');
L.push('');
for (const f of sci.values()) {
  const r = f.reference || {};
  const util = REGLES.filter((x) => x.fiche === f.id).map((x) => x.titre);
  L.push(`### ${f.affirmation}`);
  L.push('');
  L.push(`- **Référence principale** : ${r.titre} — [lien](${r.url})`);
  L.push(`- **Auteurs, année** : ${r.auteurs}, ${r.annee}`);
  L.push(`- **Résumé** : ${f.resume}`);
  L.push(`- **Conditions d’application** : ${f.conditions}`);
  L.push(`- **Limites** : ${f.limites_methodo}`);
  L.push(`- **Niveau de confiance** : ${CONF[f.confiance] || f.confiance}`);
  if (f.sources.length > 1) L.push(`- **Autres sources de la fiche** : ${f.sources.filter((s) => s.url !== r.url).map((s) => `[${s.organisme || s.titre}](${s.url})`).join(', ')}`);
  L.push(`- **Consignes qui s’y réfèrent** : ${util.join(' ; ') || '—'}`);
  L.push('');
}
L.push('## 6. Données personnelles');
L.push('');
L.push('- Les réponses au questionnaire servent au calcul puis restent dans la page ; **aucun profil n’est enregistré automatiquement**. L’enregistrement d’un profil (sous un surnom libre, sans nom réel requis) est une action explicite, limitée à 12 profils, sur cet appareil uniquement (localStorage).');
L.push('- La discussion en cours (faits déjà utilisés, retours) et la liste des fiches récemment consultées sont gardées en sessionStorage et disparaissent à la fermeture de l’onglet.');
L.push('- La page « Mes données » liste tout ce qui est stocké et permet de supprimer chaque élément ou tout effacer.');
L.push('- En mode autonome, rien n’est envoyé sur le réseau. En mode connecté, le profil nettoyé (options prédéfinies seulement, jamais de texte libre identifiant) est transmis au serveur pour la requête en cours et n’est pas conservé.');
L.push('');
L.push('## 7. Limites');
L.push('');
L.push('- Le moteur adapte la **présentation** de faits vérifiés ; il ne peut pas être plus riche que la fiche (une fiche de trois faits limite la variété possible).');
L.push('- L’interprétation du texte libre des retours repose sur des mots-clés : elle peut se tromper, et l’utilisateur peut toujours choisir le bon bouton.');
L.push('- Les profils sont des hypothèses de l’utilisateur sur une personne, jamais un diagnostic ; les règles décrivent des tendances moyennes observées dans la recherche, qui peuvent ne pas s’appliquer à une personne donnée.');
L.push('- Aucune efficacité persuasive n’a été mesurée sur de vraies personnes.');

mkdirSync(join(ROOT, 'docs'), { recursive: true });
writeFileSync(join(ROOT, 'docs/MOTEUR-PERSONNALISATION.md'), `${L.join('\n')}\n`);
console.log('docs/MOTEUR-PERSONNALISATION.md écrit');
