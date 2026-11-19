// Chercheur de sources du moteur interne (SANS IA, sans Claude, gratuit) — il ne fait QUE ça.
// Pour une question restée « à écrire à la main », il cherche des PISTES de sources qui permettent d'argumenter
// avec les valeurs de gauche ou le programme L'Avenir en commun :
//   - programme L'Avenir en commun (corpus déjà relevé par le moteur, cité mot pour mot) ;
//   - recherche publique : HAL (archive ouverte des chercheurs, CNRS) et OpenAlex (publications scientifiques) ;
//   - données publiques : data.gouv.fr (jeux de données des administrations : Insee, ministères, Drees…) ;
//   - vérification des faits : flux RSS de rédactions reconnues (liste réglable dans data/moteur/config.json).
// Il n'écrit AUCUNE fiche et ne tranche rien : les pistes ne sont pas lues, elles sont à ouvrir et à vérifier
// (par le propriétaire ou par Claude lors de la mise à jour hebdomadaire). Les sources d'extrême droite ou de droite
// et les encyclopédies sont écartées d'office (politique documentaire de l'application).
// Essai sans rien enregistrer : node scripts/moteur/sources.js --essai "question"
import { kbNormalize, kbTokens } from '../../public/js/kbsearch.js';
import { classerSource, LE_CLASSES } from '../../public/js/ligne-editoriale.js';
import { motsQuestion, mesuresPertinentes } from './fiches.js';
import { lire, pause } from './reseau.js';

// Mots trop vagues pour une recherche (en plus des mots vides de kbTokens)
const VAGUES = new Set(['france', 'francais', 'francaise', 'gens', 'tout', 'tous', 'toutes', 'faut', 'veut', 'veulent', 'plus', 'moins', 'trop', 'rien', 'jamais', 'toujours', 'gauche', 'droite', 'vrai', 'faux', 'cause', 'chose', 'fait', 'font', 'sont', 'etre', 'avoir', 'aussi', 'meme', 'comme', 'alors', 'donc', 'parce', 'quand', 'leur', 'leurs', 'nous', 'vous', 'nos', 'notre', 'votre', 'cette', 'ces', 'ceux', 'celle', 'partout', 'aujourd', 'hui']);

export const FLUX_DEFAUT = [
  { nom: 'Le Monde — Les Décodeurs', url: 'https://www.lemonde.fr/les-decodeurs/rss_full.xml' },
];

/** Mots-clés de recherche : mots porteurs de la question (sans les mots vagues), les plus longs d'abord. */
export function motsCles(question, { max = 5 } = {}) {
  const mots = [...new Set(kbTokens(question).filter((t) => t.length >= 4 && !VAGUES.has(t)))];
  const { concepts } = motsQuestion(question);
  const labels = concepts.filter((c) => c.central).flatMap((c) => kbTokens(c.label)).filter((t) => t.length >= 4 && !VAGUES.has(t));
  return [...new Set([...mots.sort((a, b) => b.length - a.length), ...labels])].slice(0, max);
}

