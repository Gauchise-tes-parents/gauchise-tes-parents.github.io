// Banc d'essai du moteur de personnalisation : scénarios synthétiques et critères explicites.
// Ces tests vérifient la cohérence et la traçabilité du moteur ; ils NE mesurent PAS l'efficacité persuasive
// sur de vraies personnes.
import { composer, planifier, suite } from '../../public/js/composer.js';
import { kbMatch } from '../../public/js/kbsearch.js';
import { nettoyerProfil } from '../../public/js/profile.js';
import { extractNumbers } from '../../server/engine/util.js';

export const FICHES_TEST = [
  'impots-assistanat', 'rsa-smic', 'chomeurs-travailler', 'delinquance-partout', 'justice-laxiste-prison', 'immigration-chiffres-definitions',
  'immigres-aides', 'electricite-nucleaire-renouvelables', 'dividendes-salaires', 'securite-sociale-1945', 'front-populaire-1936',
  'laicite-loi-1905', 'lfi-antisemite', 'melenchon-crie', 'gauche-laicite-debats', 'commune-paris-1871',
];

export const PROFILS_TEST = {
  neutre: { inconnu: true },
  chiffres: { faits: 'chiffres', connaissance: 'elevee' },
  mefiant: { autorite: 'mefiance' },
  braque: { debat: 'susceptible' },
  confrontation: { debat: 'competitif', objectif: 'riposter' },
  provocateur_public: { debat: 'provocateur', cadre: 'reseaux' },
  vecu: { faits: 'experience', valeurs: ['justice_sociale'] },
  securitaire: { valeurs: ['securite', 'ordre'], changement: 'prudent' },
  hesitant: { debat: 'hesitant', connaissance: 'faible' },
  parent_repas: { lien: 'parent', cadre: 'repas', debat: 'evite' },
  patriote: { valeurs: ['souverainete', 'tradition'], politique: 'partisan' },
  correcteur: { objectif: 'corriger', autorite: 'independantes', faits: 'logique' },
};

