// v13 — Audit automatique de confidentialité et de sécurité (les 10 vérifications demandées, rejouées à chaque test).
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync, statSync, mkdtempSync, rmSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import { tmpdir } from 'node:os';
import { execFileSync } from 'node:child_process';
import { recordProposal } from '../../server/engine/knowledge.js';
import { createAnthropicProvider } from '../../server/engine/providers/anthropic.js';
import { testConfig, startServer } from '../helpers.js';

const ROOT = new URL('../..', import.meta.url).pathname;
function fichiers(dir, ext = /\.(js|mjs|html|css|json|webmanifest|toml|yml)$/) {
  const out = [];
  for (const n of readdirSync(dir)) {
    if (['node_modules', '.git', 'dist', '.wrangler'].includes(n)) continue;
    const p = join(dir, n);
    if (statSync(p).isDirectory()) out.push(...fichiers(p, ext)); else if (ext.test(n)) out.push(p);
  }
  return out;
}
const lire = (p) => readFileSync(p, 'utf8');
const NAVIGATEUR = fichiers(join(ROOT, 'public')).filter((p) => !p.includes('/kb/'));
const SERVEUR = [...fichiers(join(ROOT, 'server')), ...fichiers(join(ROOT, 'worker', 'src')).filter((p) => !p.endsWith('kb.json'))];