const nettoyerTexte = (s) => String(s || '').replace(/<[^>]+>/g, ' ').replace(/&(?:#(\d+)|([a-z]+));/gi, (m, n, nom) => (n ? String.fromCharCode(Number(n)) : ({ amp: '&', lt: '<', gt: '>', quot: '"', apos: "'", nbsp: ' ' }[nom] ?? ' '))).replace(/\s+/g, ' ').trim();
const extrait = (s, n = 240) => { const t = nettoyerTexte(s); return t.length > n ? `${t.slice(0, n).replace(/\s+\S*$/, '')}…` : t; };
const httpsOk = (u) => /^https:\/\/[^\s"<>]+$/i.test(String(u || ''));

/** Pertinence d'une piste : part des mots-clés présents dans le titre (double) et le résumé. */
export function pertinence(piste, mots) {
  const titre = kbNormalize(piste.titre || '');
  const corps = kbNormalize(`${piste.extrait || ''} ${piste.organisme || ''}`);
  let score = 0;
  for (const m of mots) {
    const r = m.slice(0, Math.max(4, m.length - 2)); // tolère pluriels et accords
    if (titre.includes(r)) score += 2; else if (corps.includes(r)) score += 1;
  }
  return score;
}

// ── Lecteurs (fonctions pures sur les réponses, testées hors ligne) ──
export function lireHal(json) {
  return (json?.response?.docs || []).map((d) => ({
    origine: 'hal', titre: nettoyerTexte([].concat(d.title_s || [])[0]), url: d.uri_s,
    organisme: `HAL (archive ouverte de la recherche, CNRS)${d.journalTitle_s ? ` — ${nettoyerTexte(d.journalTitle_s)}` : ''}`,
    auteurs: [].concat(d.authFullName_s || []).slice(0, 3).join(', '), date: d.producedDateY_i ? String(d.producedDateY_i) : '',
    extrait: extrait([].concat(d.abstract_s || [])[0]),
  }));
}
export function lireOpenAlex(json) {
  return (json?.results || []).map((w) => ({
    origine: 'openalex', titre: nettoyerTexte(w.title || w.display_name),
    url: w.primary_location?.landing_page_url || (w.doi ? String(w.doi) : ''),
    organisme: `Publication scientifique (OpenAlex)${w.primary_location?.source?.display_name ? ` — ${nettoyerTexte(w.primary_location.source.display_name)}` : ''}`,
    auteurs: (w.authorships || []).slice(0, 3).map((a) => a.author?.display_name).filter(Boolean).join(', '),
    date: w.publication_year ? String(w.publication_year) : '', extrait: '',
  }));
}
export function lireDataGouv(json) {
  return (json?.data || []).map((d) => ({
    origine: 'data.gouv.fr', titre: nettoyerTexte(d.title), url: d.page,
    organisme: `${nettoyerTexte(d.organization?.name || 'Producteur non indiqué')} (données publiques, data.gouv.fr)`,
    auteurs: '', date: String(d.last_update || d.created_at || '').slice(0, 10), extrait: extrait(d.description),
  }));
}
export function lireRss(xml, nom) {
  const items = String(xml || '').match(/<item[\s>][\s\S]*?<\/item>/gi) || [];
  const champ = (it, t) => { const m = it.match(new RegExp(`<${t}[^>]*>([\\s\\S]*?)<\\/${t}>`, 'i')); return m ? m[1].replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, '$1').trim() : ''; };
  return items.map((it) => ({
    origine: 'flux', titre: nettoyerTexte(champ(it, 'title')), url: nettoyerTexte(champ(it, 'link')), organisme: nom,
    auteurs: '', date: (() => { const d = Date.parse(champ(it, 'pubDate')); return Number.isFinite(d) ? new Date(d).toISOString().slice(0, 10) : ''; })(),
    extrait: extrait(champ(it, 'description')),
  }));
}

/** Garde les pistes utilisables : https, pas de droite ni d'encyclopédie, pertinentes ; dédoublonnées. */
export function filtrer(pistes, mots, { min = 2, max = 8 } = {}) {
  const vues = new Set();
  return pistes
    .filter((p) => p.titre && httpsOk(p.url))
    .map((p) => ({ ...p, classe: classerSource(p), score: pertinence(p, mots) }))
    .filter((p) => !['droite', 'partisane', 'tertiaire'].includes(p.classe) && p.score >= min)
    .filter((p) => (vues.has(p.url) ? false : vues.add(p.url)))
    .sort((a, b) => (LE_CLASSES[b.classe]?.role === 'autorite') - (LE_CLASSES[a.classe]?.role === 'autorite') || b.score - a.score)
    .slice(0, max);
}

/** Cherche les pistes d'une question. Les erreurs d'un service sont signalées, jamais bloquantes. */
export async function chercherSources(question, { corpus = null, flux = FLUX_DEFAUT, fetchImpl = fetch, fluxCache = new Map(), journal = console } = {}) {
  const mots = motsCles(question);
  const res = { question, mots, programme: [], pistes: [], erreurs: [] };
  if (corpus) {
    res.programme = mesuresPertinentes(question, corpus, { max: 4 }).map((m) => ({ texte: m.texte, chapitre: m.chapitre, section: m.section, url: m.url }));
  }
  if (!mots.length) { res.erreurs.push('aucun mot-clé exploitable'); return res; }
  const q = encodeURIComponent(mots.join(' '));
  const qOu = encodeURIComponent(mots.join(' OR '));
  const services = [
    ['HAL', `https://api.archives-ouvertes.fr/search/?q=${qOu}&wt=json&rows=12&fl=title_s,uri_s,producedDateY_i,journalTitle_s,authFullName_s,abstract_s&fq=language_s:fr&sort=score%20desc`, lireHal],
    ['OpenAlex', `https://api.openalex.org/works?search=${q}&filter=language:fr&per-page=12&select=title,display_name,doi,publication_year,primary_location,authorships`, lireOpenAlex],
    ['data.gouv.fr', `https://www.data.gouv.fr/api/1/datasets/?q=${q}&page_size=12`, lireDataGouv],
  ];
  const brutes = [];
  for (const [nom, url, lecteur] of services) {
    try { brutes.push(...lecteur(await lire(url, { fetchImpl, type: 'json' }))); } catch (e) { res.erreurs.push(`${nom} : ${e.message}`); }
    await pause(300); // politesse envers les services publics
  }
  for (const f of flux) {
    try {
      if (!fluxCache.has(f.url)) fluxCache.set(f.url, lireRss(await lire(f.url, { fetchImpl }), f.nom));
      brutes.push(...fluxCache.get(f.url));
    } catch (e) { fluxCache.set(f.url, []); res.erreurs.push(`flux ${f.nom} : ${e.message}`); }
  }
  res.pistes = filtrer(brutes, mots);
  if (res.erreurs.length) journal.warn?.(`sources « ${question} » : ${res.erreurs.join(' ; ')}`);
  return res;
}

/** Texte lisible (compte rendu du moteur et fichier data/moteur/pistes.md). */
export function pistesMarkdown(r) {
  const l = [`### « ${r.question} »`, `Mots-clés : ${r.mots.join(', ') || '—'}`];
  if (r.programme.length) l.push('', 'Programme *L’Avenir en commun* :', ...r.programme.map((m) => `- « ${m.texte} » — ${m.chapitre}${m.url ? ` (${m.url})` : ''}`));
  if (r.pistes.length) l.push('', 'Pistes de sources (NON LUES : à ouvrir et vérifier avant toute citation) :', ...r.pistes.map((p) => `- [${p.titre}](${p.url}) — ${p.organisme}${p.date ? `, ${p.date}` : ''}${p.auteurs ? ` (${p.auteurs})` : ''}`));
  if (!r.programme.length && !r.pistes.length) l.push('', 'Aucune piste trouvée.');
  if (r.erreurs.length) l.push('', `Services indisponibles : ${r.erreurs.join(' ; ')}`);
  return l.join('\n');
}

// ── Essai en ligne de commande, sans rien enregistrer ──
if (process.argv[1] && process.argv[1].endsWith('sources.js') && process.argv.includes('--essai')) {
  const { readFileSync } = await import('node:fs');
  const { join, dirname } = await import('node:path');
  const { fileURLToPath } = await import('node:url');
  const D = join(dirname(fileURLToPath(import.meta.url)), '..', '..', 'data', 'moteur');
  let corpus = null; let flux = FLUX_DEFAUT;
  try { corpus = JSON.parse(readFileSync(join(D, 'aec.json'), 'utf8')); } catch { /* pas de programme relevé */ }
  try { flux = JSON.parse(readFileSync(join(D, 'config.json'), 'utf8')).flux_verification || flux; } catch { /* défaut */ }
  const questions = process.argv.slice(process.argv.indexOf('--essai') + 1).join(' ').split('|').map((s) => s.trim()).filter(Boolean);
  const cache = new Map();
  for (const question of questions) console.log(`${pistesMarkdown(await chercherSources(question, { corpus, flux, fluxCache: cache }))}\n`);
}
