// Source unique de vérité pour les modes, volets thématiques, profils et contextes.
// Importé à la fois par le serveur (validation, consignes au modèle) et par l'interface.

export const TIPEEE_URL = 'https://fr.tipeee.com/martyducanda/';

export const MODES = {
  gagner: {
    label: 'GAGNER LE DÉBAT',
    carte: 'GAGNER LE DÉBAT',
    sousTitre: 'Tu ne le convaincras peut-être pas. Mais toute la table t’écoute.',
    description: 'Prépare des arguments solides, des réponses incisives et une démonstration qui marque les esprits.',
    bouton: 'Préparer ma riposte',
    court: 'Gagner le débat',
  },
  convaincre: {
    label: 'CONVAINCRE SANS BRAQUER',
    carte: 'CONVAINCRE AVEC EMPATHIE',
    sousTitre: 'Comprendre ses inquiétudes pour ouvrir une autre perspective.',
    description: 'Comprends ses préoccupations et trouve la bonne manière d’expliquer les faits.',
    bouton: 'Préparer le dialogue',
    court: 'Convaincre sans braquer',
  },
};

export const VOLETS = [
  {
    id: 'immigration', label: 'Immigration, intégration et discriminations', court: 'Immigration',
    sousThemes: ['Immigration et démographie', 'Immigration de travail', 'Asile et réfugiés', 'Nationalité et accès aux droits', 'Intégration', 'Économie et immigration', 'Immigration et finances publiques', 'Délinquance et immigration', 'Logement', 'Discriminations', 'Racisme', 'Comparaisons européennes', 'Histoire des migrations'],
    exemples: ['Les immigrés touchent plus d’aides que les Français.', 'L’immigration coûte une fortune à la France.'],
  },
  {
    id: 'securite', label: 'Sécurité, justice et libertés', court: 'Sécurité',
    sousThemes: ['Délinquance', 'Violences', 'Homicides', 'Violences sexuelles', 'Violences intrafamiliales', 'Police et gendarmerie', 'Justice pénale', 'Prisons', 'Récidive', 'Sécurité du quotidien', 'Criminalité organisée', 'Comparaisons statistiques', 'Prévention et politiques publiques'],
    exemples: ['La délinquance augmente partout.', 'La justice est laxiste, personne ne va en prison.'],
  },
  {
    id: 'social', label: 'Assistanat, travail et aides sociales', court: 'Aides sociales',
    sousThemes: ['RSA', 'Allocations familiales', 'Aides au logement', 'Chômage', 'Fraude sociale', 'Fraude fiscale', 'Conditions d’accès aux prestations', 'Emploi et salaires', 'Précarité', 'Pauvreté', 'Minimum social et niveau de vie', 'Coût et efficacité des aides', 'Revenus du travail et du patrimoine'],
    exemples: ['Les chômeurs ne veulent pas travailler.', 'Avec le RSA, on gagne autant qu’au SMIC.'],
  },
  {
    id: 'economie', label: 'Économie, capitalisme et pouvoir d’achat', court: 'Économie',
    sousThemes: ['Inflation', 'Salaires', 'Prix alimentaires', 'Loyers', 'Marges et profits', 'Grandes entreprises', 'PME et artisans', 'Fiscalité', 'Patrimoine', 'Dividendes', 'Dette publique', 'Déficit public', 'Services publics', 'Répartition des richesses', 'Inégalités économiques', 'Comparaisons internationales'],
    exemples: ['Les impôts ne servent qu’à payer l’assistanat.', 'Taxer les riches les fera tous partir.'],
  },
  {
    id: 'ecologie', label: 'Écologie, énergie et agriculture', court: 'Écologie',
    sousThemes: ['Changement climatique', 'Émissions de gaz à effet de serre', 'Nucléaire', 'Énergies renouvelables', 'Prix de l’énergie', 'Transports', 'Agriculture', 'Pesticides', 'Biodiversité', 'Rénovation thermique', 'Industrie', 'Justice climatique', 'Transition énergétique et emploi'],
    exemples: ['La France ne pollue presque pas, ça ne sert à rien de faire des efforts.', 'Les éoliennes ne servent à rien.'],
  },
  {
    id: 'services', label: 'Santé, éducation et services publics', court: 'Services publics',
    sousThemes: ['Hôpital public', 'Médecins et déserts médicaux', 'Assurance maladie', 'École publique', 'Inégalités scolaires', 'Université', 'Éducation prioritaire', 'Services publics locaux', 'Transports collectifs', 'Accès aux soins', 'Fonction publique', 'Financement des services essentiels'],
    exemples: ['Il y a trop de fonctionnaires en France.', 'L’hôpital a plein d’argent, il est juste mal géré.'],
  },
  {
    id: 'droits', label: 'Droits, société et égalité', court: 'Droits et égalité',
    sousThemes: ['Féminisme', 'Égalité salariale', 'Violences faites aux femmes', 'Droits des personnes LGBT', 'Laïcité', 'Libertés publiques', 'Discriminations', 'Handicap et accessibilité', 'Droits des travailleurs', 'Égalité des chances', 'Émancipation', 'Histoire des conquêtes sociales'],
    exemples: ['L’égalité salariale hommes-femmes, c’est réglé.', 'Les discriminations à l’embauche, ça n’existe plus.'],
  },
  {
    id: 'politique', label: 'Politique, médias et démocratie', court: 'Politique et médias',
    sousThemes: ['France insoumise', 'Rassemblement national', 'Droite et extrême droite', 'Gauche et pluralisme politique', 'Programmes électoraux', 'Institutions françaises', 'Constitution', 'Médias', 'Désinformation', 'Sondages', 'Abstention', 'Financement politique', 'Union européenne', 'Souveraineté', 'Démocratie directe', 'Comparaisons internationales', 'Histoire politique contemporaine'],
    exemples: ['Les médias cachent volontairement la vérité.', 'Le RN défend les travailleurs.'],
  },
  {
    id: 'international', label: 'Histoire, géopolitique et international', court: 'International',
    sousThemes: ['Histoire sociale', 'Histoire économique', 'Histoire du mouvement ouvrier', 'Colonisation et décolonisation', 'Guerres et conflits', 'Palestine et Israël', 'Relations internationales', 'États-Unis', 'Europe', 'Chine', 'Russie', 'Amérique latine', 'Institutions internationales', 'Comparaisons entre modèles économiques et sociaux'],
    exemples: ['Les congés payés, c’est le patronat qui les a offerts.', 'Le modèle social français est le pire d’Europe.'],
  },
  {
    id: 'autre', label: 'Autre sujet', court: 'Autre sujet',
    sousThemes: [],
    exemples: [],
  },
];

