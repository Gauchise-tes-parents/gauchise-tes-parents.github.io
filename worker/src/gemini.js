// Fournisseur d'IA : Google Gemini (API officielle generateContent, en-tête x-goog-api-key).
// Interface commune à tout fournisseur (pour ajouter plus tard une solution de secours) :
//   generate({ system, user, search, maxTokens, temperature }) → { text, recherche: { requetes, pages }, usage, modele }
// Les erreurs sont normalisées en IaError (code, message en français, statut HTTP, relance possible).
// La clé n'est jamais journalisée ni renvoyée au navigateur.

export class IaError extends Error {
  constructor(code, message, status = 502, extra = {}) {
    super(message);
    this.code = code;
    this.status = status;
    this.extra = extra;
  }
}

const MESSAGES = {
  config: "L'intelligence artificielle n'est pas encore configurée sur ce site (clé absente côté serveur). La bibliothèque reste disponible.",
  quota: "Google refuse la demande pour une question de quota (quota gratuit épuisé ou nul pour ce modèle). L'administrateur du site doit activer la facturation sur le projet Google de la clé, ou choisir un autre modèle. La bibliothèque reste disponible.",
  frequence: "Trop de demandes à l'intelligence artificielle en peu de temps. Réessaie dans une minute.",
  cle: "La clé de l'intelligence artificielle est refusée par Google (révoquée ou invalide). L'administrateur du site doit la renouveler.",
  modele: "Le modèle d'intelligence artificielle configuré n'est pas disponible. L'administrateur du site doit changer GEMINI_MODEL.",
  refus: "L'intelligence artificielle a refusé de répondre à cette demande.",
  vide: "L'intelligence artificielle n'a pas renvoyé de réponse exploitable. Tu peux relancer.",
  delai: "L'intelligence artificielle a mis trop de temps à répondre. Tu peux relancer.",
  reseau: "Impossible de joindre l'intelligence artificielle (problème réseau). Tu peux relancer.",
  service: "Le service d'intelligence artificielle de Google est momentanément indisponible. Tu peux relancer.",
  requete: "La demande n'a pas pu être traitée par l'intelligence artificielle.",
};
export const iaErreur = (code, extra) => new IaError(code, MESSAGES[code] || MESSAGES.requete, { config: 503, quota: 429, frequence: 429, cle: 503, modele: 503, refus: 422, vide: 502, delai: 504, reseau: 502, service: 503 }[code] || 502, extra);

/** Classe une réponse d'erreur de l'API Gemini (format { error: { code, status, message } }). */
export function classerErreur(httpStatus, body) {
  const st = String(body?.error?.status || '');
  const msg = String(body?.error?.message || '').toLowerCase();
  if (httpStatus === 429 || st === 'RESOURCE_EXHAUSTED') {
    // « limit: 0 » = aucun quota pour ce modèle ou cet outil (cas typique sans facturation) : ce n'est pas une affaire de fréquence
    if (/limit:\s*0\b|free_?tier|billing|quota exceeded/.test(msg) && !/per ?minute|perminute/.test(msg.replace(/limit:\s*0\b/, ''))) return 'quota';
    if (/limit:\s*0\b/.test(msg)) return 'quota';
    return /per ?minute|perminute|rate limit|too many requests/.test(msg) ? 'frequence' : 'quota';
  }
  if (httpStatus === 401 || httpStatus === 403 || st === 'PERMISSION_DENIED' || st === 'UNAUTHENTICATED' || /api key/.test(msg)) return 'cle';
  if (httpStatus === 404 || st === 'NOT_FOUND') return 'modele';
  if (httpStatus === 400 && /location is not supported|user location/.test(msg)) return 'service';
  if (httpStatus >= 500) return 'service';
  return 'requete';
}

/** Message d'erreur de Google, sans lien, raccourci : aide au diagnostic (il ne contient jamais la question). */
export const detailGoogle = (body) => String(body?.error?.message || '').replace(/https?:\/\/\S+/g, '').replace(/\s+/g, ' ').trim().slice(0, 300);

