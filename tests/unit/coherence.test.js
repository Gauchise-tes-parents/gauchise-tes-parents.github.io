// v11 — Cohérence des réponses dans tous les domaines : les 764 affirmations suggérées, traitées comme dans
// l'application, avec des choix différents (mode, profil d'interlocuteur), doivent mener à des réponses cohérentes.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary } from '../../server/library.js';
import { resoudrePhrase, conceptsFiche } from '../../public/js/analyse.js';
import { composer } from '../../public/js/composer.js';
import { SG_BIBLIOTHEQUE, suggestionsPour } from '../../public/js/suggestions.js';
import { VOLETS } from '../../public/js/taxonomy.js';
import { auditCoherence } from '../../scripts/audit-coherence.js';

const lib = loadLibrary(undefined, { warn() {} });
const lignes = auditCoherence(lib);
const couvertes = lignes.filter((l) => l.statut === 'coherent');
const cache = new Map(lignes.map((l) => [l.texte, Boolean(l.fiche)]));
const estCouverte = (t) => cache.get(t) ?? Boolean(resoudrePhrase(t, lib).fiche);
// Sous-thèmes encore sans fiche (lacunes documentées dans le rapport, à combler par des fiches sourcées)
// v12 : « Histoire économique » n'était couverte que par un faux positif (« nationalisations » reconnu comme
// « nation » et envoyé vers la fiche sur le patriotisme) ; la lacune est désormais annoncée honnêtement.
// v13 : « Libertés publiques » n'était couverte que par un faux positif (« protège les honnêtes gens » reconnu comme
// « la justice protège les délinquants ») ; corrigé, la lacune est annoncée.
const SANS_FICHE = ['Émancipation', 'Institutions françaises', 'Constitution', 'Histoire économique', 'Libertés publiques'];
const PROFILS = [{ inconnu: true }, { faits: 'chiffres', debat: 'competitif' }, { debat: 'susceptible', lien: 'parent', valeurs: ['securite'] }];

describe('cohérence des réponses dans tous les domaines (v11)', () => {
  test('aucune affirmation suggérée ne renvoie vers une fiche d’un autre domaine', () => {
    const suspects = lignes.filter((l) => l.statut === 'suspect').map((l) => `[${l.volet} / ${l.sous_theme}] ${l.texte} → ${l.fiche}`);
    assert.deepEqual(suspects, []);
  });

  test('couverture : au moins 435 affirmations sur 764 obtiennent une fiche cohérente', () => {
    assert.equal(lignes.length, 764);
    assert.ok(couvertes.length >= 435, String(couvertes.length));
  });

  test('chaque sous-thème (hors lacunes documentées) a au moins une affirmation qui mène à une fiche', () => {
    for (const v of VOLETS) for (const st of v.sousThemes) {
      const n = couvertes.filter((l) => l.volet === v.id && l.sous_theme === st).length;
      if (SANS_FICHE.includes(st)) continue;
      assert.ok(n >= 1, `${v.id} › ${st} : aucune affirmation couverte`);
    }
  });

  test('les suggestions affichées en premier mènent à une réponse, quels que soient le mode et le profil', () => {
    for (const [volet, sts] of Object.entries(SG_BIBLIOTHEQUE)) for (const st of Object.keys(sts)) {
      const n = couvertes.filter((l) => l.volet === volet && l.sous_theme === st).length;
      if (!n) continue;
      for (const mode of ['gagner', 'convaincre']) for (const p of PROFILS) {
        const r = suggestionsPour({ volet, sousTheme: st, mode, interlocuteur: p.inconnu ? {} : p, estCouverte }, 3);
        const ok = r.suggestions.filter((x) => estCouverte(x.texte)).length;
        assert.equal(ok, Math.min(3, n), `${volet} › ${st} (${mode}) : ${ok} suggestion(s) couverte(s) sur ${Math.min(3, n)} possibles`);
      }
    }
  });

  test('toutes les affirmations couvertes × 2 modes × 3 profils : réponse d’abord, preuves sourcées, modes distincts', () => {
    let n = 0;
    for (const l of couvertes) {
      const f = lib.find((x) => x.id === l.fiche);
      const cf = conceptsFiche(f);
      assert.ok(f.volet === l.volet || l.concepts.some((c) => cf.includes(c)) || f.sous_theme === l.sous_theme || f.type === 'histoire', `${l.texte} → ${f.id}`);
      for (const p of PROFILS) {
        const a = composer(f, p, { bibliotheque: lib });
        for (const mode of ['gagner', 'convaincre']) {
          const b = a[mode].blocs;
          assert.equal(b[0].type, 'replique', `${f.id} (${mode}) : la réponse vient d’abord`);
          assert.ok(b[0].texte && b[0].texte.length > 30, `${f.id} : réponse vide`);
          const pr = b.find((x) => x.type === 'preuves');
          assert.ok(pr && pr.items.length && pr.items.every((i) => i.source?.url), `${f.id} (${mode}) : preuves sourcées`);
          if (f.lecture) assert.ok(b.some((x) => x.type === 'lecture'), `${f.id} (${mode}) : lecture de gauche`);
          n += 1;
        }
        const tg = a.gagner.blocs.map((x) => x.titre); const tc = a.convaincre.blocs.map((x) => x.titre);
        assert.ok(tg.includes('La réplique qui sème le doute') && !tg.some((t) => /indécis|expliquer simplement|mots simples|se faire son avis/i.test(t)), `${f.id} : mode gagner`);
        assert.ok(tc.includes('Pour l’expliquer simplement'), `${f.id} : mode convaincre`);
      }
    }
    assert.ok(n >= 435 * 6, String(n));
  });
});
