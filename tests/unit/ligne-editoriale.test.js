// v10 — Identité éditoriale de gauche et politique documentaire : 15 sujets obligatoires, audit des sources,
// garde-fou de dignité, lecture de gauche, consignes du mode connecté.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary } from '../../server/library.js';
import { analyserPhrase } from '../../public/js/analyse.js';
import { composer } from '../../public/js/composer.js';
import { auditFiche, classerSource, roleSource, atteintesDignite, LE_PRINCIPES, LE_SIGNATURE, LE_POLITIQUE_SOURCES } from '../../public/js/ligne-editoriale.js';
import { researchSystemPrompt } from '../../server/engine/research.js';
import { strategySystemPrompt } from '../../server/engine/strategy.js';
import { conversationSystemPrompt } from '../../server/engine/conversation.js';
import { SPEECH_SYSTEM } from '../../server/engine/speech.js';

const lib = loadLibrary(undefined, { warn() {} });
const thema = lib.filter((f) => f.type !== 'science');
const byId = (id) => lib.find((f) => f.id === id);

// Les 15 sujets du cahier des charges : une phrase typique, la fiche qui doit répondre.
const SUJETS = [
  ['Judéo-bolchevisme et Vichy', 'Le judéo-bolchevisme, c’était juste de l’anticommunisme.', 'judeo-bolchevisme-histoire'],
  ['Islamo-gauchisme', 'L’islamo-gauchisme gangrène l’université.', 'islamo-gauchisme-origine-usages'],
  ['Immigration et travail', 'Les immigrés prennent le travail des Français.', 'immigration-emploi'],
  ['Immigration et prestations', 'Les immigrés touchent plus d’aides que nous.', 'immigres-aides'],
  ['Immigration et criminalité', 'Les étrangers remplissent les prisons.', 'etrangers-prisons'],
  ['Nationalisme et patriotisme', 'La gauche déteste la France.', 'gauche-nation-debats'],
  ['Laïcité et liberté religieuse', 'La laïcité, c’est interdire le voile partout.', 'laicite-loi-1905'],
  ['Mélenchon et communication', 'Mélenchon crie tout le temps.', 'melenchon-crie'],
  ['Capitalisme et richesses', 'Ce sont les riches qui créent les emplois.', 'riches-creent-emplois'],
  ['Sécurité sociale et CNR', 'La Sécu, c’est un cadeau qu’on ne peut plus se payer.', 'securite-sociale-1945'],
  ['Racisme et discriminations', 'Les discriminations à l’embauche, ça n’existe plus.', 'discriminations-embauche'],
  ['Droits humains et migrations', 'Il ne faut pas secourir les migrants en mer, ça crée un appel d’air.', 'migrants-mediterranee'],
  ['Antisémitisme et instrumentalisation', 'L’antisémitisme, c’est un faux problème pour faire taire la gauche.', 'antisemitisme-aujourdhui'],
  ['Services publics et justice sociale', 'La France n’a plus les moyens de financer ses services publics.', 'services-publics-moyens'],
  ['Égalité femmes-hommes', 'L’égalité salariale entre les femmes et les hommes, c’est réglé.', 'egalite-salariale'],
];
const chiffres = (t) => (String(t).match(/\d[\d\s,.]*/g) || []).map((x) => x.replace(/[\s.,]+$/, '').trim()).filter(Boolean);

