// Compatibilité navigateurs : l'application doit s'ouvrir sur Firefox, Safari (y compris iPhone/iPad un peu anciens)
// et les navigateurs basés sur Chromium. Une seule expression régulière non comprise par un moteur, compilée au
// chargement d'un module, suffit à laisser la page blanche : on interdit donc les constructions récentes.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const DIR = new URL('../../public/js/', import.meta.url).pathname;
const fichiers = [...readdirSync(DIR).filter((f) => f.endsWith('.js')).map((f) => join(DIR, f)), new URL('../../public/sw.js', import.meta.url).pathname];

// [motif interdit, raison]
const INTERDITS = [
  [/\(\?<[=!]/, 'assertion arrière (?<= / (?<! dans une expression régulière : Safari < 16.4'],
  [/\bstructuredClone\(/, 'structuredClone : Safari < 15.4'],
  [/\.at\(-?\d/, 'Array.prototype.at : Safari < 15.4'],
  [/\bObject\.hasOwn\(/, 'Object.hasOwn : Safari < 15.4'],
  [/\.findLast(Index)?\(/, 'findLast : Safari < 15.4, Firefox < 104'],
  [/\brequestIdleCallback\b/, 'requestIdleCallback : absent de Safari'],
  [/\brandomUUID\(/, 'crypto.randomUUID : Safari < 15.4'],
  [/AbortSignal\.(timeout|any)\(/, 'AbortSignal.timeout/any : Safari < 16'],
  [/\.toSorted\(|\.toReversed\(|\.toSpliced\(/, 'méthodes « to… » des tableaux : Safari < 16, Firefox < 115'],
  [/\bObject\.groupBy\(|\bPromise\.withResolvers\(/, 'Object.groupBy / Promise.withResolvers : trop récents'],
];

test('aucune construction JavaScript trop récente pour Safari 15 / Firefox 100', () => {
  const pb = [];
  for (const f of fichiers) {
    const src = readFileSync(f, 'utf8');
    src.split('\n').forEach((ligne, i) => {
      if (/^\s*\/\//.test(ligne)) return; // commentaires
      for (const [re, raison] of INTERDITS) if (re.test(ligne)) pb.push(`${f.split('/public/')[1]}:${i + 1} — ${raison}`);
    });
  }
  assert.deepEqual(pb, []);
});

test('tous les motifs de la cartographie et de la ligne éditoriale se compilent sans fonctionnalité récente', async () => {
  const carto = await import('../../public/js/cartographie.js');
  const le = await import('../../public/js/ligne-editoriale.js');
  const motifs = [];
  for (const c of Object.values(carto.CA_CONCEPTS)) motifs.push(...c.motifs);
  for (const c of [...Object.values(carto.CA_EMOTIONS || {}), ...Object.values(carto.CA_PROCEDES || {})]) motifs.push(...(c.motifs || []));
  for (const a of carto.CA_ARGUMENTS) motifs.push(...(a.signaux || []), ...Object.values(a.choisir || {}));
  for (const c of Object.values(le.LE_CLASSES)) motifs.push(...c.motifs);
  for (const m of motifs) {
    assert.doesNotMatch(m, /\(\?<[=!]|\(\?<[A-Za-z]|\\[pP]\{/, `motif trop récent pour certains navigateurs : ${m}`);
    assert.doesNotThrow(() => new RegExp(m), m);
  }
});

test('la classification des sources reste correcte sans assertion arrière (« Public Sénat » n’est pas le Sénat)', async () => {
  const { classerSource } = await import('../../public/js/ligne-editoriale.js');
  assert.equal(classerSource({ organisme: 'Public Sénat', url: 'https://www.publicsenat.fr/x' }), 'presse_reference');
  assert.equal(classerSource({ organisme: 'Sénat, commission des lois', url: 'https://www.senat.fr/x' }), 'institution');
});
