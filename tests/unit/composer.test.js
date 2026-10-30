// Mode autonome : questionnaire, consignes justifiées, compositeur (sans invention), adaptation progressive.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary, LIBRARY_DIR } from '../../server/library.js';
import { extractNumbers } from '../../server/engine/util.js';
import { nettoyerProfil, strategieProfil, profilSimple, resumeProfil, REGLES } from '../../public/js/profile.js';
import { composer, suite, versionSolide } from '../../public/js/composer.js';
import { kbDataAge } from '../../public/js/kbsearch.js';
import { validateBase } from '../../public/js/kbstore.js';
import { buildKb } from '../../server/kbexport.js';
import { strategyUserPrompt } from '../../server/engine/strategy.js';
import { validateOptions } from '../../server/engine/options.js';
import { INTERLOCUTEUR, RETOURS } from '../../public/js/taxonomy.js';
import { silent, DOSSIER_JSON } from '../helpers.js';

const lib = loadLibrary(LIBRARY_DIR, silent);
const byId = (id) => lib.find((e) => e.id === id);
const sciences = new Set(lib.filter((e) => e.type === 'science').map((e) => e.id));

describe('questionnaire et consignes', () => {
  test('dix dimensions (dont le niveau de connaissance), option « je ne connais pas », valeurs hors liste ignorées', () => {
    assert.equal(INTERLOCUTEUR.length, 10);
    assert.ok(INTERLOCUTEUR.some((d) => d.id === 'connaissance'));
    assert.deepEqual(nettoyerProfil({}), { inconnu: true });
    const p = nettoyerProfil({ debat: 'competitif', valeurs: ['securite', 'merite', 'ordre', 'liberte'], faits: 'inventé', religion: 'x', inconnu: false });
    assert.deepEqual(p, { inconnu: false, debat: 'competitif', valeurs: ['securite', 'merite', 'ordre'] });
    assert.equal(nettoyerProfil({ inconnu: true, debat: 'competitif' }).debat, undefined);
  });

  test('chaque consigne renvoie à une fiche scientifique existante', () => {
    for (const r of REGLES) assert.ok(sciences.has(r.fiche), `${r.id} → ${r.fiche}`);
  });

  test('profils contrastés → consignes différentes', () => {
    const ids = (p) => strategieProfil(p).regles.map((r) => r.id);
    assert.deepEqual(ids({ inconnu: true }), ['inconnu', 'ethique']);
    assert.ok(ids({ debat: 'competitif' }).includes('confrontation'));
    assert.ok(ids({ debat: 'provocateur' }).includes('provocation'));
    assert.ok(ids({ autorite: 'mefiance' }).includes('mefiance'));
    assert.ok(ids({ valeurs: ['securite'] }).includes('securite'));
    assert.ok(ids({ valeurs: ['justice_sociale'] }).includes('justice'));
    assert.ok(ids({ politique: 'partisan' }).includes('identite'));
    assert.ok(ids({ faits: 'chiffres' }).includes('chiffres'));
    assert.ok(ids({ faits: 'experience' }).includes('experience'));
    assert.ok(ids({ debat: 'susceptible' }).includes('susceptible'));
    assert.equal(profilSimple({ debat: 'provocateur' }), 'provocateur');
    assert.equal(profilSimple({}), 'mystere');
    assert.match(resumeProfil({ debat: 'calme', lien: 'parent' }), /calme · parent/);
  });
});

