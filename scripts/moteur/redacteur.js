// Rédacteur du moteur interne (SANS IA, sans Claude, gratuit) : pour une question « à écrire à la main », il rédige
// une fiche au format de la bibliothèque à partir des pistes du chercheur de sources (sources.js) :
//   - résumés de travaux de recherche (HAL) et descriptions de données publiques (data.gouv.fr) ou d'articles de
//     vérification, CITÉS mot pour mot et attribués (« Selon le résumé de… ») ;
//   - mesures du programme L'Avenir en commun, citées mot pour mot ;
//   - repères chiffrés officiels (Eurostat), s'ils concernent le sujet ;
//   - et, comme les autres fiches : résumé, contexte, explication, argumentaires (court, moyen, détaillé, empathie),
//     objections, questions, limites, réponses aux deux publics, lecture de gauche.
// Il ne tranche JAMAIS (pas de verdict) : un programme sans IA ne peut pas juger une affirmation. Il le dit dans la
// fiche. Seuls les résumés ont été lus, pas les travaux complets : la fiche le dit aussi. Les fiches passent par les
// mêmes garde-fous que les autres (fiches.js : controler) puis par les tests, et sont PROPOSÉES en pull request.
import { kbNormalize, kbTokens } from '../../public/js/kbsearch.js';
import { classerSource, LE_CLASSES } from '../../public/js/ligne-editoriale.js';
import { motsQuestion, chiffresPertinents, VERSION_MOTEUR } from './fiches.js';
import { factuel } from './chiffres.js';
import { VOLETS } from '../../public/js/taxonomy.js';

const VALEURS_VOLET = { ecologie: ['vulnerables', 'internationalisme', 'services_publics'], economie: ['repartition', 'egalite', 'travailleurs'], social: ['solidarite', 'dignite', 'services_publics'], services: ['services_publics', 'egalite', 'universalite'], politique: ['democratie', 'libertes', 'egalite'], international: ['paix', 'internationalisme', 'democratie'], droits: ['egalite', 'libertes', 'dignite'], immigration: ['antiracisme', 'dignite', 'universalite'], securite: ['libertes', 'democratie', 'dignite'] };
// Mots-repères pour choisir le volet quand la cartographie ne reconnaît pas la question
const INDICES_VOLET = {
  immigration: ['immigr', 'migrant', 'etranger', 'asile', 'refugie', 'frontiere', 'nationalite'],
  securite: ['delinqu', 'crime', 'criminal', 'police', 'prison', 'justice', 'violence', 'securite', 'drogue'],
  social: ['chomeu', 'chomage', 'retraite', 'allocation', 'pauvre', 'precari', 'logement', 'famille', 'minima'],
  economie: ['impot', 'fiscal', 'salaire', 'entreprise', 'dette', 'inflation', 'prix', 'budget', 'emploi', 'travail', 'marche'],
  ecologie: ['eolien', 'climat', 'ecolog', 'energie', 'nucleaire', 'pesticide', 'agricult', 'carbone', 'pollution', 'paysage'],
  services: ['hopital', 'sante', 'ecole', 'medecin', 'universite', 'service public', 'transport'],
  droits: ['femme', 'laicite', 'religion', 'racisme', 'discrimination', 'liberte', 'handicap'],
  international: ['europe', 'russie', 'ukraine', 'chine', 'etats unis', 'israel', 'palestin', 'afrique', 'otan'],
  politique: ['election', 'depute', 'parti', 'gouvernement', 'constitution', 'media', 'journaliste'],
};
const guillemets = (t) => `« ${String(t).replace(/^[«"\s]+|[»"\s.]+$/g, '')} »`; // garde « … » : un extrait coupé le reste
const slug = (s) => kbNormalize(s).replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').split('-').slice(0, 8).join('-').slice(0, 50).replace(/-$/, '');
const sansChiffre = (t) => !/\d/.test(t);

