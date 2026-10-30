"""Fiches de couverture (v11) : sous-thèmes qui n'avaient encore aucune fiche.

Homicides, loyers, rénovation thermique, handicap, désinformation, sondages, abstention, bilan de la gauche au pouvoir.
Sources ouvertes et lues le 30 octobre 2026 (consultee=True).
Usage : python3 scripts/fiches/couverture_sous_themes.py  (puis npm run fiches:corriger et npm run enrichir)
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche, OUT, INSEE_PAUV

AN_HOMICIDES = ('an_hom', src("Réponse du ministère de l'Intérieur à la question écrite n° 12954 (homicides)", "Assemblée nationale / ministère de l'Intérieur et des Outre-mer (données SSMSI)", "5 décembre 2023",
  "https://questions.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE12954.pdf",
  "Victimes d'homicide enregistrées : 911 en 2016, 826 en 2017, 831 en 2018, 857 en 2019, 823 en 2020, 882 en 2021, 959 en 2022 ; les chiffres antérieurs à 2016 ne sont pas fiabilisés ; environ 29 % des homicides sont commis dans la famille ; les homicides « crapuleux » (règlements de comptes et vols) représentent environ 10 % de l'ensemble.",
  "Données officielles du service statistique du ministère de l'Intérieur."))
CESDIP = ('cesdip', src("L'homicide est rare (Observatoire scientifique du crime et de la justice)", "CESDIP (CNRS, ministère de la Justice, UVSQ) — OSCJ", "Janvier 2023",
  "https://oscj2.cesdip.fr/wp-content/uploads/2023/01/Lhomicide-est-rare.pdf",
  "Comparaison des statistiques de police et des causes médicales de décès (Inserm-CépiDc), 1971-2021 : les deux séries évoluent ensemble (corrélation 0,90) ; depuis 2010, les homicides consommés « ne cesse[nt] de décroître » tandis que les tentatives enregistrées par la police progressent ; « l'homicide volontaire se situe actuellement à un niveau très bas ».",
  "Laboratoire de recherche public spécialisé en criminologie.", 'etude'))
APUR = ('apur', src("Impact de l'encadrement des loyers à Paris : actualisation de l'évaluation et extension à 5 autres villes régulées", "Atelier parisien d'urbanisme (APUR) — Marie Breuillé, Camille Grivault, Yoann Morin, Martin Regnaud", "Juin 2025",
  "https://www.apur.org/sites/default/files/2025-06/rapport-impact_encadrement_loyers_paris.pdf",
  "Paris, juillet 2019 - juin 2024 : l'encadrement réduit les loyers d'environ 5 %, soit entre 79 € et 82 € par mois pour un loyer moyen de 1 492 € ; « plus de 4 annonces sur 10 proposent un loyer supérieur au seuil fixé » (43,2 % en 2023-2024), sans pouvoir distinguer dépassements illégaux et compléments justifiés ; données d'annonces SeLoger, pas de baux signés.",
  "Évaluation d'une agence publique d'urbanisme réalisée avec des chercheurs.", 'etude'))
SDES = ('sdes', src("Le parc de logements par classe de performance énergétique au 1er janvier 2025", "SDES (service statistique du ministère de la Transition écologique)", "12 novembre 2025",
  "https://www.statistiques.developpement-durable.gouv.fr/le-parc-de-logements-par-classe-de-performance-energetique-au-1er-janvier-2025",
  "Au 1er janvier 2025 : 12,7 % des 30,9 millions de résidences principales sont des passoires énergétiques (F et G), soit environ 3,9 millions, 327 000 de moins qu'un an plus tôt (dont près de 40 % de la baisse due à la réforme du DPE des petites surfaces) ; logements classés G : 4,8 % ; parc locatif privé : 13,8 % de passoires (environ 1,1 million), parc social : 5,8 %, propriétaires occupants : 14,0 %.",
  "Statistique publique de référence."))
AAH = ('aah', src("Montant 2026 de l'AAH (allocation aux adultes handicapés)", "Mon Parcours Handicap (site public, CNSA et Caisse des dépôts)", "Mis à jour le 5 mai 2026",
  "https://www.monparcourshandicap.gouv.fr/actualite/montant-aah",
  "« Depuis le 1er avril 2026, le montant maximum à taux plein » de l'AAH est de « 1 041,59 € par mois » pour une personne sans autres revenus ; déconjugalisation en vigueur depuis le 1er octobre 2023 : seules les ressources de la personne handicapée sont prises en compte.",
  "Site d'information public."))
VIGINUM = ('viginum', src("Rapport d'activité VIGINUM 2024", "VIGINUM — Secrétariat général de la défense et de la sécurité nationale (SGDSN)", "Hiver 2025",
  "https://www.vie-publique.fr/files/rapport/pdf/301522.pdf",
  "En 2024 : 259 phénomènes inauthentiques détectés, 174 modes opératoires suivis ; 25 manœuvres visant les scrutins français (14 pour les européennes, 11 pour les législatives) ; campagnes russes « Portal Kombat » (réseau initial de 193 faux sites d'information) et « Matriochka » (faux contenus usurpant des médias, dont des deepfakes) ; contenus liés à l'Azerbaïdjan lors des événements de Nouvelle-Calédonie.",
  "Rapport d'un service de l'État chargé de la protection contre les ingérences numériques."))
PS_SONDAGES = ('ps_sond', src("Sondages : comment fonctionne la marge d'erreur ?", "Public Sénat (Louis Mollier-Sabet)", "7 avril 2022",
  "https://www.publicsenat.fr/actualites/politique/sondages-comment-fonctionne-la-marge-d-erreur-201683",
  "La plupart des sondages reposent sur un intervalle de confiance de 95 % ; pour un échantillon de 1 000 personnes, un score de 10 % se situe entre 8,2 % et 11,8 %, un score de 50 % entre 46,9 % et 53,1 % ; depuis une loi de 2016, la marge d'erreur doit être adressée à la Commission des sondages et publiée avec le sondage.",
  "Média parlementaire, explication pédagogique.", 'media'))
INSEE_VOTE = ('insee_vote', src("Élections présidentielle et législatives de 2022 : seul un tiers des électeurs a voté à tous les tours (Insee Première n° 1928)", "Insee (Kilian Bloch)", "17 novembre 2022",
  "https://www.insee.fr/fr/statistiques/6658145",
  "Inscrits : 36 % ont voté à tous les tours, 16 % se sont abstenus à tous les tours, 48 % ont voté par intermittence. Abstention systématique : 23,8 % des 18-24 ans contre 9,2 % des 60-64 ans ; 30,1 % des non-diplômés contre 9,6 % des diplômés du supérieur ; 23,6 % des ouvriers non qualifiés contre 7,4 % des cadres.",
  "Statistique publique de référence (enquête participation électorale)."))
INSEE_RTT = ('insee_rtt', src("Les effets de la RTT sur l'emploi : des estimations ex ante aux évaluations ex post (Économie et Statistique n° 376-377)", "Insee (Alain Gubian, Stéphane Jugnot, Frédéric Lerais, Vladimir Passeron)", "Juin 2005",
  "https://www.insee.fr/fr/statistiques/1376464",
  "La réduction du temps de travail a créé « près de 350 000 postes » sur 1998-2002, « sans grand déséquilibre financier pour les entreprises » ; la baisse effective de la durée du travail a été moins forte que dans les simulations ex ante.",
  "Revue de la statistique publique.", 'etude'))
AN_RTT = ('an_rtt', src("Rapport de la commission d'enquête sur l'impact de la réduction progressive du temps de travail (n° 2436)", "Assemblée nationale (rapporteure Barbara Romagnan)", "9 décembre 2014",
  "https://www.assemblee-nationale.fr/14/pdf/rap-enq/r2436.pdf",
  "350 000 emplois : le chiffre « le plus communément admis » pour la loi de 1998, confirmé par des études commandées par la Dares ; les prévisions initiales espéraient 700 000 postes ; coût net ex post pour les finances publiques estimé à 2,5 milliards d'euros ; le président de la commission ne partage pas les conclusions du rapport.",
  "Rapport parlementaire (conclusions contestées par le président de la commission)."))
COR = ('cor', src("Évolution historique et projetée de l'âge de départ à la retraite (document n° 4, séance du 21 février 2019)", "Conseil d'orientation des retraites (secrétariat général)", "21 février 2019",
  "https://www.cor-retraites.fr/sites/default/files/2019-06/doc-4439.pdf",
  "L'ordonnance du 26 mars 1982 « finalise ainsi la généralisation de la retraite à 60 ans » en permettant aux hommes de partir à cet âge sans décote avec au moins 37,5 ans de cotisation.",
  "Organisme public d'expertise sur les retraites."))
SENAT_1981 = ('senat81', src("Les circonstances de l'adoption de la loi du 9 octobre 1981", "Sénat", "Archives",
  "https://www.senat.fr/evenement/archives/D22/loi1981.html",
  "Après l'élection de François Mitterrand, un projet de loi portant abolition de la peine de mort, « définitive et générale », est déposé le 29 août 1981 et défendu par le garde des Sceaux Robert Badinter ; les tentatives de 1979 et 1980 n'avaient pas abouti.",
  "Ressource historique d'une assemblée parlementaire."))

FICHES = []

FICHES.append(fiche(
 id='homicides-record', affirmation="Il n'y a jamais eu autant de meurtres en France.", volet='securite', sous_theme='Homicides',
 mots_cles=['meurtres', 'homicides', 'tués', 'assassinats', 'jamais eu autant', 'violence', 'narcotrafic', 'règlements de comptes', 'record'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Sur le long terme, l'homicide est à un niveau historiquement bas : les statistiques de police et celles des causes médicales de décès montrent la même tendance depuis les années 1970. Les victimes enregistrées par la police oscillent autour de 800 à 960 par an depuis 2016 (959 en 2022). Ce qui augmente, ce sont surtout les tentatives enregistrées et certains règlements de comptes.",
 contexte="Les faits divers et les règlements de comptes liés au trafic de drogue donnent l'impression d'une explosion des meurtres.",
 explication="Deux sources indépendantes mesurent l'homicide : la police et les certificats de décès. Leur concordance sur cinquante ans permet de dégager une tendance fiable. Les variations d'une année sur l'autre sont réelles mais faibles par rapport à cette tendance de fond.",
 sources=[CESDIP, AN_HOMICIDES],
 faits=[
  fait("Selon les chercheurs du CESDIP, qui comparent statistiques de police et causes médicales de décès sur 1971-2021, les homicides consommés diminuent depuis 2010 et l'homicide volontaire se situe à un niveau très bas.", 'cesdip', '1971-2021', 'France', "Sur le long terme, l'idée d'un record ne tient pas.", 'estimation'),
  fait("Le ministère de l'Intérieur a enregistré 911 victimes d'homicide en 2016, 823 en 2020 et 959 en 2022 ; les chiffres antérieurs à 2016 ne sont pas fiabilisés.", 'an_hom', '2016-2022', 'France', "Une hausse récente existe, mais dans une fourchette stable depuis 2016.", 'etabli', '959'),
  fait("Environ 29 % des homicides sont commis dans la famille ; les homicides « crapuleux » (règlements de comptes et vols) en représentent environ 10 %.", 'an_hom', 'Données récentes', 'France', "La violence mortelle est souvent intrafamiliale, loin de l'image de la rue.", 'etabli', '29 %'),
 ],
 court="Faux : sur cinquante ans, l'homicide est à un niveau très bas, selon les chercheurs qui croisent police et certificats de décès. La police enregistre entre 820 et 960 victimes par an depuis 2016. Ce qui inquiète à juste titre, ce sont les règlements de comptes liés au trafic, pas un record général.",
 moyen="L'impression d'un record vient des faits divers, pas des données. Les chercheurs du CESDIP comparent deux sources indépendantes, la police et les certificats de décès, depuis 1971 : elles montrent la même tendance, et l'homicide volontaire est aujourd'hui à un niveau très bas.\n\nDepuis 2016, le ministère de l'Intérieur enregistre entre 823 et 959 victimes par an. Et près d'un tiers des homicides ont lieu dans la famille. Les règlements de comptes liés au trafic sont un vrai problème, qui appelle des moyens contre les réseaux, pas des discours sur une explosion générale.",
 detaille="Pour savoir si les meurtres augmentent, il faut une série longue et fiable. Les chercheurs du CESDIP (CNRS) croisent les statistiques de police et celles des causes médicales de décès (Inserm) de 1971 à 2021 : les deux évoluent ensemble, et l'homicide volontaire se situe aujourd'hui à un niveau très bas. Depuis 2010, les homicides consommés diminuent ; ce sont les tentatives enregistrées par la police qui progressent, en partie en raison des pratiques d'enregistrement.\n\nLes données récentes du ministère de l'Intérieur montrent une hausse en 2021-2022 (959 victimes en 2022), mais dans une fourchette stable depuis 2016. Environ 29 % des homicides sont commis dans la famille ; les homicides liés aux règlements de comptes et aux vols en représentent environ 10 %.\n\nLe narcotrafic provoque des violences graves dans certains quartiers : cela justifie des moyens d'enquête et de prévention, pas l'idée fausse d'un pays qui n'a jamais été aussi violent.",
 empathie="Je comprends : quand on entend parler de fusillades, on a l'impression que c'est pire que jamais. Mais les chercheurs qui suivent ça depuis cinquante ans montrent que les meurtres sont plutôt à un niveau bas. Les violences liées au trafic, elles, sont bien réelles, et c'est là qu'il faut agir.",
 legitimes=["Les victimes d'homicide enregistrées ont augmenté en 2021-2022.", "Les tentatives d'homicide enregistrées progressent, et les violences liées au trafic de drogue sont réelles dans certains territoires."],
 contre=[
  ("Les chiffres sont maquillés.", "Deux sources indépendantes (police et certificats de décès) évoluent ensemble depuis cinquante ans : on ne peut pas maquiller les deux."),
  ("Avant, on ne tuait pas pour un regard.", "Les données ne montrent pas de violence mortelle plus fréquente qu'avant ; la perception est façonnée par la médiatisation des faits divers."),
 ],
 questions=["Sur quelle source t'appuies-tu pour dire que c'est un record ?", "Sais-tu qu'un tiers des homicides ont lieu dans la famille ?"],
 limites=["Les données du ministère antérieures à 2016 ne sont pas fiabilisées.", "Les données récentes ne couvrent pas 2023-2025 dans les sources retenues."],
 a_actualiser='2027-03-31',
))

FICHES.append(fiche(
 id='encadrement-loyers', affirmation="L'encadrement des loyers ne sert à rien.", volet='economie', sous_theme='Loyers',
 mots_cles=['encadrement des loyers', 'loyers', 'loyer', 'plafonnement', 'propriétaires', 'locataires', 'paris', 'logement cher', 'bailleurs'],
 verdict='contredit', fiabilite='interpretation',
 resume="À Paris, l'évaluation de l'Atelier parisien d'urbanisme estime que l'encadrement a fait baisser les loyers d'environ 5 %, soit 79 à 82 € par mois pour un loyer moyen de 1 492 €. Mais plus de 4 annonces sur 10 dépassent encore le plafond : l'outil marche, à condition d'être appliqué et contrôlé.",
 contexte="L'encadrement des loyers est appliqué à Paris depuis juillet 2019 et dans plusieurs autres villes. Ses opposants disent qu'il est inefficace ou qu'il fait fuir les propriétaires.",
 explication="L'évaluation compare l'évolution des loyers annoncés à Paris avec ce qui se serait passé sans encadrement. Elle porte sur des annonces, pas sur des baux signés, et ne peut pas distinguer dépassements illégaux et compléments de loyer justifiés.",
 sources=[APUR],
 faits=[
  fait("Selon l'évaluation de l'APUR, l'encadrement a réduit les loyers parisiens d'environ 5 %, soit entre 79 € et 82 € par mois pour un loyer moyen de 1 492 € (juillet 2019 - juin 2024).", 'apur', '2019-2024', 'Paris', "L'encadrement fait baisser les loyers de manière mesurable.", 'estimation', '79 à 82 €'),
  fait("Selon la même évaluation, plus de 4 annonces sur 10 proposent un loyer supérieur au plafond (43,2 % en 2023-2024), sans qu'on puisse distinguer dépassements illégaux et compléments justifiés.", 'apur', '2023-2024', 'Paris', "Le respect de la règle reste insuffisant : il faut des contrôles.", 'estimation', '43,2 %'),
 ],
 court="Faux : à Paris, l'encadrement a fait baisser les loyers d'environ 5 %, soit près de 80 € par mois pour un locataire (APUR, 2025). Le vrai problème, c'est qu'il est mal respecté : plus de 4 annonces sur 10 dépassent encore le plafond.",
 moyen="On a une évaluation sérieuse : l'Atelier parisien d'urbanisme a mesuré l'effet de l'encadrement entre 2019 et 2024. Résultat : des loyers environ 5 % plus bas que sans encadrement, soit 79 à 82 € par mois pour un loyer moyen de 1 492 €.\n\nLe point faible n'est pas la règle, c'est son application : plus de 4 annonces sur 10 restent au-dessus du plafond. La conclusion logique, c'est de contrôler et de sanctionner, pas de supprimer l'outil.",
 detaille="L'évaluation actualisée de l'APUR (juin 2025), réalisée avec des chercheurs, compare les loyers annoncés à Paris à ce qu'ils auraient été sans encadrement. Entre juillet 2019 et juin 2024, l'encadrement les a réduits d'environ 5 % : entre 79 € et 82 € par mois pour un loyer moyen de 1 492 €.\n\nLa même étude montre que plus de 4 annonces sur 10 proposent un loyer supérieur au plafond, une part plus élevée pour les meublés ; une partie de ces dépassements peut être légale (complément de loyer justifié), mais l'étude ne peut pas les distinguer.\n\nL'évaluation porte sur des annonces de professionnels, pas sur des baux signés. L'effet sur le nombre de logements mis en location n'est pas couvert par cette fiche. En l'état des données, dire que l'encadrement « ne sert à rien » est faux ; dire qu'il est insuffisamment appliqué est juste.",
 empathie="Je comprends qu'on doute : les loyers restent très chers. Mais une évaluation sérieuse montre que sans l'encadrement, ils seraient encore plus hauts, d'environ 80 € par mois à Paris. Le problème, c'est que beaucoup de bailleurs ne le respectent pas.",
 legitimes=["Plus de 4 annonces sur 10 dépassent le plafond : l'application est insuffisante.", "L'évaluation repose sur des annonces, pas sur des baux signés."],
 contre=[
  ("Ça fait fuir les propriétaires.", "Cette fiche ne contient pas de donnée sur l'offre de logements ; ce qui est mesuré, c'est une baisse des loyers d'environ 5 %. La question de l'offre mérite d'être examinée avec des données, pas affirmée."),
  ("Les loyers ont quand même augmenté.", "Oui, mais moins qu'ils ne l'auraient fait sans encadrement : c'est exactement ce que mesure l'évaluation."),
 ],
 questions=["Tu préfères 80 € de plus par mois de loyer, ou des contrôles pour faire respecter la règle ?", "Sur quoi t'appuies-tu pour dire que ça ne marche pas ?"],
 limites=["L'effet de l'encadrement sur le nombre de logements proposés à la location n'est pas couvert par cette fiche.", "Données d'annonces SeLoger, hors particuliers."],
 a_actualiser='2027-06-30',
))

FICHES.append(fiche(
 id='passoires-thermiques', affirmation="Interdire de louer les passoires thermiques va vider le marché locatif.", volet='ecologie', sous_theme='Rénovation thermique',
 mots_cles=['passoires thermiques', 'passoires', 'dpe', 'rénovation', 'isolation', 'location', 'marché locatif', 'logements g', 'interdiction de louer', 'propriétaires'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Au 1er janvier 2025, 13,8 % des logements du parc locatif privé sont des passoires énergétiques (F ou G), environ 1,1 million, et leur nombre diminue chaque année. L'interdiction concerne d'abord les logements G (4,8 % des résidences principales) : il s'agit de rénover une minorité de logements, pas de vider le marché.",
 contexte="La loi Climat et résilience interdit progressivement la mise en location des logements les plus énergivores (G, puis F). Certains annoncent un effondrement de l'offre locative.",
 explication="Les chiffres du SDES permettent de mesurer l'ampleur réelle du problème et son évolution. Une partie de la baisse récente vient de la réforme du DPE pour les petites surfaces, une autre des rénovations.",
 sources=[SDES],
 faits=[
  fait("Au 1er janvier 2025, 12,7 % des résidences principales sont des passoires énergétiques (environ 3,9 millions), 327 000 de moins qu'un an plus tôt ; près de 40 % de cette baisse s'explique par la réforme du DPE des petites surfaces.", 'sdes', '1er janvier 2025', 'France, résidences principales', "Le stock diminue, même si une partie de la baisse est un effet de méthode.", 'etabli', '12,7 %'),
  fait("Le parc locatif privé compte 13,8 % de passoires (environ 1,1 million de logements) ; les logements classés G représentent 4,8 % des résidences principales.", 'sdes', '1er janvier 2025', 'France', "L'interdiction concerne une minorité du parc locatif.", 'etabli', '13,8 %'),
 ],
 court="Non : les passoires représentent 13,8 % du parc locatif privé, et l'interdiction vise d'abord les logements G (4,8 % des résidences principales). Il s'agit de rénover une minorité de logements où les locataires paient des factures énormes, pas de vider le marché.",
 moyen="Regardons l'ampleur : selon le service statistique du ministère, 13,8 % des logements loués dans le privé sont des passoires, environ 1,1 million. Et leur nombre baisse chaque année.\n\nL'interdiction concerne d'abord les logements G, les pires, 4,8 % des résidences principales. Les locataires de ces logements paient des factures d'énergie très lourdes. La vraie question, c'est d'aider les propriétaires modestes à rénover, pas de laisser des gens vivre dans des logements qui ne se chauffent pas.",
 detaille="Selon le SDES, au 1er janvier 2025, 12,7 % des résidences principales sont des passoires énergétiques (classes F et G), soit environ 3,9 millions de logements. Leur nombre a baissé de 327 000 en un an ; près de 40 % de cette baisse est due à la réforme du DPE des petites surfaces, le reste reflétant notamment des rénovations.\n\nDans le parc locatif privé, la part de passoires est de 13,8 %, environ 1,1 million de logements. Les logements G, premiers concernés par l'interdiction de mise en location, représentent 4,8 % des résidences principales.\n\nLe risque de retrait de certains logements du marché existe, et il faut l'accompagner. Mais la réponse est d'aider à rénover, notamment les propriétaires modestes, plutôt que de renoncer à protéger les locataires des logements les plus énergivores.",
 empathie="Je comprends l'inquiétude des petits propriétaires : rénover coûte cher. Mais on parle d'une minorité de logements, où les locataires grelottent ou paient des factures énormes. L'enjeu, c'est de les aider à faire les travaux.",
 legitimes=["Une partie de la baisse du nombre de passoires est un effet de la réforme du DPE, pas des travaux.", "La rénovation coûte cher et certains propriétaires modestes ont du mal à la financer."],
 contre=[
  ("Les propriétaires vont vendre plutôt que rénover.", "Un logement vendu reste un logement ; et les aides à la rénovation existent pour éviter ce choix. Il faut les rendre plus accessibles."),
  ("Le DPE n'est pas fiable.", "Le DPE a été réformé et son calcul évolue ; c'est un argument pour l'améliorer, pas pour laisser les passoires sur le marché."),
 ],
 questions=["Tu accepterais de louer un logement qui ne se chauffe pas correctement ?", "Comment aider les propriétaires modestes à rénover, selon toi ?"],
 limites=["Le nombre de passoires varie avec la méthode du DPE (réforme 2024, nouveau coefficient de l'électricité en 2026).", "Les données ne disent pas combien de logements seraient retirés du marché."],
 a_actualiser='2026-12-31',
))

FICHES.append(fiche(
 id='aah-suffisante', affirmation="L'AAH, c'est assez pour vivre.", volet='droits', sous_theme='Handicap et accessibilité',
 mots_cles=['aah', 'allocation adulte handicapé', 'handicap', 'handicapés', 'assez pour vivre', 'seuil de pauvreté', 'déconjugalisation', 'minima sociaux'],
 verdict='contredit', fiabilite='etabli',
 resume="Depuis le 1er avril 2026, l'AAH à taux plein est de 1 041,59 € par mois, alors que le seuil de pauvreté est de 1 337 € par mois pour une personne seule (Insee, 2024). Une personne qui n'a que l'AAH vit donc sous le seuil de pauvreté.",
 contexte="L'allocation aux adultes handicapés est destinée aux personnes dont le handicap limite fortement la capacité à travailler. Depuis octobre 2023, elle ne dépend plus des revenus du conjoint.",
 explication="Comparer le montant maximal de l'AAH au seuil de pauvreté monétaire (60 % du niveau de vie médian) permet de savoir si elle protège de la pauvreté une personne sans autre ressource.",
 sources=[AAH, INSEE_PAUV],
 faits=[
  fait("Depuis le 1er avril 2026, le montant maximal de l'AAH à taux plein est de 1 041,59 € par mois pour une personne sans autres revenus.", 'aah', 'Avril 2026', 'France', "C'est le maximum, pour une personne sans autre ressource.", 'etabli', '1 041,59 €'),
  fait("En 2024, le seuil de pauvreté est de 1 337 € par mois et par unité de consommation.", 'insee_pauv', '2024', 'France métropolitaine', "L'AAH maximale reste près de 300 € sous ce seuil.", 'etabli', '1 337 €'),
  fait("Depuis le 1er octobre 2023, l'AAH est déconjugalisée : seules les ressources de la personne handicapée sont prises en compte, plus celles de son conjoint.", 'aah', 'Octobre 2023', 'France', "Une avancée obtenue après des années de mobilisation, qui met fin à la dépendance financière au conjoint.", 'etabli'),
 ],
 court="Non : l'AAH maximale est de 1 041,59 € par mois, alors que le seuil de pauvreté est de 1 337 € (Insee). Quelqu'un qui ne vit que de l'AAH vit sous le seuil de pauvreté.",
 moyen="Les chiffres sont simples : depuis avril 2026, l'AAH à taux plein, c'est 1 041,59 € par mois, au maximum. Le seuil de pauvreté, selon l'Insee, est de 1 337 €. Une personne qui ne peut pas travailler à cause de son handicap et n'a que l'AAH vit donc sous le seuil de pauvreté.\n\nIl y a eu une avancée : depuis octobre 2023, l'AAH ne dépend plus des revenus du conjoint. Mais son montant reste trop bas pour vivre dignement.",
 detaille="L'allocation aux adultes handicapés s'adresse aux personnes dont le taux d'incapacité est d'au moins 80 %, ou compris entre 50 et 79 % avec une restriction durable d'accès à l'emploi. Depuis le 1er avril 2026, son montant maximal est de 1 041,59 € par mois pour une personne sans autres revenus.\n\nLe seuil de pauvreté, défini comme 60 % du niveau de vie médian, s'établit à 1 337 € par mois en 2024 selon l'Insee. L'AAH maximale est donc inférieure d'environ 300 € à ce seuil.\n\nDepuis le 1er octobre 2023, l'AAH est déconjugalisée : seules les ressources de la personne handicapée comptent. Cette réforme, longtemps réclamée par les associations, a mis fin à une dépendance financière envers le conjoint. Reste le niveau de l'allocation, qui maintient sous le seuil de pauvreté les personnes qui n'ont pas d'autre ressource.",
 empathie="Je comprends qu'on pense que l'AAH suffit, puisqu'on en parle comme d'une aide importante. Mais elle est d'environ 1 040 € au maximum, sous le seuil de pauvreté. Imagine payer un loyer, se nourrir et se soigner avec ça, sans pouvoir travailler.",
 legitimes=["L'AAH a été revalorisée et déconjugalisée en 2023.", "Certaines personnes cumulent l'AAH avec d'autres aides (logement, complément de ressources) selon leur situation."],
 contre=[
  ("Avec les aides au logement, ça suffit.", "Les aides au logement aident à payer le loyer, mais l'AAH seule reste sous le seuil de pauvreté ; et ces aides dépendent de la situation de chacun."),
  ("Ils peuvent travailler à côté.", "L'AAH est justement destinée à des personnes dont le handicap limite fortement la capacité à travailler."),
 ],
 questions=["Tu pourrais vivre avec 1 041 € par mois, loyer compris ?", "Pourquoi une personne qui ne peut pas travailler devrait-elle vivre sous le seuil de pauvreté ?"],
 limites=["Le seuil de pauvreté comparé est celui de 2024 ; l'AAH est celle d'avril 2026.", "Les situations individuelles varient selon les aides cumulables."],
 a_actualiser='2027-04-30',
))

FICHES.append(fiche(
 id='ingerences-etrangeres', affirmation="Les ingérences étrangères dans nos élections, c'est du fantasme.", volet='politique', sous_theme='Désinformation',
 mots_cles=['ingérences', 'ingérence étrangère', 'désinformation', 'fausses informations', 'fake news', 'russie', 'élections', 'réseaux sociaux', 'viginum', 'manipulation', 'fact-checking'],
 verdict='contredit', fiabilite='etabli',
 resume="Le service de l'État chargé de les détecter, VIGINUM, a recensé en 2024 25 manœuvres visant les élections européennes et législatives, et documenté des campagnes russes comme « Portal Kombat » (un réseau de 193 faux sites d'information) ou « Matriochka » (faux contenus imitant des médias, deepfakes).",
 contexte="Les ingérences numériques étrangères sont parfois minimisées, parfois exagérées. Depuis 2021, un service rattaché au SGDSN, VIGINUM, est chargé de les détecter et de les caractériser.",
 explication="VIGINUM observe des comportements inauthentiques coordonnés (faux comptes, faux sites, usurpation de médias) et les attribue quand c'est possible. Son rapport d'activité donne des ordres de grandeur et des exemples documentés.",
 sources=[VIGINUM],
 faits=[
  fait("En 2024, VIGINUM a détecté 259 phénomènes inauthentiques et suivi 174 modes opératoires.", 'viginum', '2024', 'France', "Les ingérences sont un phénomène régulier et suivi, pas une rumeur.", 'etabli', '259'),
  fait("Lors des élections européennes et des législatives anticipées de 2024, VIGINUM a détecté 25 manœuvres ciblant les scrutins français (14 et 11).", 'viginum', '2024', 'France', "Les élections sont directement visées.", 'etabli', '25'),
  fait("La campagne russe « Portal Kombat » reposait sur un réseau initial de 193 faux portails d'information relayant des contenus prorusses et dénigrant les soutiens de l'Ukraine, dont la France.", 'viginum', '2024', 'France et Europe', "Des campagnes concrètes ont été documentées et dénoncées publiquement.", 'etabli', '193'),
 ],
 court="Ce n'est pas un fantasme : en 2024, le service de l'État VIGINUM a détecté 25 manœuvres visant nos élections européennes et législatives, et démonté des campagnes russes comme « Portal Kombat », un réseau de 193 faux sites d'information.",
 moyen="Il existe un service de l'État dont c'est le métier : VIGINUM. En 2024, il a détecté 259 phénomènes inauthentiques, dont 25 manœuvres visant directement les élections européennes et législatives.\n\nCe sont des faits documentés : le réseau russe « Portal Kombat » et ses 193 faux sites d'information, la campagne « Matriochka » qui imite de vrais médias et utilise des deepfakes. Se protéger de la désinformation, c'est défendre notre souveraineté démocratique.",
 detaille="Les ingérences numériques étrangères sont un sujet sérieux, qu'il ne faut ni nier ni exagérer. Le service VIGINUM, rattaché au Secrétariat général de la défense et de la sécurité nationale, publie un rapport d'activité. En 2024, il a détecté 259 phénomènes inauthentiques et suivi 174 modes opératoires.\n\nPendant les élections européennes et les législatives anticipées de 2024, il a repéré 25 manœuvres ciblant les scrutins français. Parmi les campagnes documentées : « Portal Kombat », un réseau russe d'abord composé de 193 faux portails d'information ; « Matriochka », qui diffuse de faux contenus imitant des médias et des personnalités, y compris par deepfakes ; ou des contenus liés à l'Azerbaïdjan lors des événements de Nouvelle-Calédonie.\n\nDétecter une manœuvre ne veut pas dire qu'elle a changé un résultat : mesurer l'effet réel sur les votes est difficile. Mais l'existence de ces campagnes est établie.",
 empathie="Je comprends la méfiance : on a parfois l'impression qu'on agite la menace étrangère pour tout expliquer. Mais là, ce sont des campagnes précises, documentées par un service de l'État, avec des faux sites et des faux comptes. On peut les regarder ensemble.",
 legitimes=["Détecter une manœuvre ne prouve pas qu'elle a modifié le résultat d'une élection.", "L'accusation d'ingérence peut aussi être utilisée pour disqualifier des opinions légitimes."],
 contre=[
  ("C'est le gouvernement qui invente ça pour censurer.", "Les campagnes décrites (faux sites, usurpation de médias) sont documentées et ont été dénoncées par plusieurs États européens ; les détecter, ce n'est pas censurer des opinions."),
  ("Ça ne change rien aux résultats.", "C'est difficile à mesurer, et il faut rester prudent ; mais la volonté de manipuler est établie, et elle vise notre souveraineté démocratique."),
 ],
 questions=["Si un faux site imite un vrai journal pour diffuser une rumeur, tu appelles ça une opinion ?", "Comment vérifies-tu une information qui circule sur les réseaux ?"],
 limites=["Le rapport ne mesure pas l'effet de ces manœuvres sur les votes.", "Certaines attributions d'origine restent prudentes ou non publiques."],
 a_actualiser='2027-03-31',
))

FICHES.append(fiche(
 id='sondages-mille-personnes', affirmation="Un sondage sur mille personnes, ça ne veut rien dire.", volet='politique', sous_theme='Sondages',
 mots_cles=['sondages', 'sondage', 'mille personnes', '1000 personnes', 'marge d erreur', 'échantillon', 'truqués', 'commission des sondages', 'intervalle de confiance'],
 verdict='trompeur', fiabilite='etabli',
 resume="Un échantillon de 1 000 personnes bien construit donne une estimation avec une marge d'erreur connue : pour un score de 50 %, le vrai chiffre a 95 % de chances d'être entre 46,9 % et 53,1 %. Un sondage n'est pas une prédiction, c'est une estimation à un moment donné, et depuis 2016 sa marge d'erreur doit être publiée.",
 contexte="Les sondages sont souvent accusés d'être truqués ou de faire l'élection. Leur fonctionnement statistique est mal connu.",
 explication="La marge d'erreur dépend surtout de la taille de l'échantillon, pas de celle de la population. Elle est maximale autour de 50 %. Elle ne couvre pas les autres sources d'erreur (personnes qui refusent de répondre, changement d'avis).",
 sources=[PS_SONDAGES],
 faits=[
  fait("Pour un échantillon de 1 000 personnes et un intervalle de confiance de 95 %, un score de 10 % se situe entre 8,2 % et 11,8 %, et un score de 50 % entre 46,9 % et 53,1 %.", 'ps_sond', '2022', 'France', "La précision d'un sondage de 1 000 personnes est connue et chiffrable.", 'etabli', '3,1 points'),
  fait("Depuis une loi de 2016, la marge d'erreur doit être adressée à la Commission des sondages et publiée avec le sondage.", 'ps_sond', 'Depuis 2016', 'France', "La transparence est obligatoire : on peut vérifier.", 'etabli'),
 ],
 court="Si, à condition de lire la marge d'erreur : avec 1 000 personnes, un score de 50 % veut dire « entre 46,9 et 53,1 % », avec 95 % de confiance. Un sondage est une photo avec un flou connu, pas une prédiction, et sa marge d'erreur doit être publiée depuis 2016.",
 moyen="Ce qui compte, c'est la taille de l'échantillon et sa construction, pas la taille du pays. Avec 1 000 personnes, on connaît la précision : pour un score de 50 %, le vrai chiffre est entre 46,9 et 53,1 % dans 95 % des cas.\n\nLe vrai problème, c'est quand on commente des écarts de 1 ou 2 points comme s'ils voulaient dire quelque chose. Depuis 2016, la marge d'erreur doit être publiée : lisons-la avant de crier victoire ou à la manipulation.",
 detaille="Un sondage repose sur un échantillon : on interroge un nombre limité de personnes pour estimer l'opinion de l'ensemble. La précision dépend surtout de la taille de l'échantillon. Pour 1 000 personnes, avec un intervalle de confiance de 95 %, un score de 10 % se situe entre 8,2 et 11,8 %, et un score de 50 % entre 46,9 et 53,1 %.\n\nDepuis une loi de 2016, la marge d'erreur doit être transmise à la Commission des sondages et publiée avec le sondage.\n\nLa marge d'erreur ne couvre pas tout : refus de répondre, échantillons mal construits, changements d'avis avant le vote. Un sondage est une estimation à un moment donné, pas une prédiction. On peut critiquer leur usage médiatique, notamment les commentaires sur des écarts inférieurs à la marge d'erreur, sans dire qu'ils ne veulent rien dire.",
 empathie="Je comprends le doute : on n'a jamais été interrogé, et les sondages se trompent parfois. Mais la statistique permet de savoir à quel point ils peuvent se tromper. Le problème, c'est surtout la façon dont on les commente.",
 legitimes=["Les sondages peuvent se tromper au-delà de la marge d'erreur (refus de répondre, changements d'avis).", "Leur usage médiatique surinterprète souvent des écarts minimes."],
 contre=[
  ("On ne m'a jamais sondé.", "C'est normal : on n'interroge qu'environ 1 000 personnes ; la précision vient de la méthode, pas du fait que chacun soit interrogé."),
  ("Les sondages font l'élection.", "Leur influence est débattue ; ce qui est sûr, c'est qu'il faut les lire avec leur marge d'erreur et ne pas les prendre pour des prédictions."),
 ],
 questions=["Tu as déjà regardé la marge d'erreur d'un sondage avant de le commenter ?", "Pourquoi goûter une cuillère de soupe suffirait-il pour savoir si elle est salée ?"],
 limites=["La source est un article pédagogique ; les notices des instituts détaillent chaque sondage.", "La marge d'erreur calculée suppose un échantillon aléatoire ; les quotas sont une approximation."],
 a_actualiser='2028-06-30',
))

FICHES.append(fiche(
 id='abstention-inegale', affirmation="L'abstention, c'est un choix individuel : chacun est libre de ne pas voter.", volet='politique', sous_theme='Abstention',
 mots_cles=['abstention', 'abstentionnistes', 'voter ne sert à rien', 'vote', 'ne pas voter', 'participation électorale', 'jeunes', 'ouvriers', 'qui s abstient'],
 verdict='trompeur', fiabilite='etabli',
 resume="Chacun est libre de ne pas voter, mais l'abstention n'est pas répartie au hasard : en 2022, 30,1 % des non-diplômés se sont abstenus à tous les tours, contre 9,6 % des diplômés du supérieur ; 23,6 % des ouvriers non qualifiés contre 7,4 % des cadres (Insee). Ceux qui votent le moins sont ceux qui pèsent le moins dans les choix politiques.",
 contexte="L'abstention progresse depuis des décennies. On l'explique souvent par le désintérêt individuel.",
 explication="L'enquête de l'Insee sur la participation électorale suit chaque inscrit à tous les tours de 2022. Elle montre que l'abstention dépend fortement de l'âge, du diplôme et de la position sociale.",
 sources=[INSEE_VOTE],
 faits=[
  fait("Aux élections nationales de 2022, 36 % des inscrits ont voté à tous les tours, 48 % par intermittence et 16 % se sont abstenus à tous les tours.", 'insee_vote', '2022', 'France, inscrits', "L'abstention totale est minoritaire ; le vote intermittent domine.", 'etabli', '16 %'),
  fait("L'abstention systématique atteint 30,1 % chez les non-diplômés contre 9,6 % chez les diplômés du supérieur, et 23,6 % chez les ouvriers non qualifiés contre 7,4 % chez les cadres.", 'insee_vote', '2022', 'Inscrits de 25 ans ou plus', "L'abstention est socialement inégale : les classes populaires sont moins représentées.", 'etabli', '30,1 % / 9,6 %'),
  fait("23,8 % des 18-24 ans se sont abstenus à tous les tours, contre 9,2 % des 60-64 ans.", 'insee_vote', '2022', 'Inscrits', "Les jeunes pèsent moins dans les élections.", 'etabli', '23,8 %'),
 ],
 court="Libre, oui ; réparti au hasard, non : en 2022, 30 % des non-diplômés se sont abstenus à tous les tours, contre moins de 10 % des diplômés du supérieur (Insee). Ceux qui votent le moins sont ceux dont on tient le moins compte.",
 moyen="L'abstention n'est pas un simple choix personnel. L'Insee a suivi les électeurs sur tous les tours de 2022 : 30,1 % des non-diplômés n'ont voté à aucun tour, contre 9,6 % des diplômés du supérieur ; 23,6 % des ouvriers non qualifiés, contre 7,4 % des cadres ; 23,8 % des 18-24 ans.\n\nRésultat : les politiques s'adressent d'abord à ceux qui votent. Faire revenir les classes populaires et les jeunes aux urnes, c'est une question d'égalité démocratique.",
 detaille="L'enquête de l'Insee sur la participation aux élections de 2022 montre que seul un tiers des inscrits (36 %) a voté à tous les tours, 48 % ont voté par intermittence et 16 % se sont abstenus à chaque fois.\n\nL'abstention systématique est très inégale : 30,1 % chez les non-diplômés contre 9,6 % chez les diplômés du supérieur ; 23,6 % chez les ouvriers non qualifiés contre 7,4 % chez les cadres ; 23,8 % chez les 18-24 ans contre 9,2 % chez les 60-64 ans.\n\nLe droit de ne pas voter existe. Mais quand l'abstention se concentre dans certains groupes sociaux, la représentation politique se déforme : les préoccupations des plus votants pèsent davantage. Comprendre l'abstention, c'est donc aussi poser la question de la place des classes populaires dans la démocratie.",
 empathie="Je comprends qu'on n'ait plus envie de voter quand on a l'impression que rien ne change. Mais regarde : ce sont surtout les ouvriers, les jeunes et les moins diplômés qui s'abstiennent. Du coup, ce sont ceux dont les politiques s'occupent le moins.",
 legitimes=["Le droit de ne pas voter fait partie de la liberté démocratique.", "L'abstention peut exprimer un rejet politique conscient, pas seulement un désintérêt."],
 contre=[
  ("Voter ne sert à rien, ils sont tous pareils.", "Les politiques tiennent compte des électorats qui votent ; quand les classes populaires s'abstiennent beaucoup plus, leurs intérêts pèsent moins."),
  ("Ceux qui ne votent pas n'ont qu'à ne pas se plaindre.", "Les écarts d'abstention suivent le diplôme et la position sociale : ce n'est pas seulement une affaire de volonté individuelle."),
 ],
 questions=["Pourquoi crois-tu que les cadres votent trois fois plus souvent que les ouvriers non qualifiés ?", "Qu'est-ce qui donnerait envie aux gens qui ne votent plus de revenir ?"],
 limites=["L'enquête porte sur les élections nationales de 2022.", "Elle mesure la participation, pas les raisons de l'abstention."],
 a_actualiser='2027-12-31',
))

FICHES.append(fiche(
 id='gauche-au-pouvoir-bilan', affirmation="La gauche n'a jamais rien fait de bien au pouvoir.", volet='politique', sous_theme='Histoire politique contemporaine',
 mots_cles=['gauche au pouvoir', 'bilan de la gauche', 'mitterrand', 'jospin', '35 heures', 'retraite à 60 ans', 'peine de mort', 'réformes sociales', 'jamais rien fait', '1981'],
 verdict='contredit', fiabilite='etabli',
 resume="Les gouvernements de gauche ont porté des réformes majeures : abolition de la peine de mort (1981), retraite à 60 ans (1982), réduction du temps de travail (environ 350 000 emplois créés selon l'Insee), sans oublier les congés payés de 1936 ou la Sécurité sociale de 1945. Leur bilan comporte aussi des échecs et des renoncements, qu'il faut regarder en face.",
 contexte="L'idée que la gauche « n'a jamais rien fait » revient souvent, à droite comme chez des déçus de la gauche.",
 explication="Les réformes peuvent être évaluées à partir de sources publiques : textes de loi, rapports parlementaires, études de la statistique publique.",
 sources=[SENAT_1981, COR, INSEE_RTT, AN_RTT],
 faits=[
  fait("Après l'élection de François Mitterrand, un projet de loi portant abolition de la peine de mort est déposé le 29 août 1981 et défendu par Robert Badinter ; il aboutit à la loi du 9 octobre 1981.", 'senat81', '1981', 'France', "Une réforme de civilisation portée par la gauche, après l'échec des tentatives précédentes.", 'etabli'),
  fait("L'ordonnance du 26 mars 1982 généralise la retraite à 60 ans, avec au moins 37,5 ans de cotisation.", 'cor', '1982', 'France', "Un droit social majeur obtenu sous un gouvernement de gauche.", 'etabli', '60 ans'),
  fait("Selon une étude publiée par l'Insee, la réduction du temps de travail a créé près de 350 000 postes sur 1998-2002, sans grand déséquilibre financier pour les entreprises.", 'insee_rtt', '1998-2002', 'France', "Les 35 heures ont eu un effet mesurable sur l'emploi.", 'estimation', '350 000'),
  fait("Selon le rapport parlementaire de 2014, les prévisions initiales espéraient 700 000 postes, et le président de la commission ne partageait pas les conclusions favorables du rapport.", 'an_rtt', '2014', 'France', "Les résultats ont été inférieurs aux promesses et restent discutés.", 'debat', '700 000'),
 ],
 court="Faux : abolition de la peine de mort en 1981, retraite à 60 ans en 1982, 35 heures avec environ 350 000 emplois créés selon l'Insee, et avant ça les congés payés et la Sécu. On peut critiquer des échecs de la gauche, pas prétendre qu'elle n'a rien fait.",
 moyen="Il suffit de regarder les textes. En 1981, la gauche abolit la peine de mort, défendue par Robert Badinter. En 1982, la retraite à 60 ans est généralisée. Entre 1998 et 2002, la réduction du temps de travail crée près de 350 000 emplois selon une étude publiée par l'Insee.\n\nEt avant ça : les congés payés du Front populaire, la Sécurité sociale issue du programme du CNR. Bien sûr, il y a eu des échecs et des renoncements : on peut en débattre. Mais « rien fait de bien », c'est faux.",
 detaille="L'histoire récente de la gauche au pouvoir comporte des réformes majeures, documentées par des sources publiques.\n\nEn 1981, après l'élection de François Mitterrand, un projet de loi d'abolition « définitive et générale » de la peine de mort est déposé et défendu par le garde des Sceaux Robert Badinter ; il aboutit à la loi du 9 octobre 1981, après l'échec des tentatives de 1979 et 1980. En 1982, l'ordonnance du 26 mars généralise la retraite à 60 ans pour 37,5 années de cotisation.\n\nSous le gouvernement Jospin, la réduction du temps de travail a créé près de 350 000 emplois entre 1998 et 2002 selon une étude publiée par l'Insee. C'est moins que les 700 000 espérés au départ, et le bilan reste discuté : le président de la commission d'enquête parlementaire de 2014 ne partageait pas ses conclusions favorables.\n\nOn peut et on doit débattre des échecs et des renoncements de la gauche, notamment des politiques de rigueur. Mais l'idée qu'elle n'aurait « jamais rien fait » ne résiste pas aux faits.",
 empathie="Je comprends la déception : beaucoup de gens de gauche ont été déçus par leurs gouvernements. Mais si on regarde l'histoire, il y a des choses qui ont changé la vie de tout le monde : les congés payés, la Sécu, la retraite à 60 ans, l'abolition de la peine de mort.",
 legitimes=["Les gouvernements de gauche ont aussi connu des échecs et des renoncements, notamment des politiques de rigueur.", "Les créations d'emplois des 35 heures ont été inférieures aux prévisions et restent discutées."],
 contre=[
  ("La retraite à 60 ans, on ne pouvait pas se la payer.", "Le débat sur le financement des retraites est légitime ; mais c'était un choix de répartition des gains de productivité, pas une impossibilité."),
  ("Les 35 heures ont tué la compétitivité.", "Une étude publiée par l'Insee estime qu'elles ont créé près de 350 000 emplois sans grand déséquilibre financier pour les entreprises ; leur bilan reste discuté, mais pas catastrophique."),
 ],
 questions=["Tu voudrais revenir sur l'abolition de la peine de mort ou sur les congés payés ?", "Quelle réforme sociale importante n'a pas été portée par la gauche, selon toi ?"],
 limites=["Les évaluations des 35 heures divergent selon les méthodes.", "Cette fiche ne fait pas le bilan complet des gouvernements de gauche."],
 stabilite='historique',
))

INSEE_HIST = ('insee_hist', src("Histoire des migrations et diversité des origines géographiques des immigrés (Immigrés et descendants d'immigrés en France, édition 2023)", "Insee (Insee Références)", "30 mars 2023",
  "https://www.insee.fr/fr/statistiques/6793226",
  "Part des immigrés dans la population : 2,8 % en 1911, 3,7 % en 1921, 6,6 % en 1931, 7,4 % en 1975, 10,3 % en 2021. Dans les années 1920, arrivées de Belgique, d'Italie, d'Espagne, de Pologne, de Russie et d'Arménie pour compenser les pertes de la Grande Guerre ; Office national d'immigration créé en 1945 pour recruter des travailleurs étrangers ; pendant les Trente Glorieuses, immigration espagnole et algérienne, puis portugaise, marocaine et turque ; immigration de travail freinée en 1974.",
  "Statistique publique de référence."))
AN_AT = ('an_at', src("Réponse du ministère du Travail et des Solidarités à la question écrite n° 10291 (accidents du travail mortels)", "Assemblée nationale / ministère du Travail et des Solidarités", "3 mars 2026",
  "https://questions.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE10291.pdf",
  "764 accidents du travail mortels en 2024 au régime général et 51 en 2023 au régime agricole ; après une baisse de plusieurs décennies, le nombre d'accidents mortels a atteint « un plancher dans les années 2010 » ; en 2019, 4,81 accidents mortels pour 100 000 salariés en France contre 2,17 en moyenne européenne, comparaison délicate (la France compte les malaises mortels) ; publics prioritaires : intérim, travaux en hauteur, transport routier, jeunes, travailleurs détachés et saisonniers.",
  "Réponse ministérielle officielle."))

FICHES.append(fiche(
 id='france-pays-immigration', affirmation="La France n'a jamais été un pays d'immigration.", volet='immigration', sous_theme='Histoire des migrations',
 mots_cles=['pays d immigration', 'histoire de l immigration', 'italiens', 'polonais', 'espagnols', 'portugais', 'il y a cent ans', 'après la guerre', 'reconstruit', 'intégration', 'avant'],
 verdict='contredit', fiabilite='etabli',
 resume="La France est un pays d'immigration depuis plus d'un siècle : les immigrés représentaient près de 3 % de la population en 1911, 6,6 % en 1931 et 10,3 % en 2021 (Insee). Belges, Italiens, Polonais, Espagnols puis Portugais et Maghrébins sont venus, souvent recrutés pour reconstruire le pays et faire tourner son industrie.",
 contexte="On oppose souvent une immigration d'autrefois, qui se serait bien intégrée, à celle d'aujourd'hui. L'histoire montre que chaque vague a d'abord été mal accueillie.",
 explication="Les recensements permettent de suivre la part des immigrés dans la population depuis plus d'un siècle, et l'Insee retrace les grandes vagues migratoires et leurs causes.",
 sources=[INSEE_HIST],
 faits=[
  fait("La part des immigrés dans la population est passée de 2,8 % en 1911 à 6,6 % en 1931, puis 7,4 % en 1975 et 10,3 % en 2021.", 'insee_hist', '1911-2021', 'France', "L'immigration est ancienne et massive dès l'entre-deux-guerres.", 'etabli', '6,6 %'),
  fait("Dans les années 1920, des immigrés venus de Belgique, d'Italie, d'Espagne, de Pologne, de Russie et d'Arménie arrivent pour compenser les pertes humaines de la Grande Guerre.", 'insee_hist', 'Années 1920', 'France', "L'immigration a répondu aux besoins du pays.", 'etabli'),
  fait("L'Office national d'immigration est créé en 1945 pour recruter des travailleurs étrangers ; pendant les Trente Glorieuses arrivent des Espagnols et des Algériens, puis des Portugais, des Marocains et des Turcs.", 'insee_hist', '1945-1974', 'France', "L'État a lui-même organisé l'immigration de travail.", 'etabli'),
 ],
 court="Faux : dès 1931, les immigrés représentaient 6,6 % de la population, contre 10,3 % aujourd'hui (Insee). Italiens, Polonais, Espagnols, Portugais, Maghrébins : la France les a souvent recrutés elle-même pour reconstruire et produire.",
 moyen="La France est un vieux pays d'immigration. Selon l'Insee, les immigrés étaient près de 3 % de la population en 1911, 6,6 % en 1931, 10,3 % en 2021.\n\nAprès la Première Guerre mondiale, on fait venir Belges, Italiens, Polonais pour remplacer les morts. En 1945, l'État crée l'Office national d'immigration pour recruter des travailleurs. Et chaque vague a été accusée, à son époque, de ne pas pouvoir s'intégrer.",
 detaille="Les recensements montrent une immigration ancienne. Selon l'Insee, les immigrés représentaient 2,8 % de la population en 1911, 6,6 % en 1931 (un niveau proche de celui des années 1970), 7,4 % en 1975 et 10,3 % en 2021.\n\nDans les années 1920, la France fait venir des travailleurs de Belgique, d'Italie, d'Espagne et de Pologne, et accueille des réfugiés russes et arméniens, pour compenser les pertes de la Grande Guerre. En 1945, l'État crée l'Office national d'immigration pour recruter des travailleurs étrangers. Pendant les Trente Glorieuses arrivent Espagnols et Algériens, puis Portugais, Marocains et Turcs ; l'immigration de travail est freinée en 1974, et l'immigration familiale prend le relais.\n\nL'histoire de France est donc aussi une histoire d'immigration, souvent organisée par l'État lui-même, au service de la reconstruction et de l'industrie.",
 empathie="Je comprends qu'on ait l'impression que l'immigration est un phénomène récent. Mais regarde : en 1931, il y avait déjà 6,6 % d'immigrés. Beaucoup de familles françaises ont un grand-parent italien, polonais ou espagnol.",
 legitimes=["La part des immigrés est aujourd'hui plus élevée qu'aux époques précédentes.", "Les origines des immigrés ont changé au cours du siècle."],
 contre=[
  ("Avant, ils s'intégraient ; aujourd'hui, non.", "Chaque vague a été accusée de ne pas pouvoir s'intégrer à son époque ; l'histoire montre que l'intégration prend du temps, sur plusieurs générations."),
  ("Les Italiens, eux, étaient européens et chrétiens.", "Ils ont pourtant subi une forte xénophobie à leur arrivée ; l'argument de la proximité culturelle est souvent reconstruit après coup."),
 ],
 questions=["Tu sais combien d'immigrés il y avait en France en 1931 ?", "Dans ta famille ou chez tes voisins, il n'y a personne qui a des origines italiennes, polonaises, espagnoles ou portugaises ?"],
 limites=["Les données historiques reposent sur les recensements, dont les définitions ont évolué."],
 stabilite='historique',
))

FICHES.append(fiche(
 id='morts-au-travail', affirmation="Les accidents du travail, c'est un problème du passé.", volet='droits', sous_theme='Droits des travailleurs',
 mots_cles=['accidents du travail', 'morts au travail', 'sécurité au travail', 'santé au travail', 'code du travail', 'droit du travail', 'inspection du travail', 'mortalité au travail', 'btp', 'intérim'],
 verdict='contredit', fiabilite='etabli',
 resume="En 2024, 764 accidents du travail mortels ont été reconnus au régime général, et 51 en 2023 au régime agricole. Après des décennies de baisse, le nombre de morts ne diminue plus depuis les années 2010, et la France se situe au-dessus de la moyenne européenne, même si les comparaisons sont délicates.",
 contexte="On imagine souvent que les accidents mortels appartiennent à l'industrie d'autrefois. Ils touchent aujourd'hui notamment l'intérim, le bâtiment, le transport et les jeunes travailleurs.",
 explication="Les chiffres viennent des régimes de sécurité sociale qui reconnaissent les accidents du travail. La réponse du ministère du Travail rappelle les tendances et les publics les plus exposés.",
 sources=[AN_AT],
 faits=[
  fait("764 accidents du travail mortels ont été reconnus en 2024 au régime général, et 51 en 2023 au régime agricole.", 'an_at', '2023-2024', 'France', "Chaque année, des centaines de personnes meurent en travaillant.", 'etabli', '764'),
  fait("Après une baisse de plusieurs décennies, le nombre d'accidents mortels a atteint un plancher dans les années 2010 et ne diminue plus.", 'an_at', 'Depuis les années 2010', 'France', "Les progrès se sont arrêtés.", 'etabli'),
  fait("En 2019, la France comptait 4,81 accidents mortels pour 100 000 salariés, contre 2,17 en moyenne européenne ; le ministère souligne que la comparaison est délicate car la France compte les malaises mortels.", 'an_at', '2019', 'France et Union européenne', "La France n'est pas un modèle en matière de sécurité au travail.", 'estimation', '4,81'),
 ],
 court="Faux : en 2024, 764 personnes sont mortes d'un accident du travail au régime général, et les progrès sont bloqués depuis les années 2010 (ministère du Travail). Les plus exposés : intérimaires, jeunes, BTP, transport.",
 moyen="Ce n'est pas de l'histoire ancienne : le ministère du Travail compte 764 accidents mortels en 2024 au régime général, plus les agriculteurs. Après des décennies de baisse, ça ne baisse plus depuis les années 2010.\n\nEt la France fait plutôt moins bien que ses voisins, même si les comparaisons sont délicates. Les plus touchés sont les intérimaires, les jeunes, les travailleurs du bâtiment et du transport. Le droit du travail et l'inspection du travail ne sont pas des contraintes inutiles : ils sauvent des vies.",
 detaille="Selon la réponse du ministère du Travail publiée en mars 2026, 764 accidents du travail mortels ont été reconnus en 2024 au régime général ; le régime agricole en comptait 51 en 2023. Après une longue baisse sur plusieurs décennies, ce nombre a atteint un plancher dans les années 2010.\n\nEn 2019, la France comptait 4,81 accidents mortels pour 100 000 salariés, contre 2,17 en moyenne européenne ; le ministère rappelle que la comparaison est délicate, la France comptabilisant notamment les malaises mortels survenus au travail.\n\nLes publics prioritaires identifiés sont les intérimaires, les travailleurs en hauteur, le transport routier, les jeunes, les indépendants, les travailleurs détachés et saisonniers. Les accidents non mortels ont, eux, baissé entre 2019 et 2023. La santé et la sécurité au travail restent un enjeu majeur de protection des travailleurs.",
 empathie="Je comprends qu'on pense que c'est réglé : les usines d'autrefois ont disparu. Mais des centaines de personnes meurent encore chaque année en travaillant, souvent des jeunes ou des intérimaires. Ça vaut la peine d'en parler.",
 legitimes=["Les accidents du travail non mortels ont baissé entre 2019 et 2023.", "Les comparaisons européennes sont délicates, la France comptant les malaises mortels."],
 contre=[
  ("Le Code du travail est trop lourd.", "Une partie de ces règles protège la santé et la vie des salariés ; avec des centaines de morts par an, les alléger n'est pas sans conséquences."),
  ("C'est souvent la faute de l'imprudence.", "Les publics les plus touchés (intérimaires, jeunes, détachés) sont aussi les moins formés et les plus précaires : c'est une question d'organisation du travail."),
 ],
 questions=["Tu savais qu'il y a plus de 700 morts au travail par an ?", "Qui doit être responsable de la sécurité d'un intérimaire sur un chantier ?"],
 limites=["Les chiffres portent sur les accidents reconnus ; les maladies professionnelles ne sont pas comptées ici."],
 a_actualiser='2027-03-31',
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
