// Corpus « L'Avenir en commun » : parcourt la table des matières du programme et relève, chapitre par chapitre,
// les sections, la mesure clé et les mesures à puces. Résultat : data/moteur/aec.json (versionné).
// Le texte est recopié tel quel (citations), avec l'adresse exacte de chaque chapitre et la date de relevé.
import { blocs, liens } from './html.js';
import { lire, pause } from './reseau.js';

export const AEC_INDEX = 'https://melenchon2027.fr/programme/livre/';
const CHAPITRE_RE = /\/programme\/livre\/([a-z0-9-]+)\/chapitre(\d+)\/?$/;
const NAVIGATION = /^(pr[ée]c[ée]dent|suivant|partager|lire la suite|retour|accueil|menu|sommaire)\b/i;

// Volet de l'application selon la partie (et, au besoin, le chapitre) du programme
const VOLET_PARTIE = {
  'pour-une-bifurcation-ecologique-et-sociale': 'ecologie',
  'une-economie-au-service-des-besoins': 'economie',
  'mettre-en-securite-sociale': 'social',
  'le-gout-du-futur-aux-nouvelles-frontieres-de-l-humanite': 'services',
  'fonder-la-6e-republique': 'politique',
  'un-monde-ordonne': 'international',
};
const VOLET_CHAPITRE = {
  'mettre-en-securite-sociale/2': 'droits', 'mettre-en-securite-sociale/3': 'droits', 'mettre-en-securite-sociale/4': 'immigration',
  'fonder-la-6e-republique/2': 'securite', 'un-monde-ordonne/1': 'politique',
};
export const voletChapitre = (partie, n) => VOLET_CHAPITRE[`${partie}/${n}`] || VOLET_PARTIE[partie] || 'politique';

/** Analyse une page de chapitre (structure observée : h2 partie, h1 chapitre, h3 sections, h6 « Mesure clé », puces). */
export function analyserChapitre(html, url) {
  const b = blocs(html);
  const i1 = b.findIndex((x) => x.balise === 'h1');
  if (i1 < 0) return null;
  const partieTitre = [...b.slice(0, i1)].reverse().find((x) => x.balise === 'h2' && /partie/i.test(x.texte))?.texte || '';
  const m = url.match(CHAPITRE_RE);
  const chap = { url, partie: m ? m[1] : '', numero: m ? Number(m[2]) : 0, partie_titre: partieTitre, titre: b[i1].texte, sections: [] };
  chap.volet = voletChapitre(chap.partie, chap.numero);
  let sec = null;
  let attendreMesureCle = false;
  for (const x of b.slice(i1 + 1)) {
    if (NAVIGATION.test(x.texte)) { if (sec) break; continue; }
    if (x.balise === 'h1' || x.balise === 'h2') break;
    if (x.balise === 'h3') { sec = { titre: x.texte, intro: '', mesure_cle: '', mesures: [] }; chap.sections.push(sec); continue; }
    if (!sec) continue;
    if (/^h[4-6]$/.test(x.balise)) { attendreMesureCle = /mesure cl/i.test(x.texte); continue; }
    if (x.balise === 'p') {
      if (attendreMesureCle) { sec.mesure_cle = x.texte; attendreMesureCle = false; } else if (!sec.mesures.length && sec.intro.length < 1200) sec.intro = `${sec.intro} ${x.texte}`.trim();
      continue;
    }
    if (x.balise === 'li' && x.texte.length >= 15 && x.texte.length <= 500) sec.mesures.push(x.texte);
  }
  chap.sections = chap.sections.filter((s) => s.mesure_cle || s.mesures.length);
  return chap;
}

/** Liste des chapitres à partir de la table des matières. */
export function chapitresDepuisIndex(html, base = AEC_INDEX) {
  return [...new Set(liens(html, base).map((u) => u.replace(/\/?$/, '/')).filter((u) => CHAPITRE_RE.test(u) && u.startsWith(new URL(base).origin)))];
}

/** Relève tout le programme. Échoue (sans rien écraser) si le résultat est manifestement incomplet. */
export async function releverAec({ fetchImpl = fetch, index = AEC_INDEX, attente = 800, journal = console } = {}) {
  const urls = chapitresDepuisIndex(await lire(index, { fetchImpl }), index);
  if (urls.length < 5) throw new Error(`table des matières illisible (${urls.length} chapitre(s) trouvés)`);
  const chapitres = [];
  let diagnostic = false;
  for (const u of urls) {
    try {
      const html = await lire(u, { fetchImpl });
      const c = analyserChapitre(html, u);
      if (c?.sections.length) chapitres.push(c);
      else {
        journal.warn?.(`chapitre sans mesure reconnue : ${u}`);
        // diagnostic (une fois) : structure lue, pour adapter l'analyse si le site change de présentation
        if (!diagnostic) { diagnostic = true; journal.warn?.(`structure lue : ${blocs(html).slice(0, 60).map((x) => `${x.balise}:${x.texte.slice(0, 50)}`).join(' | ')} — taille ${html.length}, balises ${JSON.stringify(compterBalises(html))}`); }
      }
    } catch (e) { journal.warn?.(`chapitre non lu : ${e.message}`); }
    await pause(attente);
  }
  const nbMesures = chapitres.reduce((n, c) => n + c.sections.reduce((k, s) => k + (s.mesure_cle ? 1 : 0) + s.mesures.length, 0), 0);
  if (chapitres.length < urls.length * 0.6 || nbMesures < 50) throw new Error(`relevé incomplet : ${chapitres.length}/${urls.length} chapitres, ${nbMesures} mesures`);
  return { source: index, titre: 'L’Avenir en commun (programme de la France insoumise, édition 2027)', releve_le: new Date().toISOString().slice(0, 10), nb_chapitres: chapitres.length, nb_mesures: nbMesures, chapitres };
}

function compterBalises(html) {
  const n = {};
  for (const m of String(html).matchAll(/<(h[1-6]|p|li|ul|section|article|main|div)\b/gi)) n[m[1].toLowerCase()] = (n[m[1].toLowerCase()] || 0) + 1;
  return n;
}

/** Mesures à plat, avec leur contexte (pour la recherche). */
export function mesuresAPlat(corpus) {
  const out = [];
  for (const c of corpus?.chapitres || []) {
    for (const s of c.sections) {
      if (s.mesure_cle) out.push({ texte: s.mesure_cle, cle: true, section: s.titre, chapitre: c.titre, url: c.url, volet: c.volet });
      for (const t of s.mesures) out.push({ texte: t, cle: false, section: s.titre, chapitre: c.titre, url: c.url, volet: c.volet });
    }
  }
  return out;
}
