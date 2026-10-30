// Bibliothèque des idées reçues : une fiche = un fichier JSON dans data/library/.
// Ajouter une fiche ne demande aucune modification du code : il suffit de déposer un fichier valide.
import { readdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
import { ROOT } from './config.js';
import { VOLETS, VERDICTS, voletById, RUBRIQUE_IDS, rubriqueById, FIABILITES, STABILITES, TYPES_FICHE, ROBUSTESSES } from '../public/js/taxonomy.js';
import { isSafeHttpUrl } from './engine/util.js';
import { kbSearch, kbMatch, kbFreshness } from '../public/js/kbsearch.js';

export const LIBRARY_DIR = join(ROOT, 'data', 'library');
const DATE = /^\d{4}-\d{2}-\d{2}$/;

/**
 * Une URL de page d'accueil (chemin vide ou « / » sans paramètre) ne prouve pas une statistique précise :
 * elle est refusée comme source d'une fiche.
 */
export function isHomepageUrl(url) {
  try {
    const u = new URL(url);
    return (u.pathname === '' || u.pathname === '/') && !u.search;
  } catch {
    return false;
  }
}

const ARG_KEYS = ['court', 'moyen', 'detaille', 'empathie'];

/** Contrôle de schéma d'une fiche (v3). Renvoie la liste des problèmes (vide si la fiche est valide). */
export function validateEntry(e) {
  const errs = [];
  const need = (cond, msg) => { if (!cond) errs.push(msg); };
  need(e && typeof e === 'object', 'fiche non objet');
  if (errs.length) return errs;
  need(/^[a-z0-9-]{3,60}$/.test(e.id || ''), 'id invalide (minuscules, chiffres, tirets)');
  need(TYPES_FICHE[e.type], `type inconnu : ${e.type}`);
  need(typeof e.affirmation === 'string' && e.affirmation.length > 5, 'affirmation manquante');
  need(VOLETS.some((v) => v.id === e.volet), `volet inconnu : ${e.volet}`);
  if (e.sous_theme != null) need(voletById(e.volet).sousThemes.includes(e.sous_theme), `sous-thème inconnu pour ce volet : ${e.sous_theme}`);
  need(Array.isArray(e.rubriques) && e.rubriques.every((r) => RUBRIQUE_IDS.includes(r)), 'rubriques : tableau de rubriques connues requis');
  need(Array.isArray(e.mots_cles) && e.mots_cles.length >= 3 && e.mots_cles.every((m) => typeof m === 'string' && m), 'au moins 3 mots-clés requis');
  // Le verdict est facultatif : certaines fiches (débats, réponses à des critiques) n'appellent pas de verdict binaire.
  if (e.verdict != null) need(VERDICTS[e.verdict], `verdict inconnu : ${e.verdict}`);
  need(FIABILITES[e.fiabilite], `fiabilité inconnue : ${e.fiabilite}`);
  need(STABILITES[e.stabilite], `stabilité inconnue : ${e.stabilite}`);
  need(typeof e.resume === 'string' && e.resume.length > 20, 'résumé manquant');
  need(typeof e.contexte === 'string' && e.contexte.length > 20, 'contexte manquant');
  need(typeof e.explication === 'string' && e.explication.length > 20, 'explication grand public manquante');
  for (const k of ARG_KEYS) need(typeof e.argumentaires?.[k] === 'string' && e.argumentaires[k].length > 20, `argumentaire « ${k} » manquant`);
  need(Array.isArray(e.contre_arguments) && e.contre_arguments.length > 0 && e.contre_arguments.every((c) => c.objection && c.reponse), 'au moins un contre-argument (objection + réponse) requis');
  need(DATE.test(e.derniere_verification || ''), 'derniere_verification au format AAAA-MM-JJ requise');
  need(DATE.test(e.a_actualiser_le || ''), 'a_actualiser_le au format AAAA-MM-JJ requise');
  need(Array.isArray(e.limites) && e.limites.length > 0, 'au moins une limite est requise');
  need(Array.isArray(e.sources) && e.sources.length > 0, 'au moins une source est requise');
  need(Array.isArray(e.faits) && e.faits.length >= 1 && e.faits.length <= 8, '1 à 8 faits requis');
  for (const [i, s] of (e.sources || []).entries()) {
    need(typeof s.titre === 'string' && s.titre, `source ${i} : titre manquant`);
    need(typeof s.organisme === 'string' && s.organisme, `source ${i} : organisme manquant`);
    need(typeof s.date_publication === 'string' && s.date_publication, `source ${i} : date de publication manquante`);
    need(isSafeHttpUrl(s.url), `source ${i} : URL invalide`);
    need(!isHomepageUrl(s.url), `source ${i} : une page d'accueil ne peut pas servir de preuve (${s.url})`);
    need(typeof s.consultee === 'boolean', `source ${i} : champ « consultee » (true/false) requis`);
  }
  for (const [i, f] of (e.faits || []).entries()) {
    need(typeof f.fait === 'string' && f.fait, `fait ${i} : texte manquant`);
    if (f.fiabilite != null) need(FIABILITES[f.fiabilite], `fait ${i} : fiabilité inconnue`);
    need(Number.isInteger(f.source) && e.sources?.[f.source], `fait ${i} : index de source invalide`);
    if (Number.isInteger(f.source) && e.sources?.[f.source]) {
      need(e.sources[f.source].consultee === true, `fait ${i} : doit s'appuyer sur une source réellement consultée`);
    }
  }
  if (e.type === 'science') {
    need(ROBUSTESSES[e.robustesse], `robustesse inconnue : ${e.robustesse}`);
    need(Array.isArray(e.application) && e.application.length > 0 && e.application.every((a) => a.situation && a.tactique), 'fiche scientifique : au moins une application (situation + tactique)');
  }
  for (const [i, c] of (e.citations || []).entries()) {
    need(c.auteur && c.texte && c.date, `citation ${i} : auteur, texte et date requis`);
    need(Number.isInteger(c.source) && e.sources?.[c.source]?.consultee === true, `citation ${i} : doit renvoyer à une source consultée`);
  }
  return errs;
}

/** Fraîcheur : logique partagée avec le navigateur (public/js/kbsearch.js). */
export const freshness = (e, opts) => kbFreshness(e, opts);

export function loadLibrary(dir = LIBRARY_DIR, logger = console) {
  const entries = [];
  for (const file of readdirSync(dir).filter((f) => f.endsWith('.json')).sort()) {
    try {
      const e = JSON.parse(readFileSync(join(dir, file), 'utf8'));
      const errs = validateEntry(e);
      if (errs.length) {
        logger.warn?.(`[bibliothèque] ${file} ignorée : ${errs.join(' ; ')}`);
        continue;
      }
      entries.push({
        ...e,
        verdict: e.verdict ?? null,
        verdict_label: e.verdict ? VERDICTS[e.verdict] : null,
        volet_label: voletById(e.volet).label,
        fiabilite_label: FIABILITES[e.fiabilite],
        stabilite_label: STABILITES[e.stabilite],
        type_label: TYPES_FICHE[e.type],
        rubriques_labels: e.rubriques.map((r) => rubriqueById(r).court),
      });
    } catch (err) {
      logger.warn?.(`[bibliothèque] ${file} illisible : ${err.message}`);
    }
  }
  return entries;
}

// La logique de recherche est partagée avec le navigateur (aperçu statique) : public/js/kbsearch.js.
export { kbNormalize as normalize, kbTokens as tokens, kbScore as scoreEntry } from '../public/js/kbsearch.js';

/** Recherche par mots-clés avec filtres (volet, sous-thème, rubrique, fiabilité). */
export function searchLibrary(entries, query, volet = null, sousTheme = null, { rubrique = null, fiabilite = null, min = 1 } = {}) {
  return kbSearch(entries, query, { volet, sousTheme, rubrique, fiabilite, min });
}

/** Correspondances locales pour une affirmation soumise (voir kbMatch). */
export const matchLocal = (entries, query, opts) => kbMatch(entries, query, opts);

/** Version allégée pour les listes. */
export function summarize(e, opts) {
  return {
    id: e.id, type: e.type, type_label: e.type_label, affirmation: e.affirmation, volet: e.volet, volet_label: e.volet_label,
    sous_theme: e.sous_theme || null, rubriques: e.rubriques, rubriques_labels: e.rubriques_labels,
    verdict: e.verdict, verdict_label: e.verdict_label, fiabilite: e.fiabilite, fiabilite_label: e.fiabilite_label,
    stabilite: e.stabilite, stabilite_label: e.stabilite_label,
    resume: e.resume, court: e.argumentaires.court, derniere_verification: e.derniere_verification,
    nb_sources: e.sources.length, nb_sources_consultees: e.sources.filter((s) => s.consultee).length,
    fraicheur: freshness(e, opts),
  };
}
