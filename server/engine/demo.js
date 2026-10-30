// Mode démonstration : utilisé quand aucune clé API n'est configurée.
// Il ne simule JAMAIS une recherche : aucune source, aucun verdict, aucune stratégie générée.
// Il oriente vers les fiches de la bibliothèque, qui ont été vérifiées à la main.
import { searchLibrary, summarize } from '../library.js';

export function demoAnalyse(req, library, opts) {
  const byText = searchLibrary(library, req.claim, null);
  const byVolet = req.volet !== 'autre' ? searchLibrary(library, '', req.volet) : [];
  const suggestions = [...new Map([...byText, ...byVolet].map((e) => [e.id, e])).values()].slice(0, 3).map((e) => summarize(e, opts));
  return {
    mode: 'demo',
    affirmation: req.claim,
    volet: req.volet,
    sous_theme: req.sousTheme,
    mode_debat: req.mode,
    message: "Mode démonstration : le moteur de recherche n'est pas configuré sur ce serveur. Aucune recherche web n'a été effectuée et aucune riposte n'est générée. Les fiches proposées viennent de la base locale, vérifiée à la main.",
    suggestions_bibliotheque: suggestions,
  };
}
