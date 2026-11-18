// Moteur interne de fiches (v15, sans IA) : lecture du programme, chiffres officiels, assemblage et garde-fous.
// Les pages utilisées ici sont FICTIVES (tests/fixtures/moteur) : aucun accès réseau pendant les tests.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { analyserChapitre, chapitresDepuisIndex, releverAec, mesuresAPlat } from '../../scripts/moteur/aec.js';
import { lireJsonStat, releverChiffres, INDICATEURS } from '../../scripts/moteur/chiffres.js';
import { ajouter, cleQuestion } from '../../scripts/moteur/file.js';
import { assemblerFiche, controler, mesuresPertinentes, radical } from '../../scripts/moteur/fiches.js';
import { nettoyer, createHandler } from '../../worker-questions/src/handler.js';
import { loadLibrary } from '../../server/library.js';
import { resoudrePhrase } from '../../public/js/analyse.js';

const FX = new URL('../fixtures/moteur/', import.meta.url);
const html = (n) => readFileSync(new URL(n, FX), 'utf8');
const URL_CHAP = 'https://exemple.test/programme/livre/le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite/chapitre3/';
const chap = analyserChapitre(html('chapitre.html'), URL_CHAP);
const corpus = { releve_le: '2026-11-18', chapitres: [chap] };
const JS = JSON.parse(html('eurostat.json'));
const chiffres = { indicateurs: Object.fromEntries(INDICATEURS.map((i) => [i.id, { ...i, valeur: 12.5, periode: '2025', url: `https://ec.europa.eu/eurostat/databrowser/view/${i.jeu}/default/table?lang=fr`, releve_le: '2026-11-18' }])) };
const lib = loadLibrary(undefined, { warn() {} }).filter((f) => f.type !== 'science');

describe('programme L’Avenir en commun', () => {
  test('lecture d’un chapitre : partie, titre, sections, mesure clé, puces ; navigation et scripts ignorés', () => {
    assert.equal(chap.titre, 'Chapitre 3 : Humaniser par la culture et le sport');
    assert.match(chap.partie_titre, /Partie 4/);
    assert.equal(chap.volet, 'services');
    assert.deepEqual(chap.sections.map((s) => s.titre), ['Des vacances pour tous les enfants', 'Des bibliothèques ouvertes']);
    assert.match(chap.sections[0].mesure_cle, /colonies de vacances/);
    assert.equal(chap.sections[0].mesures.length, 2, 'puce trop courte écartée');
    assert.ok(!JSON.stringify(chap).includes('piège') && !JSON.stringify(chap).includes('Ne doit pas') && !JSON.stringify(chap).includes('Menu du site'));
    assert.equal(mesuresAPlat(corpus).length, 5);
  });
  test('table des matières : chapitres du même site, dédoublonnés', () => {
    const u = chapitresDepuisIndex(html('index.html'), 'https://exemple.test/programme/livre/');
    assert.equal(u.length, 5);
    assert.ok(u.every((x) => x.startsWith('https://exemple.test/') && x.endsWith('/')));
  });
  test('un relevé incomplet échoue au lieu d’écraser le corpus', async () => {
    const f = async (url) => ({ ok: true, text: async () => (url.endsWith('/livre/') ? html('index.html') : html('chapitre.html')) });
    await assert.rejects(releverAec({ fetchImpl: f, index: 'https://exemple.test/programme/livre/', attente: 0, journal: {} }), /incomplet/);
  });
});

describe('chiffres officiels (Eurostat)', () => {
  test('JSON-stat : dernière valeur de l’unique série', () => {
    assert.deepEqual(lireJsonStat(JS), { valeur: 7.6, periode: '2026-09', mise_a_jour_source: '2026-11-01T11:00:00+0100' });
  });
  test('filtre incomplet refusé (jamais de valeur ambiguë)', () => {
    assert.throws(() => lireJsonStat({ ...JS, size: [1, 2, 2] }), /filtre incomplet/);
  });
  test('indicateur illisible : dernière valeur connue conservée, rien d’inventé', async () => {
    const anciens = { indicateurs: { chomage: { id: 'chomage', valeur: 7.4, periode: '2026-08' } } };
    const { chiffres: c } = await releverChiffres({ fetchImpl: async () => ({ ok: false, status: 503 }), anciens, journal: {} });
    assert.equal(c.indicateurs.chomage.valeur, 7.4);
    assert.ok(c.indicateurs.chomage.erreur_dernier_releve);
    assert.equal(Object.keys(c.indicateurs).length, 1);
  });
});

