// Base de connaissances v3 : schéma, rubriques, recherche locale, décision web, comparaison et API.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { loadLibrary, validateEntry, matchLocal, searchLibrary, isHomepageUrl, LIBRARY_DIR } from '../../server/library.js';
import { decideWeb, compareWithFiche } from '../../server/engine/knowledge.js';
import { RUBRIQUES, FICHE_TABS, FIABILITES } from '../../public/js/taxonomy.js';
import { silent, testConfig, startServer, routerFetch, defaultRoutes, researchResponse, DOSSIER_JSON, GOOD_URL } from '../helpers.js';

const lib = loadLibrary(LIBRARY_DIR, silent);
const byId = (id) => lib.find((e) => e.id === id);
const readFiche = (id) => JSON.parse(readFileSync(join(LIBRARY_DIR, `${id}.json`), 'utf8'));
const TODAY = { today: '2026-10-29' };

describe('schéma v3 et contenu', () => {
  test('toutes les fiches du dossier sont chargées (aucune ignorée)', () => {
    const files = readdirSync(LIBRARY_DIR).filter((f) => f.endsWith('.json'));
    assert.equal(lib.length, files.length);
    assert.ok(lib.length >= 40);
  });

  test('cinq rubriques transversales, chacune alimentée', () => {
    assert.deepEqual(RUBRIQUES.map((r) => r.id), ['patriotisme-de-gauche', 'islamo-gauchisme-laicite', 'melenchon-lfi', 'immigration-prisons', 'science-du-dialogue']);
    assert.ok(lib.filter((e) => e.rubriques.includes('immigration-prisons')).length >= 11);
    assert.ok(lib.filter((e) => e.rubriques.includes('science-du-dialogue')).length >= 14);
    const count = (r) => lib.filter((e) => e.rubriques.includes(r)).length;
    assert.ok(count('patriotisme-de-gauche') >= 8);
    assert.ok(count('islamo-gauchisme-laicite') >= 6);
    assert.ok(count('melenchon-lfi') >= 11);
  });

  test('chaque fiche fournit les 7 onglets (15 s, 1 min, 3 min, sources, contre-arguments, contexte, empathie)', () => {
    assert.equal(FICHE_TABS.length, 7);
    for (const e of lib) {
      for (const k of ['court', 'moyen', 'detaille', 'empathie']) assert.ok(e.argumentaires[k].length > 20, `${e.id}.${k}`);
      assert.ok(e.contre_arguments.length > 0 && e.contexte && e.sources.length, e.id);
      assert.ok(FIABILITES[e.fiabilite], e.id);
    }
  });

  test('fiches Mélenchon/LFI : structure en cinq parties complète', () => {
    const m = lib.filter((e) => e.rubriques.includes('melenchon-lfi'));
    const attendues = ['melenchon-crie', 'melenchon-agressif', 'melenchon-autoritaire', 'melenchon-dangereux-democratie', 'lfi-antisemite', 'lfi-communautarisme', 'melenchon-ruiner-france', 'programme-irrealisable', 'lfi-contre-police', 'melenchon-change-avis', 'gauche-assistes-travailleurs'];
    assert.deepEqual(attendues.filter((id) => !m.some((e) => e.id === id)), []);
    for (const e of m) {
      assert.equal(e.type, 'reponse_critique', e.id);
      assert.ok(e.reproche?.length > 40, `${e.id} : reproche`); // 1. ce qui est reproché
      assert.ok(e.faits.length >= 3, `${e.id} : faits`); // 2. faits vérifiables
      assert.ok(e.argumentaires.moyen.length > 200, `${e.id} : réponse`); // 3. réponse argumentée
      assert.ok(e.objections_legitimes?.length >= 2, `${e.id} : objections légitimes`); // 4.
      assert.equal(e.formulation_table, e.argumentaires.court, e.id); // 5. formulation à table
    }
  });

  test('pas de blanchiment : la fiche « crie » admet qu’il hausse le ton ; la fiche antisémitisme reste un débat sans verdict', () => {
    const crie = byId('melenchon-crie');
    assert.match(crie.argumentaires.court, /hausse le ton/);
    assert.doesNotMatch(JSON.stringify(crie), /ne hausse jamais|ne crie jamais/);
    const as = byId('lfi-antisemite');
    assert.equal(as.verdict, null);
    assert.equal(as.fiabilite, 'debat');
    assert.match(as.argumentaires.detaille, /n'est pas de l'antisémitisme/); // critique d'Israël ≠ antisémitisme
    assert.match(as.argumentaires.detaille, /ne suffit pas à l'exonérer/); // mais pas d'absolution automatique
  });

  test('comparaison « islamo-gauchisme » / « judéo-bolchevisme » : jamais présentée comme identique', () => {
    const c = byId('islamo-gauchisme-judeo-bolchevisme-comparaison');
    assert.match(c.argumentaires.court, /ne sont pas identiques/);
    assert.match(c.resume, /fausse si l'on prétend que les deux expressions sont identiques/);
    assert.ok(c.rubriques.includes('islamo-gauchisme-laicite'));
  });

  test('chaque citation renvoie à une source consultée', () => {
    let n = 0;
    for (const e of lib) for (const c of e.citations || []) { n++; assert.equal(e.sources[c.source].consultee, true, e.id); }
    assert.ok(n >= 5);
  });

  test('validateEntry : page d’accueil, fiabilité inconnue, argumentaire manquant refusés ; verdict facultatif accepté', () => {
    assert.equal(isHomepageUrl('https://www.insee.fr/'), true);
    assert.equal(isHomepageUrl('https://www.insee.fr'), true);
    assert.equal(isHomepageUrl('https://www.europenowjournal.org/?p=11603'), false);
    assert.equal(isHomepageUrl('https://www.insee.fr/fr/statistiques/8612512'), false);
    const e = readFiche('laicite-loi-1905');
    e.verdict = null;
    assert.deepEqual(validateEntry(e), []);
    e.sources[0].url = 'https://www.legifrance.gouv.fr/';
    e.fiabilite = 'certain';
    delete e.argumentaires.empathie;
    e.rubriques = ['inconnue'];
    const errs = validateEntry(e);
    assert.ok(errs.some((m) => m.includes("page d'accueil")));
    assert.ok(errs.some((m) => m.includes('fiabilité inconnue')));
    assert.ok(errs.some((m) => m.includes('empathie')));
    assert.ok(errs.some((m) => m.includes('rubriques')));
  });

  test('aucune source de fiche n’est une page d’accueil', () => {
    for (const e of lib) for (const s of e.sources) assert.equal(isHomepageUrl(s.url), false, `${e.id} : ${s.url}`);
  });
});

describe('recherche locale', () => {
  test('correspondances fortes, insensibles aux accents et à la casse', () => {
    assert.equal(matchLocal(lib, 'la police tue')[0].fiche.id, 'lfi-contre-police');
    assert.equal(matchLocal(lib, 'la police tue')[0].force, 'forte');
    assert.equal(matchLocal(lib, 'Mélenchon crie tout le temps')[0].fiche.id, 'melenchon-crie');
    assert.equal(matchLocal(lib, 'MELENCHON CRIE')[0].fiche.id, 'melenchon-crie');
    assert.equal(matchLocal(lib, 'LFI est antisémite')[0].fiche.id, 'lfi-antisemite');
    assert.equal(matchLocal(lib, 'Les immigrés touchent plus d’aides')[0].fiche.id, 'immigres-aides');
    assert.equal(matchLocal(lib, 'les chômeurs ne veulent pas travailler')[0].fiche.id, 'chomeurs-travailler');
    assert.equal(matchLocal(lib, 'programme du CNR')[0].fiche.id, 'programme-cnr-1944');
  });

  test('aucune correspondance pour un sujet absent', () => {
    assert.deepEqual(matchLocal(lib, 'le prix du pain au Moyen Âge'), []);
    assert.deepEqual(matchLocal(lib, 'zzzz qqqq'), []);
  });

  test('filtres par rubrique et par fiabilité', () => {
    const r = searchLibrary(lib, '', null, null, { rubrique: 'melenchon-lfi' });
    assert.ok(r.length >= 11 && r.every((e) => e.rubriques.includes('melenchon-lfi')));
    const d = searchLibrary(lib, '', null, null, { fiabilite: 'debat' });
    assert.ok(d.length > 0 && d.every((e) => e.fiabilite === 'debat'));
    assert.equal(searchLibrary(lib, 'laïcité 1905')[0].id, 'laicite-loi-1905');
  });
});

describe('décision : fiche seule ou complément web', () => {
  const strong = (id) => ({ fiche: byId(id), force: 'forte' });
  test('fait historique stable → pas de recherche web', () => {
    assert.equal(decideWeb(strong('front-populaire-1936'), { freshOpts: TODAY }).web, false);
  });
  test('donnée évolutive à jour → pas de recherche web', () => {
    const d = decideWeb(strong('impots-assistanat'), { freshOpts: TODAY });
    assert.equal(d.web, false);
    assert.equal(d.motif, 'fiche_a_jour');
  });
  test('actualité, fiche à actualiser, sujet non couvert, demande fraîche → recherche web', () => {
    assert.equal(decideWeb(strong('lfi-antisemite'), { freshOpts: TODAY }).motif, 'actualite');
    assert.equal(decideWeb(strong('chomeurs-travailler'), { freshOpts: TODAY }).motif, 'a_actualiser');
    assert.equal(decideWeb(undefined).motif, 'non_couvert');
    assert.equal(decideWeb({ fiche: byId('rsa-smic'), force: 'partielle' }).motif, 'non_couvert');
    assert.equal(decideWeb(strong('front-populaire-1936'), { fraiche: true }).motif, 'demande');
  });
});

describe('comparaison web ↔ fiche', () => {
  test('verdict différent et nouvelle source consultée → proposition de mise à jour', () => {
    const fiche = byId('impots-assistanat');
    const dossier = {
      verdict: 'confirme', verdict_label: 'Confirmé',
      faits: [{ fait: 'Les dépenses publiques atteignent 1 700 Md€ en 2025.', chiffre: '1 700 Md€' }],
      sources: [
        { titre: 'Nouveau', organisme: 'Insee', url: 'https://www.insee.fr/fr/statistiques/1234567', acces: 'document_consulte' },
        { titre: 'Ancienne', organisme: 'Insee', url: fiche.sources[0].url, acces: 'document_consulte' },
      ],
    };
    const c = compareWithFiche(dossier, fiche);
    assert.equal(c.contradiction_possible, true);
    assert.equal(c.mise_a_jour_proposee, true);
    assert.deepEqual(c.sources_communes, [fiche.sources[0].url]);
    assert.equal(c.nouvelles_sources.length, 1);
    assert.ok(c.chiffres_fiche_absents.length >= 1);
    assert.ok(c.signaux.length >= 2);
  });

  test('mêmes conclusions, aucune source nouvelle consultée → pas de proposition', () => {
    const fiche = byId('impots-assistanat');
    const c = compareWithFiche({ verdict: 'contredit', faits: [], sources: [{ url: fiche.sources[0].url, acces: 'document_consulte' }, { url: 'https://exemple.fr/extrait', acces: 'extrait_recherche' }] }, fiche);
    assert.equal(c.contradiction_possible, false);
    assert.equal(c.mise_a_jour_proposee, false);
  });
});

describe('API base locale', () => {
  const ASK = { affirmation: 'Les impôts ne servent qu’à payer l’assistanat.', volet: 'economie', mode: 'gagner', profil: 'colerique', contexte: 'repas' };

  test('GET /api/kb/search : correspondances immédiates, sans appel externe', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(testConfig({ liveMode: true, apiKey: 'sk-test' }), { fetchImpl: f });
    try {
      const d = await (await s.get(`/api/kb/search?q=${encodeURIComponent('la police tue')}`)).json();
      assert.equal(d.correspondances[0].id, 'lfi-contre-police');
      assert.equal(d.correspondances[0].force, 'forte');
      assert.ok(d.correspondances[0].court.length > 20);
      assert.equal(typeof d.decision.web_complementaire, 'boolean');
      assert.equal(f.calls.length, 0);
      assert.equal((await s.get('/api/kb/search?q=a')).status, 400);
      const rub = await (await s.get('/api/library?rubrique=melenchon-lfi')).json();
      assert.ok(rub.fiches.length >= 11 && rub.fiches.every((x) => x.rubriques.includes('melenchon-lfi')));
      const fia = await (await s.get('/api/library?fiabilite=debat')).json();
      assert.ok(fia.fiches.every((x) => x.fiabilite === 'debat'));
    } finally { await s.close(); }
  });

  test('mode démonstration : les fiches locales sont proposées, aucune recherche simulée', async () => {
    const s = await startServer(testConfig({ liveMode: false, apiKey: '' }));
    try {
      const d = await (await s.post('/api/analyse', { affirmation: 'Mélenchon crie tout le temps', volet: 'politique' })).json();
      assert.equal(d.mode, 'demo');
      assert.equal(d.base_locale.correspondances[0].id, 'melenchon-crie');
      assert.equal(d.strategie, undefined);
      assert.equal(d.dossier, undefined);
    } finally { await s.close(); }
  });

  test('fiche forte et à jour : réponse construite sur la fiche, sans recherche web', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(testConfig({ liveMode: true, apiKey: 'sk-test', kbDirectAnswer: true }), { fetchImpl: f });
    try {
      const d = await (await s.post('/api/analyse', ASK)).json();
      assert.equal(d.origine, 'bibliotheque');
      assert.equal(d.fiche_id, 'impots-assistanat');
      assert.equal(d.base_locale.decision.web_complementaire, false);
      assert.equal(f.calls.filter((c) => c.kind === 'research').length, 0);
      assert.equal(f.calls.filter((c) => c.kind === 'gagner').length, 1);
      assert.ok(d.dossier.sources.every((x) => x.acces === 'document_consulte' || x.acces === 'non_consulte'));
    } finally { await s.close(); }
  });

  test('recherche fraîche demandée : complément web comparé à la fiche, proposition consignée en cas d’écart', async () => {
    const routes = defaultRoutes();
    routes.research = researchResponse({ json: { ...DOSSIER_JSON, verdict: 'plutot_exact' } });
    const f = routerFetch(routes);
    const cfg = testConfig({ liveMode: true, apiKey: 'sk-test', kbDirectAnswer: true });
    const s = await startServer(cfg, { fetchImpl: f });
    try {
      const d = await (await s.post('/api/analyse', { ...ASK, fraiche: true })).json();
      assert.equal(d.origine, 'recherche');
      assert.equal(d.base_locale.decision.motif, 'demande');
      assert.equal(f.calls.filter((c) => c.kind === 'research').length, 1);
      // les sources vérifiées de la fiche sont transmises comme pistes à la recherche
      assert.match(f.calls.find((c) => c.kind === 'research').body.messages[0].content, /insee\.fr\/fr\/statistiques\/8735252/);
      assert.equal(d.comparaison_fiche.fiche_id, 'impots-assistanat');
      assert.ok(d.comparaison_fiche.sources_communes.some((u) => u.includes('8735252')));
      if (d.comparaison_fiche.mise_a_jour_proposee) {
        assert.ok(existsSync(cfg.updatesFile));
        const line = JSON.parse(readFileSync(cfg.updatesFile, 'utf8').trim().split('\n')[0]);
        assert.equal(line.statut, 'a_examiner');
        assert.equal(line.fiche_id, 'impots-assistanat');
      }
      // la fiche elle-même n'est jamais modifiée
      assert.equal(readFiche('impots-assistanat').verdict, 'contredit');
    } finally { await s.close(); }
  });

  test('sujet d’actualité : recherche web lancée même avec une fiche forte', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(testConfig({ liveMode: true, apiKey: 'sk-test', kbDirectAnswer: true }), { fetchImpl: f });
    try {
      const d = await (await s.post('/api/analyse', { affirmation: 'LFI est antisémite', volet: 'politique', mode: 'gagner' })).json();
      assert.equal(d.base_locale.decision.motif, 'actualite');
      assert.equal(f.calls.filter((c) => c.kind === 'research').length, 1);
      assert.equal(d.comparaison_fiche.fiche_id, 'lfi-antisemite');
    } finally { await s.close(); }
  });

  test('erreur de source côté web : la base locale reste renvoyée par /api/kb/search', async () => {
    const routes = defaultRoutes();
    routes.research = researchResponse({ json: DOSSIER_JSON, searchError: 'unavailable', fetched: [], fetchErrors: [] });
    const f = routerFetch(routes);
    const s = await startServer(testConfig({ liveMode: true, apiKey: 'sk-test', kbDirectAnswer: true }), { fetchImpl: f });
    try {
      const r = await s.post('/api/analyse', { affirmation: 'LFI est antisémite', volet: 'politique' });
      assert.equal(r.status, 503);
      const err = await r.json();
      assert.equal(err.relancer, true);
      const kb = await (await s.get(`/api/kb/search?q=${encodeURIComponent('LFI est antisémite')}`)).json();
      assert.equal(kb.correspondances[0].id, 'lfi-antisemite');
    } finally { await s.close(); }
  });
});

test('GOOD_URL des tests correspond bien à une source de fiche (pistes)', () => {
  assert.ok(byId('impots-assistanat').sources.some((s) => s.url === GOOD_URL));
});
