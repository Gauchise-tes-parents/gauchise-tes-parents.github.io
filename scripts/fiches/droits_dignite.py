"""Fiches « droits et dignité » (v10) : discriminations, égalité femmes-hommes, morts aux frontières, antisémitisme.

Sources ouvertes et lues le 30 octobre 2026 (consultee=True). Chaque fiche signale aussi les faits qui
ne vont pas dans le sens attendu (règle : ne jamais cacher un résultat contradictoire).
Usage : python3 scripts/fiches/droits_dignite.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche, OUT  # mêmes conventions

DARES = ('dares', src("Discrimination à l'embauche des personnes d'origine supposée maghrébine : quels enseignements d'une grande étude par testing ? (Dares Analyses n° 67)", "Dares, Institut des politiques publiques (IPP) et ISM Corum", "Novembre 2021",
  "https://migrant-integration.ec.europa.eu/system/files/2022-01/Dares%20Analyses_testing_discrimination_embauche.pdf",
  "Testing de décembre 2019 à avril 2021 (interruption mars-juin 2020) : 2 400 offres, 9 600 candidatures, 11 métiers, France métropolitaine. Taux de rappel 33,3 % pour les candidatures à consonance française, 22,8 % pour celles à consonance maghrébine : « Ces candidatures sont 31,5 % moins souvent rappelées » ; il faut environ 1,5 fois plus de CV pour obtenir autant de rappels. CV non strictement identiques, rotation systématique des identités.",
  "Étude publique de référence (ministère du Travail), copie hébergée par le site de la Commission européenne."))
INSEE_DISC = ('insee_disc', src("Les discriminations sur le marché du travail subies par les personnes d'origine maghrébine (Immigrés et descendants d'immigrés en France, édition 2023)", "Insee (Émilie Arnoult, Dares)", "30 mars 2023",
  "https://www.insee.fr/fr/statistiques/6793310",
  "Taux de chômage des 18-59 ans diplômés (CAP à bac+5), 2019-2020 : 6 % pour les personnes sans ascendance migratoire, 16 % pour les immigrés et descendants d'immigrés du Maghreb ; 66 % de l'écart n'est pas expliqué par les caractéristiques observées. Sentiment de refus injuste d'un emploi : 37 % des hommes immigrés du Maghreb, contre 15 % des hommes sans ascendance migratoire.",
  "Statistique publique de référence."))
INSEE_FH = ('insee_fh', src("Écart de salaire entre femmes et hommes en 2024 (Insee Focus n° 377)", "Insee", "26 février 2026",
  "https://insee.fr/fr/statistiques/8743657",
  "Secteur privé, 2024 : revenu salarial moyen des femmes inférieur de 21,8 % à celui des hommes (22 060 € contre 28 220 €) ; écart de salaire en équivalent temps plein de 14,0 % ; écart « à emploi comparable » (même poste, même établissement) estimé à 3,6 %, sur environ 25 % des établissements, sans mesurer directement la discrimination.",
  "Statistique publique de référence."))
ONU_OIM = ('onu_oim', src("Près de 8 000 migrants morts ou disparus sur les routes migratoires en 2025 (ONU Info, d'après l'OIM, Global Migration Routes Overview 2025)", "ONU Info / Organisation internationale pour les migrations", "21 avril 2026",
  "https://news.un.org/fr/story/2026/04/1158713",
  "« Près de 8 000 » personnes mortes ou disparues sur les routes migratoires en 2025, après un record de 9 200 en 2024 ; « plus de 82 000 » depuis 2014 ; 1 723 depuis le début de 2026. La baisse de 2025 s'explique en partie par une diminution réelle des traversées dangereuses, et peut-être par des moyens réduits pour documenter les décès. « Une baisse des mouvements ne signifie pas automatiquement des voyages plus sûrs. »",
  "Agence des Nations unies ; données du projet Missing Migrants."))
EUI = ('eui', src("Sea rescue NGOs: a pull factor of irregular migration? (Policy Brief 2019/22, Migration Policy Centre)", "European University Institute (Eugenio Cusumano, Matteo Villa)", "Novembre 2019",
  "https://cadmus.eui.eu/handle/1814/65024",
  "Flux mensuels Libye-Italie de 2014 à octobre 2019 : « We find no relationship between the presence of NGOs at sea and the number of migrants leaving Libyan shores » ; les auteurs appellent à davantage de données et de recherches.",
  "Note de recherche d'un institut universitaire européen.", 'etude'))
DOALOS = ('doalos', src("Expert Meeting on Refugees and Asylum-seekers in Distress at Sea — présentation de la Division des affaires maritimes et du droit de la mer", "Nations unies, Bureau des affaires juridiques (DOALOS)", "Novembre 2011",
  "https://www.unhcr.org/us/sites/en-us/files/legacy-pdf/4ef2ff8a9.pdf",
  "Article 98 de la Convention des Nations unies sur le droit de la mer : obligation de « render assistance to any person found at sea in danger of being lost » et de « proceed with all possible speed to the rescue of persons in distress » ; obligation applicable dans toutes les zones maritimes.",
  "Présentation officielle des Nations unies (droit international de la mer)."))
CNCDH25 = ('cncdh25', src("Rapport sur la lutte contre le racisme, l'antisémitisme et la xénophobie — année 2025 (communiqué de presse)", "Commission nationale consultative des droits de l'homme (CNCDH)", "25 juin 2026",
  "https://www.cncdh.fr/sites/default/files/2026-06/25.06.2026%20CP%20Rapport%20Racisme%202025.pdf",
  "En 2025 : 1 320 faits antisémites (DNRT), niveau « très inquiétant » ; 326 faits antimusulmans (+88 %) ; 9 737 crimes ou délits racistes, xénophobes ou antireligieux (SSMSI, +5 %). Indice longitudinal de tolérance : 64/100. 35 % des personnes interrogées pensent que « les Juifs ont un rapport particulier à l'argent ».",
  "Autorité administrative indépendante ; données du ministère de l'Intérieur et baromètre annuel."))
CNCDH24 = ('cncdh24', src("Les essentiels du rapport sur la lutte contre le racisme, l'antisémitisme et la xénophobie — année 2024", "Commission nationale consultative des droits de l'homme (CNCDH)", "Juin 2025",
  "https://www.cncdh.fr/sites/default/files/2025-06/Essentiels%20RRacisme%202024%20Format%20A4%20VDEF.pdf",
  "1 570 faits antisémites en 2024 (DNRT), « en légère baisse au regard des chiffres de l'année 2023 qui constituait un niveau inédit », niveau « extrêmement inquiétant » ; 36 % pensent que « les Juifs ont un rapport particulier à l'argent ».",
  "Autorité administrative indépendante."))
MAYER = ('mayer', src("Unité et diversité des préjugés racistes et antisémites (Droits & Libertés n° 214)", "Nonna Mayer (Sciences Po / CNRS), revue de la Ligue des droits de l'Homme", "Juillet 2026",
  "https://www.ldh-france.org/wp-content/uploads/2026/07/DL214-Dossier-3.-Unite-et-diversite-des-prejuges-racistes-et-antisemites.pdf",
  "Baromètre de la CNCDH (Ipsos, fin 2025) : le « vieil » antisémitisme (pouvoir, argent, communautarisme, déloyauté) « reste le plus prégnant » ; en trois ans, l'adhésion aux préjugés antisémites a baissé de 7 points chez les sympathisants du RN et progressé de 10 points chez ceux de LFI ; fin 2025, 48 % des sympathisants RN et 47 % des sympathisants LFI obtiennent une note de 2 sur 5 ou plus, un niveau « jamais atteint » pour LFI. Distinction entre le rejet d'Israël associé aux préjugés antijuifs et la critique d'Israël sans stéréotype.",
  "Analyse d'une chercheuse spécialiste, à partir des données de la CNCDH (publiée dans une revue associative).", 'etude'))
MEMORIAL = ('memorial', src("Les Juifs de France dans la Shoah (panneaux d'exposition itinérante)", "Mémorial de la Shoah", "2016",
  "https://memorialdelashoah.org/wp-content/uploads/2016/04/les-juifs-de-france-kakemono-caisse_155.pdf",
  "« Sur les 330 000 Juifs vivant en France en 1939, 76 000 d'entre eux ont été déportés et assassinés » ; panneaux « La législation antisémite » et « Une propagande antisémite acharnée ».",
  "Institution de référence sur l'histoire de la Shoah."))

FICHES = []

FICHES.append(fiche(
 id='discriminations-embauche', affirmation="Les discriminations à l'embauche, ça n'existe plus : c'est une excuse.", volet='droits', sous_theme='Discriminations',
 mots_cles=['discrimination', 'discriminations', 'embauche', 'racisme', 'testing', 'cv', 'nom', 'origine', 'maghrébin', 'arabe', 'excuse', 'victimisation', 'égalité des chances'],
 verdict='contredit', fiabilite='etabli',
 resume="Les discriminations à l'embauche sont mesurées, pas supposées : dans le grand testing public de 2019-2021, à candidature équivalente, les personnes d'origine supposée maghrébine sont rappelées 31,5 % moins souvent. Le chômage des personnes originaires du Maghreb est près de trois fois plus élevé, et les deux tiers de l'écart ne s'expliquent ni par le diplôme ni par l'âge.",
 contexte="Le soupçon de « victimisation » revient souvent quand on parle de racisme. La méthode du testing permet justement de sortir de l'impression : on envoie des candidatures comparables qui ne diffèrent que par le nom.",
 explication="Un testing mesure l'effet du seul nom sur les rappels. L'étude de la Dares, de l'IPP et d'ISM Corum porte sur 2 400 offres et 9 600 candidatures. L'Insee complète avec les enquêtes Emploi et Trajectoires et origines : écarts de chômage et sentiment de discrimination.",
 sources=[DARES, INSEE_DISC],
 faits=[
  fait("À candidature équivalente, les candidatures à consonance maghrébine sont rappelées 31,5 % moins souvent (22,8 % contre 33,3 %) : il faut envoyer environ 1,5 fois plus de CV pour obtenir autant de rappels.", 'dares', 'Décembre 2019 - avril 2021', '2 400 offres, 11 métiers, France métropolitaine', "La discrimination est mesurée par une méthode expérimentale, pas déduite d'impressions.", 'etabli', '31,5 %'),
  fait("En 2019-2020, le taux de chômage des 18-59 ans diplômés est de 16 % pour les immigrés et descendants d'immigrés du Maghreb, contre 6 % pour les personnes sans ascendance migratoire ; 66 % de l'écart n'est pas expliqué par les caractéristiques observées.", 'insee_disc', '2019-2020', 'France, 18-59 ans, diplômés du CAP à bac+5', "Même à diplôme égal, l'écart reste massif.", 'etabli', '16 % / 6 %'),
  fait("37 % des hommes immigrés du Maghreb déclarent s'être vu refuser injustement un emploi, contre 15 % des hommes sans ascendance migratoire.", 'insee_disc', 'Enquête Trajectoires et origines 2 (2019-2020)', 'France', "Le vécu déclaré concorde avec la mesure expérimentale.", 'etabli', '37 % / 15 %'),
 ],
 court="Ce n'est pas une impression, c'est mesuré : dans le testing public de 2019-2021, à CV équivalent, un nom à consonance maghrébine est rappelé 31,5 % moins souvent (Dares). Et à diplôme égal, le chômage des personnes originaires du Maghreb est de 16 % contre 6 %.",
 moyen="On n'a pas besoin de croire qui que ce soit sur parole : on a mesuré. Entre 2019 et 2021, la Dares et des chercheurs de l'IPP ont envoyé 9 600 candidatures à 2 400 offres. Seule différence : le nom. Résultat : 22,8 % de rappels pour un nom à consonance maghrébine, contre 33,3 % pour un nom à consonance française.\n\nL'Insee confirme : à diplôme égal, 16 % de chômage pour les personnes originaires du Maghreb contre 6 % pour les autres, et les deux tiers de cet écart ne s'expliquent ni par l'âge ni par le diplôme. Ce n'est pas une excuse : c'est une injustice, et c'est un délit.",
 detaille="Dire que les discriminations sont une « excuse », c'est renverser la charge : on accuse les victimes de se plaindre. Or la discrimination à l'embauche est l'un des phénomènes sociaux les mieux mesurés, grâce au testing.\n\nLa grande étude publique conduite par la Dares, l'Institut des politiques publiques et ISM Corum (décembre 2019 - avril 2021) a envoyé 9 600 candidatures à 2 400 offres, dans 11 métiers. Les candidatures à consonance maghrébine sont rappelées 31,5 % moins souvent : 22,8 % contre 33,3 %.\n\nLes données de l'Insee vont dans le même sens : en 2019-2020, à diplôme comparable, le taux de chômage des immigrés et descendants d'immigrés du Maghreb atteint 16 %, contre 6 % pour les personnes sans ascendance migratoire, et 66 % de l'écart reste inexpliqué par les caractéristiques observées. 37 % des hommes immigrés du Maghreb déclarent avoir été injustement refusés à un emploi.\n\nLa discrimination est interdite par la loi. La combattre, c'est défendre l'égalité républicaine, pas « victimiser » qui que ce soit.",
 empathie="Je comprends qu'on n'ait pas envie de croire que notre pays discrimine : moi non plus, ça ne me fait pas plaisir. Mais on l'a mesuré très simplement, avec des CV qui ne diffèrent que par le nom, et le résultat est net. Reconnaître le problème, c'est la première étape pour être fidèle à l'égalité.",
 legitimes=["Un testing mesure les rappels, pas les embauches finales.", "Les résultats varient selon les métiers et les entreprises."],
 contre=[
  ("C'est le niveau de diplôme ou le quartier, pas le racisme.", "Le testing compare des candidatures équivalentes qui ne diffèrent que par le nom ; et selon l'Insee, deux tiers de l'écart de chômage ne s'expliquent pas par les caractéristiques observées."),
  ("Ils n'ont qu'à mieux s'intégrer.", "Les candidats du testing ont le même parcours fictif que les autres : la seule différence, c'est le nom. On ne peut pas « s'intégrer » davantage en changeant son nom."),
 ],
 questions=["Si deux CV identiques ne diffèrent que par le nom, comment expliques-tu l'écart de rappels ?", "Qu'est-ce qui te ferait accepter qu'une discrimination existe, si un testing ne suffit pas ?"],
 limites=["Le testing de 2019-2021 porte sur les grandes et moyennes entreprises et sur 11 métiers.", "Les données d'enquête datent de 2019-2020."],
 a_actualiser='2028-06-30',
))

FICHES.append(fiche(
 id='egalite-salariale', affirmation="L'égalité salariale entre les femmes et les hommes, c'est réglé.", volet='droits', sous_theme='Égalité salariale',
 mots_cles=['égalité salariale', 'femmes', 'hommes', 'écart de salaire', 'inégalités', 'féminisme', 'temps partiel', 'à travail égal salaire égal', 'c est réglé'],
 verdict='contredit', fiabilite='etabli',
 resume="En 2024, dans le privé, les femmes gagnent en moyenne 21,8 % de moins que les hommes sur l'année, et 14,0 % de moins à temps de travail égal (Insee). À poste comparable dans le même établissement, l'écart est plus faible (3,6 %) : l'essentiel de l'inégalité tient au temps partiel, aux métiers féminisés moins payés et aux carrières freinées.",
 contexte="L'égalité de salaire « à travail égal » est inscrite dans la loi depuis 1972. Beaucoup en concluent que le problème est réglé.",
 explication="L'Insee mesure plusieurs écarts emboîtés : sur le revenu salarial annuel, en équivalent temps plein, puis à emploi comparable. Chaque niveau dit quelque chose de différent : l'écart total révèle les inégalités de temps de travail et de métiers ; l'écart à poste comparable approche, sans la mesurer directement, la discrimination pure.",
 sources=[INSEE_FH],
 faits=[
  fait("En 2024, dans le secteur privé, le revenu salarial moyen des femmes est inférieur de 21,8 % à celui des hommes (22 060 € contre 28 220 €).", 'insee_fh', '2024', 'Salariés du secteur privé', "Sur une année, l'écart reste d'un cinquième.", 'etabli', '21,8 %'),
  fait("À temps de travail égal (en équivalent temps plein), l'écart de salaire atteint 14,0 %.", 'insee_fh', '2024', 'Salariés du secteur privé', "Même en neutralisant le temps partiel, l'écart persiste.", 'etabli', '14,0 %'),
  fait("À emploi comparable (même poste, même établissement), l'écart est estimé à 3,6 %, sur environ un quart des établissements ; il ne mesure pas directement la discrimination.", 'insee_fh', '2024', 'Environ 25 % des établissements du privé', "L'essentiel de l'écart vient du temps partiel, des métiers et des carrières, pas seulement d'un salaire différent pour le même poste.", 'estimation', '3,6 %'),
 ],
 court="Non : en 2024, les femmes gagnent 21,8 % de moins que les hommes sur l'année, et 14 % de moins à temps de travail égal (Insee). L'égalité est dans la loi depuis 1972 ; dans les fiches de paie, pas encore.",
 moyen="La loi impose l'égalité « à travail égal » depuis 1972, mais regarde les chiffres de l'Insee pour 2024 : sur l'année, les femmes du privé gagnent 21,8 % de moins que les hommes ; à temps de travail égal, 14 % de moins.\n\nÀ poste identique dans la même entreprise, l'écart tombe à 3,6 %. C'est justement intéressant : l'inégalité ne vient pas seulement d'un salaire différent pour le même poste, mais du temps partiel subi, des métiers féminisés moins bien payés (soin, nettoyage, aide à domicile) et des carrières freinées par les enfants. C'est là que ça se joue.",
 detaille="L'égalité salariale « à travail égal » est obligatoire depuis 1972. Pourtant, selon l'Insee, en 2024, dans le secteur privé, le revenu salarial moyen des femmes est inférieur de 21,8 % à celui des hommes : 22 060 € contre 28 220 €.\n\nUne partie de cet écart vient du temps de travail : en équivalent temps plein, l'écart reste de 14,0 %. À emploi comparable, dans le même établissement, il est estimé à 3,6 %, sur environ un quart des établissements ; l'Insee précise que cet indicateur ne mesure pas directement la discrimination.\n\nCe résultat ne « dégonfle » pas le problème, il le précise : l'inégalité est d'abord structurelle. Les femmes sont plus souvent à temps partiel, concentrées dans des métiers moins rémunérés, et leurs carrières ralentissent davantage après une naissance. Réduire l'écart suppose de revaloriser les métiers féminisés, de lutter contre le temps partiel subi et de partager le congé parental, en plus de sanctionner les discriminations directes.",
 empathie="Je comprends qu'on pense que c'est réglé : la loi existe depuis longtemps. Mais les chiffres de l'Insee montrent encore 14 % d'écart à temps de travail égal. Ce n'est pas forcément ton patron qui triche : c'est la façon dont on paie les métiers et dont on organise les carrières.",
 legitimes=["À poste comparable dans le même établissement, l'écart est faible (3,6 %).", "Une partie de l'écart reflète des différences de temps de travail et de métiers, qui ne relèvent pas toutes d'une discrimination directe."],
 contre=[
  ("C'est parce que les femmes choisissent le temps partiel.", "Une partie du temps partiel est subie, et elle pèse surtout sur les femmes ; même en équivalent temps plein, l'écart reste de 14,0 %."),
  ("À poste égal, il n'y a presque plus d'écart.", "C'est vrai que l'écart à poste comparable est faible (3,6 %). Mais pourquoi les métiers où il y a beaucoup de femmes sont-ils moins bien payés ? L'inégalité est surtout là."),
 ],
 questions=["Pourquoi, selon toi, une aide-soignante gagne-t-elle moins qu'un technicien de maintenance ?", "Si c'est réglé, comment expliques-tu les 14 % d'écart à temps de travail égal ?"],
 limites=["Les chiffres portent sur le secteur privé.", "L'écart à emploi comparable ne couvre qu'environ un quart des établissements."],
 a_actualiser='2027-03-31',
))

FICHES.append(fiche(
 id='migrants-mediterranee', affirmation="Il ne faut pas secourir les migrants en mer : ça crée un appel d'air.", volet='immigration', sous_theme='Immigration et asile',
 mots_cles=['migrants', 'méditerranée', 'secourir', 'sauvetage', 'ong', 'appel d air', 'bateaux', 'noyés', 'naufrage', 'mer', 'laisser mourir', 'pull factor', 'droit de la mer'],
 verdict='contredit', fiabilite='interpretation',
 resume="Secourir une personne en détresse en mer est une obligation du droit international, quelle que soit la personne. Plus de 82 000 personnes sont mortes ou ont disparu sur les routes migratoires depuis 2014 (OIM). Et l'étude de l'Institut universitaire européen ne trouve aucune relation entre la présence des ONG en mer et le nombre de départs depuis la Libye.",
 contexte="L'argument de l'« appel d'air » (en anglais pull factor) a servi à justifier la fin d'opérations de sauvetage et des poursuites contre des ONG.",
 explication="Les départs dépendent surtout de la situation dans les pays de départ et de transit (guerres, répression, conditions en Libye), des réseaux de passeurs et des politiques des États. Les études qui ont comparé la présence des navires de sauvetage et les départs n'observent pas de lien. L'obligation de secours, elle, ne dépend d'aucun calcul : elle protège toute personne en danger.",
 sources=[DOALOS, ONU_OIM, EUI],
 faits=[
  fait("L'article 98 de la Convention des Nations unies sur le droit de la mer impose de prêter assistance à toute personne trouvée en mer en danger de disparaître et de se porter au secours des personnes en détresse, dans toutes les zones maritimes.", 'doalos', 'Droit en vigueur (convention de 1982)', 'Droit international', "Le secours en mer n'est pas une option politique : c'est une obligation.", 'etabli'),
  fait("Plus de 82 000 personnes sont mortes ou ont disparu sur les routes migratoires dans le monde depuis 2014, dont près de 8 000 en 2025 après un record de 9 200 en 2024.", 'onu_oim', '2014-2025', 'Monde', "Derrière le débat, des dizaines de milliers de vies.", 'etabli', '82 000'),
  fait("Sur les flux Libye-Italie de 2014 à octobre 2019, l'étude de l'Institut universitaire européen ne trouve aucune relation entre la présence des ONG en mer et le nombre de départs.", 'eui', '2014 - octobre 2019', 'Méditerranée centrale', "L'« appel d'air » des sauvetages n'est pas observé dans les données.", 'estimation'),
 ],
 court="Secourir quelqu'un qui se noie est une obligation du droit de la mer, sans condition de nationalité. Plus de 82 000 morts et disparus depuis 2014 (OIM). Et l'« appel d'air » n'apparaît pas dans les données : aucune relation entre la présence des ONG et les départs de Libye (Institut universitaire européen).",
 moyen="D'abord, le droit : l'article 98 de la Convention des Nations unies sur le droit de la mer impose de porter secours à toute personne en détresse. Ce n'est pas une opinion, c'est une obligation.\n\nEnsuite, les faits : plus de 82 000 personnes sont mortes ou ont disparu sur les routes migratoires depuis 2014, selon l'OIM. Et l'« appel d'air » ? Des chercheurs de l'Institut universitaire européen ont comparé, mois par mois, la présence des ONG en mer et les départs depuis la Libye entre 2014 et 2019 : aucune relation. Les gens partent à cause de ce qu'ils fuient, pas à cause des bateaux de secours.",
 detaille="Le débat sur le sauvetage en mer oppose une vie humaine à un calcul politique. Commençons par le droit : l'article 98 de la Convention des Nations unies sur le droit de la mer oblige à prêter assistance à toute personne trouvée en mer en danger de disparaître, dans toutes les zones maritimes. La nationalité ou le statut de la personne ne changent rien à cette obligation.\n\nLe coût humain est massif : selon l'Organisation internationale pour les migrations, plus de 82 000 personnes sont mortes ou ont disparu sur les routes migratoires depuis 2014, dont près de 8 000 en 2025. L'OIM rappelle qu'« une baisse des mouvements ne signifie pas automatiquement des voyages plus sûrs ».\n\nQuant à l'« appel d'air », il a été testé : Eugenio Cusumano et Matteo Villa (Institut universitaire européen) ont comparé les flux mensuels entre la Libye et l'Italie de 2014 à 2019 et n'ont trouvé aucune relation entre la présence des ONG et le nombre de départs. Les auteurs appellent à plus de recherches, mais rien ne permet d'affirmer que laisser mourir dissuade de partir.\n\nOn peut débattre des politiques migratoires. On ne peut pas faire de la noyade un instrument de politique migratoire.",
 empathie="Je comprends l'inquiétude devant l'arrivée de bateaux, et l'envie que ça s'arrête. Mais quand quelqu'un se noie, la question n'est plus l'immigration : c'est une vie. Et les chercheurs n'ont pas trouvé que les secours poussent les gens à partir.",
 legitimes=["La politique migratoire et le contrôle des frontières sont des sujets de débat légitimes.", "L'étude de 2019 porte sur la Méditerranée centrale et ses auteurs appellent à davantage de recherches."],
 contre=[
  ("Les ONG font le travail des passeurs.", "Les données de 2014-2019 ne montrent pas de lien entre leur présence et les départs ; et le droit de la mer impose à tout navire de porter secours."),
  ("Ils n'ont qu'à ne pas partir.", "On peut discuter des politiques migratoires ; mais laisser des gens se noyer n'est une politique acceptable dans aucun État de droit."),
 ],
 questions=["Si c'était ton enfant sur ce bateau, tu voudrais qu'on calcule l'appel d'air avant de le sortir de l'eau ?", "Qu'est-ce qui te fait penser que les secours font partir plus de gens, alors que les études ne le montrent pas ?"],
 limites=["Les chiffres de l'OIM sont des minimums : beaucoup de décès ne sont jamais documentés.", "L'étude de l'Institut universitaire européen s'arrête en 2019."],
 a_actualiser='2027-06-30',
))

FICHES.append(fiche(
 id='antisemitisme-aujourdhui', affirmation="L'antisémitisme, c'est un faux problème brandi pour faire taire la gauche.", volet='droits', sous_theme='Discriminations',
 mots_cles=['antisémitisme', 'antisemite', 'juifs', 'actes antisémites', 'instrumentalisation', 'faire taire', 'gauche', 'israël', 'sionisme', 'résiduel', 'préjugés', 'cncdh'],
 verdict='contredit', fiabilite='etabli',
 resume="L'antisémitisme est un problème réel et massif : 1 570 faits antisémites recensés en 2024 et 1 320 en 2025, et un tiers des Français adhèrent encore au préjugé du « rapport particulier à l'argent » (CNCDH). Il existe à l'extrême droite, et aussi à gauche : chez les sympathisants de LFI, l'adhésion aux préjugés antisémites a progressé de 10 points en trois ans. Le combattre partout fait partie de l'antifascisme ; on peut critiquer le gouvernement israélien sans recourir aux stéréotypes antijuifs.",
 contexte="Le débat sur l'antisémitisme est devenu un champ de bataille politique depuis le 7 octobre 2023 et la guerre à Gaza. Certains accusent toute critique d'Israël d'antisémitisme ; d'autres minimisent l'antisémitisme comme une arme rhétorique.",
 explication="Les deux attitudes sont dangereuses. Les données de la CNCDH distinguent le « vieil » antisémitisme (pouvoir, argent, déloyauté), toujours le plus répandu, et une forme liée au rejet d'Israël quand elle se mêle aux stéréotypes antijuifs. La critique d'un État et de sa politique est légitime ; l'assignation des Juifs de France à cet État ne l'est pas.",
 sources=[CNCDH24, CNCDH25, MAYER, MEMORIAL],
 faits=[
  fait("1 570 faits antisémites ont été recensés en 2024, un niveau jugé « extrêmement inquiétant » après le record de 2023, puis 1 320 en 2025.", 'cncdh24', '2024-2025', 'France (données du ministère de l\'Intérieur)', "Les actes sont nombreux et violents : ce n'est pas une invention.", 'etabli', '1 570'),
  fait("En 2025, 35 % des personnes interrogées pensent que « les Juifs ont un rapport particulier à l'argent ».", 'cncdh25', '2025', 'France (baromètre CNCDH)', "Les vieux mythes antisémites restent largement partagés.", 'etabli', '35 %'),
  fait("Selon l'analyse de Nonna Mayer des données de la CNCDH, en trois ans l'adhésion aux préjugés antisémites a baissé de 7 points chez les sympathisants du RN et progressé de 10 points chez ceux de LFI ; fin 2025, 48 % des premiers et 47 % des seconds obtiennent une note de 2 sur 5 ou plus.", 'mayer', '2022-2025', 'France (baromètre CNCDH)', "L'antisémitisme n'est pas l'apanage d'un camp : la gauche doit le regarder en face chez elle aussi.", 'estimation', '+10 points'),
  fait("Sur les 330 000 Juifs vivant en France en 1939, 76 000 ont été déportés et assassinés.", 'memorial', '1940-1944', 'France', "C'est l'histoire que la lutte contre l'antisémitisme oblige à ne jamais oublier.", 'etabli', '76 000'),
 ],
 court="Non : 1 570 actes antisémites en 2024, 1 320 en 2025, et un tiers des Français croient encore au mythe des Juifs et de l'argent (CNCDH). Être de gauche, c'est combattre l'antisémitisme partout, y compris chez nous : les préjugés ont progressé de 10 points chez les sympathisants LFI en trois ans.",
 moyen="L'antisémitisme n'est pas un argument de débat : ce sont des actes. La CNCDH en recense 1 570 en 2024 et 1 320 en 2025. Et les vieux préjugés tiennent : 35 % des personnes interrogées pensent que les Juifs ont un rapport particulier à l'argent.\n\nSoyons honnêtes : ce n'est pas qu'un problème d'extrême droite. Selon la politiste Nonna Mayer, les préjugés antisémites ont reculé chez les sympathisants du RN mais progressé de 10 points chez ceux de LFI en trois ans. La gauche antifasciste doit le combattre chez elle aussi. Et on peut critiquer le gouvernement israélien, défendre les Palestiniens, sans jamais reprendre un stéréotype antijuif : c'est même la condition pour être crédible.",
 detaille="Réduire l'antisémitisme à un « faux problème » est une erreur factuelle et une faute politique. Selon la CNCDH, 1 570 faits antisémites ont été recensés en 2024, un niveau « extrêmement inquiétant » après le record de 2023, et 1 320 en 2025. Le baromètre de la CNCDH montre que 35 % des personnes interrogées adhèrent encore au préjugé selon lequel « les Juifs ont un rapport particulier à l'argent ».\n\nLe « vieil » antisémitisme (pouvoir, argent, communautarisme, déloyauté) reste le plus répandu. Mais selon l'analyse de Nonna Mayer, l'adhésion aux préjugés antisémites a progressé de 10 points chez les sympathisants de LFI en trois ans, quand elle reculait de 7 points chez ceux du RN : fin 2025, les deux électorats sont à un niveau comparable.\n\nPour la gauche, ce résultat dérangeant doit être intégré, pas nié : l'antifascisme est indivisible. L'histoire le rappelle : 76 000 Juifs de France ont été déportés et assassinés, au terme d'une propagande qui les désignait comme ennemis intérieurs. Il est parfaitement possible, et nécessaire, de critiquer la politique d'un État, y compris Israël, sans assigner les Juifs de France à cet État ni recycler les mythes antijuifs. Et il faut refuser aussi l'instrumentalisation inverse, qui assimile toute critique d'Israël à de l'antisémitisme ou qui absout une extrême droite à l'histoire antisémite.",
 empathie="Je comprends qu'on ait l'impression que l'accusation d'antisémitisme sert parfois à faire taire des critiques. Mais les actes sont réels, ils visent des gens concrets, et même des personnes de gauche partagent des préjugés sans le voir. Défendre les Palestiniens et combattre l'antisémitisme, ça va ensemble.",
 legitimes=["L'accusation d'antisémitisme est parfois utilisée de façon abusive pour disqualifier des critiques de la politique israélienne.", "Les préjugés antisémites restent aussi élevés chez les sympathisants du RN."],
 contre=[
  ("On ne peut plus critiquer Israël sans être traité d'antisémite.", "On peut critiquer un gouvernement et une politique ; ce qui est antisémite, c'est d'attribuer aux Juifs un pouvoir occulte ou de les tenir pour responsables de la politique d'un État."),
  ("L'antisémitisme, c'est l'extrême droite.", "Historiquement, oui, et les préjugés y restent élevés (48 % de notes de 2 sur 5 ou plus). Mais les données montrent une progression chez les sympathisants de LFI : l'antifascisme exige de le combattre partout."),
 ],
 questions=["Qu'est-ce qui te permet de distinguer une critique d'Israël d'un préjugé antijuif ?", "Si les actes antisémites sont réels, en quoi le dire ferait-il taire la gauche ?"],
 limites=["Les chiffres d'actes reposent sur les plaintes et signalements recensés.", "Les comparaisons par sympathie partisane reposent sur des sous-échantillons d'un baromètre d'environ un millier de personnes."],
 a_actualiser='2027-06-30',
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