/** Attentes explicites par option du profil (vérifiées seulement quand elles ne sont pas en concurrence). */
export function attentes(p, plans, fiche, a) {
  const v = [];
  const g = plans.gagner;
  const c = plans.convaincre;
  const blocsC = a.convaincre.blocs.map((b) => b.type);
  const nbChiffres = fiche.faits.filter((f) => f.chiffre).length;
  const check = (ok, msg) => { if (!ok) v.push(msg); };
  if (p.inconnu) check(c.entree === 'question' && c.ordre.slice(0, 2).join() === 'entree,question' && c.questions.length > 0, 'profil neutre : la stratégie empathique doit commencer par des questions ouvertes');
  if (p.debat === 'competitif') check(g.max_preuves === 1 && g.ton === 'ferme', 'confrontation : une seule preuve, ton ferme');
  if (p.debat === 'provocateur') check(g.recentrage && g.max_preuves === 1, 'provocation : recentrage et réponse courte');
  if (p.debat === 'susceptible' || p.debat === 'evite') check(c.ordre.indexOf('question') > -1 && c.ordre.indexOf('question') < c.ordre.indexOf('preuves') && (g.ordre.indexOf('question') > -1 && g.ordre.indexOf('question') < g.ordre.indexOf('replique')), 'se braque : questions avant tout contre-argument (dans les deux modes)');
  if (p.debat === 'hesitant') check(c.conclusion === 'pistes', 'hésitant : plusieurs pistes plutôt qu’une conclusion');
  if (p.faits === 'chiffres') check(nbChiffres ? g.preuves[0].chiffre : g.incertitudes.some((x) => /pas de donnée chiffrée/.test(x)), 'chiffres : preuve chiffrée en tête, ou absence de chiffre signalée');
  if (p.faits === 'experience') check(['vecu', 'exemple', 'reformulation', 'question'].includes(c.entree), 'expérience : entrée par le vécu (sauf entrée prioritaire)');
  if (p.autorite === 'mefiance' || p.autorite === 'independantes') check(g.preuves.every((x) => x.methode), 'méfiance : méthode affichée pour chaque preuve');
  if ((p.valeurs || []).some((x) => x === 'securite' || x === 'ordre')) check(c.angles.includes('securite'), 'sécurité : angle sécurité présent');
  if ((p.valeurs || []).includes('justice_sociale')) check(c.angles.includes('justice'), 'justice sociale : angle justice présent');
  if ((p.valeurs || []).some((x) => x === 'souverainete' || x === 'tradition')) check(c.angles.includes('nation'), 'souveraineté : angle nation présent');
  if (p.cadre === 'reseaux' || p.cadre === 'plusieurs' || p.lien === 'public') check(g.public && g.conclusion === 'public', 'public présent : conclusion adressée au public');
  if (p.cadre === 'repas') check(blocsC.includes('texte') && c.apaisement, 'repas : proposition de pause dans la stratégie empathique');
  if (!p.lien && (c.ton === 'chaleureux')) v.push('ton « rappelle le lien » sans lien déclaré');
  if (c.entree === 'question' && c.ordre.includes('question')) check(c.ordre[c.ordre.indexOf('entree') + 1] === 'question', 'entrée « j’aimerais comprendre » non suivie des questions');
  if (p.lien === 'parent' || p.lien === 'conjoint') check(c.conclusion === 'lien' || c.conclusion === 'pistes', 'proche : conclusion sur le lien');
  if (p.connaissance === 'faible') check(g.ton === 'pedagogique' || g.ton === 'ferme' || g.ton === 'nuance' || c.ton === 'pedagogique' || c.ton === 'nuance' || c.ton === 'calme', 'connaissance faible : ton pédagogique ou nuancé');
  if (p.connaissance === 'elevee') check(g.detail !== 'bref' && g.preuves.every((x) => x.methode), 'connaissance élevée : détail et méthode');
  if (p.objectif === 'corriger') check(g.entree === 'correction', 'corriger : entrée par la correction expliquée');
  if (p.objectif === 'riposter') check(g.public, 'riposter : phrase pour le public');
  if (p.politique === 'partisan' && (fiche.objections_legitimes?.length || ['plutot_exact', 'trompeur'].includes(fiche.verdict))) check(g.entree === 'concession' || g.entree === 'correction', 'partisan : reconnaître d’abord un point fondé');
  return v;
}

const sansTitres = (x) => JSON.stringify(x, (k, val) => (k === 'index' || k === 'titre' ? undefined : val));

/** Vérifications communes de vérité et de traçabilité. */
export function verite(fiche, a) {
  const err = [];
  const nums = extractNumbers(JSON.stringify(fiche));
  for (const mode of ['gagner', 'convaincre']) {
    const extra = [...extractNumbers(sansTitres(a[mode].blocs))].filter((n) => !nums.has(n));
    if (extra.length) err.push(`${mode} : nombre absent de la fiche (${extra.join(', ')})`);
    for (const pr of a.plans[mode].preuves) {
      const f = fiche.faits[pr.index];
      if (!f || f.fait !== pr.texte) err.push(`${mode} : fait modifié ou inexistant`);
      const s = fiche.sources[f?.source];
      if (!s || !s.consultee || s.url !== pr.source?.url) err.push(`${mode} : source incohérente ou non consultée`);
    }
    const replique = a[mode].blocs.find((b) => b.type === 'replique');
    if (replique && replique.texte !== fiche.argumentaires.court) err.push(`${mode} : réponse courte modifiée`);
    // pas de duplication à l'intérieur d'une même réponse
    const morceaux = a[mode].blocs.flatMap((b) => [b.texte, ...(b.type === 'questions' ? b.items : [])]).filter(Boolean);
    const doublons = morceaux.filter((t, k) => morceaux.indexOf(t) !== k);
    if (doublons.length) err.push(`${mode} : texte répété dans la même réponse (« ${doublons[0].slice(0, 60)} »)`);
    const texte = sansTitres(a[mode].blocs);
    if (/(est (susceptible|méfiant|méfiante|provocat)|diagnostic|sa personnalité)/i.test(texte)) err.push(`${mode} : le profil est présenté comme un fait`);
  }
  return err;
}

