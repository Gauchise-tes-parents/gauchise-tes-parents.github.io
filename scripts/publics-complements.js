// Réponses selon le public (v14) pour des fiches dont le générateur n'existe plus ou n'est plus relancé.
// Textes écrits UNIQUEMENT à partir du contenu déjà sourcé de chaque fiche (résumé et faits).
// Appliqué par scripts/corrections-v10.js (idempotent : remplace le champ « publics » par la version ci-dessous).
// Ajouts du 7 novembre 2026 (passage de 12 h).
export const PUBLICS = {
  'immigres-aides': {
    convaincus: "Pour toucher le RSA, un étranger non européen doit en principe avoir un titre de séjour qui l'autorise à travailler depuis au moins cinq ans. Et selon l'OCDE, dans presque tous les pays étudiés, on dépense moins par immigré que par natif. Si leur contribution nette est plus faible, c'est surtout parce qu'ils ont moins souvent un emploi, pas parce qu'ils touchent plus.",
    indecis: "C'est une question qu'on entend souvent, et la réponse est plutôt rassurante : l'accès aux aides est encadré par des conditions de séjour. Selon l'OCDE, la dépense publique par immigré est plus faible que par natif dans presque tous les pays étudiés. Le vrai levier, c'est l'accès à l'emploi.",
  },
  'rsa-smic': {
    convaincus: "Fais le calcul : le RSA pour une personne seule, c'est 651,69 € par mois depuis avril 2026. Un SMIC à temps plein, c'est environ 1 443 € net. Le travail rapporte donc plus du double, sans même compter la prime d'activité.",
    indecis: "On entend souvent que le RSA vaudrait un salaire ; les montants officiels disent autre chose. Une personne seule touche 651,69 € par mois au RSA, contre environ 1 443 € net au SMIC à temps plein. Si le SMIC paraît insuffisant pour vivre, c'est un argument pour augmenter les salaires, pas pour baisser le RSA.",
  },
  'chomeurs-travailler': {
    convaincus: "France Travail a contrôlé les chômeurs : en 2023, 83 % des contrôles ont montré une recherche active ou une remobilisation, et près de 91 % quand les chômeurs étaient tirés au hasard. Il y a des abus, 17 % ont été sanctionnés, mais c'est une minorité. On ne peut pas juger des millions de gens sur cette minorité.",
    indecis: "C'est vrai qu'une partie des chômeurs contrôlés est sanctionnée, et il est légitime de vérifier. Mais les contrôles de France Travail montrent qu'une large majorité cherche vraiment du travail. Le chômage s'explique d'abord par le manque d'emplois adaptés, pas par la paresse.",
  },
  'laicite-loi-1905': {
    convaincus: "Relis la loi de 1905 : son article 1er dit que « la République assure la liberté de conscience » et garantit le libre exercice des cultes. C'est l'État qui doit être neutre, pas les citoyens. La laïcité protège aussi ta liberté de critiquer les religions.",
    indecis: "La laïcité est souvent mal comprise. La loi de 1905 impose la neutralité à l'État, qui ne reconnaît ni ne finance aucun culte, et garantit à chacun la liberté de croire ou de ne pas croire. Elle ne demande pas aux croyants de se cacher dans la rue.",
  },
  'musulmans-amalgames': {
    convaincus: "Les chiffres de l'enquête publique Trajectoires et Origines sont clairs : 44 % des immigrés se disent musulmans, donc la majorité ne l'est pas. Et être musulman, c'est une croyance ; l'islamisme, c'est un projet politique. Mettre tout le monde dans le même sac, c'est faire le jeu des islamistes, qui veulent parler au nom de tous.",
    indecis: "On peut s'inquiéter de l'islamisme sans soupçonner tous les musulmans. Selon l'Insee et l'Ined, 10 % des 18-59 ans se déclarent musulmans, et moins de la moitié des immigrés. Distinguer la croyance, le projet politique et le crime permet de combattre les vrais dangers.",
  },
  'souverainete-populaire': {
    convaincus: "La souveraineté n'appartient pas aux nationalistes : depuis 1789, elle vient de la nation, et la Constitution de 1958 dit qu'elle « appartient au peuple ». Défendre le droit du peuple à décider, par ses élus et par référendum, c'est une idée démocratique, pas une idée d'extrême droite.",
    indecis: "Vouloir que le peuple décide de son avenir est légitime, et c'est même inscrit dans la Constitution. La souveraineté populaire est née avec la Révolution française, pas avec le nationalisme. On peut la défendre tout en refusant de diviser les gens selon leur origine.",
  },
  'justice-laxiste-prison': {
    convaincus: "Les prisons n'ont jamais été aussi pleines : 84 741 détenus au 1er janvier 2026, contre 68 359 en 2022, et plus de 107 000 incarcérations en 2025. Plus de 6 500 détenus dorment sur un matelas par terre. On peut discuter de l'exécution des peines, mais dire que personne ne va en prison, c'est faux.",
    indecis: "Le sentiment que les délinquants ne sont pas punis existe, et l'exécution des peines mérite un débat. Mais les chiffres du ministère de la Justice montrent des prisons surpeuplées, à 136 % de leur capacité. Le problème est plutôt de savoir si la prison, dans ces conditions, protège vraiment de la récidive.",
  },
  'melenchon-ruiner-france': {
    convaincus: "Le programme coûte cher, personne ne le nie : le NFP l'a chiffré lui-même à environ 150 milliards d'ici 2027, financés en grande partie par de nouvelles recettes. Mais « ruiner », c'est un jugement : il s'agit de faire payer davantage les plus aisés et les grandes entreprises. On peut être contre, mais il faut discuter de qui paie, pas crier à la ruine.",
    indecis: "Le coût du programme est réel et se discute : l'Institut Montaigne l'estimait à 179 milliards par an, contre 71 pour le RN. La question est de savoir si les recettes prévues, surtout des impôts sur les plus aisés, suffiraient. C'est un choix de redistribution, dont les effets économiques sont débattus.",
  },
  'france-pays-immigration': {
    convaincus: "La France accueille des immigrés depuis plus d'un siècle : près de 3 % de la population en 1911, 6,6 % en 1931. Après 1918, puis pendant les Trente Glorieuses, on est allé chercher des travailleurs italiens, polonais, espagnols, portugais ou maghrébins pour reconstruire le pays. Beaucoup de Français ont un grand-parent venu d'ailleurs.",
    indecis: "L'immigration n'est pas un phénomène nouveau : selon l'Insee, les immigrés représentaient déjà 6,6 % de la population en 1931. L'État a même créé en 1945 un office pour recruter des travailleurs étrangers. Cela n'empêche pas de débattre de la politique migratoire, mais à partir de cette histoire."
  },
  'pauvrete-france': {
    convaincus: "Selon l'Insee, 9,8 millions de personnes vivaient sous le seuil de pauvreté en 2024, soit 15,4 % de la population, le plus haut niveau depuis 1996. Le seuil, c'est 1 337 € par mois pour une personne seule. Les aides existent, mais elles ne suffisent pas à faire disparaître la pauvreté.",
    indecis: "On peut avoir l'impression qu'avec toutes les aides, la pauvreté a disparu. Les chiffres de l'Insee montrent l'inverse : 15,4 % de la population est pauvre en 2024, et les inégalités sont à leur plus haut depuis 1996. Les aides limitent la pauvreté, elles ne l'effacent pas.",
  },
};