function choisirVolet(question, domaines) {
  if (domaines?.length) return domaines[0];
  const n = ` ${kbNormalize(question)} `;
  let meilleur = ['politique', 0];
  for (const [v, indices] of Object.entries(INDICES_VOLET)) {
    const s = indices.filter((i) => n.includes(i)).length;
    if (s > meilleur[1]) meilleur = [v, s];
  }
  return meilleur[0];
}
function choisirSousTheme(volet, question) {
  const v = VOLETS.find((x) => x.id === volet);
  const toks = new Set(kbTokens(question).map((t) => t.slice(0, 5)));
  return (v?.sousThemes || []).find((st) => kbTokens(st).some((x) => toks.has(x.slice(0, 5)))) || null;
}

/** Pistes utilisables comme faits : un résumé lu, assez long, et une source qui n'est ni de droite ni encyclopédique. */
export function pistesCitables(pistes = []) {
  return pistes.filter((p) => p.extrait && p.extrait.length >= 80 && p.url && !['droite', 'partisane', 'tertiaire'].includes(classerSource(p)));
}

/**
 * Rédige une fiche à partir des pistes d'une question, ou renvoie { raison } si la matière est insuffisante.
 * Exige au moins deux éléments sourcés dont au moins un résumé de recherche, de données ou de vérification.
 */