function incertitudesOk(fiche, a, force) {
  const inc = [...a.plans.gagner.incertitudes, ...a.plans.convaincre.incertitudes].join(' ');
  const err = [];
  if (fiche.stabilite !== 'historique' && !/vérifi|actualis|évolu/i.test(inc)) err.push('ancienneté des données non signalée');
  if ((fiche.fiabilite === 'debat' || fiche.fiabilite === 'interpretation') && !/débattu|interprétatif/i.test(inc)) err.push('caractère débattu non signalé');
  if (force === 'partielle' && !/sujet voisin/.test(inc)) err.push('correspondance partielle non signalée');
  return err;
}

export const empreinte = (pl) => ({
  structure: pl.ordre.join('>'),
  preuves: pl.preuves.map((x) => x.index).join(','),
  ordre: pl.preuves.map((x) => x.index).join('>'),
  questions: pl.questions.join('|'),
  detail: `${pl.detail}${pl.preuves.some((x) => x.methode) ? '+méthode' : ''}`,
  strategie: `${pl.approche}/${pl.entree}/${pl.conclusion}`,
  objection: String(pl.objection?.index ?? '-'),
  contexte: `${pl.ton}/${pl.public}/${pl.lien}/${pl.apaisement}/${pl.recentrage}/${(pl.angles || []).join('+')}`,
});

/** Construit au moins 100 scénarios. */
export function construireScenarios(lib) {
  const byId = new Map(lib.map((f) => [f.id, f]));
  const sc = [];
  let n = 0;
  for (const id of FICHES_TEST) {
    const f = byId.get(id);
    for (const [nom, profil] of Object.entries(PROFILS_TEST)) {
      if ((n++ % 2) && !['neutre', 'chiffres', 'mefiant', 'braque'].includes(nom)) continue; // couverture tournante
      sc.push({ type: 'profil', id: `${id}/${nom}`, fiche: f, nom, profil });
    }
  }
  // échanges successifs (objections, preuves, désescalade)
  const seqs = [
    ['impots-assistanat', 'mefiant', ['truquees', 'preuves', 'ecoute', 'ecoute']],
    ['rsa-smic', 'braque', ['braque', 'braque']],
    ['delinquance-partout', 'securitaire', ['causes', 'solution', 'concede']],
    ['chomeurs-travailler', 'confrontation', ['preuves', 'diversion', 'diversion']],
    ['lfi-antisemite', 'patriote', ['hesite', 'ecoute', 'fin']],
    ['electricite-nucleaire-renouvelables', 'chiffres', ['ecoute', 'ecoute', 'ecoute', 'ecoute', 'ecoute']],
    ['immigres-aides', 'vecu', ['truquees', 'causes', 'concede', 'fin']],
    ['securite-sociale-1945', 'parent_repas', ['braque', 'hesite']],
  ];
  for (const [id, nom, retours] of seqs) sc.push({ type: 'echange', id: `${id}/${nom}/${retours.join('+')}`, fiche: byId.get(id), nom, profil: PROFILS_TEST[nom], retours });
  // questions saisies librement (correspondance, partielle, absente)
  const questions = [
    ['Les impôts servent à payer les assistés', 'impots-assistanat'],
    ['la police tue', 'lfi-contre-police'],
    ['Avec le RSA on gagne autant qu’en bossant', 'rsa-smic'],
    ['Mélenchon gueule tout le temps', 'melenchon-crie'],
    ['Le prix du pain au Moyen Âge', 'aucune'],
    ['Les extraterrestres contrôlent la Banque centrale', 'aucune'],
    ['La laïcité interdit les signes religieux dans la rue', 'laicite-loi-1905'],
    ['Les chômeurs profitent du système', 'chomeurs-travailler'],
  ];
  for (const [q, attendu] of questions) sc.push({ type: 'question', id: `question:${q}`, question: q, attendu, profil: PROFILS_TEST.neutre });
  // options facultatives absentes, invalides ou partielles : le parcours ne doit jamais bloquer
  const bizarres = [{}, { debat: 'inexistant' }, { valeurs: ['securite', 'merite', 'ordre', 'liberte', 'tradition'] }, { inconnu: true, debat: 'competitif' }, null, { lien: 'parent' }];
  bizarres.forEach((p, i) => sc.push({ type: 'facultatif', id: `facultatif-${i}`, fiche: byId.get(FICHES_TEST[i]), profil: p }));
  return sc;
}

