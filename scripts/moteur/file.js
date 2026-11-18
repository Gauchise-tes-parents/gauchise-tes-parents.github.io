// File des questions sans réponse : regroupe les questions reçues (collecteur du site, opt-in) et celles que le
// propriétaire ajoute à la main dans data/moteur/questions.txt (une par ligne, # pour un commentaire).
import { readFileSync, existsSync } from 'node:fs';
import { kbNormalize } from '../../public/js/kbsearch.js';
import { lire } from './reseau.js';

export const cleQuestion = (t) => kbNormalize(t).replace(/[^a-z0-9]+/g, ' ').trim();

/** Ajoute des questions à la file (dédoublonnées sur leur forme normalisée). */
export function ajouter(file, questions, origine, jour = new Date().toISOString().slice(0, 10)) {
  file.questions ||= {};
  let nouvelles = 0;
  for (const q of questions) {
    const texte = String(q || '').replace(/\s+/g, ' ').trim();
    const cle = cleQuestion(texte);
    if (cle.length < 6 || texte.length > 300) continue;
    const ex = file.questions[cle];
    if (ex) { ex.occurrences += 1; ex.derniere = jour; if (!ex.origines.includes(origine)) ex.origines.push(origine); continue; }
    file.questions[cle] = { texte, premiere: jour, derniere: jour, occurrences: 1, origines: [origine], statut: 'en_attente' };
    nouvelles += 1;
  }
  return nouvelles;
}

/** Questions écrites à la main par le propriétaire. */
export function questionsManuelles(chemin) {
  if (!existsSync(chemin)) return [];
  return readFileSync(chemin, 'utf8').split('\n').map((l) => l.trim()).filter((l) => l && !l.startsWith('#'));
}

/** Questions envoyées depuis le site (collecteur worker-questions/), purgées du collecteur après lecture. */
export async function questionsCollecteur({ base, jeton, fetchImpl = fetch }) {
  if (!base || !jeton) return { questions: [], statut: 'non configuré' };
  const r = await fetchImpl(`${base.replace(/\/+$/, '')}/export?purger=1`, { headers: { authorization: `Bearer ${jeton}` } });
  if (!r.ok) throw new Error(`collecteur : HTTP ${r.status}`);
  const d = await r.json();
  return { questions: (d.questions || []).map((q) => q.texte).filter(Boolean), statut: 'lu' };
}

export { lire };
