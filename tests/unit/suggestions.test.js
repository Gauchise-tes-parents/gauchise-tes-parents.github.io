// v7 : suggestions spécialisées par sous-thème, rubrique « Immigration, délinquance et prisons »,
// rebonds de conversation (changement d'argument). Tests exécutés hors ligne, sans clé API.
import { test, describe } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary, LIBRARY_DIR } from '../../server/library.js';
import { VOLETS } from '../../public/js/taxonomy.js';
import { SG_BIBLIOTHEQUE, suggestionsPour, auditSuggestions, sgPool } from '../../public/js/suggestions.js';
import { kbMatch } from '../../public/js/kbsearch.js';
import { composer } from '../../public/js/composer.js';
import { nouvelleConversation, repondreConversation } from '../../public/js/conversation.js';
import { silent } from '../helpers.js';

const lib = loadLibrary(LIBRARY_DIR, silent);
const byId = (id) => lib.find((e) => e.id === id);
const thematiques = lib.filter((e) => e.type !== 'science');
const textes = (r) => r.suggestions.map((s) => s.texte);

describe('bibliothèque de suggestions : validation automatique', () => {
  test('chaque sous-thème a au moins 5 suggestions distinctes, dont 2 par mode, sans doublon ni quasi-doublon', () => {
    const a = auditSuggestions();
    assert.deepEqual(a.problemes, []);
    assert.equal(a.sousThemes, VOLETS.reduce((n, v) => n + v.sousThemes.length, 0));
    assert.ok(a.sousThemes >= 127, String(a.sousThemes));
    assert.ok(a.suggestions >= 5 * a.sousThemes);
  });

  test('le validateur détecte un sous-thème insuffisant et un doublon (test du test)', () => {
    const sauve = SG_BIBLIOTHEQUE.immigration['Logement'];
    SG_BIBLIOTHEQUE.immigration['Logement'] = ['c|Les étrangers font monter les loyers.', 'i|Les étrangers font monter les loyers.'];
    try {
      const a = auditSuggestions();
      assert.ok(a.problemes.some((p) => /Logement : 2 suggestion/.test(p)));
      assert.ok(a.problemes.some((p) => /doublon/.test(p)));
    } finally { SG_BIBLIOTHEQUE.immigration['Logement'] = sauve; }
  });

  test('aucune suggestion n’est présentée comme une citation attribuée', () => {
    for (const v of Object.values(SG_BIBLIOTHEQUE)) for (const arr of Object.values(v)) for (const s of arr) {
      assert.doesNotMatch(s, /(a déclaré|selon [A-Z]|a dit que)/, s);
    }
  });
});

