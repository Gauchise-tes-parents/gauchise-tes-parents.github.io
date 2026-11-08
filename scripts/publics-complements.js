// Réponses selon le public (v14) pour des fiches dont le générateur n'existe plus ou n'est plus relancé.
// Textes écrits UNIQUEMENT à partir du contenu déjà sourcé de chaque fiche (résumé et faits).
// Appliqué par scripts/corrections-v10.js (idempotent : remplace le champ « publics » par la version ci-dessous).
// Ajouts du 7 novembre 2026 (passages de 12 h et de 20 h 15).
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
  // Ajouts du 7 novembre 2026 (passage de 20 h 15).
  'medias-concentration': {
    convaincus: "Regarde qui possède les grands médias privés : Bolloré, Arnault, Drahi, Niel, Bouygues. Vincent Bolloré contrôle Canal+, Europe 1 et le JDD, dont la ligne est classée à droite. Des milliardaires qui financeraient des médias gauchistes, ça ne tient pas debout.",
    indecis: "Le pluralisme des médias est un vrai sujet, et chacun a le droit de trouver certains médias orientés. Mais les grands médias appartiennent surtout à de grandes fortunes, avec des lignes éditoriales très diverses. Le Conseil d'État a d'ailleurs demandé en 2024 un contrôle plus large du pluralisme, pour toutes les chaînes.",
  },
  'delinquance-partout': {
    convaincus: "Les chiffres du ministère de l'Intérieur ne disent pas que tout augmente : en 2025, les cambriolages, les vols avec armes et les vols de véhicules baissent, et les homicides sont stables. Ce qui monte, ce sont surtout les violences sexuelles déclarées, les escroqueries et les affaires de stupéfiants. Pour lutter contre la délinquance, il faut regarder infraction par infraction.",
    indecis: "Ton inquiétude est compréhensible, et certaines formes de délinquance augmentent vraiment, comme les violences sexuelles enregistrées ou le trafic de stupéfiants. Mais d'autres baissent, comme les cambriolages, et les homicides sont stables. Une partie des hausses vient aussi de plaintes plus nombreuses.",
  },
  'homicides-record': {
    convaincus: "Les chercheurs qui comparent les chiffres de la police et ceux des certificats de décès depuis 1971 arrivent à la même conclusion : l'homicide est à un niveau historiquement bas. Depuis 2016, on compte entre 800 et 960 victimes par an. Ce qui augmente, ce sont surtout les tentatives enregistrées et certains règlements de comptes.",
    indecis: "Les faits divers donnent l'impression que les meurtres explosent, mais sur le long terme, ce n'est pas le cas. Depuis 2016, le nombre de victimes oscille autour de 800 à 960 par an. Près d'un tiers des homicides sont commis dans la famille, ce qui demande aussi des réponses de prévention.",
  },
  'lfi-contre-police': {
    convaincus: "Le programme de LFI ne supprime pas la police : il propose une police de proximité, le démantèlement des BAC et un organe de contrôle indépendant à la place de l'IGPN. On peut être en désaccord, mais c'est une autre police, pas l'absence de police. Certaines déclarations, comme « La police tue », ont choqué et ont été vivement dénoncées.",
    indecis: "LFI critique durement certaines pratiques policières, et certaines phrases de ses dirigeants ont été jugées excessives. Mais son programme prévoit une police de proximité et un contrôle indépendant, pas la fin de la police. Le débat porte sur le type de police que l'on veut.",
  },
  'discriminations-embauche': {
    convaincus: "Ce n'est pas une impression, c'est mesuré : dans le grand testing public de 2019-2021, à CV équivalent, les candidats à nom maghrébin sont rappelés 31,5 % moins souvent. Il leur faut envoyer une fois et demie plus de CV pour obtenir autant de réponses. Ça n'excuse personne, mais ça pèse sur la vie de millions de gens.",
    indecis: "Les discriminations à l'embauche sont mesurées par des tests où seul le nom change sur le CV : un candidat d'origine maghrébine est rappelé nettement moins souvent. Le chômage des diplômés originaires du Maghreb est près de trois fois plus élevé, et l'essentiel de l'écart ne s'explique ni par le diplôme ni par l'âge.",
  },
  'electricite-nucleaire-renouvelables': {
    convaincus: "Le nucléaire fait bien l'essentiel, 68 % en 2025. Mais les renouvelables produisent plus d'un quart de notre électricité, hydraulique en tête : sans eux, pas de record de 95 % d'électricité bas carbone. Les deux se complètent, et c'est ce qui permet à la France d'exporter un record d'électricité.",
    indecis: "La France produit une électricité très peu carbonée, grâce au nucléaire (68 %) mais aussi aux barrages, à l'éolien et au solaire, qui fournissent plus d'un quart du total. Opposer les deux n'a pas beaucoup de sens : c'est leur combinaison qui donne une électricité propre.",
  },
  'rsa-profiteurs': {
    convaincus: "C'est l'inverse : selon la DREES, environ un tiers des foyers qui ont droit au RSA ne le demandent pas, soit plus de 500 000 foyers fin 2021. Si tout le monde se jetait dessus, la dépense augmenterait de 2,5 milliards. Le vrai problème, ce sont ceux qui passent à côté de leurs droits.",
    indecis: "On imagine souvent l'inverse, mais la DREES montre qu'un tiers des foyers éligibles au RSA ne le perçoivent pas. Ce non-recours vient souvent de la complexité des démarches ou de la honte de demander. C'est une réalité qu'on connaît mal.",
  },
  'impots-assistanat': {
    convaincus: "Regarde où va l'argent : sur 1 672 milliards de dépenses publiques en 2024, les minima sociaux pèsent 31,6 milliards, environ 2 %, dont 12 milliards pour le RSA. La plus grosse part va aux retraites, à la santé et à l'école. Ce que tu appelles assistanat, c'est une petite partie de tes impôts.",
    indecis: "Les impôts financent d'abord les retraites, la santé, l'école, la sécurité et la dette. Les minima sociaux, dont le RSA, représentent environ 2 % des dépenses publiques. On peut débattre de leur efficacité, mais ils ne sont pas le cœur de la dépense.",
  },
  'expulser-tous-etrangers-condamnes': {
    convaincus: "La loi permet déjà d'éloigner beaucoup d'étrangers condamnés : le juge peut prononcer une interdiction du territoire, et depuis 2024 les protections tombent pour les condamnations graves. Le vrai blocage, c'est l'exécution : environ 10 % des OQTF seulement, parce que de nombreux pays d'origine sont réticents à délivrer les laissez-passer. Promettre de « tout expulser » sans régler ça, c'est un slogan.",
    indecis: "C'est une proposition politique, et l'inquiétude derrière est légitime. Mais le droit permet déjà d'expulser de nombreux condamnés, en tenant compte de leurs attaches en France, comme l'exige la Cour européenne des droits de l'homme. Le principal problème est l'exécution des décisions, qui dépend de la coopération des pays d'origine.",
  },
  'dividendes-salaires': {
    convaincus: "Toutes les entreprises ne roulent pas sur l'or, beaucoup de petites ont des marges faibles. Mais les grandes entreprises cotées ont versé environ 61 milliards d'euros de dividendes au seul deuxième trimestre 2026, la France est en tête en Europe. Dire que « les entreprises » n'ont pas les moyens, c'est mettre le boulanger et le CAC 40 dans le même sac.",
    indecis: "La situation dépend vraiment des entreprises : les petites ont souvent des marges serrées, quand les grandes entreprises cotées versent des dividendes record. Le taux de marge moyen reste élevé (32,2 % en 2025). Le débat sur les salaires gagne à distinguer ces situations.",
  },
  // Ajouts du 8 novembre 2026 (premier passage)
  'aah-suffisante': {
    convaincus: "L'AAH à taux plein, c'est 1 041,59 € par mois depuis avril 2026, alors que le seuil de pauvreté est de 1 337 €. Une personne qui ne vit que de l'AAH vit donc sous le seuil de pauvreté. Ce sont souvent des gens qui ne peuvent pas travailler : est-ce qu'on veut vraiment qu'ils vivent dans la pauvreté ?",
    indecis: "Le montant peut sembler correct, mais il reste inférieur au seuil de pauvreté de l'Insee (1 337 € par mois). Depuis 2023, l'AAH ne dépend plus des revenus du conjoint, ce qui a amélioré la situation de nombreux couples. La question est de savoir si une allocation versée à des personnes handicapées doit permettre de vivre au-dessus du seuil de pauvreté.",
  },
  'egalite-salariale': {
    convaincus: "L'égalité est dans la loi, mais pas sur les fiches de paie : en 2024, les femmes gagnent 21,8 % de moins que les hommes dans le privé, et 14 % de moins à temps de travail égal. À poste identique, l'écart est plus faible, mais le temps partiel et les métiers féminisés moins payés pèsent lourd. Ta mère, ta sœur ou ta fille sont directement concernées.",
    indecis: "À poste égal dans la même entreprise, l'écart est d'environ 3,6 %, ce qui montre des progrès. Mais sur l'année, les femmes gagnent 21,8 % de moins, à cause du temps partiel, des métiers moins payés et des carrières freinées. Le débat porte sur ces causes, pas seulement sur la discrimination directe.",
  },
  'encadrement-loyers': {
    convaincus: "L'évaluation de l'APUR montre qu'à Paris, l'encadrement a fait baisser les loyers d'environ 5 %, soit près de 80 € par mois pour un locataire. Ce n'est pas une idée de bobos : c'est de l'argent rendu aux gens qui louent. Le vrai problème, c'est que plus de 4 annonces sur 10 dépassent encore le plafond.",
    indecis: "L'outil a un effet mesuré à Paris, environ 5 % de baisse des loyers. Mais il est mal respecté, avec plus de 4 annonces sur 10 au-dessus du plafond. On peut débattre de ses effets sur l'offre de logements, mais pas dire qu'il ne sert à rien : son efficacité dépend surtout des contrôles.",
  },
  'immigration-emploi': {
    convaincus: "Le travail n'est pas un gâteau fixe : les immigrés travaillent, mais ils consomment et créent aussi de l'activité. Ils sont d'ailleurs moins souvent en emploi que les autres (62,4 % contre 71,4 %), et ils occupent beaucoup de métiers pénibles, comme l'entretien ou l'aide à domicile. Les études trouvent un effet moyen nul ou positif à long terme sur l'emploi des Français.",
    indecis: "Une étude trouve un effet négatif à court terme pour les travailleurs directement en concurrence avec des immigrés : la crainte n'est pas absurde. Mais à long terme, les études sur la France ne trouvent pas d'effet défavorable sur l'emploi des natifs. Ce qui protège vraiment, ce sont des droits égaux pour tous les travailleurs.",
  },
  'immigration-salaires': {
    convaincus: "Les études sur la France ne trouvent pas de baisse du salaire moyen des Français due à l'immigration ; l'une trouve même une hausse d'environ 3 % sur 1962-1999. Ce qui tire les salaires vers le bas, c'est l'exploitation de travailleurs sans droits. Les patrons qui emploient au noir sont les vrais responsables.",
    indecis: "Un effet très faible à court terme est possible pour les salariés directement en concurrence, et c'est une inquiétude légitime. Mais à long terme, les études ne trouvent pas d'effet défavorable sur le salaire moyen. La meilleure protection, c'est « à travail égal, salaire égal », contrôlé pour tous.",
  },
  'chomage-penurie-recrutement': {
    convaincus: "C'est vrai, la moitié des recrutements prévus en 2025 sont jugés difficiles par les employeurs. Mais ce n'est pas la preuve que les chômeurs ne veulent pas travailler : les postes, les compétences et les lieux ne coïncident pas toujours. Et les métiers qui recrutent mal cumulent souvent pénibilité et horaires difficiles.",
    indecis: "Les deux sont vrais en même temps : des postes restent difficiles à pourvoir et le chômage persiste. Cela vient d'un décalage de compétences, de lieux et de conditions de travail. Améliorer les salaires, la formation et les conditions dans ces métiers aide à rapprocher les deux.",
  },
  'morts-au-travail': {
    convaincus: "En 2024, 764 personnes sont mortes d'un accident du travail au régime général. Ce ne sont pas des statistiques lointaines : ce sont surtout des ouvriers du BTP, des intérimaires, des jeunes. Et depuis les années 2010, le nombre de morts ne baisse plus.",
    indecis: "Les accidents mortels ont beaucoup baissé pendant des décennies, mais ils stagnent depuis les années 2010, avec 764 morts en 2024 au régime général. Les comparaisons européennes sont délicates, car la France compte les malaises mortels. La prévention reste un enjeu réel, surtout dans le bâtiment et le transport.",
  },
  'agriculteurs-revenus': {
    convaincus: "Selon l'Insee, les ménages agricoles sont plus souvent pauvres que la moyenne (18,1 % contre 15,1 %), et un exploitant sur six déclare un revenu nul ou négatif certaines années. La retraite moyenne d'un ancien exploitant tourne autour de 840 €. Dire qu'ils vivent tous très bien, c'est ignorer ceux qui n'arrivent pas à se payer.",
    indecis: "Les agriculteurs ont souvent un patrimoine professionnel important, mais ce n'est pas un revenu disponible. Leurs revenus sont très inégaux, et beaucoup vivent mal : taux de pauvreté plus élevé que la moyenne, petites retraites. Le débat porte sur la répartition des aides et sur les prix payés aux producteurs.",
  },
  'abstention-inegale': {
    convaincus: "Chacun est libre de ne pas voter, mais l'abstention n'est pas un hasard : en 2022, 30,1 % des non-diplômés n'ont voté à aucun tour, contre 9,6 % des diplômés du supérieur. Les ouvriers votent beaucoup moins que les cadres. Et ceux qui votent le moins sont ceux dont les responsables politiques tiennent le moins compte.",
    indecis: "Ne pas voter est un droit. Mais les chiffres de l'Insee montrent que l'abstention touche surtout les moins diplômés, les ouvriers et les jeunes. Cela déforme la représentation : les choix politiques tiennent davantage compte de ceux qui votent.",
  },
  'sondages-mille-personnes': {
    convaincus: "Un échantillon de 1 000 personnes bien construit donne une estimation avec une marge d'erreur connue : un score de 50 % veut dire entre 46,9 % et 53,1 %. Ce n'est pas une prédiction, c'est une photo à un moment donné. Depuis 2016, la marge d'erreur doit être publiée : tu peux la vérifier toi-même.",
    indecis: "Un sondage n'est pas une certitude, mais ce n'est pas rien : avec 1 000 personnes, la marge d'erreur est d'environ 3 points autour de 50 %. Il faut regarder cette marge et la méthode, publiées obligatoirement depuis 2016. Un sondage mesure une opinion à un moment, il ne prédit pas un résultat.",
  },
};
