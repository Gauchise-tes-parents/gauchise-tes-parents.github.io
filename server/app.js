// Serveur HTTP sans dépendance : API JSON + fichiers statiques du frontend (compressés).
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { join, normalize, extname, sep } from 'node:path';
import { gzipSync } from 'node:zlib';
import { ROOT } from './config.js';
import { timingSafeEqual, createHash } from 'node:crypto';
import { loadLibrary, searchLibrary, summarize, freshness, LIBRARY_DIR } from './library.js';
import { buildKb, assetManifest } from './kbexport.js';
import { watchConfig, runWatch, readState, startScheduler } from './watch/veille.js';
import { localLookup } from './engine/knowledge.js';
import { validateAnalyseRequest, validateOptions, validateDuree } from './engine/options.js';
import { createEngine } from './engine/pipeline.js';
import { createAnthropicProvider } from './engine/providers/anthropic.js';
import { BudgetLedger } from './engine/cost.js';
import { EngineError } from './engine/util.js';
import { demoAnalyse } from './engine/demo.js';
import { SlidingWindowLimiter } from './rateLimit.js';
import { validateConversationRequest, runConversationTurn } from './engine/conversation.js';
import { sumCosts } from './engine/cost.js';
import { validateFeedback, storeFeedback } from './feedback.js';
import { VOLETS, RUBRIQUE_IDS, FIABILITES, LIMITS } from '../public/js/taxonomy.js';

const PUBLIC_DIR = join(ROOT, 'public');
const KB_PATHS = { '/kb/base.json': 'json', '/kb/manifest.json': 'manifest', '/asset-manifest.json': 'assets', '/kb/veille.json': 'veille' };
// Mode connecté avec une interface hébergée ailleurs (ex. GitHub Pages) : origine autorisée pour l'API.
const corsOrigin = process.env.CORS_ORIGIN && /^https:\/\/[a-z0-9.-]+(:\d+)?$/i.test(process.env.CORS_ORIGIN) ? process.env.CORS_ORIGIN : null;
const MAX_BODY = 16 * 1024;

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.json': 'application/json; charset=utf-8',
  '.webmanifest': 'application/manifest+json',
  '.txt': 'text/plain; charset=utf-8',
};
const COMPRESSIBLE = new Set(['.html', '.js', '.css', '.svg', '.json', '.webmanifest', '.txt']);

const SECURITY_HEADERS = {
  'Content-Security-Policy': "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'",
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'no-referrer',
  'X-Frame-Options': 'DENY',
  'Permissions-Policy': 'camera=(), microphone=(), geolocation=(), interest-cohort=()',
  'Cross-Origin-Opener-Policy': 'same-origin',
};

class HttpError extends Error {
  constructor(status, message, extra = {}) {
    super(message);
    this.status = status;
    this.extra = extra;
  }
}

