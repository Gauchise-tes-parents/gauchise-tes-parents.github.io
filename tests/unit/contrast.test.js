// Contrôle automatique des contrastes (WCAG 2.1) sur les couples couleur de texte / fond utilisés.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';

const css = readFileSync(new URL('../../public/css/styles.css', import.meta.url), 'utf8');
const token = (name) => {
  const m = css.match(new RegExp(`--${name}:\\s*(#[0-9A-Fa-f]{6})`));
  assert.ok(m, `jeton --${name} introuvable`);
  return m[1];
};
const lum = (hex) => {
  const [r, g, b] = [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16) / 255)
    .map((c) => (c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4));
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
};
const ratio = (a, b) => {
  const [x, y] = [lum(a), lum(b)].sort((p, q) => q - p);
  return (x + 0.05) / (y + 0.05);
};

const PAIRS = [
  // [texte, fond, minimum]
  ['ink', 'cream', 4.5], ['ink-2', 'cream', 4.5], ['ink', 'lemon', 4.5], ['night', 'lemon', 4.5],
  ['cream', 'night', 4.5], ['lemon', 'night', 4.5], ['ink-2', 'paper', 4.5], ['night', 'cream', 4.5],
  ['teal', 'paper', 4.5], ['raspberry', 'paper', 4.5], ['orange-ink', 'cream', 4.5], ['ink', 'orange', 4.5],
  ['ink', 'sky', 4.5], ['ink', 'sand', 4.5], ['ink-2', 'sand', 4.5], ['lemon', 'night-2', 4.5], ['cream', 'night-2', 4.5],
];

for (const [fg, bg, min] of PAIRS) {
  test(`contraste --${fg} sur --${bg} ≥ ${min}`, () => {
    const r = ratio(token(fg), token(bg));
    assert.ok(r >= min, `ratio ${r.toFixed(2)} insuffisant`);
  });
}
