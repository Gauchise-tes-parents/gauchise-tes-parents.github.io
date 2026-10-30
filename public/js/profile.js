// Profil de l'interlocuteur : nettoyage, consignes justifiées et table de décision documentée.
// Les profils sont des HYPOTHÈSES DE TRAVAIL fournies par l'utilisateur : rien n'est déduit, rien n'est diagnostiqué.
// Chaque consigne renvoie à une fiche « Science du dialogue » et indique son fondement :
//   « recherche »  : appuyée sur des résultats publiés (fiche citée) ;
//   « pratique »   : choix de communication raisonnable, sans démonstration empirique directe (signalé comme tel).
import { INTERLOCUTEUR, PROFILS } from './taxonomy.js';

export const profilVide = () => ({ inconnu: true });

/** Garde uniquement des valeurs connues (listes fermées). */
export function nettoyerProfil(p = {}) {
  const out = { inconnu: Boolean(p && p.inconnu) };
  if (!p || typeof p !== 'object' || out.inconnu) return { inconnu: true };
  for (const d of INTERLOCUTEUR) {
    const ok = new Set(d.options.map(([k]) => k));
    if (d.multi) {
      const v = Array.isArray(p[d.id]) ? [...new Set(p[d.id].filter((x) => ok.has(x)))].slice(0, d.multi) : [];
      if (v.length) out[d.id] = v;
    } else if (ok.has(p[d.id])) out[d.id] = p[d.id];
  }
  if (Object.keys(out).length === 1) out.inconnu = true;
  return out;
}

export const has = (p, dim, v) => (Array.isArray(p[dim]) ? p[dim].includes(v) : p[dim] === v);
const any = (p, dim, vals) => vals.some((v) => has(p, dim, v));

