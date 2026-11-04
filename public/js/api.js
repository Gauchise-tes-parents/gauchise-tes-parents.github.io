// Accès aux données.
// - Bibliothèque, fiches, recherche locale : TOUJOURS servies par la base locale (mode autonome, sans réseau).
// - Recherche web, stratégie IA, retours : serveur facultatif (mode connecté). Rien n'est simulé sans lui.
import { kb } from './kbstore.js';
import { kbSearch, kbMatch, kbFreshness } from './kbsearch.js';

const API_STATIC = typeof window !== 'undefined' ? window.__GTP_STATIC__ : null;
const API_BASE = (typeof window !== 'undefined' && window.GTP_CONFIG?.apiBase) ? String(window.GTP_CONFIG.apiBase).replace(/\/+$/, '') : '';

// Backend IA (Gemini, Cloudflare Worker) : URL publique facultative, sans aucun secret (la clé reste côté serveur).
const IA_BASE = (typeof window !== 'undefined' && window.GTP_CONFIG?.iaBase) ? String(window.GTP_CONFIG.iaBase).replace(/\/+$/, '') : '';

export class ApiError extends Error {
  constructor(message, status, data = {}) {
    super(message);
    this.status = status;
    this.data = data;
  }
}

async function request(path, { method = 'GET', body } = {}) {
  let res;
  try {
    res = await fetch(API_BASE + path, {
      method,
      headers: body ? { 'content-type': 'application/json' } : {},
      body: body ? JSON.stringify(body) : undefined,
    });
  } catch {
    throw new ApiError('Le serveur ne répond pas. Vérifie ta connexion puis relance. Le mode autonome reste disponible.', 0, { relancer: true });
  }
  let data = {};
  try { data = await res.json(); } catch { /* corps vide ou page HTML d'un hébergeur statique */ }
  if (!res.ok) throw new ApiError(data.erreur || `Erreur ${res.status}.`, res.status, data);
  return data;
}

const withFreshApi = (e) => ({ ...e, fraicheur: kbFreshness(e) });
const NO_SERVER = 'Cette fonction a besoin du serveur du mode connecté, qui n’est pas configuré pour ce site. Le mode autonome reste disponible.';

export const api = {
  isStatic: Boolean(API_STATIC),

  /** État du serveur (mode connecté uniquement). Absence de serveur = état normal, pas une erreur. */
  async status() {
    if (API_STATIC) return { mode: 'absent' };
    try {
      const s = await request('/api/status');
      return s && s.mode ? s : { mode: 'absent' };
    } catch {
      return { mode: 'absent' };
    }
  },

  async library({ q = '', volet = '', rubrique = '', fiabilite = '' } = {}) {
    await kb.load();
    return { fiches: kbSearch(kb.fiches, q, { volet: volet || null, rubrique: rubrique || null, fiabilite: fiabilite || null }).map(withFreshApi) };
  },

  async fiche(id) {
    await kb.load();
    const e = kb.fiches.find((x) => x.id === id);
    if (!e) throw new ApiError('Cette fiche n’existe pas dans la bibliothèque locale.', 404);
    return withFreshApi(e);
  },

  /** Recherche instantanée dans la base locale (aucun réseau). */
  async kbSearch(q) {
    await kb.load();
    const m = kbMatch(kb.fiches, q);
    const best = m[0];
    return {
      correspondances: m.map((x) => ({ ...withFreshApi(x.fiche), force: x.force, score: x.score, court: x.fiche.argumentaires?.court })),
      decision: {
        web_complementaire: !best || best.force !== 'forte',
        motif: !best ? 'non_couvert' : best.force,
        raison: best && best.force === 'forte' ? 'Une fiche vérifiée de la bibliothèque locale traite cette affirmation.' : best ? 'Les fiches trouvées traitent un sujet voisin.' : 'La bibliothèque locale ne contient pas encore cette information.',
      },
    };
  },

  analyse: (payload) => (API_STATIC ? Promise.reject(new ApiError(NO_SERVER, 503)) : request('/api/analyse', { method: 'POST', body: payload })),
  strategie: (payload) => (API_STATIC ? Promise.reject(new ApiError(NO_SERVER, 503)) : request('/api/strategie', { method: 'POST', body: payload })),
  reformuler: (payload) => (API_STATIC ? Promise.reject(new ApiError(NO_SERVER, 503)) : request('/api/reformuler', { method: 'POST', body: payload })),
  demonstration: (payload) => (API_STATIC ? Promise.reject(new ApiError(NO_SERVER, 503)) : request('/api/demonstration', { method: 'POST', body: payload })),
  conversation: (payload) => (API_STATIC ? Promise.reject(new ApiError(NO_SERVER, 503)) : request('/api/conversation', { method: 'POST', body: payload })),
  /** IA (Gemini) : configurée seulement si une URL de backend est fournie au déploiement. */
  iaConfiguree: Boolean(IA_BASE) && !API_STATIC,
  async iaStatut() {
    if (!IA_BASE || API_STATIC) return { disponible: false, configure: false };
    try {
      const r = await fetch(`${IA_BASE}/api/ia/statut`, { method: 'GET', credentials: 'omit' });
      const d = await r.json();
      return { ...d, configure: true };
    } catch {
      return { disponible: false, configure: true, injoignable: true };
    }
  },
  async ia(payload) {
    if (!IA_BASE || API_STATIC) throw new ApiError('L’intelligence artificielle n’est pas configurée pour ce site.', 503, { code: 'config' });
    let res;
    try {
      res = await fetch(`${IA_BASE}/api/ia`, { method: 'POST', credentials: 'omit', headers: { 'content-type': 'application/json' }, body: JSON.stringify(payload) });
    } catch {
      throw new ApiError('Impossible de joindre l’intelligence artificielle. Vérifie ta connexion puis relance. La bibliothèque reste disponible.', 0, { relancer: true, code: 'reseau' });
    }
    let data = {};
    try { data = await res.json(); } catch { /* réponse vide */ }
    if (!res.ok) throw new ApiError(data.erreur || `Erreur ${res.status}.`, res.status, data);
    return data;
  },
  feedback: (payload) => (API_STATIC ? Promise.reject(new ApiError('Les retours ont besoin du serveur, qui n’est pas configuré pour ce site.', 503)) : request('/api/feedback', { method: 'POST', body: payload })),

  /** Veille : état donné par le serveur, sinon fichier publié avec la base. */
  async veille() {
    if (API_STATIC) return { statut: 'indisponible' };
    {
      try { return await request('/api/veille/status'); } catch { /* pas de serveur : on essaie le fichier publié */ }
    }
    try {
      const r = await fetch('kb/veille.json', { cache: 'no-store' });
      if (r.ok) return await r.json();
    } catch { /* hors ligne */ }
    return { statut: 'indisponible' };
  },
  veilleRun: (token) => request('/api/veille/run', { method: 'POST', body: { token } }),
};
