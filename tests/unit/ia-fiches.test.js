// Phase bêta — fiches sur mesure créées par l'IA. Google (Gemini, pages consultées) et GitHub sont SIMULÉS au format
// de leurs API ; on vérifie notre code : rattachement des faits aux pages, refus sans sources, validation par le
// VRAI validateur de la bibliothèque, enregistrement, aucun doublon, aucun appel inutile.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary, validateEntry } from '../../server/library.js';
import { buildKb } from '../../server/kbexport.js';
import { createHandler } from '../../worker/src/handler.js';
import { idFiche } from '../../worker/src/fiche.js';

const FICHES = JSON.parse(buildKb(loadLibrary(undefined, { warn() {} })).json).fiches;
const ORIGINE = 'https://gauchise-tes-parents.github.io';
const ENV = { GEMINI_API_KEY: 'cle-test', GEMINI_MODEL: 'gemini-test', ALLOWED_ORIGINS: ORIGINE, FICHES_IA: '1', GITHUB_TOKEN: 'jeton-test', GITHUB_REPO: 'Gauchise-tes-parents/gauchise-tes-parents.github.io', LIMITE_PAR_VISITEUR: '100' };
const Q = 'Les pistes cyclables tuent le commerce de centre-ville ?';

const FICHE_IA = {
  affirmation: 'Les pistes cyclables tuent le commerce de centre-ville.', volet: 'ecologie', sous_theme: 'Transports', verdict: 'trompeur',
  mots_cles: ['pistes cyclables', 'vélo', 'commerce', 'centre-ville'],
  resume: 'Les études disponibles ne montrent pas de baisse du commerce liée aux pistes cyclables ; les cyclistes dépensent souvent autant que les automobilistes.',
  contexte: 'Des commerçants craignent que la suppression de places de stationnement fasse fuir la clientèle.',
  explication: 'Les commerçants surestiment souvent la part de leurs clients venus en voiture ; les effets dépendent des aménagements.',
  faits: [
    { fait: 'Les commerçants surestiment la part de clients venant en voiture', chiffre: null, periode: '2020', perimetre: 'France', explication: 'La perception diffère des comportements réels.', fiabilite: 'etabli' },
    { fait: 'Les clients à vélo viennent plus souvent dans les commerces de proximité', chiffre: null, periode: '2021', perimetre: 'France', explication: 'Fréquence plus élevée.', fiabilite: 'estimation' },
    { fait: 'Un fait inventé que personne ne soutient', chiffre: '99 %', periode: '2022', perimetre: 'France', explication: 'Doit disparaître.', fiabilite: 'etabli' },
  ],
  court: 'Faux : les études montrent que les clients à vélo viennent plus souvent, et les commerçants surestiment la voiture.',
  moyen: 'Premier paragraphe argumenté sur les données disponibles.\n\nDeuxième paragraphe sur les choix d’aménagement.',
  detaille: 'Premier paragraphe détaillé.\n\nDeuxième paragraphe détaillé.\n\nTroisième paragraphe détaillé.',
  empathie: 'Je comprends l’inquiétude des commerçants, mais les études montrent que les clients à pied et à vélo sont fidèles.',
  contre_arguments: [{ objection: 'Sans parking, plus de clients.', reponse: 'La plupart des clients viennent à pied, à vélo ou en transports.' }],
  questions: ['Combien de tes clients viennent vraiment en voiture ?'], limites: ['Les effets varient selon les villes.'], objections_legitimes: ['Les travaux peuvent gêner temporairement.'],
  lecture: { valeurs: ['services_publics', 'solidarite', 'inexistante'], mecanismes: 'La voiture individuelle occupe l’espace public au détriment des autres usages.', consequences: 'Pollution et insécurité routière.', democratie: 'Partage de l’espace public.', propositions: ['Aménagements cyclables sécurisés.'], defavorables: [{ fait: 'Les travaux gênent temporairement.', integration: 'Accompagner les commerçants.' }] },
};
const PAGE1 = 'https://www.insee.fr/fr/statistiques/1234567';
const PAGE2 = 'https://www.ademe.fr/etude-velo-commerce';

function monde({ supports = true, existante = null } = {}) {
  const appels = { gemini: 0, put: null, urls: [] };
  const fn = async (url, init = {}) => {
    appels.urls.push(url);
    if (url.includes('generativelanguage')) {
      appels.gemini += 1;
      const texte = JSON.stringify(FICHE_IA);
      return { ok: true, status: 200, json: async () => ({ candidates: [{ finishReason: 'STOP', content: { parts: [{ text: texte }] }, groundingMetadata: {
        webSearchQueries: ['pistes cyclables commerce étude'],
        groundingChunks: [{ web: { uri: 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/A', title: 'insee.fr' } }, { web: { uri: 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/B', title: 'ademe.fr' } }],
        groundingSupports: supports ? [
          { segment: { text: 'Les commerçants surestiment la part de clients venant en voiture' }, groundingChunkIndices: [0] },
          { segment: { text: 'Les clients à vélo viennent plus souvent dans les commerces de proximité' }, groundingChunkIndices: [1] },
        ] : [],
      } }] }) };
    }
    if (url.endsWith('/grounding-api-redirect/A')) return { ok: false, status: 302, headers: new Headers({ location: PAGE1 }) };
    if (url.endsWith('/grounding-api-redirect/B')) return { ok: false, status: 302, headers: new Headers({ location: PAGE2 }) };
    if (url === PAGE1) return { ok: true, status: 200, text: async () => '<html><head><title>Mobilités et commerce | Insee</title></head></html>' };
    if (url === PAGE2) return { ok: true, status: 200, text: async () => '<html><head><title>Vélo et commerce de proximité &amp; centres-villes</title></head></html>' };
    if (url.includes('api.github.com')) {
      if (url.includes('/contents/') && init.method === 'PUT') { appels.put = JSON.parse(init.body); return { status: 201, json: async () => ({}) }; }
      if (url.includes('/contents/')) return existante ? { status: 200, text: async () => JSON.stringify(existante), json: async () => existante } : { status: 404, text: async () => '', json: async () => ({}) };
      if (url.includes('/git/ref/heads/')) return { status: 200, json: async () => ({ object: { sha: 'abc' } }) };
    }
    throw new Error(`appel inattendu : ${url}`);
  };
  fn.appels = appels;
  return fn;
}
const req = (question) => new Request('https://ia.example/api/ia/fiche', { method: 'POST', headers: { 'content-type': 'application/json', origin: ORIGINE, 'cf-connecting-ip': '203.0.113.5' }, body: JSON.stringify({ question }) });