// ─── Consignes (une par option ou groupe d'options) ─────────────────────────
export const REGLES = [
  { id: 'inconnu', quand: (p) => p.inconnu, titre: 'Profil neutre : commencer par comprendre', consigne: 'Tu ne connais pas assez cette personne : commence par une question ouverte pour comprendre son point de vue, puis un seul fait vérifiable.', fiche: 'sci-entretien-motivationnel', fondement: 'recherche' },
  { id: 'calme', quand: (p) => has(p, 'debat', 'calme'), titre: 'Elle discute calmement', consigne: 'Un échange posé permet de présenter plusieurs éléments et d’entrer dans le détail.', fiche: 'sci-deliberation', fondement: 'pratique' },
  { id: 'confrontation', quand: (p) => has(p, 'debat', 'competitif'), titre: 'Elle aime la confrontation', consigne: 'Réponse courte, ferme et structurée : une idée centrale et une preuve vérifiable. Ne multiplie pas les arguments ; demande une preuve précise pour toute affirmation contestable.', fiche: 'sci-persuasion-modeste', fondement: 'pratique' },
  { id: 'provocation', quand: (p) => has(p, 'debat', 'provocateur'), titre: 'Elle cherche surtout à provoquer', consigne: 'Pas d’escalade : identifie la seule affirmation qui mérite une réponse, refuse les détournements et prévois une phrase courte pour les personnes qui écoutent.', fiche: 'sci-polarisation-groupe', fondement: 'pratique' },
  { id: 'susceptible', quand: (p) => any(p, 'debat', ['susceptible', 'evite']), titre: 'Elle se braque facilement', consigne: 'Reformule et pose une question ouverte AVANT tout contre-argument ; évite ce qui peut la faire passer pour mal informée ; laisse-lui le droit de ne pas changer d’avis tout de suite.', fiche: 'sci-reactance', fondement: 'recherche' },
  { id: 'hesitant', quand: (p) => has(p, 'debat', 'hesitant'), titre: 'Elle hésite', consigne: 'Propose plusieurs pistes et reconnais les incertitudes plutôt que de forcer une conclusion.', fiche: 'sci-autonomie', fondement: 'pratique' },
  { id: 'chiffres', quand: (p) => any(p, 'faits', ['chiffres', 'logique']), titre: 'Elle aime les chiffres ou la logique', consigne: 'Des données sourcées, comparables, avec ordres de grandeur, période, périmètre et limites. Pas d’avalanche de statistiques.', fiche: 'sci-raisonnement-motive', fondement: 'pratique' },
  { id: 'experience', quand: (p) => any(p, 'faits', ['experience', 'temoignages', 'exemples']), titre: 'Elle raisonne par l’expérience ou l’exemple', consigne: 'Pars d’un exemple concret ou de son vécu, reconnais qu’il est réel pour elle, puis mets-le en perspective avec des données plus générales.', fiche: 'sci-persuasion-modeste', fondement: 'recherche' },
  { id: 'mefiance', quand: (p) => any(p, 'autorite', ['mefiance', 'independantes']), titre: 'Elle se méfie des institutions ou préfère les sources indépendantes', consigne: 'Montre d’où viennent les données, comment elles sont calculées et leurs limites ; ajoute une source indépendante concordante quand il y en a une. Ne réponds pas « les experts l’ont dit », mais n’écarte pas pour autant les données publiques.', fiche: 'sci-desinformation-confiance', fondement: 'recherche' },
  { id: 'confiance', quand: (p) => has(p, 'autorite', 'confiance'), titre: 'Elle fait confiance aux institutions', consigne: 'Appuie-toi d’abord sur la source officielle (organisme, date, document).', fiche: 'sci-desinformation-confiance', fondement: 'pratique' },
  { id: 'prudent', quand: (p) => has(p, 'changement', 'prudent'), titre: 'Elle est prudente face au changement', consigne: 'Insiste sur ce qui est établi et sur les risques ; présente des pas progressifs plutôt qu’un bouleversement.', fiche: 'sci-dissonance', fondement: 'pratique' },
  { id: 'pragmatique', quand: (p) => has(p, 'changement', 'pragmatique'), titre: 'Elle est pragmatique', consigne: 'Parle de résultats mesurables et de conséquences concrètes, plus que de principes.', fiche: 'sci-valeurs-morales', fondement: 'pratique' },
  { id: 'reformiste', quand: (p) => has(p, 'changement', 'reformiste'), titre: 'Elle est réformiste', consigne: 'Mets en avant les améliorations possibles et les exemples institutionnels qui ont fonctionné.', fiche: 'sci-valeurs-morales', fondement: 'pratique' },
  { id: 'rupture', quand: (p) => has(p, 'changement', 'rupture'), titre: 'Elle est favorable aux ruptures', consigne: 'Elle accepte l’idée de changements profonds : montre l’ampleur du problème et les choix structurels, sans exagérer les faits.', fiche: 'sci-valeurs-morales', fondement: 'pratique' },
  { id: 'securite', quand: (p) => any(p, 'valeurs', ['securite', 'ordre']), titre: 'Elle tient à l’ordre et à la sécurité', consigne: 'Pars de sa préoccupation pour la sécurité ; examine les résultats mesurables des politiques. Ne caricature pas sa volonté de sécurité.', fiche: 'sci-menace-biologie', fondement: 'recherche' },
  { id: 'justice', quand: (p) => any(p, 'valeurs', ['justice_sociale', 'egalite', 'solidarite']), titre: 'Elle tient à la justice sociale', consigne: 'Pars des situations vécues et des inégalités ; relie les chiffres à des conséquences concrètes, en présentant les arbitrages et les limites.', fiche: 'sci-valeurs-morales', fondement: 'recherche' },
  { id: 'merite', quand: (p) => any(p, 'valeurs', ['merite', 'liberte']), titre: 'Elle tient au mérite ou à la liberté', consigne: 'Présente le fait sous l’angle du travail récompensé, de la responsabilité ou de la liberté de choix, sans changer les faits.', fiche: 'sci-valeurs-morales', fondement: 'recherche' },
  { id: 'nation', quand: (p) => any(p, 'valeurs', ['souverainete', 'tradition', 'protection_groupe']), titre: 'Elle tient à la nation, à la tradition ou à son groupe', consigne: 'Appuie-toi sur l’histoire commune et la fierté collective (conquêtes sociales, institutions) pour présenter les faits.', fiche: 'sci-valeurs-morales', fondement: 'recherche' },
  { id: 'connaissance_faible', quand: (p) => has(p, 'connaissance', 'faible') || has(p, 'politique', 'peu_informe'), titre: 'Elle connaît peu le sujet', consigne: 'Reste simple et concret : un fait clair, des mots courants, pas de jargon ni de sigles.', fiche: 'sci-autonomie', fondement: 'pratique' },
  { id: 'connaissance_elevee', quand: (p) => has(p, 'connaissance', 'elevee'), titre: 'Elle connaît bien le sujet', consigne: 'Va au détail : méthode, période, périmètre, limites ; anticipe l’objection la plus sérieuse.', fiche: 'sci-raisonnement-motive', fondement: 'pratique' },
  { id: 'identite', quand: (p) => any(p, 'politique', ['partisan', 'engage']), titre: 'Elle est très attachée à son camp', consigne: 'Ne l’humilie pas et ne présente pas son camp comme mauvais par nature ; reconnais d’abord ce qui est fondé dans sa position ; propose des faits à examiner sans exiger de capitulation.', fiche: 'sci-identite-sociale', fondement: 'recherche' },
  { id: 'desabuse', quand: (p) => has(p, 'politique', 'desabuse'), titre: 'Elle est désabusée', consigne: 'Évite les étiquettes de partis ; pars du quotidien et de ce qui peut changer concrètement.', fiche: 'sci-autonomie', fondement: 'pratique' },
  { id: 'ouvert', quand: (p) => has(p, 'politique', 'ouvert'), titre: 'Elle est ouverte à la discussion', consigne: 'Tu peux proposer plusieurs angles et entrer dans le détail.', fiche: 'sci-deliberation', fondement: 'pratique' },
  { id: 'famille', quand: (p) => any(p, 'lien', ['parent', 'conjoint']), titre: 'C’est un proche', consigne: 'Rappelle que le désaccord ne change rien au lien ; reconnais l’histoire familiale avant d’exposer ton point de vue.', fiche: 'sci-famille-socialisation', fondement: 'recherche' },
  { id: 'ami', quand: (p) => has(p, 'lien', 'ami'), titre: 'C’est un ami', consigne: 'La franchise est possible : dis clairement ton désaccord, en gardant le respect.', fiche: 'sci-autonomie', fondement: 'pratique' },
  { id: 'collegue', quand: (p) => has(p, 'lien', 'collegue'), titre: 'C’est un collègue', consigne: 'Reste bref et factuel ; évite que le désaccord déborde sur le travail.', fiche: 'sci-deliberation', fondement: 'pratique' },
  { id: 'connaissance_lien', quand: (p) => has(p, 'lien', 'connaissance'), titre: 'C’est une simple connaissance', consigne: 'Pas de lien à préserver à tout prix : reste factuel et courtois, sans chercher à convaincre à tout prix.', fiche: 'sci-persuasion-modeste', fondement: 'pratique' },
  { id: 'prive', quand: (p) => has(p, 'cadre', 'prive'), titre: 'Discussion en tête-à-tête', consigne: 'Sans public, la personne peut changer d’avis sans perdre la face : tu peux approfondir.', fiche: 'sci-dissonance', fondement: 'recherche' },
  { id: 'repas', quand: (p) => has(p, 'cadre', 'repas'), titre: 'Repas de famille', consigne: 'Relation personnelle et risque de conflit : une question vaut souvent mieux qu’un long argumentaire ; propose de reprendre plus tard si ça monte.', fiche: 'sci-communication-non-violente', fondement: 'pratique' },
  { id: 'public', quand: (p) => any(p, 'cadre', ['plusieurs', 'reseaux']) || has(p, 'lien', 'public'), titre: 'D’autres personnes écoutent', consigne: 'Le vrai public, ce sont aussi les autres : une phrase claire et vérifiable, sans attaque personnelle ; n’exige pas d’aveu en public.', fiche: 'sci-polarisation-groupe', fondement: 'recherche' },
  { id: 'reflechir', quand: (p) => has(p, 'objectif', 'reflechir'), titre: 'Objectif : faire réfléchir', consigne: 'Termine par une question plutôt que par une conclusion.', fiche: 'sci-entretien-motivationnel', fondement: 'recherche' },
  { id: 'riposter', quand: (p) => has(p, 'objectif', 'riposter'), titre: 'Objectif : répondre à une attaque', consigne: 'Réponse courte, vérifiable, sans digression ; vise aussi ceux qui écoutent.', fiche: 'sci-polarisation-groupe', fondement: 'pratique' },
  { id: 'corriger', quand: (p) => has(p, 'objectif', 'corriger'), titre: 'Objectif : corriger une information', consigne: 'Donne le bon chiffre, sa source et pourquoi l’autre est faux ; propose une explication de remplacement.', fiche: 'sci-backfire', fondement: 'recherche' },
  { id: 'terrain', quand: (p) => has(p, 'objectif', 'terrain'), titre: 'Objectif : trouver un terrain d’entente', consigne: 'Commence par ce sur quoi vous êtes d’accord ; cherche une valeur commune.', fiche: 'sci-valeurs-morales', fondement: 'recherche' },
  { id: 'evoluer', quand: (p) => has(p, 'objectif', 'evoluer'), titre: 'Objectif : faire évoluer une opinion', consigne: 'Vise un petit pas, pas une conversion ; échange des expériences plutôt qu’empiler des arguments.', fiche: 'sci-persuasion-modeste', fondement: 'recherche' },
  { id: 'ethique', quand: () => true, titre: 'Règle de base', consigne: 'Faits exacts et sourcés, aucune pression ni chantage affectif ; l’autre reste libre de vérifier et d’être en désaccord.', fiche: 'sci-persuasion-manipulation', fondement: 'recherche' },
];

