// Protection contre les abus : limite par visiteur (adresse IP hachée, en mémoire, jamais stockée ni journalisée)
// et plafond global quotidien (KV Cloudflare si une liaison GTP_KV est déclarée, sinon mémoire de l'instance).
// Recommandé en production : une règle « Rate limiting » Cloudflare (WAF) en plus, appliquée avant le Worker.

async function hacher(texte, sel) {
  const d = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(`${sel}|${texte}`));
  return btoa(String.fromCharCode(...new Uint8Array(d))).slice(0, 22);
}

export class LimiteurMemoire {
  constructor({ limite, fenetreMs, maintenant = () => Date.now() }) {
    this.limite = limite; this.fenetreMs = fenetreMs; this.maintenant = maintenant; this.hits = new Map();
  }
  prendre(cle) {
    const t = this.maintenant();
    const l = (this.hits.get(cle) || []).filter((x) => t - x < this.fenetreMs);
    if (l.length >= this.limite) { this.hits.set(cle, l); return { ok: false, apres: Math.ceil((this.fenetreMs - (t - l[0])) / 1000) }; }
    l.push(t); this.hits.set(cle, l);
    if (this.hits.size > 20000) for (const [k, v] of this.hits) if (!v.some((x) => t - x < this.fenetreMs)) this.hits.delete(k);
    return { ok: true, apres: 0 };
  }
}

const jour = (d = new Date()) => d.toISOString().slice(0, 10);

export function creerLimites(env, { maintenant = () => Date.now() } = {}) {
  const parVisiteur = new LimiteurMemoire({ limite: Number(env.LIMITE_PAR_VISITEUR || 12), fenetreMs: Number(env.FENETRE_MINUTES || 10) * 60000, maintenant });
  const plafondJour = Number(env.PLAFOND_QUOTIDIEN || 800);
  const memoire = { jour: jour(), n: 0 };
  // le sel change chaque jour : impossible de relier deux jours d'activité d'une même adresse
  const sel = () => `${env.SEL_LIMITES || 'gtp'}|${jour(new Date(maintenant()))}`;
  return {
    async visiteur(ip) { return parVisiteur.prendre(await hacher(ip || 'inconnu', sel())); },
    async global() {
      if (!plafondJour) return { ok: true };
      const j = jour(new Date(maintenant()));
      if (env.GTP_KV) {
        const cle = `compte:${j}`;
        const n = Number((await env.GTP_KV.get(cle)) || 0);
        if (n >= plafondJour) return { ok: false };
        await env.GTP_KV.put(cle, String(n + 1), { expirationTtl: 172800 });
        return { ok: true };
      }
      if (memoire.jour !== j) { memoire.jour = j; memoire.n = 0; }
      if (memoire.n >= plafondJour) return { ok: false };
      memoire.n += 1;
      return { ok: true };
    },
  };
}
