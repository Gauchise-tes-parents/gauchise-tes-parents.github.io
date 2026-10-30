// Outils de test partagés. IMPORTANT : les réponses du service d'IA sont SIMULÉES
// (format documenté de l'API Anthropic). Ces tests valident le traitement côté serveur,
// pas la qualité de la recherche réelle.
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { loadConfig } from '../server/config.js';
import { createApp } from '../server/app.js';

export const silent = { info() {}, warn() {}, error() {} };

export function testConfig(overrides = {}) {
  const dir = mkdtempSync(join(tmpdir(), 'gtp-test-'));
  return {
    ...loadConfig({ PORT: '0' }),
    feedbackFile: join(dir, 'feedback.jsonl'),
    usageFile: join(dir, 'budget.json'),
    updatesFile: join(dir, 'proposals.jsonl'),
    // Les tests historiques du moteur vérifient la recherche web : la réponse directe par fiche est testée à part.
    kbDirectAnswer: false,
    ...overrides,
  };
}

export const GOOD_URL = 'https://www.insee.fr/fr/statistiques/8735252';
export const SEARCH_ONLY_URL = 'https://www.drees.solidarites-sante.gouv.fr/rapport-minima';
export const BLOCKED_URL = 'https://www.cour-des-comptes.fr/rapport-bloque';
export const FAKE_URL = 'https://www.insee.fr/fr/statistiques/9999999-rapport-invente';
export const DOC_TEXT = 'Les dépenses publiques atteignent 1 672 Md€ en 2024, soit 57,0 % du PIB. La protection sociale représente 693 Md€.';

/** Réponse simulée de la phase de recherche (outils web_search + web_fetch). */
export function researchResponse({ json, results = [GOOD_URL, SEARCH_ONLY_URL, BLOCKED_URL], fetched = [{ url: GOOD_URL, text: DOC_TEXT }], fetchErrors = [{ url: BLOCKED_URL, code: 'url_not_accessible' }], citations = [], searchError = null, stop = 'end_turn', usage } = {}) {
  const content = [{ type: 'text', text: 'Je cherche.' }, { type: 'server_tool_use', id: 's1', name: 'web_search', input: { query: 'dépenses publiques par fonction 2024' } }];
  content.push(searchError
    ? { type: 'web_search_tool_result', tool_use_id: 's1', content: { type: 'web_search_tool_result_error', error_code: searchError } }
    : { type: 'web_search_tool_result', tool_use_id: 's1', content: results.map((u) => ({ type: 'web_search_result', url: u, title: `Titre ${u.split('/').pop()}`, page_age: 'February 5, 2026', encrypted_content: 'x' })) });
  fetched.forEach((f, i) => {
    content.push({ type: 'server_tool_use', id: `f${i}`, name: 'web_fetch', input: { url: f.url } });
    content.push({ type: 'web_fetch_tool_result', tool_use_id: `f${i}`, content: { type: 'web_fetch_result', url: f.url, retrieved_at: '2026-10-29T10:00:00Z', content: { type: 'document', title: 'Document', source: f.pdf ? { type: 'base64', media_type: 'application/pdf', data: 'JVBERi0' } : { type: 'text', media_type: 'text/plain', data: f.text } } } });
  });
  fetchErrors.forEach((f, i) => {
    content.push({ type: 'server_tool_use', id: `e${i}`, name: 'web_fetch', input: { url: f.url } });
    content.push({ type: 'web_fetch_tool_result', tool_use_id: `e${i}`, content: { type: 'web_fetch_tool_result_error', error_code: f.code } });
  });
  if (citations.length) content.push({ type: 'text', text: 'Selon la source,', citations: citations.map((c) => ({ type: 'web_search_result_location', url: c.url, title: 't', encrypted_index: 'y', cited_text: c.text })) });
  if (json !== undefined) content.push({ type: 'text', text: `\n\`\`\`json\n${typeof json === 'string' ? json : JSON.stringify(json)}\n\`\`\`` });
  return { content, stop_reason: stop, usage: usage || { input_tokens: 20000, output_tokens: 2000, server_tool_use: { web_search_requests: 1, web_fetch_requests: fetched.length + fetchErrors.length } } };
}

