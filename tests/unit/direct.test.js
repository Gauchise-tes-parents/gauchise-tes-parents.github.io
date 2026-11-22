// Onglet « Direct » (v15) : détecteur de live (worker-direct/) et adresses du lecteur et du chat.
import { test, describe, beforeEach } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { createHandler, analyserPageYoutube, statut, _reinitialiser } from '../../worker-direct/src/handler.js';
import { CHAINES, plateformesEnDirect, urlLecteur, urlChat, urlLive, ORIGINES_LECTEURS } from '../../public/js/direct.js';

const ENV = { ALLOWED_ORIGINS: 'https://gauchise-tes-parents.github.io', TWITCH_CLIENT_ID: 'id', TWITCH_CLIENT_SECRET: 'secret', TWITCH_LOGIN: 'martyducanda', YOUTUBE_HANDLE: 'Martyducanda', CACHE_SECONDES: '60' };
const PAGE_LIVE = '<html><link rel="canonical" href="https://www.youtube.com/watch?v=abcDEF12345"><meta name="title" content="Débat &amp; questions"><script>{"isLiveNow":true}</script></html>';
const PAGE_OFF = '<html><link rel="canonical" href="https://www.youtube.com/channel/UCxyz"><script>{"isLiveNow":false}</script></html>';

function faux({ twitch = false, youtube = PAGE_OFF, appels = [] } = {}) {
  return async (url, opts = {}) => {
    appels.push(String(url));
    if (String(url).startsWith('https://id.twitch.tv/oauth2/token')) return new Response(JSON.stringify({ access_token: 'tok', expires_in: 3600 }), { status: 200 });
    if (String(url).startsWith('https://api.twitch.tv/helix/streams')) {
      assert.equal(opts.headers['client-id'], 'id');
      return new Response(JSON.stringify({ data: twitch ? [{ type: 'live', title: 'Live du soir' }] : [] }), { status: 200 });
    }
    if (String(url).startsWith('https://www.youtube.com/@Martyducanda/live')) return new Response(youtube, { status: 200 });
    throw new Error(`appel inattendu ${url}`);
  };
}

describe('détecteur de direct', () => {
  beforeEach(() => _reinitialiser());

  test('YouTube : live détecté seulement avec la vidéo canonique ET isLiveNow', () => {
    assert.deepEqual(analyserPageYoutube(PAGE_LIVE), { enDirect: true, videoId: 'abcDEF12345', titre: 'Débat & questions' });
    assert.deepEqual(analyserPageYoutube(PAGE_OFF), { enDirect: false });
    assert.deepEqual(analyserPageYoutube(PAGE_LIVE.replace('true', 'false')), { enDirect: false }, 'vidéo programmée, pas encore en direct');
  });

  test('statut combiné : Twitch prioritaire, YouTube sinon, aucun sinon', async () => {
    assert.equal((await statut(ENV, faux({ twitch: true, youtube: PAGE_LIVE }))).plateforme, 'twitch');
    _reinitialiser();
    const s = await statut(ENV, faux({ youtube: PAGE_LIVE }));
    assert.equal(s.plateforme, 'youtube');
    assert.equal(s.youtube.videoId, 'abcDEF12345');
    _reinitialiser();
    assert.equal((await statut(ENV, faux())).enDirect, false);
  });

  test('sans secret Twitch : pas d’erreur, YouTube reste détecté', async () => {
    const s = await statut({ ...ENV, TWITCH_CLIENT_SECRET: '' }, faux({ youtube: PAGE_LIVE }));
    assert.equal(s.plateforme, 'youtube');
    assert.match(s.twitch.erreur, /non configuré/);
  });

  test('GET /statut : CORS limité au site, statut mis en cache (une vérification par minute)', async () => {
    const appels = [];
    const handle = createHandler({ fetchImpl: faux({ twitch: true, appels }) });
    const req = (origin) => new Request('https://direct.example/statut', { headers: origin ? { origin } : {} });
    const r1 = await handle(req('https://gauchise-tes-parents.github.io'), ENV);
    assert.equal(r1.status, 200);
    assert.equal(r1.headers.get('access-control-allow-origin'), 'https://gauchise-tes-parents.github.io');
    assert.equal((await r1.json()).plateforme, 'twitch');
    const n = appels.length;
    const r2 = await handle(req('https://autre.example'), ENV);
    assert.equal(r2.headers.get('access-control-allow-origin'), null);
    assert.equal(appels.length, n, 'deuxième demande servie depuis le cache');
    assert.equal((await handle(new Request('https://direct.example/autre'), ENV)).status, 404);
  });

  test('aucun secret dans la configuration versionnée du Worker', () => {
    const toml = readFileSync(new URL('../../worker-direct/wrangler.toml', import.meta.url), 'utf8');
    assert.ok(!/TWITCH_CLIENT_SECRET\s*=/.test(toml));
  });
});

