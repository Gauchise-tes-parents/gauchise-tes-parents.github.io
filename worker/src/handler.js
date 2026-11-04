// Backend IA de « Gauchise tes parents » (Cloudflare Worker, ou tout environnement qui fournit fetch/Request/Response).
// Parcours d'une question : contrôle → limites anti-abus → repérage des thèmes et des fiches de la bibliothèque
// (même moteur que l'application) → consigne + extraits vérifiés → Gemini (+ recherche Google si activée)
// → contrôle de la réponse (aucun lien inventé) → réponse JSON qui dit d'où vient chaque élément.
//
// Confidentialité : la question n'est ni stockée, ni journalisée ; l'adresse IP n'est utilisée que hachée, en mémoire,
// pour la limite anti-abus. Seule une réponse générique (question qui correspond à une fiche, sans contexte de
// conversation) peut être mise en cache une heure, sous une clé hachée.
import { analyserPhrase, resoudrePhrase } from '../../public/js/analyse.js';
import { createGeminiProvider, IaError, iaErreur } from './gemini.js';
import { consigneSysteme, documentsBibliotheque, messageUtilisateur, nettoyer, MODES_IA, VARIANTES_IA } from './prompt.js';
import { extraireJson, normaliser } from './parse.js';
import { creerLimites } from './limits.js';

export const VERSION_IA = '1';
const MAX_CORPS = 8 * 1024;
const MAX_QUESTION = 600;
const JETONS = { express: 700, gagner: 2200, convaincre: 1800, approfondir: 3500 };

const ENTETES = { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store', 'x-content-type-options': 'nosniff', 'referrer-policy': 'no-referrer' };

function origines(env) { return String(env.ALLOWED_ORIGINS || '').split(',').map((s) => s.trim().replace(/\/+$/, '')).filter(Boolean); }
function cors(req, env) {
  const o = req.headers.get('origin');
  const ok = o && origines(env).includes(o);
  return ok ? { 'access-control-allow-origin': o, 'access-control-allow-methods': 'GET, POST, OPTIONS', 'access-control-allow-headers': 'content-type', 'access-control-max-age': '86400', vary: 'Origin' } : { vary: 'Origin' };
}
const json = (req, env, status, body, extra = {}) => new Response(JSON.stringify(body), { status, headers: { ...ENTETES, ...cors(req, env), ...extra } });
const erreur = (req, env, e) => json(req, env, e.status || 500, { erreur: e.message, code: e.code || 'erreur', relancer: ['delai', 'reseau', 'service', 'vide', 'frequence'].includes(e.code) }, e.extra?.apres ? { 'retry-after': String(e.extra.apres) } : {});

async function lireCorps(req) {
  if (!(req.headers.get('content-type') || '').includes('application/json')) throw new IaError('format', 'Format attendu : JSON.', 415);
  const buf = await req.arrayBuffer();
  if (buf.byteLength > MAX_CORPS) throw new IaError('taille', 'Requête trop volumineuse.', 413);
  try { return JSON.parse(new TextDecoder().decode(buf) || '{}'); } catch { throw new IaError('format', 'JSON invalide.', 400); }
}

export function validerDemande(b) {
  const question = nettoyer(b?.question, MAX_QUESTION + 1);
  if (question.length < 3) throw new IaError('question', 'Écris une affirmation ou une question (au moins quelques mots).', 400);
  if (question.length > MAX_QUESTION) throw new IaError('question', `Question trop longue (${MAX_QUESTION} caractères au maximum).`, 400);
  const mode = MODES_IA.includes(b?.mode) ? b.mode : 'gagner';
  const variante = VARIANTES_IA.includes(b?.variante) ? b.variante : null;
  const contexte = Array.isArray(b?.contexte) ? b.contexte.slice(-4).map((c) => nettoyer(c, 300)).filter(Boolean) : [];
  return { question, mode, variante, contexte, relance: b?.relance === true };
}

/** Fiches de la bibliothèque qui répondent VRAIMENT aux thèmes de la question (jamais une fiche voisine forcée). */
export function fichesPertinentes(question, fiches) {
  const lib = fiches.filter((f) => f.type !== 'science');
  const r = resoudrePhrase(question, lib);
  const an = r.an || analyserPhrase(question, { bibliotheque: lib });
  const ids = [...new Set([r.fiche?.id, ...an.arguments.filter((a) => a.fiche).map((a) => a.fiche.id)].filter(Boolean))].slice(0, 3);
  return { analyse: an, fiches: ids.map((id) => lib.find((f) => f.id === id)).filter(Boolean) };
}

async function hacherCle(t) {
  const d = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(t));
  return [...new Uint8Array(d)].map((x) => x.toString(16).padStart(2, '0')).join('');
}

