// Accompagnateur de conversation (MODE AUTONOME : règles explicites, sans modèle d'IA).
//
// Boucle : l'utilisateur rapporte la réaction de son interlocuteur → le moteur l'analyse à la lumière de
// tout l'historique → il propose la prochaine intervention → et ainsi de suite, SANS LIMITE de tours.
// Seul l'utilisateur termine la conversation (bouton « Conversation terminée »).
//
// Garde-fous :
// - aucun fait, chiffre ou source n'est créé : tout vient des fiches vérifiées ;
// - ce que l'utilisateur rapporte (« propos rapportés ») est stocké séparément des hypothèses du profil
//   et des faits de la bibliothèque ;
// - l'analyse d'un message est une indication approximative fondée sur des mots-clés, corrigeable.
//
// NB : tous les noms de haut niveau sont préfixés (cv…, CV_…) car l'aperçu concatène les modules.
import { kbMatch, kbTokens, kbNormalize } from './kbsearch.js';
import { analyserPhrase, conceptsFiche, AN_SUJETS_PORTEURS } from './analyse.js';
import { fichesLiees } from './composer.js';
import { nettoyerProfil, resumeProfil } from './profile.js';

export const CV_VERSION = 1;
const CV_MAX_TEXTE = 1000; // un propos rapporté est tronqué au-delà (stockage local et envoi au serveur)

/** Types de réactions reconnus (libellés présentés comme une lecture approximative). */
export const CV_TYPES = {
  source: 'Demande une source',
  chiffre: 'Conteste un chiffre ou une méthode',
  objection: 'Objection nouvelle',
  objection_connue: 'Objection déjà discutée',
  partiel_causes: 'D’accord sur le constat, pas sur les causes',
  partiel_solution: 'D’accord sur le problème, pas sur la solution',
  partiel: 'Désaccord partiel',
  reconnaissance: 'Reconnaît un point',
  sujet: 'Change de sujet',
  deplacement: 'Déplace la discussion vers un autre argument',
  provocation: 'Provocation',
  incomprehension: 'Incompréhension',
  hesitation: 'Hésitation',
  evolution: 'Son avis semble évoluer',
  essoufflement: 'La conversation s’essouffle',
  conclusion: 'Veut clore la discussion',
  braque: 'Se braque',
  desaccord: 'N’est pas d’accord',
  aide: 'Tu ne sais pas quoi répondre',
  autre: 'Nouvel argument',
};

/** Raccourcis facultatifs de l'interface (ils complètent la saisie libre, ne la remplacent pas). */
export const CV_RACCOURCIS = [
  ['source', 'Demande une source'],
  ['desaccord', 'N’est pas d’accord'],
  ['reconnaissance', 'Reconnaît un point'],
  ['sujet', 'Change de sujet'],
  ['braque', 'Se braque'],
  ['aide', 'Je ne sais pas quoi répondre'],
];

const CV_FICHE_SCIENCE = {
  source: 'sci-desinformation-confiance', chiffre: 'sci-desinformation-confiance', objection: 'sci-identite-sociale', objection_connue: 'sci-persuasion-modeste',
  partiel_causes: 'sci-entretien-motivationnel', partiel_solution: 'sci-valeurs-morales', partiel: 'sci-entretien-motivationnel', reconnaissance: 'sci-dissonance',
  sujet: 'sci-deliberation', deplacement: 'sci-deliberation', provocation: 'sci-polarisation-groupe', incomprehension: 'sci-autonomie', hesitation: 'sci-autonomie', evolution: 'sci-persuasion-modeste',
  essoufflement: 'sci-reactance', conclusion: 'sci-autonomie', braque: 'sci-reactance', desaccord: 'sci-raisonnement-motive', aide: 'sci-entretien-motivationnel', autre: 'sci-raisonnement-motive',
};

// ─── Détection (mots-clés, texte normalisé sans accents) ─────────────────────
const CV_RE = {
  provocation: /(gauchiste|gauchos|bobo|wokiste|\bwoke\b|islamo|facho|connard|debile|abruti|crétin|cretin|\bmdr\b|\blol\b|ptdr|ta gueule|degage|va vivre (a|en)|retourne (a|en)|bisounours|moralisat)/,
  braque: /(ca suffit|arrete (avec|de)|lache[- ]moi|tu me saoules|tu me soules|tu me fatigues|j en ai marre|laisse tomber|change de disque|tu m enerves|on va se facher|tu vas pas m apprendre)/,
  conclusion: /(on en reste la|restons[- ]en la|on verra bien|on ne sera jamais d accord|on sera jamais d accord|on passe a autre chose|parlons d autre chose|bon,? on arrete|on arrete la)/,
  reconnaissance: /(tu as raison|t as raison|c est (vrai|juste|pas faux)|je (te l )?(reconnais|l accorde|te l accorde)|admettons|d accord (sur|pour) (ce point|ca)|ok pour ca|je (ne )?savais pas|bon point|effectivement)/,
  mais: /\b(mais|par contre|cependant|n empeche|neanmoins|pourtant|reste que)\b/,
  causes: /(cause|pourquoi|a cause|la faute|responsable|explique)/,
  solution: /(solution|que proposes|tu proposes|vous proposez|faire quoi|on fait quoi|programme|mesure|alternative|qu est ce qu on fait)/,
  evolution: /(je n y avais pas pense|j y avais pas pense|ca se tient|interessant|je vais (regarder|verifier|y reflechir|me renseigner)|vu comme ca|ca m interroge|peut[- ]etre que tu as raison|ca me fait reflechir|je reconnais que je)/,
  chiffre: /(chiffre|statisti|\bstats?\b|truque|manipul|bidon|sondage|pourcentage|%|on peut faire dire|ment(ent)? |mal compte|comptent pas|calcul|methodolog|definition)/,
  source: /(source|preuve|prouve|ou (est[- ]ce que )?tu as vu|d ou tu (sors|tiens)|qui dit ca|\blien\b|etude|reference|tu l as lu ou|ou c est ecrit|montre[- ]moi)/,
  incomprehension: /(je (ne )?comprends? pas|je (ne )?vois pas|c est quoi|ca veut dire quoi|qu est[- ]ce que ca veut dire|explique|pas clair|quel rapport)/,
  hesitation: /(je (ne )?sais pas|peut[- ]etre|faut voir|pas sur|j hesite|ca depend|mouais|je suis partage|pourquoi pas)/,
  essoufflement: /^\W*(ouais|ouai|ouaip|bof|ok|okay|mouais|si tu veux|bref|bon|m+h*|hm+|pf+|on verra|c est ca|oui oui|ah)\W*$/,
  desaccord: /(faux|pas vrai|n importe quoi|pas d accord|\bnon\b|mensonge|tu racontes|c est pas ca|ca ne prouve rien|ca prouve rien|propagande|foutaise|j y crois pas|je n y crois pas|tu reves|naif)/,
  // rejet explicite de l'argument précédent : « peu importe les chiffres, … »
  rebond: /(peu importe|qu importe|on s en fout|on s en fiche|je m en fiche|je m en fous|osef|la n est pas la question|le probleme c est pas|le vrai probleme|meme si|admettons mais|et alors|ca change rien|ca ne change rien)/,
  sujet: /(et (l |les |le |la )\w+ alors|parlons (de|plutot)|de toute facon|au fait|et sinon|et (puis )?(l |les )immigr|et (les|le) (impots|chomage|retraites|police))/,
};

const cvNorm = (t) => ` ${kbNormalize(t).replace(/[^a-z0-9%?! ]+/g, ' ').replace(/\s+/g, ' ').trim()} `;
const cvStemSet = (t) => new Set(kbTokens(t).map((x) => x.slice(0, 6)));
const cvSimilarite = (a, b) => {
  const A = cvStemSet(a);
  const B = cvStemSet(b);
  if (!A.size || !B.size) return { communs: 0, ratio: 0, couverture: 0 };
  let n = 0;
  for (const x of A) if (B.has(x)) n += 1;
  return { communs: n, ratio: n / Math.min(A.size, B.size), couverture: n / Math.max(A.size, B.size) };
};
const cvPremierePhrase = (t) => { const m = String(t || '').match(/^.*?[.!?](\s|$)/); return (m ? m[0] : String(t || '')).trim(); };
const cvCle = (ficheId, i) => `${ficheId}#${i}`;

