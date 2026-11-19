// Détecteur de direct de « Gauchise tes parents » (onglet « Direct »).
// - GET /statut : { enDirect, plateforme, twitch: {enDirect, titre}, youtube: {enDirect, videoId, titre}, verifie_le }
//   Aucune donnée sur le visiteur n'est lue ni enregistrée (ni IP, ni cookie, ni identifiant).
// - Twitch : API officielle Helix (/streams), jeton d'application obtenu avec TWITCH_CLIENT_ID + secret TWITCH_CLIENT_SECRET.
// - YouTube : page publique https://www.youtube.com/@<chaîne>/live (sans clé d'API) ; quand un live est en cours,
//   elle renvoie vers la vidéo du direct (lien « canonical » watch?v=…) et signale « isLiveNow ».
// - Le statut est mis en cache CACHE_SECONDES (60 s par défaut) : quel que soit le nombre de visiteurs,
//   Twitch et YouTube sont interrogés au plus une fois par minute et par instance.

const VIDEO_ID = /^[A-Za-z0-9_-]{11}$/;
let jeton = null; // { valeur, expire } — jeton d'application Twitch, réutilisé jusqu'à son expiration
let memo = null;  // { cle, expire, statut } — dernier statut calculé

export function _reinitialiser() { jeton = null; memo = null; }

/** Analyse la page « /live » d'une chaîne YouTube. */
export function analyserPageYoutube(html) {
  const s = String(html || '');
  const canon = s.match(/<link rel="canonical" href="https:\/\/www\.youtube\.com\/watch\?v=([A-Za-z0-9_-]{11})"/);
  const enDirect = Boolean(canon) && /"isLiveNow":\s*true/.test(s);
  if (!enDirect) return { enDirect: false };
  const t = s.match(/<meta name="title" content="([^"]{1,300})"/);
  return { enDirect: true, videoId: canon[1], titre: t ? decoder(t[1]) : null };
}

function decoder(x) {
  return x.replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, '’').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
}

async function jetonTwitch(env, fetchImpl) {
  if (jeton && jeton.expire > Date.now()) return jeton.valeur;
  const corps = new URLSearchParams({ client_id: env.TWITCH_CLIENT_ID, client_secret: env.TWITCH_CLIENT_SECRET, grant_type: 'client_credentials' });
  const r = await fetchImpl('https://id.twitch.tv/oauth2/token', { method: 'POST', body: corps });
  if (!r.ok) throw new Error(`jeton Twitch refusé (${r.status})`);
  const d = await r.json();
  jeton = { valeur: d.access_token, expire: Date.now() + Math.max(60, (Number(d.expires_in) || 3600) - 300) * 1000 };
  return jeton.valeur;
}

export async function statutTwitch(env, fetchImpl = fetch) {
  if (!env.TWITCH_CLIENT_ID || !env.TWITCH_CLIENT_SECRET || !env.TWITCH_LOGIN) return { enDirect: false, erreur: 'Twitch non configuré' };
  const appel = async () => fetchImpl(`https://api.twitch.tv/helix/streams?user_login=${encodeURIComponent(env.TWITCH_LOGIN)}`, {
    headers: { 'client-id': env.TWITCH_CLIENT_ID, authorization: `Bearer ${await jetonTwitch(env, fetchImpl)}` },
  });
  let r = await appel();
  if (r.status === 401) { jeton = null; r = await appel(); }
  if (!r.ok) return { enDirect: false, erreur: `Twitch indisponible (${r.status})` };
  const d = await r.json();
  const live = (d.data || []).find((x) => x.type === 'live');
  return live ? { enDirect: true, titre: String(live.title || '').slice(0, 300) || null } : { enDirect: false };
}

export async function statutYoutube(env, fetchImpl = fetch) {
  if (!env.YOUTUBE_HANDLE) return { enDirect: false, erreur: 'YouTube non configuré' };
  const r = await fetchImpl(`https://www.youtube.com/@${encodeURIComponent(env.YOUTUBE_HANDLE)}/live`, {
    headers: { 'accept-language': 'fr-FR,fr;q=0.9', 'user-agent': 'Mozilla/5.0 (compatible; gauchise-direct/1.0)', cookie: 'SOCS=CAI; CONSENT=YES+1' },
    redirect: 'follow',
  });
  if (!r.ok) return { enDirect: false, erreur: `YouTube indisponible (${r.status})` };
  return analyserPageYoutube(await r.text());
}

/** Statut combiné ; si les deux plateformes sont en direct, Twitch est proposé en premier. */
export async function statut(env, fetchImpl = fetch) {
  const [tw, yt] = await Promise.all([
    statutTwitch(env, fetchImpl).catch((e) => ({ enDirect: false, erreur: String(e.message || e) })),
    statutYoutube(env, fetchImpl).catch((e) => ({ enDirect: false, erreur: String(e.message || e) })),
  ]);
  const plateforme = tw.enDirect ? 'twitch' : yt.enDirect ? 'youtube' : null;
  return {
    enDirect: Boolean(plateforme), plateforme,
    twitch: { enDirect: tw.enDirect, titre: tw.titre || null, login: env.TWITCH_LOGIN || null, ...(tw.erreur ? { erreur: tw.erreur } : {}) },
    youtube: { enDirect: yt.enDirect, videoId: VIDEO_ID.test(yt.videoId || '') ? yt.videoId : null, titre: yt.titre || null, chaine: env.YOUTUBE_HANDLE || null, ...(yt.erreur ? { erreur: yt.erreur } : {}) },
    verifie_le: new Date().toISOString(),
  };
}

export function createHandler({ fetchImpl = (...a) => fetch(...a) } = {}) {
  return async function handle(request, env) {
    const url = new URL(request.url);
    const origines = String(env.ALLOWED_ORIGINS || '').split(',').map((s) => s.trim()).filter(Boolean);
    const origin = request.headers.get('origin') || '';
    const cors = origines.includes(origin) ? { 'access-control-allow-origin': origin, vary: 'origin' } : {};
    const cache = Math.max(15, Number(env.CACHE_SECONDES) || 60);
    const json = (status, obj) => new Response(JSON.stringify(obj), { status, headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': `public, max-age=${Math.min(cache, 30)}`, ...cors } });

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: cors['access-control-allow-origin'] ? 204 : 403, headers: { ...cors, 'access-control-allow-methods': 'GET', 'access-control-max-age': '86400' } });
    }
    if (url.pathname === '/statut' && request.method === 'GET') {
      const cle = `${env.TWITCH_LOGIN}|${env.YOUTUBE_HANDLE}`;
      if (!memo || memo.cle !== cle || memo.expire <= Date.now()) {
        memo = { cle, expire: Date.now() + cache * 1000, statut: await statut(env, fetchImpl) };
      }
      return json(200, memo.statut);
    }
    return json(404, { erreur: 'introuvable' });
  };
}