/** Exécute un scénario et l'évalue selon les critères explicites. */
export function evaluer(s, lib) {
  const r = { id: s.id, type: s.type, ok: true, violations: [], erreurs: [], incertitudes: [] };
  try {
    if (s.type === 'question') {
      const m = kbMatch(lib.filter((f) => f.type !== 'science'), s.question);
      if (!m.length) { r.resultat = 'non couvert'; if (s.attendu !== 'aucune') r.violations.push('fiche attendue non trouvée'); r.ok = !r.violations.length; return r; }
      r.resultat = `${m[0].fiche.id} (${m[0].force})`;
      if (s.attendu === 'aucune') r.violations.push(`correspondance abusive avec ${m[0].fiche.id}`);
      else if (m[0].fiche.id !== s.attendu) r.violations.push(`fiche ${m[0].fiche.id} au lieu de ${s.attendu}`);
      const a = composer(m[0].fiche, s.profil, { bibliotheque: lib, force: m[0].force });
      r.erreurs.push(...verite(m[0].fiche, a));
      r.incertitudes.push(...incertitudesOk(m[0].fiche, a, m[0].force));
    } else if (s.type === 'echange') {
      const session = { utilises: [], objectionsVues: [], questionsPosees: [], retours: [] };
      const seen = new Set();
      const etapes = [];
      for (const ret of s.retours) {
        const x = suite(s.fiche, s.profil, ret, session, { bibliotheque: lib });
        session.retours.push(ret);
        if (x.utilise != null) {
          if (session.utilises.includes(x.utilise) && ret === 'ecoute') r.violations.push(`« ${ret} » : fait déjà présenté répété`);
          session.utilises.push(x.utilise);
        }
        if (x.objection != null) session.objectionsVues.push(x.objection);
        if (x.question) session.questionsPosees.push(x.question);
        if (!/approximative/.test(x.note)) r.violations.push('caractère approximatif non indiqué');
        if (x.preuve && x.preuve.texte !== s.fiche.faits[x.preuve.index].fait) r.erreurs.push('fait modifié dans la suite');
        const key = `${x.titre}|${x.texte}`;
        if (seen.has(key) && !['ecoute'].includes(ret)) r.violations.push(`réponse identique répétée après « ${ret} »`);
        seen.add(key);
        etapes.push(x.titre);
      }
      r.resultat = etapes.join(' → ');
    } else {
      const a = composer(s.fiche, s.profil, { bibliotheque: lib });
      r.plan = { gagner: empreinte(a.plans.gagner), convaincre: empreinte(a.plans.convaincre) };
      r.erreurs.push(...verite(s.fiche, a));
      r.incertitudes.push(...incertitudesOk(s.fiche, a));
      r.violations.push(...attentes(nettoyerProfil(s.profil), a.plans, s.fiche, a));
      if (!a.gagner.blocs.length || !a.convaincre.blocs.length) r.violations.push('stratégie vide');
      r.resultat = `${a.plans.gagner.approche}/${a.plans.gagner.entree} · ${a.plans.convaincre.approche}/${a.plans.convaincre.entree}`;
    }
  } catch (err) {
    r.erreurs.push(`exception : ${err.message}`);
  }
  r.ok = !r.violations.length && !r.erreurs.length && !r.incertitudes.length;
  return r;
}