export const VOLET_IDS = VOLETS.map((v) => v.id);
export const voletById = (id) => VOLETS.find((v) => v.id === id) || VOLETS[VOLETS.length - 1];

// Les profils servent uniquement à adapter le ton et la pédagogie de la réponse en cours.
export const PROFILS = [
  ['mystere', 'Mystère total', 'Tu ne le connais pas assez.'],
  ['convaincu', 'Le convaincu', 'Défend fermement sa position.'],
  ['sceptique', 'Le sceptique', 'Demande des preuves, se méfie des discours politiques.'],
  ['colerique', 'Le colérique', 'Ça peut vite monter en tension.'],
  ['pragmatique', 'Le pragmatique', 'Cherche des solutions concrètes.'],
  ['preoccupe', 'Le préoccupé', 'S’inquiète pour la sécurité, le pouvoir d’achat ou l’avenir.'],
  ['provocateur', 'Le provocateur', 'Lance des phrases choc pour faire réagir.'],
  ['curieux', 'Le curieux', 'Ouvert à d’autres points de vue.'],
];

export const CONTEXTES = [
  ['repas', 'Repas de famille'],
  ['amis', 'Entre amis'],
  ['prive', 'Conversation privée en ligne'],
  ['reseaux', 'Réseaux sociaux'],
  ['public', 'Débat public'],
  ['preparation', 'Préparation personnelle'],
];

export const DUREES = [[30, '30 secondes'], [60, '1 minute'], [180, '3 minutes']];

