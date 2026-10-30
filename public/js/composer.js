// Moteur de personnalisation du MODE AUTONOME (sans Internet, sans modèle d'IA).
//
// Principe : un PLAN explicite est d'abord calculé à partir du contexte (fiche, affirmation, mode, profil,
// objectif, lien, cadre, arguments déjà avancés, réactions observées), puis rendu en blocs ordonnés.
// Le plan choisit : l'approche, le point d'entrée, l'argument principal, les preuves, le niveau de détail,
// la source mise en avant, l'ordre, l'objection à anticiper, les questions, le ton, la conclusion et la
// prochaine étape. Chaque choix est accompagné de sa raison et, quand elle existe, de la fiche scientifique.
//
// Garde-fous : aucun fait, chiffre, citation ou source n'est créé ni modifié. Les seuls textes ajoutés
// sont des formules de liaison sans contenu factuel (questions, transitions, consignes).
import { LE_PRINCIPES } from './ligne-editoriale.js';
import { nettoyerProfil, strategieProfil, has, REGLES } from './profile.js';
import { kbDataAge, kbScore } from './kbsearch.js';
import { INTERLOCUTEUR } from './taxonomy.js';

const firstSentence = (t) => { const m = String(t || '').match(/^.*?[.!?](\s|$)/); return (m ? m[0] : String(t || '')).trim(); };
const anyOf = (p, dim, vals) => vals.some((v) => has(p, dim, v));
const yearsOf = (t) => (String(t || '').match(/\b(1[5-9]\d\d|20\d\d)\b/g) || []).map(Number);

// ─── Effets de chaque option sur le plan (table de décision exécutable) ─────────────────
// Poids d'approche : F = factuelle et statistique, H = historique et institutionnelle, V = valeurs et conséquences.
export const EFFETS = {
  debat: {
    calme: { detail: +1, influence: ['niveau de détail'] },
    competitif: { detail: -2, ton: 'ferme', entree: 'fait', conclusion: 'demande_preuve', maxPreuves: 1, F: 1, influence: ['niveau de détail', 'ton', 'point d’entrée', 'conclusion', 'nombre de preuves', 'approche'] },
    provocateur: { detail: -2, ton: 'ferme', entree: 'cadre', conclusion: 'public', maxPreuves: 1, recentrage: true, influence: ['niveau de détail', 'ton', 'point d’entrée', 'conclusion', 'recentrage'] },
    susceptible: { ton: 'calme', entree: 'reformulation', questionsAvant: true, maxPreuves: 2, V: 2, influence: ['point d’entrée', 'ton', 'ordre (questions avant contre-argument)', 'nombre de preuves'] },
    evite: { ton: 'calme', entree: 'question', questionsAvant: true, maxPreuves: 2, V: 2, influence: ['point d’entrée', 'ton', 'ordre'] },
    hesitant: { ton: 'nuance', conclusion: 'pistes', incertitudes: true, questionsAvant: true, influence: ['conclusion (plusieurs pistes)', 'incertitudes', 'ton', 'ordre (demander ce qui fait hésiter)'] },
  },
  faits: {
    chiffres: { F: 3, preuve: 'chiffre', detail: +1, methode: true, influence: ['approche', 'choix des preuves', 'niveau de détail', 'méthode'] },
    logique: { F: 2, preuve: 'chiffre', conclusion: 'synthese', influence: ['approche', 'conclusion'] },
    exemples: { V: 3, preuve: 'concret', entree: 'exemple', influence: ['approche', 'point d’entrée', 'choix des preuves'] },
    temoignages: { V: 3, preuve: 'concret', entree: 'exemple', influence: ['approche', 'point d’entrée', 'choix des preuves'] },
    experience: { V: 2, preuve: 'concret', entree: 'vecu', influence: ['approche', 'point d’entrée', 'questions'] },
  },
  autorite: {
    confiance: { source: 'institutionnelle', H: 1, influence: ['source mise en avant', 'approche'] },
    mefiance: { source: 'concordantes', methode: true, objection: 'sources', question: 'source', influence: ['méthode', 'sources concordantes', 'objection anticipée', 'questions'] },
    independantes: { source: 'independante', methode: true, influence: ['source mise en avant', 'méthode'] },
  },
  changement: {
    prudent: { H: 1, conclusion: 'petit_pas', influence: ['approche', 'conclusion'] },
    pragmatique: { preuve: 'concret', F: 1, influence: ['choix des preuves', 'approche'] },
    reformiste: { H: 2, influence: ['approche (exemples institutionnels)'] },
    rupture: { detail: +1, F: 1, influence: ['niveau de détail', 'approche'] },
  },
  valeurs: {
    justice_sociale: { V: 2, angle: 'justice', influence: ['approche', 'angle de valeur', 'choix des preuves'] },
    egalite: { V: 2, angle: 'justice', influence: ['approche', 'angle de valeur', 'choix des preuves'] },
    solidarite: { V: 2, angle: 'justice', influence: ['approche', 'angle de valeur', 'choix des preuves'] },
    securite: { V: 2, angle: 'securite', entree: 'preoccupation', influence: ['approche', 'angle de valeur', 'point d’entrée', 'choix des preuves'] },
    ordre: { V: 1, H: 1, angle: 'securite', entree: 'preoccupation', influence: ['approche', 'angle de valeur', 'point d’entrée'] },
    liberte: { V: 1, angle: 'merite', influence: ['angle de valeur', 'choix des preuves'] },
    merite: { V: 1, F: 1, angle: 'merite', influence: ['angle de valeur', 'choix des preuves'] },
    tradition: { H: 2, angle: 'nation', influence: ['approche', 'angle de valeur'] },
    souverainete: { H: 2, angle: 'nation', influence: ['approche', 'angle de valeur'] },
    protection_groupe: { V: 1, H: 1, angle: 'nation', influence: ['approche', 'angle de valeur'] },
  },
  connaissance: {
    faible: { detail: -1, ton: 'pedagogique', preuve: 'court', question: 'origine', influence: ['niveau de détail', 'ton', 'choix des preuves', 'questions'] },
    moyenne: { influence: [], neutre: 'Valeur par défaut : aucun changement volontaire.' },
    elevee: { detail: +2, methode: true, objection: 'serieuse', influence: ['niveau de détail', 'méthode', 'objection anticipée'] },
  },
  politique: {
    engage: { concession: true, influence: ['point d’entrée (reconnaître ce qui est fondé)', 'ton'] },
    partisan: { concession: true, entree: 'concession', ton: 'calme', influence: ['point d’entrée', 'ton'] },
    desabuse: { ton: 'pedagogique', preuve: 'concret', V: 1, influence: ['ton', 'choix des preuves'] },
    peu_informe: { detail: -1, ton: 'pedagogique', preuve: 'court', influence: ['niveau de détail', 'ton', 'choix des preuves'] },
    ouvert: { detail: +1, approchesMultiples: true, influence: ['niveau de détail', 'comparaison des approches mise en avant'] },
  },
  lien: {
    parent: { ton: 'chaleureux', conclusion: 'lien', lienPhrase: true, influence: ['ton', 'conclusion', 'phrase sur le lien'] },
    conjoint: { ton: 'chaleureux', conclusion: 'lien', lienPhrase: true, influence: ['ton', 'conclusion', 'phrase sur le lien'] },
    ami: { ton: 'franc', influence: ['ton'] },
    collegue: { detail: -1, ton: 'neutre', influence: ['niveau de détail', 'ton'] },
    connaissance: { ton: 'neutre', influence: ['ton'] },
    public: { conclusion: 'public', ton: 'ferme', publicPhrase: true, influence: ['conclusion', 'ton', 'phrase pour le public'] },
  },
  cadre: {
    prive: { detail: +1, influence: ['niveau de détail (on peut approfondir sans public)'] },
    repas: { detail: -1, entree: 'question', apaisement: true, influence: ['niveau de détail', 'point d’entrée', 'proposition de pause'] },
    plusieurs: { publicPhrase: true, regles: true, influence: ['phrase pour le public', 'règles de discussion'] },
    reseaux: { publicPhrase: true, detail: -1, influence: ['phrase pour le public', 'niveau de détail'] },
  },
  objectif: {
    reflechir: { conclusion: 'question', influence: ['conclusion'] },
    riposter: { detail: -1, entree: 'fait', publicPhrase: true, influence: ['niveau de détail', 'point d’entrée', 'phrase pour le public'] },
    corriger: { F: 2, correction: true, entree: 'correction', influence: ['approche', 'point d’entrée (correction expliquée)'] },
    terrain: { entree: 'accord', V: 1, conclusion: 'accord', influence: ['point d’entrée', 'conclusion'] },
    evoluer: { conclusion: 'petit_pas', V: 1, influence: ['conclusion', 'approche'] },
  },
};

