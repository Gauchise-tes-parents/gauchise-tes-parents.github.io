// Banc d'essai du moteur de personnalisation (mode autonome) : au moins 100 scénarios synthétiques.
// Vérifie la cohérence et la traçabilité ; ne mesure pas l'efficacité persuasive sur de vraies personnes.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary, LIBRARY_DIR } from '../../server/library.js';
import { composer, planifier, EFFETS, comparerApproches } from '../../public/js/composer.js';
import { INTERLOCUTEUR } from '../../public/js/taxonomy.js';
import { REGLES } from '../../public/js/profile.js';
import { toutExecuter, evaluer, empreinte, verite, attentes } from '../personnalisation/scenarios.js';
import { silent } from '../helpers.js';

const lib = loadLibrary(LIBRARY_DIR, silent);
const byId = (id) => lib.find((e) => e.id === id);
const run = toutExecuter(lib);

describe('scénarios synthétiques', () => {
  test('au moins 100 scénarios, de tous les types', () => {
    assert.ok(run.scenarios.length >= 100, String(run.scenarios.length));
    for (const t of ['profil', 'echange', 'question', 'facultatif']) assert.ok(run.scenarios.some((s) => s.type === t), t);
  });

  test('chaque scénario respecte les huit critères', () => {
    const ko = run.resultats.filter((r) => !r.ok).map((r) => `${r.id} : ${[...r.violations, ...r.erreurs, ...r.incertitudes].join(' ; ')}`);
    assert.deepEqual(ko, []);
  });

  test('les critères détectent réellement les erreurs (test des tests)', () => {
    const f = byId('impots-assistanat');
    const ok = composer(f, { faits: 'chiffres' }, { bibliotheque: lib });
    assert.deepEqual(verite(f, ok), []);
    // 1. un fait altéré dans la sortie
    const m1 = structuredClone(ok);
    m1.plans.gagner.preuves[0].texte = m1.plans.gagner.preuves[0].texte.replace(/\d/, '9');
    assert.ok(verite(f, m1).some((e) => /fait modifié/.test(e)));
    // 2. un nombre ajouté dans un bloc
    const m2 = structuredClone(ok);
    m2.gagner.blocs.push({ type: 'texte', texte: 'Et 87 654 personnes le confirment.' });
    assert.ok(verite(f, m2).some((e) => /absent de la fiche/.test(e)));
    // 3. une source non consultée
    const f3 = structuredClone(f);
    for (const s of f3.sources) s.consultee = false;
    assert.ok(verite(f3, composer(f3, {}, { bibliotheque: lib })).some((e) => /source/.test(e)));
    // 4. un profil présenté comme un fait
    const m4 = structuredClone(ok);
    m4.convaincre.blocs.push({ type: 'texte', texte: 'Cette personne est susceptible.' });
    assert.ok(verite(f, m4).some((e) => /profil/.test(e)));
    // 5. une attente de profil non respectée
    const m5 = structuredClone(ok.plans);
    m5.gagner.max_preuves = 3;
    assert.ok(attentes({ debat: 'competitif' }, m5, f, ok).length > 0);
    // 6. une fiche sans chiffre pour un profil « chiffres » : l'absence est signalée, rien n'est comblé
    const r6 = evaluer({ type: 'profil', id: 'chiffres-sans-chiffre', fiche: byId('laicite-loi-1905'), profil: { faits: 'chiffres' } }, lib);
    assert.ok(r6.ok, JSON.stringify(r6));
  });

  test('diversité : la grande majorité des paires de profils diffèrent sur le fond', () => {
    const d = run.diversite;
    assert.ok(d.paires > 500);
    assert.ok(d.pertinentes / d.paires > 0.85, `${d.pertinentes}/${d.paires}`);
    assert.equal(d.identiques.length, 0, d.identiques.join('\n'));
  });
});

