// Collecteur des questions restées sans fiche (moteur interne de « Gauchise tes parents », v15).
// - POST /questions {texte} : enregistre UNIQUEMENT le texte de la question (nettoyé), sans adresse IP, sans cookie,
//   sans identifiant ; envoi déclenché par un clic explicite sur le site (« Envoyer anonymement ma question »).
// - GET /export (en-tête Authorization: Bearer <EXPORT_TOKEN>) : liste les questions pour le moteur (GitHub Actions) ;
//   ?purger=1 les supprime après lecture.
// Stockage : Cloudflare KV (binding QUESTIONS), expiration automatique après 90 jours.
// Limitation d'abus : compteur par jour sur une empreinte salée de l'adresse IP (l'IP elle-même n'est jamais écrite),
// effacé au bout de 24 h.

export const LIMITES = { min: 6, max: 300, parJour: 20, ttlJours: 90 };

/** Nettoie une question : retire adresses e-mail, numéros de téléphone et liens ; espaces normalisés. */
export function nettoyer(texte) {
  return String(texte || '')
    .replace(/[\u0000-\u001f\u007f]/g, ' ')
    .replace(/\S+@\S+\.\S+/g, '[adresse retirée]')
    .replace(/(\+33|0)\s*[1-9](?:[\s.-]*\d{2}){4}/g, '[numéro retiré]')
    .replace(/https?:\/\/\S+|www\.\S+/gi, '[lien retiré]')
    .replace(/\s+/g, ' ')
    .trim();
}

async function sha256(s) {
  const d = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return [...new Uint8Array(d)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

export function createHandler() {
  return async function handle(request, env) {
    const url = new URL(request.url);
    const origines = String(env.ALLOWED_ORIGINS || '').split(',').map((s) => s.trim()).filter(Boolean);
    const origin = request.headers.get('origin') || '';
    const cors = origines.includes(origin) ? { 'access-control-allow-origin': origin, vary: 'origin' } : {};
    const json = (status, obj) => new Response(JSON.stringify(obj), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', ...cors } });

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: cors['access-control-allow-origin'] ? 204 : 403, headers: { ...cors, 'access-control-allow-methods': 'POST', 'access-control-allow-headers': 'content-type', 'access-control-max-age': '86400' } });
    }
    if (url.pathname === '/questions' && request.method === 'POST') {
      if (!cors['access-control-allow-origin']) return json(403, { erreur: 'origine non autorisée' });
      let body;
      try { body = await request.json(); } catch { return json(400, { erreur: 'requête illisible' }); }
      const texte = nettoyer(body?.texte);
      if (texte.length < LIMITES.min || texte.length > LIMITES.max) return json(400, { erreur: 'question trop courte ou trop longue' });
      const jour = new Date().toISOString().slice(0, 10);
      const ip = request.headers.get('cf-connecting-ip') || 'inconnue';
      const cle = `limite:${jour}:${(await sha256(`${env.SEL || 'sel'}|${jour}|${ip}`)).slice(0, 24)}`;
      const n = Number(await env.QUESTIONS.get(cle)) || 0;
      if (n >= LIMITES.parJour) return json(429, { erreur: 'trop de questions aujourd’hui' });
      await env.QUESTIONS.put(cle, String(n + 1), { expirationTtl: 86400 });
      const id = `q:${jour}:${(await sha256(`${Date.now()}|${Math.random()}|${texte}`)).slice(0, 16)}`;
      await env.QUESTIONS.put(id, JSON.stringify({ texte, jour }), { expirationTtl: LIMITES.ttlJours * 86400 });
      return json(201, { ok: true });
    }
    if (url.pathname === '/export' && request.method === 'GET') {
      const jeton = env.EXPORT_TOKEN || '';
      if (!jeton || request.headers.get('authorization') !== `Bearer ${jeton}`) return json(401, { erreur: 'non autorisé' });
      const out = [];
      let cursor;
      do {
        const page = await env.QUESTIONS.list({ prefix: 'q:', cursor });
        for (const k of page.keys) { const v = await env.QUESTIONS.get(k.name); if (v) out.push({ id: k.name, ...JSON.parse(v) }); }
        cursor = page.list_complete ? undefined : page.cursor;
      } while (cursor);
      if (url.searchParams.get('purger') === '1') for (const q of out) await env.QUESTIONS.delete(q.id);
      return json(200, { questions: out });
    }
    return json(404, { erreur: 'introuvable' });
  };
}
