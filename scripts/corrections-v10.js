#!/usr/bin/env node
// Corrections documentaires (v10), appliquées après les générateurs de fiches et avant `npm run enrichir` :
//  1. remplacements de sources encyclopédiques par des sources vérifiées (lues le 30 octobre 2026) ;
//  2. attribution explicite (« Selon X, … ») des faits qui reposent sur une source de vulgarisation, partisane
//     ou de droite, pour ne pas les présenter comme établis par une autorité qu'ils n'ont pas ;
//  3. ajout de la « lecture de gauche » (scripts/lectures-gauche.js).
// Idempotent : peut être relancé sans dupliquer les modifications.
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { auditFiche, classerSource, LE_CLASSES } from '../public/js/ligne-editoriale.js';
import { LECTURES } from './lectures-gauche.js';

const DIR = join(dirname(fileURLToPath(import.meta.url)), '..', 'data', 'library');
const lire = (id) => JSON.parse(readFileSync(join(DIR, `${id}.json`), 'utf8'));
const ecrire = (f) => writeFileSync(join(DIR, `${f.id}.json`), `${JSON.stringify(f, null, 2)}\n`);
const src = (titre, organisme, date, url, passage, pertinence, type = 'primaire') => ({ titre, organisme, date_publication: date, url, passage, pertinence, type, consultee: true });
const journal = [];

// ── 1. Sources encyclopédiques remplacées ──────────────────────────────────
const POLITOSCOPE = src('« Islamogauchisme » : le piège de l’Alt-right se referme sur la Macronie (Politoscope)', 'CNRS — David Chavalarias (CAMS / ISC-PIF), Politoscope', '21 février 2021',
  'https://politoscope.org/2021/02/islamogauchisme-le-piege-de-lalt-right-se-referme-sur-la-macronie/',
  'Analyse de 230 millions de tweets (août 2017 - décembre 2020) : le terme apparaît dans 73 806 messages (0,032 %) ; les comptes les plus impliqués sont « tous idéologiquement d’extrême-droite » ; forte hausse à partir d’octobre 2020, après les interventions de ministres. Limites : données Twitter seules, catégories issues d’un algorithme, interprétations de l’auteur (« piège », alt-right).',
  'Mesure empirique de la circulation du terme par un chercheur du CNRS ; interprétations à distinguer des données.', 'etude');
const MARLIERE = src('The « Islamo-gauchiste threat » as political nudge (French Cultural Studies)', 'Philippe Marlière (University College London), revue à comité de lecture', '2023',
  'https://discovery.ucl.ac.uk/id/eprint/10166996/1/09571558231152992.pdf',
  'Pierre-André Taguieff a promu le terme dans son livre de 2002 sur la « nouvelle judéophobie » et a ensuite affirmé l’avoir forgé en 2000 pour décrire une alliance de fait entre islamistes et extrême gauche ; l’attribution à Chris Harman (SWP) par Pascal Bruckner est contestée, Harman concluant que les islamistes ne peuvent être des alliés naturels de la gauche ; avant 2020 le terme circulait surtout dans les réseaux d’extrême droite ; trois ministres ont contribué à le banaliser en quatre mois.',
  'Article universitaire évalué par les pairs.', 'etude');
const PARIS_COMMUNE = src('Les 150 ans de la Commune : la fin sanglante et les conséquences (5/5)', 'Ville de Paris', 'Mis à jour le 7 avril 2021',
  'https://www.paris.fr/pages/les-150-ans-de-la-commune-la-fin-sanglante-et-les-consequences-5-5-17210',
  'Pas de « réel consensus parmi les historiens » sur le nombre de morts : entre 3 000 et 5 000 fédérés morts au combat et environ 20 000 autres massacrés ; 500 à 800 Versaillais tués ; environ une centaine d’otages exécutés par les fédérés, dont l’archevêque Georges Darboy.',
  'Page historique d’une collectivité publique (commémoration).');
const MEMORIAL = src('Les Juifs de France dans la Shoah (panneaux d’exposition itinérante)', 'Mémorial de la Shoah', '2016',
  'https://memorialdelashoah.org/wp-content/uploads/2016/04/les-juifs-de-france-kakemono-caisse_155.pdf',
  '« Sur les 330 000 Juifs vivant en France en 1939, 76 000 d’entre eux ont été déportés et assassinés » ; panneaux « La législation antisémite » et « Une propagande antisémite acharnée ».',
  'Institution de référence sur l’histoire de la Shoah.');

function remplacerSource(f, ancienneUrl, nouvelle) {
  const i = f.sources.findIndex((s) => s.url === ancienneUrl);
  if (i >= 0) { f.sources[i] = nouvelle; return i; }
  const j = f.sources.findIndex((s) => s.url === nouvelle.url);
  if (j >= 0) return j;
  f.sources.push(nouvelle); return f.sources.length - 1;
}

