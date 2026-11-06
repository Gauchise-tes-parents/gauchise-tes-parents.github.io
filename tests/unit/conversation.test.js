// Conversation continue : aucune limite artificielle de tours ; seul l'utilisateur termine.
// Mode autonome (moteur de règles local) et mode connecté (service d'IA SIMULÉ).
import { test, describe, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { loadLibrary, LIBRARY_DIR } from '../../server/library.js';
import { extractNumbers } from '../../server/engine/util.js';
import {
  nouvelleConversation, repondreConversation, terminerConversation, basculerSujet, resumeConversation,
  chargeServeur, enregistrerTour, analyserMessage, corrigerHypotheses, CV_TYPES,
} from '../../public/js/conversation.js';
import { silent, testConfig, startServer, routerFetch, jsonResponse, textResponse } from '../helpers.js';

const lib = loadLibrary(LIBRARY_DIR, silent);
const byId = (id) => lib.find((e) => e.id === id);

/** Joue une suite de messages et vérifie les invariants à chaque tour. */
function jouer(ficheId, messages, { mode = 'gagner', profil = {} } = {}) {
  const conv = nouvelleConversation(byId(ficheId), { mode, profil });
  const tours = [];
  for (const m of messages) {
    const [msg, raccourci] = Array.isArray(m) ? m : [m, null];
    const r = repondreConversation(conv, msg, { raccourci, bibliotheque: lib });
    assert.ok(!r.erreur && !r.doublon, `tour refusé : ${msg}`);
    tours.push(r.tour);
  }
  return { conv, tours };
}

/** Invariants : jamais deux fois la même intervention, aucun chiffre ni source hors bibliothèque, conversation ouverte. */
function verifier(conv) {
  const vus = new Set();
  for (const t of conv.tours) {
    const i = t.intervention;
    assert.ok(i.texte && i.texte.length > 10, `tour ${t.n} vide`);
    const cle = `${i.texte}|${i.preuve?.fiche_id}#${i.preuve?.index}`;
    assert.ok(!vus.has(cle), `tour ${t.n} : intervention répétée « ${i.texte.slice(0, 60)} »`);
    vus.add(cle);
    // chiffres : uniquement ceux des fiches de la bibliothèque ou du propos rapporté
    const ref = new Set([...extractNumbers(JSON.stringify(lib)), ...extractNumbers(t.message || '')]);
    const extra = [...extractNumbers(`${i.texte} ${i.question || ''} ${i.strategie}`)].filter((n) => !ref.has(n));
    assert.deepEqual(extra, [], `tour ${t.n} : chiffre inventé`);
    // sources : uniquement des sources consultées de la fiche citée
    if (i.preuve?.source) {
      const f = byId(i.preuve.fiche_id);
      assert.equal(i.preuve.texte, f.faits[i.preuve.index].fait, 'fait modifié');
      assert.ok(f.sources.some((s) => s.url === i.preuve.source.url && s.consultee), 'source inventée ou non consultée');
    }
  }
  assert.equal(conv.terminee, false, 'la conversation ne doit jamais se terminer seule');
}

describe('conversation continue (moteur local)', () => {
  test('1. trois échanges', () => {
    const { conv } = jouer('impots-assistanat', ['N’importe quoi, tout part dans les aides', 'T’as une source ?', 'Ok, c’est vrai.']);
    assert.equal(conv.tours.length, 3);
    verifier(conv);
  });

  test('2. cinq échanges', () => {
    const { conv } = jouer('rsa-smic', ['C’est faux', 'Prouve-le', 'Tes chiffres sont bidons', 'Bon, je ne sais pas', 'Pourquoi pas'], { mode: 'convaincre' });
    assert.equal(conv.tours.length, 5);
    verifier(conv);
  });

  test('3. dix échanges, puis encore : aucune limite de tours', () => {
    const msgs = ['N’importe quoi', 'Source ?', 'Les stats de l’Insee sont truquées', 'Pas d’accord', 'Ouais', 'Ça suffit', 'Espèce de gauchiste', 'Je ne comprends pas', 'Je ne sais pas', 'Bon, je vais regarder', 'Non mais quand même', 'Et alors ?', 'D’où tu sors ça', 'Bof', 'Pff'];
    const { conv } = jouer('impots-assistanat', msgs);
    assert.equal(conv.tours.length, 15);
    verifier(conv);
    const r = repondreConversation(conv, 'Et les fraudeurs alors ?', { bibliotheque: lib });
    assert.ok(r.tour, 'un seizième tour est accepté');
  });

  test('4. l’interlocuteur change plusieurs fois d’argument', () => {
    const { conv, tours } = jouer('impots-assistanat', ['Et l’immigration alors, ça coûte une fortune', 'De toute façon les chômeurs ne veulent pas travailler', 'Et la délinquance augmente partout']);
    assert.ok(tours.every((t) => t.analyse.type === 'sujet'), tours.map((t) => t.analyse.type).join());
    const cibles = tours.map((t) => t.analyse.fiche_sujet);
    assert.equal(lib.find((f) => f.id === cibles[0]).volet, 'immigration');
    assert.deepEqual(cibles.slice(1), ['chomeurs-travailler', 'delinquance-partout']);
    assert.ok(tours.every((t) => t.intervention.options.some((o) => o.action === 'basculer') && t.intervention.options.some((o) => o.action === 'rester')));
    basculerSujet(conv, 'chomeurs-travailler');
    const r = repondreConversation(conv, 'T’as une source ?', { bibliotheque: lib });
    assert.equal(r.tour.intervention.preuve.fiche_id, 'chomeurs-travailler', 'la suite porte sur le nouveau sujet');
    assert.equal(conv.sujet.fiche_id, 'impots-assistanat', 'le sujet initial est conservé');
    verifier(conv);
  });

  test('5. plusieurs demandes successives de sources : jamais la même, jamais inventée', () => {
    const { conv, tours } = jouer('impots-assistanat', ['T’as une source ?', 'Une autre source ?', 'Et une troisième ?', 'Encore une ?', 'Encore ?']);
    const urls = tours.map((t) => t.intervention.preuve?.source?.url).filter(Boolean);
    assert.equal(new Set(urls).size, urls.length, 'chaque source donnée une seule fois');
    assert.ok(tours.every((t) => t.analyse.type === 'source'), tours.map((t) => t.analyse.type).join());
    assert.ok(tours.slice(-1)[0].intervention.epuise, 'quand il n’y a plus de source, le moteur le dit');
    verifier(conv);
  });

  test('6. reconnaît un point, puis en conteste un autre', () => {
    const { conv, tours } = jouer('impots-assistanat', ['N’importe quoi', 'Ok, tu as raison sur ce point', 'Mais tes chiffres sur les minima sociaux sont faux']);
    assert.equal(tours[1].analyse.type, 'reconnaissance');
    assert.equal(tours[2].analyse.type, 'chiffre');
    assert.equal(conv.memoire.accords.length, 1);
    assert.ok(!tours[2].intervention.texte.includes(tours[0].intervention.preuve.texte), 'le point accepté n’est pas répété');
    const dernierTexte = tours[2].intervention.preuve.texte;
    assert.match(dernierTexte, /minima sociaux/);
    verifier(conv);
  });

  test('8. conversation longue : le résumé évolue et reste borné', () => {
    const conv = nouvelleConversation(byId('delinquance-partout'), { profil: { autorite: 'mefiance' } });
    const resumes = [];
    const msgs = ['Faux', 'Source ?', 'Truqué', 'Tu as raison', 'Mais les causes, c’est l’immigration', 'Ouais', 'Ça suffit', 'Je vais regarder'];
    for (let k = 0; k < 40; k++) {
      repondreConversation(conv, `${msgs[k % msgs.length]} (${k})`, { bibliotheque: lib });
      resumes.push(conv.resume);
    }
    assert.equal(conv.tours.length, 40);
    assert.ok(new Set(resumes).size === resumes.length, 'résumé actualisé à chaque tour');
    assert.ok(resumes.every((r) => r.length <= 2500), 'résumé borné');
    assert.match(conv.resume, /Sujet initial : « La délinquance augmente partout/);
    assert.match(conv.resume, /Hypothèses .* \(non vérifiées\) : se méfie des institutions/);
    assert.match(conv.resume, /Échanges : 40/);
    const charge = chargeServeur(conv, 'nouveau message');
    assert.ok(JSON.stringify(charge).length < 9000, 'charge envoyée au serveur bornée');
    assert.equal(charge.derniers.length, 6);
  });

  test('9. interruption volontaire puis reprise : l’état sérialisé suffit', () => {
    const { conv } = jouer('rsa-smic', ['Faux', 'Source ?']);
    const copie = JSON.parse(JSON.stringify(conv)); // ce que l'interface garde dans l'onglet
    const r = repondreConversation(copie, 'Bon, je ne sais pas', { bibliotheque: lib });
    assert.equal(r.tour.n, 3);
    assert.equal(copie.sujet.fiche_id, 'rsa-smic');
    verifier(copie);
  });

  test('10. « Conversation terminée » : bilan fidèle à l’historique, puis nouvelle conversation séparée', () => {
    const { conv } = jouer('impots-assistanat', ['N’importe quoi', 'T’as une source ?', 'c’est vrai que les retraites pèsent lourd, mais les étrangers profitent des aides', 'Bof']);
    const b = terminerConversation(conv, { bibliotheque: lib });
    assert.equal(conv.terminee, true);
    assert.equal(b.nb_echanges, 4);
    assert.deepEqual(b.arguments.map((a) => a.texte), conv.memoire.arguments.map((a) => a.texte));
    assert.deepEqual(b.sources.map((s) => s.url), conv.memoire.sources.map((s) => s.url));
    assert.ok(b.accords.some((a) => a.includes('retraites pèsent lourd')), 'accord rapporté');
    assert.ok(b.desaccords.some((a) => a.includes('étrangers profitent')), 'désaccord rapporté');
    assert.match(b.message, /Bravo/);
    assert.match(b.message, /sources/);
    assert.doesNotMatch(b.message, /a changé d’avis\b(?!.*Sans)/);
    assert.ok(repondreConversation(conv, 'encore', { bibliotheque: lib }).erreur, 'une conversation terminée n’accepte plus de tour');
    const nouvelle = nouvelleConversation(byId('impots-assistanat'));
    assert.notEqual(nouvelle.id, conv.id);
    assert.equal(nouvelle.tours.length, 0);
    assert.equal(nouvelle.memoire.arguments.length, 0);
    assert.equal(nouvelle.memoire.sources.length, 0);
  });

  test('bilan personnalisé : discussion tendue, désaccord, aucune fausse conversion', () => {
    const tendu = jouer('impots-assistanat', ['Espèce de gauchiste', 'Ça suffit', 'Tu me saoules']).conv;
    const b1 = terminerConversation(tendu, { bibliotheque: lib });
    assert.match(b1.message, /tendue/);
    assert.match(b1.message, /poser des limites/);
    const desaccord = jouer('rsa-smic', ['Faux', 'Pas d’accord']).conv;
    const b2 = terminerConversation(desaccord, { bibliotheque: lib });
    assert.match(b2.message, /restés en désaccord/);
    assert.doesNotMatch(b2.message, /reconnu|ouverture/);
    const vide = nouvelleConversation(byId('rsa-smic'));
    assert.match(terminerConversation(vide, { bibliotheque: lib }).message, /pas encore vraiment commencé/);
  });

  test('analyse : les types attendus sont reconnus', () => {
    const conv = nouvelleConversation(byId('impots-assistanat'));
    const cas = {
      'Tu as une source ?': 'source', 'Les statistiques sont truquées': 'chiffre', 'Espèce de bobo gauchiste': 'provocation',
      'Ça suffit, tu me saoules': 'braque', 'Je ne comprends pas ce que tu veux dire': 'incomprehension', 'Je ne sais pas, peut-être': 'hesitation',
      'Je n’y avais pas pensé, ça se tient': 'evolution', 'ouais': 'essoufflement', 'Bon, on en reste là': 'conclusion',
      'Tu as raison': 'reconnaissance', 'D’accord sur le constat, mais pas sur les causes': 'partiel_causes', 'Ok il y a un problème mais ta solution ne marchera jamais': 'partiel_solution',
      'Et l’immigration alors ?': 'sujet', 'N’importe quoi': 'desaccord',
    };
    for (const [m, attendu] of Object.entries(cas)) assert.equal(analyserMessage(conv, m, { bibliotheque: lib }).type, attendu, m);
    assert.equal(analyserMessage(conv, '', { raccourci: 'aide', bibliotheque: lib }).type, 'aide');
    for (const t of Object.keys(cas)) assert.ok(CV_TYPES[cas[t]]);
  });

  test('protection contre les boucles : un message identique envoyé deux fois demande confirmation', () => {
    const conv = nouvelleConversation(byId('rsa-smic'));
    repondreConversation(conv, 'Faux', { bibliotheque: lib });
    const r = repondreConversation(conv, 'Faux', { bibliotheque: lib });
    assert.ok(r.doublon);
    assert.equal(conv.tours.length, 1);
    assert.equal(repondreConversation(conv, 'Faux', { bibliotheque: lib, force: true }).tour.n, 2);
  });

  test('hypothèses et faits ne sont jamais confondus ; correction tracée', () => {
    const conv = nouvelleConversation(byId('rsa-smic'), { profil: { debat: 'susceptible' } });
    repondreConversation(conv, 'Les gens au RSA ne font rien', { bibliotheque: lib });
    corrigerHypotheses(conv, { debat: 'calme' });
    assert.equal(conv.memoire.corrections.length, 1);
    assert.match(conv.resume, /\(non vérifiées\) : calme/);
    assert.match(conv.resume, /Derniers propos rapportés par l’utilisateur : « Les gens au RSA ne font rien »/);
    for (const t of conv.tours) assert.doesNotMatch(t.intervention.texte, /(est|semble) susceptible/);
  });

  test('le mode choisi est respecté à chaque tour', () => {
    const g = jouer('rsa-smic', ['Espèce de gauchiste'], { mode: 'gagner' }).tours[0].intervention.texte;
    const c = jouer('rsa-smic', ['Espèce de gauchiste'], { mode: 'convaincre' }).tours[0].intervention.texte;
    assert.match(g, /ton|étiquettes|traiter/);
    assert.match(c, /agace|fâche|étiquettes/);
    assert.notEqual(g, c);
  });
});

describe('conversation continue (mode connecté, service d’IA simulé)', () => {
  const TOUR = { type: 'source', lecture: 'Il demande une source.', texte: 'Les minima sociaux pèsent 31,6 Md€ selon la DREES.', strategie: 'Donner la source.', question: 'Quelle source accepterais-tu ?', faits_utilises: [3], objection_traitee: null, conclusion_possible: false };
  const fiche = byId('impots-assistanat');
  const corps = (conv, msg) => ({ ...chargeServeur(conv, msg), interlocuteur: {}, mode: 'gagner' });
  let s;
  let f;
  before(async () => {
    f = routerFetch({ conversation: [{ status: 529 }, jsonResponse(TOUR), jsonResponse({ ...TOUR, texte: 'Selon une étude, 87 % des gens trichent.' }), jsonResponse(TOUR)] });
    s = await startServer(testConfig({ liveMode: true, apiKey: 'sk-test-secret', perIpConversationLimit: 6 }), { fetchImpl: f });
  });
  after(() => s.close());

  test('7. erreur temporaire, puis reprise sans perdre le fil', async () => {
    const conv = nouvelleConversation(fiche);
    const r1 = await s.post('/api/conversation', corps(conv, 'T’as une source ?'));
    assert.equal(r1.status, 503);
    const e = await r1.json();
    assert.match(e.erreur, /temporairement indisponible/);
    assert.equal(e.relancer, true);
    assert.equal(conv.tours.length, 0, 'aucun tour simulé en cas d’erreur');
    const r2 = await s.post('/api/conversation', corps(conv, 'T’as une source ?'));
    assert.equal(r2.status, 200);
    const { intervention } = await r2.json();
    enregistrerTour(conv, { message: 'T’as une source ?', analyse: { type: intervention.type }, intervention, origine: 'connecte' });
    assert.equal(conv.tours.length, 1);
    assert.equal(intervention.preuve.texte, fiche.faits[3].fait, 'la preuve vient de la bibliothèque, pas du modèle');
    assert.equal(intervention.preuve.source.url, fiche.sources[fiche.faits[3].source].url);
    // le modèle a reçu le résumé et les faits, pas tout l'historique
    const envoye = f.calls.filter((c) => c.kind === 'conversation').at(-1).body.messages[0].content;
    assert.match(envoye, /<resume>/);
    assert.match(envoye, /F3 :/);
  });

  test('un chiffre absent des sources est signalé, jamais présenté comme vérifié', async () => {
    const conv = nouvelleConversation(fiche);
    const r = await (await s.post('/api/conversation', corps(conv, 'Ah bon ?'))).json();
    assert.deepEqual(r.intervention.chiffres_non_sources, ['87']);
    assert.match(r.intervention.avertissement, /absent des sources vérifiées/);
  });

  test('limites techniques annoncées clairement (taille, fréquence), sans limite de tours', async () => {
    const conv = nouvelleConversation(fiche);
    const trop = await s.post('/api/conversation', { ...corps(conv, ''), message: 'x'.repeat(1001) });
    assert.equal(trop.status, 400);
    assert.match((await trop.json()).erreur, /trop long/);
    const vide = await s.post('/api/conversation', { ...corps(conv, ''), raccourci: null });
    assert.equal(vide.status, 400);
    let dernier;
    for (let k = 0; k < 6; k++) dernier = await s.post('/api/conversation', corps(conv, `message ${k}`));
    assert.equal(dernier.status, 429);
    assert.match((await dernier.json()).erreur, /Trop de demandes/);
    assert.ok(dernier.headers.get('retry-after'));
  });

  test('budget atteint : message clair, aucune réponse simulée', async () => {
    const s2 = await startServer(testConfig({ liveMode: true, apiKey: 'sk-test-secret', dailyBudgetUsd: 0.001, estimateConversationUsd: 0.02 }), { fetchImpl: routerFetch({ conversation: jsonResponse(TOUR) }) });
    try {
      const r = await s2.post('/api/conversation', corps(nouvelleConversation(fiche), 'Source ?'));
      assert.equal(r.status, 503);
      const d = await r.json();
      assert.equal(d.mode, 'quota');
      assert.match(d.erreur, /budget/);
    } finally { await s2.close(); }
  });

  test('sans clé API, la route le dit au lieu de simuler', async () => {
    const s3 = await startServer(testConfig({ liveMode: false, apiKey: '' }));
    try {
      const r = await s3.post('/api/conversation', corps(nouvelleConversation(fiche), 'Source ?'));
      assert.equal(r.status, 503);
      assert.equal((await r.json()).mode, 'demo');
    } finally { await s3.close(); }
  });

  test('réponse illisible du modèle : erreur explicite et relançable', async () => {
    const s4 = await startServer(testConfig({ liveMode: true, apiKey: 'sk-test-secret' }), { fetchImpl: routerFetch({ conversation: textResponse('pas de json') }) });
    try {
      const r = await s4.post('/api/conversation', corps(nouvelleConversation(fiche), 'Source ?'));
      assert.equal(r.status, 502);
      assert.equal((await r.json()).relancer, true);
    } finally { await s4.close(); }
  });
});

test('résumé : sujet, objectif et hypothèses toujours présents', () => {
  const conv = nouvelleConversation(byId('rsa-smic'), { mode: 'convaincre' });
  assert.match(resumeConversation(conv), /Public : personne indécise/);
});
