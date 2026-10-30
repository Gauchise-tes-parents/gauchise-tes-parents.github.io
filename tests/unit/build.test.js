// Publication statique : contenu, chemins relatifs (sous-dossier GitHub Pages), absence de secret.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { mkdtempSync, readFileSync, existsSync, readdirSync, statSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { createHash } from 'node:crypto';

test('build:static produit un site autonome, sans clé, avec base vérifiable', () => {
  const out = join(mkdtempSync(join(tmpdir(), 'gtp-site-')), 'site');
  const root = new URL('../..', import.meta.url).pathname;
  execFileSync(process.execPath, ['scripts/build-static.js'], { cwd: root, env: { ...process.env, STATIC_OUT: out, ANTHROPIC_API_KEY: 'sk-ant-secret-de-test', GTP_API_BASE: '' }, stdio: 'pipe' });
  for (const f of ['index.html', 'sw.js', 'config.js', 'asset-manifest.json', 'kb/base.json', 'kb/manifest.json', 'kb/veille.json', '.nojekyll', '404.html']) assert.ok(existsSync(join(out, f)), f);
  const html = readFileSync(join(out, 'index.html'), 'utf8');
  assert.doesNotMatch(html, /(href|src)="\//, 'chemins relatifs uniquement');
  assert.match(readFileSync(join(out, 'config.js'), 'utf8'), /apiBase: null/);
  const manifest = JSON.parse(readFileSync(join(out, 'kb/manifest.json'), 'utf8'));
  assert.equal(createHash('sha256').update(readFileSync(join(out, 'kb/base.json'))).digest('hex'), manifest.sha256);
  const assets = JSON.parse(readFileSync(join(out, 'asset-manifest.json'), 'utf8'));
  for (const f of assets.fichiers.filter((x) => x !== './')) assert.ok(existsSync(join(out, f)), `fichier mis en cache manquant : ${f}`);
  // aucune trace de la clé dans les fichiers publiés
  const walk = (d) => readdirSync(d).flatMap((n) => (statSync(join(d, n)).isDirectory() ? walk(join(d, n)) : [join(d, n)]));
  for (const f of walk(out)) assert.ok(!readFileSync(f).includes('sk-ant-secret-de-test'), f);
  assert.throws(() => execFileSync(process.execPath, ['scripts/build-static.js'], { cwd: root, env: { ...process.env, STATIC_OUT: out, GTP_API_BASE: 'javascript:alert(1)' }, stdio: 'pipe' }));
});

test('veille en ligne de commande sans clé : refus explicite, rien de simulé', () => {
  const root = new URL('../..', import.meta.url).pathname;
  let code = 0;
  let stderr = '';
  try { execFileSync(process.execPath, ['scripts/veille.js'], { cwd: root, env: { ...process.env, ANTHROPIC_API_KEY: '', FORCE_DEMO: '1' }, stdio: 'pipe' }); } catch (e) { code = e.status; stderr = String(e.stderr); }
  assert.equal(code, 2);
  assert.match(stderr, /Rien n’est simulé/);
});
