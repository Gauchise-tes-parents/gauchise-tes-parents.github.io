"""Fiches quotidiennes du 8 novembre 2026, passage de 06 h 13 (UTC) — phase alpha.

25 questions qui circulent (extrême droite, clichés sur la gauche, programmes) et qui n'avaient pas de fiche
qui leur réponde vraiment. Toutes les sources ont été ouvertes et lues le 8 novembre 2026 (consultee=True) ;
les chiffres viennent uniquement des passages cités. Données anciennes signalées dans les limites.
Chaque fiche contient les réponses selon le public (« publics » : électeur d'extrême droite convaincu / indécis).
Usage : python3 scripts/fiches/quotidien_20261108_0613.py  (puis node scripts/corrections-v10.js et node scripts/enrichir-fiches.js)
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

# ── Sources : immigration, Europe, aide au développement ─────────────────────
INED_RF = ('ined_rf', src("Cinquante ans de regroupement familial : une voie d'entrée sur le territoire désormais plus rare (Population & Sociétés n° 643)", "Ined (Julia Descamps)", "avril 2026",
  "https://www.ined.fr/sites/default/files/2026-04/643F.pdf",
  "Entre 2000 et 2023, le regroupement familial a donné lieu en moyenne à environ 11 000 premiers titres par an, contre 20 000 à 32 000 entre 1987 et 1992. En 2023, 12 885 titres ont été délivrés, soit 5 % des premiers titres d'au moins un an (11 % en 2000). Au sens large, l'immigration familiale représente 81 032 titres en 2023, soit 31 % des premières délivrances ; elle inclut les familles de Français et les « liens personnels et familiaux ». Le SMIC est exigé depuis 1993 hors prestations familiales, des critères de logement existent depuis 1999 ; en 2023, 15 780 demandes, 82 % d'acceptation, refus surtout pour ressources (11 %) et logement (3 %).",
  "Publication scientifique d'un institut public de recherche (données jusqu'en 2023)."))
HERAN_VC = ('heran_vc', src("Vérités et contrevérités sur l'immigration", "François Héran (Collège de France, Institut Convergences Migrations / CNRS)", "2 novembre 2023",
  "https://icmigrations.cnrs.fr/wp-content/uploads/2023/11/Immigration-et-projet-de-loi-Darmanin_Verites-contreverites_Heran-02-11-2023.pdf",
  "Le regroupement familial concerne « 12 à 14 000 personnes par an » ; l'auteur reproche de le confondre avec la migration familiale globale, d'environ 85 000 personnes par an. Selon l'enquête ELIPA, environ 40 % des premiers titres familiaux concernent des personnes entrées en France depuis au moins neuf ans.",
  "Synthèse d'un démographe du Collège de France.", 'etude'))
PS_RF = ('ps_rf', src("Loi immigration : comment le Sénat veut limiter le regroupement familial", "Public Sénat (Simon Barbarit)", "31 octobre 2023",
  "https://www.publicsenat.fr/actualites/politique/loi-immigration-comment-le-senat-veut-limiter-le-regroupement-familial",
  "Conditions en vigueur : 18 mois de séjour régulier, des ressources « stables et suffisantes » évaluées sur la moyenne du SMIC des 12 derniers mois, un logement « normal » pour une famille comparable de la même région ; les ascendants sont exclus. Titres délivrés : 12 149 en 2018, 10 041 en 2020 et 14 314 en 2021. Les sénateurs jugent que l'immigration en France « demeure une immigration largement familiale ».",
  "Média parlementaire.", 'media'))
PS_TITRES = ('ps_titres', src("Immigration : titres de séjour en nette hausse et régularisations en baisse sur l'année 2025", "Public Sénat (Romain David, avec l'AFP)", "27 janvier 2026",
  "https://www.publicsenat.fr/actualites/societe/immigration-titres-de-sejour-en-nette-hausse-et-regularisations-en-baisse-sur-lannee-2025",
  "D'après la direction générale des étrangers en France, 384 230 premiers titres ont été délivrés en 2025 (+11,2 %). Le motif étudiant arrive en tête (118 000), devant l'humanitaire (92 600) et l'économique (51 190).",
  "Média parlementaire reprenant la statistique publique.", 'media'))
LCP_LEPEN22 = ('lcp_lepen22', src("Présidentielle : l'immigration, figure imposée, mais pas thème central de la campagne", "LCP (Raphaël Marchal)", "28 mars 2022",
  "https://lcp.fr/actualites/presidentielle-l-immigration-figure-imposee-mais-pas-theme-central-de-la-campagne-107256",
  "Marine Le Pen réclame, comme Éric Zemmour, la fin du regroupement familial. Elle propose une révision constitutionnelle par référendum, avec une « priorité nationale », pour permettre des mesures actuellement « inapplicables en raison de la Constitution ».",
  "Média parlementaire.", 'media'))
AN_PPLC_RN = ('an_pplc_rn', src("Proposition de loi constitutionnelle Citoyenneté-Identité-Immigration (n° 2120)", "Assemblée nationale (texte déposé par Marine Le Pen et les députés du groupe RN)", "25 janvier 2024",
  "https://www.assemblee-nationale.fr/dyn/16/textes/l16b2120_proposition-loi.pdf",
  "L'article 1er crée un article 4-1 de la Constitution : « Le regroupement familial des étrangers peut être limité ou interdit. » Le texte prévoit aussi que « Toute juridiction doit, le cas échéant, laisser inappliquées » les règles internationales contraires à la Constitution, et qu'un acte de l'Union européenne jugé contraire « ne peut produire d'effets en droit national ».",
  "Texte parlementaire du RN, cité pour décrire sa position."))
LCP_RN24 = ('lcp_rn24', src("Législatives 2024 : le programme du Rassemblement national en matière d'immigration à l'épreuve de la Constitution", "LCP (Raphaël Marchal)", "28 juin 2024",
  "https://lcp.fr/actualites/legislatives-2024-le-programme-du-rassemblement-national-en-matiere-d-immigration-a-l",
  "Le programme de 2024 évoque un « durcissement des conditions du regroupement familial », par une loi ordinaire. Des mesures similaires avaient été censurées début 2024 comme « cavaliers législatifs », pour une raison de forme.",
  "Média parlementaire.", 'media'))
UT_9325 = ('ut_9325', src("Décision n° 93-325 DC du 13 août 1993 (traduction anglaise)", "University of Texas at Austin, Foreign Law Translations", "décision de 1993",
  "https://law.utexas.edu/transnational/foreign-law-translations/french/case.php?id=1004",
  "Le Conseil constitutionnel cite le 10e alinéa du Préambule de 1946 et juge que les étrangers « have the right to lead a normal family life in the same way as French nationals », ce qui leur permet de faire venir leur conjoint et leurs enfants mineurs, sous réserve de restrictions liées à l'ordre public et à la santé publique.",
  "Traduction universitaire d'une décision du Conseil constitutionnel.", 'secondaire'))
EU_DIR = ('eu_dir', src("Directive 2003/86/CE du Conseil du 22 septembre 2003 relative au droit au regroupement familial", "Union européenne (EUR-Lex)", "22 septembre 2003",
  "https://eur-lex.europa.eu/eli/dir/2003/86/oj/eng",
  "Selon l'article 4, les États « shall authorise » l'entrée du conjoint et des enfants mineurs du regroupant. L'article 7 permet d'exiger un logement normal, une assurance maladie et des ressources « stable and regular » ; l'article 8 autorise un délai de séjour préalable « not exceeding two years ».",
  "Texte juridique de l'Union européenne."))
CAMPUS_25 = ('campus_25', src("Mobilité étudiante : la France consolide son attractivité dans un contexte de forte concurrence (Chiffres clés 2025)", "Campus France", "20 mai 2025",
  "https://www.campusfrance.org/system/files/medias/documents/2025-05/CP_Chiffres_cles_2025_FR_vdef.pdf",
  "Plus de 430 000 étudiants étrangers étaient en France en 2023-2024, en hausse de 21 % sur cinq ans, soit moins vite que la moyenne mondiale. La France est le septième pays d'accueil. Origines : Afrique du Nord-Moyen-Orient 28 %, Europe 25 %, Afrique subsaharienne 25 %.",
  "Établissement public chargé de la promotion de l'enseignement supérieur français, partie prenante.", 'secondaire'))
OCDE_ETU = ('ocde_etu', src("Rétention des étudiants internationaux et répercussions économiques dans l'OCDE (Perspectives des migrations internationales 2022)", "OCDE (Elisabeth Kamm, Thomas Liebig)", "2022",
  "https://www.oecd.org/fr/publications/perspectives-des-migrations-internationales-2022_7244fc44-fr/full-report/component-11.html",
  "Pour la cohorte des premiers titres étudiants de 2015, environ 43 % étaient encore en France cinq ans après, contre environ 30 % en moyenne OCDE. En 2019, les changements de statut d'anciens étudiants représentaient 52 % des admissions pour motif professionnel en France ; plus de trois sur quatre passent vers un titre de travail. Dix ans après un premier titre étudiant obtenu en 2010, 10 % des titulaires avaient un titre familial.",
  "Organisation internationale (données 2015-2020)."))
CAMPUS_ECO = ('campus_eco', src("Les étudiants internationaux : un apport de 5 milliards d'euros à l'économie française", "Campus France, avec Kantar Public", "28 novembre 2022",
  "https://www.campusfrance.org/system/files/medias/documents/2022-11/CP%20Impact%20%C3%A9conomique%20des%20%C3%A9tudiants%20internationaux%20en%20France.pdf",
  "L'étude, menée auprès de 10 000 étudiants, évalue leur apport à 5 Md€ et le coût public à environ 3,1 Md€ de dépenses d'enseignement supérieur, plus les aides au logement, la sécurité sociale et les bourses ; elle en tire « un apport net de 1,35 milliard d'euros ».",
  "Étude commandée par un opérateur public partie prenante.", 'secondaire'))
MESR_BEF = ('mesr_bef', src("« Bienvenue en France » : la stratégie d'attractivité pour les étudiants internationaux", "Ministère de l'Enseignement supérieur et de la Recherche", "8 avril 2019",
  "https://www.enseignementsup-recherche.gouv.fr/fr/bienvenue-en-france-la-strategie-d-attractivite-pour-les-etudiants-internationaux-49178",
  "Depuis la rentrée 2019, les droits différenciés pour les étudiants extra-européens sont de « 2 770€ en licence » et « 3 770€ en master », soit « moins du tiers du coût réel de la formation ».",
  "Source gouvernementale (2019)."))
CE_SCHENGEN = ('ce_schengen', src("Le rétablissement du contrôle aux frontières intérieures est conforme au nouveau règlement « Schengen » (décision n° 499702)", "Conseil d'État", "7 mars 2025",
  "https://conseil-etat.fr/actualites/le-retablissement-du-controle-aux-frontieres-interieures-est-conforme-au-nouveau-reglement-schengen",
  "Après les attentats de novembre 2015, la France a rétabli des contrôles aux frontières avec les États Schengen, « reconduit tous les six mois » sans interruption. Le Conseil d'État valide la décision du 4 octobre 2024 (contrôles du 1er novembre 2024 au 30 avril 2025), justifiée par le risque terroriste et les réseaux de passeurs, et rejette le recours des associations.",
  "Juridiction administrative suprême."))
CE_NOTIF = ('ce_notif', src("Temporary reintroduction of border control", "Commission européenne, DG Migration et affaires intérieures", "page consultée le 8 novembre 2026",
  "https://home-affairs.ec.europa.eu/policies/schengen/schengen-area/temporary-reintroduction-border-control_en",
  "Les contrôles intérieurs sont une « measure of last resort » : jusqu'à six mois renouvelables jusqu'à deux ans pour une menace prévisible, jusqu'à trois ans en situation exceptionnelle. Les notifications françaises couvrent notamment le 1er novembre 2026 au 30 avril 2027, pour toutes les frontières intérieures (Belgique, Allemagne, Luxembourg, Suisse, Espagne, Italie).",
  "Source institutionnelle de l'Union européenne."))
PE_SCHENGEN = ('pe_schengen', src("MEPs give green light to a reformed Schengen Borders Code", "Parlement européen", "24 avril 2024",
  "https://www.europarl.europa.eu/news/en/press-room/20240419IPR20558/meps-give-green-light-to-a-reformed-schengen-borders-code",
  "En cas de menace grave (terrorisme, criminalité organisée, entrées non autorisées massives), un État peut réintroduire des contrôles jusqu'à deux ans, avec une prolongation possible d'un an. La réforme crée une procédure de transfert vers l'État voisin des personnes en situation irrégulière interpellées lors de patrouilles conjointes. Texte adopté par 311 voix contre 267.",
  "Institution de l'Union européenne."))
MOT_SCH = ('mot_sch', src("Internal border controls within the Schengen Area: the European Commission calls for a phased lifting – Analysis focusing on France", "Mission opérationnelle transfrontalière (Domitille Ayral)", "18 juin 2026",
  "https://www.espaces-transfrontaliers.org/en/internal-border-controls-within-the-schengen-area-the-european-commission-calls-for-a-phased-lifting-analysis-focusing-on-france/",
  "Dans ses avis du 2 juin 2026, la Commission rappelle que les contrôles doivent rester « exceptional, temporary and proportionate » et recommande une levée progressive, avec des alternatives (contrôles mobiles, systèmes EES et ETIAS). Selon les autorités françaises, les contrôles ne sont « pas systématiques » et reposent sur l'analyse de risque.",
  "Structure d'expertise transfrontalière.", 'secondaire'))
PS_CC_FRONT = ('ps_cc_front', src("Immigration : quand la Cour des comptes reprend les constats d'un rapport sénatorial", "Public Sénat (Simon Barbarit)", "8 janvier 2024",
  "https://www.publicsenat.fr/actualites/politique/immigration-quand-la-cour-des-comptes-reprend-les-constats-dun-rapport-senatorial",
  "La Cour des comptes juge que l'organisation entre police aux frontières et douanes « n'est pas suffisamment optimisée ». La police ne relève que l'identité déclarée des personnes interpellées, « sans l'intégrer dans un système d'information national ».",
  "Média parlementaire rendant compte d'un rapport de la Cour des comptes.", 'media'))
OCDE_APD = ('ocde_apd', src("Preliminary official development assistance levels in 2025 (DCD(2026)8)", "OCDE, Comité d'aide au développement", "9 avril 2026, amendé le 15 juin 2026",
  "https://one.oecd.org/document/DCD%282026%298/en/pdf",
  "L'aide publique au développement de la France atteint 14,5 milliards de dollars en 2025, soit 0,42 % du revenu national brut, en baisse réelle de 10,9 %. L'aide totale du CAD recule de 23,1 %, « the largest annual contraction recorded in the history of ODA » ; l'aide bilatérale du CAD vers l'Afrique baisse de 23,9 %. Seuls quatre pays atteignent 0,7 %.",
  "Statistique internationale officielle (données préliminaires)."))
SEN_APD = ('sen_apd', src("Avis n° 141 (2025-2026) sur le projet de loi de finances pour 2026, tome IV : Aide publique au développement", "Sénat, commission des affaires étrangères (Christian Cambon, Patrice Joly)", "24 novembre 2025",
  "https://www.senat.fr/rap/a25-141-4/a25-141-41.pdf",
  "L'aide publique au développement française atteint « un peu plus de 13 Md€ » en 2025 (-10,7 %), soit 0,43 % du RNB, contre 0,56 % en 2022 ; la loi du 4 août 2021 fixait l'objectif de 0,7 %. Les crédits de la mission passent de 5,76 Md€ (2024) à 3,67 Md€ (PLF 2026). L'Afrique représente 40 % de l'aide française. La commission d'évaluation prévue en 2021 n'a été installée qu'en 2025.",
  "Rapport parlementaire."))
FOCUS_APD = ('focus_apd', src("L'aide publique au développement de la France dans un monde en turbulences : la fin d'une ambition ? Bilan 2017-2024", "Focus 2030", "octobre 2024",
  "https://focus2030.org/IMG/pdf/focus2030_bilan_apd_2017_2024.pdf",
  "Les dons représentent 88 % de l'aide en 2023, contre 92 % en moyenne au CAD. En 2022, environ 27 % de l'aide bilatérale ne quitte pas le territoire, dont 1 532 M€ pour l'accueil des réfugiés et 984 M€ de frais d'écolage d'étudiants étrangers. L'objectif de 0,7 % a été reporté de 2025 à 2030 en juillet 2023.",
  "Centre d'analyse indépendant favorable à l'aide.", 'secondaire'))
AFD_8 = ('afd_8', src("8 choses à savoir sur l'Aide publique au développement", "Agence française de développement (AFD)", "mis à jour le 2 septembre 2026",
  "https://www.afd.fr/fr/actualites/8-choses-savoir-sur-laide-publique-au-developpement",
  "En 2025, le groupe AFD a engagé plus de 10 Md€ en prêts, contre 0,8 Md€ en dons ; seuls 40 % de ses décaissements sont comptés en aide publique au développement. Les marchés financés par l'AFD auraient généré près de 12 Md€ de retombées pour des entreprises françaises entre 2020 et 2025.",
  "Opérateur public, partie prenante.", 'secondaire'))

# ── Sources : travail, social, pouvoir d'achat ──────────────────────────────
CC_IJ = ('cc_ij', src("L'indemnisation des arrêts de travail pour maladie du régime général (RALFSS 2024, chapitre V)", "Cour des comptes", "29 mai 2024",
  "https://www.ccomptes.fr/sites/default/files/2024-05/20240529-Ralfss-2024-Indemnisation-arrets-de-travail-pour-maladie-du-regime-general.pdf",
  "Les indemnités sont « passées de 7,7 Md€ à 12 Md€ entre 2017 et 2022 (+ 56 %) ». Sur 4,3 Md€ de hausse, « 1,7 Md€ est directement imputable à la crise sanitaire », 0,7 Md€ à l'augmentation du SMIC et du salaire moyen, 0,2 Md€ à la hausse de la population active, 0,4 Md€ à l'extension aux indépendants ; « 0,9 Md€ ne peuvent être rattachés à aucune de ces causes prises isolément ». Les plus de 55 ans font 18,3 % des actifs mais 27 % des journées indemnisées ; les arrêts de plus de six mois font 6 % des arrêts mais 45 % de la dépense. La fraude détectée (12,8 M€ en 2022) est jugée « faible ».",
  "Juridiction financière."))
DREES_IJ = ('drees_ij', src("Les indemnités journalières (fiche 25, Les dépenses de santé en 2024, édition 2025)", "DREES", "décembre 2025",
  "https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-12/CNS%20-%20Fiche%2025%20-%20Les%20indemnit%C3%A9s%20journali%C3%A8res.pdf",
  "Les indemnités journalières maladie atteignent 12,1 Md€ en 2024. « En 2024, les IJ maladie hors Covid-19 progressent de nouveau fortement : +7,0 % après +5,6 % en 2023. » Les revalorisations du SMIC augmentent les IJ, indexées sur les salaires ; la population active vieillit et les arrêts des plus âgés sont plus longs. La hausse du taux de recours et de la durée des arrêts, à âge donné, joue aussi.",
  "Service statistique ministériel."))
PS_IJ = ('ps_ij', src("Arrêts maladie : quelles solutions face à leur augmentation ?", "Public Sénat (Emile Boissel-Dombreval)", "22 juillet 2025",
  "https://www.publicsenat.fr/actualites/economie/arrets-maladie-quelles-solutions-face-a-leur-augmentation",
  "La dépense a crû de 2,9 % par an entre 2010 et 2019, puis de 6,3 % par an entre 2019 et 2023. Les facteurs démographiques et économiques expliquent 58 % de la hausse entre 2019 et 2023 ; selon l'Assurance maladie, 42 % vient d'un recours accru aux arrêts, notamment chez les jeunes, et de durées plus longues.",
  "Média parlementaire.", 'media'))
LEGI_FRAUDE = ('legi_fraude', src("Fraude à l'Assurance maladie et faux arrêts de travail : bilan record en 2024", "Legisocial (Audrey Catany), d'après le bilan de l'Assurance maladie", "21 mars 2025",
  "https://www.legisocial.fr/actualites-sociales/7246-fraude-assurance-maladie-faux-arrets-travail-bilan-record-2024.html",
  "La fraude totale détectée par l'Assurance maladie atteint 628 M€ en 2024 (+35 %). « Les fraudes aux indemnités journalières ont atteint 42 millions d'euros en 2024 », contre 17 M€ en 2023.",
  "Site juridique relayant le bilan de l'Assurance maladie (source primaire non lue).", 'secondaire'))
IPP_RSA = ('ipp_rsa', src("Évaluation quantitative de l'accompagnement rénové des bénéficiaires du RSA (synthèse du rapport n° 68)", "Dares et Institut des politiques publiques (M. Fouquet, R. Lardeux, T. Breda et al.)", "juin 2026",
  "https://www.ipp.eu/wp-content/uploads/2026/06/Synthese_dares_ipp_brsa.pdf",
  "Évaluation sur 18 territoires pilotes, de mars 2023 à décembre 2024 (environ 41 900 allocataires), sans le nouveau régime de sanctions. L'emploi salarié progresse de 0,9 point à six mois dans les territoires concernés ; chez les participants, de 3,2 points en moyenne sur l'année. L'emploi durable progresse de 2,2 points, mais de 0,7 point sans les contrats aidés ; pas d'effet sur le salaire. Les gains sont compensés par des effets négatifs sur les autres demandeurs : « on ne peut ainsi exclure que l'effet net de l'expérimentation sur la création d'emplois salariés soit nul ». L'étude ne mesure pas l'effet propre des 15 heures.",
  "Évaluation statistique publique et universitaire.", 'etude'))
LOC_RSA = ('loc_rsa', src("RSA : une évaluation souligne les progrès et limites de « l'accompagnement rénové »", "Banque des Territoires (Localtis, Catherine Abou El Khair)", "19 décembre 2024",
  "https://www.banquedesterritoires.fr/rsa-une-evaluation-souligne-les-progres-et-limites-de-laccompagnement-renove",
  "Selon une évaluation qualitative pour le ministère du Travail, 38 % des allocataires suivis ont occupé un emploi dans les six mois et 14 % ont obtenu un CDI ou un CDD de plus de six mois, sans point de comparaison. La norme de 15 à 20 heures est jugée « particulièrement exigeante » ; les exemptions vont de 15 % à 20 % selon les territoires.",
  "Presse spécialisée des collectivités.", 'media'))
LOC_SANC = ('loc_sanc', src("RSA : le décret Sanctions entre en vigueur", "Banque des Territoires (Localtis, Catherine Abou El Khair)", "2 juin 2025",
  "https://www.banquedesterritoires.fr/rsa-le-decret-sanctions-entre-en-vigueur",
  "Le décret n° 2025-478 du 30 mai 2025, en vigueur le 1er juin 2025, crée une « suspension-remobilisation » d'au moins 30 % de l'allocation pendant un à deux mois, avec reversement si l'allocataire se remet en conformité ; la suppression est possible au second manquement.",
  "Presse spécialisée des collectivités.", 'media'))
CNCDH_RSA = ('cncdh_rsa', src("Loi pour le plein emploi : l'obligation d'heures d'activité en contrepartie du RSA porte atteinte aux droits humains (déclaration D-2024-7)", "Commission nationale consultative des droits de l'homme (CNCDH)", "19 décembre 2024",
  "https://www.cncdh.fr/sites/default/files/2024-12/D%20-%202024%20-%207%20-%20D%C3%A9claration%20Loi%20Plein%20Emploi%20RSA%20Conditionn%C3%A9_0.pdf",
  "La CNCDH estime que le droit à des « moyens convenables d'existence » est menacé, que l'efficacité n'est pas démontrée faute d'analyse publique complète de l'expérimentation, et craint des heures non rémunérées qui se substitueraient à de vrais emplois. Elle recommande d'abroger la durée « d'au moins quinze heures ».",
  "Avis d'une autorité administrative indépendante."))
INSEE_MT25 = ('insee_mt25', src("Une photographie du marché du travail en 2025 (Insee Première n° 2096)", "Insee (Émilie Pénicaud)", "25 mars 2026",
  "https://www.insee.fr/fr/statistiques/8901327",
  "Chez les 15-24 ans en 2025, le taux d'emploi est de 34,5 %, soit 4,6 points de plus qu'en 2019 ; le taux d'activité est de 43,0 %. Le taux de chômage des jeunes « augmente de 1,0 point en 2025 et atteint 19,8 % », sous la moyenne des années 2010 (24,6 %). « 30,5 % d'entre eux sont en alternance ou en stage. »",
  "Statistique publique de référence."))
LOC_JEUNES = ('loc_jeunes', src("Emploi des jeunes : une exception française ?", "Banque des Territoires (Localtis, Guillaume Ducable)", "6 mars 2024",
  "https://www.banquedesterritoires.fr/emploi-des-jeunes-une-exception-francaise",
  "Selon l'Insee, le taux d'emploi des 15-24 ans est de 34,9 % en 2022, « le plus haut depuis 1991 ». Il est d'environ 35 % en France contre 42 % en moyenne dans l'OCDE, mais proche de la moyenne européenne (34,8 %). Chez les 25-29 ans, le taux d'emploi est de 78 %, 2 points au-dessus de la moyenne de l'OCDE.",
  "Presse spécialisée relayant l'Insee et l'OCDE.", 'media'))
TRESOR_APP = ('tresor_app', src("L'apprentissage en France : quel bilan pour quels objectifs ? (Trésor-Éco n° 376)", "Direction générale du Trésor (V. Barde, T. Gantois, J. Gouy-Waz, B. Leclair)", "25 novembre 2025",
  "https://www.tresor.economie.gouv.fr/Articles/2025/11/25/l-apprentissage-en-france-quel-bilan-pour-quels-objectifs",
  "« 879 000 nouveaux contrats ont été signés en 2024 », contre 306 000 en 2017 ; plus d'un million d'apprentis sont en cours de contrat fin 2024. Le coût public atteint environ 15 Md€ en 2023, soit « 14 700 € par apprenti ».",
  "Administration économique."))
MONTAIGNE_JEUNES = ('montaigne_jeunes', src("Les jeunes et le travail : aspirations et désillusions des 16-30 ans (communiqué)", "Institut Montaigne (Y. Algan, O. Galland, M. Lazar)", "29 avril 2025",
  "https://institutmontaigne.org/communiques-de-presse/les-jeunes-et-le-travail-aspirations-et-desillusions-des-16-30-ans",
  "Enquête auprès de 6 000 jeunes à l'automne 2024 : « 80 % des jeunes se disent prêts à travailler, même sans besoin financier » ; 66 % de ceux qui ont déjà travaillé perçoivent un décalage entre leurs attentes et la réalité ; 60 % des jeunes salariés envisagent de quitter leur entreprise d'ici cinq ans.",
  "Think tank libéral, cité ici comme source peu suspecte de complaisance.", 'secondaire'))
INSEE_PA = ('insee_pa', src("Revenu disponible brut et pouvoir d'achat – Données annuelles de 1960 à 2025", "Insee", "29 mai 2026",
  "https://www.insee.fr/fr/statistiques/2830244",
  "Évolution du pouvoir d'achat du revenu disponible brut par unité de consommation : -0,3 % en 2020, +2,8 % en 2021, -0,3 % en 2022, +0,4 % en 2023, +2,2 % en 2024 et -0,7 % en 2025 (provisoire).",
  "Comptes nationaux officiels."))
INSEE_FPS = ('insee_fps', src("Revenu disponible brut et pouvoir d'achat des ménages (France, portrait social, édition 2025)", "Insee (Insee Références)", "18 novembre 2025",
  "https://www.insee.fr/fr/statistiques/8612564",
  "« En 2024, le pouvoir d'achat du RDB par UC augmente de 2,1 %. » Depuis 2010, le pouvoir d'achat progresse en moyenne de 1,1 % par an, et de 0,5 % par an par unité de consommation, nettement moins que dans les années 1960.",
  "Statistique publique de référence."))
INSEE_CN25 = ('insee_cn25', src("Les comptes de la Nation en 2025 – Le PIB ralentit et le pouvoir d'achat des ménages se replie (Insee Première n° 2105)", "Insee (J. Eguienta, J.-C. Héam, P. Meinzel)", "29 mai 2026",
  "https://www.insee.fr/fr/statistiques/8996855",
  "Par unité de consommation, le pouvoir d'achat recule de 0,7 % en 2025, après +2,2 % en 2024. Contributions en 2025 : revenus du patrimoine -0,9 point (chute des dividendes après le bond de 2024), impôts -0,6 point, prix -0,8 point, revenus d'activité +1,0 point.",
  "Comptes nationaux officiels."))
INSEE_SAL24 = ('insee_sal24', src("Les salaires dans le secteur privé en 2024 (Insee Première n° 2079)", "Insee (T. Duquesne, N. P. Sokhna)", "23 octobre 2025",
  "https://www.insee.fr/fr/statistiques/8657156",
  "« Le salaire net moyen augmente de 0,8 % en 2024, après -1,3 % en 2022 puis -1,0 % en 2023. » « Ce regain en 2024 permet à peine d'atteindre le niveau de 2019 en euros constants. » Le salaire net moyen est de 2 733 € par mois.",
  "Statistique publique de référence."))
BDF_PA = ('bdf_pa', src("Le pouvoir d'achat (ABC de l'économie)", "Banque de France", "mars 2025",
  "https://www.banque-france.fr/system/files/2025-03/825155_Pouvoir-achat.pdf",
  "« Il peut y avoir un décalage entre le ressenti de la population et les statistiques d'évolution du pouvoir d'achat. » Causes avancées : sensibilité aux achats fréquents, effet qualité, dépenses pré-engagées (27,9 % du budget en 2022, contre 14,2 % il y a soixante ans), baisses d'impôt peu perçues.",
  "Document pédagogique de la banque centrale."))
INSEE_FINS = ('insee_fins', src("Embauches et fins de contrat dans le secteur privé (Emploi, chômage, revenus du travail, édition 2025)", "Insee (Insee Références)", "26 juin 2025",
  "https://www.insee.fr/fr/statistiques/8376832",
  "Fins de CDI en 2024 : 75 700 licenciements économiques, 506 700 licenciements non économiques, 514 600 ruptures conventionnelles et 1 850 100 démissions, sur 4 233 000 fins de CDI.",
  "Statistique publique de référence."))
SEN_RC = ('sen_rc', src("Rapport n° 488 (2025-2026) sur la transposition de l'avenant n° 3 relatif à l'assurance chômage", "Sénat, commission des affaires sociales (Laurent Burgoa)", "31 mars 2026",
  "https://www.senat.fr/rap/l25-488/l25-4881.pdf",
  "Selon la Dares, les ruptures conventionnelles « atteignent 514 768 en 2024 », contre 192 278 en 2009 (+167 %) ; les très petites entreprises en réalisent 41,6 %. Près de 375 000 ruptures ouvrent des droits au chômage.",
  "Rapport parlementaire."))
LD_BAREME = ('ld_bareme', src("Indemnités pour licenciement abusif : le barème obligatoire (article L1235-3 du code du travail)", "Lefebvre Dalloz (fiche pratique)", "27 avril 2026",
  "https://open.lefebvre-dalloz.fr/droit-social/rupture-contrat-travail/indemnites-licenciement-abusif-bareme-obligatoire_t7545",
  "Montants maximaux en mois de salaire brut selon l'ancienneté : 1 mois à 0 an, 3,5 mois à 2 ans, 6 mois à 5 ans, 10 mois à 10 ans, 20 mois à partir de 29 ans. Le barème ne s'applique pas en cas de licenciement nul (au moins 6 mois).",
  "Éditeur juridique.", 'secondaire'))
LD_CEDS = ('ld_ceds', src("Le « barème Macron » est contraire à la Charte sociale européenne", "Lefebvre Dalloz (Patrick Saget)", "10 octobre 2022",
  "https://open.lefebvre-dalloz.fr/droit-social/actualites/bareme-macron-contraire-charte-sociale-europeenne_f81059035-caa0-4da8-8532-a4c466b36b38",
  "Le Comité européen des droits sociaux (décision du 23 mars 2022) juge que le droit à une indemnité adéquate est violé par le barème ; la décision n'est pas contraignante en droit interne. Le 11 mai 2022, la Cour de cassation a jugé le barème conforme à la convention 158 de l'OIT.",
  "Éditeur juridique.", 'secondaire'))
OCDE_EPL = ('ocde_epl', src("Perspectives de l'emploi de l'OCDE 2020, chapitre 3 : la protection de l'emploi", "OCDE", "juillet 2020",
  "https://www.oecd.org/fr/publications/2020/07/oecd-employment-outlook-2020_19b4fc0d/full-report/component-8.html",
  "Entre 2013 et 2019, certaines réformes visaient à « atténuer la rigueur de la protection contre les licenciements », « notamment en France, en Italie, en Lituanie et en Slovénie ». L'OCDE rappelle l'introduction en France en 2008 de la rupture conventionnelle ouvrant droit au chômage.",
  "Organisation internationale."))
IRES_EPL = ('ires_epl', src("Les indicateurs de législation protectrice de l'emploi au crible de l'analyse juridique (La Revue de l'IRES n° 82)", "Raphaël Dalmasso (Université de Lorraine), IRES", "2014",
  "https://ires.fr/wp-content/uploads/2023/01/R82-2.pdf",
  "Au 1er janvier 2013, la France obtient 2,82 sur 6 à l'indicateur de l'OCDE pour la protection des CDI, l'Italie 2,79 et le Royaume-Uni 1,62 : « La France et l'Italie [...] apparaissent comme des législations particulièrement rigides. » L'auteur critique ensuite ces indicateurs.",
  "Article universitaire (données de 2013, antérieures aux ordonnances de 2017).", 'etude'))

# ── Sources : économie, fiscalité, programmes ───────────────────────────────
PS_AIDES = ('ps_aides', src("Un coût annuel de 211 milliards d'euros : la commission d'enquête du Sénat sur les aides publiques aux entreprises réclame un « choc de transparence »", "Public Sénat (Guillaume Jacquot)", "8 juillet 2025",
  "https://www.publicsenat.fr/actualites/economie/un-cout-annuel-de-211-milliards-deuros-la-commission-denquete-du-senat-sur-les-aides-publiques-aux-entreprises-reclame-un-choc-de-transparence",
  "La commission d'enquête du Sénat estime à au moins 211 milliards d'euros les aides publiques d'État aux entreprises en 2023 (subventions, aides de Bpifrance, dépenses fiscales, allègements de cotisations), hors aides des collectivités et de l'Europe. Rapport adopté à l'unanimité le 1er juillet 2025 ; président Olivier Rietmann (LR), rapporteur Fabien Gay (communiste) ; plus de 2 200 dispositifs recensés.",
  "Média parlementaire.", 'media'))
PS_AIDES_CALC = ('ps_aides_calc', src("211 milliards d'euros d'aides publiques aux entreprises : sur quoi repose le calcul de la commission d'enquête du Sénat ?", "Public Sénat (Guillaume Jacquot)", "15 septembre 2025",
  "https://www.publicsenat.fr/actualites/economie/211-milliards-deuros-daides-publiques-aux-entreprises-sur-quoi-repose-le-calcul-de-la-commission-denquete-du-senat",
  "Le total de 2023 se décompose en 7 Md€ de subventions, 41 Md€ d'interventions de Bpifrance, 88 Md€ de dépenses fiscales et 75 Md€ d'allègements de cotisations. Au « sens strict », la commission arrive à 108 Md€. Le Haut-commissariat au Plan donne 112 Md€ hors allègements ; le ministre Éric Lombard parle d'environ 150 Md€. Le président de la commission voit dans les allègements des « compensations » ; le Medef conteste l'addition.",
  "Média parlementaire.", 'media'))
SEN_808 = ('sen_808', src("Rapport n° 808 (2024-2025) de la commission d'enquête sur les aides publiques aux grandes entreprises, partie V : plusieurs tentatives pour établir le coût des aides", "Sénat", "juillet 2025",
  "https://www.senat.fr/rap/r24-808-1/r24-808-17.html",
  "La commission s'appuie sur France Stratégie (2020 : entre 139 et 223 Md€ pour 2019 selon le périmètre), le Clersé (2022 : 205 Md€ par an) et Rexecode (2023). Elle conclut qu'il est « impossible de déterminer avec précision le montant des aides publiques versées aux grandes entreprises ».",
  "Rapport parlementaire."))
DREES_MS = ('drees_ms', src("Minima sociaux et prestations de solidarité, édition 2025 — Fiche 07 : Les dépenses d'allocations", "DREES", "décembre 2025",
  "https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-12/MS2025%20-%20Fiche%2007%20-%20Les%20d%C3%A9penses%20d%27allocations.pdf",
  "En 2023, les minima sociaux « s'élèvent à 31,6 milliards d'euros, soit 1,1 % du produit intérieur brut » ; pour le RSA, « le montant des allocations versées à ce titre s'élève à 12,2 milliards d'euros, soit 0,4 % du PIB ».",
  "Service statistique ministériel."))
FS_ISF = ('fs_isf', src("Comité d'évaluation des réformes de la fiscalité du capital – Rapport final, avis du comité", "France Stratégie", "octobre 2023",
  "https://www.strategie.gouv.fr/sites/strategie.gouv.fr/files/atoms/files/fs-2023-rapport-isf-quatrieme_rapport_complet_17octobre_avis.pdf",
  "« Aucun effet n'a été détecté sur l'investissement et les salaires parmi les entreprises » les plus exposées. Les dividendes déclarés passent d'environ 14 Md€ par an (2013-2017) à environ 23 Md€ (2018-2020), surtout à cause du prélèvement forfaitaire unique ; 1 % des foyers concentre 96 % des montants. Depuis 2018, environ 380 retours pour 260 départs par an chez les redevables de l'IFI, contre 370 retours pour 950 départs sous l'ISF (2011-2016). Le coût de la transformation de l'ISF serait « vraisemblablement supérieur à 4 milliards d'euros » en 2022.",
  "Évaluation publique de référence."))
PS_ISF = ('ps_isf', src("Suppression de l'ISF, flat tax : « Ce n'est pas du ruissellement, mais de l'évaporation ! », critique Eric Bocquet", "Public Sénat (Romain David)", "15 octobre 2021",
  "https://www.publicsenat.fr/actualites/politique/suppression-de-l-isf-flat-tax-ca-n-est-pas-du-ruissellement-mais-de-l-evaporation",
  "D'après le troisième rapport du comité d'évaluation, en 2019, 62 % des dividendes sont allés à 0,1 % des foyers (39 000 foyers) ; aucun effet observable sur l'économie réelle n'est constaté à ce stade. Bercy répond que les effets sont de long terme. La sénatrice LR Christine Lavarde explique la concentration des dividendes par celle de l'actionnariat.",
  "Média parlementaire.", 'media'))
LOC_IFI = ('loc_ifi', src("Logement / Fiscalité : premier bilan mitigé pour l'IFI et retour du « retraité de l'île de Ré »", "Banque des Territoires (Localtis, Jean-Noël Escudié)", "10 octobre 2019",
  "https://www.banquedesterritoires.fr/logement-fiscalite-premier-bilan-mitige-pour-lifi-et-retour-du-retraite-de-lile-de-re",
  "Selon le rapport du Sénat d'octobre 2019, l'IFI a rapporté en 2018 2,9 Md€ de moins que l'ISF ; les dons ont reculé de 49 % ; la réforme a « fortement freiné les départs à l'étranger, sans provoquer de retours ».",
  "Presse spécialisée rendant compte d'un rapport parlementaire (2019).", 'media'))
LEGIF_ZUC = ('legif_zuc', src("Adoption à l'Assemblée nationale de la taxe dite Zucman fixant un impôt plancher sur le patrimoine des ultra-riches", "Legifiscal", "février 2025",
  "https://www.legifiscal.fr/actualites-fiscales/4043-adoption-assemblee-nationale-taxe-dite-zucman-fixant-impot-plancher-patrimoine-ultra-riches.html",
  "Le 20 février 2025, l'Assemblée a adopté en première lecture, par 116 voix contre 39, un impôt plancher de 2 % sur les patrimoines de plus de 100 M€, qui viserait environ 1 800 foyers ; le RN s'est abstenu.",
  "Site d'information fiscale.", 'secondaire'))
PS_RNFISC = ('ps_rnfisc', src("Budget 2026 : le RN s'éloigne de la gauche sur la fiscalité", "Public Sénat (Guillaume Jacquot)", "21 octobre 2025",
  "https://www.publicsenat.fr/actualites/economie/budget-2026-le-rn-seloigne-de-la-gauche-sur-la-fiscalite",
  "Pendant le budget 2026, les députés RN ont fait barrage à la taxe Zucman, après s'être abstenus l'année précédente. Marine Le Pen l'a qualifiée de « stupide et nocive ». Le RN a refusé de porter la flat tax de 30 à 33 %. Il proposait un « impôt sur la fortune financière » excluant les biens professionnels, les parts de PME et l'immobilier de la classe moyenne, et une taxe sur les superdividendes.",
  "Média parlementaire.", 'media'))
LCP_ZUC = ('lcp_zuc', src("Taxe Zucman : la taxe sur les très hauts patrimoines rejetée en commission à l'Assemblée nationale", "LCP (Raphaël Marchal)", "20 octobre 2025",
  "https://lcp.fr/node/410175",
  "En commission des finances, les amendements prévoyant « un impôt annuel minimum de 2 % sur le patrimoine lorsque celui-ci, y compris professionnel, est d'au moins 100 millions » d'euros ont été rejetés, avec contre eux l'ex-majorité, LR, le RN et l'UDR.",
  "Média parlementaire.", 'media'))
DATAN_3300 = ('datan_3300', src("Scrutin n° 3300 : amendement instaurant la taxe Zucman sur les patrimoines supérieurs à 100 millions d'euros (PLF 2026)", "Datan, d'après les données ouvertes de l'Assemblée nationale", "31 octobre 2025",
  "https://datan.fr/votes/legislature-17/vote_3300",
  "L'amendement est rejeté par 228 voix contre 172. Groupe RN : 0 pour, 0 abstention, 88 contre. La gauche vote pour (socialistes 61, LFI 60, écologistes 33, GDR 12) ; EPR, Droite républicaine et UDR votent contre.",
  "Données officielles de scrutin relayées par un site civique.", 'secondaire'))
LCP_IFIMP = ('lcp_ifimp', src("Budget 2026 : l'Assemblée nationale vote pour l'instauration d'un « impôt sur la fortune improductive »", "LCP (Raphaël Marchal)", "1er novembre 2025",
  "https://lcp.fr/actualites/budget-2026-l-assemblee-nationale-vote-pour-l-instauration-d-un-impot-sur-la-fortune",
  "Le 31 octobre 2025, un amendement MoDem est adopté par 163 voix contre 150 contre l'avis du gouvernement : il remplace l'IFI par un « impôt sur la fortune improductive » à 1 % au-dessus de 1,3 M€ (yachts, voitures de collection, cryptoactifs, fonds euros d'assurance-vie). La majorité est venue du MoDem, du PS, du RN et de LIOT.",
  "Média parlementaire.", 'media'))
NFP_PROG = ('nfp_prog', src("Contrat de législature du Nouveau Front populaire", "Nouveau Front populaire (programme publié par La France insoumise)", "juin 2024",
  "https://lafranceinsoumise.fr/wp-content/uploads/2024/06/PROGRAMME-FRONT-POPULAIRE.pdf",
  "Rubrique « Décréter l'état d'urgence sociale » : « Bloquer les prix des biens de première nécessité dans l'alimentation, l'énergie et les carburants par décret, et renforcer le bouclier qualité-prix pour les outre-mer ». Le programme prévoit aussi de taxer « les superprofits des agro-industriels et de la grande distribution » ; il ne détaille ni la liste des produits ni le mécanisme de compensation.",
  "Programme partisan, cité pour décrire son contenu.", 'secondaire'))
CDJ_PRIX = ('cdj_prix', src("Le blocage des prix sur les produits de première nécessité ? Oui, mais…", "Le Club des juristes (Romain Loir, Université de La Réunion)", "24 juin 2024",
  "https://www.leclubdesjuristes.com/economie/le-blocage-des-prix-sur-les-produits-de-premiere-necessite-oui-mais-6385/",
  "Depuis l'ordonnance de 1986, les prix sont « librement déterminés par le jeu de la concurrence », principe de valeur seulement législative. L'article L410-2 du code de commerce permet déjà de réglementer les prix par décret, de façon permanente dans les secteurs peu concurrentiels ou temporairement, six mois au plus, en cas de crise (produits pétroliers pendant la guerre du Golfe, gel hydroalcoolique pendant le Covid). Limites : la liberté d'entreprendre et le droit de l'Union européenne.",
  "Analyse juridique universitaire.", 'etude'))
MONTAIGNE_PRIX = ('montaigne_prix', src("Bloquer les prix des produits de première nécessité (chiffrage des législatives 2024)", "Institut Montaigne", "juin 2024",
  "https://www.institutmontaigne.org/legislatives-2024/nouveau-front-populaire/bloquer-les-prix-des-produits-de-premiere-necessite",
  "Coût médian estimé à environ 24 Md€ par an (fourchette 9 à 38 Md€). Risques avancés : producteurs nationaux qui réduisent leur production, producteurs étrangers qui vendent ailleurs, demande maintenue faute de signal-prix ; mesure non ciblée qui profiterait davantage aux ménages aisés.",
  "Think tank libéral, cité comme argument contraire.", 'secondaire'))
INSEE_BOUCLIER = ('insee_bouclier', src("La flambée des prix de l'énergie : un effet sur l'inflation réduit de moitié par le « bouclier tarifaire » (Insee Analyses n° 75)", "Insee (Alexandre Bourgeois, Raphaël Lafrogne-Joussier)", "1er septembre 2022",
  "https://www.insee.fr/fr/statistiques/6524161",
  "Entre le 2e trimestre 2021 et le 2e trimestre 2022, l'énergie a contribué pour 3,1 points à une inflation de 5,3 % ; sans le bouclier, sa contribution aurait été de 6,2 points et l'inflation aurait atteint 8,4 %. Les prix de l'énergie pour les ménages ont augmenté de 28 % avec le bouclier, contre 54 % sans.",
  "Statistique publique de référence."))
BDF_BOUCLIER = ('bdf_bouclier', src("Bouclier tarifaire sur les prix de l'énergie en France : quel bilan ? (Bulletin n° 253)", "Banque de France (M. Lemoine, A. Petronevich, A. Zhutova)", "15 juillet 2024",
  "https://www.banque-france.fr/fr/publications-et-statistiques/publications/bouclier-tarifaire-sur-les-prix-de-lenergie-en-france-quel-bilan",
  "Sur 2022-2023, le bouclier a eu un « impact cumulé de – 2,2 points de pourcentage » sur l'inflation et environ +0,3 point sur le PIB, pour un coût cumulé de 2,2 % du PIB. Face à un choc durable, il ne ferait que différer l'inflation, sauf à être maintenu indéfiniment, avec un coût budgétaire prohibitif.",
  "Étude de la banque centrale."))
LCP_GAROT = ('lcp_garot', src("Déserts médicaux : l'Assemblée adopte la proposition de loi qui prévoit de réguler l'installation des médecins", "LCP (Maxence Kagni)", "8 mai 2025",
  "https://lcp.fr/actualites/deserts-medicaux-l-assemblee-adopte-la-proposition-de-loi-qui-prevoit-de-reguler-l",
  "Le texte crée une autorisation d'installation délivrée par l'ARS : de droit en zone sous-dotée, seulement en cas de départ d'un praticien en zone sur-dotée. Il prévoit aussi une première année de médecine dans chaque département. Adopté le 7 mai 2025 par 99 voix pour, 9 contre et 10 abstentions ; le RN s'est abstenu. Le ministre Yannick Neuder y était opposé : il faut « former plus de médecins ».",
  "Média parlementaire.", 'media'))
LCP_GAROT2 = ('lcp_garot2', src("Déserts médicaux : « Inscrivez notre texte à l'ordre du jour du Sénat », demande Guillaume Garot à Sébastien Lecornu", "LCP (Anne-Charlotte Dusseaulx)", "17 septembre 2025",
  "https://lcp.fr/actualites/deserts-medicaux-inscrivez-notre-texte-a-l-ordre-du-jour-du-senat-demande-guillaume",
  "Selon Guillaume Garot, le texte interdit l'installation dans les zones déjà suffisamment dotées et préserve la liberté d'installation ailleurs. Il est soutenu par des députés des neuf groupes.",
  "Média parlementaire.", 'media'))
PS_MOUILLER = ('ps_mouiller', src("Santé : moins d'une semaine après l'Assemblée, le Sénat examine sa propre proposition de loi pour encadrer l'installation des médecins", "Public Sénat (Romain David)", "13 mai 2025",
  "https://www.publicsenat.fr/actualites/sante/sante-moins-dune-semaine-apres-lassemblee-le-senat-examine-sa-propre-proposition-de-loi-pour-encadrer-linstallation-des-medecins",
  "La proposition de Philippe Mouiller (LR) conditionne l'installation des généralistes dans les zones bien dotées à un engagement d'exercer à temps partiel en zone sous-dense. Le gouvernement Bayrou veut ajouter une « mission de solidarité territoriale obligatoire » : deux jours de consultations par mois en zone prioritaire. Le texte Garot « va plus loin dans la coercition » et suscite une forte opposition de la profession.",
  "Média parlementaire.", 'media'))
LOC_GAROT = ('loc_garot', src("Lutte contre les déserts médicaux : à la régulation façon Garot, les sénateurs préfèrent l'« aménagement » de la liberté d'installation", "Banque des Territoires (Localtis, Caroline Megglé)", "12 juin 2026",
  "https://www.banquedesterritoires.fr/lutte-contre-les-deserts-medicaux-la-regulation-facon-garot-les-senateurs-preferent-lamenagement-de",
  "Le Sénat a examiné le texte Garot le 11 juin 2026 sans aller au bout, faute de temps : il n'est pas adopté. En commission, la régulation avait été remplacée par le dispositif Mouiller. La rapporteure Corinne Imbert (LR) y voit « la restriction la plus stricte jamais imposée à une profession de santé ».",
  "Presse spécialisée des collectivités.", 'media'))
DREES_1144 = ('drees_1144', src("En 2018, les territoires sous-dotés en médecins généralistes concernent près de 6 % de la population (Études et Résultats n° 1144)", "DREES (Blandine Legendre)", "février 2020",
  "https://drees.solidarites-sante.gouv.fr/sites/default/files/er1144.pdf",
  "En 2018, 5,7 % de la population, soit environ 3,8 millions de personnes, vit en zone sous-dotée (2,5 consultations par an et par habitant ou moins), contre 3,8 % en 2015. Les communes rurales sont surreprésentées, mais aussi certaines banlieues parisiennes ; le recul vient des départs en retraite non remplacés, en partie à cause des numerus clausus passés.",
  "Service statistique ministériel (données 2018)."))
DREES_1267 = ('drees_1267', src("Les deux tiers des généralistes déclarent être amenés à refuser de nouveaux patients comme médecin traitant (Études et Résultats n° 1267)", "DREES", "mai 2023",
  "https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2023-06/ER1267.pdf",
  "Le quart de la population le moins bien servi ne dispose que de 19 % des généralistes, contre 31 % pour le quart le mieux servi. La part des généralistes qui jugent l'offre locale insuffisante passe de 67 % en 2019 à 78 % en 2022.",
  "Service statistique ministériel."))

# ── Sources : école, laïcité, institutions, sécurité, hôpital ───────────────
CC_PRIVE = ('cc_prive', src("L'enseignement privé sous contrat (rapport public thématique)", "Cour des comptes", "1er juin 2023",
  "https://www.ccomptes.fr/sites/default/files/2023-10/20230601-enseignement-prive-sous-contrat.pdf",
  "Les crédits de l'État au privé sous contrat atteignent « 8 Md€ en 2022 » ; l'État finance 55 % du premier degré privé et 68 % du second degré privé. Les élèves de milieux favorisés ou très favorisés « sont désormais majoritaires dans ce secteur (55,4 % en 2021) », contre 32,3 % dans le public ; boursiers : 11,8 % contre 29,1 %. Les résultats du privé « apparaissent globalement meilleurs », mais les travaux sur la valeur ajoutée « ne permettent pas d'identifier dans le privé sous contrat une plus-value supérieure ou inférieure » : à composition sociale égale, la performance « apparaît sensiblement la même que celle du public ».",
  "Juridiction financière (données 2021-2022)."))
LOC_PRIVE = ('loc_prive', src("Enseignement privé : la Cour des comptes veut moduler les moyens selon la composition sociale des établissements", "Banque des Territoires (Localtis, Jean Damien Lesay)", "2 juin 2023",
  "https://www.banquedesterritoires.fr/enseignement-prive-la-cour-des-comptes-veut-moduler-les-moyens-selon-la-composition-sociale-des",
  "D'après la Cour des comptes, la part d'élèves très favorisés dans le privé sous contrat passe de 26,4 % en 2000 à 40,2 % en 2021. Les écarts d'indice de position sociale sont aussi importants entre établissements publics. Le contrôle financier du privé « n'est pas mis en œuvre ».",
  "Presse spécialisée des collectivités.", 'media'))
LOC_IPS = ('loc_ips', src("Le niveau social des lycées varie fortement selon les départements", "Banque des Territoires (Localtis, Virginie Fauvel), d'après la DEPP", "8 avril 2025",
  "https://www.banquedesterritoires.fr/le-niveau-social-des-lycees-varie-fortement-selon-les-departements",
  "Selon la DEPP, « les lycées privés sous contrat sont nettement plus favorisés (IPS de 125) que les lycées publics (105) ».",
  "Presse spécialisée relayant la statistique publique.", 'media'))
AN_VOILE = ('an_voile', src("Question écrite n° 57422 et réponse du ministère de l'Éducation nationale", "Assemblée nationale (14e législature)", "réponse publiée au JO le 17 mars 2015",
  "https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE57422.pdf",
  "La neutralité des parents accompagnateurs « ne fait pas l'objet de dispositions législatives ou réglementaires spécifiques ». Selon l'étude du Conseil d'État du 19 décembre 2013, « les parents d'élèves doivent être regardés comme des usagers du service public de l'éducation ». On peut leur demander « de s'abstenir de manifester leur appartenance ou leurs croyances religieuses en cas de risque de prosélytisme » ; « les circonstances de fait sont déterminantes ».",
  "Réponse ministérielle officielle (2015)."))
SURL_VOILE = ('surl_voile', src("Chez les Surligneurs : Bruno Retailleau peut-il interdire le voile lors des sorties scolaires ?", "Les Surligneurs, publié par Actu-Juridique", "non daté (vers janvier 2025)",
  "https://www.actu-juridique.fr/ntic-medias-presse/chez-les-surligneurs-bruno-retailleau-peut-il-interdire-le-voile-lors-des-sorties-scolaires/",
  "L'étude du Conseil d'État de 2013 considère que les parents accompagnateurs sont des usagers, non soumis à la neutralité, position que l'article juge « fragile ». Le tribunal administratif de Nice l'a suivie en 2015 ; celui de Montreuil avait validé un règlement imposant la neutralité, dans la ligne de la circulaire du 27 mars 2012. Une interdiction visant le seul voile serait discriminatoire et exigerait une base légale solide.",
  "Vérification juridique animée par des universitaires.", 'media'))
PS_VOILE19 = ('ps_voile19', src("Interdiction du voile pour les sorties scolaires : retour sur l'émergence du texte", "Public Sénat", "29 octobre 2019",
  "https://www.publicsenat.fr/actualites/politique/interdiction-du-voile-pour-les-sorties-scolaires-retour-sur-l-emergence-du",
  "Un amendement d'interdiction est rejeté à l'Assemblée en février 2019. En mai 2019, un amendement est adopté au Sénat, puis retiré en commission mixte paritaire. Une proposition de loi de Jacqueline Eustache-Brinio est déposée en juillet 2019.",
  "Média parlementaire.", 'media'))
PS_VOILE21 = ('ps_voile21', src("Séparatisme : le Sénat vote l'interdiction des signes religieux pour les accompagnateurs de sorties scolaires", "Public Sénat", "30 mars 2021",
  "https://www.publicsenat.fr/article/parlementaire/separatisme-le-senat-vote-l-interdiction-des-signes-religieux-pour-les",
  "Un amendement est adopté au Sénat par 177 voix contre 141 dans le projet de loi confortant le respect des principes de la République ; le ministre Gérald Darmanin évoque un risque de censure par le Conseil constitutionnel.",
  "Média parlementaire.", 'media'))
PS_VOILE_PPL = ('ps_voile_ppl', src("Port du voile et sorties scolaires : le Sénat adopte la proposition de loi Eustache-Brinio", "Public Sénat", "29 octobre 2019",
  "https://www.publicsenat.fr/actualites/politique/port-du-voile-et-sorties-scolaires-le-senat-adopte-la-proposition-de-loi",
  "Le texte est adopté au Sénat par 163 voix contre 114. Le ministre Jean-Michel Blanquer estime qu'« une loi irait au-delà du nécessaire et aurait des effets contre-productifs » ; ses chances d'adoption à l'Assemblée sont jugées faibles.",
  "Média parlementaire.", 'media'))
LCP_CC24 = ('lcp_cc24', src("Loi immigration : le Conseil constitutionnel censure largement le texte voté en fin d'année dernière", "LCP (Raphaël Marchal)", "25 janvier 2024",
  "https://lcp.fr/index%2Ephp/actualites/loi-immigration-le-conseil-constitutionnel-censure-largement-le-texte-vote-en-fin-d",
  "La loi compte 86 articles ; 35 sont censurés totalement ou partiellement, dont 32 comme « cavaliers législatifs » et 3 sur le fond. Parmi les cavaliers figurent les restrictions aux prestations familiales, au regroupement familial et au droit du sol. Sur le fond sont censurés les quotas migratoires votés chaque année et la prise d'empreintes sans consentement. Gérald Darmanin affirme que le texte du gouvernement est validé dans son « intégralité ».",
  "Média parlementaire.", 'media'))
AJ_CC24 = ('aj_cc24', src("La décision du Conseil constitutionnel relative à la loi sur l'immigration", "Actu-Juridique", "2024",
  "https://www.actu-juridique.fr/constitutionnel/la-decision-du-conseil-constitutionnel-relative-a-la-loi-sur-limmigration/",
  "« Ce projet comportait 27 articles », alors que la loi déférée en compte 86. « La censure de cavaliers ne préjuge en effet en rien de la constitutionnalité au fond. » La notion de gouvernement des juges est « un sujet ancien ».",
  "Revue juridique.", 'secondaire'))
AN_NC = ('an_nc', src("Question écrite n° 15699 et réponse du ministère de la Justice sur les décisions de non-conformité du Conseil constitutionnel", "Assemblée nationale (15e législature)", "réponse publiée au JO le 26 février 2019",
  "https://questions.assemblee-nationale.fr/q15/15-15699QE.htm",
  "La réponse détaille, année par année, les décisions de non-conformité de 1971 au 1er février 2019 : pour les décisions de contrôle a priori, la très grande majorité sont des non-conformités partielles et les non-conformités totales sont rares.",
  "Réponse ministérielle officielle (données de 2019)."))
AN_REV = ('an_rev', src("La révision de la Constitution (fiche de synthèse n° 55)", "Assemblée nationale", "page consultée le 8 novembre 2026",
  "https://www.assemblee-nationale.fr/dyn/synthese/fonctionnement-assemblee-nationale/travail-legislatif/la-revision-de-la-constitution",
  "L'initiative de la révision appartient au Président de la République, sur proposition du Premier ministre, ou aux parlementaires. Les deux assemblées votent le texte en termes identiques ; l'adoption définitive passe par référendum ou par le Congrès, à la majorité des trois cinquièmes des suffrages exprimés.",
  "Document institutionnel."))
SEN_REV = ('sen_rev', src("Les révisions de la Constitution de 1958 : les révisions abouties", "Sénat", "page consultée le 8 novembre 2026",
  "https://www.senat.fr/connaitre-le-senat/evenements-et-manifestations-culturelles/les-revisions-de-la-constitution/les-revisions-de-la-constitution-de-1958-les-revisions-abouties.html",
  "Après la censure partielle de la loi Pasqua (décision du 13 août 1993), « le gouvernement décide de réviser la Constitution » : la loi constitutionnelle du 25 novembre 1993 crée l'article 53-1. D'autres révisions ont suivi des décisions du Conseil (Maastricht en 1992, Cour pénale internationale et traité d'Amsterdam en 1999).",
  "Document institutionnel."))
PS_LR_CC = ('ps_lr_cc', src("Loi immigration : face au spectre de la censure du Conseil constitutionnel, LR prépare la riposte", "Public Sénat (Simon Barbarit)", "25 janvier 2024",
  "https://www.publicsenat.fr/actualites/politique/loi-immigration-face-au-spectre-de-la-censure-du-conseil-constitutionnel-lr-prepare-la-riposte",
  "Les Républicains veulent une révision constitutionnelle ; Gérard Larcher estime qu'« il faudra modifier la Constitution » et Bruno Retailleau parle d'« un dévoiement des institutions ».",
  "Média parlementaire.", 'media'))
SEN_NARCO = ('sen_narco', src("Commission d'enquête sur l'impact du narcotrafic en France : l'essentiel (rapport n° 588, 2023-2024)", "Sénat (président Jérôme Durain, rapporteur Étienne Blanc)", "mai 2024",
  "https://conferenceconsensuslogement.senat.fr/rap/r23-588-2/r23-588-2-syn.pdf",
  "Le chiffre d'affaires du trafic est d'au moins « 3,5 milliards d'euros au minimum » selon le ministre de l'Économie. Selon l'office central de lutte contre le crime organisé, « entre 80 à 90 % » des règlements de comptes entre délinquants sont liés au trafic de stupéfiants. L'OFAST « ne dispose toujours pas des moyens requis ».",
  "Rapport parlementaire transpartisan."))
SEN_LOI_NARCO = ('sen_loi_narco', src("Proposition de loi visant à sortir la France du piège du narcotrafic (La loi en clair)", "Sénat", "2025",
  "https://www.senat.fr/travaux-parlementaires/textes-legislatifs/la-loi-en-clair/proposition-de-loi-visant-a-sortir-la-france-du-piege-du-narcotrafic.html",
  "Le texte est adopté définitivement le 29 avril 2025, jugé « partiellement conforme » par le Conseil constitutionnel le 12 juin et promulgué le 13 juin 2025. Il crée un parquet national anti-criminalité organisée, des quartiers de lutte contre la criminalité organisée en prison et un statut des « repentis ». La page reprend la formule de la commission : « submersion de la France par le narcotrafic ».",
  "Document institutionnel."))
AFP_NARCO24 = ('afp_narco24', src("Narcotrafic : 110 morts et explosion des saisies de cocaïne en France en 2024", "AFP, reprise par Imaz Press", "6 février 2025",
  "https://imazpress.com/france-monde/narcotrafic-110-morts-et-explosion-des-saisies-de-cocaine-en-france-en-2024",
  "D'après le ministère de l'Intérieur, 110 morts liés au narcotrafic en 2024 contre 139 en 2023 ; 367 homicides et tentatives contre 418. Cocaïne saisie : 53,5 tonnes, « une augmentation de 130% comparé à 2023 (23 tonnes) » ; cannabis saisi : 101 tonnes, en baisse de 19 %.",
  "Dépêche d'agence reprenant des chiffres officiels.", 'media'))
AFP_NARCO25 = ('afp_narco25', src("Narcotrafic : 84,3 tonnes de cocaïne saisies en France en 2025, contre 53,5 tonnes en 2024", "AFP, reprise par Outremers 360", "18 mars 2026",
  "https://outremers360.com/bassin-atlantique-appli/narcotrafic-84-3-tonnes-de-cocaine-saisies-en-france-en-2025-contre-53-5-tonnes-en-2024",
  "Selon le ministre de l'Intérieur, 84,3 tonnes de cocaïne ont été saisies en 2025 (+58 %) et 127,3 tonnes de cannabis ; les mis en cause augmentent d'environ 7 % par an depuis 2017.",
  "Dépêche d'agence reprenant des chiffres officiels.", 'media'))
AFP_OFDT = ('afp_ofdt', src("Drogues : plus d'un million d'usagers de cocaïne en France en 2023", "AFP, d'après l'OFDT, publié par Les Nouvelles Calédoniennes", "16 janvier 2025",
  "https://www.lnc.nc/article/france/societe/drogues-plus-d-un-million-d-usagers-de-cocaine-en-france-en-2023",
  "Selon l'OFDT, 1,1 million d'usagers de cocaïne dans l'année en 2023, contre 600 000 dans le rapport précédent : « La demande en cocaïne n'a jamais été aussi forte ». Le cannabis est « relativement stable », avec 5 millions d'usagers dans l'année.",
  "Dépêche d'agence reprenant l'observatoire public des drogues.", 'media'))
DREES_PNM = ('drees_pnm', src("Les postes de personnel non médical salarié (fiche 06, Les établissements de santé en 2024, édition 2026)", "DREES", "juillet 2026",
  "https://drees.solidarites-sante.gouv.fr/sites/default/files/2026-07/ES%202026%20-%20Fiche%2006%20-%20Les%20postes%20de%20personnel%20non%20m%C3%A9dical%20salari%C3%A9.pdf",
  "Au 31 décembre 2024, 1 170 588 postes non médicaux salariés : 797 151 soignants, 161 924 administratifs, 123 907 techniques, 65 065 médico-techniques, 22 541 éducatifs et sociaux. Dans le public : 576 868 soignants pour 110 089 administratifs. La fiche compte des postes, pas des personnes.",
  "Service statistique ministériel."))
DREES_PM = ('drees_pm', src("Les postes de personnel médical ou pharmaceutique (fiche 05, Les établissements de santé en 2024, édition 2026)", "DREES", "juillet 2026",
  "https://drees.solidarites-sante.gouv.fr/sites/default/files/2026-07/ES%202026%20-%20Fiche%2005%20-%20Les%20postes%20de%20personnel%20m%C3%A9dical%20ou%20pharmaceutique.pdf",
  "« 231 800 postes de personnel médical ou pharmaceutique » fin 2024 : 126 800 médecins, odontologistes et pharmaciens salariés, 43 000 libéraux, 45 200 internes et docteurs juniors, 16 900 sages-femmes.",
  "Service statistique ministériel."))
AP_HOP = ('ap_hop', src("À l'hôpital, la guerre des chiffres autour de la place des personnels non soignants", "Acteurs publics (Marie Malaterre)", "7 juillet 2025",
  "https://acteurspublics.fr/articles/a-lhopital-la-guerre-des-chiffres-entre-personnels-soignants-et-non-soignants/",
  "Selon l'OCDE, la France compte 34 % de personnels non soignants à l'hôpital, dont 14 % d'administratifs, 10 % de techniques et 9 % d'agents de service ; Belgique 36 %, Allemagne et Italie 25 %, Espagne 24 %, l'écart s'expliquant en partie par l'externalisation chez les voisins. À l'AP-HP, 6,8 % des effectifs relèvent des fonctions administratives et de direction.",
  "Presse spécialisée du secteur public.", 'media'))
AP_JOMIER = ('ap_jomier', src("Bernard Jomier : « La bureaucratie à l'hôpital est le fruit d'une mauvaise administration »", "Acteurs publics (Bastien Scordia)", "9 juillet 2025",
  "https://acteurspublics.fr/articles/bernard-jomier-la-bureaucratie-a-lhopital-est-le-fruit-dune-mauvaise-administration/",
  "Le président de la commission d'enquête du Sénat sur l'hôpital juge que la France ne se distingue pas fortement de ses voisins : « Nous ne sommes pas dans des niveaux à près de 50% de postes de direction et administratifs dans nos hôpitaux. » Un syndicat de directeurs fait état de plus de 200 demandes de reporting par an.",
  "Presse spécialisée du secteur public (entretien).", 'media'))

# ── Sources : histoire, international, écologie ─────────────────────────────
LDH_MAYER = ('ldh_mayer', src("Unité et diversité des préjugés racistes et antisémites (Droits & Libertés n° 214)", "Nonna Mayer (CEE Sciences Po / CNRS), revue de la Ligue des droits de l'Homme", "juillet 2026",
  "https://www.ldh-france.org/wp-content/uploads/2026/07/DL214-Dossier-3.-Unite-et-diversite-des-prejuges-racistes-et-antisemites.pdf",
  "D'après le baromètre CNCDH/Ipsos de fin 2025, l'adhésion aux préjugés antisémites a baissé de 7 points en trois ans chez les sympathisants RN et augmenté de 10 points chez ceux de LFI ; fin 2025, 48 % (RN) et 47 % (LFI) ont un score égal ou supérieur à 2 sur 5, un niveau « jamais atteint jusqu'ici chez les Insoumis ». L'autrice parle d'une instrumentalisation de l'antisémitisme « à front renversé » depuis le 7 octobre. Les proches de la gauche ont un indice de tolérance supérieur à 80, ceux du RN de 50.",
  "Analyse d'une politiste de référence, co-autrice de la partie sondage du rapport de la CNCDH.", 'etude'))
CNCDH_CP25 = ('cncdh_cp25', src("Rapport 2025 sur la lutte contre le racisme, l'antisémitisme et la xénophobie (communiqué de presse)", "Commission nationale consultative des droits de l'homme (CNCDH)", "25 juin 2026",
  "https://www.cncdh.fr/sites/default/files/2026-06/25.06.2026%20CP%20Rapport%20Racisme%202025.pdf",
  "1 320 faits antisémites ont été recensés en 2025 par le ministère de l'Intérieur, un niveau jugé « très inquiétant ». 35 % des personnes interrogées pensent que « les Juifs ont un rapport particulier à l'argent ». L'indice longitudinal de tolérance est de 64 sur 100.",
  "Autorité administrative indépendante."))
PS_LEPEN_DETAIL = ('ps_lepen_detail', src("Chambres à gaz qualifiées de « détail » : Jean-Marie Le Pen définitivement condamné", "Public Sénat", "27 mars 2018",
  "https://www.publicsenat.fr/actualites/politique/chambres-a-gaz-qualifiees-de-detail-jean-marie-le-pen-definitivement-condamne",
  "La Cour de cassation rend définitive la condamnation de Jean-Marie Le Pen à 30 000 euros d'amende pour contestation de crime contre l'humanité : il avait de nouveau qualifié les chambres à gaz de « détail » de l'histoire en avril 2015, après une première fois en 1987. Marine Le Pen avait critiqué ces propos ; il a été exclu du parti.",
  "Média parlementaire.", 'media'))
AFP_LEPEN = ('afp_lepen', src("France : les principales condamnations et provocations de Jean-Marie Le Pen", "AFP, publié par JusticeInfo.net", "7 janvier 2025",
  "https://www.justiceinfo.net/fr?p=139986",
  "Condamnations civiles en 1991 et 1999 pour le « point de détail » de 1987 ; en 2012 en appel, trois mois avec sursis et 10 000 € pour avoir dit en 2005 que l'Occupation allemande n'avait pas été « particulièrement inhumaine » ; en 1993, amende pour injure publique pour le jeu de mots « Durafour crématoire ».",
  "Récapitulatif d'agence de presse.", 'media'))
ELY_AUDIN = ('ely_audin', src("Déclaration du Président de la République sur la mort de Maurice Audin", "Présidence de la République (Élysée)", "13 septembre 2018",
  "https://www.elysee.fr/emmanuel-macron/2018/09/13/declaration-du-president-de-la-republique-sur-la-mort-de-maurice-audin",
  "La mort de Maurice Audin, arrêté le 11 juin 1957, a été rendue possible par « un système légalement institué qui a favorisé les disparitions ». « Ce système s'est institué sur un fondement légal : les pouvoirs spéciaux », votés en 1956. La torture « restait impunie parce qu'elle était conçue comme une arme contre le FLN ». Les archives de l'État sur ce sujet sont ouvertes à la libre consultation.",
  "Déclaration officielle du chef de l'État."))
ELY_BOUMENDJEL = ('ely_boumendjel', src("Reconnaissance par la France de l'assassinat d'Ali Boumendjel", "Présidence de la République (Élysée)", "2 mars 2021",
  "https://www.elysee.fr/emmanuel-macron/2021/03/02/reconnaissance-par-la-france-de-lassassinat-dali-boumendjel",
  "Ali Boumendjel, arrêté par l'armée française et détenu au secret, a été tué le 23 mars 1957 : « Il a été torturé puis assassiné. » Paul Aussaresses « avoua lui-même avoir ordonné à l'un de ses subordonnés de le tuer et de maquiller le crime en suicide ». Cette reconnaissance figurait parmi les recommandations du rapport de Benjamin Stora.",
  "Communiqué officiel du chef de l'État."))
BRANCHE = ('branche', src("Torturer des terroristes ? Justifications, méthodes et effets du recours à la torture dans une guerre « contre le terrorisme ». L'exemple de la France en Algérie, 1954-1962", "Raphaëlle Branche (Université Paris 1), publié par le CICR", "septembre 2007",
  "https://www.icrc.org/fre/assets/files/other/irrc-867-branche.pdf",
  "La torture y est décrite comme « massive » : « une violence quotidienne, banale, utilisée indifféremment en ville ou dans les montagnes », visant surtout des civils soupçonnés d'aider les maquis ; l'électricité était « la technique la plus utilisée ». Les tortures sont « le plus souvent le fait de certains soldats particuliers », du renseignement et des détachements spécialisés ; il est « interdit d'affirmer que l'ensemble des officiers de renseignement ont eu recours à la torture ». Mais « aucun responsable militaire n'est sanctionné pour ces méthodes ».",
  "Article d'une historienne universitaire de référence (2007).", 'etude'))
BNF_TRAITE = ('bnf_traite', src("Slave trade (Patrimoines partagés France-Amériques)", "Bibliothèque nationale de France (Cécile Vidal)", "mai 2021",
  "https://heritage.bnf.fr/france-ameriques/en/slave-trade-1",
  "D'après la base Slave Voyages, 4 118 expéditions sous pavillon français ont déporté 1 381 404 Africains entre 1551 et 1875, soit 11 % de la traite transatlantique (plus de 12,5 millions de personnes) ; environ 13 % des captifs sont morts pendant la traversée ; Nantes a organisé 44 % des expéditions. La Convention a aboli l'esclavage le 4 février 1794 ; Bonaparte l'a rétabli le 20 mai 1802.",
  "Institution patrimoniale publique."))
SEN_TRAITE = ('sen_traite', src("Rapport n° 262 (1999-2000) sur la proposition de loi tendant à la reconnaissance de la traite et de l'esclavage en tant que crime contre l'humanité", "Sénat, commission des lois (Jean-Pierre Schosteck)", "8 mars 2000",
  "https://www.senat.fr/rap/l99-262/l99-2621.pdf",
  "Le Code noir (1685) a servi de cadre juridique à l'esclavage pendant plus de 160 ans. Abolitions : 4 février 1794 dans toutes les colonies, rétablissement en 1802, décret du 4 mars 1848 et modalités du 27 avril 1848. Le rapport rappelle aussi la traite arabo-musulmane, antérieure et étendue à partir du VIIe siècle.",
  "Rapport parlementaire (2000)."))
AN_TAUBIRA = ('an_taubira', src("Question écrite n° 13957 et réponse du ministère de l'Europe et des Affaires étrangères", "Assemblée nationale (17e législature)", "réponse publiée le 2 juin 2026",
  "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE13957",
  "Le gouvernement rappelle que la France a été le premier pays à reconnaître la traite et l'esclavage comme « crime contre l'humanité » par la loi dite « Taubira », visant les crimes « perpétrés à partir du XVe siècle, aux Amériques, aux Caraïbes, dans l'Océan Indien et en Europe ». La France s'est abstenue sur une résolution de l'ONU portée par le Ghana, au motif qu'elle refuse de hiérarchiser les crimes contre l'humanité.",
  "Réponse ministérielle officielle."))
COTTIAS = ('cottias', src("Quand la science permet de penser les réparations coloniales", "Myriam Cottias (CNRS), JusticeInfo.net", "25 juin 2021",
  "https://www.justiceinfo.net/fr/79113-quand-science-permet-penser-reparations-coloniales.html",
  "Après l'abolition de 1848, la France a versé 126 millions de francs-or aux propriétaires d'esclaves, et non aux esclaves. Haïti a dû payer une « dette de l'indépendance » de 90 millions de francs-or, remboursée jusqu'en 1887. À la Martinique, 30 à 40 % des bénéficiaires de l'indemnité étaient de petits propriétaires dits « de couleur ».",
  "Tribune d'une historienne du CNRS.", 'etude'))
ASOM_TRAITE = ('asom_traite', src("Compte rendu de Être esclave. Afrique-Amériques, XVe-XIXe siècles (C. Coquery-Vidrovitch et É. Mesnard)", "Académie des sciences d'outre-mer (Yves Rodrigue, Jean-Marie Breton)", "non daté (ouvrage de 2013)",
  "https://www.academieoutremer.fr/images/files/Etre-Esclave-Afrique-Amerique-(59_404)(1).pdf",
  "Les Portugais « s'engagèrent dans le commerce des esclaves avec les négriers africains et arabo-musulmans » ; les forts européens négociaient avec des négriers locaux. Ces réseaux sont devenus particulièrement efficaces « quand la demande explosa avec le développement de la production sucrière dans les îles atlantiques ».",
  "Compte rendu d'un ouvrage d'historiennes universitaires.", 'secondaire'))
TRESOR_RU = ('tresor_ru', src("Situation économique et financière de la Russie en 2025", "Direction générale du Trésor", "30 juin 2026",
  "https://www.tresor.economie.gouv.fr/Pays/RU/situation-economique-et-financiere-de-la-russie-mai-2018",
  "Croissance de 4,9 % en 2024 puis 1 % en 2025, un « atterrissage » après deux ans de surchauffe due au « keynésianisme de guerre ». Inflation : pic d'environ 18 % en avril 2022, 5,59 % en décembre 2025. Taux directeur monté jusqu'à 21 %, 16 % depuis décembre 2025. Recettes pétrolières et gazières en baisse de 23,8 % en 2025 avec la baisse des cours ; déficit de 2,6 % du PIB et TVA relevée à 22 %. La page ne chiffre pas l'effet propre des sanctions.",
  "Administration économique française."))
CE_SANCTIONS = ('ce_sanctions', src("Les sanctions contre la Russie fonctionnent", "Représentation en France de la Commission européenne", "17 mai 2024",
  "https://france.representation.ec.europa.eu/informations/les-sanctions-contre-la-russie-fonctionnent-2024-05-17_fr",
  "Selon la Commission, l'État russe aurait environ 400 milliards d'euros de moins à dépenser et est passé d'un excédent budgétaire à un déficit de 2 à 3 %. Les importations européennes de brut russe par voie maritime ont baissé de 90 % fin 2022 ; environ 95 % de la flotte aérienne russe ne peut plus être correctement entretenue.",
  "Communication de l'institution qui sanctionne, à lire avec recul."))
CE_GAZ = ('ce_gaz', src("Une feuille de route pour mettre un terme à la dépendance de l'UE à l'égard de l'énergie russe", "Commission européenne", "6 mai 2025",
  "https://commission.europa.eu/news-and-media/news/roadmap-fully-end-eu-dependency-russian-energy-2025-05-06_fr",
  "Grâce à REPowerEU, la part du gaz russe dans les importations de l'UE est passée « de 45 % à 19 % » ; la page signale un rebond des importations de gaz russe en 2024.",
  "Communication officielle de l'Union européenne."))
EUROSTAT_INF = ('eurostat_inf', src("Jährliche Inflation im Euroraum auf 10,7 % gestiegen (estimation rapide, communiqué 122/2022)", "Eurostat", "31 octobre 2022",
  "https://ec.europa.eu/eurostat/documents/2995521/15131964/2-31102022-AP-DE.pdf",
  "L'inflation de la zone euro atteint 10,7 % sur un an en octobre 2022 (estimation rapide) ; la composante énergie atteint 41,9 %.",
  "Statistique officielle européenne."))
BDF_ENERGIE = ('bdf_energie', src("Solde énergétique en 2022 : la crise de la production électronucléaire survenue au pire moment (Bloc-notes Éco n° 329)", "Banque de France (G. Gaulier, C. Serfaty)", "24 novembre 2023",
  "https://www.banque-france.fr/fr/publications-et-statistiques/publications/solde-energetique-en-2022-la-crise-de-la-production-electronucleaire-survenue-au-pire-moment",
  "La balance énergétique française « s'est dégradée de 68 milliards d'euros » en 2022. La guerre en Ukraine a amplifié une hausse du gaz engagée dès l'été 2021, et la baisse de la production nucléaire a coûté à elle seule environ 16 milliards d'euros en 2022.",
  "Analyse de la banque centrale."))
SPF_AIR = ('spf_air', src("Pollution de l'air ambiant : nouvelles estimations de son impact sur la santé des Français", "Santé publique France", "14 avril 2021",
  "https://www.santepubliquefrance.fr/presse/pollution-de-lair-ambiant-nouvelles-estimations-de-son-impact-sur-la-sante-des-francais",
  "Près de 40 000 décès par an sont attribuables aux particules fines PM2,5 chez les 30 ans et plus (2016-2019), soit 7 % de la mortalité totale, contre 9 % en 2007-2008 ; la perte moyenne d'espérance de vie est d'environ 8 mois. L'agence constate une « tendance à la baisse ».",
  "Agence nationale de santé publique (données 2016-2019)."))
AEE_FR = ('aee_fr', src("Health impacts of air pollution – France (Europe's environment 2025)", "Agence européenne pour l'environnement", "29 septembre 2025",
  "https://www.eea.europa.eu/en/europe-environment-2025/countries/france/health-impacts-of-air-pollution",
  "Les décès prématurés liés aux PM2,5 ont baissé de 47 % en France entre 2005 et 2022 (45 % dans l'UE) ; les émissions de PM2,5 ont baissé d'environ 50 % et les concentrations d'environ 42 % (2009-2022). Les méthodes de l'Agence et de Santé publique France diffèrent et ne sont pas directement comparables.",
  "Agence de l'Union européenne."))
OMS_AIR = ('oms_air', src("Pollution de l'air ambiant (extérieur) et santé : principaux repères", "Organisation mondiale de la santé (Nations unies)", "24 octobre 2024",
  "https://www.who.int/fr/news-room/fact-sheets/detail/ambient-(outdoor)-air-quality-and-health",
  "4,2 millions de décès prématurés par an dans le monde sont liés à la pollution de l'air ambiant (estimation 2019) ; 99 % de la population mondiale vivait en 2019 au-delà des seuils de l'OMS. Les cardiopathies ischémiques et les AVC représentent 68 % de ces décès.",
  "Organisation internationale."))
SDES_AIR = ('sdes_air', src("Bilan de la qualité de l'air extérieur en France en 2024", "SDES, ministère de la Transition écologique", "2025",
  "https://www.statistiques.developpement-durable.gouv.fr/bilan-de-la-qualite-de-lair-exterieur-en-france-en-2024",
  "Les émissions de la plupart des polluants ont baissé entre 2000 et 2024 ; les concentrations de PM10, PM2,5 et NO2 diminuent. En 2024, les valeurs limites ont encore été dépassées pour le NO2 dans 2 agglomérations et pour les PM10 dans 3 ; la valeur cible d'ozone l'a été dans 17 agglomérations (moyenne 2022-2024).",
  "Statistique publique."))

# ══ FICHES ══════════════════════════════════════════════════════════════════

# 1 ── Regroupement familial : les chiffres ──────────────────────────────────
FICHES.append(fiche(
 id='regroupement-familial-chiffres', affirmation="Le regroupement familial fait venir des centaines de milliers d'immigrés chaque année.", volet='immigration', sous_theme='Immigration et démographie',
 mots_cles=['regroupement familial', 'regroupements familiaux', 'immigration familiale', 'faire venir sa famille', 'titres familiaux', 'regroupement des familles'],
 verdict='contredit', fiabilite='etabli',
 resume="Non. Le regroupement familial au sens strict, c'est environ 13 000 titres de séjour en 2023, soit 5 % des premiers titres. Même en comptant toute l'immigration familiale (conjoints de Français, familles d'Européens, liens personnels), on arrive à environ 81 000 titres, loin des « centaines de milliers ». Et les conditions sont strictes : ressources au niveau du SMIC, logement adapté, 18 mois de séjour régulier.",
 contexte="Le regroupement familial est souvent présenté comme la grande porte d'entrée de l'immigration ; il est au cœur des programmes du RN et de Reconquête.",
 explication="Le regroupement familial permet à un étranger en situation régulière de faire venir son conjoint et ses enfants mineurs. Il ne faut pas le confondre avec l'immigration familiale au sens large, qui comprend surtout les conjoints et parents de Français.",
 sources=[INED_RF, HERAN_VC, PS_RF, PS_TITRES],
 faits=[
  fait("En 2023, 12 885 titres ont été délivrés au titre du regroupement familial, soit 5 % des premiers titres d'au moins un an ; la moyenne 2000-2023 est d'environ 11 000 par an.", 'ined_rf', '2000-2023', 'France', "Le regroupement familial pèse peu dans les entrées.", 'etabli', '12 885 titres'),
  fait("Au sens large, l'immigration familiale représente 81 032 titres en 2023, soit 31 % des premières délivrances.", 'ined_rf', '2023', 'France', "Même au sens large, on est loin des centaines de milliers.", 'etabli', '81 032 titres'),
  fait("En 2023, 82 % des 15 780 demandes de regroupement familial ont été acceptées ; les refus tiennent surtout aux ressources et au logement.", 'ined_rf', '2023', 'France', "Les conditions sont réellement contrôlées.", 'etabli'),
  fait("Selon Public Sénat, il faut 18 mois de séjour régulier, des ressources au moins égales au SMIC et un logement « normal » pour une famille comparable de la même région.", 'ps_rf', '2023', 'France', "Les conditions sont exigeantes.", 'etabli'),
  fait("Selon la statistique publique relayée par Public Sénat, 384 230 premiers titres ont été délivrés en 2025, le motif étudiant arrivant en tête (118 000).", 'ps_titres', '2025', 'France', "Le premier motif d'entrée n'est pas familial.", 'etabli'),
 ],
 court="Faux : le regroupement familial, c'est environ 13 000 titres par an, 5 % des entrées. Toute l'immigration familiale réunie, conjoints de Français compris, fait environ 81 000 titres. On est très loin des centaines de milliers.",
 moyen="Le regroupement familial au sens strict a concerné 12 885 titres en 2023, selon l'Ined. C'est environ 5 % des premiers titres de séjour. Il faut des ressources au niveau du SMIC, un logement adapté et 18 mois de séjour régulier, et près d'une demande sur cinq est refusée.\n\nL'immigration familiale au sens large, qui inclut les conjoints et parents de Français, représente environ 81 000 titres, soit 31 % des entrées. C'est important, mais c'est loin des centaines de milliers, et cela concerne souvent des personnes déjà installées en France depuis des années.",
 detaille="Le regroupement familial permet à un étranger installé régulièrement de faire venir son conjoint et ses enfants mineurs. Selon l'Ined, il a donné lieu en moyenne à environ 11 000 titres par an entre 2000 et 2023, et à 12 885 en 2023. C'était 20 000 à 32 000 par an à la fin des années 1980 : la voie est devenue plus rare.\n\nLes conditions sont strictes : ressources au moins égales au SMIC hors prestations, logement adapté à la taille de la famille, 18 mois de séjour régulier. En 2023, 18 % des demandes ont été refusées.\n\nCe qui est souvent appelé « regroupement familial » est en réalité l'immigration familiale au sens large : 81 032 titres en 2023, dont beaucoup pour des conjoints de Français. Selon le démographe François Héran, environ 40 % des premiers titres familiaux concernent des personnes déjà entrées en France depuis au moins neuf ans. Au total, la France a délivré 384 230 premiers titres en 2025, le premier motif étant les études.",
 empathie="On peut se demander combien de personnes arrivent par la famille, c'est une vraie question. Les chiffres officiels donnent une réponse précise, bien plus modeste que ce qu'on entend souvent.",
 legitimes=["L'immigration familiale au sens large reste un flux important, environ un tiers des premiers titres.", "Les sénateurs jugent que l'immigration en France demeure « largement familiale »."],
 contre=[
  ("Avec les conjoints de Français, ça fait beaucoup.", "Oui, l'immigration familiale au sens large représente environ 81 000 titres, mais elle concerne surtout des couples formés avec des Français, pas le regroupement familial."),
  ("Les chiffres sont cachés.", "Ils sont publiés chaque année par le ministère de l'Intérieur et analysés par l'Ined."),
 ],
 questions=["Sais-tu combien de titres de séjour sont délivrés chaque année au titre du regroupement familial ?", "Faut-il empêcher un Français d'épouser une personne étrangère ?"],
 limites=["Les chiffres détaillés lus s'arrêtent à 2023 ; le total familial de 2025 n'a pas été lu.", "Les pages du ministère de l'Intérieur n'ont pas pu être ouvertes : les chiffres viennent de l'Ined et de Public Sénat."],
 publics={'convaincus': "Le regroupement familial, c'est 12 885 titres en 2023, soit 5 % des entrées, selon l'Ined. Et il faut gagner au moins le SMIC, avoir un logement assez grand et 18 mois de séjour régulier. Les « centaines de milliers », ce chiffre n'existe dans aucune statistique.",
  'indecis': "La question est légitime : selon l'Ined, l'immigration familiale au sens large représente environ un tiers des titres, 81 000 en 2023. Mais il s'agit surtout de conjoints de Français ; le regroupement familial au sens strict ne concerne qu'environ 13 000 personnes par an, sous conditions strictes."},
 a_actualiser='2027-06-30', raison="Nouvelles statistiques annuelles des titres de séjour.",
))

# 2 ── Le RN et le regroupement familial ─────────────────────────────────────
FICHES.append(fiche(
 id='rn-regroupement-familial', affirmation="Le RN veut supprimer le regroupement familial.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['supprimer le regroupement familial', 'fin du regroupement familial', 'interdire le regroupement familial', 'rn regroupement familial', 'le pen regroupement familial'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="Plutôt vrai : en 2022, Marine Le Pen proposait la fin du regroupement familial, et la proposition de loi constitutionnelle du RN de 2024 prévoit qu'il « peut être limité ou interdit ». Mais son programme des législatives 2024 se limitait à un « durcissement ». Une suppression se heurterait à la Constitution, qui protège depuis 1993 le droit de mener une vie familiale normale, et au droit européen : le RN propose donc de changer la Constitution et d'écarter les traités.",
 contexte="La mesure revient à chaque élection ; elle suppose une réforme constitutionnelle par référendum.",
 explication="Le droit de vivre avec sa famille est protégé par le Préambule de 1946, la Convention européenne des droits de l'homme et une directive européenne de 2003. Supprimer le regroupement familial suppose de modifier la Constitution et d'écarter des engagements européens.",
 sources=[LCP_LEPEN22, AN_PPLC_RN, LCP_RN24, UT_9325, EU_DIR],
 faits=[
  fait("Selon LCP, en 2022, Marine Le Pen réclamait la fin du regroupement familial, par une révision constitutionnelle soumise à référendum.", 'lcp_lepen22', '2022', 'France', "La suppression a bien été proposée.", 'etabli'),
  fait("La proposition de loi constitutionnelle du RN de janvier 2024 prévoit : « Le regroupement familial des étrangers peut être limité ou interdit. »", 'an_pplc_rn', '2024', 'France', "Le RN veut se donner le pouvoir de l'interdire.", 'etabli'),
  fait("Le même texte du RN prévoit que les juridictions laissent inappliquées les règles internationales contraires à la Constitution, et qu'un acte européen contraire « ne peut produire d'effets ».", 'an_pplc_rn', '2024', 'France', "La mesure suppose d'écarter le droit européen.", 'etabli'),
  fait("Selon LCP, le programme des législatives 2024 parlait seulement d'un « durcissement des conditions du regroupement familial ».", 'lcp_rn24', '2024', 'France', "Le discours varie selon les élections.", 'etabli'),
  fait("Selon sa décision de 1993, le Conseil constitutionnel reconnaît aux étrangers le droit de mener une vie familiale normale, qui leur permet de faire venir conjoint et enfants mineurs.", 'ut_9325', '1993', 'France', "Une simple loi ne suffit pas.", 'etabli'),
  fait("La directive européenne 2003/86/CE oblige les États à autoriser l'entrée du conjoint et des enfants mineurs, sous conditions de ressources et de logement.", 'eu_dir', '2003', 'Union européenne', "La suppression contredit le droit européen.", 'etabli'),
 ],
 court="Plutôt vrai : le RN a proposé en 2022 la fin du regroupement familial et veut inscrire dans la Constitution qu'il peut être « interdit ». Mais c'est contraire au droit de vivre en famille, protégé par la Constitution et le droit européen.",
 moyen="En 2022, Marine Le Pen proposait de mettre fin au regroupement familial. En 2024, la proposition de loi constitutionnelle du RN prévoit qu'il « peut être limité ou interdit ». Le programme des législatives 2024, lui, parlait seulement de durcissement.\n\nPour aller jusqu'à la suppression, il faudrait réviser la Constitution, qui protège depuis 1993 le droit de mener une vie familiale normale, et écarter une directive européenne. Le RN le sait : son texte demande aux juges de laisser de côté les traités contraires. C'est une rupture avec l'État de droit européen.",
 detaille="Le RN a bien porté la fin du regroupement familial. En 2022, selon LCP, Marine Le Pen la réclamait par un référendum constitutionnel. En janvier 2024, la proposition de loi constitutionnelle de son groupe prévoit que le regroupement familial « peut être limité ou interdit ». Le programme des législatives de 2024 se contentait d'un « durcissement des conditions ».\n\nCe n'est pas un détail juridique. Depuis 1993, le Conseil constitutionnel reconnaît aux étrangers en situation régulière le droit de mener une vie familiale normale, donc de faire venir leur conjoint et leurs enfants mineurs. La directive européenne de 2003 oblige aussi les États à l'autoriser, sous conditions. Le texte du RN prévoit donc que les juges écartent les règles internationales et européennes contraires.\n\nLe vrai débat porte sur ce prix : séparer durablement des parents et des enfants en situation régulière, et sortir de fait du cadre européen. Les conditions du regroupement peuvent déjà être durcies dans le cadre actuel : délai de séjour, ressources, logement.",
 empathie="On peut vouloir mieux maîtriser l'immigration sans souhaiter séparer des parents de leurs enfants. C'est pour ça qu'il vaut mieux savoir exactement ce que propose le RN et ce que cela implique.",
 legitimes=["Le droit au regroupement familial n'est pas absolu : des conditions de ressources, de logement et de délai sont permises.", "Le programme législatif de 2024 du RN ne parlait que de durcissement."],
 contre=[
  ("D'autres pays l'ont restreint.", "Restreindre est possible dans le cadre européen ; interdire ne l'est pas sans sortir de ce cadre."),
  ("Il suffit d'un référendum.", "Le RN le propose, mais il faudrait aussi écarter la directive européenne et la Convention européenne des droits de l'homme."),
 ],
 questions=["Que penses-tu d'une loi qui empêcherait un travailleur en règle de vivre avec ses enfants ?", "Sais-tu que le RN propose que les juges écartent les traités européens ?"],
 limites=["La décision de 1993 a été lue dans une traduction universitaire, la page du Conseil constitutionnel n'ayant pas pu être ouverte.", "Le programme du RN pour 2027 n'a pas été vérifié."],
 publics={'convaincus': "Le RN l'a bien proposé en 2022, et son texte de 2024 permet de l'« interdire ». Mais pour ça, il faut réécrire la Constitution et demander aux juges d'ignorer les traités européens. Tu es prêt à ce qu'un travailleur en règle, qui paie ses impôts, ne puisse plus vivre avec ses enfants ?",
  'indecis': "C'est vrai, le RN veut pouvoir supprimer le regroupement familial, même si son programme de 2024 parlait seulement de durcissement. Le droit de vivre en famille est protégé par la Constitution depuis 1993 et par le droit européen. Il est déjà possible de durcir les conditions sans aller jusqu'à cette rupture."},
 a_actualiser='2027-06-30', raison="Programme du RN pour 2027.",
))

# 3 ── Étudiants étrangers ───────────────────────────────────────────────────
FICHES.append(fiche(
 id='etudiants-etrangers-immigration', affirmation="Les étudiants étrangers, c'est une immigration déguisée.", volet='immigration', sous_theme='Économie et immigration',
 mots_cles=['etudiants etrangers', 'etudiants internationaux', 'visa etudiant', 'titre etudiant', 'immigration deguisee', 'faux etudiants', 'etudiants africains'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. Les études sont devenues le premier motif de titre de séjour (118 000 en 2025), mais une majorité d'étudiants repart : selon l'OCDE, environ 43 % étaient encore en France cinq ans après leur premier titre. Ceux qui restent passent surtout vers un titre de travail, par une voie légale. Et selon Campus France, leur apport économique dépasse leur coût public.",
 contexte="L'idée d'une « filière étudiante » détournée circule depuis que le motif étudiant a dépassé les autres motifs de titres.",
 explication="Un titre étudiant est temporaire. À la fin des études, la personne part, ou demande un autre titre (travail, famille), qui obéit à ses propres conditions.",
 sources=[PS_TITRES, CAMPUS_25, OCDE_ETU, CAMPUS_ECO, MESR_BEF],
 faits=[
  fait("Selon la statistique publique relayée par Public Sénat, 118 000 premiers titres ont été délivrés pour motif étudiant en 2025, le premier motif.", 'ps_titres', '2025', 'France', "Le flux est réel et important.", 'etabli', '118 000 titres'),
  fait("Selon Campus France, plus de 430 000 étudiants étrangers étaient en France en 2023-2024, un nombre qui progresse moins vite que la moyenne mondiale.", 'campus_25', '2023-2024', 'France', "La France n'est pas une exception.", 'etabli'),
  fait("Pour la cohorte des premiers titres étudiants de 2015, environ 43 % étaient encore en France cinq ans après, contre environ 30 % en moyenne dans l'OCDE.", 'ocde_etu', '2015-2020', 'France et OCDE', "Une majorité repart, mais la France retient plus que la moyenne.", 'etabli', '43 %'),
  fait("Plus de trois anciens étudiants sur quatre qui changent de statut passent vers un titre de travail ; dix ans après, 10 % ont un titre familial.", 'ocde_etu', '2010-2020', 'France', "Ceux qui restent travaillent surtout.", 'etabli'),
  fait("Selon une étude de Campus France et Kantar, les étudiants internationaux apportent 5 Md€ à l'économie française, pour un apport net estimé à 1,35 Md€.", 'campus_eco', '2022', 'France', "Leur bilan économique est jugé positif.", 'estimation'),
 ],
 court="Trompeur : une majorité des étudiants étrangers repart après ses études. Ceux qui restent passent surtout par un titre de travail, une voie légale. Et leur apport économique est estimé supérieur à leur coût.",
 moyen="Les études sont bien devenues le premier motif de titre de séjour : 118 000 en 2025. Mais un titre étudiant est temporaire. Selon l'OCDE, environ 43 % des étudiants arrivés en 2015 étaient encore en France cinq ans après : la majorité est repartie.\n\nCeux qui restent obtiennent surtout un titre de travail, après avoir été formés ici : c'est la loi qui le permet, pas une fraude. Et selon Campus France, leurs dépenses rapportent davantage que ce qu'ils coûtent à l'État.",
 detaille="Plus de 430 000 étudiants étrangers étaient en France en 2023-2024, et les études sont le premier motif de premier titre de séjour, avec 118 000 titres en 2025. Ce flux augmente, mais moins vite que la moyenne mondiale : la France est le septième pays d'accueil.\n\nSelon l'OCDE, pour la cohorte de 2015, environ 43 % étaient encore en France cinq ans après. C'est plus que la moyenne de l'OCDE, d'environ 30 % : une minorité importante s'installe. Mais elle s'installe surtout par le travail : plus de trois changements de statut sur quatre vont vers un titre professionnel, et les anciens étudiants fournissent 52 % des admissions pour motif professionnel. Dix ans après, seulement 10 % ont un titre familial.\n\nSur le plan économique, une étude de Campus France estime l'apport à 5 Md€ et le solde net à 1,35 Md€. Les frais différenciés pour les étudiants extra-européens, instaurés en 2019, restent inférieurs au tiers du coût réel de la formation.",
 empathie="Il est normal de se demander si les visas étudiants sont détournés. Les données disponibles montrent plutôt des jeunes formés ici, dont une partie reste pour travailler.",
 legitimes=["Environ 43 % sont encore là cinq ans après, au-dessus de la moyenne de l'OCDE.", "L'étude sur l'apport économique a été commandée par Campus France, partie prenante."],
 contre=[
  ("Ils viennent pour rester.", "La majorité repart ; ceux qui restent passent par un titre de travail, après avoir été formés en France."),
  ("Ils coûtent cher à nos universités.", "Selon Campus France, leurs dépenses rapportent plus que leur coût public ; cette estimation vient toutefois d'un acteur concerné."),
 ],
 questions=["Si un étudiant formé ici trouve un emploi qualifié, vaut-il mieux qu'il reste ou qu'il parte ?", "Sais-tu combien d'étudiants étrangers repartent après leurs études ?"],
 limites=["Les données de l'OCDE portent sur la cohorte 2015 ; elles sont anciennes.", "L'étude économique de 2022 est commandée par Campus France et n'a pas été vérifiée de façon indépendante."],
 publics={'convaincus': "Une majorité des étudiants étrangers repart : selon l'OCDE, 43 % seulement sont encore en France cinq ans après. Et ceux qui restent passent surtout par un titre de travail, après avoir été formés ici. Où est le déguisement, si c'est la loi qui le prévoit ?",
  'indecis': "Le motif étudiant est devenu le premier motif de titre de séjour, c'est vrai. Mais la plupart repartent, et ceux qui restent travaillent le plus souvent. Si l'on veut en débattre, la vraie question est celle des métiers où la France a besoin de diplômés."},
 a_actualiser='2027-06-30', raison="Nouvelles données de Campus France et de l'OCDE.",
))

# 4 ── Schengen et les frontières ────────────────────────────────────────────
FICHES.append(fiche(
 id='schengen-controles-frontieres', affirmation="Schengen empêche la France de contrôler ses frontières.", volet='politique', sous_theme='Union européenne',
 mots_cles=['schengen', 'espace schengen', 'controle aux frontieres', 'controles aux frontieres', 'retablir les frontieres', 'frontieres interieures', 'frontieres nationales', 'code frontieres'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux. La France contrôle ses frontières intérieures sans interruption depuis novembre 2015, en renouvelant tous les six mois des contrôles que le code Schengen prévoit lui-même en cas de menace grave. Le Conseil d'État les a jugés conformes en 2025, et les notifications courent jusqu'en avril 2027. Schengen encadre la durée et la proportionnalité de ces contrôles : la Commission a demandé en 2026 leur levée progressive.",
 contexte="L'idée que l'Europe nous interdit d'avoir des frontières nourrit les appels à sortir de Schengen.",
 explication="Schengen supprime les contrôles systématiques entre pays membres, mais permet de les rétablir temporairement en cas de menace grave pour l'ordre public ou la sécurité intérieure. Les frontières extérieures restent contrôlées.",
 sources=[CE_SCHENGEN, CE_NOTIF, PE_SCHENGEN, MOT_SCH, PS_CC_FRONT],
 faits=[
  fait("Après les attentats de novembre 2015, la France a rétabli des contrôles à ses frontières avec les États Schengen, « reconduit tous les six mois » sans interruption.", 'ce_schengen', '2015-2025', 'France', "Les contrôles existent depuis dix ans.", 'etabli'),
  fait("Le Conseil d'État a jugé en 2025 la réintroduction des contrôles conforme au règlement Schengen modifié en 2024 et a rejeté le recours des associations.", 'ce_schengen', '2025', 'France', "Ces contrôles sont légaux au regard du droit européen.", 'etabli'),
  fait("Les notifications de la France à la Commission européenne couvrent notamment la période du 1er novembre 2026 au 30 avril 2027, pour toutes ses frontières intérieures.", 'ce_notif', '2026-2027', 'France', "Les contrôles continuent.", 'etabli'),
  fait("La réforme du code Schengen de 2024 permet des contrôles jusqu'à deux ans en cas de menace grave, avec une prolongation possible d'un an, et crée une procédure de transfert vers l'État voisin.", 'pe_schengen', '2024', 'Union européenne', "Le cadre européen a même renforcé les outils.", 'etabli'),
  fait("Selon la Mission opérationnelle transfrontalière, la Commission a recommandé en juin 2026 une levée progressive des contrôles, qui doivent rester « exceptional, temporary and proportionate ».", 'mot_sch', '2026', 'Union européenne', "Schengen limite bien la durée des contrôles.", 'etabli'),
  fait("Selon Public Sénat, la Cour des comptes juge l'organisation entre police aux frontières et douanes « pas suffisamment optimisée ».", 'ps_cc_front', '2024', 'France', "Les faiblesses relevées sont nationales.", 'etabli'),
 ],
 court="Faux : la France contrôle ses frontières intérieures depuis novembre 2015, sans interruption, en utilisant une possibilité prévue par Schengen lui-même. Le Conseil d'État a validé ces contrôles en 2025.",
 moyen="Depuis les attentats de 2015, la France a rétabli des contrôles à toutes ses frontières avec ses voisins européens, et les renouvelle tous les six mois. Le code Schengen prévoit cette possibilité en cas de menace grave, et la réforme de 2024 l'a même précisée.\n\nSchengen pose des limites : ces contrôles doivent rester exceptionnels et proportionnés, et la Commission a demandé en 2026 qu'ils soient levés progressivement. Mais dire que l'Europe empêche de contrôler les frontières est faux. Les faiblesses pointées par la Cour des comptes tiennent à l'organisation de nos propres services.",
 detaille="Depuis novembre 2015, la France contrôle ses frontières terrestres, maritimes et aériennes avec les autres pays de Schengen. Ces contrôles sont renouvelés tous les six mois, au nom du risque terroriste et de la lutte contre les passeurs. Les notifications envoyées à la Commission courent jusqu'au 30 avril 2027.\n\nCes contrôles ne sont pas une désobéissance à Schengen : ils sont prévus par le code frontières Schengen. Le Conseil d'État les a jugés conformes au nouveau règlement en 2025. La réforme adoptée en 2024 permet des contrôles jusqu'à deux ans, plus un an, et crée une procédure de transfert vers l'État voisin des personnes en situation irrégulière interpellées lors de patrouilles conjointes.\n\nLa limite est réelle : ces contrôles doivent rester temporaires et proportionnés, et la Commission a demandé en juin 2026 leur levée progressive. Selon les autorités françaises, ils ne sont d'ailleurs pas systématiques. Quant aux défaillances relevées par la Cour des comptes, comme l'absence de fichier national des personnes interpellées, elles relèvent de choix nationaux.",
 empathie="L'inquiétude sur le contrôle des frontières est compréhensible. Il faut juste savoir que la France contrôle déjà ses frontières intérieures depuis dix ans, avec l'accord du droit européen.",
 legitimes=["Schengen limite la durée et la proportionnalité des contrôles intérieurs.", "La Commission a demandé en 2026 une levée progressive des contrôles français."],
 contre=[
  ("Les contrôles ne sont pas systématiques.", "C'est un choix d'organisation et de moyens ; contrôler chaque véhicule bloquerait des centaines de milliers de travailleurs frontaliers."),
  ("Il faut sortir de Schengen.", "La France contrôle déjà ses frontières dans Schengen, tout en profitant de la coopération policière et des fichiers européens."),
 ],
 questions=["Savais-tu que la France contrôle ses frontières intérieures depuis 2015 ?", "Que changerait concrètement une sortie de Schengen ?"],
 limites=["Aucune source lue ne chiffre l'efficacité des contrôles (non-admissions, interpellations).", "L'avis de la Commission de juin 2026 n'a été lu qu'à travers une analyse spécialisée."],
 publics={'convaincus': "La France contrôle ses frontières avec ses voisins européens depuis novembre 2015, sans interruption, et le Conseil d'État a jugé ça conforme à Schengen. Ce n'est donc pas l'Europe qui empêche les contrôles. Si ça ne marche pas assez, la Cour des comptes pointe plutôt nos propres services.",
  'indecis': "Schengen supprime les contrôles systématiques, mais permet de les rétablir en cas de menace grave : c'est ce que fait la France depuis 2015. L'Europe demande que ces contrôles restent temporaires et proportionnés. Le débat porte donc sur leur durée et leurs moyens, pas sur leur existence."},
 a_actualiser='2027-04-30', raison="Fin de la période de contrôles notifiée et suites de l'avis de la Commission.",
))

# 5 ── Aide au développement et Afrique ──────────────────────────────────────
FICHES.append(fiche(
 id='aide-developpement-afrique', affirmation="La France donne des milliards d'aide au développement à l'Afrique pour rien.", volet='international', sous_theme='Relations internationales',
 mots_cles=['aide au developpement', 'aide publique au developpement', 'aide a l afrique', 'milliards a l afrique', 'apd', 'afd', 'aide aux pays pauvres'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. La France consacre bien plus de 13 milliards d'euros par an à l'aide au développement, mais l'Afrique n'en reçoit qu'environ 40 %, une partie importante est faite de prêts remboursables, et un quart de l'aide bilatérale ne quitte pas la France (accueil des réfugiés, frais de scolarité d'étudiants). Cette aide baisse fortement : 0,43 % du revenu national en 2025, loin de l'objectif légal de 0,7 %. Son efficacité est mal évaluée, ce qui ne prouve pas qu'elle soit inutile.",
 contexte="L'aide au développement est régulièrement présentée comme un gaspillage, surtout envers les pays d'Afrique en conflit avec la France.",
 explication="L'aide publique au développement regroupe des dons, des prêts à taux avantageux et certaines dépenses faites en France. Elle est comptabilisée selon les règles de l'OCDE.",
 sources=[OCDE_APD, SEN_APD, FOCUS_APD, AFD_8],
 faits=[
  fait("L'aide publique au développement de la France atteint 14,5 milliards de dollars en 2025, soit 0,42 % du revenu national brut, en baisse réelle de 10,9 %.", 'ocde_apd', '2025', 'France', "Il s'agit bien de milliards, mais en forte baisse.", 'etabli', '0,42 % du RNB'),
  fait("Selon le Sénat, l'Afrique représente 40 % de l'aide française ; l'aide est passée de 0,56 % du revenu national en 2022 à 0,43 % en 2025, loin de l'objectif légal de 0,7 %.", 'sen_apd', '2022-2025', 'France', "La majorité de l'aide ne va pas à l'Afrique.", 'etabli', '40 %'),
  fait("Les crédits de la mission aide au développement passent de 5,76 Md€ en 2024 à 3,67 Md€ dans le projet de budget 2026.", 'sen_apd', '2024-2026', 'France', "Les crédits budgétaires reculent fortement.", 'etabli'),
  fait("Selon Focus 2030, en 2022, environ 27 % de l'aide bilatérale ne quittait pas le territoire, dont 1,5 Md€ pour l'accueil des réfugiés et près de 1 Md€ de frais de scolarité d'étudiants étrangers.", 'focus_apd', '2022', 'France', "Une partie de l'aide est dépensée en France.", 'estimation'),
  fait("Selon l'AFD, le groupe a engagé en 2025 plus de 10 Md€ en prêts contre 0,8 Md€ en dons.", 'afd_8', '2025', 'France', "Une grande partie est prêtée, donc remboursée.", 'estimation'),
  fait("Selon le Sénat, la commission d'évaluation de l'aide prévue par la loi de 2021 n'a été installée qu'en 2025.", 'sen_apd', '2021-2025', 'France', "L'évaluation est bien insuffisante.", 'etabli'),
 ],
 court="Trompeur : l'aide française dépasse 13 milliards, mais seulement 40 % vont à l'Afrique, une grande partie sont des prêts remboursés, et un quart de l'aide bilatérale est dépensée en France. Elle baisse fortement, loin des 0,7 % promis.",
 moyen="La France dépense bien plus de 13 milliards d'euros par an au titre de l'aide au développement. Mais selon le Sénat, l'Afrique n'en reçoit qu'environ 40 %. Une part importante prend la forme de prêts, et une autre ne quitte jamais la France : accueil des réfugiés, frais de scolarité d'étudiants étrangers.\n\nCette aide recule fortement : 0,43 % du revenu national en 2025, contre 0,56 % en 2022, alors que la loi fixait 0,7 %. Son efficacité est mal évaluée, c'est un vrai reproche. Mais « pour rien » n'est démontré par aucune source.",
 detaille="Selon l'OCDE, la France a consacré 14,5 milliards de dollars à l'aide publique au développement en 2025, soit 0,42 % de son revenu national, en baisse réelle de 10,9 %. Le Sénat note que l'aide est passée de 0,56 % en 2022 à 0,43 % en 2025, et que les crédits de la mission budgétaire passent de 5,76 Md€ en 2024 à 3,67 Md€ en 2026. L'objectif légal de 0,7 % a été repoussé à 2030.\n\nCes milliards ne vont pas tous en Afrique : environ 40 % selon le Sénat. Une partie importante prend la forme de prêts : en 2025, l'AFD a engagé plus de 10 Md€ de prêts contre 0,8 Md€ de dons. Et selon Focus 2030, environ 27 % de l'aide bilatérale restait en France en 2022, pour l'accueil des réfugiés et la scolarité d'étudiants étrangers.\n\nLe reproche le plus solide est l'évaluation : la commission prévue par la loi de 2021 n'a été installée qu'en 2025. Mais aucune source lue ne démontre que l'aide serait inutile ; l'OCDE note plutôt que la baisse de l'aide mondiale en 2025 est la plus forte jamais enregistrée.",
 empathie="C'est normal de vouloir savoir où va l'argent public. La réponse est plus nuancée qu'un chèque envoyé à l'Afrique : beaucoup de prêts, une partie dépensée en France, et une aide en baisse.",
 legitimes=["L'évaluation de l'efficacité de l'aide est réellement insuffisante.", "Les chiffres de retombées favorables viennent souvent de l'AFD elle-même."],
 contre=[
  ("Cet argent devrait servir aux Français.", "Une partie de l'aide est déjà dépensée en France, et la mission budgétaire a perdu plus de 2 Md€ depuis 2024."),
  ("Ces pays nous insultent et on les paie.", "La France a mis fin à son aide au Mali, au Niger et au Burkina Faso, selon le Sénat."),
 ],
 questions=["Savais-tu qu'une grande partie de l'aide est prêtée et remboursée ?", "Comment évaluer une aide qui finance des écoles ou des hôpitaux ?"],
 limites=["Les chiffres de l'OCDE pour 2025 sont préliminaires.", "Aucune évaluation indépendante de l'impact de l'aide française en Afrique n'a été lue."],
 publics={'convaincus': "Selon le Sénat, seulement 40 % de l'aide française va à l'Afrique. Une grosse partie, ce sont des prêts remboursés, et un quart de l'aide bilatérale est dépensée en France même. Et cette aide baisse : on est passé de 0,56 % à 0,43 % du revenu national en trois ans.",
  'indecis': "La France dépense bien plus de 13 milliards par an en aide au développement, et son évaluation est insuffisante : c'est un reproche fondé. Mais cette aide comprend beaucoup de prêts et de dépenses faites en France, et elle recule fortement. La question est de savoir comment mieux la cibler, pas de croire qu'elle part dans le vide."},
 a_actualiser='2027-06-30', raison="Chiffres définitifs de l'OCDE et budget 2027.",
))

# 6 ── Arrêts maladie ────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='arrets-maladie-abus', affirmation="Les Français abusent des arrêts maladie.", volet='services', sous_theme='Assurance maladie',
 mots_cles=['arrets maladie', 'arret maladie', 'arrets de travail', 'indemnites journalieres', 'faux arrets', 'abus d arrets'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. Les indemnités d'arrêts maladie ont fortement augmenté, de 7,7 à 12 milliards d'euros entre 2017 et 2022. Mais selon la Cour des comptes, une grande partie de la hausse vient du Covid, des hausses de salaires et du vieillissement des actifs, et la fraude détectée est « faible » : 42 millions d'euros en 2024, environ 0,35 % des indemnités. Une part de la hausse, liée à un recours accru, reste mal expliquée.",
 contexte="La hausse des dépenses d'arrêts de travail sert d'argument pour réduire leur indemnisation.",
 explication="Les indemnités journalières dépendent du salaire, du nombre d'actifs et de la durée des arrêts : quand les salaires augmentent et que les actifs vieillissent, la dépense monte mécaniquement.",
 sources=[CC_IJ, DREES_IJ, PS_IJ, LEGI_FRAUDE],
 faits=[
  fait("Les indemnités maladie sont passées de 7,7 Md€ à 12 Md€ entre 2017 et 2022 ; sur 4,3 Md€ de hausse, 1,7 Md€ est imputable à la crise sanitaire et 0,7 Md€ à la hausse du SMIC et des salaires.", 'cc_ij', '2017-2022', 'Régime général', "Une grande partie de la hausse est mécanique.", 'etabli', '+56 %'),
  fait("Les plus de 55 ans représentent 18,3 % des actifs mais 27 % des journées indemnisées ; les arrêts de plus de six mois font 6 % des arrêts mais 45 % de la dépense.", 'cc_ij', '2022', 'Régime général', "La dépense vient surtout d'arrêts longs et de salariés âgés.", 'etabli'),
  fait("La Cour des comptes juge « faible » la fraude détectée aux indemnités, 12,8 M€ en 2022.", 'cc_ij', '2022', 'Régime général', "La fraude n'explique pas la hausse.", 'etabli'),
  fait("Selon un bilan de l'Assurance maladie relayé par Legisocial, la fraude détectée aux indemnités journalières atteint 42 M€ en 2024, contre 17 M€ en 2023.", 'legi_fraude', '2024', 'France', "La fraude progresse, mais reste marginale face à 12 Md€.", 'estimation', '42 M€'),
  fait("En 2024, les indemnités maladie hors Covid progressent encore de 7,0 % ; la hausse du taux de recours et de la durée des arrêts, à âge donné, joue aussi.", 'drees_ij', '2024', 'France', "Une part de la hausse n'est pas mécanique.", 'etabli'),
  fait("Selon l'Assurance maladie citée par Public Sénat, 42 % de la hausse entre 2019 et 2023 vient d'un recours accru et de durées plus longues.", 'ps_ij', '2019-2023', 'France', "Le recours aux arrêts augmente réellement.", 'estimation'),
 ],
 court="Trompeur : la hausse des arrêts maladie vient surtout du Covid, des salaires et du vieillissement des actifs. La fraude détectée est minime, environ 0,35 % des indemnités. Une part de la hausse, liée à plus de recours, reste à expliquer.",
 moyen="Les indemnités d'arrêts maladie ont augmenté de 56 % entre 2017 et 2022. Mais la Cour des comptes a décomposé cette hausse : le Covid en explique une grosse partie, la hausse des salaires une autre, l'allongement des carrières aussi. Les plus de 55 ans font 27 % des journées indemnisées.\n\nLa fraude existe, mais la Cour la juge « faible » : 42 millions d'euros détectés en 2024, pour 12 milliards d'indemnités. Il reste une part de hausse liée à un recours accru, qu'il faut comprendre : conditions de travail, santé mentale, accès aux soins.",
 detaille="Les indemnités journalières maladie du régime général sont passées de 7,7 Md€ en 2017 à 12 Md€ en 2022. Sur 4,3 Md€ de hausse, la Cour des comptes attribue 1,7 Md€ au Covid, 0,7 Md€ aux hausses du SMIC et des salaires, 0,2 Md€ à la hausse du nombre d'actifs et 0,4 Md€ à l'extension aux indépendants. 0,9 Md€ reste inexpliqué.\n\nLa dépense est concentrée : les arrêts de plus de six mois font 6 % des arrêts mais 45 % de la dépense, et les plus de 55 ans 27 % des journées pour 18,3 % des actifs. Le recul de l'âge de la retraite accentue ce phénomène, note la DREES.\n\nLa fraude détectée aux indemnités atteint 42 M€ en 2024, soit environ 0,35 % des 12,1 Md€ versés. Mais tout ne s'explique pas : selon l'Assurance maladie, 42 % de la hausse de 2019 à 2023 tient à un recours accru et à des arrêts plus longs, y compris chez les jeunes. C'est un signal sur la santé au travail plus qu'une preuve de paresse.",
 empathie="On peut être agacé par l'idée que certains abusent. Les contrôles et la lutte contre la fraude sont légitimes. Mais les chiffres montrent surtout des salariés plus âgés, des arrêts longs et un effet du Covid.",
 legitimes=["La dépense augmente encore fortement hors Covid, de 7 % en 2024.", "Une part de la hausse vient d'un recours accru aux arrêts, non expliqué par la démographie."],
 contre=[
  ("La fraude explose.", "La fraude détectée a plus que doublé en un an, mais elle reste autour de 0,35 % des indemnités versées."),
  ("Les médecins signent trop facilement.", "Les arrêts longs, liés à des maladies graves, font l'essentiel de la dépense."),
 ],
 questions=["Sais-tu quelle part de la hausse vient simplement des hausses de salaires et du Covid ?", "Que faudrait-il faire pour réduire les arrêts liés au travail lui-même ?"],
 limites=["Le bilan de l'Assurance maladie sur la fraude n'a été lu qu'à travers des sites juridiques.", "La part de hausse liée au recours accru reste mal expliquée par les sources."],
 publics={'convaincus': "La Cour des comptes a fait le calcul : sur la hausse des arrêts entre 2017 et 2022, le Covid et les hausses de salaires pèsent très lourd. La fraude détectée, c'est 42 millions en 2024 pour 12 milliards d'indemnités. Les salariés de plus de 55 ans, qu'on fait travailler plus longtemps, font 27 % des journées d'arrêt.",
  'indecis': "La dépense augmente vraiment, et une partie vient d'un recours accru aux arrêts, que les chiffres n'expliquent pas entièrement. Mais l'essentiel tient au Covid, aux salaires et au vieillissement des actifs, et la fraude détectée est faible. La santé au travail est sans doute une meilleure piste que le soupçon généralisé."},
 a_actualiser='2027-06-30', raison="Nouveaux bilans de l'Assurance maladie et de la Cour des comptes.",
))

# 7 ── RSA et 15 heures d'activité ───────────────────────────────────────────
FICHES.append(fiche(
 id='rsa-15-heures-activite', affirmation="Le RSA conditionné à 15 heures d'activité, ça remet les gens au travail.", volet='social', sous_theme='RSA',
 mots_cles=['15 heures', 'quinze heures', 'rsa conditionne', 'rsa contre activite', 'heures d activite', 'loi plein emploi', 'contrepartie du rsa'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. L'évaluation officielle de la Dares et de l'IPP (2026) montre qu'un accompagnement renforcé des allocataires augmente un peu leur emploi : +3,2 points en moyenne sur l'année chez les participants. Mais les gains sont en partie pris aux autres demandeurs d'emploi, si bien qu'un effet net nul « ne peut être exclu ». Et ni l'obligation de 15 heures ni les sanctions, en vigueur depuis juin 2025, n'ont été évaluées.",
 contexte="La loi pour le plein emploi de 2023 a généralisé l'inscription des allocataires du RSA à France Travail et une durée d'activité d'au moins 15 heures, avec des sanctions.",
 explication="L'expérimentation mêlait plusieurs choses : plus de suivi par des conseillers, des démarches régulières, et un objectif d'heures d'activité. Les évaluations ne permettent pas d'isoler l'effet des 15 heures.",
 sources=[IPP_RSA, LOC_RSA, LOC_SANC, CNCDH_RSA],
 faits=[
  fait("Selon l'évaluation de la Dares et de l'IPP, l'emploi salarié des participants progresse de 3,2 points en moyenne sur l'année ; l'emploi durable de 0,7 point seulement hors contrats aidés.", 'ipp_rsa', '2023-2024', '18 territoires pilotes', "L'effet existe mais reste modeste.", 'etabli', '+3,2 points'),
  fait("Selon les évaluateurs, « on ne peut ainsi exclure que l'effet net de l'expérimentation sur la création d'emplois salariés soit nul », à cause d'effets négatifs sur les autres demandeurs d'emploi.", 'ipp_rsa', '2023-2024', '18 territoires pilotes', "Les emplois trouvés ont pu l'être aux dépens d'autres chômeurs.", 'etabli'),
  fait("L'expérimentation évaluée s'est faite sans le nouveau régime de sanctions et ne mesure pas l'effet propre des 15 heures.", 'ipp_rsa', '2023-2024', 'France', "Le cœur de la mesure n'a pas été évalué.", 'etabli'),
  fait("Selon Localtis, la norme de 15 à 20 heures est jugée « particulièrement exigeante » par l'évaluation qualitative ; les exemptions vont de 15 % à 20 % selon les territoires.", 'loc_rsa', '2024', 'France', "Beaucoup d'allocataires ne peuvent pas s'y plier.", 'etabli'),
  fait("Depuis le 1er juin 2025, un manquement peut entraîner la suspension d'au moins 30 % de l'allocation, puis sa suppression au second manquement.", 'loc_sanc', '2025', 'France', "La pression sur les allocataires s'est accrue.", 'etabli'),
  fait("La CNCDH estime que l'efficacité de la mesure n'est pas démontrée et recommande d'abroger la durée « d'au moins quinze heures ».", 'cncdh_rsa', '2024', 'France', "Une autorité indépendante juge la mesure contraire aux droits.", 'etabli'),
 ],
 court="Trompeur : c'est l'accompagnement renforcé qui a un peu augmenté l'emploi des allocataires, de façon modeste, et peut-être aux dépens d'autres chômeurs. L'effet des 15 heures et des sanctions n'a jamais été évalué.",
 moyen="L'évaluation officielle de la Dares et de l'Institut des politiques publiques est claire : un suivi plus intensif des allocataires du RSA augmente un peu leur retour à l'emploi, de 3,2 points en moyenne sur l'année. C'est positif, mais modeste, et les emplois durables hors contrats aidés progressent à peine.\n\nSurtout, les évaluateurs n'excluent pas un effet net nul : les allocataires accompagnés ont pu prendre des emplois à d'autres chômeurs. Et l'obligation des 15 heures elle-même, comme les sanctions, n'a pas été évaluée. Ce qui marche, c'est l'accompagnement, qui coûte de l'argent, pas la contrainte.",
 detaille="La loi pour le plein emploi de 2023 conditionne le RSA à une durée d'activité d'au moins quinze heures par semaine, réductible mais pas nulle. Avant sa généralisation, elle a été expérimentée dans 18 territoires de 2023 à 2024.\n\nL'évaluation de la Dares et de l'IPP, publiée en juin 2026, montre que l'emploi salarié des participants progresse de 3,2 points en moyenne sur l'année, mais que l'emploi durable hors contrats aidés ne progresse que de 0,7 point, sans effet sur les salaires. Les gains sont compensés en partie par des effets négatifs sur les autres demandeurs d'emploi : un effet net nul ne peut être exclu. L'étude ne mesure pas l'effet propre des 15 heures, et les sanctions n'étaient pas appliquées.\n\nDepuis juin 2025, les sanctions permettent de suspendre au moins 30 % de l'allocation. La CNCDH juge l'efficacité non démontrée et craint des heures non rémunérées qui remplacent de vrais emplois. Les auteurs de l'évaluation notent toutefois que leurs résultats « n'invalident pas la logique » d'un accompagnement renforcé.",
 empathie="L'idée qu'on demande quelque chose en échange d'une aide peut sembler juste. Mais l'évaluation montre que ce qui aide vraiment, c'est l'accompagnement, et que la contrainte n'a jamais été mesurée.",
 legitimes=["Un accompagnement plus intensif augmente réellement l'emploi des participants.", "Les auteurs de l'évaluation estiment que leurs résultats n'invalident pas la logique de la réforme."],
 contre=[
  ("C'est normal de demander une contrepartie.", "Le RSA est déjà conditionné à des démarches ; la question est de savoir si les 15 heures aident, et cela n'a pas été démontré."),
  ("Ça marche, les gens retrouvent un emploi.", "Les participants un peu plus, mais l'effet net sur l'emploi total pourrait être nul."),
 ],
 questions=["Sais-tu que l'obligation des 15 heures n'a jamais été évaluée à part ?", "Que faire pour ceux qui ne peuvent pas suivre ces heures, à cause de leur santé ou de leurs enfants ?"],
 limites=["Aucun bilan chiffré de la généralisation de 2025 n'a été lu.", "L'évaluation porte sur une expérimentation sans sanctions."],
 publics={'convaincus': "L'évaluation officielle de la Dares montre que ce qui aide, c'est un conseiller qui suit vraiment les gens : +3,2 points d'emploi chez les participants. Mais l'effet net pourrait être nul, et les 15 heures n'ont jamais été évaluées. Tu veux de l'efficacité ou juste de la punition ?",
  'indecis': "Demander un engagement en échange du RSA peut paraître juste. Les données montrent qu'un accompagnement renforcé améliore un peu le retour à l'emploi, mais que l'effet des 15 heures et des sanctions n'est pas démontré. Le levier efficace semble être le suivi, ce qui suppose des moyens."},
 a_actualiser='2027-06-30', raison="Premiers bilans de la généralisation et des sanctions.",
))

# 8 ── Les jeunes et le travail ──────────────────────────────────────────────
FICHES.append(fiche(
 id='jeunes-ne-veulent-plus-travailler', affirmation="Les jeunes ne veulent plus travailler.", volet='social', sous_theme='Emploi et salaires',
 mots_cles=['jeunes ne veulent plus travailler', 'les jeunes ne veulent pas travailler', 'generation z', 'jeunes feignants', 'jeunes paresseux', 'emploi des jeunes', 'valeur travail jeunes'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux. Le taux d'emploi des 15-24 ans est à un niveau historiquement élevé : 34,9 % en 2022, le plus haut depuis 1991, et 34,5 % en 2025, 4,6 points de plus qu'en 2019. L'apprentissage a explosé (879 000 contrats en 2024). Et 80 % des 16-30 ans se disent prêts à travailler même sans besoin financier. Beaucoup sont en revanche déçus par leurs conditions de travail.",
 contexte="Le cliché d'une jeunesse rétive au travail revient régulièrement, notamment depuis le Covid.",
 explication="Le taux d'emploi des 15-24 ans est faible partout car beaucoup sont en études ; il faut le comparer dans le temps et avec les autres pays.",
 sources=[INSEE_MT25, LOC_JEUNES, TRESOR_APP, MONTAIGNE_JEUNES],
 faits=[
  fait("En 2025, le taux d'emploi des 15-24 ans est de 34,5 %, soit 4,6 points de plus qu'en 2019.", 'insee_mt25', '2019-2025', 'France', "Les jeunes travaillent davantage qu'avant le Covid.", 'etabli', '34,5 %'),
  fait("Selon l'Insee cité par Localtis, le taux d'emploi des 15-24 ans atteint 34,9 % en 2022, « le plus haut depuis 1991 ».", 'loc_jeunes', '2022', 'France', "C'est un record sur trente ans.", 'etabli'),
  fait("879 000 nouveaux contrats d'apprentissage ont été signés en 2024, contre 306 000 en 2017.", 'tresor_app', '2017-2024', 'France', "Les jeunes se forment massivement en entreprise.", 'etabli'),
  fait("Selon une enquête de l'Institut Montaigne auprès de 6 000 jeunes, 80 % se disent prêts à travailler même sans besoin financier ; 66 % de ceux qui ont travaillé perçoivent un décalage entre leurs attentes et la réalité.", 'montaigne_jeunes', '2024', 'France', "Les jeunes veulent travailler, mais sont souvent déçus.", 'estimation', '80 %'),
  fait("30,5 % des jeunes en emploi sont en alternance ou en stage, et leur taux de chômage remonte à 19,8 % en 2025.", 'insee_mt25', '2025', 'France', "La hausse repose en partie sur l'apprentissage aidé.", 'etabli'),
 ],
 court="Faux : le taux d'emploi des jeunes est au plus haut depuis plus de trente ans, et 80 % se disent prêts à travailler même sans besoin d'argent. Beaucoup sont surtout déçus par les conditions de travail.",
 moyen="Les chiffres de l'Insee contredisent le cliché : le taux d'emploi des 15-24 ans était en 2022 au plus haut depuis 1991, et il reste en 2025 bien au-dessus de son niveau de 2019. L'apprentissage a presque triplé depuis 2017.\n\nSelon une enquête de l'Institut Montaigne, pourtant libéral, 80 % des jeunes se disent prêts à travailler même sans besoin financier. Ce qui ressort, c'est une déception : deux sur trois trouvent un décalage entre leurs attentes et la réalité du travail. C'est un problème de conditions de travail, pas de paresse.",
 detaille="Selon l'Insee, le taux d'emploi des 15-24 ans est de 34,5 % en 2025, 4,6 points au-dessus de 2019. Il avait atteint 34,9 % en 2022, le plus haut niveau depuis 1991. Il est proche de la moyenne européenne, même s'il reste sous la moyenne de l'OCDE, et celui des 25-29 ans dépasse cette moyenne.\n\nCette hausse doit beaucoup à l'apprentissage : 879 000 contrats signés en 2024 contre 306 000 en 2017, pour un coût public d'environ 15 Md€ en 2023. 30,5 % des jeunes en emploi sont en alternance ou en stage, et le chômage des jeunes remonte, à 19,8 % en 2025.\n\nSur les mentalités, une enquête de l'Institut Montaigne auprès de 6 000 jeunes montre que 80 % sont prêts à travailler même sans besoin financier, mais que 66 % de ceux qui ont déjà travaillé sont déçus et que 60 % des jeunes salariés envisagent de quitter leur entreprise. Le rapport au travail change ; l'envie de travailler, elle, est toujours là.",
 empathie="On a tous entendu un employeur se plaindre de jeunes qui ne restent pas. Les chiffres montrent pourtant qu'ils n'ont jamais autant travaillé depuis trente ans ; ce qu'ils refusent plus souvent, ce sont de mauvaises conditions.",
 legitimes=["La hausse de l'emploi des jeunes repose largement sur l'apprentissage subventionné.", "Beaucoup de jeunes salariés envisagent de quitter leur entreprise."],
 contre=[
  ("Ils changent tout le temps de boulot.", "Beaucoup sont déçus par leurs conditions de travail ; changer d'emploi, ce n'est pas refuser de travailler."),
  ("C'est grâce aux aides à l'apprentissage.", "En partie, oui ; mais ce sont bien des jeunes qui travaillent en entreprise."),
 ],
 questions=["Sais-tu que le taux d'emploi des jeunes est au plus haut depuis trente ans ?", "Qu'est-ce qui, selon toi, décourage un jeune dans son premier emploi ?"],
 limites=["L'enquête de l'Institut Montaigne n'a été lue qu'à travers son communiqué.", "Le taux d'emploi des jeunes dépend aussi de la durée des études."],
 publics={'convaincus': "Les jeunes n'ont jamais autant travaillé depuis trente ans : en 2022, leur taux d'emploi était au plus haut depuis 1991, selon l'Insee. Et même l'Institut Montaigne, think tank libéral, trouve que 80 % sont prêts à travailler sans besoin d'argent. Ce qu'ils fuient, ce sont les mauvaises conditions.",
  'indecis': "Le rapport au travail des jeunes change, c'est vrai : beaucoup sont déçus et changent d'emploi. Mais leur taux d'emploi est historiquement élevé, porté par l'apprentissage. La question est plutôt de savoir quels emplois on leur propose."},
 a_actualiser='2027-06-30', raison="Nouvelles données de l'Insee sur le marché du travail.",
))

# 9 ── Pouvoir d'achat ───────────────────────────────────────────────────────
FICHES.append(fiche(
 id='pouvoir-achat-baisse', affirmation="Le pouvoir d'achat des Français ne cesse de baisser.", volet='economie', sous_theme='Inflation',
 mots_cles=['pouvoir d achat', 'pouvoir d achat baisse', 'baisse du pouvoir d achat', 'on vit moins bien', 'fin du mois', 'vie chere'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. Selon l'Insee, le pouvoir d'achat par unité de consommation progresse sur longue période, d'environ 0,5 % par an depuis 2010, mais beaucoup moins vite qu'autrefois. Il a reculé certaines années (2020, 2022 et 2025, -0,7 %) et le salaire réel moyen du privé a baissé en 2022 et 2023, retrouvant « à peine » son niveau de 2019 en 2024. Le ressenti s'explique aussi par le poids des dépenses contraintes.",
 contexte="Le pouvoir d'achat est la première préoccupation des Français dans les enquêtes depuis la vague d'inflation de 2022.",
 explication="Le pouvoir d'achat mesure l'évolution des revenus après impôts, corrigée des prix. L'Insee le calcule par « unité de consommation » pour tenir compte de la taille des ménages. C'est une moyenne, qui ne reflète pas chaque situation.",
 sources=[INSEE_PA, INSEE_FPS, INSEE_CN25, INSEE_SAL24, BDF_PA],
 faits=[
  fait("Le pouvoir d'achat par unité de consommation évolue de -0,3 % en 2020, +2,8 % en 2021, -0,3 % en 2022, +0,4 % en 2023, +2,2 % en 2024 et -0,7 % en 2025 (provisoire).", 'insee_pa', '2020-2025', 'France', "Il n'y a pas de baisse continue, mais des années de recul.", 'etabli'),
  fait("Depuis 2010, le pouvoir d'achat par unité de consommation progresse en moyenne de 0,5 % par an, nettement moins que dans les années 1960.", 'insee_fps', '2010-2024', 'France', "La progression est lente, ce qui nourrit le sentiment de stagnation.", 'etabli', '+0,5 % par an'),
  fait("En 2025, le recul de 0,7 % s'explique notamment par la chute des revenus du patrimoine (-0,9 point), les impôts (-0,6 point) et les prix (-0,8 point), les revenus d'activité contribuant pour +1,0 point.", 'insee_cn25', '2025', 'France', "La baisse de 2025 vient en partie des dividendes.", 'etabli'),
  fait("Le salaire net moyen du privé a baissé de 1,3 % en 2022 et de 1,0 % en 2023 en euros constants ; en 2024, il retrouve « à peine » son niveau de 2019.", 'insee_sal24', '2019-2024', 'France', "Les salaires réels ont stagné depuis 2019.", 'etabli'),
  fait("Selon la Banque de France, les dépenses pré-engagées pèsent 27,9 % du budget des ménages en 2022, contre 14,2 % il y a soixante ans, ce qui peut créer un décalage entre ressenti et statistiques.", 'bdf_pa', '2022', 'France', "Le ressenti a des causes réelles.", 'etabli'),
 ],
 court="Trompeur : selon l'Insee, le pouvoir d'achat moyen progresse lentement sur longue période, mais il a reculé certaines années, dont 2025. Les salaires réels, eux, ont à peine retrouvé leur niveau de 2019. Le sentiment de stagnation est fondé ; la baisse continue, non.",
 moyen="Le pouvoir d'achat ne baisse pas sans cesse : selon l'Insee, il a progressé de 2,2 % par unité de consommation en 2024, et d'environ 0,5 % par an en moyenne depuis 2010. Mais c'est très lent, et il a reculé en 2022 et en 2025.\n\nSurtout, les salaires réels ont baissé en 2022 et 2023 et ont à peine retrouvé leur niveau de 2019. Les dépenses contraintes, comme le logement et l'énergie, pèsent de plus en plus. Le malaise est donc réel : il vient d'abord de salaires qui ne suivent pas, alors que les profits et les dividendes ont bondi en 2024.",
 detaille="L'Insee mesure le pouvoir d'achat du revenu disponible brut par unité de consommation. Selon ses séries révisées, il évolue de -0,3 % en 2020, +2,8 % en 2021, -0,3 % en 2022, +0,4 % en 2023, +2,2 % en 2024 et -0,7 % en 2025. Depuis 2010, la moyenne est d'environ +0,5 % par an, bien loin des années 1960.\n\nLe recul de 2025 s'explique en partie par la chute des dividendes après leur bond de 2024 et par les impôts ; les revenus d'activité ont, eux, contribué positivement. Pour les salariés du privé, le tableau est plus sombre : le salaire net moyen a baissé en euros constants en 2022 et 2023 et retrouve « à peine » son niveau de 2019 en 2024.\n\nLa Banque de France rappelle que le ressenti peut différer des statistiques : les achats fréquents marquent les esprits, et les dépenses pré-engagées pèsent près de 28 % du budget. Une moyenne nationale ne dit rien non plus de la situation des ménages modestes.",
 empathie="Si tu as l'impression de vivre moins bien qu'avant, tu n'es pas seul, et ce n'est pas une illusion : les salaires réels ont stagné depuis 2019 et les dépenses contraintes pèsent lourd.",
 legitimes=["Le pouvoir d'achat a reculé en 2020, 2022 et 2025.", "Les salaires réels du privé ont baissé en 2022 et 2023."],
 contre=[
  ("Les statistiques ne reflètent pas la réalité.", "Elles mesurent une moyenne ; la Banque de France explique pourquoi le ressenti peut différer, notamment à cause des dépenses contraintes."),
  ("C'est la faute de l'immigration.", "Les sources lues expliquent le recul par les prix, les impôts, les dividendes et des salaires qui ne suivent pas."),
 ],
 questions=["Quelles dépenses pèsent le plus dans ton budget aujourd'hui ?", "Sais-tu que les salaires réels ont à peine retrouvé leur niveau de 2019 ?"],
 limites=["Le pouvoir d'achat moyen masque de fortes différences entre ménages.", "Les données de 2025 sont provisoires."],
 publics={'convaincus': "Tu as raison sur un point : les salaires réels ont baissé en 2022 et 2023 et ont à peine retrouvé leur niveau de 2019, selon l'Insee. Mais le pouvoir d'achat moyen ne baisse pas sans arrêt : il a monté de 2,2 % en 2024. Le vrai problème, ce sont des salaires qui stagnent pendant que les dividendes bondissent.",
  'indecis': "Ton ressenti est fondé : la progression du pouvoir d'achat est très lente depuis 2010, et il a reculé en 2025. Les dépenses contraintes, comme le logement, pèsent près de 28 % du budget. La question centrale, c'est celle des salaires."},
 a_actualiser='2027-06-30', raison="Comptes nationaux 2026.",
))

# 10 ── Licencier en France ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='licenciement-impossible-france', affirmation="En France, on ne peut pas licencier.", volet='droits', sous_theme='Droits des travailleurs',
 mots_cles=['on ne peut pas licencier', 'impossible de licencier', 'licencier en france', 'licenciement', 'licenciements', 'rupture conventionnelle', 'bareme macron', 'prud hommes'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux. En 2024, il y a eu environ 580 000 licenciements de salariés en CDI (75 700 économiques et 506 700 pour d'autres motifs) et 515 000 ruptures conventionnelles, selon l'Insee. Les indemnités pour licenciement abusif sont plafonnées depuis 2017, et l'OCDE classe la France parmi les pays qui ont assoupli leur protection. La procédure reste encadrée, et la France était en 2013 parmi les législations jugées les plus protectrices.",
 contexte="L'idée d'un droit du travail qui empêcherait de licencier est souvent avancée pour expliquer le chômage.",
 explication="Un licenciement doit avoir un motif réel et sérieux et suivre une procédure. Depuis 2008, la rupture conventionnelle permet aussi une séparation d'un commun accord, avec droit au chômage.",
 sources=[INSEE_FINS, SEN_RC, LD_BAREME, LD_CEDS, OCDE_EPL, IRES_EPL],
 faits=[
  fait("En 2024, les fins de CDI comprennent 75 700 licenciements économiques, 506 700 licenciements non économiques et 514 600 ruptures conventionnelles.", 'insee_fins', '2024', 'Secteur privé', "On licencie des centaines de milliers de salariés chaque année.", 'etabli'),
  fait("Selon la Dares citée par le Sénat, les ruptures conventionnelles atteignent 514 768 en 2024, contre 192 278 en 2009.", 'sen_rc', '2009-2024', 'France', "La séparation négociée a fortement progressé.", 'etabli', '+167 %'),
  fait("Selon Lefebvre Dalloz, l'indemnité pour licenciement abusif est plafonnée depuis 2017 : 3,5 mois de salaire au maximum à 2 ans d'ancienneté, 20 mois au maximum au-delà de 29 ans.", 'ld_bareme', '2017-2026', 'France', "Le coût d'un licenciement injustifié est prévisible et limité.", 'etabli'),
  fait("Selon Lefebvre Dalloz, le Comité européen des droits sociaux a jugé en 2022 que ce barème viole le droit à une indemnité adéquate ; la Cour de cassation l'a néanmoins validé.", 'ld_ceds', '2022', 'France', "Le barème est critiqué pour protéger trop peu les salariés.", 'etabli'),
  fait("L'OCDE cite la France parmi les pays dont les réformes de 2013 à 2019 visaient à « atténuer la rigueur de la protection contre les licenciements ».", 'ocde_epl', '2013-2019', 'France', "La protection a été assouplie.", 'etabli'),
  fait("En 2013, l'indicateur de l'OCDE donnait à la France 2,82 sur 6 pour la protection des CDI, contre 1,62 au Royaume-Uni.", 'ires_epl', '2013', 'France', "La France était alors parmi les plus protectrices.", 'etabli'),
 ],
 court="Faux : en 2024, environ 580 000 salariés en CDI ont été licenciés et 515 000 ruptures conventionnelles ont été signées. Depuis 2017, les indemnités pour licenciement abusif sont plafonnées.",
 moyen="Les chiffres de l'Insee sont parlants : en 2024, 75 700 licenciements économiques, 506 700 licenciements pour d'autres motifs, et 514 600 ruptures conventionnelles. On licencie donc beaucoup en France.\n\nDepuis 2017, un salarié licencié sans motif valable ne peut obtenir qu'une indemnité plafonnée, par exemple 3,5 mois de salaire avec deux ans d'ancienneté. L'OCDE note que la France a assoupli sa protection. Un licenciement doit être justifié et suivre une procédure : c'est une protection contre l'arbitraire, pas une interdiction.",
 detaille="Selon l'Insee, sur 4,2 millions de fins de CDI en 2024, on compte 75 700 licenciements économiques, 506 700 licenciements non économiques, 514 600 ruptures conventionnelles et 1,85 million de démissions. La rupture conventionnelle, créée en 2008, est passée de 192 278 en 2009 à 514 768 en 2024 ; les très petites entreprises en réalisent plus de 40 %.\n\nDepuis les ordonnances de 2017, l'indemnité en cas de licenciement sans cause réelle et sérieuse est plafonnée selon l'ancienneté : 3,5 mois maximum à deux ans, 20 mois maximum au-delà de 29 ans. Le Comité européen des droits sociaux a jugé ce barème contraire à la Charte sociale européenne, mais la Cour de cassation l'a validé en 2022. L'OCDE classe la France parmi les pays qui ont assoupli la protection contre les licenciements entre 2013 et 2019.\n\nIl serait faux de dire que la France ne protège pas : en 2013, son indicateur de l'OCDE la plaçait parmi les législations les plus protectrices des CDI, et un plan social reste obligatoire pour les licenciements collectifs dans les grandes entreprises. Mais licencier est possible, fréquent, et moins coûteux qu'avant 2017.",
 empathie="Pour un petit patron, la procédure peut sembler lourde, et la peur des prud'hommes est réelle. Mais les chiffres montrent que les licenciements et les ruptures négociées se comptent par centaines de milliers chaque année.",
 legitimes=["La procédure de licenciement reste encadrée et peut sembler complexe pour une petite entreprise.", "En 2013, la France était parmi les pays les plus protecteurs selon l'indicateur de l'OCDE."],
 contre=[
  ("Les prud'hommes ruinent les patrons.", "Depuis 2017, l'indemnité pour licenciement abusif est plafonnée selon l'ancienneté."),
  ("C'est pour ça qu'il y a du chômage.", "La protection a été assouplie depuis 2013 ; les sources lues ne permettent pas d'en tirer un effet sur le chômage."),
 ],
 questions=["Sais-tu combien de licenciements ont lieu chaque année en France ?", "Un salarié licencié sans raison valable devrait-il être indemnisé à hauteur du préjudice réel ?"],
 limites=["La note actuelle de la France à l'indicateur de l'OCDE n'a pas pu être lue ; la valeur citée date de 2013.", "Le barème a été lu sur un site d'éditeur juridique, pas sur Légifrance."],
 publics={'convaincus': "En 2024, selon l'Insee, il y a eu environ 580 000 licenciements de salariés en CDI, et plus de 500 000 ruptures conventionnelles. Et depuis 2017, même un licenciement abusif coûte au maximum 3,5 mois de salaire à deux ans d'ancienneté. On peut licencier en France, et beaucoup.",
  'indecis': "Le droit du travail impose un motif et une procédure, ce qui peut sembler lourd pour une petite entreprise. Mais les licenciements sont nombreux, la rupture conventionnelle facilite les séparations, et les indemnités sont plafonnées depuis 2017. Ces protections évitent surtout l'arbitraire."},
 a_actualiser='2027-06-30', raison="Nouvelles données de l'Insee et de la Dares sur les fins de contrat.",
))

# 11 ── Aides publiques aux entreprises ──────────────────────────────────────
FICHES.append(fiche(
 id='aides-publiques-entreprises', affirmation="Les entreprises ne touchent presque pas d'aides publiques, c'est l'assistanat des pauvres qui coûte.", volet='economie', sous_theme='Grandes entreprises',
 mots_cles=['aides publiques aux entreprises', 'aides aux entreprises', '211 milliards', 'assistanat des entreprises', 'subventions aux entreprises', 'cadeaux aux entreprises', 'exonerations de cotisations'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux. La commission d'enquête du Sénat, présidée par un sénateur LR, estime les aides publiques aux entreprises à au moins 211 milliards d'euros en 2023, et à 108 milliards au sens strict. En comparaison, le RSA a coûté 12,2 milliards d'euros et l'ensemble des minima sociaux 31,6 milliards. Le montant exact dépend du périmètre retenu, et une partie de ces aides, comme les allègements de cotisations, est défendue comme une compensation du coût du travail.",
 contexte="Le débat sur « l'assistanat » vise presque toujours les allocataires de minima sociaux, rarement les entreprises.",
 explication="Les aides aux entreprises comprennent des subventions, des prêts et garanties publics, des réductions d'impôts et des allègements de cotisations sociales. Il n'existe pas de définition officielle unique, d'où des estimations différentes.",
 sources=[PS_AIDES, PS_AIDES_CALC, SEN_808, DREES_MS],
 faits=[
  fait("La commission d'enquête du Sénat estime à au moins 211 milliards d'euros les aides publiques d'État aux entreprises en 2023 ; son rapport a été adopté à l'unanimité.", 'ps_aides', '2023', 'France', "Le montant est très élevé et le constat transpartisan.", 'etabli', '211 Md€'),
  fait("Ce total comprend 7 Md€ de subventions, 41 Md€ d'interventions de Bpifrance, 88 Md€ de dépenses fiscales et 75 Md€ d'allègements de cotisations ; au sens strict, la commission arrive à 108 Md€.", 'ps_aides_calc', '2023', 'France', "Même au sens strict, le montant dépasse 100 milliards.", 'etabli'),
  fait("En 2023, les minima sociaux s'élèvent à 31,6 milliards d'euros, dont 12,2 milliards pour le RSA.", 'drees_ms', '2023', 'France', "Le RSA coûte environ neuf fois moins que les aides aux entreprises au sens strict.", 'etabli', '12,2 Md€'),
  fait("Le Sénat juge « impossible de déterminer avec précision le montant des aides publiques versées aux grandes entreprises » ; les estimations antérieures allaient de 139 à 223 Md€ selon le périmètre.", 'sen_808', '2019-2025', 'France', "L'ordre de grandeur est sûr, le chiffre exact non.", 'etabli'),
  fait("Selon Public Sénat, le président de la commission voit dans les allègements de cotisations des « compensations », et le Medef conteste l'addition.", 'ps_aides_calc', '2025', 'France', "Le classement des allègements en « aides » est discuté.", 'etabli'),
 ],
 court="Faux : le Sénat chiffre les aides publiques aux entreprises à au moins 211 milliards d'euros en 2023, et à 108 milliards au sens strict. Le RSA, c'est 12,2 milliards.",
 moyen="Une commission d'enquête du Sénat, présidée par un sénateur LR, a recensé plus de 2 200 dispositifs d'aide aux entreprises. Total : au moins 211 milliards d'euros en 2023, dont 75 milliards d'allègements de cotisations. Même au sens strict, on dépasse 100 milliards.\n\nLe RSA, lui, a coûté 12,2 milliards en 2023, et tous les minima sociaux 31,6 milliards. On peut défendre certaines aides aux entreprises, mais si on parle d'argent public versé sans contrepartie claire, c'est d'abord de ce côté qu'il faut regarder.",
 detaille="En juillet 2025, la commission d'enquête du Sénat sur les aides publiques aux entreprises, présidée par Olivier Rietmann (LR) avec le communiste Fabien Gay comme rapporteur, a adopté à l'unanimité son rapport. Elle estime ces aides à au moins 211 Md€ en 2023 : 7 Md€ de subventions, 41 Md€ d'interventions de Bpifrance, 88 Md€ de dépenses fiscales et 75 Md€ d'allègements de cotisations, sans compter les aides des collectivités et de l'Europe.\n\nLe chiffre dépend du périmètre : 108 Md€ au sens strict selon la commission, 112 Md€ hors allègements pour le Haut-commissariat au Plan, environ 150 Md€ selon le ministre de l'Économie. Le Sénat reconnaît qu'il est impossible d'établir un montant précis, et le Medef conteste l'addition. Mais aucune de ces estimations ne descend sous 100 Md€.\n\nÀ titre de comparaison, la DREES chiffre les minima sociaux à 31,6 Md€ en 2023, dont 12,2 Md€ pour le RSA. La commission ne demande pas de supprimer les aides aux entreprises, mais un « choc de transparence » et des contreparties.",
 empathie="On peut trouver injuste de financer des gens qui ne travaillent pas, c'est un sentiment répandu. Mais si l'on cherche où va l'argent public sans contrepartie, les aides aux entreprises pèsent bien plus lourd.",
 legitimes=["Les allègements de cotisations sont présentés comme une compensation du coût du travail.", "Le montant exact varie selon le périmètre, et le Sénat le juge impossible à établir précisément."],
 contre=[
  ("Ces aides créent des emplois.", "Certaines peut-être, mais le Sénat demande justement des contreparties et une évaluation, faute de transparence."),
  ("Ce ne sont pas des aides, juste moins d'impôts.", "Le périmètre strict de la commission, 108 Md€, reste près de neuf fois le coût du RSA."),
 ],
 questions=["Savais-tu que le Sénat chiffre les aides aux entreprises à plus de 200 milliards ?", "Faut-il exiger des contreparties aux entreprises aidées, comme on en exige des allocataires du RSA ?"],
 limites=["Le montant total dépend du périmètre et fait l'objet de contestations.", "La comparaison avec le seul RSA ne couvre pas l'ensemble de la protection sociale."],
 publics={'convaincus': "Une commission du Sénat présidée par un LR a chiffré les aides aux entreprises : au moins 211 milliards en 2023, et 108 milliards même au sens strict. Le RSA, c'est 12,2 milliards. Si on veut chasser l'assistanat, pourquoi ne jamais parler de ces milliards-là ?",
  'indecis': "Il est légitime de vouloir que l'argent public soit bien utilisé. Les aides aux entreprises représentent selon le Sénat entre 108 et 211 milliards par an, contre 12,2 milliards pour le RSA. Certaines sont utiles, mais le Sénat demande plus de transparence et de contreparties."},
 a_actualiser='2027-06-30', raison="Suites du rapport du Sénat et nouvelles estimations.",
))

# 12 ── Suppression de l'ISF ─────────────────────────────────────────────────
FICHES.append(fiche(
 id='suppression-isf-investissement', affirmation="La suppression de l'ISF a relancé l'investissement.", volet='economie', sous_theme='Fiscalité',
 mots_cles=['isf', 'suppression de l isf', 'impot sur la fortune', 'ifi', 'flat tax', 'pfu', 'retablir l isf', 'ruissellement'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux d'après l'évaluation officielle : le comité de France Stratégie n'a détecté « aucun effet » sur l'investissement et les salaires des entreprises les plus concernées. La réforme a en revanche fait bondir les dividendes, de 14 à 23 milliards d'euros par an, très concentrés sur 1 % des foyers, pour un coût de plus de 4 milliards par an. Elle a bien réduit l'exil fiscal, mais sur quelques centaines de foyers.",
 contexte="En 2018, l'ISF a été remplacé par un impôt sur la fortune immobilière (IFI), avec un prélèvement forfaitaire unique sur les revenus du capital, au nom de l'investissement.",
 explication="L'idée du « ruissellement » était que les plus riches investiraient davantage dans les entreprises. Un comité indépendant a été chargé de l'évaluer.",
 sources=[FS_ISF, PS_ISF, LOC_IFI],
 faits=[
  fait("Le comité d'évaluation écrit : « Aucun effet n'a été détecté sur l'investissement et les salaires parmi les entreprises » les plus exposées à la réforme.", 'fs_isf', '2023', 'France', "La promesse principale n'est pas vérifiée.", 'etabli'),
  fait("Les dividendes déclarés passent d'environ 14 Md€ par an (2013-2017) à environ 23 Md€ (2018-2020) ; 1 % des foyers concentre 96 % des montants.", 'fs_isf', '2013-2020', 'France', "La réforme a surtout profité aux plus riches.", 'etabli', '96 %'),
  fait("Le coût de la transformation de l'ISF en IFI serait « vraisemblablement supérieur à 4 milliards d'euros » en 2022.", 'fs_isf', '2022', 'France', "La réforme coûte cher aux finances publiques.", 'etabli', '+4 Md€'),
  fait("Depuis 2018, on compte environ 380 retours pour 260 départs par an chez les redevables de l'IFI, contre 370 retours pour 950 départs sous l'ISF.", 'fs_isf', '2011-2020', 'France', "L'exil fiscal a reculé, mais sur de petits effectifs.", 'etabli'),
  fait("Selon Public Sénat, en 2019, 62 % des dividendes sont allés à 0,1 % des foyers ; Bercy invoque des effets de long terme.", 'ps_isf', '2019-2021', 'France', "Le gouvernement conteste le manque de recul.", 'etabli'),
 ],
 court="Faux : l'évaluation officielle de France Stratégie n'a détecté aucun effet de la suppression de l'ISF sur l'investissement. Les dividendes, eux, ont bondi, au profit de 1 % des foyers.",
 moyen="En 2018, l'ISF a été remplacé par un impôt sur la seule fortune immobilière, au nom de l'investissement. Le comité d'évaluation de France Stratégie a cherché : aucun effet n'a été détecté sur l'investissement ni sur les salaires dans les entreprises concernées.\n\nCe qui a augmenté, ce sont les dividendes, passés d'environ 14 à 23 milliards par an, dont 96 % pour 1 % des foyers. Coût pour l'État : plus de 4 milliards par an. Il faut reconnaître un effet : les départs de contribuables fortunés ont nettement diminué, mais on parle de quelques centaines de foyers.",
 detaille="Le comité d'évaluation des réformes de la fiscalité du capital, placé auprès de France Stratégie, a rendu son rapport final en octobre 2023. Sa conclusion principale : « Aucun effet n'a été détecté sur l'investissement et les salaires parmi les entreprises » les plus exposées. Les créations d'entreprises semblent plus liées au prélèvement forfaitaire unique et à l'impôt sur les sociétés qu'à l'IFI.\n\nLa réforme a en revanche fait bondir les dividendes déclarés, d'environ 14 Md€ par an avant 2018 à environ 23 Md€ ensuite, avec 1 % des foyers qui en reçoit 96 %. Son coût est estimé à plus de 4 Md€ en 2022.\n\nL'effet sur l'exil fiscal est réel : environ 260 départs par an après 2018 contre 950 sous l'ISF, et plus de retours que de départs. Mais il s'agit de quelques centaines de foyers. Bercy répond que les effets sur l'investissement se mesurent sur le long terme ; à ce jour, ils n'ont pas été observés.",
 empathie="L'idée que baisser les impôts des riches profite à tous est intuitive, et elle a été sincèrement défendue. L'avantage, c'est qu'elle a été évaluée : les résultats ne la confirment pas.",
 legitimes=["Les départs de contribuables fortunés ont nettement reculé depuis 2018.", "Bercy estime que les effets de long terme ne sont pas encore mesurables."],
 contre=[
  ("Les riches seraient partis.", "Les départs ont reculé, mais ils concernent quelques centaines de foyers par an, pour un coût de plus de 4 milliards."),
  ("Il faut du temps pour voir les effets.", "Le rapport final date de 2023, cinq ans après la réforme, et ne détecte aucun effet sur l'investissement."),
 ],
 questions=["Sais-tu ce qu'a conclu l'évaluation officielle de la suppression de l'ISF ?", "À qui ont profité les dividendes supplémentaires ?"],
 limites=["Les données s'arrêtent vers 2021-2022.", "Les effets de long terme sur l'investissement restent débattus."],
 publics={'convaincus': "Le gouvernement lui-même a fait évaluer la suppression de l'ISF par France Stratégie : aucun effet détecté sur l'investissement. Les dividendes ont bondi de 14 à 23 milliards, dont 96 % pour 1 % des foyers. Ça coûte plus de 4 milliards par an : qui a payé ?",
  'indecis': "La réforme a réduit les départs de contribuables fortunés, c'est un fait. Mais selon l'évaluation officielle, elle n'a pas relancé l'investissement, et elle a surtout augmenté les dividendes des plus riches. La question est de savoir si ces 4 milliards par an ne seraient pas mieux utilisés ailleurs."},
 a_actualiser='2028-06-30', raison="Nouvelles évaluations de la fiscalité du capital.",
))

# 13 ── Le RN et la taxe Zucman ──────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-taxe-zucman', affirmation="Le RN veut taxer les super-riches.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['rn taxe zucman', 'rn taxer les riches', 'rn super riches', 'rn ultra riches', 'impot sur la fortune financiere', 'fortune improductive', 'vote du rn sur la taxe zucman'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. Le RN s'est abstenu sur la taxe Zucman en février 2025, puis ses 88 députés ont voté contre en octobre 2025 ; Marine Le Pen l'a jugée « stupide et nocive ». Le RN a aussi refusé de relever la flat tax. Il défend un « impôt sur la fortune financière » et a voté un « impôt sur la fortune improductive », mais qui excluent l'outil de travail, c'est-à-dire l'essentiel du patrimoine des plus grandes fortunes.",
 contexte="Le RN se présente comme le défenseur du pouvoir d'achat face aux « élites », et revendique de vouloir taxer la spéculation.",
 explication="La taxe Zucman est un impôt plancher de 2 % sur les patrimoines de plus de 100 millions d'euros, biens professionnels compris, qui concernerait environ 1 800 foyers.",
 sources=[LEGIF_ZUC, PS_RNFISC, LCP_ZUC, DATAN_3300, LCP_IFIMP],
 faits=[
  fait("Selon Legifiscal, le 20 février 2025, l'Assemblée a adopté la taxe Zucman en première lecture par 116 voix contre 39 ; le RN s'est abstenu.", 'legif_zuc', '2025', 'France', "Le RN n'a pas soutenu la taxe.", 'etabli'),
  fait("Selon les données de scrutin relayées par Datan, le 31 octobre 2025, les 88 députés RN présents ont voté contre l'amendement instaurant la taxe Zucman, rejeté par 228 voix contre 172.", 'datan_3300', '2025', 'France', "Le RN a contribué au rejet.", 'etabli', '88 contre'),
  fait("Selon LCP, la taxe avait déjà été rejetée en commission des finances avec les voix de l'ex-majorité, de LR, du RN et de l'UDR.", 'lcp_zuc', '2025', 'France', "Le vote du RN est constant à l'automne 2025.", 'etabli'),
  fait("Selon Public Sénat, Marine Le Pen a qualifié la taxe de « stupide et nocive », et le RN a refusé de porter la flat tax de 30 à 33 %.", 'ps_rnfisc', '2025', 'France', "Le RN refuse de taxer davantage les revenus du capital.", 'etabli'),
  fait("Selon Public Sénat, le RN propose un « impôt sur la fortune financière » qui exclut les biens professionnels et les parts de PME.", 'ps_rnfisc', '2025', 'France', "Le RN épargne l'outil de travail, cœur des très grandes fortunes.", 'etabli'),
  fait("Selon LCP, le RN a contribué à adopter, le 31 octobre 2025, un « impôt sur la fortune improductive » à 1 % remplaçant l'IFI.", 'lcp_ifimp', '2025', 'France', "Le RN n'est pas opposé à tout impôt sur le patrimoine.", 'etabli'),
 ],
 court="Trompeur : le RN s'est abstenu sur la taxe Zucman, puis a voté contre en octobre 2025. Il défend un impôt sur la fortune qui exclut l'outil de travail, c'est-à-dire l'essentiel du patrimoine des milliardaires.",
 moyen="La taxe Zucman vise environ 1 800 foyers dont le patrimoine dépasse 100 millions d'euros. Le RN s'est abstenu lors de son adoption en février 2025, puis ses 88 députés ont voté contre en octobre 2025, et Marine Le Pen l'a qualifiée de « stupide et nocive ».\n\nLe RN met en avant un « impôt sur la fortune financière » et a voté un impôt sur la fortune « improductive ». Mais ces impôts excluent les biens professionnels, qui constituent l'essentiel de la fortune des milliardaires. Le RN taxe les yachts, pas les empires.",
 detaille="La taxe dite Zucman est un impôt minimal de 2 % sur les patrimoines supérieurs à 100 millions d'euros, biens professionnels compris, qui viserait environ 1 800 foyers. Adoptée en première lecture le 20 février 2025, avec l'abstention du RN, elle a ensuite été rejetée à l'automne 2025, en commission puis en séance, le RN votant contre à 88 voix sur 88 le 31 octobre.\n\nMarine Le Pen a jugé la taxe « stupide et nocive », et le RN a aussi refusé de relever la flat tax sur les revenus du capital de 30 à 33 %. Il argue de la protection de l'« outil de travail ».\n\nLe RN n'est pas hostile à tout impôt sur le patrimoine : il propose un « impôt sur la fortune financière » et a voté, le 31 octobre 2025, un impôt sur la fortune improductive à 1 %. Mais en excluant les biens professionnels et les parts d'entreprises, ces impôts laissent de côté l'essentiel des très grandes fortunes, constituées de titres de sociétés. Les sources lues ne disent pas si cet impôt a été maintenu dans la loi finale.",
 empathie="Il est normal de vouloir que les plus riches paient leur juste part, beaucoup d'électeurs du RN le souhaitent. C'est justement pour ça qu'il faut regarder ses votes sur la seule taxe qui vise les milliardaires.",
 legitimes=["Le RN a voté un impôt sur la fortune improductive et propose un impôt sur la fortune financière.", "Il propose aussi de taxer les superdividendes."],
 contre=[
  ("Le RN protège les PME, pas les milliardaires.", "La taxe Zucman ne touche que les patrimoines de plus de 100 millions d'euros, environ 1 800 foyers."),
  ("Il s'est abstenu, il n'a pas voté contre.", "En février 2025, oui ; en octobre 2025, ses 88 députés ont voté contre."),
 ],
 questions=["Sais-tu comment le RN a voté sur la taxe Zucman en octobre 2025 ?", "Un patrimoine de plus de 100 millions d'euros, est-ce encore une PME ?"],
 limites=["Les votes sont lus sur un site civique et dans la presse parlementaire, pas sur les pages officielles de scrutin.", "Le sort de l'impôt sur la fortune improductive dans la loi de finances finale n'a pas été vérifié."],
 publics={'convaincus': "La taxe Zucman, c'est 2 % sur les patrimoines de plus de 100 millions, environ 1 800 foyers. En octobre 2025, les 88 députés RN ont voté contre, et Marine Le Pen l'a jugée « stupide et nocive ». Le RN propose d'autres impôts, mais qui exonèrent l'outil de travail, c'est-à-dire la fortune des milliardaires.",
  'indecis': "Le RN défend un impôt sur la fortune « financière » ou « improductive », ce qui n'est pas rien. Mais il a voté contre la taxe qui vise les patrimoines de plus de 100 millions d'euros, outil de travail compris. Pour juger, mieux vaut regarder les votes que les slogans."},
 a_actualiser='2027-06-30', raison="Budget 2027 et programme du RN.",
))

# 14 ── Blocage des prix ─────────────────────────────────────────────────────
FICHES.append(fiche(
 id='blocage-prix-penuries', affirmation="Le blocage des prix proposé par la gauche provoquerait des pénuries.", volet='economie', sous_theme='Prix alimentaires',
 mots_cles=['blocage des prix', 'bloquer les prix', 'gel des prix', 'controle des prix', 'prix de premiere necessite', 'penuries', 'bouclier tarifaire', 'bouclier qualite prix'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. Le programme du Nouveau Front populaire prévoit de bloquer par décret les prix des biens de première nécessité. Le droit français le permet déjà pour six mois en cas de crise, et cela a été fait (carburants pendant la guerre du Golfe, gel hydroalcoolique pendant le Covid). Le bouclier tarifaire sur l'énergie a réduit l'inflation sans pénurie signalée, mais il était compensé par l'État. Le risque d'une baisse de l'offre sans compensation, et le coût, sont des objections sérieuses.",
 contexte="Le blocage des prix est souvent présenté comme une mesure « soviétique » vouée à vider les rayons.",
 explication="Un blocage des prix fixe un prix maximum. S'il est inférieur au coût de production et non compensé, des producteurs peuvent réduire leur offre ; s'il est temporaire ou compensé, il protège les ménages.",
 sources=[NFP_PROG, CDJ_PRIX, INSEE_BOUCLIER, BDF_BOUCLIER, MONTAIGNE_PRIX],
 faits=[
  fait("Le programme du NFP prévoit de « Bloquer les prix des biens de première nécessité dans l'alimentation, l'énergie et les carburants par décret », sans détailler la liste des produits ni la compensation.", 'nfp_prog', '2024', 'France', "La mesure est réelle mais peu précisée.", 'etabli'),
  fait("Selon Le Club des juristes, l'article L410-2 du code de commerce permet déjà de réglementer les prix par décret, pour six mois au plus en cas de crise, comme pour les carburants pendant la guerre du Golfe ou le gel hydroalcoolique pendant le Covid.", 'cdj_prix', '2024', 'France', "Le contrôle des prix existe déjà en droit.", 'etabli'),
  fait("Selon l'Insee, sans bouclier tarifaire, l'inflation aurait atteint 8,4 % au lieu de 5,3 % entre mi-2021 et mi-2022 ; les prix de l'énergie des ménages auraient augmenté de 54 % au lieu de 28 %.", 'insee_bouclier', '2021-2022', 'France', "Plafonner les prix a protégé les ménages.", 'etabli'),
  fait("Selon la Banque de France, le bouclier a réduit l'inflation de 2,2 points sur 2022-2023 pour un coût de 2,2 % du PIB ; face à un choc durable, il ne ferait que différer l'inflation, à un coût prohibitif.", 'bdf_bouclier', '2022-2023', 'France', "L'outil fonctionne contre un choc temporaire, pas durable.", 'etabli'),
  fait("Selon l'Institut Montaigne, think tank libéral, un blocage coûterait environ 24 Md€ par an et risquerait de réduire l'offre des producteurs.", 'montaigne_prix', '2024', 'France', "Le coût et le risque sur l'offre sont des objections sérieuses.", 'estimation'),
 ],
 court="Trompeur : bloquer temporairement des prix est déjà prévu par le droit français et a été fait sans pénurie, comme le bouclier sur l'énergie. Le risque existe si le blocage dure et n'est pas compensé : tout dépend de sa mise en œuvre.",
 moyen="Le programme du NFP propose de bloquer par décret les prix des produits de première nécessité. Ce n'est pas une invention : le code de commerce permet déjà au gouvernement de le faire pendant six mois en cas de crise, et cela a été fait pour les carburants ou le gel hydroalcoolique.\n\nLe bouclier tarifaire sur l'énergie, décidé par un gouvernement de droite, a réduit l'inflation de plusieurs points sans pénurie. Mais il était payé par l'État. Un blocage durable, sans compensation ni négociation avec les producteurs, pourrait réduire l'offre : c'est la vraie question, et le programme ne la tranche pas.",
 detaille="Le contrat de législature du NFP de 2024 prévoit de bloquer par décret les prix des biens de première nécessité dans l'alimentation, l'énergie et les carburants, et de renforcer le bouclier qualité-prix des outre-mer. Il ne publie ni la liste des produits ni le mécanisme de compensation.\n\nJuridiquement, l'article L410-2 du code de commerce permet déjà de réglementer les prix, de façon permanente dans les secteurs peu concurrentiels ou pour six mois en cas de crise. Économiquement, l'expérience récente est le bouclier tarifaire : selon l'Insee, il a ramené la hausse des prix de l'énergie des ménages de 54 % à 28 % entre 2021 et 2022 ; selon la Banque de France, il a réduit l'inflation de 2,2 points sur 2022-2023, pour un coût de 2,2 % du PIB.\n\nLes objections sont réelles. La Banque de France prévient qu'un plafonnement ne fait que différer l'inflation face à un choc durable. L'Institut Montaigne chiffre un blocage à environ 24 Md€ par an et redoute une baisse de l'offre. Le résultat dépend donc de la durée, de la liste des produits, de la compensation et de la taxation des marges de la grande distribution prévue dans le programme.",
 empathie="On peut craindre qu'en bloquant les prix, les rayons se vident : c'est un argument économique réel. Mais les expériences françaises récentes montrent qu'un blocage temporaire et bien conçu peut protéger les ménages sans pénurie.",
 legitimes=["Un blocage durable non compensé peut réduire l'offre.", "Le coût budgétaire d'un bouclier est élevé et ses aides sont mal ciblées."],
 contre=[
  ("Ça a toujours échoué dans les pays communistes.", "La France a plafonné des prix récemment, notamment l'énergie, sans pénurie ; la durée et la compensation font la différence."),
  ("Ce sont les producteurs qui paieront.", "Le programme prévoit aussi de taxer les superprofits de l'agro-industrie et de la grande distribution."),
 ],
 questions=["Savais-tu que le bouclier tarifaire sur l'énergie était déjà une forme de blocage des prix ?", "Qui doit supporter la hausse des prix : les ménages, l'État ou les marges des distributeurs ?"],
 limites=["Aucune source lue ne prédit l'effet du blocage tel que le NFP le formule.", "Le bouclier énergie était compensé par l'État, ce qui le distingue d'un blocage imposé aux vendeurs."],
 publics={'convaincus': "Bloquer temporairement des prix, la droite l'a fait : le bouclier sur l'énergie a évité que la facture des ménages augmente de 54 % au lieu de 28 %, selon l'Insee, et il n'y a pas eu de pénurie. Le code de commerce le permet déjà en cas de crise. Le vrai débat, c'est qui paie : l'État, les ménages ou les marges de la grande distribution.",
  'indecis': "Ta crainte a un fondement : un blocage durable et non compensé peut décourager les producteurs. Mais un blocage temporaire, comme le bouclier énergie, a protégé les ménages sans pénurie. Tout dépend de sa durée, de sa compensation et de son ciblage, que le programme du NFP devrait préciser."},
 a_actualiser='2027-06-30', raison="Programmes de 2027.",
))

# 15 ── Régulation de l'installation des médecins ─────────────────────────────
FICHES.append(fiche(
 id='regulation-installation-medecins', affirmation="La gauche veut forcer les médecins à s'installer à la campagne.", volet='services', sous_theme='Médecins et déserts médicaux',
 mots_cles=['regulation de l installation', 'installation des medecins', 'liberte d installation', 'forcer les medecins', 'loi garot', 'obliger les medecins', 'deserts medicaux'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. La proposition de loi Garot, transpartisane et adoptée par l'Assemblée en mai 2025 par 99 voix contre 9, n'oblige personne à s'installer à la campagne : elle soumet l'installation à une autorisation, de droit dans les zones sous-dotées, et accordée seulement en cas de départ d'un médecin dans les zones déjà bien dotées. La droite sénatoriale et le gouvernement Bayrou ont eux aussi proposé des obligations. Le texte n'est pas adopté au Sénat, et ses opposants estiment qu'il ne fait que répartir la pénurie.",
 contexte="Les déserts médicaux touchent des millions de Français ; la régulation de l'installation divise la profession et les partis.",
 explication="Réguler l'installation, c'est limiter les nouvelles installations là où il y a déjà beaucoup de médecins.",
 sources=[LCP_GAROT, LCP_GAROT2, PS_MOUILLER, LOC_GAROT, DREES_1144, DREES_1267],
 faits=[
  fait("Selon LCP, le texte Garot crée une autorisation d'installation, accordée de droit en zone sous-dotée et, en zone sur-dotée, seulement en cas de départ d'un praticien.", 'lcp_garot', '2025', 'France', "Personne n'est obligé de s'installer à la campagne.", 'etabli'),
  fait("Selon LCP, le texte a été adopté le 7 mai 2025 par 99 voix contre 9 et 10 abstentions, dont celle du RN, avec le soutien de députés des neuf groupes.", 'lcp_garot', '2025', 'France', "C'est un texte transpartisan, pas seulement de gauche.", 'etabli'),
  fait("Selon Public Sénat, la proposition du sénateur LR Philippe Mouiller conditionne l'installation en zone bien dotée à un exercice partiel en zone sous-dense, et le gouvernement Bayrou voulait deux jours de consultations par mois en zone prioritaire.", 'ps_mouiller', '2025', 'France', "La droite propose aussi des contraintes.", 'etabli'),
  fait("Selon Localtis, le Sénat n'a pas adopté le texte Garot en juin 2026 ; la rapporteure LR y voit « la restriction la plus stricte jamais imposée à une profession de santé ».", 'loc_garot', '2026', 'France', "Le texte reste bloqué et contesté.", 'etabli'),
  fait("En 2018, 5,7 % de la population, environ 3,8 millions de personnes, vivait en zone sous-dotée en généralistes, contre 3,8 % en 2015 ; certaines banlieues sont aussi concernées.", 'drees_1144', '2015-2018', 'France', "Les déserts médicaux ne sont pas seulement ruraux.", 'etabli'),
  fait("Le quart de la population le moins bien servi ne dispose que de 19 % des généralistes, contre 31 % pour le quart le mieux servi.", 'drees_1267', '2023', 'France', "La répartition des médecins est très inégale.", 'etabli'),
 ],
 court="Trompeur : le texte Garot, voté par des députés de tous les groupes, ne force personne à aller à la campagne. Il limite seulement les nouvelles installations là où il y a déjà assez de médecins. La droite sénatoriale propose aussi des obligations.",
 moyen="La proposition de loi portée par le socialiste Guillaume Garot, et soutenue par des députés des neuf groupes, a été adoptée par l'Assemblée en mai 2025. Elle ne dit pas « installez-vous à la campagne » : elle dit « ne vous installez pas, sauf remplacement, là où il y a déjà assez de médecins ». Partout ailleurs, la liberté reste entière.\n\nLa droite n'est pas en reste : le sénateur LR Philippe Mouiller propose d'obliger les nouveaux médecins des zones bien dotées à exercer en partie dans les zones sous-denses. Les opposants estiment qu'on répartit la pénurie au lieu de former plus de médecins : c'est un argument sérieux, mais les inégalités d'accès sont massives.",
 detaille="Selon la DREES, en 2018, 5,7 % de la population vivait dans une zone sous-dotée en médecins généralistes, contre 3,8 % en 2015, et le quart de la population le moins bien servi ne dispose que de 19 % des généralistes. Les communes rurales sont surreprésentées, mais certaines banlieues aussi.\n\nLe texte Garot crée une autorisation d'installation délivrée par l'agence régionale de santé : accordée de droit en zone sous-dotée, et seulement en cas de départ d'un confrère en zone sur-dotée. Il prévoit aussi une première année d'études de médecine dans chaque département. Il a été adopté le 7 mai 2025 par 99 voix contre 9 ; le RN s'est abstenu.\n\nLa droite sénatoriale a préféré son propre dispositif, imposant un exercice partiel en zone sous-dense aux médecins qui s'installent en zone dense, et le gouvernement Bayrou avait proposé deux jours de consultations par mois en zone prioritaire. En juin 2026, le Sénat n'a pas adopté le texte Garot. Le ministre de la Santé et la profession y sont opposés : selon eux, il faut d'abord former plus de médecins.",
 empathie="Il est normal de défendre la liberté des médecins, qui ont fait de longues études. Mais quand des millions de personnes n'ont plus de médecin traitant, limiter les installations dans les zones déjà bien servies est une mesure modérée, soutenue bien au-delà de la gauche.",
 legitimes=["La régulation ne crée pas de médecins supplémentaires et risque de répartir la pénurie.", "La profession médicale y est fortement opposée."],
 contre=[
  ("Les médecins vont partir à l'étranger ou se déconventionner.", "Le risque est invoqué par les opposants ; aucune source lue ne permet de le mesurer."),
  ("Il suffit de former plus de médecins.", "Le texte prévoit aussi une première année de médecine dans chaque département, mais former prend dix ans."),
 ],
 questions=["Sais-tu que ce texte a été soutenu par des députés de tous les groupes ?", "Que proposer aux habitants qui n'ont plus de médecin traitant, en attendant que de nouveaux médecins soient formés ?"],
 limites=["Les données de la DREES sur les zones sous-dotées datent de 2018.", "Le texte n'est pas adopté : son application concrète reste incertaine."],
 publics={'convaincus': "Le texte Garot ne force personne à aller à la campagne : il limite seulement les nouvelles installations là où il y a déjà assez de médecins. Il a été voté par des députés des neuf groupes, et la droite sénatoriale propose aussi d'obliger les médecins à exercer en partie dans les zones sous-dotées. Qui défend les habitants sans médecin ?",
  'indecis': "La liberté d'installation est une vraie valeur pour les médecins, et former plus de médecins reste indispensable. Mais selon la DREES, le quart de la population le moins bien servi n'a que 19 % des généralistes. La régulation proposée est limitée aux zones déjà bien dotées, et l'idée est soutenue bien au-delà de la gauche."},
 a_actualiser='2027-06-30', raison="Suite de l'examen au Sénat.",
))

# 16 ── École privée ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='ecole-privee-meilleure', affirmation="L'école privée est meilleure que l'école publique.", volet='services', sous_theme='Inégalités scolaires',
 mots_cles=['ecole privee', 'enseignement prive', 'prive sous contrat', 'ecole privee meilleure', 'prive ou public', 'mettre ses enfants dans le prive', 'ips'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. Les résultats bruts du privé sous contrat sont « globalement meilleurs », mais selon la Cour des comptes, à composition sociale égale, sa performance « apparaît sensiblement la même que celle du public ». La différence vient surtout des élèves accueillis : 55,4 % d'élèves favorisés ou très favorisés dans le privé contre 32,3 % dans le public, et 11,8 % de boursiers contre 29,1 %. Et ce privé est financé à 55 % à 68 % par l'État.",
 contexte="Le choix du privé progresse chez les familles aisées et alimente l'idée d'un public en déclin.",
 explication="Comparer les résultats bruts revient à comparer des publics différents. Pour juger l'efficacité d'une école, il faut comparer des élèves d'origine sociale comparable, ce qu'on appelle la valeur ajoutée.",
 sources=[CC_PRIVE, LOC_PRIVE, LOC_IPS],
 faits=[
  fait("Les résultats du privé sous contrat « apparaissent globalement meilleurs que ceux du secteur public ».", 'cc_prive', '2023', 'France', "Le constat brut est exact.", 'etabli'),
  fait("Les travaux sur la valeur ajoutée « ne permettent pas d'identifier dans le privé sous contrat une plus-value » : à composition sociale égale, la performance « apparaît sensiblement la même que celle du public ».", 'cc_prive', '2023', 'France', "Le privé n'est pas plus efficace à élèves comparables.", 'etabli'),
  fait("Les élèves de milieux favorisés ou très favorisés représentent 55,4 % des élèves du privé en 2021, contre 32,3 % dans le public ; les boursiers 11,8 % contre 29,1 %.", 'cc_prive', '2021', 'France', "Le privé accueille un public beaucoup plus favorisé.", 'etabli', '55,4 % contre 32,3 %'),
  fait("Selon Localtis, d'après la Cour des comptes, la part d'élèves très favorisés dans le privé passe de 26,4 % en 2000 à 40,2 % en 2021.", 'loc_prive', '2000-2021', 'France', "L'écart social se creuse.", 'etabli'),
  fait("Selon la DEPP citée par Localtis, l'indice de position sociale moyen est de 125 dans les lycées privés sous contrat contre 105 dans les lycées publics.", 'loc_ips', '2025', 'France', "La différence de public est massive.", 'etabli'),
  fait("L'État verse 8 Md€ au privé sous contrat en 2022 et finance 55 % du premier degré privé et 68 % du second degré privé.", 'cc_prive', '2022', 'France', "Le privé est surtout financé par l'argent public.", 'etabli', '8 Md€'),
 ],
 court="Trompeur : le privé a de meilleurs résultats bruts parce qu'il accueille des élèves plus favorisés. À origine sociale égale, la Cour des comptes ne trouve pas de différence de performance avec le public.",
 moyen="Oui, les résultats bruts du privé sont meilleurs. Mais selon la Cour des comptes, quand on compare des élèves d'origine sociale comparable, la performance du privé « apparaît sensiblement la même que celle du public ». La différence vient des élèves : plus de la moitié sont issus de milieux favorisés, contre un tiers dans le public, et il y a deux fois et demie moins de boursiers.\n\nCe privé est financé majoritairement par l'argent public, 8 milliards d'euros de l'État en 2022, et il se ferme de plus en plus aux familles modestes. Le problème n'est pas la qualité des professeurs du public, mais la ségrégation sociale entre écoles.",
 detaille="La Cour des comptes a consacré en 2023 un rapport à l'enseignement privé sous contrat, qui scolarise environ 17,6 % des élèves. Elle constate que ses résultats « apparaissent globalement meilleurs », mais que les travaux sur la valeur ajoutée ne permettent pas d'y identifier une plus-value : à composition sociale égale, la performance est « sensiblement la même » que dans le public.\n\nLa différence de public est considérable : 55,4 % d'élèves favorisés ou très favorisés dans le privé en 2021, contre 32,3 % dans le public ; 11,8 % de boursiers contre 29,1 %. La part d'élèves très favorisés y est passée de 26,4 % en 2000 à 40,2 % en 2021. Selon la DEPP, l'indice de position sociale moyen des lycées privés est de 125, contre 105 pour les lycées publics.\n\nCe secteur est financé à 55 % (premier degré) et 68 % (second degré) par l'État, soit 8 Md€ en 2022, et son contrôle financier « n'est pas mis en œuvre », selon la Cour. Il faut toutefois noter que les écarts sociaux sont aussi importants entre établissements publics : la ségrégation scolaire n'est pas seulement une affaire de public et de privé.",
 empathie="Vouloir le meilleur pour ses enfants est la chose la plus normale du monde, et beaucoup de familles choisissent le privé par inquiétude. Les chiffres montrent que cette réussite tient surtout au public accueilli, pas à une meilleure pédagogie.",
 legitimes=["Les résultats bruts du privé sont meilleurs.", "Les écarts sociaux sont aussi importants entre établissements publics."],
 contre=[
  ("Le privé a de meilleures méthodes.", "Selon la Cour des comptes, à élèves comparables, il n'y a pas de différence de performance démontrée."),
  ("Le privé coûte moins cher à l'État.", "L'État le finance majoritairement, 8 Md€ en 2022, et les familles qui y accèdent sont plus aisées."),
 ],
 questions=["Sais-tu ce que dit la Cour des comptes quand on compare des élèves du même milieu social ?", "Est-il juste que l'argent public finance des écoles qui accueillent peu d'élèves modestes ?"],
 limites=["Les données datent de 2021-2022 ; la note de la DEPP sur les indices sociaux n'a été lue qu'à travers Localtis.", "La valeur ajoutée est difficile à mesurer, ce que la Cour reconnaît."],
 publics={'convaincus': "La Cour des comptes l'a vérifié : à élèves d'origine sociale comparable, le privé ne fait pas mieux que le public. S'il a de meilleurs résultats, c'est qu'il accueille 55 % d'élèves favorisés contre 32 % dans le public. Et l'État le finance à hauteur de 8 milliards par an.",
  'indecis': "Choisir le privé pour ses enfants se comprend. Mais selon la Cour des comptes, sa réussite tient surtout au milieu social de ses élèves, pas à une meilleure efficacité. Le vrai enjeu, c'est la mixité sociale dans toutes les écoles, publiques comme privées."},
 a_actualiser='2027-06-30', raison="Nouvelles données de la DEPP sur la composition sociale.",
))

# 17 ── Mères voilées et sorties scolaires ───────────────────────────────────
FICHES.append(fiche(
 id='meres-voilees-sorties-scolaires', affirmation="Les mères voilées n'ont pas le droit d'accompagner les sorties scolaires.", volet='droits', sous_theme='Laïcité',
 mots_cles=['meres voilees', 'mamans voilees', 'sorties scolaires', 'accompagnatrices voilees', 'parents accompagnateurs', 'voile sortie scolaire', 'accompagner une sortie scolaire'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux. Aucun texte de loi ou règlement n'interdit le voile aux mères qui accompagnent une sortie scolaire. Selon l'étude du Conseil d'État de 2013, les parents accompagnateurs sont des « usagers » du service public, non soumis à la neutralité des agents ; des restrictions restent possibles au cas par cas, par exemple en cas de prosélytisme. Le Sénat a voté l'interdiction plusieurs fois depuis 2019, mais aucune n'est devenue loi.",
 contexte="La question revient régulièrement, souvent à l'occasion d'incidents médiatisés ou de propositions de loi de la droite et de l'extrême droite.",
 explication="La laïcité impose la neutralité religieuse à l'État et à ses agents, et la loi de 2004 l'impose aux élèves des écoles publiques. Les parents, eux, sont des usagers du service public.",
 sources=[AN_VOILE, SURL_VOILE, PS_VOILE19, PS_VOILE_PPL, PS_VOILE21],
 faits=[
  fait("Selon la réponse ministérielle de 2015, la neutralité des parents accompagnateurs « ne fait pas l'objet de dispositions législatives ou réglementaires spécifiques ».", 'an_voile', '2015', 'France', "Aucun texte n'interdit le voile aux accompagnatrices.", 'etabli'),
  fait("Selon l'étude du Conseil d'État de 2013 citée par le ministère, les parents d'élèves doivent être regardés comme des usagers du service public de l'éducation.", 'an_voile', '2013', 'France', "La neutralité des agents ne leur est pas imposée.", 'etabli'),
  fait("Le ministère précise qu'on peut demander aux parents de s'abstenir de manifester leurs croyances « en cas de risque de prosélytisme », au cas par cas.", 'an_voile', '2015', 'France', "Des restrictions ponctuelles sont possibles.", 'etabli'),
  fait("Selon Les Surligneurs, un tribunal administratif a validé un règlement imposant la neutralité aux parents, dans la ligne d'une circulaire de 2012, et la position du Conseil d'État est jugée « fragile ».", 'surl_voile', '2025', 'France', "Le droit n'est pas totalement figé.", 'etabli'),
  fait("Selon Public Sénat, le Sénat a voté l'interdiction en 2019, puis en 2021 par 177 voix contre 141 ; le ministre Gérald Darmanin évoquait un risque de censure constitutionnelle.", 'ps_voile21', '2019-2021', 'France', "Ces votes ne sont pas devenus loi.", 'etabli'),
  fait("Selon Public Sénat, l'amendement adopté par le Sénat en mai 2019 a été retiré en commission mixte paritaire.", 'ps_voile19', '2019', 'France', "Le Parlement n'a pas inscrit l'interdiction dans la loi.", 'etabli'),
 ],
 court="Faux : aucune loi n'interdit le voile aux mères qui accompagnent une sortie scolaire. Pour le Conseil d'État, ce sont des usagers du service public, pas des agents tenus à la neutralité. Des restrictions sont possibles au cas par cas.",
 moyen="La laïcité impose la neutralité aux enseignants et, depuis 2004, interdit les signes religieux ostensibles aux élèves. Les parents qui accompagnent une sortie, eux, ne sont pas des agents publics : le Conseil d'État les considère depuis 2013 comme des usagers du service public. Aucun texte ne leur interdit le voile.\n\nUn directeur peut demander une abstention en cas de prosélytisme, au cas par cas. Le Sénat a plusieurs fois voté une interdiction générale, mais elle n'a jamais été adoptée, notamment à cause du risque de discrimination.",
 detaille="Selon la réponse du ministère de l'Éducation nationale publiée en 2015, la neutralité des parents accompagnateurs ne fait l'objet d'aucune disposition législative ou réglementaire spécifique. Le ministère s'appuie sur l'étude du Conseil d'État du 19 décembre 2013, qui considère les parents comme des usagers du service public. Des restrictions sont possibles en cas de prosélytisme ou de trouble, et les circonstances sont déterminantes.\n\nLe droit n'est pas parfaitement fixé : une circulaire de 2012 allait vers la neutralité, un tribunal administratif a validé un règlement intérieur l'imposant, et Les Surligneurs jugent la position du Conseil d'État « fragile ». Une interdiction visant le seul voile serait en revanche discriminatoire.\n\nPolitiquement, le Sénat a voté l'interdiction en mai 2019, en octobre 2019 (163 voix contre 114) et en mars 2021 (177 voix contre 141). Aucune de ces mesures n'est devenue loi : l'amendement de 2019 a été retiré en commission mixte paritaire, et les gouvernements successifs s'y sont opposés, évoquant un risque de censure.",
 empathie="Tu peux être attaché à la laïcité à l'école, c'est un principe précieux. La laïcité protège justement les enfants du prosélytisme, mais elle n'oblige pas leurs parents à se cacher.",
 legitimes=["Des restrictions au cas par cas sont possibles en cas de prosélytisme.", "Une circulaire de 2012 et un jugement allaient vers une neutralité des parents."],
 contre=[
  ("Pendant la sortie, la mère représente l'école.", "Le Conseil d'État la considère comme une usagère, non comme une agente du service public."),
  ("Le Sénat a voté l'interdiction.", "Oui, plusieurs fois, mais aucune de ces mesures n'est devenue loi."),
 ],
 questions=["Sais-tu ce que dit le Conseil d'État sur les parents accompagnateurs ?", "Qui accompagnera les sorties si l'on exclut une partie des parents volontaires ?"],
 limites=["L'étude du Conseil d'État de 2013 n'a pas été lue directement, mais à travers la réponse ministérielle et Les Surligneurs.", "Le sort final de l'amendement sénatorial de 2021 n'a pas été vérifié sur Légifrance."],
 publics={'convaincus': "Aucune loi n'interdit à une mère voilée d'accompagner une sortie : le ministère l'a confirmé en 2015, en s'appuyant sur le Conseil d'État. La neutralité, c'est pour les agents de l'État, pas pour les parents. Le Sénat a voulu l'interdire plusieurs fois, et ça n'est jamais passé, notamment parce que ce serait discriminatoire.",
  'indecis': "La laïcité impose la neutralité aux enseignants et aux élèves, pas aux parents, que le Conseil d'État considère comme des usagers. Un directeur peut intervenir en cas de prosélytisme. La question est surtout de savoir si l'on veut associer tous les parents à la vie de l'école."},
 a_actualiser='2027-06-30', raison="Nouvelles propositions de loi ou jurisprudence.",
))

# 18 ── Conseil constitutionnel et « gouvernement des juges » ────────────────
FICHES.append(fiche(
 id='conseil-constitutionnel-gouvernement-juges', affirmation="Le Conseil constitutionnel empêche la volonté du peuple, c'est le gouvernement des juges.", volet='politique', sous_theme='Constitution',
 mots_cles=['conseil constitutionnel', 'gouvernement des juges', 'sages', 'censure de la loi immigration', 'cavaliers legislatifs', 'juges constitutionnels', 'etat de droit'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. En janvier 2024, le Conseil constitutionnel a censuré 35 des 86 articles de la loi immigration, mais 32 l'ont été comme « cavaliers législatifs », c'est-à-dire pour une raison de procédure : ces mesures, ajoutées à un projet initial de 27 articles, n'avaient pas de lien avec lui. Seuls 3 articles l'ont été sur le fond. Surtout, le dernier mot appartient au peuple et à ses représentants : la Constitution peut être révisée, comme en 1993 après la censure de la loi Pasqua.",
 contexte="Après la censure de la loi immigration, une partie de la droite et l'extrême droite ont dénoncé un « gouvernement des juges ».",
 explication="Le Conseil constitutionnel vérifie que les lois respectent la Constitution, y compris la procédure. Un « cavalier » est un article ajouté à un texte sans lien avec son objet : il est censuré sans que son contenu soit jugé.",
 sources=[LCP_CC24, AJ_CC24, AN_REV, SEN_REV, PS_LR_CC],
 faits=[
  fait("Selon LCP, sur les 86 articles de la loi immigration, 35 ont été censurés totalement ou partiellement, dont 32 comme « cavaliers législatifs » et 3 sur le fond.", 'lcp_cc24', '2024', 'France', "La censure est surtout procédurale.", 'etabli', '32 sur 35'),
  fait("Selon Actu-Juridique, le projet initial comportait 27 articles, et « la censure de cavaliers ne préjuge en effet en rien de la constitutionnalité au fond ».", 'aj_cc24', '2024', 'France', "Les mesures censurées peuvent revenir dans un texte adapté.", 'etabli'),
  fait("Selon LCP, ont été censurés sur le fond les quotas migratoires votés chaque année par le Parlement et la prise d'empreintes sans consentement.", 'lcp_cc24', '2024', 'France', "Il y a eu aussi des censures de fond.", 'etabli'),
  fait("La Constitution peut être révisée à l'initiative du Président de la République ou des parlementaires, puis adoptée par référendum ou par le Congrès à la majorité des trois cinquièmes.", 'an_rev', '2026', 'France', "Le dernier mot appartient au constituant.", 'etabli'),
  fait("Après la censure partielle de la loi Pasqua en août 1993, le gouvernement a fait réviser la Constitution dès novembre 1993.", 'sen_rev', '1993', 'France', "Une censure peut être surmontée démocratiquement.", 'etabli'),
  fait("Selon Public Sénat, des responsables LR comme Gérard Larcher et Bruno Retailleau ont réclamé une révision constitutionnelle après la décision de 2024.", 'ps_lr_cc', '2024', 'France', "La critique du Conseil dépasse l'extrême droite.", 'etabli'),
 ],
 court="Trompeur : la plupart des articles censurés de la loi immigration l'ont été pour une raison de procédure, pas de fond. Et si le peuple veut changer la règle, il peut réviser la Constitution, comme en 1993.",
 moyen="En janvier 2024, le Conseil constitutionnel a censuré 35 articles de la loi immigration, dont 32 parce qu'ils avaient été ajoutés sans lien avec le projet initial. Cela ne dit rien de leur contenu : ils peuvent être repris dans un texte adapté. Seuls trois articles ont été censurés sur le fond.\n\nLe Conseil ne fait qu'appliquer une Constitution adoptée par le peuple. Si une majorité veut changer cette Constitution, elle peut le faire, par le Parlement réuni en Congrès ou par référendum : c'est arrivé en 1993. Ce qui dérange, ce n'est pas un gouvernement des juges, c'est qu'il existe des limites aux majorités du moment.",
 detaille="Le projet de loi immigration comportait 27 articles ; la loi votée en décembre 2023 en comptait 86. Le 25 janvier 2024, le Conseil constitutionnel en a censuré 35 en tout ou partie : 32 comme cavaliers législatifs, sur le fondement de l'article 45 de la Constitution, et 3 sur le fond, dont les quotas migratoires annuels et la prise d'empreintes sans consentement. Parmi les cavaliers figuraient des restrictions aux prestations familiales, au regroupement familial et au droit du sol.\n\nUne censure pour cavalier ne juge pas le fond : elle sanctionne une procédure. Le ministre de l'Intérieur de l'époque affirmait d'ailleurs que le texte du gouvernement était validé dans son « intégralité ».\n\nSurtout, la Constitution n'est pas figée. Elle peut être révisée à l'initiative du Président ou des parlementaires, puis adoptée par référendum ou par le Congrès. En 1993, après la censure partielle de la loi Pasqua, le gouvernement l'a fait réviser en trois mois. Le contrôle des lois protège les droits de chacun, y compris des minorités politiques, contre une majorité passagère.",
 empathie="On peut être frustré de voir une loi votée par ses élus censurée. Mais les règles du jeu valent pour tous les gouvernements, y compris ceux qu'on n'aime pas, et le peuple garde le pouvoir de les changer.",
 legitimes=["Le Conseil a aussi censuré des mesures sur le fond.", "La notion de gouvernement des juges est un débat ancien, et des responsables LR ont critiqué la décision."],
 contre=[
  ("Les membres du Conseil sont nommés, pas élus.", "Ils appliquent une Constitution que le peuple peut réviser, par référendum ou par le Congrès."),
  ("Ils ont censuré la volonté du Parlement.", "Pour l'essentiel, ils ont sanctionné des ajouts sans lien avec le texte, une règle de procédure parlementaire."),
 ],
 questions=["Sais-tu pourquoi la plupart des articles de la loi immigration ont été censurés ?", "Voudrais-tu qu'un futur gouvernement qui te déplaît puisse voter n'importe quelle loi sans contrôle ?"],
 limites=["La décision n° 2023-863 DC n'a pas pu être lue sur le site du Conseil constitutionnel : les chiffres viennent de LCP et d'Actu-Juridique.", "La part des censures dans l'ensemble des décisions n'a pas été établie par une source lue."],
 publics={'convaincus': "Sur la loi immigration, 32 des 35 articles censurés l'ont été parce qu'ils avaient été ajoutés sans lien avec le projet : c'est une règle de procédure, pas un jugement sur le fond. Et si le peuple veut changer la Constitution, il peut le faire par référendum ou par le Congrès, comme en 1993. Où est la dictature des juges ?",
  'indecis': "Voir une loi votée censurée peut frustrer, et la critique du Conseil vient aussi de la droite classique. Mais pour la loi immigration, l'essentiel de la censure tenait à la procédure. Et le dernier mot reste au peuple, qui peut réviser la Constitution."},
 a_actualiser='2028-06-30', raison="Nouvelles décisions majeures ou révision constitutionnelle.",
))

# 19 ── Narcotrafic ──────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='narcotrafic-explosion', affirmation="Le narcotrafic explose en France.", volet='securite', sous_theme='Criminalité organisée',
 mots_cles=['narcotrafic', 'trafic de drogue', 'narchomicides', 'cocaine', 'points de deal', 'narcotrafiquants', 'saisies de drogue', 'trafic de stupefiants'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="Plutôt vrai pour la cocaïne : les saisies sont passées de 23 tonnes en 2023 à 53,5 tonnes en 2024 et 84,3 tonnes en 2025, et le nombre d'usagers a presque doublé, à 1,1 million. Le Sénat, dans un rapport transpartisan, parle de « submersion ». Mais les morts liés au trafic ont baissé entre 2023 et 2024 (139 puis 110), et la consommation de cannabis est stable. La réponse de gauche porte sur la demande, le blanchiment et les moyens des enquêteurs.",
 contexte="Les règlements de comptes à Marseille, Nîmes ou Grenoble ont fait du narcotrafic un thème central du débat sur la sécurité.",
 explication="Les saisies mesurent à la fois le trafic et l'activité des services : une hausse peut refléter plus de drogue et plus de contrôles. Les homicides liés au trafic et la consommation sont d'autres indicateurs.",
 sources=[SEN_NARCO, SEN_LOI_NARCO, AFP_NARCO24, AFP_NARCO25, AFP_OFDT],
 faits=[
  fait("Selon l'AFP, d'après le ministère de l'Intérieur, 53,5 tonnes de cocaïne ont été saisies en 2024, contre 23 tonnes en 2023.", 'afp_narco24', '2023-2024', 'France', "Le trafic de cocaïne progresse fortement.", 'etabli', '+130 %'),
  fait("Selon l'AFP, d'après le ministre de l'Intérieur, 84,3 tonnes de cocaïne ont été saisies en 2025, et les mis en cause augmentent d'environ 7 % par an depuis 2017.", 'afp_narco25', '2017-2025', 'France', "La hausse se poursuit.", 'etabli', '84,3 tonnes'),
  fait("Selon l'OFDT cité par l'AFP, 1,1 million de personnes ont consommé de la cocaïne dans l'année en 2023, contre 600 000 dans le rapport précédent.", 'afp_ofdt', '2023', 'France', "La demande de cocaïne explose.", 'etabli', '1,1 million'),
  fait("Selon l'AFP, 110 personnes sont mortes en lien avec le narcotrafic en 2024, contre 139 en 2023 ; les homicides et tentatives passent de 418 à 367.", 'afp_narco24', '2023-2024', 'France', "Les violences mortelles ont baissé en 2024.", 'etabli'),
  fait("Selon le rapport du Sénat, le chiffre d'affaires du trafic atteint au moins 3,5 milliards d'euros, et 80 à 90 % des règlements de comptes entre délinquants sont liés aux stupéfiants.", 'sen_narco', '2024', 'France', "Le trafic est un marché massif et violent.", 'etabli'),
  fait("Selon l'OFDT cité par l'AFP, la consommation de cannabis est « relativement stable », autour de 5 millions d'usagers dans l'année.", 'afp_ofdt', '2023', 'France', "Tout le marché n'explose pas.", 'etabli'),
  fait("La loi du 13 juin 2025 crée un parquet national anti-criminalité organisée et des quartiers de lutte contre la criminalité organisée en prison.", 'sen_loi_narco', '2025', 'France', "L'État a renforcé son arsenal.", 'etabli'),
 ],
 court="Plutôt vrai pour la cocaïne : saisies multipliées par près de quatre entre 2023 et 2025, et 1,1 million d'usagers. Mais les morts liés au trafic ont baissé en 2024, et le cannabis est stable.",
 moyen="Le trafic de cocaïne progresse fortement : 23 tonnes saisies en 2023, 84,3 tonnes en 2025, et le nombre d'usagers a presque doublé. Le Sénat, dans un rapport porté par un socialiste et un LR, parle de « submersion » et d'un marché d'au moins 3,5 milliards d'euros.\n\nLe tableau est plus nuancé ailleurs : les morts liés au trafic ont baissé en 2024, et la consommation de cannabis est stable. Pour lutter contre ce marché, il faut s'attaquer à l'argent, au blanchiment, aux têtes de réseau, et à la demande, pas seulement aux petits revendeurs.",
 detaille="Tous les indicateurs liés à la cocaïne sont à la hausse. Selon le ministère de l'Intérieur, les saisies sont passées de 23 tonnes en 2023 à 53,5 tonnes en 2024 puis 84,3 tonnes en 2025, et les mis en cause augmentent d'environ 7 % par an depuis 2017. Selon l'OFDT, 1,1 million de personnes ont consommé de la cocaïne dans l'année en 2023, presque deux fois plus que dans l'enquête précédente.\n\nLa commission d'enquête du Sénat, présidée par le socialiste Jérôme Durain avec le LR Étienne Blanc pour rapporteur, parle de « submersion ». Elle chiffre le marché à au moins 3,5 milliards d'euros et relève que 80 à 90 % des règlements de comptes entre délinquants sont liés au trafic, tout en soulignant le manque de moyens de l'office antistupéfiants. La loi du 13 juin 2025 a créé un parquet spécialisé.\n\nD'autres indicateurs sont plus stables : 110 morts liés au trafic en 2024 contre 139 en 2023, et une consommation de cannabis stable. Les saisies mesurent aussi l'activité des services, pas seulement le volume du trafic.",
 empathie="Voir des fusillades dans des quartiers où vivent des familles est terrifiant, et l'inquiétude est légitime. Les chiffres confirment que le trafic de cocaïne progresse fortement ; la question est de savoir comment frapper les réseaux là où ça leur fait mal.",
 legitimes=["Le trafic de cocaïne et sa consommation progressent fortement.", "Le Sénat, de façon transpartisane, parle de « submersion »."],
 contre=[
  ("C'est la faute de l'immigration.", "Les sources lues décrivent un marché porté par la demande française de cocaïne et des réseaux criminels, sans en faire une question d'origine."),
  ("Il faut juste plus de répression.", "Le Sénat insiste aussi sur les moyens d'enquête, le blanchiment et la corruption."),
 ],
 questions=["Sais-tu que la consommation de cocaïne a presque doublé en France ?", "Qui achète la drogue que vendent les trafiquants ?"],
 limites=["Les chiffres du ministère de l'Intérieur et de l'OFDT ont été lus à travers des dépêches de l'AFP.", "Les saisies dépendent aussi de l'activité des services."],
 publics={'convaincus': "Tu as raison sur la cocaïne : les saisies ont presque quadruplé entre 2023 et 2025. Mais demande-toi qui consomme : 1,1 million de Français en ont pris en 2023, selon l'OFDT. Le Sénat demande surtout des moyens pour frapper l'argent et les têtes de réseau, pas seulement les guetteurs.",
  'indecis': "Le trafic de cocaïne progresse vraiment, et le Sénat parle de « submersion ». Les violences mortelles ont pourtant baissé en 2024, et le cannabis est stable. Pour agir, il faut viser l'argent des réseaux, le blanchiment et la demande."},
 a_actualiser='2027-03-31', raison="Bilan annuel du ministère de l'Intérieur et de l'OFDT.",
))

# 20 ── Hôpital : administratifs et soignants ────────────────────────────────
FICHES.append(fiche(
 id='hopital-administratifs-soignants', affirmation="À l'hôpital, il y a plus d'administratifs que de soignants.", volet='services', sous_theme='Hôpital public',
 mots_cles=['administratifs a l hopital', 'bureaucratie hospitaliere', 'plus d administratifs que de soignants', 'personnel administratif', 'soignants', 'hopital bureaucratie', 'non soignants'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux. Selon la DREES, fin 2024, les établissements de santé comptent 797 151 postes de soignants non médicaux contre 161 924 postes administratifs, soit près de cinq fois plus, sans compter 231 800 postes de médecins, pharmaciens et sages-femmes. Les administratifs représentent environ 14 % des postes non médicaux. La France a en revanche une part de personnels non soignants (administratifs, techniques, agents de service) plus élevée que plusieurs voisins, et la lourdeur administrative est réelle.",
 contexte="La « bureaucratie » hospitalière est souvent accusée d'expliquer la crise de l'hôpital, au détriment des moyens.",
 explication="Les personnels non soignants comprennent les administratifs, mais aussi les techniciens, les agents d'entretien, les cuisiniers ou les brancardiers, sans lesquels un hôpital ne fonctionne pas.",
 sources=[DREES_PNM, DREES_PM, AP_HOP, AP_JOMIER],
 faits=[
  fait("Fin 2024, les établissements de santé comptent 797 151 postes de soignants non médicaux et 161 924 postes administratifs.", 'drees_pnm', '2024', 'France', "Il y a près de cinq soignants pour un administratif.", 'etabli', '797 151 contre 161 924'),
  fait("Dans les hôpitaux publics, on compte 576 868 postes de soignants pour 110 089 postes administratifs.", 'drees_pnm', '2024', 'Hôpitaux publics', "Le constat vaut aussi pour l'hôpital public.", 'etabli'),
  fait("S'y ajoutent 231 800 postes de personnel médical ou pharmaceutique, dont 126 800 médecins, odontologistes et pharmaciens salariés et 45 200 internes et docteurs juniors.", 'drees_pm', '2024', 'France', "Les soignants sont encore plus majoritaires.", 'etabli'),
  fait("Selon l'OCDE citée par Acteurs publics, la France compte 34 % de personnels non soignants à l'hôpital, dont 14 % d'administratifs, contre 25 % de non-soignants en Allemagne ; l'écart s'explique en partie par l'externalisation chez les voisins.", 'ap_hop', '2025', 'France et Europe', "La France a plus de non-soignants que certains voisins.", 'etabli'),
  fait("Selon Acteurs publics, le président de la commission d'enquête du Sénat sur l'hôpital juge que « nous ne sommes pas dans des niveaux à près de 50% de postes de direction et administratifs ».", 'ap_jomier', '2025', 'France', "La bureaucratie existe, mais sans commune mesure avec le cliché.", 'etabli'),
 ],
 court="Faux : selon la DREES, il y a près de cinq postes de soignants pour un poste administratif à l'hôpital, sans compter les médecins. La lourdeur administrative est réelle, mais les soignants restent très largement majoritaires.",
 moyen="Les chiffres de la DREES pour 2024 sont nets : 797 151 postes de soignants non médicaux, 161 924 postes administratifs, et en plus 231 800 postes de médecins, pharmaciens et sages-femmes. Les administratifs représentent environ 14 % du personnel non médical.\n\nLa France compte bien plus de personnels non soignants que l'Allemagne selon l'OCDE, mais cela inclut techniciens et agents de service, souvent externalisés ailleurs. La paperasse épuise les équipes, c'est vrai. Mais si l'hôpital manque de bras, c'est d'abord de soignants, pas parce qu'ils seraient minoritaires.",
 detaille="Selon la DREES, au 31 décembre 2024, les établissements de santé comptent 1 170 588 postes de personnel non médical salarié, dont 797 151 soignants, 161 924 administratifs, 123 907 techniques et 65 065 médico-techniques. Dans le public, on compte 576 868 soignants pour 110 089 administratifs. S'ajoutent 231 800 postes médicaux ou pharmaceutiques. Ces chiffres comptent des postes, pas des personnes.\n\nLes comparaisons internationales nuancent le tableau : selon l'OCDE citée par Acteurs publics, les non-soignants représentent 34 % du personnel hospitalier en France, dont 14 % d'administratifs, contre 25 % en Allemagne et en Italie. L'écart s'explique en partie par l'externalisation de services chez nos voisins. À l'AP-HP, les fonctions administratives et de direction représentent 6,8 % des effectifs.\n\nLe président de la commission d'enquête du Sénat sur l'hôpital estime que la France ne se distingue pas fortement de ses voisins, mais un syndicat de directeurs décrit plus de 200 demandes de reporting par an : la lourdeur vient aussi des exigences de l'État.",
 empathie="Beaucoup de soignants se plaignent de passer trop de temps sur des papiers, et ils ont raison. Mais l'idée qu'il y aurait plus de bureaucrates que de soignants ne correspond pas aux chiffres.",
 legitimes=["La part des personnels non soignants est plus élevée en France qu'en Allemagne ou en Italie.", "La charge administrative pesant sur les équipes est réelle."],
 contre=[
  ("Il suffit de supprimer des postes administratifs.", "Les administratifs gèrent aussi les admissions, la paie ou la facturation ; la lourdeur vient en partie des demandes de reporting de l'État."),
  ("L'OCDE dit 34 % de non-soignants.", "Ce chiffre inclut techniciens et agents de service ; les administratifs en représentent 14 %."),
 ],
 questions=["Sais-tu combien de soignants il y a pour un administratif à l'hôpital ?", "Qui impose les tâches administratives qui pèsent sur les soignants ?"],
 limites=["La DREES compte des postes, pas des personnes.", "Les comparaisons de l'OCDE ont été lues à travers la presse spécialisée."],
 publics={'convaincus': "Selon la DREES, fin 2024, il y a 797 151 postes de soignants pour 161 924 postes administratifs dans les établissements de santé, sans compter les médecins. Près de cinq pour un. La paperasse pèse, mais ce n'est pas les administratifs qui manquent : ce sont les infirmières.",
  'indecis': "La lourdeur administrative à l'hôpital est réelle, et la France a plus de personnels non soignants que l'Allemagne. Mais les soignants restent très largement majoritaires : près de cinq pour un administratif selon la DREES. Pour améliorer l'hôpital, il faut alléger les procédures et embaucher des soignants."},
 a_actualiser='2027-09-30', raison="Nouvelle édition de la DREES sur les établissements de santé.",
))

# 21 ── Le RN, rempart contre l'antisémitisme ? ──────────────────────────────
FICHES.append(fiche(
 id='rn-rempart-antisemitisme', affirmation="Le RN est le meilleur rempart contre l'antisémitisme.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['rempart contre l antisemitisme', 'rn rempart', 'le rn protege les juifs', 'bouclier des juifs', 'rn et les juifs', 'rn antisemitisme'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. Selon les données de la CNCDH analysées par Nonna Mayer, fin 2025, 48 % des sympathisants RN adhèrent à des préjugés antisémites, autant que chez LFI (47 %). Le fondateur du FN a été condamné définitivement pour avoir qualifié les chambres à gaz de « détail ». Le RN a pris ses distances, et ces préjugés ont reculé chez ses sympathisants alors qu'ils ont progressé à LFI ; mais la chercheuse décrit une instrumentalisation de l'antisémitisme « à front renversé », pas une protection.",
 contexte="Depuis le 7 octobre 2023, Marine Le Pen et Jordan Bardella se présentent comme les défenseurs des Français juifs face à l'islamisme et à LFI.",
 explication="Les enquêtes de la CNCDH mesurent l'adhésion aux préjugés (par exemple sur l'argent ou le pouvoir) selon la proximité politique. Elles mesurent des opinions, pas des actes.",
 sources=[LDH_MAYER, CNCDH_CP25, PS_LEPEN_DETAIL, AFP_LEPEN],
 faits=[
  fait("Selon l'analyse par Nonna Mayer du baromètre de la CNCDH, fin 2025, 48 % des sympathisants RN et 47 % de ceux de LFI ont un score de préjugés antisémites égal ou supérieur à 2 sur 5.", 'ldh_mayer', '2025', 'France', "L'électorat RN n'est pas épargné par ces préjugés.", 'etabli', '48 %'),
  fait("Selon la même analyse, en trois ans, ces préjugés ont baissé de 7 points chez les sympathisants RN et augmenté de 10 points chez ceux de LFI, un niveau « jamais atteint jusqu'ici chez les Insoumis ».", 'ldh_mayer', '2022-2025', 'France', "L'antisémitisme progresse aussi à gauche.", 'etabli'),
  fait("Selon Nonna Mayer, l'antisémitisme est instrumentalisé « à front renversé » depuis le 7 octobre : Marine Le Pen met en avant la défense d'Israël pour se présenter en rempart des Français juifs.", 'ldh_mayer', '2023-2025', 'France', "La posture du RN relève de la stratégie politique.", 'etabli'),
  fait("1 320 faits antisémites ont été recensés en 2025, et 35 % des personnes interrogées pensent que « les Juifs ont un rapport particulier à l'argent ».", 'cncdh_cp25', '2025', 'France', "L'antisémitisme reste massif dans toute la société.", 'etabli'),
  fait("Selon Public Sénat, la Cour de cassation a rendu définitive en 2018 la condamnation de Jean-Marie Le Pen pour contestation de crime contre l'humanité ; il avait été exclu du parti.", 'ps_lepen_detail', '2015-2018', 'France', "Le parti a un passé lourd, dont il s'est en partie démarqué.", 'etabli'),
  fait("Selon l'AFP, Jean-Marie Le Pen a aussi été condamné pour avoir dit que l'Occupation allemande n'avait pas été « particulièrement inhumaine » et pour le jeu de mots « Durafour crématoire ».", 'afp_lepen', '1993-2012', 'France', "Les condamnations du fondateur sont nombreuses.", 'etabli'),
 ],
 court="Trompeur : fin 2025, 48 % des sympathisants RN partagent des préjugés antisémites selon les données de la CNCDH, autant qu'à LFI. Le fondateur du FN a été condamné pour avoir qualifié les chambres à gaz de « détail ».",
 moyen="Les données de la CNCDH, analysées par la politiste Nonna Mayer, montrent que fin 2025, 48 % des sympathisants RN adhèrent à des préjugés antisémites, autant que ceux de LFI. Il faut le dire honnêtement : ces préjugés ont reculé chez les électeurs RN et nettement progressé chez les Insoumis, ce qui doit inquiéter la gauche.\n\nMais un « rempart » ? Le parti a été fondé par un homme condamné définitivement pour avoir qualifié les chambres à gaz de « détail ». La chercheuse parle d'une instrumentalisation de l'antisémitisme « à front renversé » : se proclamer défenseur des Juifs ne suffit pas à les protéger. Lutter contre l'antisémitisme suppose de lutter contre tous les racismes.",
 detaille="La CNCDH recense 1 320 faits antisémites en 2025, et 35 % des personnes interrogées adhèrent au préjugé sur le rapport des Juifs à l'argent. Selon l'analyse de Nonna Mayer, fin 2025, 48 % des sympathisants RN et 47 % des sympathisants LFI ont un score de préjugés antisémites de 2 sur 5 ou plus. En trois ans, ce score a baissé de 7 points au RN et augmenté de 10 points à LFI, un niveau inédit chez les Insoumis. Les proches de la gauche restent globalement les plus tolérants.\n\nLe Front national a été fondé et dirigé par Jean-Marie Le Pen, condamné définitivement pour contestation de crime contre l'humanité, et aussi pour ses propos sur l'Occupation et le jeu de mots « Durafour crématoire ». Marine Le Pen a critiqué ces propos et son père a été exclu du parti.\n\nNonna Mayer décrit depuis le 7 octobre une instrumentalisation « à front renversé » : Marine Le Pen met en avant la défense d'Israël pour se présenter en rempart des Français juifs, tandis que Jean-Luc Mélenchon tient des propos que l'autrice juge proches de l'antisémitisme. Aucun parti ne peut se dire rempart quand près de la moitié de ses sympathisants partagent ces préjugés.",
 empathie="L'inquiétude face à la montée de l'antisémitisme est légitime, et elle concerne aussi la gauche. Mais il vaut mieux regarder ce que pensent réellement les électeurs de chaque parti que se fier aux slogans.",
 legitimes=["Les préjugés antisémites ont reculé chez les sympathisants RN et progressé chez ceux de LFI.", "Marine Le Pen a pris ses distances avec les propos de son père, exclu du parti."],
 contre=[
  ("Aujourd'hui, l'antisémitisme est à gauche.", "Il progresse à LFI, c'est vrai ; mais il est au même niveau chez les sympathisants RN."),
  ("Le RN a changé.", "Le RN a exclu son fondateur, mais près de la moitié de ses sympathisants partagent des préjugés antisémites selon les données de la CNCDH."),
 ],
 questions=["Savais-tu que les préjugés antisémites sont aussi répandus chez les sympathisants RN que chez ceux de LFI ?", "Un parti peut-il combattre un racisme tout en en tolérant d'autres ?"],
 limites=["Le rapport complet de la CNCDH n'a pas été lu ; les résultats par parti viennent de l'analyse de Nonna Mayer.", "Les préjugés mesurés par sondage ne disent rien des actes antisémites."],
 publics={'convaincus': "Selon les données de la CNCDH, fin 2025, 48 % des sympathisants RN partagent des préjugés antisémites, autant qu'à LFI. Le fondateur du parti a été condamné pour avoir qualifié les chambres à gaz de « détail ». Se proclamer rempart ne suffit pas : il faut regarder ce que pensent les électeurs et d'où vient le parti.",
  'indecis': "L'antisémitisme progresse, y compris à gauche, et c'est un vrai sujet. Mais selon les enquêtes de la CNCDH, les préjugés antisémites sont aussi répandus chez les sympathisants RN que chez ceux de LFI. Aucun parti ne peut se présenter comme un rempart : la lutte contre l'antisémitisme passe par la lutte contre tous les racismes."},
 a_actualiser='2027-06-30', raison="Rapport 2026 de la CNCDH.",
))

# 22 ── Torture pendant la guerre d'Algérie ──────────────────────────────────
FICHES.append(fiche(
 id='torture-guerre-algerie', affirmation="Pendant la guerre d'Algérie, la torture était l'exception.", volet='international', sous_theme='Colonisation et décolonisation',
 mots_cles=['torture en algerie', 'guerre d algerie', 'torture', 'maurice audin', 'ali boumendjel', 'bataille d alger', 'aussaresses', 'pouvoirs speciaux'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux. L'État français reconnaît officiellement depuis 2018 que la mort de Maurice Audin a été rendue possible par « un système légalement institué », fondé sur les pouvoirs spéciaux votés en 1956, et que la torture « restait impunie parce qu'elle était conçue comme une arme contre le FLN ». L'historienne Raphaëlle Branche la décrit comme « massive », « quotidienne, banale ». Tous les soldats n'ont pas torturé : la pratique relevait surtout d'unités spécialisées, mais elle était couverte par la hiérarchie.",
 contexte="La mémoire de la guerre d'Algérie reste conflictuelle ; une partie de la droite et de l'extrême droite refuse ce qu'elle appelle la « repentance ».",
 explication="Dire que la torture était « systématique » ne signifie pas que chaque soldat a torturé, mais qu'elle relevait d'un système toléré, organisé et couvert par l'État.",
 sources=[ELY_AUDIN, ELY_BOUMENDJEL, BRANCHE],
 faits=[
  fait("Selon la déclaration du président de la République de 2018, la mort de Maurice Audin a été rendue possible par « un système légalement institué qui a favorisé les disparitions », fondé sur les pouvoirs spéciaux de 1956.", 'ely_audin', '1956-1957', 'Algérie', "L'État reconnaît un système, pas une bavure.", 'etabli'),
  fait("Selon la même déclaration, la torture « restait impunie parce qu'elle était conçue comme une arme contre le FLN ».", 'ely_audin', '1954-1962', 'Algérie', "La torture était une méthode de guerre.", 'etabli'),
  fait("Selon le communiqué de l'Élysée de 2021, Ali Boumendjel « a été torturé puis assassiné » en 1957, et le crime a été maquillé en suicide sur ordre de Paul Aussaresses, selon ses propres aveux.", 'ely_boumendjel', '1957', 'Algérie', "L'État a menti pendant des décennies.", 'etabli'),
  fait("Selon l'historienne Raphaëlle Branche, la torture était « massive » : « une violence quotidienne, banale, utilisée indifféremment en ville ou dans les montagnes », visant surtout des civils.", 'branche', '1954-1962', 'Algérie', "L'historiographie confirme l'ampleur.", 'etabli'),
  fait("Selon Raphaëlle Branche, il est « interdit d'affirmer que l'ensemble des officiers de renseignement ont eu recours à la torture », mais « aucun responsable militaire n'est sanctionné pour ces méthodes ».", 'branche', '1954-1962', 'Algérie', "Tous n'ont pas torturé, mais la hiérarchie a couvert.", 'etabli'),
 ],
 court="Faux : l'État français reconnaît lui-même un « système légalement institué » et une torture « conçue comme une arme contre le FLN ». Les historiens la décrivent comme massive et quotidienne, même si tous les soldats n'y ont pas participé.",
 moyen="En 2018, le président de la République a reconnu que Maurice Audin était mort en raison d'un « système légalement institué », rendu possible par les pouvoirs spéciaux votés en 1956, et que la torture était « conçue comme une arme contre le FLN ». En 2021, l'État a reconnu qu'Ali Boumendjel avait été torturé puis assassiné.\n\nL'historienne Raphaëlle Branche décrit une torture « massive », « quotidienne, banale », surtout contre des civils. Cela ne veut pas dire que tous les soldats ont torturé : beaucoup ne l'ont pas fait, et certains s'y sont opposés. Mais aucun responsable n'a été sanctionné. Le reconnaître, c'est respecter la vérité, pas humilier l'armée.",
 detaille="Le 13 septembre 2018, Emmanuel Macron a reconnu que Maurice Audin, arrêté le 11 juin 1957, était mort à cause d'un « système légalement institué qui a favorisé les disparitions ». Ce système reposait sur les pouvoirs spéciaux votés par le Parlement en 1956, et la torture « restait impunie parce qu'elle était conçue comme une arme contre le FLN ». Les archives sur ce sujet ont été ouvertes. En 2021, l'État a aussi reconnu qu'Ali Boumendjel avait été « torturé puis assassiné », le crime ayant été maquillé en suicide.\n\nLes travaux de l'historienne Raphaëlle Branche décrivent une torture « massive », « une violence quotidienne, banale », pratiquée en ville comme dans les montagnes, surtout contre des civils soupçonnés d'aider les maquis. L'électricité était la technique la plus utilisée.\n\nL'historienne apporte aussi une nuance : les tortures étaient « le plus souvent le fait de certains soldats particuliers », d'unités de renseignement et de détachements spécialisés, et l'on ne peut pas dire que tous les officiers de renseignement ont torturé. Mais aucun responsable militaire n'a été sanctionné, et une interdiction explicite n'est venue que tardivement. C'est ce qui fait de la torture un système et non une exception.",
 empathie="Beaucoup de familles ont un grand-père qui a fait l'Algérie, et entendre parler de torture peut être douloureux. Reconnaître ce système ne revient pas à accuser chaque appelé : c'est l'État qui l'a organisé et couvert.",
 legitimes=["Tous les soldats n'ont pas torturé ; la pratique relevait surtout d'unités spécialisées.", "Certains responsables militaires ont exprimé leur désaccord."],
 contre=[
  ("Le FLN aussi a commis des atrocités.", "Les violences d'un camp n'effacent pas celles de l'autre : elles ne changent rien au système reconnu par l'État français."),
  ("C'est de la repentance.", "C'est une reconnaissance des faits par le chef de l'État, fondée sur les archives et le travail des historiens."),
 ],
 questions=["Sais-tu ce que l'État français a reconnu en 2018 au sujet de Maurice Audin ?", "Reconnaître un crime d'État, est-ce trahir son pays ou le respecter ?"],
 limites=["L'article de Raphaëlle Branche date de 2007.", "Le nombre de victimes de la torture n'est pas établi par les sources lues."],
 publics={'convaincus': "Ce n'est pas la gauche qui le dit, c'est le président de la République en 2018 : un « système légalement institué », et une torture « conçue comme une arme contre le FLN ». Tous les soldats n'ont pas torturé, l'historienne Raphaëlle Branche le précise. Mais aucun responsable n'a jamais été sanctionné.",
  'indecis': "La guerre d'Algérie touche beaucoup de familles, et il est normal d'être prudent. L'État reconnaît pourtant officiellement un système de torture et de disparitions, et les historiens le décrivent comme massif. Le reconnaître n'accuse pas chaque soldat, mais ceux qui l'ont organisé et couvert."},
 a_actualiser='2028-06-30', raison="Nouvelles ouvertures d'archives ou reconnaissances officielles.",
))

# 23 ── Esclavage et traite ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='esclavage-traite-responsabilite', affirmation="L'esclavage, la France n'a pas à s'en excuser, ce sont des Africains qui vendaient les esclaves.", volet='international', sous_theme='Colonisation et décolonisation',
 mots_cles=['esclavage', 'traite negriere', 'traite atlantique', 'code noir', 'loi taubira', 'africains vendaient les esclaves', 'commerce triangulaire', 'repentance esclavage'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. Des marchands et États africains capturaient et vendaient des captifs, et une traite arabo-musulmane plus ancienne a existé. Mais la demande, le transport et l'exploitation étaient européens : 4 118 expéditions françaises ont déporté plus de 1,38 million d'Africains, et le Code noir a encadré l'esclavage français pendant plus de 160 ans. À l'abolition de 1848, la France a indemnisé les propriétaires, pas les esclaves. La loi de 2001 reconnaît la traite et l'esclavage comme crime contre l'humanité.",
 contexte="L'argument du rôle des intermédiaires africains est souvent utilisé pour rejeter toute « repentance » sur l'esclavage.",
 explication="La traite atlantique reposait sur une chaîne : capture en Afrique, achat par des négriers européens, transport, vente et exploitation dans les colonies. Reconnaître le rôle de chaque maillon n'efface pas celui des puissances qui organisaient et profitaient du système.",
 sources=[BNF_TRAITE, SEN_TRAITE, AN_TAUBIRA, COTTIAS, ASOM_TRAITE],
 faits=[
  fait("D'après la base Slave Voyages citée par la BnF, 4 118 expéditions sous pavillon français ont déporté 1 381 404 Africains entre 1551 et 1875, soit 11 % de la traite transatlantique.", 'bnf_traite', '1551-1875', 'France', "La France a été un acteur majeur de la traite.", 'etabli', '1 381 404 personnes'),
  fait("Environ 13 % des captifs sont morts pendant la traversée, et Nantes a organisé 44 % des expéditions françaises.", 'bnf_traite', '1551-1875', 'France', "La traite a enrichi des ports français.", 'etabli'),
  fait("Le Code noir de 1685 a servi de cadre juridique à l'esclavage pendant plus de 160 ans ; aboli en 1794, l'esclavage est rétabli en 1802 et aboli définitivement en 1848.", 'sen_traite', '1685-1848', 'France', "L'esclavage était organisé par la loi française.", 'etabli'),
  fait("Selon l'historienne Myriam Cottias, la France a versé après 1848 126 millions de francs-or aux propriétaires d'esclaves, et non aux esclaves ; Haïti a dû payer 90 millions de francs-or pour faire reconnaître son indépendance.", 'cottias', '1825-1887', 'France et Haïti', "Les victimes n'ont jamais été indemnisées.", 'etabli'),
  fait("Selon le compte rendu de l'Académie des sciences d'outre-mer, les Portugais commerçaient avec des « négriers africains et arabo-musulmans », réseaux devenus très efficaces quand la demande sucrière a explosé.", 'asom_traite', 'XVe-XIXe siècles', 'Afrique et Atlantique', "Des intermédiaires africains ont participé, sous l'effet de la demande européenne.", 'etabli'),
  fait("Le gouvernement rappelle que la France a été le premier pays à reconnaître la traite et l'esclavage comme « crime contre l'humanité », par la loi dite Taubira.", 'an_taubira', '2001', 'France', "La reconnaissance est déjà inscrite dans la loi.", 'etabli'),
 ],
 court="Trompeur : des marchands africains vendaient des captifs, mais ce sont des navires européens, dont plus de 4 000 expéditions françaises, qui les ont déportés et des colons qui les ont exploités, sous le Code noir. La loi de 2001 reconnaît un crime contre l'humanité.",
 moyen="Il est vrai que des marchands et des États africains capturaient et vendaient des captifs, et qu'une traite arabo-musulmane plus ancienne a existé. Mais la traite atlantique répondait à une demande européenne : 4 118 expéditions françaises ont déporté plus de 1,38 million d'Africains, et Nantes en a organisé 44 %.\n\nL'esclavage dans les colonies françaises était organisé par la loi, le Code noir, pendant plus de 160 ans. À l'abolition, la France a indemnisé les propriétaires, pas les esclaves, et a fait payer à Haïti son indépendance. Reconnaître ce crime, comme le fait la loi de 2001, ce n'est pas haïr la France : c'est dire la vérité sur son histoire.",
 detaille="Selon la base Slave Voyages citée par la BnF, 4 118 expéditions sous pavillon français ont déporté 1 381 404 Africains entre 1551 et 1875, soit 11 % de la traite transatlantique. Environ 13 % des captifs sont morts pendant la traversée. Le Code noir de 1685 a encadré l'esclavage pendant plus de 160 ans ; aboli en 1794 par la Convention, il a été rétabli par Bonaparte en 1802, puis aboli définitivement en 1848.\n\nLe rôle d'intermédiaires africains est établi par les historiens : les forts européens négociaient avec des négriers locaux, et des réseaux anciens existaient vers le Maghreb et le Proche-Orient. Le rapport du Sénat de 2000 rappelle aussi la traite arabo-musulmane. Mais ces réseaux sont devenus massifs quand la demande des plantations sucrières a explosé.\n\nAprès 1848, la France a versé 126 millions de francs-or aux propriétaires d'esclaves, dont une part de petits propriétaires « de couleur » en Martinique, et rien aux esclaves. Haïti a dû payer 90 millions de francs-or pour faire reconnaître son indépendance. La loi de 2001 reconnaît la traite et l'esclavage comme crime contre l'humanité.",
 empathie="On peut se sentir accusé personnellement quand on parle d'esclavage, alors que personne aujourd'hui n'en est coupable. Reconnaître ce crime, ce n'est pas culpabiliser les vivants, c'est comprendre une histoire dont les effets durent.",
 legitimes=["Des marchands et États africains capturaient et vendaient des captifs.", "Une traite arabo-musulmane plus ancienne a existé."],
 contre=[
  ("Les autres aussi pratiquaient l'esclavage.", "C'est vrai, et la France refuse de hiérarchiser les crimes ; cela n'efface pas la part française."),
  ("La France a aboli l'esclavage.", "Oui, en 1794 puis en 1848, après l'avoir rétabli en 1802, et en indemnisant les propriétaires, pas les esclaves."),
 ],
 questions=["Sais-tu combien d'Africains ont été déportés par des navires français ?", "Qui a été indemnisé lors de l'abolition de 1848 ?"],
 limites=["Le texte de la loi de 2001 n'a pas été lu sur Légifrance : son contenu est cité à travers une réponse ministérielle.", "Les estimations globales de la traite varient selon les sources."],
 publics={'convaincus': "Des marchands africains vendaient des captifs, c'est vrai. Mais 4 118 expéditions françaises en ont déporté plus de 1,38 million, et le Code noir organisait l'esclavage dans nos colonies. En 1848, la France a indemnisé les propriétaires, pas les esclaves. Qui achète porte aussi la responsabilité.",
  'indecis': "Personne aujourd'hui n'est coupable de l'esclavage, et des intermédiaires africains y ont participé. Mais la France a été un acteur majeur de la traite atlantique, et ses lois ont organisé l'esclavage pendant plus de 160 ans. La loi de 2001 en fait un crime contre l'humanité : c'est un fait historique, pas une accusation contre les Français d'aujourd'hui."},
 a_actualiser='2028-06-30', raison="Sujet historique, à revoir selon les travaux nouveaux.",
))

# 24 ── Sanctions contre la Russie ───────────────────────────────────────────
FICHES.append(fiche(
 id='sanctions-russie-effets', affirmation="Les sanctions contre la Russie nous font plus de mal qu'à elle.", volet='international', sous_theme='Russie',
 mots_cles=['sanctions contre la russie', 'sanctions russie', 'sanctions economiques', 'les sanctions ne marchent pas', 'economie russe', 'gaz russe', 'embargo russie'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur. L'Europe a bien payé un choc énergétique en 2022 : inflation énergétique de 41,9 % en octobre 2022 dans la zone euro, facture énergétique française alourdie de 68 milliards d'euros. Mais la hausse du gaz avait commencé dès 2021 et l'arrêt de réacteurs nucléaires a coûté environ 16 milliards à la France. L'économie russe, après avoir résisté grâce aux dépenses de guerre, ralentit fortement : croissance de 1 % en 2025, recettes pétrolières et gazières en baisse de 23,8 %, taux directeur monté jusqu'à 21 %.",
 contexte="Le RN et une partie de l'extrême droite ont souvent jugé les sanctions inefficaces ou contraires aux intérêts français.",
 explication="Les sanctions limitent les exportations russes d'énergie, l'accès aux technologies et aux financements. Leur effet se mesure dans la durée et se mêle à d'autres facteurs, comme les cours du pétrole.",
 sources=[TRESOR_RU, CE_SANCTIONS, CE_GAZ, EUROSTAT_INF, BDF_ENERGIE],
 faits=[
  fait("Selon le Trésor, la croissance russe est passée de 4,9 % en 2024 à 1 % en 2025, un « atterrissage » après deux ans de « keynésianisme de guerre ».", 'tresor_ru', '2024-2025', 'Russie', "L'économie russe ralentit fortement.", 'etabli'),
  fait("Selon le Trésor, les recettes pétrolières et gazières russes ont baissé de 23,8 % en 2025, avec la baisse des cours ; le taux directeur est monté jusqu'à 21 % et la TVA a été relevée à 22 %.", 'tresor_ru', '2022-2025', 'Russie', "L'État russe est sous pression.", 'etabli'),
  fait("En octobre 2022, l'inflation de la zone euro atteint 10,7 % sur un an, dont 41,9 % pour l'énergie (estimation rapide).", 'eurostat_inf', '2022', 'Zone euro', "Les Européens ont payé un choc énergétique.", 'etabli'),
  fait("Selon la Banque de France, la balance énergétique française s'est dégradée de 68 milliards d'euros en 2022 ; la hausse du gaz avait commencé dès l'été 2021, et la baisse de la production nucléaire a coûté à elle seule environ 16 milliards.", 'bdf_energie', '2021-2022', 'France', "Le choc ne vient pas seulement des sanctions.", 'etabli'),
  fait("Selon la Commission européenne, la part du gaz russe dans les importations de l'UE est passée de 45 % à 19 %, malgré un rebond en 2024.", 'ce_gaz', '2021-2024', 'Union européenne', "L'Europe a réduit sa dépendance.", 'etabli'),
  fait("Selon la Commission européenne, l'État russe aurait environ 400 milliards d'euros de moins à dépenser, et 95 % de sa flotte aérienne ne peut plus être correctement entretenue.", 'ce_sanctions', '2024', 'Russie', "Les sanctions pèsent sur l'économie russe.", 'estimation'),
 ],
 court="Trompeur : l'Europe a payé un choc énergétique en 2022, mais en partie dû à d'autres causes. L'économie russe, elle, ralentit fortement : 1 % de croissance en 2025 et des recettes pétrolières et gazières en baisse de près d'un quart.",
 moyen="Il faut reconnaître que l'Europe a payé cher en 2022 : l'énergie a augmenté de 41,9 % en un an dans la zone euro, et la facture énergétique française s'est alourdie de 68 milliards. Mais selon la Banque de France, la hausse du gaz avait commencé dès 2021, et nos réacteurs nucléaires à l'arrêt ont coûté à eux seuls 16 milliards.\n\nDe son côté, la Russie a d'abord tenu grâce à une économie de guerre, puis elle s'essouffle : croissance de 1 % en 2025, recettes pétrolières et gazières en baisse de 23,8 %, taux d'intérêt montés jusqu'à 21 %. Dire que les sanctions nous font plus de mal qu'à elle ne tient pas.",
 detaille="Le coût pour l'Europe est réel. En octobre 2022, l'inflation de la zone euro a atteint 10,7 %, dont 41,9 % pour l'énergie, selon Eurostat. La Banque de France estime que la balance énergétique française s'est dégradée de 68 milliards d'euros en 2022. Mais elle rappelle que la hausse du gaz avait commencé dès l'été 2021, et que l'arrêt de réacteurs nucléaires a coûté environ 16 milliards à lui seul. Depuis, l'Union a ramené la part du gaz russe dans ses importations de 45 % à 19 %.\n\nLa Russie a d'abord résisté, avec une croissance de 4,9 % en 2024 portée par les dépenses militaires. Selon le Trésor, elle tombe à 1 % en 2025 ; les recettes pétrolières et gazières reculent de 23,8 %, le déficit atteint 2,6 % du PIB et la TVA est relevée à 22 %. Le taux directeur est monté jusqu'à 21 %, et l'inflation a culminé vers 18 % en 2022.\n\nLe Trésor ne chiffre pas l'effet propre des sanctions, qui se mêle à la baisse des cours du pétrole, et les chiffres de la Commission européenne viennent de l'institution qui sanctionne. Mais aucune source lue ne montre que l'Europe souffrirait davantage que la Russie.",
 empathie="La flambée des factures de 2022 a été dure pour beaucoup de ménages, et il est normal de se demander si cela valait le coup. Les données montrent pourtant que la Russie paie aussi un prix élevé, de plus en plus visible.",
 legitimes=["L'Europe a subi un choc énergétique sévère en 2022.", "La Russie a d'abord bien résisté, grâce à son économie de guerre."],
 contre=[
  ("La Russie vend son pétrole ailleurs.", "Elle a trouvé d'autres acheteurs, mais ses recettes pétrolières et gazières ont reculé de 23,8 % en 2025."),
  ("Nos factures ont explosé à cause des sanctions.", "En partie, mais la hausse du gaz avait commencé en 2021 et l'arrêt de réacteurs nucléaires a coûté 16 milliards en 2022."),
 ],
 questions=["Sais-tu que la hausse du gaz avait commencé avant la guerre ?", "Que se passerait-il si l'Europe restait dépendante du gaz russe ?"],
 limites=["Aucune source lue ne chiffre l'effet propre des sanctions sur l'économie russe.", "Le chiffre d'inflation d'octobre 2022 est une estimation rapide, ensuite révisée à la marge."],
 publics={'convaincus': "En 2022, on a payé cher l'énergie, personne ne le nie. Mais selon la Banque de France, la hausse du gaz avait commencé dès 2021, et nos réacteurs à l'arrêt ont coûté 16 milliards à eux seuls. La Russie, elle, est passée de 4,9 % à 1 % de croissance, avec des taux d'intérêt montés jusqu'à 21 %.",
  'indecis': "Les sanctions ont un coût pour nous, surtout en 2022, et il est normal de se poser la question. Mais l'économie russe ralentit nettement depuis 2025, et l'Europe a réduit sa dépendance au gaz russe de 45 % à 19 %. Le coût pour la Russie est réel et grandissant."},
 a_actualiser='2027-03-31', raison="Nouvelles données sur l'économie russe.",
))

# 25 ── Pollution de l'air ───────────────────────────────────────────────────
FICHES.append(fiche(
 id='pollution-air-deces', affirmation="La pollution de l'air, ça ne tue pas tant que ça.", volet='ecologie', sous_theme='Transports',
 mots_cles=['pollution de l air', 'particules fines', 'qualite de l air', 'pm2 5', 'morts de la pollution', 'deces lies a la pollution', '40 000 morts'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux. Selon Santé publique France, près de 40 000 décès par an sont attribuables aux particules fines en France (2016-2019), soit 7 % de la mortalité, et environ 8 mois d'espérance de vie perdus en moyenne. Dans le monde, l'OMS estime à 4,2 millions les décès prématurés liés à la pollution de l'air ambiant. La bonne nouvelle : la situation s'améliore, avec des décès liés aux particules fines en baisse de 47 % en France entre 2005 et 2022.",
 contexte="Les mesures contre la pollution, comme les zones à faibles émissions, sont souvent attaquées au nom d'un danger jugé exagéré.",
 explication="Les décès « attribuables » à la pollution sont estimés par modélisation : on calcule combien de décès seraient évités si l'exposition baissait à un certain seuil. Ce ne sont pas des décès constatés un par un, mais des estimations solides et convergentes.",
 sources=[SPF_AIR, AEE_FR, OMS_AIR, SDES_AIR],
 faits=[
  fait("Selon Santé publique France, près de 40 000 décès par an sont attribuables aux particules fines chez les 30 ans et plus (2016-2019), soit 7 % de la mortalité totale.", 'spf_air', '2016-2019', 'France', "La pollution de l'air est une cause majeure de mortalité.", 'etabli', '40 000 décès'),
  fait("Selon Santé publique France, cette pollution représente une perte moyenne d'espérance de vie d'environ 8 mois.", 'spf_air', '2016-2019', 'France', "L'impact touche toute la population.", 'etabli'),
  fait("Selon l'OMS, 4,2 millions de décès prématurés par an dans le monde sont liés à la pollution de l'air ambiant, et 99 % de la population mondiale vivait en 2019 au-delà de ses seuils.", 'oms_air', '2019', 'Monde', "C'est un problème sanitaire mondial.", 'etabli'),
  fait("Les décès prématurés liés aux particules fines ont baissé de 47 % en France entre 2005 et 2022, selon l'Agence européenne pour l'environnement.", 'aee_fr', '2005-2022', 'France', "Les politiques de réduction de la pollution fonctionnent.", 'etabli', '-47 %'),
  fait("En 2024, les valeurs limites de pollution ont encore été dépassées pour le dioxyde d'azote dans 2 agglomérations et pour les PM10 dans 3 ; la valeur cible d'ozone l'a été dans 17 agglomérations.", 'sdes_air', '2024', 'France', "Le problème n'est pas réglé.", 'etabli'),
 ],
 court="Faux : selon Santé publique France, près de 40 000 décès par an sont attribuables aux particules fines, soit 7 % des décès. La pollution baisse, et les décès liés aux particules ont reculé de 47 % depuis 2005 : les efforts paient.",
 moyen="Santé publique France estime que près de 40 000 décès par an sont attribuables aux particules fines, soit 7 % de la mortalité, et que cette pollution coûte en moyenne 8 mois d'espérance de vie. Ce sont des estimations par modélisation, mais elles convergent avec celles de l'OMS, qui compte 4,2 millions de décès prématurés dans le monde.\n\nLa pollution baisse : les décès liés aux particules ont reculé de 47 % en France entre 2005 et 2022. C'est la preuve que les normes et les politiques publiques marchent. Il faut continuer, en protégeant d'abord ceux qui vivent près des grands axes, sans faire payer les plus modestes.",
 detaille="Selon Santé publique France, près de 40 000 décès par an sont attribuables aux particules fines PM2,5 chez les 30 ans et plus sur la période 2016-2019, soit 7 % de la mortalité totale, contre 9 % en 2007-2008. Cette pollution représente une perte moyenne d'espérance de vie d'environ 8 mois. Dans le monde, l'OMS compte 4,2 millions de décès prématurés par an, surtout par maladies cardiaques et AVC.\n\nLa tendance est à l'amélioration. Selon l'Agence européenne pour l'environnement, les décès liés aux PM2,5 ont baissé de 47 % en France entre 2005 et 2022, les émissions d'environ 50 % et les concentrations d'environ 42 %. Le ministère de la Transition écologique confirme la baisse des concentrations de la plupart des polluants depuis 2000.\n\nLe problème n'est pas réglé : en 2024, des valeurs limites ont encore été dépassées dans plusieurs agglomérations, et la valeur cible d'ozone dans 17. Ces chiffres sont des estimations par modélisation, et les méthodes européennes et françaises diffèrent, mais toutes concluent à un impact sanitaire majeur.",
 empathie="On peut se méfier des chiffres qui servent à justifier des contraintes, comme les zones à faibles émissions. Mais les estimations de Santé publique France et de l'OMS concordent : l'air pollué abîme réellement la santé, et sa baisse sauve des vies.",
 legitimes=["Les décès attribuables sont des estimations par modélisation, pas des décès constatés.", "La pollution de l'air baisse nettement depuis vingt ans."],
 contre=[
  ("On ne meurt pas de la pollution, on meurt d'un infarctus.", "Justement : la pollution augmente le risque de maladies cardiaques et d'AVC, qui représentent 68 % des décès estimés par l'OMS."),
  ("Ça s'améliore, donc inutile d'agir.", "Ça s'améliore parce qu'on a agi ; des seuils sont encore dépassés dans plusieurs villes."),
 ],
 questions=["Sais-tu combien de décès par an Santé publique France attribue aux particules fines ?", "Qui respire l'air le plus pollué : les habitants des centres aisés ou ceux qui vivent le long des grands axes ?"],
 limites=["Les données de Santé publique France portent sur 2016-2019.", "Les méthodes de l'Agence européenne et de Santé publique France ne sont pas directement comparables."],
 publics={'convaincus': "Santé publique France estime à près de 40 000 par an les décès attribuables aux particules fines, 7 % de la mortalité. Ce n'est pas un chiffre militant : l'OMS arrive aux mêmes conclusions au niveau mondial. Et quand la pollution baisse, comme depuis 2005, ces décès reculent.",
  'indecis': "Les chiffres sont des estimations, mais ils convergent : près de 40 000 décès par an en France selon Santé publique France. La bonne nouvelle, c'est que la pollution baisse et que les décès liés aux particules ont reculé de 47 % depuis 2005. Le défi est de continuer sans pénaliser les ménages modestes."},
 a_actualiser='2027-06-30', raison="Nouvelle évaluation de Santé publique France.",
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
