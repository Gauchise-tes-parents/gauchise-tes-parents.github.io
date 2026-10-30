// Tests de bout en bout dans un vrai navigateur (Chromium via Playwright), formats téléphone d'abord.
// Playwright n'est pas une dépendance du projet : s'il est absent, ces tests sont ignorés.
// Le mode « réel » utilise un service d'IA SIMULÉ : il valide l'interface, pas la recherche réelle.
import { test, describe, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { readdirSync, readFileSync } from 'node:fs';
import { testConfig, startServer, routerFetch, defaultRoutes, researchResponse, DOSSIER_JSON, jsonResponse } from '../helpers.js';

const LIB_DIR = new URL('../../data/library/', import.meta.url);
const FICHES = readdirSync(LIB_DIR).filter((f) => f.endsWith('.json')).map((f) => JSON.parse(readFileSync(new URL(f, LIB_DIR), 'utf8')));

let chromium = null;
try {
  ({ chromium } = await import('playwright'));
} catch {
  for (const p of [process.env.PLAYWRIGHT_PATH, '/opt/npm-tools/node_modules/playwright/index.mjs'].filter(Boolean)) {
    try { ({ chromium } = await import(p)); break; } catch { /* suivant */ }
  }
}
const skip = chromium ? false : 'Playwright non installé';

const PHONE = { width: 390, height: 844, isMobile: true, hasTouch: true };
const SMALL = [
  { name: 'iPhone SE (320)', width: 320, height: 568, isMobile: true, hasTouch: true },
  { name: 'Android (360)', width: 360, height: 740, isMobile: true, hasTouch: true },
  { name: 'Android grand (412)', width: 412, height: 915, isMobile: true, hasTouch: true },
];
const DESKTOP = { width: 1280, height: 860 };

async function newPage(browser, vp, errors, { connecte = false } = {}) {
  const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, isMobile: vp.isMobile, hasTouch: vp.hasTouch, reducedMotion: 'reduce', serviceWorkers: 'block' });
  // Réglage stocké sur l'appareil : mode connecté pour les tests du moteur ; mise à jour auto de la base désactivée.
  await ctx.addInitScript((c) => { if (!localStorage.getItem('gtp-donnees-v1')) localStorage.setItem('gtp-donnees-v1', JSON.stringify({ reglages: { mode: c ? 'connecte' : 'autonome', majAuto: false } })); }, connecte);
  await ctx.grantPermissions(['clipboard-read', 'clipboard-write']).catch(() => {});
  const page = await ctx.newPage();
  page.on('pageerror', (e) => errors.push(e.message));
  page.on('console', (m) => { if (m.type() === 'error' && !/Failed to load resource/.test(m.text())) errors.push(m.text()); });
  return page;
}
const overflow = (page) => page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
const tab = (page, name) => page.locator('[data-tabbar]').getByRole('link', { name, exact: true });