function cvSource(fiche, fait) {
  const s = fiche.sources?.[fait.source];
  return s ? { titre: s.titre, organisme: s.organisme, date: s.date_publication, url: s.url, type: s.type || null, consultee: Boolean(s.consultee) } : null;
}

function cvPreuve(fiche, i) {
  const f = fiche.faits[i];
  const s = cvSource(fiche, f);
  return {
    fiche_id: fiche.id, index: i, texte: f.fait, chiffre: f.chiffre || null, periode: f.periode || null, perimetre: f.perimetre || null,
    explication: f.explication || null, source: s,
    methode: [f.periode && `Période : ${f.periode}`, f.perimetre && `Périmètre : ${f.perimetre}`, s && `Source : ${s.organisme}${s.type ? ` (${s.type})` : ''}, ${s.date}`].filter(Boolean).join(' · '),
  };
}

// ─── État ──────────────────────────────────────────────────────────────────
/** Nouvelle conversation, sur un contexte séparé (aucun élément d'une conversation précédente). */
export function nouvelleConversation(fiche, { mode = 'gagner', profil = {}, question = null, infos = [], dejaAvances = [] } = {}) {
  const now = new Date().toISOString();
  return {
    version: CV_VERSION,
    id: `cv-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 7)}`,
    debut: now,
    sujet: { fiche_id: fiche.id, affirmation: fiche.affirmation, question: question || null },
    mode: mode === 'convaincre' ? 'convaincre' : 'gagner',
    hypotheses: nettoyerProfil(profil), // hypothèses de l'utilisateur sur la personne : JAMAIS des faits
    infos: infos.slice(0, 10).map((x) => String(x).slice(0, 300)), // informations données par l'utilisateur
    courante: fiche.id,
    fiches: [fiche.id],
    tours: [], // { n, message (propos rapporté), raccourci, analyse, intervention, date }
    memoire: {
      arguments: dejaAvances.map((i) => ({ fiche_id: fiche.id, index: i, texte: fiche.faits[i]?.fait, tour: 0 })).filter((x) => x.texte),
      sources: [], // { url, titre, organisme, date, tour }
      sources_detaillees: [], // urls dont la méthode a déjà été expliquée
      objections: [], // { texte (rapporté), fiche_id, index|null, traitee, tour }
      accords: [], // { texte, tour }
      contestes: [], // { texte, tour, resolu }
      questions: [],
      textes: [], // empreintes des interventions déjà proposées (anti-répétition)
      reactions: [], // { tour, type, apres (dernier élément présenté) }
      incertitudes: [],
      corrections: [], // corrections d'hypothèses par l'utilisateur
    },
    resume: '',
    terminee: false,
    bilan: null,
  };
}

/** Correction des hypothèses en cours de route (tracée, sans effacer l'historique). */
export function corrigerHypotheses(conv, profil) {
  const avant = resumeProfil(conv.hypotheses);
  conv.hypotheses = nettoyerProfil(profil);
  conv.memoire.corrections.push({ tour: conv.tours.length, avant, apres: resumeProfil(conv.hypotheses) });
  conv.resume = resumeConversation(conv);
  return conv;
}

const cvDernierArgument = (conv) => conv.memoire.arguments[conv.memoire.arguments.length - 1] || null;
const cvFiche = (lib, id) => lib.find((f) => f.id === id) || null;
/** Deux fiches du même domaine : même volet et même sous-thème, ou une rubrique commune. */
const cvMemeDomaine = (a, b) => Boolean(a && b && a.volet === b.volet && ((a.sous_theme && a.sous_theme === b.sous_theme) || (a.rubriques || []).some((r) => (b.rubriques || []).includes(r))));

// ─── Analyse d'un propos rapporté ─────────────────────────────────────────
/**
 * Lecture approximative du message, à la lumière de l'historique.
 * Renvoie { type, secondaires, fiche_sujet, objection, fait_vise, indices, approximatif: true }.
 */
