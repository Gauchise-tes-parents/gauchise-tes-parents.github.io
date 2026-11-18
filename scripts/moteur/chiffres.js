// Chiffres officiels tenus à jour automatiquement (API publique d'Eurostat, sans clé, format JSON-stat).
// Résultat : data/moteur/chiffres.json. Un indicateur illisible garde sa dernière valeur connue (jamais inventée).
import { lire } from './reseau.js';

const API = 'https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/';
const PAGE = (code) => `https://ec.europa.eu/eurostat/databrowser/view/${code}/default/table?lang=fr`;

// mots : radicaux qui rattachent l'indicateur à une question ; domaines : volets de l'application
export const INDICATEURS = [
  { id: 'chomage', libelle: 'taux de chômage en France (corrigé des variations saisonnières)', unite: '% de la population active', jeu: 'une_rt_m', filtres: { geo: 'FR', s_adj: 'SA', age: 'TOTAL', sex: 'T', unit: 'PC_ACT' }, mots: ['chomage', 'chomeur', 'emploi', 'boulot', 'licenci', 'usine'], domaines: [] },
  { id: 'inflation', libelle: 'hausse des prix à la consommation sur un an en France (indice harmonisé)', unite: '%', jeu: 'prc_hicp_manr', filtres: { geo: 'FR', coicop: 'CP00', unit: 'RCH_A' }, mots: ['prix', 'inflation', 'pouvoir d achat', 'vie chere', 'courses', 'cher'], domaines: [] },
  { id: 'dette', libelle: 'dette publique de la France', unite: '% du PIB', jeu: 'gov_10dd_edpt1', filtres: { geo: 'FR', na_item: 'GD', sector: 'S13', unit: 'PC_GDP' }, mots: ['dette', 'endette', 'faillite', 'budget de l etat', 'nos enfants paieront'], domaines: ['economie'] },
  { id: 'deficit', libelle: 'déficit public de la France (solde des administrations publiques)', unite: '% du PIB', jeu: 'gov_10dd_edpt1', filtres: { geo: 'FR', na_item: 'B9', sector: 'S13', unit: 'PC_GDP' }, mots: ['deficit', 'depense publique', 'depenses publiques', 'argent public', 'trop d impots'], domaines: [] },
  { id: 'pauvrete', libelle: 'taux de risque de pauvreté en France (sous 60 % du revenu médian, après transferts)', unite: '% de la population', jeu: 'ilc_li02', filtres: { geo: 'FR' }, mots: ['pauvre', 'pauvrete', 'rsa', 'precaire', 'precarite', 'misere', 'assist', 'modeste', 'fin de mois', 'smic', 'allocation'], domaines: ['social'] },
  { id: 'inegalites', libelle: 'rapport entre les revenus des 20 % les plus aisés et des 20 % les plus modestes en France (S80/S20)', unite: 'fois', jeu: 'ilc_di11', filtres: { geo: 'FR', age: 'TOTAL', sex: 'T' }, mots: ['inegalite', 'riche', 'richesse', 'partage', 'fortune'], domaines: ['economie', 'social', 'droits'] },
  { id: 'emploi', libelle: 'taux d’emploi des 20-64 ans en France', unite: '% de la population de 20 à 64 ans', jeu: 'lfsi_emp_a', filtres: { geo: 'FR', age: 'Y20-64', sex: 'T', unit: 'PC_POP', indic_em: 'EMP_LFS' }, mots: ['emploi', 'travailler', 'actifs', 'bosser'], domaines: [] },
  { id: 'renouvelables', libelle: 'part des énergies renouvelables dans la consommation finale brute d’énergie en France', unite: '%', jeu: 'nrg_ind_ren', filtres: { geo: 'FR', nrg_bal: 'REN', unit: 'PC' }, mots: ['renouvelable', 'eolien', 'solaire', 'energie', 'electricite', 'nucleaire'], domaines: ['ecologie'] },
  { id: 'ges', libelle: 'total des émissions de gaz à effet de serre de la France déclarées à l’Union européenne (hors postes pour mémoire)', unite: 'millions de tonnes équivalent CO2', jeu: 'env_air_gge', filtres: { geo: 'FR', airpol: 'GHG', src_crf: 'TOTXMEMONIA', unit: 'MIO_T' }, mots: ['climat', 'rechauffement', 'co2', 'carbone', 'emission', 'pollution', 'ecolo'], domaines: ['ecologie'] },
];

