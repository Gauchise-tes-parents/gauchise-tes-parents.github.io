// Utilitaires purs partagés par le moteur (sans dépendance au fournisseur d'IA).

export class EngineError extends Error {
  constructor(code, message, status = 502, { retry = false } = {}) {
    super(message);
    this.code = code;
    this.status = status;
    this.retry = retry;
  }
}

/** Normalise une URL pour comparaison (hôte en minuscules, sans www, fragment ni « / » final). */
export function normalizeUrl(u) {
  if (typeof u !== 'string') return null;
  try {
    const url = new URL(u.trim());
    if (url.protocol !== 'https:' && url.protocol !== 'http:') return null;
    url.hash = '';
    url.hostname = url.hostname.toLowerCase().replace(/^www\./, '');
    let s = url.toString();
    if (s.endsWith('/')) s = s.slice(0, -1);
    try { s = decodeURI(s); } catch { /* déjà décodée */ }
    return s.replace(/^http:/, 'https:');
  } catch {
    return null;
  }
}

/** Seuls les liens http(s) sont acceptés pour l'affichage (évite javascript:, data:, etc.). */
export function isSafeHttpUrl(u) {
  try {
    const url = new URL(u);
    return url.protocol === 'https:' || url.protocol === 'http:';
  } catch {
    return false;
  }
}

/** Extrait le dernier objet JSON d'un texte (bloc ```json``` en priorité). */
export function extractJson(text) {
  if (typeof text !== 'string') return null;
  const fenced = [...text.matchAll(/```(?:json)?\s*([\s\S]*?)```/g)];
  const candidates = fenced.map((m) => m[1]).reverse();
  const first = text.indexOf('{');
  const last = text.lastIndexOf('}');
  if (first !== -1 && last > first) candidates.push(text.slice(first, last + 1));
  for (const c of candidates) {
    try {
      const obj = JSON.parse(c.trim());
      if (obj && typeof obj === 'object' && !Array.isArray(obj)) return obj;
    } catch { /* candidat suivant */ }
  }
  return null;
}

/** Extrait les nombres d'un texte, normalisés (« 1 672 » → 1672, « 12,2 » → 12.2). */
export function extractNumbers(text) {
  const t = String(text || '').replace(/(\d)[\s  .](?=\d{3}(?!\d))/g, '$1');
  const m = t.match(/\d+(?:[.,]\d+)?/g) || [];
  return new Set(m.map((n) => n.replace(',', '.').replace(/(\.\d*?)0+$/, '$1').replace(/\.$/, '')));
}

/** Nombres de `candidate` absents de `reference` (liste vide = aucun chiffre inventé). */
export function newNumbers(candidate, reference) {
  const ref = reference instanceof Set ? reference : extractNumbers(reference);
  return [...extractNumbers(candidate)].filter((n) => !ref.has(n));
}

export const str = (v, max = 4000) => (typeof v === 'string' ? v.trim().slice(0, max) : '');
export const strOrNull = (v, max = 400) => {
  const s = str(v, max);
  return s || null;
};
export const arr = (v) => (Array.isArray(v) ? v : []);
export const isoToday = () => new Date().toLocaleDateString('sv-SE', { timeZone: 'Europe/Paris' });
export const frToday = () => new Date().toLocaleDateString('fr-FR', { timeZone: 'Europe/Paris', day: 'numeric', month: 'long', year: 'numeric' });