describe('différenciation réelle', () => {
  test('profils qui ne justifient pas de différence : réponse strictement identique', () => {
    const ko = run.temoins.filter((t) => !t.ok).map((t) => `${t.raison} : ${t.ecarts.join(', ')}`);
    assert.deepEqual(ko, []);
  });

  test('même affirmation, trois profils (chiffres, méfiance, se braque) : plans différents, faits identiques', () => {
    const f = byId('impots-assistanat');
    const plans = [{ faits: 'chiffres' }, { autorite: 'mefiance' }, { debat: 'susceptible' }].map((p) => planifier(f, { profil: p, mode: 'gagner', bibliotheque: lib }));
    const [c, m, s] = plans;
    assert.equal(c.approche, 'factuelle');
    assert.ok(c.preuves[0].chiffre);
    assert.ok(m.preuves.every((x) => x.methode));
    assert.ok(m.preuves.length >= c.preuves.length);
    // v9 : en mode « gagner », même face à quelqu'un qui se braque, on entre par le fond (pas par une écoute de principe) ;
    // la reformulation reste la porte d'entrée du mode « convaincre »
    assert.ok(['concession', 'fait', 'correction', 'cadre', 'exemple'].includes(s.entree), s.entree);
    assert.equal(planifier(f, { profil: { debat: 'susceptible' }, mode: 'convaincre', bibliotheque: lib }).entree, 'reformulation');
    assert.notEqual(s.ton, c.ton, 'le ton reste adapté au profil');
    for (const pl of plans) for (const pr of pl.preuves) assert.equal(pr.texte, f.faits[pr.index].fait);
    assert.notDeepEqual(empreinte(c), empreinte(m));
    assert.notDeepEqual(empreinte(m), empreinte(s));
  });

  test('chaque option du questionnaire modifie le plan sur au moins une fiche, ou est documentée comme neutre', () => {
    const fiches = lib.filter((f) => f.type !== 'science');
    const fp = (a) => JSON.stringify({ g: a.gagner.blocs, c: a.convaincre.blocs });
    for (const d of INTERLOCUTEUR) {
      for (const [k] of d.options) {
        const e = EFFETS[d.id]?.[k];
        assert.ok(e, `${d.id}.${k} absent de la table EFFETS`);
        const base = d.id === 'debat' ? { faits: 'chiffres' } : { debat: 'calme' };
        const p = { ...base, [d.id]: d.multi ? [k] : k };
        const n = fiches.filter((f) => fp(composer(f, p, { bibliotheque: lib })) !== fp(composer(f, base, { bibliotheque: lib }))).length;
        if (e.neutre) assert.equal(n, 0, `${d.id}.${k} déclaré neutre mais modifie ${n} fiches`);
        else assert.ok(n > 0, `${d.id}.${k} sans effet`);
      }
    }
  });

  test('le mode change le contenu, pas les faits', () => {
    const f = byId('rsa-smic');
    const g = planifier(f, { profil: {}, mode: 'gagner', bibliotheque: lib });
    const c = planifier(f, { profil: {}, mode: 'convaincre', bibliotheque: lib });
    assert.notEqual(g.ordre.join(), c.ordre.join());
    for (const pl of [g, c]) for (const pr of pl.preuves) assert.equal(pr.texte, f.faits[pr.index].fait);
  });

  test('arguments déjà avancés : le moteur ne les répète pas', () => {
    const f = byId('impots-assistanat');
    const a = planifier(f, { profil: {}, mode: 'gagner', bibliotheque: lib });
    const deja = a.preuves.map((p) => p.index);
    const b = planifier(f, { profil: {}, mode: 'gagner', deja, bibliotheque: lib });
    assert.ok(b.preuves.every((p) => !deja.includes(p.index)) || b.preuves.length === 0 || f.faits.length <= deja.length);
  });

  test('comparaison de 2 ou 3 approches, sans garantie ni pourcentage', () => {
    for (const id of ['impots-assistanat', 'front-populaire-1936', 'melenchon-crie']) {
      const ap = comparerApproches(byId(id), { profil: { autorite: 'mefiance' }, mode: 'convaincre', bibliotheque: lib });
      assert.ok(ap.length >= 2 && ap.length <= 3, id);
      for (const x of ap) {
        assert.ok(x.profil && x.pourquoi && x.risques && x.limites && x.questions?.length, `${id} ${x.approche}`);
        assert.doesNotMatch(JSON.stringify({ ...x, preuves: undefined, limites: undefined }), /\d+\s?%|garanti|probabilit/i);
      }
    }
  });

  test('chaque consigne repose sur une fiche scientifique dotée de son référentiel', () => {
    const sci = new Map(lib.filter((e) => e.type === 'science').map((e) => [e.id, e]));
    assert.ok(sci.size >= 16);
    for (const r of REGLES) {
      const f = sci.get(r.fiche);
      assert.ok(f, r.id);
      assert.ok(['recherche', 'pratique'].includes(r.fondement), r.id);
    }
    for (const f of sci.values()) {
      assert.ok(f.reference?.auteurs && f.reference?.annee && f.reference?.url?.startsWith('https://'), f.id);
      assert.ok(['elevee', 'moyenne', 'faible'].includes(f.confiance), f.id);
      assert.ok(f.conditions && f.limites_methodo, f.id);
    }
  });
});