export const textResponse = (text, usage = { input_tokens: 3000, output_tokens: 800 }) => ({ content: [{ type: 'text', text }], stop_reason: 'end_turn', usage });
export const jsonResponse = (obj) => textResponse(`\`\`\`json\n${JSON.stringify(obj)}\n\`\`\``);

export const DOSSIER_JSON = {
  reformulation: 'Les impôts financeraient uniquement les aides sociales.',
  verifiable: true,
  verdict: 'contredit',
  resume: 'La protection sociale est la première dépense, mais la santé, l’enseignement et la dette pèsent lourd.',
  faits: [
    { fait: 'Les dépenses publiques atteignent 1 672 Md€ en 2024.', chiffre: '1 672 Md€', periode: '2024', perimetre: 'Administrations publiques', montre: 'Le total', ne_montre_pas: 'Le financement', sens: 'contredit_affirmation', source_url: 'https://insee.fr/fr/statistiques/8735252/' },
    { fait: 'Une part inventée.', chiffre: '42 %', periode: '2024', perimetre: 'France', montre: 'x', ne_montre_pas: 'y', sens: 'contexte', source_url: GOOD_URL },
    { fait: 'Les minima sociaux représentent 31,6 Md€.', chiffre: '31,6 Md€', periode: '2023', perimetre: 'France', montre: 'x', ne_montre_pas: 'y', sens: 'contredit_affirmation', source_url: SEARCH_ONLY_URL },
    { fait: 'Fait sans source réelle.', chiffre: '12 %', periode: '2024', perimetre: 'France', montre: 'x', ne_montre_pas: 'y', sens: 'contexte', source_url: FAKE_URL },
  ],
  contradictions: [{ element: 'Les prestations sociales augmentent plus vite que le PIB.', source_url: GOOD_URL }],
  alerte: null,
  jugements_de_valeur: ['Ce qui mérite d’être financé relève d’un choix politique.'],
  manques: [],
  sources: [
    { titre: 'Usage de l’argent public', organisme: 'Insee', date_publication: '5 février 2026', periode_couverte: '2024', type: 'primaire', url: GOOD_URL, passage: '1 672 Md€', pertinence: 'Officiel' },
    { titre: 'Minima sociaux', organisme: 'DREES', date_publication: 'Décembre 2025', periode_couverte: '2023', type: 'primaire', url: SEARCH_ONLY_URL, passage: '31,6 Md€', pertinence: 'Officiel' },
    { titre: 'Rapport bloqué', organisme: 'Cour des comptes', date_publication: '2025', type: 'primaire', url: BLOCKED_URL, passage: '…', pertinence: '…' },
    { titre: 'Rapport inventé', organisme: 'Insee', date_publication: '2026', url: FAKE_URL, passage: 'faux', pertinence: 'faux' },
  ],
  limites: ['Données 2024 provisoires.'],
};

export const STRATEGY_GAGNER = {
  these: 'L’argent public finance surtout des services utilisés par tout le monde.',
  replique: 'Sur 1 672 milliards de dépenses publiques, les minima sociaux pèsent 31,6 milliards.',
  demonstration: [
    { argument: 'Le total est énorme : 1 672 Md€.', pourquoi: 'Ordre de grandeur', comment_le_dire: 'Simplement', nature: 'fait', faits: ['F1'] },
    { argument: 'Les minima sociaux ne sont qu’une petite part.', pourquoi: 'Comparaison', comment_le_dire: 'Calmement', nature: 'fait', faits: ['F3', 'F99'] },
    { argument: 'En plus, 99 % des gens utilisent l’hôpital.', pourquoi: 'Chiffre inventé', comment_le_dire: 'x', nature: 'fait', faits: [] },
  ],
  donnees: [{ fait: 'F1', montre: 'Le total', ne_montre_pas: 'Le financement' }],
  objections: [{ objection: 'Et la fraude ?', reponse: 'Elle existe mais ne change pas l’ordre de grandeur.', faits: ['F3'] }],
  sophismes: [{ type: 'généralisation abusive', passage: 'ne servent qu’à', explication: 'Le mot « que » exclut tout le reste.' }],
  questions: ['Qu’est-ce que tu appelles assistanat ?'],
  conclusion: 'L’impôt paie l’école, l’hôpital et les routes avant tout.',
};

