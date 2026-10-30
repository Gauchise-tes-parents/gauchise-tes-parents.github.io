// Tests du serveur. Mode réel : le service d'IA est SIMULÉ (réponses au format documenté).
import { test, describe, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { gunzipSync } from 'node:zlib';
import {
  testConfig, startServer, routerFetch, defaultRoutes, researchResponse, jsonResponse, textResponse,
  DOSSIER_JSON, STRATEGY_GAGNER, GOOD_URL,
} from '../helpers.js';
import { parseDotenv, loadConfig } from '../../server/config.js';

const live = (over = {}) => testConfig({ liveMode: true, apiKey: 'sk-test-secret', ...over });
const ASK = { affirmation: 'Les impôts ne servent qu’à payer l’assistanat.', volet: 'economie', sous_theme: 'Fiscalité', mode: 'gagner', profil: 'colerique', contexte: 'repas' };

describe('mode démonstration (aucune clé API)', () => {
  let s;
  const cfg = testConfig({ liveMode: false, apiKey: '' });
  before(async () => { s = await startServer(cfg); });
  after(() => s.close());

  test('accueil servi, compressé, avec en-têtes de sécurité', async () => {
    const r = await s.get('/', { 'accept-encoding': 'gzip' });
    assert.equal(r.status, 200);
    assert.match(r.headers.get('content-security-policy'), /default-src 'self'/);
    const raw = await fetch(`${s.base}/js/app.js`, { headers: { 'accept-encoding': 'gzip' }, decompress: false });
    assert.equal(raw.headers.get('content-encoding'), 'gzip');
    assert.match(await r.text(), /Gauchise tes parents/);
  });

  test('routes côté client et protection contre la traversée de répertoire', async () => {
    assert.equal((await s.get('/bibliotheque')).status, 200);
    assert.equal((await s.get('/js/inexistant.js')).status, 404);
    assert.notEqual((await s.get('/..%2f..%2fserver%2fconfig.js')).status, 200);
    assert.notEqual((await s.get('/%2e%2e/.env.example')).status, 200);
  });

  test('statut : mode démo annoncé, pas de recherche', async () => {
    const st = await (await s.get('/api/status')).json();
    assert.equal(st.mode, 'demo');
    assert.equal(st.recherche_web, false);
  });

  test('analyse en démo : aucun verdict, aucune source, aucune stratégie ; fiches suggérées', async () => {
    const d = await (await s.post('/api/analyse', ASK)).json();
    assert.equal(d.mode, 'demo');
    assert.equal(d.dossier, undefined);
    assert.equal(d.strategie, undefined);
    assert.equal(d.suggestions_bibliotheque[0].id, 'impots-assistanat');
  });

  test('stratégie, démonstration et reformulation refusées en démo', async () => {
    for (const p of ['/api/strategie', '/api/demonstration', '/api/reformuler']) {
      const r = await s.post(p, { analyse_id: 'abcdefgh-1234', mode: 'gagner', duree: 30 });
      assert.equal(r.status, 503, p);
      assert.equal((await r.json()).mode, 'demo');
    }
  });

  test('entrées invalides : 400, 413, 415', async () => {
    assert.equal((await s.post('/api/analyse', { affirmation: '' })).status, 400);
    assert.equal((await fetch(`${s.base}/api/analyse`, { method: 'POST', body: 'x' })).status, 415);
    assert.equal((await s.post('/api/analyse', { affirmation: 'x'.repeat(20000) })).status, 413);
  });

  test('bibliothèque : filtres par volet et sous-thème, fraîcheur, 404', async () => {
    const all = await (await s.get('/api/library')).json();
    assert.equal(all.fiches.length, readdirSync(new URL('../../data/library/', import.meta.url)).filter((f) => f.endsWith('.json')).length);
    assert.ok(all.fiches.every((f) => f.fraicheur && f.volet_label));
    const social = await (await s.get('/api/library?volet=social&sous_theme=RSA')).json();
    assert.ok(social.fiches.length >= 2 && social.fiches.every((f) => f.sous_theme === 'RSA'));
    const fiche = await (await s.get('/api/library/chomeurs-travailler')).json();
    assert.equal(fiche.fraicheur.statut, 'a_actualiser');
    assert.equal((await s.get('/api/library/nexiste-pas')).status, 404);
  });

  test('retours : stockage minimal sans IP', async () => {
    assert.equal((await s.post('/api/feedback', { type: 'avis', note: 'partiel', commentaire: 'Il manque X', affirmation: 'secret', joindre_affirmation: false, mode_debat: 'gagner', volet: 'social' })).status, 200);
    assert.equal((await s.post('/api/feedback', { type: 'source_incorrecte', url: 'javascript:alert(1)' })).status, 400);
    const lines = readFileSync(cfg.feedbackFile, 'utf8').trim().split('\n').map((l) => JSON.parse(l));
    assert.equal(lines.length, 1);
    assert.equal(lines[0].affirmation, null);
    assert.equal(lines[0].mode_debat, 'gagner');
    assert.ok(!JSON.stringify(lines).includes('127.0.0.1'));
  });
});

describe('mode réel (service d’IA simulé)', () => {
  test('analyse complète : recherche + consultation, sources vérifiées, stratégie « gagner »', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const r = await s.post('/api/analyse', ASK);
      assert.equal(r.status, 200);
      const d = await r.json();
      // outils réellement demandés au fournisseur
      const research = f.calls.find((c) => c.kind === 'research');
      const types = research.body.tools.map((t) => `${t.type}:${t.max_uses}`);
      assert.deepEqual(types, ['web_search_20250305:6', 'web_fetch_20250910:3']);
      assert.match(research.body.messages[0].content, /<affirmation>/);
      assert.match(research.body.messages[0].content, /Fiscalité/);
      // la stratégie est générée SANS outil de recherche
      assert.equal(f.calls.find((c) => c.kind === 'gagner').body.tools, undefined);
      // dossier vérifié
      assert.deepEqual(d.dossier.sources.map((x) => x.acces), ['document_consulte', 'extrait_recherche', 'extrait_recherche']);
      assert.equal(d.dossier.sources_rejetees.length, 1);
      assert.equal(d.dossier.faits[0].controle_chiffre.statut, 'retrouve');
      assert.equal(d.dossier.faits[1].controle_chiffre.statut, 'non_retrouve');
      assert.equal(d.dossier.contradictions.length, 1);
      assert.equal(d.strategie.mode, 'gagner');
      assert.equal(d.strategie.demonstration.length, 3);
      assert.deepEqual(d.strategie.demonstration[2].chiffres_non_sources, ['99']);
      // coût mesuré et secret jamais renvoyé
      assert.ok(d.technique.cout_usd > 0);
      assert.ok(!JSON.stringify(d).includes('sk-test-secret'));
      assert.equal(research.headers['x-api-key'], 'sk-test-secret');
    } finally { await s.close(); }
  });

  test('changement de mode sans nouvelle recherche, puis démonstration orale et reformulation', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const a = await (await s.post('/api/analyse', ASK)).json();
      const b = await (await s.post('/api/strategie', { analyse_id: a.analyse_id, mode: 'convaincre', profil: 'preoccupe' })).json();
      assert.equal(b.strategie.mode, 'convaincre');
      assert.equal(b.analyse_id, a.analyse_id);
      assert.equal(f.count('research'), 1); // la recherche n'est pas relancée
      // revenir à « gagner » réutilise la stratégie déjà calculée pour ce profil
      await s.post('/api/strategie', { analyse_id: a.analyse_id, mode: 'gagner', profil: 'colerique', contexte: 'repas' });
      assert.equal(f.count('gagner'), 1);
      const sp = await (await s.post('/api/demonstration', { analyse_id: a.analyse_id, duree: 60, mode: 'convaincre', profil: 'preoccupe' })).json();
      assert.match(sp.redigee, /1 672/);
      assert.deepEqual(sp.chiffres_non_sources, []);
      assert.equal(sp.spontanee.length, 2);
      assert.equal((await s.post('/api/demonstration', { analyse_id: a.analyse_id, duree: 45 })).status, 400);
      const rp = await (await s.post('/api/reformuler', { analyse_id: a.analyse_id, variante: 'pedagogique', mode: 'gagner', profil: 'colerique', contexte: 'repas' })).json();
      assert.match(rp.replique, /31,6/);
      assert.equal((await s.post('/api/strategie', { analyse_id: 'inexistant-123', mode: 'gagner' })).status, 410);
    } finally { await s.close(); }
  });

  test('cache : même affirmation = pas de nouvelle recherche ; « recherche fraîche » relance', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(live(), { fetchImpl: f });
    try {
      await s.post('/api/analyse', ASK);
      const again = await (await s.post('/api/analyse', { ...ASK, affirmation: 'les impôts ne servent qu’à payer l’assistanat' })).json();
      assert.equal(f.count('research'), 1);
      assert.ok(again.cache);
      await s.post('/api/analyse', { ...ASK, fraiche: true });
      assert.equal(f.count('research'), 2);
    } finally { await s.close(); }
  });

  test('réponse express : budget de recherche réduit', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const d = await (await s.post('/api/analyse', { ...ASK, express: true })).json();
      assert.equal(d.express, true);
      assert.deepEqual(f.calls[0].body.tools.map((t) => t.max_uses), [3, 1]);
      assert.match(f.calls.find((c) => c.kind === 'gagner').body.messages[0].content, /Réponse express/);
    } finally { await s.close(); }
  });

  test('recherche Web indisponible : erreur explicite, relance possible, aucun résultat affiché', async () => {
    const f = routerFetch({ ...defaultRoutes(), research: researchResponse({ json: DOSSIER_JSON, searchError: 'unavailable', fetched: [], fetchErrors: [] }) });
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const r = await s.post('/api/analyse', ASK);
      assert.equal(r.status, 503);
      const d = await r.json();
      assert.equal(d.code, 'search_unavailable');
      assert.equal(d.relancer, true);
      assert.equal(d.dossier, undefined);
      assert.equal(f.count('gagner'), 0);
    } finally { await s.close(); }
  });

  test('sources insuffisantes : verdict rétrogradé, manques et avertissements affichés', async () => {
    const json = { ...DOSSIER_JSON, sources: [], manques: ['Aucune donnée officielle récente trouvée.'] };
    const f = routerFetch({ ...defaultRoutes(), research: researchResponse({ json, results: [], fetched: [], fetchErrors: [] }) });
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const d = await (await s.post('/api/analyse', ASK)).json();
      assert.equal(d.dossier.verdict, 'inverifiable');
      assert.equal(d.dossier.sources.length, 0);
      assert.deepEqual(d.dossier.manques, ['Aucune donnée officielle récente trouvée.']);
      assert.ok(d.dossier.avertissements.some((w) => w.includes('aucun résultat')));
      assert.ok(d.dossier.faits.every((x) => !x.source_verifiee));
    } finally { await s.close(); }
  });

  test('données qui donnent raison à l’interlocuteur : alerte transmise', async () => {
    const json = { ...DOSSIER_JSON, verdict: 'plutot_exact', alerte: { constat: 'Les dépenses sociales sont bien la première dépense.', reformulation_solide: 'Dis plutôt : la protection sociale, ce sont surtout les retraites.' } };
    const f = routerFetch({ ...defaultRoutes(), research: researchResponse({ json }) });
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const d = await (await s.post('/api/analyse', ASK)).json();
      assert.equal(d.dossier.verdict, 'plutot_exact');
      assert.match(d.dossier.alerte.reformulation_solide, /retraites/);
      assert.match(f.calls.find((c) => c.kind === 'gagner').body.messages[0].content, /reformulation_solide/);
    } finally { await s.close(); }
  });

  test('erreurs du fournisseur traduites sans fuite ; réponse illisible', async () => {
    for (const [status, expected] of [[401, 503], [429, 503], [500, 503], [400, 502]]) {
      const f = routerFetch({ research: { status, body: { error: { message: 'détail interne sk-ant-xxx' } } } });
      const s = await startServer(live(), { fetchImpl: f });
      try {
        const r = await s.post('/api/analyse', ASK);
        assert.equal(r.status, expected);
        assert.ok(!JSON.stringify(await r.json()).includes('sk-ant'));
      } finally { await s.close(); }
    }
    const f = routerFetch({ ...defaultRoutes(), research: researchResponse({ json: 'pas du json' }) });
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const r = await s.post('/api/analyse', ASK);
      assert.equal(r.status, 502);
      assert.equal((await r.json()).code, 'parse');
    } finally { await s.close(); }
  });

  test('pause_turn : la recherche longue est reprise et cumulée', async () => {
    const first = researchResponse({ stop: 'pause_turn' });
    const second = jsonResponse(DOSSIER_JSON);
    let n = 0;
    const calls = [];
    const f = async (url, init) => {
      const body = JSON.parse(init.body);
      calls.push(body);
      const r = body.tools ? (n++ === 0 ? first : second) : jsonResponse(STRATEGY_GAGNER);
      return { ok: true, status: 200, json: async () => r };
    };
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const d = await (await s.post('/api/analyse', ASK)).json();
      assert.equal(calls[1].messages.at(-1).role, 'assistant');
      assert.equal(d.dossier.sources.length, 3);
    } finally { await s.close(); }
  });

  test('contrôle des coûts : budget financier mesuré atteint → refus', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(live({ dailyBudgetUsd: 0.5, estimateResearchUsd: 0.1, estimateStrategyUsd: 0.01 }), { fetchImpl: f });
    try {
      const first = await (await s.post('/api/analyse', ASK)).json();
      // 20 000 jetons en entrée, 2 000 en sortie, 1 recherche (Sonnet : 2 $ / 10 $ par million) + stratégie
      assert.equal(first.technique.couts[0].usd, Number((0.04 + 0.02 + 0.01).toFixed(4)));
      const spent = s.ledger.snapshot().dayUsd;
      assert.ok(spent > 0.07 && spent < 0.1);
      s.ledger.record(0.45); // on simule une journée déjà chargée
      const r = await s.post('/api/analyse', { ...ASK, affirmation: 'Une autre affirmation à vérifier' });
      assert.equal(r.status, 503);
      assert.equal((await r.json()).code, 'budget');
    } finally { await s.close(); }
  });

  test('limite de fréquence par IP', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(live({ perIpAnalysisLimit: 2 }), { fetchImpl: f });
    try {
      assert.equal((await s.post('/api/analyse', ASK)).status, 200);
      assert.equal((await s.post('/api/analyse', ASK)).status, 200);
      const r = await s.post('/api/analyse', ASK);
      assert.equal(r.status, 429);
      assert.ok(r.headers.get('retry-after'));
    } finally { await s.close(); }
  });

  test('stratégie à partir d’une fiche : aucune recherche, sources de la fiche', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const d = await (await s.post('/api/strategie', { fiche_id: 'rsa-smic', mode: 'gagner' })).json();
      assert.equal(f.count('research'), 0);
      assert.equal(d.origine, 'bibliotheque');
      assert.equal(d.fiche_id, 'rsa-smic');
      assert.equal(d.dossier.sources[0].acces, 'document_consulte');
      assert.equal((await s.post('/api/strategie', { fiche_id: 'nexiste-pas', mode: 'gagner' })).status, 404);
    } finally { await s.close(); }
  });

  test('démonstration : un chiffre inventé est signalé si la seconde tentative échoue aussi', async () => {
    const bad = jsonResponse({ redigee: 'Le RSA, c’est 900 euros.', spontanee: ['900 euros'] });
    const f = routerFetch({ ...defaultRoutes(), speech: [bad, bad] });
    const s = await startServer(live(), { fetchImpl: f });
    try {
      const a = await (await s.post('/api/analyse', ASK)).json();
      const sp = await (await s.post('/api/demonstration', { analyse_id: a.analyse_id, duree: 30, mode: 'gagner', profil: 'colerique', contexte: 'repas' })).json();
      assert.deepEqual(sp.chiffres_non_sources, ['900']);
      assert.match(sp.avertissement, /900/);
      assert.equal(f.count('speech'), 2);
    } finally { await s.close(); }
  });

  test('statut en mode réel : outils et budget annoncés', async () => {
    const s = await startServer(live(), { fetchImpl: routerFetch(defaultRoutes()) });
    try {
      const st = await (await s.get('/api/status')).json();
      assert.equal(st.mode, 'live');
      assert.equal(st.consultation_documents, true);
      assert.equal(st.budget_disponible, true);
      assert.ok(!JSON.stringify(st).includes('sk-test'));
    } finally { await s.close(); }
  });
});

test('configuration : .env, mode réel seulement avec clé, modèles et budget', () => {
  assert.deepEqual(parseDotenv('# c\nA=1\nB="deux"\n\nC = trois'), { A: '1', B: 'deux', C: 'trois' });
  assert.equal(loadConfig({}).liveMode, false);
  assert.equal(loadConfig({ ANTHROPIC_API_KEY: 'k' }).liveMode, true);
  assert.equal(loadConfig({ ANTHROPIC_API_KEY: 'k', FORCE_DEMO: '1' }).liveMode, false);
  const c = loadConfig({ RESEARCH_MODEL: 'claude-opus-5-5', STRATEGY_MODEL: 'claude-haiku-5-5', DAILY_BUDGET_USD: '0' });
  assert.equal(c.researchModel, 'claude-opus-5-5');
  assert.equal(c.strategyModel, 'claude-haiku-5-5');
  assert.equal(c.dailyBudgetUsd, 0);
  assert.ok(textResponse('x'));
});