/** Consignes applicables à un profil. */
export function strategieProfil(profil) {
  const p = nettoyerProfil(profil);
  return { profil: p, regles: REGLES.filter((r) => r.quand(p)) };
}

/** Correspondance avec les 8 profils simples utilisés par le moteur connecté. */
export function profilSimple(profil) {
  const p = nettoyerProfil(profil);
  if (p.inconnu) return 'mystere';
  if (p.debat === 'provocateur') return 'provocateur';
  if (p.debat === 'competitif') return 'convaincu';
  if (p.debat === 'susceptible') return 'colerique';
  if (p.autorite === 'mefiance' || p.autorite === 'independantes') return 'sceptique';
  if ((p.valeurs || []).some((v) => v === 'securite' || v === 'ordre')) return 'preoccupe';
  if (p.changement === 'pragmatique') return 'pragmatique';
  if (p.politique === 'ouvert' || p.debat === 'hesitant') return 'curieux';
  return PROFILS[0][0];
}

/** Résumé lisible, présenté comme une hypothèse. */
export function resumeProfil(profil) {
  const p = nettoyerProfil(profil);
  if (p.inconnu) return 'Profil neutre (tu ne connais pas assez cette personne)';
  const parts = [];
  for (const d of INTERLOCUTEUR) {
    const v = p[d.id];
    if (!v) continue;
    parts.push((Array.isArray(v) ? v : [v]).map((x) => d.options.find(([k]) => k === x)?.[1]).filter(Boolean).join(', ').toLowerCase());
  }
  return parts.join(' · ');
}