/** Diversité : comparaison deux à deux des plans d'une même fiche, dimension par dimension. */
export function diversite(resultats) {
  const parFiche = new Map();
  for (const r of resultats.filter((x) => x.type === 'profil' && x.plan)) {
    const f = r.id.split('/')[0];
    if (!parFiche.has(f)) parFiche.set(f, []);
    parFiche.get(f).push(r);
  }
  const dims = ['structure', 'preuves', 'ordre', 'questions', 'detail', 'strategie', 'objection', 'contexte'];
  const compte = Object.fromEntries(dims.map((d) => [d, 0]));
  let paires = 0;
  let pertinentes = 0;
  let superficielles = 0;
  const listeSuperficielles = [];
  const identiques = [];
  for (const [f, rs] of parFiche) {
    for (let i = 0; i < rs.length; i++) for (let j = i + 1; j < rs.length; j++) {
      for (const mode of ['gagner', 'convaincre']) {
        paires += 1;
        const a = rs[i].plan[mode];
        const b = rs[j].plan[mode];
        const diff = dims.filter((d) => a[d] !== b[d]);
        diff.forEach((d) => { compte[d] += 1; });
        const fond = diff.filter((d) => d !== 'contexte');
        if (fond.length >= 2) pertinentes += 1;
        else if (diff.length) { superficielles += 1; listeSuperficielles.push(`${f} · ${mode} : ${rs[i].id.split('/')[1]} / ${rs[j].id.split('/')[1]} (diffèrent seulement par : ${diff.join(', ')})`); }
        else identiques.push(`${f} · ${mode} : ${rs[i].id.split('/')[1]} = ${rs[j].id.split('/')[1]}`);
      }
    }
  }
  return { paires, pertinentes, superficielles, listeSuperficielles, identiques, compte };
}

/** Profils qui NE justifient PAS de différence : le moteur doit produire exactement le même plan. */
export const PAIRES_TEMOINS = [
  [{ debat: 'calme' }, { debat: 'calme', connaissance: 'moyenne' }, 'connaissance « un peu » est la valeur par défaut'],
  [{ lien: 'parent' }, { lien: 'conjoint' }, 'deux proches : même consigne de lien'],
  [{ valeurs: ['justice_sociale'] }, { valeurs: ['egalite'] }, 'même angle de valeur (justice)'],
  [{ valeurs: ['securite', 'ordre'] }, { valeurs: ['ordre', 'securite'] }, 'ordre de saisie des valeurs'],
  [{ inconnu: true }, { inconnu: true, debat: 'competitif', faits: 'chiffres' }, '« je ne connais pas » annule les autres hypothèses'],
  [{ debat: 'calme' }, { debat: 'calme', religion: 'x', nom: 'Jean' }, 'champs hors questionnaire ignorés (aucune donnée personnelle)'],
];

export function temoins(lib) {
  const ids = FICHES_TEST.slice(0, 8);
  return PAIRES_TEMOINS.map(([a, b, raison]) => {
    const ecarts = [];
    for (const id of ids) {
      const f = lib.find((x) => x.id === id);
      const A = composer(f, a, { bibliotheque: lib });
      const B = composer(f, b, { bibliotheque: lib });
      for (const m of ['gagner', 'convaincre']) if (JSON.stringify(A[m].blocs) !== JSON.stringify(B[m].blocs)) ecarts.push(`${id}/${m}`);
    }
    return { a, b, raison, ok: !ecarts.length, ecarts };
  });
}

export function toutExecuter(lib) {
  const sc = construireScenarios(lib);
  const resultats = sc.map((s) => evaluer(s, lib));
  return { scenarios: sc, resultats, diversite: diversite(resultats), temoins: temoins(lib) };
}

/** Exemple comparatif : une affirmation, plusieurs profils. */
export function exempleComparatif(fiche, profils, lib) {
  return profils.map(([nom, p]) => {
    const a = composer(fiche, p, { bibliotheque: lib });
    return { nom, profil: p, gagner: a.plans.gagner, convaincre: a.plans.convaincre, blocsG: a.gagner.blocs, blocsC: a.convaincre.blocs };
  });
}
