// Fournisseur « Anthropic » : modèle Claude + outils serveur de recherche Web et de consultation de pages.
// Ce module est le SEUL à connaître le format de l'API Anthropic. Il renvoie au reste du moteur
// un format neutre (texte, preuves normalisées, consommation), ce qui permet de changer de fournisseur
// en écrivant un autre module exposant la même interface `complete()`.
import { EngineError, normalizeUrl } from '../util.js';

export const SEARCH_TOOL_TYPE = 'web_search_20250305';
export const FETCH_TOOL_TYPE = 'web_fetch_20250910';

export function createAnthropicProvider(config, { fetchImpl = fetch } = {}) {
  async function post(body) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), config.requestTimeoutMs);
    let res;
    try {
      res = await fetchImpl(config.apiUrl, {
        method: 'POST',
        signal: controller.signal,
        headers: { 'content-type': 'application/json', 'x-api-key': config.apiKey, 'anthropic-version': '2023-06-01' },
        body: JSON.stringify(body),
      });
    } catch (err) {
      if (err?.name === 'AbortError') throw new EngineError('timeout', "L'analyse a pris trop de temps et a été interrompue. Tu peux relancer.", 504, { retry: true });
      throw new EngineError('network', "Impossible de joindre le service d'IA (problème réseau). Tu peux relancer.", 502, { retry: true });
    } finally {
      clearTimeout(timer);
    }
    let data;
    try { data = await res.json(); } catch { throw new EngineError('bad_response', "Réponse illisible du service d'IA.", 502, { retry: true }); }
    if (!res.ok) {
      // Le détail brut n'est jamais renvoyé au client (il peut contenir des informations de configuration).
      if (res.status === 401 || res.status === 403) throw new EngineError('auth', "Le service d'IA a refusé la clé API configurée sur le serveur.", 503);
      if (res.status === 429) throw new EngineError('rate_limited', "Le service d'IA est momentanément saturé. Réessaie dans quelques minutes.", 503, { retry: true });
      if (res.status === 529 || res.status >= 500) throw new EngineError('overloaded', "Le service d'IA est temporairement indisponible. Tu peux relancer.", 503, { retry: true });
      throw new EngineError('api_error', "Le service d'IA a rejeté la requête.", 502);
    }
    return data;
  }

  /**
   * @param {object} p
   * @param {string} p.model
   * @param {string} p.system
   * @param {string} p.user
   * @param {{maxSearches?:number, maxFetches?:number, fetchMaxTokens?:number}} [p.tools] absent = pas d'outil
   * @param {number} [p.maxTokens]
   * @returns {Promise<{text:string, evidence:object, requests:object[]}>}
   */
  async function complete({ model, system, user, tools = null, maxTokens = 4000 }) {
    const toolDefs = [];
    if (tools?.maxSearches) {
      // v13 : aucune localisation n'est transmise au moteur de recherche (le périmètre « France » vient du sujet, dans la consigne)
      toolDefs.push({ type: SEARCH_TOOL_TYPE, name: 'web_search', max_uses: tools.maxSearches });
    }
    if (tools?.maxFetches) {
      toolDefs.push({ type: FETCH_TOOL_TYPE, name: 'web_fetch', max_uses: tools.maxFetches, max_content_tokens: tools.fetchMaxTokens || 12000 });
    }
    const messages = [{ role: 'user', content: user }];
    const blocks = [];
    const requests = [];
    for (let round = 0; round < (config.maxContinuations ?? 3) + 1; round += 1) {
      const data = await post({ model, max_tokens: maxTokens, system, messages, ...(toolDefs.length ? { tools: toolDefs } : {}) });
      const content = Array.isArray(data.content) ? data.content : [];
      blocks.push(...content);
      requests.push({ model, usage: data.usage || {} });
      if (data.stop_reason !== 'pause_turn') break;
      // Reprise d'un tour long interrompu par les outils serveur : on renvoie le tour de l'assistant tel quel.
      messages.push({ role: 'assistant', content });
    }
    return { text: joinText(blocks), evidence: normalizeEvidence(blocks), requests };
  }

  return { name: 'anthropic', complete };
}

export function joinText(blocks) {
  return (blocks || []).filter((b) => b?.type === 'text').map((b) => b.text || '').join('');
}

/**
 * Convertit les blocs de l'API en preuves neutres :
 * - results   : pages renvoyées par la recherche (titre, ancienneté) — seul un extrait chiffré est vu par le modèle ;
 * - documents : pages réellement ouvertes par l'outil de consultation (texte intégral si texte/HTML) ;
 * - citations : extraits exacts cités par l'API pour une URL ;
 * - fetchErrors, errors, queries, fetches.
 */
export function normalizeEvidence(blocks) {
  const ev = {
    results: new Map(), documents: new Map(), citations: new Map(), fetchErrors: new Map(),
    queries: [], fetches: [], errors: [],
  };
  const fetchUrlById = new Map();
  for (const b of blocks || []) {
    if (!b || typeof b !== 'object') continue;
    if (b.type === 'server_tool_use' && b.name === 'web_search' && b.input?.query) {
      ev.queries.push(String(b.input.query));
    } else if (b.type === 'server_tool_use' && b.name === 'web_fetch' && b.input?.url) {
      fetchUrlById.set(b.id, String(b.input.url));
      ev.fetches.push(String(b.input.url));
    } else if (b.type === 'web_search_tool_result') {
      if (Array.isArray(b.content)) {
        for (const r of b.content) {
          if (r?.type !== 'web_search_result') continue;
          const key = normalizeUrl(r.url);
          if (key && !ev.results.has(key)) ev.results.set(key, { url: r.url, title: r.title || '', page_age: r.page_age || null });
        }
      } else if (b.content?.type === 'web_search_tool_result_error') {
        ev.errors.push(`recherche:${b.content.error_code || 'unavailable'}`);
      }
    } else if (b.type === 'web_fetch_tool_result') {
      const c = b.content || {};
      if (c.type === 'web_fetch_result') {
        const key = normalizeUrl(c.url);
        const src = c.content?.source || {};
        const isText = src.type === 'text' && typeof src.data === 'string';
        if (key) {
          ev.documents.set(key, {
            url: c.url,
            title: c.content?.title || '',
            retrieved_at: c.retrieved_at || null,
            media_type: src.media_type || null,
            text: isText ? src.data : null, // les PDF arrivent en base64 : pas de contrôle automatique des chiffres
          });
        }
      } else if (c.type === 'web_fetch_tool_result_error') {
        const url = fetchUrlById.get(b.tool_use_id);
        const key = normalizeUrl(url);
        if (key) ev.fetchErrors.set(key, c.error_code || 'unavailable');
      }
    } else if (b.type === 'text' && Array.isArray(b.citations)) {
      for (const c of b.citations) {
        if (c?.type !== 'web_search_result_location') continue;
        const key = normalizeUrl(c.url);
        if (!key) continue;
        if (!ev.results.has(key)) ev.results.set(key, { url: c.url, title: c.title || '', page_age: null });
        if (c.cited_text) {
          const list = ev.citations.get(key) || [];
          if (!list.includes(c.cited_text)) list.push(c.cited_text);
          ev.citations.set(key, list);
        }
      }
    }
  }
  return ev;
}