export function analyserMessage(conv, message, { raccourci = null, bibliotheque = [] } = {}) {
  const t = cvNorm(message);
  const brut = String(message || '');
  const courante = cvFiche(bibliotheque, conv.courante);
  const thematiques = bibliotheque.filter((f) => f.type !== 'science');
  const res = { type: 'autre', secondaires: [], fiche_sujet: null, objection: null, fait_vise: null, indices: [], approximatif: true, message: brut.slice(0, 300) };
  const ind = (x) => res.indices.push(x);

  // objection répertoriée dans la fiche courante (ou une fiche déjà parcourue)
  let meilleure = null;
  if (brut.trim()) {
    for (const id of conv.fiches) {
      const f = cvFiche(bibliotheque, id);
      (f?.contre_arguments || []).forEach((o, k) => {
        const s = cvSimilarite(brut, o.objection);
        if (s.communs >= 3 || (s.communs >= 2 && s.couverture >= 0.4)) {
          if (!meilleure || s.couverture > meilleure.couv) meilleure = { fiche_id: f.id, index: k, ratio: s.ratio, couv: s.couverture };
        }
      });
    }
  }
  // fait visé par un chiffre cité
  const nums = brut.match(/\d[\d\s.,]*\d|\d/g) || [];
  if (nums.length && courante) {
    const n0 = nums.map((n) => n.replace(/\s/g, ''));
    const k = courante.faits.findIndex((f) => n0.some((n) => `${f.fait} ${f.chiffre || ''}`.replace(/\s/g, '').includes(n)));
    if (k >= 0) res.fait_vise = k;
  }
  if (res.fait_vise === null && courante && brut.trim()) {
    let best = null;
    courante.faits.forEach((f, k) => { const s = cvSimilarite(brut, `${f.fait} ${f.chiffre || ''}`); if (s.communs >= 2 && (!best || s.communs > best.c)) best = { k, c: s.communs }; });
    if (best) res.fait_vise = best.k;
  }
  // nouveau sujet : une autre fiche correspond nettement
  const apresRebond = CV_RE.rebond.test(t) ? brut.replace(/^.*?(peu importe|qu['’]importe|on s['’]en (fout|fiche)|je m['’]en (fiche|fous)|osef|même si[^,]*,|admettons,? mais|et alors|ça (ne )?change rien)[^,.;:!?]*[,.;:!?]?/i, '') : brut;
  if (brut.trim().length > 8) {
    // 1. analyse argumentative (concepts → argument → fiche qui y répond vraiment) ;
    // 2. à défaut d'argument reconnu, correspondance textuelle (comportement antérieur).
    const an = analyserPhrase(apresRebond.trim().length > 8 ? apresRebond : brut, { bibliotheque: thematiques, mode: conv.mode, contexte: courante ? conceptsFiche(courante).filter((c) => AN_SUJETS_PORTEURS.includes(c)) : [] });
    res.lecture_phrase = { arguments: an.arguments.map((a) => ({ id: a.id, label: a.label, fiche: a.fiche?.id || null, lacune: a.lacune })), emotions: an.emotions.map((e) => ({ id: e.id, label: e.label, reponse: e.reponse })), procedes: an.procedes.map((p) => ({ id: p.id, label: p.label, question: p.question })) };
    const surCourante = an.arguments.some((a) => a.fiche?.id === conv.courante);
    const nouveau = an.arguments.find((a) => a.fiche && a.fiche.id !== conv.courante && a.pertinence === 'directe');
    if (an.arguments.length && an.arguments.some((a) => a.id !== 'texte')) {
      if (nouveau && !surCourante) res.fiche_sujet = nouveau.fiche.id;
      else if (!surCourante && an.arguments.every((a) => a.lacune)) res.lacune_sujet = an.arguments[0].label;
    } else {
      const m = kbMatch(thematiques, apresRebond.trim().length > 8 ? apresRebond : brut);
      const top = m.find((x) => x.fiche.id !== conv.courante);
      const courTop = m.find((x) => x.fiche.id === conv.courante);
      const indice = CV_RE.sujet.test(t);
      if (top && (top.force === 'forte' || top.score >= 6 || (indice && top.score >= 3)) && (!courTop || top.score > courTop.score + 2)) res.fiche_sujet = top.fiche.id;
    }
  }

  const precType = [...conv.tours].reverse().find((x) => x.analyse && !['aide', 'autre'].includes(x.analyse.type))?.analyse.type;
  if (raccourci && CV_TYPES[raccourci]) {
    res.type = raccourci;
    ind('raccourci choisi');
  } else if (precType && brut.trim().length < 40 && !CV_RE.source.test(t) && !CV_RE.chiffre.test(t) && /^\s*(encore|(et )?(une|un) (autre|troisieme|deuxieme|seconde|quatrieme|de plus)|autre chose|et alors|et apres|et ensuite)\b/.test(t.trim())) {
    res.type = precType === 'objection' ? 'objection_connue' : precType; ind('relance de la même demande');
  } else if (!brut.trim()) {
    res.type = 'aide';
  } else if (CV_RE.rebond.test(t) && res.fiche_sujet) {
    res.type = 'deplacement'; ind('argument précédent écarté au profit d’un autre');
  } else if (CV_RE.provocation.test(t) || (brut.replace(/[^A-ZÀ-Ý]/g, '').length > 12 && brut.replace(/[^A-ZÀ-Ý]/g, '').length / brut.replace(/[^A-Za-zÀ-ÿ]/g, '').length > 0.6) || /!!!/.test(brut)) {
    res.type = 'provocation'; ind('ton provocateur ou insultant');
  } else if (CV_RE.braque.test(t)) {
    res.type = 'braque'; ind('signal d’agacement');
  } else if (CV_RE.conclusion.test(t)) {
    res.type = 'conclusion'; ind('souhaite clore');
  } else if (CV_RE.evolution.test(t)) {
    res.type = 'evolution'; ind('ouverture exprimée');
  } else if ((CV_RE.reconnaissance.test(t) || /\bd accord\b/.test(t)) && CV_RE.mais.test(t) && !/pas d accord/.test(t)) {
    res.type = /constat/.test(t) || CV_RE.causes.test(t) ? 'partiel_causes' : CV_RE.solution.test(t) || /probleme/.test(t) ? 'partiel_solution' : 'partiel';
    ind('accord partiel suivi d’une réserve');
  } else if (CV_RE.reconnaissance.test(t)) {
    res.type = 'reconnaissance'; ind('reconnaissance d’un point');
  } else if (/probleme/.test(t) && CV_RE.solution.test(t)) {
    res.type = 'partiel_solution'; ind('problème admis, solution contestée');
  } else if (CV_RE.chiffre.test(t) || (res.fait_vise !== null && CV_RE.desaccord.test(t))) {
    res.type = 'chiffre'; ind('mise en cause d’un chiffre ou d’une méthode');
  } else if (CV_RE.source.test(t)) {
    res.type = 'source'; ind('demande de source');
  } else if (CV_RE.incomprehension.test(t)) {
    res.type = 'incomprehension'; ind('demande d’explication');
  } else if (CV_RE.essoufflement.test(t) || brut.trim().length < 6) {
    res.type = 'essoufflement'; ind('réponse très courte');
  } else if (CV_RE.hesitation.test(t)) {
    res.type = 'hesitation'; ind('hésitation exprimée');
  } else if (courante && cvSimilarite(brut, courante.affirmation).couverture >= 0.5 && cvSimilarite(brut, courante.affirmation).couverture >= (meilleure?.couv || 0)) {
    res.type = 'desaccord'; res.insiste = true; ind('reprend l’affirmation de départ');
  } else if (meilleure) {
    res.type = conv.memoire.objections.some((o) => o.fiche_id === meilleure.fiche_id && o.index === meilleure.index && o.traitee) ? 'objection_connue' : 'objection';
    ind('objection répertoriée dans la bibliothèque');
  } else if (res.fiche_sujet && cvMemeDomaine(courante, cvFiche(bibliotheque, res.fiche_sujet))) {
    res.type = 'deplacement'; ind('nouvel argument dans le même domaine');
  } else if (res.fiche_sujet || CV_RE.sujet.test(t)) {
    res.type = 'sujet'; ind('nouveau sujet');
  } else if (CV_RE.desaccord.test(t)) {
    res.type = 'desaccord'; ind('désaccord exprimé');
  } else {
    res.type = 'autre'; ind('argument non répertorié');
  }
  if (meilleure && !res.insiste && ['desaccord', 'autre', 'partiel', 'sujet'].includes(res.type)) {
    res.secondaires.push(res.type);
    res.type = conv.memoire.objections.some((o) => o.fiche_id === meilleure.fiche_id && o.index === meilleure.index && o.traitee) ? 'objection_connue' : 'objection';
  }
  if (meilleure) res.objection = { fiche_id: meilleure.fiche_id, index: meilleure.index };
  if (res.type.startsWith('partiel') || res.type === 'reconnaissance') {
    const coupe = brut.split(/\b(?:mais|par contre|cependant|n['’]emp[eê]che|néanmoins|neanmoins|pourtant)\b/i);
    res.accorde = coupe[0].replace(/^[\s,.;:!?-]*(ok|oui|bon|bah|ben)?[\s,]*/i, '').replace(/[\s,;:.!?-]+$/, '').trim().slice(0, 200) || null;
    res.reserve = coupe.length > 1 ? coupe.slice(1).join(' ').replace(/^[\s,]+/, '').trim().slice(0, 200) : null;
    if (res.reserve && res.reserve.length > 8) {
      const m2 = kbMatch(thematiques, res.reserve).find((x) => x.fiche.id !== conv.courante && x.score >= 3);
      if (m2) { res.fiche_sujet = m2.fiche.id; if (!res.secondaires.includes('sujet')) res.secondaires.push('sujet'); }
    }
  }
  if (res.fiche_sujet && res.type !== 'sujet') res.secondaires.push('sujet');
  if (res.type === 'sujet' && !res.fiche_sujet && raccourci !== 'sujet') ind('aucune fiche trouvée pour ce nouveau sujet');
  return res;
}

// ─── Choix du contenu (sans répétition) ─────────────────────────────────────
/** Fiches où chercher, dans l'ordre : courante, déjà parcourues, voisines. */
function cvFichesOrdre(conv, lib) {
  const courante = cvFiche(lib, conv.courante);
  const ids = [conv.courante, ...conv.fiches.filter((x) => x !== conv.courante)];
  const voisines = courante ? fichesLiees(courante, lib).filter((f) => f.volet === courante.volet).slice(0, 3).map((f) => f.id) : [];
  return [...new Set([...ids, ...voisines])].map((id) => cvFiche(lib, id)).filter(Boolean);
}

function cvProchainFait(conv, lib, { prefere = null, exclureVoisines = true } = {}) {
  const deja = new Set(conv.memoire.arguments.map((a) => cvCle(a.fiche_id, a.index)));
  const fiches = cvFichesOrdre(conv, lib).filter((f) => !exclureVoisines || conv.fiches.includes(f.id));
  for (const f of fiches) {
    const libres = f.faits.map((x, i) => i).filter((i) => !deja.has(cvCle(f.id, i)));
    if (!libres.length) continue;
    const score = (i) => {
      const x = f.faits[i];
      let s = 0;
      if (prefere === 'chiffre' && x.chiffre) s += 2;
      if (prefere === 'court' && x.fait.length < 170) s += 2;
      if (prefere === 'source' && f.sources?.[x.source]?.url && !conv.memoire.sources.some((y) => y.url === f.sources[x.source].url)) s += 3;
      return s;
    };
    const i = [...libres].sort((a, b) => score(b) - score(a) || a - b)[0];
    return { fiche: f, index: i, preuve: cvPreuve(f, i), voisine: !conv.fiches.includes(f.id) };
  }
  return null;
}

function cvProchaineQuestion(conv, lib, extra = []) {
  const f = cvFiche(lib, conv.courante);
  const pool = [...extra, ...(f?.questions || []), 'Qu’est-ce qui te ferait changer d’avis, toi ?', 'Qu’est-ce qui compte le plus pour toi dans cette question ?', 'Sur quoi est-ce qu’on est d’accord, finalement ?', 'Comment tu t’es fait ton avis là-dessus ?'];
  return pool.find((q) => !conv.memoire.questions.includes(q)) || null;
}

const cvVariante = (liste, n) => liste[n % liste.length];

/** Texte de repli tiré de la fiche courante (réponse courte, explication…), jamais deux fois le même. */
function cvRepli(conv, fiche) {
  const A = fiche?.argumentaires || {};
  const cands = [['court', A.court], ['explication', cvPremierePhrase(fiche?.explication)], ['moyen', cvPremierePhrase(A.moyen)], ['resume', cvPremierePhrase(fiche?.resume)]];
  for (const [k, txt] of cands) if (txt && !conv.memoire.textes.includes(`repli:${fiche.id}:${k}`)) return { texte: txt, marque: `repli:${fiche.id}:${k}` };
  return null;
}
const cvCompte = (conv, type) => conv.memoire.reactions.filter((r) => r.type === type).length;
const cvDire = (conv, gagner, convaincre) => (conv.mode === 'gagner' ? gagner : convaincre);

// ─── Intervention ─────────────────────────────────────────────────────────
function cvConstruire(conv, analyse, lib) {
  const type = analyse.type;
  const n = cvCompte(conv, type); // nombre de fois où ce type est déjà apparu (avant ce tour)
  const courante = cvFiche(lib, conv.courante);
  const A = courante?.argumentaires || {};
  const dernier = cvDernierArgument(conv);
  const out = { type, lecture: CV_TYPES[type], texte: '', strategie: '', preuve: null, question: null, options: [], objection: null, source_detaillee: null, fiche_science: CV_FICHE_SCIENCE[type], conclusion_possible: false, voisine: false, epuise: false };
  out.marques = [];
  // élément suivant : un fait non encore présenté (fiches du fil), sinon un texte de la fiche courante
  // pas encore utilisé, sinon (si autorisé) un fait d'une fiche voisine, signalé comme tel.
  const avecFait = (prefere, { voisine = true } = {}) => {
    const x = cvProchainFait(conv, lib, { prefere });
    if (x) { out.preuve = x.preuve; return x; }
    const r = cvRepli(conv, courante);
    if (r) { out.marques.push(r.marque); return { preuve: { texte: r.texte }, repli: true }; }
    if (voisine) {
      const v = cvProchainFait(conv, lib, { prefere, exclureVoisines: false });
      if (v) {
        out.preuve = v.preuve; out.voisine = true; out.fiche_voisine = { id: v.fiche.id, affirmation: v.fiche.affirmation };
        return { ...v, preuve: { ...v.preuve, texte: `sur un point voisin (« ${v.fiche.affirmation} ») : ${v.preuve.texte}` } };
      }
    }
    return null;
  };
  switch (type) {
    case 'source': {
      // une source pas encore donnée ; sinon la source du dernier fait, avec ce qu'elle démontre
      let x = null;
      if (dernier) {
        const f = cvFiche(lib, dernier.fiche_id);
        const s = f && cvSource(f, f.faits[dernier.index]);
        if (s && !conv.memoire.sources.some((y) => y.url === s.url)) x = { fiche: f, index: dernier.index, preuve: cvPreuve(f, dernier.index) };
      }
      if (!x) x = cvProchainFait(conv, lib, { prefere: 'source' });
      if (x && !conv.memoire.sources.some((y) => y.url === x.preuve.source?.url)) {
        const p = x.preuve;
        const f = x.fiche;
        out.preuve = p;
        out.voisine = !conv.fiches.includes(f.id);
        out.texte = cvDire(conv, `La source : ${p.source.organisme}, « ${p.source.titre} » (${p.source.date}). Elle montre ceci : ${p.texte}`, `Bien sûr, c’est normal de vouloir vérifier. Ça vient de cette source : ${p.source.organisme}, « ${p.source.titre} » (${p.source.date}). Ce document montre ceci : ${p.texte}`);
        out.strategie = `Donne le lien, explique ce que la source démontre${p.explication ? ` (${p.explication})` : ''} et ce qu’elle ne démontre pas${f.limites?.[0] ? ` : ${f.limites[0]}` : '.'}`;
      } else {
        const toutes = conv.memoire.sources.map((s) => `${s.organisme} (${s.date})`).join(', ');
        out.epuise = true;
        const s0 = conv.memoire.sources[0];
        out.texte = !toutes ? 'Je n’ai pas de source vérifiée de plus sur ce point précis. Et toi, sur quelle source t’appuies-tu ?' : cvVariante([
          `Je t’ai donné toutes les sources dont je dispose sur ce point : ${toutes}. Laquelle as-tu pu regarder ? Et toi, sur quelle source t’appuies-tu ?`,
          'Je n’ai vraiment pas d’autre source vérifiée sous la main. Quelle source te semblerait fiable, à toi ? On peut la regarder ensemble.',
          `Plutôt que d’empiler les sources, on peut en regarder une ensemble, tranquillement : « ${s0.titre} » (${s0.organisme}).`,
        ], n);
        out.strategie = 'La bibliothèque ne contient pas d’autre source vérifiée : ne cite rien de plus. Retourne la question, ou utilise le mode connecté pour une recherche fraîche.';
      }
      break;
    }
    case 'chiffre': {
      let idx = analyse.fait_vise;
    if (idx === null) {
      const nm = kbNormalize(analyse.message || '');
      const k = courante.faits.findIndex((f) => { const o = courante.sources?.[f.source]?.organisme; return o && nm.includes(kbNormalize(o).split(/[ ,(]/)[0]); });
      if (k >= 0) idx = k;
    }
      if (idx === null && dernier && dernier.fiche_id === conv.courante && courante.faits[dernier.index]?.chiffre) idx = dernier.index;
      if (idx === null) idx = courante.faits.findIndex((f) => f.chiffre && !conv.memoire.sources_detaillees.includes(`${courante.id}#${courante.faits.indexOf(f)}`));
      if (idx === null || idx < 0) idx = courante.faits.findIndex((f) => f.chiffre);
      if (idx < 0) {
        out.texte = 'Sur ce point, je ne m’appuie pas sur un chiffre mais sur des faits et des textes. Lequel te paraît faux ?';
        out.strategie = 'La fiche ne contient pas de donnée chiffrée : n’en avance pas.';
        break;
      }
      const p = cvPreuve(courante, idx);
      const cle = `${courante.id}#${idx}`;
      const dejaDetaille = conv.memoire.sources_detaillees.includes(cle);
      const orgs = [...new Set(courante.faits.map((f) => courante.sources?.[f.source]?.organisme).filter(Boolean))];
      out.preuve = p;
      out.source_detaillee = cle;
      out.texte = dejaDetaille
        ? cvDire(conv, `On a déjà regardé comment ce chiffre est construit. Si tu le contestes, dis-moi précisément quoi : la définition, la période ou le périmètre ? Et quelle source donne un autre résultat ?`, `On a déjà regardé ensemble d’où vient ce chiffre. Qu’est-ce qui te gêne précisément : la définition, la période, ou le fait que ce soit une source officielle ? Tu as vu un autre chiffre quelque part ?`)
        : cvDire(conv, `Regardons comment ce chiffre est fabriqué. ${p.methode}.${p.explication ? ` ${p.explication}` : ''}`, `Tu as raison de vouloir comprendre d’où vient un chiffre. ${p.methode}.${p.explication ? ` ${p.explication}` : ''}`);
      out.strategie = `${orgs.length > 1 ? `Plusieurs organismes vont dans le même sens (${orgs.slice(0, 3).join(', ')}). ` : ''}Examine la définition, la période et la méthode ; reconnais honnêtement les limites${courante.limites?.[0] ? ` (${courante.limites[0]})` : ''}.`;
      out.question = dejaDetaille ? null : 'Quelle source accepterais-tu, même si elle te donnait tort ?';
      break;
    }
    case 'objection':
    case 'objection_connue': {
      const ref = analyse.objection;
      const f = ref && cvFiche(lib, ref.fiche_id);
      const o = f?.contre_arguments?.[ref.index];
      if (o && type === 'objection') {
        out.objection = { fiche_id: f.id, index: ref.index, objection: o.objection };
        out.texte = cvDire(conv, `${o.reponse}`, `C’est une vraie question, je la prends au sérieux. ${o.reponse}`);
        out.strategie = 'Objection connue : réponds-y honnêtement, sur le fond, sans la caricaturer. Reconnais ce qui est fondé.';
        if (f.objections_legitimes?.length) out.strategie += ` Point à reconnaître : ${f.objections_legitimes[0]}`;
      } else {
        const x = avecFait();
        out.texte = `On en a déjà parlé${o ? ` (« ${cvPremierePhrase(o.reponse)} »)` : ''}. ${x ? `Un autre élément, alors : ${x.preuve.texte}` : 'Qu’est-ce qui ne te convainc pas dans cette réponse ?'}`;
        out.strategie = 'Ne répète pas la même réponse : demande ce qui ne convainc pas, ou apporte un élément nouveau.';
        out.question = x ? 'Qu’est-ce qui ne te convainc pas dans ce que je t’ai dit ?' : null;
      }
      break;
    }
    case 'partiel_causes': {
      const dejaExpl = conv.memoire.textes.includes('causes:' + courante.id);
      const x = dejaExpl ? avecFait() : null;
      out.texte = dejaExpl
        ? `On est d’accord sur le constat. Sur les causes, un élément de plus : ${x ? x.preuve.texte : 'je n’ai pas d’autre élément vérifié.'}`
        : `On est d’accord sur le constat, c’est déjà beaucoup. Sur les causes, voilà ce qu’on sait : ${courante.explication || courante.contexte || cvPremierePhrase(A.moyen)}`;
      out.marque = 'causes:' + courante.id;
      out.strategie = 'Ne répète pas ce qui est acquis : sépare le constat (acquis) des causes (à discuter), puis demande quelle cause lui paraît la plus importante.';
      out.question = 'D’après toi, qu’est-ce qui explique le plus ce problème ?';
      break;
    }
    case 'partiel_solution': {
      const objSol = (courante.contre_arguments || []).map((o, k) => ({ o, k })).find(({ o, k }) => !conv.memoire.objections.some((y) => y.fiche_id === courante.id && y.index === k) && /solution|propos|financ|cout|coût|programme|mesure|faire/i.test(o.objection));
      out.texte = cvDire(conv, 'On est d’accord qu’il y a un problème : c’est l’essentiel. Sur la solution, il y a plusieurs options, et chacune a des limites ; comparons-les plutôt que de les caricaturer.', 'On est d’accord qu’il y a un problème, et c’est déjà important. Pour la solution, on peut ne pas être d’accord : qu’est-ce que tu proposerais, toi ? On peut comparer.');
      if (objSol) { out.objection = { fiche_id: courante.id, index: objSol.k, objection: objSol.o.objection }; out.complement = `Objection probable : « ${objSol.o.objection} » — ${objSol.o.reponse}`; }
      out.strategie = `Passe du constat à la comparaison des solutions : présente-les comme des choix de valeurs, avec leurs limites${courante.limites?.[0] ? ` (par exemple : ${courante.limites[0]})` : ''}.`;
      out.question = 'Qu’est-ce que tu proposerais, toi, et qu’est-ce qui te paraît le plus réaliste ?';
      break;
    }
    case 'partiel':
    case 'reconnaissance': {
      const contest = conv.memoire.contestes.filter((c) => !c.resolu).slice(-1)[0];
      const x = avecFait();
      const acquis = dernier ? `« ${cvPremierePhrase(dernier.texte)} »` : 'ce point';
      const accorde = analyse.accorde && analyse.accorde.length > 3 ? `« ${analyse.accorde} »` : null;
      const reserve = analyse.reserve && analyse.reserve.length > 3 ? analyse.reserve : null;
      const nf = type === 'partiel' && analyse.fiche_sujet ? cvFiche(lib, analyse.fiche_sujet) : null;
      if (type === 'partiel' && (accorde || reserve)) {
        out.texte = `On est donc d’accord sur une partie${accorde ? ` : ${accorde}` : ''}. ${reserve ? `Sur ton autre point (« ${reserve} »), ` : 'Sur ce qui reste en discussion, '}${nf ? `voici ce qu’on sait : ${nf.argumentaires?.court || cvPremierePhrase(nf.resume)}` : x ? `voici un élément : ${x.preuve.texte}` : 'dis-moi ce qui te paraît le plus discutable.'}`;
        if (nf) {
          if (out.preuve && !x?.repli) { out.preuve = null; }
          out.options = [{ action: 'basculer', fiche_id: nf.id, label: `Approfondir « ${nf.affirmation} »` }, { action: 'rester', label: 'Rester sur le sujet initial' }];
          out.fiche_nouvelle = { id: nf.id, affirmation: nf.affirmation };
        }
      } else out.texte = type === 'reconnaissance'
        ? cvDire(conv, `On est d’accord sur ${acquis}. ${x ? `Alors allons plus loin : ${x.preuve.texte}` : 'C’est un vrai point commun.'}`, `Merci, ça compte. On a au moins ce point commun. ${x ? `Et si on regarde aussi ceci : ${x.preuve.texte}` : 'On peut s’arrêter là-dessus pour aujourd’hui.'}`)
        : `On est donc d’accord sur une partie. Sur ce qui reste en discussion${contest ? ` (« ${cvPremierePhrase(contest.texte)} »)` : ''}, ${x ? `voici un élément : ${x.preuve.texte}` : 'dis-moi ce qui te paraît le plus discutable.'}`;
      out.strategie = 'Ne répète pas ce qui est déjà accepté : prends acte sans triompher et poursuis seulement sur le point encore discuté.';
      out.question = cvProchaineQuestion(conv, lib, type === 'partiel' ? ['Sur quoi exactement est-on encore en désaccord ?'] : []);
      out.conclusion_possible = type === 'reconnaissance' && conv.memoire.accords.length >= 1;
      if (!x) out.epuise = true;
      break;
    }
    case 'sujet': {
      const nf = analyse.fiche_sujet && cvFiche(lib, analyse.fiche_sujet);
      if (nf) {
        out.options = [{ action: 'basculer', fiche_id: nf.id, label: `Répondre sur « ${nf.affirmation} »` }, { action: 'rester', label: 'Revenir au point initial' }];
        out.texte = cvDire(conv, `Sur ce nouveau sujet, réponse courte : ${nf.argumentaires?.court || cvPremierePhrase(nf.resume)} Mais on parlait de « ${conv.sujet.affirmation} » : on termine ce point d’abord ?`, `D’accord, on peut en parler. En deux mots : ${nf.argumentaires?.court || cvPremierePhrase(nf.resume)} Tu veux qu’on revienne ensuite à ce qu’on disait sur « ${conv.sujet.affirmation} » ?`);
        out.strategie = 'Décide : répondre au nouveau sujet (bouton ci-dessous, le contexte initial est conservé) ou revenir au point initial. Un changement de sujet répété peut être une façon d’éviter le premier.';
        out.fiche_nouvelle = { id: nf.id, affirmation: nf.affirmation };
      } else {
        out.texte = cvVariante(['On parlait d’un point précis ; je veux bien parler de l’autre sujet, mais d’abord : est-ce qu’on est d’accord sur ce premier fait ?', 'C’est un autre débat. Je n’ai pas d’élément vérifié dessus ici ; revenons à ce qu’on disait, et on regardera l’autre sujet plus tard.'], n);
        out.strategie = 'Ce nouveau sujet n’est pas dans la bibliothèque : ne réponds pas au hasard. Recentre, ou décris le sujet dans une nouvelle recherche.';
        out.options = [{ action: 'rester', label: 'Revenir au point initial' }];
      }
      break;
    }
    case 'deplacement': {
      // la fiche courante a déjà été basculée vers le nouvel argument (voir repondreConversation)
      const ancienne = analyse.depuis ? cvFiche(lib, analyse.depuis) : null;
      const x = avecFait(conv.mode === 'gagner' ? 'chiffre' : null, { voisine: false });
      const court = A.court || cvPremierePhrase(courante.resume);
      out.texte = cvDire(conv,
        `Tu changes d’argument : on ne parle plus de « ${ancienne?.affirmation || 'ce point'} », mais de « ${courante.affirmation} ». Sur ce nouveau point : ${court}`,
        `D’accord, c’est une autre question : « ${courante.affirmation} ». Elle mérite une vraie réponse. ${court}`);
      if (x?.repli) out.preuve = null;
      out.question = cvProchaineQuestion(conv, lib);
      out.strategie = `L’interlocuteur a déplacé la discussion. Ne reprends pas l’argument précédent : réponds sur le nouveau terrain (${courante.sous_theme || courante.affirmation}), avec les éléments propres à ce sujet, puis pose une question.${courante.objections_legitimes?.length ? ` Point légitime à reconnaître : ${courante.objections_legitimes[0]}` : ''}`;
      if (ancienne) out.options = [{ action: 'basculer', fiche_id: ancienne.id, label: `Revenir à « ${ancienne.affirmation} »` }];
      out.fiche_nouvelle = { id: courante.id, affirmation: courante.affirmation };
      break;
    }
    case 'provocation': {
      const x = avecFait('court', { voisine: false });
      out.texte = cvDire(conv,
        cvVariante([`Je ne vais pas répondre sur ce ton. Sur le fond : ${x ? x.preuve.texte : cvPremierePhrase(A.court)}`, `Les étiquettes ne sont pas des arguments. Un fait : ${x ? x.preuve.texte : cvPremierePhrase(A.court)}`, `Tu peux me traiter de ce que tu veux, ça ne change pas les chiffres : ${x ? x.preuve.texte : cvPremierePhrase(A.court)}`], n),
        cvVariante([`Je sens que ça t’agace. Je ne veux pas qu’on se fâche. Juste un point : ${x ? x.preuve.texte : cvPremierePhrase(A.court)}`, `On peut ne pas être d’accord sans s’envoyer des étiquettes. Ce que je voulais dire : ${x ? x.preuve.texte : cvPremierePhrase(A.court)}`], n));
      out.strategie = 'Réponse ferme et concise, sans escalade : un seul fait, pas d’attaque personnelle, pas de surenchère. Le public éventuel juge le calme.';
      break;
    }
    case 'braque': {
      out.texte = cvVariante([
        A.empathie || 'Je comprends que ça t’agace. On n’est pas obligés d’être d’accord.',
        'On n’est pas obligés d’en parler maintenant. Si tu veux, on reprendra un autre jour.',
        'Je ne cherche pas à avoir le dernier mot. Ce qui compte pour moi, c’est qu’on puisse en parler sans se fâcher.',
        'Dis-moi plutôt ce qui te tient à cœur là-dedans, je t’écoute.',
      ], n);
      out.strategie = n === 0 ? 'Arrête d’ajouter des arguments : reformule son inquiétude, rappelle qu’elle reste libre de son avis.' : 'Nouveau signal d’agacement : propose une pause ou change d’approche (écoute). La conversation reste ouverte : si elle reprend, note ici sa réaction.';
      out.question = n >= 3 ? 'Qu’est-ce qui t’énerve le plus dans ce sujet ?' : null;
      out.conclusion_possible = n >= 1;
      break;
    }
    case 'incomprehension': {
      const dejaCourt = conv.memoire.textes.includes('court:' + courante.id);
      const x = dejaCourt ? avecFait('court') : null;
      out.texte = dejaCourt ? `Autrement dit, plus simplement : ${x ? x.preuve.texte : cvPremierePhrase(courante.explication || courante.resume)}` : `Je reformule plus simplement : ${A.court || cvPremierePhrase(courante.explication)}`;
      out.marque = 'court:' + courante.id;
      out.strategie = 'Mots courants, une idée à la fois, pas de sigles. Vérifie ensuite que c’est clair.';
      out.question = 'Est-ce que c’est plus clair dit comme ça ?';
      break;
    }
    case 'hesitation': {
      out.texte = cvVariante(['Il y a plusieurs façons de regarder la question : les chiffres, l’histoire, les conséquences concrètes. Prends le temps.', 'C’est normal d’hésiter, le sujet est compliqué. Qu’est-ce qui te ferait pencher d’un côté ou de l’autre ?'], n);
      out.strategie = `Reconnais ce qu’on ne sait pas${courante.limites?.[0] ? ` (${courante.limites[0]})` : ''} et laisse-la choisir l’angle qui lui parle. Ne force pas une conclusion.`;
      out.question = cvProchaineQuestion(conv, lib, ['Qu’est-ce qui te fait hésiter ?']);
      break;
    }
    case 'evolution': {
      out.texte = cvVariante(['C’est chouette qu’on ait pu en parler comme ça. Si tu veux, je t’envoie la source pour que tu regardes tranquillement.', 'Prends le temps d’y réfléchir, il n’y a pas d’urgence. On en reparlera si tu veux.'], n);
      out.strategie = 'Valorise l’ouverture sans triompher et sans en demander plus : un petit pas qui dure vaut mieux qu’une victoire forcée. C’est peut-être le bon moment pour conclure.';
      out.conclusion_possible = true;
      break;
    }
    case 'essoufflement': {
      out.texte = cvVariante([`${cvProchaineQuestion(conv, lib) || 'Et toi, qu’est-ce que tu en penses vraiment ?'}`, 'On a déjà pas mal discuté. On peut s’arrêter là pour aujourd’hui, si tu veux.'], n);
      out.strategie = n === 0 ? 'La discussion ralentit : une question légère plutôt qu’un nouvel argument.' : 'La discussion s’essouffle : c’est souvent le bon moment pour conclure en douceur.';
      out.conclusion_possible = n >= 1;
      break;
    }
    case 'conclusion': {
      out.texte = cvDire(conv, 'D’accord, on en reste là. Retiens juste ceci : ' + (dernier ? cvPremierePhrase(dernier.texte) : cvPremierePhrase(A.court)), 'D’accord, on en reste là. Merci d’en avoir parlé avec moi, ça compte.');
      out.strategie = 'Ton interlocuteur veut clore : ne force pas. Tu peux terminer la conversation quand tu veux avec le bouton prévu, ou noter ici si elle reprend.';
      out.conclusion_possible = true;
      break;
    }
    case 'aide': {
      const derniereAnalyse = [...conv.tours].reverse().find((t) => t.analyse && t.analyse.type !== 'aide')?.analyse;
      const x = avecFait();
      const q = cvProchaineQuestion(conv, lib);
      out.texte = x ? cvDire(conv, `Tu peux simplement avancer un fait vérifiable : ${x.preuve.texte}`, `Tu peux lui poser une question, puis glisser un fait : ${q ? `« ${q} » ` : ''}${x.preuve.texte}`) : (q ? `Tu peux lui poser une question ouverte : « ${q} »` : 'Tu peux résumer ce sur quoi vous êtes d’accord, et proposer d’en rester là pour aujourd’hui.');
      out.question = x ? q : null;
      out.strategie = derniereAnalyse ? `Dernière réaction lue : ${CV_TYPES[derniereAnalyse.type].toLowerCase()}. Quand on ne sait pas quoi répondre, une question vaut mieux qu’un argument improvisé.` : 'Une question vaut mieux qu’un argument improvisé.';
      if (!x && !q) out.epuise = true;
      break;
    }
    case 'desaccord': {
      const x = avecFait(conv.mode === 'gagner' ? 'chiffre' : null);
      out.texte = cvDire(conv,
        x ? cvVariante([`Regarde ce fait, il est vérifiable : ${x.preuve.texte}`, `Alors un autre élément : ${x.preuve.texte}`, `Ce n’est pas mon opinion, c’est documenté : ${x.preuve.texte}`], n) : 'Sur quoi exactement n’es-tu pas d’accord : le chiffre, la source ou la conclusion ?',
        x ? cvVariante([`Je comprends. Sur quoi exactement n’es-tu pas d’accord ? Moi, je m’appuie sur ceci : ${x.preuve.texte}`, `D’accord, on n’est pas du même avis. Je te propose juste de regarder ceci : ${x.preuve.texte}`], n) : 'Je comprends. Qu’est-ce qui te fait dire ça ? J’aimerais comprendre ton point de vue.');
      out.strategie = 'Fais préciser le désaccord (chiffre, source ou conclusion ?) avant d’empiler les arguments.';
      out.question = cvProchaineQuestion(conv, lib, ['Sur quoi exactement n’es-tu pas d’accord : le chiffre, la source ou la conclusion ?']);
      if (!x) out.epuise = true;
      break;
    }
    case 'autre':
    default: {
      const x = avecFait();
      out.texte = cvDire(conv,
        `Ce que tu dis là, je ne peux pas le vérifier tout de suite : tu as une source ? Ce qui est vérifié, en revanche : ${x ? x.preuve.texte : cvPremierePhrase(A.court)}`,
        `C’est intéressant, d’où tu tiens ça ? De mon côté, ce qui est vérifié : ${x ? x.preuve.texte : cvPremierePhrase(A.court)}`);
      out.strategie = 'Cet argument n’est pas répertorié dans la bibliothèque : ne l’accepte ni ne le réfute sans source. Demande d’où il vient ; le mode connecté peut vérifier.';
      out.question = 'D’où tu tiens ça ?';
      out.incertitude = 'Argument non vérifiable hors ligne.';
      break;
    }
  }
  if (out.epuise) {
    out.strategie += ' La bibliothèque n’a plus d’élément nouveau ici : tu peux poser une question, résumer vos points d’accord, lancer une recherche fraîche (mode connecté) ou conclure quand tu le souhaites.';
  }
  if (out.question && out.texte.includes(out.question)) out.question = null;
  return out;
}

/** Anti-répétition : si la même intervention a déjà été proposée, on change d'élément ou de formulation. */
const cvEmpreinte = (o) => kbNormalize(`${o.texte}|${o.preuve ? cvCle(o.preuve.fiche_id, o.preuve.index) : ''}`).replace(/\s+/g, ' ').slice(0, 400);

/**
 * Traite un nouveau propos rapporté et renvoie l'intervention proposée. La conversation reste ouverte.
 * `options` : { raccourci, bibliotheque, force } — `force` contourne la protection contre les doublons.
 */
export function repondreConversation(conv, message, { raccourci = null, bibliotheque = [], force = false } = {}) {
  if (conv.terminee) return { erreur: 'Cette conversation est terminée. Commence-en une nouvelle (contexte séparé).' };
  const msg = String(message || '').slice(0, CV_MAX_TEXTE);
  // protection contre les boucles involontaires : même message envoyé deux fois de suite
  const prec = conv.tours[conv.tours.length - 1];
  if (!force && prec && msg.trim() && cvNorm(prec.message) === cvNorm(msg) && (prec.raccourci || null) === (raccourci || null)) {
    return { doublon: true, message: 'Tu viens d’envoyer exactement le même message. Si c’est bien une nouvelle réaction, confirme.' };
  }
  const analyse = analyserMessage(conv, msg, { raccourci, bibliotheque });
  if (analyse.type === 'deplacement' && analyse.fiche_sujet) {
    analyse.depuis = conv.courante;
    basculerSujet(conv, analyse.fiche_sujet);
  }
  let inter = cvConstruire(conv, analyse, bibliotheque);
  // anti-répétition stricte
  let garde = 0;
  while (conv.memoire.textes.includes(cvEmpreinte(inter)) && garde < 4) {
    garde += 1;
    if (inter.preuve) conv.memoire.arguments.push({ fiche_id: inter.preuve.fiche_id, index: inter.preuve.index, texte: inter.preuve.texte, tour: -1, ecarte: true });
    conv.memoire.reactions.push({ tour: -1, type: analyse.type, fantome: true });
    inter = cvConstruire(conv, analyse, bibliotheque);
  }
  if (conv.memoire.textes.includes(cvEmpreinte(inter))) {
    // dernier recours : une question jamais posée, pour ne jamais proposer deux fois la même chose
    const q = cvProchaineQuestion(conv, bibliotheque) || 'Et si on résumait ensemble ce sur quoi on est d’accord ?';
    inter = { ...inter, texte: `${inter.texte} Tu peux aussi lui demander : « ${q} »`, question: null, relance: q };
  }
  conv.memoire.arguments = conv.memoire.arguments.filter((a) => !a.ecarte);
  conv.memoire.reactions = conv.memoire.reactions.filter((r) => !r.fantome);
  return enregistrerTour(conv, { message: msg, raccourci, analyse, intervention: inter, origine: 'locale' });
}

/** Enregistre un tour (intervention locale ou du serveur) et met à jour la mémoire structurée. */
export function enregistrerTour(conv, { message, raccourci = null, analyse, intervention, origine = 'locale' }) {
  const n = conv.tours.length + 1;
  const m = conv.memoire;
  const dernier = cvDernierArgument(conv);
  const t = analyse.type;
  // réactions et effets sur les points d'accord / contestés
  m.reactions.push({ tour: n, type: t, apres: dernier ? cvCle(dernier.fiche_id, dernier.index) : null });
  if ((t === 'reconnaissance' || t === 'partiel' || t === 'partiel_causes' || t === 'partiel_solution') && (dernier || t !== 'reconnaissance')) {
    const rapporte = analyse.accorde && analyse.accorde.length > 3 ? analyse.accorde : null;
    const texte = rapporte ? `« ${rapporte} »` : t === 'partiel_causes' ? `Le constat : ${conv.sujet.affirmation}` : t === 'partiel_solution' ? 'Il y a un problème à traiter' : dernier?.texte;
    const origine = rapporte ? 'rapporte' : t === 'reconnaissance' ? 'deduit' : 'rapporte';
    if (texte && !m.accords.some((a) => a.texte === texte)) m.accords.push({ texte, tour: n, origine });
    m.contestes.forEach((c) => { if (c.texte === texte) c.resolu = true; });
  }
  if (['desaccord', 'chiffre', 'objection', 'objection_connue', 'partiel', 'partiel_causes', 'partiel_solution', 'autre', 'provocation'].includes(t)) {
    const texte = t === 'partiel_causes' ? 'Les causes du problème' : t === 'partiel_solution' ? 'La solution à apporter' : t === 'partiel' && analyse.reserve ? `« ${analyse.reserve} »` : (t === 'autre' || t === 'objection' || t === 'objection_connue') && message ? `« ${message.slice(0, 200)} »` : dernier?.texte;
    if (texte && !m.contestes.some((c) => c.texte === texte && !c.resolu)) m.contestes.push({ texte, tour: n, resolu: false });
  }
  if ((t === 'objection' || t === 'autre') && message) m.objections.push({ texte: message.slice(0, 300), fiche_id: analyse.objection?.fiche_id || null, index: analyse.objection?.index ?? null, traitee: Boolean(intervention.objection), tour: n });
  if (intervention.objection && t !== 'objection') m.objections.push({ texte: intervention.objection.objection, fiche_id: intervention.objection.fiche_id, index: intervention.objection.index, traitee: true, anticipee: true, tour: n });
  // éléments présentés
  if (intervention.preuve) {
    const p = intervention.preuve;
    if (!m.arguments.some((a) => a.fiche_id === p.fiche_id && a.index === p.index)) m.arguments.push({ fiche_id: p.fiche_id, index: p.index, texte: p.texte, tour: n });
    if (p.source?.url && (t === 'source' || t === 'chiffre' || !m.sources.some((s) => s.url === p.source.url))) {
      if (!m.sources.some((s) => s.url === p.source.url)) m.sources.push({ url: p.source.url, titre: p.source.titre, organisme: p.source.organisme, date: p.source.date, tour: n });
    }
    if (p.fiche_id && !conv.fiches.includes(p.fiche_id)) conv.fiches.push(p.fiche_id);
  }
  if (intervention.source_detaillee && !m.sources_detaillees.includes(intervention.source_detaillee)) m.sources_detaillees.push(intervention.source_detaillee);
  if (intervention.question) m.questions.push(intervention.question);
  if (intervention.relance) m.questions.push(intervention.relance);
  if (intervention.marque) m.textes.push(intervention.marque);
  for (const k of intervention.marques || []) m.textes.push(k);
  if (intervention.incertitude) m.incertitudes.push({ texte: intervention.incertitude, tour: n });
  m.textes.push(cvEmpreinte(intervention));
  const tour = { n, message, raccourci, analyse, intervention, origine, date: new Date().toISOString() };
  conv.tours.push(tour);
  conv.resume = resumeConversation(conv);
  return { tour, conversation: conv };
}

/** L'utilisateur choisit de répondre sur le nouveau sujet : la fiche devient courante, le sujet initial est conservé. */
export function basculerSujet(conv, ficheId) {
  if (!conv.fiches.includes(ficheId)) conv.fiches.push(ficheId);
  conv.courante = ficheId;
  conv.resume = resumeConversation(conv);
  return conv;
}
export function revenirSujetInitial(conv) {
  conv.courante = conv.sujet.fiche_id;
  conv.resume = resumeConversation(conv);
  return conv;
}

// ─── Résumé évolutif (borné, pour l'affichage et l'envoi au serveur) ──────────
export function resumeConversation(conv, { max = 2500 } = {}) {
  const m = conv.memoire;
  const last = (arr, k) => arr.slice(-k);
  const L = [];
  L.push(`Sujet initial : « ${conv.sujet.affirmation} »${conv.sujet.question && conv.sujet.question !== conv.sujet.affirmation ? ` (question posée : « ${conv.sujet.question} »)` : ''}.`);
  L.push(`Objectif : ${conv.mode === 'gagner' ? 'gagner le débat' : 'convaincre avec empathie'}.`);
  L.push(`Hypothèses de l’utilisateur sur l’interlocuteur (non vérifiées) : ${conv.hypotheses.inconnu ? 'aucune' : resumeProfil(conv.hypotheses) || 'aucune'}.`);
  if (conv.infos.length) L.push(`Informations données par l’utilisateur : ${conv.infos.join(' ; ')}.`);
  L.push(`Échanges : ${conv.tours.length}. Sujet en cours : ${conv.courante === conv.sujet.fiche_id ? 'le sujet initial' : `un sujet voisin (${conv.courante})`}.`);
  const guil = (x) => (x.startsWith('«') ? x : `« ${x} »`);
  if (m.accords.length) L.push(`Points d’accord : ${last(m.accords, 6).map((a) => guil(cvPremierePhrase(a.texte).slice(0, 160))).join(' ; ')}.`);
  const ouverts = m.contestes.filter((c) => !c.resolu);
  if (ouverts.length) L.push(`Points contestés : ${last(ouverts, 6).map((c) => cvPremierePhrase(c.texte).slice(0, 160)).join(' ; ')}.`);
  if (m.objections.length) L.push(`Objections formulées : ${last(m.objections.filter((o) => !o.anticipee), 6).map((o) => `« ${o.texte.slice(0, 140)} »${o.traitee ? ' (traitée)' : ''}`).join(' ; ')}.`);
  if (m.arguments.length) L.push(`Faits vérifiés déjà présentés : ${m.arguments.length} (derniers : ${last(m.arguments, 4).map((a) => `« ${cvPremierePhrase(a.texte).slice(0, 120)} »`).join(' ; ')}).`);
  if (m.sources.length) L.push(`Sources déjà citées : ${m.sources.map((s) => `${s.organisme}, ${s.date}`).join(' ; ')}.`);
  const rapportes = last(conv.tours.filter((t) => t.message), 3);
  if (rapportes.length) L.push(`Derniers propos rapportés par l’utilisateur : ${rapportes.map((t) => `« ${t.message.slice(0, 200)} »`).join(' ; ')}.`);
  if (m.corrections.length) L.push(`Hypothèses corrigées ${m.corrections.length} fois par l’utilisateur.`);
  let txt = L.join('\n');
  if (txt.length > max) txt = `${txt.slice(0, max - 1)}…`;
  return txt;
}

/** Phase de la discussion (indicatif). */
export function phaseConversation(conv) {
  const r = conv.memoire.reactions.slice(-4).map((x) => x.type);
  if (!conv.tours.length) return 'ouverture';
  if (r.filter((x) => x === 'braque' || x === 'provocation').length >= 2) return 'tension';
  if (r.filter((x) => x === 'essoufflement' || x === 'conclusion').length >= 1) return 'essoufflement';
  if (r.some((x) => x === 'reconnaissance' || x === 'evolution' || x.startsWith('partiel'))) return 'convergence';
  return 'approfondissement';
}

// ─── Clôture (décidée par l'utilisateur uniquement) ─────────────────────────
export function terminerConversation(conv, { bibliotheque = [] } = {}) {
  const m = conv.memoire;
  const types = m.reactions.map((r) => r.type);
  const nb = (...k) => types.filter((x) => k.includes(x)).length;
  const positifs = nb('reconnaissance', 'evolution', 'partiel', 'partiel_causes', 'partiel_solution', 'hesitation');
  const negatifs = nb('braque', 'provocation');
  const P = [];
  if (!conv.tours.length) {
    P.push('Bravo d’avoir préparé cette discussion !');
    P.push('La conversation n’a pas encore vraiment commencé ici : tu as tes arguments et tes sources sous la main pour la prochaine fois.');
  } else {
    P.push(negatifs >= 2 && negatifs > positifs ? 'Bravo d’avoir essayé !' : 'Bravo pour cet échange !');
    if (negatifs >= 2 && negatifs > positifs) {
      P.push('La discussion a été tendue, et tu as gardé ton calme pour défendre des faits : ce n’est pas rien.');
      P.push('Il est aussi légitime de poser des limites quand le ton monte : préserver la relation compte autant que l’argument.');
    } else if (positifs > 0) {
      P.push('Tu as pris le temps d’écouter, d’expliquer tes arguments et de faire vivre la discussion.');
    } else {
      P.push('Tu as tenu la discussion sur la durée, sans lâcher le fil.');
    }
    if (m.sources.length) P.push(`Tu as appuyé tes propos sur des faits vérifiables et des sources précises : c’est ce qui rend un échange solide.`);
    const acc = m.accords.find((a) => a.origine === 'rapporte') || m.accords[0];
    if (acc) P.push(acc.origine === 'deduit'
      ? `D’après ce que tu as rapporté, ton interlocuteur t’a donné raison sur au moins un point : c’est une vraie avancée, même modeste.`
      : `Ton interlocuteur a reconnu au moins un point (${acc.texte.startsWith('«') ? acc.texte.slice(0, 160) : `« ${cvPremierePhrase(acc.texte).slice(0, 140)} »`}) : c’est une vraie avancée, même modeste.`);
    if (nb('evolution')) P.push('D’après ce que tu as rapporté, il ou elle a montré de l’ouverture. Sans en conclure qu’il ou elle a changé d’avis, c’est une porte entrouverte.');
    if (!m.accords.length && !nb('evolution')) P.push('Vous êtes restés en désaccord, et ce n’est pas un échec : une opinion évolue souvent lentement. Tu as peut-être semé des graines de réflexion.');
    P.push('L’essentiel est d’avoir pu échanger et de continuer à réfléchir ensemble.');
  }
  const libFiche = (id) => cvFiche(bibliotheque, id);
  const bilan = {
    message: P.join(' '),
    nb_echanges: conv.tours.length,
    arguments: m.arguments.map((a) => ({ texte: a.texte, fiche_id: a.fiche_id, affirmation: libFiche(a.fiche_id)?.affirmation || null })),
    accords: m.accords.map((a) => (a.origine === 'deduit' ? `${a.texte} (point auquel il ou elle a donné raison, d’après toi)` : a.texte)),
    desaccords: m.contestes.filter((c) => !c.resolu).map((c) => c.texte),
    objections: m.objections.filter((o) => !o.anticipee).map((o) => ({ texte: o.texte, traitee: o.traitee })),
    sources: m.sources.map((s) => ({ ...s })),
    sujets: conv.fiches.map((id) => libFiche(id)?.affirmation).filter(Boolean),
    incertitudes: m.incertitudes.map((x) => x.texte),
    fin: new Date().toISOString(),
  };
  conv.terminee = true;
  conv.bilan = bilan;
  return bilan;
}

/** Charge utile bornée pour le mode connecté (résumé évolutif + derniers tours, jamais tout l'historique). */
export function chargeServeur(conv, message, { raccourci = null, derniers = 6 } = {}) {
  return {
    conversation_id: conv.id,
    mode: conv.mode,
    fiche_id: conv.courante,
    sujet_fiche_id: conv.sujet.fiche_id,
    interlocuteur: conv.hypotheses,
    resume: (conv.resume || resumeConversation(conv)).slice(0, 3000),
    derniers: conv.tours.slice(-derniers).map((t) => ({ rapporte: (t.message || '').slice(0, 600), conseil: String(t.intervention?.texte || '').slice(0, 600) })),
    deja: conv.memoire.arguments.filter((a) => a.fiche_id === conv.courante).map((a) => a.index),
    message: String(message || '').slice(0, CV_MAX_TEXTE),
    raccourci,
    tour: conv.tours.length + 1,
  };
}