export const STRATEGY_CONVAINCRE = {
  replique: 'Je comprends l’agacement. Regardons ensemble où va l’argent.',
  preoccupation: ['Hypothèse : un sentiment d’injustice fiscale.'],
  reconnaissance: 'C’est normal de vouloir savoir où vont ses impôts.',
  terrain_commun: [{ valeur: 'efficacité des dépenses publiques', formulation: 'On veut tous que l’argent soit bien utilisé.' }],
  faits_progressifs: [{ fait: 'F1', explication: 'Le total des dépenses.', pourquoi: 'Ordre de grandeur' }, { fait: 'F7', explication: 'inexistant', pourquoi: 'x' }],
  pont: 'On peut trouver l’impôt lourd sans que l’assistanat en soit la cause.',
  solutions: [{ solution: 'Rendre visible l’usage de l’impôt.', avantages: 'Transparence', limites: 'Ne règle pas tout', conditions: 'Données publiques', nature: 'proposition', faits: [] }],
  question_ouverte: 'Qu’est-ce qui te ferait changer d’avis ?',
  sortie: 'On peut en reparler une autre fois.',
};

export const SPEECH = { redigee: 'Mille six cents milliards… En vrai, 1 672 milliards de dépenses publiques.', spontanee: ['Le total', 'La petite part des minima'] };

/**
 * Faux `fetch` qui aiguille selon le type d'appel (recherche, stratégie, démonstration, reformulation)
 * et mémorise toutes les requêtes. Chaque entrée peut être une réponse ou une liste (servie dans l'ordre).
 */
export function routerFetch(map) {
  const calls = [];
  const counters = {};
  const kindOf = (body) => {
    if (body.tools) return 'research';
    if (body.system.includes('Tu accompagnes une personne pendant une discussion')) return 'conversation';
    if (body.system.includes('DIT à voix haute')) return 'speech';
    if (body.system.includes('reformules')) return 'rephrase';
    if (body.system.includes('CONVAINCRE SANS BRAQUER')) return 'convaincre';
    return 'gagner';
  };
  const fn = async (url, init) => {
    const body = JSON.parse(init.body);
    const kind = kindOf(body);
    calls.push({ kind, body, headers: init.headers });
    let r = map[kind];
    if (Array.isArray(r)) { counters[kind] = (counters[kind] || 0) + 1; r = r[Math.min(counters[kind] - 1, r.length - 1)]; }
    if (!r) throw new Error(`pas de réponse simulée pour ${kind}`);
    if (r.status) return { ok: false, status: r.status, json: async () => r.body || {} };
    return { ok: true, status: 200, json: async () => r };
  };
  fn.calls = calls;
  fn.count = (k) => calls.filter((c) => c.kind === k).length;
  return fn;
}

export const defaultRoutes = () => ({
  research: researchResponse({ json: DOSSIER_JSON, citations: [{ url: SEARCH_ONLY_URL, text: 'Les minima sociaux représentent 31,6 milliards d’euros' }] }),
  gagner: jsonResponse(STRATEGY_GAGNER),
  convaincre: jsonResponse(STRATEGY_CONVAINCRE),
  speech: jsonResponse(SPEECH),
  rephrase: textResponse('Les minima sociaux, c’est 31,6 milliards sur 1 672.'),
});

export async function startServer(config, deps = {}) {
  const app = createApp(config, { logger: silent, ...deps });
  await new Promise((resolve) => app.server.listen(0, '127.0.0.1', resolve));
  const { port } = app.server.address();
  const base = `http://127.0.0.1:${port}`;
  return {
    ...app,
    base,
    close: () => new Promise((resolve) => app.server.close(resolve)),
    get: (p, headers = {}) => fetch(base + p, { headers }),
    post: (p, body) => fetch(base + p, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) }),
  };
}