export const VERDICTS = {
  confirme: 'Confirmé par les données consultées',
  plutot_exact: 'Plutôt exact, mais incomplet',
  trompeur: 'Trompeur ou hors contexte',
  contredit: 'Contredit par les données consultées',
  inverifiable: "Impossible à vérifier en l'état",
  opinion: "Question d'opinion ou de valeurs",
};

export const NATURES = {
  fait: 'Fait vérifié',
  interpretation: 'Interprétation',
  valeur: 'Jugement de valeur',
  proposition: 'Proposition politique',
};

export const LIMITS = { claimMax: 600, commentMax: 1000 };

// ─── Base de connaissances v3 ────────────────────────────────────────────────
// Rubriques transversales : une fiche peut appartenir à plusieurs rubriques, en plus de son volet.
export const RUBRIQUES = [
  {
    id: 'patriotisme-de-gauche', label: 'Patriotisme de gauche', court: 'Patriotisme de gauche',
    description: 'Souveraineté populaire, Résistance, programme du CNR, Sécurité sociale, conquêtes sociales, souverainetés industrielle, alimentaire et énergétique. Et la différence entre patriotisme, nationalisme et chauvinisme.',
    avertissement: "La gauche n'a pas le monopole du patriotisme, et toute la droite n'est pas hostile aux conquêtes sociales : ces fiches montrent une tradition, pas une exclusivité.",
  },
  {
    id: 'islamo-gauchisme-laicite', label: '« Islamo-gauchisme », laïcité et instrumentalisation', court: 'Islamo-gauchisme et laïcité',
    description: "Origine et usages du terme, loi de 1905, distinction entre critique d'une religion et discrimination, débats internes à la gauche, histoire du mythe du « judéo-bolchevisme » et comparaison rigoureuse des mécanismes rhétoriques.",
    avertissement: "Comparer des mécanismes de propagande n'est pas assimiler : les deux expressions n'ont ni le même contexte, ni les mêmes cibles, ni la même gravité historique.",
  },
  {
    id: 'melenchon-lfi', label: '« Mélenchon crie, il est agressif, il est dangereux »', court: 'Mélenchon et LFI',
    description: "Les critiques fréquentes adressées à Jean-Luc Mélenchon et à La France insoumise, chacune en cinq parties : le reproche, les faits vérifiables, la réponse, les objections légitimes et une formulation simple à table.",
    avertissement: "Ces fiches ne blanchissent personne : elles distinguent le style, le fond et les comportements légitimement critiquables, et signalent ce qui reste discutable.",
  },
  {
    id: 'science-du-dialogue', label: 'Science du dialogue', court: 'Science du dialogue',
    description: "Ce que la psychologie sociale, la sociologie et la science politique disent de la persuasion : réactance, raisonnement motivé, identité, valeurs morales, écoute, désinformation, délibération, et la frontière entre persuasion et manipulation.",
    avertissement: "Ces résultats décrivent des tendances moyennes observées dans des conditions précises, souvent hors de France. Ils guident la manière de discuter ; ils ne permettent pas de diagnostiquer une personne.",
  },
];
export const RUBRIQUE_IDS = RUBRIQUES.map((r) => r.id);
export const rubriqueById = (id) => RUBRIQUES.find((r) => r.id === id) || null;

// Niveau de fiabilité global d'une fiche (et de chaque fait).
export const FIABILITES = {
  etabli: 'Fait solidement établi',
  estimation: 'Estimation',
  interpretation: 'Interprétation',
  debat: 'Débat historiographique ou politique',
};

// Stabilité dans le temps : décide si une recherche web complémentaire est utile.
export const STABILITES = {
  historique: 'Fait historique stable',
  evolutive: 'Donnée qui évolue (à actualiser)',
  actualite: "Sujet d'actualité",
};

export const TYPES_FICHE = {
  idee_recue: 'Idée reçue',
  reference: 'Fiche de référence',
  reponse_critique: 'Réponse à une critique',
  histoire: 'Fiche historique',
  science: 'Fiche scientifique',
};

// Robustesse des résultats scientifiques (fiches « science »).
export const ROBUSTESSES = {
  robuste: 'Résultat robuste',
  modere: 'Résultat modéré ou à confirmer',
  controverse: 'Résultat discuté',
  hypothese: 'Hypothèse',
};