// ─── Table de décision documentée : ce que chaque choix change dans le moteur ─────────────
// info : ce que le choix apporte ; influence : éléments du plan modifiés ; neutre : quand il ne doit rien changer.
export const DECISIONS = {
  mode: {
    gagner: { info: 'Objectif de l’échange : convaincre le public présent, même si l’interlocuteur reste campé.', influence: ['entree', 'detail', 'ordre', 'conclusion', 'ton', 'stratégie ouverte par défaut'], neutre: 'Les faits et les sources restent identiques dans les deux modes.' },
    convaincre: { info: 'Objectif : faire avancer la personne elle-même, sans la braquer.', influence: ['entree', 'questions', 'ordre', 'conclusion', 'ton', 'stratégie ouverte par défaut'], neutre: 'Les faits et les sources restent identiques dans les deux modes.' },
  },
  volet: { info: 'Thème de la question.', influence: ['choix de la fiche (départage des correspondances)'], neutre: 'Quand l’affirmation correspond fortement à une fiche, le volet ne la remplace pas.' },
  debat: {
    calme: { info: 'Échange posé.', influence: ['detail'], neutre: 'Ne change ni l’approche ni les preuves.' },
    competitif: { info: 'Aime la confrontation.', influence: ['detail', 'entree', 'ton', 'conclusion', 'nombre de preuves'], neutre: 'N’autorise aucun raccourci factuel.' },
    provocateur: { info: 'Cherche à faire réagir.', influence: ['detail', 'ton', 'conclusion', 'recentrage', 'phrase pour le public'], neutre: 'Ne change pas les faits.' },
    susceptible: { info: 'Se braque vite.', influence: ['entree', 'ton', 'ordre (questions avant contre-argument)', 'nombre de preuves'], neutre: 'Les faits ne sont pas atténués.' },
    evite: { info: 'Évite le conflit.', influence: ['entree', 'ton', 'ordre'], neutre: 'Les faits ne sont pas atténués.' },
    hesitant: { info: 'Hésite.', influence: ['conclusion (plusieurs pistes)', 'incertitudes mises en avant', 'ton', 'ordre (demander ce qui fait hésiter)'], neutre: 'Ne fabrique pas d’incertitude là où les faits sont établis.' },
  },
  faits: {
    chiffres: { info: 'Sensible aux données.', influence: ['approche (factuelle)', 'choix des preuves (chiffrées)', 'detail', 'méthode affichée'], neutre: 'Si la fiche n’a pas de chiffre, le moteur le signale au lieu d’en inventer.' },
    logique: { info: 'Sensible au raisonnement.', influence: ['approche (factuelle)', 'ordre', 'conclusion (synthèse)'], neutre: '—' },
    exemples: { info: 'Sensible aux exemples concrets.', influence: ['approche (valeurs et conséquences)', 'entree (exemple)', 'choix des preuves (conséquences concrètes)'], neutre: 'Aucun exemple n’est inventé : seuls les faits de la fiche sont utilisés.' },
    temoignages: { info: 'Sensible aux récits.', influence: ['approche (valeurs et conséquences)', 'entree'], neutre: 'Aucun témoignage n’est inventé.' },
    experience: { info: 'Raisonne par son vécu.', influence: ['entree (reconnaître le vécu)', 'approche', 'questions'], neutre: '—' },
  },
  autorite: {
    confiance: { info: 'Fait confiance aux institutions.', influence: ['source mise en avant (institutionnelle)', 'choix des preuves'], neutre: '—' },
    mefiance: { info: 'Se méfie des institutions.', influence: ['méthode affichée', 'sources concordantes', 'objection anticipée', 'questions', 'prochaine étape'], neutre: 'Les données publiques restent utilisées : le moteur montre leur méthode, il ne les écarte pas.' },
    independantes: { info: 'Préfère les sources indépendantes.', influence: ['source mise en avant (indépendante si disponible)', 'sources concordantes'], neutre: 'Les médias et institutions ne sont pas exclus automatiquement.' },
  },
  connaissance: {
    faible: { info: 'Connaît peu le sujet.', influence: ['detail (bref)', 'ton (pédagogique)', 'preuves plus courtes', 'questions'], neutre: '—' },
    moyenne: { info: 'Connaît un peu le sujet.', influence: [], neutre: 'Valeur par défaut : aucun changement volontaire.' },
    elevee: { info: 'Connaît bien le sujet.', influence: ['detail (approfondi)', 'méthode', 'objection anticipée'], neutre: '—' },
  },
};

export function decisionFor(dim, val) {
  return DECISIONS[dim]?.[val] || null;
}