describe('adresses du lecteur et du chat', () => {
  const S = { twitch: { enDirect: true }, youtube: { enDirect: true, videoId: 'abcDEF12345' } };
  test('plateformes en direct, Twitch d’abord ; YouTube exige un identifiant de vidéo valide', () => {
    assert.deepEqual(plateformesEnDirect(S), ['twitch', 'youtube']);
    assert.deepEqual(plateformesEnDirect({ youtube: { enDirect: true, videoId: '"><script>' } }), []);
    assert.deepEqual(plateformesEnDirect(null), []);
  });
  test('lecteurs officiels uniquement, son coupé au départ', () => {
    const tw = urlLecteur('twitch', S, 'gauchise-tes-parents.github.io');
    assert.match(tw, /^https:\/\/player\.twitch\.tv\/\?channel=martyducanda&parent=gauchise-tes-parents\.github\.io&autoplay=true&muted=true$/);
    assert.equal(urlLecteur('youtube', S, 'x'), 'https://www.youtube-nocookie.com/embed/abcDEF12345?autoplay=1&mute=1&playsinline=1');
    for (const u of [tw, urlLecteur('youtube', S, 'x')]) assert.ok(ORIGINES_LECTEURS.includes(new URL(u).origin));
    assert.match(urlLecteur('twitch', S, 'bad host<'), /parent=gauchise-tes-parents\.github\.io/);
  });
  test('le bouton du chat renvoie vers la plateforme du live', () => {
    assert.equal(urlChat('twitch', S), 'https://www.twitch.tv/popout/martyducanda/chat');
    assert.equal(urlChat('youtube', S), 'https://www.youtube.com/live_chat?is_popout=1&v=abcDEF12345');
    assert.equal(urlLive('youtube', S), 'https://www.youtube.com/watch?v=abcDEF12345');
    assert.equal(CHAINES.youtube.url, 'https://www.youtube.com/@Martyducanda');
  });
});

test('publication : sans détecteur, aucun cadre tiers ; avec détecteur, seuls les deux lecteurs officiels', async () => {
  const { execFileSync } = await import('node:child_process');
  const { mkdtempSync } = await import('node:fs');
  const { tmpdir } = await import('node:os');
  const { join } = await import('node:path');
  const root = new URL('../..', import.meta.url).pathname;
  const csp = (env) => {
    const out = join(mkdtempSync(join(tmpdir(), 'gtp-direct-')), 'site');
    execFileSync(process.execPath, ['scripts/build-static.js'], { cwd: root, env: { ...process.env, STATIC_OUT: out, GTP_API_BASE: '', GTP_IA_BASE: '', GTP_QUESTIONS_BASE: 'aucun', ...env }, stdio: 'pipe' });
    return { csp: readFileSync(join(out, 'index.html'), 'utf8').match(/Content-Security-Policy" content="([^"]+)"/)[1], config: readFileSync(join(out, 'config.js'), 'utf8') };
  };
  const sans = csp({ GTP_DIRECT_BASE: 'aucun' });
  assert.doesNotMatch(sans.csp, /frame-src/);
  assert.match(sans.config, /directBase: null/);
  const avec = csp({ GTP_DIRECT_BASE: 'https://gauchise-direct.exemple.workers.dev' });
  assert.match(avec.csp, /frame-src https:\/\/player\.twitch\.tv https:\/\/www\.youtube-nocookie\.com;/);
  assert.match(avec.csp, /connect-src 'self' https:\/\/gauchise-direct\.exemple\.workers\.dev/);
  assert.match(avec.config, /directBase: "https:\/\/gauchise-direct\.exemple\.workers\.dev"/);
  assert.match(avec.config, /kbRelais: "https:\/\/gauchise-direct\.exemple\.workers\.dev\/kb"/, 'relais de la base sur le même Worker');
  assert.match(sans.config, /kbRelais: null/);
  assert.throws(() => csp({ GTP_DIRECT_BASE: 'javascript:alert(1)' }));
});
