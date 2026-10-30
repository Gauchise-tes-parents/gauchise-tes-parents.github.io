// Vérification des preuves : indépendante du fournisseur.
// Règles :
//  1. une source n'est présentée que si son URL a réellement été obtenue pendant la recherche ;
//  2. on distingue un document réellement ouvert (« document consulté ») d'une page connue
//     seulement par un résultat de recherche (« extrait de recherche seulement ») ;
//  3. chaque chiffre est recherché dans le texte réellement consulté ; s'il n'y figure pas tel quel,
//     on le signale ;
//  4. un verdict tranché sans source consultée est rétrogradé.
import { VERDICTS } from '../../public/js/taxonomy.js';
import { normalizeUrl, isSafeHttpUrl, extractNumbers, str, strOrNull, arr } from './util.js';

const VERDICTS_NEEDING_SOURCES = new Set(['confirme', 'plutot_exact', 'trompeur', 'contredit']);
const SENS = new Set(['contredit_affirmation', 'soutient_affirmation', 'contexte']);
const SOURCE_TYPES = new Set(['primaire', 'secondaire', 'media']);

const FETCH_ERRORS = {
  url_not_accessible: 'page inaccessible',
  url_not_allowed: 'consultation refusée par le site',
  unsupported_content_type: 'format non lisible',
  too_many_requests: 'trop de demandes',
};

/** Vérifie les sources proposées par le modèle et leur attribue un identifiant S1, S2… */
export function verifySources(rawSources, ev) {
  const kept = [];
  const rejected = [];
  const seen = new Set();
  for (const s of arr(rawSources).slice(0, 14)) {
    const key = normalizeUrl(s?.url);
    if (!key || !isSafeHttpUrl(s?.url)) {
      rejected.push({ url: str(s?.url, 500), raison: 'URL invalide' });
      continue;
    }
    if (seen.has(key)) continue;
    const doc = ev.documents.get(key);
    const hit = ev.results.get(key);
    if (!doc && !hit) {
      rejected.push({ url: str(s.url, 500), titre: str(s?.titre, 300), raison: "absente des résultats réellement obtenus pendant la recherche" });
      continue;
    }
    seen.add(key);
    const fetchError = ev.fetchErrors.get(key);
    kept.push({
      id: `S${kept.length + 1}`,
      titre: str(s.titre, 300) || doc?.title || hit?.title || (doc || hit).url,
      titre_resultat: doc?.title || hit?.title || null,
      organisme: strOrNull(s.organisme, 200),
      date_publication: strOrNull(s.date_publication, 80) || hit?.page_age || null,
      periode_couverte: strOrNull(s.periode_couverte, 120),
      type: SOURCE_TYPES.has(s.type) ? s.type : null,
      url: (doc || hit).url,
      acces: doc ? 'document_consulte' : 'extrait_recherche',
      acces_detail: doc
        ? `Document ouvert et lu${doc.retrieved_at ? ` le ${doc.retrieved_at.slice(0, 10)}` : ''}${doc.text ? '' : ' (PDF : chiffres non contrôlables automatiquement)'}`
        : `Seul un extrait issu de la recherche était disponible${fetchError ? ` (ouverture impossible : ${FETCH_ERRORS[fetchError] || fetchError})` : ''}`,
      extraits_cites: (ev.citations.get(key) || []).slice(0, 3),
      passage: strOrNull(s.passage, 600),
      pertinence: strOrNull(s.pertinence, 500),
      consultee: true,
    });
  }
  return { kept, rejected };
}

/** Recherche les chiffres d'un fait dans le texte réellement consulté pour sa source. */
export function checkFigures(figureText, source, ev) {
  const nums = [...extractNumbers(figureText)];
  if (!nums.length) return { statut: 'sans_chiffre' };
  const key = normalizeUrl(source?.url);
  const doc = key ? ev.documents.get(key) : null;
  const corpus = [doc?.text || '', ...(ev.citations.get(key) || [])].join('\n');
  if (!corpus.trim()) return { statut: 'non_verifiable', detail: 'Texte du document non disponible pour un contrôle automatique.' };
  const inDoc = extractNumbers(corpus);
  const missing = nums.filter((n) => !inDoc.has(n));
  if (!missing.length) return { statut: 'retrouve', detail: 'Chiffre retrouvé dans le texte consulté.' };
  return { statut: 'non_retrouve', detail: `Non retrouvé tel quel dans le texte consulté : ${missing.join(', ')} (calcul, arrondi ou erreur possible : à vérifier).` };
}

