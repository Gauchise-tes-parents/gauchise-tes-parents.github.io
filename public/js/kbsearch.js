// Recherche dans la base locale, partagée entre le serveur et le navigateur (aperçu statique).
// Insensible aux accents et à la casse ; chaque mot de la question compte une fois, au poids du meilleur champ.
import { rubriqueById, voletById } from './taxonomy.js';

export const kbNormalize = (s) => String(s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[’']/g, ' ');
const KB_STOP = new Set(['les', 'des', 'une', 'que', 'qui', 'pas', 'est', 'sont', 'ont', 'pour', 'dans', 'avec', 'plus', 'tout', 'tous', 'toute', 'toutes', 'leur', 'leurs', 'aux', 'par', 'sur', 'mais', 'ils', 'elles', 'nous', 'vous', 'ces', 'cette', 'quand', 'comme', 'son', 'ses', 'elle', 'lui', 'fait', 'font', 'faut', 'etre', 'avoir', 'bien', 'tres', 'trop', 'rien', 'jamais', 'toujours', 'meme', 'deja', 'alors', 'donc', 'car', 'entre', 'sans', 'chez', 'apres', 'avant', 'encore', 'aussi', 'cela', 'quoi', 'dit', 'dire', 'veut', 'veulent', 'temps']);
export const kbTokens = (s) => kbNormalize(s).split(/[^a-z0-9]+/).filter((t) => t.length > 2 && !KB_STOP.has(t));
const kbStem = (t) => t.slice(0, Math.min(t.length, 6));
const kbSet = (s) => new Set(kbTokens(s).map(kbStem));

const KB_FIELDS = [['affirmation', 3], ['mots_cles', 3], ['sous_theme', 2], ['rubriques', 2], ['resume', 1], ['contexte', 1], ['volet', 1]];
const kbCache = new WeakMap();

function kbFieldTokens(e) {
  let tok = kbCache.get(e);
  if (tok) return tok;
  tok = {
    affirmation: kbSet(e.affirmation),
    mots_cles: kbSet((e.mots_cles || []).join(' ')),
    sous_theme: kbSet(e.sous_theme),
    rubriques: kbSet((e.rubriques || []).map((r) => rubriqueById(r)?.label || '').join(' ')),
    resume: kbSet(e.resume),
    contexte: kbSet(`${e.contexte || ''} ${e.reproche || ''}`),
    volet: kbSet(voletById(e.volet).label),
  };
  kbCache.set(e, tok);
  return tok;
}

/** Score de pertinence d'une fiche pour une question (0 si aucun mot commun). */
export function kbScore(e, query) {
  const q = [...new Set(kbTokens(query).map(kbStem))];
  if (!q.length) return { score: 0, couverture: 0 };
  const tok = kbFieldTokens(e);
  let score = 0;
  let hits = 0;
  for (const t of q) {
    let best = 0;
    for (const [f, w] of KB_FIELDS) if (w > best && tok[f].has(t)) best = w;
    if (best) { score += best; hits += 1; }
  }
  // Bonus pour une expression-clé complète (« la police tue », « loi de 1905 »…).
  const nq = ` ${kbNormalize(query).replace(/[^a-z0-9]+/g, ' ')} `;
  for (const k of e.mots_cles || []) {
    const nk = kbNormalize(k).replace(/[^a-z0-9]+/g, ' ').trim();
    if (nk.includes(' ') && nq.includes(` ${nk} `)) score += 3;
  }
  return { score, couverture: hits / q.length, hits };
}

/** Fiches les plus proches d'une affirmation : « forte » = même affirmation très probable ; « partielle » = sujet voisin. */
export function kbMatch(entries, query, { limit = 3 } = {}) {
  return entries
    .map((e) => ({ e, ...kbScore(e, query) }))
    .filter((x) => x.score >= 3 && x.couverture >= 0.25 && (x.hits >= 2 || x.couverture > 0.3)) // un seul mot commun dans une phrase de 4 mots ou plus ne suffit pas
    .sort((a, b) => b.score - a.score || b.couverture - a.couverture)
    .slice(0, limit)
    .map((x) => ({
      fiche: x.e, score: x.score, couverture: Math.round(x.couverture * 100) / 100,
      force: (x.score >= 6 && x.couverture >= 0.6) || x.score >= 9 ? 'forte' : 'partielle',
    }));
}

/** Recherche avec filtres (texte facultatif). */
export function kbSearch(entries, query, { volet = null, sousTheme = null, rubrique = null, fiabilite = null, min = 1 } = {}) {
  const filtered = entries.filter((e) => (!volet || e.volet === volet) && (!sousTheme || e.sous_theme === sousTheme)
    && (!rubrique || (e.rubriques || []).includes(rubrique)) && (!fiabilite || e.fiabilite === fiabilite));
  if (!kbTokens(query).length) return filtered;
  return filtered
    .map((e) => ({ e, ...kbScore(e, query) }))
    .filter((x) => x.score >= min)
    .sort((a, b) => b.score - a.score || b.couverture - a.couverture)
    .map((x) => x.e);
}

// ─── Fraîcheur et ancienneté des données (partagé serveur / navigateur) ─────────
export const kbToday = () => new Date().toLocaleDateString('sv-SE', { timeZone: 'Europe/Paris' });

/** Une fiche dont la date de révision est passée (ou trop ancienne) est signalée « à actualiser ». */
export function kbFreshness(e, { today = kbToday(), staleDays = 365 } = {}) {
  const ageDays = Math.floor((Date.parse(today) - Date.parse(e.derniere_verification)) / 86400000);
  if (e.a_actualiser_le && today >= e.a_actualiser_le) {
    return { statut: 'a_actualiser', raison: e.raison_actualisation || 'De nouvelles données sont probablement disponibles.' };
  }
  if (staleDays > 0 && ageDays > staleDays) return { statut: 'a_actualiser', raison: `Dernière vérification il y a plus de ${staleDays} jours.` };
  return { statut: 'a_jour', raison: null };
}

/**
 * Avertissement d'ancienneté pour un usage hors ligne : un fait historique reste utilisable ;
 * une statistique susceptible d'évoluer est toujours présentée avec sa date de référence.
 */
export function kbDataAge(e, opts = {}) {
  const f = kbFreshness(e, opts);
  if (f.statut === 'a_actualiser') return { niveau: 'ancienne', texte: `Données à actualiser : ${f.raison} Vérifiées le ${e.derniere_verification}.` };
  if (e.stabilite === 'historique') return { niveau: 'stable', texte: 'Fait historique stable : utilisable hors ligne.' };
  if (e.stabilite === 'actualite') return { niveau: 'datee', texte: `Sujet d'actualité vérifié le ${e.derniere_verification} : la situation a pu évoluer depuis.` };
  return { niveau: 'datee', texte: `Statistiques vérifiées le ${e.derniere_verification} : elles ont pu évoluer depuis (prochaine révision prévue le ${e.a_actualiser_le}).` };
}