// Onglets d'une fiche, dans l'ordre d'affichage.
export const FICHE_TABS = [
  ['court', 'Réponse en 15 secondes'],
  ['moyen', 'Argumentaire en 1 minute'],
  ['detaille', 'Développement en 3 minutes'],
  ['sources', 'Sources et preuves'],
  ['contre', 'Contre-arguments'],
  ['contexte', 'Contexte historique'],
  ['empathie', 'Réponse avec empathie'],
];

// ─── Questionnaire rapide sur l'interlocuteur (toutes les réponses sont facultatives) ───────
// Ce sont des hypothèses de travail fournies par l'utilisateur, pas un diagnostic de personnalité.
export const INTERLOCUTEUR = [
  { id: 'debat', label: 'Rapport au débat', essentiel: true, options: [['calme', 'Calme'], ['competitif', 'Compétitif'], ['provocateur', 'Provocateur'], ['susceptible', 'Susceptible'], ['evite', 'Évite le conflit'], ['hesitant', 'Hésitant']] },
  { id: 'faits', label: 'Ce qui le convainc', essentiel: true, options: [['chiffres', 'Chiffres et statistiques'], ['exemples', 'Exemples concrets'], ['temoignages', 'Témoignages'], ['logique', 'Raisonnement logique'], ['experience', 'Expérience personnelle']] },
  { id: 'autorite', label: 'Rapport aux institutions et aux sources', essentiel: true, options: [['confiance', 'Fait confiance aux institutions'], ['mefiance', 'Se méfie des institutions'], ['independantes', 'Préfère les sources indépendantes']] },
  { id: 'changement', label: 'Rapport au changement', options: [['prudent', 'Prudent'], ['pragmatique', 'Pragmatique'], ['reformiste', 'Réformiste'], ['rupture', 'Favorable aux ruptures']] },
  { id: 'valeurs', label: 'Valeurs prioritaires (3 au plus)', multi: 3, options: [['justice_sociale', 'Justice sociale'], ['securite', 'Sécurité'], ['liberte', 'Liberté'], ['ordre', 'Ordre'], ['solidarite', 'Solidarité'], ['merite', 'Mérite'], ['egalite', 'Égalité'], ['tradition', 'Tradition'], ['souverainete', 'Souveraineté'], ['protection_groupe', 'Protection du groupe']] },
  { id: 'connaissance', label: 'Ce qu’il sait du sujet', options: [['faible', 'Peu de choses'], ['moyenne', 'Un peu'], ['elevee', 'Beaucoup']] },
  { id: 'politique', label: 'Rapport à la politique', options: [['engage', 'Très engagé'], ['partisan', 'Partisan'], ['desabuse', 'Désabusé'], ['peu_informe', 'Peu informé'], ['ouvert', 'Ouvert à la discussion']] },
  { id: 'lien', label: 'Ton lien avec lui ou elle', options: [['parent', 'Parent'], ['ami', 'Ami'], ['collegue', 'Collègue'], ['conjoint', 'Conjoint'], ['connaissance', 'Connaissance'], ['public', 'Débat public']] },
  { id: 'cadre', label: 'Contexte', options: [['prive', 'Discussion privée'], ['repas', 'Repas de famille'], ['plusieurs', 'Conversation à plusieurs'], ['reseaux', 'Réseaux sociaux']] },
  { id: 'objectif', label: 'Ton objectif', options: [['reflechir', 'Faire réfléchir'], ['riposter', 'Répondre à une attaque'], ['corriger', 'Corriger une information'], ['terrain', 'Trouver un terrain d’entente'], ['evoluer', 'Faire évoluer une opinion']] },
];
export const RETOURS = [
  ['ecoute', 'La personne a écouté'],
  ['braque', 'Elle s’est braquée'],
  ['preuves', 'Elle a demandé une source ou une preuve'],
  ['truquees', 'Elle dit que les chiffres sont truqués'],
  ['causes', 'D’accord sur le constat, pas sur les causes'],
  ['solution', 'D’accord sur le problème, pas sur la solution'],
  ['hesite', 'Elle hésite'],
  ['diversion', 'Elle a changé de sujet'],
  ['concede', 'Elle a reconnu un point'],
  ['fin', 'La discussion est terminée'],
];
