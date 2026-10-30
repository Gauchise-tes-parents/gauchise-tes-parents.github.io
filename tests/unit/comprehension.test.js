// v8 — Compréhension argumentative : 180 phrases (cas obligatoires, multi-sujets, familières, fautes,
// insinuations, émotions, procédés, changements de sujet, hors sujet, lot de validation).
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary } from '../../server/library.js';
import { analyserPhrase, anSegments } from '../../public/js/analyse.js';
import { CA_ARGUMENTS, CA_CONCEPTS } from '../../public/js/cartographie.js';
import { kbMatch } from '../../public/js/kbsearch.js';
import { PHRASES } from '../comprehension/phrases.js';
import { evaluer } from '../comprehension/evaluer.js';

const lib = loadLibrary(undefined, { warn() {} });
const ids = new Set(lib.map((f) => f.id));

describe('compréhension argumentative (v8)', () => {
  test('au moins 150 phrases, toutes les fiches citées existent', () => {
    assert.ok(PHRASES.length >= 150, String(PHRASES.length));
    for (const it of PHRASES) for (const id of [...[].concat(it.f ?? []), ...(it.x || [])]) if (id) assert.ok(ids.has(id), `${it.t} : fiche inconnue ${id}`);
  });

  test('la cartographie ne pointe que vers des fiches existantes', () => {
    for (const a of CA_ARGUMENTS) {
      for (const id of [...a.fiches, ...(a.exclues || []), ...Object.keys(a.choisir || {})]) assert.ok(ids.has(id), `${a.id} → ${id}`);
      for (const c of [...a.tous, ...(a.aucun || [])]) assert.ok(CA_CONCEPTS[c], `${a.id} : concept ${c}`);
    }
  });

  for (const it of PHRASES) {
    test(`[${it.cat}] ${it.t}`, () => {
      const r = evaluer(it, analyserPhrase(it.t, { bibliotheque: lib }));
      assert.ok(r.ok, r.erreurs.join(' ; '));
    });
  }

  test('démonstration : « Plus il y a d’immigrés, moins il y a de travail pour les Français »', () => {
    const t = 'Plus il y a d’immigrés, moins il y a de travail pour les Français.';
    // v7 : correspondance par mots, sur la bibliothèque d'alors (sans les trois fiches emploi ajoutées en v8)
    const V8 = ['immigration-emploi', 'immigration-salaires', 'chomage-penurie-recrutement'];
    const avant = kbMatch(lib.filter((f) => f.type !== 'science' && !V8.includes(f.id)), t)[0];
    assert.equal(avant.fiche.id, 'immigres-aides', 'l’ancienne correspondance par mots choisissait la fiche sur les aides');
    // même avec la nouvelle fiche présente, l'ancien moteur garde la fiche « aides » parmi ses candidates
    assert.ok(kbMatch(lib.filter((f) => f.type !== 'science'), t).some((m) => m.fiche.id === 'immigres-aides'));
    const an = analyserPhrase(t, { bibliotheque: lib });
    assert.equal(an.principal.id, 'imm_emploi');
    assert.equal(an.principal.fiche.id, 'immigration-emploi');
    assert.deepEqual(an.causalites.map((c) => [c.cause, c.effet]), [['Immigration', 'Emploi et marché du travail']]);
    for (const id of ['immigres-aides', 'rsa-smic']) {
      const e = an.ecartees.find((x) => x.id === id);
      assert.ok(e, `${id} doit figurer parmi les fiches écartées`);
      assert.match(e.raison, /pas de/);
    }
  });

  test('phrase à plusieurs sujets : réponses distinctes, chiffres non mélangés', () => {
    const an = analyserPhrase('Les immigrés prennent le travail des Français et en plus ils viennent toucher le RSA.', { bibliotheque: lib });
    assert.deepEqual(an.arguments.map((a) => a.fiche?.id), ['immigration-emploi', 'immigres-aides']);
    assert.deepEqual(anSegments(an.texte).length, 2);
    assert.notEqual(an.arguments[0].segment, an.arguments[1].segment, 'chaque argument est relié à sa propre proposition');
  });

  test('lacune reconnue plutôt qu’une fiche voisine', () => {
    for (const t of ['On ne peut plus se loger à cause de l’immigration.', 'On ne peut plus rien dire sur l’islam.', 'La France était mieux avant.']) {
      const an = analyserPhrase(t, { bibliotheque: lib });
      assert.equal(an.lacune, true, t);
      assert.equal(an.arguments.filter((a) => a.fiche).length, 0, t);
    }
  });

  test('formules marquantes : jamais de chiffre, différentes selon le mode', () => {
    for (const it of PHRASES.slice(0, 40)) {
      const g = analyserPhrase(it.t, { bibliotheque: lib, mode: 'gagner' });
      const c = analyserPhrase(it.t, { bibliotheque: lib, mode: 'convaincre' });
      assert.doesNotMatch(g.phrase + c.phrase, /\d/, it.t);
      if (g.principal) assert.notEqual(g.phrase, c.phrase, it.t);
    }
  });

  test('émotions et procédés : signalés comme possibles, avec question et élément à vérifier', () => {
    const an = analyserPhrase('Mon voisin est arabe et il touche toutes les aides.', { bibliotheque: lib });
    assert.ok(an.procedes.some((p) => p.id === 'anecdote'));
    assert.ok(an.procedes.some((p) => p.id === 'amalgame'), 'origine supposée ≠ nationalité');
    for (const p of an.procedes) { assert.ok(p.question); assert.ok(p.verifier); }
    assert.ok(an.aVerifier.length);
  });
});
