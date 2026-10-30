// v12 — Le moteur doit donner une vraie réponse aux questions fréquentes : les 20 questions de la demande
// (et 3 variantes), dans les deux modes ; une phrase proposée doit être prête à l'emploi ; sans fiche, la limite
// est annoncée (aucune fiche voisine) ; les sujets RSA ne contaminent pas les autres.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary } from '../../server/library.js';
import { resoudrePhrase, analyserPhrase } from '../../public/js/analyse.js';
import { composer } from '../../public/js/composer.js';
import { suggestionsPour, SG_BIBLIOTHEQUE } from '../../public/js/suggestions.js';
import { auditFiche } from '../../public/js/ligne-editoriale.js';

const lib = loadLibrary(undefined, { warn() {} });

import { Q20 } from '../v12-questions.js';

const VARIANTES = [
  ['Pourquoi est-il si difficile de retrouver du travail après 50 ans ?', 'emploi-apres-50-ans'],
  ['L’héritage, c’est le fruit du travail des parents, il ne faut pas le taxer.', 'heritage-taxation'],
  ['Peut-on encore devenir propriétaire avec un salaire moyen ?', 'devenir-proprietaire'],
  // formulations inédites ou familières des mêmes sujets
  ['Franchement les syndicats ils bloquent tout, ils servent à rien.', 'syndicats-bloquent'],
  ['On nous remplace, bientôt la France aura disparu.', 'grand-remplacement'],
  ['La naturalisation, on la donne à n’importe qui.', 'nationalite-trop-facile'],
  ['Les fraudeurs aux allocs nous coûtent une fortune.', 'fraude-sociale-fiscale'],
];
const MODES = ['gagner', 'convaincre'];

describe('v12 — les 20 questions de la demande', () => {
  for (const [q, attendu] of [...Q20, ...VARIANTES]) {
    test(q, () => {
      const r = resoudrePhrase(q, lib);
      assert.equal(r.fiche?.id, attendu, `fiche obtenue : ${r.fiche?.id || 'aucune'} (${r.voie})`);
      const f = r.fiche;
      // prête à l'emploi : réponse courte, argumentaire, faits sourcés, plusieurs sources, réfutation, proposition
      assert.ok(f.argumentaires.court.length > 40, 'réponse courte');
      assert.ok(f.argumentaires.moyen && f.argumentaires.detaille, 'argumentaire');
      assert.ok(f.faits.length >= 2 && f.faits.every((x) => f.sources[x.source]?.url), 'faits sourcés');
      assert.ok(f.sources.length >= 2, `plusieurs sources (${f.sources.length})`);
      assert.ok(f.contre_arguments.length >= 2, 'réfutation des objections');
      assert.ok(f.lecture?.propositions?.length >= 1, 'proposition alternative (lecture de gauche)');
      assert.deepEqual(auditFiche(f), [], 'politique documentaire respectée');
      const a = composer(f, {}, { bibliotheque: lib });
      for (const mode of MODES) {
        const b = a[mode].blocs;
        assert.equal(b[0].type, 'replique', `${mode} : la réponse vient d’abord`);
        const ordre = b.map((x) => x.priorite).filter((p, i, t) => p && p !== t[i - 1]);
        assert.deepEqual(ordre.slice(0, 3), ['reponse', 'preuves', 'lecture'], `${mode} : réponse → preuves → lecture de gauche (${ordre.join(', ')})`);
        assert.ok(b.find((x) => x.type === 'preuves').items.every((i) => i.source?.url), `${mode} : preuves avec lien`);
      }
      const tg = a.gagner.blocs.map((x) => x.titre); const tc = a.convaincre.blocs.map((x) => x.titre);
      assert.ok(tg.includes('La riposte qui fait réfléchir') && !tg.some((t) => /empathie|sans braquer/i.test(t)), 'mode gagner sans les outils du mode convaincre');
      assert.ok(tc.includes('Pour l’introduire sans braquer') && !tc.includes('La riposte qui fait réfléchir'), 'mode convaincre sans la riposte');
    });
  }
});