describe('identité éditoriale et politique documentaire (v10)', () => {
  for (const [sujet, phrase, id] of SUJETS) {
    test(`sujet : ${sujet}`, () => {
      const an = analyserPhrase(phrase, { bibliotheque: lib });
      assert.equal(an.principal?.fiche?.id, id, `« ${phrase} » → ${an.principal?.fiche?.id}`);
      const f = byId(id);
      // pertinence des sources : conformes à la politique documentaire, au moins une source d'autorité
      assert.deepEqual(auditFiche(f), [], `${id} : ${auditFiche(f).join(' ; ')}`);
      // pour la communication politique, la presse de référence est la source pertinente ; sinon, une autorité est exigée
      assert.ok(f.sources.some((s) => roleSource(s) === 'autorite' || classerSource(s) === 'presse_reference'), `${id} : ni autorité ni presse de référence`);
      if (!['melenchon-crie'].includes(id)) assert.ok(f.sources.some((s) => roleSource(s) === 'autorite'), `${id} : aucune source d’autorité`);
      assert.ok(!f.sources.some((s) => classerSource(s) === 'tertiaire'), `${id} : source encyclopédique`);
      // cohérence avec les valeurs : lecture de gauche complète
      const L = f.lecture;
      assert.ok(L, `${id} : pas de lecture de gauche`);
      assert.ok(L.valeurs.length >= 2 && L.valeurs.every((v) => LE_PRINCIPES[v]), `${id} : valeurs`);
      assert.ok(L.mecanismes && L.democratie, `${id} : mécanismes et enjeux démocratiques`);
      assert.ok(L.propositions.length >= 1, `${id} : propositions`);
      // capacité à reconnaître les faits défavorables
      assert.ok(L.defavorables.length >= 1 && L.defavorables.every((d) => d.fait && d.integration), `${id} : faits défavorables`);
      // absence de fausse référence : aucun chiffre de la lecture qui ne figure pas dans les faits et sources de la fiche
      const ref = JSON.stringify({ faits: f.faits, sources: f.sources, resume: f.resume, contexte: f.contexte, A: f.argumentaires, limites: f.limites, legit: f.objections_legitimes });
      for (const n of chiffres(JSON.stringify(L))) assert.ok(ref.includes(n), `${id} : chiffre « ${n} » de la lecture absent des faits sourcés`);
      // présent dans l'argumentaire, dans les deux modes, propositions étiquetées comme telles
      const a = composer(f, { inconnu: true }, { bibliotheque: lib });
      for (const mode of ['gagner', 'convaincre']) {
        const b = a[mode].blocs.find((x) => x.type === 'lecture');
        assert.ok(b && b.priorite === 'lecture', `${id} (${mode}) : bloc lecture`);
        const types = a[mode].blocs.map((x) => x.type);
        assert.ok(types.indexOf('preuves') < types.indexOf('lecture'), 'les preuves avant la lecture politique');
      }
    });
  }

  test('toutes les fiches respectent la politique documentaire', () => {
    const pb = thema.flatMap((f) => auditFiche(f).map((p) => `${f.id} : ${p}`));
    assert.deepEqual(pb, []);
  });

  test('aucun fait ne repose sur une encyclopédie ; toute source de droite ou partisane est attribuée', () => {
    for (const f of thema) {
      for (const x of f.faits) {
        const s = f.sources[x.source];
        assert.notEqual(classerSource(s), 'tertiaire', `${f.id} : « ${x.fait.slice(0, 60)} »`);
        if (roleSource(s) === 'origine') assert.match(x.fait, /selon|programme|propos|déclar|écrit|estim|pourtant|simulation|tribune|contest|\bdit\b|dit «|affirm|qualifi|jug|dénon|d’après|rapport/i, `${f.id} : « ${x.fait.slice(0, 80)} »`);
      }
    }
  });

  test('classement des sources', () => {
    const c = (organisme, url = '') => classerSource({ organisme, url });
    assert.equal(c('Insee'), 'recherche');
    assert.equal(c('DREES'), 'recherche');
    assert.equal(c('Sénat'), 'institution');
    assert.equal(c('Défenseur des droits'), 'institution');
    assert.equal(c('Mémorial de la Shoah'), 'histoire');
    assert.equal(c('Public Sénat'), 'presse_reference');
    assert.equal(c('Le Monde'), 'presse_reference');
    assert.equal(c('Amnesty International'), 'association');
    assert.equal(c('Fondation iFRAP (Gilles Koleda)'), 'droite');
    assert.equal(c('CNews'), 'droite');
    assert.equal(c('Institut Montaigne'), 'droite');
    assert.equal(c('Union populaire / La France insoumise (source partisane)'), 'partisane');
    assert.equal(c('Wikipédia'), 'tertiaire');
    assert.equal(roleSource({ organisme: 'Fondation iFRAP' }), 'origine');
    assert.equal(roleSource({ organisme: 'Insee' }), 'autorite');
  });

  test('corrections documentaires : islamo-gauchisme ré-sourcé, date erronée corrigée, otages de la Commune conservés', () => {
    const f = byId('islamo-gauchisme-origine-usages');
    assert.ok(f.sources.some((s) => /politoscope/.test(s.url)) && f.sources.some((s) => /ucl\.ac\.uk/.test(s.url)));
    assert.doesNotMatch(JSON.stringify(f), /octobre 2019/);
    const c = byId('commune-paris-1871');
    assert.ok(c.faits.some((x) => /otages/.test(x.fait) && /Darboy/.test(x.fait)), 'le fait défavorable aux communards reste présent');
    const a = byId('antisemitisme-aujourdhui');
    assert.ok(a.faits.some((x) => /LFI/.test(x.fait)), 'le fait défavorable à la gauche est présent');
  });

  test('dignité humaine : fermeté sur la déshumanisation, la violence, l’exclusion collective et l’antisémitisme', () => {
    const cas = {
      'Les immigrés sont des parasites.': 'deshumanisation', 'Ces gens-là sont des animaux.': 'deshumanisation',
      'Il faut les laisser se noyer.': 'violence', 'Les migrants ? Qu’ils crèvent.': 'violence', 'On devrait couler leurs bateaux.': 'violence',
      'Tous les arabes dehors !': 'exclusion_collective', 'Il faut organiser la remigration.': 'exclusion_collective',
      'Les juifs contrôlent les médias.': 'antisemitisme',
    };
    for (const [t, id] of Object.entries(cas)) assert.ok(atteintesDignite(t).some((d) => d.id === id), t);
    // critiquer une politique n'est pas une atteinte à la dignité
    for (const t of ['Il faut réduire l’immigration.', 'La justice est trop laxiste.', 'Je critique la politique du gouvernement israélien.', 'Le virus de la grippe revient.', 'L’islam, comme toute religion, peut être critiqué.', 'Il faut expulser les étrangers condamnés pour des crimes graves.']) {
      assert.deepEqual(atteintesDignite(t), [], t);
    }
    assert.ok(analyserPhrase('Les immigrés sont des parasites.', { bibliotheque: lib }).dignite.length);
  });

  test('mode connecté : la ligne éditoriale et la politique documentaire sont dans toutes les consignes', () => {
    for (const p of [strategySystemPrompt('gagner'), strategySystemPrompt('convaincre'), conversationSystemPrompt('gagner'), SPEECH_SYSTEM]) {
      assert.ok(p.includes(LE_SIGNATURE), 'signature éditoriale');
      assert.match(p, /antifasciste/);
      assert.match(p, /Ne jamais inventer une statistique/);
      assert.match(p, /patriotisme, souveraineté nationale, nationalisme et xénophobie/);
    }
    const r = researchSystemPrompt('2026-10-30');
    assert.ok(r.includes(LE_POLITIQUE_SOURCES));
    assert.match(r, /jamais l'autorité qui valide un fait/);
    assert.match(r, /CNCDH/);
  });
});
