"""Fiches quotidiennes du 8 novembre 2026, premier passage (UTC) — phase alpha.

25 questions qui circulent (extrême droite, clichés sur la gauche, programmes) et qui n'avaient pas de fiche
qui leur réponde vraiment. Toutes les sources ont été ouvertes et lues le 8 novembre 2026 (consultee=True) ;
les chiffres viennent uniquement des passages cités. Données anciennes signalées dans les limites.
Chaque fiche contient les réponses selon le public (« publics » : électeur d'extrême droite convaincu / indécis).
Usage : python3 scripts/fiches/quotidien_20261108_0000.py  (puis node scripts/corrections-v10.js et node scripts/enrichir-fiches.js)
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche as _fiche, OUT

TODAY = '2026-11-08'

def fiche(**k):
    d = _fiche(**k)
    d['derniere_verification'] = TODAY
    return d

# ── Sources : immigration et comparaisons européennes ─────────────────────
INA_ROCARD = ('ina_rocard', src("« Toute la misère du monde » : l'histoire de la petite phrase de Michel Rocard", "INA (INA éclaire l'actu, Romane Laignel Sauvage)", "25 septembre 2023",
  "https://www.ina.fr/ina-eclaire-actu/toute-la-misere-du-monde-histoire-politique-michel-rocard",
  "Le 3 décembre 1989, Michel Rocard, Premier ministre, déclare sur TF1 dans « 7 sur 7 » : « nous ne pouvons pas héberger toute la misère du monde ». Il répète la formule en janvier 1990. En 1993, il la complète : « la part qu'elle en a, elle prend la responsabilité de la traiter la mieux possible ». À partir du milieu des années 1990, il dit que sa citation a été tronquée et qu'il ajoutait que la France devait « savoir en prendre fidèlement sa part ». En septembre 2009, il écrit que la France et l'Europe « peuvent et doivent accueillir toute la part qui leur revient de la misère du monde ».",
  "Archives audiovisuelles publiques."))
CFJ_ROCARD = ('cfj_rocard', src("« La misère du monde » : le fardeau de Michel Rocard", "3millions7 (site de vérification des étudiants du CFJ)", "27 avril 2015",
  "https://3millions7.cfjlab.fr/2015/04/27/la-misere-du-monde-le-fardeau-de-michel-rocard/",
  "Le site recense les occurrences : version courte le 3 décembre 1989 ; le 13 décembre 1989 à l'Assemblée, « notre pays ne peut accueillir et soulager toute la misère du monde », suivi de l'annonce d'un renforcement des contrôles aux frontières ; version courte encore le 7 janvier 1990. Pour la version longue qu'il aurait prononcée en novembre 1989 devant la Cimade, « aucune archive » ne permet de vérifier ; la seconde partie apparaît clairement dans une tribune de 1996.",
  "Vérification d'une école de journalisme (2015).", 'media'))
CIMADE_ROCARD = ('cimade_rocard', src("Ce que Michel Rocard a dit à La Cimade", "La Cimade", "4 juillet 2016",
  "https://www.lacimade.org/ce-que-michel-rocard-a-dit-a-la-cimade/",
  "Selon l'association, Michel Rocard aurait dit en novembre 1989, pour ses cinquante ans : « La France ne peut accueillir toute la misère du monde, mais elle doit savoir en prendre fidèlement sa part », et aurait ensuite regretté une lecture déformée de sa pensée. En 2009, à Strasbourg, il dit que la France et l'Europe doivent accueillir « toute la part qui leur revient de la misère du monde ».",
  "Témoignage d'une association d'aide aux migrants, partie prenante.", 'secondaire'))
SURL_CENT = ('surl_cent', src("Non, il n'y a pas des dizaines de milliers de faux centenaires retraités français en Algérie", "Les Surligneurs (Clara Robert-Motta)", "28 novembre 2024",
  "https://lessurligneurs.eu/non-il-ny-a-pas-des-dizaines-de-milliers-de-faux-centenaires-retraites-francais-en-algerie/",
  "La rumeur vient d'un rapport de la Cour des comptes d'avril 2010, que la Direction de la Sécurité sociale a contesté en 2018. Au 31 décembre 2023, la CNAV compte environ 337 183 pensionnés du régime général résidant en Algérie, pour une pension moyenne de 262 € par mois, dont 1 018 centenaires (0,3 %). La Cour avait relevé de faux actes d'état civil pour 8 prestataires sur 111 dans une commune contrôlée ; les missions de la CNAV en Algérie en 2012 et 2016 ont détecté très peu de fraudes. La biométrie est expérimentée depuis juin 2024 pour les certificats d'existence.",
  "Site de vérification juridique animé par des universitaires.", 'media'))
CNAV_ALG = ('cnav_alg', src("Structure et mortalité des retraités d'Algérie (étude 2020-039)", "CNAV, direction statistiques, prospective et recherche (Marie Ménard)", "19 juillet 2021",
  "https://statistiques-recherche.lassuranceretraite.fr/app/uploads/2021/10/structure-et-mortalite-des-retraites-d-Algerie-2021-039_demographie.pdf",
  "358 065 retraités du régime général résident en Algérie au 31 décembre 2020 (2,5 % du total), contre environ 440 000 en 2010. Les centenaires représentent 0,17 % de ces retraités, contre 0,12 % en France, écart en partie dû au creux des naissances en France pendant la Première Guerre mondiale. L'étude admet une mortalité « légèrement sous-estimée » à cause de décès non déclarés, sans remettre en cause ses résultats.",
  "Étude statistique de la caisse nationale d'assurance vieillesse."))
AN_CENT = ('an_cent', src("Question écrite n° 1690 et réponse du ministère des Affaires sociales et de la Santé", "Assemblée nationale (14e législature)", "réponse publiée au JO le 27 novembre 2012",
  "https://www.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE1690.pdf",
  "Au 31 mars 2009, 438 351 retraités résidant en Algérie percevaient une pension de la CNAV, dont 421 centenaires ; le taux de centenaires y est « très légèrement inférieur » à celui de France (0,096 % contre 0,097 %). Les caisses demandent une à quatre attestations d'existence par an et suspendent la pension en cas de fausse attestation.",
  "Réponse ministérielle officielle (données 2009)."))
CCME_CC = ('ccme_cc', src("Un rapport officiel met en garde contre des failles dans les pensions des retraités résidant hors de France", "Conseil de la communauté marocaine à l'étranger (résumé d'un rapport de la Cour des comptes)", "26 novembre 2025",
  "https://www.ccme.org.ma/un-rapport-officiel-met-en-garde-contre-des-failles-dans-les-pensions-des-retraites-residant-hors-de-france",
  "Environ 1,1 million de retraités du régime général et 800 000 du régime complémentaire résident à l'étranger (7 % des affiliés), dont 31 % en Algérie ; les montants versés sont de 3,9 milliards d'euros par an pour le régime général. Lors de contrôles menés entre 2019 et 2022 sur 2 500 dossiers, 2,27 % des documents n'étaient pas conformes. La Cour recommande davantage d'échanges d'état civil et de contrôles physiques.",
  "Résumé, par un organisme public marocain, d'un rapport de la Cour des comptes non lu directement.", 'secondaire'))
IT_MININT = ('it_minint', src("Cruscotto statistico giornaliero (tableau de bord quotidien) au 28 novembre 2025", "Ministère italien de l'Intérieur, département des libertés civiles et de l'immigration", "28 novembre 2025",
  "https://libertaciviliimmigrazione.dlci.interno.gov.it/sites/default/files/2025-11/Cruscotto%20statistico%20giornaliero%2028-11-2025.pdf",
  "Débarquements du 1er janvier au 28 novembre : 152 216 en 2023, 62 264 en 2024 et 63 260 en 2025. Totaux annuels : 157 651 en 2023 et 66 617 en 2024. Mineurs non accompagnés débarqués : 18 820 en 2023, 8 752 en 2024, 11 661 en 2025 (au 24 novembre).",
  "Statistique officielle italienne."))
ISTAT_24 = ('istat_24', src("Indicatori demografici – Anno 2024", "ISTAT (institut national de statistique italien)", "mars 2025",
  "https://www.istat.it/wp-content/uploads/2025/03/Indicatori_demografici_2024.pdf",
  "En 2024, 435 000 immigrations depuis l'étranger, dont 382 000 d'étrangers ; solde migratoire avec l'étranger : +244 000. Au 1er janvier 2025, 5 422 000 étrangers résident en Italie (+169 000 en un an), soit 9,2 % de la population.",
  "Statistique publique italienne (données provisoires)."))
GC_MELONI = ('gc_meloni', src("Meloni va-t-elle vraiment admettre 500 000 migrants non-européens en trois ans pour travailler en Italie ?", "Le Grand Continent (Marin Saillofest)", "9 janvier 2026",
  "https://legrandcontinent.eu/fr/2026/01/09/meloni-va-t-elle-vraiment-admettre-500-000-migrants-non-europeens-en-trois-ans-pour-travailler-en-italie/",
  "Le décret de flux adopté à l'été 2025 autorise 500 000 entrées de travailleurs étrangers sur 2026-2028 ; le quota 2026 est de 164 850, contre 30 850 en 2019. Mais « la majorité de ces quotas ne sont toutefois pas pourvus » : en 2023, seuls 23,52 % des quotas ont abouti à un titre de séjour et un emploi stable.",
  "Revue d'analyse géopolitique.", 'media'))
EN_ALB = ('en_alb', src("EU court rebukes Italy over migrant transfers to Albania", "Euronews (Vincenzo Genovese)", "1er août 2025",
  "https://www.euronews.com/my-europe/2025/08/01/eu-court-rebukes-italy-over-migrant-transfers-to-albania",
  "La Cour de justice de l'UE donne raison à un tribunal italien qui contestait la désignation du Bangladesh comme pays sûr : la désignation doit pouvoir être contrôlée par un juge. Les centres en Albanie n'accueillent que quelques dizaines de personnes, pour un objectif de 3 000 par mois ; selon une étude universitaire italienne, une place y coûte plus de 153 000 €, contre 21 000 € en Sicile.",
  "Média européen.", 'media'))
POL_25 = ('pol_25', src("Minskat antal skjutningar men fler sprängningar under 2025 (Moins de fusillades mais plus d'explosions en 2025)", "Police suédoise (Polisen)", "5 janvier 2026",
  "https://polisen.se/aktuellt/nyheter/nationell/2026/januari/minskat-antal-skjutningar-men-fler-sprangningar-under-2025/",
  "158 fusillades en 2025 (46 morts, 44 blessés), contre 391 en 2022. En revanche, 189 explosions en 2025 contre 136 en 2024 : la violence d'intimidation et d'extorsion augmente. La police décrit le recrutement massif de très jeunes exécutants.",
  "Statistique policière officielle."))
POL_26 = ('pol_26', src("Skjutningarna på historiskt låga nivåer (Les fusillades à des niveaux historiquement bas)", "Police suédoise (Polisen)", "3 juillet 2026",
  "https://polisen.se/aktuellt/nyheter/nationell/2026/juli/skjutningarna-pa-historiskt-laga-nivaer/",
  "Au premier semestre 2026, 39 fusillades, 8 morts et 15 blessés : le niveau le plus bas depuis le début des statistiques en 2017. Premiers semestres précédents : 205 fusillades en 2022, 187 en 2023, 149 en 2024, 86 en 2025. La police attribue la baisse à un travail coordonné et à des centaines d'arrestations, tout en jugeant le niveau de conflit toujours élevé.",
  "Statistique policière officielle."))
BRA_25 = ('bra_25', src("Konstaterade fall av dödligt våld 2025 (Cas constatés de violence mortelle en 2025, rapport 2026:10)", "Brå, Conseil national suédois pour la prévention du crime", "2026",
  "https://bra.se/download/18.3b6b697b19d24d83762587f/1774614625537/2026_10_Konstaterade%20fall%20av%20d%C3%B6dligt%20v%C3%A5ld.pdf",
  "Cas de violence mortelle : 106 en 2016, 124 en 2020, 116 en 2022, 121 en 2023, 92 en 2024 et 84 en 2025. Le taux est de 1,1 à 1,2 pour 100 000 habitants de 2016 à 2023, puis 0,9 en 2024 et 0,8 en 2025. La part des homicides par arme à feu passe de 28 % (2016) à 54 % (2022), puis 50 % en 2025.",
  "Statistique publique suédoise."))
BRA_GUN = ('bra_gun', src("Gun homicide in Sweden and other European countries (rapport 2021:8)", "Brå, Conseil national suédois pour la prévention du crime (Klara Hradilova-Selin)", "26 mai 2021",
  "https://bra.se/english/publications/archive/2021-05-26-gun-homicide-in-sweden-and-other-european-countries",
  "La Suède compte environ 4 homicides par arme à feu par million d'habitants et par an, contre environ 1,6 en moyenne européenne ; sa hausse n'a pas d'équivalent dans les 22 pays étudiés. Elle est étroitement liée aux milieux criminels des quartiers socialement défavorisés : 8 homicides par arme à feu sur 10 surviennent en milieu criminel.",
  "Étude d'un organisme public suédois.", 'etude'))
BRA_ORIG = ('bra_orig', src("Registered offending among persons of native and non-native background (rapport 2021:9)", "Brå, Conseil national suédois pour la prévention du crime", "25 août 2021",
  "https://bra.se/english/publications/archive/2021-08-25-registered-offending-among-persons-of-native-and-non-native-background",
  "Le risque d'être enregistré comme suspect est plus élevé chez les personnes nées à l'étranger, et plus encore chez celles nées en Suède de deux parents nés à l'étranger ; une grande partie de l'écart tient à la structure par âge. La proportion de suspects a baissé entre 2007 et 2018 dans tous les groupes, avec des exceptions. L'étude est descriptive, n'explique pas les causes et porte sur des suspects, non sur des condamnés.",
  "Étude d'un organisme public suédois.", 'etude'))
SEN_VOTE = ('sen_vote', src("Proposition de loi constitutionnelle visant à accorder le droit de vote et d'éligibilité aux élections municipales aux étrangers non ressortissants de l'Union européenne (texte adopté n° 21)", "Sénat", "8 décembre 2011",
  "https://www.senat.fr/leg/tas11-021.pdf",
  "Le Sénat adopte un article 72-5 de la Constitution ouvrant le vote et l'éligibilité aux municipales aux « étrangers non ressortissants de l'Union européenne résidant en France ». Ces étrangers ne peuvent pas exercer les fonctions de maire ou d'adjoint, ni participer à l'élection des sénateurs.",
  "Texte parlementaire."))
AN_VOTE = ('an_vote', src("Rapport n° 2428 de la commission des lois sur la proposition de loi constitutionnelle n° 149 (deuxième lecture)", "Assemblée nationale (rapporteure Léa Balage El Mariky)", "4 février 2026",
  "https://www.assemblee-nationale.fr/dyn/17/rapports/cion_lois/l17b2428_rapport-fond.pdf",
  "Le texte reprend la proposition adoptée par l'Assemblée le 3 mai 2000, puis par le Sénat le 8 décembre 2011. Le rapport rappelle la promesse de François Mitterrand en 1981 et celle de François Hollande en 2012, et que depuis la révision consécutive à la décision du Conseil constitutionnel de 1992, l'article 88-3 de la Constitution ouvre le vote municipal aux citoyens de l'UE, effectif depuis 2001. Une adoption conforme déclencherait un référendum (article 89).",
  "Rapport parlementaire."))
LCP_VOTE = ('lcp_vote', src("Droit de vote des étrangers aux municipales : la proposition de loi écologiste adoptée en commission", "LCP (Maxence Kagni)", "4 février 2026",
  "https://lcp.fr/actualites/droit-de-vote-des-etrangers-aux-municipales-la-proposition-de-loi-ecologiste-adoptee-en",
  "Toute la gauche (écologistes, insoumis, socialistes, communistes) a permis l'adoption en commission ; le socle gouvernemental, le RN, l'UDR et LIOT sont contre. Pour la Droite républicaine, le droit de vote est lié à la nationalité. Le texte devrait être approuvé par référendum pour entrer en vigueur.",
  "Média parlementaire.", 'media'))
LCP_NICHE = ('lcp_niche', src("Les députés écologistes dénoncent « l'asphyxie » de leur niche parlementaire", "LCP (Anne-Charlotte Dusseaulx)", "10 février 2026",
  "https://lcp.fr/actualites/les-deputes-ecologistes-denoncent-l-asphyxie-de-leur-niche-parlementaire-430944",
  "La droite et l'extrême droite ont déposé 501 amendements ; les écologistes ont placé le texte en dernière position de leur niche du 12 février, ce qui lui enlève a priori toute chance d'être examiné.",
  "Média parlementaire.", 'media'))
INSEE_DISC = ('insee_disc', src("En dix ans, le sentiment de discrimination augmente, porté par les femmes et le motif sexiste (Insee Première n° 1911)", "Insee et Ined (J. Lê, O. Rouhban, P. Tanneau, C. Beauchemin, M. Ichou, P. Simon)", "5 juillet 2022, actualisé le 23 février 2023",
  "https://www.insee.fr/fr/statistiques/6473349",
  "Enquête Trajectoires et Origines 2 (2019-2020), 18-49 ans, France métropolitaine. 15 % des personnes sans ascendance migratoire déclarent des traitements inégalitaires ou des discriminations, tous motifs confondus, contre 10 % en 2008-2009 ; la moyenne est de 18 %. Pour le motif « origine, nationalité ou couleur de peau », le taux est de 8 % pour l'ensemble, 22 % pour les immigrés et 20 % pour les descendants d'immigrés, et environ un tiers pour les personnes originaires d'Afrique hors Maghreb.",
  "Statistique publique de référence."))
INED_RAC = ('ined_rac', src("Expérience et perception des discriminations et du racisme (séminaire de valorisation TeO)", "Ined (Christelle Hamel)", "non daté (données TeO 2008)",
  "https://teo.site.ined.fr/fichier/rte/2/Mini%20sites/Teo/seminaire%20valorisation/discriminations.et.racisme.fr.pdf",
  "18-50 ans, insultes, propos ou attitudes racistes subis au cours de la vie : 36 % des descendants d'immigrés, 32 % des immigrés et 16 % de la population majoritaire. Discriminations déclarées sur cinq ans : 31 % pour les descendants de deux parents immigrés, 26 % pour les immigrés, 10 % pour la population majoritaire. Pour la population majoritaire, le racisme subi n'est pas lié à des discriminations en raison de l'origine, contrairement aux immigrés et à leurs enfants.",
  "Exploitation de l'enquête de l'Ined et de l'Insee (données de 2008).", 'etude'))
CNCDH_25 = ('cncdh_25', src("Rapport sur la lutte contre le racisme, l'antisémitisme et la xénophobie – Année 2025 (Les Essentiels)", "Commission nationale consultative des droits de l'homme (CNCDH)", "juin 2026",
  "https://www.cncdh.fr/sites/default/files/2026-06/CNCDH%20Essentiels%20du%20rapport%20racisme%202025.pdf",
  "Selon l'enquête Vécu et ressenti en matière de sécurité du SSMSI (2023), environ 1,2 million de personnes de 14 ans et plus s'estiment victimes chaque année d'au moins une atteinte raciste, antisémite ou xénophobe, et 97 % ne portent pas plainte. Le ministère de l'Intérieur a enregistré 9 737 crimes et délits à caractère raciste en 2025. L'indice de tolérance est de 64 sur 100.",
  "Autorité administrative indépendante."))

# ── Sources : sécurité, justice ─────────────────────────────────────────────
AFP_FRANCO = ('afp_franco', src("'Francocide': new French far-right term enters language battle", "AFP, republié par The Local France", "16 juin 2023",
  "https://www.thelocal.fr/20230616/francocide-new-french-far-right-term-enters-language-battle",
  "D'après l'AFP, Éric Zemmour a forgé le terme lors d'un discours en septembre 2022, sur le modèle de « génocide » ou « féminicide » ; le RN évitait alors le mot. Le politiste Philippe Corcuff le relie à la théorie du « grand remplacement ». L'article ne cite aucune statistique d'homicide : ses seuls chiffres mesurent la diffusion du mot sur les réseaux sociaux.",
  "Dépêche d'agence reprise par un média.", 'media'))
ULG_FRANCO = ('ulg_franco', src("Eric Zemmour et le « grand remplacement »", "François Debras (Université de Liège / HELMo)", "non daté (sources consultées en juillet 2024)",
  "https://orbi.uliege.be/bitstream/2268/326783/1/Eric%20Zemmour%20et%20le%20%C2%AB%20grand%20remplacement%20%C2%BB%20(FDEBRAS).pdf",
  "Zemmour définit le francocide comme « un crime contre un Français par un étranger ». Le terme sert à décrire le peuple français comme occupé par une civilisation étrangère qui le remplacerait ; l'auteur le rattache à un registre guerrier et qualifie le « grand remplacement » de formule complotiste sans fondement dans les données.",
  "Analyse universitaire.", 'etude'))
BDT_SSMSI = ('bdt_ssmsi', src("Délinquance : une évolution contrastée sur les douze mois précédant les JO", "Banque des Territoires (Localtis), d'après le SSMSI", "30 octobre 2024",
  "https://www.banquedesterritoires.fr/delinquance-une-evolution-contrastee-sur-les-douze-mois-precedant-les-jo",
  "D'après le service statistique du ministère de l'Intérieur, sur douze mois glissants au 30 juin 2024, les homicides baissent de 8 % et les tentatives d'homicide augmentent de 11 %.",
  "Compte rendu de statistiques publiques.", 'secondaire'))
SEN_MIN = ('sen_min', src("Prévenir la délinquance des mineurs – Éviter la récidive (rapport d'information n° 885, partie II)", "Sénat, commissions de la culture et des lois", "21 septembre 2022",
  "https://www.senat.fr/rap/r21-885/r21-8856.html",
  "Le nombre de mineurs mis en cause passe de 98 864 en 1992 à 190 127 en 2019, mais n'augmente que de 6 % entre 2002 et 2019 ; leur part parmi les mis en cause reste proche de 18 % depuis 2002 (séries non validées par le SSMSI). Entre 2016 et 2021, les atteintes aux personnes augmentent (violences sexuelles sur mineurs +59,7 %, en partie par libération de la parole), les vols sans violence baissent de 28,4 % et les vols violents de 14,9 % ; les mineurs mis en cause pour trafic de stupéfiants augmentent de 35 %. La répartition par âge est globalement stable entre 2016 et 2019 : les difficultés statistiques empêchent de conclure à un rajeunissement.",
  "Rapport parlementaire."))
PS_ATTAL = ('ps_attal', src("Justice des mineurs : le Conseil constitutionnel censure largement le texte Attal, notamment la dérogation de l'excuse de minorité", "Public Sénat (Simon Barbarit)", "19 juin 2025",
  "https://www.publicsenat.fr/actualites/politique/justice-des-mineurs-le-conseil-constitutionnel-censure-largement-le-texte-attal-notamment-la-derogation-de-lexcuse-de-minorite",
  "La loi prévoyait d'inverser la règle pour les 16-18 ans récidivistes : le juge aurait dû motiver l'application de l'atténuation de peine, et non plus son exclusion. Le Conseil constitutionnel a censuré cette disposition au nom du « principe de l'atténuation de la responsabilité pénale des mineurs en fonction de l'âge », ainsi que la comparution immédiate dès 16 ans, au nom de l'exigence de « relèvement éducatif et moral des mineurs ». Les dispositions sur la responsabilité des parents ont été validées.",
  "Média parlementaire.", 'media'))
LCP_ATTAL = ('lcp_attal', src("Justice des mineurs : le Conseil constitutionnel censure plusieurs articles de la loi de Gabriel Attal", "LCP (Anne-Charlotte Dusseaulx)", "19 juin 2025",
  "https://lcp.fr/actualites/justice-des-mineurs-le-conseil-constitutionnel-censure-plusieurs-articles-de-la-loi-de",
  "Six articles sont censurés en tout ou partie. Sur l'excuse de minorité, le Conseil estime que l'atténuation doit rester la règle et son absence l'exception ; la comparution immédiate doit être réservée à des infractions suffisamment graves ou à des cas exceptionnels.",
  "Média parlementaire.", 'media'))
JUST_205 = ('just_205', src("Infostat Justice n° 205", "Ministère de la Justice, service statistique", "novembre 2025",
  "https://www.justice.gouv.fr/sites/default/files/2025-11/Infostat_Justice_205.pdf",
  "Les mineurs représentent 39,4 % des mis en cause pour viols et agressions sexuelles sur mineurs entre 2017 et 2024. Les mises en cause de mineurs pour viol sur mineur augmentent de 109 % entre 2020 et 2024, ce que l'étude explique en partie par le confinement et la libération de la parole ; 31 % de ces mineurs ont moins de 13 ans.",
  "Statistique publique."))
ONISR_80 = ('onisr_80', src("Limitation de vitesse à 80 km/h sur les routes hors agglomération sans séparation centrale", "Observatoire national interministériel de la sécurité routière (évaluation Cerema-ONISR)", "20 juillet 2020, mis à jour le 14 août 2020",
  "https://www.onisr.securite-routiere.gouv.fr/etudes-et-recherches/evaluation/evaluation-des-mesures/limitation-de-vitesse-a-80-kmh-sur-les-routes-hors-agglomeration-sans-separation-centrale",
  "L'évaluation conclut à « 349 vies épargnées les 20 premiers mois de la mesure » (juillet 2018 à février 2020), par rapport à la moyenne 2013-2017. Les voitures roulent en moyenne 3,5 km/h moins vite. Le nombre d'accidents ne change pas, mais leur gravité baisse : de 15,2 à 13,7 tués pour 100 accidents. Le bilan socio-économique est d'environ +700 M€ par an.",
  "Évaluation officielle."))
CEREMA_80 = ('cerema_80', src("Lowering of the maximum authorised speed to 80 km/h – Final assessment report", "Cerema", "20 juillet 2020",
  "https://www.cerema.fr/en/node/7630",
  "Sur 18 mois, le réseau concerné compte 331 tués de moins que la référence 2013-2017, 349 en ajoutant janvier et février 2020 ; la baisse est d'environ 12 % par rapport au reste du réseau. La vitesse moyenne baisse de 3,3 km/h (143 millions de passages mesurés) ; le temps de trajet augmente d'environ 1 seconde par kilomètre. En décembre 2019, 58 % des conducteurs de véhicules légers dépassaient encore 80 km/h.",
  "Établissement public d'expertise.", 'etude'))
ONISR_90 = ('onisr_90', src("Le relèvement de la vitesse maximale autorisée à 90 km/h (synthèse)", "ONISR / Délégation à la sécurité routière", "mise à jour au 26 octobre 2022",
  "https://www.onisr.securite-routiere.gouv.fr/sites/default/files/2022-12/2022_ONISR_Synthese%20de%20l%20impact%20du%20relevement%20de%20la%20VMA%20%C3%A0%2090kmh.pdf",
  "Entre la référence 2013-2017 et 2021, la mortalité baisse de 21,3 % sur les routes restées à 80 km/h, contre 16,0 % sur celles repassées à 90 km/h. L'ONISR estime à 42 le nombre de tués supplémentaires en 2021, voire 74 en tenant compte des dates de relèvement. Au 26 octobre 2022, 44 départements avaient relevé environ 51 000 km de routes.",
  "Évaluation officielle."))
PS_493 = ('ps_493', src("Recours au 49-3 : les précédents depuis le gouvernement Rocard", "Public Sénat", "29 février 2020",
  "https://www.publicsenat.fr/actualites/politique/recours-au-49-3-les-precedents-depuis-le-gouvernement-rocard-181003",
  "Michel Rocard (1988-1991), faute de majorité absolue, a engagé sa responsabilité à 28 reprises, record en la matière. Suivent Édith Cresson (8), Pierre Bérégovoy (3), Édouard Balladur (1), Alain Juppé (2), Jean-Pierre Raffarin (2), Dominique de Villepin (1) et Manuel Valls (6). Jean-Marc Ayrault, François Fillon et Lionel Jospin ne l'ont jamais utilisé.",
  "Média parlementaire (décompte arrêté en 2020).", 'media'))
AN_493 = ('an_493', src("Fiche de synthèse n° 64 : La mise en cause de la responsabilité du Gouvernement", "Assemblée nationale", "non daté (postérieur à décembre 2024)",
  "https://www.assemblee-nationale.fr/dyn/contenu/telechargement/629167/file/Fiche%2064%20-%20Responsabilit%C3%A9%20du%20Gouvernement.pdf",
  "La révision de 2008 limite le 49.3, hors lois de finances et de financement de la sécurité sociale, à « un autre projet ou proposition de loi par session ». La fiche compte 39 usages sous la IXe législature (1988-1993, gouvernements Rocard, Cresson et Bérégovoy) et 23 sous la XVIe (2022-2024).",
  "Document officiel de l'Assemblée."))
TLN_493 = ('tln_493', src("« 49.3 budgétaire » et « 49.3 social »", "Jean de Saint Sernin (Université de Lille), congrès français de droit constitutionnel 2023", "2023",
  "https://cfdc2023.univ-tln.fr/wp-content/uploads/Atelier-1-DE-SAINT-SERNIN-Jean.pdf",
  "L'auteur compte 100 utilisations du 49.3 depuis 1958, sur 55 textes, dont 40 sur des textes budgétaires ou sociaux ; 11 pour Élisabeth Borne sur ces seuls textes. Selon lui, la révision de 2008 n'a pas entraîné de baisse significative de l'usage sur les textes financiers.",
  "Contribution universitaire.", 'etude'))
NFP_PROG = ('nfp_prog', src("Contrat de législature du Nouveau Front populaire", "Nouveau Front populaire (document hébergé par LFI)", "juin 2024",
  "https://lafranceinsoumise.fr/wp-content/uploads/2024/06/PROGRAMME-FRONT-POPULAIRE.pdf",
  "La section « Vers une 6e République » prévoit d'« Abolir la monarchie présidentielle dans la pratique des institutions », d'« Instaurer la proportionnelle », d'« Abroger le 49.3 » et d'« Instaurer le référendum d'initiative citoyenne (RIC) », puis de passer à une 6e République par une assemblée constituante.",
  "Programme électoral, cité pour décrire les propositions.", 'partisane'))

# ── Sources : international, économie, travail ────────────────────────────
OBR_BREXIT = ('obr_brexit', src("Brexit analysis", "Office for Budget Responsibility (organisme budgétaire public britannique)", "mise à jour du 20 juillet 2026",
  "https://obr.uk/forecasts-in-depth/the-economy-forecast/brexit-analysis/",
  "Dans sa prévision de mars 2026, l'OBR suppose que l'accord de commerce avec l'UE réduira la productivité de long terme de 4 % par rapport au maintien dans l'UE ; environ deux cinquièmes de cet effet étaient déjà réalisés à l'entrée en vigueur de l'accord. Exportations et importations seraient d'environ 15 % inférieures à long terme. L'hypothèse d'immigration nette a été relevée de 129 000 à 290 000 par an à moyen terme. En mars 2024, l'OBR jugeait son hypothèse sur le commerce « broadly on track » ; en mars 2022, il notait que le pays avait raté une grande partie de la reprise du commerce mondial après la pandémie.",
  "Prévision d'une institution publique indépendante (hypothèse de modélisation)."))
OBR_2020 = ('obr_2020', src("The effect on productivity of leaving the EU (encadré 2.1)", "Office for Budget Responsibility", "mars 2020",
  "https://obr.uk/box/the-effect-on-productivity-of-leaving-the-eu/",
  "L'effet du Brexit déjà constaté sur la productivité est relevé de 1,0 à 1,4 %, du fait d'un investissement plus faible. L'effet de long terme, dans un scénario d'accord de libre-échange, est estimé à environ 4 %, avec une fourchette large ; il doit mettre 15 ans à se matérialiser.",
  "Institution publique indépendante.", 'etude'))
YOUGOV_BX = ('yougov_bx', src("What do Britons think of Brexit, 10 years since the referendum?", "YouGov (Dylan Difford)", "9 juin 2026",
  "https://yougov.com/en-gb/articles/54925-what-do-britons-think-of-brexit-10-years-since-the-referendum",
  "30 % des Britanniques estiment que voter pour la sortie était le bon choix, 57 % une erreur ; 61 % jugent le Brexit un échec et 12 % un succès. Seuls 25 % des électeurs du Leave parlent de succès, mais 64 % d'entre eux maintiennent que voter pour la sortie était juste. 55 % sont favorables à un retour dans l'UE. Sondage en ligne auprès de 2 114 adultes, 2 et 3 juin 2026.",
  "Sondage d'un institut.", 'etude'))
ONS_MIG = ('ons_mig', src("Improving long-term international migration statistics: November 2025", "Office for National Statistics (ONS)", "18 novembre 2025",
  "https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/articles/improvinglongterminternationalmigrationstatisticsupdatingourmethodsandestimates/november2025",
  "Le pic révisé d'immigration nette atteint 944 000 sur l'année close en mars 2023 ; le dernier chiffre provisoire est de 345 000 pour l'année close en décembre 2024. Pour les ressortissants de l'UE, le solde est de −69 000 en décembre 2024 ; pour les non-Européens, le pic est révisé à 1 047 000 (mars 2023).",
  "Statistique publique britannique."))
KSH_FEC = ('ksh_fec', src("22.1.1.6. Live births, total fertility rate", "KSH (office central de statistique hongrois)", "mis à jour le 17 juillet 2026",
  "https://www.ksh.hu/stadat_files/nep/en/nep0006.html",
  "Indice de fécondité : 1,25 en 2010, 1,23 en 2011, 1,45 en 2015, 1,59 en 2020, 1,61 en 2021, puis 1,55 en 2022, 1,51 en 2023, 1,39 en 2024 et 1,31 en 2025. Naissances vivantes : 90 335 en 2010, 93 039 en 2021, 77 511 en 2024 et 72 017 en 2025.",
  "Statistique publique hongroise."))
AFP_HONG = ('afp_hong', src("Pour doper la natalité, la Hongrie adopte une mesure alléchante pour les parents", "La Libre Belgique / AFP", "29 avril 2025",
  "https://www.lalibre.be/international/europe/2025/04/29/pour-doper-la-natalite-la-hongrie-adopte-une-mesure-allechante-pour-les-parents-un-havre-fiscal-pour-les-familles-KJLLECBMCVDFNMMNDEJZQKMF5Y/",
  "La fécondité est tombée à 1,31 enfant par femme en mars 2025, contre un pic de 1,61 en 2021. Le gouvernement vise 2,1 en 2035. L'exonération à vie d'impôt sur le revenu pour les mères d'au moins deux enfants coûterait 2,3 Md€ d'ici 2029 selon le gouvernement ; elle s'ajoute aux prêts bébé, aux aides au logement et à la garde gratuite. L'AFP parle d'une stratégie coûteuse aux « effets mitigés ».",
  "Dépêche d'agence reprise par un quotidien.", 'media'))
AEI_HONG = ('aei_hong', src("Hungary's Fertility Outcomes Highlight Pro-Natal Policy Limitations", "American Enterprise Institute, Cosm (Vanessa Brown Calder)", "21 novembre 2025",
  "https://cosm.aei.org/hungarys-fertility-outcomes-highlight-pro-natal-policy-limitations/",
  "La Hongrie consacre environ 5 % de son PIB aux aides aux familles, selon les dispositifs inclus. Le démographe Wolfgang Lutz y voit surtout un effet de calendrier des naissances ; les indicateurs corrigés de ces effets montrent une fécondité plutôt stable de 2010 à 2021.",
  "Analyse d'un think tank conservateur américain.", 'etude'))
DARES_DET = ('dares_det', src("L'emploi de salariés détachés en 2022 (Dares Résultats n° 1)", "Dares, ministère du Travail", "janvier 2024",
  "https://dares.travail-emploi.gouv.fr/sites/default/files/22d3e4c99d4739c9e2107d81cbdc6a2e/Dares_resultats_emploi-salaries-detaches-2022.pdf",
  "En 2022, hors transport routier, 223 300 salariés ont été détachés au moins une fois en France, pour 646 900 détachements. En moyenne, 59 300 détachés sont présents à une date donnée, 18 % de moins qu'en 2019, soit 0,3 % de l'emploi salarié privé ; 1,5 % dans l'agriculture. Le BTP regroupe 42 % des détachés et l'industrie 29 %. 70 % viennent de l'UE.",
  "Statistique publique."))
PE_DET = ('pe_det', src("Posting of workers (fiches thématiques sur l'Union européenne)", "Parlement européen", "mars 2026",
  "https://www.europarl.europa.eu/factsheets/en/sheet/37/posting-of-workers",
  "La directive révisée de 2018 s'applique depuis le 30 juillet 2020 : les règles de rémunération du pays d'accueil s'appliquent dès le premier jour, « equal pay for the same work in the same place ». Les frais de voyage, de logement et de nourriture ne peuvent pas être déduits du salaire. Le détachement est limité à 12 mois, prolongeables de 6 ; au-delà, le droit du travail du pays d'accueil s'applique. Les détachements avaient augmenté de 44,4 % entre 2010 et 2014, en partie à cause des écarts de salaires et de coût du travail.",
  "Document officiel du Parlement européen."))
SEN_FRAUDE = ('sen_fraude', src("Lutter contre la fraude sociale, un impératif pour le juste droit (rapport d'information n° 599)", "Sénat, mission d'évaluation et de contrôle de la sécurité sociale", "28 juin 2017",
  "https://www.senat.fr/rap/r16-599/r16-5994.html",
  "Le rapport décrit des fraudes au détachement : entreprises qui ne versent pas de cotisations dans le pays d'origine, sociétés « boîtes aux lettres » sans activité réelle, agences d'intérim créées uniquement pour détacher. Il juge les moyens de contrôle limités. Les formulaires de détachement reçus par la France sont passés de 7 500 en 2000 à 190 000 en 2015.",
  "Rapport parlementaire (2017, avant la révision de la directive)."))
EUROSTAT_SM = ('eurostat_sm', src("Now available: first 2026 data on minimum wages", "Eurostat", "30 janvier 2026",
  "https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260130-2",
  "Au 1er janvier 2026, six pays dépassent 1 500 € brut par mois : Luxembourg 2 704 €, Irlande 2 391 €, Allemagne 2 343 €, Pays-Bas 2 295 €, Belgique 2 112 €, France 1 823 €. Huit pays sont entre 1 000 et 1 500 €, huit en dessous de 1 000 €. En standards de pouvoir d'achat, la France fait partie des huit pays au-dessus de 1 500 SPA. Danemark, Italie, Autriche, Finlande et Suède n'ont pas de salaire minimum national.",
  "Statistique publique européenne."))
EUROSTAT_SE = ('eurostat_se', src("Minimum wage statistics (Statistics Explained)", "Eurostat", "juillet 2026",
  "https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Minimum_wage_statistics",
  "Au 1er juillet 2026, le salaire minimum est de 1 867 € en France, 2 771 € au Luxembourg et 620 € en Bulgarie. En 2024, le salaire minimum de la France dépasse 60 % du salaire médian horaire brut, comme aux Pays-Bas et au Luxembourg ; il est entre 50 et 60 % en Allemagne, en Irlande et en Espagne.",
  "Statistique publique européenne."))
INSEE_SMIC = ('insee_smic', src("Salaire minimum de croissance (Insee Références, Emploi, chômage, revenus du travail)", "Insee, d'après la Dares", "2 juillet 2026",
  "https://www.insee.fr/fr/statistiques/8733087",
  "Au 1er novembre 2024, 2,2 millions de salariés ont bénéficié directement de la revalorisation du SMIC, soit 12,4 % des salariés du champ étudié (17,3 % en janvier 2023) ; 19,4 % dans les entreprises de moins de 10 salariés et 24,5 % chez les salariés à temps partiel. Le SMIC horaire brut est de 12,02 € au 1er janvier 2026.",
  "Statistique publique."))
CC_VILLE26 = ('cc_ville26', src("Articuler davantage la politique de la ville et les politiques de droit commun dans les quartiers prioritaires (Rapport public annuel 2026)", "Cour des comptes", "mars 2026",
  "https://www.ccomptes.fr/sites/default/files/2026-03/20260325-RPA-2026-3e-partie_0.pdf",
  "Le programme budgétaire 147 (politique de la ville) a consommé 524 M€ en 2024, niveau stable depuis 2020. De 2004 à 2024, 11 Md€ cumulés pour les actions des contrats de ville et 14 Md€ pour le renouvellement urbain. « Le montant global des moyens budgétaires dont bénéficient les QPV est dès lors inconnu. » La Cour signale un « risque de substitution ou d'éviction des crédits de droit commun ». Pauvreté : 44 % dans les quartiers prioritaires contre 15 % en métropole ; chômage passé de 25 % à 18 % entre 2014 et 2022 ; revenu médian +10 % de 2017 à 2022 contre +17 % pour la France.",
  "Rapport de la juridiction financière."))
CC_VILLE20 = ('cc_ville20', src("Evaluation of the Attractiveness of Priority Neighbourhoods (synthèse du rapport « L'évaluation de l'attractivité des quartiers prioritaires »)", "Cour des comptes", "décembre 2020",
  "https://www.ccomptes.fr/sites/default/files/2021-07/20201202-summary-Evaluating-attractiveness-targeted-poor-districts.pdf",
  "Le premier programme de rénovation urbaine (2003-2012) a mobilisé 12 Md€ de fonds publics pour 46,1 Md€ d'investissements. L'attractivité des quartiers a peu progressé entre 2008 et 2018 et la concentration de pauvreté a à peine diminué. Les dépenses de droit commun sont mal identifiées ; dans six des huit quartiers étudiés, le droit commun ne bénéficie pas, ou pas systématiquement, au quartier.",
  "Rapport de la juridiction financière (synthèse en anglais)."))
AN_93 = ('an_93', src("Évaluation de l'action de l'État dans l'exercice de ses missions régaliennes en Seine-Saint-Denis (rapport d'information n° 1014)", "Assemblée nationale, comité d'évaluation et de contrôle (F. Cornut-Gentille, R. Kokouendo)", "31 mai 2018",
  "https://www.assemblee-nationale.fr/15/pdf/rap-info/i1014.pdf",
  "En 2015-2016, les absences courtes des enseignants du primaire étaient remplacées à 51,26 % en Seine-Saint-Denis contre 78,41 % en France. Au tribunal d'instance d'Aubervilliers, il fallait 12 mois pour obtenir une audience contre 2 mois à Paris. Le rapport conclut à « l'échec de l'État, et en conséquence de la République ».",
  "Rapport parlementaire transpartisan (données 2015-2017)."))

# ── Sources : école, travail, retraites ────────────────────────────────────
IH2EF_PROF = ('ih2ef_prof', src("Temps de travail des enseignants", "IH2EF (ministère de l'Éducation nationale), d'après la Note d'information DEPP n° 22.30", "7 novembre 2022",
  "https://www.ih2ef.gouv.fr/temps-de-travail-des-enseignants",
  "La moitié des enseignants à temps plein déclare travailler au moins 43 heures par semaine (enquête de 2018). L'enseignement face aux élèves représente 59 % du temps de travail dans le premier degré et 49 % dans le second degré, où la préparation et la correction pèsent davantage. Les enseignants déclarent aussi travailler pendant les vacances.",
  "Synthèse publiée par un institut du ministère."))
WEKA_PROF = ('weka_prof', src("Les enseignants déclarent travailler plus de 41 heures par semaine", "Weka (d'après la DEPP)", "10 novembre 2025",
  "https://www.weka.fr/actualite/education/article/les-enseignants-declarent-travailler-plus-de-41-heures-par-semaine-206718/",
  "En 2022-2023, les enseignants à temps plein déclarent 41,4 heures par semaine hors vacances : 53 % d'enseignement devant les élèves, 33 % de préparation et de correction, 15 % d'autres activités. Ils déclarent en moyenne 33 jours travaillés pendant les vacances, soit environ 1 635 heures par an, 28 de plus que les 1 607 heures légales.",
  "Média spécialisé relayant une publication de la DEPP.", 'secondaire'))
LEGI_ORS = ('legi_ors', src("Décret n° 2014-940 du 20 août 2014 relatif aux obligations de service des enseignants du second degré", "Légifrance", "20 août 2014 (version en vigueur)",
  "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000029390906",
  "L'article 2 fixe le maximum de service d'enseignement hebdomadaire à quinze heures pour les agrégés et à dix-huit heures pour les certifiés. Il range parmi les missions liées au service la préparation des cours, le suivi et l'évaluation des élèves, les relations avec les parents et le travail en équipe.",
  "Texte réglementaire."))
COR_SNCF = ('cor_sncf', src("Fiche régime : Caisse de prévoyance et de retraite du personnel ferroviaire (CPRPF)", "Conseil d'orientation des retraites (projections de juin 2024)", "juillet 2024",
  "https://cor-retraites.fr/sites/default/files/2024-07/Fiche_CPRPF%20%28SNCF%29.pdf",
  "Pour la pension d'ancienneté, l'âge minimal de base est de 55 ans pour les sédentaires et de 50 ans pour les conducteurs, relevé progressivement à 59 et 54 ans. La loi de 2018 a fermé le régime aux nouvelles recrues au 1er janvier 2020 ; les réformes de 2010, 2014 et 2023 y sont transposées avec un décalage. L'âge moyen de départ doit se stabiliser à 62 ans pour les sédentaires et 57 ans pour les conducteurs. En 2023, le régime compte 112 000 cotisants et 233 000 pensionnés.",
  "Organisme public d'expertise sur les retraites."))
PS_SNCF23 = ('ps_sncf23', src("Réforme des retraites : à quoi faut-il s'attendre pour les régimes spéciaux ?", "Public Sénat (Guillaume Jacquot)", "10 janvier 2023",
  "https://www.publicsenat.fr/actualites/politique/reforme-des-retraites-a-quoi-faut-il-s-attendre-pour-les-regimes-speciaux",
  "L'âge moyen de départ à la SNCF est de 56,9 ans selon un rapport de la Cour des comptes de 2019. Depuis le 1er janvier 2020, le régime n'accueille plus de nouveaux affiliés.",
  "Média parlementaire.", 'media'))
PS_SNCF24 = ('ps_sncf24', src("À la SNCF, un accord atténue une partie de la réforme des retraites", "Public Sénat (Romain David)", "23 avril 2024",
  "https://www.publicsenat.fr/actualites/economie/a-la-sncf-un-accord-attenue-une-partie-de-la-reforme-des-retraites-un-symbole-pour-la-gauche-une-catastrophe-pour-la-droite",
  "L'âge légal de départ à la SNCF va de 52 à 57 ans selon le poste ; le relèvement de deux ans prévu par la réforme de 2023 s'y applique à partir de 2025. L'accord d'avril 2024 crée une cessation anticipée d'activité pour les agents ayant au moins 20 ans de métier pénible. L'État verse environ 3 milliards d'euros par an pour les retraites des cheminots.",
  "Média parlementaire.", 'media'))
DREES_AGE = ('drees_age', src("L'âge moyen de départ à la retraite et son évolution (fiche 15, Les retraités et les retraites, édition 2025)", "DREES", "juillet 2025",
  "https://drees.solidarites-sante.gouv.fr/sites/default/files/2025-07/Fiche%2015%20-%20L%27%C3%A2ge%20moyen%20de%20d%C3%A9part%20%C3%A0%20la%20retraite%20et%20son%20%C3%A9volution.pdf",
  "Fin 2023, l'âge conjoncturel de départ se situe entre 56,2 et 59,8 ans pour la SNCF, la RATP et les industries électriques et gazières ; il est de 62 ans et 9 mois tous régimes confondus.",
  "Statistique publique."))
CE_ABAYA = ('ce_abaya', src("Laïcité : l'interdiction du port de tenues de type abaya à l'école est conforme à la loi", "Conseil d'État", "27 septembre 2024",
  "https://conseil-etat.fr/actualites/laicite-l-interdiction-du-port-de-tenues-de-type-abaya-a-l-ecole-est-conforme-a-la-loi",
  "Le Conseil d'État valide l'interdiction des abayas décidée à la rentrée 2023 sur le fondement de la loi du 15 mars 2004. Les signalements d'atteintes à la laïcité sont passés à 4 710 en 2022-2023, contre 2 167 et 2 226 les deux années précédentes ; ceux qui concernent des tenues atteignent 1 984 en 2022-2023, contre 148 en 2020-2021 et 617 en 2021-2022, en majorité des abayas.",
  "Décision de la juridiction administrative suprême."))
PS_LAIC = ('ps_laic', src("Diminution des atteintes à la laïcité à l'école : « Je ne suis pas sûr que la situation soit si idyllique »", "Public Sénat (Rose-Amélie Bécel)", "14 octobre 2024",
  "https://www.publicsenat.fr/actualites/education/diminution-des-atteintes-a-la-laicite-a-lecole-je-ne-suis-pas-sur-que-la-situation-soit-si-idyllique-assure-le-senateur-max-brisson",
  "Selon la ministre, il y a eu 838 atteintes à la laïcité en septembre 2023 et 110 en septembre 2024. Les chiffres varient fortement selon l'actualité et les consignes données aux personnels. Des sénateurs estiment que les atteintes ne se limitent pas à l'abaya (contestation d'enseignements, sport).",
  "Média parlementaire.", 'media'))
CHN_ABAYA = ('chn_abaya', src("French schools send dozens of girls home for violating new ban on Muslim robes", "Courthouse News (Cain Burdeau)", "septembre 2023",
  "https://www.courthousenews.com/french-schools-send-dozens-of-girls-home-for-violating-new-ban-on-muslim-robes/",
  "Selon le ministre de l'Éducation, 298 élèves se sont présentées en abaya le jour de la rentrée ; 67 ont été renvoyées chez elles pour avoir refusé de retirer leur tenue. L'article rappelle qu'il y a environ 12 millions d'élèves.",
  "Média américain rapportant des chiffres ministériels.", 'media'))
SEN_TRANS = ('sen_trans', src("Rapport n° 622 (2023-2024) sur la proposition de loi visant à encadrer les pratiques médicales chez les mineurs en questionnement de genre", "Sénat, commission des affaires sociales (rapporteur Alain Milon)", "22 mai 2024",
  "https://senat.fr/rap/l23-622/l23-6221.pdf",
  "En 2020, 294 mineurs sur 8 952 bénéficiaires étaient en affection de longue durée « transidentité » (3,3 %). Sur 1 615 séjours hospitaliers codés « transsexualisme », 48 concernaient des mineurs, dont aucun pour une chirurgie pelvienne. Dans le service de la Pitié-Salpêtrière, sur 239 jeunes reçus entre 2012 et 2022, 26 (11 %) ont reçu des bloqueurs de puberté (âge moyen 13,9 ans), 105 (44 %) des hormones (âge moyen 16,9 ans) et 30 une torsoplastie (âge moyen 18,4 ans, le plus jeune 16 ans) ; les chirurgies pelviennes n'y ont concerné que des majeurs.",
  "Rapport parlementaire (porté par la droite sénatoriale)."))
PS_TRANS = ('ps_trans', src("Transidentité : le Sénat examine la proposition de loi LR visant à encadrer la transition de genre des mineurs", "Public Sénat (Simon Barbarit)", "28 mai 2024",
  "https://www.publicsenat.fr/actualites/societe/transidentite-les-senateurs-examinent-la-proposition-de-loi-lr-visant-a-encadrer-la-transition-de-genre-des-mineurs",
  "La proposition de loi interdit les hormones et la chirurgie de réassignation avant 18 ans ; en commission, les bloqueurs de puberté ont été réautorisés dans des centres de référence. Les mineurs en affection de longue durée sont passés de 8 en 2013 à 294 en 2020. La gauche et les associations jugent le texte transphobe.",
  "Média parlementaire.", 'media'))
HAS_TRANS = ('has_trans', src("Transition de genre : la HAS publie les premières recommandations sur la prise en charge médicale de l'adulte", "Haute Autorité de santé", "18 juillet 2025",
  "https://has-sante.fr/jcms/p_3636602/fr/transition-de-genre-la-has-publie-les-premieres-recommandations-sur-la-prise-en-charge-medicale-de-l-adulte",
  "Les recommandations portent sur les personnes de 18 ans et plus ; les mineurs font l'objet de travaux séparés. Un peu plus de 22 000 personnes étaient en affection de longue durée pour « troubles de l'identité sexuelle » en 2023, tous âges confondus.",
  "Autorité publique de santé."))
BDT_UNIF = ('bdt_unif', src("Uniforme à l'école : mention passable et avenir incertain", "Banque des Territoires (Localtis, Jean-Damien Lesay), sur le rapport de la DEPP", "13 mai 2026",
  "https://www.banquedesterritoires.fr/uniforme-lecole-mention-passable-et-avenir-incertain",
  "L'expérimentation 2024-2025 porte sur 115 établissements volontaires (97 écoles, 14 collèges, 4 lycées). Dans le premier degré, 75 % des directeurs voient un effet positif sur le sentiment d'appartenance, mais 36 % seulement sur le climat scolaire. La DEPP conclut à des effets limités sur le comportement et les apprentissages. Coût : 1,6 million d'euros en 2024-2025, financé à moitié par l'État ; une généralisation à 200 € par trousseau coûterait 2,4 milliards d'euros pour 12 millions d'élèves.",
  "Compte rendu d'une évaluation publique.", 'secondaire'))
AFP_UNIF = ('afp_unif', src("Uniforme à l'école : des effets inégaux, selon une première étude", "L'Info Durable / AFP", "12 mai 2026",
  "https://www.linfodurable.fr/uniforme-lecole-des-effets-inegaux-selon-une-premiere-etude-56159",
  "57 % des écoliers n'aiment pas porter la tenue et 63 % des collégiens ne se sentent pas bien dedans ; 43 % des écoliers voient moins de moqueries sur les vêtements, 45 % ne voient pas de changement. L'évaluation, menée en juin 2025 par le service statistique du ministère, repose surtout sur des déclarations de chefs d'établissement.",
  "Dépêche AFP.", 'media'))
OSU_UNIF = ('osu_unif', src("School uniforms don't improve child behavior, study finds", "Ohio State University (étude d'Arya Ansari et al., Early Childhood Research Quarterly)", "20 décembre 2021",
  "https://news.osu.edu/school-uniforms-dont-improve-child-behavior-study-finds/",
  "L'étude suit 6 320 élèves américains de l'école élémentaire. Elle ne trouve aucun effet de l'uniforme sur l'anxiété, l'agressivité ou les compétences sociales. Il n'y a pas d'effet global sur l'assiduité. Les élèves plus âgés en uniforme déclarent un sentiment d'appartenance plus faible.",
  "Étude universitaire publiée dans une revue scientifique.", 'etude'))
UH_UNIF = ('uh_unif', src("UH Study Suggests School Uniforms Reduce Student Absences, Disciplinary Problems", "University of Houston (Scott Imberman, Elizabetta Gentile)", "vers 2010",
  "https://www.uh.edu/news-events/stories/2010articles/april2010/0405schooluniforms.php",
  "L'étude porte sur 160 écoles d'un district urbain entre 1993 et 2006. Elle constate une amélioration de l'assiduité et du comportement au collège et au lycée après l'adoption de l'uniforme, surtout chez les filles.",
  "Étude universitaire ancienne, un seul district.", 'etude'))

# ── Sources : écologie, LFI, RN ────────────────────────────────────────────
LCP_DUPLOMB = ('lcp_duplomb', src("Loi agricole Duplomb : le Conseil constitutionnel censure la réintroduction de l'acétamipride", "LCP (Raphaël Marchal)", "7 août 2025",
  "https://lcp.fr/actualites/loi-agricole-duplomb-le-conseil-constitutionnel-censure-la-reintroduction-de-l",
  "Le Conseil constitutionnel juge la réintroduction dérogatoire de l'acétamipride contraire à la Charte de l'environnement, le législateur ayant « privé de garanties légales le droit de vivre dans un environnement équilibré et respectueux de la santé ». Le reste de la loi est largement validé. Une pétition contre la loi a réuni plus de 2,1 millions de signatures en un peu moins d'un mois, un record.",
  "Média parlementaire.", 'media'))
PS_ACETA = ('ps_aceta', src("Néonicotinoïdes : qu'est-ce que l'acétamipride, pesticide réintroduit par la loi Duplomb ?", "Public Sénat (Louis Mollier-Sabet)", "26 mai 2025",
  "https://www.publicsenat.fr/actualites/economie/neonicotinoides-quest-ce-que-lacetamipride-pesticide-reintroduit-par-la-loi-duplomb",
  "La France a interdit l'acétamipride en 2018 ; l'Union européenne l'autorise jusqu'en 2033. Les filières concernées sont surtout la betterave sucrière et la noisette, et la FNSEA dénonce une concurrence déloyale. En 2024, l'Autorité européenne de sécurité des aliments a évoqué des « incertitudes majeures » sur les effets neurodéveloppementaux ; selon des chercheurs de l'INRAE, les effets sur les pollinisateurs sont clairement documentés.",
  "Média parlementaire.", 'media'))
ANSES_NNI = ('anses_nni', src("Risques et bénéfices des produits phytopharmaceutiques à base de néonicotinoïdes et de leurs alternatives", "Anses", "30 mai 2018",
  "https://www.anses.fr/fr/content/risques-et-benefices-des-produits-phytopharmaceutiques-base-de-neonicotinoides-et-de-leurs",
  "Sur 130 usages autorisés, l'agence trouve des alternatives efficaces et opérationnelles pour la majorité, mais aucune dans 6 cas. Dans 89 % des cas, l'alternative est chimique, et il existe au moins une alternative non chimique dans 78 % des cas. L'impact économique est jugé difficile à anticiper.",
  "Agence publique d'expertise (2018)."))
INRAE_NNI = ('inrae_nni', src("Alternatives chimiques et non chimiques existantes à l'usage des néonicotinoïdes", "INRAE (à la demande du ministère de l'Agriculture)", "octobre 2025",
  "https://www.inrae.fr/sites/default/files/pdf/rapportcompletnni-inrae-vf-27oct25.pdf",
  "Près d'un tiers des insecticides disponibles avant l'interdiction ont été retirés depuis. Dans les fermes du réseau DEPHY, une année sans néonicotinoïdes a causé des pertes de 60 à 80 % sur 7 fermes sur 294 (2,4 %). Le rendement national de la betterave a baissé d'environ 5 t/ha par rapport à la période d'avant 2018, avec de multiples causes possibles. La filière noisette est soumise à une telle pression sanitaire qu'elle est décrite comme au bord de la faillite ; aucune alternative isolée n'égale l'efficacité des néonicotinoïdes.",
  "Expertise d'un organisme public de recherche.", 'etude'))
AAF_BASS = ('aaf_bass', src("Avis sur les réserves de substitution : quelques conditions préalables à leur développement", "Académie d'agriculture de France", "février 2024",
  "https://www.academie-agriculture.fr/system/files_force/publications/avis-recommandations/2024/20240221avisacademiquereservessubstitution.pdf?download=1",
  "Les réserves sont « un des moyens » de mobiliser une ressource supplémentaire, sous conditions : seuils de prélèvement, transition agroécologique et gestion collective, présentée comme une condition du succès. Environ deux tiers du financement est public. Pour une réserve des Deux-Sèvres, l'évaporation annuelle est estimée à environ 12 % du volume maximal. Le modèle du BRGM montre un faible effet sur les débits et un effet positif sur les nappes en été ; avec le changement climatique, certaines réserves pourraient ne pas se remplir certaines années.",
  "Avis d'une académie savante."))
BDT_BASS = ('bdt_bass', src("« Mégabassines » : deux projets annulés par le tribunal administratif en Poitou-Charentes", "Banque des Territoires (Localtis, avec AFP)", "4 octobre 2023",
  "https://www.banquedesterritoires.fr/megabassines-deux-projets-annules-par-le-tribunal-administratif-en-poitou-charentes",
  "Le tribunal administratif de Poitiers annule deux autorisations portant sur 15 réserves (environ trois millions de m³). Les volumes reposaient sur des données du début des années 2000 et ne tenaient pas compte du changement climatique ; dans la Vienne, le tribunal relève un « sur-dimensionnement du projet ».",
  "Média des collectivités locales.", 'media'))
AFP_BASS = ('afp_bass', src("La justice confirme la réduction des prélèvements d'eau dans le Marais Poitevin", "AFP, publié par Terre-net", "26 septembre 2025",
  "https://www.terre-net.fr/irrigation/article/888144/la-justice-confirme-la-reduction-des-prelevements-d-eau-dans-le-marais-poitevin",
  "La cour administrative d'appel de Bordeaux juge excessifs les volumes d'irrigation autorisés en 2021 : les prélèvements doivent baisser d'environ un quart. Le projet de 16 retenues porté par un groupement de 450 agriculteurs coûte 78 M€, financé à moitié par l'État ; seules quatre réserves ont été construites. Les agriculteurs redoutent une catastrophe économique et sociale.",
  "Dépêche AFP.", 'media'))
LCP_UKR = ('lcp_ukr', src("L'Assemblée nationale soutient largement l'accord avec l'Ukraine, sans le RN qui s'abstient et LFI qui vote contre", "LCP (Ludovic Fau)", "12 mars 2024",
  "https://lcp.fr/actualites/l-assemblee-nationale-soutient-largement-l-accord-avec-l-ukraine-sans-le-rn-qui-s",
  "L'accord de sécurité France-Ukraine est approuvé par 372 voix contre 99 ; LFI et le PCF votent contre, le RN s'abstient. Un député LFI dénonce un président « va-t-en-guerre ». PS, écologistes, LIOT et la majorité de LR votent pour.",
  "Média parlementaire.", 'media'))
PS_UKR = ('ps_ukr', src("Guerre en Ukraine : « Les Insoumis n'ont jamais soutenu l'Ukraine, ils ont toujours été pro-Poutine », fustige Anne Hidalgo", "Public Sénat (Clarisse Guibert)", "13 mars 2025",
  "https://www.publicsenat.fr/actualites/international/guerre-en-ukraine-les-insoumis-nont-jamais-soutenu-lukraine-ils-ont-toujours-ete-pro-poutine-fustige-anne-hidalgo",
  "Le 12 mars 2025, l'Assemblée adopte une résolution de soutien à l'Ukraine qui condamne l'agression russe et encourage son adhésion à l'UE. LFI et une partie des communistes votent contre, au motif des problèmes sociaux et géopolitiques posés par cette adhésion. L'accusation « pro-Poutine » est celle d'une adversaire politique.",
  "Média parlementaire.", 'media'))
AN_UKR22 = ('an_ukr22', src("Compte rendu intégral de la séance du mardi 1er mars 2022 (débat sur la guerre en Ukraine)", "Assemblée nationale", "1er mars 2022",
  "https://www.assemblee-nationale.fr/dyn/15/comptes-rendus/seance/session-ordinaire-de-2021-2022/seance-du-mardi-01-mars-2022.pdf",
  "Jean-Luc Mélenchon, président du groupe LFI, impute au gouvernement de Vladimir Poutine la totale responsabilité de la guerre. Il plaide pour sortir de l'OTAN et donner la priorité à la diplomatie, et critique les livraisons d'armes, qui pourraient faire de la France une partie au conflit.",
  "Compte rendu officiel des débats."))
DFI_UKR = ('dfi_ukr', src("Le chemin de la paix est le seul raisonnable (communiqué)", "Délégation de la France insoumise au Parlement européen", "1er mars 2022",
  "https://d-fi.lafranceinsoumise.fr/wp-content/uploads/2022/03/CP-Ukraine-1.pdf",
  "La délégation dit avoir voté pour « la condamnation totale de cette agression » et pour la résolution finale du Parlement européen, mais contre les paragraphes sur les livraisons d'armes, le renforcement de l'OTAN et l'accélération de l'adhésion de l'Ukraine à l'UE.",
  "Communiqué partisan, cité pour décrire le vote de LFI.", 'partisane'))
PS_BINAT = ('ps_binat', src("Législatives 2024 : le RN peut-il interdire les « emplois sensibles » aux Français binationaux ?", "Public Sénat (Rose-Amélie Bécel)", "25 juin 2024",
  "https://www.publicsenat.fr/actualites/politique/legislatives-2024-le-rn-peut-il-interdire-les-emplois-sensibles-aux-francais-binationaux",
  "Jordan Bardella annonce vouloir « réserver un certain nombre d'emplois stratégiques dans les secteurs notamment liés à la sécurité et à la défense » ; Marine Le Pen parle de « quelques dizaines d'emplois très sensibles ». Une juriste estime que distinguer les Français selon leur mode d'acquisition de la nationalité romprait avec le principe d'égalité. Les emplois de souveraineté sont déjà réservés aux Français, et des habilitations permettent un filtrage au cas par cas. La proposition de loi constitutionnelle RN de janvier 2024 visait à interdire l'accès à des emplois dans l'administration.",
  "Média parlementaire.", 'media'))
LCP_BINAT = ('lcp_binat', src("Législatives 2024 : déclarations, événements... Retrouvez l'essentiel de la campagne au fil des jours", "LCP (Adèle Daumas)", "25 juin 2024, mis à jour le 3 juillet 2024",
  "https://lcp.fr/actualites/legislatives-2024-declarations-evenements-retrouvez-l-essentiel-de-la-campagne-au-fil",
  "Le programme du RN prévoit d'exclure les binationaux des postes « les plus stratégiques de l'État », soit une cinquantaine de postes, hors mandats électifs et fonctions ministérielles selon le parti. Un député RN a jugé que des binationaux ne devraient pas être ministres, en parlant d'un avis personnel ; Marine Le Pen l'a désavoué.",
  "Média parlementaire.", 'media'))
INED_BINAT = ('ined_binat', src("Trajectoires et Origines : enquête sur la diversité des populations en France (premiers résultats)", "Ined / Insee", "enquête 2008-2009",
  "https://www.ined.fr/fichier/rte/143/TeO2/4pages_Resultats_TeO1.pdf",
  "« En 2009, les binationaux représentent 5 % de l'ensemble de la population et près du quart des enfants d'immigré(s). » Les résultats portent sur les 18-50 ans.",
  "Statistique publique (données anciennes)."))
AEC_PROG = ('aec_prog', src("L'Avenir en commun – la version abrégée", "Programme de Jean-Luc Mélenchon / Union populaire", "avril 2022",
  "https://melenchon.fr/wp-content/uploads/2022/04/programme-avenir-en-commun-abrege.pdf",
  "Le programme prévoit de « Convoquer une Assemblée constituante par un référendum (article 11 de la Constitution) », dont les membres seraient élus ou tirés au sort, puis de soumettre le projet de Constitution à référendum. Il propose un régime parlementaire avec la proportionnelle, un référendum d'initiative citoyenne pour proposer ou abroger une loi, modifier la Constitution et révoquer les élus, le droit de vote à 16 ans et la reconnaissance du vote blanc.",
  "Programme électoral, cité pour décrire les propositions.", 'partisane'))
PS_RIC = ('ps_ric', src("Le RIC des Insoumis rejeté à l'Assemblée nationale", "Public Sénat (Charlotte Hill)", "21 février 2019",
  "https://www.publicsenat.fr/actualites/politique/le-ric-des-insoumis-rejete-a-l-assemblee-nationale-138267",
  "La proposition de loi constitutionnelle de LFI prévoyait des référendums d'initiative citoyenne pour proposer ou abroger une loi, révoquer les élus, président compris, et convoquer une assemblée constituante. La majorité jugeait trop bas le seuil de 2 % des électeurs ; le texte a été écarté par 91 voix contre 50.",
  "Média parlementaire.", 'media'))

FICHES = []

# 1 ── Rocard et « la misère du monde » ────────────────────────────────────────
FICHES.append(fiche(
 id='rocard-misere-du-monde', affirmation="« La France ne peut pas accueillir toute la misère du monde », même Michel Rocard le disait.", volet='immigration', sous_theme='Immigration et asile',
 mots_cles=['rocard', 'misere du monde', 'toute la misere du monde', 'accueillir toute la misere', 'citation de rocard', 'prendre sa part', 'en prendre fidelement sa part'],
 verdict='trompeur', fiabilite='etabli',
 resume="Michel Rocard a bien dit, en 1989, « nous ne pouvons pas héberger toute la misère du monde ». Mais il a ensuite toujours affirmé que la France devait « en prendre fidèlement sa part », et il a écrit en 2009 que la France et l'Europe « doivent accueillir toute la part qui leur revient ». Utiliser sa phrase pour justifier une fermeture, c'est lui faire dire le contraire de ce qu'il défendait.",
 contexte="La phrase est l'une des plus citées du débat sur l'immigration ; elle permet d'attribuer à un socialiste une position de fermeture.",
 explication="La version courte a été prononcée et répétée en 1989-1990. La seconde moitié (« en prendre sa part ») n'est clairement documentée qu'à partir de 1993-1996, mais Rocard l'a revendiquée jusqu'à la fin de sa vie.",
 sources=[INA_ROCARD, CFJ_ROCARD, CIMADE_ROCARD],
 faits=[
  fait("Le 3 décembre 1989, Michel Rocard déclare sur TF1 : « nous ne pouvons pas héberger toute la misère du monde ».", 'ina_rocard', '1989', 'France', "La version courte a bien été prononcée.", 'etabli'),
  fait("Le 13 décembre 1989, à l'Assemblée, il dit que « notre pays ne peut accueillir et soulager toute la misère du monde » et annonce un renforcement des contrôles aux frontières.", 'cfj_rocard', '1989', 'France', "À l'époque, la formule accompagnait une politique de contrôle.", 'etabli'),
  fait("À partir du milieu des années 1990, Rocard affirme que la France doit aussi « savoir en prendre fidèlement sa part ».", 'ina_rocard', '1993-1996', 'France', "Il revendique une seconde moitié à sa phrase.", 'etabli'),
  fait("En 2009, il écrit que la France et l'Europe « peuvent et doivent accueillir toute la part qui leur revient de la misère du monde ».", 'ina_rocard', '2009', 'France', "Sa position finale est un devoir d'accueil.", 'etabli'),
  fait("Aucune archive ne permet de vérifier qu'il ait prononcé la version longue dès novembre 1989.", 'cfj_rocard', '1989', 'France', "L'idée d'une citation « tronquée » dès l'origine n'est pas prouvée.", 'interpretation'),
 ],
 court="Trompeur : Rocard a bien dit en 1989 qu'on ne pouvait pas accueillir toute la misère du monde. Mais il a toujours ajouté ensuite que la France devait « en prendre fidèlement sa part ». Il défendait l'accueil, pas la fermeture.",
 moyen="La phrase a bien été prononcée par Michel Rocard, Premier ministre, en décembre 1989, et répétée plusieurs fois. Elle accompagnait alors un renforcement des contrôles aux frontières.\n\nMais Rocard a ensuite toujours expliqué que sa pensée avait une seconde moitié : la France doit « en prendre fidèlement sa part ». En 2009, il écrivait que la France et l'Europe « doivent accueillir toute la part qui leur revient ». Le citer pour refuser tout accueil, c'est trahir ce qu'il a défendu.",
 detaille="Le 3 décembre 1989, sur TF1, Michel Rocard déclare : « nous ne pouvons pas héberger toute la misère du monde ». Il le redit à l'Assemblée le 13 décembre, en annonçant un renforcement des contrôles aux frontières, puis en janvier 1990. Il ne faut donc pas nier que la version courte existe, ni qu'elle a servi une politique de contrôle.\n\nÀ partir de 1993, puis clairement dans une tribune de 1996, Rocard complète : la France doit « savoir en prendre fidèlement sa part ». Il assure l'avoir dit dès novembre 1989 devant la Cimade, mais aucune archive ne permet de le vérifier. En 2009, il écrit que la France et l'Europe « peuvent et doivent accueillir toute la part qui leur revient de la misère du monde ».\n\nLa phrase pose donc une vraie question, celle du partage de l'accueil, et non une justification du refus. C'est précisément le débat actuel : quelle part la France prend-elle, comparée à ses voisins ?",
 empathie="Je comprends qu'on ait l'impression qu'on ne peut pas accueillir tout le monde : personne ne le prétend. Même Rocard, qu'on cite souvent, disait que la vraie question était de prendre notre juste part.",
 legitimes=["La version courte a bien été prononcée, plusieurs fois, en 1989-1990.", "Elle accompagnait une politique de contrôle des frontières."],
 contre=[
  ("Rocard a inventé la seconde partie après coup.", "C'est possible pour 1989, aucune archive ne le prouve. Mais il l'a revendiquée publiquement pendant près de vingt ans : c'est bien sa position."),
  ("Peu importe, il avait raison sur le fond.", "Sur le fond, il défendait le partage de l'accueil, pas la fermeture. La vraie question est la part que la France prend."),
 ],
 questions=["Sais-tu ce que Rocard a ajouté à cette phrase dans les années suivantes ?", "Quelle serait, pour toi, la juste part de la France ?"],
 limites=["La tribune de 1996 et celle de 2009 n'ont été lues qu'à travers l'INA et le site du CFJ.", "Le témoignage de la Cimade émane d'une association partie prenante."],
 publics={'convaincus': "Rocard l'a bien dit, en 1989. Mais il a passé vingt ans à répéter la suite : la France doit « en prendre fidèlement sa part ». Le citer pour refuser tout accueil, c'est utiliser un socialiste contre ce qu'il pensait vraiment.",
  'indecis': "La phrase est réelle, mais incomplète. Rocard posait une question raisonnable : comment chaque pays prend-il sa juste part ? Personne ne propose d'accueillir tout le monde ; le débat porte sur la part de la France et les conditions de l'accueil."},
 a_actualiser='2028-06-30', raison="Sujet historique, à revoir si de nouvelles archives sont publiées.",
))

# 2 ── Centenaires « fantômes » ────────────────────────────────────────────────
FICHES.append(fiche(
 id='retraites-centenaires-algerie', affirmation="Des milliers de retraités centenaires fantômes à l'étranger, notamment en Algérie, touchent encore leur pension.", volet='social', sous_theme='Fraude sociale',
 mots_cles=['centenaires', 'retraites fantomes', 'centenaires algeriens', 'retraites en algerie', 'pensions a l etranger', 'certificat d existence', 'retraites morts', 'fraude aux pensions'],
 verdict='trompeur', fiabilite='etabli',
 resume="Il y avait fin 2023 environ 1 000 centenaires parmi les 337 000 retraités du régime général résidant en Algérie, soit 0,3 %, et non des milliers de « fantômes ». La proportion de centenaires y est proche de celle observée en France. La fraude aux décès non déclarés existe et les contrôles ont des failles, mais les missions de contrôle n'ont trouvé que peu de cas.",
 contexte="La rumeur revient régulièrement depuis un rapport de la Cour des comptes de 2010 ; elle a été relayée en 2024 sur des médias nationaux.",
 explication="Les retraités qui ont travaillé en France et vivent ailleurs touchent la pension pour laquelle ils ont cotisé. Ils doivent envoyer chaque année des certificats d'existence ; un décès non déclaré peut prolonger indûment le versement.",
 sources=[SURL_CENT, CNAV_ALG, AN_CENT, CCME_CC],
 faits=[
  fait("Au 31 décembre 2023, la CNAV compte environ 337 183 pensionnés résidant en Algérie, pour une pension moyenne de 262 € par mois, dont 1 018 centenaires (0,3 %).", 'surl_cent', '2023', 'Algérie', "On est loin de « milliers de fantômes ».", 'etabli', '1 018 centenaires'),
  fait("Fin 2020, les centenaires représentent 0,17 % des retraités du régime général vivant en Algérie, contre 0,12 % en France ; l'écart s'explique en partie par le creux des naissances en France pendant la Première Guerre mondiale.", 'cnav_alg', '2020', 'Algérie et France', "L'écart est faible et en partie démographique.", 'etabli', '0,17 % contre 0,12 %'),
  fait("En 2009, le taux de centenaires parmi les retraités vivant en Algérie était même « très légèrement inférieur » à celui de France (0,096 % contre 0,097 %).", 'an_cent', '2009', 'Algérie et France', "Le gouvernement réfutait déjà la rumeur.", 'etabli'),
  fait("La CNAV reconnaît que la mortalité de ces retraités peut être « légèrement sous-estimée » à cause de décès non déclarés.", 'cnav_alg', '2021', 'Algérie', "Il y a bien des décès non déclarés.", 'etabli'),
  fait("Lors de contrôles menés entre 2019 et 2022 sur 2 500 dossiers de retraités à l'étranger, 2,27 % des documents n'étaient pas conformes, selon la Cour des comptes.", 'ccme_cc', '2019-2022', 'Retraités résidant hors de France', "La fraude existe, mais reste minoritaire.", 'estimation', '2,27 %'),
 ],
 court="Trompeur : fin 2023, il y avait environ 1 000 centenaires parmi 337 000 retraités du régime général vivant en Algérie, soit 0,3 %. La proportion est proche de celle de la France. Des fraudes existent, mais les contrôles en trouvent peu.",
 moyen="La rumeur part d'un rapport de 2010, contesté depuis par l'administration. Les chiffres de la CNAV montrent environ 1 000 centenaires parmi les retraités vivant en Algérie, qui touchent en moyenne 262 € par mois. La part de centenaires y est proche de celle de France.\n\nDes décès ne sont pas toujours déclarés, et la Cour des comptes demande plus de contrôles : c'est un vrai sujet. Mais ces retraités ont cotisé en France, souvent pendant des décennies, et l'immense majorité sont bien vivants.",
 detaille="Fin 2023, environ 337 000 retraités du régime général résidaient en Algérie, avec une pension moyenne de 262 € par mois. Parmi eux, 1 018 centenaires, soit 0,3 %. En 2020, la CNAV comptait 0,17 % de centenaires parmi ces retraités, contre 0,12 % en France, un écart en partie lié au creux des naissances en France pendant la Grande Guerre. En 2009, le taux était même légèrement inférieur à celui de France.\n\nLa fraude existe : faux actes d'état civil relevés dans une commune par la Cour des comptes, décès non déclarés que la CNAV elle-même reconnaît. Sur des contrôles de 2 500 dossiers entre 2019 et 2022, 2,27 % des documents n'étaient pas conformes. La Cour recommande plus d'échanges d'état civil, et la biométrie est expérimentée depuis 2024.\n\nCes retraités sont d'anciens travailleurs immigrés qui ont cotisé en France. Lutter contre la fraude est légitime ; présenter tous ces retraités comme des « fantômes » ne l'est pas.",
 empathie="C'est normal d'être choqué à l'idée que des morts touchent une pension. Les contrôles doivent être sérieux. Mais les chiffres montrent quelques centaines de cas possibles, pas des milliers.",
 legitimes=["Des décès ne sont pas déclarés et la CNAV le reconnaît.", "La Cour des comptes pointe des failles dans les contrôles à l'étranger."],
 contre=[
  ("La Cour des comptes l'a dit en 2010.", "Ce rapport a été contesté par l'administration, et les chiffres officiels ultérieurs montrent une part de centenaires proche de celle de France."),
  ("Ils n'ont rien cotisé.", "Ils touchent la retraite des années travaillées en France ; la pension moyenne de 262 € reflète souvent des carrières incomplètes."),
 ],
 questions=["Sais-tu combien touche en moyenne un retraité du régime général vivant en Algérie ?", "Ne vaut-il pas mieux renforcer les contrôles que soupçonner tout le monde ?"],
 limites=["Le rapport de la Cour des comptes de 2025 n'a été lu qu'à travers un résumé.", "Le montant total de la fraude n'est pas établi par une source lue."],
 publics={'convaincus': "Les chiffres officiels comptent environ 1 000 centenaires sur 337 000 retraités vivant en Algérie, une proportion proche de celle de la France. Il y a des fraudes, et il faut les traquer. Mais ces retraités ont travaillé et cotisé ici, et la plupart touchent quelques centaines d'euros.",
  'indecis': "La fraude aux décès non déclarés existe, et la Cour des comptes demande plus de contrôles. Mais l'ordre de grandeur est faible : environ 0,3 % de centenaires, et 2,27 % de documents non conformes lors des contrôles. Le vrai sujet, c'est la qualité des contrôles, pas une invasion de « fantômes »."},
 a_actualiser='2027-06-30', raison="Nouvelles données de la CNAV et généralisation de la biométrie.",
))

# 3 ── Meloni et l'immigration ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='meloni-immigration-italie', affirmation="Giorgia Meloni a stoppé l'immigration en Italie.", volet='immigration', sous_theme='Comparaisons européennes',
 mots_cles=['meloni', 'italie immigration', 'arrivees en italie', 'lampedusa', 'albanie', 'centres en albanie', 'modele italien', 'debarquements'],
 verdict='contredit', fiabilite='etabli',
 resume="Les débarquements en Italie ont fortement baissé après le pic de 2023, atteint sous Giorgia Meloni : de 157 651 en 2023 à 66 617 en 2024. Mais l'immigration n'est pas stoppée : l'Italie a accueilli 382 000 immigrants étrangers en 2024, et le gouvernement Meloni a autorisé 500 000 entrées de travailleurs étrangers pour 2026-2028. Les centres de rétention en Albanie restent quasi vides.",
 contexte="L'extrême droite française présente l'Italie de Meloni comme la preuve qu'une politique de fermeture fonctionne.",
 explication="Les arrivées irrégulières par la mer ne sont qu'une petite partie de l'immigration : la majorité passe par des voies légales (travail, famille, études). Un gouvernement peut réduire l'une et augmenter l'autre.",
 sources=[IT_MININT, ISTAT_24, GC_MELONI, EN_ALB],
 faits=[
  fait("Les débarquements en Italie sont passés de 157 651 en 2023 à 66 617 en 2024 ; du 1er janvier au 28 novembre, ils étaient de 63 260 en 2025.", 'it_minint', '2023-2025', 'Italie', "La baisse est réelle après le pic de 2023, survenu sous Meloni.", 'etabli', '-58 %'),
  fait("En 2024, l'Italie a enregistré 435 000 immigrations, dont 382 000 d'étrangers ; 5,4 millions d'étrangers y résident au 1er janvier 2025, soit 9,2 % de la population.", 'istat_24', '2024-2025', 'Italie', "L'immigration totale reste élevée.", 'etabli', '382 000'),
  fait("Le gouvernement Meloni a autorisé 500 000 entrées de travailleurs étrangers sur 2026-2028 ; le quota 2026 est de 164 850, contre 30 850 en 2019.", 'gc_meloni', '2019-2028', 'Italie', "Meloni a elle-même ouvert la porte à l'immigration de travail.", 'etabli', '500 000'),
  fait("La majorité de ces quotas ne sont pas pourvus : en 2023, seuls 23,52 % ont abouti à un titre de séjour et un emploi stable.", 'gc_meloni', '2023', 'Italie', "Les quotas affichés ne sont pas des entrées effectives.", 'estimation', '23,52 %'),
  fait("Les centres italiens en Albanie n'accueillent que quelques dizaines de personnes pour un objectif de 3 000 par mois, et la Cour de justice de l'UE a exigé un contrôle par le juge de la notion de pays sûr.", 'en_alb', '2025', 'Italie et Albanie', "La mesure phare est bloquée.", 'etabli'),
 ],
 court="Faux : les débarquements ont baissé après le record de 2023, atteint sous Meloni. Mais l'Italie a accueilli 382 000 immigrants étrangers en 2024, et Meloni a autorisé 500 000 travailleurs étrangers pour 2026-2028. Les centres en Albanie restent quasi vides.",
 moyen="La baisse des arrivées par la mer est réelle : de 157 651 en 2023 à 66 617 en 2024. Mais le record de 2023 a eu lieu sous Meloni elle-même.\n\nSurtout, l'immigration continue par les voies légales : 382 000 immigrants étrangers en 2024. Face au manque de main-d'œuvre, le gouvernement Meloni a même multiplié les quotas de travailleurs étrangers, jusqu'à 500 000 sur trois ans. Le « modèle italien », c'est moins de bateaux, mais plus de travailleurs immigrés.",
 detaille="Le ministère italien de l'Intérieur compte 157 651 débarquements en 2023, année du record, sous le gouvernement Meloni, puis 66 617 en 2024 et environ autant en 2025. Cette baisse est réelle et c'est l'argument central de ses partisans.\n\nMais les arrivées par la mer ne sont qu'une partie de l'immigration. Selon l'Istat, l'Italie a enregistré 382 000 immigrations d'étrangers en 2024, et compte 5,4 millions d'étrangers, 9,2 % de sa population. Le gouvernement a adopté un décret autorisant 500 000 entrées de travailleurs étrangers pour 2026-2028, avec un quota de 164 850 pour 2026 contre 30 850 en 2019. Ces quotas sont peu pourvus, mais ils montrent que l'économie italienne a besoin de main-d'œuvre.\n\nLa mesure la plus médiatisée, les centres en Albanie, coûte plus de 153 000 € par place selon une étude universitaire, et reste quasi vide après les décisions de justice.",
 empathie="Je comprends que l'image de Lampedusa ait marqué, et que la baisse des arrivées en bateau soit rassurante. Mais il faut regarder tout le tableau : même Meloni fait venir des centaines de milliers de travailleurs étrangers.",
 legitimes=["Les débarquements ont baissé de plus de moitié entre 2023 et 2024.", "Les quotas de travail affichés sont en grande partie non pourvus."],
 contre=[
  ("Les arrivées ont baissé, c'est la preuve que ça marche.", "Elles ont baissé après un record atteint sous Meloni ; les causes ne sont pas toutes liées à sa politique, et l'immigration légale reste élevée."),
  ("Les travailleurs, ce n'est pas pareil.", "C'est justement le point : l'Italie a besoin d'immigrés pour travailler, et Meloni l'organise."),
 ],
 questions=["Sais-tu combien de travailleurs étrangers le gouvernement Meloni a autorisés pour 2026-2028 ?", "Dans quelle année l'Italie a-t-elle connu le record d'arrivées par la mer ?"],
 limites=["Les causes de la baisse (accords avec la Tunisie et la Libye) ne sont pas documentées par les sources lues.", "Les arrivées de 2022 n'ont pas été vérifiées."],
 publics={'convaincus': "Les débarquements ont baissé, c'est vrai, mais après un record atteint sous Meloni elle-même. Et son gouvernement a autorisé 500 000 travailleurs étrangers pour trois ans : l'Italie de Meloni n'a pas fermé ses portes, elle les a ouvertes à la main-d'œuvre.",
  'indecis': "La baisse des arrivées par bateau est réelle et compréhensible comme objectif. Mais elle ne représente qu'une partie de l'immigration, qui reste élevée en Italie. Le cas italien montre surtout que le besoin de main-d'œuvre s'impose même à un gouvernement d'extrême droite."},
 a_actualiser='2027-03-31', raison="Chiffres annuels du ministère italien et de l'Istat.",
))

# 4 ── Suède ──────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='suede-violence-immigration', affirmation="La Suède a sombré dans la violence à cause de l'immigration.", volet='immigration', sous_theme='Immigration et délinquance',
 mots_cles=['suede', 'suede violence', 'fusillades suede', 'gangs suede', 'stockholm', 'malmo', 'modele suedois', 'explosions suede'],
 verdict='trompeur', fiabilite='interpretation',
 resume="La Suède a connu une vague de fusillades sans équivalent en Europe, liée aux conflits entre réseaux criminels dans des quartiers défavorisés. Mais le taux global d'homicides est resté autour de 1,1 pour 100 000 habitants, puis il est tombé à 0,8 en 2025, et les fusillades ont fortement baissé depuis 2022. Les statistiques montrent une surreprésentation des personnes d'origine étrangère parmi les suspects, qui tient en grande partie à l'âge et aux conditions sociales.",
 contexte="La Suède est souvent présentée comme le contre-modèle d'un pays ouvert qui aurait « sombré ».",
 explication="Les fusillades suédoises sont surtout des règlements de comptes entre gangs liés au trafic de drogue, qui recrutent des adolescents dans des quartiers ségrégués. La violence est concentrée dans ces milieux, pas répandue dans tout le pays.",
 sources=[POL_25, POL_26, BRA_25, BRA_GUN, BRA_ORIG],
 faits=[
  fait("La Suède compte environ 4 homicides par arme à feu par million d'habitants et par an, contre environ 1,6 en moyenne européenne ; 8 sur 10 surviennent en milieu criminel.", 'bra_gun', '2021', 'Suède et Europe', "La vague de fusillades est réelle et concentrée dans les milieux criminels.", 'etabli', '4 contre 1,6'),
  fait("Le taux de violence mortelle est de 1,1 à 1,2 pour 100 000 habitants de 2016 à 2023, puis 0,9 en 2024 et 0,8 en 2025.", 'bra_25', '2016-2025', 'Suède', "Le pays n'a pas « sombré » : le taux global a baissé.", 'etabli', '0,8'),
  fait("Les fusillades sont passées de 391 en 2022 à 158 en 2025, et le premier semestre 2026 est le plus bas depuis 2017 (39 fusillades).", 'pol_26', '2022-2026', 'Suède', "Les fusillades ont fortement reculé.", 'etabli', '391 à 158'),
  fait("Les explosions sont passées de 136 en 2024 à 189 en 2025, une violence d'intimidation et d'extorsion en hausse.", 'pol_25', '2024-2025', 'Suède', "Toutes les formes de violence ne baissent pas.", 'etabli', '189'),
  fait("Le risque d'être enregistré comme suspect est plus élevé chez les personnes nées à l'étranger, et plus encore chez celles nées en Suède de deux parents immigrés ; une grande partie de l'écart tient à la structure par âge.", 'bra_orig', '2007-2018', 'Suède', "La surreprésentation existe, mais l'étude n'en explique pas les causes.", 'etabli'),
 ],
 court="Trompeur : la Suède a connu une vague de fusillades entre gangs unique en Europe. Mais son taux d'homicides est tombé à 0,8 pour 100 000 en 2025 et les fusillades ont chuté depuis 2022. La violence est concentrée dans des milieux criminels de quartiers ségrégués.",
 moyen="La hausse des fusillades en Suède est réelle : environ 4 homicides par arme à feu par million d'habitants, contre 1,6 en moyenne en Europe. Elle est liée aux réseaux criminels des quartiers défavorisés.\n\nMais le pays n'a pas « sombré » : le taux global d'homicides est resté autour de 1,1 pour 100 000 et il est tombé à 0,8 en 2025. Les fusillades ont baissé de 391 en 2022 à 158 en 2025, grâce à des centaines d'arrestations.",
 detaille="L'organisme public suédois de prévention du crime constate une hausse des homicides par arme à feu sans équivalent dans 22 pays européens, presque uniquement liée aux règlements de comptes en milieu criminel. Ces violences touchent surtout des jeunes hommes, dans des quartiers défavorisés.\n\nLes statistiques suédoises montrent aussi une surreprésentation des personnes nées à l'étranger, et plus encore de leurs enfants nés en Suède, parmi les suspects. Il ne faut pas le nier. Mais le même organisme précise qu'une grande partie de l'écart tient à l'âge et que son étude ne dit rien des causes. Ce qui est en jeu, c'est la ségrégation sociale, le marché de la drogue et le recrutement de mineurs par les gangs.\n\nEnfin, la tendance s'inverse : le taux de violence mortelle est tombé de 1,2 pour 100 000 en 2023 à 0,8 en 2025, et les fusillades ont fortement reculé, même si les explosions augmentent.",
 empathie="Les images de fusillades en Suède sont effrayantes, et c'est normal de s'inquiéter. Mais regarde aussi ce qui s'est passé ensuite : en ciblant les gangs, la Suède a fait chuter les fusillades.",
 legitimes=["La vague de fusillades de 2013-2023 est unique en Europe.", "Les personnes d'origine étrangère sont surreprésentées parmi les suspects.", "Les explosions augmentaient encore en 2025."],
 contre=[
  ("Les gangs sont composés d'immigrés.", "Les suspects sont souvent des jeunes de quartiers ségrégués, beaucoup nés en Suède ; l'organisme public ne lie pas cette violence à l'immigration en tant que telle."),
  ("La Suède est devenue le pays le plus dangereux d'Europe.", "Son taux global d'homicides, 0,8 pour 100 000 en 2025, est à son plus bas depuis dix ans."),
 ],
 questions=["Sais-tu comment ont évolué les fusillades en Suède depuis 2022 ?", "Qu'est-ce qui a fait baisser la violence : moins d'immigrés, ou la lutte contre les gangs ?"],
 limites=["L'effet des revenus, de l'éducation et du quartier sur l'écart entre groupes n'a pas été chiffré dans les sources lues.", "La comparaison européenne vient de l'organisme suédois, pas d'Eurostat."],
 publics={'convaincus': "La vague de fusillades est réelle, et les jeunes d'origine immigrée y sont surreprésentés. Mais la Suède ne l'a pas fait reculer en expulsant : elle a ciblé les gangs, et les fusillades sont passées de 391 en 2022 à 158 en 2025. Le problème, c'est le crime organisé dans des quartiers abandonnés.",
  'indecis': "La Suède a connu une vraie vague de violences entre gangs, concentrée dans certains quartiers. Le taux global d'homicides est pourtant resté bas et il baisse fortement depuis 2023. C'est un exemple des dégâts de la ségrégation et du trafic de drogue, et de ce qu'une action ciblée peut obtenir."},
 a_actualiser='2027-06-30', raison="Statistiques annuelles de la police suédoise et de Brå.",
))

# 5 ── Droit de vote des étrangers ─────────────────────────────────────────────
FICHES.append(fiche(
 id='droit-vote-etrangers', affirmation="La gauche veut donner le droit de vote aux étrangers.", volet='politique', sous_theme='Programmes électoraux',
 mots_cles=['droit de vote des etrangers', 'vote des etrangers', 'etrangers voter', 'vote aux municipales', 'droit de vote municipales', 'eligibilite des etrangers', 'citoyennete de residence'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="Oui, mais seulement aux élections municipales, pour les étrangers non européens résidant en France, sans pouvoir être maire ou adjoint ni voter aux sénatoriales. C'est une revendication de la gauche depuis 1981, votée par l'Assemblée en 2000 et par le Sénat en 2011, jamais appliquée. Les citoyens de l'Union européenne votent déjà aux municipales depuis 2001.",
 contexte="La mesure revient régulièrement dans le débat ; une proposition de loi écologiste a été adoptée en commission en février 2026.",
 explication="Il s'agirait de modifier la Constitution. Les citoyens européens votent déjà aux municipales et aux européennes ; la proposition étendrait ce droit aux autres étrangers résidents. Une telle révision exige un référendum ou une majorité des trois cinquièmes du Congrès.",
 sources=[SEN_VOTE, AN_VOTE, LCP_VOTE, LCP_NICHE],
 faits=[
  fait("Le texte adopté par le Sénat en 2011 ouvre le vote et l'éligibilité aux municipales aux étrangers non européens résidant en France, sans fonctions de maire ou d'adjoint ni participation à l'élection des sénateurs.", 'sen_vote', '2011', 'France', "La proposition est limitée aux municipales.", 'etabli'),
  fait("La proposition a été adoptée par l'Assemblée le 3 mai 2000 et par le Sénat le 8 décembre 2011 ; elle reste en attente de deuxième lecture.", 'an_vote', '2000-2026', 'France', "Elle n'a jamais été appliquée.", 'etabli'),
  fait("Les citoyens de l'Union européenne votent aux municipales en France depuis 2001.", 'an_vote', '2001', 'France', "Des étrangers votent déjà aux municipales.", 'etabli'),
  fait("En février 2026, écologistes, insoumis, socialistes et communistes ont adopté le texte en commission ; le socle gouvernemental, le RN, l'UDR et LIOT s'y opposent.", 'lcp_vote', '2026', 'France', "C'est bien une position de toute la gauche.", 'etabli'),
  fait("La droite et l'extrême droite ont déposé 501 amendements, et le texte n'a a priori pas pu être examiné en séance.", 'lcp_niche', '2026', 'France', "Le blocage parlementaire continue.", 'etabli', '501'),
 ],
 court="Plutôt vrai, mais limité : la gauche propose le droit de vote aux municipales pour les étrangers non européens résidents, sans pouvoir être maire. C'est déjà le cas pour les Européens depuis 2001. La mesure n'a jamais été appliquée.",
 moyen="La gauche défend depuis 1981 le droit de vote des étrangers non européens aux élections municipales. L'Assemblée l'a voté en 2000, le Sénat en 2011, mais la réforme constitutionnelle n'est jamais allée au bout.\n\nIl ne s'agit pas de voter à la présidentielle ou aux législatives : seulement aux municipales, sans pouvoir être maire ou adjoint. Les citoyens européens ont déjà ce droit depuis 2001. L'idée : ceux qui vivent, travaillent et paient des impôts dans une commune participent à la vie locale.",
 detaille="La proposition de loi constitutionnelle, adoptée à l'Assemblée en 2000 puis au Sénat en 2011, créerait un article 72-5 de la Constitution. Elle ouvrirait le vote et l'éligibilité aux municipales aux étrangers non européens résidant en France. Ils ne pourraient ni être maire ou adjoint, ni participer à l'élection des sénateurs.\n\nC'est une promesse de François Mitterrand en 1981 et de François Hollande en 2012, jamais tenue. En février 2026, toute la gauche a adopté le texte en commission ; la droite et l'extrême droite ont déposé 501 amendements et le texte n'a pas été examiné. Une adoption définitive déclencherait un référendum.\n\nDepuis 2001, les citoyens de l'Union européenne votent déjà aux municipales. Le débat porte donc sur le lien entre citoyenneté et nationalité : pour la droite, voter suppose d'être français ; pour la gauche, la démocratie locale doit associer tous les résidents.",
 empathie="Je comprends que le droit de vote paraisse lié à la nationalité. Mais il ne s'agit que des municipales, et un Allemand ou un Portugais qui vit dans ta commune vote déjà depuis 2001.",
 legitimes=["C'est bien une revendication de toute la gauche depuis 1981.", "La droite considère que le droit de vote doit rester lié à la nationalité, ce qui est un choix politique défendable."],
 contre=[
  ("Ils voteront pour les présidentielles.", "Non : la proposition ne concerne que les municipales, sans pouvoir être maire ni adjoint."),
  ("Qu'ils demandent la nationalité.", "C'est une option ; la proposition repose sur l'idée que la vie locale concerne tous ceux qui y résident durablement."),
 ],
 questions=["Savais-tu que les citoyens européens votent déjà aux municipales depuis 2001 ?", "Pourquoi un étranger qui vit dans ta commune depuis vingt ans n'aurait-il pas son mot à dire sur l'école ou les transports ?"],
 limites=["Le sort exact du texte le 12 février 2026 n'a pas été confirmé par une source lue.", "La décision du Conseil constitutionnel de 1992 n'a pas été lue directement."],
 publics={'convaincus': "Il ne s'agit que des municipales, sans pouvoir être maire, et les Européens votent déjà depuis 2001. Un étranger qui vit, travaille et paie ses impôts dans ta commune depuis des années n'aurait pas son mot à dire sur la cantine ou la voirie ?",
  'indecis': "C'est vrai, la gauche le propose depuis 1981, mais limité aux municipales et jamais appliqué. Le vrai débat est de savoir si la démocratie locale doit associer tous les résidents ou seulement les nationaux. Une réforme passerait de toute façon par un référendum."},
 a_actualiser='2027-06-30', raison="Suite de la navette parlementaire et programmes de 2027.",
))

# 6 ── Racisme « anti-blanc » ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='racisme-anti-blanc', affirmation="Le racisme anti-blanc est devenu le racisme le plus répandu en France.", volet='immigration', sous_theme='Racisme',
 mots_cles=['racisme anti blanc', 'racisme anti blancs', 'racisme contre les blancs', 'francais de souche discrimines', 'haine des blancs', 'racisme inverse', 'blancs victimes'],
 verdict='contredit', fiabilite='etabli',
 resume="Les grandes enquêtes de la statistique publique montrent l'inverse : les immigrés et descendants d'immigrés déclarent environ deux fois plus de propos racistes, et bien plus de discriminations liées à l'origine, que la population sans ascendance migratoire. Des personnes de la population majoritaire subissent aussi des insultes racistes (16 % au cours de leur vie en 2008), mais celles-ci se traduisent rarement en discriminations.",
 contexte="L'expression est utilisée pour renverser le débat sur les discriminations ; elle s'appuie sur des expériences réelles d'insultes.",
 explication="Les enquêtes Trajectoires et Origines de l'Insee et de l'Ined interrogent des milliers de personnes sur les traitements inégalitaires et les propos racistes qu'elles ont subis. Elles distinguent les insultes, que tout le monde peut subir, et les discriminations (emploi, logement), qui dépendent d'un rapport de pouvoir.",
 sources=[INSEE_DISC, INED_RAC, CNCDH_25],
 faits=[
  fait("En 2008, 36 % des descendants d'immigrés et 32 % des immigrés déclarent avoir subi des insultes ou propos racistes au cours de leur vie, contre 16 % de la population majoritaire.", 'ined_rac', '2008', 'France, 18-50 ans', "Le racisme subi est deux fois plus fréquent chez les immigrés et leurs enfants.", 'etabli', '36 % contre 16 %'),
  fait("En 2008, les discriminations déclarées sur cinq ans touchent 31 % des descendants de deux parents immigrés et 10 % de la population majoritaire ; pour cette dernière, le racisme subi n'est pas lié à des discriminations en raison de l'origine.", 'ined_rac', '2008', 'France', "Les insultes ne se traduisent pas en discriminations pour la population majoritaire.", 'etabli'),
  fait("En 2019-2020, 22 % des immigrés et 20 % des descendants d'immigrés déclarent des discriminations liées à l'origine, la nationalité ou la couleur de peau, contre 8 % de l'ensemble de la population.", 'insee_disc', '2019-2020', 'France métropolitaine, 18-49 ans', "Les discriminations liées à l'origine visent surtout les immigrés et leurs enfants.", 'etabli', '22 % et 20 %'),
  fait("Les discriminations déclarées par les personnes sans ascendance migratoire, tous motifs confondus, passent de 10 % à 15 % entre 2008 et 2019-2020, hausse portée surtout par le motif sexiste.", 'insee_disc', '2008-2020', 'France métropolitaine', "La hausse chez la population majoritaire concerne surtout le sexisme.", 'etabli', '15 %'),
  fait("Environ 1,2 million de personnes s'estiment victimes chaque année d'une atteinte raciste, antisémite ou xénophobe, et 97 % ne portent pas plainte.", 'cncdh_25', '2023', 'France', "Le racisme reste massif et peu déclaré.", 'estimation', '1,2 million'),
 ],
 court="Faux : selon l'Insee et l'Ined, les immigrés et leurs enfants déclarent deux fois plus de propos racistes que la population majoritaire, et beaucoup plus de discriminations. Des insultes visent aussi des Blancs, mais elles se traduisent rarement en discriminations.",
 moyen="Les enquêtes de la statistique publique sont nettes : en 2008, 36 % des descendants d'immigrés déclaraient avoir subi des propos racistes, contre 16 % de la population majoritaire. En 2019-2020, plus d'un immigré sur cinq déclarait des discriminations liées à son origine.\n\nLes insultes visant des personnes blanches existent, et elles sont blessantes. Mais selon l'Ined, elles ne s'accompagnent pas de discriminations à l'embauche ou au logement, contrairement à ce que vivent les immigrés et leurs enfants.",
 detaille="L'enquête Trajectoires et Origines de 2008 montre que 36 % des descendants d'immigrés et 32 % des immigrés ont subi des insultes ou propos racistes au cours de leur vie, contre 16 % de la population majoritaire. Ce dernier chiffre n'est pas nul : le racisme visant des personnes blanches existe.\n\nMais la différence est dans les conséquences. Les discriminations déclarées sur cinq ans touchent 31 % des descendants de deux parents immigrés et 10 % de la population majoritaire, et pour celle-ci, selon l'Ined, le racisme subi n'est pas lié à des discriminations en raison de l'origine. En 2019-2020, 22 % des immigrés et 20 % des descendants déclarent des discriminations liées à l'origine ou à la couleur de peau, environ un tiers pour les personnes originaires d'Afrique subsaharienne.\n\nLes discriminations déclarées par la population sans ascendance migratoire progressent (de 10 % à 15 %), mais surtout à cause du sexisme. Le racisme, lui, reste massif et peu dénoncé : 97 % des victimes ne portent pas plainte.",
 empathie="Si tu as été insulté à cause de ta couleur de peau, c'est inacceptable, et tu as raison de le dire. Les enquêtes montrent simplement que ce racisme est moins fréquent et qu'il ferme moins de portes que celui que subissent les immigrés et leurs enfants.",
 legitimes=["16 % de la population majoritaire déclarait en 2008 avoir subi des propos racistes.", "Les discriminations déclarées par les personnes sans ascendance migratoire augmentent."],
 contre=[
  ("Les Blancs n'osent pas le dire.", "Les enquêtes sont anonymes et posent les mêmes questions à tous ; la population majoritaire déclare deux fois moins de propos racistes."),
  ("Les enquêtes ne s'intéressent pas aux Blancs.", "Elles interrogent toute la population, y compris les personnes sans ascendance migratoire, dont 16 % déclaraient en 2008 avoir subi des propos racistes."),
 ],
 questions=["Sais-tu ce que mesurent les enquêtes de l'Insee et de l'Ined sur le racisme ?", "Une insulte et un refus d'embauche, est-ce la même chose ?"],
 limites=["Le détail du motif « origine » pour la population majoritaire en 2019-2020 n'a pas été lu.", "Une partie des données date de 2008."],
 publics={'convaincus': "Une insulte raciste contre un Blanc est inacceptable, et elle existe. Mais les enquêtes anonymes de l'Insee et de l'Ined montrent que les immigrés et leurs enfants en subissent deux fois plus, et surtout des discriminations au travail et au logement. Combattre tous les racismes, c'est commencer par regarder les chiffres.",
  'indecis': "Le racisme visant des personnes blanches existe, mais les enquêtes publiques montrent qu'il est moins fréquent et qu'il ne se traduit pas en discriminations. Ce sont surtout les immigrés et leurs enfants qui se voient refuser un emploi ou un logement. On peut refuser toutes les formes de racisme sans les mettre sur le même plan."},
 a_actualiser='2027-06-30', raison="Nouvelles exploitations de l'enquête TeO2 et rapport annuel de la CNCDH.",
))

# 7 ── « Francocide » ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='francocide-terme', affirmation="Les « francocides » se multiplient : on tue des Français parce qu'ils sont français.", volet='securite', sous_theme='Homicides',
 mots_cles=['francocide', 'francocides', 'tues parce que francais', 'tuer des francais', 'meurtres de francais', 'blancs tues', 'zemmour francocide'],
 verdict='inverifiable', fiabilite='interpretation',
 resume="Le mot « francocide » a été forgé par Éric Zemmour en 2022 pour désigner « un crime contre un Français par un étranger ». Il ne correspond à aucune catégorie statistique ni juridique : rien ne permet de mesurer une « multiplication ». Le terme relie des faits divers différents à la théorie complotiste du « grand remplacement ».",
 contexte="Le terme circule après chaque meurtre très médiatisé ; il est repris par une partie de l'extrême droite.",
 explication="Les statistiques de la police comptent les homicides, mais aucune ne classe les crimes selon la nationalité de l'auteur et de la victime ou selon un mobile « anti-français ». Les crimes visant une personne en raison de ce qu'elle est relèvent de qualifications spécifiques, qui ne dépendent pas de l'origine de l'auteur.",
 sources=[AFP_FRANCO, ULG_FRANCO, BDT_SSMSI],
 faits=[
  fait("Le terme a été forgé par Éric Zemmour lors d'un discours en septembre 2022, sur le modèle de « génocide » ou « féminicide ».", 'afp_franco', '2022', 'France', "C'est un mot militant récent.", 'etabli'),
  fait("Zemmour le définit comme « un crime contre un Français par un étranger » ; un chercheur le rattache à la théorie du « grand remplacement ».", 'ulg_franco', '2022-2024', 'France', "Le mot désigne la nationalité de l'auteur, pas un mobile prouvé.", 'etabli'),
  fait("L'article de l'AFP sur l'apparition du terme ne cite aucune statistique d'homicide : ses seuls chiffres mesurent la diffusion du mot sur les réseaux sociaux.", 'afp_franco', '2023', 'France', "Aucune donnée n'appuie une « multiplication ».", 'etabli'),
  fait("D'après le SSMSI, sur douze mois glissants au 30 juin 2024, les homicides baissent de 8 % et les tentatives d'homicide augmentent de 11 %.", 'bdt_ssmsi', '2023-2024', 'France', "Les statistiques ne disent rien du mobile ; les tentatives sont en hausse.", 'etabli', '-8 % / +11 %'),
 ],
 court="Invérifiable et trompeur : le « francocide » est un mot inventé par Éric Zemmour en 2022, sans aucune définition statistique ni juridique. Personne ne peut mesurer sa « multiplication ». Il transforme des drames en preuve d'une guerre ethnique.",
 moyen="Le mot a été créé en 2022 par Éric Zemmour pour désigner « un crime contre un Français par un étranger ». Aucune statistique ne compte ces crimes, et ceux qui utilisent le mot n'apportent pas de données.\n\nChaque meurtre est un drame, et la justice doit punir. Mais regrouper des faits divers différents sous un même mot, c'est suggérer une guerre contre les Français, ce que les chiffres ne montrent pas.",
 detaille="Selon l'AFP, le mot « francocide » apparaît dans un discours d'Éric Zemmour en septembre 2022, sur le modèle du mot « féminicide ». Il le définit comme « un crime contre un Français par un étranger ». Des chercheurs le rattachent à la théorie du « grand remplacement », qui décrit les Français comme victimes d'une population étrangère.\n\nLe problème est double. D'abord, aucune catégorie statistique ne permet de compter ces crimes : la police compte les homicides, pas la nationalité des auteurs et des victimes croisée avec un mobile. Ensuite, la définition repose sur l'origine de l'auteur, pas sur son mobile : un crime crapuleux devient ainsi un crime « contre les Français ».\n\nLes statistiques disponibles montrent des évolutions contrastées : sur douze mois à juin 2024, les homicides baissent de 8 % et les tentatives augmentent de 11 %. Ces chiffres méritent attention, mais ne disent rien d'un mobile anti-français.",
 empathie="Je comprends la colère après un meurtre atroce, surtout quand on a l'impression que la victime a été visée pour ce qu'elle est. Mais le mot « francocide » ne repose sur aucun chiffre ; il fabrique une guerre à partir de drames différents.",
 legitimes=["Les tentatives d'homicide ont augmenté sur un an à mi-2024.", "Des crimes racistes visant des personnes blanches peuvent exister et doivent être punis comme tels."],
 contre=[
  ("Les médias cachent ces crimes.", "Les meurtres invoqués ont été très médiatisés ; ce qui manque, ce sont des données montrant une tendance."),
  ("On a bien inventé « féminicide ».", "Le féminicide désigne un mobile (tuer une femme parce qu'elle est une femme), documenté par des statistiques annuelles ; « francocide » désigne seulement l'origine de l'auteur."),
 ],
 questions=["Sais-tu qui a inventé le mot et sur quelles données il s'appuie ?", "Un crime commis par un étranger est-il forcément commis contre « les Français » ?"],
 limites=["Les statistiques officielles du SSMSI n'ont été lues qu'à travers un compte rendu.", "Aucun fact-check français sur le terme n'a pu être ouvert."],
 publics={'convaincus': "Chaque meurtre mérite justice. Mais le mot « francocide » a été inventé en 2022 sans aucune statistique derrière. Il range sous un même nom des drames différents pour faire croire à une guerre contre les Français.",
  'indecis': "Ce mot ne correspond à aucune catégorie statistique ni juridique : personne ne peut dire s'il y en a plus ou moins. Les homicides sont comptés par la police et ils ne montrent pas de vague liée à un mobile « anti-français ». Méfie-toi des mots qui transforment des faits divers en guerre de civilisation."},
 a_actualiser='2027-06-30', raison="Bilans annuels du SSMSI sur les homicides.",
))

# 8 ── Mineurs délinquants et excuse de minorité ──────────────────────────────
FICHES.append(fiche(
 id='excuse-de-minorite', affirmation="Les mineurs délinquants sont de plus en plus jeunes et violents, il faut supprimer l'excuse de minorité.", volet='securite', sous_theme='Justice pénale',
 mots_cles=['excuse de minorite', 'mineurs delinquants', 'delinquance des mineurs', 'mineurs violents', 'de plus en plus jeunes', 'justice des mineurs', 'loi attal', 'ordonnance de 1945'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Les données ne montrent pas de rajeunissement établi : la part des mineurs parmi les personnes mises en cause est stable autour de 18 % depuis 2002. Certaines infractions augmentent (violences sexuelles, trafic de stupéfiants), d'autres baissent (vols). Et l'atténuation de peine selon l'âge est un principe constitutionnel : en 2025, le Conseil constitutionnel a censuré la loi qui voulait l'inverser.",
 contexte="Le sujet revient après chaque fait divers impliquant un mineur ; une loi de 2025 a tenté de durcir la justice des mineurs.",
 explication="L'« excuse de minorité » réduit la peine encourue par un mineur ; pour les plus de 16 ans, le juge peut l'écarter par une décision motivée. Elle repose sur l'idée qu'un adolescent est moins responsable qu'un adulte et doit pouvoir être rééduqué.",
 sources=[SEN_MIN, PS_ATTAL, LCP_ATTAL, JUST_205],
 faits=[
  fait("Le nombre de mineurs mis en cause n'augmente que de 6 % entre 2002 et 2019, et leur part parmi les mis en cause reste proche de 18 % depuis 2002.", 'sen_min', '2002-2019', 'France', "Pas d'explosion de la délinquance des mineurs.", 'estimation', '18 %'),
  fait("La répartition par âge des mineurs mis en cause est globalement stable entre 2016 et 2019 ; les sénateurs jugent impossible de conclure à un rajeunissement.", 'sen_min', '2016-2019', 'France', "Le « de plus en plus jeunes » n'est pas démontré.", 'interpretation'),
  fait("Entre 2016 et 2021, les vols sans violence commis par des mineurs baissent de 28,4 % et les vols violents de 14,9 %, mais les mineurs mis en cause pour trafic de stupéfiants augmentent de 35 %.", 'sen_min', '2016-2021', 'France', "Les évolutions sont contrastées selon les infractions.", 'estimation', '+35 %'),
  fait("Les mises en cause de mineurs pour viol sur mineur augmentent de 109 % entre 2020 et 2024, ce que l'étude explique en partie par le confinement et la libération de la parole.", 'just_205', '2020-2024', 'France', "Certaines violences progressent nettement.", 'etabli', '+109 %'),
  fait("En juin 2025, le Conseil constitutionnel a censuré l'inversion de l'excuse de minorité au nom du « principe de l'atténuation de la responsabilité pénale des mineurs en fonction de l'âge ».", 'ps_attal', '2025', 'France', "On ne peut pas supprimer ce principe par une simple loi.", 'etabli'),
 ],
 court="Trompeur : la part des mineurs parmi les délinquants est stable autour de 18 % depuis 2002, et aucun rajeunissement n'est démontré. Certaines violences augmentent. Mais l'atténuation de peine selon l'âge est un principe constitutionnel, rappelé par le Conseil constitutionnel en 2025.",
 moyen="Les chiffres ne montrent pas d'explosion : le nombre de mineurs mis en cause n'a augmenté que de 6 % entre 2002 et 2019, et leur part reste autour de 18 %. Les vols baissent ; le trafic de stupéfiants et les violences sexuelles augmentent.\n\nSupprimer l'excuse de minorité n'est pas possible par une simple loi : en 2025, le Conseil constitutionnel a censuré la loi qui voulait l'inverser. Les juges peuvent déjà l'écarter pour les plus de 16 ans. Le vrai manque, ce sont les moyens éducatifs pour suivre ces jeunes.",
 detaille="Le Sénat a examiné en 2022 les chiffres de la délinquance des mineurs. Le nombre de mineurs mis en cause a augmenté de 6 % entre 2002 et 2019, et leur part parmi les mis en cause est restée proche de 18 %. La répartition par âge est globalement stable : les sénateurs n'ont pas pu conclure à un rajeunissement, même si le terrain signale des guetteurs de 13 ans.\n\nLes évolutions diffèrent selon les infractions : baisse des vols, hausse du trafic de stupéfiants (+35 % entre 2016 et 2021) et des violences sexuelles, dont les mises en cause ont doublé entre 2020 et 2024, en partie du fait de la libération de la parole. Ces hausses sont réelles et méritent une réponse.\n\nL'excuse de minorité réduit la peine encourue ; le juge peut déjà l'écarter, en le motivant, pour les 16-18 ans. En 2025, une loi voulait en faire l'exception pour les récidivistes : le Conseil constitutionnel l'a censurée, rappelant que l'atténuation selon l'âge et le « relèvement éducatif et moral des mineurs » sont des exigences constitutionnelles.",
 empathie="Je comprends le choc quand un adolescent commet un acte très violent, et l'envie qu'il soit puni comme un adulte. Mais les chiffres ne montrent pas une vague de délinquance juvénile, et punir plus durement un mineur ne dit pas comment l'empêcher de recommencer.",
 legitimes=["Le trafic de stupéfiants et les violences sexuelles impliquant des mineurs augmentent.", "Des réseaux recrutent des adolescents très jeunes."],
 contre=[
  ("Ils savent qu'ils ne risquent rien.", "Les mineurs sont jugés et condamnés ; le juge peut écarter l'atténuation pour les plus de 16 ans."),
  ("Il suffit de changer la loi.", "Le Conseil constitutionnel a jugé en 2025 que l'atténuation selon l'âge est un principe constitutionnel."),
 ],
 questions=["Sais-tu que la part des mineurs parmi les délinquants est stable depuis vingt ans ?", "Qu'est-ce qui empêche le mieux un adolescent de récidiver : une peine plus longue, ou un suivi éducatif ?"],
 limites=["Les séries du Sénat s'arrêtent en 2021 et ne sont pas validées par le SSMSI.", "La décision du Conseil constitutionnel n'a été lue qu'à travers deux médias parlementaires."],
 publics={'convaincus': "La part des mineurs parmi les délinquants n'a pas bougé depuis 2002, autour de 18 %. Le juge peut déjà écarter l'excuse de minorité pour les plus de 16 ans, et le Conseil constitutionnel a rappelé en 2025 qu'on ne peut pas la supprimer. Ce qui manque, ce sont des éducateurs et des places de suivi.",
  'indecis': "Certaines violences impliquant des mineurs augmentent, notamment le trafic de drogue, et c'est inquiétant. Mais il n'y a pas d'explosion globale ni de rajeunissement démontré. Le droit permet déjà des peines lourdes pour les plus âgés ; l'enjeu est d'éviter la récidive."},
 a_actualiser='2027-06-30', raison="Statistiques annuelles de la Justice et du SSMSI.",
))

# 9 ── 80 km/h ──────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='limitation-80-kmh', affirmation="La limitation à 80 km/h n'a servi à rien.", volet='securite', sous_theme='Prévention et politiques publiques',
 mots_cles=['80 km h', '80 kmh', 'quatre vingt km h', 'limitation de vitesse', 'retour a 90', '90 km h', 'routes departementales', 'securite routiere'],
 verdict='contredit', fiabilite='etabli',
 resume="L'évaluation officielle du Cerema estime à 349 le nombre de vies épargnées pendant les 20 premiers mois de la mesure. Le nombre d'accidents n'a pas baissé, mais leur gravité oui. Sur les routes repassées à 90 km/h, la mortalité a moins baissé que sur celles restées à 80 km/h.",
 contexte="La mesure de 2018 a été très impopulaire, notamment dans les zones rurales ; depuis 2020, de nombreux départements sont revenus à 90 km/h.",
 explication="À vitesse plus faible, la distance de freinage et la violence des chocs diminuent. Même si le nombre d'accidents ne change pas, ils sont moins souvent mortels.",
 sources=[ONISR_80, CEREMA_80, ONISR_90],
 faits=[
  fait("L'évaluation officielle conclut à « 349 vies épargnées les 20 premiers mois de la mesure », par rapport à la moyenne 2013-2017.", 'onisr_80', '2018-2020', 'France, routes hors agglomération', "La mesure a sauvé des vies.", 'estimation', '349 vies'),
  fait("La baisse de la mortalité est d'environ 12 % par rapport au reste du réseau, et la vitesse moyenne baisse de 3,3 km/h.", 'cerema_80', '2018-2019', 'France', "L'effet est mesuré par comparaison avec les autres routes.", 'estimation', '-12 %'),
  fait("Le nombre d'accidents ne change pas, mais leur gravité baisse : de 15,2 à 13,7 tués pour 100 accidents.", 'onisr_80', '2018-2020', 'France', "La mesure réduit la gravité, pas le nombre d'accidents.", 'etabli', '15,2 à 13,7'),
  fait("Entre 2013-2017 et 2021, la mortalité baisse de 21,3 % sur les routes restées à 80 km/h, contre 16,0 % sur celles repassées à 90 km/h.", 'onisr_90', '2013-2021', 'France', "Le retour à 90 km/h coûte des vies.", 'estimation', '21,3 % contre 16,0 %'),
  fait("Le temps de trajet augmente d'environ une seconde par kilomètre.", 'cerema_80', '2019', 'France', "Le coût en temps est faible.", 'estimation', '1 s/km'),
 ],
 court="Faux : l'évaluation officielle estime que le 80 km/h a épargné 349 vies en 20 mois. Les routes repassées à 90 km/h ont vu leur mortalité baisser moins vite. Le temps perdu est d'environ une seconde par kilomètre.",
 moyen="Le Cerema a comparé les routes passées à 80 km/h au reste du réseau : 349 vies épargnées sur les 20 premiers mois. Il y a autant d'accidents, mais ils tuent moins.\n\nDepuis, une partie des départements est revenue à 90 km/h. Sur ces routes, la mortalité a moins baissé que sur celles restées à 80 km/h. On peut critiquer la manière dont la mesure a été imposée, mais pas dire qu'elle n'a servi à rien.",
 detaille="L'évaluation menée par le Cerema pour la Sécurité routière conclut à 349 vies épargnées entre juillet 2018 et février 2020, par rapport à la moyenne 2013-2017. La mortalité y a baissé d'environ 12 % de plus que sur le reste du réseau, et la vitesse moyenne de 3,3 km/h, mesurée sur 143 millions de passages.\n\nLe nombre d'accidents n'a pas baissé : c'est leur gravité qui diminue (13,7 tués pour 100 accidents contre 15,2). Le temps de trajet supplémentaire est d'environ une seconde par kilomètre, et le bilan socio-économique est estimé positif d'environ 700 millions d'euros par an.\n\nAprès 2020, 44 départements ont relevé environ 51 000 km de routes à 90 km/h. Sur ces routes, la mortalité a baissé de 16 % entre 2013-2017 et 2021, contre 21,3 % sur celles restées à 80 km/h. L'ONISR estime entre 42 et 74 le nombre de morts supplémentaires en 2021.",
 empathie="Je comprends que la mesure ait été vécue comme imposée d'en haut, surtout quand on vit à la campagne et qu'on fait beaucoup de route. Mais les évaluations sont claires : elle a sauvé des centaines de vies, pour une seconde de plus par kilomètre.",
 legitimes=["Le nombre d'accidents n'a pas baissé.", "La mesure a été imposée sans concertation et mal vécue dans les zones rurales.", "Les méthodes d'évaluation ont des limites reconnues par les auteurs."],
 contre=[
  ("La mortalité baisse partout, ce n'est pas grâce au 80.", "L'évaluation compare précisément les routes à 80 avec le reste du réseau : la baisse y est plus forte."),
  ("C'est juste pour les radars.", "Le temps perdu est d'une seconde par kilomètre, et la mortalité a moins baissé là où on est revenu à 90."),
 ],
 questions=["Combien de temps perds-tu vraiment sur un trajet de 30 km à 80 au lieu de 90 ?", "Sais-tu ce qui s'est passé sur les routes revenues à 90 km/h ?"],
 limites=["Les évaluations datent de 2020 à 2022.", "Les auteurs reconnaissent des limites de méthode (périmètre, groupes de comparaison, crise sanitaire)."],
 publics={'convaincus': "On peut trouver que la mesure a été imposée d'en haut, et c'est un vrai reproche. Mais les comptages sont là : 349 vies épargnées en 20 mois, et une mortalité qui baisse moins vite là où les départements sont revenus à 90. Tout ça pour une seconde par kilomètre.",
  'indecis': "La mesure a été mal vécue, surtout en zone rurale. Les évaluations officielles montrent pourtant moins de morts sur les routes à 80 km/h, sans baisse du nombre d'accidents. Le débat porte sur la méthode, pas sur l'efficacité."},
 a_actualiser='2027-06-30', raison="Nouvelles évaluations de l'ONISR.",
))

# 10 ── 49.3 ──────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='article-49-3-gauche', affirmation="La gauche dénonce le 49.3, mais c'est elle qui l'a le plus utilisé.", volet='politique', sous_theme='Institutions françaises',
 mots_cles=['49 3', '49.3', 'quarante neuf trois', 'article 49', 'rocard 49 3', 'borne 49 3', 'passage en force'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="En partie vrai : le record individuel revient au socialiste Michel Rocard (28 fois) et les gouvernements socialistes de 1988-1993 l'ont utilisé 39 fois, faute de majorité absolue. Mais la droite l'a aussi beaucoup utilisé, et la législature 2022-2024 de la majorité présidentielle en compte 23. Aujourd'hui, la gauche du NFP propose de l'abroger.",
 contexte="L'argument sert à renvoyer la gauche à ses contradictions quand elle dénonce l'usage du 49.3.",
 explication="L'article 49 alinéa 3 permet au gouvernement de faire adopter un texte sans vote, sauf si une motion de censure est votée. Depuis 2008, il est limité à un texte par session, hors budgets.",
 sources=[PS_493, AN_493, TLN_493, NFP_PROG],
 faits=[
  fait("Michel Rocard a engagé sa responsabilité à 28 reprises, record en la matière ; suivent Édith Cresson (8) et Manuel Valls (6).", 'ps_493', '1988-2016', 'France', "Le record individuel est socialiste.", 'etabli', '28'),
  fait("L'Assemblée compte 39 usages du 49.3 sous la législature 1988-1993, celle des gouvernements socialistes, et 23 sous celle de 2022-2024.", 'an_493', '1988-2024', 'France', "Les deux périodes de majorité relative concentrent les usages.", 'etabli', '39 et 23'),
  fait("Depuis 2008, le 49.3 est limité à un texte par session hors lois de finances et de financement de la sécurité sociale.", 'an_493', '2008', 'France', "La règle a changé depuis Rocard.", 'etabli'),
  fait("Un universitaire compte 100 utilisations du 49.3 depuis 1958, sur 55 textes.", 'tln_493', '1958-2023', 'France', "Tous les camps l'ont utilisé.", 'estimation', '100'),
  fait("Le programme du Nouveau Front populaire de 2024 propose d'« Abroger le 49.3 ».", 'nfp_prog', '2024', 'France', "La gauche actuelle veut le supprimer.", 'etabli'),
 ],
 court="En partie vrai : le socialiste Michel Rocard détient le record (28 fois), faute de majorité absolue. Mais tous les camps l'ont utilisé, la majorité présidentielle 23 fois entre 2022 et 2024. Et la gauche propose aujourd'hui de l'abroger.",
 moyen="C'est exact pour le passé : Michel Rocard, Premier ministre socialiste sans majorité absolue, l'a utilisé 28 fois, et la législature 1988-1993 compte 39 usages.\n\nMais le 49.3 a été utilisé par la droite comme par la majorité présidentielle (23 fois entre 2022 et 2024). La gauche d'aujourd'hui en tire la leçon : le programme du NFP propose de l'abroger. On peut reprocher une incohérence passée, mais pas une hypocrisie actuelle.",
 detaille="Michel Rocard (1988-1991), sans majorité absolue à l'Assemblée, a engagé la responsabilité de son gouvernement 28 fois : c'est le record. Avec Édith Cresson et Pierre Bérégovoy, la législature 1988-1993 compte 39 usages. Manuel Valls l'a utilisé 6 fois. Les critiques sur la cohérence de la gauche sont donc fondées sur l'histoire.\n\nMais le 49.3 a servi à tous les gouvernements : un universitaire compte 100 utilisations depuis 1958. La législature 2022-2024, celle de la majorité relative d'Emmanuel Macron, en compte 23. Depuis 2008, son usage est limité à un texte par session, hors budgets, mais pas sur les textes budgétaires.\n\nAujourd'hui, la gauche propose de supprimer l'outil : le programme du Nouveau Front populaire de 2024 prévoit d'« Abroger le 49.3 » et d'instaurer la proportionnelle.",
 empathie="Tu as raison de pointer que la gauche l'a beaucoup utilisé : c'est vrai, et Rocard détient le record. La question est de savoir ce qu'on en pense aujourd'hui, et la gauche propose maintenant de le supprimer.",
 legitimes=["Le record individuel et le record par législature sont socialistes.", "La gauche l'a dénoncé surtout quand elle était dans l'opposition."],
 contre=[
  ("Donc la gauche est hypocrite.", "Elle l'a été dans le passé, comme la droite ; aujourd'hui, elle propose de supprimer l'outil, ce qui l'engagerait aussi si elle gouvernait."),
  ("Le 49.3 est démocratique, il permet une censure.", "C'est vrai, l'Assemblée peut renverser le gouvernement ; mais le texte est adopté sans vote sur son contenu."),
 ],
 questions=["Sais-tu combien de fois le 49.3 a été utilisé entre 2022 et 2024 ?", "Faut-il garder un outil qui permet d'adopter une loi sans vote ?"],
 limites=["Le décompte nominatif d'Élisabeth Borne et les usages de 2025 n'ont pas été vérifiés.", "Les totaux de Raymond Barre et des gouvernements d'avant 1988 ne sont pas détaillés dans les sources lues."],
 publics={'convaincus': "Tu as raison : Rocard détient le record, et la gauche a beaucoup utilisé le 49.3. Mais tous les gouvernements l'ont fait, et la gauche d'aujourd'hui propose de le supprimer.. La vraie question, c'est de savoir si l'on garde un outil qui permet d'adopter une loi sans vote.",
  'indecis': "L'argument est en partie juste : les socialistes ont été les plus gros utilisateurs du 49.3, quand ils n'avaient pas de majorité absolue. Mais la droite et la majorité présidentielle l'ont aussi largement utilisé. La vraie question est de savoir si on garde cet outil ; la gauche propose de l'abroger."},
 a_actualiser='2027-06-30', raison="Usages du 49.3 lors des prochaines lois de finances.",
))

# 11 ── Brexit ─────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='brexit-succes', affirmation="Le Brexit a été un succès pour le Royaume-Uni.", volet='international', sous_theme='Europe',
 mots_cles=['brexit', 'royaume uni', 'sortie de l ue', 'frexit', 'quitter l union europeenne', 'leave', 'britanniques regrettent'],
 verdict='contredit', fiabilite='interpretation',
 resume="L'organisme budgétaire public britannique estime que le Brexit réduira la productivité de long terme de 4 % et le commerce d'environ 15 %. 61 % des Britanniques le jugent aujourd'hui un échec. L'immigration, que le Brexit devait réduire, a atteint un record de 944 000 en solde net en 2023, même si celle venue de l'UE est devenue négative.",
 contexte="Le Brexit est souvent cité comme exemple par les partisans d'un Frexit ou d'une sortie des traités européens.",
 explication="En quittant l'UE, le Royaume-Uni a retrouvé la maîtrise de sa politique commerciale et migratoire, mais a perdu l'accès sans frictions au marché unique, son premier partenaire commercial.",
 sources=[OBR_BREXIT, OBR_2020, YOUGOV_BX, ONS_MIG],
 faits=[
  fait("L'OBR suppose que le Brexit réduira la productivité de long terme de 4 % par rapport au maintien dans l'UE, et que les exportations et importations seront environ 15 % plus faibles.", 'obr_brexit', 'prévision 2026', 'Royaume-Uni', "L'effet économique attendu est négatif.", 'estimation', '-4 %'),
  fait("Dès 2020, l'OBR constatait un effet déjà réalisé sur la productivité de 1,4 %, lié à un investissement plus faible.", 'obr_2020', '2016-2020', 'Royaume-Uni', "Les coûts ont commencé dès le référendum.", 'estimation', '1,4 %'),
  fait("En juin 2026, 61 % des Britanniques jugent le Brexit un échec et 12 % un succès ; 55 % sont favorables à un retour dans l'UE.", 'yougov_bx', '2026', 'Grande-Bretagne', "Une large majorité le voit comme un échec.", 'etabli', '61 %'),
  fait("Le solde migratoire a atteint 944 000 sur l'année close en mars 2023, puis 345 000 fin 2024 ; celui des ressortissants de l'UE est devenu négatif (−69 000).", 'ons_mig', '2023-2024', 'Royaume-Uni', "L'immigration a augmenté, mais en changeant d'origine.", 'etabli', '944 000'),
 ],
 court="Faux pour l'économie : l'organisme public britannique prévoit 4 % de productivité et 15 % de commerce en moins. 61 % des Britanniques jugent le Brexit un échec. Et l'immigration a battu des records après la sortie.",
 moyen="L'Office for Budget Responsibility, organisme public britannique, estime que le Brexit coûtera 4 % de productivité à long terme et réduira le commerce d'environ 15 %. Ce sont des estimations, mais l'organisme les juge confirmées par les données.\n\nLe Brexit devait aussi faire baisser l'immigration : le solde migratoire a atteint un record de 944 000 en 2023. L'immigration européenne est devenue négative, mais celle du reste du monde a explosé. Aujourd'hui, 61 % des Britanniques parlent d'échec.",
 detaille="Selon l'Office for Budget Responsibility, chargé des prévisions budgétaires britanniques, l'accord de commerce avec l'UE réduira la productivité de long terme de 4 % et le commerce d'environ 15 %. Deux cinquièmes de cet effet étaient déjà réalisés en 2021, à cause de l'investissement freiné après le référendum. Ce sont des hypothèses de modélisation, pas des mesures directes, mais l'organisme les juge toujours conformes aux données.\n\nSur l'immigration, le résultat est inverse de la promesse : le solde migratoire a atteint 944 000 sur l'année close en mars 2023. La libre circulation a pris fin et le solde des Européens est devenu négatif, mais l'immigration venue du reste du monde a fortement augmenté, avec un pic révisé à plus d'un million de non-Européens.\n\nDix ans après le référendum, 61 % des Britanniques jugent le Brexit un échec, et 55 % souhaitent un retour dans l'UE. Les électeurs du Leave restent toutefois majoritairement convaincus d'avoir eu raison de voter.",
 empathie="Je comprends l'envie de reprendre le contrôle face à une Union européenne qui paraît lointaine. Mais l'exemple britannique montre qu'en sortir coûte cher, et ne règle pas les questions qu'on voulait régler.",
 legitimes=["La libre circulation a pris fin et le solde migratoire avec l'UE est devenu négatif.", "64 % des électeurs du Leave pensent toujours avoir eu raison.", "Les chiffres de l'OBR sont des estimations par rapport à un scénario théorique."],
 contre=[
  ("Le Royaume-Uni a retrouvé sa souveraineté.", "Il a retrouvé la maîtrise de ses règles, mais il en paie le prix en commerce et en productivité, et l'immigration a augmenté."),
  ("Les difficultés viennent du covid.", "L'OBR distingue l'effet du Brexit de celui de la pandémie, et note que le pays a raté une partie de la reprise du commerce mondial."),
 ],
 questions=["Sais-tu ce que pensent aujourd'hui les Britanniques du Brexit ?", "Qu'est-ce qui a été réglé par la sortie de l'UE ?"],
 limites=["Les estimations de l'OBR reposent sur une comparaison avec un scénario contrefactuel.", "Les statistiques britanniques du commerce n'ont pas été lues directement."],
 publics={'convaincus': "Le Brexit devait rendre au pays le contrôle de son économie et de ses frontières. Résultat : l'organisme public britannique prévoit 4 % de productivité en moins, et l'immigration a atteint un record en 2023. Ce sont les Britanniques eux-mêmes, à 61 %, qui parlent d'échec.",
  'indecis': "Le Brexit a permis au Royaume-Uni de décider seul de ses règles, notamment sur la libre circulation. Mais son coût économique est estimé à 4 % de productivité, et l'immigration n'a pas baissé. Avant de proposer une sortie de l'UE en France, il est utile de regarder ce bilan."},
 a_actualiser='2027-06-30', raison="Prévisions annuelles de l'OBR et données de l'ONS.",
))

# 12 ── Hongrie et natalité ────────────────────────────────────────────────────
FICHES.append(fiche(
 id='hongrie-natalite-orban', affirmation="Orbán a réussi à relancer la natalité en Hongrie.", volet='international', sous_theme='Europe',
 mots_cles=['orban', 'hongrie', 'natalite hongrie', 'politique nataliste', 'politique familiale hongroise', 'fecondite hongrie', 'pret bebe'],
 verdict='contredit', fiabilite='etabli',
 resume="La fécondité hongroise est passée de 1,23 enfant par femme en 2011 à 1,61 en 2021, mais elle est retombée à 1,31 en 2025. Les naissances sont au plus bas : 72 017 en 2025, contre 90 335 en 2010. La politique familiale, qui coûterait environ 5 % du PIB, n'a pas produit le redressement durable promis.",
 contexte="La Hongrie de Viktor Orbán est présentée par l'extrême droite comme le modèle d'une politique nataliste qui permettrait de se passer d'immigration.",
 explication="L'indice de fécondité peut monter temporairement quand des couples avancent des naissances qu'ils auraient eues plus tard (« effet de calendrier ») ; cela ne change pas forcément le nombre total d'enfants par femme.",
 sources=[KSH_FEC, AFP_HONG, AEI_HONG],
 faits=[
  fait("L'indice de fécondité hongrois est passé de 1,23 en 2011 à 1,61 en 2021, puis à 1,51 en 2023, 1,39 en 2024 et 1,31 en 2025.", 'ksh_fec', '2011-2025', 'Hongrie', "La hausse a été suivie d'une rechute.", 'etabli', '1,31 en 2025'),
  fait("Les naissances vivantes sont passées de 90 335 en 2010 à 72 017 en 2025.", 'ksh_fec', '2010-2025', 'Hongrie', "Il naît moins d'enfants qu'avant les mesures.", 'etabli', '72 017'),
  fait("Le gouvernement vise 2,1 enfants par femme en 2035 et a ajouté en 2025 une exonération d'impôt sur le revenu à vie pour les mères de deux enfants, estimée à 2,3 Md€ d'ici 2029.", 'afp_hong', '2025', 'Hongrie', "La politique coûte cher et s'intensifie.", 'estimation', '2,3 Md€'),
  fait("La Hongrie consacrerait environ 5 % de son PIB aux aides aux familles ; selon un démographe, la hausse de 2011-2021 tient surtout à un effet de calendrier des naissances.", 'aei_hong', '2010-2025', 'Hongrie', "L'effet durable est discuté.", 'interpretation', '5 % du PIB'),
 ],
 court="Faux : la fécondité hongroise est remontée de 1,23 à 1,61 entre 2011 et 2021, puis retombée à 1,31 en 2025. Il naît moins d'enfants qu'en 2010, malgré une politique familiale estimée à 5 % du PIB.",
 moyen="La Hongrie a connu une vraie remontée de la fécondité, de 1,23 enfant par femme en 2011 à 1,61 en 2021. Mais la tendance s'est inversée : 1,31 en 2025, et seulement 72 017 naissances, le plus bas niveau.\n\nUn démographe explique la hausse surtout par des naissances avancées dans le temps. Malgré des aides très coûteuses (prêts, logement, exonérations d'impôt), la Hongrie n'a pas trouvé la recette pour relancer durablement la natalité.",
 detaille="Selon l'office statistique hongrois, l'indice de fécondité était de 1,23 en 2011, l'un des plus bas d'Europe. Il a progressé jusqu'à 1,61 en 2021, ce que le gouvernement Orbán présente comme le succès de sa politique familiale : prêts bébé, aides au logement et à l'achat de voiture, garde gratuite, exonérations fiscales.\n\nDepuis, la fécondité recule chaque année : 1,51 en 2023, 1,39 en 2024, 1,31 en 2025. Les naissances sont tombées à 72 017, contre 90 335 en 2010. Le démographe Wolfgang Lutz estime que la hausse tenait surtout à un effet de calendrier : des couples ont avancé des naissances. L'AFP parle d'une stratégie très coûteuse aux « effets mitigés ».\n\nLe cas hongrois montre que des aides financières massives ne suffisent pas à relancer durablement la natalité.",
 empathie="Je comprends l'inquiétude devant la baisse des naissances, et l'envie d'aider les familles. Mais la Hongrie montre qu'on ne relance pas durablement la natalité à coups d'aides : elle a dépensé énormément, et la fécondité est retombée.",
 legitimes=["La fécondité hongroise a fortement remonté entre 2011 et 2021, d'un des niveaux les plus bas d'Europe."],
 contre=[
  ("C'est mieux que rien.", "La fécondité de 2025 (1,31) est à peine supérieure à celle de 2011 (1,23), et il naît moins d'enfants qu'en 2010."),
  ("La France devrait faire pareil.", "Le cas hongrois montre que l'efficacité de ces aides, très coûteuses, est limitée et discutée."),
 ],
 questions=["Sais-tu ce qu'est devenue la fécondité hongroise depuis 2021 ?", "Qu'est-ce qui aide vraiment les couples à avoir des enfants : une prime, ou un logement et un emploi stables ?"],
 limites=["Le coût de 5 % du PIB vient d'un think tank conservateur américain et n'a pas été vérifié auprès de l'OCDE.", "La baisse du nombre de femmes en âge d'avoir des enfants n'a pas été vérifiée."],
 publics={'convaincus': "Orbán a dépensé des sommes énormes pour la natalité, et la fécondité a bien monté jusqu'en 2021. Mais elle est retombée à 1,31 en 2025, et il naît moins d'enfants qu'en 2010. Même le modèle préféré de l'extrême droite ne marche pas durablement.",
  'indecis': "La Hongrie a connu une remontée réelle de la fécondité, puis une rechute nette. Les chercheurs pensent que les aides ont surtout fait avancer des naissances. Pour soutenir les familles, le logement, l'emploi stable et les modes de garde comptent au moins autant que les primes."},
 a_actualiser='2027-07-31', raison="Données annuelles de l'office statistique hongrois.",
))

# 13 ── Travailleurs détachés ─────────────────────────────────────────────────
FICHES.append(fiche(
 id='travailleurs-detaches-dumping', affirmation="Les travailleurs détachés font du dumping social.", volet='social', sous_theme='Emploi et salaires',
 mots_cles=['travailleurs detaches', 'salaries detaches', 'detachement', 'directive detachement', 'plombier polonais', 'dumping social', 'travail detache'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Le dumping existe, mais il est limité et encadré. Depuis 2020, le droit européen impose de payer un détaché comme un salarié du pays d'accueil dès le premier jour. Les détachés présents à un moment donné ne représentent que 0,3 % de l'emploi salarié privé. Les cotisations sociales restent payées dans le pays d'origine, et les fraudes documentées par le Sénat sont réelles.",
 contexte="Le thème du « plombier polonais » est ancien ; il est repris aussi bien par l'extrême droite que par une partie de la gauche.",
 explication="Un travailleur détaché est envoyé temporairement en France par une entreprise d'un autre pays. Il doit recevoir le salaire prévu en France, mais reste affilié à la sécurité sociale de son pays, souvent moins coûteuse.",
 sources=[DARES_DET, PE_DET, SEN_FRAUDE],
 faits=[
  fait("En 2022, 59 300 salariés détachés sont présents en moyenne à une date donnée, 18 % de moins qu'en 2019, soit 0,3 % de l'emploi salarié privé (1,5 % dans l'agriculture).", 'dares_det', '2022', 'France hors transport routier', "Le phénomène est marginal à l'échelle de l'emploi.", 'etabli', '0,3 %'),
  fait("Le BTP regroupe 42 % des détachés et l'industrie 29 % ; 70 % viennent de l'UE.", 'dares_det', '2022', 'France', "Il est concentré dans quelques secteurs.", 'etabli', '42 %'),
  fait("Depuis le 30 juillet 2020, les règles de rémunération du pays d'accueil s'appliquent dès le premier jour, et les frais de voyage et de logement ne peuvent pas être déduits du salaire.", 'pe_det', '2020', 'Union européenne', "Le dumping salarial est désormais illégal.", 'etabli'),
  fait("Le Parlement européen reconnaît que la hausse des détachements de 44,4 % entre 2010 et 2014 tenait en partie aux écarts de salaires et de coût du travail.", 'pe_det', '2010-2014', 'Union européenne', "Le dumping a bien existé.", 'etabli', '+44,4 %'),
  fait("Le Sénat a documenté des fraudes : cotisations non versées dans le pays d'origine, sociétés « boîtes aux lettres », agences d'intérim créées pour détacher.", 'sen_fraude', '2017', 'France', "La fraude est réelle et difficile à contrôler.", 'etabli'),
 ],
 court="Trompeur : depuis 2020, un détaché doit être payé comme un salarié français dès le premier jour, et les détachés ne pèsent que 0,3 % de l'emploi privé. Mais les cotisations restent payées dans le pays d'origine et la fraude existe : c'est un problème de contrôle.",
 moyen="Le dumping a été réel : le Parlement européen reconnaît que les écarts de salaires ont fait grimper les détachements. Depuis 2020, la règle a changé : « à travail égal, salaire égal » dès le premier jour.\n\nLes détachés restent peu nombreux : 59 300 présents en moyenne en 2022, 0,3 % de l'emploi privé, surtout dans le BTP. Les problèmes qui restent sont les cotisations payées dans le pays d'origine et les fraudes. La réponse, ce sont des contrôles et des inspecteurs du travail, pas la fermeture des frontières.",
 detaille="Selon la Dares, 223 300 salariés ont été détachés au moins une fois en France en 2022, hors transport routier, mais 59 300 seulement sont présents à une date donnée, soit 0,3 % de l'emploi salarié privé. Le BTP en concentre 42 %, l'industrie 29 %, et leur part atteint 1,5 % dans l'agriculture.\n\nLe dumping a existé : les détachements ont augmenté de 44,4 % entre 2010 et 2014, en partie à cause des écarts de salaires. La directive révisée, appliquée depuis 2020, impose la rémunération du pays d'accueil dès le premier jour et interdit de retenir le logement ou le transport sur le salaire. Au-delà de 12 à 18 mois, tout le droit du travail français s'applique.\n\nUn écart de coût légal subsiste, car les cotisations sociales sont payées dans le pays d'origine. Et le Sénat a décrit des fraudes : sociétés boîtes aux lettres, cotisations non versées. Ce sont des failles de contrôle.",
 empathie="Je comprends la colère des artisans et ouvriers du bâtiment qui ont vu arriver des concurrents moins chers. Ce dumping a existé. Aujourd'hui, la loi impose les mêmes salaires ; ce qu'il faut, ce sont des contrôles pour la faire respecter.",
 legitimes=["Les cotisations sociales restent payées dans le pays d'origine, souvent moins cher.", "La fraude au détachement est documentée.", "Le dumping a nourri la hausse des détachements dans les années 2010."],
 contre=[
  ("Ils prennent le travail des Français.", "Ils représentent 0,3 % de l'emploi salarié privé, et leur nombre a baissé de 18 % entre 2019 et 2022."),
  ("C'est la faute de l'Europe.", "L'Europe a aussi durci la règle en 2018 ; le problème restant est le contrôle et l'écart de cotisations."),
 ],
 questions=["Sais-tu que depuis 2020, un détaché doit être payé au salaire français dès le premier jour ?", "Qui profite vraiment de la fraude : le travailleur ou l'entreprise qui l'emploie ?"],
 limites=["Les chiffres de fraude constatée par l'inspection du travail n'ont pas été lus.", "Le rapport du Sénat date de 2017, avant la révision de la directive.", "Le transport routier est exclu des chiffres de la Dares."],
 publics={'convaincus': "Le dumping a existé, tu as raison. Mais depuis 2020, la loi impose de payer un détaché comme un Français, et ils ne pèsent que 0,3 % de l'emploi privé. Ceux qui trichent, ce sont des entreprises qui fraudent : il faut plus d'inspecteurs du travail, pas moins de droits pour les salariés.",
  'indecis': "La concurrence par les bas salaires a été réelle, surtout dans le bâtiment. La règle a changé en 2020 : même salaire dès le premier jour. Restent un écart de cotisations et des fraudes, qui appellent surtout des contrôles renforcés."},
 a_actualiser='2027-06-30', raison="Nouvelle publication de la Dares sur le détachement.",
))

# 14 ── SMIC en Europe ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='smic-europe-classement', affirmation="Le SMIC français est l'un des plus élevés d'Europe.", volet='economie', sous_theme='Salaires',
 mots_cles=['smic europe', 'salaire minimum europe', 'smic le plus eleve', 'smic allemagne', 'classement smic', 'salaires minimums europeens', 'smic trop haut'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="Plutôt vrai : avec 1 823 € brut par mois au 1er janvier 2026, le SMIC français est 6e sur 22 pays de l'UE dotés d'un salaire minimum, mais environ 500 € derrière l'Allemagne et l'Irlande. Il est parmi les plus élevés par rapport au salaire médian (plus de 60 %), ce qui reflète aussi des salaires médians tassés. Et 12,4 % des salariés sont payés au SMIC.",
 contexte="L'argument sert à refuser toute hausse du SMIC, ou à l'inverse à vanter le modèle social français.",
 explication="On compare les salaires minimums en euros, en pouvoir d'achat (qui tient compte des prix), ou par rapport au salaire médian du pays. Plusieurs pays riches, comme le Danemark ou la Suède, n'ont pas de salaire minimum légal : les salaires y sont fixés par des conventions collectives.",
 sources=[EUROSTAT_SM, EUROSTAT_SE, INSEE_SMIC],
 faits=[
  fait("Au 1er janvier 2026, le salaire minimum brut mensuel est de 2 704 € au Luxembourg, 2 391 € en Irlande, 2 343 € en Allemagne, 2 295 € aux Pays-Bas, 2 112 € en Belgique et 1 823 € en France.", 'eurostat_sm', '2026', 'Union européenne', "La France est 6e, nettement derrière cinq pays.", 'etabli', '1 823 €'),
  fait("Danemark, Italie, Autriche, Finlande et Suède n'ont pas de salaire minimum national.", 'eurostat_sm', '2026', 'Union européenne', "Plusieurs pays riches échappent au classement.", 'etabli'),
  fait("En 2024, le salaire minimum français dépasse 60 % du salaire médian, comme aux Pays-Bas et au Luxembourg ; il est entre 50 et 60 % en Allemagne.", 'eurostat_se', '2024', 'Union européenne', "Rapporté au salaire médian, le SMIC est parmi les plus élevés.", 'etabli', '> 60 %'),
  fait("Au 1er novembre 2024, 2,2 millions de salariés, soit 12,4 % du champ étudié, ont bénéficié directement de la revalorisation du SMIC.", 'insee_smic', '2024', 'France', "Beaucoup de salariés sont payés au minimum.", 'etabli', '12,4 %'),
 ],
 court="Plutôt vrai : le SMIC est 6e de l'UE avec 1 823 € brut, mais environ 500 € derrière l'Allemagne. Il est élevé par rapport au salaire médian, ce qui montre aussi que les salaires au-dessus du SMIC progressent peu.",
 moyen="En euros, le SMIC français (1 823 € brut en janvier 2026) est 6e dans l'UE, derrière le Luxembourg, l'Irlande, l'Allemagne, les Pays-Bas et la Belgique. Il fait partie du groupe de tête en pouvoir d'achat.\n\nIl est surtout élevé par rapport au salaire médian (plus de 60 %). Mais cela veut aussi dire que les salaires moyens sont tassés : beaucoup de salariés restent bloqués près du SMIC. Le problème n'est pas un SMIC trop haut, mais des salaires qui ne décollent pas.",
 detaille="Selon Eurostat, au 1er janvier 2026, six pays de l'UE dépassent 1 500 € brut par mois : le Luxembourg (2 704 €), l'Irlande (2 391 €), l'Allemagne (2 343 €), les Pays-Bas (2 295 €), la Belgique (2 112 €) et la France (1 823 €). La France est donc dans le haut du classement, mais à environ 500 € de l'Allemagne. Cinq pays, dont le Danemark et la Suède, n'ont pas de salaire minimum légal.\n\nRapporté au salaire médian, le SMIC français est parmi les plus élevés : plus de 60 % en 2024, contre 50 à 60 % en Allemagne. C'est en partie vrai que le SMIC « mord » beaucoup ; mais c'est aussi le signe d'une échelle des salaires écrasée vers le bas.\n\nEn novembre 2024, 12,4 % des salariés ont été concernés directement par la revalorisation du SMIC, et près d'un quart des salariés à temps partiel. La question n'est pas seulement le niveau du SMIC, mais la progression des salaires au-dessus.",
 empathie="C'est vrai que le SMIC français est dans le haut du tableau européen, et on peut en être fier. Mais quand on vit avec, à 1 823 € brut, on sait que ça ne fait pas une vie confortable, et beaucoup de salariés y restent bloqués.",
 legitimes=["Le SMIC français est 6e de l'UE en euros.", "Par rapport au salaire médian, il est parmi les plus élevés d'Europe."],
 contre=[
  ("Si on l'augmente, on détruit des emplois.", "Le ratio élevé avec le salaire médian montre surtout que les salaires médians progressent peu ; d'autres pays ont des minimums bien plus hauts."),
  ("On est les mieux payés d'Europe.", "Non : cinq pays font mieux, dont l'Allemagne avec environ 500 € de plus."),
 ],
 questions=["Sais-tu combien gagne un salarié au salaire minimum en Allemagne ?", "Pourquoi tant de salariés restent-ils bloqués au SMIC pendant des années ?"],
 limites=["Le chiffre exact de la France en standards de pouvoir d'achat n'a pas été lu.", "Le ratio SMIC/salaire médian de l'OCDE n'a pas été lu directement."],
 publics={'convaincus': "Oui, le SMIC est dans le haut du classement, mais l'Allemagne paie son salaire minimum environ 500 € de plus. Si le SMIC paraît élevé par rapport aux autres salaires, c'est surtout parce que ceux-ci progressent trop peu. Le problème, ce sont des patrons qui tassent les salaires, pas les smicards.",
  'indecis': "Le SMIC français est l'un des plus élevés d'Europe en euros et par rapport au salaire médian. Mais 12,4 % des salariés sont payés au SMIC et beaucoup y restent bloqués. Le vrai débat porte sur la progression des salaires au-dessus du minimum."},
 a_actualiser='2027-02-28', raison="Données Eurostat de janvier 2027.",
))

# 15 ── Banlieues et « milliards » ──────────────────────────────────────────────
FICHES.append(fiche(
 id='banlieues-milliards-politique-ville', affirmation="On a déversé des milliards dans les banlieues, pour rien.", volet='services', sous_theme='Services publics locaux',
 mots_cles=['politique de la ville', 'milliards dans les banlieues', 'plan banlieue', 'renovation urbaine', 'quartiers prioritaires', 'anru', 'argent des banlieues', 'deverse des milliards'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Les crédits propres à la politique de la ville sont modestes : environ 524 millions d'euros par an, et 25 milliards cumulés en vingt ans pour les contrats de ville et la rénovation urbaine. Selon la Cour des comptes, le total réellement dépensé dans les quartiers est inconnu, et les services publics ordinaires y sont souvent moins présents qu'ailleurs. Les résultats sont décevants, mais le chômage y a reculé.",
 contexte="L'argument oppose les quartiers populaires aux zones rurales, qui seraient abandonnées pendant que les banlieues seraient « arrosées ».",
 explication="La politique de la ville apporte des crédits supplémentaires aux quartiers prioritaires. Mais elle ne remplace pas les services publics ordinaires (école, police, justice, santé), dits de « droit commun », qui devraient bénéficier à ces quartiers comme aux autres.",
 sources=[CC_VILLE26, CC_VILLE20, AN_93],
 faits=[
  fait("Le programme budgétaire de la politique de la ville a consommé 524 M€ en 2024, niveau stable depuis 2020.", 'cc_ville26', '2020-2024', 'France', "Les crédits propres sont modestes.", 'etabli', '524 M€'),
  fait("De 2004 à 2024, 11 Md€ cumulés ont financé les actions des contrats de ville et 14 Md€ le renouvellement urbain.", 'cc_ville26', '2004-2024', 'France', "Les « milliards » sont étalés sur vingt ans.", 'etabli', '25 Md€ en 20 ans'),
  fait("La Cour des comptes écrit que « le montant global des moyens budgétaires dont bénéficient les QPV est dès lors inconnu », et signale un risque que les crédits spécifiques remplacent ceux de droit commun.", 'cc_ville26', '2026', 'France', "Personne ne peut affirmer que les quartiers reçoivent plus qu'ailleurs.", 'etabli'),
  fait("En Seine-Saint-Denis, en 2015-2016, les absences courtes des enseignants du primaire étaient remplacées à 51,26 %, contre 78,41 % en France.", 'an_93', '2015-2016', 'Seine-Saint-Denis', "Les services publics ordinaires y sont moins présents.", 'etabli', '51 % contre 78 %'),
  fait("Dans les quartiers prioritaires, le chômage est passé de 25 % à 18 % entre 2014 et 2022, mais la pauvreté reste de 44 % contre 15 % en métropole, et le revenu médian a moins progressé qu'ailleurs.", 'cc_ville26', '2014-2022', 'France', "Il y a des progrès, mais les écarts restent énormes.", 'etabli', '44 %'),
 ],
 court="Trompeur : les crédits de la politique de la ville sont d'environ 524 millions par an, une goutte d'eau dans le budget de l'État. Selon la Cour des comptes, les services publics ordinaires y sont souvent moins présents qu'ailleurs. Les résultats sont faibles, mais le chômage y a reculé.",
 moyen="Les « milliards » existent, mais sur vingt ans : environ 25 milliards pour les contrats de ville et la rénovation urbaine depuis 2004. Le budget annuel de la politique de la ville est de 524 millions d'euros.\n\nSurtout, la Cour des comptes constate que ces crédits remplacent parfois les services publics ordinaires au lieu de s'y ajouter. En Seine-Saint-Denis, un rapport parlementaire montrait moins de remplacements de professeurs et une justice plus lente qu'ailleurs. Les quartiers n'ont pas reçu plus : ils ont souvent reçu moins.",
 detaille="La politique de la ville dispose d'un programme budgétaire de 524 millions d'euros par an. Entre 2004 et 2024, 11 milliards ont financé les contrats de ville et 14 milliards la rénovation urbaine. Ces sommes sont importantes, mais étalées sur vingt ans.\n\nLa Cour des comptes juge que le montant total des moyens dont bénéficient ces quartiers est « inconnu ». Elle signale un risque que les crédits spécifiques remplacent les crédits ordinaires. En Seine-Saint-Denis, un rapport parlementaire transpartisan de 2018 montrait des absences d'enseignants moins remplacées et au tribunal d'instance d'Aubervilliers, des délais d'audience six fois plus longs qu'à Paris, et parlait d'un « échec de l'État ».\n\nLes résultats sont décevants : la pauvreté reste de 44 % dans les quartiers prioritaires, contre 15 % en métropole, et leur attractivité a peu progressé. Mais le chômage y est passé de 25 % à 18 % entre 2014 et 2022. Le problème n'est pas que l'argent coule à flots, c'est que l'égalité des services publics n'est pas assurée.",
 empathie="Je comprends le sentiment d'injustice quand on vit dans un village où la poste et l'école ferment. Mais les quartiers populaires vivent la même chose : la Cour des comptes montre que l'État y est souvent moins présent qu'ailleurs.",
 legitimes=["La Cour des comptes juge les résultats faibles : pauvreté toujours concentrée, attractivité stagnante.", "La rénovation urbaine a mobilisé des sommes importantes."],
 contre=[
  ("Pendant ce temps, la campagne est abandonnée.", "Les quartiers populaires souffrent aussi du recul des services publics : les deux territoires ont le même intérêt à l'égalité."),
  ("Ça n'a servi à rien.", "Le chômage y a baissé de 25 % à 18 % entre 2014 et 2022, même si les écarts restent énormes."),
 ],
 questions=["Sais-tu quel est le budget annuel de la politique de la ville ?", "Les quartiers reçoivent-ils autant de professeurs, de policiers et de juges que les autres ?"],
 limites=["Le chiffrage des crédits de droit commun dépensés dans les quartiers n'existe pas, selon la Cour des comptes.", "Les données sur la Seine-Saint-Denis datent de 2015 à 2017."],
 publics={'convaincus': "Le budget de la politique de la ville, c'est 524 millions par an, une goutte d'eau. La Cour des comptes montre que dans ces quartiers, l'État fournit souvent moins de profs et de juges qu'ailleurs. Les habitants des banlieues et ceux des campagnes subissent le même abandon des services publics.",
  'indecis': "Des sommes importantes ont été investies, notamment pour rénover les logements, et les résultats sont décevants. Mais ces crédits remplacent souvent les services publics ordinaires au lieu de s'y ajouter. Le vrai enjeu, c'est que chaque quartier ait les mêmes écoles, la même police et la même justice que les autres."},
 a_actualiser='2027-06-30', raison="Rapports de la Cour des comptes et de l'Observatoire national de la politique de la ville.",
))

# 16 ── Profs 18 heures ────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='profs-18-heures', affirmation="Les profs ne travaillent que 18 heures par semaine.", volet='services', sous_theme='École publique',
 mots_cles=['profs 18 heures', 'enseignants 18 heures', 'temps de travail des enseignants', 'profs vacances', 'profs toujours en vacances', 'obligations de service', 'heures de cours'],
 verdict='trompeur', fiabilite='etabli',
 resume="Les 18 heures sont les heures de cours que doit un professeur certifié du second degré (15 pour un agrégé), pas son temps de travail. Les enquêtes du ministère donnent 41 à 43 heures déclarées par semaine, avec la préparation des cours et la correction des copies, et environ 33 jours travaillés pendant les vacances. Sur l'année, cela fait autour des 1 607 heures légales.",
 contexte="Le cliché revient à chaque grève ou débat sur les salaires des enseignants.",
 explication="Les « obligations de service » fixent le nombre d'heures de cours. Mais le décret qui les fixe range dans les missions du professeur la préparation des cours, le suivi et l'évaluation des élèves, les relations avec les parents et le travail en équipe.",
 sources=[LEGI_ORS, IH2EF_PROF, WEKA_PROF],
 faits=[
  fait("Le service d'enseignement hebdomadaire est de 15 heures pour les agrégés et 18 heures pour les certifiés ; la préparation des cours, l'évaluation des élèves et les relations avec les parents font partie des missions.", 'legi_ors', '2014', 'France, second degré', "Les 18 heures sont des heures de cours, pas tout le travail.", 'etabli', '18 h'),
  fait("La moitié des enseignants à temps plein déclarent travailler au moins 43 heures par semaine (enquête de 2018).", 'ih2ef_prof', '2018', 'France', "Le temps de travail réel est bien supérieur.", 'estimation', '43 h'),
  fait("En 2022-2023, les enseignants déclarent 41,4 heures par semaine hors vacances : 53 % devant les élèves, 33 % de préparation et de correction.", 'weka_prof', '2022-2023', 'France', "Un tiers du temps sert à préparer et corriger.", 'estimation', '41,4 h'),
  fait("Ils déclarent en moyenne 33 jours travaillés pendant les vacances, soit environ 1 635 heures par an, 28 de plus que les 1 607 heures légales.", 'weka_prof', '2022-2023', 'France', "Sur l'année, ils travaillent l'équivalent d'un temps plein.", 'estimation', '1 635 h'),
 ],
 court="Faux : 18 heures, ce sont les heures de cours d'un professeur certifié. Avec la préparation et les corrections, les enseignants déclarent 41 à 43 heures par semaine, et environ 1 635 heures par an, autant qu'un temps plein.",
 moyen="Le décret de 2014 fixe 18 heures de cours pour un certifié, 15 pour un agrégé. Mais il précise que la préparation des cours, les corrections et les relations avec les parents font partie du métier.\n\nLes enquêtes du ministère donnent 41 à 43 heures de travail déclarées par semaine. En comptant les vacances, où ils travaillent en moyenne 33 jours, les enseignants arrivent à environ 1 635 heures par an, un peu plus que les 1 607 heures d'un salarié à temps plein.",
 detaille="Le décret du 20 août 2014 fixe le service d'enseignement à 18 heures hebdomadaires pour les professeurs certifiés et 15 pour les agrégés. Il énumère aussi les missions liées à ce service : préparation des cours, suivi du travail des élèves, évaluation, relations avec les parents, travail en équipe.\n\nSelon les enquêtes du ministère, la moitié des enseignants à temps plein déclarent travailler au moins 43 heures par semaine (2018). En 2022-2023, ils déclarent 41,4 heures hors vacances, dont 53 % devant les élèves et un tiers pour préparer et corriger. Ils travaillent aussi en moyenne 33 jours pendant les vacances.\n\nSur l'année, cela représente environ 1 635 heures, à peine plus que les 1 607 heures légales d'un temps plein. Ces chiffres sont déclarés par les enseignants eux-mêmes, mais ils sont cohérents d'une enquête à l'autre. Le vrai débat porte sur l'organisation du temps et sur les salaires, pas sur la paresse supposée d'une profession.",
 empathie="Je comprends que les vacances scolaires fassent envie, et qu'on ait l'impression que les profs ont la belle vie. Mais les 18 heures sont seulement le temps passé devant les élèves ; derrière, il y a les cours à préparer et les copies à corriger.",
 legitimes=["Les heures de travail sont déclarées par les enseignants, pas mesurées.", "Le total annuel dépasse à peine les 1 607 heures légales."],
 contre=[
  ("Ils ont quatre mois de vacances.", "Ils déclarent travailler en moyenne 33 jours pendant les vacances, et leur total annuel atteint environ 1 635 heures."),
  ("Une fois les cours préparés, c'est fini.", "Un tiers de leur temps est consacré à préparer et corriger, chaque année, selon les enquêtes du ministère."),
 ],
 questions=["Combien de temps faut-il pour préparer une heure de cours et corriger 30 copies ?", "Sais-tu combien d'heures par an déclarent les enseignants ?"],
 limites=["Les données de 2022-2023 ne sont connues qu'à travers un média spécialisé.", "Les obligations du premier degré n'ont pas été vérifiées sur un texte officiel."],
 publics={'convaincus': "Les 18 heures, ce sont les heures de cours, pas tout le travail : le décret lui-même inclut la préparation et les corrections. Les enquêtes donnent 41 heures par semaine, et environ 1 635 heures par an, autant qu'un temps plein.",
  'indecis': "Les enseignants ont 18 heures de cours (15 pour les agrégés), mais ils déclarent en moyenne 41 à 43 heures de travail par semaine. Sur l'année, en comptant les vacances, ils sont proches d'un temps plein. On peut débattre de l'organisation de leur temps, mais pas les réduire à 18 heures."},
 a_actualiser='2027-11-30', raison="Nouvelle enquête de la DEPP sur le temps de travail.",
))

# 17 ── Cheminots ──────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='cheminots-retraite-50-ans', affirmation="Les cheminots partent à la retraite à 50 ans.", volet='droits', sous_theme='Droits des travailleurs',
 mots_cles=['cheminots', 'retraite des cheminots', 'sncf retraite', 'regime special sncf', 'regimes speciaux', 'conducteurs de train', 'retraite a 50 ans'],
 verdict='trompeur', fiabilite='etabli',
 resume="L'âge de 50 ans ne concernait que les conducteurs de train, et il est relevé progressivement à 54 ans. L'âge moyen de départ à la SNCF était de 56,9 ans en 2019, et il doit monter à 57 ans pour les conducteurs et 62 ans pour les autres agents. Surtout, le régime spécial est fermé depuis 2020 : les cheminots embauchés depuis relèvent du régime général.",
 contexte="Les cheminots sont souvent présentés comme des privilégiés, notamment lors des grèves contre les réformes des retraites.",
 explication="Le régime spécial de la SNCF prévoyait des âges de départ plus bas pour tenir compte de métiers pénibles et des horaires décalés. Il est en voie d'extinction : plus aucun nouvel embauché n'y entre depuis le 1er janvier 2020.",
 sources=[COR_SNCF, PS_SNCF23, PS_SNCF24, DREES_AGE],
 faits=[
  fait("L'âge minimal de base est de 50 ans pour les conducteurs et 55 ans pour les sédentaires, relevé progressivement à 54 et 59 ans.", 'cor_sncf', '2024', 'Régime de la SNCF', "Les 50 ans ne concernaient que les conducteurs, et sont relevés.", 'etabli', '50 à 54 ans'),
  fait("L'âge moyen de départ à la SNCF était de 56,9 ans selon un rapport de la Cour des comptes de 2019.", 'ps_sncf23', '2019', 'SNCF', "On part en moyenne vers 57 ans, pas à 50.", 'etabli', '56,9 ans'),
  fait("Le régime est fermé aux nouvelles recrues depuis le 1er janvier 2020.", 'cor_sncf', '2020', 'SNCF', "Les jeunes cheminots relèvent du régime général.", 'etabli'),
  fait("L'âge moyen de départ doit se stabiliser à 62 ans pour les sédentaires et 57 ans pour les conducteurs.", 'cor_sncf', 'projection', 'SNCF', "L'écart avec le régime général se réduit.", 'estimation', '62 et 57 ans'),
  fait("Fin 2023, l'âge conjoncturel de départ se situe entre 56,2 et 59,8 ans pour la SNCF, la RATP et les industries électriques et gazières, contre 62 ans et 9 mois tous régimes confondus.", 'drees_age', '2023', 'France', "Les régimes spéciaux partent encore plus tôt que la moyenne.", 'etabli'),
 ],
 court="Trompeur : 50 ans ne concernait que les conducteurs, et c'est relevé à 54 ans. L'âge moyen de départ à la SNCF était de 56,9 ans en 2019. Et le régime spécial est fermé depuis 2020 aux nouveaux embauchés.",
 moyen="Seuls les conducteurs de train pouvaient partir dès 50 ans ; cet âge est relevé progressivement à 54 ans. Pour les autres agents, l'âge minimal passe de 55 à 59 ans. En moyenne, les cheminots partaient à 56,9 ans en 2019.\n\nLe régime spécial est fermé depuis 2020 : les cheminots embauchés depuis cotisent au régime général. Il reste un écart avec la moyenne nationale, qui tient à des métiers pénibles et des horaires décalés, mais il se réduit.",
 detaille="Selon le Conseil d'orientation des retraites, l'âge minimal de départ du régime de la SNCF était de 50 ans pour les conducteurs et de 55 ans pour les sédentaires ; il est relevé progressivement à 54 et 59 ans, au fil des réformes de 2010, 2014 et 2023. En 2024, l'âge légal allait de 52 à 57 ans selon le poste.\n\nL'âge moyen de départ était de 56,9 ans en 2019 selon la Cour des comptes. Fin 2023, il se situait entre 56,2 et 59,8 ans pour les grands régimes spéciaux, contre près de 63 ans tous régimes confondus. L'écart est donc réel. Il doit se réduire : le COR projette 57 ans pour les conducteurs et 62 ans pour les autres agents.\n\nSurtout, depuis le 1er janvier 2020, plus aucun nouvel embauché n'entre dans ce régime. Le régime compte 112 000 cotisants pour 233 000 pensionnés, ce qui explique que l'État le subventionne, à hauteur d'environ 3 milliards d'euros par an.",
 empathie="Je comprends que ça puisse choquer quand on doit soi-même travailler jusqu'à 64 ans. Mais les 50 ans, c'était pour les conducteurs, avec des horaires de nuit et de week-end, et ce régime est fermé depuis 2020.",
 legitimes=["Les cheminots partent encore plusieurs années avant la moyenne nationale.", "L'État subventionne le régime à hauteur d'environ 3 milliards d'euros par an.", "Un accord de 2024 a créé une cessation anticipée pour les métiers pénibles."],
 contre=[
  ("Ce sont des privilégiés.", "Les âges plus bas compensaient des métiers pénibles et des horaires décalés ; le régime est fermé aux nouveaux embauchés depuis 2020."),
  ("C'est nous qui payons leur retraite.", "La subvention de l'État s'explique par le déséquilibre démographique d'un régime fermé : 112 000 cotisants pour 233 000 pensionnés."),
 ],
 questions=["Sais-tu que le régime spécial de la SNCF est fermé depuis 2020 ?", "Faut-il prendre en compte la pénibilité des métiers dans l'âge de départ, pour tous les salariés ?"],
 limites=["Le rapport de la Cour des comptes de 2019 n'a été lu qu'à travers Public Sénat.", "La valeur DREES propre à la SNCF n'est donnée que dans une fourchette."],
 publics={'convaincus': "Les 50 ans ne concernaient que les conducteurs, et c'est relevé à 54. En moyenne, un cheminot partait à 56,9 ans, et le régime est fermé depuis 2020. Plutôt que d'en vouloir aux cheminots, pourquoi ne pas exiger que la pénibilité soit reconnue pour tous ?",
  'indecis': "Les cheminots partent encore plus tôt que la moyenne, c'est vrai, mais pas à 50 ans pour la plupart : vers 57 ans en moyenne. Ce régime est en voie d'extinction depuis 2020. La vraie question est de savoir comment prendre en compte la pénibilité de tous les métiers."},
 a_actualiser='2027-06-30', raison="Rapport annuel du COR.",
))

# 18 ── Abaya et laïcité à l'école ─────────────────────────────────────────────
FICHES.append(fiche(
 id='abaya-laicite-ecole', affirmation="Les abayas et les atteintes à la laïcité envahissent l'école.", volet='droits', sous_theme='Laïcité',
 mots_cles=['abaya', 'abayas', 'qamis', 'atteintes a la laicite', 'tenues religieuses ecole', 'interdiction de l abaya'],
 verdict='trompeur', fiabilite='etabli',
 resume="Les signalements d'atteintes à la laïcité ont bien doublé en 2022-2023, à 4 710, surtout à cause des abayas. Mais rapportés à environ 12 millions d'élèves, les volumes restent très faibles : 298 élèves se sont présentées en abaya à la rentrée 2023. Après l'interdiction, validée par le Conseil d'État, les signalements sont retombés à 110 en septembre 2024.",
 contexte="L'abaya a fait la une à la rentrée 2023, quand le ministre de l'Éducation l'a interdite.",
 explication="La loi de 2004 interdit à l'école les signes et tenues par lesquels les élèves manifestent ostensiblement une appartenance religieuse. Le ministère publie des bilans des signalements faits par les personnels.",
 sources=[CE_ABAYA, PS_LAIC, CHN_ABAYA],
 faits=[
  fait("Les signalements d'atteintes à la laïcité sont passés à 4 710 en 2022-2023, contre 2 167 et 2 226 les deux années précédentes ; ceux qui concernent des tenues atteignent 1 984, en majorité des abayas.", 'ce_abaya', '2020-2023', 'France', "La hausse de 2022-2023 est réelle.", 'etabli', '4 710'),
  fait("Le jour de la rentrée 2023, 298 élèves se sont présentées en abaya, et 67 ont été renvoyées chez elles faute d'avoir accepté de la retirer, pour environ 12 millions d'élèves.", 'chn_abaya', '2023', 'France', "Le phénomène est très minoritaire.", 'etabli', '298'),
  fait("Le Conseil d'État a jugé l'interdiction des abayas conforme à la loi de 2004.", 'ce_abaya', '2024', 'France', "La loi permet déjà d'agir.", 'etabli'),
  fait("Selon la ministre, il y a eu 838 atteintes à la laïcité en septembre 2023 et 110 en septembre 2024.", 'ps_laic', '2023-2024', 'France', "Les signalements ont fortement baissé.", 'etabli', '838 puis 110'),
  fait("Des sénateurs estiment que les atteintes ne se limitent pas aux tenues (contestation d'enseignements, sport).", 'ps_laic', '2024', 'France', "D'autres atteintes existent.", 'interpretation'),
 ],
 court="Trompeur : les signalements ont bien doublé en 2022-2023, surtout à cause des abayas. Mais 298 élèves en abaya à la rentrée 2023, sur 12 millions, ce n'est pas une invasion. Après l'interdiction, les signalements sont retombés à 110 en septembre 2024.",
 moyen="La hausse a été réelle : 4 710 signalements en 2022-2023, deux fois plus qu'avant, en majorité pour des tenues comme l'abaya. Le Conseil d'État a validé leur interdiction.\n\nMais il faut les rapporter aux 12 millions d'élèves : 298 se sont présentées en abaya le jour de la rentrée 2023. Les signalements sont retombés à 110 en septembre 2024. La loi de 2004 fonctionne ; l'école n'est pas « envahie ».",
 detaille="Selon le Conseil d'État, les signalements d'atteintes à la laïcité à l'école sont passés de 2 167 en 2020-2021 et 2 226 en 2021-2022 à 4 710 en 2022-2023. Les tenues en représentent 1 984, contre 148 deux ans plus tôt, en majorité des abayas. Cette hausse, relayée par les réseaux sociaux, est documentée.\n\nÀ la rentrée 2023, le ministre a interdit l'abaya, et le Conseil d'État a jugé cette interdiction conforme à la loi de 2004. Le jour de la rentrée, 298 élèves se sont présentées en abaya, sur environ 12 millions. Les signalements sont tombés de 838 en septembre 2023 à 110 en septembre 2024.\n\nDes sénateurs rappellent que d'autres atteintes existent, comme la contestation de certains cours. Mais les chiffres montrent un phénomène minoritaire, que la loi permet de traiter. Présenter l'école comme envahie risque surtout de stigmatiser les élèves musulmans.",
 empathie="Je comprends que tu tiennes à une école laïque, à l'abri des pressions religieuses : c'est un principe essentiel. Justement, la loi de 2004 s'applique, et les chiffres montrent qu'elle fonctionne.",
 legitimes=["Les signalements ont doublé en 2022-2023.", "Le Conseil d'État retient une logique de contournement de la loi.", "D'autres atteintes que les tenues existent."],
 contre=[
  ("Les profs n'osent pas signaler.", "Les signalements dépendent en effet des consignes ; mais même une forte sous-déclaration ne transforme pas quelques milliers de cas en invasion."),
  ("La baisse prouve qu'il fallait interdire.", "C'est possible : la loi de 2004 le permettait déjà, ce qui montre que le cadre existant suffit."),
 ],
 questions=["Sais-tu combien d'élèves sont venues en abaya à la rentrée 2023 ?", "La laïcité protège-t-elle les élèves, ou sert-elle ici à viser une religion ?"],
 limites=["Le chiffre de 298 élèves provient d'un média étranger rapportant les propos du ministre.", "Aucun bilan détaillé 2024-2025 n'a été lu ; les signalements dépendent des consignes données aux personnels."],
 publics={'convaincus': "La hausse de 2022-2023 était réelle, et l'interdiction a été validée par le Conseil d'État. Mais on parle de 298 élèves en abaya sur 12 millions, et les signalements sont retombés à 110 en septembre 2024. La loi de 2004 marche : inutile d'en faire une guerre contre les musulmans.",
  'indecis': "Les atteintes à la laïcité ont augmenté en 2022-2023, puis fortement baissé après l'interdiction de l'abaya. Rapporté au nombre d'élèves, le phénomène reste très minoritaire. La laïcité à l'école est protégée par la loi, qui s'applique."},
 a_actualiser='2027-06-30', raison="Bilans annuels du ministère de l'Éducation nationale.",
))

# 19 ── Mineurs et transition de genre ─────────────────────────────────────────
FICHES.append(fiche(
 id='mineurs-transition-genre', affirmation="En France, on fait changer de sexe des enfants.", volet='droits', sous_theme='Droits des personnes LGBT',
 mots_cles=['changer de sexe', 'changement de sexe enfants', 'transition de genre mineurs', 'enfants trans', 'bloqueurs de puberte', 'operation de sexe', 'theorie du genre', 'transidentite'],
 verdict='trompeur', fiabilite='etabli',
 resume="Aucune chirurgie génitale n'est recensée chez les mineurs dans les données du Sénat. Des adolescents, quelques centaines, reçoivent des traitements (bloqueurs de puberté vers 14 ans, hormones vers 17 ans) après un suivi spécialisé, et quelques torsoplasties ont lieu à 16-17 ans. Le nombre de mineurs pris en charge a fortement augmenté, et les experts reconnaissent l'absence de consensus.",
 contexte="Le sujet circule à partir d'exemples étrangers et d'une proposition de loi sénatoriale de 2024 visant à interdire les traitements avant 18 ans.",
 explication="La transition peut être sociale (prénom, vêtements), médicale (bloqueurs de puberté, hormones) ou chirurgicale. Dans les données lues, les traitements médicaux concernent des adolescents suivis par des équipes hospitalières spécialisées.",
 sources=[SEN_TRANS, PS_TRANS, HAS_TRANS],
 faits=[
  fait("Sur 1 615 séjours hospitaliers codés « transsexualisme » en 2020, 48 concernaient des mineurs, dont aucun pour une chirurgie pelvienne.", 'sen_trans', '2020', 'France', "Aucune chirurgie génitale de mineur n'est recensée.", 'etabli', '0'),
  fait("En 2020, 294 mineurs étaient en affection de longue durée « transidentité », contre 8 en 2013.", 'ps_trans', '2013-2020', 'France', "Les effectifs sont faibles mais en forte hausse.", 'etabli', '294'),
  fait("Dans un service parisien de référence, sur 239 jeunes reçus entre 2012 et 2022, 11 % ont reçu des bloqueurs de puberté (âge moyen 13,9 ans), 44 % des hormones (âge moyen 16,9 ans) et 30 une torsoplastie (âge moyen 18,4 ans, le plus jeune 16 ans).", 'sen_trans', '2012-2022', 'Paris', "Des traitements existent, à l'adolescence, pas chez les enfants.", 'etabli'),
  fait("La Haute Autorité de santé a publié en 2025 des recommandations pour les adultes ; les mineurs font l'objet de travaux séparés.", 'has_trans', '2025', 'France', "Il n'existe pas encore de recommandation officielle pour les mineurs.", 'etabli'),
 ],
 court="Trompeur : aucune chirurgie génitale de mineur n'est recensée en France. Quelques centaines d'adolescents reçoivent des traitements, suivis par des équipes spécialisées. Leur nombre augmente, et le sujet mérite un débat médical serein.",
 moyen="Les traitements médicaux recensés concernent des adolescents suivis à l'hôpital : bloqueurs de puberté vers 14 ans en moyenne, hormones vers 17 ans. Sur 48 séjours hospitaliers de mineurs en 2020, aucun ne concernait une chirurgie génitale.\n\nLes effectifs ont fortement augmenté (294 mineurs en affection de longue durée en 2020, contre 8 en 2013), et la Haute Autorité de santé prépare des recommandations. C'est un débat médical légitime, qui n'a rien à voir avec l'image d'enfants opérés.",
 detaille="Selon le rapport du Sénat de 2024, 294 mineurs étaient en affection de longue durée pour transidentité en 2020, soit 3,3 % des bénéficiaires, contre 8 en 2013. Sur 1 615 séjours hospitaliers liés à la transidentité, 48 concernaient des mineurs, et aucun pour une chirurgie génitale.\n\nDans le service de référence de la Pitié-Salpêtrière, sur 239 jeunes reçus entre 2012 et 2022, 26 ont reçu des bloqueurs de puberté (âge moyen 13,9 ans), 105 des hormones (âge moyen 16,9 ans), et 30 une ablation des seins (torsoplastie), à 18,4 ans en moyenne, la plus jeune personne ayant 16 ans. Les chirurgies génitales n'y ont concerné que des majeurs.\n\nCes traitements existent et suscitent un vrai débat : la Haute Autorité de santé reconnaît l'absence de consensus pour les mineurs et y consacre des travaux à part. Une proposition de loi de la droite sénatoriale voulait interdire hormones et chirurgie avant 18 ans ; la gauche et les associations la jugent transphobe. On peut débattre de la prudence nécessaire sans faire croire qu'on opère des enfants.",
 empathie="C'est normal de s'inquiéter pour des adolescents qui prennent des décisions lourdes. Mais les données disponibles ne recensent aucune chirurgie génitale de mineur : les traitements concernent quelques centaines d'adolescents suivis par des équipes spécialisées.",
 legitimes=["Des traitements hormonaux et quelques torsoplasties concernent des mineurs.", "Le nombre de mineurs pris en charge a fortement augmenté.", "La Haute Autorité de santé reconnaît l'absence de consensus pour les mineurs."],
 contre=[
  ("C'est à cause de l'école et de la théorie du genre.", "Les sources lues ne montrent aucun lien ; la prise en charge médicale se fait dans des services hospitaliers spécialisés."),
  ("On opère des enfants de 10 ans.", "Dans le service de référence étudié par le Sénat, la plus jeune personne opérée (torsoplastie) avait 16 ans, et les chirurgies génitales n'ont concerné que des majeurs."),
 ],
 questions=["Sais-tu combien de mineurs ont eu une chirurgie génitale en France en 2020 ?", "Qui est le mieux placé pour fixer les règles : des autorités médicales, ou une loi générale ?"],
 limites=["Les données nationales sur les bloqueurs et les hormones chez les mineurs ne sont pas disponibles ; les chiffres détaillés viennent d'un seul service.", "Les données d'affection de longue durée datent de 2020."],
 publics={'convaincus': "En 2020, aucune chirurgie génitale de mineur n'a été recensée dans les séjours hospitaliers. Il s'agit de quelques centaines d'adolescents, suivis à l'hôpital, avec des traitements discutés entre médecins. On peut vouloir plus de prudence sans répandre des images fausses qui font souffrir ces jeunes et leurs familles.",
  'indecis': "La question des traitements chez les adolescents est un vrai débat médical, et la Haute Autorité de santé prépare des recommandations. Mais les chiffres montrent quelques centaines de jeunes concernés, aucune chirurgie génitale de mineur, et des traitements à l'adolescence. Les cas sont rares et encadrés."},
 a_actualiser='2027-12-31', raison="Recommandations attendues de la Haute Autorité de santé pour les mineurs.",
))

# 20 ── Uniforme ───────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='uniforme-ecole-discipline', affirmation="L'uniforme à l'école réglerait les problèmes de discipline.", volet='services', sous_theme='École publique',
 mots_cles=['uniforme', 'uniforme a l ecole', 'tenue unique', 'tenue scolaire unique', 'blouse', 'discipline a l ecole', 'autorite a l ecole'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Le bilan officiel de l'expérimentation française, publié en 2026, conclut à des effets « limités » sur le comportement et les apprentissages. Une grande étude américaine ne trouve aucun effet sur le comportement des élèves. Les chefs d'établissement sont plutôt satisfaits, mais une généralisation coûterait environ 2,4 milliards d'euros.",
 contexte="L'uniforme est défendu par le RN et une partie de la droite comme un symbole d'autorité ; une expérimentation a été lancée en 2024.",
 explication="L'expérimentation porte sur 115 établissements volontaires. L'évaluation repose surtout sur les déclarations des chefs d'établissement et des élèves, sans groupe de comparaison.",
 sources=[BDT_UNIF, AFP_UNIF, OSU_UNIF, UH_UNIF],
 faits=[
  fait("L'évaluation officielle conclut à des effets limités sur le comportement et les apprentissages ; dans le premier degré, 36 % des directeurs voient un effet positif sur le climat scolaire.", 'bdt_unif', '2024-2025', 'France, 115 établissements', "L'uniforme ne règle pas la discipline.", 'etabli', '36 %'),
  fait("57 % des écoliers n'aiment pas porter la tenue et 63 % des collégiens ne se sentent pas bien dedans ; 43 % des écoliers voient moins de moqueries sur les vêtements.", 'afp_unif', '2025', 'France', "Les élèves sont partagés.", 'etabli', '57 %'),
  fait("Une étude sur 6 320 élèves américains ne trouve aucun effet de l'uniforme sur l'anxiété, l'agressivité ou les compétences sociales.", 'osu_unif', '2021', 'États-Unis', "La recherche internationale ne montre pas d'effet sur le comportement.", 'etabli'),
  fait("Une étude plus ancienne sur un district de Houston trouve une amélioration de l'assiduité et du comportement au collège et au lycée.", 'uh_unif', '1993-2006', 'Houston', "Certaines études trouvent des effets modestes.", 'estimation'),
  fait("Une généralisation à 200 € par trousseau coûterait 2,4 milliards d'euros pour 12 millions d'élèves.", 'bdt_unif', '2026', 'France', "La mesure serait coûteuse.", 'estimation', '2,4 Md€'),
 ],
 court="Trompeur : l'évaluation officielle de l'expérimentation conclut à des effets « limités » sur le comportement. Une grande étude américaine ne trouve aucun effet. Et la généraliser coûterait environ 2,4 milliards d'euros.",
 moyen="L'expérimentation menée depuis 2024 dans 115 établissements a été évaluée par le ministère : les effets sur le comportement et les apprentissages sont limités. Les élèves sont partagés, et beaucoup n'aiment pas la tenue.\n\nLes études étrangères vont dans le même sens : une étude américaine sur plus de 6 000 élèves ne trouve aucun effet sur l'agressivité. Une généralisation coûterait environ 2,4 milliards.",
 detaille="L'expérimentation de la tenue scolaire unique porte sur 115 établissements volontaires (97 écoles, 14 collèges, 4 lycées), souvent en éducation prioritaire. Le bilan publié en mai 2026 par le service statistique du ministère conclut à des effets limités sur le comportement et les apprentissages. Dans le premier degré, 75 % des directeurs voient un effet positif sur le sentiment d'appartenance, mais 36 % seulement sur le climat scolaire.\n\nLes élèves sont partagés : 57 % des écoliers n'aiment pas la tenue, mais 43 % voient moins de moqueries sur les vêtements. Les chefs d'établissement du secondaire sont plus positifs et la plupart veulent continuer. L'évaluation repose surtout sur des déclarations, sans groupe de comparaison.\n\nAux États-Unis, une étude de l'université d'État de l'Ohio sur 6 320 élèves ne trouve aucun effet sur le comportement ; une étude plus ancienne à Houston trouvait des gains modestes d'assiduité. L'uniforme peut avoir un intérêt symbolique, mais les évaluations disponibles ne montrent pas qu'il règle la discipline.",
 empathie="Je comprends l'envie de retrouver de l'ordre à l'école, et l'idée que l'uniforme efface les différences de marques entre élèves. Mais les évaluations montrent qu'il change peu de choses à la discipline ; il faut chercher ailleurs les leviers.",
 legitimes=["Les chefs d'établissement du secondaire sont majoritairement positifs.", "43 % des écoliers voient moins de moqueries sur les vêtements.", "Une étude de Houston trouve des effets positifs sur l'assiduité."],
 contre=[
  ("Ça marche au Royaume-Uni.", "Aucune étude lue ne montre un effet de l'uniforme sur la discipline ; la grande étude américaine ne trouve rien."),
  ("Au moins, ça efface les inégalités.", "C'est un argument réel, mais l'effet sur les moqueries est partiel : 45 % des écoliers ne voient pas de changement."),
 ],
 questions=["Sais-tu ce qu'a conclu l'évaluation de l'expérimentation française ?", "Qu'est-ce qui améliore vraiment la discipline : un uniforme, ou plus d'adultes dans l'établissement ?"],
 limites=["Le rapport du ministère n'a été lu qu'à travers Localtis et l'AFP.", "L'évaluation repose sur des perceptions, sans groupe témoin ; les résultats de la deuxième année ne sont pas connus."],
 publics={'convaincus': "L'expérimentation voulue par le gouvernement a été évaluée : effets limités sur le comportement, et une majorité d'élèves qui n'aiment pas la tenue. Une grande étude américaine ne trouve aucun effet. Avant de dépenser 2,4 milliards en trousseaux, il faudrait des preuves que ça marche.",
  'indecis': "L'uniforme plaît à une partie des chefs d'établissement et réduit un peu les moqueries sur les vêtements. Mais l'évaluation française et la recherche étrangère ne montrent pas d'effet net sur la discipline. C'est un symbole, pas une solution."},
 a_actualiser='2027-06-30', raison="Bilan de la deuxième année d'expérimentation.",
))

# 21 ── Néonicotinoïdes ────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='neonicotinoides-agriculteurs', affirmation="Interdire les néonicotinoïdes comme l'acétamipride tue nos agriculteurs.", volet='ecologie', sous_theme='Pesticides',
 mots_cles=['neonicotinoides', 'acetamipride', 'loi duplomb', 'duplomb', 'pesticides interdits', 'noisette', 'betterave', 'tueurs d abeilles'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Certaines filières sont réellement en difficulté depuis l'interdiction de 2018, surtout la noisette et en partie la betterave et la pomme. Mais l'agriculture française n'est pas « tuée » : l'Anses a trouvé des alternatives pour la majorité des usages, et dans un réseau de 294 fermes suivies, seules 7 ont subi de lourdes pertes. En 2025, le Conseil constitutionnel a censuré la réintroduction de l'acétamipride au nom du droit à un environnement sain.",
 contexte="La loi Duplomb de 2025 voulait réautoriser l'acétamipride par dérogation ; une pétition contre la loi a réuni plus de 2,1 millions de signatures.",
 explication="Les néonicotinoïdes sont des insecticides très efficaces, mais toxiques pour les abeilles et les pollinisateurs. La France les a interdits en 2018, alors que l'UE autorise encore l'acétamipride jusqu'en 2033, d'où un sentiment de concurrence déloyale.",
 sources=[LCP_DUPLOMB, PS_ACETA, ANSES_NNI, INRAE_NNI],
 faits=[
  fait("Sur 130 usages examinés en 2018, l'Anses a trouvé des alternatives efficaces pour la majorité, mais aucune dans 6 cas ; il existe une alternative non chimique dans 78 % des cas.", 'anses_nni', '2018', 'France', "Les impasses existent, mais sont limitées.", 'etabli', '6 sur 130'),
  fait("Dans les fermes du réseau DEPHY, une année sans néonicotinoïdes a causé des pertes de 60 à 80 % sur 7 fermes sur 294 (2,4 %).", 'inrae_nni', '2025', 'France', "Les grosses pertes touchent une minorité de fermes.", 'etabli', '2,4 %'),
  fait("L'INRAE décrit la filière noisette comme au bord de la faillite et note une baisse du rendement de la betterave d'environ 5 t/ha depuis 2018, aux causes multiples.", 'inrae_nni', '2018-2025', 'France', "Certaines filières souffrent vraiment.", 'etabli'),
  fait("L'acétamipride reste autorisé dans l'UE jusqu'en 2033 ; en 2024, l'agence européenne a évoqué des « incertitudes majeures » sur ses effets neurodéveloppementaux, et ses effets sur les pollinisateurs sont documentés.", 'ps_aceta', '2024-2025', 'Union européenne', "Il y a un écart de règles, mais aussi des risques sanitaires.", 'etabli'),
  fait("Le Conseil constitutionnel a jugé la réintroduction de l'acétamipride contraire à la Charte de l'environnement en août 2025.", 'lcp_duplomb', '2025', 'France', "La réintroduction est impossible en l'état.", 'etabli'),
 ],
 court="Trompeur : des filières comme la noisette souffrent vraiment depuis 2018. Mais l'Anses a trouvé des alternatives pour la plupart des usages, et seules 7 fermes sur 294 suivies ont subi de lourdes pertes. Le Conseil constitutionnel a censuré la réintroduction au nom de la santé et de l'environnement.",
 moyen="L'interdiction de 2018 a créé de vraies difficultés pour quelques filières : la noisette surtout, et en partie la betterave et la pomme. Et l'acétamipride reste autorisé ailleurs en Europe, ce qui crée une concurrence déloyale.\n\nMais ce n'est pas toute l'agriculture : l'Anses a trouvé des alternatives pour la majorité des usages, et dans un réseau de 294 fermes, 7 ont eu de fortes pertes. Ses effets sur les pollinisateurs sont documentés et l'agence européenne relève des incertitudes sur la santé. La réponse, c'est d'aider les filières en impasse et d'imposer les mêmes règles à toute l'Europe.",
 detaille="La France a interdit les néonicotinoïdes en 2018. En 2025, la loi Duplomb a voulu réautoriser l'acétamipride par dérogation ; le Conseil constitutionnel l'a censuré, estimant que le législateur avait « privé de garanties légales le droit de vivre dans un environnement équilibré et respectueux de la santé ». Plus de 2,1 millions de personnes avaient signé une pétition contre la loi.\n\nLes difficultés agricoles sont réelles, mais ciblées. Selon l'INRAE, la filière noisette est au bord de la faillite, et le rendement de la betterave a baissé d'environ 5 tonnes par hectare depuis 2018, pour des causes multiples. Mais dans le réseau DEPHY, seules 7 fermes sur 294 ont subi des pertes de 60 à 80 %. L'Anses avait trouvé en 2018 des alternatives pour la majorité des 130 usages, et aucune dans 6 cas seulement.\n\nL'acétamipride reste autorisé dans l'UE jusqu'en 2033, ce qui crée un écart de concurrence. Mais l'agence européenne a relevé des « incertitudes majeures » sur ses effets sur le développement du cerveau, et ses effets sur les pollinisateurs sont documentés.",
 empathie="Je comprends le désespoir d'un producteur de noisettes qui voit sa récolte ravagée pendant que ses concurrents italiens utilisent un produit interdit en France. Cette injustice est réelle. Mais la réponse n'est pas de réautoriser un produit nocif pour les abeilles : c'est d'aider ces filières et d'harmoniser les règles en Europe.",
 legitimes=["La filière noisette est au bord de la faillite selon l'INRAE.", "L'acétamipride reste autorisé ailleurs dans l'UE, ce qui crée une concurrence déloyale.", "Aucune alternative isolée n'égale l'efficacité des néonicotinoïdes."],
 contre=[
  ("Les écolos préfèrent les abeilles aux paysans.", "La censure vient du Conseil constitutionnel, au nom du droit à un environnement sain ; et les effets de la molécule sur les pollinisateurs sont documentés par des chercheurs de l'INRAE."),
  ("Il n'y a aucune alternative.", "L'Anses en a trouvé pour la majorité des usages ; les impasses réelles concernent quelques filières, qu'il faut aider."),
 ],
 questions=["Sais-tu combien de fermes du réseau suivi par l'INRAE ont subi de lourdes pertes ?", "Ne faudrait-il pas plutôt interdire ces produits dans toute l'Europe ?"],
 limites=["Les données de l'Anses datent de 2018.", "Aucun chiffre de pertes pour la filière noisette n'a été lu.", "La décision du Conseil constitutionnel n'a été lue qu'à travers LCP."],
 publics={'convaincus': "Les producteurs de noisettes souffrent vraiment, et la concurrence de pays où le produit est autorisé est injuste. Mais sur 294 fermes suivies, 7 ont subi de lourdes pertes, et l'Anses a trouvé des alternatives pour la plupart des usages. Réautoriser un produit nocif pour les abeilles, avec des incertitudes sur la santé, n'est pas la seule réponse : des aides ciblées et des règles communes en Europe le sont aussi.",
  'indecis': "Certaines filières sont en vraie difficulté depuis l'interdiction, et leur colère est légitime. Mais l'agriculture dans son ensemble a trouvé des alternatives, et les risques pour la santé et les abeilles sont documentés. La solution passe par des aides ciblées et des règles communes en Europe."},
 a_actualiser='2027-06-30', raison="Évolution des autorisations européennes et des filières en impasse.",
))

# 22 ── Mégabassines ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='megabassines-agriculture', affirmation="Les mégabassines sont indispensables pour l'agriculture.", volet='ecologie', sous_theme='Agriculture',
 mots_cles=['megabassines', 'mega bassines', 'bassines', 'reserves de substitution', 'sainte soline', 'irrigation', 'marais poitevin', 'retenues d eau'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Les réserves de substitution sont un outil possible pour une partie des irrigants, sous conditions strictes, selon l'Académie d'agriculture elle-même. Elles ne concernent qu'une minorité d'agriculteurs, sont financées aux deux tiers par l'argent public, et plusieurs projets ont été annulés par la justice pour surdimensionnement ou volumes excessifs.",
 contexte="Les « mégabassines » des Deux-Sèvres et de la Vienne sont devenues un symbole du conflit sur l'eau, après les affrontements de Sainte-Soline en 2023.",
 explication="Une réserve de substitution pompe l'eau des nappes en hiver pour irriguer en été, afin de réduire les prélèvements pendant la sécheresse. Son intérêt dépend des volumes, de la gestion collective et du remplissage, qui pourrait devenir incertain avec le changement climatique.",
 sources=[AAF_BASS, BDT_BASS, AFP_BASS],
 faits=[
  fait("L'Académie d'agriculture présente les réserves comme « un des moyens » de mobiliser de l'eau, sous conditions : seuils de prélèvement, transition agroécologique et gestion collective.", 'aaf_bass', '2024', 'France', "Même leurs partisans posent des conditions.", 'etabli'),
  fait("Environ deux tiers du financement des réserves est public.", 'aaf_bass', '2024', 'France', "L'argent public doit servir l'intérêt général.", 'estimation', '2/3'),
  fait("Le modèle du BRGM montre un faible effet sur les débits et un effet positif sur les nappes en été ; mais certaines réserves pourraient ne pas se remplir certaines années avec le changement climatique.", 'aaf_bass', '2024', 'Deux-Sèvres', "L'effet existe mais reste incertain à l'avenir.", 'interpretation'),
  fait("En 2023, le tribunal administratif de Poitiers a annulé deux autorisations portant sur 15 réserves, relevant un « sur-dimensionnement du projet » et des volumes calculés sans tenir compte du changement climatique.", 'bdt_bass', '2023', 'Vienne', "Des projets ont été jugés illégaux.", 'etabli', '15 réserves'),
  fait("En 2025, la cour administrative d'appel de Bordeaux a jugé excessifs les volumes d'irrigation autorisés dans le Marais poitevin ; le projet de 16 retenues pour 450 agriculteurs coûte 78 M€, financé à moitié par l'État.", 'afp_bass', '2025', 'Marais poitevin', "Les bénéficiaires sont peu nombreux et le coût public élevé.", 'etabli', '78 M€'),
 ],
 court="Trompeur : même l'Académie d'agriculture n'y voit qu'« un des moyens », sous conditions strictes. Ces réserves servent une minorité d'irrigants, sont payées aux deux tiers par l'argent public, et plusieurs ont été annulées par la justice.",
 moyen="Les réserves de substitution peuvent soulager les nappes en été, selon le BRGM. Mais l'Académie d'agriculture pose des conditions : volumes limités, gestion collective, changement des pratiques.\n\nElles profitent à une minorité d'agriculteurs, avec deux tiers d'argent public. Dans le Marais poitevin, 16 retenues pour 450 agriculteurs coûtent 78 millions d'euros. La justice a annulé plusieurs projets surdimensionnés. Ce n'est pas l'agriculture en général qui en dépend, mais un modèle d'irrigation intensive.",
 detaille="Le principe est de pomper en hiver pour stocker l'eau et irriguer en été. Selon l'Académie d'agriculture, c'est « un des moyens » de mobiliser de l'eau, à condition de fixer des seuils de prélèvement, d'engager une transition agroécologique et d'organiser une gestion collective. Le modèle du BRGM montre un effet positif sur les nappes en été, mais avec le changement climatique, certaines réserves pourraient ne pas se remplir.\n\nCes projets coûtent cher et profitent à peu d'agriculteurs : environ deux tiers du financement est public, et dans le Marais poitevin, 16 retenues pour 450 agriculteurs coûtent 78 millions d'euros. La justice a annulé en 2023 deux autorisations portant sur 15 réserves, jugées surdimensionnées, et a confirmé en 2025 la réduction des prélèvements d'environ un quart.\n\nLes irrigants qui en dépendent redoutent une catastrophe économique, et leur inquiétude est réelle. Le débat porte sur le partage d'une ressource commune : qui a droit à l'eau, pour quelles cultures, et qui paie.",
 empathie="Je comprends l'angoisse d'un agriculteur qui voit ses cultures sécher et qui a besoin d'eau l'été. Mais ces réserves profitent à une minorité, avec beaucoup d'argent public ; la question est de partager l'eau entre tous.",
 legitimes=["Le BRGM montre un effet positif sur les nappes en été.", "Les irrigants concernés redoutent de graves difficultés économiques."],
 contre=[
  ("Sans bassines, pas de nourriture.", "Les réserves ne concernent qu'une partie des irrigants ; la plupart des agriculteurs n'en bénéficient pas."),
  ("Ce sont des écoterroristes qui s'y opposent.", "Les annulations viennent de tribunaux administratifs, qui ont jugé des volumes excessifs et des projets surdimensionnés."),
 ],
 questions=["Sais-tu combien d'agriculteurs bénéficient des retenues du Marais poitevin ?", "Qui doit décider du partage de l'eau en période de sécheresse ?"],
 limites=["La part totale des agriculteurs bénéficiaires n'a pas été chiffrée par une source lue.", "Le jugement validant la réserve de Sainte-Soline n'a pas été lu.", "L'expertise de 2016 sur les retenues ne traitait pas spécifiquement des réserves de substitution."],
 publics={'convaincus': "Les bassines ne servent pas « l'agriculture » mais une minorité d'irrigants : dans le Marais poitevin, 450 agriculteurs pour 78 millions d'euros, à moitié payés par l'État. Ce sont des tribunaux, pas des militants, qui ont jugé plusieurs projets surdimensionnés. L'eau est un bien commun à partager entre tous les paysans.",
  'indecis': "Les réserves peuvent aider certains agriculteurs pendant les sécheresses, et leur inquiétude est légitime. Mais l'Académie d'agriculture elle-même pose des conditions strictes, et la justice a annulé des projets trop gros. Le vrai débat porte sur le partage de l'eau et l'usage de l'argent public."},
 a_actualiser='2027-06-30', raison="Décisions de justice et bilans des réserves existantes.",
))

# 23 ── LFI pro-Poutine ────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='lfi-pro-poutine', affirmation="LFI est pro-Poutine.", volet='politique', sous_theme='France insoumise',
 mots_cles=['lfi pro poutine', 'insoumis pro poutine', 'melenchon poutine', 'lfi russie', 'lfi ukraine', 'vote ukraine assemblee', 'lfi otan'],
 verdict='trompeur', fiabilite='interpretation',
 resume="LFI a condamné l'invasion de l'Ukraine et imputé à Vladimir Poutine la « totale responsabilité » de la guerre. Mais elle a voté contre l'accord de sécurité avec l'Ukraine en 2024 et contre une résolution de soutien en 2025, s'oppose aux livraisons d'armes et veut sortir de l'OTAN. C'est une ligne non alignée, contestée y compris à gauche, pas un soutien à Poutine.",
 contexte="L'accusation vient aussi bien de la droite et du centre que d'une partie de la gauche ; elle est aussi utilisée par le RN, lui-même accusé de liens avec la Russie.",
 explication="LFI défend une politique étrangère « non alignée » : refus de l'OTAN, priorité à la diplomatie, opposition à l'élargissement de l'UE. Ses adversaires y voient une complaisance envers Moscou.",
 sources=[AN_UKR22, DFI_UKR, LCP_UKR, PS_UKR],
 faits=[
  fait("Le 1er mars 2022, à l'Assemblée, Jean-Luc Mélenchon impute au gouvernement de Vladimir Poutine la totale responsabilité de la guerre, tout en plaidant pour la diplomatie et contre les livraisons d'armes.", 'an_ukr22', '2022', 'France', "LFI a condamné l'agression.", 'etabli'),
  fait("Au Parlement européen, la délégation LFI a voté la condamnation de l'agression russe et la résolution finale, mais contre les livraisons d'armes, le renforcement de l'OTAN et l'adhésion accélérée de l'Ukraine à l'UE.", 'dfi_ukr', '2022', 'Union européenne', "Le vote est nuancé.", 'etabli'),
  fait("En mars 2024, l'accord de sécurité France-Ukraine a été approuvé par 372 voix contre 99 ; LFI et le PCF ont voté contre, le RN s'est abstenu.", 'lcp_ukr', '2024', 'France', "LFI a voté plus durement que le RN contre ce texte.", 'etabli', '372 contre 99'),
  fait("En mars 2025, LFI a voté contre une résolution de soutien à l'Ukraine, en raison de l'adhésion de l'Ukraine à l'UE qu'elle encourageait.", 'ps_ukr', '2025', 'France', "L'opposition de LFI porte surtout sur l'élargissement de l'UE et l'armement.", 'etabli'),
 ],
 court="Trompeur : LFI a condamné l'invasion et désigné Poutine comme seul responsable. Mais elle vote contre les textes de soutien militaire à l'Ukraine et veut sortir de l'OTAN. C'est une ligne non alignée contestable, pas un soutien à Poutine.",
 moyen="Dès 2022, Jean-Luc Mélenchon a déclaré que le gouvernement de Poutine portait « la totale responsabilité » de la guerre. LFI a voté la condamnation de l'agression au Parlement européen.\n\nMais LFI s'oppose aux livraisons d'armes, à l'OTAN et à l'adhésion rapide de l'Ukraine à l'UE, et a voté contre l'accord de sécurité de 2024. On peut contester cette ligne ; la qualifier de « pro-Poutine » efface sa condamnation explicite de l'agression.",
 detaille="Le 1er mars 2022, à l'Assemblée nationale, Jean-Luc Mélenchon affirme que le gouvernement de Vladimir Poutine porte « la totale responsabilité » de la guerre. Au Parlement européen, les eurodéputés LFI votent la condamnation de l'agression et la résolution finale.\n\nLFI défend en revanche une ligne non alignée : sortie de l'OTAN, priorité à la diplomatie, refus des livraisons d'armes, opposition à une adhésion rapide de l'Ukraine à l'UE. Elle a voté contre l'accord de sécurité France-Ukraine en 2024, alors que le RN s'abstenait, et contre une résolution de soutien en 2025. Ces votes nourrissent les critiques, y compris à gauche.\n\nLe débat est donc légitime : une politique de paix sans armer l'Ukraine est-elle réaliste face à une invasion ? Mais confondre cette ligne avec un soutien à Poutine est inexact. Et l'accusation est souvent portée par le RN, dont les liens avec la Russie sont documentés par ailleurs.",
 empathie="Je comprends que les votes de LFI contre certains textes de soutien à l'Ukraine choquent. On peut les critiquer. Mais LFI a condamné clairement l'invasion russe ; sa position, c'est la diplomatie plutôt que les armes, pas un soutien à Poutine.",
 legitimes=["LFI a voté contre l'accord de sécurité de 2024 et la résolution de 2025.", "Elle s'oppose aux livraisons d'armes à l'Ukraine.", "Sa ligne est critiquée par d'autres partis de gauche."],
 contre=[
  ("Refuser d'armer l'Ukraine, c'est aider Poutine.", "C'est la critique principale, et elle se discute ; mais LFI a condamné l'agression et désigné Poutine comme responsable."),
  ("Mélenchon a toujours défendu la Russie.", "En 2022, il a imputé au gouvernement russe la totale responsabilité de la guerre ; ses positions sur l'OTAN sont plus anciennes."),
 ],
 questions=["Sais-tu ce qu'a dit Mélenchon à l'Assemblée le 1er mars 2022 ?", "Peut-on condamner une invasion tout en refusant d'envoyer des armes ?"],
 limites=["Les votes de LFI au Parlement européen après 2022 n'ont pas été vérifiés.", "Les citations du compte rendu de 2022 sont restituées par un outil de lecture et pourraient être revérifiées mot à mot."],
 publics={'convaincus': "Mélenchon a dit dès mars 2022 que Poutine portait la totale responsabilité de la guerre. LFI refuse d'armer l'Ukraine et veut quitter l'OTAN : on peut le contester. Mais en 2024, sur l'accord avec l'Ukraine, c'est le RN qui s'est abstenu, et ses liens avec la Russie sont documentés.",
  'indecis': "LFI a condamné l'invasion russe, mais elle vote contre l'aide militaire à l'Ukraine et l'adhésion rapide à l'UE. Cette ligne pacifiste est critiquée, y compris à gauche. Ce n'est pas un soutien à Poutine, mais une divergence sur les moyens."},
 a_actualiser='2027-06-30', raison="Nouveaux votes parlementaires sur l'Ukraine.",
))

# 24 ── RN et binationaux ─────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-binationaux-postes', affirmation="Le RN veut interdire certains postes aux binationaux.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['binationaux', 'double nationalite', 'rn binationaux', 'bardella binationaux', 'postes strategiques', 'emplois sensibles', 'francais de papier'],
 verdict='confirme', fiabilite='etabli',
 resume="Oui : le programme législatif du RN de 2024 prévoyait d'exclure les Français binationaux d'une cinquantaine de postes « les plus stratégiques de l'État », dans la sécurité et la défense. Une proposition de loi constitutionnelle du RN de janvier 2024 visait plus large. Pour une juriste, distinguer les Français selon leur nationalité rompt le principe d'égalité, et des contrôles au cas par cas existent déjà.",
 contexte="La mesure a fait polémique pendant la campagne des législatives de 2024, quand un député RN a jugé qu'une ancienne ministre binationale n'aurait pas dû être nommée.",
 explication="Un binational est pleinement français. Les emplois de souveraineté sont déjà réservés aux Français, binationaux compris, et l'accès aux postes sensibles passe par des habilitations de sécurité individuelles.",
 sources=[PS_BINAT, LCP_BINAT, INED_BINAT],
 faits=[
  fait("En juin 2024, Jordan Bardella annonce vouloir « réserver un certain nombre d'emplois stratégiques dans les secteurs notamment liés à la sécurité et à la défense ».", 'ps_binat', '2024', 'France', "La mesure figure bien dans le projet du RN.", 'etabli'),
  fait("Le programme du RN prévoit d'exclure les binationaux d'une cinquantaine de postes « les plus stratégiques de l'État », hors mandats électifs et fonctions ministérielles selon le parti.", 'lcp_binat', '2024', 'France', "Le périmètre annoncé est restreint.", 'etabli', 'une cinquantaine'),
  fait("La proposition de loi constitutionnelle du RN de janvier 2024 visait à interdire aux binationaux l'accès à des emplois dans l'administration.", 'ps_binat', '2024', 'France', "Le projet initial était plus large.", 'etabli'),
  fait("Une juriste estime que distinguer les Français selon leur mode d'acquisition de la nationalité romprait avec le principe d'égalité ; des habilitations permettent déjà un filtrage au cas par cas.", 'ps_binat', '2024', 'France', "La mesure est juridiquement fragile et peu utile.", 'interpretation'),
  fait("En 2009, les binationaux représentaient 5 % de la population de 18 à 50 ans et près du quart des enfants d'immigrés.", 'ined_binat', '2008-2009', 'France', "La mesure vise d'abord des enfants d'immigrés.", 'etabli', '5 %'),
 ],
 court="Vrai : le RN voulait en 2024 réserver une cinquantaine de postes « stratégiques » aux Français sans autre nationalité. Une juriste y voit une rupture d'égalité entre Français, alors que des contrôles individuels existent déjà.",
 moyen="Le programme du RN pour les législatives de 2024 prévoyait d'exclure les binationaux d'une cinquantaine de postes stratégiques, dans la défense et la sécurité. Une proposition de loi de janvier 2024 allait plus loin.\n\nUn binational est pleinement français. Les postes sensibles exigent déjà une habilitation de sécurité, accordée au cas par cas. La mesure créerait des Français de seconde zone, en visant notamment des enfants d'immigrés.",
 detaille="Le 24 juin 2024, Jordan Bardella annonce vouloir réserver certains emplois stratégiques, liés à la sécurité et à la défense, aux Français n'ayant pas d'autre nationalité. Selon le RN, une cinquantaine de postes seraient concernés, hors mandats électifs et fonctions ministérielles. Une proposition de loi constitutionnelle déposée en janvier 2024 visait plus largement les emplois dans l'administration.\n\nPendant la campagne, un député RN a jugé que des binationaux ne devraient pas être ministres ; Marine Le Pen l'a désavoué. Le périmètre annoncé est donc limité, mais le principe reste le même : distinguer les Français selon leurs origines.\n\nSelon une juriste interrogée par Public Sénat, cela romprait avec le principe d'égalité et ne passerait pas le Conseil constitutionnel. Les emplois de souveraineté sont déjà réservés aux Français, et les habilitations de sécurité permettent un filtrage individuel. En 2009, les binationaux représentaient 5 % des 18-50 ans et près du quart des enfants d'immigrés : la mesure les soupçonne collectivement.",
 empathie="Je comprends le souci de protéger les postes sensibles de l'État. Mais ces postes exigent déjà une enquête individuelle. Exclure tous les binationaux, c'est soupçonner des Français pour leurs origines.",
 legitimes=["Le périmètre annoncé en 2024 était restreint à une cinquantaine de postes.", "Le RN a désavoué l'idée d'exclure les binationaux des fonctions ministérielles.", "La sécurité des postes sensibles est une préoccupation légitime."],
 contre=[
  ("Un binational peut avoir une double loyauté.", "Les postes sensibles exigent déjà une habilitation individuelle ; la loyauté se vérifie personne par personne, pas par catégorie."),
  ("Ce n'est qu'une cinquantaine de postes.", "Le principe compte : créer deux catégories de Français. Et la proposition de loi de janvier 2024 allait beaucoup plus loin."),
 ],
 questions=["Sais-tu que les postes sensibles exigent déjà une habilitation de sécurité individuelle ?", "Un Français né en France d'un parent étranger est-il moins français que toi ?"],
 limites=["Le texte même du programme RN et de la proposition de loi constitutionnelle n'a pas été lu.", "Le nombre actuel de binationaux n'a pas été vérifié ; le chiffre lu date de 2009.", "Le Conseil constitutionnel ne s'est pas prononcé sur cette mesure."],
 publics={'convaincus': "Les postes sensibles exigent déjà une habilitation, accordée après enquête individuelle. Exclure tous les binationaux, c'est dire à des Français, souvent enfants d'immigrés, qu'ils sont suspects par naissance. Même Marine Le Pen a dû désavouer un député qui voulait aller plus loin.",
  'indecis': "La mesure figurait bien dans le programme du RN en 2024, limitée à une cinquantaine de postes. Mais des contrôles individuels existent déjà, et une juriste y voit une rupture d'égalité entre Français. La question est de savoir si l'on juge les gens sur leurs actes ou sur leurs origines."},
 a_actualiser='2027-06-30', raison="Programme du RN pour 2027.",
))

# 25 ── LFI et la VIe République ───────────────────────────────────────────────
FICHES.append(fiche(
 id='lfi-sixieme-republique', affirmation="LFI veut une VIe République.", volet='politique', sous_theme='France insoumise',
 mots_cles=['sixieme republique', '6e republique', 'vie republique', 'assemblee constituante', 'constituante', 'revocation des elus', 'nouvelle constitution'],
 verdict='confirme', fiabilite='etabli',
 resume="Oui : le programme de LFI de 2022 et celui du Nouveau Front populaire de 2024 prévoient de passer à une VIe République par une assemblée constituante, avec la proportionnelle, le référendum d'initiative citoyenne, la révocation des élus et l'abrogation du 49.3. La nouvelle Constitution serait soumise à référendum. Ce n'est pas une prise de pouvoir, mais une procédure démocratique, dont certaines modalités sont discutées.",
 contexte="L'idée est souvent présentée comme une menace pour les institutions ; elle répond à la crise de confiance envers la Ve République.",
 explication="Une assemblée constituante est élue (ou en partie tirée au sort) pour rédiger une nouvelle Constitution, qui est ensuite soumise au vote des citoyens. LFI veut ainsi passer d'un régime présidentiel à un régime parlementaire.",
 sources=[AEC_PROG, NFP_PROG, PS_RIC],
 faits=[
  fait("Le programme L'Avenir en commun prévoit de « Convoquer une Assemblée constituante par un référendum (article 11 de la Constitution) », dont les membres seraient élus ou tirés au sort, puis de soumettre la nouvelle Constitution à référendum.", 'aec_prog', '2022', 'France', "La VIe République passe par le vote des citoyens.", 'etabli'),
  fait("Le programme prévoit un régime parlementaire, la proportionnelle, le référendum d'initiative citoyenne, y compris pour révoquer les élus, le droit de vote à 16 ans et la reconnaissance du vote blanc.", 'aec_prog', '2022', 'France', "Le projet vise à donner plus de pouvoir aux citoyens.", 'etabli'),
  fait("Le programme du NFP de 2024 prévoit d'« Abolir la monarchie présidentielle dans la pratique des institutions », d'« Instaurer la proportionnelle » et d'« Abroger le 49.3 ».", 'nfp_prog', '2024', 'France', "Toute la gauche unie a repris l'objectif.", 'etabli'),
  fait("En 2019, la proposition de loi constitutionnelle de LFI sur le référendum d'initiative citoyenne a été écartée par 91 voix contre 50 ; la majorité jugeait trop bas le seuil de 2 % des électeurs.", 'ps_ric', '2019', 'France', "Les modalités du RIC sont critiquées.", 'etabli', '2 %'),
 ],
 court="Vrai : LFI et le programme du NFP veulent une VIe République, rédigée par une assemblée constituante et adoptée par référendum. Le but est de passer à un régime parlementaire, avec la proportionnelle et le référendum d'initiative citoyenne.",
 moyen="C'est assumé : le programme de LFI prévoit de convoquer par référendum une assemblée constituante, élue ou tirée au sort, puis de faire voter la nouvelle Constitution par les citoyens. Le programme du NFP reprend l'idée.\n\nLe projet : fin de la « monarchie présidentielle », proportionnelle, référendum d'initiative citoyenne, révocation des élus, suppression du 49.3. On peut discuter de ces choix, notamment du seuil du RIC. Mais il s'agit de changer de Constitution par le vote, pas de renverser les institutions.",
 detaille="Le programme L'Avenir en commun (2022) prévoit de « Convoquer une Assemblée constituante par un référendum », en s'appuyant sur l'article 11 de la Constitution. Ses membres seraient élus ou tirés au sort, et la nouvelle Constitution serait soumise à référendum. Le programme du Nouveau Front populaire de 2024 reprend l'objectif d'une VIe République et d'en finir avec la « monarchie présidentielle ».\n\nLes propositions sont précises : régime parlementaire, proportionnelle, référendum d'initiative citoyenne pour proposer ou abroger une loi, modifier la Constitution ou révoquer un élu, vote à 16 ans, reconnaissance du vote blanc, abrogation du 49.3.\n\nCes propositions sont discutables. En 2019, la majorité de l'époque jugeait trop bas le seuil de 2 % des électeurs pour déclencher un RIC, et le recours à l'article 11 pour convoquer une constituante fait débat. Mais l'idée de VIe République est une procédure démocratique de changement de Constitution, comme la France en a connu plusieurs.",
 empathie="Je comprends qu'on puisse s'inquiéter de changer les règles du jeu. Mais le projet de LFI prévoit que ce soient les citoyens qui votent la nouvelle Constitution, par référendum : rien ne se fait sans eux.",
 legitimes=["Le seuil de 2 % pour le RIC a été jugé trop bas.", "Le recours à l'article 11 pour convoquer une constituante est juridiquement discuté."],
 contre=[
  ("C'est un projet pour prendre le pouvoir.", "La nouvelle Constitution serait rédigée par une assemblée élue ou tirée au sort, puis soumise à référendum."),
  ("La Ve République fonctionne très bien.", "C'est un choix ; LFI et le NFP estiment qu'elle concentre trop de pouvoir dans les mains du président."),
 ],
 questions=["Sais-tu comment LFI propose d'adopter la nouvelle Constitution ?", "Les citoyens devraient-ils pouvoir révoquer un élu en cours de mandat ?"],
 limites=["Aucune analyse de constitutionnaliste n'a été lue.", "Le programme de 2027 n'a pas été vérifié ; les sources principales sont des programmes partisans."],
 publics={'convaincus': "Le projet de LFI, c'est une Constitution rédigée par une assemblée élue ou tirée au sort, puis votée par tous les Français. Avec le RIC, tu pourrais toi-même proposer une loi ou révoquer un élu. Qu'est-ce qui est dangereux dans le fait de donner plus de pouvoir au peuple ?",
  'indecis': "LFI et le NFP veulent bien une VIe République, avec un régime parlementaire, la proportionnelle et le référendum d'initiative citoyenne. Certaines modalités sont discutées, comme le seuil du RIC. Mais la démarche passe par le vote des citoyens."},
 a_actualiser='2027-06-30', raison="Programmes de 2027.",
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
