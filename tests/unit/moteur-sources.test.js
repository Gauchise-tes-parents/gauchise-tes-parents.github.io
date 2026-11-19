// Chercheur de sources du moteur interne (sans IA) : réponses FICTIVES des services, aucun accès réseau.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { motsCles, lireHal, lireOpenAlex, lireDataGouv, lireRss, filtrer, chercherSources, pistesMarkdown } from '../../scripts/moteur/sources.js';

const HAL = { response: { docs: [
  { title_s: ['Les retraites des immigrés en France'], uri_s: 'https://hal.science/hal-0001', producedDateY_i: 2021, authFullName_s: ['A. Chercheuse'], abstract_s: ['Étude sur les pensions de retraite et le minimum vieillesse des immigrés.'] },
  { title_s: ['Un sujet sans rapport'], uri_s: 'https://hal.science/hal-0002', producedDateY_i: 2019 },
] } };
const OA = { results: [{ title: 'Immigration et retraites : une évaluation', publication_year: 2020, primary_location: { landing_page_url: 'https://doi.org/10.1234/x', source: { display_name: 'Revue économique' } }, authorships: [{ author: { display_name: 'B. Auteur' } }] }] };
const DG = { data: [
  { title: 'Bénéficiaires du minimum vieillesse', page: 'https://www.data.gouv.fr/fr/datasets/minimum-vieillesse/', organization: { name: 'Direction de la recherche, des études, de l’évaluation et des statistiques (DREES)' }, last_update: '2025-06-01T00:00:00', description: 'Retraites et minimum vieillesse par nationalité.' },
  { title: 'Retraites des immigrés selon un observatoire partisan', page: 'https://www.data.gouv.fr/fr/datasets/x/', organization: { name: 'Observatoire de l’immigration et de la démographie' }, description: 'retraites immigres' },
] };
const RSS = `<?xml version="1.0"?><rss><channel><item><title><![CDATA[Les immigrés touchent-ils plus de retraite que les Français ?]]></title><link>https://www.lemonde.fr/les-decodeurs/article/2026/01/01/x.html</link><pubDate>Thu, 01 Jan 2026 10:00:00 +0100</pubDate><description>Vérification sur les retraites.</description></item><item><title>Autre sujet</title><link>http://insecure.example/x</link></item></channel></rss>`;

const repondre = (url) => {
  if (url.includes('archives-ouvertes')) return { ok: true, json: async () => HAL };
  if (url.includes('openalex')) return { ok: true, json: async () => OA };
  if (url.includes('data.gouv')) return { ok: true, json: async () => DG };
  if (url.includes('rss')) return { ok: true, text: async () => RSS };
  return { ok: false, status: 404, text: async () => '' };
};
const fetchFictif = async (url) => repondre(url);
const Q = 'Les immigrés touchent des retraites sans avoir cotisé.';

describe('chercheur de sources (sans IA)', () => {
  test('mots-clés porteurs, sans mots vagues', () => {
    const m = motsCles('En France, les immigrés touchent plus de retraite que tout le monde');
    assert.ok(m.includes('immigres') && m.includes('retraite'), m.join(','));
    assert.ok(!m.includes('france') && !m.includes('plus'));
  });

  test('lecteurs des services : HAL, OpenAlex, data.gouv.fr, RSS', () => {
    assert.equal(lireHal(HAL)[0].url, 'https://hal.science/hal-0001');
    assert.match(lireHal(HAL)[0].organisme, /CNRS/);
    assert.equal(lireOpenAlex(OA)[0].date, '2020');
    assert.match(lireDataGouv(DG)[0].organisme, /DREES/);
    const r = lireRss(RSS, 'Le Monde — Les Décodeurs');
    assert.equal(r[0].titre, 'Les immigrés touchent-ils plus de retraite que les Français ?');
    assert.equal(r[0].date, '2026-01-01');
  });

  test('filtre : pertinence, https seulement, sources de droite écartées, autorités en tête', () => {
    const mots = motsCles(Q);
    const p = filtrer([...lireHal(HAL), ...lireDataGouv(DG), ...lireRss(RSS, 'Le Monde — Les Décodeurs')], mots);
    assert.ok(!p.some((x) => /sans rapport/.test(x.titre)), 'piste hors sujet gardée');
    assert.ok(!p.some((x) => /Observatoire de l’immigration/.test(x.organisme)), 'source de droite gardée');
    assert.ok(!p.some((x) => x.url.startsWith('http:')), 'lien non sécurisé gardé');
    assert.ok(['recherche', 'institution'].includes(p[0].classe), p[0].classe);
  });

  test('recherche complète avec un service en panne : pistes quand même, panne signalée, rien d’inventé', async () => {
    const enPanne = async (url) => (url.includes('openalex') ? { ok: false, status: 503, text: async () => 'indisponible' } : repondre(url));
    const r = await chercherSources(Q, { fetchImpl: enPanne, journal: { warn() {} } });
    assert.ok(r.pistes.length >= 2, `${r.pistes.length} pistes`);
    assert.ok(r.erreurs.some((e) => /OpenAlex/.test(e)));
    for (const p of r.pistes) assert.ok([...lireHal(HAL), ...lireDataGouv(DG), ...lireRss(RSS, 'x')].some((b) => b.url === p.url), `piste inventée : ${p.url}`);
    const md = pistesMarkdown(r);
    assert.match(md, /NON LUES/);
    assert.match(md, /Services indisponibles/);
  });

  test('aucun accès réseau sans mot-clé exploitable', async () => {
    let appels = 0;
    const r = await chercherSources('Et alors ?', { fetchImpl: async (u) => { appels += 1; return fetchFictif(u); } });
    assert.equal(appels, 0);
    assert.deepEqual(r.pistes, []);
  });
});