describe('file des questions', () => {
  test('dédoublonnage et comptage', () => {
    const file = {};
    assert.equal(ajouter(file, ['Les colonies, c’est fini !', 'les colonies c est fini', 'x'], 'site', '2026-11-18'), 1);
    assert.equal(file.questions[cleQuestion('Les colonies, c’est fini !')].occurrences, 2);
  });
  test('radical : rapproche les formes d’un même mot', () => {
    assert.equal(radical('bibliotheques'), radical('bibliotheque'));
  });
});

describe('assemblage et garde-fous', () => {
  const Q = 'Les colonies de vacances sont devenues trop chères pour les familles modestes';
  test('mesures pertinentes du programme', () => {
    const m = mesuresPertinentes(Q, corpus);
    assert.ok(m.length >= 2);
    assert.match(m[0].texte, /colonies/);
    assert.ok(!m.some((x) => /bibliothèques/.test(x.texte)));
  });
  test('fiche valide, honnête (sans verdict) et conforme à la politique documentaire', () => {
    const { fiche } = assemblerFiche(Q, { corpus, chiffres, jour: '2026-11-18' });
    assert.equal(fiche.origine, 'moteur');
    assert.equal(fiche.verdict, null);
    assert.ok(fiche.publics.convaincus && fiche.publics.indecis);
    assert.ok(fiche.faits.some((f) => /L’Avenir en commun propose/.test(f.fait)));
    assert.ok(fiche.sources.some((s) => /Eurostat/.test(s.organisme)));
    assert.ok(fiche.limites.some((l) => /sans IA/.test(l)));
    const avant = new Map(lib.slice(0, 60).map((f) => [f.affirmation, resoudrePhrase(f.affirmation, lib).fiche?.id || null]));
    assert.deepEqual(controler(fiche, { bibliotheque: lib, phrasesControle: [...avant.keys()], avant }), []);
  });
  test('sujet absent du programme : pas de fiche, une raison', () => {
    assert.match(assemblerFiche('Les bateaux de pêche bretons sont trop vieux', { corpus, chiffres }).raison, /programme/);
  });
  test('détournement d’une phrase de contrôle détecté', () => {
    const { fiche } = assemblerFiche(Q, { corpus, chiffres, jour: '2026-11-18' });
    const avant = new Map([[Q, 'une-autre-fiche']]);
    assert.ok(controler(fiche, { bibliotheque: lib, phrasesControle: [Q], avant }).some((p) => /détournerait/.test(p)));
  });
});

describe('collecteur de questions (Worker séparé)', () => {
  const kv = () => { const m = new Map(); return { m, get: async (k) => m.get(k) ?? null, put: async (k, v) => { m.set(k, v); }, delete: async (k) => { m.delete(k); }, list: async ({ prefix }) => ({ keys: [...m.keys()].filter((k) => k.startsWith(prefix)).map((name) => ({ name })), list_complete: true }) }; };
  const env = () => ({ QUESTIONS: kv(), ALLOWED_ORIGINS: 'https://site.test', EXPORT_TOKEN: 'jeton', SEL: 's' });
  const post = (body, origin = 'https://site.test') => new Request('https://w.test/questions', { method: 'POST', headers: { origin, 'content-type': 'application/json', 'cf-connecting-ip': '1.2.3.4' }, body: JSON.stringify(body) });
  test('données personnelles retirées', () => {
    assert.equal(nettoyer('écris-moi à jean@exemple.fr ou au 06 12 34 56 78 https://x.fr'), 'écris-moi à [adresse retirée] ou au [numéro retiré] [lien retiré]');
  });
  test('seul le texte est stocké ; jamais l’adresse IP ; export protégé par jeton', async () => {
    const h = createHandler(); const e = env();
    assert.equal((await h(post({ texte: 'Les colonies de vacances sont trop chères', nom: 'Jean' }), e)).status, 201);
    const stocke = [...e.QUESTIONS.m.values()].join(' ');
    assert.ok(!stocke.includes('1.2.3.4') && !stocke.includes('Jean'));
    assert.equal((await h(new Request('https://w.test/export'), e)).status, 401);
    const r = await h(new Request('https://w.test/export?purger=1', { headers: { authorization: 'Bearer jeton' } }), e);
    assert.deepEqual((await r.json()).questions.map((q) => q.texte), ['Les colonies de vacances sont trop chères']);
    assert.equal([...e.QUESTIONS.m.keys()].filter((k) => k.startsWith('q:')).length, 0);
  });
  test('autre site refusé ; abus limité', async () => {
    const h = createHandler(); const e = env();
    assert.equal((await h(post({ texte: 'Une question valable' }, 'https://pirate.test'), e)).status, 403);
    for (let i = 0; i < 20; i += 1) await h(post({ texte: `Question numéro ${i} assez longue` }), e);
    assert.equal((await h(post({ texte: 'Une question de trop' }), e)).status, 429);
  });
});