describe('parcours immigration : suggestions réellement adaptées au sous-thème', () => {
  const PARCOURS = {
    'Immigration et travail': /(travail|salaire|métier|cotis|emploi|ménage|bâtiment)/i,
    'Immigration et aides sociales': /(aide|RSA|allocation|Sécu)/i,
    'Immigration et asile': /(asile|débout|misère)/i,
    'Immigration et démographie': /(population|natalité|vieilli|retraite|remplacement|tiers)/i,
    'Intégration': /(intégr|français|école|travail)/i,
    'Immigration et délinquance': /(délinqu|vols|insécurité|police|mis en cause)/i,
    'Immigration, délinquance et prisons': /(prison|carcéral|délinqu|sûre|détention|insécurité)/i,
    'Expulsion des étrangers condamnés': /(expuls|renvoy|séjour|crime|OQTF|criminel)/i,
  };
  for (const [st, re] of Object.entries(PARCOURS)) {
    test(`${st} : 3 suggestions distinctes et pertinentes dans chaque mode`, () => {
      for (const mode of ['gagner', 'convaincre']) {
        const r = suggestionsPour({ volet: 'immigration', sousTheme: st, mode }, 3);
        assert.equal(r.suggestions.length, 3);
        assert.equal(new Set(textes(r)).size, 3);
        for (const s of r.suggestions) {
          assert.equal(s.sousTheme, st);
          assert.match(s.texte, re, `${st} (${mode}) : « ${s.texte} »`);
        }
      }
    });
  }

  test('les 5 formulations sur les prisons et les 6 sur l’expulsion sont proposées et chacune a sa propre fiche', () => {
    const prisons = sgPool('immigration', 'Immigration, délinquance et prisons').map((s) => s.texte);
    const expulsion = sgPool('immigration', 'Expulsion des étrangers condamnés').map((s) => s.texte);
    const attendus = {
      'Les immigrés représentent une part disproportionnée de la population carcérale.': 'immigres-prisons-surrepresentation',
      'Les étrangers remplissent les prisons françaises.': 'etrangers-prisons',
      'La délinquance est principalement liée à l’immigration.': 'delinquance-principalement-immigration',
      'La France serait plus sûre si elle accueillait moins d’immigrés.': 'france-plus-sure-moins-immigres',
      'Les statistiques de délinquance démontrent que l’immigration augmente l’insécurité.': 'statistiques-prouvent-insecurite-immigration',
      'Tous les étrangers condamnés devraient être expulsés.': 'expulser-tous-etrangers-condamnes',
      'Un étranger qui commet un crime n’a plus sa place en France.': 'etranger-crime-plus-sa-place',
      'Il suffit d’expulser les délinquants étrangers pour réduire la criminalité.': 'expulser-reduit-criminalite',
      'Les criminels étrangers sont protégés par la justice française.': 'criminels-etrangers-proteges-justice',
      'Il faut renvoyer tous les étrangers qui ont déjà été condamnés.': 'renvoyer-tous-deja-condamnes',
      'Une personne étrangère condamnée devrait automatiquement perdre son droit de séjour.': 'perte-automatique-droit-sejour',
    };
    for (const [t, id] of Object.entries(attendus)) {
      assert.ok(prisons.includes(t) || expulsion.includes(t), t);
      const m = kbMatch(thematiques, t)[0];
      assert.equal(m.fiche.id, id, t);
      assert.equal(m.force, 'forte', t);
    }
    assert.equal(new Set(Object.values(attendus)).size, 11, 'onze fiches distinctes : les formulations ne sont pas traitées comme équivalentes');
    // « immigrés » n'est pas redirigé vers la fiche sur les étrangers
    assert.equal(kbMatch(thematiques, 'Les immigrés remplissent les prisons françaises.')[0].fiche.id, 'immigres-prisons-surrepresentation');
  });
});

describe('sélection contextuelle et renouvellement', () => {
  test('9. le mode change réellement la sélection', () => {
    for (const v of VOLETS.filter((x) => x.sousThemes.length)) for (const st of v.sousThemes) {
      const g = suggestionsPour({ volet: v.id, sousTheme: st, mode: 'gagner' }, 3);
      const c = suggestionsPour({ volet: v.id, sousTheme: st, mode: 'convaincre' }, 3);
      assert.notDeepEqual(textes(g), textes(c), `${v.id} › ${st}`);
      assert.ok(g.suggestions[0].choc && !c.suggestions[0].choc, `${v.id} › ${st}`);
    }
  });

  test('« Autres affirmations » : renouvellement sans répétition jusqu’à épuisement, puis nouveau cycle', () => {
    const ctx = { volet: 'immigration', sousTheme: 'Expulsion des étrangers condamnés', mode: 'gagner' };
    const vues = [];
    const total = sgPool(ctx.volet, ctx.sousTheme).length;
    let r;
    while (vues.length < total) {
      r = suggestionsPour({ ...ctx, vues }, 3);
      const nouvelles = textes(r).filter((t) => !vues.includes(t));
      assert.ok(nouvelles.length >= Math.min(3, total - vues.length), 'les suggestions déjà vues ne reviennent pas tant qu’il en reste');
      vues.push(...nouvelles);
    }
    assert.equal(new Set(vues).size, total);
    assert.equal(suggestionsPour({ ...ctx, vues }, 3).cycle, true);
  });

  test('l’interlocuteur et le contexte influencent la sélection', () => {
    const base = suggestionsPour({ volet: 'immigration', sousTheme: 'Immigration et travail', mode: 'convaincre' }, 3);
    const chiffres = suggestionsPour({ volet: 'immigration', sousTheme: 'Immigration et travail', mode: 'convaincre', interlocuteur: { faits: 'chiffres' } }, 3);
    assert.ok(chiffres.suggestions[0].chiffre, 'argument chiffré en tête pour un profil « chiffres »');
    const vecu = suggestionsPour({ volet: 'immigration', sousTheme: 'Immigration et travail', mode: 'convaincre', interlocuteur: { faits: 'experience' } }, 3);
    assert.ok(vecu.suggestions[0].vecu, 'argument de vécu en tête pour un profil « expérience »');
    assert.notDeepEqual(textes(chiffres), textes(vecu));
    assert.ok(base.suggestions.length === 3);
    const secu = suggestionsPour({ volet: 'immigration', mode: 'gagner', interlocuteur: { valeurs: ['securite'] } }, 3);
    assert.ok(secu.suggestions.every((s) => /(sécurit|délinqu|police|prison|crime|expuls)/i.test(s.texte)), textes(secu).join(' / '));
  });

  test('volet sans sous-thème : les suggestions viennent de sous-thèmes différents', () => {
    const r = suggestionsPour({ volet: 'economie', mode: 'gagner' }, 3);
    assert.equal(new Set(r.suggestions.map((s) => s.sousTheme)).size, 3);
    assert.equal(suggestionsPour({ volet: 'autre', mode: 'gagner' }, 3).suggestions.length, 3);
  });
});

