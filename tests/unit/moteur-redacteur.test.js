// Rédacteur du moteur interne (sans IA) : fiches rédigées à partir de pistes FICTIVES, aucun accès réseau.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { redigerFiche, pistesCitables } from '../../scripts/moteur/redacteur.js';
import { controler } from '../../scripts/moteur/fiches.js';
import { validateEntry, loadLibrary } from '../../server/library.js';
import { auditFiche } from '../../public/js/ligne-editoriale.js';
import { resoudrePhrase } from '../../public/js/analyse.js';

const Q = 'Les chômeurs refusent les offres d’emploi qu’on leur propose';
const PISTES = [
  { origine: 'hal', titre: 'Les bienfaits de l’emploi dégradé', url: 'https://sciencespo.hal.science/hal-00000001v1', organisme: 'HAL (archive ouverte de la recherche, CNRS)', auteurs: 'A. Chercheur', date: '2019', extrait: 'Cette enquête auprès de conseillers et de demandeurs d’emploi montre comment des offres de mauvaise qualité finissent par être acceptées sous la contrainte des contrôles.' },
  { origine: 'hal', titre: 'Les offres d’emploi non pourvues : un mythe tenace', url: 'https://hal.science/hal-00000002v1', organisme: 'HAL (archive ouverte de la recherche, CNRS) — Travail et Emploi', auteurs: 'B. Autrice', date: '2021', extrait: 'L’article analyse les offres d’emploi déposées et montre qu’une partie importante est pourvue ou retirée, et que les refus tiennent souvent aux conditions proposées (horaires, salaire, distance).' },
  { origine: 'openalex', titre: 'Sans résumé', url: 'https://doi.org/10.1/x', organisme: 'Publication scientifique (OpenAlex)', date: '2015', extrait: '' },
];
const PROGRAMME = [{ texte: 'Créer une garantie d’emploi pour les chômeurs de longue durée', chapitre: 'Chapitre 1', section: 'Emploi', url: 'https://melenchon2027.fr/programme/livre/x/chapitre1/' }];
const lib = loadLibrary(undefined, { warn() {} }).filter((f) => f.type !== 'science');

describe('rédacteur du moteur (sans IA)', () => {
  const { fiche } = redigerFiche(Q, { pistes: PISTES, programme: PROGRAMME, jour: '2026-11-19' });

  test('fiche complète au format de la bibliothèque, conforme à la politique documentaire', () => {
    assert.ok(fiche, 'pas de fiche');
    assert.deepEqual(validateEntry(fiche), []);
    assert.deepEqual(auditFiche(fiche), []);
    for (const k of ['court', 'moyen', 'detaille', 'empathie']) assert.ok(fiche.argumentaires[k].length > 20, k);
    assert.ok(fiche.publics.convaincus && fiche.publics.indecis);
    assert.ok(fiche.lecture.valeurs.length >= 2 && fiche.lecture.defavorables.length >= 1);
    assert.doesNotMatch(JSON.stringify(fiche.lecture), /\d/, 'chiffre dans la lecture de gauche');
  });

  test('honnête : sans verdict, résumés cités mot pour mot, rien d’inventé, limites dites', () => {
    assert.equal(fiche.verdict, null);
    assert.equal(fiche.origine, 'moteur');
    assert.equal(fiche.moteur.redacteur, true);
    for (const p of PISTES.filter((x) => x.extrait)) assert.ok(JSON.stringify(fiche.faits).includes(p.extrait.replace(/[.\s]+$/, '')), `résumé non cité tel quel : ${p.titre}`);
    const urls = new Set([...PISTES.map((p) => p.url), ...PROGRAMME.map((m) => m.url)]);
    for (const s of fiche.sources) assert.ok(urls.has(s.url), `source inventée : ${s.url}`);
    assert.ok(fiche.sources.find((s) => s.url === 'https://doi.org/10.1/x')?.consultee === false, 'piste sans résumé présentée comme lue');
    assert.ok(fiche.faits.some((f) => /^Limite/.test(f.fait)));
    assert.ok(fiche.limites.some((l) => /sans IA/.test(l)));
  });

  test('garde-fous : la question mène à la fiche, aucune autre phrase détournée', () => {
    const phrases = lib.slice(0, 120).map((f) => f.affirmation);
    const avant = new Map(phrases.map((p) => [p, resoudrePhrase(p, lib).fiche?.id || null]));
    assert.deepEqual(controler(fiche, { bibliotheque: lib, phrasesControle: phrases, avant }), []);
  });

  test('matière insuffisante : pas de fiche, une raison', () => {
    assert.ok(redigerFiche(Q, { pistes: [PISTES[2]], programme: PROGRAMME }).raison);
    assert.ok(redigerFiche(Q, { pistes: [PISTES[0]], programme: [] }).raison);
    assert.equal(pistesCitables([{ ...PISTES[0], organisme: 'Le Figaro', url: 'https://www.lefigaro.fr/x' }]).length, 0, 'source de droite citée');
  });
});