function send(res, status, body, headers = {}) {
  const isJson = typeof body === 'object' && !Buffer.isBuffer(body);
  res.writeHead(status, {
    ...SECURITY_HEADERS,
    ...(isJson ? { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' } : {}),
    ...headers,
  });
  res.end(isJson ? JSON.stringify(body) : body);
}

async function readJson(req) {
  if (!(req.headers['content-type'] || '').includes('application/json')) throw new HttpError(415, 'Format attendu : JSON.');
  const chunks = [];
  let size = 0;
  for await (const chunk of req) {
    size += chunk.length;
    if (size > MAX_BODY) throw new HttpError(413, 'Requête trop volumineuse.');
    chunks.push(chunk);
  }
  try {
    return JSON.parse(Buffer.concat(chunks).toString('utf8') || '{}');
  } catch {
    throw new HttpError(400, 'JSON invalide.');
  }
}

function clientIp(req, trustProxy) {
  if (trustProxy) {
    const fwd = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim();
    if (fwd) return fwd;
  }
  return req.socket.remoteAddress || 'inconnu';
}

export function createApp(config, deps = {}) {
  const logger = deps.logger || console;
  const libraryDir = deps.libraryDir || LIBRARY_DIR;
  const library = deps.library || loadLibrary(libraryDir, logger);
  const wc = deps.watchConfig || watchConfig(process.env, ROOT);
  // Base téléchargeable pour le mode autonome (recalculée après une veille).
  let kbCache = null;
  const kbFiles = () => {
    if (!kbCache) {
      const st = readState(wc);
      const { json, manifest } = buildKb(library, { veille: { derniere_reussite: st.derniere_reussite, prochaine: st.prochaine } });
      kbCache = { json, manifest: JSON.stringify(manifest), assets: JSON.stringify(assetManifest(PUBLIC_DIR)) };
    }
    return kbCache;
  };
  const reloadLibrary = () => {
    const fresh = loadLibrary(libraryDir, logger);
    library.splice(0, library.length, ...fresh);
    kbCache = null;
  };
  const freshOpts = { staleDays: config.libraryStaleDays, ...(deps.today ? { today: deps.today } : {}) };
  const ledger = deps.ledger || new BudgetLedger({ file: config.usageFile, dailyUsd: config.dailyBudgetUsd, monthlyUsd: config.monthlyBudgetUsd });
  const provider = deps.provider || createAnthropicProvider(config, { fetchImpl: deps.fetchImpl || fetch });
  const engine = createEngine({ config, provider, library, ledger, logger });
  const windowMs = config.perIpWindowMinutes * 60 * 1000;
  const limiters = {
    analyse: new SlidingWindowLimiter({ limit: config.perIpAnalysisLimit, windowMs }),
    strategie: new SlidingWindowLimiter({ limit: config.perIpStrategyLimit, windowMs }),
    feedback: new SlidingWindowLimiter({ limit: 10, windowMs }),
    conversation: new SlidingWindowLimiter({ limit: config.perIpConversationLimit ?? 40, windowMs }),
    // plafond global (toutes adresses confondues) : protège le budget même si les adresses changent
    conversationGlobal: new SlidingWindowLimiter({ limit: config.globalConversationPerHour ?? 400, windowMs: 3600 * 1000 }),
  };
  const staticCache = new Map();
  let scheduler = { next: () => null, stop() {} };
  const veilleStatus = () => {
    const st = readState(wc);
    const next = scheduler.next?.();
    const externe = process.env.WATCH_EXTERNAL_SCHEDULE || '';
    return {
      statut: wc.enabled || externe ? 'actif' : 'inactif',
      planificateur: wc.enabled ? 'serveur Node (WATCH_ENABLED=1)' : externe || null,
      intervalle_heures: wc.enabled ? wc.intervalHours : null,
      derniere_reussite: st.derniere_reussite,
      derniere_tentative: st.derniere_tentative,
      prochaine: next ? next.toISOString() : null,
      application_automatique: wc.autoApply,
      dernier_rapport: st.dernier_rapport,
    };
  };
  const runVeille = async (manual) => {
    const report = await runWatch({ wc, config, provider, library, ledger, libraryDir, logger, manual, fetchImpl: deps.fetchImpl || fetch });
    reloadLibrary();
    return report;
  };
  if (deps.scheduler !== false && wc.enabled && config.liveMode) scheduler = startScheduler({ wc, run: () => runVeille(false), logger });

  const limit = (name, req) => {
    const r = limiters[name].take(clientIp(req, config.trustProxy));
    if (!r.ok) throw new HttpError(429, `Doucement ! Trop de demandes en peu de temps. Réessaie dans ${Math.max(1, Math.ceil(r.retryAfterSec / 60))} min.`, { retryAfter: r.retryAfterSec });
  };
  const requireLive = () => {
    if (!config.liveMode) throw new HttpError(503, "Mode démonstration : cette fonction a besoin du moteur de recherche, qui n'est pas configuré sur ce serveur. Rien n'est inventé à la place.", { mode: 'demo' });
  };
  const analyseId = (v) => (typeof v === 'string' && /^[A-Za-z0-9-]{8,80}$/.test(v) ? v : null);
  const ficheWithFreshness = (e) => ({ ...e, fraicheur: freshness(e, freshOpts) });

  const routes = {
    'GET /api/status': async () => ({
      mode: config.liveMode ? 'live' : 'demo',
      recherche_web: config.liveMode,
      consultation_documents: config.liveMode && config.maxFetches > 0,
      modeles: config.liveMode ? { recherche: config.researchModel, strategie: config.strategyModel } : null,
      budget_disponible: config.liveMode ? ledger.canSpend(config.estimateResearchUsd) : null,
      fiches: library.length,
    }),

    'GET /api/library': async (req, url) => {
      const q = (url.searchParams.get('q') || '').slice(0, 120);
      const volet = url.searchParams.get('volet');
      const v = VOLETS.find((x) => x.id === volet);
      const st = url.searchParams.get('sous_theme');
      const rubrique = RUBRIQUE_IDS.includes(url.searchParams.get('rubrique')) ? url.searchParams.get('rubrique') : null;
      const fiabilite = FIABILITES[url.searchParams.get('fiabilite')] ? url.searchParams.get('fiabilite') : null;
      return {
        fiches: searchLibrary(library, q, v ? v.id : null, v?.sousThemes.includes(st) ? st : null, { rubrique, fiabilite })
          .map((e) => summarize(e, freshOpts)),
      };
    },

    // Recherche instantanée dans la base locale (aucun appel externe, aucun coût).
    'GET /api/kb/search': async (req, url) => {
      const q = (url.searchParams.get('q') || '').slice(0, LIMITS.claimMax);
      if (q.trim().length < 3) throw new HttpError(400, 'Question trop courte.');
      return { ...localLookup(library, q, { freshOpts }).payload, recherche_web_disponible: config.liveMode };
    },

    'POST /api/analyse': async (req) => {
      const v = validateAnalyseRequest(await readJson(req));
      if (!v.ok) throw new HttpError(400, v.error);
      // 1. Base locale d'abord.
      const lookup = localLookup(library, v.value.claim, { freshOpts, fraiche: v.value.fraiche });
      if (!config.liveMode) return { ...demoAnalyse(v.value, library, freshOpts), base_locale: lookup.payload };
      limit('analyse', req);
      const best = lookup.matches[0];
      // 2. Fiche forte, stable et à jour : réponse construite sur la fiche, sans recherche web.
      if (config.kbDirectAnswer && best && !lookup.payload.decision.web_complementaire) {
        return { ...(await engine.fromFiche(best.fiche, v.value)), base_locale: lookup.payload };
      }
      // 3. Sinon : recherche web complémentaire, comparée à la fiche la plus proche si elle est forte.
      const r = await engine.analyse(v.value, { fiche: best?.force === 'forte' ? best.fiche : null });
      return { ...r, base_locale: lookup.payload };
    },

    'POST /api/strategie': async (req) => {
      const body = await readJson(req);
      requireLive();
      limit('strategie', req);
      const opts = validateOptions(body);
      if (typeof body.fiche_id === 'string') {
        const fiche = library.find((e) => e.id === body.fiche_id);
        if (!fiche) throw new HttpError(404, 'Fiche introuvable.');
        return engine.fromFiche(fiche, opts);
      }
      const id = analyseId(body.analyse_id);
      if (!id) throw new HttpError(400, 'Analyse inconnue.');
      return engine.switchStrategy(id, opts);
    },

    'POST /api/reformuler': async (req) => {
      const body = await readJson(req);
      requireLive();
      limit('strategie', req);
      const id = analyseId(body.analyse_id);
      if (!id) throw new HttpError(400, 'Analyse inconnue.');
      const replique = typeof body.replique === 'string' ? body.replique.slice(0, 900) : '';
      return engine.rephrase(id, { ...validateOptions(body), variante: body.variante === 'pedagogique' ? 'pedagogique' : 'variante', replique });
    },

    'POST /api/demonstration': async (req) => {
      const body = await readJson(req);
      requireLive();
      limit('strategie', req);
      const id = analyseId(body.analyse_id);
      const duree = validateDuree(body.duree);
      if (!id || !duree) throw new HttpError(400, 'Analyse ou durée invalide.');
      return engine.speech(id, { ...validateOptions(body), duree });
    },

    // Un tour de conversation (mode connecté). Pas de limite de tours : seules des limites techniques
    // (taille, fréquence, budget) s'appliquent, et elles sont annoncées clairement.
    'POST /api/conversation': async (req) => {
      const body = await readJson(req);
      requireLive();
      limit('conversation', req);
      const g = limiters.conversationGlobal.take('global');
      if (!g.ok) throw new HttpError(429, `Le site reçoit beaucoup de demandes en ce moment. Réessaie dans ${Math.max(1, Math.ceil(g.retryAfterSec / 60))} min ; ta conversation est conservée et le mode autonome reste disponible.`, { retryAfter: g.retryAfterSec });
      const v = validateConversationRequest(body, library);
      if (!v.ok) throw new HttpError(v.status || 400, v.error);
      const estimate = config.estimateConversationUsd ?? 0.02;
      if (!ledger.canSpend(estimate)) throw new HttpError(503, 'Le budget du mode connecté est atteint pour aujourd’hui. Ta conversation est conservée : tu peux continuer avec le moteur hors ligne, ou revenir plus tard.', { mode: 'quota' });
      const opts = validateOptions(body);
      const { intervention, requests } = await runConversationTurn({ provider, config, req: v.value, interlocuteur: opts.interlocuteur, mode: opts.mode });
      const c = sumCosts(requests, config.pricing, config.fallbackPricing);
      ledger.record(c.usd);
      return { intervention, origine: 'connecte', tour: v.value.tour };
    },

    'GET /api/veille/status': async () => veilleStatus(),

    // Lancement manuel : protégé par un jeton (une veille coûte des recherches web).
    'POST /api/veille/run': async (req) => {
      const body = await readJson(req);
      if (!wc.adminToken) throw new HttpError(403, 'Lancement manuel désactivé : aucun jeton WATCH_ADMIN_TOKEN configuré sur le serveur.');
      const given = createHash('sha256').update(String(body.token || '')).digest();
      const expected = createHash('sha256').update(wc.adminToken).digest();
      if (!timingSafeEqual(given, expected)) throw new HttpError(403, 'Jeton invalide.');
      requireLive();
      const r = await runVeille(true);
      if (r.statut === 'deja_en_cours') return { message: r.message };
      return { message: `Veille ${r.statut} : ${r.compteurs.verifiees} vérifiées, ${r.compteurs.en_attente} en attente, ${r.compteurs.rejetees} rejetées.`, rapport: r.id };
    },

    'POST /api/feedback': async (req) => {
      limit('feedback', req);
      const v = validateFeedback(await readJson(req));
      if (!v.ok) throw new HttpError(400, v.error);
      if (config.storeFeedback) await storeFeedback(config.feedbackFile, v.value);
      return { ok: true, message: 'Merci ! Ton retour a bien été enregistré.' };
    },
  };

  async function serveStatic(req, res, pathname) {
    let rel;
    try { rel = decodeURIComponent(pathname); } catch { return send(res, 400, { erreur: 'URL invalide.' }); }
    if (rel === '/' || !extname(rel)) rel = '/index.html'; // routage côté client
    const file = normalize(join(PUBLIC_DIR, rel));
    if (!file.startsWith(PUBLIC_DIR + sep)) return send(res, 403, { erreur: 'Accès refusé.' });
    try {
      const st = await stat(file);
      if (!st.isFile()) throw new Error('not a file');
      const ext = extname(file);
      const headers = { 'Content-Type': MIME[ext] || 'application/octet-stream', 'Cache-Control': ext === '.html' || /(sw|config)\.js$/.test(file) ? 'no-cache' : 'public, max-age=3600', Vary: 'Accept-Encoding' };
      const gzipOk = COMPRESSIBLE.has(ext) && /\bgzip\b/.test(req.headers['accept-encoding'] || '');
      const cacheKey = `${file}:${st.mtimeMs}:${gzipOk}`;
      let data = staticCache.get(cacheKey);
      if (!data) {
        data = await readFile(file);
        if (gzipOk) data = gzipSync(data);
        staticCache.set(cacheKey, data);
      }
      if (gzipOk) headers['Content-Encoding'] = 'gzip';
      return send(res, 200, req.method === 'HEAD' ? '' : data, headers);
    } catch {
      return send(res, 404, 'Introuvable', { 'Content-Type': 'text/plain; charset=utf-8' });
    }
  }

  async function handler(req, res) {
    const started = Date.now();
    let url;
    try { url = new URL(req.url, 'http://localhost'); } catch { return send(res, 400, { erreur: 'URL invalide.' }); }
    try {
      if (req.method === 'GET' && KB_PATHS[url.pathname]) {
        const files = kbFiles();
        const body = url.pathname === '/kb/veille.json' ? JSON.stringify(veilleStatus()) : files[KB_PATHS[url.pathname]];
        const gzipOk = /\bgzip\b/.test(req.headers['accept-encoding'] || '');
        return send(res, 200, gzipOk ? gzipSync(body) : body, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-cache', ...(gzipOk ? { 'Content-Encoding': 'gzip' } : {}) });
      }
      if (url.pathname.startsWith('/api/') && corsOrigin) {
        res.setHeader('Access-Control-Allow-Origin', corsOrigin);
        res.setHeader('Vary', 'Origin');
        if (req.method === 'OPTIONS') return send(res, 204, '', { 'Access-Control-Allow-Methods': 'GET, POST', 'Access-Control-Allow-Headers': 'content-type', 'Access-Control-Max-Age': '600' });
      }
      if (url.pathname.startsWith('/api/')) {
        const libMatch = url.pathname.match(/^\/api\/library\/([a-z0-9-]{3,60})$/);
        if (req.method === 'GET' && libMatch) {
          const entry = library.find((e) => e.id === libMatch[1]);
          if (!entry) throw new HttpError(404, 'Fiche introuvable.');
          return send(res, 200, ficheWithFreshness(entry));
        }
        const route = routes[`${req.method} ${url.pathname}`];
        if (!route) throw new HttpError(404, 'Route inconnue.');
        return send(res, 200, await route(req, url));
      }
      if (req.method !== 'GET' && req.method !== 'HEAD') throw new HttpError(405, 'Méthode non autorisée.');
      return await serveStatic(req, res, url.pathname);
    } catch (err) {
      if (err instanceof HttpError) {
        const headers = err.extra.retryAfter ? { 'Retry-After': String(err.extra.retryAfter) } : {};
        return send(res, err.status, { erreur: err.message, ...(err.extra.mode ? { mode: err.extra.mode } : {}) }, headers);
      }
      if (err instanceof EngineError) {
        logger.warn?.(`[moteur] ${err.code}`);
        return send(res, err.status, { erreur: err.message, code: err.code, relancer: err.retry });
      }
      // jamais le message brut : il pourrait reprendre un extrait de la question ou de la réponse du fournisseur
      logger.error?.('[serveur] erreur inattendue', err?.name || 'Error', err?.code || '');
      return send(res, 500, { erreur: 'Erreur interne. Réessaie plus tard.', relancer: true });
    } finally {
      if (url?.pathname.startsWith('/api/')) logger.info?.(`${req.method} ${url.pathname} ${res.statusCode} ${Date.now() - started}ms`);
    }
  }

  return { server: createServer(handler), library, ledger, engine, reloadLibrary, runVeille, scheduler: () => scheduler };
}