export function redigerFiche(question, { pistes = [], programme = [], chiffres = null, occurrences = 1, jour = new Date().toISOString().slice(0, 10) } = {}) {
  const citables = pistesCitables(pistes).slice(0, 3);
  const mesures = programme.slice(0, 3);
  if (!citables.length) return { raison: 'aucune piste avec un résumé lisible (le rédacteur ne cite que ce qu’il a lu)' };
  if (citables.length + mesures.length < 2) return { raison: 'matière insuffisante : une seule piste lue' };
  const { domaines } = motsQuestion(question);
  const volet = choisirVolet(question, domaines);
  const indicateurs = chiffres ? chiffresPertinents(question, chiffres, volet, { max: 1 }).filter((i) => {
    // un chiffre n'est gardé que s'il parle du sujet (mot de l'indicateur présent dans la question)
    const n = kbNormalize(question); return (i.mots || []).some((m) => n.includes(m));
  }) : [];

  const sources = [];
  const faits = [];
  for (const p of citables) {
    const idx = sources.length;
    const ref = [p.auteurs, p.date].filter(Boolean).join(', ');
    sources.push({
      titre: p.titre, organisme: p.organisme, date_publication: p.date || 'non datée', url: p.url,
      passage: `Résumé : ${guillemets(p.extrait)}`,
      pertinence: 'Piste trouvée par le chercheur de sources du moteur interne : seul le résumé a été lu (automatiquement), pas le document complet.',
      type: p.origine === 'flux' ? 'secondaire' : 'primaire', consultee: true,
    });
    const nature = p.origine === 'data.gouv.fr' ? 'la description du jeu de données publiques' : p.origine === 'flux' ? 'le résumé de l’article de vérification' : 'le résumé du travail de recherche';
    faits.push({ fait: `Selon ${nature} ${guillemets(p.titre)}${ref ? ` (${ref})` : ''} : ${guillemets(p.extrait)}.`, periode: p.date || 'non précisée', perimetre: 'voir la source', explication: 'Citation du résumé, sans interprétation : à lire en entier avant de s’en servir dans un débat.', source: idx, fiabilite: 'interpretation' });
  }
  const parChapitre = new Map();
  for (const m of mesures) { if (!parChapitre.has(m.url)) parChapitre.set(m.url, []); parChapitre.get(m.url).push(m); }
  for (const [url, ms] of parChapitre) {
    const idx = sources.length;
    sources.push({ titre: `L’Avenir en commun — ${ms[0].chapitre}`, organisme: 'La France insoumise — programme L’Avenir en commun, édition 2027 (source partisane)', date_publication: 'texte relevé par le moteur interne', url, passage: ms.map((m) => guillemets(m.texte)).join(' ; '), pertinence: 'Programme politique de la France insoumise : il dit ce que la gauche propose, il ne prouve pas un fait.', type: 'primaire', consultee: true });
    for (const m of ms) faits.push({ fait: `Le programme L’Avenir en commun propose : ${guillemets(m.texte)}.`, periode: 'programme en vigueur', perimetre: 'France', explication: 'Proposition politique, citée mot pour mot.', source: idx, fiabilite: 'etabli' });
  }
  for (const ind of indicateurs) {
    const f = factuel(ind); const idx = sources.length; sources.push(f.source);
    faits.push({ fait: f.phrase, periode: ind.periode, perimetre: 'France', explication: 'Repère chiffré officiel, mis à jour automatiquement.', source: idx, fiabilite: 'etabli', chiffre: `${String(ind.valeur).replace('.', ',')} ${ind.unite}` });
  }
  faits.push({ fait: 'Limite : cette fiche a été rédigée automatiquement, sans IA ; elle cite des résumés et des propositions mais ne vérifie pas l’affirmation, et aucun document n’a été lu en entier.', periode: jour, perimetre: 'fiche', explication: 'Fait défavorable à notre propre méthode : à dire franchement.', source: 0, fiabilite: 'interpretation' });

  const p1 = citables[0];
  const titres = citables.map((p) => `${guillemets(p.titre)} (${p.organisme.replace(/\s*\(.*$/, '')}${p.date ? `, ${p.date}` : ''})`);
  const m1 = mesures[0]?.texte.replace(/[.\s]+$/, '');
  const pistesNonLues = pistes.filter((p) => !citables.includes(p)).slice(0, 4);
  for (const p of pistesNonLues) sources.push({ titre: p.titre, organisme: p.organisme, date_publication: p.date || 'non datée', url: p.url, passage: 'Non lu : piste à ouvrir.', pertinence: 'Piste du chercheur de sources, non lue.', type: 'secondaire', consultee: false });
  const proposition = m1 ? ` Côté solutions, la gauche propose par exemple ${guillemets(m1)} (L’Avenir en commun).` : '';

  const fiche = {
    id: `pistes-${slug(question)}`, type: 'reference', origine: 'moteur', affirmation: question.replace(/\s+/g, ' ').trim(), volet, sous_theme: choisirSousTheme(volet, question),
    rubriques: [], mots_cles: [...new Set([kbNormalize(question).replace(/[^a-z0-9]+/g, ' ').trim(), ...kbTokens(question).filter((t) => t.length >= 4).slice(0, 6)])].slice(0, 8),
    verdict: null, fiabilite: 'interpretation', stabilite: 'evolutive',
    resume: `Avant de trancher, regardons ce que disent les travaux et les données publiques. Par exemple, ${titres[0]} : ${guillemets(p1.extrait)}.${proposition} Fiche rédigée automatiquement, sans verdict : les documents sont à lire en entier.`,
    contexte: `Question posée ${occurrences > 1 ? `${occurrences} fois ` : ''}et restée sans fiche vérifiée. Le moteur interne (sans IA) a cherché des sources publiques et rédigé cette fiche de travail en attendant une vérification complète.`,
    explication: 'Cette fiche ne dit pas si l’affirmation est vraie ou fausse : elle rassemble ce que des chercheurs, des administrations ou des vérificateurs de faits ont publié sur le sujet, cité mot pour mot, et ce que propose la gauche. C’est un point de départ pour argumenter avec des faits plutôt qu’avec des impressions.',
    faits: faits.slice(0, 8), sources,
    argumentaires: {
      court: `Avant de conclure, regardons ce que disent les études : ${titres[0]} en parle. Une impression ne vaut pas une enquête.${proposition}`,
      moyen: `Ce genre d’affirmation circule beaucoup, mais elle mérite d’être confrontée à des travaux sérieux. ${citables.map((p) => `${guillemets(p.titre)}${p.date ? ` (${p.date})` : ''} : ${guillemets(p.extrait)}.`).join(' ')}\n\nLa démarche de gauche, c’est de partir des faits et des conditions de vie réelles, pas de désigner des coupables.${proposition}`,
      detaille: `Ce que disent les sources trouvées (résumés cités, documents à lire en entier) :\n${citables.map((p) => `– ${guillemets(p.titre)} — ${p.organisme}${p.date ? `, ${p.date}` : ''} : ${guillemets(p.extrait)} (${p.url})`).join('\n')}${mesures.length ? `\n\nCe que propose L’Avenir en commun :\n${mesures.map((m) => `– ${m.texte.replace(/[.\s]+$/, '')}`).join('\n')}` : ''}${pistesNonLues.length ? `\n\nPour aller plus loin (non lu) :\n${pistesNonLues.map((p) => `– ${p.titre} (${p.url})`).join('\n')}` : ''}\n\nPour débattre : demander d’où vient l’affirmation, quelles données la soutiennent, et qui a intérêt à ce qu’on y croie.`,
      empathie: 'C’est une question que beaucoup de gens se posent, souvent parce qu’ils vivent eux-mêmes des difficultés réelles. On peut partir de ce qui t’inquiète, puis regarder ensemble ce que disent les études.',
    },
    contre_arguments: [
      { objection: 'Les études, on leur fait dire ce qu’on veut.', reponse: 'C’est pour ça qu’on cite leurs propres mots et leur lien : chacun peut les lire et les discuter. Une étude se critique avec une autre étude, pas avec une impression.' },
      { objection: 'Ce sont des chercheurs de gauche.', reponse: 'Ce qui compte, c’est la méthode et les données, publiées et vérifiables. Si une autre étude sérieuse dit le contraire, on peut la mettre sur la table.' },
    ],
    questions: ['D’où tiens-tu cette information ?', 'Quelle donnée te ferait changer d’avis ?'],
    limites: [
      'Fiche rédigée automatiquement par le moteur interne, sans IA et sans relecture : elle cite des résumés (HAL, data.gouv.fr, vérificateurs de faits) sans avoir lu les documents complets.',
      'Pas de verdict : la fiche ne dit pas si l’affirmation est exacte ; une fiche de vérification complète reste à écrire.',
      'Les pistes ont été choisies par mots-clés : certaines peuvent être hors sujet ou anciennes (voir leur date).',
    ],
    publics: {
      convaincus: `Je ne vais pas te dire que tu as tort sans preuve, mais toi non plus, tu n’as pas de preuve. Il existe des travaux sérieux sur le sujet, par exemple ${titres[0]}. Tu veux qu’on regarde ce qu’ils disent vraiment ?`,
      indecis: `Ta question est légitime. Pour te faire ton avis, pars des travaux publiés plutôt que des rumeurs : ${titres[0]} en est un exemple.${proposition}`,
    },
    lecture: {
      valeurs: VALEURS_VOLET[volet] || ['democratie', 'egalite'],
      mecanismes: 'Une affirmation qui circule sans source prospère sur l’inquiétude. La confronter aux travaux publiés et aux données publiques remet le débat sur le terrain des faits.',
      consequences: 'Sans repères fiables, les difficultés réelles sont attribuées à des boucs émissaires plutôt qu’aux choix politiques qui les produisent.',
      democratie: 'Un débat démocratique a besoin de faits partagés et vérifiables : citer ses sources, c’est permettre à l’autre de les discuter.',
      propositions: [...mesures.map((m) => m.texte.replace(/[.\s]+$/, '') + '.').filter(sansChiffre), 'Toujours demander la source d’une affirmation et la confronter aux études publiées.'].slice(0, 3),
      defavorables: [{ fait: 'Cette fiche ne tranche pas : elle ne prouve pas que l’affirmation est fausse.', integration: 'Le dire franchement, et compléter la fiche par une vérification complète dès que possible.' }],
    },
    derniere_verification: jour,
    a_actualiser_le: new Date(Date.parse(jour) + 90 * 864e5).toISOString().slice(0, 10),
    raison_actualisation: 'Fiche rédigée automatiquement : à remplacer par une fiche de vérification complète.',
    moteur: { version: VERSION_MOTEUR, redacteur: true, genere_le: jour, occurrences, pistes: citables.length, mesures: mesures.length, indicateurs: indicateurs.map((i) => i.id) },
  };
  // aucun chiffre dans la lecture de gauche (règle de l'application)
  fiche.lecture.propositions = fiche.lecture.propositions.filter(sansChiffre);
  if (!fiche.lecture.propositions.length) fiche.lecture.propositions = ['Toujours demander la source d’une affirmation et la confronter aux études publiées.'];
  return { fiche };
}

export const classeAutorite = (p) => LE_CLASSES[classerSource(p)]?.role === 'autorite';