/** Extrait les pages réellement consultées par la recherche Google (groundingMetadata). */
export function extraireRecherche(candidate) {
  const g = candidate?.groundingMetadata;
  if (!g) return { requetes: [], pages: [] };
  const pages = [];
  for (const c of g.groundingChunks || []) {
    const uri = c?.web?.uri;
    if (typeof uri === 'string' && /^https:\/\//.test(uri)) pages.push({ url: uri, titre: String(c.web.title || '').slice(0, 200) });
  }
  return { requetes: (g.webSearchQueries || []).filter((q) => typeof q === 'string').slice(0, 10), pages: pages.slice(0, 15) };
}

export function createGeminiProvider(env, { fetchImpl = fetch } = {}) {
  const modele = String(env.GEMINI_MODEL || '').trim();
  // modèles de secours, essayés UNIQUEMENT si le modèle principal est refusé (quota, fréquence, modèle absent)
  const secours = String(env.GEMINI_MODELES_SECOURS ?? 'gemini-2.5-flash').split(',').map((x) => x.trim()).filter((x) => x && x !== modele);
  const apiBase = String(env.GEMINI_API_BASE || 'https://generativelanguage.googleapis.com/v1beta').replace(/\/+$/, '');
  const timeoutMs = Number(env.GEMINI_TIMEOUT_MS || 45000);

  async function appel(nomModele, { system, user, search, maxTokens, temperature }) {
    const body = {
      systemInstruction: { parts: [{ text: system }] },
      contents: [{ role: 'user', parts: [{ text: user }] }],
      generationConfig: { temperature, maxOutputTokens: maxTokens },
      ...(search ? { tools: [{ google_search: {} }] } : {}),
    };
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeoutMs);
    let res;
    try {
      res = await fetchImpl(`${apiBase}/models/${encodeURIComponent(nomModele)}:generateContent`, {
        method: 'POST',
        signal: controller.signal,
        headers: { 'content-type': 'application/json', 'x-goog-api-key': env.GEMINI_API_KEY },
        body: JSON.stringify(body),
      });
    } catch (err) {
      throw iaErreur(err?.name === 'AbortError' ? 'delai' : 'reseau');
    } finally {
      clearTimeout(timer);
    }
    let data = null;
    try { data = await res.json(); } catch { data = null; }
    if (!res.ok) throw iaErreur(classerErreur(res.status, data), { detail: detailGoogle(data), http: res.status });
    if (data?.promptFeedback?.blockReason) throw iaErreur('refus');
    const cand = data?.candidates?.[0];
    if (!cand || cand.finishReason === 'SAFETY' || cand.finishReason === 'PROHIBITED_CONTENT') throw iaErreur(cand ? 'refus' : 'vide');
    const text = (cand.content?.parts || []).map((p) => (typeof p.text === 'string' && !p.thought ? p.text : '')).join('').trim();
    if (!text) throw iaErreur('vide');
    return {
      text,
      tronquee: cand.finishReason === 'MAX_TOKENS',
      recherche: extraireRecherche(cand),
      usage: { entree: data.usageMetadata?.promptTokenCount ?? null, sortie: data.usageMetadata?.candidatesTokenCount ?? null },
      modele: nomModele,
      candidate: cand,
    };
  }

  return {
    nom: 'gemini',
    modele,
    disponible: () => Boolean(env.GEMINI_API_KEY && modele),
    async generate({ system, user, search = true, maxTokens = 2048, temperature = 0.4, exigerRecherche = false }) {
      if (!env.GEMINI_API_KEY || !modele) throw iaErreur('config');
      // essais : modèle principal (avec recherche), puis sans recherche, puis modèles de secours sans recherche.
      // On ne passe à l'essai suivant que sur un refus de quota, de fréquence ou de modèle : au plus 3 appels.
      // une fiche exige la recherche (sinon pas de sources) : les essais gardent alors la recherche
      const essais = exigerRecherche
        ? [{ m: modele, search: true }, ...secours.map((m) => ({ m, search: true }))].slice(0, 2)
        : [{ m: modele, search }, ...(search ? [{ m: modele, search: false }] : []), ...secours.map((m) => ({ m, search: false }))].slice(0, 3);
      let derniere = null;
      for (const e of essais) {
        try {
          const r = await appel(e.m, { system, user, search: e.search, maxTokens, temperature });
          return { ...r, recherche_demandee: search, recherche_utilisee: e.search, secours: e.m !== modele || e.search !== search };
        } catch (err) {
          derniere = err;
          if (!(err instanceof IaError) || !['quota', 'frequence', 'modele'].includes(err.code)) throw err;
        }
      }
      throw derniere;
    },
  };
}
