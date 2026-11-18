// Accès réseau du moteur : délai maximal, identification honnête, une seule nouvelle tentative.
export const AGENT = 'GauchiseTesParents-moteur/1.0 (+https://gauchise-tes-parents.github.io ; education populaire, sans IA)';
export const pause = (ms) => new Promise((r) => setTimeout(r, ms));

export async function lire(url, { fetchImpl = fetch, type = 'text', delai = 20000 } = {}) {
  let derniere;
  for (let essai = 0; essai < 2; essai += 1) {
    const ctrl = new AbortController();
    const minuterie = setTimeout(() => ctrl.abort(), delai);
    try {
      const r = await fetchImpl(url, { headers: { 'user-agent': AGENT, accept: type === 'json' ? 'application/json' : 'text/html' }, signal: ctrl.signal });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      return type === 'json' ? await r.json() : await r.text();
    } catch (e) { derniere = e; await pause(1500); } finally { clearTimeout(minuterie); }
  }
  throw new Error(`${url} : ${derniere?.message || derniere}`);
}
