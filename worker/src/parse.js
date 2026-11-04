// Lecture et contrôle de la réponse du modèle. Rien de ce que le modèle écrit n'est affiché sans contrôle :
// - les adresses web écrites par le modèle sont SUPPRIMÉES (seuls les liens réellement disponibles sont affichés :
//   documents de la bibliothèque et pages consultées par la recherche Google) ;
// - une référence « WEB » sans recherche effective, ou une référence inconnue, rend l'élément « non vérifié » ;
// - les champs sont bornés en nombre et en longueur.
const STATUTS = new Set(['fait', 'estimation', 'interpretation', 'opinion', 'non_verifie']);
const URL_RE = /\b(?:https?:\/\/|www\.)[^\s)>\]»"]+/gi;

export const sansUrl = (t, max = 1200) => String(t ?? '').replace(URL_RE, '').replace(/\(\s*\)/g, '').replace(/\s{2,}/g, ' ').trim().slice(0, max);

/** Extrait le premier objet JSON d'un texte (tolère un bloc ```json … ``` ou du texte autour). */
export function extraireJson(text) {
  const s = String(text || '').replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/i, '');
  const debut = s.indexOf('{');
  if (debut < 0) return null;
  let prof = 0; let dansChaine = false; let echap = false;
  for (let i = debut; i < s.length; i += 1) {
    const c = s[i];
    if (dansChaine) { if (echap) echap = false; else if (c === '\\') echap = true; else if (c === '"') dansChaine = false; continue; }
    if (c === '"') dansChaine = true;
    else if (c === '{') prof += 1;
    else if (c === '}') { prof -= 1; if (prof === 0) { try { return JSON.parse(s.slice(debut, i + 1)); } catch { return null; } } }
  }
  return null;
}

/**
 * Normalise la réponse. docs : documents de la bibliothèque (B1…), recherche : { requetes, pages } réellement consultées.
 * Renvoie { reponse, sources_utilisees } ou null si la réponse est inexploitable.
 */
export function normaliser(brut, { mode, docs, recherche }) {
  if (!brut || typeof brut !== 'object') return null;
  const web = recherche.pages.length > 0;
  const utilisees = new Set();
  let webCite = false;
  const refs = (liste) => {
    const out = [];
    let inconnue = false;
    for (const r of Array.isArray(liste) ? liste.slice(0, 6) : []) {
      const k = String(r).trim().toUpperCase();
      if (k === 'WEB') { if (web) { out.push('WEB'); webCite = true; } else inconnue = true; continue; }
      if (docs.some((d) => d.ref === k)) { out.push(k); utilisees.add(k); } else inconnue = true;
    }
    return { out: [...new Set(out)], inconnue };
  };
  const item = (x, champTexte = 'texte') => {
    if (!x || typeof x !== 'object') return null;
    const texte = sansUrl(x[champTexte], 900);
    if (!texte) return null;
    const { out, inconnue } = refs(x.sources);
    let statut = STATUTS.has(x.statut) ? x.statut : 'non_verifie';
    // un fait ou un chiffre présenté comme établi doit s'appuyer sur un document réellement disponible
    if ((statut === 'fait' || statut === 'estimation') && !out.length) statut = 'non_verifie';
    return { texte, statut, sources: out, ...(inconnue ? { reference_retiree: true } : {}) };
  };
  const liste = (v, n, f) => (Array.isArray(v) ? v.slice(0, n).map(f).filter(Boolean) : []);
  const reponse = {
    sujet: sansUrl(brut.sujet, 240),
    reponse_directe: sansUrl(brut.reponse_directe, mode === 'express' ? 700 : 1600),
    arguments: liste(brut.arguments, mode === 'express' ? 2 : 6, (x) => item(x)),
    chiffres: liste(brut.chiffres, 6, (x) => {
      const it = item({ ...x, texte: x?.valeur }, 'texte');
      return it ? { ...it, valeur: it.texte, contexte: sansUrl(x.contexte, 400) } : null;
    }),
    replique: sansUrl(brut.replique, 400),
    contre_arguments: liste(brut.contre_arguments, 5, (x) => (x?.objection && x?.reponse ? { objection: sansUrl(x.objection, 400), reponse: sansUrl(x.reponse, 700) } : null)),
    procedes: liste(brut.procedes, 5, (x) => (x?.nom ? { nom: sansUrl(x.nom, 80), explication: sansUrl(x.explication, 500) } : null)),
    inquietudes: liste(brut.inquietudes, 5, (x) => sansUrl(x, 300) || null),
    valeurs_communes: liste(brut.valeurs_communes, 5, (x) => sansUrl(x, 300) || null),
    questions: liste(brut.questions, 5, (x) => sansUrl(x, 300) || null),
    sections: liste(brut.sections, 8, (x) => { const it = item(x); return it ? { titre: sansUrl(x.titre, 80), ...it } : null; }),
    limites: sansUrl(brut.limites, 700),
  };
  if (!reponse.reponse_directe) return null;
  return {
    reponse,
    sources: {
      bibliotheque: docs.filter((d) => utilisees.has(d.ref)).map(({ ref, organisme, titre, date, url, fiche_id }) => ({ ref, organisme, titre, date, url, fiche_id })),
      // pages réellement consultées par la recherche Google (liens fournis par Google, souvent des liens de redirection)
      web: recherche.pages,
      web_cite: webCite,
    },
  };
}
