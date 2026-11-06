import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { loadLibrary, validateEntry, searchLibrary, freshness, summarize, LIBRARY_DIR } from '../../server/library.js';
import { validateAnalyseRequest } from '../../server/engine/options.js';
import { VOLETS, MODES, TIPEEE_URL, PROFILS } from '../../public/js/taxonomy.js';
import { silent } from '../helpers.js';

test('dix volets thématiques avec leurs sous-thèmes', () => {
  assert.equal(VOLETS.length, 10);
  assert.deepEqual(VOLETS.map((v) => v.id), ['immigration', 'securite', 'social', 'economie', 'ecologie', 'services', 'droits', 'politique', 'international', 'autre']);
  for (const v of VOLETS.slice(0, 9)) assert.ok(v.sousThemes.length >= 12, `${v.id} : sous-thèmes manquants`);
  assert.ok(VOLETS[1].sousThemes.includes('Violences intrafamiliales'));
  assert.ok(VOLETS[7].sousThemes.includes('Rassemblement national'));
  assert.ok(VOLETS[8].sousThemes.includes('Palestine et Israël'));
  assert.equal(VOLETS[9].sousThemes.length, 0); // saisie libre
});

test('deux publics (v14), libellés conformes', () => {
  assert.equal(MODES.gagner.label, 'ÉLECTEUR D’EXTRÊME DROITE CONVAINCU');
  assert.match(MODES.gagner.sousTitre, /sans l’humilier/);
  assert.equal(MODES.gagner.bouton, 'Préparer ma réponse');
  assert.equal(MODES.convaincre.label, 'INDÉCIS');
  assert.equal(MODES.convaincre.carte, 'INDÉCIS');
  assert.equal(MODES.convaincre.bouton, 'Préparer l’échange');
  assert.equal(PROFILS.length, 8);
});

test('toutes les fiches sont valides, rattachées à un volet et chargées', () => {
  const files = readdirSync(LIBRARY_DIR).filter((f) => f.endsWith('.json'));
  for (const f of files) {
    const e = JSON.parse(readFileSync(join(LIBRARY_DIR, f), 'utf8'));
    assert.deepEqual(validateEntry(e), [], `${f} invalide`);
    assert.equal(`${e.id}.json`, f);
  }
  assert.equal(loadLibrary(LIBRARY_DIR, silent).length, files.length);
});

test('chaque fait de fiche repose sur une source réellement consultée, datée, en https', () => {
  for (const e of loadLibrary(LIBRARY_DIR, silent)) {
    for (const f of e.faits) assert.equal(e.sources[f.source].consultee, true, `${e.id}`);
    for (const s of e.sources) { assert.match(s.url, /^https:\/\//); assert.ok(s.date_publication); }
    assert.ok(e.limites.length > 0);
  }
});

test('validateEntry refuse un fait appuyé sur une source non consultée et un sous-thème inconnu', () => {
  const e = JSON.parse(readFileSync(join(LIBRARY_DIR, 'rsa-profiteurs.json'), 'utf8'));
  e.faits[0].source = 1;
  e.sous_theme = 'Licornes';
  const errs = validateEntry(e);
  assert.ok(errs.some((m) => m.includes('réellement consultée')));
  assert.ok(errs.some((m) => m.includes('sous-thème inconnu')));
});

test('fraîcheur : une fiche dont la date de révision est passée est signalée', () => {
  const lib = loadLibrary(LIBRARY_DIR, silent);
  const today = '2026-10-29';
  const stale = lib.filter((e) => freshness(e, { today }).statut === 'a_actualiser').map((e) => e.id);
  assert.deepEqual(stale, ['chomeurs-travailler']);
  const rsa = lib.find((e) => e.id === 'rsa-smic');
  assert.equal(freshness(rsa, { today: '2027-01-02' }).statut, 'a_actualiser');
  assert.equal(freshness({ ...rsa, a_actualiser_le: '2099-01-01' }, { today: '2028-06-01', staleDays: 365 }).statut, 'a_actualiser');
  assert.equal(summarize(rsa, { today }).fraicheur.statut, 'a_jour');
});

test('recherche et filtres par volet / sous-thème', () => {
  const lib = loadLibrary(LIBRARY_DIR, silent);
  assert.equal(searchLibrary(lib, 'délinquance')[0].id, 'delinquance-partout');
  assert.ok(searchLibrary(lib, '', 'social').every((e) => e.volet === 'social'));
  assert.ok(searchLibrary(lib, '', 'social', 'RSA').every((e) => e.sous_theme === 'RSA'));
  assert.equal(searchLibrary(lib, 'zzzzzz').length, 0);
});

test('validation des requêtes : bornes, listes fermées, sous-thème du bon volet', () => {
  assert.equal(validateAnalyseRequest({ affirmation: 'abc' }).ok, false);
  assert.equal(validateAnalyseRequest({ affirmation: 'x'.repeat(601) }).ok, false);
  const v = validateAnalyseRequest({ affirmation: '  Les chômeurs   ne veulent pas travailler ', volet: 'social', sous_theme: 'Nucléaire', mode: 'pirate', profil: '<script>', contexte: 'x', express: 'oui' });
  assert.equal(v.ok, true);
  assert.equal(v.value.claim, 'Les chômeurs ne veulent pas travailler');
  assert.equal(v.value.sousTheme, null);
  assert.equal(v.value.mode, 'gagner');
  assert.equal(v.value.profil, 'mystere');
  assert.equal(v.value.express, false);
  assert.equal(validateAnalyseRequest({ affirmation: 'Une affirmation', volet: 'inconnu' }).value.volet, 'autre');
});

test('le lien Tipeee est exactement celui demandé', () => {
  assert.equal(TIPEEE_URL, 'https://fr.tipeee.com/martyducanda/');
});
