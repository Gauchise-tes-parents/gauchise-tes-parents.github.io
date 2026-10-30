// Base de connaissances locale : recherche d'abord dans les fiches, décide si un complément web est utile,
// compare ensuite les résultats web avec la fiche et consigne d'éventuelles propositions de mise à jour.
// Une fiche n'est JAMAIS modifiée automatiquement : les propositions sont relues par un humain.
import { appendFile, mkdir } from 'node:fs/promises';
import { dirname } from 'node:path';
import { matchLocal, summarize, freshness } from '../library.js';
import { normalizeUrl, extractNumbers } from './util.js';

/**
 * Décide si une recherche web complémentaire est nécessaire.
 * - aucune fiche forte → web (sujet insuffisamment couvert) ;
 * - fiche d'actualité → web (données susceptibles d'avoir changé) ;
 * - fiche à actualiser → web ;
 * - fiche forte, historique ou évolutive mais à jour → la fiche suffit.
 */
export function decideWeb(best, { freshOpts = {}, fraiche = false } = {}) {
  if (fraiche) return { web: true, motif: 'demande', raison: 'Tu as demandé une vérification web fraîche.' };
  if (!best || best.force !== 'forte') {
    return { web: true, motif: 'non_couvert', raison: best ? 'Les fiches trouvées ne traitent qu’un sujet voisin : une recherche complémentaire est nécessaire.' : 'Aucune fiche de la base ne traite cette affirmation.' };
  }
  const f = best.fiche;
  const fr = freshness(f, freshOpts);
  if (fr.statut === 'a_actualiser') return { web: true, motif: 'a_actualiser', raison: `La fiche « ${f.affirmation} » doit être actualisée : ${fr.raison}` };
  if (f.stabilite === 'actualite') return { web: true, motif: 'actualite', raison: 'Sujet d’actualité : la fiche est complétée par une recherche récente.' };
  return {
    web: false,
    motif: f.stabilite === 'historique' ? 'historique' : 'fiche_a_jour',
    raison: f.stabilite === 'historique'
      ? 'Fait historique stable, déjà vérifié dans la base : pas besoin de recherche web.'
      : `Donnée vérifiée le ${f.derniere_verification} et encore à jour : pas besoin de recherche web.`,
  };
}

/** Correspondances locales + décision, au format renvoyé au client. */
export function localLookup(library, claim, { freshOpts = {}, fraiche = false } = {}) {
  const matches = matchLocal(library, claim);
  const decision = decideWeb(matches[0], { freshOpts, fraiche });
  return {
    matches,
    payload: {
      correspondances: matches.map((m) => ({ ...summarize(m.fiche, freshOpts), force: m.force, score: m.score })),
      decision: { web_complementaire: decision.web, motif: decision.motif, raison: decision.raison },
    },
  };
}

/**
 * Compare un dossier issu de la recherche web avec une fiche locale.
 * Signale : verdict différent, sources nouvelles, chiffres de la fiche absents des résultats récents.
 * Ces signaux sont des indices à examiner, pas des preuves d'erreur.
 */
export function compareWithFiche(dossier, fiche) {
  const ficheUrls = new Set(fiche.sources.map((s) => normalizeUrl(s.url)));
  const webSources = (dossier.sources || []).filter((s) => s.acces !== 'non_consulte');
  const communes = webSources.filter((s) => ficheUrls.has(normalizeUrl(s.url))).map((s) => s.url);
  const nouvelles = webSources.filter((s) => !ficheUrls.has(normalizeUrl(s.url)))
    .map((s) => ({ titre: s.titre, organisme: s.organisme, date_publication: s.date_publication, url: s.url, acces: s.acces }));
  const webNumbers = new Set();
  for (const f of dossier.faits || []) for (const n of extractNumbers(`${f.fait} ${f.chiffre || ''}`)) webNumbers.add(n);
  const chiffresAbsents = [];
  for (const f of fiche.faits) {
    if (!f.chiffre) continue;
    const nums = [...extractNumbers(f.chiffre)].filter((n) => !/^(19|20)\d\d$/.test(n));
    if (nums.length && !nums.some((n) => webNumbers.has(n))) chiffresAbsents.push({ fait: f.fait, chiffre: f.chiffre, periode: f.periode || null });
  }
  const verdictDifferent = Boolean(fiche.verdict && dossier.verdict && fiche.verdict !== dossier.verdict);
  const signaux = [];
  if (verdictDifferent) signaux.push(`La recherche récente conclut « ${dossier.verdict_label || dossier.verdict} », la fiche « ${fiche.verdict_label} ».`);
  if (chiffresAbsents.length && (dossier.faits || []).length) signaux.push(`${chiffresAbsents.length} chiffre(s) de la fiche ne figurent pas dans les résultats récents : ils sont peut-être dépassés, ou simplement non repris.`);
  if (nouvelles.length) signaux.push(`${nouvelles.length} source(s) récente(s) absente(s) de la fiche.`);
  return {
    fiche_id: fiche.id,
    fiche_affirmation: fiche.affirmation,
    fiche_verifiee_le: fiche.derniere_verification,
    sources_communes: communes,
    nouvelles_sources: nouvelles.slice(0, 6),
    chiffres_fiche_absents: chiffresAbsents.slice(0, 5),
    verdict_fiche: fiche.verdict,
    verdict_web: dossier.verdict || null,
    contradiction_possible: verdictDifferent,
    signaux,
    mise_a_jour_proposee: verdictDifferent || nouvelles.some((s) => s.acces === 'document_consulte'),
  };
}

/** Consigne une proposition de mise à jour (fichier JSONL, sans donnée personnelle). */
export async function recordProposal(file, comparison, claim) {
  const entry = {
    date: new Date().toISOString().slice(0, 10),
    statut: 'a_examiner',
    fiche_id: comparison.fiche_id,
    affirmation_soumise: String(claim).slice(0, 300),
    verdict_fiche: comparison.verdict_fiche,
    verdict_web: comparison.verdict_web,
    nouvelles_sources: comparison.nouvelles_sources,
    chiffres_fiche_absents: comparison.chiffres_fiche_absents,
    signaux: comparison.signaux,
  };
  await mkdir(dirname(file), { recursive: true });
  await appendFile(file, JSON.stringify(entry) + '\n', 'utf8');
  return entry;
}