describe('fiches sur mesure créées par l’IA (phase bêta)', () => {
  test('une question sans fiche → une fiche valide pour la bibliothèque, chaque fait rattaché à une page consultée', async () => {
    const f = monde();
    const r = await createHandler({ fiches: FICHES, fetchImpl: f, cache: null, journal: { log() {} } })(req(Q), ENV);
    const d = await r.json();
    assert.equal(r.status, 200, JSON.stringify(d));
    const fi = d.fiche;
    assert.deepEqual(validateEntry(fi), [], 'validée par le vrai validateur de la bibliothèque');
    assert.equal(fi.origine, 'ia'); assert.equal(fi.relecture, 'non_relue');
    assert.equal(fi.faits.length, 2, 'le fait que Google ne rattache à aucune page est retiré');
    assert.ok(!JSON.stringify(fi).includes('99 %'));
    assert.deepEqual(fi.sources.map((s) => s.url), [PAGE1, PAGE2], 'adresses réelles des pages, pas les liens de redirection');
    assert.equal(fi.sources[0].titre, 'Mobilités et commerce | Insee'); assert.equal(fi.sources[0].organisme, 'Insee');
    assert.equal(fi.sources[1].titre, 'Vélo et commerce de proximité & centres-villes');
    assert.ok(fi.faits.every((x) => x.fiabilite !== 'etabli'), 'un fait non relu n’est jamais présenté comme établi');
    assert.deepEqual(fi.lecture.valeurs, ['services_publics', 'solidarite'], 'valeur inconnue retirée');
    assert.match(fi.limites.at(-1), /pas encore été relue/);
    assert.equal(fi.id, await idFiche(Q));
    assert.equal(d.enregistrement, 'enregistree');
    assert.equal(f.appels.put.branch, 'fiches-ia');
    const enregistree = JSON.parse(Buffer.from(f.appels.put.content, 'base64').toString('utf8'));
    assert.equal(enregistree.id, fi.id);
    assert.equal(f.appels.gemini, 1, 'un seul appel à l’IA');
  });

  test('sans faits rattachés à des pages consultées : pas de fiche (rien d’inventé)', async () => {
    const f = monde({ supports: false });
    const r = await createHandler({ fiches: FICHES, fetchImpl: f, cache: null, journal: { log() {} } })(req(Q), ENV);
    assert.equal(r.status, 422);
    assert.equal(f.appels.put, null, 'rien n’est enregistré');
  });

  test('question déjà couverte par une fiche vérifiée : aucune fiche IA, aucun appel', async () => {
    const f = monde();
    const r = await createHandler({ fiches: FICHES, fetchImpl: f, cache: null, journal: { log() {} } })(req('Il y a des millions de cartes Vitale en trop.'), ENV);
    assert.equal(r.status, 409); assert.equal(f.appels.gemini, 0);
  });

  test('même question posée à nouveau : la fiche déjà créée est renvoyée, sans appeler l’IA', async () => {
    const f = monde({ existante: { id: 'ia-x', affirmation: 'Déjà créée' } });
    const d = await (await createHandler({ fiches: FICHES, fetchImpl: f, cache: null, journal: { log() {} } })(req(Q), ENV)).json();
    assert.equal(d.enregistrement, 'deja'); assert.equal(d.fiche.affirmation, 'Déjà créée'); assert.equal(f.appels.gemini, 0);
  });

  test('désactivé par défaut ; plafond de fiches par jour ; le statut l’annonce', async () => {
    const h = createHandler({ fiches: FICHES, fetchImpl: monde(), cache: null, journal: { log() {} } });
    assert.equal((await h(req(Q), { ...ENV, FICHES_IA: '0' })).status, 403);
    const h2 = createHandler({ fiches: FICHES, fetchImpl: monde(), cache: null, journal: { log() {} } });
    assert.equal((await h2(req(Q), { ...ENV, FICHES_IA_PAR_JOUR: '1' })).status, 200);
    assert.equal((await h2(req('Une autre question sur les trottinettes électriques ?'), { ...ENV, FICHES_IA_PAR_JOUR: '1' })).status, 429);
    const st = await (await h(new Request('https://ia.example/api/ia/statut', { headers: { origin: ORIGINE } }), ENV)).json();
    assert.equal(st.fiches_ia, true);
  });
});