describe('v12 — compréhension', () => {
  test('classification multiple : une phrase peut toucher plusieurs domaines', () => {
    const an = analyserPhrase('Les étrangers profitent des aides et volent nos emplois, c’est pour ça qu’il y a de l’insécurité.', { bibliotheque: lib });
    const ids = an.domaines.map((d) => d.id);
    for (const v of ['immigration', 'social', 'securite']) assert.ok(ids.includes(v), `${v} dans ${ids.join(', ')}`);
  });

  test('« nationalisations » n’est plus confondu avec la nation (faux positif corrigé)', () => {
    const an = analyserPhrase('Les nationalisations ont été des échecs.', { bibliotheque: lib });
    assert.ok(!an.concepts.some((c) => c.id === 'patriotisme'));
    assert.equal(resoudrePhrase('Les nationalisations ont été des échecs.', lib).fiche, null);
  });

  test('sans fiche : lacune reconnue, aucune fiche voisine présentée comme réponse', () => {
    for (const q of ['Le prix du pain au Moyen Âge.', 'Faut-il parler français pour obtenir la nationalité ?', 'Comment les grèves de 1936 ont-elles changé la vie des ouvriers ?', 'D’où vient la retraite par répartition ?']) {
      const r = resoudrePhrase(q, lib);
      assert.equal(r.fiche, null, `${q} → ${r.fiche?.id}`);
    }
  });
});

describe('v12 — non-régression RSA et absence de contamination', () => {
  const RSA = [
    ['Avec le RSA, on gagne autant qu’au SMIC.', 'rsa-smic'],
    ['Les gens préfèrent rester au RSA plutôt que travailler.', 'rsa-profiteurs'],
  ];
  for (const [q, attendu] of RSA) test(`RSA : ${q}`, () => assert.equal(resoudrePhrase(q, lib).fiche?.id, attendu));

  test('aucune des 20 questions (hors aides sociales) ne reçoit une fiche RSA', () => {
    for (const [q] of Q20) {
      const id = resoudrePhrase(q, lib).fiche?.id || '';
      assert.ok(!/^rsa-/.test(id), `${q} → ${id}`);
    }
  });

  test('une source sur le RSA n’apparaît que si la fiche établit un lien précis', () => {
    for (const [q] of Q20) {
      const f = resoudrePhrase(q, lib).fiche;
      const rsa = f.sources.filter((s) => /\bRSA\b/.test(s.titre));
      if (rsa.length) assert.ok(['immigres-aides', 'aider-tout-le-monde', 'fraude-sociale-fiscale'].includes(f.id) || /\bRSA\b/.test(f.resume + f.argumentaires.detaille), `${f.id} cite une source RSA sans lien`);
    }
  });
});

describe('v12 — les phrases proposées sont prêtes à l’emploi', () => {
  const couv = new Map();
  const estCouverte = (t) => { if (!couv.has(t)) couv.set(t, Boolean(resoudrePhrase(t, lib).fiche)); return couv.get(t); };
  test('avec seulementCouvertes, aucune suggestion sans réponse vérifiée, dans aucun sous-thème ni mode', () => {
    let proposees = 0; let enPrep = 0;
    for (const [volet, sts] of Object.entries(SG_BIBLIOTHEQUE)) for (const st of Object.keys(sts)) for (const mode of MODES) {
      const r = suggestionsPour({ volet, sousTheme: st, mode, estCouverte, seulementCouvertes: true }, 3);
      for (const s of r.suggestions) assert.ok(estCouverte(s.texte), `${volet} › ${st} : « ${s.texte} » proposée sans fiche`);
      proposees += r.suggestions.length; enPrep += r.enPreparation;
    }
    assert.ok(proposees > 300 && enPrep > 0, `${proposees} proposées, ${enPrep} en préparation`);
  });
});
