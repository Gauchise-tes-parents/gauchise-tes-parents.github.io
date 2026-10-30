// Base de connaissances locale du mode autonome.
// Chargement : base intégrée (aperçu) → cache du service worker → réseau.
// Mise à jour : seulement après vérification de l'empreinte SHA-256 et du contenu ;
// l'ancienne base n'est jamais supprimée avant que la nouvelle soit validée.
const KB_CACHE = 'gtp-kb';
const KB_META_KEY = 'gtp-kb-meta';
let kbBase = null;

const KB_STATIC = typeof window !== 'undefined' ? window.__GTP_STATIC__ : null;

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
    const res = await fetch('kb/base.json');
    if (!res.ok) throw new Error('base locale introuvable');
    const text = await res.text();
    const data = JSON.parse(text);
    if (validateBase(data).length) throw new Error('base locale invalide');
    kbBase = data;
    const m = kbReadMeta();
    if (!m?.version) {
      const manifest = await fetch('kb/manifest.json').then((r) => (r.ok ? r.json() : null)).catch(() => null);
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
    let text;
    try {
      const r = await fetch(`kb/base.json?v=${encodeURIComponent(manifest.version)}`, { cache: 'no-store' });
      if (!r.ok) return { statut: 'echec', raison: 'téléchargement impossible' };
      text = await r.text();
    } catch { return { statut: 'echec', raison: 'téléchargement interrompu' }; }
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
