import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { SOUTIEN, soutienPourcentage, euros } from '../../public/js/soutien.js';

test('jauge de soutien : chiffres plausibles et datés, objectif de 1 000 €', () => {
  assert.equal(SOUTIEN.objectif, 1000);
  assert.ok(Number.isFinite(SOUTIEN.montant) && SOUTIEN.montant >= 0);
  assert.ok(Number.isInteger(SOUTIEN.tipeurs) && SOUTIEN.tipeurs >= 0);
  assert.match(SOUTIEN.maj, /^\d{4}-\d{2}-\d{2}$/);
});

test('jauge de soutien : pourcentage borné et format des montants', () => {
  assert.equal(soutienPourcentage({ montant: 45, objectif: 1000 }), 4.5);
  assert.equal(soutienPourcentage({ montant: 0, objectif: 1000 }), 0);
  assert.equal(soutienPourcentage({ montant: 5, objectif: 1000 }), 2);
  assert.equal(soutienPourcentage({ montant: 2500, objectif: 1000 }), 100);
  assert.equal(euros(1000), '1 000 €');
  assert.equal(euros(45), '45 €');
});

test('jauge de soutien : aucune requête vers Tipeee, simple lien', () => {
  const src = readFileSync(new URL('../../public/js/soutien.js', import.meta.url), 'utf8');
  assert.doesNotMatch(src, /fetch\(|XMLHttpRequest|import\(/);
});