{
  const f = lire('islamo-gauchisme-origine-usages');
  const iP = remplacerSource(f, 'https://fr.wikipedia.org/wiki/Islamo-gauchisme', POLITOSCOPE);
  const iM = remplacerSource(f, 'https://en.wikipedia.org/wiki/Islamo-leftism', MARLIERE);
  f.faits[3] = { ...f.faits[3], fait: 'Selon l’analyse de 230 millions de tweets par le chercheur du CNRS David Chavalarias (Politoscope, février 2021), le terme reste très marginal (0,032 % des messages), est porté surtout par des comptes d’extrême droite, et son usage explose à partir d’octobre 2020, après les interventions de ministres.', source: iP, periode: 'Août 2017 - décembre 2020', fiabilite: 'estimation', chiffre: '0,032 %' };
  f.faits[4] = { ...f.faits[4], fait: 'Selon le politiste Philippe Marlière (French Cultural Studies, 2023), le terme a été promu par Pierre-André Taguieff dans un livre de 2002, qui dit l’avoir forgé pour décrire une alliance de fait entre islamistes et extrême gauche ; l’attribution au trotskiste britannique Chris Harman est contestée, Harman concluant au contraire que les islamistes ne sont pas des alliés naturels de la gauche.', source: iM, fiabilite: 'debat' };
  f.limites = [...new Set([...(f.limites || []).filter((l) => !/Wikip/i.test(l)), 'L’analyse du Politoscope repose sur Twitter seul ; ses conclusions sur une stratégie délibérée relèvent de l’interprétation.'])];
  // correction d'une erreur : la hausse date d'octobre 2020, pas d'octobre 2019
  for (const k of ['resume', 'explication', 'contexte']) if (typeof f[k] === 'string') f[k] = f[k].replace(/octobre 2019/g, 'octobre 2020');
  for (const k of ['court', 'moyen', 'detaille', 'empathie']) if (f.argumentaires?.[k]) f.argumentaires[k] = f.argumentaires[k].replace(/octobre 2019/g, 'octobre 2020');
  ecrire(f); journal.push('islamo-gauchisme-origine-usages : 2 sources encyclopédiques remplacées (Politoscope/CNRS, French Cultural Studies) ; date erronée « octobre 2019 » corrigée en « octobre 2020 ».');
}
{
  const f = lire('islamo-gauchisme-judeo-bolchevisme-comparaison');
  const iA = f.sources.findIndex((s) => /aoc/i.test(s.organisme));
  const iW = f.sources.findIndex((s) => /wikip/i.test(s.organisme));
  f.faits[0] = { ...f.faits[0], fait: 'Le rapprochement entre « islamo-gauchisme » et « judéo-bolchevisme » est présent dans le débat intellectuel, jusque dans le titre de l’analyse du philosophe Anoush Ganjipour (AOC) : « Du judéo-bolchevisme à l’islamo-gauchisme : significations d’un écart ».', source: iA, fiabilite: 'etabli' };
  if (iW >= 0 && !f.faits.some((x) => x.source === iW)) {
    f.sources.splice(iW, 1);
    for (const x of f.faits) if (x.source > iW) x.source -= 1;
  }
  ecrire(f); journal.push('islamo-gauchisme-judeo-bolchevisme-comparaison : fait reposant sur Wikipédia réécrit à partir de la source AOC ; source encyclopédique retirée.');
}
{
  const f = lire('commune-paris-1871');
  const iP = remplacerSource(f, '__aucune__', PARIS_COMMUNE);
  const i1 = 1; const i3 = 3;
  f.faits[i1] = { ...f.faits[i1], fait: 'Le nombre de morts de la Semaine sanglante ne fait pas consensus parmi les historiens : la Ville de Paris évoque 3 000 à 5 000 fédérés tués au combat et environ 20 000 autres massacrés, contre 500 à 800 Versaillais tués.', source: iP, fiabilite: 'debat', chiffre: '20 000' };
  f.faits[i3] = { ...f.faits[i3], fait: 'Les fédérés ont exécuté environ une centaine d’otages, dont l’archevêque de Paris Georges Darboy.', source: iP, fiabilite: 'etabli' };
  const used = new Set(f.faits.map((x) => x.source));
  const keep = f.sources.map((s, i) => used.has(i) || !/wikip/i.test(s.organisme));
  const remap = []; let n = 0; keep.forEach((k, i) => { remap[i] = k ? n++ : -1; });
  f.sources = f.sources.filter((_, i) => keep[i]);
  for (const x of f.faits) x.source = remap[x.source];
  ecrire(f); journal.push('commune-paris-1871 : 2 faits reposant sur Wikipédia ré-sourcés (Ville de Paris) ; le fait défavorable aux communards (exécution d’otages) est conservé.');
}
{
  const f = lire('judeo-bolchevisme-histoire');
  const iM = remplacerSource(f, '__aucune__', MEMORIAL);
  if (!f.faits.some((x) => x.source === iM)) {
    f.faits.push({ fait: 'Sur les 330 000 Juifs vivant en France en 1939, 76 000 ont été déportés et assassinés.', periode: '1940-1944', perimetre: 'France', explication: 'La désignation des Juifs comme ennemis intérieurs a précédé et accompagné leur persécution.', source: iM, fiabilite: 'etabli', chiffre: '76 000' });
  }
  ecrire(f); journal.push('judeo-bolchevisme-histoire : ajout d’un fait du Mémorial de la Shoah (bilan de la persécution en France).');
}
{
  const f = lire('aider-tout-le-monde');
  if (!/^D’après/.test(f.faits[0].fait)) f.faits[0].fait = `D’après les données de la DREES relayées par l’Observatoire des inégalités, ${f.faits[0].fait.charAt(0).toLowerCase()}${f.faits[0].fait.slice(1)}`;
  ecrire(f);
}

