import { test } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { normalizeUrl, isSafeHttpUrl, extractJson, extractNumbers, newNumbers } from '../../server/engine/util.js';
import { normalizeEvidence, joinText } from '../../server/engine/providers/anthropic.js';
import { verifySources, checkFigures, buildDossier } from '../../server/engine/evidence.js';
import { sanitizeStrategy } from '../../server/engine/strategy.js';
import { requestCost, sumCosts, BudgetLedger } from '../../server/engine/cost.js';
import { TtlStore, researchKey } from '../../server/engine/pipeline.js';
import {
  researchResponse, DOSSIER_JSON, STRATEGY_GAGNER, STRATEGY_CONVAINCRE,
  GOOD_URL, SEARCH_ONLY_URL, BLOCKED_URL, FAKE_URL,
} from '../helpers.js';

const evidence = () => normalizeEvidence(researchResponse({ json: {}, citations: [{ url: SEARCH_ONLY_URL, text: 'Les minima sociaux représentent 31,6 milliards d’euros' }] }).content);

test('URL : normalisation et sécurité', () => {
  assert.equal(normalizeUrl('https://WWW.Insee.fr/fr/statistiques/8735252/#x'), normalizeUrl('https://insee.fr/fr/statistiques/8735252'));
  assert.equal(normalizeUrl('javascript:alert(1)'), null);
  assert.equal(isSafeHttpUrl('data:text/html,x'), false);
});

test('nombres : formats français normalisés, détection des chiffres ajoutés', () => {
  assert.ok(extractNumbers('1 672 Md€').has('1672'));
  assert.ok(extractNumbers('12,2 %').has('12.2'));
  assert.ok(extractNumbers('57,0 %').has('57'));
  assert.ok(extractNumbers('2016 2025').has('2016'));
  assert.deepEqual(newNumbers('Le RSA est de 651,69 €', 'RSA : 651,69 € par mois'), []);
  assert.deepEqual(newNumbers('Le RSA est de 700 €', 'RSA : 651,69 € par mois'), ['700']);
});

test('extractJson lit le dernier bloc JSON', () => {
  assert.deepEqual(extractJson('blabla ```json\n{"a":1}\n``` fin'), { a: 1 });
  assert.equal(extractJson('rien'), null);
});

test('preuves : recherche, documents ouverts, échecs de consultation et citations', () => {
  const ev = evidence();
  assert.equal(ev.results.size, 3);
  assert.equal(ev.documents.size, 1);
  assert.ok(ev.documents.get(normalizeUrl(GOOD_URL)).text.includes('1 672'));
  assert.equal(ev.fetchErrors.get(normalizeUrl(BLOCKED_URL)), 'url_not_accessible');
  assert.deepEqual(ev.queries, ['dépenses publiques par fonction 2024']);
  assert.deepEqual(ev.fetches, [GOOD_URL, BLOCKED_URL]);
  const err = normalizeEvidence(researchResponse({ searchError: 'unavailable', fetched: [], fetchErrors: [] }).content);
  assert.deepEqual(err.errors, ['recherche:unavailable']);
  const pdf = normalizeEvidence(researchResponse({ fetched: [{ url: GOOD_URL, pdf: true }], fetchErrors: [] }).content);
  assert.equal(pdf.documents.get(normalizeUrl(GOOD_URL)).text, null);
  assert.match(joinText(researchResponse({ json: { a: 1 } }).content), /"a":1/);
});

test('sources : seules les URL réellement obtenues sont gardées, avec leur niveau d’accès', () => {
  const { kept, rejected } = verifySources(DOSSIER_JSON.sources, evidence());
  assert.deepEqual(kept.map((s) => s.id), ['S1', 'S2', 'S3']);
  assert.equal(kept[0].acces, 'document_consulte');
  assert.equal(kept[1].acces, 'extrait_recherche');
  assert.match(kept[2].acces_detail, /ouverture impossible : page inaccessible/);
  assert.equal(rejected.length, 1);
  assert.equal(rejected[0].url, FAKE_URL);
  assert.deepEqual(kept[1].extraits_cites, ['Les minima sociaux représentent 31,6 milliards d’euros']);
});

test('chiffres : retrouvés, non retrouvés ou non contrôlables dans le texte consulté', () => {
  const ev = evidence();
  const doc = { url: GOOD_URL };
  assert.equal(checkFigures('1 672 Md€', doc, ev).statut, 'retrouve');
  assert.equal(checkFigures('42 %', doc, ev).statut, 'non_retrouve');
  assert.equal(checkFigures('31,6 Md€', { url: SEARCH_ONLY_URL }, ev).statut, 'retrouve'); // via l'extrait cité
  assert.equal(checkFigures('18 %', { url: BLOCKED_URL }, ev).statut, 'non_verifiable');
  assert.equal(checkFigures('aucun chiffre', doc, ev).statut, 'sans_chiffre');
});

