// Base de connaissances locale du mode autonome.
// Chargement : base intégrée (aperçu) → cache du service worker → réseau.
// Mise à jour : seulement après vérification de l'empreinte SHA-256 et du contenu ;
// l'ancienne base n'est jamais supprimée avant que la nouvelle soit validée.
const KB_CACHE = 'gtp-kb';
const KB_META_KEY = 'gtp-kb-meta';
let kbBase = null;

const KB_STATIC = typeof window !== 'undefined' ? window.__GTP_STATIC__ : null;
// v15.1 (affluence) : relais Cloudflare de la base (worker-direct/, fichiers statiques gratuits et illimités).
// La base y est téléchargée en priorité ; son empreinte est vérifiée avec le manifeste de GitHub Pages et, au
// moindre écart ou à la moindre panne, la copie de GitHub Pages est utilisée (l'utilisateur ne voit rien).
const KB_RELAIS = (typeof window !== 'undefined' && /^https:\/\//.test(window.GTP_CONFIG?.kbRelais || '')) ? String(window.GTP_CONFIG.kbRelais).replace(/\/+$/, '') : '';

/** Télécharge la base depuis le relais si son empreinte correspond au manifeste ; sinon null. */
async function kbDepuisRelais(manifest) {
  if (!KB_RELAIS || !manifest?.sha256 || !manifest?.version) return null;
  try {
    const ctrl = typeof AbortController !== 'undefined' ? new AbortController() : null;
    const minuteur = ctrl ? setTimeout(() => ctrl.abort(), 20000) : null;
    const r = await fetch(`${KB_RELAIS}/base.json?v=${encodeURIComponent(manifest.version)}`, { credentials: 'omit', referrerPolicy: 'no-referrer', signal: ctrl?.signal });
    if (minuteur) clearTimeout(minuteur);
    if (!r.ok) return null;
    const text = await r.text();
    const hash = await kbSha256Hex(text);
    return hash && hash === manifest.sha256 ? text : null; // relais en retard ou altéré : on ne l'utilise pas
  } catch { return null; }
}

function kbReadMeta() { try { return JSON.parse(localStorage.getItem(KB_META_KEY) || 'null'); } catch { return null; } }
function kbWriteMeta(m) { try { localStorage.setItem(KB_META_KEY, JSON.stringify(m)); } catch { /* sans stockage : métadonnées en mémoire */ } }

async function kbSha256Hex(text) {
  if (!globalThis.crypto?.subtle) return null; // contexte non sécurisé : empreinte non vérifiable
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

/** Contrôle minimal de structure avant d'accepter une base. Renvoie une liste de problèmes. */
export function validateBase(data) {
  const errs = [];
  if (!data || typeof data !== 'object' || !Array.isArray(data.fiches)) return ['format inconnu'];
  if (data.fiches.length < 10) errs.push('base anormalement petite');
  for (const f of data.fiches) {
    if (!f || typeof f.id !== 'string' || typeof f.affirmation !== 'string') { errs.push('fiche sans identifiant'); break; }
    if (!Array.isArray(f.sources) || !Array.isArray(f.faits) || !f.argumentaires) { errs.push(`fiche ${f.id} incomplète`); break; }
    if (f.faits.some((x) => !f.sources[x.source] || f.sources[x.source].consultee !== true)) { errs.push(`fiche ${f.id} : fait sans source consultée`); break; }
  }
  return errs;
}

export const kb = {
  get fiches() { return kbBase?.fiches || []; },
  get meta() { return kbReadMeta(); },
  loaded: () => Boolean(kbBase),

  async load() {
    if (kbBase) return kbBase;
    if (KB_STATIC?.library) {
      kbBase = { format: 3, fiches: KB_STATIC.library };
      kbWriteMeta({ ...(kbReadMeta() || {}), version: KB_STATIC.version || 'integree', source: 'integree', nb: kbBase.fiches.length, date: KB_STATIC.date || null });
      return kbBase;
    }
    let text = null;
    let manifest = null;
    // 1. copie hors ligne déjà enregistrée (visite précédente) : aucun téléchargement
    try { if ('caches' in globalThis) { const c = await (await caches.open(KB_CACHE)).match('kb/base.json'); if (c) text = await c.text(); } } catch { /* stockage indisponible */ }
    // 2. relais Cloudflare, empreinte vérifiée ; 3. à défaut, GitHub Pages
    if (!text && KB_RELAIS) {
      manifest = await fetch('kb/manifest.json', { cache: 'no-cache' }).then((r) => (r.ok ? r.json() : null)).catch(() => null);
      text = await kbDepuisRelais(manifest);
    }
    if (!text) {
      const res = await fetch('kb/base.json');
      if (!res.ok) throw new Error('base locale introuvable');
      text = await res.text();
    }
    const data = JSON.parse(text);
    if (validateBase(data).length) throw new Error('base locale invalide');
    kbBase = data;
    // v15.1 : la base téléchargée est rangée une fois pour toutes dans le cache hors ligne (le service worker ne la
    // télécharge plus de son côté). Une base déjà présente n'est remplacée que par checkUpdate (empreinte vérifiée).
    try {
      if ('caches' in globalThis) {
        const c = await caches.open(KB_CACHE);
        if (!(await c.match('kb/base.json'))) {
          await c.put('kb/base.json', new Response(text, { headers: { 'content-type': 'application/json' } }));
          manifest = manifest || await fetch('kb/manifest.json').then((r) => (r.ok ? r.json() : null)).catch(() => null);
          if (manifest) await c.put('kb/manifest.json', new Response(JSON.stringify(manifest), { headers: { 'content-type': 'application/json' } }));
        }
      }
    } catch { /* stockage indisponible (navigation privée…) : l'application marche en ligne */ }
    const m = kbReadMeta();
    if (!m?.version) {
      manifest = manifest || await fetch('kb/manifest.json').then((r) => (r.ok ? r.json() : null)).catch(() => null);
      kbWriteMeta({ version: manifest?.version || 'inconnue', date: manifest?.genere_le || null, nb: data.fiches.length, source: 'cache', verifiee: Boolean(manifest) });
    }
    return kbBase;
  },

  /**
   * Cherche une nouvelle version. Ne fait rien hors ligne. Si `appliquer` est vrai et que la nouvelle base
   * est valide (empreinte + contenu), elle remplace l'ancienne dans le cache du service worker.
   */
  async checkUpdate({ appliquer = true } = {}) {
    if (KB_STATIC) return { statut: 'integree' };
    if (typeof navigator !== 'undefined' && navigator.onLine === false) return { statut: 'hors_ligne' };
    let manifest;
    try {
      const r = await fetch('kb/manifest.json', { cache: 'no-store' });
      if (!r.ok) return { statut: 'indisponible' };
      manifest = await r.json();
    } catch { return { statut: 'hors_ligne' }; }
    const current = kbReadMeta();
    if (!manifest?.version) return { statut: 'indisponible' };
    if (current?.version === manifest.version) return { statut: 'a_jour', version: manifest.version };
    if (!appliquer) return { statut: 'disponible', version: manifest.version, nb: manifest.nb_fiches };
    let text = await kbDepuisRelais(manifest); // relais Cloudflare d'abord (empreinte vérifiée), sinon GitHub Pages
    if (!text) {
      try {
        const r = await fetch(`kb/base.json?v=${encodeURIComponent(manifest.version)}`, { cache: 'no-store' });
        if (!r.ok) return { statut: 'echec', raison: 'téléchargement impossible' };
        text = await r.text();
      } catch { return { statut: 'echec', raison: 'téléchargement interrompu' }; }
    }
    const hash = await kbSha256Hex(text);
    if (hash && hash !== manifest.sha256) return { statut: 'echec', raison: 'empreinte invalide : base conservée' };
    let data;
    try { data = JSON.parse(text); } catch { return { statut: 'echec', raison: 'fichier illisible : base conservée' }; }
    const errs = validateBase(data);
    if (errs.length) return { statut: 'echec', raison: `contenu refusé (${errs[0]}) : base conservée` };
    if ('caches' in globalThis) {
      const c = await caches.open(KB_CACHE);
      await c.put('kb/base.json', new Response(text, { headers: { 'content-type': 'application/json' } }));
      await c.put('kb/manifest.json', new Response(JSON.stringify(manifest), { headers: { 'content-type': 'application/json' } }));
    }
    kbBase = data;
    kbWriteMeta({ version: manifest.version, date: manifest.genere_le, nb: data.fiches.length, source: 'mise_a_jour', verifiee: Boolean(hash) });
    return { statut: 'mise_a_jour', version: manifest.version, nb: data.fiches.length, empreinte_verifiee: Boolean(hash) };
  },
};
