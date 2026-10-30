// Retours utilisateurs : stockage minimal, sans IP, sans identifiant, sans profil d'interlocuteur.
// Objectif unique : détecter erreurs, explications peu claires et références manquantes.
import { appendFile, mkdir } from 'node:fs/promises';
import { dirname } from 'node:path';
import { isSafeHttpUrl } from './engine/util.js';
import { VOLETS, VERDICTS, MODES, LIMITS } from '../public/js/taxonomy.js';

export const RATINGS = {
  oui: 'Oui, carrément !',
  partiel: 'Oui, mais il manque des choses.',
  non: 'Non, il faut revoir ça.',
};
const TYPES = new Set(['avis', 'source_incorrecte', 'erreur_fiche']);

export function validateFeedback(body) {
  if (!body || typeof body !== 'object') return { ok: false, error: 'Requête invalide.' };
  const type = TYPES.has(body.type) ? body.type : 'avis';
  const rating = RATINGS[body.note] ? body.note : null;
  if (type === 'avis' && !rating) return { ok: false, error: 'Choisis une réponse.' };
  const comment = typeof body.commentaire === 'string' ? body.commentaire.trim().slice(0, LIMITS.commentMax) : '';
  const url = typeof body.url === 'string' && isSafeHttpUrl(body.url) ? body.url.slice(0, 600) : null;
  if (type === 'source_incorrecte' && !url) return { ok: false, error: 'URL de la source manquante.' };
  // L'affirmation n'est jointe que si l'utilisateur l'a explicitement accepté.
  const affirmation = body.joindre_affirmation === true && typeof body.affirmation === 'string'
    ? body.affirmation.trim().slice(0, LIMITS.claimMax) : null;
  return {
    ok: true,
    value: {
      date: new Date().toISOString().slice(0, 10), // date seule, pas d'heure précise
      type,
      note: rating,
      commentaire: comment || null,
      url,
      verdict: VERDICTS[body.verdict] ? body.verdict : null,
      volet: VOLETS.some((v) => v.id === body.volet) ? body.volet : null,
      mode_debat: MODES[body.mode_debat] ? body.mode_debat : null,
      fiche: typeof body.fiche === 'string' && /^[a-z0-9-]{3,60}$/.test(body.fiche) ? body.fiche : null,
      mode: body.mode === 'live' || body.mode === 'demo' || body.mode === 'bibliotheque' ? body.mode : null,
      affirmation,
    },
  };
}

export async function storeFeedback(file, entry) {
  await mkdir(dirname(file), { recursive: true });
  await appendFile(file, `${JSON.stringify(entry)}\n`, 'utf8');
}
