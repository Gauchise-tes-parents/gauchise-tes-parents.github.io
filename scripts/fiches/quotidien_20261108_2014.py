"""Fiches quotidiennes du 8 novembre 2026, passage de 20 h 14 (UTC) — phase alpha.

25 questions qui circulent (extrême droite, clichés sur la gauche, programmes) et qui n'avaient pas de fiche
qui leur réponde (lacunes ou questions orientées vers une fiche hors sujet). Toutes les sources ont été ouvertes
et lues le 8 novembre 2026 (consultee=True) ; les chiffres viennent uniquement des passages cités.
Données anciennes signalées dans les limites. Chaque fiche contient « publics » (électeur d'extrême droite convaincu / indécis).
Usage : python3 scripts/fiches/quotidien_20261108_2014.py  (puis node scripts/corrections-v10.js et node scripts/enrichir-fiches.js)
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche as _fiche, OUT

TODAY = '2026-11-08'

def fiche(**k):
    d = _fiche(**k)
    d['derniere_verification'] = TODAY
    return d

FICHES = []

# ══ Lot A : économie et social ══════════════════════════════════════════════

# 1 ── Semaine de 32 heures ─────────────────────────────────────────────────
NFP_PROGRAMME_2024 = ('nfp_programme_2024', src('Nouveau Front populaire. Contrat de législature', "Programme du Nouveau Front populaire, reproduit par L'Humanité", '15 juin 2024',
  'https://www.zoomdici.fr/sites/default/files/upload/documents/lhumanite-presente-le-programme-du-nouveau-front-populaire.pdf',
  "Dans la partie « Défendre les droits des travailleurs », le programme prévoit d'« Organiser une conférence nationale sur le travail et la pénibilité » en vue « du rétablissement de la durée effective hebdomadaire du travail à 35 heures », « du passage aux 32 heures dans les métiers pénibles ou de nuit immédiatement » et de « son extension par la négociation collective ».",
  "Texte du programme lui-même (copie du journal hébergée par un site tiers) ; décrit la position du NFP.", 'primaire'))
INSEE_RTT_2005 = ('insee_rtt_2005', src("Les effets de la RTT sur l'emploi : des estimations ex ante aux évaluations ex post", 'Insee, Économie et Statistique n° 376-377 (A. Gubian, S. Jugnot, F. Lerais, V. Passeron, Dares/Insee)', 'juin 2005',
  'https://www.insee.fr/fr/statistiques/1376464',
  "Les auteurs estiment que la réduction du temps de travail a entraîné sur 1998-2002 un « rapide enrichissement de la croissance en emplois de près de 350 000 postes ». La baisse effective de la durée du travail a été moins forte que prévu. L'équilibre a reposé sur la baisse de la durée, la modération salariale, les gains de productivité et l'aide de l'État, sans grand déséquilibre financier pour les entreprises.",
  'Statistique publique de référence ; donnée ancienne (2005).', 'etude'))
AN_RAPPORT_35H_2014 = ('an_rapport_35h_2014', src("Rapport de la commission d'enquête sur l'impact de la réduction progressive du temps de travail (n° 2436)", 'Assemblée nationale (rapporteure Barbara Romagnan, président Thierry Benoit)', '9 décembre 2014',
  'https://www.assemblee-nationale.fr/14/pdf/rap-enq/r2436.pdf',
  "« Le chiffre de 350 000 est le plus communément admis » pour les emplois créés par les 35 heures, alors que les prévisions initiales en espéraient 700 000. Le coût net ex post des lois Aubry pour les finances publiques « s'élève à 2,5 milliards ». Le rapport reconnaît l'intensification du travail, des tensions à l'hôpital et des difficultés dans les TPE-PME. Le président de la commission écrit ne pas partager les conclusions de la rapporteure.",
  'Rapport parlementaire officiel ; conclusions contestées par le président de la commission ; donnée ancienne (2014).', 'primaire'))
MONTAIGNE_32H_2022 = ('montaigne_32h_2022', src('Passer à la semaine de travail à 32h (chiffrage du programme de Fabien Roussel)', 'Institut Montaigne', '14 février 2022',
  'https://www.institutmontaigne.org/presidentielle-2022/fabien-roussel/passer-a-la-semaine-de-travail-a-32h/',
  "L'institut chiffre le coût budgétaire annuel net de 32 heures généralisées sans perte de salaire à 4,8, 6,2 ou 7,4 Md€ selon les hypothèses, avec 180 000 à 280 000 emplois publics supplémentaires. Il estime que « la mesure devrait conduire à une hausse du coût du travail comprise entre 2,5 et 4 points de marge ». Il prévoit un effet positif à court terme sur l'emploi, mais une baisse de l'activité des entreprises à moyen terme.",
  "Think tank libéral, proche du patronat (orientation à signaler) ; il chiffre une mesure plus large que celle du NFP de 2024.", 'etude'))
CORDIS_4JOURS_2023 = ('cordis_4jours_2023', src('La semaine de travail de quatre jours est-elle justifiée d’un point de vue scientifique ?', 'CORDIS, Commission européenne', '20 avril 2023',
  'https://cordis.europa.eu/article/id/443330-does-the-science-back-a-4-day-workweek/fr',
  "L'article présente le pilote britannique de 2022 : « 40 % des quelque 2 900 employés de 61 sociétés » déclarent moins de troubles du sommeil ; 56 entreprises poursuivent l'expérience et 18 la rendent permanente. Aucune mesure de productivité n'est donnée.",
  "Service d'information de la Commission européenne ; résultats déclaratifs, sans groupe témoin.", 'secondaire'))

FICHES.append(fiche(
 id='semaine-32-heures', affirmation="La semaine de 32 heures proposée par la gauche ruinerait l'économie.", volet='social', sous_theme='Emploi et salaires',
 mots_cles=['32 heures', '32h', 'semaine de 32', 'semaine de quatre jours', 'semaine de 4 jours', 'reduction du temps de travail', 'passer aux 32 heures'],
 verdict='trompeur', fiabilite='estimation',
 resume="Le programme du Nouveau Front populaire de 2024 ne prévoyait pas les 32 heures pour tous par la loi : il visait les métiers pénibles ou de nuit, puis une extension par la négociation. Le précédent des 35 heures a créé environ 350 000 emplois selon l'Insee et la Dares. Une généralisation sans perte de salaire aurait un coût réel pour les entreprises, mais aucune étude lue ne prédit une « ruine ».",
 contexte="Les 32 heures reviennent régulièrement dans les programmes de gauche (PCF en 2022, NFP en 2024) et sont présentées par leurs adversaires comme la preuve d'un programme irresponsable.",
 explication="Il faut distinguer ce que proposent vraiment les programmes, ce qu'a montré l'expérience des 35 heures et ce que coûterait une généralisation.",
 sources=[NFP_PROGRAMME_2024, INSEE_RTT_2005, AN_RAPPORT_35H_2014, MONTAIGNE_32H_2022, CORDIS_4JOURS_2023],
 faits=[
  fait("Le programme du NFP (2024) prévoyait de rétablir les 35 heures effectives, de passer immédiatement aux 32 heures dans les métiers pénibles ou de nuit, puis de les étendre par la négociation collective.", 'nfp_programme_2024', '2024', 'France', "La mesure était ciblée, pas généralisée par la loi.", 'etabli'),
  fait("Selon l'Insee et la Dares, la réduction du temps de travail a créé près de 350 000 emplois entre 1998 et 2002.", 'insee_rtt_2005', '1998-2002', 'France', "Le précédent des 35 heures n'a pas ruiné l'économie.", 'etabli', '350 000 emplois'),
  fait("Le rapport parlementaire de 2014 évalue le coût net des lois Aubry pour les finances publiques à 2,5 milliards d'euros, et relève aussi l'intensification du travail et des difficultés à l'hôpital.", 'an_rapport_35h_2014', '1998-2014', 'France', "Le bilan comporte des coûts et des effets négatifs, à reconnaître.", 'etabli', '2,5 milliards'),
  fait("Selon l'Institut Montaigne, des 32 heures généralisées sans perte de salaire coûteraient 4,8 à 7,4 Md€ par an au budget et réduiraient de 2,5 à 4 points la marge des entreprises.", 'montaigne_32h_2022', '2022', 'France', "Une généralisation brutale aurait un coût réel : c'est un fait défavorable.", 'estimation'),
  fait("Dans le pilote britannique de la semaine de quatre jours (61 entreprises, environ 2 900 salariés), 56 entreprises ont poursuivi l'expérience et 18 l'ont rendue permanente, selon la Commission européenne.", 'cordis_4jours_2023', '2022-2023', 'Royaume-Uni', "Des entreprises adoptent volontairement une durée plus courte.", 'estimation'),
 ],
 court="Le NFP proposait les 32 heures d'abord dans les métiers pénibles ou de nuit, puis par la négociation. Les 35 heures ont créé environ 350 000 emplois selon l'Insee. Une généralisation brutale coûterait cher, mais personne de sérieux ne parle de « ruine ».",
 moyen="Le programme du Nouveau Front populaire de 2024 prévoyait de rétablir les 35 heures effectives, de passer aux 32 heures immédiatement dans les métiers pénibles ou de nuit, puis d'étendre la mesure par la négociation collective. Ce n'est pas la semaine de 32 heures imposée à tous du jour au lendemain.\n\nLe précédent existe : selon l'Insee et la Dares, les 35 heures ont créé près de 350 000 emplois. Elles ont aussi intensifié le travail et compliqué la vie de l'hôpital, il faut le dire. Une généralisation sans perte de salaire aurait un coût pour les entreprises, chiffré par l'Institut Montaigne. Mais c'est un débat sur le rythme et le financement, pas une ruine annoncée.",
 detaille="Commençons par ce qui est proposé. Le programme du NFP de 2024 visait les 32 heures dans les métiers pénibles ou de nuit, avec une extension par la négociation collective, et le retour à 35 heures effectives. Le PCF proposait en 2022 des 32 heures plus larges.\n\nLe précédent des 35 heures est le meilleur repère. Selon l'Insee et la Dares, la réduction du temps de travail a créé près de 350 000 emplois entre 1998 et 2002. Le rapport parlementaire de 2014 retient le même ordre de grandeur et un coût net pour les finances publiques de 2,5 milliards. Il reconnaît aussi l'intensification du travail, des tensions à l'hôpital et des difficultés dans les petites entreprises ; le président de la commission ne partageait pas ses conclusions.\n\nUne généralisation sans perte de salaire coûterait cher : l'Institut Montaigne chiffre 4,8 à 7,4 Md€ par an pour le budget et 2,5 à 4 points de marge en moins pour les entreprises. C'est un argument sérieux pour avancer progressivement. À l'étranger, des entreprises adoptent volontairement la semaine de quatre jours. Le temps libéré est une conquête sociale qui se négocie, comme les congés payés en 1936.",
 empathie="Il est normal de se demander qui paiera et si les petites entreprises suivront. Ces questions méritent des réponses précises plutôt que des slogans.",
 legitimes=["Une généralisation sans perte de salaire augmenterait le coût du travail.", "Les 35 heures ont intensifié le travail et désorganisé une partie de l'hôpital."],
 contre=[
  ("Les 35 heures ont plombé la compétitivité.", "Les évaluations publiques retiennent environ 350 000 emplois créés ; les effets négatifs existent mais sont localisés."),
  ("Les petites entreprises ne pourront pas suivre.", "C'est pourquoi le programme passait d'abord par les métiers pénibles et la négociation, et non par une obligation immédiate pour tous."),
 ],
 questions=["Savais-tu que le programme du NFP visait d'abord les métiers pénibles et de nuit ?", "Qu'est-ce qui te semble le plus réaliste : une loi immédiate ou une négociation par secteur ?"],
 limites=["Les évaluations des 35 heures datent de 2005 et 2014 ; le contexte de forte croissance de 1998-2002 n'est pas transposable tel quel.", "Le chiffrage de l'Institut Montaigne porte sur des 32 heures généralisées (programme Roussel 2022), pas sur la mesure du NFP.", "Les études de la Dares de 2004 n'ont pas pu être ouvertes (vérification anti-robot)."],
 publics={'convaincus': "Le programme du NFP ne mettait pas tout le monde à 32 heures du jour au lendemain : il visait d'abord les métiers pénibles et de nuit. Les 35 heures, tant critiquées, ont créé environ 350 000 emplois selon l'Insee. Le coût existe, mais parler de ruine, aucune étude ne le dit.",
  'indecis': "La question du coût est légitime : une généralisation brutale pèserait sur les entreprises. Mais la proposition était progressive et négociée, et l'expérience des 35 heures a montré des créations d'emplois. On peut en débattre sur le rythme et le financement."},
 a_actualiser='2027-12-31', raison="Nouveaux programmes et évaluations du temps de travail.",
))

# 2 ── Trou de la Sécu ──────────────────────────────────────────────────────
SANTEMENTALE_COUR_2026 = ('santementale_cour_2026', src('Le déficit de la Sécurité sociale se creuse encore en 2025', 'Santé Mentale (presse spécialisée), sur le rapport de la Cour des comptes', '29 mai 2026',
  'https://www.santementale.fr/2026/05/le-deficit-de-la-securite-sociale-se-creuse-encore-en-2025/',
  "Selon la Cour des comptes, le déficit « a doublé en deux ans pour atteindre 21,6 Md€ en 2025 », le plus haut depuis 2012 hors années Covid. « La progression des recettes (2,6 %) a été plus faible que celle des dépenses (3,6 %) ». La Cour prévoit 19,4 Md€ en 2026 et demande un retour à l'équilibre en 2030, soit environ 10 Md€ d'économies ou de recettes chaque année.",
  "Presse professionnelle qui rend compte d'un rapport de la Cour des comptes.", 'media'))
ACTEURSPUBLICS_DSS_2026 = ('acteurspublics_dss_2026', src('Déficit de la Sécurité sociale : la quasi-totalité des branches dans le rouge en 2025', 'Acteurs publics (Philippine Ramognino), d’après la Direction de la Sécurité sociale', '20 mars 2026',
  'https://acteurspublics.fr/articles/deficit-de-la-securite-sociale-la-quasi-totalite-des-branches-dans-le-rouge-en-2025/',
  "Le déficit des régimes de base et du FSV est de 21,6 Md€ en 2025, contre 23 Md€ prévus. Branche maladie : 15,9 Md€ ; vieillesse : 7,2 Md€ ; la branche famille est en excédent de 1,2 Md€. Le déficit vieillesse s'explique « en raison du mécanisme différé de revalorisation des pensions dans un contexte de désinflation ». Le ralentissement de l'inflation a aussi réduit les recettes.",
  "Presse spécialisée de l'action publique, qui reprend des données administratives.", 'media'))
SENAT_PLFSS_2027 = ('senat_plfss_2027', src('Projet de loi de financement de la sécurité sociale pour 2027 : présentation du rapporteur général', 'Sénat (rapporteur général Olivier Henno)', '4 novembre 2026',
  'https://www.banquedesterritoires.fr/sites/default/files/2026-11/Se%CC%81nat_pre%CC%81sentation_PLFSS%202027_RG.pdf',
  "« Déficit 2026 de la sécurité sociale : 21,8 Md€ ». Pour 2027, le texte initial prévoit 696,4 Md€ de dépenses pour 683,7 Md€ de recettes, soit un solde de -12,7 Md€. Les projections donnent environ 17 Md€ de déficit en 2029, et près de 30 Md€ avec des hypothèses moins favorables.",
  'Document officiel du Sénat (copie hébergée par Localtis).', 'primaire'))
PUBLICSENAT_COUR_SECU_2026 = ('publicsenat_cour_secu_2026', src('« Une situation hautement périlleuse » : pour la Cour des comptes, la France ne peut plus différer les efforts pour résorber le trou de la Sécu', 'Public Sénat (Guillaume Jacquot)', '20 octobre 2026',
  'https://www.publicsenat.fr/actualites/sante/une-situation-hautement-perilleuse-pour-la-cour-des-comptes-la-france-ne-peut-plus-differer-les-efforts-pour-resorber-le-trou-de-la-secu',
  "La Cour des comptes qualifie la situation de « hautement périlleuse ». La dette de l'Acoss pourrait atteindre 130 Md€ en 2030, ce que la Cour juge insoutenable ; la Cades doit encore rembourser 104,2 Md€ d'ici 2033. Le ralentissement économique a réduit les recettes de cotisations.",
  'Média parlementaire public.', 'media'))
INSEE_APU_2025 = ('insee_apu_2025', src('Le compte des administrations publiques en 2025 (Insee Première n° 2106)', 'Insee', '29 mai 2026',
  'https://www.insee.fr/fr/statistiques/8997691',
  "Le déficit public est de 152,5 Md€ (5,1 % du PIB) en 2025 et la dette publique de 3 460,5 Md€ (115,7 % du PIB). Les administrations de sécurité sociale sont en déficit de 6,7 Md€ en comptabilité nationale (contre +1,1 Md€ en 2024) et leur dette atteint 293,1 Md€. Les prélèvements obligatoires représentent 43,6 % du PIB, les dépenses publiques 57,3 %. Les charges d'intérêts atteignent 64,7 Md€ (+11,2 %).",
  'Statistique publique de référence.', 'primaire'))
LCP_EXONERATIONS_2023 = ('lcp_exonerations_2023', src('Exonérations de cotisations sociales patronales : un rapport parlementaire préconise de resserrer le dispositif', 'LCP (Raphaël Marchal)', '19 septembre 2023',
  'https://lcp.fr/actualites/exonerations-de-cotisations-sociales-patronales-un-rapport-parlementaire-preconise-de',
  "Selon le rapport de Marc Ferracci (Renaissance) et Jérôme Guedj (PS), les allègements de cotisations sous 3,5 SMIC sont passés de 1,1 point de PIB en 2004 à 2,8 points en 2022, soit « près de 80 milliards d'euros ». Marc Ferracci écrit : « Alléger le coût du travail sur les plus hauts salaires ne permet pas de soutenir efficacement l'emploi ».",
  'Chaîne parlementaire ; rapport transpartisan.', 'media'))

FICHES.append(fiche(
 id='trou-secu-intenable', affirmation="Le trou de la Sécu prouve que notre modèle social est intenable.", volet='economie', sous_theme='Déficit public',
 mots_cles=['trou de la secu', 'trou de la securite sociale', 'deficit de la secu', 'deficit de la securite sociale', 'secu en faillite', 'modele social intenable', 'securite sociale intenable'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le déficit de la Sécurité sociale est réel et s'aggrave : 21,6 Md€ en 2025, 21,8 Md€ attendus en 2026, et la Cour des comptes juge la situation « hautement périlleuse ». Mais il représente environ 3 % de dépenses proches de 700 Md€, la branche famille est excédentaire, et le déficit dépend autant des recettes (désinflation, ralentissement, allègements de cotisations) que des dépenses. Un déficit appelle des choix de financement ; il ne prouve pas que le modèle est condamné.",
 contexte="Le « trou de la Sécu » sert souvent d'argument pour réduire la protection sociale ou en privatiser une partie.",
 explication="Pour juger, il faut rapporter le déficit aux dépenses totales, regarder quelles branches sont en déficit et pourquoi, et distinguer un problème de financement d'une faillite du système.",
 sources=[SANTEMENTALE_COUR_2026, ACTEURSPUBLICS_DSS_2026, SENAT_PLFSS_2027, PUBLICSENAT_COUR_SECU_2026, INSEE_APU_2025, LCP_EXONERATIONS_2023],
 faits=[
  fait("Selon la Cour des comptes, le déficit de la Sécurité sociale a doublé en deux ans pour atteindre 21,6 Md€ en 2025 ; les recettes ont progressé de 2,6 % et les dépenses de 3,6 %.", 'santementale_cour_2026', '2025', 'France', "Le déficit est réel et se dégrade : c'est un fait défavorable.", 'etabli', '21,6 Md€'),
  fait("D'après la Direction de la Sécurité sociale, le déficit 2025 vient de la maladie (15,9 Md€) et de la vieillesse (7,2 Md€), tandis que la branche famille est excédentaire (+1,2 Md€).", 'acteurspublics_dss_2026', '2025', 'France', "Le déficit n'est pas uniforme : certaines branches sont à l'équilibre.", 'etabli'),
  fait("Selon le Sénat, le projet de budget 2027 prévoit 696,4 Md€ de dépenses pour 683,7 Md€ de recettes, soit un déficit de 12,7 Md€.", 'senat_plfss_2027', '2027', 'France', "Le déficit représente une petite part des dépenses totales.", 'etabli', '696,4 Md€'),
  fait("La Cour des comptes juge la situation « hautement périlleuse » et estime que la dette de l'Acoss pourrait atteindre 130 Md€ en 2030.", 'publicsenat_cour_secu_2026', '2026', 'France', "La trajectoire n'est pas tenable sans mesures de redressement.", 'etabli'),
  fait("Selon l'Insee, la dette des administrations de sécurité sociale atteint 293,1 Md€ fin 2025, sur une dette publique totale de 3 460,5 Md€.", 'insee_apu_2025', '2025', 'France', "La dette sociale est une fraction minoritaire de la dette publique.", 'etabli', '293,1 Md€'),
  fait("Selon un rapport parlementaire transpartisan, les allègements de cotisations patronales sont passés de 1,1 point de PIB en 2004 à 2,8 points en 2022, près de 80 milliards d'euros.", 'lcp_exonerations_2023', '2004-2022', 'France', "Le financement de la Sécu dépend de choix sur les recettes ; ces allègements sont en grande partie compensés par l'État.", 'etabli', '80 milliards'),
 ],
 court="Le déficit est réel : 21,6 Md€ en 2025, et la Cour des comptes s'inquiète. Mais c'est environ 3 % d'un budget de près de 700 Md€, la branche famille est excédentaire, et les recettes comptent autant que les dépenses. C'est un problème de financement, pas la preuve d'une faillite.",
 moyen="Il ne faut pas minimiser : selon la Cour des comptes, le déficit de la Sécurité sociale a doublé en deux ans et atteint 21,6 Md€ en 2025, et la trajectoire de la dette sociale est jugée « hautement périlleuse ».\n\nMais rapporté au total, le déficit attendu en 2027 est de 12,7 Md€ pour près de 700 Md€ de dépenses. La branche famille est excédentaire ; la maladie et la vieillesse sont en déficit, notamment parce que l'inflation a ralenti et que les recettes progressent moins vite. Pendant ce temps, les allègements de cotisations ont atteint près de 80 milliards par an. La question est donc : qui finance et comment, pas : faut-il abandonner la Sécu.",
 detaille="Les chiffres sont sérieux. Selon la Cour des comptes, le déficit des régimes de base a doublé en deux ans et atteint 21,6 Md€ en 2025 : les recettes ont progressé de 2,6 % et les dépenses de 3,6 %. Le Sénat attend 21,8 Md€ en 2026. La Cour estime que la dette de l'Acoss pourrait atteindre 130 Md€ en 2030 et parle d'une situation « hautement périlleuse ».\n\nMais un déficit se lit en proportion. Le projet de budget 2027 prévoit 696,4 Md€ de dépenses pour 683,7 Md€ de recettes. Selon la Direction de la Sécurité sociale, la branche famille est excédentaire ; la maladie (15,9 Md€) et la vieillesse (7,2 Md€) concentrent le déficit, en partie à cause de la désinflation qui freine les recettes avant les pensions. Selon l'Insee, la dette des administrations de sécurité sociale représente 293 Md€ sur 3 460 Md€ de dette publique.\n\nEnfin, les recettes sont un choix politique. Un rapport transpartisan a relevé que les allègements de cotisations patronales atteignent près de 80 milliards par an, avec une efficacité discutée sur les hauts salaires ; ils sont toutefois en grande partie compensés par l'État. Redresser les comptes peut passer par des économies, mais aussi par des recettes. Le modèle de 1945 a traversé bien d'autres crises.",
 empathie="On a raison de s'inquiéter d'un déficit qui dure : c'est notre santé et nos retraites qui sont en jeu. C'est justement pour cela qu'il faut regarder les causes avant de conclure.",
 legitimes=["Le déficit se creuse et la dette sociale augmente.", "La Cour des comptes demande des mesures de redressement rapides."],
 contre=[
  ("On ne peut plus payer, il faut privatiser.", "Le déficit représente quelques pourcents des dépenses ; il se comble par des économies ciblées ou des recettes, pas forcément en démantelant."),
  ("Les exonérations, c'est compensé par l'État, donc ça ne compte pas.", "C'est en grande partie vrai pour la Sécu ; mais cela pèse alors sur le budget de l'État, et leur efficacité sur l'emploi est discutée."),
 ],
 questions=["Savais-tu que la branche famille de la Sécu est excédentaire ?", "Pour combler le déficit, préfères-tu réduire les remboursements ou revoir certaines exonérations ?"],
 limites=["Le rapport de la Cour des comptes a été lu à travers des comptes rendus de presse (Santé Mentale, Public Sénat).", "La part des allègements non compensés par l'État n'a pas été trouvée dans une source lue.", "Aucune source lue ne chiffre l'effet du vieillissement sur le déficit."],
 publics={'convaincus': "Le déficit est réel, je ne le nie pas : 21,6 milliards en 2025. Mais sur près de 700 milliards de dépenses, c'est environ 3 %, et la branche famille est même excédentaire. Un ménage qui a un découvert ne vend pas sa maison : il regarde ses recettes et ses dépenses.",
  'indecis': "Il est normal de s'inquiéter : la Cour des comptes elle-même juge la situation périlleuse. Mais le déficit dépend aussi des recettes, freinées par le ralentissement et par les allègements de cotisations. Il y a plusieurs façons de le réduire sans renoncer à la protection de tous."},
 a_actualiser='2027-06-30', raison="Nouveau rapport de la Cour des comptes sur la Sécurité sociale.",
))

# 3 ── Dette publique et dépenses sociales ─────────────────────────────────
SENAT_MOSCOVICI_2022 = ('senat_moscovici_2022', src('Débat sur le rapport public annuel de la Cour des comptes (compte rendu analytique)', 'Sénat (intervention de Pierre Moscovici, premier président de la Cour des comptes)', '24 février 2022',
  'https://www.senat.fr/cra/s20220224/s20220224_1.html',
  "La dette atteint « 113 points de PIB, elle dépasse de 16 points son niveau de 2019 ». La hausse des recettes a été freinée par « d'importantes baisses d'impôts en 2021 et 2022 » ; les prélèvements obligatoires passent de 44,5 % du PIB en 2020 à 43,4 % en 2022.",
  'Parole officielle du premier président de la Cour des comptes ; donnée datée (2022).', 'primaire'))
LOCALTIS_COUR_2024 = ('localtis_cour_2024', src('Finances publiques : les sévères mises en garde de la Cour des comptes', 'Localtis / Banque des Territoires (Claire Mallet, avec l’AFP)', '15 juillet 2024',
  'https://www.banquedesterritoires.fr/finances-publiques-les-severes-mises-en-garde-de-la-cour-des-comptes',
  "Les finances publiques ont été « malmenées par les crises sanitaire et inflationniste » ; la dette est « emportée par la réitération des déficits et par son poids ». Des mesures qui « dégradent de façon pérenne le déficit public » coûtent 6,7 Md€ : suppression de la taxe d'habitation (2,5 Md€) et réduction de la CVAE (4,2 Md€). En 2023, les hausses de taux de taxe foncière (+1,8 Md€) sont les principales hausses discrétionnaires de prélèvements ; les dépenses de fonctionnement des collectivités ont dépassé les objectifs d'environ 2 Md€. L'État a respecté ses objectifs de dépense, contrairement aux administrations sociales.",
  "Service d'information des collectivités (Caisse des dépôts), qui rend compte d'un rapport de la Cour des comptes.", 'media'))
SENAT_HUSSON_2024 = ('senat_husson_2024', src('Dégradation des finances publiques : octobre 2023 – septembre 2024 (synthèse)', 'Sénat, commission des finances (rapporteur Jean-François Husson, président Claude Raynal)', '19 novembre 2024',
  'https://conferenceconsensuslogement.senat.fr/rap/r24-153/r24-153-syn.pdf',
  "« Trois quarts de l'écart par rapport à la prévision s'expliquent par des recettes moins élevées que prévu. » Le manque de recettes atteint 41,5 Md€ en 2024 ; l'élasticité fiscale prévue était de 1,1, elle a été de 0,71. Les dépenses locales ont dépassé la prévision de 13,4 Md€.",
  'Rapport sénatorial transpartisan (site miroir du Sénat) ; il porte sur le dérapage 2023-2024.', 'primaire'))
MONTAIGNE_ECALLE_2021 = ('montaigne_ecalle_2021', src('Quinquennat Macron : le grand décryptage (fiscalité)', 'Institut Montaigne (François Ecalle, ancien magistrat de la Cour des comptes)', 'août 2021',
  'https://www.institutmontaigne.org/ressources/pdfs/publications/quinquennat-macron-le-gd-decryptage-fiscalite.pdf',
  "La suppression de la taxe d'habitation a vu son coût « porté à 18 Mds€ par an » ; la baisse de l'impôt sur les sociétés est « évaluée à 11 Mds€ » ; les impôts de production baissent de 10 Md€ par an ; le remplacement de l'ISF par l'IFI coûte « environ 3,8 Mds€ ». La baisse des prélèvements « devait s'accompagner d'économies budgétaires suffisantes pour réduire le déficit public », mais ces économies « n'ont pas été réalisées ».",
  "Auteur reconnu publié par un think tank libéral (orientation à signaler) ; donnée de 2021.", 'etude'))

FICHES.append(fiche(
 id='dette-depenses-sociales', affirmation="La dette publique vient des dépenses sociales excessives.", volet='economie', sous_theme='Dette publique',
 mots_cles=['dette publique depenses sociales', 'dette a cause des depenses sociales', 'dette vient du social', 'dette a cause de l assistanat', 'origine de la dette', 'pourquoi la dette', 'dette due aux aides sociales'],
 verdict='trompeur', fiabilite='etabli',
 resume="La dette publique atteint 3 460 Md€ fin 2025, dont 293 Md€ pour les administrations de sécurité sociale. Elle s'explique par des déficits répétés, les crises (Covid : +16 points de PIB entre 2019 et 2021, inflation) et des baisses d'impôts non compensées par des économies. Les dépenses publiques sont élevées et les administrations sociales ont dépassé leurs objectifs, mais tout attribuer aux « dépenses sociales » est réducteur.",
 contexte="L'argument sert à justifier des coupes dans les prestations sociales comme seul moyen de réduire la dette.",
 explication="La dette résulte de l'écart cumulé entre recettes et dépenses : il faut regarder les deux côtés, et les chocs extérieurs.",
 sources=[INSEE_APU_2025, SENAT_MOSCOVICI_2022, LOCALTIS_COUR_2024, SENAT_HUSSON_2024, MONTAIGNE_ECALLE_2021],
 faits=[
  fait("Selon l'Insee, la dette publique atteint 3 460,5 Md€ fin 2025 (115,7 % du PIB) ; celle des administrations de sécurité sociale est de 293,1 Md€.", 'insee_apu_2025', '2025', 'France', "La dette sociale représente moins d'un dixième de la dette publique.", 'etabli', '3 460,5 Md€'),
  fait("Selon le premier président de la Cour des comptes, la dette dépassait en 2021 de 16 points de PIB son niveau de 2019, et la hausse des recettes a été freinée par d'importantes baisses d'impôts en 2021 et 2022.", 'senat_moscovici_2022', '2019-2022', 'France', "La crise sanitaire et les baisses d'impôts ont pesé lourd.", 'etabli', '16 points de PIB'),
  fait("Selon François Ecalle, la suppression de la taxe d'habitation coûte 18 Md€ par an, la baisse de l'impôt sur les sociétés 11 Md€ et celle des impôts de production 10 Md€, sans que les économies prévues aient été réalisées.", 'montaigne_ecalle_2021', '2017-2021', 'France', "Des baisses d'impôts non financées ont creusé les déficits.", 'estimation'),
  fait("Le Sénat estime que trois quarts du dérapage du déficit en 2024 s'expliquent par des recettes plus faibles que prévu, soit 41,5 Md€ manquants.", 'senat_husson_2024', '2024', 'France', "Le dérapage récent vient surtout des recettes.", 'etabli', '41,5 Md€'),
  fait("D'après la Cour des comptes, l'État a respecté ses objectifs de dépense en 2023, contrairement aux administrations sociales.", 'localtis_cour_2024', '2023', 'France', "Les dépenses sociales ont aussi dérapé : c'est un fait défavorable.", 'etabli'),
  fait("Selon l'Insee, les dépenses publiques représentent 57,3 % du PIB et les charges d'intérêts de la dette 64,7 Md€ en 2025.", 'insee_apu_2025', '2025', 'France', "Les dépenses sont élevées et la charge de la dette augmente.", 'etabli', '57,3 % du PIB'),
 ],
 court="La dette sociale pèse moins de 10 % de la dette publique. La dette vient de déficits répétés, des crises comme le Covid et de baisses d'impôts non financées. Les dépenses comptent aussi, mais accuser seulement le social, c'est oublier la moitié des comptes.",
 moyen="Selon l'Insee, la dette publique atteint 3 460 Md€ fin 2025, dont 293 Md€ pour les administrations de sécurité sociale. La crise du Covid a ajouté 16 points de PIB entre 2019 et 2021, selon la Cour des comptes.\n\nDu côté des recettes, les baisses d'impôts ont pesé : selon François Ecalle, la suppression de la taxe d'habitation coûte 18 Md€ par an, la baisse de l'impôt sur les sociétés 11 Md€, sans les économies promises. En 2024, le Sénat attribue trois quarts du dérapage à des recettes plus faibles que prévu. Les dépenses publiques sont élevées et les administrations sociales ont dépassé leurs objectifs : il faut le dire. Mais la dette est un écart entre recettes et dépenses, pas le seul fait du social.",
 detaille="La dette publique, c'est l'accumulation des déficits. Fin 2025, elle atteint 3 460,5 Md€ selon l'Insee, soit 115,7 % du PIB. La part des administrations de sécurité sociale est de 293 Md€ : l'essentiel de la dette est celle de l'État.\n\nTrois facteurs ressortent des sources lues. D'abord les crises : selon le premier président de la Cour des comptes, la dette a gagné 16 points de PIB entre 2019 et 2021. Ensuite les recettes : la Cour relève d'importantes baisses d'impôts en 2021 et 2022, et François Ecalle chiffre la suppression de la taxe d'habitation à 18 Md€ par an, la baisse de l'impôt sur les sociétés à 11 Md€, celle des impôts de production à 10 Md€, en notant que les économies prévues « n'ont pas été réalisées ». En 2024, le Sénat attribue trois quarts du dérapage du déficit à des recettes plus faibles que prévu.\n\nEnfin les dépenses : elles atteignent 57,3 % du PIB, et la Cour constate qu'en 2023 les administrations sociales n'ont pas tenu leurs objectifs. Les intérêts de la dette (64,7 Md€ en 2025) augmentent vite. Le débat honnête porte donc sur l'équilibre entre recettes et dépenses, pas sur un coupable unique.",
 empathie="La dette inquiète, à juste titre : ses intérêts coûtent de plus en plus cher. Justement, la réduire suppose de regarder toutes ses causes.",
 legitimes=["Les dépenses publiques sont parmi les plus élevées d'Europe.", "Les administrations sociales ont dépassé leurs objectifs de dépense en 2023."],
 contre=[
  ("Les dépenses sociales sont le premier poste du budget.", "C'est vrai qu'elles sont le premier poste, mais la dette vient de l'écart entre recettes et dépenses ; les baisses d'impôts non financées y ont contribué."),
  ("Sans le Covid, il n'y aurait pas de problème.", "Le Covid a beaucoup pesé, mais les déficits existaient avant et ont continué ensuite."),
 ],
 questions=["Savais-tu que la dette de la Sécurité sociale représente moins d'un dixième de la dette publique ?", "Pour réduire la dette, faut-il seulement couper des dépenses ou aussi revenir sur certaines baisses d'impôts ?"],
 limites=["Les montants des baisses d'impôts (Ecalle, 2021) ne s'additionnent pas tels quels et datent de 2021.", "Aucune décomposition officielle de toute la dette par cause n'a été lue ; l'étude de l'OFCE sur les crises n'a pas pu être ouverte.", "Le chiffre de 60 Md€ de recettes perdues avancé par un député LFI n'a pas été retenu, faute de source institutionnelle."],
 publics={'convaincus': "Selon l'Insee, la dette de la Sécu, c'est 293 milliards sur 3 460 : moins d'un dixième. Le Covid a ajouté 16 points de PIB, et les baisses d'impôts depuis 2017 n'ont pas été compensées par des économies, selon un ancien magistrat de la Cour des comptes. Accuser seulement les aides sociales, c'est regarder la moitié des comptes.",
  'indecis': "Il est vrai que la France dépense beaucoup et que les administrations sociales ont dépassé leurs objectifs. Mais la dette vient aussi des crises et de recettes plus faibles, notamment après des baisses d'impôts. Les deux côtés du budget doivent être sur la table."},
 a_actualiser='2027-06-30', raison="Comptes nationaux 2026.",
))

# 4 ── Réforme de l'assurance chômage ──────────────────────────────────────
DARES_EVAL_CHOMAGE_2025 = ('dares_eval_chomage_2025', src("Rapport du comité d'évaluation de la réforme de l'assurance chômage 2019-2021", 'Dares (comité présidé par Rafael Lalive), publié sur Vie publique', 'avril 2025',
  'https://www.vie-publique.fr/files/rapport/pdf/298088.pdf',
  "Le nouveau calcul « réduit en moyenne leur salaire journalier de référence de 25 % et leur allocation journalière de 18 % », surtout pour les jeunes et les contrats courts. Une baisse de 10 % du salaire journalier de référence réduit la durée sans emploi d'environ 1,4 à 5 %. Mais « cette incitation ne s'est pas accompagnée d'effet sur le retour en emploi durable ». Sur le bonus-malus : « Le dispositif n'a en revanche pas eu d'impact mesurable sur l'emploi dans les entreprises affectées. »",
  'Évaluation officielle et indépendante.', 'etude'))
UNEDIC_EVAL_2025 = ('unedic_eval_2025', src("Évaluation de la réforme d'assurance chômage 2019-2021", 'Unédic', '20 mars 2025',
  'https://www.unedic.org/publications/evaluation-de-la-reforme-d-assurance-chomage-2019-2021',
  "Environ 1,5 million d'allocataires ont été touchés. Pour les parcours fragmentés, l'allocation journalière baisse d'environ 16 % et la part qui retrouve un emploi en 6 mois passe de 52 % à 56-58 %, mais « cet effet ne porte que sur l'emploi non durable (contrats de moins de 6 mois) ». Les ouvertures de droits baissent d'environ 15 % entre 2019 et 2023, surtout chez les jeunes et les peu diplômés.",
  "Gestionnaire paritaire du régime d'assurance chômage.", 'primaire'))
WEKA_AFP_CHOMAGE_2025 = ('weka_afp_chomage_2025', src("Assurance chômage : la réforme de 2019 a accéléré le retour à l'emploi et réduit les allocations", 'Weka (dépêche AFP)', '7 avril 2025',
  'https://www.weka.fr/actualite/emploi/article/assurance-chomage-la-reforme-de-2019-a-accelere-le-retour-a-l-emploi-et-reduit-les-allocations-selon-un-rapport-198124/',
  "La durée moyenne de chômage baisse d'environ 12 %. Seule la reprise d'emplois peu durables a été stimulée (intérim, CDD de moins de 6 mois). L'allocation moyenne baisse d'environ 18 %, soit 6 € par jour. L'évaluation n'intègre pas la réforme de 2023, qui a réduit la durée d'indemnisation de 25 %.",
  'Dépêche AFP.', 'media'))
UNEDIC_CONTRACYCLICITE_2025 = ('unedic_contracyclicite_2025', src('Réforme 2023 : premiers effets de la réforme de contracyclicité', 'Unédic (M.-H. Nguyen, M. Salliot)', '18 décembre 2025',
  'https://www.unedic.org/publications/reforme-2023-premiers-effets-de-la-reforme-de-contracyclicite',
  "« La durée potentielle de droit s'établit désormais à 16 mois en moyenne, contre 20 mois en 2022 (soit -20 %) ». Les fins de droit passent de 41 000 à 70 000 entre mars 2023 et mars 2025 ; la part des personnes en fin de droit qui basculent vers l'ASS passe « de 13 % mi-2022 à 20 % mi-2025 ». Les économies sont estimées à « l'ordre de 4,5 Md€ par an ». Aucun résultat n'est encore disponible sur la reprise d'emploi.",
  "Gestionnaire du régime ; étude technique.", 'primaire'))

FICHES.append(fiche(
 id='reforme-assurance-chomage-emploi', affirmation="La réforme de l'assurance chômage remet les gens au travail.", volet='social', sous_theme='Chômage',
 mots_cles=['reforme de l assurance chomage', 'reforme assurance chomage', 'reformes du chomage', 'baisser les allocations chomage', 'durcir l assurance chomage', 'degressivite des allocations', 'reduire la duree d indemnisation'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="L'évaluation officielle de la réforme de 2019-2021 montre un retour à l'emploi un peu plus rapide (durée de chômage en baisse d'environ 12 %), mais uniquement vers des contrats courts : aucun effet sur l'emploi durable. En contrepartie, l'allocation journalière a baissé de 18 % en moyenne et les ouvertures de droits d'environ 15 %. La réforme de 2023 a réduit la durée des droits de 20 mois à 16 mois en moyenne ; ses effets sur l'emploi ne sont pas encore évalués.",
 contexte="Les gouvernements successifs ont durci l'assurance chômage depuis 2019 en promettant d'inciter au retour à l'emploi.",
 explication="Il faut distinguer la vitesse de reprise d'un emploi, la qualité de cet emploi et le coût social pour les chômeurs.",
 sources=[DARES_EVAL_CHOMAGE_2025, UNEDIC_EVAL_2025, WEKA_AFP_CHOMAGE_2025, UNEDIC_CONTRACYCLICITE_2025],
 faits=[
  fait("Selon le comité d'évaluation de la Dares, une baisse de 10 % du salaire journalier de référence réduit la durée sans emploi d'environ 1,4 à 5 %.", 'dares_eval_chomage_2025', '2019-2023', 'France', "L'effet incitatif existe : c'est un fait défavorable à l'argument de gauche.", 'etabli'),
  fait("La même évaluation conclut que cette incitation ne s'est pas accompagnée d'effet sur le retour en emploi durable.", 'dares_eval_chomage_2025', '2019-2023', 'France', "Les chômeurs reprennent plus vite des emplois courts, pas des emplois stables.", 'etabli'),
  fait("Le nouveau calcul a réduit l'allocation journalière de 18 % en moyenne, surtout pour les jeunes et les contrats courts.", 'dares_eval_chomage_2025', '2019-2023', 'France', "La réforme a fait baisser les revenus des chômeurs.", 'etabli', '18 %'),
  fait("Selon l'Unédic, les ouvertures de droits ont baissé d'environ 15 % entre 2019 et 2023, surtout chez les jeunes et les peu diplômés.", 'unedic_eval_2025', '2019-2023', 'France', "Moins de chômeurs sont indemnisés.", 'etabli', '15 %'),
  fait("D'après une dépêche AFP sur l'évaluation, la durée moyenne de chômage a baissé d'environ 12 %, seule la reprise d'emplois peu durables ayant été stimulée.", 'weka_afp_chomage_2025', '2019-2023', 'France', "L'accélération est réelle mais porte sur des contrats courts.", 'etabli', '12 %'),
  fait("Selon l'Unédic, après la réforme de 2023, la durée potentielle des droits est passée de 20 à 16 mois en moyenne et les fins de droit de 41 000 à 70 000 par mois entre mars 2023 et mars 2025.", 'unedic_contracyclicite_2025', '2022-2025', 'France', "Davantage de chômeurs arrivent en fin de droits.", 'etabli', '70 000'),
 ],
 court="En partie : selon l'évaluation officielle, les chômeurs retrouvent un emploi un peu plus vite, mais seulement des contrats courts, sans effet sur l'emploi durable. Et l'allocation a baissé de 18 % en moyenne. Remettre au travail, oui, dans la précarité.",
 moyen="L'évaluation indépendante de la réforme de 2019-2021 montre un effet réel : la durée de chômage a baissé d'environ 12 %. C'est un résultat qu'il faut reconnaître.\n\nMais le même rapport précise que cet effet ne porte que sur des emplois courts, intérim et CDD de moins de six mois, sans effet sur l'emploi durable. En échange, l'allocation journalière a baissé de 18 % en moyenne et les ouvertures de droits d'environ 15 %, surtout pour les jeunes et les moins diplômés. La réforme de 2023 a encore réduit la durée des droits. On pousse plus vite vers des petits contrats ceux qui étaient déjà les plus précaires.",
 detaille="Le comité d'évaluation présidé par Rafael Lalive, pour la Dares, a publié en 2025 la meilleure évaluation disponible. Il trouve qu'une baisse de 10 % du salaire journalier de référence réduit la durée sans emploi d'environ 1,4 à 5 %. Selon l'AFP, la durée moyenne de chômage a baissé d'environ 12 %. L'incitation financière fonctionne donc, au moins à court terme.\n\nMais il précise que « cette incitation ne s'est pas accompagnée d'effet sur le retour en emploi durable ». Selon l'Unédic, pour les parcours fragmentés, la part de reprise d'emploi en six mois passe de 52 % à 56-58 %, seulement sur des contrats de moins de six mois. Le prix : une allocation journalière en baisse de 18 % en moyenne, environ 1,5 million d'allocataires touchés, des ouvertures de droits en baisse d'environ 15 %. Le bonus-malus sur les contrats courts n'a pas eu d'effet mesurable sur l'emploi.\n\nLa réforme de 2023 a réduit la durée potentielle des droits de 20 à 16 mois en moyenne ; les fins de droit sont passées de 41 000 à 70 000 par mois, pour environ 4,5 Md€ d'économies par an. Ses effets sur l'emploi ne sont pas encore évalués. L'affirmation est donc plutôt exacte sur la vitesse, mais elle tait la qualité des emplois et le coût social.",
 empathie="On peut comprendre l'idée qu'une allocation trop longue décourage certains de reprendre un emploi. Les évaluations permettent de voir ce qui marche, et à quel prix.",
 legitimes=["L'évaluation officielle mesure un retour à l'emploi plus rapide.", "La dégressivité accélère la reprise d'emploi pour les hauts revenus concernés."],
 contre=[
  ("Peu importe le contrat, l'essentiel c'est de travailler.", "Un CDD de quelques semaines suivi d'un retour au chômage avec moins de droits ne sort pas les gens de la précarité."),
  ("Le régime était trop généreux.", "Le choix de réduire les droits des plus précaires est politique ; d'autres leviers existent, comme le bonus-malus sur les contrats courts."),
 ],
 questions=["Savais-tu que l'évaluation officielle ne trouve aucun effet sur l'emploi durable ?", "Une reprise plus rapide d'un contrat court, est-ce un vrai retour au travail selon toi ?"],
 limites=["L'évaluation porte sur la réforme 2019-2021 ; celle de 2023 n'est pas encore évaluée sur l'emploi.", "Les effets mesurés dépendent aussi de la conjoncture favorable de 2021-2023."],
 publics={'convaincus': "D'accord, l'évaluation officielle montre que les chômeurs retrouvent un emploi un peu plus vite. Mais elle dit aussi : uniquement des contrats courts, aucun effet sur l'emploi durable, et des allocations en baisse de 18 %. On a surtout appauvri les plus précaires.",
  'indecis': "La réforme a un effet réel sur la vitesse de reprise d'emploi, et il faut le reconnaître. Mais ce sont surtout des contrats de moins de six mois, et les jeunes et les moins diplômés ont perdu des droits. Tout dépend de ce qu'on appelle « remettre au travail »."},
 a_actualiser='2027-06-30', raison="Évaluation de la réforme de 2023.",
))

# 5 ── Taxe foncière ───────────────────────────────────────────────────────
LOCALTIS_BASES_2025 = ('localtis_bases_2025', src('Les bases des impôts locaux seront automatiquement augmentées de 1,7 % en 2025', 'Localtis / Banque des Territoires (Thomas Beurey)', '4 décembre 2024',
  'https://www.banquedesterritoires.fr/les-bases-des-impots-locaux-seront-automatiquement-augmentees-de-17-en-2025',
  "Les valeurs locatives sont revalorisées automatiquement selon l'indice des prix harmonisé : « Ce n'est donc plus, comme antérieurement, le Parlement qui fixe l'évolution. » Revalorisations : +3,4 % en 2022, +7,1 % en 2023, +3,9 % en 2024, environ +1,7 % en 2025.",
  'Média spécialisé des collectivités (Caisse des dépôts).', 'media'))
LOCALTIS_FONCIER_2023 = ('localtis_foncier_2023', src('Taxe foncière : une « envolée » circonscrite à quelques communes', 'Localtis / Banque des Territoires (Thomas Beurey), d’après la DGFiP', '30 août 2023',
  'https://www.banquedesterritoires.fr/taxe-fonciere-une-envolee-circonscrite-quelques-communes',
  "En 2023, 14 % des 34 808 communes ont relevé leur taux, 84,7 % l'ont maintenu et 1,3 % l'ont baissé ; parmi celles qui l'ont relevé, 52,6 % l'ont fait d'un point ou moins. Les hausses sont fortes dans certaines villes : Paris +59 %, Meudon +42 %, Grenoble +31 %. La croissance est « accentuée par la revalorisation, en 2023, de 7,1 % des valeurs locatives ».",
  'Média spécialisé, données de la DGFiP.', 'media'))
LOCALTIS_FONCIER_2024 = ('localtis_foncier_2024', src('Fiscalité locale : en 2024, moins de 17 % des communes ont relevé leur taux de foncier bâti', 'Localtis / Banque des Territoires (Thomas Beurey), d’après la DGFiP et l’OFGL', '11 septembre 2024',
  'https://www.banquedesterritoires.fr/fiscalite-locale-en-2024-moins-de-17-des-communes-ont-releve-leur-taux-de-foncier-bati',
  "En 2024, 5 832 communes sur 34 915 (16,7 %) ont relevé leur taux, couvrant 14,1 % de la population. En 2023, le produit a progressé de 9,8 % : +6,8 % d'effet base et +2,8 % d'effet taux, dont seulement +1,1 % hors Paris (OFGL).",
  'Média spécialisé, données officielles.', 'media'))
MAIREINFO_DGCL_2026 = ('maireinfo_dgcl_2026', src('Taxe foncière : depuis 2018, moins de 2 % des communes ont augmenté leur taux tous les ans', 'Maire-info (Association des maires de France), d’après le bulletin n° 210 de la DGCL', '3 juin 2026',
  'https://www.maire-info.com/fiscalite-locale/taxe-fonciere-depuis-2018-moins-de-2-des-communes-ont-augmente-leur-taux-tous-les-ans-art26-30845',
  "« seulement 1,8 % des communes l'ont augmenté tous les ans ». Depuis 2019, l'effet base dépasse nettement l'effet taux. La suppression de la taxe d'habitation a « globalement entraîné une légère hausse » des taux. Le taux corrigé passe de 19,4 % (2018) à 18,2 % (2021) puis 19,8 % (2025) ; le saut du taux communal en 2021 vient du transfert de la part départementale.",
  "Média de l'association des maires (point de vue des élus locaux) ; données de la DGCL.", 'media'))

FICHES.append(fiche(
 id='taxe-fonciere-maires', affirmation="La taxe foncière explose à cause des maires dépensiers.", volet='economie', sous_theme='Fiscalité',
 mots_cles=['taxe fonciere', 'taxe fonciere explose', 'hausse de la taxe fonciere', 'impots locaux explosent', 'foncier bati', 'maires depensiers'],
 verdict='trompeur', fiabilite='etabli',
 resume="L'essentiel de la hausse récente de la taxe foncière vient de la revalorisation automatique des bases, fixée par la loi selon l'inflation : +7,1 % en 2023, +3,9 % en 2024. Seule une minorité de communes relève son taux chaque année (14 % en 2023, 16,7 % en 2024), et 1,8 % l'ont fait tous les ans depuis 2018. Mais certaines grandes villes, comme Paris ou Grenoble, ont fortement augmenté leur taux.",
 contexte="Chaque automne, l'arrivée de l'avis de taxe foncière relance l'accusation contre les maires.",
 explication="La taxe foncière dépend de deux éléments : la base (valeur locative, revalorisée par l'État) et le taux (voté par la commune). Il faut séparer les deux.",
 sources=[LOCALTIS_BASES_2025, LOCALTIS_FONCIER_2023, LOCALTIS_FONCIER_2024, MAIREINFO_DGCL_2026, LOCALTIS_COUR_2024],
 faits=[
  fait("Les valeurs locatives sont revalorisées automatiquement selon l'inflation : +7,1 % en 2023, +3,9 % en 2024 et environ +1,7 % en 2025.", 'localtis_bases_2025', '2022-2025', 'France', "La hausse des bases ne dépend pas des maires.", 'etabli', '+7,1 %'),
  fait("En 2023, le produit de la taxe foncière a progressé de 9,8 % : +6,8 % liés aux bases et +2,8 % aux taux, dont seulement +1,1 % hors Paris.", 'localtis_foncier_2024', '2023', 'France', "L'effet des bases dépasse largement celui des taux.", 'etabli', '9,8 %'),
  fait("En 2024, 16,7 % des communes ont relevé leur taux, couvrant 14,1 % de la population ; en 2023, c'était 14 %, souvent d'un point ou moins.", 'localtis_foncier_2024', '2023-2024', 'France', "La grande majorité des communes n'augmente pas son taux.", 'etabli', '16,7 %'),
  fait("Selon la DGCL citée par Maire-info, seulement 1,8 % des communes ont augmenté leur taux tous les ans depuis 2018.", 'maireinfo_dgcl_2026', '2018-2025', 'France', "Les hausses répétées sont rares.", 'etabli', '1,8 %'),
  fait("En 2023, certaines grandes villes ont fortement relevé leur taux : Paris +59 %, Meudon +42 %, Grenoble +31 %.", 'localtis_foncier_2023', '2023', 'France', "Des hausses fortes existent dans quelques villes, dont des villes de gauche : c'est un fait défavorable.", 'etabli'),
  fait("Selon la Cour des comptes, les hausses de taux de taxe foncière (+1,8 Md€) ont été en 2023 les principales hausses discrétionnaires de prélèvements, et les dépenses de fonctionnement des collectivités ont dépassé les objectifs d'environ 2 Md€.", 'localtis_cour_2024', '2023', 'France', "Les collectivités ont aussi leur part de responsabilité.", 'etabli', '1,8 Md€'),
 ],
 court="Surtout faux : la hausse vient d'abord de la revalorisation automatique des bases, indexée sur l'inflation par la loi (+7,1 % en 2023). Seule une commune sur six a relevé son taux en 2024. Certaines grandes villes, comme Paris, l'ont fortement augmenté, c'est vrai.",
 moyen="La taxe foncière, c'est une base multipliée par un taux. La base est revalorisée automatiquement selon l'inflation, sans vote des maires : +7,1 % en 2023, +3,9 % en 2024. En 2023, sur 9,8 % de hausse du produit, 6,8 points venaient des bases.\n\nCôté taux, seules 14 % des communes l'ont relevé en 2023 et 16,7 % en 2024, souvent d'un point ou moins ; 1,8 % l'ont fait tous les ans depuis 2018. Il y a des exceptions fortes, comme Paris (+59 %) ou Grenoble (+31 %) en 2023, et la Cour des comptes reproche aux collectivités d'avoir dépassé leurs objectifs de dépense. Mais la majorité des maires n'y est pour rien : c'est l'inflation et la loi.",
 detaille="Le montant de la taxe foncière dépend de deux choses. La valeur locative cadastrale, d'abord, est revalorisée chaque année selon l'indice des prix : ce n'est plus le Parlement qui fixe la hausse, c'est une règle automatique. Avec l'inflation, elle a fait +3,4 % en 2022, +7,1 % en 2023 et +3,9 % en 2024. Le taux, ensuite, est voté par la commune.\n\nLes données de la DGFiP et de l'OFGL montrent que l'effet base domine. En 2023, le produit de la taxe a augmenté de 9,8 % : 6,8 points dus aux bases, 2,8 points aux taux, dont 1,1 point seulement hors Paris. Cette année-là, 84,7 % des communes ont maintenu leur taux ; en 2024, 16,7 % l'ont relevé. Depuis 2018, seulement 1,8 % l'ont augmenté tous les ans. La suppression de la taxe d'habitation, décidée par l'État, a aussi poussé légèrement les taux à la hausse en privant les communes d'une ressource.\n\nCela n'exonère pas tout le monde. Paris (+59 %), Meudon (+42 %) ou Grenoble (+31 %) ont fortement relevé leur taux en 2023, et la Cour des comptes relève que les hausses de taux ont rapporté 1,8 Md€ cette année-là. Le débat sur la gestion d'une ville se mène ville par ville, pas en accusant tous les maires.",
 empathie="Recevoir un avis de taxe foncière en forte hausse est un vrai choc pour beaucoup de propriétaires modestes, notamment les retraités. Savoir d'où vient la hausse permet de demander des comptes à la bonne personne.",
 legitimes=["Certaines grandes villes ont fortement relevé leur taux.", "Les collectivités ont dépassé leurs objectifs de dépense en 2023 selon la Cour des comptes."],
 contre=[
  ("Mon maire a augmenté le taux, je l'ai vu sur mon avis.", "C'est possible : une commune sur six l'a fait en 2024. L'avis de taxe foncière montre séparément l'évolution de la base et celle du taux."),
  ("Les maires compensent la suppression de la taxe d'habitation.", "C'est en partie vrai : cette suppression décidée par l'État a légèrement poussé les taux à la hausse."),
 ],
 questions=["As-tu regardé sur ton avis si c'est la base ou le taux qui a augmenté ?", "Savais-tu que la revalorisation des bases est automatique et fixée par la loi ?"],
 limites=["Les données sur les taux portent sur 2023-2025 ; la situation varie fortement d'une commune à l'autre.", "Maire-info est le média de l'association des maires ; ses chiffres viennent de la DGCL."],
 publics={'convaincus': "Regarde ton avis : la base a pris 7,1 % en 2023, automatiquement, à cause de l'inflation et d'une règle fixée par la loi. Plus de huit communes sur dix n'ont pas touché à leur taux cette année-là. Si ton maire l'a augmenté, demande-lui des comptes ; mais ne mets pas tous les maires dans le même sac.",
  'indecis': "La hausse de la taxe foncière pèse lourd sur les budgets, surtout des retraités. Elle vient d'abord de la revalorisation automatique liée à l'inflation, et seule une minorité de communes relève son taux. Quelques grandes villes l'ont fortement augmenté : c'est à juger au cas par cas."},
 a_actualiser='2027-09-30', raison="Données DGFiP sur les taux votés en 2027.",
))

# ══ Lot B : immigration et comparaisons ═════════════════════════════════════

# 6 ── Remigration ─────────────────────────────────────────────────────────
PUBLICSENAT_ZEMMOUR_2022 = ('publicsenat_zemmour_2022', src('Présidentielle 2022 : Éric Zemmour détaille son programme et assume le terme « remigration »', 'Public Sénat', '23 mars 2022 (mis à jour le 4 avril 2022)',
  'https://www.publicsenat.fr/actualites/non-classe/presidentielle-2022-eric-zemmour-detaille-son-programme-et-assume-le-terme',
  "Éric Zemmour annonce « un grand ministère de la remigration » et défend le mot. Son programme prévoit de limiter l'asile « à une centaine d'individus » par an, de supprimer le regroupement familial, protégé par la Charte des droits fondamentaux de l'UE, et de réviser la Constitution pour faire primer les lois françaises sur les textes internationaux et européens.",
  'Média parlementaire public ; programme décrit avec attribution.', 'media'))
EUROPE1_ZEMMOUR_2022 = ('europe1_zemmour_2022', src('Présidentielle : Éric Zemmour veut créer un ministère de la « rémigration »', 'Europe 1', '23 mars 2022',
  'https://www.europe1.fr/politique/presidnetielle-eric-zemmour-veut-creer-un-ministere-de-la-remigration-4101123',
  "Le candidat définit le terme : « Rémigration, ça veut dire, retour des immigrés qui ne sont pas acceptés en France ». Il vise « les clandestins, puis les délinquants, les criminels, puis les fichés S étrangers » et déclare : « On peut imaginer 100 000 renvois par an ».",
  "Média de droite (groupe Bolloré) ; utilisé seulement pour des citations attribuées du candidat.", 'media'))
BERLINER_UNWORT_2024 = ('berliner_unwort_2024', src('Remigration ist das Unwort des Jahres 2023', 'Berliner Zeitung (dépêche dpa)', '15 janvier 2024',
  'https://www.berliner-zeitung.de/article/remigration-ist-das-unwort-des-jahres-2023-2176862',
  "Le jury de l'« Unwort des Jahres » qualifie le terme d'euphémisme de camouflage (« beschönigende Tarnvokabel »). Le mouvement identitaire réinterprète le mot depuis 2016. Martin Sellner a confirmé en avoir parlé à la réunion de Potsdam (novembre 2023), en présence de responsables de l'AfD et de membres de la CDU. Selon un juré, le terme vise aussi des personnes « selbst dann, wenn sie deutsche Staatsbürger sind » (même si elles sont citoyennes allemandes).",
  "Dépêche d'agence (dpa).", 'media'))
CC_DECHEANCE_2015 = ('cc_decheance_2015', src('Commentaire de la décision n° 2014-439 QPC du 23 janvier 2015', 'Conseil constitutionnel', '2015',
  'https://oos.cloudgouv-eu-west-1.outscale.com/ccqpc-drupal-prd/dqpc/commentaire/commentaire_D%C3%A9cision-n%C2%B0-2014-439-QPC-du-23-janvier-2015.pdf',
  "Seules les personnes qui ont « acquis la qualité de Français » peuvent être déchues de la nationalité (article 25 du code civil) ; les Français de naissance ne le peuvent pas. Depuis 1998, la déchéance est exclue si elle « a pour conséquence de rendre l'individu apatride ». Les motifs sont limitativement énumérés (atteinte aux intérêts fondamentaux de la Nation, terrorisme…), et le Conseil n'admet la sanction que parce qu'elle « n'est pas manifestement disproportionnée ».",
  'Juridiction constitutionnelle.', 'primaire'))
COE_EXPULSIONS_COLLECTIVES = ('coe_expulsions_collectives', src('Prohibition of collective expulsions: landmark judgment (Hirsi Jamaa et autres c. Italie)', "Conseil de l'Europe", 'arrêt du 23 février 2012',
  'https://coe.int/en/web/human-rights-convention/prohibition-of-collective-expulsions',
  "L'article 4 du Protocole n° 4 à la Convention européenne des droits de l'homme interdit les expulsions collectives. La Cour a condamné l'Italie pour un renvoi de migrants vers la Libye effectué « without any examination of each individual situation ».",
  "Institution européenne ; jurisprudence de la Cour européenne des droits de l'homme.", 'primaire'))
SENAT_PLF2026_IMMIGRATION = ('senat_plf2026_immigration', src("L'essentiel sur le projet de loi de finances pour 2026 – mission Immigration, asile et intégration", 'Sénat, commission des lois (avis)', '5 décembre 2025',
  'https://www.senat.fr/rap/a25-145-2/a25-145-2-syn.pdf',
  "« 12 856 retours forcés ont été exécutés en 2024, contre 18 906 en 2019 ». Le taux d'exécution des OQTF « s'élève ainsi à 10,9 % sur les neuf premiers mois de l'année 2025 ». La coopération consulaire de l'Algérie (laissez-passer) est arrêtée depuis mars 2025 ; les Algériens représentent 40 % des retenus en centre de rétention en métropole.",
  'Rapport parlementaire.', 'primaire'))
AFP_ELOIGNEMENTS_2025 = ('afp_eloignements_2025', src('Immigration : plus de titres de séjour et moins de régularisations en France en 2025', 'AFP (repris par lepetitjournal.com)', '27 janvier 2026',
  'https://lepetitjournal.com/fil-afp/immigration-plus-de-titres-de-sejour-et-moins-de-regularisations-en-france-en-2025-433266',
  "D'après les chiffres du ministère de l'Intérieur, « Les éloignements ont eux augmenté de 15,7 % avec 24.985 étrangers renvoyés. » « Les seuls éloignements forcés ont eux progressé de 21 % à 15.569. »",
  'Dépêche AFP.', 'media'))
INSEE_ETRANGERS_2024 = ('insee_etrangers_2024', src("En 2024, 6,0 millions d'étrangers vivent en France, 0,9 million y sont nés (Insee Première n° 2076)", 'Insee', '7 octobre 2025',
  'https://www.insee.fr/fr/statistiques/8651304',
  "La France compte 6,0 millions d'étrangers en 2024, soit « 8,8 % de la population », et 7,7 millions d'immigrés, soit 11,3 %. Estimations provisoires.",
  'Statistique publique.', 'primaire'))

FICHES.append(fiche(
 id='remigration-realisable', affirmation="La remigration proposée par l'extrême droite est réalisable.", volet='politique', sous_theme='Droite et extrême droite',
 mots_cles=['remigration', 'remigrer', 'ministere de la remigration', 'reunion de potsdam', 'renvoyer des millions', 'expulsions massives', 'sellner'],
 verdict='trompeur', fiabilite='etabli',
 resume="« Remigration » recouvre des projets différents : chez Éric Zemmour, 100 000 renvois par an d'étrangers en situation irrégulière, délinquants ou fichés S ; chez Martin Sellner et à la réunion de Potsdam, le départ de personnes jusqu'aux citoyens. La version maximaliste se heurte à la Constitution (pas de déchéance pour les Français de naissance ni d'apatridie) et à l'interdiction des expulsions collectives par la CEDH. Même la version limitée suppose de quadrupler les éloignements forcés actuels (15 569 en 2025), alors que la coopération des pays d'origine bloque.",
 contexte="Le mot a été assumé par Reconquête en 2022 et désigné « non-mot de l'année » en Allemagne en 2024 après la révélation de la réunion de Potsdam.",
 explication="Il faut d'abord demander ce que recouvre le mot, puis confronter chaque version au droit et aux chiffres réels des éloignements.",
 sources=[PUBLICSENAT_ZEMMOUR_2022, EUROPE1_ZEMMOUR_2022, BERLINER_UNWORT_2024, CC_DECHEANCE_2015, COE_EXPULSIONS_COLLECTIVES, SENAT_PLF2026_IMMIGRATION, AFP_ELOIGNEMENTS_2025, INSEE_ETRANGERS_2024],
 faits=[
  fait("Selon Europe 1, Éric Zemmour a défini la remigration comme le « retour des immigrés qui ne sont pas acceptés en France » et déclaré : « On peut imaginer 100 000 renvois par an ».", 'europe1_zemmour_2022', '2022', 'France', "C'est la version française affichée du projet.", 'etabli', '100 000 renvois'),
  fait("En Allemagne, le terme a été désigné « non-mot de l'année » en 2024 ; Martin Sellner a confirmé en avoir parlé à la réunion de Potsdam, et un juré souligne qu'il vise aussi des citoyens allemands, selon la dpa.", 'berliner_unwort_2024', '2023-2024', 'Allemagne', "Dans sa version identitaire, le projet vise aussi des citoyens.", 'etabli'),
  fait("Selon le Conseil constitutionnel, seuls les Français par acquisition peuvent être déchus de leur nationalité, jamais s'ils deviennent apatrides, et pour des motifs limitativement énumérés.", 'cc_decheance_2015', '2015', 'France', "On ne peut pas retirer la nationalité aux Français de naissance.", 'etabli'),
  fait("La Convention européenne des droits de l'homme interdit les expulsions collectives : la Cour a condamné l'Italie en 2012 pour un renvoi sans examen individuel.", 'coe_expulsions_collectives', '2012', 'Europe', "Chaque éloignement doit être examiné individuellement.", 'etabli'),
  fait("D'après les chiffres du ministère de l'Intérieur rapportés par l'AFP, 15 569 éloignements forcés ont été réalisés en 2025 (+21 %), et 24 985 éloignements au total.", 'afp_eloignements_2025', '2025', 'France', "Les éloignements augmentent, mais restent loin de 100 000 par an.", 'etabli', '15 569'),
  fait("Selon le Sénat, le taux d'exécution des OQTF est de 10,9 % sur les neuf premiers mois de 2025, et l'Algérie ne délivre plus de laissez-passer consulaires depuis mars 2025.", 'senat_plf2026_immigration', '2025', 'France', "Sans accord des pays d'origine, les renvois sont impossibles.", 'etabli', '10,9 %'),
 ],
 court="Ça dépend de ce qu'on appelle remigration. Renvoyer des Français ou expulser en masse, c'est interdit par la Constitution et la CEDH. Et même la version « limitée » de Zemmour, 100 000 renvois par an, supposerait de multiplier par six les éloignements forcés actuels, alors que les pays d'origine refusent souvent de reprendre leurs ressortissants.",
 moyen="Le mot recouvre deux projets. Éric Zemmour parle de 100 000 renvois par an d'étrangers sans papiers, délinquants ou fichés S. Dans la version de Martin Sellner, discutée à Potsdam en 2023, il s'agit aussi de pousser au départ des citoyens.\n\nLa seconde version est contraire au droit : on ne peut pas déchoir de sa nationalité un Français de naissance, ni rendre quelqu'un apatride, et la CEDH interdit les expulsions collectives. La première se heurte à la réalité : 15 569 éloignements forcés en 2025, un taux d'exécution des OQTF de 10,9 %, et des pays comme l'Algérie qui ne délivrent plus de laissez-passer. Expulser davantage les étrangers dangereux est un débat légitime ; promettre le départ de millions de personnes, c'est vendre l'impossible et désigner des boucs émissaires.",
 detaille="Première question : de quoi parle-t-on ? En 2022, Éric Zemmour a annoncé un « ministère de la remigration » et défini le mot comme le « retour des immigrés qui ne sont pas acceptés en France », en visant les clandestins, les délinquants et les fichés S étrangers, avec « 100 000 renvois par an ». Dans la mouvance identitaire européenne, le terme va plus loin : à la réunion de Potsdam en novembre 2023, Martin Sellner l'a présenté, et selon un juré allemand il vise aussi des citoyens. Le terme a été désigné « non-mot de l'année » en Allemagne.\n\nDeuxième question : est-ce légal ? Selon le Conseil constitutionnel, seuls les Français par acquisition peuvent être déchus de leur nationalité, pour des faits d'une gravité particulière, et jamais si cela les rend apatrides. La Convention européenne des droits de l'homme interdit les expulsions collectives : chaque situation doit être examinée. Le programme de 2022 prévoyait d'ailleurs de réviser la Constitution pour écarter les traités, ce qui revient à sortir du cadre européen.\n\nTroisième question : est-ce faisable ? En 2025, 15 569 éloignements forcés ont été réalisés, en hausse de 21 %. Le taux d'exécution des OQTF est de 10,9 % et l'Algérie, dont les ressortissants forment 40 % des retenus, ne délivre plus de laissez-passer depuis mars 2025. Renforcer l'exécution des expulsions légales est un débat sérieux. Promettre le départ de millions de personnes, parmi les 7,7 millions d'immigrés dont beaucoup sont français, c'est autre chose : une promesse qui désigne une partie de la population comme indésirable.",
 empathie="Beaucoup de gens qui entendent ce mot pensent surtout aux étrangers condamnés qu'on n'arrive pas à expulser, et cette frustration est compréhensible. Il faut justement distinguer ce problème réel d'un projet qui vise bien plus large.",
 legitimes=["Le taux d'exécution des OQTF est faible.", "Certains pays d'origine refusent de reprendre leurs ressortissants."],
 contre=[
  ("On changera la Constitution.", "Le droit européen et la Convention européenne des droits de l'homme resteraient ; s'en affranchir, c'est quitter le cadre européen et renoncer à des garanties qui protègent tout le monde."),
  ("Zemmour ne parle que des délinquants et des clandestins.", "Même cette version supposerait de multiplier par six les éloignements forcés actuels, sans résoudre le refus des pays d'origine ; et le mot vient d'un courant qui vise aussi des citoyens."),
 ],
 questions=["Quand tu entends « remigration », penses-tu aux étrangers condamnés ou à des Français d'origine étrangère ?", "Comment renvoyer quelqu'un si son pays refuse de le reprendre ?"],
 limites=["La définition varie selon les auteurs ; aucun programme chiffré complet de « remigration » n'a été lu.", "Les chiffres d'éloignement 2025 sont ceux du ministère de l'Intérieur rapportés par l'AFP.", "La page du ministère de l'Intérieur sur la lutte contre l'immigration irrégulière n'a pas pu être ouverte."],
 publics={'convaincus': "Zemmour promettait 100 000 renvois par an ; en 2025, il y a eu 15 569 éloignements forcés, et l'Algérie refuse de reprendre ses ressortissants. Quant à renvoyer des Français, la Constitution l'interdit : on ne peut pas déchoir un Français de naissance. Expulser les criminels étrangers, discutons-en ; la remigration, c'est une promesse impossible qui vise des gens pour leur origine.",
  'indecis': "On peut vouloir que les étrangers condamnés soient effectivement expulsés : c'est un vrai problème, le taux d'exécution des OQTF est faible. Mais le mot « remigration » vient d'un courant qui vise aussi des citoyens, et il se heurte à la Constitution et à la Convention européenne des droits de l'homme. Mieux vaut juger les propositions précises que les slogans."},
 a_actualiser='2027-06-30', raison="Chiffres annuels des éloignements.",
))

# 7 ── Allemagne : réfugiés de 2015 ────────────────────────────────────────
IAB_2025_10ANS = ('iab_2025_10ans', src('10 Jahre Fluchtmigration 2015: Haben wir es geschafft? Eine Analyse aus Sicht des Arbeitsmarktes (Kurzbericht 17/2025)', "IAB, institut de recherche de l'Agence fédérale allemande pour l'emploi (H. Brücker, P. Jaschke, Y. Kosyakova)", '25 août 2025',
  'https://doku.iab.de/kurzber/2025/kb2025-17.pdf',
  "La cohorte de réfugiés arrivés en 2015 atteint un taux d'emploi de 64 % neuf ans après l'arrivée, en 2024, contre 70 % pour l'ensemble de la population : « 76 Prozent bei den Männern und 35 Prozent bei den Frauen » (population générale : hommes 72 %, femmes 69 %). Le salaire médian à temps plein atteint « 70 Prozent des mittleren Verdienstniveaus aller Vollzeitbeschäftigten », juste au-dessus du seuil de bas salaire (66 %). En 2023, 45 % des hommes et 54 % des femmes occupent des postes d'aide.",
  "Institut de recherche public de référence sur le sujet.", 'etude'))
IAB_2024_INTEGRATION = ('iab_2024_integration', src('Arbeitsmarktintegration von Geflüchteten: Verbesserte institutionelle Rahmenbedingungen fördern die Erwerbstätigkeit (Kurzbericht 10/2024)', "IAB, institut de recherche de l'Agence fédérale allemande pour l'emploi (Brücker, Ehab, Jaschke, Kosyakova)", '18 avril 2024',
  'https://interkulturellewoche.de/system/files/aktuelles/IAB-Kurzbericht_2024-10.pdf',
  "« Für die 2015 zugezogene Kohorte lag die Erwerbstätigenquote im Jahr 2022 bei 64 Prozent » (femmes 31 %, hommes 75 %). 76 % des salariés de la cohorte travaillent à temps plein. Environ la moitié avaient terminé le cours d'intégration après 3 à 4 ans, et « nach sieben und mehr Jahren […] knapp drei Viertel » ; seul « etwa ein Fünftel » atteignait le cours de langue professionnelle avancé.",
  "Institut de recherche public (copie du PDF officiel hébergée par une association).", 'etude'))
ZDF_REFUGIES_2025 = ('zdf_refugies_2025', src('Geflüchtete auf dem Arbeitsmarkt: Haben wir es geschafft?', 'ZDFheute (Alina Reissenberger)', '25 août 2025',
  'https://www.zdfheute.de/politik/gefluechtete-migration-arbeitsmarkt-jobs-deutschland-100.html',
  "64 % des réfugiés arrivés en 2015 ont un emploi. La chercheuse Yuliya Kosyakova (IAB) estime : « Wir haben vieles geschafft. » Elle souligne que beaucoup travaillent dans des métiers en pénurie mais mal payés. 34 % des foyers de réfugiés arrivés en 2015 perçoivent encore le Bürgergeld (minimum social).",
  'Télévision publique allemande.', 'media'))
BUNDESREGIERUNG_2023 = ('bundesregierung_2023', src('Geflüchtete erfolgreich integriert – Mehr als die Hälfte erwerbstätig', 'Gouvernement fédéral allemand (archive)', '28 juillet 2023',
  'https://www.bundesregierung.de/breg-de/aktuelles/arbeitsmarktintegration-2204402',
  "« Mehr als die Hälfte der 2015 nach Deutschland Geflüchteten war 2021 erwerbstätig ». Six ans après l'arrivée, 67 % des hommes et 23 % des femmes étaient en emploi. Le texte conclut : « Frauen brauchen mehr Unterstützung. »",
  'Communication gouvernementale (visée valorisante) ; données 2021.', 'primaire'))

FICHES.append(fiche(
 id='allemagne-refugies-2015', affirmation="L'Allemagne a raté l'intégration du million de réfugiés de 2015.", volet='immigration', sous_theme='Comparaisons européennes',
 mots_cles=['refugies de 2015', 'allemagne refugies', 'merkel refugies', 'million de refugies', 'wir schaffen das', 'allemagne a rate l integration', 'migrants en allemagne'],
 verdict='contredit', fiabilite='etabli',
 resume="Selon l'institut de recherche de l'Agence fédérale allemande pour l'emploi (IAB), 64 % des réfugiés arrivés en 2015 avaient un emploi en 2024, contre 70 % pour l'ensemble de la population ; les hommes (76 %) dépassent même la moyenne masculine. Les échecs sont réels : 35 % seulement des femmes en emploi, des salaires bas (70 % du salaire médian), un tiers des foyers encore aux minima sociaux.",
 contexte="L'accueil décidé par Angela Merkel en 2015 (« Wir schaffen das ») est souvent présenté comme un fiasco qui aurait déstabilisé l'Allemagne.",
 explication="Dix ans après, les données du marché du travail permettent un bilan chiffré, avec ses réussites et ses limites.",
 sources=[IAB_2025_10ANS, IAB_2024_INTEGRATION, ZDF_REFUGIES_2025, BUNDESREGIERUNG_2023],
 faits=[
  fait("Selon l'IAB, 64 % des réfugiés arrivés en 2015 avaient un emploi en 2024, contre 70 % pour l'ensemble de la population allemande.", 'iab_2025_10ans', '2024', 'Allemagne', "L'insertion professionnelle est proche de la moyenne nationale.", 'etabli', '64 %'),
  fait("Selon l'IAB, 76 % des hommes de cette cohorte sont en emploi, plus que la moyenne masculine (72 %), mais seulement 35 % des femmes, contre 69 % en population générale.", 'iab_2025_10ans', '2024', 'Allemagne', "Réussite pour les hommes, échec relatif pour les femmes.", 'etabli', '35 %'),
  fait("Selon l'IAB, leur salaire médian à temps plein atteint 70 % du salaire médian, juste au-dessus du seuil de bas salaire (66 %).", 'iab_2025_10ans', '2024', 'Allemagne', "Beaucoup occupent des emplois mal payés.", 'etabli', '70 %'),
  fait("Selon l'IAB, 76 % des salariés de la cohorte travaillent à temps plein ; près des trois quarts ont achevé le cours d'intégration après sept ans, mais seulement un cinquième le cours de langue professionnelle avancé.", 'iab_2024_integration', '2022', 'Allemagne', "La langue progresse, mais le niveau professionnel reste un frein.", 'etabli'),
  fait("D'après la ZDF, 34 % des foyers de réfugiés arrivés en 2015 perçoivent encore le minimum social.", 'zdf_refugies_2025', '2025', 'Allemagne', "Une partie dépend encore des aides : c'est un fait défavorable.", 'etabli', '34 %'),
  fait("Selon le gouvernement fédéral, en 2021, six ans après l'arrivée, 67 % des hommes et 23 % des femmes étaient en emploi.", 'bundesregierung_2023', '2021', 'Allemagne', "L'emploi a continué de progresser entre 2021 et 2024.", 'etabli'),
 ],
 court="Faux pour l'essentiel : selon l'institut public allemand IAB, 64 % des réfugiés de 2015 ont un emploi, contre 70 % pour l'ensemble des Allemands, et les hommes dépassent la moyenne. Les vrais échecs : l'emploi des femmes et les bas salaires.",
 moyen="Dix ans après, l'institut de recherche de l'Agence fédérale allemande pour l'emploi a fait le bilan : 64 % des réfugiés arrivés en 2015 ont un emploi, contre 70 % pour l'ensemble de la population. Les hommes, à 76 %, dépassent la moyenne masculine. Les trois quarts travaillent à temps plein.\n\nLes échecs existent : seulement 35 % des femmes ont un emploi, le salaire médian reste à 70 % de la moyenne, et un tiers des foyers touche encore le minimum social. C'est un bilan contrasté, mais l'image d'un fiasco total est fausse : une grande partie de ces réfugiés travaille et paie des cotisations, souvent dans des métiers en pénurie.",
 detaille="Le bilan le plus solide vient de l'IAB, l'institut de recherche de l'Agence fédérale allemande pour l'emploi, qui suit cette cohorte depuis l'arrivée. En 2024, neuf ans après, 64 % des réfugiés arrivés en 2015 ont un emploi, contre 70 % pour l'ensemble de la population. Les hommes atteignent 76 %, au-dessus de la moyenne masculine (72 %). En 2022, 76 % des salariés de la cohorte travaillaient à temps plein. La chercheuse Yuliya Kosyakova résume : « Wir haben vieles geschafft » (nous avons réussi beaucoup de choses).\n\nLes limites sont nettes. Seulement 35 % des femmes ont un emploi, contre 69 % en population générale ; le gouvernement lui-même reconnaissait en 2023 qu'elles avaient besoin de plus de soutien. Le salaire médian à temps plein atteint 70 % de la médiane, juste au-dessus du seuil de bas salaire, et près de la moitié des hommes occupent des postes d'aide. Selon la ZDF, 34 % des foyers touchent encore le minimum social. Le niveau de langue professionnelle reste un frein : un cinquième seulement atteint le cours avancé.\n\nConclusion : l'intégration par le travail a largement fonctionné pour les hommes, beaucoup moins pour les femmes, et elle s'est faite par le bas de l'échelle des salaires. Ce sont des leçons utiles : cours de langue, garde d'enfants, reconnaissance des diplômes. Le mot « raté » ne résiste pas aux chiffres.",
 empathie="L'arrivée d'un million de personnes en peu de temps a été un choc, et il est légitime de se demander si cela a fonctionné. Les chiffres allemands permettent d'y répondre précisément.",
 legitimes=["L'emploi des femmes réfugiées reste très faible.", "Un tiers des foyers perçoit encore le minimum social."],
 contre=[
  ("Ils travaillent tous dans des petits boulots.", "Beaucoup occupent des emplois peu qualifiés et mal payés, c'est vrai ; mais les trois quarts travaillent à temps plein, souvent dans des métiers en pénurie."),
  ("Et la délinquance ?", "Cette fiche porte sur l'emploi et l'intégration économique ; la délinquance est un autre sujet, à examiner avec des données dédiées."),
 ],
 questions=["Savais-tu que les hommes réfugiés arrivés en 2015 ont un taux d'emploi supérieur à la moyenne masculine allemande ?", "Qu'est-ce qui aiderait les femmes réfugiées à trouver un emploi selon toi ?"],
 limites=["Les données portent sur l'emploi, pas sur l'ensemble de l'intégration (délinquance, logement, opinions).", "Le rapport de l'IAB de 2024 a été lu sur une copie du PDF hébergée par une association.", "La page du gouvernement fédéral est une communication à visée valorisante, avec des données 2021."],
 publics={'convaincus': "Selon l'institut public allemand de l'emploi, 64 % des réfugiés de 2015 travaillent, contre 70 % de l'ensemble des Allemands ; les hommes font même mieux que la moyenne. Il y a des échecs, surtout pour les femmes et les salaires. Mais « raté », les chiffres disent le contraire.",
  'indecis': "L'Allemagne a pris un vrai risque en 2015, et le bilan est contrasté : beaucoup d'hommes travaillent à temps plein, mais les femmes restent très peu en emploi et les salaires sont bas. Ce sont des leçons utiles sur la langue, la garde d'enfants et la reconnaissance des diplômes."},
 a_actualiser='2027-08-31', raison="Nouveau rapport de l'IAB sur la cohorte 2015.",
))

# 8 ── Danemark ────────────────────────────────────────────────────────────
SCHUMAN_DANEMARK_2026 = ('schuman_danemark_2026', src('Élections législatives au Danemark du 24 mars 2026 (analyse)', 'Fondation Robert Schuman (Helen Levy)', '31 mars 2026',
  'https://www.robert-schuman.eu/en/observatoire/6772',
  "De 2022 à 2026, le gouvernement était une coalition des sociaux-démocrates, des libéraux de Venstre (centre-droit) et des Modérés, qualifiée d'« an atypical coalition ». Le 24 mars 2026, les sociaux-démocrates obtiennent 21,9 % des voix et 38 sièges, « the worst result for the Social Democratic Party since 1903 ». Les électeurs ruraux ont soutenu la « strict stance on immigration » du gouvernement.",
  'Fondation pro-européenne ; analyse factuelle.', 'secondaire'))
RTE_DANEMARK_2026 = ('rte_danemark_2026', src('Nouveau gouvernement danois (dépêche)', 'RTÉ (radiotélévision publique irlandaise)', '2 juin 2026',
  'https://www.rte.ie/news/world/2026/0602/1576271-denmark-government/',
  "Le nouveau « minority cabinet » réunit sociaux-démocrates, sociaux-libéraux, Left Greens et Modérés ; il s'appuie « primarily on the far-left Red-Green Alliance ».",
  'Média public étranger.', 'media'))
CPHPOST_ASILE_2025 = ('cphpost_asile_2025', src('Denmark received and granted a record-low number of asylum permits in 2024', 'The Copenhagen Post, d’après le Service danois de l’immigration', '11 février 2025',
  'https://cphpost.dk/2025-02-11/general/denmark-received-and-granted-a-record-low-number-of-asylum-permits-in-2024',
  "« In 2024, approximately 2,300 people applied for asylum in Denmark ». Environ 860 personnes ont obtenu l'asile, contre « 10,849 permits were granted in 2015, and 7,493 in 2016 ».",
  'Média anglophone local qui cite des données officielles.', 'media'))
AMNESTY_SYRIENS_2021 = ('amnesty_syriens_2021', src('Danemark. Le pays doit renoncer à renvoyer de force illégalement en zone de guerre des centaines de réfugié·e·s syriens', 'Amnesty International', '26 avril 2021',
  'https://www.amnesty.org/fr/latest/news/2021/04/denmark-hundreds-of-refugees-must-not-be-illegally-forced-back-to-syrian-warzone-2/',
  "Au moins 380 Syriens ont vu leur titre révoqué ou non renouvelé entre janvier 2020 et avril 2021, au motif que « Damas et ses environs sont une zone sûre ». Les personnes placées en centres de retour « ne sont pas autorisées à travailler ». Aucune expulsion n'avait eu lieu, faute de relations diplomatiques avec Damas.",
  'ONG de défense des droits humains (engagée) ; donnée ancienne (2021).', 'secondaire'))
THELOCAL_GHETTO_2025 = ('thelocal_ghetto_2025', src('Was EU court discrimination ruling a disappointment for Mjølnerparken residents?', 'The Local Denmark (Michael Barrett)', '20 décembre 2025',
  'https://www.thelocal.dk/20251220/inside-denmark-where-does-eu-discrimination-ruling-leave-non-western-housing-residents',
  "La loi sur les « sociétés parallèles » impose aux quartiers où plus de la moitié des habitants sont « non-Western » de « rent at least 60 percent of the homes at market rates by 2030 ». En décembre 2025, la Cour de justice de l'UE renvoie à la justice danoise le soin de dire si le critère « non occidental » constitue une discrimination selon l'origine ethnique.",
  'Média anglophone local.', 'media'))
BLUEWIN_FRONTIERE_2026 = ('bluewin_frontiere_2026', src('Denmark extends border controls at the German border', 'blue News (bluewin.ch)', '14 octobre 2026',
  'https://www.bluewin.ch/en/news/denmark-extends-border-controls-at-the-german-border-li.3635840',
  "Les contrôles portent sur la frontière germano-danoise et sont prolongés de six mois, jusqu'au 11 mai 2027, avec notification à la Commission européenne. Le cadre est celui de Schengen : « In the Schengen Area, there are generally no internal border controls », des contrôles temporaires étant possibles sous conditions.",
  'Média généraliste suisse ; fiabilité moyenne.', 'media'))

CE_SCHENGEN_DK = ('ce_schengen_dk', src('Temporary Reintroduction of Border Control (Current Temporarily Reintroduced Border Controls)', 'Commission européenne, DG Migration et affaires intérieures', 'page consultée le 8 novembre 2026',
  'https://home-affairs.ec.europa.eu/policies/schengen/schengen-area/temporary-reintroduction-border-control_en?prefLang=lv',
  "La Commission liste les contrôles temporaires notifiés par les États Schengen. Danemark : du 12 juillet au 11 novembre 2026, puis du 12 novembre 2026 au 11 mai 2027, aux « land and sea borders with Germany ». Motifs invoqués : menaces de sabotage attribuées à la Russie, « ongoing terrorism-related incidents and organised crime ».",
  'Institution européenne ; page officielle (citations à revérifier mot à mot).', 'primaire'))

FICHES.append(fiche(
 id='danemark-gauche-frontieres', affirmation="Le Danemark, gouverné par la gauche, a fermé ses frontières : il faut faire pareil.", volet='immigration', sous_theme='Comparaisons européennes',
 mots_cles=['danemark', 'modele danois', 'sociaux democrates danois', 'frederiksen', 'gauche danoise', 'danemark immigration', 'danemark ferme ses frontieres'],
 verdict='trompeur', fiabilite='etabli',
 resume="Les sociaux-démocrates danois mènent bien une politique d'asile très restrictive : environ 2 300 demandes et 860 asiles accordés en 2024, contre 10 849 titres en 2015. Mais le Danemark n'a pas « fermé ses frontières » : il reste dans Schengen et pratique des contrôles temporaires à la frontière allemande, notifiés à Bruxelles. De 2022 à 2026, il était gouverné par une coalition avec le centre-droit. Cette politique a été critiquée pour les réfugiés syriens et la loi sur les « sociétés parallèles », jugée potentiellement discriminatoire.",
 contexte="Le « modèle danois » est cité par la droite et par une partie de la gauche comme la preuve qu'une gauche dure sur l'immigration gagne les élections.",
 explication="Il faut séparer ce que le Danemark a vraiment fait, ses résultats chiffrés, son coût pour les droits, et la question de savoir si c'est souhaitable.",
 sources=[SCHUMAN_DANEMARK_2026, RTE_DANEMARK_2026, CPHPOST_ASILE_2025, AMNESTY_SYRIENS_2021, THELOCAL_GHETTO_2025, BLUEWIN_FRONTIERE_2026, CE_SCHENGEN_DK],
 faits=[
  fait("D'après le Service danois de l'immigration cité par The Copenhagen Post, environ 2 300 personnes ont demandé l'asile au Danemark en 2024 et environ 860 l'ont obtenu, contre 10 849 titres accordés en 2015.", 'cphpost_asile_2025', '2015-2024', 'Danemark', "La politique restrictive a fortement réduit l'asile : c'est un fait que la gauche doit reconnaître.", 'etabli', '2 300 demandes'),
  fait("Selon la Fondation Robert Schuman, le gouvernement de 2022 à 2026 associait les sociaux-démocrates au parti libéral de centre-droit Venstre et aux Modérés.", 'schuman_danemark_2026', '2022-2026', 'Danemark', "Ce n'était pas un gouvernement de gauche.", 'etabli'),
  fait("Selon la même fondation, les sociaux-démocrates ont obtenu 21,9 % aux législatives de mars 2026, leur pire score depuis 1903.", 'schuman_danemark_2026', '2026', 'Danemark', "La ligne dure ne leur a pas garanti le succès électoral.", 'etabli', '21,9 %'),
  fait("La Commission européenne recense des contrôles temporaires notifiés par le Danemark aux seules frontières terrestres et maritimes avec l'Allemagne, du 12 novembre 2026 au 11 mai 2027, au motif de menaces de sabotage, de terrorisme et de crime organisé.", 'ce_schengen_dk', '2026-2027', 'Danemark', "Le Danemark reste dans Schengen : ses frontières ne sont pas fermées.", 'etabli'),
  fait("Selon blue News, ces contrôles sont prolongés de six mois en six mois dans le cadre des règles Schengen, qui permettent des contrôles temporaires sous conditions.", 'bluewin_frontiere_2026', '2026-2027', 'Danemark', "Il s'agit d'une exception temporaire, encadrée par l'UE.", 'estimation'),
  fait("Selon Amnesty International, au moins 380 Syriens ont perdu leur titre de séjour en 2020-2021, Damas étant jugée « zone sûre », sans pouvoir être expulsés faute de relations diplomatiques.", 'amnesty_syriens_2021', '2020-2021', 'Danemark', "La politique a des coûts humains sans toujours produire de renvois.", 'estimation'),
  fait("Selon The Local, la loi sur les « sociétés parallèles » impose 60 % de logements au prix du marché d'ici 2030 dans les quartiers majoritairement « non occidentaux » ; la Cour de justice de l'UE a renvoyé au juge danois la question de la discrimination.", 'thelocal_ghetto_2025', '2025', 'Danemark', "Le critère d'origine est contesté en justice.", 'estimation'),
 ],
 court="Le Danemark n'a pas fermé ses frontières : il reste dans Schengen, avec des contrôles temporaires à la frontière allemande. Sa politique d'asile est très restrictive, c'est vrai, mais elle a été menée avec le centre-droit, elle cible des quartiers selon l'origine et elle n'a pas empêché le pire score des sociaux-démocrates depuis 1903.",
 moyen="Il faut reconnaître un fait : les sociaux-démocrates danois ont durci l'asile, et les demandes sont tombées à environ 2 300 en 2024, contre plus de 10 000 titres accordés en 2015.\n\nMais trois choses sont fausses dans la phrase. Le Danemark n'a pas fermé ses frontières : il reste dans Schengen et contrôle temporairement la frontière allemande, avec l'accord de Bruxelles. Il n'était pas gouverné par la gauche seule, mais avec le centre-droit de 2022 à 2026. Et cette politique a un prix : retrait de titres à des Syriens, loi qui vise des quartiers selon l'origine non occidentale de leurs habitants, contestée devant la justice européenne. Électoralement, elle s'est conclue par le pire score du parti depuis 1903.",
 detaille="Le Danemark est souvent présenté comme la preuve qu'une gauche dure sur l'immigration réussit. Les faits sont plus nuancés. Sur l'asile, la politique a produit des effets massifs : environ 2 300 demandes et 860 asiles accordés en 2024, contre 10 849 titres en 2015 selon le Service danois de l'immigration. Il est impossible d'isoler l'effet de cette politique de celui des pays voisins, mais la baisse est spectaculaire.\n\nEn revanche, le pays n'a pas « fermé ses frontières ». Il est membre de Schengen et pratique des contrôles temporaires à la seule frontière allemande, prolongés de six mois en six mois et notifiés à la Commission européenne. Politiquement, le gouvernement de 2022 à 2026 associait les sociaux-démocrates au centre-droit. En mars 2026, le parti a obtenu 21,9 %, son pire score depuis 1903, et gouverne désormais en minorité avec l'appui de la gauche radicale.\n\nLe coût pour les droits est documenté. Selon Amnesty International, au moins 380 Syriens ont perdu leur titre en 2020-2021, placés dans des centres où ils ne peuvent pas travailler, sans être expulsés. La loi sur les « sociétés parallèles » impose de vendre ou louer au prix du marché 60 % des logements des quartiers majoritairement « non occidentaux » ; la Cour de justice de l'UE a demandé au juge danois de dire si ce critère est discriminatoire. Copier ce modèle, c'est accepter de traiter les gens selon leur origine.",
 empathie="On peut comprendre l'envie d'un exemple qui montrerait qu'on peut maîtriser l'immigration tout en restant un pays social. Le cas danois mérite justement d'être regardé en entier.",
 legitimes=["Le Danemark a fortement réduit le nombre de demandes d'asile.", "Une partie de l'électorat populaire a soutenu cette ligne."],
 contre=[
  ("Ça marche, les chiffres de l'asile ont chuté.", "Les demandes ont chuté, c'est vrai, mais une partie de l'effet tient au contexte régional ; et les moyens employés, comme cibler des quartiers selon l'origine, posent un problème de droits."),
  ("Même la gauche danoise le fait, donc ce n'est pas d'extrême droite.", "Une politique se juge sur son contenu ; et la coalition qui l'a menée de 2022 à 2026 comprenait le centre-droit."),
 ],
 questions=["Savais-tu que le Danemark est toujours dans l'espace Schengen ?", "Trouves-tu juste qu'une loi vise des quartiers selon l'origine non occidentale de leurs habitants ?"],
 limites=["Plusieurs chiffres viennent de médias qui citent des sources officielles (Copenhagen Post, The Local, blue News).", "La date de début des contrôles à la frontière allemande n'a pas été vérifiée ; la page de la Commission ne donne que les périodes en cours.", "Les données d'Amnesty sur les Syriens datent de 2021."],
 publics={'convaincus': "Le Danemark n'a pas fermé ses frontières : il est toujours dans Schengen et contrôle temporairement la frontière allemande avec l'accord de Bruxelles. Et c'était une coalition avec le centre-droit, qui a fini au pire score des sociaux-démocrates depuis 1903. Avant de copier, regarde aussi la loi qui vise des quartiers selon l'origine de leurs habitants.",
  'indecis': "Le Danemark a réellement réduit l'asile, et c'est un exemple souvent cité. Mais il reste dans l'espace Schengen, et sa politique est contestée en justice parce qu'elle traite certains habitants selon leur origine. On peut s'en inspirer sur certains points sans en accepter les dérives."},
 a_actualiser='2027-05-31', raison="Fin de la prolongation des contrôles à la frontière et nouvelles données sur l'asile.",
))

# 9 ── Immigration choisie et quotas : le Canada ──────────────────────────
IRCC_REDUCTION_2024 = ('ircc_reduction_2024', src('Government of Canada reduces immigration', 'Immigration, Réfugiés et Citoyenneté Canada (ministère canadien de l’Immigration)', '24 octobre 2024',
  'https://www.canada.ca/en/immigration-refugees-citizenship/news/2024/10/government-of-canada-reduces-immigration.html',
  "Le plan précédent visait 500 000 résidents permanents en 2025 et en 2026 ; les nouvelles cibles sont 395 000 (2025), 380 000 (2026) et 365 000 (2027). Objectif : ramener les résidents temporaires à 5 % de la population fin 2026. « Permanent resident admissions in the economic class will reach 61.7% of total admissions by 2027. »",
  'Ministère canadien.', 'primaire'))
IRCC_PLAN_2026 = ('ircc_plan_2026', src("Renseignements supplémentaires relatifs au Plan des niveaux d'immigration 2026-2028", 'Immigration, Réfugiés et Citoyenneté Canada (ministère canadien de l’Immigration)', '4 novembre 2025 (modifié le 13 octobre 2026)',
  'https://www.canada.ca/fr/immigration-refugies-citoyennete/organisation/mandat/initiatives-ministerielles/niveaux/renseignements-supplementaires-niveaux-immigration-2026-2028.html',
  "« le nombre d'admissions de résidents permanents se stabilisera à 380 000 de 2026 à 2028 ». Cibles 2026 : 239 800 dans la catégorie économique, 84 000 dans la catégorie familiale, 49 300 réfugiés et personnes protégées, 6 900 humanitaires et autres. 385 000 nouveaux résidents temporaires sont visés en 2026.",
  'Ministère canadien.', 'primaire'))
STATCAN_POP_2026 = ('statcan_pop_2026', src("Canada's population estimates, fourth quarter 2025", 'Statistique Canada', '18 mars 2026',
  'https://www150.statcan.gc.ca/n1/daily-quotidien/260318/dq260318b-eng.htm',
  "« the population of Canada decreased by 102,436 people (-0.2%) » en 2025 ; elle compte 41 472 081 habitants au 1er janvier 2026. Les résidents non permanents passent de 3 149 131 au pic d'octobre 2024 à 2 676 441 au 1er janvier 2026. Estimations préliminaires.",
  'Institut statistique national.', 'primaire'))
PUBLICSENAT_QUOTAS_2019 = ('publicsenat_quotas_2019', src("« Irréaliste » ou « pragmatique » ? L'État relance l'idée des « quotas » d'immigration", 'Public Sénat (Shahzad Abdul)', '7 octobre 2019',
  'https://www.publicsenat.fr/actualites/politique/irrealiste-ou-pragmatique-l-etat-relance-l-idee-des-quotas-d-immigration-146112',
  "La commission Mazeaud (2008) jugeait les quotas « pas utile à la maîtrise des flux de l'immigration professionnelle » et « impossible à réaliser, d'un point de vue constitutionnel et conventionnel, pour l'immigration familiale ». Selon Édouard Philippe, les quotas « ne peuvent pas s'appliquer à l'asile, ni à l'immigration familiale ». Jean-Christophe Dumont (OCDE) : « Ça pourrait même être contre-productif ».",
  'Média parlementaire public ; chiffres de 2018 anciens.', 'media'))
PUBLICSENAT_QUOTAS_2024 = ('publicsenat_quotas_2024', src('Loi immigration : pourquoi le débat annuel au Parlement sur la fixation de quotas a été censuré', 'Public Sénat (Guillaume Jacquot)', '26 janvier 2024',
  'https://www.publicsenat.fr/actualites/politique/loi-immigration-pourquoi-le-debat-annuel-au-parlement-sur-la-fixation-de-quotas-a-ete-censure',
  "Le Conseil constitutionnel (décision 2023-863 DC) a censuré l'obligation d'un débat annuel sur des objectifs chiffrés : l'article 48 de la Constitution ne permet pas à une loi de l'imposer, et cela « pourrait faire obstacle aux prérogatives » du Gouvernement et des assemblées. La censure porte sur la procédure, pas sur le principe des quotas.",
  'Média parlementaire public.', 'media'))
PUBLICSENAT_TITRES_2025 = ('publicsenat_titres_2025', src('Immigration : titres de séjour en nette hausse et régularisations en baisse sur l’année 2025', 'Public Sénat, d’après le ministère de l’Intérieur', '27 janvier 2026',
  'https://www.publicsenat.fr/actualites/societe/immigration-titres-de-sejour-en-nette-hausse-et-regularisations-en-baisse-sur-lannee-2025',
  "384 230 premiers titres de séjour ont été délivrés en 2025 (+11,2 %), dont environ 118 000 pour études, premier motif, 92 600 humanitaires (+65 %) et 51 190 économiques (-13 %).",
  'Média parlementaire public, données du ministère de l’Intérieur.', 'media'))

FICHES.append(fiche(
 id='immigration-choisie-canada', affirmation="Il faut une immigration choisie avec des quotas, comme au Canada.", volet='immigration', sous_theme='Immigration et travail',
 mots_cles=['modele canadien', 'comme au canada', 'immigration choisie', 'quotas d immigration', 'immigration par points', 'systeme a points', 'canada immigration'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le Canada sélectionne environ 63 % de ses nouveaux résidents permanents sur des critères économiques, bien plus que la France (51 190 titres économiques sur 384 230 en 2025). Mais le modèle canadien, c'est beaucoup d'immigration : 380 000 résidents permanents par an pour 41,5 millions d'habitants, après une cible de 500 000. En France, des quotas sur l'immigration familiale ou l'asile sont jugés impossibles constitutionnellement et conventionnellement depuis la commission Mazeaud (2008).",
 contexte="Le modèle canadien est cité à droite comme à l'extrême droite pour réclamer une immigration « choisie » plutôt que « subie ».",
 explication="Il faut regarder ce que fait vraiment le Canada (volumes et composition) et ce que le droit français permet.",
 sources=[IRCC_REDUCTION_2024, IRCC_PLAN_2026, STATCAN_POP_2026, PUBLICSENAT_QUOTAS_2019, PUBLICSENAT_QUOTAS_2024, PUBLICSENAT_TITRES_2025],
 faits=[
  fait("Selon le ministère canadien de l'Immigration, le Canada vise 380 000 nouveaux résidents permanents par an de 2026 à 2028, après une cible de 395 000 en 2025 et un plan antérieur à 500 000.", 'ircc_plan_2026', '2025-2028', 'Canada', "Le modèle canadien repose sur des volumes élevés.", 'etabli', '380 000 par an'),
  fait("Pour 2026, les cibles canadiennes sont de 239 800 admissions économiques, 84 000 familiales et 56 200 réfugiés et humanitaires.", 'ircc_plan_2026', '2026', 'Canada', "Environ deux tiers sont sélectionnés sur critères économiques, mais le regroupement familial et l'asile restent importants.", 'etabli'),
  fait("Selon Statistique Canada, la population a baissé de 102 436 personnes en 2025, sous l'effet de la réduction des résidents temporaires.", 'statcan_pop_2026', '2025', 'Canada', "Le Canada a récemment réduit l'immigration temporaire.", 'etabli'),
  fait("D'après le ministère de l'Intérieur, la France a délivré 384 230 premiers titres de séjour en 2025, dont 51 190 pour motif économique et environ 118 000 pour études.", 'publicsenat_titres_2025', '2025', 'France', "La part économique est faible en France : c'est un argument réel des partisans de l'immigration choisie.", 'etabli', '51 190'),
  fait("Selon la commission Mazeaud (2008), des quotas seraient inutiles pour l'immigration professionnelle et impossibles constitutionnellement et conventionnellement pour l'immigration familiale.", 'publicsenat_quotas_2019', '2008', 'France', "Le droit encadre fortement l'idée de quotas.", 'etabli'),
  fait("En janvier 2024, le Conseil constitutionnel a censuré l'obligation d'un débat annuel au Parlement sur des objectifs chiffrés d'immigration, pour un motif de procédure.", 'publicsenat_quotas_2024', '2024', 'France', "Les quotas ne sont pas interdits en soi, mais leur mise en œuvre bute sur la Constitution.", 'etabli'),
 ],
 court="Le Canada choisit en effet l'essentiel de ses immigrés sur des critères économiques. Mais il en accueille énormément : 380 000 résidents permanents par an pour 41 millions d'habitants. Et en France, des quotas sur la famille ou l'asile se heurtent à la Constitution et aux traités.",
 moyen="Le modèle canadien est réel : environ 63 % des nouveaux résidents permanents sont admis sur critères économiques. En France, les titres économiques ne représentaient que 51 190 des 384 230 premiers titres en 2025. Sur ce point, l'argument n'est pas absurde.\n\nMais ceux qui citent le Canada oublient les volumes : 380 000 résidents permanents par an pour 41,5 millions d'habitants, après un objectif de 500 000. Proportionnellement, c'est bien plus que la France. Et le Canada garde 84 000 admissions familiales et près de 50 000 réfugiés par an. En France, la commission Mazeaud a jugé des quotas sur l'immigration familiale impossibles constitutionnellement. Choisir son immigration, c'est d'abord la vouloir.",
 detaille="Le Canada fixe chaque année des niveaux d'immigration. Pour 2026-2028, il vise 380 000 nouveaux résidents permanents par an : en 2026, 239 800 dans la catégorie économique, 84 000 dans la catégorie familiale, 49 300 réfugiés et 6 900 cas humanitaires. Le plan précédent visait 500 000 par an ; le gouvernement l'a réduit en 2024, surtout pour limiter les résidents temporaires, et la population a baissé de 102 436 personnes en 2025 selon Statistique Canada.\n\nLa comparaison avec la France est éclairante. En 2025, la France a délivré 384 230 premiers titres de séjour, dont environ 118 000 pour études et 51 190 pour motif économique. Le Canada, avec 41,5 millions d'habitants, admet donc proportionnellement beaucoup plus de résidents permanents. Les partisans de l'immigration choisie ont raison sur un point : la part économique est faible en France. Mais le modèle canadien, c'est une immigration massive et organisée, pas une fermeture.\n\nEnfin, le droit. La commission Mazeaud, en 2008, a jugé les quotas inutiles pour l'immigration professionnelle et impossibles pour l'immigration familiale, protégée par la Constitution et les conventions. En 2024, le Conseil constitutionnel a censuré le débat annuel obligatoire sur des quotas, pour un motif de procédure. On peut améliorer l'accueil des travailleurs ; promettre des quotas sur le regroupement familial ou l'asile, c'est promettre ce que le droit ne permet pas.",
 empathie="L'idée de choisir qui vient, selon les besoins du pays, paraît de bon sens à beaucoup de gens. Le Canada montre ce que ce choix implique vraiment.",
 legitimes=["La part de l'immigration de travail est faible en France.", "Le Canada sélectionne majoritairement sur critères économiques."],
 contre=[
  ("On veut le système canadien, pas les volumes canadiens.", "Le système à points canadien sert justement à attirer beaucoup de travailleurs ; il fonctionne parce que le pays veut de l'immigration."),
  ("On changera la Constitution pour les quotas.", "Le droit de mener une vie familiale normale est aussi protégé par la Convention européenne des droits de l'homme."),
 ],
 questions=["Savais-tu que le Canada accueille proportionnellement bien plus de résidents permanents que la France ?", "Serais-tu prêt à accepter les volumes canadiens en échange d'une sélection économique ?"],
 limites=["La comparaison n'est pas à périmètre identique : les titres français incluent les étudiants, résidents temporaires au Canada.", "Le chiffre des titres familiaux français en 2025 n'a pas été trouvé dans les pages lues.", "Le rapport Mazeaud lui-même n'a pas pu être ouvert ; il est cité à travers Public Sénat (2019)."],
 publics={'convaincus': "Tu veux le modèle canadien ? Il accueille 380 000 résidents permanents par an pour 41 millions d'habitants, bien plus que nous en proportion, avec encore 84 000 admissions familiales. Sélectionner, oui, mais le Canada le fait parce qu'il veut beaucoup d'immigrés. Et des quotas sur la famille, la commission Mazeaud les a jugés contraires à la Constitution.",
  'indecis': "Il est vrai que la France accueille peu d'immigration de travail par rapport au Canada, et le débat est légitime. Mais le modèle canadien suppose des volumes très élevés, et en France le regroupement familial et l'asile sont protégés par la Constitution et les traités. On peut mieux organiser l'immigration de travail sans promettre l'impossible."},
 a_actualiser='2027-11-30', raison="Nouveau plan des niveaux d'immigration canadien.",
))

# 10 ── Féminicides et nationalité ─────────────────────────────────────────
INTERIEUR_MVC_2024 = ('interieur_mvc_2024', src('Étude nationale sur les morts violentes au sein du couple, année 2024', "Ministère de l'Intérieur, Délégation aux victimes (publié sur Vie publique)", '2025',
  'https://www.vie-publique.fr/files/rapport/pdf/300372.pdf',
  "107 femmes et 31 hommes ont été tués au sein du couple en 2024, soit 138 morts. « 116 auteurs sont de nationalité française (soit 84 %) et 22 auteurs de nationalité étrangère (soit 16 %) ». « 75 % n'exercent pas ou plus d'activité professionnelle (61 auteurs sont sans emploi et 43 à la retraite) ». Les 70 ans et plus représentent 24 % des auteurs. « les disputes (43 cas) et les séparations non acceptées (22 cas) sont les causes principales ».",
  'Étude officielle du ministère.', 'primaire'))
INTERIEUR_MVC_2023 = ('interieur_mvc_2023', src('Étude nationale sur les morts violentes au sein du couple, année 2023', "Ministère de l'Intérieur, Délégation aux victimes (publié sur Vie publique)", '2024',
  'https://www.vie-publique.fr/files/rapport/pdf/300392_0.pdf',
  "96 femmes et 23 hommes ont été tués au sein du couple en 2023, soit 119 morts. « 92 auteurs sont de nationalité française (soit 77 %) et 27 auteurs de nationalité étrangère (soit 23 %) ».",
  'Étude officielle du ministère.', 'primaire'))
PUBLICSENAT_FEMINICIDES_2025 = ('publicsenat_feminicides_2025', src('Violences conjugales : 107 femmes tuées par leur conjoint ou ex-conjoint en 2024, une augmentation de 11 %', 'Public Sénat (Aglaée Marchand)', '31 octobre 2025',
  'https://www.publicsenat.fr/actualites/societe/violences-conjugales-107-femmes-tuees-par-leur-conjoint-ou-ex-conjoint-en-2024-une-augmentation-de-11',
  "138 morts violentes au sein du couple en 2024 contre 119 en 2023 ; les femmes en représentent « 107 (77 %) » ; 403 tentatives d'homicide. Le profil type de l'auteur est « le plus souvent en couple, de nationalité française et n'exerçant pas ou plus d'activité professionnelle », et « majoritairement âgé de 20 à 49 ans ».",
  'Média parlementaire public.', 'media'))

FICHES.append(fiche(
 id='feminicides-etrangers', affirmation="Les féminicides sont surtout commis par des étrangers.", volet='securite', sous_theme='Violences intrafamiliales',
 mots_cles=['feminicide', 'feminicides', 'femmes tuees par leur conjoint', 'femmes tuees', 'morts violentes au sein du couple', 'meurtres de femmes etrangers'],
 verdict='contredit', fiabilite='etabli',
 resume="Selon l'étude officielle du ministère de l'Intérieur, 84 % des auteurs de morts violentes au sein du couple en 2024 étaient de nationalité française (116 sur 138), et 77 % en 2023. Les auteurs étrangers sont surreprésentés par rapport à leur part dans la population (16 à 23 % des auteurs pour 8,8 % de la population), mais ils sont loin d'être majoritaires. Le profil type est un homme de nationalité française, souvent sans activité professionnelle, qui tue lors d'une dispute ou d'une séparation refusée.",
 contexte="Après certains meurtres médiatisés, l'idée que les violences faites aux femmes seraient « importées » circule pour détourner le débat des violences conjugales.",
 explication="Le ministère publie chaque année la nationalité des auteurs de morts violentes au sein du couple : c'est la donnée la plus directe.",
 sources=[INTERIEUR_MVC_2024, INTERIEUR_MVC_2023, PUBLICSENAT_FEMINICIDES_2025, INSEE_ETRANGERS_2024],
 faits=[
  fait("En 2024, 107 femmes et 31 hommes ont été tués par leur conjoint ou ex-conjoint, soit 138 morts.", 'interieur_mvc_2024', '2024', 'France', "Les violences conjugales mortelles augmentent.", 'etabli', '107 femmes'),
  fait("En 2024, 116 auteurs sur 138 (84 %) étaient de nationalité française et 22 (16 %) de nationalité étrangère.", 'interieur_mvc_2024', '2024', 'France', "La grande majorité des auteurs sont français.", 'etabli', '84 %'),
  fait("En 2023, 92 auteurs sur 119 (77 %) étaient de nationalité française et 27 (23 %) de nationalité étrangère.", 'interieur_mvc_2023', '2023', 'France', "Le constat est le même d'une année sur l'autre.", 'etabli', '77 %'),
  fait("Les étrangers représentent 8,8 % de la population en 2024 selon l'Insee.", 'insee_etrangers_2024', '2024', 'France', "Les auteurs étrangers sont surreprésentés par rapport à leur poids dans la population : c'est un fait à reconnaître.", 'etabli', '8,8 %'),
  fait("En 2024, 75 % des auteurs n'exerçaient pas ou plus d'activité professionnelle (61 sans emploi, 43 retraités) ; disputes et séparations non acceptées sont les causes principales.", 'interieur_mvc_2024', '2024', 'France', "Les facteurs sociaux et la rupture pèsent lourd.", 'etabli', '75 %'),
 ],
 court="Faux : selon le ministère de l'Intérieur, 84 % des auteurs de morts violentes au sein du couple en 2024 étaient français. Les étrangers sont surreprésentés par rapport à leur poids dans la population, mais le féminicide est d'abord une violence conjugale, pas une affaire d'origine.",
 moyen="Le ministère de l'Intérieur publie chaque année une étude sur les morts violentes au sein du couple. En 2024, 107 femmes ont été tuées par leur conjoint ou ex-conjoint. Sur 138 auteurs, 116 étaient français, soit 84 %. En 2023, c'était 77 %.\n\nIl faut être honnête : les étrangers représentent 16 à 23 % des auteurs selon les années, alors qu'ils forment 8,8 % de la population. Ils sont donc surreprésentés, comme dans d'autres statistiques pénales où l'âge et la précarité jouent. Mais dire que les féminicides sont « surtout » le fait d'étrangers est faux. Le profil type est un homme français, souvent sans emploi ou retraité, qui tue lors d'une dispute ou d'une séparation qu'il refuse.",
 detaille="Les chiffres viennent de l'étude nationale de la Délégation aux victimes du ministère de l'Intérieur. En 2024, 138 personnes ont été tuées par leur conjoint ou ex-conjoint, dont 107 femmes, en hausse de 11 % ; 403 tentatives d'homicide ont aussi été recensées. Sur les 138 auteurs, 116 étaient de nationalité française (84 %) et 22 de nationalité étrangère (16 %). En 2023, la proportion était de 77 % et 23 %.\n\nLa surreprésentation existe : 16 à 23 % des auteurs sont étrangers, pour 8,8 % de la population. La comparaison reste grossière, car elle ne tient compte ni de l'âge, ni du sexe, ni de la situation de couple, et les effectifs sont petits (22 à 27 auteurs), donc les variations annuelles sont fortes. La nationalité ne dit rien non plus de l'origine des auteurs français.\n\nLe portrait qui ressort de l'étude est surtout social et conjugal : 75 % des auteurs n'exercent pas ou plus d'activité professionnelle, 24 % ont 70 ans ou plus, et les principales causes sont les disputes et les séparations non acceptées. Transformer les féminicides en question d'immigration, c'est détourner l'attention de ce qui permet de les prévenir : écouter les plaintes, protéger les femmes qui partent, suivre les hommes violents.",
 empathie="Chaque féminicide est un drame, et la colère qu'il suscite est légitime. Justement, pour protéger les femmes, il faut savoir qui tue et pourquoi.",
 legitimes=["Les auteurs étrangers sont surreprésentés par rapport à leur part dans la population.", "Le nombre de femmes tuées a augmenté en 2024."],
 contre=[
  ("Parmi les Français, beaucoup sont d'origine étrangère.", "L'étude ne donne pas l'origine ; mais la nationalité est la donnée disponible, et elle contredit l'affirmation. Le profil social et conjugal, lui, est bien documenté."),
  ("Les médias cachent la nationalité des auteurs.", "Le ministère de l'Intérieur la publie chaque année dans une étude officielle."),
 ],
 questions=["Savais-tu que plus de huit auteurs sur dix de féminicides en 2024 étaient français ?", "Qu'est-ce qui protégerait le mieux les femmes menacées, selon toi ?"],
 limites=["La nationalité porte sur tous les auteurs de morts au sein du couple, femmes autrices comprises, et non sur les seuls féminicides.", "L'étude ne publie pas de donnée sur l'origine immigrée ni la binationalité.", "La comparaison avec la part des étrangers dans la population n'est pas ajustée selon l'âge et le sexe."],
 publics={'convaincus': "Le ministère de l'Intérieur publie la nationalité des auteurs : en 2024, 84 % étaient français, 116 sur 138. Les étrangers sont un peu surreprésentés, je ne le cache pas, mais ils sont loin d'être la majorité. Le profil type, c'est un homme français qui ne supporte pas la séparation.",
  'indecis': "Les chiffres officiels montrent que la grande majorité des auteurs de féminicides sont français, même si les étrangers sont surreprésentés. Le point commun, ce sont surtout les disputes et les séparations refusées. Protéger les femmes, c'est d'abord agir sur ces situations."},
 a_actualiser='2027-11-30', raison="Étude nationale 2025 sur les morts violentes au sein du couple.",
))

# ══ Lot C : politique et institutions ══════════════════════════════════════

# 11 ── RN et sortie de l'euro ─────────────────────────────────────────────
PUBLICSENAT_LEPEN_2017 = ('publicsenat_lepen_2017', src('Les principales mesures du programme de Marine Le Pen', 'Public Sénat', '4 février 2017',
  'https://www.publicsenat.fr/article/politique/les-principales-mesures-du-programme-de-marine-le-pen-54228',
  "Le programme dévoilé à Lyon prévoit une « sortie de l'euro par le « rétablissement d'une monnaie nationale » ». Après une négociation avec l'UE, un référendum porterait sur « l'appartenance » à l'Union européenne, pour « récupérer » quatre « souverainetés » (monétaire, législative, territoriale, économique) ».",
  'Média parlementaire public.', 'media'))
PUBLICSENAT_RN_EURO_2019 = ('publicsenat_rn_euro_2019', src('Européennes : Marine Le Pen veut « tout remettre sur la table » sans quitter l’euro', 'Public Sénat (Anne Renaut)', '15 avril 2019',
  'https://www.publicsenat.fr/actualites/politique/europeennes-marine-le-pen-veut-tout-remettre-sur-la-table-sans-quitter-l-euro',
  "Le RN renonce à sortir de la monnaie unique, un changement de cap après la présidentielle. Marine Le Pen juge l'euro « qui a énormément de défauts ». Le manifeste veut retirer à la Commission « l'intégralité de ses pouvoirs » et créer une « Alliance européenne des nations ».",
  'Média parlementaire public.', 'media'))
PUBLICSENAT_BAY_2019 = ('publicsenat_bay_2019', src('Abandon de la sortie de l’euro au RN : « On n’est pas dogmatique », explique Nicolas Bay', 'Public Sénat', '15 avril 2019',
  'https://www.publicsenat.fr/article/politique/abandon-de-la-sortie-de-l-euro-au-rn-on-n-est-pas-dogmatique-explique-nicolas-bay',
  "L'eurodéputé RN Nicolas Bay déclare : « Nous, on est pragmatique, on n'est pas dogmatique dans ce domaine ». Selon lui, l'idée « qu'il fallait sortir brutalement, unilatéralement [de l'euro] était une erreur ».",
  'Média parlementaire public ; déclaration d’un dirigeant du RN.', 'media'))
PUBLICSENAT_LEPEN_EUROPE_2022 = ('publicsenat_lepen_europe_2022', src('Sur l’Europe, Marine Le Pen a-t-elle vraiment changé ?', 'Public Sénat', '14 avril 2022',
  'https://www.publicsenat.fr/article/politique/sur-l-europe-marine-le-pen-a-t-elle-vraiment-change-202482',
  "Marine Le Pen affirme en 2022 : « Le Frexit n'est nullement notre projet ». Son programme prévoit d'inscrire la supériorité de la Constitution sur le droit européen, une « Alliance européenne des nations » destinée à remplacer progressivement l'UE et une baisse de 5 milliards d'euros de la contribution française au budget européen, contraire au cadre financier 2021-2027. Le juriste Dominique Rousseau, cité par Challenges, y voit « une attaque en règle contre le droit européen » qui pourrait « à terme » conduire au Frexit.",
  'Média parlementaire public ; analyses juridiques attribuées.', 'media'))
LCP_REFERENDUM_2022 = ('lcp_referendum_2022', src('Présidentielle : est-il possible de gouverner par référendum, comme le propose Marine Le Pen ?', 'LCP (Raphaël Marchal)', '13 avril 2022',
  'https://lcp.fr/actualites/presidentielle-est-il-possible-de-gouverner-par-referendum-comme-le-propose-marine-le',
  "Le constitutionnaliste Jean-Philippe Derosier juge qu'un recours à l'article 11 sur l'immigration serait « un coup d'État constitutionnel ». Pour une révision par l'article 89, l'accord des deux chambres est « un préalable nécessaire qui ne serait pas facile à atteindre ». Faire primer le droit national exposerait la France à des sanctions ou conduirait à une sortie de l'UE.",
  'Chaîne parlementaire.', 'media'))
MONTAIGNE_LEGISLATIVES_2024 = ('montaigne_legislatives_2024', src('Législatives 2024 – Chiffrage global des programmes', 'Institut Montaigne', '5 juillet 2024',
  'https://institutmontaigne.org/communiques-de-presse/legislatives-2024-chiffrage-global-des-programmes',
  "Selon l'institut, le programme du RN représente 85 Md€ de dépenses et baisses d'impôts pour 14 Md€ d'économies, soit une hausse du déficit de 71 Md€ par an (environ 2,5 points de PIB) ; le RN « aura sans aucun doute des difficultés à tenir ses multiples engagements ». Même chiffrage : Nouveau Front populaire +179 Md€ par an, Ensemble +21 Md€ par an.",
  'Think tank libéral (orientation à signaler) ; méthode publique.', 'etude'))

FICHES.append(fiche(
 id='rn-sortie-euro-abandon', affirmation="Le RN a renoncé à sortir de l'euro, il est devenu un parti sérieux.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['rn sortie de l euro', 'rn et l euro', 'le pen euro', 'sortir de l euro', 'frexit', 'rn parti serieux', 'alliance europeenne des nations', 'rn europe'],
 verdict='trompeur', fiabilite='etabli',
 resume="C'est exact : le RN a abandonné la sortie de l'euro en 2019, après l'avoir défendue en 2017. Mais son projet européen reste en conflit avec les traités : primauté de la Constitution sur le droit européen, baisse unilatérale de 5 milliards de la contribution à l'UE, « Alliance européenne des nations » destinée à remplacer l'UE. Des constitutionnalistes y voient un risque de sanctions ou de sortie de fait. Et son programme de 2024 creusait le déficit de 71 Md€ par an selon l'Institut Montaigne. Le NFP faisait pire dans le même chiffrage.",
 contexte="Le RN met en avant l'abandon de la sortie de l'euro comme preuve de sa « normalisation » et de sa crédibilité.",
 explication="Il faut distinguer le changement réel de position sur la monnaie et la compatibilité du reste du programme avec les engagements européens et budgétaires.",
 sources=[PUBLICSENAT_LEPEN_2017, PUBLICSENAT_RN_EURO_2019, PUBLICSENAT_BAY_2019, PUBLICSENAT_LEPEN_EUROPE_2022, LCP_REFERENDUM_2022, MONTAIGNE_LEGISLATIVES_2024],
 faits=[
  fait("En 2017, le programme de Marine Le Pen prévoyait la sortie de l'euro par le « rétablissement d'une monnaie nationale » et un référendum sur l'appartenance à l'UE.", 'publicsenat_lepen_2017', '2017', 'France', "Le RN a longtemps défendu la sortie de l'euro.", 'etabli'),
  fait("En avril 2019, le RN a renoncé à la sortie de l'euro ; Nicolas Bay a déclaré que l'idée de « sortir brutalement, unilatéralement » était « une erreur ».", 'publicsenat_bay_2019', '2019', 'France', "Le changement de position est réel.", 'etabli'),
  fait("En 2022, le programme prévoyait la supériorité de la Constitution sur le droit européen et une baisse de 5 milliards de la contribution française, contraire au cadre financier européen 2021-2027.", 'publicsenat_lepen_europe_2022', '2022', 'France', "Le projet européen reste en conflit avec les traités.", 'etabli', '5 milliards'),
  fait("Le constitutionnaliste Jean-Philippe Derosier a qualifié de « coup d'État constitutionnel » le recours à l'article 11 pour un référendum sur l'immigration proposé par Marine Le Pen.", 'lcp_referendum_2022', '2022', 'France', "Plusieurs mesures butent sur la Constitution.", 'etabli'),
  fait("Selon l'Institut Montaigne, le programme du RN aux législatives de 2024 aurait creusé le déficit de 71 Md€ par an ; celui du NFP de 179 Md€ par an.", 'montaigne_legislatives_2024', '2024', 'France', "Le sérieux budgétaire du RN est contesté ; celui du NFP aussi, et davantage : c'est un fait défavorable à la gauche.", 'estimation', '71 Md€'),
 ],
 court="Oui, le RN a abandonné la sortie de l'euro en 2019. Mais il veut toujours faire primer le droit français sur le droit européen et réduire unilatéralement sa contribution : des juristes y voient une sortie de fait. Changer de slogan ne suffit pas à rendre un programme sérieux.",
 moyen="Le changement est réel : en 2017, Marine Le Pen promettait le retour à une monnaie nationale ; en 2019, le RN a jugé cette idée « une erreur ».\n\nMais le reste du projet européen n'a pas disparu. En 2022, le programme voulait faire primer la Constitution sur le droit européen, baisser unilatéralement de 5 milliards la contribution de la France et remplacer progressivement l'UE par une « Alliance européenne des nations ». Des juristes comme Dominique Rousseau y voient une attaque contre le droit européen qui pourrait mener au Frexit. Sur le budget, l'Institut Montaigne chiffrait le programme RN de 2024 à 71 Md€ de déficit supplémentaire par an. Il faut ajouter que le NFP était chiffré plus haut encore : le sérieux se démontre par le détail, pas par un renoncement.",
 detaille="Le RN a bien changé de position sur l'euro. En février 2017, le programme présidentiel prévoyait le « rétablissement d'une monnaie nationale » et un référendum sur l'appartenance à l'Union européenne. Après la défaite, en avril 2019, le parti a renoncé à la sortie de la monnaie unique ; Nicolas Bay a reconnu que l'idée de sortir « brutalement, unilatéralement » était « une erreur ».\n\nMais renoncer à l'euro ne règle pas la question européenne. En 2022, Marine Le Pen affirmait que « le Frexit n'est nullement notre projet », tout en proposant d'inscrire la supériorité de la Constitution sur le droit européen, de baisser de 5 milliards la contribution française, ce qui contrevient au cadre financier 2021-2027, et de créer une « Alliance européenne des nations » destinée à remplacer l'UE. Des constitutionnalistes ont souligné qu'appliquer ces mesures exposerait la France à des sanctions ou à une sortie de fait, et qualifié de « coup d'État constitutionnel » un référendum sur l'immigration par l'article 11.\n\nSur le budget, l'Institut Montaigne estimait en 2024 que le programme du RN creuserait le déficit de 71 Md€ par an et que le parti aurait « des difficultés à tenir ses multiples engagements ». Le même institut chiffrait le programme du NFP à 179 Md€ : la critique budgétaire vaut pour tout le monde. Ce qui distingue le RN, c'est un projet qui reste en conflit frontal avec le droit européen, présenté comme une normalisation.",
 empathie="Beaucoup d'électeurs ont été rassurés par l'abandon de la sortie de l'euro, qui leur faisait peur pour leur épargne. C'est un vrai changement ; il mérite d'être examiné jusqu'au bout.",
 legitimes=["Le RN a réellement renoncé à la sortie de l'euro.", "Le programme du NFP était chiffré à un déficit supplémentaire plus élevé que celui du RN."],
 contre=[
  ("Le RN ne veut plus sortir de l'UE, c'est écrit.", "Le programme ne parle plus de Frexit, mais il veut faire primer le droit national et réduire unilatéralement la contribution, ce que les traités interdisent."),
  ("La gauche est encore moins sérieuse sur le budget.", "Selon l'Institut Montaigne, le programme NFP creusait davantage le déficit ; la gauche doit répondre sur ses financements, ce qui ne rend pas le programme RN plus solide."),
 ],
 questions=["Savais-tu que le programme de 2022 prévoyait de remplacer progressivement l'UE par une « Alliance européenne des nations » ?", "Comment faire primer le droit français sur le droit européen sans se mettre en conflit avec l'UE ?"],
 limites=["Les analyses juridiques datent de 2022 ; aucune analyse du programme pour 2027 n'a été lue.", "L'Institut Montaigne est un think tank libéral ; ses chiffrages sont contestés par les partis concernés."],
 publics={'convaincus': "C'est vrai, le RN a lâché la sortie de l'euro en 2019, et c'est tant mieux pour ton épargne. Mais il veut toujours faire primer le droit français sur le droit européen et baisser seul sa contribution : des juristes y voient un Frexit qui ne dit pas son nom. Et l'Institut Montaigne, pas franchement de gauche, chiffrait son programme à 71 milliards de déficit en plus par an.",
  'indecis': "Le RN a changé sur l'euro, c'est un fait. Mais son projet européen reste en conflit avec les traités, et son programme budgétaire a été jugé difficile à tenir, comme d'ailleurs celui de la gauche. Le plus utile est de regarder chaque mesure et son financement."},
 a_actualiser='2027-04-30', raison="Programme présidentiel 2027 du RN.",
))

# 12 ── Sénateurs : privilèges ─────────────────────────────────────────────
PUBLICSENAT_AFM_2024 = ('publicsenat_afm_2024', src('Comment fonctionne l’avance de frais de mandats des sénateurs ?', 'Public Sénat (Simon Barbarit)', '30 janvier 2024',
  'https://www.publicsenat.fr/actualites/parlementaire/comment-fonctionne-lavance-de-frais-de-mandats-des-senateurs',
  "Au 1er janvier 2024, l'indemnité est de 7 637,39 € brut, soit 5 676,12 € net avant impôt. L'avance de frais de mandat passe de 5 900 € à 6 600 € par mois (décision du Bureau du 16 novembre 2023), au nom « du contexte inflationniste ». Les dépenses doivent être « raisonnables » et sont contrôlées par le comité de déontologie avec deux cabinets comptables ; chaque sénateur fait l'objet d'au moins un contrôle approfondi par mandat.",
  'Chaîne du Sénat (source institutionnellement liée au Sénat).', 'media'))
PUBLICSENAT_RETRAITES_2023 = ('publicsenat_retraites_2023', src('Les sénateurs vont baisser de 20 % leurs pensions de retraite', 'Public Sénat (François Vignal)', '12 juillet 2023',
  'https://www.publicsenat.fr/actualites/politique/retraites-les-senateurs-sappliquent-la-reforme-et-vont-baisser-de-20-leurs-pensions',
  "L'âge de départ passe de 62 à 64 ans. La pension pour un mandat de six ans passe d'environ 2 200 € à environ 1 800 € net par mois. La pension moyenne citée par le Sénat en 2019 était d'environ 3 856 € net. La caisse des sénateurs coûte moins de 8 M€ à la dotation de l'État, contre 67 M€ pour les députés. Gérard Larcher parlait auparavant d'« un régime avantageux ».",
  'Chaîne du Sénat.', 'media'))
SENAT_BUREAU_2023 = ('senat_bureau_2023', src('Compte rendu du Bureau du Sénat du 12 juillet 2023', 'Sénat', '12 juillet 2023',
  'https://www.senat.fr/fileadmin/cru-1746021083/Organisation_interne/Bureau/Comptes_rendus/2023/04_CR_Bureau_120723.pdf',
  "Le Bureau transpose la réforme des retraites de 2023 à compter du 1er septembre 2023 : « relèvement progressif de l'âge de départ » de 62 à 64 ans et 43 annuités. Les pensions baissent de « 20 % » et sont plafonnées au niveau de l'indemnité parlementaire. L'effort contributif reste « supérieur de 40 % au niveau de cotisation moyen des Français ». Décision votée à l'unanimité.",
  'Document officiel du Sénat.', 'primaire'))
AN_FICHE_DEPUTE_2026 = ('an_fiche_depute_2026', src('Fiche 7 : Situation matérielle du député (actualisée en janvier 2026)', 'Assemblée nationale', 'janvier 2026',
  'https://www.assemblee-nationale.fr/dyn/contenu/telechargement/631144/file/Fiche%207%20corrig%C3%A9e%20-%20Situation%20mat%C3%A9rielle%20du%20d%C3%A9put%C3%A9_actualis%C3%A9e%20080126.pdf',
  "L'indemnité du député est de 7 637,39 € brut et 5 953,34 € net (montants en vigueur depuis le 1er janvier 2024). Depuis le 1er janvier 2026, l'avance de frais est fusionnée dans une dotation de fonctionnement parlementaire de 7 238,04 € par mois en métropole. Crédit collaborateurs : 11 463 € par mois.",
  'Document officiel de l’Assemblée nationale.', 'primaire'))
PUBLICSENAT_REGIME_2023 = ('publicsenat_regime_2023', src('Réforme des retraites : comment fonctionne le régime des sénateurs ?', 'Public Sénat (Louis Mollier-Sabet)', '30 janvier 2023',
  'https://www.publicsenat.fr/article/parlementaire/reforme-des-retraites-comment-fonctionne-le-regime-des-senateurs-234504',
  "La caisse est autonome, créée en 1905. Les sénateurs cotisent à environ 15 %, contre 10 % pour les députés, et gardent un régime complémentaire que les députés n'ont plus. Les actifs couvrant les engagements de retraite atteignent 1,38 Md€ (comptes 2021). Le régime des députés a été aligné sur le régime général en 2018.",
  'Chaîne du Sénat.', 'media'))

FICHES.append(fiche(
 id='senateurs-privileges', affirmation="Les sénateurs ont des privilèges exorbitants.", volet='politique', sous_theme='Institutions françaises',
 mots_cles=['senateurs', 'privileges des senateurs', 'salaire des senateurs', 'retraite des senateurs', 'indemnite des senateurs', 'regime des senateurs', 'avance de frais de mandat'],
 verdict='trompeur', fiabilite='etabli',
 resume="Un sénateur touche la même indemnité brute qu'un député, 7 637,39 € par mois depuis 2024, plus une avance de frais de mandat de 6 600 € contrôlée. Le Sénat garde un régime de retraite spécifique, avec une caisse autonome et un régime complémentaire que les députés n'ont plus, mais il a baissé les pensions de 20 % en 2023 (environ 1 800 € net pour un mandat de six ans). « Exorbitants » relève de l'opinion ; des avantages spécifiques existent bel et bien.",
 contexte="Le Sénat est régulièrement accusé d'être un club de privilégiés, surtout lors des réformes des retraites.",
 explication="Il faut comparer l'indemnité, les frais et la retraite avec ceux des députés et vérifier les réformes récentes.",
 sources=[PUBLICSENAT_AFM_2024, PUBLICSENAT_RETRAITES_2023, SENAT_BUREAU_2023, AN_FICHE_DEPUTE_2026, PUBLICSENAT_REGIME_2023],
 faits=[
  fait("L'indemnité d'un sénateur est de 7 637,39 € brut par mois depuis le 1er janvier 2024, soit 5 676,12 € net avant impôt.", 'publicsenat_afm_2024', '2024', 'France', "C'est un revenu élevé, mais identique au brut des députés.", 'etabli', '7 637,39 €'),
  fait("L'indemnité brute d'un député est la même, 7 637,39 € par mois.", 'an_fiche_depute_2026', '2024-2026', 'France', "Les sénateurs ne sont pas mieux payés que les députés.", 'etabli'),
  fait("L'avance de frais de mandat des sénateurs est passée de 5 900 € à 6 600 € par mois fin 2023 ; les dépenses sont contrôlées par le comité de déontologie et des cabinets comptables.", 'publicsenat_afm_2024', '2023-2024', 'France', "Les frais ont augmenté mais sont encadrés.", 'etabli', '6 600 €'),
  fait("En 2023, le Sénat a relevé l'âge de départ de ses membres de 62 à 64 ans et baissé les pensions de 20 %, plafonnées au niveau de l'indemnité.", 'senat_bureau_2023', '2023', 'France', "Le régime a été réformé.", 'etabli', '20 %'),
  fait("Selon Public Sénat, la pension pour un mandat de six ans est passée d'environ 2 200 € à 1 800 € net par mois ; la pension moyenne citée en 2019 était d'environ 3 856 € net.", 'publicsenat_retraites_2023', '2019-2023', 'France', "Les pensions restent élevées par rapport à la moyenne : c'est un fait à reconnaître.", 'etabli'),
  fait("Le régime de retraite des sénateurs repose sur une caisse autonome et garde un régime complémentaire que les députés n'ont plus depuis leur alignement sur le régime général en 2018.", 'publicsenat_regime_2023', '2018-2023', 'France', "Un régime spécifique subsiste.", 'etabli'),
 ],
 court="Un sénateur gagne autant qu'un député au brut, 7 637 € par mois, et ses frais sont contrôlés. Son régime de retraite reste spécifique, mais il a été raboté de 20 % en 2023. Des avantages existent ; « exorbitants », c'est un jugement.",
 moyen="Les chiffres officiels : 7 637,39 € brut par mois, exactement comme un député, plus une avance de frais de 6 600 € contrôlée par le comité de déontologie. Ce sont des revenus élevés, mais pas des privilèges cachés.\n\nLe vrai point faible, c'est la retraite. Le Sénat garde sa caisse autonome et un régime complémentaire que les députés ont abandonné en 2018. Il a quand même baissé les pensions de 20 % en 2023 et relevé l'âge de départ à 64 ans : environ 1 800 € net pour un mandat de six ans. On peut demander l'alignement sur le régime général ; mais crier aux privilèges exorbitants sert souvent à discréditer le Parlement tout entier.",
 detaille="L'indemnité parlementaire est la même dans les deux chambres : 7 637,39 € brut par mois depuis le 1er janvier 2024, soit 5 676 € net avant impôt pour un sénateur. S'y ajoute une avance de frais de mandat, passée de 5 900 € à 6 600 € par mois fin 2023 au nom de l'inflation. Ces frais doivent être « raisonnables » et sont contrôlés par le comité de déontologie avec deux cabinets comptables, chaque sénateur faisant l'objet d'au moins un contrôle approfondi par mandat. Les députés disposent depuis 2026 d'une dotation de fonctionnement de 7 238 € par mois.\n\nLa retraite est le sujet le plus discutable. Le Sénat a une caisse autonome depuis 1905, avec un régime complémentaire que les députés ont perdu en 2018. Les sénateurs cotisent davantage, environ 15 %, et la caisse coûte moins de 8 M€ à l'État, contre 67 M€ pour celle des députés. En juillet 2023, le Bureau a transposé la réforme des retraites : départ à 64 ans, 43 annuités, pensions en baisse de 20 % et plafonnées. Une pension pour un mandat de six ans passe d'environ 2 200 € à 1 800 € net ; la pension moyenne citée en 2019 était d'environ 3 856 € net.\n\nIl y a donc des avantages réels, notamment un régime de retraite à part, que l'on peut vouloir aligner sur celui des Français. Mais la plupart des sources sont internes au Sénat, et le mot « exorbitants » relève du jugement. Le débat utile porte sur la transparence et l'alignement, pas sur le procès en bloc des élus.",
 empathie="Quand on demande aux Français de travailler jusqu'à 64 ans, il est normal de vouloir que les élus s'appliquent les mêmes règles. C'est une exigence démocratique saine.",
 legitimes=["Le régime de retraite des sénateurs reste spécifique.", "L'avance de frais a augmenté de 700 € par mois en 2023."],
 contre=[
  ("Ils touchent plus de 13 000 € par mois avec les frais.", "Les frais de mandat servent à payer des dépenses liées au mandat et sont contrôlés ; ils ne sont pas un salaire."),
  ("Le Sénat refuse l'alignement sur le régime général.", "C'est vrai : il a transposé la réforme de 2023 mais garde sa caisse ; on peut défendre l'alignement complet."),
 ],
 questions=["Savais-tu qu'un sénateur et un député touchent la même indemnité brute ?", "Faudrait-il aligner la retraite des parlementaires sur le régime général ?"],
 limites=["La plupart des sources sont internes au Sénat (Public Sénat, Bureau du Sénat) ; aucun fact-check indépendant n'a été lu.", "La pension moyenne de 3 856 € date de 2019, avant la réforme de 2023."],
 publics={'convaincus': "Un sénateur gagne 7 637 € brut par mois, exactement comme un député, et ses frais sont contrôlés. Sa retraite reste à part, d'accord, et on peut exiger qu'elle soit alignée ; mais elle a baissé de 20 % en 2023. Taper sur les élus en bloc, ça ne fait pas avancer la transparence.",
  'indecis': "Il est légitime de vouloir que les élus s'appliquent les règles qu'ils votent. Les sénateurs ont un régime de retraite spécifique, mais leur indemnité est la même que celle des députés et leurs frais sont contrôlés. Le débat utile porte sur l'alignement et la transparence."},
 a_actualiser='2027-01-31', raison="Revalorisation éventuelle des indemnités et des frais.",
))

# 13 ── Dette de Paris ─────────────────────────────────────────────────────
MONTAIGNE_PARIS_2020 = ('montaigne_paris_2020', src('Municipales 2020 – Paris', 'Institut Montaigne', 'janvier 2020 (données 2018)',
  'https://institutmontaigne.org/municipales-2020/paris',
  "Encours de dette de 4 179 M€ en 2014, puis 6 773 M€ en 2018, soit 3 039 € par habitant : « Afin de financer les investissements, la dette a fortement augmenté depuis 2014 (+ 62 %) ».",
  'Think tank libéral (orientation à signaler) ; données des comptes publics.', 'etude'))
MONTAIGNE_PARIS_2026 = ('montaigne_paris_2026', src('Bilan financier Paris (Municipales 2026 – Finances locales)', 'Institut Montaigne', '2026 (comptes 2024)',
  'https://institutmontaigne.org/municipales-2026-admin/api/download/city-financial/bilan-financier-paris-699dbde50a2a1861924076.pdf',
  "Selon le périmètre retenu par l'institut, l'encours atteint 10,6 Md€ en 2024 ; la dette par habitant passe de 1 837 € (2014) à 4 939 € (2024), contre 1 097 € en moyenne dans les villes de plus de 100 000 habitants. La durée de désendettement passe de 9,1 ans en 2014 à 38,3 ans en 2024 : « Cette capacité de désendettement est préoccupante. » La Ville conteste ces chiffres en invoquant un patrimoine de 47 Md€ et une autre méthode.",
  'Think tank libéral ; périmètre différent du budget général de la Ville.', 'etude'))
PARIS_CA_2025 = ('paris_ca_2025', src('Compte administratif 2025 – Rapport financier', 'Ville de Paris', '1er juillet 2026',
  'https://cdn.paris.fr/paris/2026/07/01/ca-2025-rapport-financier_-gk9Q.pdf',
  "Encours de dette au 31 décembre : 8 700,5 M€ en 2024 et 9 377,8 M€ en 2025 (+7,8 %). Épargne brute : 266,9 M€ en 2024 puis 800,1 M€ en 2025. Durée de désendettement : 32,6 ans en 2024, 11,7 ans en 2025, avec l'objectif de la « maintenir en deçà de 12 ans ».",
  "Document officiel, mais auto-présentation de l'exécutif municipal.", 'primaire'))
CLUBJURISTES_PARIS_2022 = ('clubjuristes_paris_2022', src('La Ville de Paris peut-elle être mise sous tutelle budgétaire pour mauvaise gestion ?', 'Le Club des juristes (Aurélien Baudu, professeur à l’Université de Lille)', '12 décembre 2022',
  'https://www.leclubdesjuristes.com/justice/la-ville-de-paris-peut-elle-etre-mise-sous-tutelle-budgetaire-pour-mauvaise-gestion-654/',
  "« Aucune disposition législative ou constitutionnelle ne limite le niveau d'endettement des collectivités territoriales. » La dette seule ne justifie pas une tutelle tant que la règle d'or est respectée. La chambre régionale des comptes relevait déjà une épargne faible et des marges réduites. Sur les loyers capitalisés : « L'insincérité budgétaire ne semble donc pas être manifeste même si la pratique est discutable. »",
  'Analyse universitaire.', 'etude'))
AN_QE_1311 = ('an_qe_1311', src('Question écrite n° 1311 et réponse du Gouvernement', 'Assemblée nationale', 'réponse publiée au JO le 28 février 2023',
  'https://www.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE1311.pdf',
  "Le Gouvernement répond que « le niveau d'endettement » seul ne rend pas une collectivité « en faillite », tant qu'elle peut rembourser ses emprunts sur ses ressources propres.",
  'Réponse ministérielle officielle.', 'primaire'))

FICHES.append(fiche(
 id='paris-dette-gestion', affirmation="Paris est ruinée par la gestion de la gauche, sa dette a explosé.", volet='economie', sous_theme='Dette publique',
 mots_cles=['dette de paris', 'paris ruinee', 'hidalgo dette', 'ville de paris dette', 'gestion de paris', 'paris endettee', 'faillite de paris'],
 verdict='trompeur', fiabilite='etabli',
 resume="La dette de Paris a réellement beaucoup augmenté : 4,2 Md€ en 2014, 8,7 Md€ fin 2024 et 9,4 Md€ fin 2025 selon la Ville. La dette par habitant est environ quatre fois la moyenne des grandes villes selon l'Institut Montaigne, et la capacité de désendettement s'est fortement dégradée en 2024. Mais Paris n'est pas « ruinée » : aucune loi ne plafonne la dette locale, une collectivité qui rembourse n'est pas en faillite, et l'épargne brute est remontée en 2025.",
 contexte="La dette de Paris est un thème central des critiques contre Anne Hidalgo et la gauche parisienne.",
 explication="Il faut distinguer l'ampleur de la hausse, qui est réelle, et la notion de « ruine », qui a un sens précis pour une collectivité.",
 sources=[MONTAIGNE_PARIS_2020, MONTAIGNE_PARIS_2026, PARIS_CA_2025, CLUBJURISTES_PARIS_2022, AN_QE_1311],
 faits=[
  fait("Selon l'Institut Montaigne, la dette de Paris était de 4 179 M€ en 2014 et avait augmenté de 62 % dès 2018 pour financer les investissements.", 'montaigne_paris_2020', '2014-2018', 'Paris', "La hausse a commencé tôt dans le mandat.", 'etabli', '4 179 M€'),
  fait("Selon la Ville de Paris, l'encours de dette atteint 8 700,5 M€ fin 2024 et 9 377,8 M€ fin 2025.", 'paris_ca_2025', '2024-2025', 'Paris', "La dette a plus que doublé depuis 2014 : c'est un fait défavorable à la majorité de gauche.", 'etabli', '9 377,8 M€'),
  fait("Selon l'Institut Montaigne, la dette par habitant est de 4 939 € en 2024, contre 1 097 € en moyenne dans les villes de plus de 100 000 habitants.", 'montaigne_paris_2026', '2024', 'Paris', "Paris est de loin la grande ville la plus endettée par habitant.", 'estimation', '4 939 €'),
  fait("La Ville indique une durée de désendettement de 32,6 ans en 2024, ramenée à 11,7 ans en 2025 grâce à une épargne brute passée de 266,9 M€ à 800,1 M€.", 'paris_ca_2025', '2024-2025', 'Paris', "La situation s'est fortement dégradée en 2024 puis redressée en 2025, selon la Ville.", 'etabli'),
  fait("Selon un professeur de droit public, aucune disposition législative ou constitutionnelle ne limite le niveau d'endettement des collectivités territoriales.", 'clubjuristes_paris_2022', '2022', 'France', "Une dette élevée n'est pas une faillite tant que la collectivité rembourse.", 'etabli'),
  fait("Le Gouvernement a répondu en 2023 que le niveau d'endettement seul ne rend pas une collectivité « en faillite », tant qu'elle peut rembourser ses emprunts sur ses ressources propres.", 'an_qe_1311', '2023', 'France', "La notion de ruine ne s'applique pas à Paris.", 'etabli'),
 ],
 court="La dette de Paris a vraiment explosé : de 4,2 milliards en 2014 à 9,4 milliards fin 2025, et environ quatre fois la moyenne des grandes villes par habitant. Mais Paris n'est pas ruinée : elle rembourse, son épargne est remontée en 2025, et une dette d'investissement n'est pas une faillite.",
 moyen="Il faut le reconnaître : la dette de la Ville de Paris a plus que doublé depuis 2014, de 4,2 à 9,4 milliards d'euros selon ses propres comptes. Par habitant, elle est environ quatre fois supérieure à la moyenne des grandes villes selon l'Institut Montaigne, et la capacité de désendettement s'est fortement dégradée en 2024.\n\nMais « ruinée » est faux. Aucune loi ne plafonne la dette d'une collectivité ; une ville qui rembourse ses emprunts n'est pas en faillite, rappelait le Gouvernement en 2023. Selon la Ville, l'épargne brute a triplé en 2025 et la durée de désendettement est revenue à 11,7 ans. Cette dette a financé des investissements, notamment du logement social, qu'on peut juger utiles ou non : c'est un débat politique, pas une faillite.",
 detaille="Les chiffres de la hausse ne font pas débat. Selon l'Institut Montaigne, l'encours de la Ville était de 4 179 M€ en 2014 et avait déjà augmenté de 62 % en 2018. Selon les comptes de la Ville elle-même, il atteint 8 700 M€ fin 2024 et 9 378 M€ fin 2025. L'Institut Montaigne, avec un périmètre plus large (10,6 Md€), calcule une dette de 4 939 € par habitant, contre 1 097 € en moyenne dans les villes de plus de 100 000 habitants, et juge la capacité de désendettement « préoccupante ».\n\nLa dégradation de 2024 est nette : selon la Ville, il aurait fallu 32,6 ans d'épargne pour rembourser la dette. En 2025, l'épargne brute est passée de 267 M€ à 800 M€ et cette durée est revenue à 11,7 ans, sous l'objectif de 12 ans que la Ville s'est fixé. Ces chiffres sont présentés par l'exécutif municipal et méritent d'être confrontés au rapport de la chambre régionale des comptes.\n\nLe mot « ruinée » ne correspond pas à la réalité juridique. Selon un professeur de droit public, aucune disposition ne plafonne l'endettement des collectivités ; le Gouvernement rappelle qu'une collectivité qui peut rembourser n'est pas en faillite. La question politique demeure : cette dette a-t-elle financé des investissements utiles, comme le logement social, ou des dépenses mal maîtrisées ? Les Parisiens en jugent par leur vote.",
 empathie="Voir la dette d'une ville doubler inquiète légitimement, surtout quand on y paie ses impôts. On peut critiquer cette gestion sans exagérer la situation.",
 legitimes=["La dette de Paris a plus que doublé depuis 2014.", "La dette par habitant est bien supérieure à celle des autres grandes villes."],
 contre=[
  ("La chambre régionale des comptes a alerté.", "Des contrôles ont relevé une épargne faible et une situation dégradée ; c'est une critique sérieuse, mais elle ne parle pas de faillite."),
  ("La Ville arrange ses chiffres.", "Les comptes de la Ville sont son auto-présentation ; ils concordent cependant avec la hausse décrite par l'Institut Montaigne."),
 ],
 questions=["Sais-tu qu'une collectivité qui rembourse ses emprunts ne peut pas être en faillite ?", "Qu'est-ce que cette dette a financé, selon toi : des logements, des équipements, du fonctionnement ?"],
 limites=["Le rapport de la chambre régionale des comptes d'Île-de-France de 2025 n'a pas été lu directement.", "Les montants varient selon le périmètre retenu (8,7 ou 10,6 Md€ pour 2024).", "Le chiffre de 2014 (Institut Montaigne) et ceux de 2024-2025 (Ville) viennent de sources différentes."],
 publics={'convaincus': "La dette de Paris a doublé depuis 2014, je ne le conteste pas, et on peut critiquer cette gestion. Mais ruinée, non : aucune loi ne plafonne la dette d'une ville, et une collectivité qui rembourse n'est pas en faillite. En 2025, selon la Ville, son épargne a triplé.",
  'indecis': "La forte hausse de la dette parisienne est réelle et mérite des comptes. Mais elle a servi en partie à investir, et la Ville rembourse ses emprunts. Le débat porte sur les choix d'investissement, pas sur une faillite."},
 a_actualiser='2027-07-31', raison="Compte administratif 2026 de la Ville de Paris.",
))

# 14 ── Agressions d'élus locaux ───────────────────────────────────────────
CALAE_2025 = ('calae_2025', src("Rapport d'activité 2023-2025 du centre d'analyse et de lutte contre les atteintes aux élus (CALAE)", "Ministère de l'Intérieur (publié sur Vie publique)", '31 mars 2025',
  'https://www.vie-publique.fr/files/rapport/pdf/298691.pdf',
  "2 759 procédures en 2023 (+13,54 % par rapport à 2022), puis 2 501 en 2024 (-9,35 %). « La majorité des atteintes envers les élus concerne les menaces et outrages. » 250 atteintes physiques en 2024. « Les maires représentent 62 % des victimes en 2023 et 64 % des victimes en 2024. »",
  'Rapport officiel du ministère.', 'primaire'))
MAIREINFO_ELUS_2026 = ('maireinfo_elus_2026', src("Les agressions d'élus en 2025, à un niveau équivalent à celui de l'année 2024", 'Maire-info (Association des maires de France)', '1er juillet 2026',
  "https://www.maire-info.com//les-agressions-d'elus-en-2025-à-un-niveau-equivalent-à-celui-de-l'annee-2024-article2-30946",
  "2 478 faits en 2025, soit -0,9 % par rapport aux 2 501 de 2024. Les menaces ou outrages représentent 68 % des faits ; 27 % des atteintes passent par voie numérique ; les maires représentent 65 % des victimes. Le ministre de l'Intérieur évoque une violence « de plus en plus décomplexée ».",
  "Média de l'association des maires.", 'media'))
PUBLICSENAT_ELUS_2026 = ('publicsenat_elus_2026', src("Agressions d'élus : déjà plus de 1500 cas recensés cette année", 'Public Sénat (Guillaume Jacquot)', '13 mai 2026',
  'https://www.publicsenat.fr/actualites/territoires/agressions-delus-deja-plus-de-1500-cas-recenses-cette-annee-en-hausse-par-rapport-a-2024-et-2025',
  "Le ministre recense plus de 1 500 cas au 13 mai 2026, contre environ 2 500 pour chacune des années 2024 et 2025 : « C'est presque la moitié par rapport à 2025 » ; « La trajectoire est loin de s'améliorer. »",
  'Média parlementaire public.', 'media'))
AN_PPL_ELUS_2024 = ('an_ppl_elus_2024', src('Proposition de loi n° 1713 relative à la sécurité des élus locaux et à la protection des maires (document de la rapporteure)', 'Assemblée nationale, commission des lois (rapporteure Violette Spillebout)', '30 janvier 2024',
  'https://www.assemblee-nationale.fr/dyn/media/16/organes/commissions-permanentes-legislatives/lois/eat-2024/eat-ppl-n-1713-securite-des-elus-locaux-et-protection-des-maires',
  "2 265 faits en 2022, « une augmentation de 32 % par rapport à l'année précédente ». Les menaces représentent 26 % et les outrages 41 % ; les violences physiques moins de 5 %. Enquête Cevipof pour l'AMF (novembre 2023) : 69 % des maires déclarent des incivilités et 7 % des violences physiques.",
  'Document parlementaire.', 'primaire'))
LOCALTIS_LOI_ELUS_2024 = ('localtis_loi_elus_2024', src('La loi renforçant la sécurité des élus locaux a été publiée', 'Localtis / Banque des Territoires (Thomas Beurey)', '22 mars 2024',
  'https://www.banquedesterritoires.fr/la-loi-renforcant-la-securite-des-elus-locaux-ete-publiee',
  "La loi n° 2024-247 du 21 mars 2024 durcit les peines, fait du harcèlement une circonstance aggravante, rend la protection fonctionnelle automatique pour les élus exécutifs et l'étend aux candidats, et rend systématique l'information du maire sur les suites judiciaires.",
  'Média spécialisé des collectivités.', 'media'))

FICHES.append(fiche(
 id='agressions-elus-locaux', affirmation="Les agressions d'élus locaux explosent.", volet='securite', sous_theme='Violences',
 mots_cles=['agressions d elus', 'elus agresses', 'maires agresses', 'violences contre les maires', 'atteintes aux elus', 'menaces contre les elus', 'securite des elus'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="Les atteintes aux élus ont fortement augmenté entre 2021 et 2023 (+32 % en 2022, 2 759 faits en 2023), puis ont reculé en 2024 (2 501) et se sont stabilisées en 2025 (2 478) à un niveau élevé. L'année 2026, marquée par les municipales, repart à la hausse (plus de 1 500 cas au 13 mai). Il s'agit surtout de menaces et d'outrages (68 %) ; les violences physiques sont minoritaires (250 en 2024). Les maires représentent près des deux tiers des victimes.",
 contexte="Plusieurs agressions de maires très médiatisées ont conduit à une loi en 2024 et à un plan national de protection.",
 explication="Il faut suivre l'évolution année par année et distinguer menaces, outrages et violences physiques.",
 sources=[CALAE_2025, MAIREINFO_ELUS_2026, PUBLICSENAT_ELUS_2026, AN_PPL_ELUS_2024, LOCALTIS_LOI_ELUS_2024],
 faits=[
  fait("Selon l'Assemblée nationale, 2 265 atteintes aux élus ont été recensées en 2022, en hausse de 32 % sur un an ; les violences physiques représentaient moins de 5 % des faits.", 'an_ppl_elus_2024', '2021-2022', 'France', "La hausse a été très forte au début des années 2020.", 'etabli', '+32 %'),
  fait("Le ministère de l'Intérieur a recensé 2 759 procédures en 2023 (+13,5 %), puis 2 501 en 2024 (-9,35 %), dont 250 atteintes physiques.", 'calae_2025', '2023-2024', 'France', "Après le pic de 2023, les faits ont reculé en 2024.", 'etabli', '2 501'),
  fait("D'après Maire-info, 2 478 faits ont été recensés en 2025 (-0,9 %), dont 68 % de menaces ou d'outrages ; les maires représentent 65 % des victimes.", 'maireinfo_elus_2026', '2025', 'France', "Le niveau reste élevé mais stable.", 'etabli', '2 478'),
  fait("Selon le ministre de l'Intérieur, plus de 1 500 cas étaient déjà recensés au 13 mai 2026, année des élections municipales.", 'publicsenat_elus_2026', '2026', 'France', "La tendance repart à la hausse en 2026.", 'etabli', '1 500'),
  fait("La loi du 21 mars 2024 a durci les peines et rendu automatique la protection fonctionnelle des maires et adjoints.", 'localtis_loi_elus_2024', '2024', 'France', "Le législateur a réagi à la hausse des violences.", 'etabli'),
 ],
 court="En partie : les atteintes aux élus ont bondi de 2021 à 2023, puis reculé en 2024 et stagné en 2025, autour de 2 500 faits par an. 2026, année de municipales, repart à la hausse. Ce sont surtout des menaces et des outrages ; les violences physiques restent minoritaires mais réelles.",
 moyen="La hausse a été réelle et forte : +32 % en 2022, puis 2 759 faits en 2023 selon le ministère de l'Intérieur. Elle a reculé en 2024 (2 501) et s'est stabilisée en 2025 (2 478). En 2026, année de municipales, plus de 1 500 cas étaient déjà recensés mi-mai.\n\nLa majorité des faits sont des menaces et des outrages, souvent en ligne ; on compte 250 atteintes physiques en 2024. Les maires représentent près des deux tiers des victimes. Une loi de 2024 a renforcé leur protection. « Explosent » est exagéré pour 2024-2025, mais le niveau reste inquiétant : quand on menace les élus de proximité, c'est la démocratie locale qu'on fragilise.",
 detaille="Les chiffres viennent du ministère de l'Intérieur. En 2022, 2 265 atteintes aux élus ont été recensées, en hausse de 32 % sur un an ; en 2023, 2 759, encore +13,5 %. C'est la période de forte hausse, qui a conduit à un plan national en 2023 et à la loi du 21 mars 2024 : peines alourdies, harcèlement comme circonstance aggravante, protection fonctionnelle automatique pour les élus exécutifs.\n\nEnsuite, les faits ont reculé en 2024 (2 501, -9,35 %) puis se sont stabilisés en 2025 (2 478). Une partie de la hausse initiale peut aussi s'expliquer par un meilleur recensement, avec la création d'un centre d'analyse dédié en 2023. En 2026, année des municipales, le ministre recensait plus de 1 500 cas dès le 13 mai et jugeait que « la trajectoire est loin de s'améliorer ».\n\nLa nature des faits compte : les menaces et outrages représentent 68 % des atteintes en 2025, et 27 % passent par voie numérique. Les violences physiques sont minoritaires, 250 en 2024. Les maires sont les premières victimes, à 65 %. Selon une enquête du Cevipof pour l'AMF, 7 % des maires déclaraient des violences physiques. Les élus locaux, souvent bénévoles ou presque, tiennent la démocratie de proximité : les protéger est une exigence républicaine.",
 empathie="Les agressions de maires choquent, parce que ce sont les élus les plus proches et souvent les plus dévoués. L'inquiétude est fondée ; les chiffres permettent de la mesurer.",
 legitimes=["Les atteintes ont fortement augmenté entre 2021 et 2023.", "2026 repart à la hausse en période électorale."],
 contre=[
  ("Les chiffres officiels sous-estiment la réalité.", "C'est possible, toutes les atteintes ne donnent pas lieu à une procédure ; mais la tendance mesurée est la même source d'une année sur l'autre."),
  ("C'est la faute de l'immigration.", "Les sources lues ne donnent aucune information sur les auteurs ; les menaces passent souvent par les réseaux sociaux."),
 ],
 questions=["Savais-tu que les atteintes aux élus ont reculé en 2024 avant de repartir en 2026 ?", "Qu'est-ce qui pourrait mieux protéger les maires, selon toi ?"],
 limites=["Les chiffres 2026 sont partiels (au 13 mai).", "Une partie de la hausse de 2022-2023 peut refléter un meilleur recensement.", "Aucune source lue ne décrit le profil des auteurs."],
 publics={'convaincus': "Les agressions d'élus ont vraiment bondi entre 2021 et 2023, et 2026 repart à la hausse : c'est grave. Mais en 2024 et 2025, les faits ont baissé puis stagné autour de 2 500 par an, surtout des menaces et des outrages. Protéger les maires, c'est défendre la démocratie, pas désigner un bouc émissaire.",
  'indecis': "Les violences et menaces contre les élus locaux sont une réalité préoccupante, surtout pour les maires. Après une forte hausse jusqu'en 2023, elles se sont stabilisées à un niveau élevé, et repartent en 2026. Une loi de 2024 a renforcé leur protection."},
 a_actualiser='2027-07-31', raison="Bilan 2026 des atteintes aux élus.",
))

# 15 ── RN et droits des homosexuels ───────────────────────────────────────
LCP_MARIAGE_10ANS = ('lcp_mariage_10ans', src('Mariage pour tous : la loi « ouvrant le mariage aux couples de personnes de même sexe » a dix ans', 'LCP (Léonard Dermarkarian)', '23 avril 2023',
  'https://lcp.fr/actualites/mariage-pour-tous-la-loi-ouvrant-le-mariage-aux-couples-de-personnes-de-meme-sexe-a-dix',
  "Le 23 avril 2013, l'Assemblée a adopté la loi par 331 voix contre 225 et 10 abstentions, après « 136 heures et 56 minutes » de débats ; elle a été promulguée le 17 mai 2013. Selon l'Insee, environ 70 000 mariages de même sexe ont été célébrés en dix ans. « Aucun responsable politique de premier plan n'affiche plus la volonté de revenir en arrière. » Gérald Darmanin, qui avait voté contre : « Je me suis trompé ».",
  'Chaîne parlementaire.', 'media'))
PINKNEWS_LEPEN_2017 = ('pinknews_lepen_2017', src("France's Marine Le Pen quietly pledges to end same-sex marriage", 'PinkNews (Nick Duffy)', '14 février 2017',
  'https://thepinknews.com/2017/02/14/frances-marine-le-pen-quietly-pledges-to-end-same-sex-marriage',
  "L'engagement 87 du programme présidentiel de 2017 propose une union civile « améliorée » pour remplacer la loi de 2013, sans effet rétroactif sur les mariages déjà célébrés.",
  'Média LGBT britannique (engagé) ; programme original non lu.', 'media'))
PUBLICSENAT_RN_PMA_2019 = ('publicsenat_rn_pma_2019', src('Le RN, hostile à la PMA pour toutes, réclame un référendum', 'Public Sénat', '24 juillet 2019',
  'https://www.publicsenat.fr/actualites/politique/le-rn-hostile-a-la-pma-pour-toutes-reclame-un-referendum-144625',
  "Jordan Bardella invoque le « droit de l'enfant à avoir à la fois un père et une mère » et déclare : « Nous serons évidemment opposés à la PMA et à la GPA ».",
  'Média parlementaire public.', 'media'))
QDM_PMA_2019 = ('qdm_pma_2019', src("L'Assemblée nationale valide le projet de loi de bioéthique et la PMA… dans la division", 'Le Quotidien du Médecin (Arnaud Janin)', '17 octobre 2019',
  'https://www.lequotidiendumedecin.fr/sante-societe/politique-de-sante/lassemblee-nationale-valide-le-projet-de-loi-de-bioethique-et-la-pma-dans-la-division',
  "Le texte est adopté en première lecture par 359 voix pour, 114 contre et 72 abstentions. Sur 8 députés RN, 2 s'abstiennent et les autres votent contre. LFI vote pour (une abstention) ; le PS est majoritairement pour (2 contre et 3 abstentions sur 29) ; LR : 75 contre, 12 pour, 15 abstentions.",
  'Presse professionnelle sérieuse ; vote de première lecture (2019).', 'media'))
LCP_CONVERSION_2022 = ('lcp_conversion_2022', src('Lutte contre les « thérapies de conversion » : la proposition de loi définitivement adoptée', 'LCP (Soizic Bonvarlet)', '25 janvier 2022',
  'https://lcp.fr/actualites/lutte-contre-les-therapies-de-conversion-la-proposition-de-loi-definitivement-adoptee',
  "Adoption définitive à l'unanimité, par 142 voix pour et 0 contre. Bastien Lachaud (LFI) déclare : « Il n'y a rien à guérir ».",
  'Chaîne parlementaire.', 'media'))
DATAN_CONVERSION_2021 = ('datan_conversion_2021', src('Vote n° 3979 (15e législature) : interdiction des pratiques visant à modifier l’orientation sexuelle, première lecture', 'Datan, d’après les données ouvertes de l’Assemblée nationale', '5 octobre 2021',
  'https://datan.fr/votes/legislature-15/vote_3979',
  "115 pour, 0 contre, 3 abstentions. LFI 4 pour, PS 8 pour, GDR 3 pour, LR 17 pour et 1 abstention. Parmi les non-inscrits, Sébastien Chenu (RN) vote pour.",
  'Site de données parlementaires (données officielles mises en forme).', 'secondaire'))
LCP_REPARATION_2024 = ('lcp_reparation_2024', src("Condamnations pour homosexualité entre 1942 et 1982 : l'Assemblée nationale approuve à l'unanimité", 'LCP (Raphaël Marchal)', '7 mars 2024',
  'https://lcp.fr/actualites/condamnations-pour-homosexualite-entre-1942-et-1982-l-assemblee-nationale-approuve-a-l',
  "Le texte de réparation, porté par le socialiste Hervé Saulignac, est adopté à l'unanimité, avec les voix des élus LR et RN.",
  'Chaîne parlementaire.', 'media'))
INEGALITES_ANTILGBT_2025 = ('inegalites_antilgbt_2025', src('Le nombre de crimes et délits anti-LGBT', 'Observatoire des inégalités', '9 octobre 2025',
  'https://inegalites.fr/nombre-crimes-delits-anti-LGBT',
  "3 055 crimes et délits anti-LGBT ont été enregistrés en 2024, un nombre « trois fois supérieur à celui de 2016 ». « Il faut interpréter cette hausse avec prudence » : elle peut aussi refléter davantage de plaintes.",
  'Association indépendante, à partir des données du ministère de l’Intérieur.', 'secondaire'))

FICHES.append(fiche(
 id='rn-homosexuels-droits', affirmation="Le RN défend mieux les homosexuels que la gauche.", volet='droits', sous_theme='Droits des personnes LGBT',
 mots_cles=['rn homosexuels', 'rn et les homosexuels', 'rn gays', 'rn lgbt', 'le pen mariage pour tous', 'homosexuels votent rn', 'rn protege les homosexuels'],
 verdict='contredit', fiabilite='etabli',
 resume="Sur les droits qui ont fait débat, le FN puis le RN se sont opposés à ce que la gauche portait : en 2017, le programme de Marine Le Pen prévoyait de remplacer le mariage pour tous par une union civile ; en 2019, le RN s'est opposé à la PMA pour toutes, que la gauche a votée. Le RN a voté des textes consensuels : l'interdiction des thérapies de conversion (adoptée à l'unanimité) et la réparation des condamnations pour homosexualité, portée par un socialiste. L'argument repose surtout sur l'idée que le RN protégerait les homosexuels de l'islamisme, ce qui n'est pas un bilan législatif.",
 contexte="Le RN met en avant des personnalités homosexuelles et se présente comme protecteur des minorités sexuelles face à l'islamisme.",
 explication="Le plus simple est de comparer les votes et les programmes sur les textes qui ont étendu les droits des personnes LGBT.",
 sources=[LCP_MARIAGE_10ANS, PINKNEWS_LEPEN_2017, PUBLICSENAT_RN_PMA_2019, QDM_PMA_2019, DATAN_CONVERSION_2021, LCP_CONVERSION_2022, LCP_REPARATION_2024, INEGALITES_ANTILGBT_2025],
 faits=[
  fait("La loi ouvrant le mariage aux couples de même sexe a été adoptée le 23 avril 2013 par 331 voix contre 225, sur un texte du gouvernement de gauche.", 'lcp_mariage_10ans', '2013', 'France', "Le mariage pour tous est une loi portée par la gauche.", 'etabli'),
  fait("Selon PinkNews, le programme présidentiel de Marine Le Pen en 2017 proposait de remplacer le mariage pour tous par une union civile « améliorée », sans effet rétroactif.", 'pinknews_lepen_2017', '2017', 'France', "Le RN voulait revenir sur le mariage pour tous.", 'estimation'),
  fait("En 2019, Jordan Bardella a déclaré : « Nous serons évidemment opposés à la PMA et à la GPA ».", 'publicsenat_rn_pma_2019', '2019', 'France', "Le RN s'est opposé à la PMA pour les couples de femmes.", 'etabli'),
  fait("D'après Le Quotidien du Médecin, en première lecture de la loi de bioéthique en 2019, les députés RN ont voté contre ou se sont abstenus, tandis que LFI et la grande majorité du PS ont voté pour.", 'qdm_pma_2019', '2019', 'France', "Sur la PMA pour toutes, la gauche a voté pour et le RN contre.", 'etabli'),
  fait("Selon Datan, l'interdiction des thérapies de conversion a été adoptée en première lecture par 115 voix contre 0, avec le vote favorable du député RN Sébastien Chenu.", 'datan_conversion_2021', '2021', 'France', "Le RN a voté ce texte consensuel : c'est un fait à reconnaître.", 'etabli'),
  fait("En mars 2024, la réparation des condamnations pour homosexualité entre 1942 et 1982, portée par le socialiste Hervé Saulignac, a été adoptée à l'unanimité, RN compris.", 'lcp_reparation_2024', '2024', 'France', "Les textes votés par tous sont souvent nés à gauche.", 'etabli'),
  fait("Selon l'Observatoire des inégalités, 3 055 crimes et délits anti-LGBT ont été enregistrés en 2024, trois fois plus qu'en 2016.", 'inegalites_antilgbt_2025', '2016-2024', 'France', "Les violences anti-LGBT restent un problème majeur, à interpréter avec prudence.", 'estimation', '3 055'),
 ],
 court="Faux sur les faits : le mariage pour tous et la PMA pour toutes ont été portés par la gauche, et le FN-RN s'y est opposé, jusqu'à vouloir remplacer le mariage par une union civile en 2017. Le RN a voté des textes consensuels, comme l'interdiction des thérapies de conversion, mais ce n'est pas lui qui a fait avancer les droits.",
 moyen="Regardons les votes. Le mariage pour tous a été adopté en 2013 sous un gouvernement de gauche. En 2017, Marine Le Pen proposait de le remplacer par une union civile. En 2019, Jordan Bardella annonçait que le RN s'opposerait à la PMA pour toutes, et ses députés ont voté contre ou se sont abstenus, quand LFI et le PS votaient pour.\n\nIl est juste de reconnaître que le RN a voté l'interdiction des thérapies de conversion et la réparation des condamnations pour homosexualité, deux textes adoptés à l'unanimité, le second porté par un socialiste. Mais se dire protecteur des homosexuels face à l'islamisme ne remplace pas un bilan : sur les droits qui ont divisé, le RN était de l'autre côté.",
 detaille="Les droits des personnes LGBT se sont construits par des lois, et les votes sont publics. Le mariage pour tous a été adopté le 23 avril 2013 par 331 voix contre 225, après plus de 136 heures de débats, sur un projet du gouvernement de gauche. En 2017, selon PinkNews, l'engagement 87 du programme de Marine Le Pen prévoyait de le remplacer par une union civile « améliorée », sans toucher aux mariages déjà célébrés. Dix ans après la loi, plus aucun responsable de premier plan ne propose de revenir en arrière, signe que la société l'a adoptée.\n\nSur la PMA pour les couples de femmes et les femmes seules, Jordan Bardella déclarait en 2019 : « Nous serons évidemment opposés à la PMA et à la GPA ». En première lecture, les huit députés RN ont voté contre ou se sont abstenus ; LFI et la quasi-totalité du PS ont voté pour.\n\nLe RN a voté des textes consensuels. Sébastien Chenu a voté l'interdiction des thérapies de conversion en 2021, adoptée définitivement à l'unanimité en 2022. En 2024, le RN a voté la réparation des condamnations pour homosexualité entre 1942 et 1982, sur un texte du socialiste Hervé Saulignac. Les crimes et délits anti-LGBT enregistrés ont triplé depuis 2016 selon l'Observatoire des inégalités : protéger les personnes LGBT, c'est défendre leurs droits contre toutes les haines, pas seulement contre celles qu'on attribue aux autres.",
 empathie="Des personnes homosexuelles peuvent se sentir menacées par l'homophobie, y compris religieuse, et chercher un parti qui les protège. Cette peur est légitime ; les votes permettent de voir qui a défendu leurs droits.",
 legitimes=["Le RN a voté l'interdiction des thérapies de conversion et la réparation des condamnations pour homosexualité.", "Plus aucun responsable de premier plan ne veut abroger le mariage pour tous."],
 contre=[
  ("Le RN ne veut plus abroger le mariage pour tous.", "C'est vrai que la question n'est plus mise en avant ; mais en 2017 il proposait de le remplacer, et il s'est opposé à la PMA pour toutes."),
  ("La gauche ferme les yeux sur l'homophobie dans certains quartiers.", "La lutte contre l'homophobie doit viser toutes ses formes ; les lois qui ont protégé les personnes LGBT ont été portées ou votées par la gauche."),
 ],
 questions=["Savais-tu qu'en 2017 le programme de Marine Le Pen prévoyait de remplacer le mariage pour tous par une union civile ?", "Pour juger qui défend les homosexuels, regardes-tu les discours ou les votes ?"],
 limites=["Le vote des deux députés FN sur le mariage pour tous en 2013 n'a pas été vérifié sur une page lue.", "Le vote définitif de la PMA en 2021 groupe par groupe n'a pas été lu ; la fiche s'appuie sur la première lecture de 2019.", "Le programme de 2017 est cité à travers PinkNews, média engagé."],
 publics={'convaincus': "Regarde les votes : le mariage pour tous et la PMA pour toutes ont été portés par la gauche, et le RN s'y est opposé ; en 2017, Marine Le Pen voulait remplacer le mariage par une union civile. Le RN a voté des textes consensuels, c'est vrai. Mais se dire protecteur des homosexuels ne remplace pas les votes sur leurs droits.",
  'indecis': "La peur de l'homophobie est légitime, d'où qu'elle vienne. Sur les grandes lois, mariage et PMA, la gauche a voté pour et le RN contre ; sur des textes consensuels, tout le monde a voté ensemble. Les votes publics sont le meilleur repère."},
 a_actualiser='2027-06-30', raison="Programmes de la présidentielle 2027.",
))

# ══ Lot D : désinformation et société ══════════════════════════════════════

# 16 ── Chemtrails ─────────────────────────────────────────────────────────
UCI_CHEMTRAILS_2016 = ('uci_chemtrails_2016', src('Surveyed scientists debunk chemtrails conspiracy theory', 'University of California, Irvine (UCI News)', '12 août 2016',
  'https://news.uci.edu/2016/08/12/surveyed-scientists-debunk-chemtrails-conspiracy-theory',
  "L'étude a interrogé 77 chimistes de l'atmosphère et géochimistes : 76 disent n'avoir jamais rencontré de preuve d'un programme d'épandage secret à grande échelle. Steven Davis : « The chemtrails conspiracy theory maps pretty closely to the origin and growth of the internet ». Ken Caldeira : « Contrails are becoming more abundant as air travel expands. »",
  'Communiqué universitaire sur une étude publiée dans une revue à comité de lecture.', 'etude'))
IOP_CHEMTRAILS_2016 = ('iop_chemtrails_2016', src('« Chemtrails » not real, say leading atmospheric science experts', 'IOP Publishing (éditeur de la revue Environmental Research Letters)', '12 août 2016',
  'https://ioppublishing.org/news/chemtrails-not-real-say-leading-atmospheric-science-experts/',
  "Les 77 experts sont des spécialistes des traînées de condensation et des géochimistes des dépôts atmosphériques ; 76 n'ont trouvé aucune preuve d'un programme secret. Les « preuves » avancées s'expliquent par la formation normale des traînées et par un échantillonnage de mauvaise qualité. Un sondage international de 2011 trouvait près de 17 % de personnes jugeant le programme secret « vrai ou en partie vrai ».",
  "Éditeur scientifique de l'étude.", 'etude'))
AN_QE_42050 = ('an_qe_42050', src('Question écrite n° 42050 et réponse du ministère de l’Écologie', 'Assemblée nationale (Journal officiel)', 'réponse publiée le 29 avril 2014',
  'https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE42050.pdf',
  "Les traînées « correspondent à une condensation de l'eau de l'atmosphère en cristaux autour des émissions normales de l'avion » ; leur formation « dépend peu de l'altitude de l'avion mais bien des conditions atmosphériques et de la météorologie ». « Elles ne sont pas nocives pour la santé et aucun élément ne contredit à ce jour cet état de fait. » L'enjeu identifié est leur contribution à l'effet de serre.",
  'Réponse ministérielle officielle ; donnée ancienne (2014).', 'primaire'))
AN_QE_31101 = ('an_qe_31101', src('Question écrite n° 31101 et réponse du ministère de l’Écologie', 'Assemblée nationale (Journal officiel)', 'réponse publiée le 3 septembre 2013',
  'https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE31101.pdf',
  "La question portait sur de prétendus « aviocirrus ». Réponse : « Il a été demandé à Météo France d'examiner ces réflexions » et « Météo France n'a pu mettre en évidence le phénomène tel que décrit. » Une reconnaissance par l'Organisation météorologique mondiale « ne peut se fonder que sur des critères scientifiques, qui ne sont pas remplis ».",
  'Réponse ministérielle officielle ; donnée ancienne (2013).', 'primaire'))
BOURSORAMA_TRAINEES_2024 = ('boursorama_trainees_2024', src('Aviation et climat : zoom sur les traînées de condensation, ce poids-lourd méconnu du réchauffement', 'Boursorama (avec Media Services)', '26 septembre 2024',
  'https://www.boursorama.com/actualite-economique/actualites/aviation-et-climat-zoom-sur-les-trainees-de-condensation-ce-poids-lourd-meconnu-du-rechauffement-54702c60a68cf5879c6d70855d17a4bf',
  "Selon une étude de 2021 dirigée par David S. Lee (Atmospheric Environment), les traînées pourraient représenter jusqu'à 57 % de l'effet réchauffant du secteur aérien. Chez Air France, 4 % des vols causent 80 % de l'impact des traînées de la compagnie. Lors d'essais d'American Airlines sur 70 vols, éviter les zones propices a réduit les traînées de 54 % pour 2 % de carburant en plus.",
  "Site financier généraliste reprenant une dépêche ; agence non confirmée.", 'media'))
EURONEWS_PILOTE_2024 = ('euronews_pilote_2024', src("Non, un pilote allemand n'a pas été licencié pour avoir refusé de pulvériser des produits chimiques", 'Euronews, EuroVerify (James Thomas)', '10 décembre 2024',
  'https://fr.euronews.com/2024/12/10/non-un-pilote-allemand-na-pas-ete-licencie-pour-avoir-refuse-de-pulveriser-des-produits-ch',
  "Une vidéo virale prétendait qu'un pilote de Lufthansa avait été licencié pour avoir refusé de répandre des chemtrails : « rien de ce qu'il affirme n'est vrai ». L'image vient du site satirique allemand Der Postillon.",
  "Cellule de vérification d'un média européen.", 'media'))

FICHES.append(fiche(
 id='chemtrails-trainees-avions', affirmation="Les traînées blanches des avions répandent des produits chimiques.", volet='politique', sous_theme='Désinformation',
 mots_cles=['chemtrails', 'chemtrail', 'trainees blanches', 'trainees des avions', 'trainees de condensation', 'epandage aerien secret', 'avions qui pulverisent'],
 verdict='contredit', fiabilite='etabli',
 resume="Les traînées blanches sont de la vapeur d'eau qui se condense en cristaux de glace autour des émissions normales des avions, quand l'air est assez humide et froid. Une étude de 2016 a interrogé 77 experts de l'atmosphère : 76 n'ont trouvé aucune preuve d'un épandage secret. Saisi en 2013, Météo-France n'a pas pu mettre en évidence le phénomène décrit. Ce qui est vrai : ces traînées contribuent au réchauffement climatique, peut-être plus que le CO2 de l'aviation.",
 contexte="La théorie des « chemtrails » circule depuis la fin des années 1990 et se nourrit de photos de ciels quadrillés et de fausses vidéos.",
 explication="La physique des traînées est connue ; la question est de savoir si un programme secret a été mis en évidence. Il ne l'a pas été.",
 sources=[UCI_CHEMTRAILS_2016, IOP_CHEMTRAILS_2016, AN_QE_42050, AN_QE_31101, BOURSORAMA_TRAINEES_2024, EURONEWS_PILOTE_2024],
 faits=[
  fait("Selon le Gouvernement (2014), les traînées correspondent à une condensation de l'eau de l'atmosphère en cristaux autour des émissions normales de l'avion, et dépendent des conditions météorologiques.", 'an_qe_42050', '2014', 'France', "Le phénomène a une explication physique simple.", 'etabli'),
  fait("Dans une étude de 2016, 76 des 77 chimistes de l'atmosphère et géochimistes interrogés n'avaient jamais rencontré de preuve d'un programme d'épandage secret.", 'uci_chemtrails_2016', '2016', 'Monde', "Les spécialistes rejettent la théorie.", 'etabli', '76 sur 77'),
  fait("Selon l'éditeur de l'étude, les « preuves » avancées s'expliquent par la formation normale des traînées et un mauvais échantillonnage ; en 2011, environ 17 % des personnes interrogées dans un sondage international jugeaient le programme secret vrai ou en partie vrai.", 'iop_chemtrails_2016', '2011-2016', 'Monde', "La croyance est répandue malgré l'absence de preuve.", 'estimation'),
  fait("En 2013, le Gouvernement a indiqué que Météo-France, saisi de la question, n'avait pu mettre en évidence le phénomène tel que décrit.", 'an_qe_31101', '2013', 'France', "Les services météorologiques ont examiné la question.", 'etabli'),
  fait("Selon une étude de 2021 citée par Boursorama, les traînées pourraient représenter jusqu'à 57 % de l'effet réchauffant de l'aviation ; chez Air France, 4 % des vols causent 80 % de leur impact.", 'boursorama_trainees_2024', '2021-2024', 'Monde', "Le vrai problème des traînées est climatique.", 'estimation', '57 %'),
  fait("Selon Euronews, la vidéo d'un pilote de Lufthansa prétendument licencié pour avoir refusé de pulvériser des produits chimiques reprenait une image du site satirique Der Postillon.", 'euronews_pilote_2024', '2024', 'Allemagne', "Les « témoignages » viraux sont souvent fabriqués.", 'estimation'),
 ],
 court="Non : ce sont des traînées de condensation, de la vapeur d'eau qui gèle derrière l'avion quand l'air est froid et humide. 76 experts sur 77 interrogés en 2016 n'ont trouvé aucune preuve d'épandage secret. Le vrai sujet, c'est que ces traînées réchauffent le climat.",
 moyen="Derrière un avion, l'eau contenue dans les gaz d'échappement et dans l'air se condense en cristaux de glace, comme notre souffle en hiver. Selon le Gouvernement, leur formation dépend surtout de l'humidité et de la température, ce qui explique pourquoi certaines restent longtemps et d'autres disparaissent.\n\nEn 2016, des chercheurs ont interrogé 77 spécialistes de l'atmosphère : 76 n'avaient jamais vu de preuve d'un programme secret. Météo-France, saisi en 2013, n'a rien trouvé non plus. Les vidéos virales, comme celle d'un pilote prétendument licencié, sont souvent des montages. Ce qui est vrai, en revanche, c'est que ces traînées contribuent fortement au réchauffement : de quoi s'intéresser à l'aviation sans inventer de complot.",
 detaille="Les traînées de condensation sont un phénomène physique connu. Les moteurs rejettent de la vapeur d'eau et des particules ; à haute altitude, dans un air froid et humide, cette eau se condense en cristaux de glace. Selon la réponse du Gouvernement à un député en 2014, leur formation « dépend peu de l'altitude de l'avion mais bien des conditions atmosphériques » : c'est pourquoi on voit parfois des ciels quadrillés et parfois aucune traînée.\n\nLa théorie des « chemtrails » a été examinée. En 2016, une étude publiée dans Environmental Research Letters a interrogé 77 chimistes de l'atmosphère et géochimistes : 76 n'avaient jamais rencontré de preuve d'épandage secret, et le seul dissident s'appuyait sur un taux de baryum explicable autrement. En 2013, le ministère de l'Écologie a demandé à Météo-France d'examiner la question, sans résultat. Les « preuves » qui circulent sont souvent fabriquées, comme la vidéo d'un pilote de Lufthansa issue d'un site satirique.\n\nIl y a pourtant un vrai sujet. Selon une étude de 2021, les traînées pourraient représenter jusqu'à 57 % de l'effet réchauffant de l'aviation, et une petite part des vols en produit l'essentiel. Des compagnies testent des trajectoires qui les évitent. La méfiance envers les pouvoirs publics est parfois justifiée ; elle doit s'appuyer sur des faits vérifiables.",
 empathie="Voir le ciel se couvrir de lignes blanches peut intriguer, et la méfiance envers ce qu'on ne nous explique pas est compréhensible. L'explication existe, et elle mène vers un vrai problème écologique.",
 legitimes=["Les traînées ont un effet réel sur le climat.", "Des projets de géo-ingénierie sont discutés par des chercheurs, sans programme secret démontré."],
 contre=[
  ("Avant, les traînées disparaissaient vite.", "Leur durée dépend de l'humidité de l'air ; et le trafic aérien a beaucoup augmenté, donc on en voit plus."),
  ("On a trouvé de l'aluminium et du baryum dans les sols.", "Ces éléments sont présents naturellement ou viennent de la pollution industrielle ; les experts interrogés jugent ces analyses mal faites."),
 ],
 questions=["Pourquoi un programme secret aurait-il besoin de traînées bien visibles dans le ciel ?", "Savais-tu que les traînées contribuent au réchauffement climatique ?"],
 limites=["Les réponses ministérielles datent de 2013 et 2014 ; aucune page de Météo-France n'a été lue directement.", "L'effet climatique des traînées reste incertain : 57 % est une borne haute.", "L'article de Boursorama reprend une dépêche dont l'agence n'est pas confirmée."],
 publics={'convaincus': "En 2016, des chercheurs ont interrogé 77 spécialistes de l'atmosphère : 76 n'ont jamais vu la moindre preuve d'épandage. Les traînées, c'est de la vapeur d'eau qui gèle, et elles durent plus ou moins selon l'humidité. Si tu veux un vrai combat, il y en a un : elles réchauffent le climat.",
  'indecis': "Les traînées blanches s'expliquent par la condensation de l'eau derrière les avions, et les scientifiques n'ont trouvé aucune trace d'un programme secret. Les vidéos qui circulent sont souvent des montages. En revanche, leur effet sur le climat est un sujet sérieux."},
 a_actualiser='2028-11-08', raison="Nouvelles études sur l'effet climatique des traînées.",
))

# 17 ── Notre-Dame ─────────────────────────────────────────────────────────
AFP_NOTREDAME_2019 = ('afp_notredame_2019', src('Incendie à Notre-Dame : « La piste accidentelle est privilégiée »', "L'Avenir (dépêche AFP)", '16 avril 2019',
  'https://www.lavenir.net/actu/monde/2019/04/16/incendie-a-notre-dame-la-piste-accidentelle-est-privilegiee-5TZTXOJB4JAWDJ5BBV4DY5KHME/',
  "Le procureur de Paris Rémy Heitz déclare : « Rien ne va dans le sens d'un acte volontaire. » Il y a eu « une première alerte à 18H20 », sans feu trouvé lors de la levée de doute ; la seconde alerte, à 18 h 43, a confirmé l'incendie dans la charpente. Près de 50 enquêteurs sont mobilisés et les ouvriers des cinq entreprises du chantier sont entendus.",
  'Dépêche AFP.', 'media'))
TENDANCEOUEST_NOTREDAME_2019 = ('tendanceouest_notredame_2019', src("Notre-Dame : « aucun élément » accréditant une origine criminelle d'après l'enquête préliminaire (parquet de Paris)", 'Tendance Ouest', '26 juin 2019',
  'https://www.tendanceouest.com/actualite-326755-notre-dame-aucun-element-accreditant-une-origine-criminelle-d-apres-l-enquete-preliminaire-parquet-de-paris',
  "À l'issue de l'enquête préliminaire, le parquet affirme qu'« aucun élément » ne soutient une origine criminelle et confie la suite à trois juges d'instruction. Les pistes évoquées sont un « dysfonctionnement du système électrique » ou « un départ de feu lié à une cigarette mal éteinte ».",
  'Média régional reprenant le communiqué du parquet.', 'media'))
PUBLICSENAT_NOTREDAME_2022 = ('publicsenat_notredame_2022', src('Incendie de Notre-Dame de Paris : trois ans plus tard, retour sur un chantier hors-normes et quelques polémiques', 'Public Sénat (Romain David)', '15 avril 2022',
  'https://www.publicsenat.fr/actualites/societe/incendie-de-notre-dame-de-paris-trois-ans-plus-tard-retour-un-chantier-hors-norme-et',
  "Le soir même, une enquête est ouverte pour « destruction involontaire par incendie ». Deux mois plus tard, la piste criminelle est écartée au profit d'un départ accidentel. Une information judiciaire contre X est ouverte pour « dégradations involontaires par incendie par violation manifestement délibérée d'une obligation de prudence ou de sécurité ».",
  'Média parlementaire public.', 'media'))
BLICK_NOTREDAME_2024 = ('blick_notredame_2024', src("La justice cherche toujours ce qui a déclenché l'incendie de Notre-Dame", 'Blick (édition française)', '9 novembre 2024',
  'https://www.blick.ch/fr/monde/cinq-ans-apres-le-drame-la-justice-cherche-toujours-ce-qui-a-declenche-lincendie-de-notre-dame-id20305657.html',
  "Le parquet indique : « Aucune mise en examen (inculpation) n'a été prononcée ». La procureure Laure Beccuau dit que toutes les pistes ont été explorées, y compris « l'hypothèse d'une intervention humaine », et que plus l'analyse avance, « plus la piste accidentelle est privilégiée ». Le juge a ordonné une « modélisation en 3D du départ de la flamme ». Des défaillances de l'alarme et de l'électricité d'un ascenseur ont pu favoriser la propagation du feu.",
  'Quotidien suisse.', 'media'))
FACTCHECK_NOTREDAME_2019 = ('factcheck_notredame_2019', src('Notre Dame Fire Fuels Anti-Muslim Conspiracy Theory', 'FactCheck.org (Angelo Fichera)', '17 avril 2019',
  'https://www.factcheck.org/2019/04/notre-dame-fire-fuels-anti-muslim-conspiracy-theory/',
  "« We could find no credible sources to support the incendiary suggestion that Muslims were responsible ». Une voiture chargée de bonbonnes de gaz datant de 2016 a été présentée à tort comme liée à l'incendie ; le prétendu « musulman sur le toit » était un pompier, selon CheckNews (Libération).",
  "Fact-checker reconnu (université de Pennsylvanie).", 'media'))
LALIBRE_NOTREDAME_2019 = ('lalibre_notredame_2019', src("Attentat, diversion, gilets jaunes : les théories les plus folles sur l'incendie à Notre-Dame de Paris", 'La Libre Belgique (AFP)', '16 avril 2019',
  'https://www.lalibre.be/international/2019/04/16/attentat-diversion-gilets-jaunes-les-theories-les-plus-folles-sur-lincendie-a-notre-dame-de-paris-VLOUHKNKBNHPVMHATWYT4Q3UFI/',
  "L'article recense les rumeurs (« Un attentat ? Une diversion ? ») et rappelle que « les premiers éléments pointent une cause accidentelle ». Le prétendu « gilet jaune » sur le toit était un pompier et la silhouette aperçue une statue.",
  'Dépêche AFP.', 'media'))

FICHES.append(fiche(
 id='notre-dame-incendie-attentat', affirmation="L'incendie de Notre-Dame était un attentat qu'on nous cache.", volet='politique', sous_theme='Désinformation',
 mots_cles=['notre dame', 'notre-dame', 'incendie de notre dame', 'incendie notre dame attentat', 'notre dame criminel', 'cathedrale incendie'],
 verdict='contredit', fiabilite='etabli',
 resume="Aucun élément ne soutient la thèse d'un attentat. Dès 2019, le parquet de Paris a écarté la piste criminelle au profit d'un accident (défaillance électrique ou cigarette mal éteinte) ; en 2024, la procureure indiquait que toutes les pistes, y compris une intervention humaine, avaient été explorées et que la piste accidentelle était de plus en plus privilégiée. Ce qui est vrai : la cause exacte n'est pas encore tranchée, et des défaillances de sécurité ont été relevées.",
 contexte="Dès le soir du 15 avril 2019, des rumeurs d'attentat ont circulé, souvent accompagnées d'accusations contre les musulmans.",
 explication="Il faut distinguer ce que l'enquête a établi, ce qu'elle n'a pas encore tranché, et les « preuves » virales démenties.",
 sources=[AFP_NOTREDAME_2019, TENDANCEOUEST_NOTREDAME_2019, PUBLICSENAT_NOTREDAME_2022, BLICK_NOTREDAME_2024, FACTCHECK_NOTREDAME_2019, LALIBRE_NOTREDAME_2019],
 faits=[
  fait("Le 16 avril 2019, le procureur de Paris a déclaré : « Rien ne va dans le sens d'un acte volontaire », près de 50 enquêteurs étant mobilisés.", 'afp_notredame_2019', '2019', 'Paris', "L'enquête a été ouverte immédiatement et à grande échelle.", 'etabli'),
  fait("Selon le parquet de Paris, en juin 2019, aucun élément n'accréditait une origine criminelle ; il évoquait une défaillance électrique ou une cigarette mal éteinte.", 'tendanceouest_notredame_2019', '2019', 'Paris', "La piste criminelle a été examinée et écartée.", 'etabli'),
  fait("Une information judiciaire contre X a été ouverte pour dégradations involontaires par incendie par violation d'une obligation de prudence ou de sécurité.", 'publicsenat_notredame_2022', '2019-2022', 'Paris', "La justice cherche d'éventuelles négligences.", 'etabli'),
  fait("Selon Blick, en novembre 2024, la procureure de Paris indiquait que l'hypothèse d'une intervention humaine avait été explorée et que la piste accidentelle était de plus en plus privilégiée ; aucune mise en examen n'avait été prononcée.", 'blick_notredame_2024', '2024', 'Paris', "La cause exacte reste à déterminer, sans élément d'attentat.", 'etabli'),
  fait("Selon FactCheck.org, aucune source crédible ne soutenait l'idée que des musulmans étaient responsables ; le prétendu « musulman sur le toit » était un pompier.", 'factcheck_notredame_2019', '2019', 'Paris', "Les « preuves » virales ont été démenties.", 'etabli'),
 ],
 court="Rien ne l'indique : le parquet a écarté la piste criminelle dès 2019, et en 2024 il jugeait l'accident de plus en plus probable après avoir exploré toutes les pistes. La cause exacte n'est pas encore tranchée, c'est vrai. Mais les « preuves » d'attentat qui ont circulé ont toutes été démenties.",
 moyen="Le soir même, une enquête a été ouverte et près de 50 enquêteurs mobilisés. En juin 2019, le parquet de Paris a conclu qu'aucun élément n'accréditait une origine criminelle et a évoqué deux pistes : une défaillance électrique ou une cigarette mal éteinte. Trois juges d'instruction cherchent depuis d'éventuelles négligences.\n\nEn 2024, la procureure expliquait que l'hypothèse d'une intervention humaine avait été examinée et que la piste accidentelle était de plus en plus privilégiée. Les images qui circulaient, une silhouette sur le toit, une voiture de bonbonnes de gaz, ont été démenties : c'était un pompier et une affaire de 2016. Dire « on nous cache un attentat » sans le moindre élément, c'est souvent une manière d'accuser une communauté.",
 detaille="L'enquête a commencé le soir même. Le 16 avril 2019, le procureur de Paris déclarait : « Rien ne va dans le sens d'un acte volontaire ». Près de 50 enquêteurs ont entendu les ouvriers des cinq entreprises présentes sur le chantier. Une première alarme avait sonné à 18 h 20 sans que le feu soit trouvé, avant une seconde à 18 h 43.\n\nEn juin 2019, au terme de l'enquête préliminaire, le parquet a indiqué qu'aucun élément n'accréditait une origine criminelle, et retenu deux hypothèses : un dysfonctionnement du système électrique ou une cigarette mal éteinte. Une information judiciaire a été ouverte pour dégradations involontaires par violation d'une obligation de prudence ou de sécurité. En novembre 2024, la procureure Laure Beccuau précisait que toutes les pistes avaient été explorées, y compris une intervention humaine, et que plus l'analyse avançait, plus l'accident était privilégié ; une modélisation en 3D du départ de feu était en cours.\n\nLes rumeurs, elles, ont été démenties dès les premiers jours : la silhouette sur le toit était un pompier, la voiture de bonbonnes de gaz datait de 2016. Il reste une part d'inconnu : la cause exacte n'est pas tranchée et des défaillances de sécurité ont été relevées. On peut exiger des réponses sur ces négligences ; affirmer un attentat caché, c'est remplacer l'enquête par un soupçon.",
 empathie="Voir brûler Notre-Dame a bouleversé beaucoup de monde, et l'idée qu'un tel drame soit un simple accident peut sembler difficile à accepter. L'enquête a pourtant cherché toutes les pistes.",
 legitimes=["La cause exacte de l'incendie n'est pas encore établie.", "Des défaillances de sécurité (alarme, électricité) ont été relevées."],
 contre=[
  ("Une cathédrale ne brûle pas toute seule.", "Le parquet évoque une défaillance électrique ou une cigarette sur un chantier ; des incendies accidentels de monuments se produisent régulièrement."),
  ("Pourquoi l'enquête dure aussi longtemps ?", "Parce que les preuves ont brûlé et que les juges cherchent d'éventuelles négligences ; la durée ne prouve pas une dissimulation."),
 ],
 questions=["Sur quel élément précis repose l'idée d'un attentat ?", "Savais-tu que la piste criminelle a été examinée par les enquêteurs ?"],
 limites=["Aucune source lue n'est postérieure à novembre 2024 ; l'enquête a pu évoluer depuis.", "Plusieurs sources sont des médias reprenant des communications du parquet (Tendance Ouest, Blick)."],
 publics={'convaincus': "Les enquêteurs ont examiné la piste criminelle, et dès 2019 le parquet a dit qu'aucun élément ne la soutenait. En 2024, ils jugeaient l'accident de plus en plus probable. Les « preuves » qui ont circulé, la silhouette sur le toit, c'était un pompier.",
  'indecis': "La cause exacte de l'incendie n'est pas encore tranchée, et il est normal de vouloir des réponses. Mais l'enquête a exploré toutes les pistes, y compris un acte volontaire, sans rien trouver qui l'accrédite. Les pistes privilégiées sont une défaillance électrique ou une cigarette."},
 a_actualiser='2027-04-15', raison="Avancée de l'information judiciaire.",
))

# 18 ── Passe sanitaire ────────────────────────────────────────────────────
CC_2021_824 = ('cc_2021_824', src('Décision n° 2021-824 DC du 5 août 2021 – Communiqué de presse', 'Conseil constitutionnel', '5 août 2021',
  'https://www.conseil-constitutionnel.fr/actualites/communique/decision-n-2021-824-dc-du-5-aout-2021-communique-de-presse',
  "Saisi par le Premier ministre, par plus de 60 députés et par deux groupes de plus de 60 sénateurs, le Conseil valide le passe sanitaire, applicable seulement jusqu'au 15 novembre 2021, jugeant qu'il opère « une conciliation équilibrée entre les exigences constitutionnelles précitées ». Il censure l'isolement automatique de dix jours des personnes positives, imposé « sans qu'aucune appréciation ne soit portée sur sa situation personnelle », et la rupture anticipée des CDD et contrats d'intérim.",
  'Juridiction constitutionnelle.', 'primaire'))
CC_2022_835 = ('cc_2022_835', src('Décision n° 2022-835 DC du 21 janvier 2022 – Communiqué de presse', 'Conseil constitutionnel', '21 janvier 2022',
  'https://www.conseil-constitutionnel.fr/actualites/communique/decision-n-2022-835-dc-du-21-janvier-2022-communique-de-presse',
  "Le Conseil valide le passe vaccinal pour les 16 ans et plus. Ces mesures ne peuvent être prises que « jusqu'au 31 juillet 2022 », et « Il y est mis fin sans délai lorsqu'elles ne sont plus nécessaires ». Il précise que la loi ne crée pas d'obligation vaccinale et censure le passe sanitaire pour les réunions politiques, qui « n'opèrent pas une conciliation équilibrée ».",
  'Juridiction constitutionnelle.', 'primaire'))
CE_PASSE_2021 = ('ce_passe_2021', src('Centres commerciaux des Alpes-Maritimes : le Conseil d’État ne suspend pas l’obligation de passe sanitaire', "Conseil d'État (ordonnance n° 456391)", '13 septembre 2021',
  'https://conseil-etat.fr/site/actualites/centres-commerciaux-des-alpes-maritimes-le-conseil-d-etat-ne-suspend-pas-l-obligation-de-passe-sanitaire',
  "Le taux d'incidence dépassait 200 cas pour 100 000 habitants. Le juge estime la mesure « nécessaire, adaptée et manifestement proportionnée à l'objectif de santé publique » et, le passe pouvant reposer sur un test ou un certificat de rétablissement, juge qu'il « n'y a pas de discrimination spécifique ».",
  'Juridiction administrative suprême.', 'primaire'))
MAIREINFO_DDD_2021 = ('maireinfo_ddd_2021', src("Extension du pass sanitaire : « L'ampleur de l'atteinte aux droits et libertés fondamentales » inquiète la Défenseure des droits", 'Maire-info (Association des maires de France)', '21 juillet 2021',
  'https://www.maire-info.com/coronavirus/extension-du-pass-sanitaire-lampleur-de-latteinte-aux-droits-et-libertes-fondamentales-inquiete-la-defenseure-des-droits-art26-25554',
  "Claire Hédon formule « dix points de vigilance ou de risque d'atteinte aux droits et libertés ». Elle critique la délégation du contrôle à des acteurs privés : « Ce contrôle devrait relever des autorités publiques ». Elle alerte sur le risque de « stigmatisation de l'élève non vacciné » et demande des réévaluations régulières pour que l'exception ne devienne pas permanente.",
  "Média de l'association des maires, qui rapporte l'avis d'une autorité indépendante.", 'media'))
CNIL_PASSE_2021 = ('cnil_passe_2021', src("Les mises en garde de la CNIL sur l'extension du passe sanitaire", 'CNIL (autorité administrative indépendante)', '21 juillet 2021',
  'https://cnil.fr/fr/les-mises-en-garde-de-la-cnil-sur-lextension-du-passe-sanitaire',
  "La CNIL appelle à « éviter toute banalisation de ce type de mesure » et alerte sur « le risque d'accoutumance et de banalisation ». Elle note que « l'appréciation de cette proportionnalité dépend grandement du caractère gratuit ou payant des tests ».",
  'Autorité administrative indépendante.', 'primaire'))
VIDAL_FIN_PASSE_2022 = ('vidal_fin_passe_2022', src('Le point sur le projet de loi sanitaire validé par le Parlement', 'VIDAL (Gérome Patrick)', '31 juillet 2022',
  'https://www.vidal.fr/actualites/29713-le-point-sur-le-projet-de-loi-sanitaire-valide-par-le-parlement.html',
  "La loi définitivement adoptée le 26 juillet 2022 « met fin le 1er août au pass sanitaire ». Le passe vaccinal était suspendu depuis le 14 mars 2022. Les régimes d'urgence prennent fin le 31 juillet 2022 et le Conseil scientifique est dissous.",
  'Presse professionnelle de santé.', 'media'))

FICHES.append(fiche(
 id='passe-sanitaire-dictature', affirmation="Le passe sanitaire, c'était une dictature.", volet='droits', sous_theme='Libertés publiques',
 mots_cles=['passe sanitaire', 'pass sanitaire', 'passe vaccinal', 'pass vaccinal', 'dictature sanitaire', 'restrictions covid libertes'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le passe sanitaire a restreint les libertés de façon inédite, et la Défenseure des droits comme la CNIL ont alerté sur ses risques. Mais il a été voté par le Parlement, contrôlé par le Conseil constitutionnel, qui en a censuré plusieurs dispositions (isolement automatique, réunions politiques), limité dans le temps et supprimé le 1er août 2022. Une dictature ne se soumet ni aux juges, ni à une date de fin votée par le Parlement.",
 contexte="Les manifestations contre le passe sanitaire de l'été 2021 ont popularisé l'expression « dictature sanitaire », reprise par une partie de l'extrême droite.",
 explication="Il faut séparer la critique légitime d'une mesure restrictive et la qualification de dictature, qui suppose l'absence de contre-pouvoirs.",
 sources=[CC_2021_824, CC_2022_835, CE_PASSE_2021, MAIREINFO_DDD_2021, CNIL_PASSE_2021, VIDAL_FIN_PASSE_2022],
 faits=[
  fait("Le Conseil constitutionnel, saisi notamment par plus de 60 députés et par des sénateurs, a validé le passe sanitaire jusqu'au 15 novembre 2021 mais censuré l'isolement automatique des personnes positives et la rupture anticipée des CDD.", 'cc_2021_824', '2021', 'France', "Les juges ont contrôlé et partiellement censuré la loi.", 'etabli'),
  fait("En janvier 2022, le Conseil constitutionnel a borné le passe vaccinal au 31 juillet 2022 et censuré son application aux réunions politiques.", 'cc_2022_835', '2022', 'France', "La mesure était limitée dans le temps et n'a pas pu toucher la vie politique.", 'etabli'),
  fait("Le Conseil d'État a jugé en septembre 2021 l'obligation de passe dans des centres commerciaux « nécessaire, adaptée et manifestement proportionnée », avec une incidence supérieure à 200 cas pour 100 000 habitants.", 'ce_passe_2021', '2021', 'France', "Les juges ont examiné la proportionnalité au cas par cas.", 'etabli'),
  fait("D'après Maire-info, la Défenseure des droits a formulé en juillet 2021 dix points de vigilance sur les atteintes aux droits et libertés, et critiqué la délégation des contrôles à des acteurs privés.", 'maireinfo_ddd_2021', '2021', 'France', "Les critiques des autorités indépendantes étaient sérieuses : c'est un fait à reconnaître.", 'etabli'),
  fait("Selon la CNIL, il fallait éviter toute banalisation de ce type de mesure, au risque d'une accoutumance.", 'cnil_passe_2021', '2021', 'France', "Le risque de pérennisation a été pointé par les institutions elles-mêmes.", 'etabli'),
  fait("Selon VIDAL, le passe vaccinal a été suspendu le 14 mars 2022 et le passe sanitaire supprimé le 1er août 2022 par une loi votée par le Parlement.", 'vidal_fin_passe_2022', '2022', 'France', "La mesure a pris fin.", 'etabli'),
 ],
 court="Non : le passe sanitaire a été voté par le Parlement, contrôlé et en partie censuré par le Conseil constitutionnel, limité dans le temps et supprimé en août 2022. Il a vraiment restreint les libertés, et des autorités indépendantes l'ont critiqué. Mais une dictature ne laisse pas les juges la censurer.",
 moyen="Le passe sanitaire a été une restriction inédite des libertés, et il était légitime de le contester : la Défenseure des droits a pointé dix risques d'atteinte aux droits, la CNIL a mis en garde contre sa banalisation.\n\nMais les contre-pouvoirs ont fonctionné. Des députés et sénateurs de l'opposition ont saisi le Conseil constitutionnel, qui a censuré l'isolement automatique des malades et le passe pour les réunions politiques, et imposé une date de fin. Le Conseil d'État a contrôlé la proportionnalité. Le passe vaccinal a été suspendu en mars 2022 et le passe sanitaire supprimé en août 2022. On peut juger la mesure excessive ; parler de dictature banalise ce que sont les vraies dictatures.",
 detaille="Il faut d'abord reconnaître ce qu'a été le passe sanitaire : une condition d'accès à de nombreux lieux de la vie quotidienne, inédite en temps de paix. Des autorités indépendantes l'ont critiqué. La Défenseure des droits a formulé dix points de vigilance, contesté le fait que des acteurs privés contrôlent le public et alerté sur la stigmatisation des élèves non vaccinés. La CNIL a appelé à éviter toute banalisation et relevé que la proportionnalité dépendait de la gratuité des tests.\n\nMais le cadre démocratique est resté en place. Les lois ont été votées par le Parlement et déférées au Conseil constitutionnel par plus de 60 députés et des groupes de sénateurs. Le 5 août 2021, le Conseil a validé le passe jusqu'au 15 novembre, en censurant l'isolement automatique des personnes positives et la rupture anticipée des CDD. Le 21 janvier 2022, il a borné le passe vaccinal au 31 juillet 2022 et censuré son application aux réunions politiques. Le Conseil d'État a contrôlé la proportionnalité des mesures locales.\n\nEnfin, la mesure a pris fin : passe vaccinal suspendu le 14 mars 2022, passe sanitaire supprimé le 1er août 2022, régimes d'urgence terminés. Défendre les libertés publiques, c'est rester vigilant face aux mesures d'exception ; c'est aussi reconnaître que des juges et un Parlement ont pu les limiter, ce qui n'existe pas dans une dictature.",
 empathie="Beaucoup de gens ont vécu le passe sanitaire comme une humiliation ou une contrainte injuste, et ce ressenti mérite d'être entendu. Les libertés publiques méritent qu'on les défende avec des mots justes.",
 legitimes=["Le passe sanitaire a restreint les libertés de façon inédite.", "La Défenseure des droits et la CNIL ont alerté sur les risques de banalisation."],
 contre=[
  ("Le Conseil constitutionnel a tout validé.", "Il a validé l'essentiel, mais censuré plusieurs dispositions et imposé des dates de fin ; il a aussi rappelé que la loi ne créait pas d'obligation vaccinale."),
  ("On a fait passer ça en urgence sans débat.", "Les textes ont été débattus et votés par le Parlement, puis contrôlés par les juges ; on peut contester le contenu, mais la procédure démocratique a existé."),
 ],
 questions=["Dans une dictature, le Conseil constitutionnel aurait-il pu censurer le gouvernement ?", "Qu'est-ce qui distingue, selon toi, une mesure excessive d'un régime autoritaire ?"],
 limites=["L'avis de la Défenseure des droits a été lu à travers Maire-info ; l'avis original n'a pas été ouvert.", "L'avis de la CNCDH n'a pas été lu.", "La question de l'efficacité sanitaire du passe n'est pas traitée ici."],
 publics={'convaincus': "Le passe sanitaire, on pouvait le trouver injuste, et la Défenseure des droits elle-même l'a critiqué. Mais il a été voté, contrôlé et en partie censuré par le Conseil constitutionnel, puis supprimé en août 2022. Une dictature, ce n'est pas un pouvoir que les juges peuvent censurer.",
  'indecis': "Le passe sanitaire a été une restriction de libertés sans précédent, et les critiques étaient légitimes. Mais le Parlement l'a voté, les juges l'ont limité et il a pris fin en 2022. Rester vigilant sur les mesures d'exception, oui ; parler de dictature, c'est autre chose."},
 a_actualiser='2028-11-08', raison="Fiche historique ; à revoir si une nouvelle crise sanitaire survient.",
))

# 19 ── Mariage pour tous et famille ───────────────────────────────────────
INSEE_MARIAGES_MEMESEXE_2026 = ('insee_mariages_memesexe_2026', src('En 2024, 3 % des mariages ont été conclus entre personnes de même sexe (Insee Focus n° 381)', 'Insee (Sofian El Atifi)', '23 avril 2026',
  'https://www.insee.fr/fr/statistiques/8975359',
  "« 84 000 couples de même sexe se sont mariés entre 2013 et 2024 ». Pic de 10 530 en 2014 (« effet de rattrapage »), puis « Depuis 2022, le nombre annuel de mariages entre partenaires de même sexe oscille autour de 6 800 ». Part dans l'ensemble des mariages : 4,4 % en 2014, 2,7 % en 2024.",
  'Statistique publique.', 'primaire'))
INSEE_MARIAGES_PACS = ('insee_mariages_pacs', src('Mariages et Pacs – Données annuelles de 1990 à 2025', 'Insee', '13 janvier 2026',
  'https://www.insee.fr/fr/statistiques/2381498',
  "Mariages : 241 292 en 2014, 224 740 en 2019, 154 581 en 2020 (Covid), 241 710 en 2022, 248 174 en 2024 et 251 000 en 2025 (provisoire). Pacs : 173 731 en 2014, 196 370 en 2019, 197 176 en 2024.",
  'Statistique publique.', 'primaire'))
INSEE_TEF_2019 = ('insee_tef_2019', src('Mariages – Pacs – Divorces (Tableaux de l’économie française, édition 2019)', 'Insee', '26 mars 2019',
  'https://www.insee.fr/fr/statistiques/3676592?sommaire=3696937',
  "Les mariages de sexe différent passent de 286 000 en 2002 à 252 000 en 2010 et 237 000 en 2011. Les divorces prononcés par un juge culminent à 155 300 en 2005 ; l'Insee parle d'une « baisse quasi continue du nombre de divorces prononcés par un juge » depuis, la chute de 2017 s'expliquant par la réforme du divorce par consentement mutuel.",
  'Statistique publique ; donnée de 2019.', 'primaire'))
INSEE_BILAN_DEMO_2025 = ('insee_bilan_demo_2025', src('Bilan démographique 2025 (Insee Première n° 2087)', 'Insee (Hélène Thélot)', '13 janvier 2026',
  'https://www.insee.fr/fr/statistiques/8719824',
  "Environ 645 000 naissances en 2025, soit 23,6 % de moins qu'en 2010 et « le plus bas niveau observé depuis 1942 ». La fécondité tombe à 1,56 enfant par femme ; elle était de 2,02 en 2010, dernier pic des naissances. Les mariages remontent à environ 251 000 (+1,4 %).",
  'Statistique publique.', 'primaire'))
SLATE_HOMOPARENTALITE = ('slate_homoparentalite', src("Y a-t-il un lien entre homoparentalité et troubles du comportement de l'enfant ?", 'Slate.fr (republication de The Conversation)', 'vers 2019 (date non affichée)',
  'https://www.slate.fr/story/182280/pma-homoparentalite-developpement-enfants-meres-lesbiennes',
  "La revue porte sur 16 publications internationales (1997 à 2017) et 9 cohortes d'enfants de mères lesbiennes nés par PMA, de 12 à 283 participants. La structure familiale n'a quasiment pas d'effet sur le développement psychologique ; la qualité de la relation parentale pèse davantage. Les auteurs appellent à la prudence méthodologique.",
  'Article de chercheurs ; date et auteurs non visibles sur la page.', 'secondaire'))

FICHES.append(fiche(
 id='mariage-pour-tous-famille', affirmation="Le mariage pour tous a détruit la famille.", volet='droits', sous_theme='Droits des personnes LGBT',
 mots_cles=['mariage pour tous', 'mariage homosexuel', 'mariage gay', 'loi taubira', 'detruit la famille', 'mariage entre personnes de meme sexe'],
 verdict='contredit', fiabilite='etabli',
 resume="Selon l'Insee, 84 000 couples de même sexe se sont mariés entre 2013 et 2024, soit environ 3 % des mariages. Le nombre total de mariages n'a pas chuté après la loi : 241 000 en 2014, 251 000 en 2025. La baisse des mariages (2002-2011), celle des divorces (depuis 2005) et celle des naissances (depuis 2010) ont toutes commencé avant 2013. Rien dans les données ne relie ces évolutions à la loi.",
 contexte="Les opposants à la loi Taubira de 2013 annonçaient la fin de la famille ; l'argument revient dans les discours conservateurs sur la natalité.",
 explication="Une loi qui « détruirait la famille » devrait laisser une trace dans les chiffres des mariages, des divorces ou des naissances après 2013.",
 sources=[INSEE_MARIAGES_MEMESEXE_2026, INSEE_MARIAGES_PACS, INSEE_TEF_2019, INSEE_BILAN_DEMO_2025, LCP_MARIAGE_10ANS, SLATE_HOMOPARENTALITE],
 faits=[
  fait("Selon l'Insee, 84 000 couples de même sexe se sont mariés entre 2013 et 2024 ; ces mariages représentent 2,7 % du total en 2024.", 'insee_mariages_memesexe_2026', '2013-2024', 'France', "Le mariage pour tous concerne une petite part des mariages.", 'etabli', '84 000'),
  fait("Le nombre total de mariages est passé de 241 292 en 2014 à environ 251 000 en 2025, hors chute due au Covid en 2020.", 'insee_mariages_pacs', '2014-2025', 'France', "Le mariage n'a pas reculé après la loi.", 'etabli', '251 000'),
  fait("Les mariages entre personnes de sexe différent avaient baissé de 286 000 en 2002 à 237 000 en 2011, avant la loi ; les divorces prononcés par un juge baissent depuis leur pic de 2005.", 'insee_tef_2019', '2002-2017', 'France', "Les tendances de fond précèdent 2013.", 'etabli'),
  fait("Selon l'Insee, les naissances ont baissé de 23,6 % depuis 2010, dernier pic, pour atteindre environ 645 000 en 2025 ; la fécondité est de 1,56 enfant par femme.", 'insee_bilan_demo_2025', '2010-2025', 'France', "La baisse de la natalité est réelle, mais commence trois ans avant la loi.", 'etabli', '1,56'),
  fait("Dix ans après la loi, aucun responsable politique de premier plan ne propose plus de revenir en arrière ; Gérald Darmanin, qui avait voté contre, a déclaré : « Je me suis trompé ».", 'lcp_mariage_10ans', '2023', 'France', "La loi s'est installée dans la société.", 'etabli'),
  fait("Une revue de 16 études (1997-2017) publiée par The Conversation trouve que la structure familiale n'a quasiment pas d'effet sur le développement psychologique des enfants de mères lesbiennes, avec des échantillons de petite taille.", 'slate_homoparentalite', '1997-2017', 'Monde', "Les études disponibles ne montrent pas de dommage pour les enfants, avec des limites méthodologiques.", 'estimation'),
 ],
 court="Les chiffres de l'Insee disent le contraire : il y a eu plus de mariages en 2025 (251 000) qu'en 2014. Les mariages de même sexe représentent 3 % du total. La baisse des naissances a commencé en 2010, trois ans avant la loi.",
 moyen="Depuis 2013, 84 000 couples de même sexe se sont mariés, environ 3 % des mariages selon l'Insee. Le mariage n'a pas reculé pour autant : 241 000 mariages en 2014, 251 000 en 2025.\n\nLes évolutions qu'on attribue à la loi ont commencé avant elle : les mariages baissaient depuis 2002, les divorces reculent depuis 2005, la natalité baisse depuis 2010. Le mariage pour tous n'a rien retiré aux familles existantes ; il a permis à d'autres d'en fonder une avec les mêmes droits. Même des responsables qui avaient voté contre, comme Gérald Darmanin, disent aujourd'hui s'être trompés.",
 detaille="Si le mariage pour tous avait détruit la famille, cela se verrait dans les chiffres. Selon l'Insee, 84 000 couples de même sexe se sont mariés entre 2013 et 2024 : 10 530 en 2014, année de rattrapage, puis environ 6 800 par an depuis 2022, soit 2,7 % des mariages en 2024. Le nombre total de mariages n'a pas baissé : 241 292 en 2014, 248 174 en 2024, environ 251 000 en 2025, hors chute du Covid en 2020. Les Pacs ont progressé dans le même temps.\n\nLes tendances de fond sont antérieures à la loi. Les mariages entre personnes de sexe différent étaient passés de 286 000 en 2002 à 237 000 en 2011. Les divorces prononcés par un juge baissent depuis leur pic de 2005. La natalité, elle, recule bien : environ 645 000 naissances en 2025, le plus bas niveau depuis 1942, et 1,56 enfant par femme. Mais ce recul a commencé en 2010, et aucune source ne le relie à la loi de 2013.\n\nSur les enfants, une revue de 16 études internationales trouve que la structure familiale n'a quasiment pas d'effet sur leur développement psychologique, la qualité de la relation parentale comptant davantage ; les échantillons sont petits et les auteurs restent prudents. La loi a été adoptée en 2013 par 331 voix contre 225, et dix ans après plus aucun responsable de premier plan ne veut l'abroger. Elle n'a rien enlevé à personne.",
 empathie="Pour certaines personnes, attachées à une conception traditionnelle du mariage, la loi a été vécue comme un bouleversement. On peut respecter cette conviction tout en regardant ce que les chiffres montrent.",
 legitimes=["La natalité baisse fortement en France.", "Les études sur l'homoparentalité reposent sur de petits échantillons."],
 contre=[
  ("La natalité s'effondre depuis la loi.", "La baisse a commencé en 2010, trois ans avant la loi ; elle touche aussi des pays sans mariage pour tous."),
  ("Un enfant a besoin d'un père et d'une mère.", "Les études disponibles montrent que c'est surtout la qualité de la relation parentale qui compte ; elles appellent à la prudence, mais aucune ne montre de dommage."),
 ],
 questions=["Savais-tu qu'il y a eu plus de mariages en 2025 qu'en 2014 ?", "En quoi le mariage de deux hommes ou de deux femmes change-t-il la famille des autres ?"],
 limites=["Les données sur les divorces datent de 2019.", "Les études sur l'homoparentalité ont de petits échantillons ; l'étude française DEVHOM n'a pas publié de résultats lus.", "Aucun sondage récent sur l'opinion des Français à propos de la loi n'a pu être lu."],
 publics={'convaincus': "Regarde les chiffres de l'Insee : 251 000 mariages en 2025, plus qu'en 2014. Les mariages de même sexe, c'est 3 % du total. Et la natalité baisse depuis 2010, trois ans avant la loi : elle n'a rien à voir.",
  'indecis': "On peut être attaché au mariage traditionnel et se poser la question. Mais les données montrent que le mariage ne recule pas et que les tendances des divorces et des naissances ont commencé avant 2013. La loi a donné des droits à des familles sans en retirer aux autres."},
 a_actualiser='2027-04-30', raison="Nouvelles données de l'Insee sur les mariages.",
))

# 20 ── Viande halal et islamisme ──────────────────────────────────────────
SENAT_ISLAM_2016 = ('senat_islam_2016', src("Mission d'information sur l'organisation, la place et le financement de l'islam en France et de ses lieux de culte (synthèse)", 'Sénat (présidente Corinne Féret, rapporteure Nathalie Goulet, co-rapporteur André Reichardt)', '2016',
  'https://www.senat.fr/fileadmin/Fichiers/Images/commission/missions/islam_en_france/14-Brochure_Mission_Islam.pdf',
  "Les cartes de sacrificateur sont délivrées par trois mosquées agréées par l'Intérieur (Paris, Évry, Lyon), un « oligopole ». Le rapport évoque une « surenchère autour du « halal business » » et l'absence de norme halal commune. Il écarte une « taxe halal » (raisons théorique, juridique — inconstitutionnalité d'une taxe liée au caractère religieux d'un produit — et politique) et juge possible une redevance pour services rendus instaurée par le culte lui-même. Le culte est financé « essentiellement par les fidèles » ; le Maroc a versé 6 M€ en 2016, l'Algérie 2 M€, l'Arabie saoudite 3,8 M€ depuis 2011 ; les financements privés étrangers sont impossibles à connaître.",
  'Rapport parlementaire transpartisan ; donnée ancienne (2016).', 'primaire'))
LOCALTIS_ISLAM_2016 = ('localtis_islam_2016', src("Un islam de France largement influencé par l'étranger", 'Localtis / Banque des Territoires (Michel Tendil)', '7 juillet 2016',
  'https://www.banquedesterritoires.fr/un-islam-de-france-largement-influence-par-letranger',
  "Les sénateurs rejettent une taxe halal et proposent une « redevance pour services rendus » sur le modèle de la cacheroute. Ils dénoncent l'oligopole des cartes de sacrificateur, détenu par la Grande Mosquée de Paris (« sous autorité algérienne ») et les mosquées de Lyon et d'Évry, et relèvent 301 imams détachés (151 turcs, 120 algériens, 30 marocains).",
  'Média des collectivités (Caisse des dépôts) ; donnée ancienne (2016).', 'media'))
VDI_HALAL_2013 = ('vdi_halal_2013', src('Les enjeux du halal en France', 'La Vie des idées, Collège de France (Mohamed Ali-Adraoui)', '9 juillet 2013',
  'https://laviedesidees.fr/Les-enjeux-du-halal-en-France',
  "Depuis un décret de 1997, l'État agrée environ 600 sacrificateurs via trois mosquées, et des certificateurs privés existent. En 1995, un accord prévoyait le versement à la Grande Mosquée de Paris d'« un franc par kilo de viande abattue ». La Mosquée de Lyon « retire environ 15 centimes d'euro par kilogramme de viande contrôlée ». Selon l'auteur, le halal est « davantage un label qu'une réalité tangible ».",
  'Revue universitaire ; donnée ancienne (2013).', 'etude'))
PUBLICSENAT_ELKAROUI_2018 = ('publicsenat_elkaroui_2018', src("Un rapport pour réformer l'islam et contrer la « fabrique de l'islamisme »", 'Public Sénat (Karine Perret)', '10 septembre 2018',
  'https://www.publicsenat.fr/actualites/non-classe/un-rapport-pour-reformer-l-islam-et-contrer-la-fabrique-de-l-islamisme-132932',
  "Le rapport d'Hakim El Karoui pour l'Institut Montaigne propose une association qui gérerait une « taxe halal » non étatique, sur le modèle de la cacheroute, pour « prélever une toute petite somme d'argent sur chaque acte de consommation » afin de financer la formation théologique.",
  'Média parlementaire public.', 'media'))
INDAILY_AUSTRAC_2015 = ('indaily_austrac_2015', src('No halal link to terror: intelligence agency', 'InDaily (Australie)', '24 septembre 2015',
  'https://www.indailysa.com.au/news/archive/2015/09/24/no-halal-link-to-terror-intelligence-agency',
  "Devant une commission d'enquête du Sénat australien, l'AUSTRAC (renseignement financier) déclare : « no evidence that halal food certification is linked to financing of terrorism ». L'Australian Crime Commission : « we have not found a direct link ».",
  'Média régional australien rapportant des auditions officielles ; contexte étranger, donnée ancienne.', 'media'))
AN_QG_3977 = ('an_qg_3977', src('Question au Gouvernement n° 3977 et réponse de Bruno Le Maire', 'Assemblée nationale (Journal officiel)', '22 février 2012',
  'https://questions.assemblee-nationale.fr/dyn/13/questions/QANR5L13QG3977.pdf',
  "Un décret soumet l'abattage rituel à autorisation : « plus aucun abattoir ne pourra procéder à un abattage rituel sans avoir l'accord formel de l'État ». Le ministre affirme que « la grande majorité de cette viande provient d'abattoirs qui ne sont pas des abattoirs rituels ».",
  'Réponse ministérielle officielle ; donnée ancienne (2012).', 'primaire'))

FICHES.append(fiche(
 id='halal-finance-islamisme', affirmation="La viande halal finance l'islamisme.", volet='droits', sous_theme='Laïcité',
 mots_cles=['halal', 'viande halal', 'taxe halal', 'certification halal', 'abattage rituel', 'halal finance'],
 verdict='trompeur', fiabilite='estimation',
 resume="Aucune source lue ne montre que la viande halal financerait l'islamisme ou le terrorisme. La certification est organisée par trois mosquées agréées par l'État et par des certificateurs privés ; les prélèvements connus sont modestes (environ 15 centimes par kilo à Lyon en 2013). Le Sénat a écarté en 2016 l'idée d'une « taxe halal », jugée inconstitutionnelle. Ce qui est vrai : la filière manque de transparence, l'une des mosquées est liée à l'Algérie, et les financements privés étrangers du culte sont mal connus.",
 contexte="L'idée d'une « taxe halal » reversée à l'islamisme circule depuis les années 2010 et revient dans les débats sur l'abattage rituel.",
 explication="Il faut distinguer le financement du culte musulman, légal et en partie opaque, et le financement de l'islamisme ou du terrorisme, qui n'est pas démontré par la filière halal.",
 sources=[SENAT_ISLAM_2016, LOCALTIS_ISLAM_2016, VDI_HALAL_2013, PUBLICSENAT_ELKAROUI_2018, INDAILY_AUSTRAC_2015, AN_QG_3977],
 faits=[
  fait("Selon le Sénat (2016), les cartes de sacrificateur sont délivrées par trois mosquées agréées par l'État (Paris, Évry, Lyon), sans norme halal commune.", 'senat_islam_2016', '2016', 'France', "La filière est encadrée par l'État mais peu transparente.", 'etabli'),
  fait("Le Sénat a écarté en 2016 l'idée d'une taxe halal, notamment parce qu'une taxe liée au caractère religieux d'un produit serait inconstitutionnelle.", 'senat_islam_2016', '2016', 'France', "Il n'existe pas de taxe halal publique.", 'etabli'),
  fait("Selon La Vie des idées, la Mosquée de Lyon prélevait environ 15 centimes d'euro par kilogramme de viande contrôlée, et un accord de 1995 prévoyait un franc par kilo pour la Grande Mosquée de Paris.", 'vdi_halal_2013', '1995-2013', 'France', "Les prélèvements connus servent au fonctionnement des institutions du culte.", 'estimation'),
  fait("Selon le Sénat, le culte musulman est financé essentiellement par les fidèles ; le Maroc a versé 6 M€ en 2016, l'Algérie 2 M€, l'Arabie saoudite 3,8 M€ depuis 2011, et les financements privés étrangers sont impossibles à connaître.", 'senat_islam_2016', '2011-2016', 'France', "L'influence étrangère sur le culte est réelle et en partie opaque : c'est un fait à reconnaître.", 'etabli'),
  fait("En 2018, le rapport El Karoui pour l'Institut Montaigne a proposé une redevance halal non étatique pour financer la formation des imams.", 'publicsenat_elkaroui_2018', '2018', 'France', "L'idée d'un prélèvement sur le halal vise aussi à financer un islam de France.", 'etabli'),
  fait("En Australie, le renseignement financier a déclaré en 2015 n'avoir trouvé « no evidence » d'un lien entre la certification halal et le financement du terrorisme, selon InDaily.", 'indaily_austrac_2015', '2015', 'Australie', "Les enquêtes menées à l'étranger n'ont pas trouvé de lien.", 'estimation'),
 ],
 court="Aucune preuve : la certification halal est organisée par trois mosquées agréées par l'État et des organismes privés, avec des prélèvements de quelques centimes par kilo. Le Sénat a même écarté l'idée d'une taxe halal. La filière manque de transparence, c'est vrai, mais opacité n'est pas financement de l'islamisme.",
 moyen="En France, l'abattage rituel est soumis à l'autorisation de l'État, et les sacrificateurs sont agréés via trois mosquées, à Paris, Évry et Lyon. Les prélèvements connus sont modestes : environ 15 centimes par kilo à Lyon selon un chercheur. En 2016, le Sénat a écarté l'idée d'une taxe halal, jugée inconstitutionnelle.\n\nCe qui est vrai, c'est que la filière manque de transparence, qu'il n'y a pas de norme commune et que la Grande Mosquée de Paris est liée à l'Algérie. Les financements privés étrangers du culte sont mal connus, selon le même rapport. Mais aucune enquête lue ne montre que l'argent du halal finance l'islamisme ou le terrorisme ; en Australie, le renseignement financier n'a trouvé aucun lien. Exiger la transparence, oui ; transformer chaque client d'une boucherie halal en financeur du terrorisme, non.",
 detaille="Le halal en France est un marché encadré. Depuis 1997, l'État agrée les sacrificateurs via trois mosquées, à Paris, Évry et Lyon, et un décret de 2012 soumet chaque abattage rituel à autorisation. À côté, des certificateurs privés vendent leur label. Les sommes connues sont modestes : un accord de 1995 prévoyait un franc par kilo pour la Grande Mosquée de Paris, et la Mosquée de Lyon prélevait environ 15 centimes par kilo de viande contrôlée selon La Vie des idées.\n\nLe Sénat a examiné la question en 2016, dans un rapport transpartisan sur le financement de l'islam. Il dénonce un « halal business » sans norme commune et un oligopole des mosquées agréées, dont la Grande Mosquée de Paris, « sous autorité algérienne ». Il écarte une taxe halal publique, inconstitutionnelle, mais juge possible une redevance gérée par le culte, idée reprise en 2018 par le rapport El Karoui pour financer la formation des imams. Il indique que le culte est financé essentiellement par les fidèles, que des États étrangers versent des sommes connues, et que les financements privés étrangers sont impossibles à connaître.\n\nAucune des sources lues ne relie la filière halal au financement de l'islamisme ou du terrorisme. En Australie, une commission sénatoriale a entendu le renseignement financier, qui n'a trouvé aucun lien. Le vrai débat porte sur la transparence de la filière et sur l'influence des États étrangers : il mérite mieux qu'un soupçon jeté sur les musulmans qui font leurs courses.",
 empathie="L'opacité de la filière halal et l'influence de certains États étrangers sur le culte peuvent légitimement inquiéter. C'est justement une raison de s'en tenir à ce qui est documenté.",
 legitimes=["La filière halal manque de transparence et de norme commune.", "Une partie du financement du culte vient d'États étrangers, et les dons privés étrangers sont mal connus."],
 contre=[
  ("Les certificateurs privés ne publient pas leurs comptes.", "C'est un vrai problème de transparence ; mais l'absence de transparence ne prouve pas un financement de l'islamisme."),
  ("La Grande Mosquée de Paris est contrôlée par l'Algérie.", "Le Sénat la décrit comme « sous autorité algérienne » ; c'est une question d'influence étrangère sur le culte, pas de terrorisme."),
 ],
 questions=["Sur quelle enquête repose l'idée que le halal finance l'islamisme ?", "Faudrait-il exiger la publication des comptes des certificateurs halal ?"],
 limites=["Les principales sources datent de 2012 à 2016.", "Les rapports complets du Sénat et de l'Assemblée sur l'abattage n'ont pas été lus, seulement la synthèse.", "Aucun fact-check français récent sur ce point n'a été trouvé ; la source australienne porte sur un autre pays."],
 publics={'convaincus': "En 2016, le Sénat, droite comprise, a enquêté sur le financement de l'islam : il dénonce l'opacité du halal, mais ne parle pas de financement du terrorisme. Les prélèvements connus, c'est quelques centimes par kilo pour faire tourner des mosquées. Exige la transparence si tu veux, je te suis ; mais accuser ceux qui achètent leur viande, c'est autre chose.",
  'indecis': "La filière halal manque de transparence et certaines mosquées sont liées à des États étrangers : ce sont des questions sérieuses. Mais aucune enquête lue ne montre que cet argent finance l'islamisme. Demander plus de transparence ne doit pas devenir un soupçon contre tous les musulmans."},
 a_actualiser='2027-11-08', raison="Nouveau rapport public sur le financement du culte ou la filière halal.",
))

# ══ Lot E : services publics, international, société ══════════════════════

# 21 ── Gratuité des transports ────────────────────────────────────────────
PUBLICSENAT_GRATUITE_2019 = ('publicsenat_gratuite_2019', src('Gratuité des transports : plus adaptée pour les villes petites et moyennes, selon un rapport du Sénat', 'Public Sénat', '26 septembre 2019',
  'https://www.publicsenat.fr/actualites/politique/gratuite-des-transports-plus-adaptee-pour-les-villes-petites-et-moyennes-selon',
  "Le rapport de la mission d'information (rapporteur Guillaume Gontard, présidente Michèle Vullien) est adopté à l'unanimité. 29 communes ou intercommunalités pratiquent la gratuité totale, dont Dunkerque, Niort et Châteauroux. Guillaume Gontard : « Elle ne doit pas s'appliquer partout de la même manière. » Quand la billetterie représente « 25 ou 30 % du budget des transports », la gratuité devient complexe ; dans les villes où bus et métros sont pleins, il faut d'abord développer l'offre.",
  'Média parlementaire public.', 'media'))
SENAT_GRATUITE_CP_2019 = ('senat_gratuite_cp_2019', src("La mission d'information sur la gratuité des transports collectifs adopte son rapport à l'unanimité", 'Sénat (communiqué de presse)', '26 septembre 2019',
  'https://www.senat.fr/presse/cp20190926.html',
  "Rapport adopté le 25 septembre 2019 ; la mission avait été créée à l'initiative du groupe communiste. Huit recommandations, dont « dépassionner le débat », penser la gratuité totale comme un outil d'une politique globale en veillant à sa soutenabilité, sortir de l'opposition entre gratuité et développement de l'offre, et revenir à une TVA de 5,5 % sur les transports de voyageurs.",
  'Communiqué officiel du Sénat.', 'primaire'))
LOCALTIS_COUR_GRATUITE_2025 = ('localtis_cour_gratuite_2025', src('Transports collectifs urbains : la gratuité peut coûter cher, pointe la Cour des comptes', 'Localtis / Banque des Territoires (Anne Lenormand)', '15 septembre 2025',
  'https://www.banquedesterritoires.fr/transports-collectifs-urbains-la-gratuite-peut-couter-cher-pointe-la-cour-des-comptes',
  "En 2019, « les recettes tarifaires ne couvraient que 41 % des seules dépenses de fonctionnement des réseaux de transport » : 45 % en Île-de-France, 33 % ailleurs, 18 % pour les autorités de moins de 100 000 habitants. Il y a « une quarantaine » de réseaux gratuits, dont Dunkerque, Aubagne, Compiègne et la métropole de Montpellier. La Cour pointe des « pertes de recettes significatives » dans les grands réseaux.",
  "Média des collectivités, qui rend compte d'un rapport de la Cour des comptes.", 'media'))
WEKA_AFP_GRATUITE_2025 = ('weka_afp_gratuite_2025', src('Gratuité des transports en commun : la Cour des comptes pointe les effets négatifs', 'Weka (dépêche AFP)', '17 septembre 2025',
  'https://www.weka.fr/actualite/?p=203904',
  "Sur les grands réseaux, la gratuité a des effets financiers négatifs et ne produit qu'un report limité des automobilistes ; sur les petits réseaux, souvent presque vides, elle peut accroître la fréquentation à coût limité. Les nouveaux usagers viennent davantage de la marche et du vélo que de la voiture. La Cour qualifie la mesure de « très coûteuse ».",
  'Dépêche AFP.', 'media'))
LOCALTIS_MONTPELLIER_2024 = ('localtis_montpellier_2024', src('Transports en commun gratuits à Montpellier : la fréquentation en hausse', 'Localtis / Banque des Territoires (Anne Lenormand, avec l’AFP)', '15 mai 2024',
  'https://www.banquedesterritoires.fr/transports-en-commun-gratuits-montpellier-la-frequentation-en-hausse',
  "Fréquentation en hausse de 23,7 % au premier trimestre 2024 par rapport au premier trimestre 2019, soit « cinq millions de déplacements dans les transports en plus », avec un changement de méthode de comptage. 86 000 abonnés avant la gratuité, 358 000 titulaires du passe gratuité. « Avec un taux de 2 % de la masse salariale, le VM a rapporté 116 millions d'euros en 2023. »",
  'Média des collectivités ; chiffres de la métropole.', 'media'))

FICHES.append(fiche(
 id='gratuite-transports-irrealiste', affirmation="La gratuité des transports publics, c'est irréaliste.", volet='services', sous_theme='Transports collectifs',
 mots_cles=['gratuite des transports', 'transports gratuits', 'transports en commun gratuits', 'bus gratuits', 'gratuite des bus', 'transport gratuit'],
 verdict='trompeur', fiabilite='etabli',
 resume="La gratuité fonctionne déjà dans une quarantaine de réseaux en France, dont Dunkerque depuis 2018 et la métropole de Montpellier depuis fin 2023. Les billets ne couvraient en 2019 que 41 % des dépenses de fonctionnement en moyenne, et 18 % dans les petits réseaux. Mais la Cour des comptes juge la mesure « très coûteuse » dans les grands réseaux, avec peu d'automobilistes attirés ; le Sénat la juge plus adaptée aux villes petites et moyennes.",
 contexte="La gratuité des transports figure dans plusieurs programmes municipaux de gauche et écologistes et est souvent présentée comme une promesse démagogique.",
 explication="La question n'est pas de savoir si c'est possible, puisque cela existe, mais où et à quel coût.",
 sources=[PUBLICSENAT_GRATUITE_2019, SENAT_GRATUITE_CP_2019, LOCALTIS_COUR_GRATUITE_2025, WEKA_AFP_GRATUITE_2025, LOCALTIS_MONTPELLIER_2024],
 faits=[
  fait("D'après la Cour des comptes, une quarantaine de réseaux de transport sont entièrement gratuits en France, dont Dunkerque, Aubagne, Compiègne et la métropole de Montpellier.", 'localtis_cour_gratuite_2025', '2025', 'France', "La gratuité existe et fonctionne dans de nombreuses villes.", 'etabli'),
  fait("En 2019, les recettes de billetterie couvraient 41 % des dépenses de fonctionnement des réseaux, 33 % hors Île-de-France et 18 % dans les réseaux de moins de 100 000 habitants.", 'localtis_cour_gratuite_2025', '2019', 'France', "Les usagers ne financent déjà qu'une partie du coût.", 'etabli', '41 %'),
  fait("À Montpellier, gratuite pour ses habitants, la fréquentation a augmenté de 23,7 % au premier trimestre 2024 par rapport à 2019, avec un changement de méthode de comptage ; le versement mobilité des employeurs a rapporté 116 M€ en 2023.", 'localtis_montpellier_2024', '2019-2024', 'Montpellier', "Une grande métropole a mis en place la gratuité.", 'etabli'),
  fait("Selon la Cour des comptes, la gratuité est « très coûteuse » dans les grands réseaux et attire surtout des piétons et des cyclistes plutôt que des automobilistes.", 'weka_afp_gratuite_2025', '2025', 'France', "L'effet écologique est limité dans les grands réseaux : c'est un fait défavorable.", 'etabli'),
  fait("Une mission d'information du Sénat a jugé en 2019, à l'unanimité, la gratuité plus adaptée aux villes petites et moyennes, et complexe quand la billetterie pèse 25 à 30 % du budget.", 'publicsenat_gratuite_2019', '2019', 'France', "La gratuité dépend du contexte local.", 'etabli'),
 ],
 court="Ce n'est pas irréaliste puisque ça existe : une quarantaine de réseaux sont gratuits, dont Dunkerque et Montpellier. Les billets ne paient qu'une partie du coût. Mais dans les grandes villes saturées, la Cour des comptes la juge très coûteuse : c'est un choix politique à faire selon les villes.",
 moyen="La gratuité existe : Dunkerque depuis 2018, la métropole de Montpellier depuis fin 2023, et une quarantaine de réseaux au total. Elle est possible parce que les billets ne couvraient en 2019 que 41 % des dépenses de fonctionnement, et seulement 18 % dans les petits réseaux ; le reste vient déjà du versement mobilité payé par les employeurs et des impôts locaux.\n\nLes limites sont réelles. La Cour des comptes juge la gratuité « très coûteuse » dans les grands réseaux, avec peu d'automobilistes qui laissent leur voiture. Le Sénat, à l'unanimité, la juge plus adaptée aux villes petites et moyennes. Ce n'est donc ni une utopie ni une solution universelle : c'est un choix de service public, à adapter selon les villes.",
 detaille="La gratuité totale des transports publics n'est pas une idée théorique. Selon la Cour des comptes, une quarantaine de réseaux sont entièrement gratuits, dont Dunkerque, Aubagne, Compiègne et la métropole de Montpellier avec ses 31 communes. À Montpellier, 358 000 habitants ont le passe gratuit, contre 86 000 abonnés auparavant, et la fréquentation a augmenté de 23,7 % au premier trimestre 2024 par rapport à 2019, avec un changement de méthode de comptage.\n\nC'est possible parce que les usagers ne paient déjà qu'une partie du coût. En 2019, les recettes tarifaires couvraient 41 % des dépenses de fonctionnement en moyenne, 33 % hors Île-de-France et 18 % dans les réseaux de moins de 100 000 habitants. Le reste vient du versement mobilité, payé par les employeurs (116 M€ à Montpellier en 2023), et des budgets locaux.\n\nLes limites sont documentées. La Cour des comptes juge la mesure « très coûteuse » dans les grands réseaux et constate que les nouveaux usagers viennent davantage de la marche et du vélo que de la voiture. Une mission sénatoriale, créée à l'initiative des communistes et adoptée à l'unanimité, la juge plus adaptée aux villes petites et moyennes, et recommande de ne pas opposer gratuité et développement de l'offre. La gratuité est donc un choix politique, qui fait du transport un service public comme l'école : réaliste dans beaucoup de villes, à manier avec prudence dans les métropoles saturées.",
 empathie="On peut craindre que ce qui est gratuit soit en réalité payé par les impôts de tous, et c'est une question légitime. La réponse dépend de chaque ville et de la façon dont le réseau est financé.",
 legitimes=["La gratuité est très coûteuse dans les grands réseaux selon la Cour des comptes.", "Elle attire peu d'automobilistes dans les grandes villes."],
 contre=[
  ("Rien n'est gratuit, ce sont nos impôts.", "C'est vrai : la gratuité est financée par les employeurs et les budgets locaux, comme l'école ou les routes. La question est de savoir si on préfère ce financement collectif."),
  ("Paris ne pourrait jamais le faire.", "Le Sénat et la Cour des comptes le disent aussi : dans les réseaux saturés, il faut d'abord développer l'offre."),
 ],
 questions=["Savais-tu que les billets ne couvrent qu'une partie du coût des transports, même quand ils sont payants ?", "Dans ta ville, la priorité serait-elle la gratuité ou plus de bus ?"],
 limites=["Le rapport de la Cour des comptes de 2025 a été lu à travers Localtis et l'AFP.", "La hausse de fréquentation à Montpellier mélange deux méthodes de comptage.", "Le chiffre des réseaux gratuits varie selon les sources et les années (29 en 2019, une quarantaine en 2025)."],
 publics={'convaincus': "Irréaliste ? Dunkerque le fait depuis 2018, Montpellier depuis 2023, et une quarantaine de villes au total. Les billets ne paient de toute façon que 41 % du fonctionnement en moyenne. Dans les grandes villes saturées, c'est plus compliqué, et je te l'accorde.",
  'indecis': "La gratuité fonctionne dans beaucoup de villes moyennes, parce que les billets ne financent qu'une petite partie du réseau. Dans les grandes métropoles, la Cour des comptes la juge très coûteuse et peu efficace pour réduire la voiture. C'est un choix à faire ville par ville."},
 a_actualiser='2027-09-30', raison="Nouveaux réseaux gratuits et évaluations.",
))

# 22 ── Droits de douane de Trump ──────────────────────────────────────────
FED_TARIFS_2019 = ('fed_tarifs_2019', src('Disentangling the Effects of the 2018-2019 Tariffs on a Globally Connected U.S. Manufacturing Sector', 'Federal Reserve Board, série FEDS (Aaron Flaaen, Justin Pierce)', 'décembre 2019',
  'https://federalreserve.gov/econres/feds/disentangling-the-effects-of-the-2018-2019-tariffs-on-a-globally-connected-us-manufacturing-sector.htm',
  "Les auteurs séparent trois canaux : la protection des industries nationales, la hausse du coût des intrants importés et les représailles des partenaires commerciaux. Les industries les plus exposées aux tarifs connaissent une baisse relative de l'emploi manufacturier : l'effet positif de la protection est plus que compensé par le coût des intrants et les représailles. Les tarifs sont aussi associés à une hausse relative des prix à la production. (Résumé paraphrasé.)",
  'Étude d’économistes de la Réserve fédérale.', 'etude'))
PIIE_ACIER_2018 = ('piie_acier_2018', src("Steel Profits Gain, but Steel Users Pay, under Trump's Protectionism", 'Peterson Institute for International Economics (Gary Clyde Hufbauer, Euijin Jung)', '20 décembre 2018',
  'https://piie.com/blogs/trade-investment-policy-watch/steel-profits-gain-steel-users-pay-under-trumps-protectionism',
  "« Yes, these actions create 8,700 jobs in the US steel industry. » Les utilisateurs d'acier paient un surcoût de 5,6 Md$ ; les bénéfices des sidérurgistes augmentent de 2,4 Md$ en 2018. Cela représente 650 000 $ payés par les utilisateurs pour chaque emploi créé.",
  'Think tank favorable au libre-échange (orientation à signaler).', 'etude'))
UCHICAGO_LAVELINGE_2019 = ('uchicago_lavelinge_2019', src('What washing machines can teach us about the cost of tariffs', 'University of Chicago News (David Fettig), sur l’étude de Flaaen, Hortaçsu et Tintelnot', '22 avril 2019',
  'https://news.uchicago.edu/story/what-washing-machines-can-teach-us-about-cost-tariffs',
  "Les tarifs de 2018 sur les lave-linge ont relocalisé de la production et créé de « new jobs » aux États-Unis. Le prix des lave-linge a augmenté d'« about 12 percent », et les sèche-linge, non taxés, ont augmenté d'autant. Coût estimé : « $820,000 per new job ».",
  'Présentation universitaire d’une étude.', 'secondaire'))
KIEL_TARIFS_2026 = ('kiel_tarifs_2026', src("America's own goal: Americans pay almost entirely for Trump's tariffs", 'Institut de Kiel pour l’économie mondiale (Hinz, Lohmann, Mahlkow, Vorwig), communiqué publié sur idw', '19 janvier 2026',
  'https://nachrichten.idw-online.de/2026/01/19/america-s-own-goal-americans-pay-almost-entirely-for-trumps-tariffs',
  "« Importers and consumers in the US bear 96 percent of the tariff burden. » « Foreign exporters absorbed only about four percent. » « US customs revenue increased by approximately 200 billion US dollars in 2025. » Méthode : plus de 25 millions d'expéditions analysées.",
  'Institut de recherche économique allemand reconnu.', 'etude'))
CBO_TARIFS_2025 = ('cbo_tarifs_2025', src('Budgetary and Economic Effects of Increases in Tariffs Implemented Between January 6 and May 13, 2025', 'Congressional Budget Office (organe budgétaire non partisan du Congrès américain)', '4 juin 2025',
  'https://www.cbo.gov/publication/61389',
  "Sur 2025-2035, les tarifs réduiraient le déficit de 2 800 Md$ après effets économiques. La production réelle baisserait en net. L'inflation augmenterait de 0,4 point par an en moyenne en 2025 et 2026, ce qui réduit « the purchasing power of households and businesses ».",
  'Organe budgétaire officiel et non partisan.', 'primaire'))
EPI_EMPLOI_MANUF_2026 = ('epi_emploi_manuf_2026', src('Cumulative change in manufacturing employment since January 2025', 'Economic Policy Institute, d’après les données du Bureau of Labor Statistics', 'données jusqu’en juin 2026',
  'https://www.epi.org/chart/jobs-day-figure-cumulative-change-in-manufacturing-employment-since-january-2025/',
  "Variation cumulée de l'emploi manufacturier depuis janvier 2025 : -11 en avril 2025, -93 en décembre 2025, -75 en juin 2026 (unité non précisée sur la page, vraisemblablement en milliers).",
  'Think tank proche des syndicats (orientation à signaler) ; données du BLS.', 'secondaire'))

FICHES.append(fiche(
 id='trump-droits-douane-ouvriers', affirmation="Les droits de douane de Trump protègent les ouvriers américains.", volet='international', sous_theme='États-Unis',
 mots_cles=['droits de douane trump', 'tarifs douaniers trump', 'trump droits de douane', 'protectionnisme trump', 'trump protege les ouvriers', 'guerre commerciale trump'],
 verdict='trompeur', fiabilite='estimation',
 resume="Les droits de douane ont protégé quelques secteurs : environ 8 700 emplois dans la sidérurgie en 2018, de nouvelles usines de lave-linge. Mais chaque emploi a coûté 650 000 à 820 000 dollars aux consommateurs et aux entreprises, et des économistes de la Réserve fédérale trouvent un effet net négatif sur l'emploi manufacturier, à cause du coût des intrants et des représailles. En 2025, les importateurs et consommateurs américains ont supporté 96 % du coût des tarifs selon l'Institut de Kiel.",
 contexte="Les droits de douane de Donald Trump (2018-2019, puis 2025) sont présentés par une partie de l'extrême droite européenne comme un modèle de protection des travailleurs.",
 explication="Il faut distinguer l'effet sur les secteurs protégés et l'effet sur l'ensemble de l'industrie et des ménages.",
 sources=[FED_TARIFS_2019, PIIE_ACIER_2018, UCHICAGO_LAVELINGE_2019, KIEL_TARIFS_2026, CBO_TARIFS_2025, EPI_EMPLOI_MANUF_2026],
 faits=[
  fait("Selon des économistes de la Réserve fédérale, les tarifs de 2018-2019 ont réduit relativement l'emploi manufacturier dans les industries les plus exposées : la protection a été plus que compensée par le coût des intrants et les représailles.", 'fed_tarifs_2019', '2018-2019', 'États-Unis', "L'effet net sur l'emploi industriel a été négatif.", 'estimation'),
  fait("Selon le Peterson Institute, les tarifs sur l'acier ont créé environ 8 700 emplois dans la sidérurgie, pour un surcoût de 5,6 Md$ pour les industries utilisatrices, soit 650 000 $ par emploi.", 'piie_acier_2018', '2018', 'États-Unis', "Quelques emplois protégés, à un coût très élevé.", 'estimation', '650 000 $'),
  fait("Selon une étude présentée par l'université de Chicago, les tarifs sur les lave-linge ont créé des emplois mais fait monter leur prix d'environ 12 %, pour un coût d'environ 820 000 $ par emploi créé.", 'uchicago_lavelinge_2019', '2018', 'États-Unis', "Les consommateurs ont payé la protection.", 'estimation', '12 %'),
  fait("Selon l'Institut de Kiel, les importateurs et consommateurs américains ont supporté 96 % du coût des droits de douane en 2025, les exportateurs étrangers environ 4 %.", 'kiel_tarifs_2026', '2025', 'États-Unis', "Ce sont les Américains qui paient les tarifs.", 'estimation', '96 %'),
  fait("Selon le Congressional Budget Office, les tarifs de 2025 réduiraient le déficit de 2 800 Md$ sur dix ans, mais augmenteraient l'inflation de 0,4 point par an en 2025 et 2026 et réduiraient la production.", 'cbo_tarifs_2025', '2025-2035', 'États-Unis', "Les tarifs rapportent des recettes, mais pèsent sur le pouvoir d'achat : un fait à présenter en entier.", 'estimation'),
  fait("D'après les données du Bureau of Labor Statistics mises en forme par l'Economic Policy Institute, l'emploi manufacturier américain a baissé depuis janvier 2025 (environ -75 000 en juin 2026).", 'epi_emploi_manuf_2026', '2025-2026', 'États-Unis', "L'emploi industriel n'a pas progressé depuis les nouveaux tarifs ; c'est une corrélation, pas une preuve causale.", 'estimation'),
 ],
 court="Quelques secteurs ont gagné des emplois, comme l'acier, mais à 650 000 dollars l'emploi payés par les autres. Selon la Réserve fédérale, l'emploi industriel a globalement baissé dans les secteurs exposés. Et en 2025, ce sont les Américains qui ont payé 96 % des tarifs.",
 moyen="Les droits de douane protègent bien certains secteurs. En 2018, ceux sur l'acier ont créé environ 8 700 emplois, ceux sur les lave-linge de nouvelles usines. Mais chaque emploi a coûté entre 650 000 et 820 000 dollars aux entreprises et aux consommateurs, avec des lave-linge 12 % plus chers.\n\nSurtout, des économistes de la Réserve fédérale ont montré que l'industrie dans son ensemble y a perdu : les entreprises qui achètent de l'acier payent plus cher et subissent les représailles des autres pays. En 2025, selon l'Institut de Kiel, 96 % du coût des nouveaux tarifs a été payé par les Américains eux-mêmes, et l'emploi manufacturier a baissé. Protéger les ouvriers, c'est possible, mais par des politiques industrielles et sociales, pas par une taxe qui retombe sur eux.",
 detaille="Les droits de douane ont des gagnants visibles. Selon le Peterson Institute, les tarifs de 2018 sur l'acier ont créé environ 8 700 emplois dans la sidérurgie et augmenté les bénéfices des sidérurgistes de 2,4 Md$. Selon une étude présentée par l'université de Chicago, les tarifs sur les lave-linge ont relocalisé de la production. Mais le coût est énorme : environ 650 000 $ par emploi dans l'acier, 820 000 $ dans les lave-linge, dont le prix a augmenté d'environ 12 %.\n\nLes perdants sont moins visibles mais plus nombreux. Des économistes de la Réserve fédérale ont séparé trois effets : la protection, le coût plus élevé des pièces importées et les représailles des partenaires. Résultat : dans les industries les plus exposées, l'emploi manufacturier a baissé relativement. En 2025, l'Institut de Kiel estime que les importateurs et consommateurs américains ont payé 96 % du coût des nouveaux tarifs. Le Congressional Budget Office prévoit 0,4 point d'inflation en plus par an en 2025 et 2026 et une production en baisse, même si les tarifs réduiraient le déficit de 2 800 Md$ sur dix ans.\n\nSelon les données du Bureau of Labor Statistics, l'emploi manufacturier a reculé d'environ 75 000 postes entre janvier 2025 et juin 2026, sans qu'on puisse attribuer toute cette baisse aux tarifs. Défendre l'industrie et les ouvriers est légitime ; la gauche le propose par la planification, l'investissement public et des normes sociales et écologiques aux frontières, pas par une taxe payée surtout par les classes populaires.",
 empathie="Les ouvriers qui ont vu leur usine délocalisée ont raison d'en vouloir au libre-échange sans règles. La question est de savoir si les tarifs de Trump les ont réellement protégés.",
 legitimes=["Certains secteurs, comme l'acier, ont gagné des emplois.", "Les tarifs rapportent d'importantes recettes publiques."],
 contre=[
  ("Le libre-échange a détruit l'industrie, il faut se protéger.", "Le libre-échange sans règles a fait des dégâts ; mais des tarifs généralisés renchérissent les pièces et provoquent des représailles qui coûtent d'autres emplois."),
  ("Ce sont les Chinois qui paient.", "Selon l'Institut de Kiel, les importateurs et consommateurs américains ont payé 96 % du coût en 2025."),
 ],
 questions=["Savais-tu que chaque emploi sauvé dans l'acier a coûté environ 650 000 dollars aux autres entreprises ?", "Qui paie un droit de douane, selon toi : l'exportateur étranger ou l'acheteur ?"],
 limites=["L'étude de la Réserve fédérale a été lue à travers un résumé paraphrasé.", "La baisse de l'emploi manufacturier depuis 2025 est une corrélation ; plusieurs causes jouent.", "Le Peterson Institute est favorable au libre-échange et l'Economic Policy Institute proche des syndicats."],
 publics={'convaincus': "Dans l'acier, les tarifs ont créé 8 700 emplois, d'accord, mais chacun a coûté 650 000 dollars aux autres entreprises. La Réserve fédérale a calculé que l'emploi industriel a baissé dans les secteurs exposés. Et en 2025, ce sont les Américains qui ont payé 96 % des tarifs, pas les Chinois.",
  'indecis': "Vouloir protéger l'industrie est légitime après des décennies de délocalisations. Mais les études montrent que les tarifs de Trump ont sauvé quelques emplois à un coût énorme, en renchérissant les produits et en provoquant des représailles. D'autres outils existent, comme l'investissement industriel."},
 a_actualiser='2027-06-30', raison="Nouvelles évaluations des tarifs de 2025.",
))

# 23 ── Aide à l'Ukraine et corruption ─────────────────────────────────────
POLITIFACT_YACHTS_2024 = ('politifact_yachts_2024', src("Did Volodymyr Zelenskyy use US aid to buy yachts? No, that's False", 'PolitiFact (Sara Swann)', '21 février 2024',
  'https://www.politifact.com/factchecks/2024/feb/21/instagram-posts/did-volodymyr-zelenskyy-use-us-aid-to-buy-yachts-n',
  "Verdict : « False ». La rumeur vient d'un podcast du 27 novembre 2023, ensuite retiré. Les documents d'achat sont fabriqués : ils utilisent l'ancien nom et l'ancien logo de l'association de courtiers, rebaptisée en 2008. Les deux yachts étaient encore en vente en février 2024. L'aide économique passe par la Banque mondiale, l'aide humanitaire par des ONG.",
  'Fact-checker américain reconnu.', 'media'))
VOA_100MDS_2025 = ('voa_100mds_2025', src("False: Russian allegations that Ukraine 'stole' $100 billion of US funds", 'Voice of America, Polygraph (Leonid Martynyuk)', '7 février 2025',
  'https://www.voanews.com/a/false-russian-allegations-that-ukraine-stole-100-billion-of-us-funds/7967072.html',
  "L'affirmation de Dmitri Medvedev est jugée fausse : elle déforme une interview où Zelensky disait avoir reçu 76 Md$ d'aide militaire. Selon le Council on Foreign Relations, le Congrès a voté 175 Md$, dont 106 Md$ d'aide directe. Une analyse du Washington Post (novembre 2023) estime que près de 90 % des 68 Md$ d'aide militaire bénéficient à des travailleurs américains.",
  'Média public américain (prudence sur les sujets liés à la Russie).', 'media'))
KYIVINDEPENDENT_OIG_2024 = ('kyivindependent_oig_2024', src('Pentagon watchdog: US did not track all weapons sent to Ukraine', 'Kyiv Independent (Abbey Fenbert)', '12 janvier 2024',
  'https://kyivindependent.com/pentagon-watchdog-us-did-not-track-all-weapons-sent-to-ukraine/',
  "Selon l'inspecteur général du Pentagone, sur 1,699 Md$ d'équipements soumis à un suivi renforcé, 1,005 Md$ restait non suivi en juin 2023. Le rapport précise : « It was beyond the scope of our evaluation to determine whether there has been diversion of such assistance. » Le Pentagone affirme qu'il n'y a « no credible evidence of illicit diversion ».",
  'Média ukrainien (non neutre sur le conflit), qui rapporte un rapport officiel américain.', 'media'))
EURONEWS_MIDAS_2025 = ('euronews_midas_2025', src("Operation « Midas »: All you need to know about anti-corruption investigation in Ukraine", 'Euronews (Sasha Vakulina)', '15 novembre 2025',
  'https://euronews.com/2025/11/15/operation-midas-all-you-need-to-know-about-anti-corruption-investigation-in-ukraine',
  "Selon le Bureau national anticorruption ukrainien (NABU), « Around $100 million in funds was laundered » via des pots-de-vin de 10 à 15 % sur les contrats d'Energoatom, l'opérateur nucléaire public. Le chef présumé, Timour Mindich, est un ancien associé de Zelensky. Deux ministres ont démissionné ; environ 70 perquisitions et huit inculpations. L'article ne relie pas ces fonds à l'aide occidentale.",
  'Média européen.', 'media'))
TIUKRAINE_CPI_2025 = ('tiukraine_cpi_2025', src('Corruption Perceptions Index 2025 (analyse)', 'Transparency International Ukraine', '2026',
  'https://ti-ukraine.org/en/research/corruption-perceptions-index-2025/',
  "L'Ukraine obtient 36/100 et se classe 104e sur 182 pays : « Ukraine matched its CPI 2023 result », avec une « very restrained progress ». L'indice mesure la perception de la corruption, pas son niveau réel.",
  'Section nationale d’une ONG internationale de référence.', 'primaire'))

GAO_UKRAINE_2024 = ('gao_ukraine_2024', src('Ukraine: DOD Should Improve Data for Both Defense Article Delivery and End-Use Monitoring (GAO-24-106289)', 'U.S. Government Accountability Office (Cour des comptes fédérale américaine)', '13 mars 2024',
  'https://www.gao.gov/assets/gao-24-106289.pdf',
  "Depuis février 2022, « the U.S. has provided more than $42 billion in security assistance ». Les données de livraison sont peu fiables : sur 135 articles prioritaires, 71 étaient marqués comme livrés alors que le commandement en Europe attendait confirmation. « DOD has delivered at least $10 billion worth of routine EUM items to Ukraine », sans pouvoir savoir s'ils ont été perdus ou détruits. Le GAO fait 8 recommandations ; le Pentagone en accepte 5, 2 en partie et en rejette 1.",
  "Organe de contrôle officiel du Congrès américain (lecture d'environ 100 000 caractères sur 120 000).", 'primaire'))

FICHES.append(fiche(
 id='ukraine-aide-corruption', affirmation="L'aide à l'Ukraine est détournée par la corruption.", volet='international', sous_theme='Guerres et conflits',
 mots_cles=['aide a l ukraine detournee', 'corruption en ukraine', 'ukraine corruption', 'zelensky yachts', 'argent detourne ukraine', 'ukraine corrompue'],
 verdict='trompeur', fiabilite='estimation',
 resume="La corruption est un problème réel en Ukraine : l'affaire Energoatom de 2025, environ 100 millions de dollars blanchis selon le Bureau anticorruption ukrainien, a touché l'entourage de Volodymyr Zelensky et fait tomber deux ministres. Mais aucun détournement massif de l'aide occidentale n'a été établi : les rumeurs emblématiques (yachts de Zelensky, « 100 milliards volés ») sont fausses, une grande partie de l'aide militaire est dépensée aux États-Unis, et le suivi des armes, d'abord lacunaire, n'a pas mis en évidence de détournement.",
 contexte="Le thème de l'aide « détournée » est largement diffusé par la propagande russe et repris par ceux qui veulent arrêter de soutenir l'Ukraine.",
 explication="Il faut distinguer la corruption en Ukraine, réelle et poursuivie, et l'affirmation précise que l'aide occidentale serait détournée.",
 sources=[POLITIFACT_YACHTS_2024, VOA_100MDS_2025, KYIVINDEPENDENT_OIG_2024, GAO_UKRAINE_2024, EURONEWS_MIDAS_2025, TIUKRAINE_CPI_2025],
 faits=[
  fait("Selon PolitiFact, la rumeur selon laquelle Zelensky aurait acheté des yachts avec l'aide américaine repose sur des documents fabriqués ; les yachts étaient encore en vente en février 2024.", 'politifact_yachts_2024', '2023-2024', 'Ukraine', "Les rumeurs les plus diffusées sont fausses.", 'estimation'),
  fait("Selon Voice of America, l'accusation russe d'un vol de 100 milliards de dollars déforme une interview ; d'après une analyse du Washington Post, près de 90 % de l'aide militaire américaine bénéficie à des travailleurs américains.", 'voa_100mds_2025', '2023-2025', 'États-Unis', "Une grande partie de l'aide est dépensée dans les pays donateurs.", 'estimation'),
  fait("Selon le Kyiv Independent, l'inspecteur général du Pentagone n'avait pas pu suivre 1,005 Md$ d'armes sur 1,699 Md$ soumis à suivi renforcé en juin 2023, sans conclure à un détournement.", 'kyivindependent_oig_2024', '2023', 'Ukraine', "Le suivi a été lacunaire : c'est un fait à reconnaître.", 'estimation', '1,005 Md$'),
  fait("La Cour des comptes fédérale américaine (GAO) a jugé en mars 2024 les données de livraison et de suivi des armes peu fiables : au moins 10 Md$ d'équipements à suivi courant ont été livrés sans que le Pentagone puisse savoir s'ils ont été perdus ou détruits ; elle a formulé 8 recommandations.", 'gao_ukraine_2024', '2022-2024', 'États-Unis et Ukraine', "Le contrôle de l'aide a eu des failles documentées, sans que le rapport conclue à un détournement.", 'etabli', '10 Md$'),
  fait("Selon Euronews, le Bureau national anticorruption ukrainien estime à environ 100 M$ les fonds blanchis dans l'affaire Energoatom (2025) ; deux ministres ont démissionné.", 'euronews_midas_2025', '2025', 'Ukraine', "La corruption est réelle et touche le sommet de l'État, mais elle est poursuivie par des institutions ukrainiennes.", 'estimation', '100 M$'),
  fait("Selon Transparency International Ukraine, l'Ukraine obtient 36/100 dans l'indice de perception de la corruption 2025 et se classe 104e sur 182.", 'tiukraine_cpi_2025', '2025', 'Ukraine', "La corruption reste perçue comme élevée.", 'estimation', '36/100'),
 ],
 court="La corruption existe en Ukraine, et un gros scandale a touché l'entourage de Zelensky en 2025. Mais aucun détournement massif de l'aide occidentale n'a été prouvé, et les rumeurs les plus partagées, comme les yachts de Zelensky, sont fausses.",
 moyen="Il ne faut pas nier la corruption : en 2025, le Bureau anticorruption ukrainien a révélé environ 100 millions de dollars blanchis autour d'Energoatom, impliquant un ancien associé de Zelensky, et deux ministres ont démissionné. L'Ukraine reste mal classée par Transparency International.\n\nMais l'affirmation « l'aide est détournée » est autre chose. Les rumeurs les plus partagées, les yachts de Zelensky ou les « 100 milliards volés » évoqués par Medvedev, ont été démenties. Une grande partie de l'aide militaire est dépensée dans les usines américaines. Le suivi des armes a été lacunaire en 2022-2023, mais l'inspecteur général n'a pas conclu à un détournement. Le fait que des enquêteurs ukrainiens fassent tomber des ministres montre plutôt que les contrôles fonctionnent.",
 detaille="La corruption est un vrai problème en Ukraine. Transparency International la classe 104e sur 182 en 2025, avec un score de 36/100 qui stagne. En novembre 2025, l'opération « Midas » du Bureau national anticorruption a mis au jour un système de pots-de-vin de 10 à 15 % sur les contrats d'Energoatom : environ 100 millions de dollars blanchis, un ancien associé de Zelensky soupçonné, deux ministres démissionnaires, environ 70 perquisitions.\n\nCela ne prouve pas que l'aide occidentale soit détournée. Selon Euronews, l'affaire n'est pas reliée à cette aide. Les rumeurs les plus diffusées ont été démenties : selon PolitiFact, les documents d'achat de yachts attribués à Zelensky étaient fabriqués ; selon Voice of America, l'accusation russe d'un vol de 100 milliards déforme une interview. Le Congrès américain a voté 175 Md$, dont 106 Md$ d'aide directe, et une analyse du Washington Post estime que près de 90 % de l'aide militaire bénéficie à des travailleurs américains.\n\nLe contrôle a eu des failles : en juin 2023, l'inspecteur général du Pentagone n'avait pas pu suivre plus d'un milliard de dollars d'équipements sensibles, sans pouvoir dire s'il y avait eu détournement ; le Pentagone affirme n'avoir aucune preuve crédible de détournement, et le suivi s'est amélioré. On peut exiger des contrôles stricts ; mais le récit d'une aide entièrement volée sert surtout ceux qui veulent laisser l'Ukraine seule face à l'invasion.",
 empathie="Il est normal de vouloir savoir où va l'argent public, surtout quand on demande des efforts aux contribuables. La corruption en Ukraine est réelle, et la vigilance l'est aussi.",
 legitimes=["La corruption est réelle en Ukraine et a touché l'entourage du président en 2025.", "Le suivi des armes américaines a été lacunaire en 2022-2023."],
 contre=[
  ("Le scandale Energoatom prouve que tout est pourri.", "Il prouve que la corruption existe, et aussi que des enquêteurs ukrainiens peuvent la poursuivre jusqu'au sommet ; il n'est pas relié à l'aide occidentale."),
  ("On ne sait pas où sont passées les armes.", "Le suivi a eu des failles en 2023, mais l'inspecteur général n'a pas établi de détournement, et le Pentagone dit n'avoir aucune preuve crédible."),
 ],
 questions=["D'où vient l'histoire des yachts de Zelensky que tu as vue passer ?", "Savais-tu que l'essentiel de l'aide militaire américaine est dépensé dans des usines américaines ?"],
 limites=["Aucun fact-check français lisible sur ce point n'a été trouvé ; les sources sont surtout anglophones.", "Voice of America est un média public américain et le Kyiv Independent un média ukrainien, tous deux engagés dans le contexte du conflit.", "Les données portent surtout sur l'aide américaine ; l'aide européenne et française n'a pas été examinée."],
 publics={'convaincus': "La corruption existe en Ukraine, je ne le nie pas : un scandale a fait tomber deux ministres en 2025. Mais c'est la justice ukrainienne qui l'a révélé, et l'affaire n'est pas liée à l'aide occidentale. L'histoire des yachts de Zelensky, elle, reposait sur de faux documents.",
  'indecis': "Vouloir que l'argent public soit contrôlé est légitime, d'autant que la corruption est réelle en Ukraine. Mais les rumeurs de détournement massif ont été démenties, et une grande partie de l'aide est dépensée dans les pays donateurs. Les contrôles ont eu des failles et se sont renforcés."},
 a_actualiser='2027-06-30', raison="Suites judiciaires de l'affaire Energoatom et nouveaux rapports d'inspection.",
))

# 24 ── Agressions de professeurs ──────────────────────────────────────────
DEPP_SIVIS_2025 = ('depp_sivis_2025', src("Les signalements d'incidents graves dans les écoles et établissements publics et privés sous contrat en 2023-2024 (Note d'information n° 25.28)", "DEPP, ministère de l'Éducation nationale (Muriella Rakotobe)", 'mai 2025',
  'https://www.pedagogie.ac-nice.fr/cpe/wp-content/uploads/sites/24/2025/06/depp-ni-2025-28-226812_0.pdf',
  "« 16 incidents graves pour 1 000 élèves ont été signalés dans les collèges et lycées » ; 5 pour 1 000 dans les écoles. Dans le premier degré, « les victimes de ces signalements sont en premier lieu les personnels (54 % des incidents graves déclarés) ». Dans le second degré, 38 % des victimes sont des personnels, contre 45 % d'élèves.",
  'Statistique publique du ministère (copie hébergée par l’académie de Nice).', 'primaire'))
LOCALTIS_SIVIS_2025 = ('localtis_sivis_2025', src("Sécurité à l'école : les incidents graves en hausse, notamment dans les lycées professionnels", 'Localtis / Banque des Territoires (Virginie Fauvel)', '6 mai 2025',
  'https://www.banquedesterritoires.fr/securite-lecole-les-incidents-graves-en-hausse-notamment-dans-les-lycees-professionnels',
  "Collèges et lycées : 16 incidents pour 1 000 élèves en 2023-2024, contre 14 en 2022-2023. Lycées professionnels : « 23 incidents pour 1.000 élèves » contre 20. Les élèves sont auteurs de 91 % des incidents du second degré ; les familles sont impliquées dans un quart des cas à l'école. Le ministère note que la hausse peut aussi refléter une meilleure remontée des informations.",
  'Média des collectivités.', 'media'))
ACTEURSPUBLICS_SIVIS_2026 = ('acteurspublics_sivis_2026', src('Dans les écoles, 61 % des incidents graves déclarés concernent des personnels', 'Acteurs publics (Victoria Beurnez)', '9 mars 2026',
  'https://acteurspublics.fr/articles/dans-les-ecoles-61-des-incidents-graves-declares-concernent-des-personnels/',
  "En 2024-2025 : « 14 incidents graves pour 1000 élèves » dans les collèges et lycées et « 4 pour 1000 élèves » dans les écoles. Les personnels sont concernés par « 61 % des incidents graves déclarés » dans le premier degré, contre 41 % dans le second. Les signalements sont « en léger recul par rapport à l'année scolaire précédente ».",
  'Presse spécialisée de la fonction publique.', 'media'))
DEPP_VECU_2025 = ('depp_vecu_2025', src("Le vécu au travail des personnels du second degré, en 2023-2024 (Note d'information n° 25.47)", "DEPP, ministère de l'Éducation nationale (Radé, Rakotobe, Simon, Traore)", 'juillet 2025',
  'https://www.pedagogie.ac-nice.fr/cpe/wp-content/uploads/sites/24/2025/07/depp-ni-2025-25-47-228592_0.pdf',
  "Enquête du printemps 2024 (35 000 réponses) : 93 % des personnels se sentent respectés par les élèves et 92 % en sécurité dans l'établissement. 57 % ont subi au moins une atteinte dans l'année, surtout arrogance ou mépris (42 %) et contestation d'enseignement (27 %) ; les atteintes physiques concernent 2 % selon le tableau, 4 % selon le texte. Le respect des règles collectives recule de 70 % en 2019 à 63 % en 2024 ; les atteintes sont plus fréquentes en collège REP (65 %).",
  'Statistique publique du ministère (copie hébergée par l’académie de Nice).', 'primaire'))
DEPP_VICTIMATION_2014 = ('depp_victimation_2014', src("Personnels de l'éducation nationale : des métiers exposés aux menaces et aux insultes (Note d'information n° 25)", "DEPP, ministère de l'Éducation nationale, et Insee (Hélène Guedj, Benjamin Beaumont)", 'juillet 2014',
  'https://www.education.gouv.fr/personnels-de-l-education-nationale-des-metiers-exposes-aux-menaces-et-aux-insultes-8420',
  "« 12 % des personnels de l'éducation nationale déclarent être victimes chaque année de menaces ou d'insultes », environ deux fois plus que l'ensemble des actifs. Violences physiques : 0,6 % par an, taux « pas significativement différent de celui des personnes en emploi dans leur ensemble (0,5 %) ».",
  'Statistique publique ; données anciennes (2014).', 'primaire'))

FICHES.append(fiche(
 id='profs-agresses-ecole-violente', affirmation="Les profs se font agresser tous les jours, l'école est devenue violente.", volet='services', sous_theme='École publique',
 mots_cles=['profs agresses', 'professeurs agresses', 'enseignants agresses', 'violence a l ecole', 'ecole violente', 'violence scolaire', 'agressions de professeurs'],
 verdict='trompeur', fiabilite='etabli',
 resume="Les tensions à l'école sont réelles : 57 % des personnels du second degré ont subi au moins une atteinte dans l'année, surtout du mépris et des contestations, et les incidents graves ont augmenté en 2023-2024, notamment en lycée professionnel. Mais les atteintes physiques concernent 2 à 4 % des personnels par an, 92 % se sentent en sécurité dans leur établissement, et les incidents graves ont légèrement reculé en 2024-2025 (14 pour 1 000 élèves au collège et au lycée).",
 contexte="Des drames très médiatisés, comme les assassinats d'enseignants, nourrissent l'idée d'une école livrée à la violence.",
 explication="Les enquêtes du ministère mesurent à la fois les incidents graves signalés et le vécu des personnels : il faut regarder les deux, et distinguer violences verbales et physiques.",
 sources=[DEPP_SIVIS_2025, LOCALTIS_SIVIS_2025, ACTEURSPUBLICS_SIVIS_2026, DEPP_VECU_2025, DEPP_VICTIMATION_2014],
 faits=[
  fait("En 2023-2024, 16 incidents graves pour 1 000 élèves ont été signalés dans les collèges et lycées, contre 14 l'année précédente, et 23 pour 1 000 en lycée professionnel.", 'localtis_sivis_2025', '2022-2024', 'France', "Les incidents graves ont augmenté cette année-là : c'est un fait à reconnaître.", 'etabli', '16 pour 1 000'),
  fait("Dans les écoles primaires, les personnels sont les premières victimes des incidents graves signalés : 54 % en 2023-2024.", 'depp_sivis_2025', '2023-2024', 'France', "Les enseignants du primaire sont particulièrement exposés, souvent avec les familles.", 'etabli', '54 %'),
  fait("D'après Acteurs publics, en 2024-2025, les signalements sont revenus à 14 incidents graves pour 1 000 élèves dans le second degré, en léger recul.", 'acteurspublics_sivis_2026', '2024-2025', 'France', "La hausse ne s'est pas poursuivie.", 'etabli', '14 pour 1 000'),
  fait("Au printemps 2024, 57 % des personnels du second degré déclarent au moins une atteinte dans l'année, surtout arrogance ou mépris (42 %) et contestation d'enseignement (27 %) ; les atteintes physiques concernent 2 à 4 % d'entre eux.", 'depp_vecu_2025', '2023-2024', 'France', "Les atteintes sont surtout verbales ou symboliques.", 'etabli', '57 %'),
  fait("La même enquête indique que 92 % des personnels se sentent en sécurité dans leur établissement et 93 % respectés par les élèves, mais que le respect des règles collectives recule (63 % en 2024 contre 70 % en 2019).", 'depp_vecu_2025', '2019-2024', 'France', "Le climat se dégrade sur certains points sans être celui d'une école violente.", 'etabli', '92 %'),
  fait("En 2014, 12 % des personnels de l'éducation nationale déclaraient des menaces ou insultes chaque année, deux fois plus que les autres actifs, mais 0,6 % des violences physiques, un taux comparable à l'ensemble des actifs.", 'depp_victimation_2014', '2014', 'France', "Les métiers de l'éducation sont exposés aux menaces plus qu'aux coups.", 'etabli'),
 ],
 court="Exagéré : selon le ministère, 2 à 4 % des personnels du second degré subissent une atteinte physique dans l'année, et 92 % se sentent en sécurité. Les tensions sont réelles, surtout le mépris, les contestations et les familles agressives dans le primaire. L'école a besoin de moyens, pas d'un récit de guerre.",
 moyen="Il y a des signaux inquiétants : en 2023-2024, les incidents graves sont passés de 14 à 16 pour 1 000 élèves au collège et au lycée, et 23 en lycée professionnel. Dans le primaire, les personnels sont les premières victimes, souvent face à des familles. Le respect des règles recule.\n\nMais l'enquête du ministère auprès de 35 000 personnels montre que 92 % se sentent en sécurité dans leur établissement. 57 % ont subi au moins une atteinte, surtout du mépris ou des contestations ; les atteintes physiques touchent 2 à 4 % des personnels. En 2024-2025, les incidents graves ont légèrement reculé. Les drames existent et doivent être combattus ; mais décrire l'école comme une zone de violence quotidienne ne correspond pas aux chiffres et décourage ceux qui y travaillent.",
 detaille="Le ministère de l'Éducation nationale suit les incidents graves signalés par les établissements. En 2023-2024, ils atteignaient 16 pour 1 000 élèves dans les collèges et lycées, contre 14 l'année précédente, et 23 pour 1 000 en lycée professionnel. Dans les écoles, 5 incidents pour 1 000 élèves, avec une particularité : les personnels sont les premières victimes (54 %), et les familles sont impliquées dans un quart des cas. En 2024-2025, les signalements sont revenus à 14 pour 1 000 dans le second degré. Le ministère note que les hausses peuvent aussi refléter une meilleure remontée des informations.\n\nL'enquête sur le vécu des personnels du second degré, menée au printemps 2024 auprès de 35 000 personnes, donne une image plus complète. 57 % ont subi au moins une atteinte dans l'année, surtout de l'arrogance ou du mépris (42 %) et des contestations d'enseignement (27 %). Les atteintes physiques concernent 2 à 4 % des personnels. 92 % se sentent en sécurité et 93 % respectés par les élèves. Le respect des règles collectives recule, et les atteintes sont plus fréquentes en éducation prioritaire.\n\nDes données plus anciennes de l'Insee et de la DEPP (2014) montraient déjà que les personnels sont deux fois plus exposés aux menaces et insultes que les autres actifs, mais pas davantage aux violences physiques. Les enseignants ont besoin de soutien face aux contestations et aux familles agressives : classes moins chargées, personnels de vie scolaire, médecine scolaire. L'image d'une école où l'on se fait agresser tous les jours ne les aide pas.",
 empathie="Les enseignants qui ont été insultés ou menacés vivent quelque chose de dur, et les assassinats de professeurs ont marqué tout le pays. Reconnaître ces souffrances n'empêche pas de regarder les chiffres d'ensemble.",
 legitimes=["Les incidents graves ont augmenté en 2023-2024, surtout en lycée professionnel.", "Le respect des règles collectives recule, et les personnels du primaire sont exposés aux familles."],
 contre=[
  ("Les profs n'osent plus signaler, les chiffres sont sous-estimés.", "C'est possible pour les signalements ; c'est pourquoi l'enquête anonyme auprès de 35 000 personnels est utile, et elle montre surtout des atteintes verbales."),
  ("C'est la faute de l'immigration.", "Les sources lues ne donnent pas d'information sur l'origine des auteurs ; elles montrent des écarts selon l'éducation prioritaire et le type d'établissement."),
 ],
 questions=["Savais-tu que 92 % des personnels du second degré se sentent en sécurité dans leur établissement ?", "Qu'est-ce qui aiderait le plus les enseignants face aux contestations : plus de sanctions ou plus d'adultes dans les établissements ?"],
 limites=["Les notes de la DEPP ont été lues sur des copies hébergées par l'académie de Nice ; les pages officielles ne s'ouvraient pas.", "La note de 2025 sur le vécu des personnels contient une incohérence (2 % d'atteintes physiques dans un tableau, 4 % dans le texte).", "L'enquête de victimation des personnels date de 2014."],
 publics={'convaincus': "Les chiffres du ministère sont clairs : 2 à 4 % des personnels du second degré subissent une atteinte physique dans l'année, et 92 % se sentent en sécurité. Il y a du mépris, des contestations et des familles agressives, et c'est grave. Mais « tous les jours », ce n'est pas la réalité des profs.",
  'indecis': "Les tensions à l'école sont réelles : contestations, familles agressives dans le primaire, hausse des incidents en lycée professionnel. Mais les agressions physiques restent rares et la grande majorité des personnels se sentent en sécurité. Les enseignants ont surtout besoin de moyens et de soutien."},
 a_actualiser='2027-06-30', raison="Nouvelle note de la DEPP sur les incidents graves.",
))

# 25 ── Gens du voyage ─────────────────────────────────────────────────────
DDD_GENSDUVOYAGE_2024 = ('ddd_gensduvoyage_2024', src('Lutter contre les discriminations et atteintes aux droits subies par les gens du voyage (fiche 10)', 'Défenseur des droits', '22 avril 2024',
  'https://www.defenseurdesdroits.fr/sites/default/files/2024-04/FICHE10_Gens-du-voyage_20240423.pdf',
  "En 2020, « seulement 77 % des places prescrites par les schémas départementaux étaient réalisées et 22 départements avaient totalement rempli leurs obligations ». En 2023 : « 80,1 % pour les aires d'accueil permanentes, 62,2 % pour les aires de grand passage et 21,3 % pour les terrains familiaux ». Les discriminations « reposent en partie sur la non acceptation du mode de vie itinérant et de l'habitat en caravane ». La Défenseure demande « la reconnaissance de la caravane comme logement » et relève des refus fréquents de domiciliation par les communes.",
  'Autorité administrative indépendante.', 'primaire'))
DDD_GENSDUVOYAGE_FICHE = ('ddd_gensduvoyage_fiche', src('Fiche « Gens du voyage »', 'Défenseur des droits (document hébergé par la préfecture du Bas-Rhin)', 'vers 2012-2015 (non daté)',
  'https://www.bas-rhin.gouv.fr/index.php/contenu/telechargement/29128/199823/file/2015_DDD_fiche_gens_voyage.pdf',
  "Les gens du voyage « possèdent très majoritairement la nationalité française ». Environ 300 000 personnes : un tiers sédentaires, un tiers semi-sédentaires, un tiers itinérants. Les caravanes sont juridiquement des véhicules, ce qui prive leurs habitants des aides au logement.",
  'Autorité administrative indépendante ; données anciennes.', 'primaire'))
LOCALTIS_LIVRET_2017 = ('localtis_livret_2017', src('Gens du voyage : un décret organise la disparition du livret de circulation et consacre la domiciliation', 'Localtis / Banque des Territoires (Jean-Noël Escudié)', '8 novembre 2017',
  'https://www.banquedesterritoires.fr/gens-du-voyage-un-decret-organise-la-disparition-du-livret-de-circulation-et-consacre-la',
  "La loi Égalité et citoyenneté du 27 janvier 2017 supprime le livret de circulation, en abrogeant la loi du 3 janvier 1969. Le décret du 2 novembre 2017 remplace la « commune de rattachement » par une domiciliation auprès d'un CCAS ou d'un organisme agréé. La loi a « revu à la hausse les droits et l'accompagnement des gens du voyage » et renforce aussi les possibilités d'évacuation forcée des campements illicites.",
  'Média des collectivités.', 'media'))
AN_QE_28087 = ('an_qe_28087', src('Question écrite n° 28087 (12e législature) et réponse du ministère de l’Économie', 'Assemblée nationale', 'réponse publiée au JO le 13 juillet 2004',
  'https://questions.assemblee-nationale.fr/dyn/12/questions/QANR5L12QE28087.pdf',
  "Réponse du ministre : « les gens du voyage sont assujettis aux mêmes obligations fiscales et aux mêmes contrôles que les autres contribuables ». Outils cités : contrôle sur pièces, vérification de comptabilité, examen de la situation fiscale personnelle ; l'article 168 du code général des impôts permet de taxer d'après le train de vie.",
  'Réponse ministérielle officielle ; donnée ancienne (2004).', 'primaire'))
AN_QE_81068 = ('an_qe_81068', src('Question écrite n° 81068 (13e législature) et réponse du ministère du Budget', 'Assemblée nationale', 'réponse publiée le 12 octobre 2010',
  'https://www.assemblee-nationale.fr/dyn/13/questions/QANR5L13QE81068.pdf',
  "« Les gens du voyage sont soumis au même traitement fiscal que l'ensemble des contribuables. » Contrôles prévus : vérifications de comptabilité, contrôle des comptes de tiers, échanges d'informations avec les organismes sociaux.",
  'Réponse ministérielle officielle ; donnée ancienne (2010).', 'primaire'))

FICHES.append(fiche(
 id='gens-du-voyage-impots', affirmation="Les gens du voyage ne paient pas d'impôts et ont tous les droits.", volet='droits', sous_theme='Discriminations',
 mots_cles=['gens du voyage', 'voyageurs caravanes', 'gitans impots', 'aires d accueil', 'caravanes impots', 'gens du voyage impots', 'campements illicites'],
 verdict='contredit', fiabilite='etabli',
 resume="Les gens du voyage sont soumis au même régime fiscal que tous les contribuables, avec les mêmes contrôles, y compris le contrôle du train de vie, selon les réponses constantes de Bercy. Ils sont très majoritairement français. Loin d'avoir « tous les droits », ils ont longtemps dû porter un livret de circulation, supprimé seulement en 2017 ; leur caravane n'est pas reconnue comme un logement, et les aires d'accueil prévues par la loi restent incomplètes (62,2 % des aires de grand passage réalisées en 2023). Les installations illicites sont un problème reconnu par la loi, qui a renforcé les évacuations.",
 contexte="Les installations de caravanes sur des terrains non prévus suscitent régulièrement des tensions locales et des accusations générales contre les gens du voyage.",
 explication="Il faut séparer le droit fiscal, qui est le droit commun, les droits réels des gens du voyage et le problème des installations illicites.",
 sources=[AN_QE_28087, AN_QE_81068, DDD_GENSDUVOYAGE_2024, DDD_GENSDUVOYAGE_FICHE, LOCALTIS_LIVRET_2017],
 faits=[
  fait("Le ministère de l'Économie a répondu en 2004 que les gens du voyage sont assujettis aux mêmes obligations fiscales et aux mêmes contrôles que les autres contribuables, y compris la taxation d'après le train de vie.", 'an_qe_28087', '2004', 'France', "Il n'existe aucune exemption fiscale pour les gens du voyage.", 'etabli'),
  fait("En 2010, le ministère du Budget a confirmé qu'ils sont soumis au même traitement fiscal que l'ensemble des contribuables, avec des contrôles spécifiques possibles.", 'an_qe_81068', '2010', 'France', "La position de l'administration fiscale est constante.", 'etabli'),
  fait("Selon le Défenseur des droits, les gens du voyage possèdent très majoritairement la nationalité française ; seul un tiers environ est itinérant.", 'ddd_gensduvoyage_fiche', 'vers 2012-2015', 'France', "Ce sont des citoyens français pour la plupart.", 'etabli'),
  fait("Le livret de circulation imposé aux gens du voyage depuis 1969 n'a été supprimé qu'en 2017 ; la même loi a aussi renforcé les évacuations forcées de campements illicites.", 'localtis_livret_2017', '2017', 'France', "Ils ont longtemps été soumis à un régime d'exception ; les installations illicites sont un problème reconnu.", 'etabli'),
  fait("En 2023, seuls 80,1 % des places en aires d'accueil permanentes, 62,2 % des aires de grand passage et 21,3 % des terrains familiaux prévus étaient réalisés.", 'ddd_gensduvoyage_2024', '2023', 'France', "Les communes ne remplissent pas toutes leurs obligations d'accueil.", 'etabli', '62,2 %'),
  fait("Le Défenseur des droits demande la reconnaissance de la caravane comme logement et relève des refus fréquents de domiciliation par les communes.", 'ddd_gensduvoyage_2024', '2024', 'France', "Les gens du voyage subissent des atteintes à leurs droits.", 'etabli'),
 ],
 court="Faux : les gens du voyage relèvent du droit fiscal commun, avec les mêmes contrôles, selon Bercy. La plupart sont français. Et loin d'avoir tous les droits, ils ont dû porter un livret de circulation jusqu'en 2017, leur caravane n'est pas un logement reconnu et les aires d'accueil prévues par la loi manquent.",
 moyen="Sur les impôts, l'administration est claire depuis des années : les gens du voyage sont soumis aux mêmes obligations fiscales et aux mêmes contrôles que les autres contribuables, y compris la taxation d'après le train de vie. Comme tout le monde, ils paient la TVA sur leurs achats.\n\nSur les droits, c'est plutôt l'inverse de l'idée reçue. Ils ont dû porter un livret de circulation jusqu'en 2017. Leur caravane n'est pas reconnue comme un logement, ce qui les prive des aides au logement. En 2023, seules 62,2 % des aires de grand passage prévues par la loi existaient. Les installations illicites posent de vrais problèmes, et la loi a renforcé les évacuations ; mais elles s'expliquent aussi par le manque d'aires que les communes devraient créer.",
 detaille="Les gens du voyage forment une population d'environ 300 000 personnes selon une ancienne fiche du Défenseur des droits, très majoritairement de nationalité française, dont un tiers seulement est itinérant. Sur le plan fiscal, Bercy a répondu à plusieurs députés, en 2004 et en 2010, qu'ils sont soumis au même traitement fiscal que l'ensemble des contribuables. L'administration dispose d'outils de contrôle : vérification de comptabilité, examen de la situation personnelle, taxation d'après le train de vie, échanges avec les organismes sociaux.\n\nLeur statut a longtemps été un régime d'exception. Jusqu'en 2017, ils devaient porter un livret de circulation hérité d'une loi de 1969 ; la loi Égalité et citoyenneté l'a supprimé et généralisé la domiciliation dans un centre communal d'action sociale. Leur caravane reste juridiquement un véhicule, pas un logement, ce qui les prive des aides au logement. Le Défenseur des droits relève des refus fréquents de domiciliation par les communes et des discriminations liées au mode de vie itinérant.\n\nLes communes ont des obligations d'accueil qu'elles ne remplissent pas toutes : en 2023, 80,1 % des places en aires permanentes, 62,2 % des aires de grand passage et 21,3 % des terrains familiaux prévus étaient réalisés. Les installations illicites sont un problème réel, que la loi de 2017 a traité en renforçant les évacuations. Le juger sérieusement suppose de regarder aussi le manque d'aires légales.",
 empathie="L'installation d'un grand groupe de caravanes sur un terrain de sport ou un champ peut être vécue comme une injustice par les habitants. Ce sentiment mérite une réponse, qui passe par les faits sur la fiscalité et l'accueil.",
 legitimes=["Les installations illicites posent de vrais problèmes locaux.", "La loi de 2017 a renforcé les évacuations forcées des campements illicites."],
 contre=[
  ("Ils ont de grosses voitures et ne déclarent rien.", "L'administration peut taxer d'après le train de vie et dispose de contrôles spécifiques ; une fraude se prouve au cas par cas, comme pour n'importe quel contribuable."),
  ("Ils s'installent où ils veulent sans rien payer.", "Les aires d'accueil sont payantes ; et beaucoup de communes n'ont pas créé les aires que la loi leur impose, ce qui pousse aux installations illicites."),
 ],
 questions=["Savais-tu que les gens du voyage devaient porter un livret de circulation jusqu'en 2017 ?", "Ta commune a-t-elle créé l'aire d'accueil prévue par le schéma départemental ?"],
 limites=["Les réponses ministérielles sur la fiscalité datent de 2004 et 2010 ; aucun chiffre de fraude spécifique n'a été trouvé.", "Le chiffre de 300 000 personnes et la répartition par mode de vie viennent d'une fiche ancienne du Défenseur des droits.", "Une taxe annuelle sur les résidences mobiles a été créée en 2010 ; son maintien n'a pas été vérifié, elle n'est donc pas citée."],
 publics={'convaincus': "Bercy l'a répondu plusieurs fois à des députés de droite : les gens du voyage ont les mêmes obligations fiscales et les mêmes contrôles que toi, y compris sur le train de vie. La plupart sont français. Et jusqu'en 2017, ils devaient porter un livret de circulation : drôle de façon d'avoir tous les droits.",
  'indecis': "Les installations illicites créent de vraies tensions, et la loi a renforcé les évacuations. Mais les gens du voyage paient les mêmes impôts que les autres, et beaucoup de communes n'ont pas créé les aires d'accueil prévues par la loi. Regarder les deux côtés aide à trouver des solutions."},
 a_actualiser='2027-11-08', raison="Nouveau bilan des aires d'accueil et des schémas départementaux.",
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
