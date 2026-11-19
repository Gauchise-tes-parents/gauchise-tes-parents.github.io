// Application mobile (Capacitor) : branchements natifs, inactifs sur le site web.
// - partage : le WebView Android n'a pas navigator.share ; on le relie au partage natif (@capacitor/share) ;
// - bouton retour Android : revient à l'écran précédent, ou ferme l'appli depuis l'accueil (@capacitor/app).
// Aucune requête réseau, aucune donnée transmise. Sans Capacitor (site web), la fonction ne fait rien.
export function installerNatif(win = globalThis.window) {
  const cap = win?.Capacitor;
  if (!cap || typeof cap.isNativePlatform !== 'function' || !cap.isNativePlatform()) return false;
  const P = cap.Plugins || {};
  try {
    if (P.Share && typeof P.Share.share === 'function') {
      const partager = async (d = {}) => {
        try {
          await P.Share.share({ title: d.title, text: d.text, url: d.url, dialogTitle: 'Partager' });
        } catch (e) {
          // annulation par l'utilisateur : même comportement que navigator.share
          const err = new Error(String(e?.message || 'Partage annulé'));
          err.name = 'AbortError';
          throw err;
        }
      };
      Object.defineProperty(win.navigator, 'share', { value: partager, configurable: true, writable: true });
    }
  } catch { /* partage natif indisponible : copie dans le presse-papiers */ }
  try {
    if (P.App && typeof P.App.addListener === 'function') {
      P.App.addListener('backButton', ({ canGoBack } = {}) => {
        const accueil = !win.location.hash || win.location.hash === '#/' || win.location.hash === '#';
        if (canGoBack && !accueil) win.history.back();
        else if (typeof P.App.exitApp === 'function') P.App.exitApp();
      });
    }
  } catch { /* bouton retour géré par le système */ }
  return true;
}