export function createHandler({ fiches, fetchImpl, cache = (typeof caches !== 'undefined' ? caches.default : null), journal = console } = {}) {
  let limites = null; let limitesEnv = null;
  return async function handle(req, env = {}) {
    const url = new URL(req.url);
    const t0 = Date.now();
    if (req.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors(req, env) });
    if (req.headers.get('origin') && origines(env).length && !origines(env).includes(req.headers.get('origin'))) return json(req, env, 403, { erreur: 'Origine non autorisée.', code: 'origine' });
    const provider = createGeminiProvider(env, { fetchImpl });
    const recherche = String(env.GEMINI_RECHERCHE ?? '1') !== '0';
    if (url.pathname === '/api/ia/statut' && req.method === 'GET') {
      const manque = [!env.GEMINI_API_KEY && 'cle', !provider.modele && 'modele'].filter(Boolean);
      return json(req, env, 200, { disponible: provider.disponible(), manque, fournisseur: 'gemini', modele: provider.modele || null, recherche_google: provider.disponible() && recherche, version: VERSION_IA });
    }
    if (url.pathname !== '/api/ia' || req.method !== 'POST') return json(req, env, 404, { erreur: 'Adresse inconnue.', code: 'introuvable' });
    let statut = 500;
    try {
      const d = validerDemande(await lireCorps(req));
      if (!provider.disponible()) throw iaErreur('config');
      if (!limites || limitesEnv !== env) { limites = creerLimites(env); limitesEnv = env; }
      const ip = req.headers.get('cf-connecting-ip') || '';
      const v = await limites.visiteur(ip);
      if (!v.ok) throw new IaError('frequence', `Doucement : trop de demandes en peu de temps. Réessaie dans ${Math.max(1, Math.ceil(v.apres / 60))} min. La bibliothèque reste disponible.`, 429, { apres: v.apres });
      const { analyse, fiches: choisies } = fichesPertinentes(d.question, fiches);
      // cache : seulement une réponse générique (question rattachée à une fiche, sans contexte personnel, pas une relance)
      const cachable = Boolean(cache) && choisies.length && !d.contexte.length && !d.relance;
      const cle = cachable ? new Request(`https://cache.gtp.invalid/ia/${await hacherCle(`${VERSION_IA}|${provider.modele}|${d.mode}|${d.variante}|${d.question.toLowerCase()}`)}`) : null;
      if (cle) {
        const hit = await cache.match(cle);
        if (hit) { statut = 200; const corps = await hit.json(); return json(req, env, 200, { ...corps, depuis_cache: true }); }
      }
      const g = await limites.global();
      if (!g.ok) throw new IaError('quota', 'Le plafond quotidien de réponses par intelligence artificielle est atteint pour ce site. Réessaie demain ; la bibliothèque reste disponible.', 429);
      const documents = documentsBibliotheque(choisies);
      const sortie = await provider.generate({
        system: consigneSysteme(d.mode, { variante: d.variante, recherche }),
        user: messageUtilisateur({ question: d.question, analyse, documents, contexte: d.contexte }),
        search: recherche,
        maxTokens: JETONS[d.mode],
        temperature: d.relance ? 0.8 : 0.4,
      });
      const lu = normaliser(extraireJson(sortie.text), { mode: d.mode, docs: documents.docs, recherche: sortie.recherche });
      if (!lu) throw iaErreur('vide');
      const corps = {
        mode: d.mode,
        variante: d.variante,
        analyse: { themes: analyse.arguments.map((a) => a.label).filter(Boolean), domaines: (analyse.domaines || []).map((x) => x.label) },
        origine: {
          bibliotheque: choisies.map((f) => ({ id: f.id, affirmation: f.affirmation })),
          ia: { fournisseur: 'gemini', modele: sortie.modele },
          recherche: { effectuee: sortie.recherche.pages.length > 0 || sortie.recherche.requetes.length > 0, requetes: sortie.recherche.requetes },
        },
        reponse: lu.reponse,
        sources: lu.sources,
        tronquee: sortie.tronquee,
        genere_le: new Date().toISOString(),
      };
      if (cle) await cache.put(cle, new Response(JSON.stringify(corps), { headers: { 'content-type': 'application/json', 'cache-control': 'max-age=3600' } })).catch(() => {});
      statut = 200;
      return json(req, env, 200, corps);
    } catch (e) {
      const err = e instanceof IaError ? e : iaErreur('service');
      statut = err.status;
      return erreur(req, env, err);
    } finally {
      // journal minimal : jamais la question, jamais l'adresse IP
      journal.log?.(`ia ${req.method} ${url.pathname} ${statut} ${Date.now() - t0}ms`);
    }
  };
}
