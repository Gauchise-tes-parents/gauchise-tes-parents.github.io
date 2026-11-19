import { test } from 'node:test';
import assert from 'node:assert/strict';
import { installerNatif } from '../../public/js/natif.js';

const fenetre = (cap) => ({ Capacitor: cap, navigator: {}, location: { hash: '#/bibliotheque' }, history: { back() { this.retour = true; } } });

test('site web : aucun effet sans Capacitor natif', () => {
  assert.equal(installerNatif(fenetre(undefined)), false);
  const w = fenetre({ isNativePlatform: () => false, Plugins: {} });
  assert.equal(installerNatif(w), false);
  assert.ok(!('share' in w.navigator));
});

test('appli : partage natif relié à navigator.share, annulation = AbortError', async () => {
  const appels = [];
  const w = fenetre({ isNativePlatform: () => true, Plugins: { Share: { share: async (d) => { appels.push(d); } } } });
  assert.equal(installerNatif(w), true);
  await w.navigator.share({ title: 'T', text: 'X', url: 'https://exemple.org/' });
  assert.deepEqual(appels[0], { title: 'T', text: 'X', url: 'https://exemple.org/', dialogTitle: 'Partager' });
  const w2 = fenetre({ isNativePlatform: () => true, Plugins: { Share: { share: async () => { throw new Error('Share canceled'); } } } });
  installerNatif(w2);
  await assert.rejects(w2.navigator.share({ text: 'X' }), (e) => e.name === 'AbortError');
});

test('appli : bouton retour Android (retour arrière, ou sortie depuis l’accueil)', () => {
  let cb; let sortie = false;
  const w = fenetre({ isNativePlatform: () => true, Plugins: { App: { addListener: (n, f) => { assert.equal(n, 'backButton'); cb = f; }, exitApp: () => { sortie = true; } } } });
  installerNatif(w);
  cb({ canGoBack: true });
  assert.equal(w.history.retour, true);
  w.location.hash = '#/';
  cb({ canGoBack: true });
  assert.equal(sortie, true);
});
