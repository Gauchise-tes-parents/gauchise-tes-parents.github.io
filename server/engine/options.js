// Validation des requêtes : toute valeur venant du client est confrontée aux listes fermées de taxonomy.js.
import { MODES, VOLETS, PROFILS, CONTEXTES, DUREES, LIMITS, voletById } from '../../public/js/taxonomy.js';
import { nettoyerProfil } from '../../public/js/profile.js';

const has = (list, id) => list.some(([k]) => k === id);

export function validateOptions(body = {}) {
  return {
    mode: MODES[body.mode] ? body.mode : 'gagner',
    profil: has(PROFILS, body.profil) ? body.profil : 'mystere',
    contexte: has(CONTEXTES, body.contexte) ? body.contexte : 'repas',
    interlocuteur: nettoyerProfil(body.interlocuteur && typeof body.interlocuteur === 'object' ? body.interlocuteur : { inconnu: true }),
  };
}

/** Valide la requête d'analyse. Renvoie { ok, value } ou { ok:false, error }. */
export function validateAnalyseRequest(body) {
  if (!body || typeof body !== 'object') return { ok: false, error: 'Requête invalide.' };
  const claim = typeof body.affirmation === 'string' ? body.affirmation.trim().replace(/\s+/g, ' ') : '';
  if (claim.length < 5) return { ok: false, error: "L'affirmation est trop courte (5 caractères minimum)." };
  if (claim.length > LIMITS.claimMax) return { ok: false, error: `L'affirmation est trop longue (${LIMITS.claimMax} caractères maximum).` };
  const volet = VOLETS.some((v) => v.id === body.volet) ? body.volet : 'autre';
  const sousTheme = voletById(volet).sousThemes.includes(body.sous_theme) ? body.sous_theme : null;
  return {
    ok: true,
    value: {
      claim, volet, sousTheme,
      express: body.express === true,
      fraiche: body.fraiche === true,
      ...validateOptions(body),
    },
  };
}

export function validateDuree(d) {
  const n = Number(d);
  return has(DUREES, n) ? n : null;
}
