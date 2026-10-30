// Coûts : calculés à partir de la consommation RÉELLE renvoyée par l'API et des tarifs du fournisseur.
// Le budget (jour / mois, en dollars) est un vrai plafond financier côté application :
// il est persisté sur disque pour survivre aux redémarrages.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
import { dirname } from 'node:path';

// Tarifs publics Anthropic (USD), relevés le 29 octobre 2026 sur
// https://platform.claude.com/docs/en/about-claude/pricing — à vérifier régulièrement.
// Recherche Web : 10 $ / 1 000 recherches ; consultation de page (web_fetch) : pas de supplément hors jetons.
export const DEFAULT_PRICING = {
  'claude-sonnet-5-5': { input: 2, output: 10, cacheRead: 0.10 },
  'claude-opus-5-5': { input: 4, output: 20, cacheRead: 0.20 },
  'claude-haiku-5-5': { input: 0.10, output: 0.50, cacheRead: 0.01, longPromptThreshold: 100000, long: { input: 0.50, output: 2.50, cacheRead: 0.05 } },
};
export const SEARCH_PRICE_PER_1000 = 10;

/** Coût en USD d'une requête à partir de son `usage`. Modèle inconnu : tarifs de repli (configurables). */
export function requestCost({ model, usage = {} }, pricing = DEFAULT_PRICING, fallback = DEFAULT_PRICING['claude-sonnet-5-5']) {
  let p = pricing[model] || fallback;
  const input = usage.input_tokens || 0;
  const cacheRead = usage.cache_read_input_tokens || 0;
  const cacheWrite = usage.cache_creation_input_tokens || 0;
  if (p.longPromptThreshold && input + cacheRead + cacheWrite > p.longPromptThreshold) p = { ...p, ...p.long };
  // L'application n'utilise pas la mise en cache de prompt : cacheWrite vaut normalement 0
  // (majoration d'écriture en cache comptée prudemment à 1,25 × le prix d'entrée).
  const tokens = ((input + cacheWrite * 1.25) * p.input + cacheRead * p.cacheRead + (usage.output_tokens || 0) * p.output) / 1e6;
  const searches = usage.server_tool_use?.web_search_requests || 0;
  return {
    usd: tokens + (searches * SEARCH_PRICE_PER_1000) / 1000,
    input_tokens: input + cacheRead + cacheWrite,
    output_tokens: usage.output_tokens || 0,
    web_search_requests: searches,
    web_fetch_requests: usage.server_tool_use?.web_fetch_requests || 0,
  };
}

export function sumCosts(requests, pricing, fallback) {
  const table = { ...DEFAULT_PRICING, ...(pricing || {}) };
  return requests.map((r) => requestCost(r, table, fallback)).reduce((a, c) => ({
    usd: a.usd + c.usd,
    input_tokens: a.input_tokens + c.input_tokens,
    output_tokens: a.output_tokens + c.output_tokens,
    web_search_requests: a.web_search_requests + c.web_search_requests,
    web_fetch_requests: a.web_fetch_requests + c.web_fetch_requests,
  }), { usd: 0, input_tokens: 0, output_tokens: 0, web_search_requests: 0, web_fetch_requests: 0 });
}

export class BudgetLedger {
  constructor({ file = null, dailyUsd = 0, monthlyUsd = 0, now = () => new Date() }) {
    this.file = file;
    this.dailyUsd = dailyUsd;
    this.monthlyUsd = monthlyUsd;
    this.now = now;
    this.state = { day: null, dayUsd: 0, month: null, monthUsd: 0 };
    if (file && existsSync(file)) {
      try { this.state = { ...this.state, ...JSON.parse(readFileSync(file, 'utf8')) }; } catch { /* fichier corrompu : on repart de zéro */ }
    }
  }

  roll() {
    const d = this.now().toLocaleDateString('sv-SE', { timeZone: 'Europe/Paris' });
    const m = d.slice(0, 7);
    if (this.state.day !== d) { this.state.day = d; this.state.dayUsd = 0; }
    if (this.state.month !== m) { this.state.month = m; this.state.monthUsd = 0; }
  }

  /** Vrai si une dépense estimée à `estimateUsd` reste dans les plafonds (0 = pas de plafond). */
  canSpend(estimateUsd) {
    this.roll();
    if (this.dailyUsd > 0 && this.state.dayUsd + estimateUsd > this.dailyUsd) return false;
    if (this.monthlyUsd > 0 && this.state.monthUsd + estimateUsd > this.monthlyUsd) return false;
    return true;
  }

  record(usd) {
    this.roll();
    this.state.dayUsd += usd;
    this.state.monthUsd += usd;
    if (this.file) {
      try {
        mkdirSync(dirname(this.file), { recursive: true });
        writeFileSync(this.file, JSON.stringify(this.state));
      } catch { /* l'échec d'écriture ne doit pas casser l'analyse */ }
    }
  }

  snapshot() {
    this.roll();
    return { ...this.state, dailyUsd: this.dailyUsd, monthlyUsd: this.monthlyUsd };
  }
}