test('dossier : faits rattachés, sources inventées écartées, contradictions conservées', () => {
  const d = buildDossier(DOSSIER_JSON, evidence(), { date: '2026-10-29' });
  assert.equal(d.verdict, 'contredit');
  assert.equal(d.faits.length, 4);
  assert.equal(d.faits[0].source, 'S1');
  assert.equal(d.faits[0].controle_chiffre.statut, 'retrouve');
  assert.equal(d.faits[1].controle_chiffre.statut, 'non_retrouve');
  assert.equal(d.faits[3].source_verifiee, false);
  assert.equal(d.contradictions[0].source, 'S1');
  assert.ok(d.avertissements.some((w) => w.includes('écartées')));
  assert.ok(d.avertissements.some((w) => w.includes('non retrouvés') || w.includes("n'ont pas été retrouvés")));
  assert.ok(!JSON.stringify(d.sources).includes('rapport-invente'));
});

test('dossier : verdict tranché sans source rétrogradé ; verdict invalide remplacé', () => {
  const ev = normalizeEvidence(researchResponse({ results: ['https://autre.fr/x'], fetched: [], fetchErrors: [] }).content);
  assert.equal(buildDossier({ ...DOSSIER_JSON, sources: [{ titre: 'x', url: FAKE_URL }] }, ev).verdict, 'inverifiable');
  assert.equal(buildDossier({ verdict: '87 % vrai' }, ev).verdict, 'inverifiable');
  assert.equal(buildDossier({ verdict: 'opinion' }, ev).verdict, 'opinion');
});

test('stratégie « gagner » : références filtrées, nature corrigée, chiffre inventé signalé', () => {
  const d = buildDossier(DOSSIER_JSON, evidence());
  const s = sanitizeStrategy(STRATEGY_GAGNER, 'gagner', d, 'Les impôts ne servent qu’à payer l’assistanat.');
  assert.equal(s.mode, 'gagner');
  assert.equal(s.demonstration.length, 3);
  assert.deepEqual(s.demonstration[1].faits, ['F3']); // F99 n'existe pas
  assert.equal(s.demonstration[2].nature, 'interpretation'); // « fait » sans fait sourcé
  assert.deepEqual(s.demonstration[2].chiffres_non_sources, ['99']);
  assert.equal(s.demonstration[0].chiffres_non_sources, undefined);
  assert.ok(s.avertissements.length === 1);
  assert.equal(s.sophismes.length, 1);
});

test('stratégie « convaincre » : faits inconnus retirés, hypothèses conservées', () => {
  const d = buildDossier(DOSSIER_JSON, evidence());
  const s = sanitizeStrategy(STRATEGY_CONVAINCRE, 'convaincre', d, 'x');
  assert.equal(s.mode, 'convaincre');
  assert.equal(s.faits_progressifs.length, 1);
  assert.equal(s.solutions[0].nature, 'proposition');
  assert.match(s.preoccupation[0], /Hypothèse/);
  assert.deepEqual(s.avertissements, []);
});

test('coûts : calcul à partir de la consommation réelle et des tarifs', () => {
  const sonnet = requestCost({ model: 'claude-sonnet-5-5', usage: { input_tokens: 1e6, output_tokens: 1e5, server_tool_use: { web_search_requests: 3 } } });
  assert.equal(sonnet.usd.toFixed(4), (2 + 1 + 0.03).toFixed(4));
  const haikuLong = requestCost({ model: 'claude-haiku-5-5', usage: { input_tokens: 200000, output_tokens: 0 } });
  assert.equal(haikuLong.usd.toFixed(4), '0.1000'); // palier > 100 000 jetons : 0,50 $/M
  const total = sumCosts([{ model: 'claude-sonnet-5-5', usage: { input_tokens: 1000, output_tokens: 1000 } }, { model: 'inconnu', usage: { input_tokens: 1000 } }]);
  assert.ok(total.usd > 0);
});

test('budget : plafonds journalier et mensuel, persistance sur disque', () => {
  const file = join(mkdtempSync(join(tmpdir(), 'gtp-')), 'b.json');
  let now = new Date('2026-10-29T10:00:00Z');
  const l = new BudgetLedger({ file, dailyUsd: 1, monthlyUsd: 1.5, now: () => now });
  assert.equal(l.canSpend(0.5), true);
  l.record(0.8);
  assert.equal(l.canSpend(0.3), false);
  const l2 = new BudgetLedger({ file, dailyUsd: 1, monthlyUsd: 1.5, now: () => now });
  assert.equal(l2.snapshot().dayUsd.toFixed(1), '0.8'); // survit au redémarrage
  now = new Date('2026-10-30T10:00:00Z');
  assert.equal(l2.canSpend(0.5), true); // nouveau jour
  assert.equal(l2.canSpend(0.8), false); // mais plafond mensuel
});

test('cache : expiration et clé stable', () => {
  let t = 0;
  const c = new TtlStore({ ttlMs: 1000, max: 2, now: () => t });
  c.set('a', 1); c.set('b', 2); c.set('c', 3);
  assert.equal(c.get('a'), undefined); // taille max
  t = 2000;
  assert.equal(c.get('b'), undefined); // expiré
  const k = (claim) => researchKey({ claim, volet: 'social', sousTheme: null, express: false });
  assert.equal(k('Les chômeurs ne veulent PAS travailler !'), k('les chômeurs ne veulent pas travailler'));
  assert.notEqual(k('a b c'), researchKey({ claim: 'a b c', volet: 'social', express: true }));
});