describe('audit de confidentialité (v13)', () => {
  test('1-3. aucune géolocalisation : ni API du navigateur, ni GPS, ni localisation par adresse IP', () => {
    const interdits = /navigator\.geolocation|getCurrentPosition|watchPosition|ipapi|ipinfo|geoip|ip-api|geolocation-db|cf-ipcountry|request\.cf\.(city|country|latitude)|user_location/i;
    for (const p of [...NAVIGATEUR, ...SERVEUR]) {
      const l = lire(p).split('\n').filter((x) => interdits.test(x) && !/Permissions-Policy|geolocation=\(\)/.test(x));
      assert.deepEqual(l, [], p);
    }
  });

  test('4. aucun compte ni identifiant : pas de champ e-mail, téléphone, mot de passe, date de naissance', () => {
    // seule exception : le jeton d'administration de la veille (réservé à l'administrateur du serveur, pas un compte)
    for (const p of NAVIGATEUR) assert.ok(!/type="(email|tel)"|type="password"(?! id="veille-token")|autocomplete="(email|tel|bday|name)"/.test(lire(p)), p);
  });

  test('5. aucun traceur ni publicité ; aucun script, police ou image d’un site tiers', () => {
    const traceurs = /google-analytics|googletagmanager|gtag\(|fbq\(|connect\.facebook|analytics\.tiktok|ttq\.load|google-analytics|matomo|plausible|hotjar|mixpanel|segment\.io|sentry|doubleclick|adsbygoogle/i;
    for (const p of NAVIGATEUR) assert.ok(!traceurs.test(lire(p)), p);
    const html = lire(join(ROOT, 'public', 'index.html'));
    assert.ok(!/<(script|link|img)[^>]+(src|href)="https?:/i.test(html), 'ressource externe dans index.html');
    assert.ok(!/@import\s+url\(\s*['"]?https?:|url\(\s*['"]?https?:/.test(lire(join(ROOT, 'public', 'css', 'styles.css'))));
    assert.ok(!/sendBeacon|navigator\.(userAgentData|deviceMemory|hardwareConcurrency)|canvas\.toDataURL|getImageData/.test(NAVIGATEUR.map(lire).join('\n')), 'pas d’empreinte du navigateur');
  });

  test('CSP présente dans la page statique (GitHub Pages ne permet pas d’en-têtes) : aucun script en ligne ni extérieur', () => {
    const m = lire(join(ROOT, 'public', 'index.html')).match(/http-equiv="Content-Security-Policy" content="([^"]+)"/);
    assert.ok(m, 'balise CSP');
    assert.match(m[1], /script-src 'self'(;|$)/);
    assert.ok(!/unsafe-inline|unsafe-eval|\*/.test(m[1]));
  });

  test('6. aucune clé d’API dans le code du navigateur, la configuration publique ou les fichiers versionnés', () => {
    const cles = /AIza[0-9A-Za-z_-]{30,}|AQ\.[0-9A-Za-z_-]{30,}|sk-ant-api[0-9A-Za-z_-]{20,}|ghp_[0-9A-Za-z]{30,}|github_pat_[0-9A-Za-z_]{30,}/;
    for (const p of [...NAVIGATEUR, ...fichiers(join(ROOT, 'worker')), ...fichiers(join(ROOT, 'scripts')), ...fichiers(join(ROOT, '.github'))]) {
      if (p.endsWith('kb.json')) continue;
      assert.ok(!cles.test(lire(p)), p);
    }
    assert.ok(!/GEMINI_API_KEY\s*=\s*"[^"]/.test(lire(join(ROOT, 'worker', 'wrangler.toml'))), 'clé dans wrangler.toml');
    const gi = lire(join(ROOT, '.gitignore'));
    for (const x of ['.env', 'worker/.dev.vars', 'data/feedback/']) assert.ok(gi.includes(x), `.gitignore : ${x}`);
    assert.match(lire(join(ROOT, 'public', 'config.js')), /iaBase: null/);
  });

  test('7. aucune conversation ni question conservée automatiquement dans le navigateur', () => {
    const app = lire(join(ROOT, 'public', 'js', 'app.js'));
    assert.ok(!/sessionStorage\.setItem\(CONV_KEY|gtp-recents'\s*,|noterConsultation/.test(app));
    assert.match(app, /function sauverConv\(\) \{ \/\* volontairement vide/);
    assert.match(app, /PARCOURS_CHAMPS = \['step', 'mode', 'volet', 'sousTheme', 'contexte'\]/);
    const store = lire(join(ROOT, 'public', 'js', 'store.js'));
    assert.ok(!/noterConsultation|historique:\s*\[\]/.test(store));
  });

  test('7b. le serveur n’écrit jamais la question : propositions de mise à jour sans le texte soumis', async () => {
    const dir = mkdtempSync(join(tmpdir(), 'gtp-'));
    try {
      const f = join(dir, 'p.jsonl');
      await recordProposal(f, { fiche_id: 'x', verdict_fiche: 'a', verdict_web: 'b', nouvelles_sources: [], chiffres_fiche_absents: [], signaux: [] }, 'Question personnelle de Gérard');
      const t = lire(f);
      assert.ok(!t.includes('Gérard') && !t.includes('affirmation_soumise'), t);
    } finally { rmSync(dir, { recursive: true, force: true }); }
  });

  test('8. les journaux du serveur ne contiennent ni la question ni l’adresse IP, même en cas d’erreur', async () => {
    const lignes = [];
    const logger = { info: (...a) => lignes.push(a.join(' ')), warn: (...a) => lignes.push(a.join(' ')), error: (...a) => lignes.push(a.join(' ')) };
    const boom = async () => { throw Object.assign(new Error('Erreur qui reprend la question : Gérard Dupont'), { name: 'Error' }); };
    const s = await startServer(testConfig({ liveMode: true, apiKey: 'sk-test' }), { logger, fetchImpl: boom });
    try {
      await s.post('/api/analyse', { affirmation: 'Gérard Dupont pense que les impôts sont trop élevés', volet: 'economie', mode: 'gagner', profil: 'mystere', contexte: 'repas' });
      await s.post('/api/conversation', { message: 'Gérard Dupont dit ceci', fiche_id: 'impots-assistanat', mode: 'gagner' });
    } finally { await s.close(); }
    assert.ok(lignes.length > 0);
    for (const l of lignes) assert.ok(!/Gérard|Dupont|127\.0\.0\.1/.test(l), l);
  });

  test('9. aucune donnée personnelle ni localisation ajoutée aux recherches web (fournisseur du mode connecté)', async () => {
    let corps = null;
    const fetchImpl = async (url, init) => { corps = init.body; return { ok: true, status: 200, json: async () => ({ content: [{ type: 'text', text: 'ok' }], stop_reason: 'end_turn', usage: { input_tokens: 1, output_tokens: 1 } }) }; };
    const p = createAnthropicProvider({ ...testConfig({ liveMode: true, apiKey: 'sk-test' }) }, { fetchImpl });
    await p.complete({ model: 'm', system: 'consigne', user: 'question', maxTokens: 10, tools: { maxSearches: 1, maxFetches: 1 } }).catch(() => {});
    assert.ok(corps, 'requête construite');
    assert.ok(!/user_location|metadata|user_id|"country"|timezone/i.test(corps), corps.slice(0, 400));
  });

  test('10. les services externes sont identifiés et documentés', () => {
    const audit = lire(join(ROOT, 'AUDIT-CONFIDENTIALITE.md'));
    for (const x of ['GitHub Pages', 'Anthropic', 'Google', 'Gemini', 'Cloudflare', 'Tipeee']) assert.ok(audit.includes(x), x);
    const app = lire(join(ROOT, 'public', 'js', 'app.js'));
    assert.match(app, /Confidentialité et sécurité/);
    assert.ok(!/aucune donnée ne quitte/i.test(app));
  });

  test('dépôt : aucun secret dans l’historique git publié (si disponible)', () => {
    const depot = join(ROOT, '..', 'depot');
    if (!existsSync(join(depot, '.git'))) return;
    const log = execFileSync('git', ['-C', depot, 'log', '--all', '-p'], { maxBuffer: 512 * 1024 * 1024 }).toString();
    assert.ok(!/AIza[0-9A-Za-z_-]{30,}|AQ\.[0-9A-Za-z_-]{30,}|sk-ant-api[0-9A-Za-z_-]{20,}|ghp_[0-9A-Za-z]{30,}/.test(log));
  });
});
