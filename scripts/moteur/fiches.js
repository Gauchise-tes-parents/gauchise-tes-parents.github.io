// Assemblage des fiches du moteur interne (SANS IA) : pour une question restée sans réponse, la fiche réunit
// les mesures de « L'Avenir en commun » qui traitent du sujet (citées mot pour mot, avec le lien du chapitre) et
// les chiffres officiels pertinents (Eurostat). Elle ne prétend pas vérifier l'affirmation : elle le dit.
// Garde-fous : validation de l'application, politique documentaire, aucune phrase de contrôle détournée, la
// question doit mener à la nouvelle fiche ; sinon la fiche reste un brouillon (data/brouillons/).
import { validateEntry } from '../../server/library.js';
import { auditFiche } from '../../public/js/ligne-editoriale.js';
import { resoudrePhrase, anConcepts, anDomaines } from '../../public/js/analyse.js';
import { kbNormalize, kbTokens } from '../../public/js/kbsearch.js';
import { VOLETS } from '../../public/js/taxonomy.js';
import { mesuresAPlat } from './aec.js';
import { INDICATEURS, factuel } from './chiffres.js';

export const VERSION_MOTEUR = '1.0';
const VALEURS_VOLET = { ecologie: ['vulnerables', 'internationalisme', 'services_publics'], economie: ['repartition', 'egalite', 'travailleurs'], social: ['solidarite', 'dignite', 'services_publics'], services: ['services_publics', 'egalite', 'universalite'], politique: ['democratie', 'libertes', 'egalite'], international: ['paix', 'internationalisme', 'democratie'], droits: ['egalite', 'libertes', 'dignite'], immigration: ['antiracisme', 'dignite', 'universalite'], securite: ['libertes', 'democratie', 'dignite'] };

// Radical grossier (français) : rapproche « retraités / retraite », « chômeurs / chômage » sans dictionnaire
export function radical(t) {
  const r = t.replace(/(issements?|ements?|ations?|ateurs?|atrices?|ites?|eurs?|euses?|ives?|ifs?|iques?|istes?|ismes?|aux|ales?|ees?|es|s|e)$/, '');
  return r.length >= 4 ? r : t;
}
const sac = (s) => new Set(kbTokens(s).map(radical));

/** Mots porteurs de la question : ses mots, plus les libellés des concepts reconnus par la cartographie. */
export function motsQuestion(question) {
  const concepts = anConcepts(kbNormalize(question).replace(/[^a-z0-9]+/g, ' '));
  const extra = concepts.filter((c) => c.central).map((c) => c.label).join(' ');
  return { mots: sac(`${question} ${extra}`), concepts, domaines: anDomaines(concepts.map((c) => c.id)) };
}

/** Mesures du programme les plus proches de la question (au moins un mot porteur dans la mesure elle-même). */
export function mesuresPertinentes(question, corpus, { max = 6 } = {}) {
  const { mots } = motsQuestion(question);
  const scores = mesuresAPlat(corpus).map((m) => {
    const dans = [...sac(m.texte)].filter((x) => mots.has(x)).length;
    const titre = [...sac(m.section)].filter((x) => mots.has(x)).length;
    const chap = [...sac(m.chapitre)].filter((x) => mots.has(x)).length;
    return { m, dans, score: dans * 2 + titre + chap * 0.5 + (m.cle ? 0.3 : 0) };
  }).filter((x) => x.dans >= 1 && x.score >= 2.5).sort((a, b) => b.score - a.score);
  const vus = new Set();
  return scores.filter(({ m }) => (vus.has(m.texte) ? false : vus.add(m.texte))).slice(0, max).map((x) => ({ ...x.m, score: x.score }));
}

/** Indicateurs chiffrés pertinents : d'abord par mots, puis par domaine. */
export function chiffresPertinents(question, chiffres, volet, { max = 2 } = {}) {
  const n = kbNormalize(question);
  const { domaines } = motsQuestion(question);
  const dispo = INDICATEURS.filter((i) => chiffres?.indicateurs?.[i.id]?.valeur != null);
  const parMots = dispo.filter((i) => i.mots.some((m) => n.includes(m)));
  const parDomaine = dispo.filter((i) => !parMots.includes(i) && (i.domaines.includes(volet) || i.domaines.some((d) => domaines.includes(d))));
  return [...parMots, ...parDomaine].slice(0, max).map((i) => chiffres.indicateurs[i.id]);
}

const slug = (s) => kbNormalize(s).replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').split('-').slice(0, 8).join('-').slice(0, 50).replace(/-$/, '');
const guillemets = (t) => `« ${t.replace(/^[«"\s]+|[»"\s.]+$/g, '')} »`;

function choisirVolet(mesures, domaines) {
  const compte = {};
  for (const m of mesures) compte[m.volet] = (compte[m.volet] || 0) + (m.score || 1);
  for (const d of domaines) compte[d] = (compte[d] || 0) + 1.5;
  return Object.entries(compte).sort((a, b) => b[1] - a[1])[0]?.[0] || 'politique';
}
function choisirSousTheme(volet, question) {
  const v = VOLETS.find((x) => x.id === volet);
  const mots = sac(question);
  return (v?.sousThemes || []).find((st) => [...sac(st)].some((x) => mots.has(x))) || null;
}