describe('compositeur hors ligne', () => {
  const sansTitres = (a) => JSON.stringify({ g: a.gagner.blocs, c: a.convaincre.blocs, v: a.version_solide }, (k, v) => (k === 'index' || k === 'titre' ? undefined : v)); // « index » = position interne ; « titre » contient le décompte « Les preuves (2) »

  test('deux stratégies toujours produites, version solide de l’argument adverse', () => {
    for (const f of lib.filter((e) => e.type !== 'science')) {
      const a = composer(f, { inconnu: true }, { bibliotheque: lib });
      assert.ok(a.gagner.replique && a.gagner.preuves.length >= 1, f.id);
      assert.ok(a.convaincre.faits_progressifs.length >= 1 && a.convaincre.empathie, f.id);
      assert.ok(a.gagner.blocs.length >= 3 && a.convaincre.blocs.length >= 3, f.id);
      assert.ok(a.version_solide.length > 30, f.id);
      assert.ok(a.approches.length >= 2 && a.approches.length <= 3, f.id);
    }
    assert.match(versionSolide(byId('lfi-antisemite')), /forme la plus solide/);
  });

  test('aucun chiffre inventé : tous les nombres de l’argumentaire figurent dans la fiche', () => {
    for (const f of lib) {
      for (const p of [{ inconnu: true }, { debat: 'competitif', autorite: 'mefiance', cadre: 'plusieurs' }, { faits: 'chiffres', valeurs: ['securite', 'merite'], lien: 'parent', objectif: 'corriger' }]) {
        const ficheNums = extractNumbers(JSON.stringify(f));
        const extra = [...extractNumbers(sansTitres(composer(f, p, { bibliotheque: lib })))].filter((n) => !ficheNums.has(n));
        assert.deepEqual(extra, [], `${f.id} : ${extra.join(', ')}`);
      }
    }
  });

  test('la confrontation donne une seule preuve et renvoie la charge de la preuve ; la méfiance montre la méthode', () => {
    const f = byId('impots-assistanat');
    const a = composer(f, { debat: 'competitif' }, { bibliotheque: lib });
    assert.equal(a.gagner.preuves.length, 1);
    assert.match(a.gagner.blocs.find((b) => b.type === 'riposte').texte, /source/);
    const m = composer(f, { autorite: 'mefiance' }, { bibliotheque: lib });
    assert.ok(m.gagner.preuves.every((p) => /Période/.test(p.methode)));
    assert.ok(m.sources.length >= 2);
    const b = composer(f, { debat: 'susceptible', lien: 'parent' }, { bibliotheque: lib });
    const types = b.convaincre.blocs.map((x) => x.type);
    // v9 : même en mode empathique, la réponse et les faits viennent d'abord ; les questions servent à les introduire
    assert.ok(types.indexOf('replique') === 0 && types.indexOf('preuves') < types.indexOf('questions'), 'la réponse et les faits avant la méthode');
    assert.match(b.convaincre.blocs.find((x) => x.type === 'conclusion' && x.titre === 'Pour conclure').texte, /rien entre nous/);
    const c = composer(f, { debat: 'provocateur' }, { bibliotheque: lib });
    assert.ok(c.plans.gagner.recentrage);
    assert.match(c.gagner.blocs.find((x) => x.type === 'riposte').texte, /ceux qui nous écoutent/);
  });

  test('ancienneté des données toujours signalée', () => {
    assert.equal(kbDataAge(byId('front-populaire-1936'), { today: '2026-10-29' }).niveau, 'stable');
    assert.equal(kbDataAge(byId('impots-assistanat'), { today: '2026-10-29' }).niveau, 'datee');
    assert.equal(kbDataAge(byId('chomeurs-travailler'), { today: '2026-10-29' }).niveau, 'ancienne');
  });

  test('adaptation progressive : une proposition par retour, fondée sur les seules observations', () => {
    const f = byId('impots-assistanat');
    const session = { utilises: [], objectionsVues: [], questionsPosees: [], retours: [] };
    for (const [k] of RETOURS) {
      const x = suite(f, { inconnu: true }, k, session, { bibliotheque: lib });
      assert.ok(x.titre && x.texte && x.conseil, k);
      assert.ok(sciences.has(x.fiche_science), k);
      assert.match(x.note, /approximative/);
    }
    const e1 = suite(f, {}, 'ecoute', session);
    session.utilises.push(e1.utilise);
    const e2 = suite(f, {}, 'ecoute', session);
    assert.notEqual(e1.utilise, e2.utilise, 'un nouvel élément à chaque fois');
    assert.ok(suite(f, {}, 'preuves', session).preuve.source.url.startsWith('https://'));
  });
});

describe('mode connecté : profil transmis au moteur', () => {
  test('les consignes du profil sont ajoutées à la consigne de stratégie', () => {
    const o = validateOptions({ mode: 'gagner', interlocuteur: { debat: 'competitif', valeurs: ['securite'], piege: '<script>' } });
    assert.deepEqual(o.interlocuteur, { inconnu: false, debat: 'competitif', valeurs: ['securite'] });
    const dossier = { ...DOSSIER_JSON, faits: [], contradictions: [], jugements_de_valeur: [], limites: [], sources: [] };
    const txt = strategyUserPrompt({ mode: 'gagner', dossier, claim: 'x', profil: 'convaincu', contexte: 'repas', volet: 'economie', interlocuteur: o.interlocuteur });
    assert.match(txt, /une idée centrale et une preuve vérifiable/);
    assert.match(txt, /forme la plus solide/);
    assert.doesNotMatch(strategyUserPrompt({ mode: 'gagner', dossier, claim: 'x', profil: 'mystere', contexte: 'repas', volet: 'economie' }), /Consignes issues/);
  });
});

test('contrôle d’intégrité de la base téléchargée', () => {
  const base = JSON.parse(buildKb(lib).json);
  assert.deepEqual(validateBase(base), []);
  assert.ok(validateBase({ fiches: [] }).length);
  const bad = structuredClone(base);
  bad.fiches[0].faits[0].source = 99;
  assert.ok(validateBase(bad).some((m) => m.includes('fait sans source')));
});