describe('interface — mode démonstration', { skip }, () => {
  let s; let browser; const errors = [];
  before(async () => { s = await startServer(testConfig({ liveMode: false, apiKey: '' })); browser = await chromium.launch(); });
  after(async () => { await browser?.close(); await s?.close(); });

  test('accueil sur téléphone : deux modes, barre d’onglets en bas, navigation', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/`);
    await page.getByRole('heading', { level: 1, name: /ENVIE DE GAUCHISER/ }).waitFor();
    assert.ok(await page.getByText('GAGNER LE DÉBAT', { exact: true }).isVisible());
    assert.ok(await page.getByText('CONVAINCRE AVEC EMPATHIE', { exact: true }).isVisible());
    assert.ok(await page.getByRole('link', { name: 'Préparer ma riposte' }).isVisible());
    assert.ok(await page.getByRole('link', { name: 'Préparer le dialogue' }).isVisible());
    assert.equal(await page.locator('#mode-pill').textContent(), 'Autonome');
    assert.equal(await page.locator('#mode-banner').count(), 0, 'plus de bandeau d’erreur serveur');
    // barre d'onglets accessible au pouce : collée en bas de l'écran
    const box = await page.locator('[data-tabbar]').boundingBox();
    assert.ok(box.y + box.height >= PHONE.height - 2 && box.y > PHONE.height - 100, `barre à y=${box.y}`);
    assert.equal(await page.locator('[data-tabbar] a').count(), 4);
    assert.ok((await overflow(page)) <= 1);
    await tab(page, 'Thématiques').click();
    await page.getByRole('heading', { name: 'Thématiques', level: 1 }).waitFor();
    assert.equal(await tab(page, 'Thématiques').getAttribute('aria-current'), 'page');
    await tab(page, 'Bibliothèque').click();
    await page.getByRole('heading', { name: 'Bibliothèque', level: 1 }).waitFor();
    await tab(page, 'Débat').click();
    await page.getByRole('heading', { name: 'Quel est ton objectif ?' }).waitFor();
    await tab(page, 'Accueil').click();
    await page.getByRole('heading', { level: 1, name: /ENVIE DE GAUCHISER/ }).waitFor();
    await page.getByRole('link', { name: 'À propos', exact: true }).first().click();
    await page.getByRole('heading', { name: 'Notre ligne éditoriale' }).waitFor();
    await page.close();
  });

  for (const vp of SMALL) {
    test(`petit écran ${vp.name} : aucun débordement horizontal`, async () => {
      const page = await newPage(browser, vp, errors);
      for (const route of ['/', '/debat', '/express', '/thematiques', '/thematiques/politique', '/bibliotheque', '/bibliotheque/delinquance-partout', '/a-propos']) {
        await page.goto(`${s.base}/#${route}`);
        await page.waitForTimeout(150);
        if (route.startsWith('/bibliotheque/')) await page.locator('.verdict-card').waitFor();
        const o = await overflow(page);
        assert.ok(o <= 1, `${route} déborde de ${o}px`);
      }
      // les boutons principaux sont assez grands pour le doigt
      await page.goto(`${s.base}/#/`);
      const h = (await page.getByRole('link', { name: 'Préparer ma riposte' }).boundingBox()).height;
      assert.ok(h >= 44, `bouton de ${h}px`);
      await page.close();
    });
  }

  test('ordinateur : la navigation passe dans l’en-tête', async () => {
    const page = await newPage(browser, DESKTOP, errors);
    await page.goto(`${s.base}/#/`);
    await page.locator('.mode-card').first().waitFor();
    const box = await page.locator('[data-tabbar]').boundingBox();
    assert.ok(box.y < 80);
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('liens Tipeee : URL exacte, nouvel onglet, sur l’accueil, le pied de page et « À propos »', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/`);
    await page.locator('[data-tipeee]').first().waitFor();
    const links = await page.locator('[data-tipeee]').evaluateAll((els) => els.map((a) => [a.getAttribute('href'), a.target, a.rel]));
    assert.equal(links.length, 2);
    for (const [href, target, rel] of links) {
      assert.equal(href, 'https://fr.tipeee.com/martyducanda/');
      assert.equal(target, '_blank');
      assert.match(rel, /noopener/);
    }
    await page.goto(`${s.base}/#/a-propos`);
    await page.getByRole('heading', { name: 'Notre ligne éditoriale' }).waitFor();
    assert.equal(await page.locator('#app [data-tipeee]').count(), 1);
    await page.close();
  });

  test('parcours : mode, volet, sous-thème, saisie, retour, changement de mode, résultat démo', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/`);
    await page.getByRole('link', { name: 'Préparer ma riposte' }).click();
    // le mode est déjà choisi : on arrive directement au sujet
    await page.getByRole('heading', { name: 'De quoi ça parle ?' }).waitFor();
    assert.equal(await page.locator('[data-pick-volet]').count(), 10);
    await page.getByRole('button', { name: 'Continuer' }).click();
    assert.match(await page.locator('#wizard-error').textContent(), /Choisis un volet/);
    await page.getByRole('radio', { name: /Assistanat, travail et aides sociales/ }).click();
    await page.getByRole('button', { name: 'Chômage', exact: true }).click();
    assert.equal(await page.getByRole('button', { name: 'Chômage', exact: true }).getAttribute('aria-pressed'), 'true');
    await page.getByRole('button', { name: 'Continuer' }).click();
    await page.getByRole('heading', { name: /qu’est-ce qu’il a encore raconté/ }).waitFor();
    assert.match(await page.locator('.step-help').textContent(), /Gagner le débat · Aides sociales · Chômage/);
    await page.getByRole('button', { name: /Les chômeurs ne veulent pas travailler/ }).click();
    assert.equal(await page.locator('#affirmation').inputValue(), 'Les chômeurs ne veulent pas travailler.');
    // retour arrière puis changement de mode : la saisie est conservée
    await page.getByRole('button', { name: /Revenir à l’étape 1/ }).click();
    await page.getByRole('radio', { name: /CONVAINCRE SANS BRAQUER/ }).click();
    await page.getByRole('heading', { name: 'De quoi ça parle ?' }).waitFor();
    assert.equal(await page.getByRole('radio', { name: /Assistanat/ }).getAttribute('aria-checked'), 'true');
    await page.getByRole('button', { name: 'Continuer' }).click();
    assert.equal(await page.locator('#affirmation').inputValue(), 'Les chômeurs ne veulent pas travailler.');
    assert.match(await page.locator('.step-help').textContent(), /Convaincre sans braquer/);
    await page.getByText('Décrire la personne en face').click();
    assert.equal(await page.getByRole('button', { name: 'Je ne connais pas assez cette personne' }).getAttribute('aria-pressed'), 'true');
    await page.getByRole('button', { name: 'Susceptible', exact: true }).click();
    await page.getByRole('button', { name: 'Repas de famille', exact: true }).click();
    assert.equal(await page.getByRole('button', { name: 'Je ne connais pas assez cette personne' }).getAttribute('aria-pressed'), 'false');
    await page.getByRole('button', { name: 'OK, SORS LES SOURCES !' }).click();
    // mode autonome : argumentaire composé localement, sans réseau ni IA
    await page.getByRole('heading', { name: 'L’argument d’en face, version solide' }).waitFor();
    assert.ok(await page.getByText('Composé à partir de la bibliothèque locale').isVisible());
    assert.equal(await page.getByRole('tab', { name: 'CONVAINCRE AVEC EMPATHIE' }).getAttribute('aria-selected'), 'true', 'le mode choisi est ouvert');
    // v9 : la réponse et les faits d'abord, puis les questions ouvertes pour les introduire (profil susceptible)
    const titresC = await page.locator('#strat-panel-convaincre h3.sub-title').allTextContents();
    assert.equal(titresC[0], 'Ce que tu peux répondre');
    assert.ok(titresC.includes('Les questions pour comprendre son point de vue'), 'profil susceptible : questions ouvertes');
    assert.ok(await page.locator('a[href="#/bibliotheque/chomeurs-travailler"]').first().isVisible());
    // les choix survivent à un rechargement de la page (stockage de session)
    await page.goto(`${s.base}/#/debat`);
    await page.reload();
    await page.locator('#affirmation').waitFor();
    assert.equal(await page.locator('#affirmation').inputValue(), 'Les chômeurs ne veulent pas travailler.');
    await page.close();
  });

  test('thématiques : 10 volets, sous-thèmes, départ d’un débat pré-rempli', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/thematiques`);
    await page.locator('.volet-link').first().waitFor();
    assert.equal(await page.locator('.volet-link').count(), 10);
    await page.getByRole('link', { name: /Sécurité, justice et libertés/ }).click();
    await page.getByRole('heading', { name: /Sécurité, justice et libertés/ }).waitFor();
    assert.equal(await page.locator('.sub-item').count(), 13);
    await page.locator('#theme-fiches .fiche-card').first().waitFor();
    await page.locator('.sub-item', { hasText: 'Récidive' }).click();
    await page.getByRole('heading', { name: 'Quel est ton objectif ?' }).waitFor();
    await page.getByRole('radio', { name: /GAGNER LE DÉBAT/ }).click();
    await page.getByRole('heading', { name: 'De quoi ça parle ?' }).waitFor();
    assert.equal(await page.getByRole('button', { name: 'Récidive', exact: true }).getAttribute('aria-pressed'), 'true');
    await page.close();
  });

  test('bibliothèque : filtre, recherche, fiche à actualiser, sources cliquables, copie', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/bibliotheque`);
    await page.locator('.fiche-card').first().waitFor();
    assert.equal(await page.locator('.fiche-card').count(), FICHES.length);
    assert.equal(await page.locator('.fresh-badge.is-stale').count(), 1);
    const nSecu = FICHES.filter((x) => x.volet === 'securite').length;
    await page.locator('#lib-volet').selectOption('securite');
    await page.getByRole('button', { name: 'Rechercher' }).click();
    await page.waitForFunction((n) => document.querySelectorAll('.fiche-card').length === n, nSecu);
    // filtres rubrique et fiabilité
    await page.locator('#lib-volet').selectOption('');
    await page.locator('#lib-rubrique').selectOption('melenchon-lfi');
    await page.getByRole('button', { name: 'Rechercher' }).click();
    const nMel = FICHES.filter((x) => x.rubriques.includes('melenchon-lfi')).length;
    await page.waitForFunction((n) => document.querySelectorAll('.fiche-card').length === n, nMel);
    await page.locator('#lib-rubrique').selectOption('');
    await page.locator('#lib-fiab').selectOption('debat');
    await page.getByRole('button', { name: 'Rechercher' }).click();
    const nDeb = FICHES.filter((x) => x.fiabilite === 'debat').length;
    await page.waitForFunction((n) => document.querySelectorAll('.fiche-card').length === n, nDeb);
    await page.locator('#lib-fiab').selectOption('');
    await page.locator('#lib-volet').selectOption('');
    await page.locator('#lib-q').fill('zzzz introuvable');
    await page.getByRole('button', { name: 'Rechercher' }).click();
    await page.getByText('Aucune fiche ne correspond').waitFor();
    await page.goto(`${s.base}/#/bibliotheque/chomeurs-travailler`);
    await page.getByText('Fiche à actualiser.').waitFor();
    await page.goto(`${s.base}/#/bibliotheque/rsa-smic`);
    await page.getByRole('heading', { name: /Contredit par les données consultées/ }).waitFor();
    await page.getByRole('tab', { name: 'Sources et preuves' }).click();
    const links = await page.locator('.source-title a').evaluateAll((els) => els.map((a) => [a.href, a.target]));
    assert.equal(links.length, 3);
    for (const [href, target] of links) { assert.match(href, /^https:\/\//); assert.equal(target, '_blank'); }
    await page.getByText('Voir les données utilisées').first().click();
    assert.ok(await page.locator('.source-passage').first().isVisible());
    await page.getByRole('tab', { name: 'Réponse en 15 secondes' }).click();
    await page.getByRole('button', { name: 'Copier la réponse' }).click();
    await page.getByText('Réplique copiée !').waitFor();
    assert.ok(await page.getByRole('link', { name: 'Composer mon argumentaire' }).isVisible());
    assert.equal(await page.getByRole('button', { name: 'Préparer ma riposte' }).count(), 0, 'pas de bouton IA en mode autonome');
    // anciennes adresses redirigées
    await page.goto(`${s.base}/#/idees-recues/rsa-smic`);
    await page.getByRole('heading', { name: /Contredit/ }).waitFor();
    await page.close();
  });

  test('réponse express en démo depuis l’accueil', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/`);
    await page.locator('#express-mini-text').fill('La délinquance augmente partout.');
    await page.getByRole('button', { name: 'Sortir une réplique' }).click();
    await page.locator('#replique-text').waitFor();
    assert.ok(await page.locator('a[href="#/bibliotheque/delinquance-partout"]').first().isVisible());
    await page.close();
  });

  test('fiche : sept onglets, structure en cinq parties, clavier, sans débordement', async () => {
    const page = await newPage(browser, { ...PHONE, width: 360, height: 740 }, errors);
    await page.goto(`${s.base}/#/bibliotheque/melenchon-crie`);
    await page.getByRole('heading', { name: 'Ce qui est reproché' }).waitFor();
    assert.equal(await page.getByRole('tab').count(), 7);
    for (const name of ['Réponse en 15 secondes', 'Argumentaire en 1 minute', 'Développement en 3 minutes', 'Sources et preuves', 'Contre-arguments', 'Contexte historique', 'Réponse avec empathie']) {
      await page.getByRole('tab', { name }).click();
      assert.equal(await page.getByRole('tab', { name }).getAttribute('aria-selected'), 'true');
      assert.equal(await page.locator('.fiche-panel:not([hidden])').count(), 1);
    }
    await page.getByRole('tab', { name: 'Sources et preuves' }).click();
    assert.ok(await page.getByText('Citations vérifiées').isVisible());
    await page.getByRole('tab', { name: 'Contre-arguments' }).click();
    assert.ok(await page.getByText('Ce qu’il faut reconnaître').isVisible());
    // clavier : flèche droite
    await page.getByRole('tab', { name: 'Contre-arguments' }).focus();
    await page.keyboard.press('ArrowRight');
    assert.equal(await page.getByRole('tab', { name: 'Contexte historique' }).getAttribute('aria-selected'), 'true');
    // les puces des cinq parties ouvrent le bon onglet
    await page.getByRole('button', { name: '4. Objections légitimes' }).click();
    assert.equal(await page.getByRole('tab', { name: 'Contre-arguments' }).getAttribute('aria-selected'), 'true');
    assert.ok((await overflow(page)) <= 1);
    // fiche sans verdict binaire
    await page.goto(`${s.base}/#/bibliotheque/lfi-antisemite`);
    await page.getByRole('heading', { name: 'Pas de verdict binaire' }).waitFor();
    assert.ok(await page.getByText('Débat historiographique ou politique').first().isVisible());
    await page.close();
  });

  test('thématiques : cinq rubriques et leurs fiches', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/thematiques`);
    await page.locator('.rub-card').first().waitFor();
    assert.equal(await page.locator('.rub-card').count(), 5);
    await page.locator('.rub-card--melenchon-lfi').click();
    await page.locator('#rubrique-fiches .fiche-card').first().waitFor();
    assert.equal(await page.locator('#rubrique-fiches .fiche-card').count(), FICHES.filter((x) => x.rubriques.includes('melenchon-lfi')).length);
    assert.equal(await tab(page, 'Thématiques').getAttribute('aria-current'), 'page');
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('argumentaire hors ligne : questionnaire, deux stratégies, consignes justifiées, retours, enregistrement, suppression', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/express`);
    await page.locator('#express-text').fill('Mélenchon crie tout le temps');
    await page.getByRole('button', { name: 'Sortir une réplique' }).click();
    await page.getByRole('heading', { name: 'L’argument d’en face, version solide' }).waitFor();
    assert.equal(await page.getByRole('tab').count(), 2);
    assert.equal(await page.locator('.source-card').count(), 0, 'aucune recherche simulée');
    // profil « compétitif + méfiant » : une seule preuve, charge de la preuve, méthode
    await page.locator('#compo-profil > summary').click();
    await page.locator('[data-ctx="compo"][data-val="competitif"]').click();
    await page.locator('[data-ctx="compo"][data-val="mefiance"]').click();
    assert.ok(await page.locator('#strat-panel-gagner .big-q', { hasText: 'source et sa date' }).count(), 'conclusion : renvoyer la charge de la preuve');
    assert.equal(await page.locator('#strat-panel-gagner .preuve').count(), 1);
    assert.ok(await page.locator('#strat-panel-gagner .preuve-methode').first().isVisible());
    await page.getByText(/Pourquoi cette stratégie/).click();
    assert.ok(await page.locator('.regles a[href="#/bibliotheque/sci-desinformation-confiance"]').first().isVisible());
    // stratégie empathique
    await page.getByRole('tab', { name: 'CONVAINCRE AVEC EMPATHIE' }).click();
    assert.ok(await page.getByText('Ce qu’il faut reconnaître').first().isVisible());
    // adaptation progressive
    await page.locator('[data-conv-raccourci="braque"]').click();
    await page.locator('#conv-fil .conv-tour').first().waitFor();
    await page.locator('[data-conv-raccourci="source"]').click();
    assert.equal(await page.locator('#conv-fil .conv-tour').count(), 2);
    assert.ok(await page.getByText(/lecture approximative/).first().isVisible());
    // enregistrement local, puis suppression
    await page.getByRole('button', { name: 'Enregistrer cet argumentaire' }).click();
    await page.getByText(/Argumentaire enregistré sur cet appareil/).waitFor();
    await page.goto(`${s.base}/#/mes-donnees`);
    assert.ok(await page.getByRole('link', { name: /Mélenchon crie/ }).isVisible());
    await page.getByRole('button', { name: 'Supprimer' }).first().click();
    await page.getByText('Aucun argumentaire enregistré.').waitFor();
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('moteur v5 : questionnaire progressif, hypothèses corrigées, arguments déjà avancés, approches, retour libre', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/express`);
    await page.locator('#express-text').fill('Les impôts servent à payer les assistés');
    await page.getByRole('button', { name: 'Sortir une réplique' }).click();
    await page.getByRole('heading', { name: 'L’argument d’en face, version solide' }).waitFor();
    // questionnaire progressif : questions essentielles visibles, les autres repliées, suggestion de la question la plus utile
    await page.locator('#compo-profil > summary').click();
    assert.ok(await page.locator('#compo-profil .interloc-suggestion').isVisible());
    assert.equal(await page.locator('#compo-profil details[data-more]').count(), 1);
    assert.equal(await page.locator('#compo-profil details[data-more]').getAttribute('open'), null);
    // corriger une hypothèse change réellement la stratégie affichée
    const avant = await page.locator('#strat-panel-gagner .plan-resume').textContent();
    await page.locator('[data-ctx="compo"][data-val="susceptible"]').click();
    const apres = await page.locator('#strat-panel-gagner .plan-resume').textContent();
    assert.notEqual(avant, apres);
    // v9 : la reformulation est réservée au mode empathique ; « gagner » garde une entrée par le fond
    assert.match(await page.locator('#strat-panel-convaincre .plan-resume').textContent(), /reformuler/);
    assert.doesNotMatch(apres, /reformuler|question ouverte/);
    // arguments déjà avancés : la preuve marquée n'est plus proposée
    const premier = await page.locator('#strat-panel-gagner .preuve .preuve-texte, #strat-panel-gagner .preuve p').first().textContent();
    await page.locator('#compo-deja > summary').click();
    await page.locator('[data-deja="1"]').click();
    assert.equal(await page.locator('[data-deja="1"]').getAttribute('aria-pressed'), 'true');
    const textesApres = await page.locator('#strat-panel-gagner .preuve').allTextContents();
    const fait1 = await page.evaluate(async () => (await (await fetch('kb/base.json')).json()).fiches.find((x) => x.id === 'impots-assistanat').faits[1].fait);
    assert.ok(textesApres.every((t) => !t.includes(fait1)), 'fait déjà avancé non répété');
    assert.ok(premier);
    // comparaison d'approches
    await page.getByText(/Comparer \d approches/).click();
    assert.ok((await page.locator('.approche').count()) >= 2);
    assert.ok(await page.locator('.approche.is-chosen').first().isVisible());
    // retour en texte libre, interprété localement
    await page.locator('#conv-msg').fill('il m’a répondu que les statistiques étaient truquées');
    await page.getByRole('button', { name: 'Il ou elle m’a répondu…' }).click();
    await page.locator('#conv-fil .conv-tour').first().waitFor();
    assert.match(await page.locator('#conv-fil .conv-tour .conv-lecture').first().textContent(), /Conteste un chiffre/);
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('conversation continue : dix échanges et plus, rechargement, « Conversation terminée », bilan, nouvelle conversation', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/express`);
    await page.locator('#express-text').fill('Les impôts servent à payer les assistés');
    await page.getByRole('button', { name: 'Sortir une réplique' }).click();
    await page.locator('#conversation').waitFor();
    const fin = page.getByRole('button', { name: 'Conversation terminée' });
    assert.ok(await fin.isVisible(), 'bouton de clôture visible');
    assert.ok(!(await fin.getAttribute('class')).includes('btn-primary'), 'clôture discrète : pas le bouton principal');
    const msgs = ['N’importe quoi', 'T’as une source ?', 'Les chiffres de l’Insee sont truqués', 'c’est vrai que les retraites pèsent lourd, mais les étrangers profitent des aides', 'ouais', 'Espèce de gauchiste', 'ça suffit', 'Je ne comprends pas', 'Bon, je vais regarder', 'Et l’immigration alors, ça coûte une fortune', 'Pas d’accord'];
    const textes = new Set();
    for (const [k, m] of msgs.entries()) {
      await page.locator('#conv-msg').fill(m);
      await page.getByRole('button', { name: 'Il ou elle m’a répondu…' }).click();
      await page.waitForFunction((n) => document.querySelectorAll('#conv-fil .conv-tour').length === n, k + 1);
      textes.add(await page.locator('#conv-fil .conv-tour:last-child .bulle--toi p').textContent());
      assert.ok(await page.locator('#conv-msg').isVisible(), `la saisie reste ouverte après l’échange ${k + 1}`);
      assert.equal(await page.locator('#conv-bilan').count(), 0, 'pas de fin automatique');
    }
    assert.equal(textes.size, msgs.length, 'aucune proposition répétée');
    assert.match(await page.locator('.conv-etat').textContent(), /11 échanges/);
    // interruption : rechargement de l'onglet, la conversation reprend où elle en était
    await page.reload();
    await page.locator('#conversation').waitFor();
    assert.equal(await page.locator('#conv-fil .conv-tour').count(), 11);
    await page.locator('[data-conv-raccourci="aide"]').click();
    await page.waitForFunction(() => document.querySelectorAll('#conv-fil .conv-tour').length === 12);
    // résumé évolutif
    await page.getByText('Où en est la discussion').click();
    assert.match(await page.locator('.conv-resume-txt').textContent(), /Échanges : 12/);
    // clôture voulue par l'utilisateur, puis bilan fidèle
    await page.getByRole('button', { name: 'Conversation terminée' }).click();
    await page.locator('#conv-bilan').waitFor();
    assert.match(await page.locator('.bilan-message').textContent(), /Bravo/);
    assert.ok((await page.locator('#conv-bilan .src-inline').count()) >= 1, 'sources consultables');
    assert.match(await page.locator('#conv-bilan').textContent(), /retraites pèsent lourd/);
    await page.getByRole('button', { name: 'Nouvelle conversation sur ce sujet' }).click();
    await page.locator('#conv-msg').waitFor();
    assert.equal(await page.locator('#conv-fil .conv-tour').count(), 0, 'nouveau contexte séparé');
    assert.match(await page.locator('.conv-etat').textContent(), /0 échange/);
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('suggestions spécialisées : sous-thème, mode, « Autres affirmations », express, rebond statistique → expulsion', async () => {
    const page = await newPage(browser, PHONE, errors);
    const chips = async () => page.locator('#sugg-wizard .sugg-chip').evaluateAll((els) => els.map((e) => e.dataset.exampleFill));
    // Immigration et travail, mode « gagner »
    await page.goto(`${s.base}/#/debat`);
    await page.getByRole('heading', { name: 'Quel est ton objectif ?' }).waitFor();
    await page.getByRole('radio', { name: /GAGNER LE DÉBAT/ }).click();
    await page.getByRole('heading', { name: 'De quoi ça parle ?' }).waitFor();
    await page.getByRole('radio', { name: /Immigration, intégration et discriminations/ }).click();
    await page.getByRole('button', { name: 'Immigration et travail', exact: true }).click();
    await page.getByRole('button', { name: 'Continuer' }).click();
    await page.locator('#sugg-wizard').waitFor();
    const travail = await chips();
    assert.equal(travail.length, 3);
    assert.ok(travail.every((t) => /(travail|salaire|métier|cotis|emploi)/i.test(t)), travail.join(' / '));
    await page.getByRole('button', { name: 'Autres affirmations' }).click();
    const autres = await chips();
    assert.equal(autres.filter((t) => travail.includes(t)).length, 0, 'renouvellement sans répétition');
    await page.locator('#sugg-wizard .sugg-chip').first().click();
    assert.equal(await page.locator('#affirmation').inputValue(), autres[0]);
    // même sous-thème en mode « convaincre » : sélection différente
    await page.getByRole('button', { name: /Revenir à l’étape 1/ }).click();
    await page.getByRole('radio', { name: /CONVAINCRE SANS BRAQUER/ }).click();
    await page.getByRole('button', { name: 'Continuer' }).click();
    await page.locator('#sugg-wizard').waitFor();
    const dialogue = await chips();
    assert.notDeepEqual(dialogue, travail);
    // prisons : les formulations de la nouvelle rubrique, avec fiche vérifiée
    await page.getByRole('button', { name: /Revenir à l’étape 2/ }).click();
    await page.getByRole('button', { name: 'Immigration, délinquance et prisons', exact: true }).click();
    await page.getByRole('button', { name: 'Continuer' }).click();
    await page.locator('#sugg-wizard').waitFor();
    const prisons = await chips();
    assert.ok(prisons.every((t) => /(prison|carcéral|délinqu|sûre|détention|insécurité)/i.test(t)), prisons.join(' / '));
    assert.ok((await page.locator('#sugg-wizard .sugg-tag').count()) >= 1, 'les suggestions couvertes par une fiche sont signalées');
    // express : les suggestions suivent le sujet choisi
    await page.goto(`${s.base}/#/express`);
    await page.locator('#sugg-express').waitFor();
    await page.locator('#express-volet').selectOption('ecologie');
    const eco = await page.locator('#sugg-express .sugg-chip').evaluateAll((els) => els.map((e) => e.dataset.exampleFill));
    assert.equal(eco.length, 3);
    assert.ok(eco.every((t) => /(climat|énerg|nucléaire|éolien|pollu|voiture|agricult|pesticide|biodiversit|isol|industrie|écolo|émission|renouvel|loyer|bio|chin)/i.test(t)), eco.join(' / '));
    // rebond : statistiques carcérales → expulsion
    await page.goto(`${s.base}/#/argumentaire/etrangers-prisons`);
    await page.locator('#conv-msg').waitFor();
    await page.locator('#conv-msg').fill('Peu importe les statistiques, il faut tous les renvoyer chez eux.');
    await page.getByRole('button', { name: 'Il ou elle m’a répondu…' }).click();
    await page.locator('#conv-fil .conv-tour').first().waitFor();
    assert.match(await page.locator('.conv-lecture').first().textContent(), /Déplace la discussion/);
    assert.match(await page.locator('#conv-fil .bulle--toi').first().textContent(), /Tous les étrangers condamnés devraient être expulsés/);
    assert.ok(await page.getByRole('button', { name: /Revenir à « Les étrangers remplissent les prisons/ }).isVisible());
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('v8 — analyse de la phrase : emploi ≠ aides, plusieurs arguments, lacune reconnue, sans débordement', async () => {
    const page = await newPage(browser, PHONE, errors);
    const express = async (t) => {
      await page.goto(`${s.base}/#/`);
      await page.locator('#express-mini-text').fill(t);
      await page.getByRole('button', { name: 'Sortir une réplique' }).click();
      await page.locator('.analyse').waitFor();
    };
    // démonstration : la fiche emploi est retenue, la fiche « aides » est écartée avec sa raison
    await express('Plus il y a d’immigrés, moins il y a de travail pour les Français.');
    assert.ok(await page.locator('a[href="#/bibliotheque/immigration-emploi"]').first().isVisible());
    assert.match(await page.locator('.claim-reform').textContent(), /Les immigrés prennent le travail des Français/);
    await page.locator('.an-ecartees > summary').click();
    const ecart = await page.locator('.an-ecartees').textContent();
    assert.match(ecart, /Les immigrés touchent plus d'aides/);
    assert.match(ecart, /pas de : emploi/);
    assert.match(await page.locator('.fiche-panel:not([hidden]) .riposte').textContent(), /gâteau fixe|moins souvent en emploi|employeurs/);
    assert.ok((await overflow(page)) <= 1);
    // deux sujets : deux cartes, chacune avec sa fiche et sa source
    await express('Les immigrés prennent le travail des Français et en plus ils viennent toucher le RSA.');
    assert.equal(await page.locator('.an-arg').count(), 2);
    const sec = page.locator('.an-arg').nth(1);
    assert.match(await sec.textContent(), /prestations sociales/);
    assert.ok(await sec.locator('a[href="#/bibliotheque/immigres-aides"]').isVisible());
    assert.ok(await sec.locator('.an-src a').first().isVisible(), 'la donnée secondaire est sourcée');
    // lacune : aucune fiche voisine présentée comme réponse
    await express('On ne peut plus se loger à cause de l’immigration.');
    await page.getByRole('heading', { name: 'Pas encore dans la bibliothèque' }).waitFor();
    assert.match(await page.locator('.verdict-summary').textContent(), /immigration et logement/);
    assert.equal(await page.locator('.analyse a[href="#/bibliotheque/immigres-aides"]').count() - await page.locator('.an-ecartees a[href="#/bibliotheque/immigres-aides"]').count(), 0);
    assert.match(await page.locator('.analyse').textContent(), /Ce qui peut se jouer derrière/);
    await page.close();
  });

  test('v9 — la réponse avant la méthode : 10 affirmations × (express sans thème, « gagner », « convaincre »)', async () => {
    const page = await newPage(browser, PHONE, errors);
    const CAS = [
      ['On ne peut pas aider tout le monde.', 'aider-tout-le-monde'],
      ['Les immigrés prennent le travail des Français.', 'immigration-emploi'],
      ['Les Français ne veulent plus travailler.', 'chomeurs-travailler'],
      ['Les riches créent les emplois.', 'riches-creent-emplois'],
      ['La gauche veut augmenter tous les impôts.', 'gauche-augmenter-impots'],
      ['Il faut renvoyer tous les criminels étrangers.', null],
      ['La France n’a plus les moyens de financer ses services publics.', 'services-publics-moyens'],
      ['Mélenchon crie tout le temps, il est dangereux.', 'melenchon-crie'],
      ['Les aides sociales encouragent les gens à ne pas travailler.', 'rsa-smic'],
      ['La France doit d’abord s’occuper de ses propres citoyens.', 'immigres-aides'],
    ];
    const GENERIQUE = /j’aimerais comprendre ton point de vue|Avant de te répondre|reconnaître ses émotions|faire preuve d’empathie/i;
    const lancer = async (t, mode, depuisAccueil) => {
      await page.goto(`${s.base}/#/${depuisAccueil ? '' : 'express'}`);
      await page.locator(`[data-express-mode="${mode}"]`).first().click();
      await page.locator(depuisAccueil ? '#express-mini-text' : '#express-text').fill(t);
      await page.getByRole('button', { name: 'Sortir une réplique' }).click();
      await page.locator('.fiche-panel:not([hidden])').waitFor();
      return page.locator('.fiche-panel:not([hidden])');
    };
    for (const [t, id] of CAS) {
      const vus = {};
      for (const [mode, accueil] of [['gagner', true], ['gagner', false], ['convaincre', false]]) {
        const panel = await lancer(t, mode, accueil);
        assert.equal(await panel.getAttribute('id'), `strat-panel-${mode}`, `${t} : le mode choisi (${mode}) est respecté`);
        if (id) assert.ok(await page.locator(`.crumb a[href="#/bibliotheque/${id}"]`).count(), `${t} → ${id}`);
        const titres = await panel.locator('h3.sub-title').allTextContents();
        assert.equal(titres[0], 'Ce que tu peux répondre', `${t} (${mode}) : la réponse vient en premier`);
        assert.match(await panel.locator('.prio-label').first().textContent(), /1 · La réponse/);
        const txt = await panel.innerText();
        const avantPreuves = txt.slice(0, txt.indexOf('Source :'));
        assert.ok(txt.indexOf('Source :') > 0, `${t} (${mode}) : des sources`);
        assert.doesNotMatch(avantPreuves, GENERIQUE, `${t} (${mode}) : pas de conseil générique avant la réponse et les preuves`);
        const bas = txt.toLowerCase();
        assert.ok(bas.indexOf('5 · comment aborder la discussion') > bas.indexOf('2 · les preuves') && bas.indexOf('2 · les preuves') > 0, 'la communication vient en dernier');
        if (mode === 'gagner') {
          assert.ok(titres.includes('La riposte qui fait réfléchir'), `${t} : riposte`);
          assert.ok(!titres.some((x) => /empathie|sans braquer|comprendre son point de vue/i.test(x)), `${t} : pas de bloc empathique en mode gagner (${titres.join(' / ')})`);
          assert.doesNotMatch(txt, GENERIQUE);
        } else {
          assert.ok(titres.includes('Pour l’introduire sans braquer'), `${t} : présentation adaptée`);
          assert.ok(titres.some((x) => /empathie/i.test(x)), `${t} : version empathique`);
        }
        vus[mode] = { sources: await panel.locator('.preuve-src a').count(), titres };
      }
      assert.ok(vus.convaincre.sources >= 1 && vus.gagner.sources >= 1, `${t} : les sources restent dans les deux modes`);
      assert.notDeepEqual(vus.gagner.titres, vus.convaincre.titres, `${t} : les deux modes sont visiblement différents`);
    }
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('v10 — lecture de gauche (valeurs, propositions, faits défavorables) et fermeté sur la dignité humaine', async () => {
    const page = await newPage(browser, PHONE, errors);
    const express = async (t, mode = 'gagner') => {
      await page.goto(`${s.base}/#/express`);
      await page.locator(`[data-express-mode="${mode}"]`).click();
      await page.locator('#express-text').fill(t);
      await page.getByRole('button', { name: 'Sortir une réplique' }).click();
      await page.waitForFunction(() => ['#/argumentaire', '#/introuvable'].includes(location.hash));
    };
    for (const mode of ['gagner', 'convaincre']) {
      await express('Les immigrés prennent le travail des Français.', mode);
      const panel = page.locator('.fiche-panel:not([hidden])');
      const txt = (await panel.innerText()).toLowerCase();
      assert.ok(txt.indexOf('3 · la lecture de gauche') > txt.indexOf('2 · les preuves'), 'la lecture politique vient après les preuves');
      const lect = panel.locator('.lecture');
      assert.match(await lect.textContent(), /Les valeurs en jeu/);
      assert.match(await lect.textContent(), /propositions politiques : des choix assumés, pas des faits/);
      assert.match(await lect.textContent(), /Ce qui ne va pas dans notre sens/);
      assert.match(await lect.textContent(), /Protection des travailleurs/);
    }
    // déshumanisation : pas de faux équilibre, même sans fiche
    await express('Les immigrés sont des parasites.');
    assert.match(await page.locator('.dignite').textContent(), /n’est pas une opinion comme une autre/);
    assert.match(await page.locator('.dignite').textContent(), /Déshumanisation/);
    // appel à laisser mourir : fermeté + réponse sourcée sur le droit de la mer
    await express('Il faut les laisser se noyer en mer.');
    assert.match(await page.locator('.dignite').textContent(), /Appel à la violence ou à la mort/);
    assert.ok(await page.locator('.crumb a[href="#/bibliotheque/migrants-mediterranee"]').count());
    // critique d'une politique : pas d'alerte de dignité
    await express('Il faut réduire l’immigration.');
    assert.equal(await page.locator('.dignite').count(), 0);
    // la fiche affiche aussi sa lecture de gauche
    await page.goto(`${s.base}/#/bibliotheque/antisemitisme-aujourdhui`);
    await page.locator('.lecture-fiche > summary').click();
    assert.match(await page.locator('.lecture-fiche').textContent(), /LFI/);
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('question non couverte : message simple, sans fausse erreur de connexion', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/express`);
    await page.locator('#express-text').fill('Le prix du pain au Moyen Âge');
    await page.getByRole('button', { name: 'Sortir une réplique' }).click();
    await page.getByRole('heading', { name: 'Pas encore dans la bibliothèque' }).waitFor();
    const txt = await page.locator('main').textContent();
    assert.ok(!/serveur|connexion|Ça n’a pas marché/i.test(txt));
    await page.close();
  });

  test('changement de mode : connecté sans serveur configuré = signalé, pas bloquant ; pages Publier et Veille', async () => {
    const page = await newPage(browser, PHONE, errors);
    await page.goto(`${s.base}/#/mode`);
    await page.getByRole('radio', { name: 'Connecté' }).click();
    await page.waitForFunction(() => document.querySelector('#mode-pill').textContent.startsWith('Connecté'));
    assert.match(await page.locator('#mode-pill').textContent(), /non configuré/);
    // la bibliothèque et les argumentaires restent disponibles
    await page.goto(`${s.base}/#/bibliotheque/rsa-smic`);
    await page.getByRole('link', { name: 'Composer mon argumentaire' }).click();
    await page.locator('#replique-text').waitFor();
    await page.goto(`${s.base}/#/mode`);
    await page.getByRole('radio', { name: 'Autonome — sans Internet' }).click();
    await page.waitForFunction(() => document.querySelector('#mode-pill').textContent === 'Autonome');
    await page.goto(`${s.base}/#/publier`);
    await page.getByRole('heading', { name: 'Avant de partager : la checklist' }).waitFor();
    assert.ok(await page.getByText(/version locale ou un aperçu/).isVisible(), 'l’adresse locale est signalée comme non partageable');
    await page.goto(`${s.base}/#/veille`);
    await page.getByText('Aucune planification active pour ce site.').waitFor();
    await page.close();
  });

  test('aucune erreur JavaScript', () => { assert.deepEqual(errors, []); });
});

describe('interface — mode réel (service d’IA simulé)', { skip }, () => {
  let s; let browser; let f; const errors = [];
  before(async () => {
    f = routerFetch(defaultRoutes());
    s = await startServer(testConfig({ liveMode: true, apiKey: 'k', perIpAnalysisLimit: 50 }), { fetchImpl: f });
    browser = await chromium.launch();
  });
  after(async () => { await browser?.close(); await s?.close(); });

  test('résultat mobile : conclusion, réplique, 3 arguments, sources, détails ; changement de mode sans nouvelle recherche', async () => {
    const page = await newPage(browser, PHONE, errors, { connecte: true });
    await page.goto(`${s.base}/#/`);
    await page.waitForFunction(() => document.querySelector('#mode-pill').textContent === 'Connecté');
    await page.getByRole('link', { name: 'Préparer ma riposte' }).click();
    await page.getByRole('radio', { name: /Économie, capitalisme/ }).click();
    await page.getByRole('button', { name: 'Continuer' }).click();
    await page.locator('#affirmation').fill('Les impôts ne servent qu’à payer l’assistanat.');
    await page.getByRole('button', { name: 'OK, SORS LES SOURCES !' }).click();
    await page.getByRole('heading', { name: /Contredit par les données consultées/ }).waitFor();
    // ordre mobile : conclusion → réplique → arguments → sources → détails
    const order = await page.evaluate(() => ['.verdict-card', '#replique-title', '#args-title', '#sources-title', '#details-title'].map((sel) => document.querySelector(sel).getBoundingClientRect().top));
    assert.deepEqual([...order].sort((a, b) => a - b), order);
    assert.equal(await page.locator('.args > li').count(), 3);
    assert.equal(await page.locator('.source-card').count(), 3);
    assert.equal(await page.locator('.access--document_consulte').count(), 1);
    assert.ok(await page.getByText('Chiffre absent du dossier vérifié : 99').isVisible());
    assert.ok(!(await page.locator('.sources').textContent()).includes('Rapport inventé'));
    // détails dépliables
    await page.getByText('Ce qui complique notre argument').click();
    assert.ok(await page.getByText('Les prestations sociales augmentent plus vite que le PIB.').isVisible());
    await page.getByText(/Tous les faits vérifiés/).click();
    assert.ok(await page.getByText('Chiffre non retrouvé tel quel').isVisible());
    assert.ok(await page.getByText(/Références écartées \(1\)/).isVisible());
    // démonstration orale
    await page.getByText('Préparer ma démonstration').click();
    await page.getByRole('button', { name: '1 minute' }).click();
    await page.getByText('Version spontanée').waitFor();
    // changement de mode
    await page.getByRole('radio', { name: 'Convaincre sans braquer' }).click();
    await page.getByRole('heading', { name: 'Les faits, un par un' }).waitFor();
    assert.ok(await page.getByText('C’est normal de vouloir savoir où vont ses impôts.').isVisible());
    assert.equal(f.count('research'), 1);
    assert.equal(f.count('convaincre'), 1);
    // reformulation, copie des références, partage, signalement, avis
    await page.getByRole('button', { name: 'Autre formulation' }).click();
    await page.getByText('Nouvelle formulation prête !').waitFor();
    await page.getByRole('button', { name: 'Copier les références' }).click();
    const clip = await page.evaluate(() => navigator.clipboard.readText()).catch(() => null);
    if (clip !== null) assert.match(clip, /\[S1\] Insee/);
    await page.getByRole('button', { name: 'Partager' }).click();
    await page.getByText(/Résumé sourcé copié/).waitFor();
    const shared = await page.evaluate(() => navigator.clipboard.readText()).catch(() => null);
    if (shared !== null) { assert.match(shared, /Verdict documentaire/); assert.ok(!/préoccupé|colérique/i.test(shared)); }
    await page.getByText('Voir les données utilisées').first().click();
    await page.getByRole('button', { name: 'Signaler une source incorrecte' }).first().click();
    await page.locator('.report-source-form textarea').fill('Le chiffre a été révisé.');
    await page.locator('.report-source-form').getByRole('button', { name: 'Envoyer le signalement' }).click();
    await page.locator('.report-source-form').getByText('Merci !').waitFor();
    await page.getByText('Oui, mais il manque des choses.').click();
    await page.locator('#feedback-form').getByRole('button', { name: 'Envoyer mon avis' }).click();
    await page.locator('#feedback-form').getByText('Merci !').waitFor();
    assert.ok((await overflow(page)) <= 1);
    await page.close();
  });

  test('réponse express : la réplique est en tête et se copie', async () => {
    const page = await newPage(browser, { ...PHONE, width: 360, height: 740 }, errors, { connecte: true });
    await page.goto(`${s.base}/#/express`);
    await page.getByRole('radio', { name: 'Gagner le débat' }).click();
    await page.locator('#express-text').fill('Les chômeurs ne veulent pas travailler, c’est bien connu.');
    await page.getByRole('button', { name: 'Sortir une réplique' }).click();
    await page.locator('#replique-text').waitFor();
    await page.getByRole('button', { name: 'Copier la réponse' }).click();
    await page.getByText('Réplique copiée !').waitFor();
    await page.close();
  });

  test('fiche → riposte construite sans nouvelle recherche', async () => {
    const before = f.count('research');
    const page = await newPage(browser, PHONE, errors, { connecte: true });
    await page.goto(`${s.base}/#/bibliotheque/rsa-smic`);
    await page.getByRole('button', { name: 'Préparer ma riposte' }).click();
    await page.getByRole('heading', { name: 'La démonstration en 3 points' }).waitFor();
    assert.equal(f.count('research'), before);
    await page.close();
  });

  test('aucune erreur JavaScript', () => { assert.deepEqual(errors, []); });
});

describe('interface — base locale d’abord (service d’IA simulé)', { skip }, () => {
  test('fiche forte et à jour : réponse sans recherche web, lien vers la fiche', async () => {
    const f = routerFetch(defaultRoutes());
    const s = await startServer(testConfig({ liveMode: true, apiKey: 'k', kbDirectAnswer: true }), { fetchImpl: f });
    const browser = await chromium.launch();
    const errors = [];
    try {
      const page = await newPage(browser, PHONE, errors, { connecte: true });
      await page.goto(`${s.base}/#/express`);
      await page.locator('#express-text').fill('Les impôts ne servent qu’à payer l’assistanat.');
      await page.getByRole('button', { name: 'Sortir une réplique' }).click();
      await page.locator('#replique-text').waitFor();
      assert.ok(await page.getByText(/Réponse construite à partir de la fiche vérifiée/).isVisible());
      assert.equal(f.count('research'), 0);
      assert.deepEqual(errors, []);
    } finally { await browser.close(); await s.close(); }
  });
});

describe('interface — recherche indisponible puis relance', { skip }, () => {
  test('erreur explicite, bouton Relancer, puis résultat', async () => {
    const routes = defaultRoutes();
    const f = routerFetch({ ...routes, research: [researchResponse({ json: DOSSIER_JSON, searchError: 'unavailable', fetched: [], fetchErrors: [] }), routes.research] });
    const s = await startServer(testConfig({ liveMode: true, apiKey: 'k' }), { fetchImpl: f });
    const browser = await chromium.launch();
    const errors = [];
    try {
      const page = await newPage(browser, PHONE, errors, { connecte: true });
      await page.goto(`${s.base}/#/express`);
      await page.locator('#express-text').fill('Les impôts ne servent qu’à payer l’assistanat.');
      await page.getByRole('button', { name: 'Sortir une réplique' }).click();
      await page.getByRole('heading', { name: 'Ça n’a pas marché' }).waitFor();
      assert.match(await page.locator('.error-box').textContent(), /recherche Web n'a pas fonctionné/);
      assert.equal(await page.locator('.verdict-card').count(), 0);
      await page.getByRole('button', { name: 'Relancer' }).click();
      await page.locator('#replique-text').waitFor();
      assert.deepEqual(errors, []);
    } finally { await browser.close(); await s.close(); }
  });
});

describe('interface — conversation en mode connecté (service d’IA simulé)', { skip }, () => {
  test('erreur temporaire : message réel, bouton Réessayer, le fil est conservé ; puis plusieurs tours', async () => {
    const TOUR = { type: 'desaccord', lecture: 'Il conteste.', texte: 'Regarde ce fait : les minima sociaux représentent une petite part des dépenses publiques.', strategie: 'Préciser le désaccord.', question: null, faits_utilises: [3], objection_traitee: null, conclusion_possible: false };
    const f = routerFetch({ conversation: [{ status: 529 }, jsonResponse(TOUR), jsonResponse({ ...TOUR, texte: 'Autre proposition, sur la source.', faits_utilises: [0] }), jsonResponse({ ...TOUR, texte: 'Troisième proposition.' })] });
    const s = await startServer(testConfig({ liveMode: true, apiKey: 'k' }), { fetchImpl: f });
    const browser = await chromium.launch();
    const errors = [];
    try {
      const page = await newPage(browser, PHONE, errors, { connecte: true });
      await page.goto(`${s.base}/#/argumentaire/impots-assistanat`);
      await page.locator('#conv-msg').waitFor();
      await page.locator('#conv-msg').fill('N’importe quoi');
      await page.getByRole('button', { name: 'Il ou elle m’a répondu…' }).click();
      await page.locator('#conversation .notice--error').waitFor();
      assert.match(await page.locator('#conversation .notice--error').textContent(), /temporairement indisponible/);
      assert.equal(await page.locator('#conv-fil .conv-tour').count(), 0, 'aucune réponse simulée');
      assert.equal(await page.locator('#conv-msg').inputValue(), 'N’importe quoi', 'le message n’est pas perdu');
      await page.getByRole('button', { name: 'Réessayer' }).click();
      await page.waitForFunction(() => document.querySelectorAll('#conv-fil .conv-tour').length === 1);
      assert.match(await page.locator('.conv-lecture').first().textContent(), /mode connecté/);
      for (const [k, m] of ['Source ?', 'Bof'].entries()) {
        await page.locator('#conv-msg').fill(m);
        await page.getByRole('button', { name: 'Il ou elle m’a répondu…' }).click();
        await page.waitForFunction((n) => document.querySelectorAll('#conv-fil .conv-tour').length === n, k + 2);
      }
      const corps = f.calls.filter((c) => c.kind === 'conversation').at(-1).body.messages[0].content;
      assert.match(corps, /Échanges : 2/, 'le résumé évolutif est transmis');
      assert.deepEqual(errors, []);
    } finally { await browser.close(); await s.close(); }
  });
});

describe('interface — hors ligne après la première visite (service worker)', { skip }, () => {
  test('mode avion : bibliothèque, fiche et argumentaire disponibles', async () => {
    const s = await startServer(testConfig({ liveMode: false, apiKey: '' }));
    const browser = await chromium.launch();
    const errors = [];
    try {
      const ctx = await browser.newContext({ viewport: { width: 390, height: 844 } });
      const page = await ctx.newPage();
      page.on('pageerror', (e) => errors.push(e.message));
      await page.goto(`${s.base}/#/`);
      await page.evaluate(() => navigator.serviceWorker.ready);
      await page.waitForFunction(async () => (await caches.keys()).some((k) => k.startsWith('gtp-shell-')) && (await (await caches.open('gtp-kb')).match('kb/base.json')) !== undefined);
      await ctx.setOffline(true);
      await page.reload();
      await page.getByRole('heading', { level: 1, name: /ENVIE DE GAUCHISER/ }).waitFor();
      await page.goto(`${s.base}/#/bibliotheque`);
      await page.locator('.fiche-card').first().waitFor();
      assert.ok((await page.locator('.fiche-card').count()) >= 50);
      await page.goto(`${s.base}/#/argumentaire/front-populaire-1936`);
      await page.locator('#replique-text').waitFor();
      assert.ok(await page.getByText('Fait historique stable').isVisible());
      assert.deepEqual(errors, []);
    } finally { await browser.close(); await s.close(); }
  });
});
