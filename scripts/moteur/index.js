// Moteur interne de création de fiches (SANS IA, sans Claude) — lancé chaque jour par GitHub Actions
// (.github/workflows/moteur.yml) ou à la main :
//   node scripts/moteur/index.js               passage complet (programme, chiffres, questions, fiches)
//   node scripts/moteur/index.js --hors-ligne  sans réseau : réutilise le programme et les chiffres déjà relevés
//   node scripts/moteur/index.js --repli       retire de la bibliothèque les fiches du dernier passage (tests échoués)
// Guide : docs/MOTEUR.md
import { readFileSync, writeFileSync, existsSync, mkdirSync, readdirSync, renameSync, appendFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { loadLibrary, LIBRARY_DIR } from '../../server/library.js';
import { resoudrePhrase } from '../../public/js/analyse.js';
import { releverAec } from './aec.js';
import { releverChiffres } from './chiffres.js';
import { ajouter, questionsManuelles, questionsCollecteur } from './file.js';
import { assemblerFiche, controler } from './fiches.js';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..', '..');
const D = process.env.GTP_MOTEUR_DIR || join(ROOT, 'data', 'moteur');
const LIB = process.env.GTP_LIBRARY_DIR || LIBRARY_DIR;
const BROUILLONS = process.env.GTP_BROUILLONS_DIR || join(ROOT, 'data', 'brouillons');
const args = process.argv.slice(2);
const jour = new Date().toISOString().slice(0, 10);
const lireJson = (f, defaut) => { try { return JSON.parse(readFileSync(join(D, f), 'utf8')); } catch { return defaut; } };
const ecrireJson = (dir, f, obj) => { mkdirSync(dir, { recursive: true }); writeFileSync(join(dir, f), `${JSON.stringify(obj, null, 2)}\n`); };
const sortie = (k, v) => { if (process.env.GITHUB_OUTPUT) appendFileSync(process.env.GITHUB_OUTPUT, `${k}=${v}\n`); };
mkdirSync(D, { recursive: true });

// ── Repli : les tests ont échoué après l'ajout des fiches → elles redeviennent des brouillons ──
if (args.includes('--repli')) {
  const dernier = lireJson('dernier-passage.json', { fiches: [] });
  const file = lireJson('file.json', { questions: {} });
  mkdirSync(BROUILLONS, { recursive: true });
  for (const id of dernier.fiches) {
    const src = join(LIB, `${id}.json`);
    if (!existsSync(src)) continue;
    renameSync(src, join(BROUILLONS, `${id}.json`));
    for (const q of Object.values(file.questions)) if (q.fiche === id) { q.statut = 'brouillon'; q.note = 'tests de l’application échoués après ajout : à reprendre à la main'; }
  }
  ecrireJson(D, 'file.json', file);
  appendFileSync(join(D, 'rapport.md'), `\n**Repli :** les tests de l’application ont échoué après l’ajout des fiches ; ${dernier.fiches.length} fiche(s) déplacée(s) dans data/brouillons/.\n`);
  sortie('fiches', 0);
  console.log(`Repli : ${dernier.fiches.length} fiche(s) remise(s) en brouillon.`);
  process.exit(0);
}

const config = { max_fiches_par_passage: 10, aec_jours: 7, ...lireJson('config.json', {}) };
const horsLigne = args.includes('--hors-ligne');
const rapport = [`# Moteur interne — passage du ${jour}`, ''];
const alertes = [];
const journal = { warn: (m) => { alertes.push(m); console.warn(m); } };

// 1. Programme L'Avenir en commun (relevé une fois par semaine)
let corpus = lireJson('aec.json', null);
const ageJours = corpus ? (Date.parse(jour) - Date.parse(corpus.releve_le)) / 864e5 : Infinity;
if (!horsLigne && ageJours >= config.aec_jours) {
  try { corpus = await releverAec({ journal }); ecrireJson(D, 'aec.json', corpus); rapport.push(`- Programme relevé : ${corpus.nb_chapitres} chapitres, ${corpus.nb_mesures} mesures.`); }
  catch (e) { alertes.push(`programme non relevé : ${e.message}`); rapport.push(`- Programme : relevé impossible (${e.message}) ; ${corpus ? `version du ${corpus.releve_le} conservée` : 'aucune version disponible'}.`); }
} else rapport.push(corpus ? `- Programme : version du ${corpus.releve_le} (${corpus.nb_mesures} mesures).` : '- Programme : pas encore relevé.');

// 2. Chiffres officiels
let chiffres = lireJson('chiffres.json', { indicateurs: {} });
if (!horsLigne) {
  try {
    const r = await releverChiffres({ anciens: chiffres, journal });
    chiffres = r.chiffres; ecrireJson(D, 'chiffres.json', chiffres);
    rapport.push(`- Chiffres officiels : ${Object.keys(chiffres.indicateurs).length} indicateurs disponibles.`);
    if (r.changements.length) rapport.push('', '**Chiffres qui ont changé** (à reporter dans les fiches qui les citent) :', ...r.changements.map((c) => `- ${c}`), '');
  } catch (e) { alertes.push(`chiffres non relevés : ${e.message}`); }
}

// 3. Questions sans réponse
const file = lireJson('file.json', { questions: {} });
let recues = 0;
if (!horsLigne) {
  try { const c = await questionsCollecteur({ base: process.env.GTP_QUESTIONS_BASE, jeton: process.env.GTP_QUESTIONS_TOKEN }); recues = ajouter(file, c.questions, 'site', jour); if (c.statut !== 'lu') rapport.push(`- Collecteur du site : ${c.statut}.`); }
  catch (e) { alertes.push(e.message); }
}
const manuelles = ajouter(file, questionsManuelles(join(D, 'questions.txt')), 'manuel', jour);
rapport.push(`- Questions nouvelles : ${recues} venues du site, ${manuelles} ajoutées à la main.`);

// 4. Fiches
const bibliotheque = loadLibrary(LIB, { warn() {}, info() {}, error() {} }).filter((f) => f.type !== 'science');
const journalTxt = (() => { try { return readFileSync(join(ROOT, 'rapports', 'journal-quotidien.md'), 'utf8'); } catch { return ''; } })();
const scenarios = (() => { try { return readFileSync(join(ROOT, 'tests', 'personnalisation', 'scenarios.js'), 'utf8'); } catch { return ''; } })();
const phrasesControle = [...new Set([
  ...bibliotheque.map((f) => f.affirmation),
  ...[...journalTxt.matchAll(/^\d+\. (.+)$/gm)].map((m) => m[1].trim()),
  ...[...journalTxt.matchAll(/^- « ([^»]{8,140}) »/gm)].map((m) => m[1].trim()),
  ...[...scenarios.matchAll(/\['([^']{6,140})', '[a-z0-9-]+'\]/g)].map((m) => m[1]),
  ...Object.values(file.questions).filter((q) => q.statut !== 'en_attente').map((q) => q.texte),
])];
const avant = new Map(phrasesControle.map((p) => [p, resoudrePhrase(p, bibliotheque).fiche?.id || null]));
const creees = [];
const brouillons = [];
const enAttente = Object.values(file.questions).filter((q) => q.statut === 'en_attente').sort((a, b) => b.occurrences - a.occurrences || a.premiere.localeCompare(b.premiere));
for (const q of enAttente.slice(0, config.max_fiches_par_passage)) {
  const deja = resoudrePhrase(q.texte, bibliotheque).fiche;
  if (deja) { q.statut = 'couverte'; q.fiche = deja.id; q.note = 'une fiche existante y répond (à vérifier si hors sujet)'; continue; }
  if (!corpus) { q.note = 'programme pas encore relevé'; continue; }
  const r = assemblerFiche(q.texte, { corpus, chiffres, occurrences: q.occurrences, jour });
  if (r.raison) { q.statut = 'a_ecrire'; q.note = r.raison; continue; }
  const pb = controler(r.fiche, { bibliotheque, phrasesControle, avant });
  if (pb.length) {
    ecrireJson(BROUILLONS, `${r.fiche.id}.json`, { ...r.fiche, problemes: pb });
    q.statut = 'brouillon'; q.fiche = r.fiche.id; q.note = pb.join(' ; ');
    brouillons.push({ id: r.fiche.id, question: q.texte, pb });
    continue;
  }
  ecrireJson(LIB, `${r.fiche.id}.json`, r.fiche);
  bibliotheque.push(r.fiche);
  avant.set(r.fiche.affirmation, r.fiche.id); phrasesControle.push(r.fiche.affirmation);
  q.statut = 'fiche'; q.fiche = r.fiche.id; delete q.note;
  creees.push({ id: r.fiche.id, question: q.texte, mesures: r.fiche.moteur.mesures, indicateurs: r.fiche.moteur.indicateurs });
}
ecrireJson(D, 'file.json', file);
ecrireJson(D, 'dernier-passage.json', { jour, fiches: creees.map((c) => c.id), brouillons: brouillons.map((b) => b.id) });

const restantes = Object.values(file.questions).filter((q) => ['a_ecrire', 'en_attente'].includes(q.statut));
rapport.push('', `## Fiches créées : ${creees.length}`, ...creees.map((c) => `- \`${c.id}\` — « ${c.question} » (${c.mesures} mesures du programme ; chiffres : ${c.indicateurs.join(', ')})`));
rapport.push('', `## Brouillons à reprendre : ${brouillons.length}`, ...brouillons.map((b) => `- \`${b.id}\` — « ${b.question} » : ${b.pb.join(' ; ')}`));
rapport.push('', `## Questions à écrire à la main (ou par Claude) : ${restantes.length}`, ...restantes.slice(0, 30).map((q) => `- « ${q.texte} »${q.occurrences > 1 ? ` (${q.occurrences} fois)` : ''}${q.note ? ` — ${q.note}` : ''}`));
if (alertes.length) rapport.push('', '## Alertes', ...alertes.map((a) => `- ${a}`));
rapport.push('', 'Valider = fusionner cette demande de fusion (pull request). Les fiches portent la mention « assemblée automatiquement » sur le site.');
writeFileSync(join(D, 'rapport.md'), `${rapport.join('\n')}\n`);
sortie('fiches', creees.length); sortie('brouillons', brouillons.length);
console.log(rapport.join('\n'));
