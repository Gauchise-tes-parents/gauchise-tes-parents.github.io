// Microtextes de l'interface. Ils varient selon la situation ; les verdicts ne sont commentés
// qu'une fois l'analyse terminée.

export const QUIPS = {
  confirme: ['Bon… sur ce coup-là, les chiffres lui donnent raison.', 'Les sources sont d’accord avec lui. Ça arrive, et c’est utile de le savoir.'],
  plutot_exact: ['Pas faux, mais il manque un bout de l’histoire.', 'Le fond tient, les détails coincent.'],
  trompeur: ['Un fond de vérité, beaucoup de raccourcis.', 'Attention : cette statistique mérite un peu de contexte.'],
  contredit: ['Les sources ne sont pas du tout d’accord.', 'Les chiffres ont parlé, et ils ne disent pas ça.'],
  inverifiable: ['On a cherché, mais les sources ne permettent pas encore de conclure.', 'Personne ne peut trancher avec ce qu’on a sous la main.'],
  opinion: ['Ici, ce ne sont plus les chiffres qui tranchent, ce sont les valeurs.', 'Question de valeurs : les faits éclairent, ils ne décident pas.'],
  debat: ['Pas de verdict en un mot : il y a des faits, des objections sérieuses et du débat.', 'Ici, on démêle le vrai, le discutable et le critiquable.'],
};

export const LOADING = [
  'On va demander aux chiffres avant de s’énerver.',
  'La recherche est en cours. Ton oncle devra patienter.',
  'Une affirmation, une vérification, des sources.',
  'Doc Source ouvre les rapports officiels. Oui, même les PDF de 200 pages.',
  'On cherche aussi ce qui pourrait nous contredire. C’est le jeu.',
];

export const LOADING_STRATEGY = [
  'Les sources sont là. On prépare la façon de le dire.',
  'Même dossier, autre stratégie : ça va vite.',
];

export const STEPS_RESEARCH = [
  'Repérer ce qui se vérifie',
  'Chercher les sources officielles',
  'Ouvrir les documents',
  'Chercher ce qui contredit',
  'Construire la réponse',
];

export const pick = (list) => list[Math.floor(Math.random() * list.length)];
