// Chargement de la configuration depuis les variables d'environnement (et un éventuel fichier .env).
// Aucune dépendance externe : le fichier .env est lu avec un petit analyseur maison.
import { readFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

export const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');

export function parseDotenv(text) {
  const out = {};
  for (const raw of text.split(/\r?\n/)) {
    const line = raw.trim();
    if (!line || line.startsWith('#')) continue;
    const eq = line.indexOf('=');
    if (eq === -1) continue;
    const key = line.slice(0, eq).trim();
    let val = line.slice(eq + 1).trim();
    if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
      val = val.slice(1, -1);
    }
    out[key] = val;
  }
  return out;
}

function loadDotenv() {
  const file = join(ROOT, '.env');
  if (!existsSync(file)) return;
  const parsed = parseDotenv(readFileSync(file, 'utf8'));
  for (const [k, v] of Object.entries(parsed)) {
    if (process.env[k] === undefined) process.env[k] = v; // l'environnement réel reste prioritaire
  }
}

const int = (v, d) => {
  const n = Number.parseInt(v, 10);
  return Number.isFinite(n) && n >= 0 ? n : d;
};

const num = (v, d) => {
  const n = Number.parseFloat(v);
  return Number.isFinite(n) && n >= 0 ? n : d;
};

export function loadConfig(env = null) {
  if (!env) {
    loadDotenv();
    env = process.env;
  }
  const apiKey = (env.ANTHROPIC_API_KEY || '').trim();
  const pricing = {};
  // Tarifs personnalisés facultatifs (USD par million de jetons) pour un modèle absent de la table intégrée.
  if (env.PRICE_INPUT_PER_MTOK && env.PRICE_OUTPUT_PER_MTOK) {
    const custom = { input: num(env.PRICE_INPUT_PER_MTOK, 2), output: num(env.PRICE_OUTPUT_PER_MTOK, 10), cacheRead: num(env.PRICE_CACHE_READ_PER_MTOK, 0) };
    for (const m of [env.RESEARCH_MODEL, env.STRATEGY_MODEL].filter(Boolean)) pricing[m] = custom;
  }
  return {
    port: int(env.PORT, 3000),
    host: env.HOST || '127.0.0.1',
    apiKey,
    // Moteur réel uniquement si une clé est fournie ET que le mode démo n'est pas forcé.
    liveMode: Boolean(apiKey) && env.FORCE_DEMO !== '1',
    provider: env.LLM_PROVIDER || 'anthropic',
    researchModel: env.RESEARCH_MODEL || env.ANTHROPIC_MODEL || 'claude-sonnet-5-5',
    strategyModel: env.STRATEGY_MODEL || env.ANTHROPIC_MODEL || 'claude-sonnet-5-5',
    apiUrl: env.ANTHROPIC_API_URL || 'https://api.anthropic.com/v1/messages',
    maxSearches: int(env.MAX_SEARCHES_PER_ANALYSIS, 6),
    maxFetches: int(env.MAX_FETCHES_PER_ANALYSIS, 3),
    maxSearchesExpress: int(env.MAX_SEARCHES_EXPRESS, 3),
    maxFetchesExpress: int(env.MAX_FETCHES_EXPRESS, 1),
    fetchMaxTokens: int(env.FETCH_MAX_CONTENT_TOKENS, 12000),
    maxContinuations: int(env.MAX_CONTINUATIONS, 3),
    requestTimeoutMs: int(env.REQUEST_TIMEOUT_MS, 180000),
    // Budget financier réel (USD), calculé sur la consommation mesurée. 0 = pas de plafond.
    dailyBudgetUsd: num(env.DAILY_BUDGET_USD, 3),
    monthlyBudgetUsd: num(env.MONTHLY_BUDGET_USD, 30),
    estimateResearchUsd: num(env.ESTIMATE_RESEARCH_USD, 0.35),
    estimateStrategyUsd: num(env.ESTIMATE_STRATEGY_USD, 0.06),
    pricing: Object.keys(pricing).length ? pricing : undefined,
    fallbackPricing: undefined,
    usageFile: env.USAGE_FILE || join(ROOT, 'data', 'usage', 'budget.json'),
    cacheTtlHours: num(env.CACHE_TTL_HOURS, 1), // v13 : les dossiers ne restent qu'une heure en mémoire vive
    perIpAnalysisLimit: int(env.PER_IP_ANALYSIS_LIMIT, 5),
    perIpStrategyLimit: int(env.PER_IP_STRATEGY_LIMIT, 20),
    // Conversation continue (mode connecté) : limites techniques, jamais un nombre de tours.
    perIpConversationLimit: int(env.PER_IP_CONVERSATION_LIMIT, 40),
    globalConversationPerHour: int(env.GLOBAL_CONVERSATION_PER_HOUR, 400),
    estimateConversationUsd: num(env.ESTIMATE_CONVERSATION_USD, 0.02),
    conversationMaxTokens: int(env.CONVERSATION_MAX_TOKENS, 900),
    perIpWindowMinutes: int(env.PER_IP_WINDOW_MINUTES, 10),
    libraryStaleDays: int(env.LIBRARY_STALE_DAYS, 365),
    trustProxy: env.TRUST_PROXY === '1',
    feedbackFile: env.FEEDBACK_FILE || join(ROOT, 'data', 'feedback', 'feedback.jsonl'),
    storeFeedback: env.STORE_FEEDBACK !== '0',
    // Base locale d'abord : une fiche qui correspond fortement, stable et à jour répond sans recherche web.
    kbDirectAnswer: env.KB_DIRECT_ANSWER !== '0',
    // Propositions de mise à jour des fiches (jamais appliquées automatiquement).
    updatesFile: env.UPDATES_FILE || join(ROOT, 'data', 'updates', 'proposals.jsonl'),
    storeUpdates: env.STORE_UPDATES !== '0',
  };
}