/** Extrait l'unique série d'une réponse JSON-stat et en garde la dernière observation. */
export function lireJsonStat(js) {
  const ids = js?.id || [];
  const tailles = js?.size || [];
  const iTemps = ids.indexOf('time');
  if (iTemps < 0 || !js.value) throw new Error('réponse sans dimension temporelle');
  const multiples = ids.map((d, i) => (i !== iTemps && tailles[i] !== 1 ? `« ${d} » à ${tailles[i]} valeurs (${Object.keys(js.dimension?.[d]?.category?.index || {}).slice(0, 12).join(', ')})` : null)).filter(Boolean);
  if (multiples.length) throw new Error(`filtre incomplet : ${multiples.join(' ; ')}`);
  const periodes = Object.entries(js.dimension.time.category.index).sort((a, b) => a[1] - b[1]).map(([p]) => p);
  for (let k = periodes.length - 1; k >= 0; k -= 1) {
    const v = js.value[String(k)];
    if (v != null && Number.isFinite(Number(v))) return { valeur: Number(v), periode: periodes[k], mise_a_jour_source: js.updated || null };
  }
  throw new Error('aucune valeur');
}

export async function releverChiffres({ fetchImpl = fetch, anciens = {}, journal = console } = {}) {
  const out = { source: 'Eurostat (office statistique de l’Union européenne), API publique', releve_le: new Date().toISOString().slice(0, 10), indicateurs: {} };
  const changements = [];
  for (const ind of INDICATEURS) {
    const qs = new URLSearchParams({ ...ind.filtres, format: 'JSON', lang: 'fr', lastTimePeriod: '4' });
    const url = `${API}${ind.jeu}?${qs}`;
    const prec = anciens.indicateurs?.[ind.id];
    try {
      const r = lireJsonStat(await lire(url, { fetchImpl, type: 'json' }));
      out.indicateurs[ind.id] = { id: ind.id, libelle: ind.libelle, unite: ind.unite, valeur: r.valeur, periode: r.periode, jeu: ind.jeu, url_api: url, url: PAGE(ind.jeu), mise_a_jour_source: r.mise_a_jour_source, releve_le: out.releve_le };
      if (prec && (prec.valeur !== r.valeur || prec.periode !== r.periode)) changements.push(`${ind.libelle} : ${prec.valeur} (${prec.periode}) → ${r.valeur} (${r.periode})`);
    } catch (e) {
      journal.warn?.(`indicateur ${ind.id} non relevé : ${e.message}`);
      if (prec) out.indicateurs[ind.id] = { ...prec, erreur_dernier_releve: e.message.slice(0, 200) };
    }
  }
  return { chiffres: out, changements };
}

/** Phrase factuelle et source d'un indicateur, au format des fiches. */
export function factuel(ind) {
  const v = String(ind.valeur).replace('.', ',');
  return {
    phrase: `Selon Eurostat, le ${ind.libelle} est de ${v} ${ind.unite === '%' ? '%' : ind.unite} (${ind.periode}).`.replace(' % de', ' % de'),
    source: {
      titre: `Eurostat — jeu de données ${ind.jeu} (${ind.libelle})`,
      organisme: 'Eurostat (office statistique de l’Union européenne)',
      date_publication: `données ${ind.periode}, relevées le ${ind.releve_le}`,
      url: ind.url,
      passage: `Dernière valeur publiée : ${v} ${ind.unite} pour la période ${ind.periode} (relevé automatique de l’API publique d’Eurostat le ${ind.releve_le}).`,
      pertinence: 'Statistique publique européenne de référence.',
      type: 'primaire',
      consultee: true,
    },
  };
}