describe('nouvelles fiches : catégories statistiques et juridiques jamais mélangées', () => {
  const ids = ['etrangers-prisons', 'immigres-prisons-surrepresentation', 'delinquance-principalement-immigration', 'france-plus-sure-moins-immigres', 'statistiques-prouvent-insecurite-immigration',
    'expulser-tous-etrangers-condamnes', 'etranger-crime-plus-sa-place', 'expulser-reduit-criminalite', 'criminels-etrangers-proteges-justice', 'renvoyer-tous-deja-condamnes', 'perte-automatique-droit-sejour'];

  test('onze fiches, toutes sourcées par des sources consultées en https', () => {
    for (const id of ids) {
      const f = byId(id);
      assert.ok(f, id);
      assert.ok(f.rubriques.includes('immigration-prisons'), id);
      assert.ok(f.sources.every((s) => s.consultee && s.url.startsWith('https://')), id);
      assert.ok(f.faits.length >= 3 && f.contre_arguments.length >= 2 && f.questions.length >= 2 && f.limites.length >= 2, id);
    }
  });

  test('les chiffres sur la nationalité ne sont jamais attribués aux « immigrés »', () => {
    for (const id of ids) for (const fa of byId(id).faits) {
      if (/24,2 %|24,7 %|17,7 %|18 %/.test(fa.fait)) assert.doesNotMatch(fa.fait, /immigré/i, `${id} : « ${fa.fait} »`);
    }
    const b = byId('immigres-prisons-surrepresentation');
    assert.equal(b.verdict, 'inverifiable');
    assert.match(b.resume, /nationalité, pas le statut d'immigré/);
  });

  test('association statistique ≠ causalité', () => {
    for (const id of ['france-plus-sure-moins-immigres', 'statistiques-prouvent-insecurite-immigration', 'etrangers-prisons']) {
      const t = JSON.stringify(byId(id));
      assert.match(t, /(association|corrélation)/i, id);
      assert.match(t, /cause/i, id);
    }
  });

  test('distinctions juridiques : OQTF, expulsion, ITF, protections, CEDH, exécution ; garanties ≠ impunité', () => {
    const f = JSON.stringify(byId('expulser-tous-etrangers-condamnes'));
    for (const re of [/OQTF/, /arrêté d'expulsion|expulser/i, /interdiction du territoire/, /extradition/, /L\. 631-3/, /Cour européenne des droits de l'homme|CEDH/, /10 %/, /laissez-passer/]) assert.match(f, re);
    for (const id of ids.slice(5)) {
      const t = JSON.stringify(byId(id), (k, v) => (k === 'objection' || k === 'mots_cles' ? undefined : v)); // les objections et mots-clés citent l'adversaire
      for (const m of t.matchAll(/[^.]*impunité[^.]*/gi)) assert.match(m[0], /(pas|n'est pas|non|sentiment)/i, `${id} : ${m[0]}`);
    }
  });

  test('7. personnalisation conservée : mêmes faits, stratégie différente selon le profil', () => {
    const f = byId('etrangers-prisons');
    const a = composer(f, { faits: 'chiffres' }, { bibliotheque: lib });
    const b = composer(f, { faits: 'experience', debat: 'susceptible' }, { bibliotheque: lib });
    const c = composer(f, { valeurs: ['securite'] }, { bibliotheque: lib });
    assert.notEqual(a.plans.convaincre.entree, b.plans.convaincre.entree);
    assert.ok(c.plans.convaincre.angles.includes('securite'));
    for (const x of [a, b, c]) for (const p of x.plans.gagner.preuves) assert.equal(p.texte, f.faits[p.index].fait);
    assert.equal(a.gagner.replique, b.gagner.replique, 'la réponse courte (le fond) ne change pas');
  });
});

describe('rebonds de conversation : changement d’argument', () => {
  test('10. statistiques → droit de l’expulsion : le moteur ne recommence pas l’argument statistique', () => {
    const conv = nouvelleConversation(byId('etrangers-prisons'));
    repondreConversation(conv, 'N’importe quoi', { bibliotheque: lib });
    const r = repondreConversation(conv, 'Peu importe les statistiques, il faut tous les renvoyer chez eux.', { bibliotheque: lib });
    assert.equal(r.tour.analyse.type, 'deplacement');
    assert.equal(conv.courante, 'expulser-tous-etrangers-condamnes');
    assert.match(r.tour.intervention.texte, /Tu changes d’argument/);
    assert.ok(r.tour.intervention.options.some((o) => o.fiche_id === 'etrangers-prisons'), 'possibilité de revenir au point précédent');
    assert.ok(r.tour.intervention.question, 'une question pour poursuivre');
    assert.equal(conv.sujet.fiche_id, 'etrangers-prisons', 'le contexte initial est conservé');
    const s = repondreConversation(conv, 'T’as une source ?', { bibliotheque: lib });
    assert.equal(s.tour.intervention.preuve.fiche_id, 'expulser-tous-etrangers-condamnes', 'les preuves portent désormais sur l’expulsion');
    assert.doesNotMatch(s.tour.intervention.texte, /24,2 %/);
  });

  test('« même si… surreprésentés » : réponse spécifique sur la surreprésentation et les dénominateurs', () => {
    const conv = nouvelleConversation(byId('etrangers-prisons'));
    const r = repondreConversation(conv, 'Même si tous ne sont pas étrangers, les étrangers sont surreprésentés dans les prisons.', { bibliotheque: lib });
    assert.equal(r.tour.analyse.type, 'objection');
    assert.match(r.tour.intervention.texte, /comparer ce qui est comparable/);
    const depuisAutre = repondreConversation(nouvelleConversation(byId('delinquance-principalement-immigration')), 'Même si tous ne sont pas étrangers, les étrangers sont surreprésentés dans les prisons.', { bibliotheque: lib });
    assert.equal(depuisAutre.tour.analyse.type, 'deplacement');
    assert.equal(depuisAutre.conversation.courante, 'etrangers-prisons');
  });

  test('« Pourquoi garder en France quelqu’un qui a commis un crime ? » : bascule vers la justice pénale et l’éloignement', () => {
    const conv = nouvelleConversation(byId('etrangers-prisons'));
    const r = repondreConversation(conv, 'Pourquoi garder en France quelqu’un qui a commis un crime ?', { bibliotheque: lib });
    assert.equal(r.tour.analyse.type, 'deplacement');
    assert.equal(conv.courante, 'etranger-crime-plus-sa-place');
    assert.equal(r.tour.intervention.preuve.fiche_id, 'etranger-crime-plus-sa-place');
  });

  test('la logique de rebond fonctionne dans toute l’application', () => {
    const cas = [['rsa-smic', 'Peu importe, de toute façon les chômeurs ne veulent pas travailler', 'chomeurs-travailler'], ['impots-assistanat', 'On s’en fiche des chiffres, les immigrés touchent plus d’aides que les Français', 'immigres-aides']];
    for (const [depart, msg, cible] of cas) {
      const conv = nouvelleConversation(byId(depart));
      const r = repondreConversation(conv, msg, { bibliotheque: lib });
      assert.equal(r.tour.analyse.type, 'deplacement', msg);
      assert.equal(conv.courante, cible, msg);
    }
  });

  test('plusieurs rebondissements successifs, profils différents, sans répétition', () => {
    for (const profil of [{ faits: 'chiffres' }, { debat: 'susceptible' }, { valeurs: ['securite'] }]) {
      for (const mode of ['gagner', 'convaincre']) {
        const conv = nouvelleConversation(byId('etrangers-prisons'), { mode, profil });
        const msgs = ['C’est faux', 'Même si tous ne sont pas étrangers, les étrangers sont surreprésentés dans les prisons.', 'Peu importe les statistiques, il faut tous les renvoyer chez eux.', 'De toute façon les juges les protègent.', 'T’as une source ?', 'Ça suffit', 'Bon, je vais regarder'];
        const vus = new Set();
        for (const m of msgs) {
          const r = repondreConversation(conv, m, { bibliotheque: lib });
          const cle = `${r.tour.intervention.texte}|${r.tour.intervention.preuve?.index}`;
          assert.ok(!vus.has(cle), `répétition (${mode}) : ${m}`);
          vus.add(cle);
        }
        assert.equal(conv.courante, 'criminels-etrangers-proteges-justice');
        assert.equal(conv.terminee, false);
      }
    }
  });
});