// ── 2. Attribution explicite des faits non appuyés par une source d'autorité ─
const court = (o) => String(o || '').split(/\s[(—–]|,\s/)[0].trim();
const NOMS = { 'Institut Montaigne': 'l’Institut Montaigne', 'Cabinet Kohen Avocats': 'le cabinet Kohen Avocats', 'Connaissance des Énergies': 'le site Connaissance des Énergies', 'La finance pour tous': 'le site La finance pour tous', Larousse: 'l’encyclopédie Larousse', WebLex: 'le site WebLex', 'Herodote.net': 'le site Herodote.net', 'Fondation iFRAP': 'la Fondation iFRAP' };
const MOTS_COMMUNS = /^(Le|La|Les|L['’]|En|Un|Une|Pour|Au|Aux|À|Son|Sa|Ses|Dans|Depuis|Il|Elle|Ils|Ce|Cette|Ces|À l['’]origine|Selon)\b/;
const minuscule = (t) => (MOTS_COMMUNS.test(t) ? t.charAt(0).toLowerCase() + t.slice(1) : t);
const attribuer = (t, org) => `Selon ${NOMS[court(org)] || court(org)}, ${minuscule(t)}`;
let attribues = 0;
for (const fichier of readdirSync(DIR).filter((x) => x.endsWith('.json'))) {
  const f = JSON.parse(readFileSync(join(DIR, fichier), 'utf8'));
  if (f.type === 'science') continue;
  let modif = false;
  for (const p of auditFiche(f)) {
    const m = p.match(/^fait (\d+) : (présenté comme établi sans source d’autorité|repose sur une source d’origine)/);
    if (!m) continue;
    const x = f.faits[Number(m[1])]; const s = f.sources[x.source];
    if (/^Selon /.test(x.fait)) continue;
    x.fait = attribuer(x.fait, s.organisme);
    modif = true; attribues += 1;
  }
  // reprise des attributions générées par une version précédente (forme brute « Selon Organisme, minuscule… »)
  for (const x of f.faits) {
    const s = f.sources[x.source]; if (!s) continue;
    const brut = `Selon ${court(s.organisme)}, `;
    if (x.fait.startsWith(brut) && NOMS[court(s.organisme)] !== undefined) {
      const reste = x.fait.slice(brut.length);
      const original = reste.charAt(0).toUpperCase() + reste.slice(1);
      x.fait = attribuer(original, s.organisme); modif = true;
    }
  }
  if (modif) ecrire(f);
}
journal.push(`${attribues} faits rendus explicitement attribués (« Selon … ») parce que leur source n’est pas une autorité (vulgarisation, source partisane ou de droite).`);

// ── 3. Lecture de gauche ─────────────────────────────────────────────────
let lectures = 0;
for (const [id, lecture] of Object.entries(LECTURES)) {
  try { const f = lire(id); f.lecture = lecture; ecrire(f); lectures += 1; } catch { journal.push(`lecture ignorée : fiche ${id} absente`); }
}
journal.push(`${lectures} fiches dotées d’une « lecture de gauche ».`);

// ── Bilan ─────────────────────────────────────────────────────────────────
let restants = 0;
for (const fichier of readdirSync(DIR).filter((x) => x.endsWith('.json'))) {
  const f = JSON.parse(readFileSync(join(DIR, fichier), 'utf8'));
  if (f.type === 'science') continue;
  const p = auditFiche(f);
  if (p.length) { restants += 1; journal.push(`À CORRIGER — ${f.id} : ${p.join(' ; ')}`); }
}
journal.push(`Fiches encore non conformes à la politique documentaire : ${restants}.`);
console.log(journal.join('\n'));
void classerSource; void LE_CLASSES;