// ─── Caractéristiques des faits et des sources ─────────────────────────────
const INSTITUTION = /(insee|drees|dares|france travail|légifrance|legifrance|constitution|assemblée|assemblee|sénat|senat|conseil d|conseil constitutionnel|ministère|ministere|rte|cour des comptes|eurostat|ocde|oecd|commission européenne|justice)/i;
const CONCRET = /(concr|quotidien|famille|foyer|salari|travail|loyer|retraite|enfant|ménage|vie|mois|personne seule|smic|rsa)/i;
const ANGLE_RE = {
  securite: /(sécurit|securit|police|délinqu|delinqu|prison|justice|protég|violence|crim)/i,
  justice: /(inégal|inegal|pauvre|pauvret|salaire|social|solidar|redistrib|précar|precar|travailleur)/i,
  merite: /(travail|cotis|effort|emploi|mérit|merit|libert|entreprise)/i,
  nation: /(france|national|république|republique|résistance|resistance|1945|1936|histoire|souverain|patri)/i,
};
const OBJECTION_RE = {
  sources: /(chiffre|statist|source|officiel|médias|medias|truqu|manipul|gouvernement|étude|etude|journalist)/i,
  securite: /(sécurit|securit|police|délinqu|delinqu|crim|justice)/i,
  merite: /(travail|assist|mérit|merit|profit|fraude|paress)/i,
  nation: /(france|national|étranger|etranger|immigr|identit)/i,
  justice: /(injust|inégal|inegal|riches|patron)/i,
  vecu: /(je connais|j'ai vu|autour de|dans mon|chez moi|exemple)/i,
};

function faitInfo(fiche, f, i) {
  const s = fiche.sources[f.source] || {};
  const years = yearsOf(`${f.periode || ''} ${f.fait}`);
  return {
    i,
    chiffre: Boolean(f.chiffre),
    historique: fiche.type === 'histoire' || (years.length > 0 && Math.min(...years) < 2000),
    institutionnel: INSTITUTION.test(`${s.organisme || ''} ${s.titre || ''}`),
    primaire: s.type === 'primaire',
    independant: (s.type === 'secondaire' || s.type === 'media') && !INSTITUTION.test(s.organisme || ''),
    concret: CONCRET.test(`${f.fait} ${f.explication || ''}`),
    court: f.fait.length < 170,
    etabli: (f.fiabilite || fiche.fiabilite) === 'etabli',
    texte: `${f.fait} ${f.explication || ''}`,
  };
}

function sourceOf(fiche, fait) {
  const s = fiche.sources[fait.source];
  return s ? { titre: s.titre, organisme: s.organisme, date: s.date_publication, url: s.url, type: s.type || null, consultee: s.consultee } : null;
}

function preuve(fiche, i, methode) {
  const fait = fiche.faits[i];
  const s = sourceOf(fiche, fait);
  return {
    index: i,
    texte: fait.fait,
    chiffre: fait.chiffre || null,
    periode: fait.periode || null,
    perimetre: fait.perimetre || null,
    explication: fait.explication || null,
    fiabilite: fait.fiabilite || fiche.fiabilite,
    source: s,
    methode: methode ? [fait.periode && `Période : ${fait.periode}`, fait.perimetre && `Périmètre : ${fait.perimetre}`, s && `Source : ${s.organisme}${s.type ? ` (${s.type})` : ''}, ${s.date}`].filter(Boolean).join(' · ') : null,
  };
}

/** Effets cumulés du profil (sans hasard : même contexte = même plan). */
export function effetsProfil(profil) {
  const p = nettoyerProfil(profil);
  const e = { F: 0, H: 0, V: 0, detail: 0, angles: [], entrees: [], conclusions: [], tons: [], preuves: [], sources: [], objections: [], questions: [] };
  if (p.inconnu) return { p, e: { ...e, entrees: ['question'], questionsAvant: true, inconnu: true } };
  for (const d of INTERLOCUTEUR) {
    const vals = Array.isArray(p[d.id]) ? p[d.id] : p[d.id] ? [p[d.id]] : [];
    for (const v of vals) {
      const x = EFFETS[d.id]?.[v];
      if (!x) continue;
      for (const k of ['F', 'H', 'V', 'detail']) if (x[k]) e[k] += x[k];
      if (x.angle) e.angles.push(x.angle);
      if (x.entree) e.entrees.push(x.entree);
      if (x.conclusion) e.conclusions.push(x.conclusion);
      if (x.ton) e.tons.push(x.ton);
      if (x.preuve) e.preuves.push(x.preuve);
      if (x.source) e.sources.push(x.source);
      if (x.objection) e.objections.push(x.objection);
      if (x.question) e.questions.push(x.question);
      if (x.maxPreuves) e.maxPreuves = Math.min(e.maxPreuves ?? 9, x.maxPreuves);
      for (const k of ['methode', 'recentrage', 'questionsAvant', 'incertitudes', 'concession', 'approchesMultiples', 'lienPhrase', 'publicPhrase', 'apaisement', 'regles', 'correction']) if (x[k]) e[k] = true;
    }
  }
  e.angles = [...new Set(e.angles)];
  return { p, e };
}

// ─── Fiches liées (autre angle, exemple historique) ─────────────────────────
export function fichesLiees(fiche, bibliotheque = [], { exclure = [] } = {}) {
  const q = `${fiche.affirmation} ${(fiche.mots_cles || []).join(' ')}`;
  return bibliotheque
    .filter((x) => x.id !== fiche.id && x.type !== 'science' && !exclure.includes(x.id))
    .map((x) => ({ x, s: kbScore(x, q).score + ((x.rubriques || []).some((r) => (fiche.rubriques || []).includes(r)) ? 2 : 0) + (x.volet === fiche.volet ? 1 : 0) }))
    .filter((y) => y.s >= 5)
    .sort((a, b) => b.s - a.s)
    .map((y) => y.x);
}

// ─── Approches ─────────────────────────────────────────────────────────────
const APPROCHES = {
  factuelle: { titre: 'Approche factuelle et statistique', profil: 'Personnes sensibles aux chiffres, à la logique ou qui demandent des preuves.', risque: 'Peut sembler froide ou être perçue comme une leçon ; une avalanche de chiffres braque.' },
  historique: { titre: 'Approche historique ou institutionnelle', profil: 'Personnes attachées à la tradition, à la nation, aux institutions ou à la continuité.', risque: 'Peut sembler éloignée du présent ; un exemple historique ne prouve pas à lui seul une situation actuelle.' },
  valeurs: { titre: 'Approche par les valeurs et les conséquences concrètes', profil: 'Personnes qui raisonnent par l’expérience, les valeurs ou qui se braquent face aux chiffres.', risque: 'Peut paraître émotionnelle ; il faut garder les faits vérifiés au centre.' },
};

function scorePreuve(info, approche, e) {
  let s = 0;
  if (approche === 'factuelle') s += (info.chiffre ? 3 : 0) + (info.primaire ? 1 : 0);
  if (approche === 'historique') s += (info.historique ? 3 : 0) + (info.institutionnel ? 2 : 0);
  if (approche === 'valeurs') s += (info.concret ? 2 : 0) + (info.chiffre ? 0.5 : 0);
  for (const pr of e.preuves) {
    if (pr === 'chiffre' && info.chiffre) s += 2;
    if (pr === 'concret' && info.concret) s += 2;
    if (pr === 'court' && info.court) s += 1.5;
  }
  for (const a of e.angles) if (ANGLE_RE[a]?.test(info.texte)) s += 1.5;
  if (e.sources.includes('institutionnelle') && info.institutionnel) s += 1.5;
  if (e.sources.includes('independante') && info.independant) s += 2;
  if (info.etabli) s += 0.5;
  return s;
}

function approcheScores(fiche, infos, e, liees) {
  const nbChiffres = infos.filter((x) => x.chiffre).length;
  const nbHist = infos.filter((x) => x.historique || x.institutionnel).length;
  const histLiee = liees.find((x) => x.type === 'histoire');
  return {
    factuelle: { score: 0.5 + e.F + (nbChiffres ? 1 : -3) + (e.correction ? 1 : 0), disponible: nbChiffres > 0 || infos.some((x) => x.primaire), manque: nbChiffres ? null : 'La fiche ne contient pas de donnée chiffrée : l’approche statistique est limitée.' },
    historique: { score: e.H + (fiche.type === 'histoire' ? 3 : 0) + (nbHist ? 1 : 0) + (histLiee ? 0.5 : 0), disponible: nbHist > 0 || Boolean(histLiee), liee: nbHist ? null : histLiee || null, manque: nbHist || histLiee ? null : 'Pas d’élément historique ou institutionnel dans la bibliothèque pour ce sujet.' },
    valeurs: { score: 0.5 + e.V + (infos.some((x) => x.concret) ? 1 : 0), disponible: true, manque: null },
  };
}

// ─── Plan ──────────────────────────────────────────────────────────────────
/**
 * Calcule un plan explicite. `ctx` : { profil, mode, deja: [indices de faits déjà avancés],
 * objectionsVues: [...], questionsPosees: [...], bibliotheque, recents: [ids de fiches récemment utilisées], force }.
 */
export function planifier(fiche, ctx = {}) {
  const mode = ctx.mode === 'convaincre' ? 'convaincre' : 'gagner';
  const { p, e } = effetsProfil(ctx.profil);
  const deja = new Set(ctx.deja || []);
  const infos = fiche.faits.map((f, i) => faitInfo(fiche, f, i));
  const liees = fichesLiees(fiche, ctx.bibliotheque || [], { exclure: ctx.recents || [] });
  const sc = approcheScores(fiche, infos, e, liees);
  // le mode infléchit l'approche : gagner → factuel ; convaincre → valeurs (sans écraser le profil)
  if (mode === 'gagner') sc.factuelle.score += 0.75; else sc.valeurs.score += 0.75;
  const approche = Object.entries(sc).filter(([, v]) => v.disponible).sort((a, b) => b[1].score - a[1].score)[0][0];
  const pourquoi = [];
  const raison = (choix, texte, ficheSci = null) => pourquoi.push({ choix, raison: texte, fiche: ficheSci });

  // niveau de détail
  let d = e.detail + (mode === 'gagner' ? -0.5 : 0.5);
  const detail = d <= -1 ? 'bref' : d >= 2 ? 'approfondi' : 'standard';
  const maxPreuves = Math.min(e.maxPreuves ?? 9, detail === 'bref' ? 1 : detail === 'approfondi' ? 3 : 2);

  // preuves
  const ordre = infos.map((x) => ({ i: x.i, s: scorePreuve(x, approche, e) - (deja.has(x.i) ? 100 : 0) })).sort((a, b) => b.s - a.s || a.i - b.i);
  let choisis = ordre.filter((x) => x.s > -50).slice(0, maxPreuves).map((x) => x.i);
  if (!choisis.length) choisis = ordre.slice(0, 1).map((x) => x.i); // tout a déjà été dit : on reprend le plus solide
  // méfiance : une seconde source d'un autre organisme si elle existe
  let concordantes = null;
  if (e.sources.includes('concordantes') || e.sources.includes('independante')) {
    const orgs = new Set(choisis.map((i) => fiche.sources[fiche.faits[i].source]?.organisme));
    const autre = ordre.find((x) => !choisis.includes(x.i) && !orgs.has(fiche.sources[fiche.faits[x.i].source]?.organisme) && x.s > -50);
    if (autre && choisis.length < Math.min(3, e.maxPreuves ?? 3)) choisis = [...choisis, autre.i]; // une limite explicite (confrontation) l'emporte
    const orgs2 = [...new Set(choisis.map((i) => fiche.sources[fiche.faits[i].source]?.organisme))];
    concordantes = orgs2.length >= 2 ? orgs2 : null;
  }
  const preuves = choisis.map((i) => preuve(fiche, i, e.methode));

  // source mise en avant
  const indep = choisis.find((i) => infos[i].independant);
  const inst = choisis.find((i) => infos[i].institutionnel);
  let sourceAvant = choisis[0];
  if (e.sources.includes('independante') && indep !== undefined) sourceAvant = indep;
  else if (e.sources.includes('institutionnelle') && inst !== undefined) sourceAvant = inst;

  // point d'entrée
  const pref = mode === 'gagner' ? ['correction', 'fait', 'cadre', 'concession', 'preoccupation', 'exemple', 'vecu', 'accord', 'reformulation', 'question'] : ['reformulation', 'question', 'vecu', 'exemple', 'preoccupation', 'accord', 'concession', 'correction', 'cadre', 'fait'];
  const candidats = [...e.entrees];
  if (e.concession && (fiche.objections_legitimes?.length || ['plutot_exact', 'trompeur'].includes(fiche.verdict))) candidats.push('concession');
  if (!candidats.length) candidats.push(mode === 'gagner' ? 'fait' : 'question');
  // « gagner » : on entre par le fond (fait, correction, cadre, concession), jamais par une écoute de principe
  const ENTREES_GAGNER = ['correction', 'fait', 'cadre', 'concession', 'exemple'];
  const entree = mode === 'gagner'
    ? (pref.find((x) => candidats.includes(x) && ENTREES_GAGNER.includes(x)) || (fiche.verdict === 'contredit' || fiche.verdict === 'trompeur' ? 'correction' : 'fait'))
    : (pref.find((x) => candidats.includes(x)) || candidats[0]);

  // ton
  const tonPref = mode === 'gagner' ? ['ferme', 'franc', 'neutre', 'pedagogique', 'nuance', 'calme', 'chaleureux'] : ['calme', 'chaleureux', 'pedagogique', 'nuance', 'franc', 'neutre', 'ferme'];
  const ton = tonPref.find((x) => e.tons.includes(x)) || (mode === 'gagner' ? 'assure' : 'bienveillant');

  // objection anticipée (pas déjà traitée)
  const vues = new Set(ctx.objectionsVues || []);
  const concerns = [...e.objections, ...e.angles, ...(e.preuves.includes('concret') ? ['vecu'] : [])];
  const objs = (fiche.contre_arguments || []).map((o, k) => ({ o, k, s: concerns.reduce((acc, c) => acc + (OBJECTION_RE[c]?.test(o.objection) ? 2 : 0), 0) + (e.objections.includes('serieuse') ? o.reponse.length / 400 : 0) - (vues.has(k) ? 100 : 0) }))
    .sort((a, b) => b.s - a.s || a.k - b.k);
  const objection = objs.length && objs[0].s > -50 ? { ...objs[0].o, index: objs[0].k } : null;
  const objections = objs.filter((x) => x.s > -50).slice(0, mode === 'gagner' ? 2 : 1).map((x) => ({ ...x.o, index: x.k }));

  // questions
  const posees = new Set(ctx.questionsPosees || []);
  const pool = [];
  if (e.questions.includes('source')) pool.push('Quelle source te paraîtrait fiable pour vérifier ça ?');
  if (e.questions.includes('origine')) pool.push('Tu as entendu ça où ?');
  if (e.preuves.includes('concret') && anyOf(p, 'faits', ['experience'])) pool.push('Qu’est-ce que tu as vu autour de toi qui te fait penser ça ?');
  if (has(p, 'debat', 'hesitant')) pool.push('Qu’est-ce qui te fait hésiter ?');
  if (e.angles.length) pool.push('Qu’est-ce qui compte le plus pour toi dans cette question ?');
  pool.push(...(fiche.questions || []));
  if (e.inconnu && mode === 'convaincre') pool.unshift('Qu’est-ce qui t’amène à penser ça ?');
  // « gagner » : d'abord les questions qui mettent le raisonnement à l'épreuve (celles de la fiche)
  if (mode === 'gagner') pool.unshift(...(fiche.questions || []));
  const nbQ = mode === 'convaincre' ? (detail === 'bref' ? 1 : 2) : (e.questionsAvant ? 1 : detail === 'approfondi' ? 1 : 0);
  const restantes = [...new Set(pool)].filter((q) => !posees.has(q));
  const questions = restantes.slice(0, Math.max(nbQ, mode === 'convaincre' ? 1 : 0));
  // question de conclusion : jamais une question déjà posée dans la même réponse
  const questionFinale = restantes.find((q) => !questions.includes(q)) || 'Et toi, qu’est-ce que tu en penses maintenant ?';

  // conclusion
  const conclPref = mode === 'gagner' ? ['public', 'demande_preuve', 'synthese', 'pistes', 'lien', 'accord', 'petit_pas', 'question'] : ['pistes', 'lien', 'accord', 'petit_pas', 'question', 'synthese', 'public', 'demande_preuve'];
  const conclusion = conclPref.find((x) => e.conclusions.includes(x) || (x === 'public' && e.publicPhrase)) || (mode === 'gagner' ? 'synthese' : 'question');

  // ordre des blocs
  let ordreBlocs;
  if (mode === 'gagner') {
    ordreBlocs = e.questionsAvant ? ['entree', 'question', 'replique', 'preuves', 'objection', 'conclusion'] : ['entree', 'replique', 'preuves', 'objection', 'developpement', 'conclusion'];
    if (entree === 'concession') ordreBlocs = ['entree', 'replique', 'preuves', 'objection', 'conclusion'];
    if (detail === 'approfondi') ordreBlocs = [...ordreBlocs.filter((b) => b !== 'developpement' && b !== 'conclusion'), 'developpement', 'conclusion'];
    if (detail === 'bref') ordreBlocs = ordreBlocs.filter((b) => b !== 'developpement' && (b !== 'objection' || e.objections.length));
  } else {
    ordreBlocs = e.questionsAvant || e.inconnu ? ['question', 'entree', 'angle', 'preuves', 'reconnaitre', 'empathie', 'conclusion'] : ['entree', 'angle', 'preuves', 'reconnaitre', 'question', 'empathie', 'conclusion'];
    if (approche === 'factuelle') ordreBlocs = ordreBlocs.filter((b) => b !== 'angle').concat([]);
    if (entree === 'vecu' || entree === 'exemple') ordreBlocs = ['entree', 'preuves', 'angle', 'question', 'reconnaitre', 'empathie', 'conclusion'];
  }
  // une entrée « j'aimerais comprendre » doit être suivie immédiatement des questions
  if (entree === 'question' && ordreBlocs.includes('question')) {
    ordreBlocs = ordreBlocs.filter((b) => b !== 'question');
    ordreBlocs.splice(ordreBlocs.indexOf('entree') + 1, 0, 'question');
  }
  if (e.apaisement && mode === 'convaincre') ordreBlocs.push('pause');
  if (e.recentrage) ordreBlocs.splice(1, 0, 'recentrage');
  ordreBlocs = [...new Set(ordreBlocs)];

  // prochaine étape (conditionnelle)
  const suivantes = [];
  if (e.sources.includes('concordantes') || e.methode) suivantes.push(['truquees', 'Si elle dit que les chiffres sont truqués : montre comment ils sont calculés et propose de vérifier ensemble une seconde source.']);
  if (has(p, 'debat', 'competitif') || has(p, 'debat', 'provocateur')) suivantes.push(['preuves', 'Si elle conteste : demande-lui sa source, avec la date, et compare-la à la tienne.']);
  if (e.questionsAvant) suivantes.push(['braque', 'Si elle se braque : arrête d’argumenter, reformule son inquiétude, propose d’en reparler plus tard.']);
  suivantes.push(['concede', 'Si elle reconnaît un point : consolide-le sans triompher et arrête-toi là pour aujourd’hui.']);
  const prochaine = suivantes.slice(0, 2).map(([retour, texte]) => ({ retour, texte }));

  // incertitudes et hypothèses
  const incertitudes = [];
  const age = kbDataAge(fiche, ctx.today ? { today: ctx.today } : {});
  if (age.niveau !== 'stable') incertitudes.push(age.texte);
  if (fiche.fiabilite === 'debat' || fiche.fiabilite === 'interpretation') incertitudes.push('Sujet débattu ou interprétatif : présente-le comme tel, sans certitude excessive.');
  if (ctx.force === 'partielle') incertitudes.push('La fiche traite un sujet voisin de ta question : vérifie qu’elle y répond vraiment.');
  if (e.preuves.includes('chiffre') && !infos.some((x) => x.chiffre)) incertitudes.push('La bibliothèque ne contient pas de donnée chiffrée sur ce point : n’en avance pas.');
  if (e.sources.includes('independante') && indep === undefined) incertitudes.push('Pas de source indépendante dans cette fiche : explique plutôt la méthode de la source officielle.');
  if (e.incertitudes && fiche.limites?.length) incertitudes.push(`Ce qu’on ne sait pas : ${fiche.limites[0]}`);
  if (sc[approche].liee && approche === 'historique') incertitudes.push(`Exemple historique tiré d’une fiche liée (« ${sc[approche].liee.affirmation} ») : il éclaire, il ne prouve pas la situation actuelle.`);
  const hypotheses = p.inconnu ? [] : REGLES.filter((r) => r.id !== 'ethique' && r.quand(p)).map((r) => r.titre);

  // justification des choix
  raison('approche', `${APPROCHES[approche].titre} : ${approche === 'factuelle' ? 'profil sensible aux preuves ou mode « gagner »' : approche === 'historique' ? 'profil attaché à l’histoire, à la nation ou aux institutions' : 'profil sensible aux valeurs, au vécu ou au risque de braquer'}.`, approche === 'valeurs' ? 'sci-valeurs-morales' : approche === 'factuelle' ? 'sci-backfire' : null);
  raison('point d’entrée', { correction: 'Correction expliquée : le bon chiffre, sa source, pourquoi l’autre est faux.', fait: 'Entrée directe par un fait vérifiable.', cadre: 'Poser le cadre et s’adresser au public plutôt que suivre la provocation.', concession: 'Reconnaître d’abord ce qui est fondé dans la position adverse.', preoccupation: 'Partir de la préoccupation déclarée.', exemple: 'Partir d’un exemple concret tiré de la fiche.', vecu: 'Reconnaître le vécu avant de le mettre en perspective.', accord: 'Commencer par ce sur quoi on est d’accord.', reformulation: 'Reformuler avant tout contre-argument.', question: 'Commencer par une question ouverte.' }[entree], { reformulation: 'sci-reactance', question: 'sci-entretien-motivationnel', concession: 'sci-identite-sociale', correction: 'sci-backfire', vecu: 'sci-persuasion-modeste', exemple: 'sci-persuasion-modeste', cadre: 'sci-polarisation-groupe', accord: 'sci-valeurs-morales', preoccupation: 'sci-valeurs-morales', fait: null }[entree]);
  raison('niveau de détail', `${detail} (${maxPreuves} preuve${maxPreuves > 1 ? 's' : ''} au plus).`);
  if (concordantes) raison('sources', `Sources de plusieurs organismes : ${concordantes.join(', ')}.`, 'sci-desinformation-confiance');
  if (objection) raison('objection anticipée', `« ${objection.objection} » (choisie selon les préoccupations du profil).`);

  return {
    mode, approche, approche_titre: APPROCHES[approche].titre, entree, ton, detail, max_preuves: maxPreuves,
    preuves, source_avant: preuve(fiche, sourceAvant, true).source, concordantes, objection, objections, questions, question_finale: questionFinale, conclusion,
    ordre: ordreBlocs, prochaine, incertitudes, hypotheses, pourquoi,
    angles: e.angles, lien: Boolean(e.lienPhrase), public: Boolean(e.publicPhrase), regles_discussion: Boolean(e.regles), apaisement: Boolean(e.apaisement), recentrage: Boolean(e.recentrage),
    scores: Object.fromEntries(Object.entries(sc).map(([k, v]) => [k, { score: Number(v.score.toFixed(2)), disponible: v.disponible, manque: v.manque }])),
    liee: sc[approche].liee ? { id: sc[approche].liee.id, affirmation: sc[approche].liee.affirmation } : null,
  };
}

// ─── Rendu : formules de liaison (sans fait) selon le ton ───────────────────
const ANGLES = {
  securite: 'Si ce qui compte pour toi, c’est la sécurité, la vraie question est : qu’est-ce qui protège concrètement ? Regardons ce que disent les faits.',
  justice: 'Derrière ces chiffres, il y a des situations concrètes et des inégalités vécues : c’est ça qui doit nous guider.',
  merite: 'Si on veut que le travail et l’effort soient récompensés, il faut partir des faits, pas des impressions.',
  nation: 'C’est aussi une question de fierté collective : ce qu’on a construit ensemble, et ce qu’on veut protéger.',
};

function texteEntree(plan, fiche) {
  const q = `« ${fiche.affirmation} »`;
  switch (plan.entree) {
    case 'correction': return `Je crois que cette affirmation est inexacte, et je peux te dire pourquoi, source à l’appui : ${q}`;
    case 'fait': return plan.ton === 'ferme' ? 'Un seul fait, vérifiable :' : 'Regardons d’abord les faits :';
    case 'cadre': return 'Je vais répondre sur le fond, une seule fois, pour ceux qui nous écoutent.';
    case 'concession': return `Il y a un point sérieux dans ce que tu dis : ${fiche.objections_legitimes?.[0] || 'la préoccupation est réelle'} Mais sur le fond, les faits disent autre chose.`;
    case 'preoccupation': return 'Ta préoccupation est légitime, et je la partage. Regardons ce qui marche vraiment.';
    case 'exemple': return 'Partons d’un cas concret :';
    case 'vecu': return 'Ce que tu as vécu ou vu autour de toi est réel. Regardons simplement si ça se retrouve à plus grande échelle.';
    case 'accord': return 'On est sans doute d’accord sur une chose : on veut tous les deux que ça aille mieux. Le désaccord porte sur le comment.';
    case 'reformulation': return `Si je te comprends bien, tu penses que ${q}. C’est une idée qu’on entend souvent, et elle part souvent d’une vraie préoccupation.`;
    case 'question': default: return 'Avant de te répondre, j’aimerais comprendre ton point de vue.';
  }
}

function texteConclusion(plan, fiche) {
  const A = fiche.argumentaires || {};
  switch (plan.conclusion) {
    case 'public': return `Pour ceux qui nous écoutent : ${firstSentence(A.court)}${plan.source_avant ? ` Source : ${plan.source_avant.organisme}, ${plan.source_avant.date}.` : ''}`;
    case 'demande_preuve': return `Et toi, sur quoi t’appuies-tu pour dire « ${fiche.affirmation} » ? Donne-moi un chiffre précis, avec sa source et sa date.`;
    case 'synthese': return `En résumé : ${firstSentence(A.court)}`;
    case 'pistes': return 'Il y a plusieurs façons de voir la question : on peut regarder les chiffres, l’histoire, ou les conséquences concrètes. Tu n’es pas obligé de trancher maintenant.';
    case 'lien': return 'Quoi qu’on en pense chacun, ça ne change rien entre nous.';
    case 'accord': return 'On a déjà un point commun ; le reste, on peut y réfléchir chacun de notre côté.';
    case 'petit_pas': return 'Pas besoin de tout changer d’un coup : si on est d’accord sur ce premier point, c’est déjà beaucoup.';
    case 'question': default: return plan.question_finale || 'Et toi, qu’est-ce que tu en penses maintenant ?';
  }
}

const TONS = {
  ferme: 'Ton ferme et posé : phrases courtes, pas de digression, pas d’attaque personnelle.',
  franc: 'Ton franc : dis clairement ton désaccord, avec le respect qu’on doit à un ami.',
  neutre: 'Ton neutre et factuel : pas d’émotion, pas de leçon.',
  pedagogique: 'Ton pédagogique : mots simples, un élément à la fois, sans jargon.',
  nuance: 'Ton nuancé : distingue ce qui est sûr de ce qui reste incertain.',
  calme: 'Ton calme : ralentis, reformule, ne coupe pas la parole.',
  chaleureux: 'Ton chaleureux : rappelle le lien avant le désaccord.',
  bienveillant: 'Ton bienveillant : montre que tu prends son avis au sérieux avant de donner le tien.',
  assure: 'Ton assuré : affirme les faits avec leur source, sans agressivité.',
};

// Ordre de présentation (v9) — la réponse avant la méthode :
//   1. la réponse à l'affirmation et les arguments ; 2. les preuves et ce qu'elles démontrent ;
//   3. comment présenter l'argument (riposte, objections, entrée) ; 4. les conseils de communication.
// Les deux modes gardent les mêmes faits et les mêmes sources ; seules la formulation et la partie 3-4 changent.
// (clés sans chiffre : les contrôles « aucun nombre absent de la fiche » lisent tout le contenu des blocs)
export const PRIORITES = { reponse: ['1', 'La réponse'], preuves: ['2', 'Les preuves'], lecture: ['3', 'La lecture de gauche'], presenter: ['4', 'Comment présenter l’argument'], communication: ['5', 'Comment aborder la discussion'] };
function blocs(plan, fiche, extra = {}) {
  const A = fiche.argumentaires || {};
  const g = plan.mode === 'gagner';
  const out = [];
  const add = (priorite, b) => out.push({ priorite, ...b });
  const paragraphes = (t) => String(t || '').split(/\n{2,}/).filter(Boolean);
  // 1 — la réponse
  add('reponse', { type: 'replique', titre: 'Ce que tu peux répondre', texte: A.court });
  const dev = paragraphes(plan.detail === 'approfondi' ? A.detaille : A.moyen);
  if (dev.length && (plan.detail !== 'bref' || !g)) add('reponse', { type: 'developpement', titre: 'Les arguments solides', paragraphes: dev });
  // 2 — les preuves, chacune avec ce qu'elle démontre
  if (plan.preuves.length) add('preuves', { type: 'preuves', titre: plan.preuves.length > 1 ? `Les preuves et les sources (${plan.preuves.length})` : 'La preuve et sa source', items: plan.preuves, concordantes: plan.concordantes });
  // 3 — lecture de gauche : mécanismes, conséquences humaines, enjeux démocratiques, valeurs, propositions,
  //     et faits défavorables honnêtement intégrés (v10). Les propositions sont étiquetées comme des choix politiques.
  const L = fiche.lecture;
  if (L) {
    add('lecture', {
      type: 'lecture', titre: g ? 'Ce que la gauche répond sur le fond' : 'Ce qui se joue derrière la question',
      mecanismes: L.mecanismes || null, consequences: L.consequences || null, democratie: L.democratie || null,
      valeurs: (L.valeurs || []).filter((v) => LE_PRINCIPES[v]).map((v) => ({ id: v, label: LE_PRINCIPES[v].label, texte: LE_PRINCIPES[v].texte })),
      propositions: L.propositions || [],
      defavorables: L.defavorables || [],
    });
  }
  // 4 — présenter l'argument
  if (g) {
    // la formule propre à l'argument repéré, sinon la conclusion choisie selon le profil (public, charge de la preuve…)
    const finale = texteConclusion({ ...plan, conclusion: plan.conclusion === 'synthese' ? 'demande_preuve' : plan.conclusion }, fiche);
    add('presenter', { type: 'riposte', titre: 'La riposte qui fait réfléchir', texte: extra.formule || finale, question: plan.questions[0] || null });
    // conclusion propre au profil (public, charge de la preuve) : seulement si le profil l'a demandée
    if (extra.formule && ['public', 'demande_preuve'].includes(plan.conclusion)) add('presenter', { type: 'conclusion', titre: 'Pour conclure', texte: finale });
    for (const o of plan.objections) add('presenter', { type: 'objection', titre: 'S’il te répond ceci', objection: o.objection, reponse: o.reponse });
    add('presenter', { type: 'entree', titre: 'Pour lancer l’argument', texte: texteEntree(plan, fiche) });
    if (plan.recentrage) add('presenter', { type: 'texte', titre: 'S’il détourne le sujet', texte: 'On parlait de ce point précis ; je te réponds volontiers sur l’autre sujet ensuite.' });
  } else {
    add('presenter', { type: 'entree', titre: 'Pour l’introduire sans braquer', texte: texteEntree(plan, fiche) });
    if (plan.questions.length) add('presenter', { type: 'questions', titre: 'Les questions pour comprendre son point de vue', items: plan.questions.slice(0, 3) });
    if (fiche.objections_legitimes?.length) add('presenter', { type: 'liste', titre: 'Ce qu’il faut reconnaître', items: fiche.objections_legitimes });
    for (const o of plan.objections) add('presenter', { type: 'objection', titre: 'S’il te répond ceci', objection: o.objection, reponse: o.reponse });
    if (extra.formule) add('presenter', { type: 'conclusion', titre: 'Une phrase pour faire réfléchir', texte: extra.formule });
  }
  // 4 — communication, selon le mode
  add('communication', { type: 'ton', titre: 'Le ton', texte: TONS[plan.ton] || TONS.assure });
  if (g) {
    add('communication', { type: 'texte', titre: 'Pour ne pas te disperser', texte: 'Un argument à la fois, une source pour chaque chiffre ; s’il change de sujet, ramène-le au point de départ.' });
  } else {
    if (plan.angles.length) add('communication', { type: 'texte', titre: 'Partir de ce qui compte pour lui', texte: plan.angles.map((a) => ANGLES[a]).join(' ') });
    if (A.empathie) add('communication', { type: 'empathie', titre: 'La même réponse, dite avec empathie', texte: A.empathie });
    add('communication', { type: 'conclusion', titre: 'Pour conclure', texte: texteConclusion(plan, fiche) });
    if (plan.apaisement) add('communication', { type: 'texte', titre: 'Si ça monte', texte: 'On peut en reparler plus tard, tranquillement. Ce n’est pas grave de ne pas être d’accord ce soir.' });
  }
  if (plan.regles_discussion) add('communication', { type: 'texte', titre: 'Une règle pour la discussion', texte: 'On est plusieurs : je propose que chacun termine sa phrase, et qu’on essaie de comprendre l’autre position avant de répondre.' });
  return out;
}

/** Comparaison de 2 ou 3 approches (pour les sujets complexes). */
export function comparerApproches(fiche, ctx = {}) {
  const res = [];
  const plan = planifier(fiche, { ...ctx, mode: ctx.mode || 'gagner' });
  const { e } = effetsProfil(ctx.profil);
  for (const key of ['factuelle', 'historique', 'valeurs']) {
    const infos = fiche.faits.map((f, i) => faitInfo(fiche, f, i));
    const dispo = plan.scores[key];
    if (!dispo.disponible) continue;
    const idx = infos.map((x) => ({ i: x.i, s: scorePreuve(x, key, e) })).sort((a, b) => b.s - a.s || a.i - b.i).slice(0, 2).map((x) => x.i);
    const pertinentes = idx.filter((i) => (key === 'factuelle' ? infos[i].chiffre || infos[i].primaire : key === 'historique' ? infos[i].historique || infos[i].institutionnel : true));
    const liee = key === 'historique' && !pertinentes.length ? fichesLiees(fiche, ctx.bibliotheque || [], { exclure: ctx.recents || [] }).find((x) => x.type === 'histoire') : null;
    if (key === 'historique' && !pertinentes.length && !liee) continue;
    res.push({
      approche: key,
      titre: APPROCHES[key].titre,
      profil: APPROCHES[key].profil,
      pourquoi: key === plan.approche ? 'Approche la mieux adaptée aux informations données sur la personne.' : `Alternative (score qualitatif ${dispo.score} contre ${plan.scores[plan.approche].score} pour l’approche retenue).`,
      preuves: pertinentes.map((i) => preuve(fiche, i, key === 'factuelle')),
      exemple_lie: liee ? { id: liee.id, affirmation: liee.affirmation, resume: firstSentence(liee.resume) } : null,
      risques: APPROCHES[key].risque,
      limites: [dispo.manque, fiche.limites?.[0]].filter(Boolean),
      questions: (key === 'factuelle' ? ['Quelle source te paraîtrait fiable ?'] : key === 'historique' ? ['Tu savais d’où vient cette règle ?'] : ['Qu’est-ce qui compte le plus pour toi là-dedans ?']).concat((fiche.questions || []).slice(0, 1)),
      score: dispo.score,
    });
  }
  return res.sort((a, b) => b.score - a.score);
}

/** La version la plus solide de l'argument adverse, tirée de la fiche (pas d'homme de paille). */
export function versionSolide(fiche) {
  if (fiche.version_solide) return fiche.version_solide;
  const point = fiche.objections_legitimes?.[0] || fiche.contre_arguments?.[0]?.objection || null;
  return point
    ? `Dans sa forme la plus solide, cette position s’appuie sur ceci : « ${point} » Si ce point est fondé, reconnais-le avant de répondre.`
    : `Prends l’affirmation au sérieux telle qu’elle est formulée : « ${fiche.affirmation} ». Réponds sur les faits, pas sur la personne.`;
}

/**
 * Compose les deux stratégies (plans distincts) et la comparaison des approches.
 * `options` : { mode, deja, objectionsVues, questionsPosees, bibliotheque, recents, force, today }.
 */
export function composer(fiche, profil, options = {}) {
  const ctx = { ...options, profil };
  const pg = planifier(fiche, { ...ctx, mode: 'gagner' });
  const pc = planifier(fiche, { ...ctx, mode: 'convaincre' });
  const { p } = effetsProfil(profil);
  const regles = strategieProfil(p).regles;
  const consulted = fiche.sources.filter((x) => x.consultee);
  return {
    fiche_id: fiche.id,
    affirmation: fiche.affirmation,
    origine: 'composition_locale',
    profil: p,
    donnees: kbDataAge(fiche, options.today ? { today: options.today } : {}),
    version_solide: versionSolide(fiche),
    regles: regles.map((r) => ({ id: r.id, titre: r.titre, consigne: r.consigne, fiche: r.fiche, fondement: r.fondement })),
    plans: { gagner: pg, convaincre: pc },
    gagner: { blocs: blocs(pg, fiche, { formule: options.formules?.gagner }), replique: fiche.argumentaires?.court, preuves: pg.preuves },
    convaincre: { blocs: blocs(pc, fiche, { formule: options.formules?.convaincre }), empathie: fiche.argumentaires?.empathie, faits_progressifs: pc.preuves },
    approches: comparerApproches(fiche, ctx),
    sources: pg.concordantes || pc.concordantes ? consulted.map((x) => ({ titre: x.titre, organisme: x.organisme, date: x.date_publication, url: x.url, type: x.type || null })) : null,
    objections: fiche.contre_arguments || [],
    limites: fiche.limites || [],
    nb_faits: fiche.faits.length,
  };
}

// ─── Échanges successifs ────────────────────────────────────────────────────
const RETOUR_FICHE = { ecoute: 'sci-persuasion-modeste', braque: 'sci-reactance', preuves: 'sci-desinformation-confiance', truquees: 'sci-desinformation-confiance', causes: 'sci-entretien-motivationnel', solution: 'sci-valeurs-morales', hesite: 'sci-autonomie', diversion: 'sci-deliberation', concede: 'sci-dissonance', fin: 'sci-autonomie' };
const RE_RETOUR = [
  ['truquees', /(truqu|bidon|faux chiffres|manipul|mensong|on nous ment|propagande|inventé|invente)/i],
  ['preuves', /(source|preuve|officiel|lien|étude|etude|où tu as vu|d'où ça vient|montre[- ]moi)/i],
  ['causes', /(cause|pourquoi|la faute|à cause|a cause|constat)/i],
  ['solution', /(solution|que faire|quoi faire|proposition|remède|remede|mesure)/i],
  ['braque', /(braqu|énerv|enerv|vexé|vexe|en colère|en colere|crié|crie|parti|claqué|fâch|fach|ferm[ée])/i],
  ['diversion', /(changé de sujet|change de sujet|autre sujet|parlé d'autre chose|et les |et l'immigration|et la dette)/i],
  ['hesite', /(hésit|hesit|sais pas|pas sûr|pas sur|peut-être|peut etre|doute)/i],
  ['concede', /(reconna|d'accord|admet|concède|concede|pas faux|raison sur)/i],
  ['fin', /(fini|terminé|termine|stop|on arrête|on arrete|plus en parler)/i],
  ['ecoute', /(écout|ecout|intéress|interess|réfléch|reflech)/i],
];

/** Interprète une réaction décrite librement (règles explicites, sans IA) ; l'utilisateur peut corriger. */
export function interpreterRetour(texte) {
  const t = String(texte || '');
  const hasConstat = /constat/i.test(t) && /cause/i.test(t);
  if (hasConstat) return 'causes';
  if (/probl[eè]me/i.test(t) && /solution/i.test(t)) return 'solution';
  for (const [k, re] of RE_RETOUR) if (re.test(t)) return k;
  return null;
}

/**
 * Prochaine proposition après un retour. `session` = { utilises, objectionsVues, questionsPosees, retours }.
 * Ne répète pas un élément déjà présenté ; change d'approche si la précédente a échoué.
 */
export function suite(fiche, profil, retour, session = {}, options = {}) {
  const s = { utilises: [], objectionsVues: [], questionsPosees: [], retours: [], ...session };
  const ctx = { ...options, profil, deja: s.utilises, objectionsVues: s.objectionsVues, questionsPosees: s.questionsPosees };
  const A = fiche.argumentaires || {};
  const note = 'Proposition fondée uniquement sur ce que tu as observé : c’est une indication approximative, pas une mesure de ce que ressent la personne.';
  const base = { retour, fiche_science: RETOUR_FICHE[retour] || 'sci-autonomie', note, utilise: null, objection: null, question: null };
  const plan = planifier(fiche, { ...ctx, mode: ['braque', 'hesite', 'causes', 'solution'].includes(retour) ? 'convaincre' : 'gagner' });
  const nouveau = plan.preuves.find((pr) => !s.utilises.includes(pr.index));
  const restantesQ = [...(fiche.questions || [])].filter((q) => !s.questionsPosees.includes(q));
  const deja = s.retours.filter((r) => r === retour).length;
  switch (retour) {
    case 'ecoute':
      return nouveau
        ? { ...base, titre: 'Elle écoute : un élément de plus, pas dix', texte: nouveau.texte, preuve: { ...nouveau, methode: nouveau.methode || preuve(fiche, nouveau.index, true).methode }, conseil: 'Présente un seul nouvel élément, puis demande ce qu’elle en pense.', utilise: nouveau.index, question: restantesQ[0] || null }
        : { ...base, titre: 'Tous les faits de la fiche ont été présentés', texte: restantesQ[0] || 'Qu’en penses-tu, maintenant ?', conseil: 'Laisse-la conclure elle-même ; une question ouverte plutôt qu’un nouvel argument.', question: restantesQ[0] || null };
    case 'braque':
      return { ...base, titre: deja ? 'Elle se braque encore : propose une pause' : 'Elle s’est braquée : on ralentit', texte: deja ? 'On n’est pas obligés d’en parler maintenant. On reprendra un autre jour, si tu veux.' : A.empathie, conseil: deja ? 'Nouveau signal : propose une pause, sans chercher le dernier mot. La conversation reste ouverte si elle reprend.' : 'Arrête d’ajouter des arguments. Reformule son inquiétude, rappelle qu’elle reste libre de son avis, propose de reprendre plus tard.', complement: deja ? null : 'Tu n’es pas obligé d’être d’accord avec moi. Je voulais juste qu’on regarde ça ensemble.' };
    case 'preuves': {
      const pr = nouveau || preuve(fiche, s.utilises[0] ?? plan.preuves[0].index, true);
      const p2 = preuve(fiche, pr.index, true);
      return { ...base, titre: 'Elle demande une source : montre-la, avec la méthode', texte: p2.texte, preuve: p2, conseil: `Donne le lien, la date et le périmètre${p2.source?.type === 'primaire' ? ' (c’est une source officielle ou primaire)' : ''}. Dis aussi ce que le chiffre ne montre pas${fiche.limites?.[0] ? ` : ${fiche.limites[0]}` : '.'}`, utilise: pr.index };
    }
    case 'truquees': {
      const orgs = [...new Set(fiche.faits.map((f) => fiche.sources[f.source]?.organisme))];
      const pr = preuve(fiche, plan.preuves[0].index, true);
      return { ...base, titre: 'Elle doute des chiffres : explique leur fabrication', texte: `Prends un chiffre et montre comment il est fabriqué : qui le produit (${pr.source?.organisme}, ${pr.source?.date}), sur quelle période et quel périmètre. Le détail est juste en dessous.`, preuve: pr, conseil: orgs.length > 1 ? `Montre que plusieurs organismes vont dans le même sens (${orgs.slice(0, 3).join(', ')}), et dis honnêtement les limites. Ne réponds pas « les experts l’ont dit ».` : 'Une seule source dans la bibliothèque : explique sa méthode et ses limites, et propose de chercher ensemble une seconde source (mode connecté).', complement: 'Quelle source accepterais-tu, même si elle te donnait tort ?', utilise: pr.index };
    }
    case 'causes':
      return { ...base, titre: 'D’accord sur le constat, pas sur les causes', texte: `On est d’accord sur le constat, c’est déjà beaucoup. Sur les causes, voilà ce qu’on sait : ${fiche.explication || fiche.contexte}`, conseil: 'Sépare le constat (acquis) des causes (à discuter) ; demande quelle cause lui paraît la plus importante et pourquoi.', complement: 'D’après toi, qu’est-ce qui explique le plus ce problème ?', question: 'D’après toi, qu’est-ce qui explique le plus ce problème ?' };
    case 'solution': {
      const obj = (fiche.contre_arguments || []).find((o, k) => !s.objectionsVues.includes(k));
      return { ...base, titre: 'D’accord sur le problème, pas sur la solution', texte: 'On est d’accord qu’il y a un problème. On peut ne pas être d’accord sur la solution, c’est normal : regardons les options et leurs limites.', conseil: `Discute des solutions comme d’un choix de valeurs, en reconnaissant leurs limites${fiche.limites?.[0] ? ` (par exemple : ${fiche.limites[0]})` : ''}.`, complement: obj ? `Objection probable : « ${obj.objection} » — ${obj.reponse}` : null, objection: obj ? (fiche.contre_arguments || []).indexOf(obj) : null };
    }
    case 'hesite':
      return { ...base, titre: 'Elle hésite : propose des pistes, pas une conclusion', texte: 'Il y a plusieurs façons de regarder la question : les chiffres, l’histoire, les conséquences concrètes. Prends le temps.', conseil: `Reconnais ce qu’on ne sait pas${fiche.limites?.[0] ? ` (${fiche.limites[0]})` : ''} et laisse-la choisir l’angle qui lui parle.`, complement: 'Qu’est-ce qui te fait hésiter ?', question: 'Qu’est-ce qui te fait hésiter ?' };
    case 'diversion':
      return { ...base, titre: deja ? 'Elle change encore de sujet' : 'Elle a changé de sujet', texte: deja ? 'D’accord, parlons de ton sujet. On reviendra au premier une autre fois.' : 'On parlait de ce point précis. Je veux bien parler de l’autre sujet, mais d’abord : est-ce qu’on est d’accord sur ce premier fait ?', conseil: deja ? 'Ne t’acharne pas : accepte le nouveau sujet et cherche une fiche dessus.' : 'Recentre une fois, calmement. Si elle insiste, accepte de changer de sujet.' };
    case 'concede':
      return { ...base, titre: 'Elle a reconnu un point : consolide sans triompher', texte: 'C’est déjà un vrai point commun entre nous. Le reste, on peut y réfléchir chacun de notre côté.', conseil: 'Salue l’ouverture, ne demande pas davantage tout de suite : un petit pas qui dure vaut mieux qu’une victoire forcée.', complement: restantesQ[0] || null, question: restantesQ[0] || null };
    case 'fin':
    default:
      return { ...base, titre: 'La discussion est terminée', texte: 'Merci d’en avoir parlé. On n’est pas forcément d’accord, mais je suis content qu’on ait pu en discuter. Je t’envoie la source si tu veux.', conseil: 'Termine sur le lien, pas sur le désaccord. Tu peux enregistrer cet argumentaire pour la prochaine fois.' };
  }
}

/** Questions du questionnaire qui changeraient le plus la réponse, compte tenu de ce qui est déjà renseigné. */
export function questionsUtiles(fiches, profil, { max = 3 } = {}) {
  const base = nettoyerProfil(profil);
  const fp = (pl) => JSON.stringify([pl.approche, pl.entree, pl.detail, pl.conclusion, pl.ton, pl.preuves.map((x) => x.index), pl.ordre]);
  const ref = fiches.slice(0, 6);
  const res = [];
  for (const d of INTERLOCUTEUR) {
    if (!base.inconnu && base[d.id]) continue;
    let changes = 0;
    for (const [k] of d.options) {
      const p = { ...(base.inconnu ? {} : base), [d.id]: d.multi ? [k] : k };
      for (const f of ref) for (const m of ['gagner', 'convaincre']) if (fp(planifier(f, { profil: p, mode: m })) !== fp(planifier(f, { profil: base, mode: m }))) changes += 1;
    }
    res.push({ id: d.id, label: d.label, impact: changes / (d.options.length * ref.length * 2) });
  }
  return res.sort((a, b) => b.impact - a.impact).slice(0, max);
}