/** Assemble le dossier documentaire vérifié à partir de la sortie brute du modèle. */
export function buildDossier(raw, ev, meta = {}) {
  const warnings = [];
  const { kept, rejected } = verifySources(raw?.sources, ev);
  if (rejected.length) warnings.push(`${rejected.length} référence(s) proposée(s) par l'IA ont été écartées car elles ne figuraient pas dans les résultats réellement obtenus.`);
  const byUrl = new Map(kept.map((s) => [normalizeUrl(s.url), s]));
  const link = (url) => byUrl.get(normalizeUrl(url)) || null;

  let verdict = VERDICTS[raw?.verdict] ? raw.verdict : 'inverifiable';
  if (!VERDICTS[raw?.verdict]) warnings.push("Verdict invalide renvoyé par l'IA : remplacé par « Impossible à vérifier en l'état ».");

  const faits = arr(raw?.faits).slice(0, 8).map((f, i) => {
    const src = link(f?.source_url);
    const fig = src ? checkFigures(`${f?.chiffre || ''} ${f?.fait || ''}`, src, ev) : { statut: 'non_verifiable' };
    return {
      id: `F${i + 1}`,
      fait: str(f?.fait, 600),
      chiffre: strOrNull(f?.chiffre, 200),
      periode: strOrNull(f?.periode, 200),
      perimetre: strOrNull(f?.perimetre, 300),
      montre: strOrNull(f?.montre, 500),
      ne_montre_pas: strOrNull(f?.ne_montre_pas, 500),
      sens: SENS.has(f?.sens) ? f.sens : 'contexte',
      source: src ? src.id : null,
      source_verifiee: Boolean(src),
      controle_chiffre: fig,
    };
  }).filter((f) => f.fait);

  const orphans = faits.filter((f) => !f.source_verifiee).length;
  if (orphans) warnings.push(`${orphans} fait(s) ne sont rattachés à aucune source consultée : à considérer avec prudence.`);
  const unfound = faits.filter((f) => f.controle_chiffre.statut === 'non_retrouve').length;
  if (unfound) warnings.push(`${unfound} chiffre(s) n'ont pas été retrouvés tels quels dans les documents consultés.`);

  const contradictions = arr(raw?.contradictions).slice(0, 5).map((c) => {
    const src = link(c?.source_url);
    return { element: str(c?.element, 600), source: src ? src.id : null, source_verifiee: Boolean(src) };
  }).filter((c) => c.element);

  if (VERDICTS_NEEDING_SOURCES.has(verdict) && kept.length === 0) {
    warnings.push(`Verdict initial « ${VERDICTS[verdict]} » rétrogradé : aucune source consultée ne permet de l'étayer.`);
    verdict = 'inverifiable';
  }

  const alerte = raw?.alerte && typeof raw.alerte === 'object' && str(raw.alerte.constat)
    ? { constat: str(raw.alerte.constat, 600), reformulation_solide: str(raw.alerte.reformulation_solide, 600) }
    : null;

  return {
    reformulation: str(raw?.reformulation, 600),
    verifiable: raw?.verifiable !== false,
    verdict,
    verdict_label: VERDICTS[verdict],
    resume: str(raw?.resume, 1500),
    faits,
    contradictions,
    alerte,
    jugements_de_valeur: arr(raw?.jugements_de_valeur).map((x) => str(x, 400)).filter(Boolean).slice(0, 4),
    manques: arr(raw?.manques).map((x) => str(x, 400)).filter(Boolean).slice(0, 5),
    limites: arr(raw?.limites).map((x) => str(x, 500)).filter(Boolean).slice(0, 6),
    sources: kept,
    sources_rejetees: rejected,
    avertissements: warnings,
    recherche: {
      requetes: ev.queries,
      documents_ouverts: ev.documents.size,
      nb_resultats: ev.results.size,
      erreurs: [...ev.errors, ...[...ev.fetchErrors.values()].map((e) => `consultation:${e}`)],
    },
    date_verification: meta.date || null,
  };
}

/** Texte de référence (tout ce qui est sourcé) pour contrôler qu'une stratégie n'invente pas de chiffre. */
export function dossierReferenceText(dossier, claim = '') {
  const parts = [claim, dossier.reformulation, dossier.resume];
  for (const f of dossier.faits) parts.push(f.fait, f.chiffre, f.periode, f.perimetre, f.montre, f.ne_montre_pas);
  for (const c of dossier.contradictions) parts.push(c.element);
  for (const s of dossier.sources) parts.push(s.date_publication, s.periode_couverte, s.passage, s.titre);
  if (dossier.alerte) parts.push(dossier.alerte.constat, dossier.alerte.reformulation_solide);
  return parts.filter(Boolean).join('\n');
}