/** Construit la fiche (objet au format de la bibliothèque) ou renvoie { raison } si c'est impossible. */
export function assemblerFiche(question, { corpus, chiffres, occurrences = 1, jour = new Date().toISOString().slice(0, 10) }) {
  const mesures = mesuresPertinentes(question, corpus);
  if (mesures.length < 2) return { raison: 'le programme ne semble pas traiter ce sujet (moins de deux mesures proches)' };
  const { domaines } = motsQuestion(question);
  const volet = choisirVolet(mesures, domaines);
  const indicateurs = chiffresPertinents(question, chiffres, volet);
  if (!indicateurs.length) return { raison: 'aucun chiffre officiel pertinent disponible (une fiche doit citer au moins une source d’autorité)' };

  const parChapitre = new Map();
  for (const m of mesures) { if (!parChapitre.has(m.url)) parChapitre.set(m.url, []); parChapitre.get(m.url).push(m); }
  const sources = [];
  const cleSource = new Map();
  for (const [url, ms] of parChapitre) {
    cleSource.set(url, sources.length);
    sources.push({
      titre: `L’Avenir en commun — ${ms[0].chapitre}`,
      organisme: 'La France insoumise — programme L’Avenir en commun, édition 2027 (source partisane)',
      date_publication: `texte relevé le ${corpus.releve_le}`,
      url,
      passage: ms.map((m) => `${m.section} : ${guillemets(m.texte)}`).join(' ; '),
      pertinence: 'Programme politique de la France insoumise : il dit ce que la gauche propose, il ne prouve pas un fait.',
      type: 'primaire',
      consultee: true,
    });
  }
  const faitsChiffres = indicateurs.map((ind) => { const f = factuel(ind); sources.push(f.source); return { f, idx: sources.length - 1, ind }; });

  const faits = [
    ...mesures.slice(0, 5).map((m) => ({ fait: `Le programme L’Avenir en commun propose : ${guillemets(m.texte)} (section « ${m.section} »).`, periode: `programme relevé le ${corpus.releve_le}`, perimetre: 'France', explication: 'Proposition politique de la France insoumise, citée mot pour mot.', source: cleSource.get(m.url), fiabilite: 'etabli' })),
    ...faitsChiffres.map(({ f, idx, ind }) => ({ fait: f.phrase, periode: ind.periode, perimetre: 'France', explication: 'Repère chiffré officiel, mis à jour automatiquement.', source: idx, fiabilite: 'etabli', chiffre: `${String(ind.valeur).replace('.', ',')} ${ind.unite}` })),
  ].slice(0, 8);

  const m1 = mesures[0].texte.replace(/[.\s]+$/, '');
  const m2 = mesures[1].texte.replace(/[.\s]+$/, '');
  const c1 = faitsChiffres[0].f.phrase;
  const liste = mesures.slice(0, 5).map((m) => `– ${m.texte.replace(/[.\s]+$/, '')}`).join('\n');
  const id = `moteur-${slug(question)}`;
  const fiche = {
    id, type: 'reference', origine: 'moteur', affirmation: question.replace(/\s+/g, ' ').trim(), volet, sous_theme: choisirSousTheme(volet, question),
    rubriques: [], mots_cles: [...new Set([kbNormalize(question).replace(/[^a-z0-9]+/g, ' ').trim(), ...kbTokens(question).slice(0, 6)])].filter(Boolean).slice(0, 8),
    verdict: null, fiabilite: 'interpretation', stabilite: 'evolutive',
    resume: `Repères en attendant une fiche de vérification complète : sur ce sujet, le programme L’Avenir en commun propose notamment ${guillemets(m1)}. ${c1}`,
    contexte: `Question posée ${occurrences > 1 ? `${occurrences} fois ` : ''}dans l’application et restée sans fiche. Cette fiche a été assemblée automatiquement par le moteur interne (sans IA) à partir du programme et de chiffres officiels.`,
    explication: 'Cette fiche ne tranche pas sur l’exactitude de l’affirmation. Elle donne deux repères fiables : ce que propose concrètement la gauche (L’Avenir en commun, cité mot pour mot) et les derniers chiffres officiels utiles. Une fiche de vérification complète, avec des sources contradictoires, reste à écrire.',
    faits, sources,
    argumentaires: {
      court: `Sur ce sujet, la gauche a une proposition précise : ${guillemets(m1)} (L’Avenir en commun). Et pour fixer les idées : ${c1.charAt(0).toLowerCase()}${c1.slice(1)}`,
      moyen: `Plutôt que de répondre par un slogan, on peut regarder ce que la gauche propose. Le programme L’Avenir en commun prévoit notamment ${guillemets(m1)} et ${guillemets(m2)}.\n\nLes chiffres officiels donnent le cadre du débat : ${faitsChiffres.map((x) => x.f.phrase).join(' ')}`,
      detaille: `Ce que propose L’Avenir en commun sur ce sujet :\n${liste}\n\nRepères chiffrés : ${faitsChiffres.map((x) => x.f.phrase).join(' ')}\n\nCes mesures sont des choix politiques, à discuter comme tels : on peut demander, pour chacune, qui en profiterait, qui la paierait et ce qu’elle changerait concrètement.`,
      empathie: 'C’est une question que beaucoup de gens se posent, et elle mérite mieux qu’une réponse toute faite. On peut partir de ce qui t’inquiète, puis regarder ensemble les chiffres et les propositions concrètes.',
    },
    contre_arguments: [
      ['C’est un programme, pas une preuve.', 'C’est vrai : la fiche le dit. Elle sert à montrer qu’une autre politique est proposée, mesure par mesure, et les chiffres officiels donnent le contexte. Chaque mesure peut se discuter.'],
      ['Tout ça coûtera trop cher.', `Demande quelle mesure précise poserait problème, et pourquoi. Par exemple : ${guillemets(m1)}. Le débat devient alors concret.`],
    ].map(([objection, reponse]) => ({ objection, reponse })),
    questions: ['Qu’est-ce qui te fait penser ça ?', `Si l’on appliquait la mesure ${guillemets(m1)}, qu’est-ce qui changerait pour toi ?`],
    limites: [
      'Fiche assemblée automatiquement par le moteur interne, sans IA : les mesures et les chiffres sont recopiés de leurs sources, mais l’ensemble n’a pas été relu mot à mot.',
      'Elle présente un programme politique (source partisane) et des repères chiffrés : ce n’est pas une vérification de l’affirmation.',
      `Mesures relevées le ${corpus.releve_le} sur le site du programme ; le texte a pu évoluer depuis.`,
    ],
    publics: {
      convaincus: `Je ne vais pas te dire que tu as tort sans l’avoir vérifié. Mais sur ce sujet, la gauche propose quelque chose de précis : ${guillemets(m1)}. Qu’est-ce qui te gêne dans cette proposition ?`,
      indecis: `Ta question est légitime. Pour te faire ton avis, regarde les chiffres officiels (${c1.charAt(0).toLowerCase()}${c1.slice(1).replace(/\.$/, '')}) et compare les propositions des programmes : L’Avenir en commun prévoit par exemple ${guillemets(m1)}.`,
    },
    lecture: {
      valeurs: VALEURS_VOLET[volet] || ['democratie', 'egalite'],
      mecanismes: 'Quand une question reste sans réponse, la rumeur ou le slogan prennent la place. Revenir aux propositions concrètes et aux chiffres officiels permet de remettre le débat sur le terrain des choix politiques.',
      consequences: 'Sans repères fiables, les inquiétudes réelles sont captées par ceux qui désignent des boucs émissaires plutôt que des solutions.',
      democratie: 'Comparer des programmes mesure par mesure, à partir de leur texte, est la base d’un débat démocratique honnête.',
      propositions: mesures.slice(0, 3).map((m) => m.texte.replace(/[.\s]+$/, '') + '.').filter((t) => !/\d/.test(t)),
      defavorables: [{ fait: 'Un programme politique ne prouve pas qu’une affirmation est fausse.', integration: 'Le dire franchement, et compléter la fiche par une vérification sourcée dès que possible.' }],
    },
    derniere_verification: jour,
    a_actualiser_le: new Date(Date.parse(jour) + 120 * 864e5).toISOString().slice(0, 10),
    raison_actualisation: 'Fiche automatique : à remplacer par une fiche de vérification complète, et chiffres mis à jour.',
    moteur: { version: VERSION_MOTEUR, genere_le: jour, occurrences, mesures: mesures.length, indicateurs: indicateurs.map((i) => i.id) },
  };
  if (!fiche.lecture.propositions.length) fiche.lecture.propositions = ['Comparer les programmes mesure par mesure, à partir de leur texte.'];
  return { fiche };
}

/** Garde-fous avant d'ajouter une fiche à la bibliothèque. Renvoie la liste des problèmes (vide = acceptée). */
export function controler(fiche, { bibliotheque, phrasesControle, avant }) {
  const pb = [...validateEntry(fiche), ...auditFiche(fiche)];
  if (bibliotheque.some((f) => f.id === fiche.id)) pb.push('identifiant déjà pris');
  if (pb.length) return pb;
  const apres = [...bibliotheque, fiche];
  const atteinte = resoudrePhrase(fiche.affirmation, apres).fiche?.id === fiche.id;
  if (!atteinte) pb.push('la question ne mène pas à la fiche (rattachement à faire dans public/js/cartographie.js)');
  const detournees = phrasesControle.filter((p) => (resoudrePhrase(p, apres).fiche?.id || null) !== avant.get(p)).slice(0, 3);
  if (detournees.length) pb.push(`détournerait des phrases de contrôle : ${detournees.map((p) => `« ${p} »`).join(', ')}`);
  return pb;
}
