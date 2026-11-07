"""Fiches quotidiennes du 7 novembre 2026 (phase alpha) : 25 questions qui circulent et qui n'avaient pas de fiche
qui leur réponde vraiment (aucune fiche, ou une fiche voisine hors sujet).

Toutes les sources ont été ouvertes et lues le 7 novembre 2026 (consultee=True) ; les chiffres viennent uniquement
des passages cités. Les données anciennes sont signalées dans les limites. Chaque fiche contient les réponses
selon le public (« publics » : électeur d'extrême droite convaincu / personne indécise).
Usage : python3 scripts/fiches/quotidien_20261107_0028.py  (puis node scripts/corrections-v10.js et node scripts/enrichir-fiches.js)
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche as _fiche, OUT

TODAY = '2026-11-07'

def fiche(**k):
    d = _fiche(**k)
    d['derniere_verification'] = TODAY
    return d

# ── Sources ────────────────────────────────────────────────────────────────
# Immigration et droits
LCP_AME = ('lcp_ame', src("Aide médicale d'État : un dispositif « utile » et « globalement maîtrisé », qui « mérite d'être adapté », juge la mission Stefanini / Évin", "LCP (Raphaël Marchal), d'après le rapport de Claude Évin et Patrick Stefanini", "4 décembre 2023",
  "https://lcp.fr/actualites/aide-medicale-d-etat-un-dispositif-utile-et-globalement-maitrise-qui-merite-d-etre",
  "Selon la mission Évin-Stefanini, le dispositif est contrôlé par l'Assurance maladie, sans « atypismes, abus ou fraudes structurelles » dans la consommation de soins, et l'AME n'est pas un facteur d'attractivité ; 400 327 bénéficiaires en moyenne en 2022, environ 466 000 attendus en 2023 (+39 % entre fin 2015 et mi-2023), hausse attribuée à l'augmentation du nombre de personnes sans papiers ; consommation trimestrielle moyenne par personne : 642 € en 2009, 604 € en 2022 ; environ 50 % des bénéficiaires potentiels ne feraient pas la demande ; la mission propose de soumettre certains soins à accord préalable.",
  "Média parlementaire rendant compte d'un rapport commandé par le Gouvernement.", 'media'))
SENAT_AME = ('senat_ame', src("Projet de loi de finances pour 2026 : Santé (rapport général n° 139, tome III, annexe 27)", "Sénat, commission des finances (Vincent Delahaye, rapporteur spécial)", "24 novembre 2025",
  "https://www.senat.fr/rap/l25-139-327/l25-139-3273.html",
  "Dépenses réelles de l'AME de droit commun : 1,255 milliard d'euros en 2024 ; 465 208 bénéficiaires fin 2024 (+1,9 %), 461 833 au 31 mars 2025 ; dépense moyenne par bénéficiaire : 2 699 € en 2024, contre 3 659 € pour la population générale en 2023 ; plafond de ressources : 10 339 euros par an pour une personne seule en métropole en 2025 ; le rapporteur dénonce « l'absence totale de maitrise du dispositif ».",
  "Rapport parlementaire de contrôle budgétaire (rapporteur de droite, critique du dispositif)."))
SENAT_AME_SYN = ('senat_ame_syn', src("L'aide médicale de l'État, une réforme nécessaire (synthèse du rapport d'information)", "Sénat, commission des finances (Vincent Delahaye)", "9 juillet 2025",
  "https://www.senat.fr/rap/r24-841/r24-841-syn.pdf",
  "Pour bénéficier de l'AME, il faut être étranger « vivant en France depuis au moins trois mois consécutifs en situation irrégulière », avec des ressources d'au plus 862 € par mois en 2025 ; 465 744 bénéficiaires au 30 septembre 2024, environ deux fois plus qu'en 2011 ; coût total réel 2024 : 1 386,8 M€ ; 60,8 % des dépenses à l'hôpital.",
  "Rapport parlementaire de contrôle."))
DREES_ASPA = ('drees_aspa', src("Les allocations du minimum vieillesse (Minima sociaux et prestations de solidarité, édition 2025, fiche 28)", "DREES", "Décembre 2025",
  "https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-12/MS2025%20-%20Fiche%2028%20-%20Les%20allocations%20du%20minimum%20vieillesse.pdf",
  "« Fin 2023, 723 000 allocataires perçoivent le minimum vieillesse », dont 606 600 au titre de l'ASPA ; conditions : 65 ans (ou l'âge légal en cas d'inaptitude), résider en France « au moins neuf mois au cours de l'année civile » ; pour les étrangers hors Espace économique européen et Suisse, titre de séjour autorisant à travailler depuis au moins dix ans ; récupération sur succession si l'actif net dépasse 107 616 euros en métropole ; plafond de ressources : 1 034,28 euros par mois pour une personne seule au 1er janvier 2025.",
  "Service statistique du ministère des Solidarités."))
AN_ASPA = ('an_aspa', src("Question écrite n° 891 (allocation de solidarité aux personnes âgées et étrangers) et réponse du ministère", "Assemblée nationale / ministère des Solidarités", "17 février 2026",
  "https://questions.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE891",
  "Le ministère rappelle que les étrangers hors Union européenne doivent détenir un titre de séjour autorisant à travailler depuis au moins 10 ans (sauf réfugiés, apatrides, bénéficiaires de la protection subsidiaire) ; il n'existe pas de statistique de nationalité sur l'ensemble des allocataires ; en 2018, l'enquête BMS comptait 154 900 personnes nées à l'étranger parmi 396 100 bénéficiaires du minimum vieillesse (lieu de naissance, pas nationalité).",
  "Réponse officielle du ministère compétent."))
CC_MNA = ('cc_mna', src("Commentaire de la décision n° 2018-768 QPC du 21 mars 2019 (examens radiologiques osseux aux fins de détermination de l'âge)", "Conseil constitutionnel", "21 mars 2019",
  "https://oos.cloudgouv-eu-west-1.outscale.com/ccqpc-drupal-prd/dqpc/commentaire/commentaire_D%C3%A9cision-n%C2%B0-2018-768-QPC-du-21-mars-2019.pdf",
  "« Il était établi que les résultats des examens osseux peuvent comporter une marge d'erreur significative » ; autour de 18 ans, une marge d'erreur de 18 à 24 mois ; le législateur « a exclu que ces conclusions puissent constituer l'unique fondement dans la détermination de l'âge » et le doute « doit profiter à la qualité de mineur de l'intéressé » ; le Haut Conseil de la santé publique : « Aucune méthode à elle seule ne peut scientifiquement donner un âge précis ».",
  "Juridiction constitutionnelle (commentaire officiel)."))
LOCALTIS_MNA = ('localtis_mna', src("Le Sénat débat de la question des MNA et cherche à voir clair dans les chiffres", "Banque des Territoires (Localtis, Jean-Noël Escudié)", "22 février 2021",
  "https://www.banquedesterritoires.fr/le-senat-debat-de-la-question-des-mna-et-cherche-voir-clair-dans-les-chiffres",
  "Selon le secrétaire d'État Adrien Taquet, « en 2017, 44.000 jeunes se sont déclarés MNA pour être évalués, et 14.000 ont été reconnus comme tels » ; « le taux d'acceptation est donc compris entre 30% et 40% » ; le chiffre de « près de 70% de prétendus mineurs » qui ne le seraient pas est cité comme une allégation.",
  "Compte rendu d'un débat au Sénat par un média public spécialisé.", 'media'))
DDD_MNA = ('ddd_mna', src("Les mineurs non accompagnés au regard du droit (synthèse)", "Défenseur des droits", "Janvier 2022",
  "https://www.defenseurdesdroits.fr/sites/default/files/2023-07/ddd_rapport-les-mineurs-non-accompagnes-au-regard-du-droit_synthese_20210124.pdf",
  "L'évaluation de la minorité est « parfois entachée de ces représentations négatives » et la situation varie « grandement d'un département à l'autre » ; le Défenseur recommande une présomption de minorité jusqu'à décision judiciaire définitive et l'interdiction des tests osseux ; il déplore l'absence de chiffres consolidés et fiables.",
  "Autorité administrative indépendante chargée de la défense des droits."))
ACADMED_MNA = ('acadmed_mna', src("Sur la fiabilité des examens médicaux visant à déterminer l'âge à des fins judiciaires (rapport 07-01)", "Académie nationale de médecine (J.-L. Chaussain, Y. Chapuis)", "16 janvier 2007",
  "https://www.academie-medecine.fr/07-01-sur-la-fiabilite-des-examens-medicaux-visant-a-determiner-lage-a-des-fins-judiciaires-et-la-possiblite-damelioration-en-la-matiere-pour-les-mineurs-etrangers-isoles/",
  "La méthode de Greulich et Pyle « ne permet pas de distinction nette entre seize et dix-huit ans » ; les difficultés concernent les deux sexes au-delà de quinze ans, en particulier chez le garçon.",
  "Institution scientifique de référence (avis ancien)."))
CC_1993 = ('cc_1993', src("Décision n° 93-325 DC du 13 août 1993 (loi relative à la maîtrise de l'immigration), texte reproduit", "Conseil constitutionnel (texte reproduit par la Revue générale du droit)", "13 août 1993",
  "https://www.revuegeneraledudroit.eu/blog/decisions/conseil-constitutionnel-13-aout-1993-loi-relative-a-la-maitrise-de-limmigration-et-aux-conditions-dentree-daccueil-et-de-sejour-des-etrangers-en-france-decision-numero-93-325-dc",
  "Si le législateur peut prendre à l'égard des étrangers des dispositions spécifiques, « il lui appartient de respecter les libertés et droits fondamentaux de valeur constitutionnelle reconnus à tous ceux qui résident sur le territoire de la République » ; « les étrangers jouissent des droits à la protection sociale, dès lors qu'ils résident de manière stable et régulière sur le territoire français ».",
  "Décision de la juridiction constitutionnelle."))
CDJ_RIP = ('cdj_rip', src("Pourquoi le référendum sur l'accès des étrangers aux prestations sociales n'aura pas lieu", "Le Club des juristes (Lola Isidro, maîtresse de conférences, université Paris Nanterre)", "12 avril 2024",
  "https://www.leclubdesjuristes.com/justice/pourquoi-le-referendum-sur-lacces-des-etrangers-aux-prestations-sociales-naura-pas-lieu-5667/",
  "Le 11 avril 2024, le Conseil constitutionnel a rejeté la proposition de loi référendaire qui conditionnait certaines prestations à 5 ans de séjour régulier ou 30 mois d'affiliation : ces durées sont jugées disproportionnées au regard des alinéas 10 et 11 du Préambule de 1946 ; une condition de durée de résidence reste possible si elle n'est pas excessive.",
  "Analyse juridique universitaire.", 'etude'))
PS_REF_LP = ('ps_ref_lp', src("Immigration : le référendum voulu par Marine Le Pen est-il constitutionnel ?", "Public Sénat (Romain David)", "29 septembre 2021",
  "https://www.publicsenat.fr/article/politique/immigration-le-referendum-voulu-par-marine-le-pen-est-il-constitutionnel-190598",
  "Le projet comprend une « priorité nationale » pour le logement et l'emploi ; selon le constitutionnaliste Dominique Rousseau, on ne peut pas faire entrer la priorité nationale dans le référendum de l'article 11 : il faudrait d'abord réviser la Constitution par l'article 89, qui exige un vote dans les mêmes termes par les deux assemblées ; Didier Maus signale un conflit possible avec les traités européens.",
  "Média parlementaire, avec avis de constitutionnalistes.", 'media'))
NFP_PROG = ('nfp_prog', src("Contrat de législature du Nouveau Front populaire (programme)", "Nouveau Front populaire (document hébergé par La France insoumise)", "Juin 2024",
  "https://lafranceinsoumise.fr/wp-content/uploads/2024/06/PROGRAMME-FRONT-POPULAIRE.pdf",
  "Rubrique « Garantir un accueil digne » : « Faciliter l'accès aux visas, régulariser les travailleurs, étudiants, parents d'enfants scolarisés » ; « instituer la carte de séjour de dix ans comme titre de séjour de référence » ; « Abroger les lois asile et immigration de Macron ». Le document ne prévoit pas de régularisation générale sans condition.",
  "Programme électoral, cité uniquement pour décrire ce que propose la coalition.", 'partisane'))
AN_CL737 = ('an_cl737', src("Amendement CL737 au projet de loi pour contrôler l'immigration, améliorer l'intégration (n° 1855)", "Assemblée nationale (amendement de députés LFI : Danièle Obono, Ugo Bernalicis, Adrien Quatennens et autres)", "23 novembre 2023",
  "https://www.assemblee-nationale.fr/dyn/16/amendements/1855/CION_LOIS/CL737.pdf",
  "Les auteurs indiquent que leur programme prévoit de « régulariser tous les travailleurs et travailleuses sans-papiers » et demandent pour eux un titre de séjour de plein droit en établissant par tout moyen leur exercice professionnel.",
  "Document parlementaire officiel décrivant une proposition du groupe LFI."))
PS_REGUL = ('ps_regul', src("Immigration : titres de séjour en nette hausse et régularisations en baisse sur l'année 2025", "Public Sénat (Romain David, avec l'AFP), d'après la DGEF", "27 janvier 2026",
  "https://www.publicsenat.fr/actualites/societe/immigration-titres-de-sejour-en-nette-hausse-et-regularisations-en-baisse-sur-lannee-2025",
  "Selon la direction générale des étrangers en France, 28 610 étrangers ont été régularisés en 2025 (-10,1 %), avec une baisse de 11,5 % pour motif économique et de 6,4 % pour motif familial ; « il y a l'impact de la circulaire Retailleau ».",
  "Média parlementaire rendant compte des chiffres officiels du ministère de l'Intérieur.", 'media'))

# Économie, Europe, fiscalité
SENAT_UE = ('senat_ue', src("L'essentiel — PLF 2025, mission « Affaires européennes »", "Sénat, commission des finances (Jean-Marie Mizzon, rapporteur spécial)", "31 octobre 2024",
  "https://senat.fr/fileadmin/Commissions/Finances/2024-2025/PLF_2025/Essentiel/Mission_Aff_europeennes_Essentiel_PLF_2025.pdf",
  "Prélèvement sur recettes au profit de l'UE pour 2025 : 23,321 milliards d'euros ; en 2023, la France était « le deuxième contributeur net » avec « un solde net estimé à – 9,333 milliards d'euros » (Allemagne -19,8 Md€) ; la France est « le premier bénéficiaire en volume de l'Union européenne », mais seulement 22e par habitant (242 euros) ; subventions du plan de relance : 40,3 Md€ au total.",
  "Rapport parlementaire budgétaire."))
TLE_UE = ('tle_ue', src("Budget européen : que paie la France et que reçoit-elle en retour ?", "Toute l'Europe (Vincent Lequeux)", "20 octobre 2026",
  "https://www.touteleurope.eu/fonctionnement-de-l-ue/budget-europeen-que-paie-la-france-et-que-recoit-elle-en-retour/",
  "Contribution française « autour de 24 milliards par an en moyenne de 2021 à 2025 » ; dépenses de l'UE en France : environ 16 Md€ ces dernières années, soit un solde net d'environ 8 Md€ par an hors plan de relance ; en comptant les subventions du plan de relance, le solde tombe à environ 3 Md€ par an, soit 0,1 % du PIB ; une partie des fonds versés aux autres pays revient à des entreprises françaises.",
  "Site d'information de référence sur les questions européennes.", 'media'))
CEPII_UE = ('cepii_ue', src("L'Union européenne : combien a-t-on gagné à la faire (et combien perdrait-on à la défaire) ? (La Lettre du CEPII n° 389)", "CEPII (Thierry Mayer, Vincent Vicard, Soledad Zignago)", "Juin 2018",
  "https://www.cepii.fr/PDF_PUB/lettre/2018/let389.pdf",
  "Gain de PIB réel lié à l'intégration commerciale européenne : France 3,4 % ; « un retour en arrière entraînerait une perte symétrique en termes de commerce ou de PIB ».",
  "Centre public d'études économiques internationales.", 'etude'))
TLE_IS = ('tle_is', src("[Carte] L'impôt sur les sociétés dans les États membres de l'Union européenne", "Toute l'Europe (Juliette Verdes)", "11 mai 2023",
  "https://www.touteleurope.eu/economie-et-social/carte-impot-sur-les-societes-dans-les-etats-membres-de-l-union-europeenne/",
  "Taux légal de l'impôt sur les sociétés en France : 25,8 % avec la contribution sociale, légèrement au-dessus de la moyenne européenne ; plus élevé à Malte (35 %), au Portugal (31,5 %) et en Allemagne (29,8 % avec la fiscalité locale) ; plus bas en Hongrie (9 %), Bulgarie (10 %), Irlande (12,5 %) ; la France est le 2e pays au monde où le taux légal a le plus baissé entre 2021 et 2022.",
  "Site d'information de référence sur les questions européennes.", 'media'))
MONTAIGNE_PROD = ('montaigne_prod', src("Baromètre européen des impôts de production 2023", "Institut Montaigne (Lisa Darbois)", "Février 2023",
  "https://www.institutmontaigne.org/publications/barometre-europeen-des-impots-de-production-2023",
  "En 2021, les impôts de production représentent en France 3,8 % du PIB (95 Md€), contre 4,4 % en 2020 ; moyenne des 11 pays étudiés : 2,5 % du PIB ; la baisse s'explique surtout par la baisse de la CVAE.",
  "Think tank libéral (proche des entreprises) : cité pour un fait défavorable.", 'etude'))
PS_AIDES = ('ps_aides', src("Un coût annuel de 211 milliards d'euros : la commission d'enquête du Sénat sur les aides publiques aux entreprises réclame un « choc de transparence »", "Public Sénat (Guillaume Jacquot)", "8 juillet 2025",
  "https://www.publicsenat.fr/actualites/economie/un-cout-annuel-de-211-milliards-deuros-la-commission-denquete-du-senat-sur-les-aides-publiques-aux-entreprises-reclame-un-choc-de-transparence",
  "En 2023, les aides publiques de l'État aux entreprises atteignent « au moins 211 milliards d'euros », dont environ 80 Md€ d'allègements de cotisations et environ 43 Md€ de dépenses fiscales ; rapport adopté à l'unanimité le 1er juillet 2025 (président LR, rapporteur PCF).",
  "Média parlementaire rendant compte d'une commission d'enquête transpartisane.", 'media'))
TLE_IS21 = ('tle_is21', src("Taxation des entreprises : comprendre la concurrence fiscale en Europe", "Toute l'Europe (Arthur Olivier)", "20 juillet 2021",
  "https://www.touteleurope.eu/economie-et-social/taxation-des-entreprises-comprendre-la-concurrence-fiscale-en-europe/",
  "Le taux légal de l'impôt sur les sociétés en France était au maximum de 33 % avant la réforme, avec un objectif de 25 % ; en 2019, la France avait « le taux effectif moyen le plus élevé d'Europe (30,3 % en 2019) », contre 20,1 % en moyenne dans l'OCDE.",
  "Site d'information de référence sur les questions européennes (données anciennes).", 'media'))
OCDE_RECETTES = ('ocde_recettes', src("Statistiques des recettes publiques 2025 — Tendances des recettes fiscales 1965-2024", "OCDE", "Décembre 2025",
  "https://www.oecd.org/fr/publications/statistiques-des-recettes-publiques-2025_f7a1e5e4-fr/full-report/tax-revenue-trends-1965-2024_98c75833.html",
  "Les recettes fiscales « s'établissaient en moyenne à 34.1 % » du PIB dans l'OCDE en 2024 (données provisoires) ; le Danemark (45,2 %) s'est classé au premier rang pour la deuxième année consécutive, la France est deuxième (43,5 %) ; le ratio le plus bas est celui du Mexique (18,3 %).",
  "Organisation internationale de référence pour les comparaisons fiscales."))
TLE_PO = ('tle_po', src("Impôts : la France occupe à nouveau la première place en Europe", "Toute l'Europe (Léa Deseille), d'après Eurostat", "29 octobre 2026",
  "https://www.touteleurope.eu/economie-et-social/impots-la-france-occupe-a-nouveau-la-premiere-place-en-europe/",
  "En 2025, selon Eurostat, les impôts et cotisations sociales nettes ont atteint 46 % du PIB en France, premier rang de l'UE, devant le Danemark (45,1 %) et la Belgique (44,7 %) ; moyenne de l'UE : 40,7 % ; avec la méthode de l'Insee, le taux est de 43,6 %.",
  "Site d'information de référence, d'après Eurostat.", 'media'))
DREES_PROT = ('drees_prot', src("La protection sociale en France et en Europe en 2024 (Panoramas de la DREES, édition 2025)", "DREES", "17 décembre 2025",
  "https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/panoramas-de-la-drees/251217-protection-sociale-france-europe-2024",
  "Les prestations de protection sociale atteignent 932,5 Md€ en 2024, soit 31,9 % du PIB, contre 27,3 % en moyenne dans l'UE à 27 ; « les risques vieillesse-survie et santé […] représentent 80 % de l'ensemble des dépenses de prestations sociales ».",
  "Service statistique du ministère des Solidarités."))
OCDE_SANTE = ('ocde_sante', src("Panorama de la santé 2025 — Dépenses de santé par mode de financement", "OCDE", "2025",
  "https://www.oecd.org/fr/publications/panorama-de-la-sante-2025_2f564c6c-fr/full-report/health-expenditure-by-financing-scheme_074bead0.html",
  "En France, « plus des trois quarts des dépenses étaient pris en charge par une forme d'assurance maladie obligatoire » (2023) ; aux États-Unis, 55 % relèvent de régimes obligatoires, dont des assurances privées rendues obligatoires, et les régimes publics n'en couvrent qu'environ 28 %.",
  "Organisation internationale de référence."))
INSEE_FP = ('insee_fp', src("L'emploi dans la fonction publique en 2024 (Insee Première n° 2094)", "Insee (Léna Esbelin, Téo Moreau) et DGAFP (Sarah Touzé)", "10 février 2026",
  "https://www.insee.fr/fr/statistiques/8732435",
  "« 5,9 millions d'agents travaillent dans la fonction publique » fin 2024, soit +0,6 % (+32 800) : 2 587 400 dans la fonction publique de l'État, 2 039 400 dans la territoriale et 1 249 900 dans l'hospitalière.",
  "Statistique publique de référence."))
OCDE_EMPLOI_PUB = ('ocde_emp', src("Panorama des administrations publiques 2025 — Emploi dans les administrations publiques", "OCDE", "19 juin 2025",
  "https://www.oecd.org/fr/publications/panorama-des-administrations-publiques-2025_758a7905-fr/full-report/employment-in-general-government_dafcfac5",
  "« En 2023, l'emploi public représentait en moyenne 18.4 % de l'emploi total dans les pays de l'OCDE » ; Norvège 30,1 %, Suède 28,2 %, Danemark 27,3 % ; pour la France, une baisse de 0,9 point entre 2019 et 2023.",
  "Organisation internationale de référence."))
FS_EMPLOI_PUB = ('fs_emp', src("Comment la France se compare-t-elle en matière d'emploi public ? (communiqué)", "France Stratégie", "19 décembre 2017",
  "https://www.strategie-plan.gouv.fr/files/files/Presse/CP%202017/2017-12-19_Comment%20la%20France%20se%20compare-t-elle%20en%20mati%C3%A8re%20d%E2%80%99emploi%20public.pdf",
  "La France compte 89 emplois publics pour 1 000 habitants, « un taux relativement élevé » (Norvège 159, Japon 40) ; l'écart se réduit si l'on tient compte des services achetés au privé : les dépenses de fonctionnement « indirectes » valent 6 % du PIB en France, contre 8 % en Allemagne, 9 % au Japon et 10 % aux Pays-Bas.",
  "Organisme public d'expertise (données anciennes).", 'etude'))
PS_TVA = ('ps_tva', src("Baisse de la TVA sur l'énergie proposée par le RN : une mesure chiffrée à 17 milliards selon Bercy", "Public Sénat", "14 juin 2024",
  "https://www.publicsenat.fr/actualites/politique/baisse-de-la-tva-sur-lenergie-proposee-par-le-rn-une-mesure-chiffree-a-17-milliards-selon-bercy",
  "La baisse de la TVA à 5,5 % sur l'énergie est une promesse du Rassemblement national pour les législatives de 2024 ; selon Bercy, elle aurait « un coût global de 16,8 milliards d'euros pour les finances publiques » : environ 4,5 Md€ pour l'électricité, 2,3 Md€ pour le gaz et 10 Md€ pour les carburants.",
  "Média parlementaire rendant compte d'un chiffrage du ministère de l'Économie (gouvernement de l'époque).", 'media'))
MONTAIGNE_TVA = ('montaigne_tva', src("Baisser la TVA de 20 % à 5,5 % pour les carburants, l'électricité, le gaz et le fioul domestique (chiffrage Législatives 2024, Rassemblement national)", "Institut Montaigne", "Juin 2024",
  "https://www.institutmontaigne.org/legislatives-2024/rassemblement-national/baisser-la-tva-de-20-a-55-pour-les-carburants-lelectricite-le-gaz-et-le-fioul-domestique",
  "« Au total, la perte de recettes fiscales s'établirait à 11,3 Md€ environ par an » (fourchette de 9 à 13,6 Md€) ; pour le gaz et l'électricité, un taux réduit est possible sous conditions de la directive TVA ; pour les carburants, la directive ne le prévoit pas : il faudrait la réviser, ce qui exige l'unanimité des États.",
  "Think tank libéral, chiffrage indépendant des programmes.", 'etude'))
INSEE_ENERGIE = ('insee_energie', src("Entre janvier 2021 et juin 2022, la hausse des prix de l'énergie a entraîné une perte de pouvoir d'achat, malgré la mise en œuvre des mesures exceptionnelles (Insee Analyses n° 78)", "Insee (Flore Cornuet)", "19 décembre 2022",
  "https://www.insee.fr/fr/statistiques/6655850",
  "Le bouclier tarifaire et la remise carburant ont réduit les dépenses de 210 euros en moyenne pour les 30 % les plus modestes et de 350 euros pour les 30 % les plus aisés ; les gains « atteignent 420 euros pour les 10 % les plus aisés, contre 180 euros pour les 10 % les plus modestes » ; rapporté au revenu, +0,7 % pour les 30 % les plus modestes contre +0,4 % pour les 30 % les plus aisés ; résultats de simulation jugés fragiles.",
  "Statistique publique de référence."))

# Écologie, santé, société
GIEC = ('giec', src("Climate Change 2021: The Physical Science Basis — Summary for Policymakers (AR6, groupe de travail I)", "GIEC (IPCC)", "Août 2021",
  "https://ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers",
  "A.1 : « It is unequivocal that human influence has warmed the atmosphere, ocean and land » ; température de surface 1,09 °C plus élevée en 2011-2020 qu'en 1850-1900 ; réchauffement d'origine humaine estimé à 1,07 °C (0,8 à 1,3 °C) ; « Global surface temperature has increased faster since 1970 than in any other 50-year period over at least the last 2000 years » ; en 2019, concentration de CO2 plus élevée qu'à n'importe quel moment depuis au moins 2 millions d'années.",
  "Synthèse scientifique internationale de référence, approuvée par les États."))
METEO_FR = ('meteo_fr', src("Le changement climatique en France", "Météo-France", "28 février 2020",
  "https://meteofrance.com/changement-climatique/le-changement-climatique-en-france",
  "Hausse des températures moyennes en France de 1,7 °C depuis 1900 ; tendance de +0,3 °C par décennie sur la période 1959-2009.",
  "Service public de météorologie et de climatologie."))
MTE_ADAPT = ('mte_adapt', src("La France s'adapte", "Ministère de la Transition écologique", "Mise à jour du 23 octobre 2026",
  "https://www.ecologie.gouv.fr/es/node/4194",
  "En France métropolitaine, « le réchauffement a déjà atteint 1,9 °C sur la dernière décennie depuis 1900 ».",
  "Ministère compétent."))
AN_EOL = ('an_eol', src("Question écrite n° 23435 (coût écologique de l'énergie éolienne et procédures de recyclage) et réponse du ministère", "Assemblée nationale / ministère de la Transition écologique", "16 février 2021",
  "https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE23435.pdf",
  "Une analyse de cycle de vie de 2015 réalisée pour l'Agence de la transition écologique évalue l'éolien terrestre à « 12,7 g de CO2 eq / kWh », contre « 1000 g » pour le charbon, « 840 g » pour le pétrole et « 469 g » pour le gaz naturel ; l'arrêté du 22 juin 2020 impose « l'excavation totale des fondations » ; selon l'ADEME, « moins de 30 % du parc installé contient des terres rares » et les installations terrestres actuelles n'en contiennent plus.",
  "Réponse officielle du ministère compétent."))
DREAL_EOL = ('dreal_eol', src("Fiche thématique — Économie circulaire de l'éolien", "DREAL Auvergne-Rhône-Alpes (services de l'État), avec le pôle Tenerrdis", "Juin 2023",
  "https://www.auvergne-rhone-alpes.developpement-durable.gouv.fr/IMG/pdf/fteol4-202301-ecocirculaireeol_vf.pdf",
  "Obligations réglementaires : excavation de la totalité des fondations, recyclage ou réutilisation de 90 % de la masse de l'éolienne et de 35 % du rotor, portés progressivement à 95 % et 55 % jusqu'en 2025 ; les pales en matériaux composites sont plus difficiles à recycler, avec environ 50 % de matière récupérée lors des premières opérations ; le projet ZEBRA vise des pales 100 % recyclables.",
  "Services déconcentrés de l'État."))
ADEME_VE = ('ademe_ve', src("Voitures électriques et bornes de recharge (Les avis de l'ADEME)", "ADEME (Agence de la transition écologique)", "Octobre 2022",
  "https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/actualites/14983/14983-avis-ademe-voitures-electriques-et-bornes-recharges-octobre-2022.pdf",
  "Une voiture électrique à batterie raisonnable (moins de 60 kWh) « a un impact carbone 2 à 3 fois inférieur à celui d'un modèle similaire thermique » ; elle part avec une « dette carbone » à 0 km, amortie avant 20 000 km pour une citadine, vers 70 000 km pour une compacte et au-delà de 100 000 km pour une batterie de 100 kWh ; l'électricité peu carbonée de la France réduit les émissions à l'usage ; besoins en lithium « entre +300% et +800% » par rapport à 2020 ; particules liées à l'usure des pneus et des freins, accentuées par la masse.",
  "Agence publique de référence (document hébergé par Eduscol)."))
ICCT_VE = ('icct_ve', src("A global comparison of the life-cycle greenhouse gas emissions of combustion engine and electric passenger cars", "International Council on Clean Transportation (ICCT)", "Juillet 2021",
  "https://theicct.org/publication/a-global-comparison-of-the-life-cycle-greenhouse-gas-emissions-of-combustion-engine-and-electric-passenger-cars/",
  "Pour les voitures moyennes immatriculées en 2021, les émissions sur toute la durée de vie des voitures électriques sont « already lower than comparable gasoline cars by 66%–69% in Europe », 60 à 68 % aux États-Unis, 37 à 45 % en Chine et 19 à 34 % en Inde.",
  "Centre de recherche indépendant sur les transports.", 'etude'))
C4_VE = ('c4_ve', src("Les idées reçues sur le véhicule électrique", "Carbone 4", "Février 2022",
  "https://carbone4.com/files/359_publication_faq_vehicule_electrique.pdf",
  "En France, un véhicule électrique émet « 3 à 4 fois moins de CO2e que son équivalent thermique » sur sa durée de vie ; sa fabrication émet davantage, « essentiellement du fait de la fabrication des batteries » ; une Audi e-tron a une empreinte « 2 fois supérieure » à celle d'une petite citadine électrique.",
  "Cabinet de conseil spécialisé dans le climat.", 'etude'))
OFDT_CANNABIS = ('ofdt_cannabis', src("Levels of illegal drug use in France in 2023 (Tendances n° 164)", "OFDT (S. Spilka, O. Le Nézet, É. Janssen et al.)", "24 juin 2024",
  "https://en.ofdt.fr/publication/2024/levels-illegal-drug-use-france-2023-2122",
  "En 2023, 10,8 % des 18-64 ans ont consommé du cannabis dans l'année, un niveau qui « has remained stable for about ten years » ; plus de la moitié des adultes l'ont déjà expérimenté ; la consommation recule chez les jeunes.",
  "Observatoire public des drogues et des tendances addictives."))
AN_CANNABIS = ('an_cannabis', src("La légalisation du cannabis en question(s) — dossier de presse du rapport de la mission d'information", "Assemblée nationale (mission d'information, rapporteure Caroline Janvier, président Robin Reda)", "5 mai 2021",
  "https://www2.assemblee-nationale.fr/static/15/mission-information/DP_Cannabis_05.05.21.pdf",
  "« La France est aujourd'hui le plus gros consommateur de cannabis au sein de l'Union européenne » ; 18 millions de personnes l'ont expérimenté, 5 millions en ont consommé dans l'année, 1,5 million sont des usagers réguliers dont 900 000 quotidiens ; le rapport fait le « constat d'un échec de la politique répressive ».",
  "Rapport parlementaire transpartisan."))
CAE_CANNABIS = ('cae_cannabis', src("Cannabis : comment reprendre le contrôle ? (dossier de presse de la note n° 52)", "Conseil d'analyse économique (Emmanuelle Auriol, Pierre-Yves Geoffard)", "20 juin 2019",
  "https://cae-eco.fr/static/pdf/conf_de_presse_note052.pdf",
  "« Le système de prohibition français est à la fois coûteux et inefficace » ; les Français sont « parmi les plus gros consommateurs de cannabis de l'Union européenne » ; selon les travaux cités, la légalisation entraîne une hausse des usages chez les consommateurs réguliers, mais peut réduire ceux des plus jeunes si l'interdiction de vente aux mineurs est respectée.",
  "Organisme public d'expertise économique placé auprès du Premier ministre.", 'etude'))
STATCAN = ('statcan', src("Évolution de la consommation de cannabis de 2018 à 2020 (Le Quotidien)", "Statistique Canada", "21 avril 2021",
  "https://www150.statcan.gc.ca/n1/daily-quotidien/210421/dq210421c-fra.htm",
  "Consommation au cours des trois derniers mois : 14 % avant la légalisation, 18 % dans les premiers mois après, 20 % fin 2020 ; consommation quotidienne ou quasi quotidienne : « 7,9 %, comparativement à 6,1 % en 2019 et à 5,4 % en 2018 ».",
  "Institut statistique public du Canada."))
DREES_IVG = ('drees_ivg', src("En 2024, 251 270 IVG ont eu lieu en France, dont 80 % sont médicamenteuses (Études et Résultats n° 1350)", "DREES (Annick Vilain, Jeanne Fresson)", "25 septembre 2025",
  "https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/etudes-et-resultats/250925-ER-ivg-en-france-en-2024",
  "« 251 270 IVG ont été réalisées en France en 2024, soit 7 000 de plus qu'en 2023 » ; « le taux de recours à l'IVG atteint ainsi 17,3 ‰ en 2024 contre 16,8 ‰ en 2023 » chez les femmes de 15 à 49 ans ; le taux le plus élevé concerne les 25-29 ans (29,8 ‰) ; chez les moins de 20 ans, il est plus faible qu'il y a dix ans (5,5 ‰ contre 8,7 ‰).",
  "Service statistique du ministère de la Santé."))
HAS_CONTRA = ('has_contra', src("Vers une contraception mieux adaptée au profil de chacun (communiqué)", "Haute Autorité de santé (HAS)", "15 mai 2013",
  "https://has-sante.fr/jcms/c_1545515/fr/vers-une-contraception-mieux-adaptee-au-profil-de-chacun",
  "« Deux grossesses non prévues sur 3 surviennent alors qu'une méthode contraceptive est utilisée » ; « un tiers de ces grossesses est dû à l'absence de contraception ».",
  "Autorité publique indépendante d'expertise en santé (données anciennes)."))
AN_IVG = ('an_ivg', src("Question écrite n° 91517 (IVG et contraception) et réponse du ministère de la Santé", "Assemblée nationale / ministère de la Santé", "8 mars 2011",
  "https://www.questions.assemblee-nationale.fr/dyn/13/questions/QANR5L13QE91517.pdf",
  "La question cite le rapport de l'IGAS : « 72 % des IVG sont réalisés sur des femmes sous contraception » ; la réponse du ministère indique : « Deux tiers des IVG sont le résultat d'échecs contraceptifs ».",
  "Réponse officielle du ministère compétent (données anciennes)."))

# Histoire et vie politique
MEMORIAL = ('memorial', src("The Jews of France in the Shoah", "Mémorial de la Shoah", "Page mise à jour le 21 juillet 2017",
  "https://www.memorialdelashoah.org/en/archives-et-documentation/quest-ce-que-la-shoah/juifs-de-france-shoah.html",
  "« 76,000 Jews, including more than 11,000 children, were deported by the Nazis with the help of the Vichy government » ; Vichy a promulgué le statut des Juifs (presse du 19 octobre 1940) ; à l'été 1942, le gouvernement de Vichy a livré aux occupants des Juifs étrangers de la zone sud et des enfants ; 25 % de la population juive de France a été victime de la Shoah.",
  "Institution de référence sur l'histoire de la Shoah."))
JOLY_NANTES = ('joly', src("Vichy, le Troisième Reich et les Juifs (notes de la conférence de Laurent Joly, directeur de recherche au CNRS)", "Académie de Nantes / Mémorial de la Shoah (notes de Riselaine Chapel)", "Octobre 2022",
  "https://pedagogie.ac-nantes.fr/medias/fichier/laurent-joly-vichy-le-troisieme-reich-et-les-juifs-paf-memorial-de-la-shoah-octobre-2022_1696660194350-pdf",
  "« Le 3 octobre 1940 c'est la promulgation du statut des Juifs qui vise aussi les Juifs français » ; « le bilan est de 74 500 Juifs dont 24 500 Français » ; la rafle du Vél d'Hiv a été organisée et menée par la police française, « sans la présence d'un seul Allemand », avec environ 4 500 policiers.",
  "Formation d'enseignants, conférence d'un historien du CNRS.", 'secondaire'))
APHG_JOLY = ('aphg_joly', src("Compte rendu de « L'État contre les Juifs » (Laurent Joly, Grasset)", "APHG Languedoc-Roussillon (Dalila Chalabi)", "Non daté",
  "https://www.aphg.fr/IMG/pdf/joly_l_etat_contre_les_juifs.pdf",
  "Le statut des Juifs est décrit comme « un choix délibéré et non contraint par l'occupant » ; l'ouvrage s'inscrit « dans la continuité des travaux de Robert Paxton et de Michael Marrus » et réfute l'idée que l'État français aurait livré les Juifs étrangers pour protéger les Juifs français.",
  "Association des professeurs d'histoire-géographie (compte rendu d'un ouvrage d'historien).", 'secondaire'))
PS_SEMELIN = ('ps_semelin', src("« Si tant de juifs ont survécu à l'occupation ce n'est pas grâce au régime de Vichy », rappelle Jacques Semelin", "Public Sénat (Simon Barbarit)", "8 septembre 2023",
  "https://www.publicsenat.fr/actualites/societe/propos-de-zemmour-sur-petain-si-tant-de-juifs-ont-survecu-a-loccupation-ce-nest-pas-grace-au-regime-de-vichy-rappelle-lhistorien-jacques-semelin",
  "L'historien Jacques Semelin (CNRS, Sciences Po) : « Si tant de juifs ont survécu à l'occupation en France c'est en dépit de Vichy mais pas grâce à Vichy » ; il chiffre à 24 500 les Juifs français exterminés ; les Juifs français étaient moins exposés aux arrestations que les étrangers.",
  "Média parlementaire, entretien avec un historien.", 'media'))
PS_CHIRAC = ('ps_chirac', src("Le discours du Vel d'Hiv : un moment fort de la présidence Chirac", "Public Sénat", "24 juin 2015",
  "https://www.publicsenat.fr/actualites/politique/le-discours-du-vel-d-hiv-un-moment-fort-de-la-presidence-chirac-145873",
  "Discours du 16 juillet 1995 : « Oui, la folie criminelle de l'occupant a été secondée par des Français, par l'Etat français » ; les 16 et 17 juillet 1942, quelque 13 000 Juifs ont été arrêtés par des policiers et gendarmes français.",
  "Média parlementaire.", 'media'))
LEBOURG_FN = ('lebourg', src("FN et radicaux : une interaction dynamique (Hommes & Libertés n° 166)", "Nicolas Lebourg (historien, université de Perpignan)", "Juin 2014",
  "https://www.ldh-france.org/wp-content/uploads/2014/10/HL166-Dossier-7.-FN-et-radicaux-une-interaction-dynamique.pdf",
  "« Se trouve en son sein l'ancien de la division Charlemagne, Pierre Bousquet, qui sera le premier trésorier du FN » ; la revue Militant était animée « par les ex-Waffen-SS Pierre Bousquet et Jean Castrillo ».",
  "Article d'un historien spécialiste de l'extrême droite (revue de la Ligue des droits de l'homme).", 'etude'))
RTBF_FN = ('rtbf_fn', src("Des débuts modestes avec des anciens SS et ex-membres de l'OAS : comment est né le Front national ?", "RTBF (Pierre Marlet)", "8 octobre 2021",
  "https://www.rtbf.be/article/comment-est-ne-le-front-national-10853858",
  "Parmi ceux qui ont joué un rôle actif dans la création du FN figurent d'anciens de la Waffen-SS comme Pierre Bousquet ; François Brigneau est présenté comme ancien membre de la Milice française sous Vichy.",
  "Média public belge.", 'media'))
FJJ_ON = ('fjj_on', src("Aux racines du FN. L'histoire du mouvement Ordre nouveau", "Fondation Jean-Jaurès (présentation d'ouvrage)", "Non daté",
  "https://www.jean-jaures.org/publication/aux-racines-du-fn-lhistoire-du-mouvement-ordre-nouveau/",
  "Ordre nouveau « fonda le Front national en 1972 » et en fut la « véritable colonne vertébrale idéologique et militante » ; il était placé sous le patronage de « grands anciens » passés par les mouvements nationalistes d'avant 1940 ou par la Révolution nationale.",
  "Fondation proche du Parti socialiste ; présentation d'un ouvrage d'historiens.", 'partisane'))
AN_COLO = ('an_colo', src("Question écrite n° 81742 (article 4 de la loi du 23 février 2005) et réponse du ministre de l'Éducation nationale", "Assemblée nationale / ministère de l'Éducation nationale", "15 août 2006",
  "https://www.assemblee-nationale.fr/dyn/12/questions/QANR5L12QE81742.pdf",
  "La question vise l'article 4 de la loi du 23 février 2005 sur « le rôle positif de la présence française outre-mer, notamment en Afrique du Nord » ; la réponse indique que le Conseil constitutionnel, saisi par le Premier ministre, a jugé que le second alinéa relevait du domaine réglementaire et que le décret n° 2006-160 du 15 février 2006 l'a abrogé.",
  "Réponse officielle du ministère compétent."))
KATEB_ALGERIE = ('kateb', src("Les séparations scolaires dans l'Algérie coloniale (Insaniyat n° 25-26)", "Kamel Kateb (chercheur à l'INED)", "30 septembre 2004",
  "https://www.insaniyat.crasc.dz/en/article/les-separations-scolaires-dans-lalgerie-coloniale",
  "Taux de scolarisation des enfants de 6 à 14 ans en 1954, d'après les annuaires statistiques : 16,7 % pour les « indigènes » (304 015 sur 1 833 623), 85,4 % pour les Européens d'Algérie, 97,6 % en France ; pour les « indigènes » : 3,8 % en 1911, 7,9 % en 1936, 9,8 % en 1948.",
  "Article scientifique d'un démographe de l'INED.", 'etude'))
AN_TRAVAIL_FORCE = ('an_travail_force', src("Question écrite n° 14134 (loi Houphouët-Boigny)", "Assemblée nationale", "7 avril 2026",
  "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE14134",
  "Rappel de la « loi n° 46-645 du 11 avril 1946 relative à la suppression du travail forcé dans les territoires d'outre-mer », dite loi Houphouët-Boigny, qui « a posé le principe de l'interdiction absolue du travail forcé ».",
  "Document parlementaire officiel."))
AN_INGERENCES = ('an_ingerences', src("Rapport n° 1311 de la commission d'enquête relative aux ingérences politiques, économiques et financières de puissances étrangères (tome I)", "Assemblée nationale (président Jean-Philippe Tanguy, rapporteure Constance Le Grip)", "1er juin 2023",
  "https://www.assemblee-nationale.fr/dyn/16/rapports/ceingeren/l16b1311-t1_rapport-enquete.pdf",
  "« Le prêt de 9,4 millions d'euros contracté en 2014 auprès de la First Czech Russian Bank (FCRB), alors contrôlée par un oligarque russe, a été finalement racheté par l'entreprise russe Aviazapchast à la suite de la faillite de la banque en 2016 » ; « cette firme appartenant au complexe militaro-industriel en a rééchelonné le remboursement jusqu'en 2028 » ; la CNCCFP y voit un « avantage certain et conséquent » ; le rapport mentionne des déplacements d'élus au Donbass ou en Crimée annexée.",
  "Rapport parlementaire officiel (adopté par la majorité de la commission)."))
LCP_INGERENCES = ('lcp_ingerences', src("Ingérences : qualifié de « courroie de transmission » de la Russie dans le rapport de la commission d'enquête, le RN dénonce un « procès politique »", "LCP (Raphaël Marchal)", "1er juin 2023",
  "https://lcp.fr/actualites/ingerences-qualifie-de-courroie-de-transmission-de-la-russie-dans-le-rapport-de-la",
  "Le rapport présente le FN/RN comme « une courroie de transmission » de la Russie ; selon la rapporteure, le parti s'est « avéré un relais assez affirmé, assez constant », notamment sur l'annexion de la Crimée en 2014 ; le président RN de la commission affirme que « rien n'a permis d'établir une ingérence au cours des auditions » ; rapport adopté par 11 voix contre 5.",
  "Chaîne parlementaire.", 'media'))
LOCAL_PRET = ('local_pret', src("French far-right party says Russian loan repaid", "AFP, via The Local", "21 septembre 2023",
  "https://www.thelocal.fr/20230921/french-far-right-party-says-russian-loan-repaid",
  "Le Rassemblement national a annoncé dans un communiqué avoir remboursé par anticipation les 6,1 millions d'euros restants sur le prêt de 9,4 millions, avant l'échéance de 2028.",
  "Dépêche AFP rapportant une annonce du parti.", 'media'))
JUSTICE_ELECTIONS = ('justice_elec', src("Élections professionnelles 2026 relatives à la nouvelle commission d'avancement des magistrats", "Ministère de la Justice", "13 février 2026",
  "https://www.justice.gouv.fr/actualites/espace-presse/elections-professionnelles-2026-relatives-nouvelle-commission-davancement-magistrats",
  "Résultats : USM 60,99 % (4 sièges), Syndicat de la magistrature 25,03 % (1 siège), Unité Magistrats-FO 12,51 % (1 siège), CFDT-Magistrats 1,46 % ; participation : 62,75 %.",
  "Communiqué officiel du ministère."))
PS_SM = ('ps_sm', src("Inéligibilité de Marine Le Pen : que pèse le Syndicat de la magistrature ciblé par le RN et une partie de la droite ?", "Public Sénat (Simon Barbarit)", "7 avril 2025",
  "https://www.publicsenat.fr/actualites/politique/ineligibilite-de-marine-pen-pourquoi-le-syndicat-de-la-magistrature-est-cible-par-le-rn-et-une-partie-de-la-droite",
  "Environ 9 500 magistrats, dont au moins la moitié ne sont pas syndiqués ; adhérents : USM environ 2 500, Syndicat de la magistrature « pas beaucoup plus de 1000 » ; élections au CSM de fin 2022 : USM 66,6 %, SM 33,3 % ; le sociologue Laurent Willemez : « l'essence même du métier de magistrat est d'être le plus impartial possible » ; en 2013, un panneau de photos (« mur des cons ») a été découvert au local du SM et son ancienne présidente a été condamnée pour injure publique.",
  "Média parlementaire.", 'media'))
PS_IMPART = ('ps_impart', src("Magistrats syndiqués : le Sénat impose le respect du « principe d'impartialité »", "Public Sénat (Simon Barbarit)", "8 juin 2023",
  "https://www.publicsenat.fr/actualites/politique/magistrats-syndiques-le-senat-impose-le-respect-du-principe-dimpartialite",
  "Le Sénat a adopté un amendement rappelant « le respect du principe d'impartialité pour les magistrats syndiqués » ; le Conseil supérieur de la magistrature avait affirmé que « la liberté syndicale est reconnue aux magistrats » et que l'appartenance syndicale ne peut fonder à elle seule une remise en cause de l'impartialité d'un magistrat.",
  "Média parlementaire.", 'media'))
ACTU_JUR_MUR = ('actujur_mur', src("« Mur des cons » : une cinglante condamnation", "Actu-Juridique", "12 mars 2019",
  "https://www.actu-juridique.fr/professions/mur-des-cons-une-cinglante-condamnation/",
  "Par un jugement du 31 janvier 2019, le tribunal correctionnel de Paris a condamné l'ancienne présidente du Syndicat de la magistrature pour injure publique envers un des plaignants, à 500 euros d'amende ; les autres plaignants ont été déboutés.",
  "Média juridique spécialisé.", 'media'))

# École, social, services
OCDE_PISA = ('ocde_pisa', src("PISA 2022 Results — Factsheets: France", "OCDE", "5 décembre 2023",
  "https://oecd.org/publication/pisa-2022-results/webbooks/dynamic/pisa-country-notes/8008535b/pdf/france.pdf",
  "« Average 2022 results were down compared to 2018 in mathematics and reading » ; « 2022 results are among the lowest ever measured by PISA in all three subjects » ; en mathématiques, « the large decline observed over the most recent period is unprecedented » ; 71 % des élèves atteignent au moins le niveau 2 en mathématiques (moyenne OCDE : 69 %) ; écart de 113 points entre élèves favorisés et défavorisés, plus grand que la moyenne de l'OCDE (93 points).",
  "Organisation internationale de référence (enquête PISA)."))
PS_PISA = ('ps_pisa', src("Classement Pisa : chute historique du score de la France en mathématiques", "Public Sénat (Henri Clavier)", "5 décembre 2023",
  "https://publicsenat.fr/actualites/education/classement-pisa-chute-historique-du-score-de-la-france-en-mathematiques",
  "En mathématiques, le score français chute de 21 points, à 474, alors que la moyenne de l'OCDE perd 15 points, à 472 ; le score chute de 19 points en compréhension de l'écrit, contre 10 points dans l'OCDE ; selon l'OCDE, la baisse « n'est attribuable qu'en partie à la pandémie de covid-19 ».",
  "Média parlementaire, d'après l'OCDE.", 'media'))
DEPP_TIMSS = ('depp_timss', src("TIMSS 2023 en quatrième pour les mathématiques : des résultats stables en France et un accroissement des écarts de performance entre les élèves (Note d'information n° 24.48)", "DEPP, ministère de l'Éducation nationale (A. Lacroix, C. Philippe, F. Salles)", "Décembre 2024",
  "https://cafepedagogique.net/wp-content/uploads/2024/12/depp-ni-2024-48.pdf",
  "En 4e, la France obtient 479 points, inférieur à la moyenne des 22 pays de l'OCDE et de l'UE participants (507) ; pas de différence significative avec 2019 (483) ; « 17 % des élèves de France n'atteignent pas le niveau bas défini par Timss », contre 3 % en 1995 et 12 % en 2019 ; 3 % d'élèves au niveau avancé, contre 11 % en moyenne.",
  "Service statistique du ministère de l'Éducation nationale (copie hébergée par le Café pédagogique)."))
UNEDIC_MONTANT = ('unedic_montant', src("Le montant d'indemnisation chômage au 4e trimestre 2025", "Unédic (Adrien Gaboulaud)", "27 mai 2026",
  "https://www.unedic.org/publications/le-montant-dindemnisation-chomage-au-4e-trimestre-2025",
  "« Au 4e trimestre 2025, l'allocation est en moyenne de 1040 € » ; « 54 % touchent une indemnisation inférieure à 1000 € nets mensuels » ; 7 % touchent plus de 2 000 € et 2 % 3 000 € ou plus ; « une majorité d'allocataires perçoit une allocation inférieure au montant mensuel du Smic net (1426,30 € au 4e trimestre 2025) ».",
  "Organisme paritaire gestionnaire de l'assurance chômage."))
UNEDIC_CALCUL = ('unedic_calcul', src("Revalorisation des allocations d'assurance chômage, mode d'emploi — juin 2025", "Unédic", "25 juin 2025",
  "https://www.unedic.org/publications/revalorisation-des-allocations-d-assurance-chomage-mode-d-emploi-juin-2025",
  "L'allocation est calculée sur le salaire journalier de référence (SJR) : « 40,4 % SJR + partie fixe » ou « 57 % SJR » ; « les SJR les plus faibles bénéficient d'un taux de remplacement de 75 % », les plus élevés sont indemnisés à hauteur de 57 % ; dégressivité jusqu'à 30 % après 182 jours pour les moins de 55 ans aux allocations élevées.",
  "Organisme paritaire gestionnaire de l'assurance chômage."))
UNEDIC_INSCRITS = ('unedic_inscrits', src("Est-ce que toutes les personnes inscrites à France Travail perçoivent une allocation chômage ?", "Unédic", "2025",
  "https://www.unedic.org/lassurance-chomage-en-france/decryptage/est-ce-que-toutes-les-personnes-inscrites-a-pole-emploi-percoivent-une-allocation-chomage",
  "« 5,7 millions de demandeurs d'emploi étaient inscrits », dont « 3,8 millions étaient allocataires de l'Assurance chômage, dont 2,6 millions étaient indemnisés ».",
  "Organisme paritaire gestionnaire de l'assurance chômage."))
FT_TAUX = ('ft_taux', src("Taux de remplacement mensuel net (fiche)", "France Travail (pour le ministère du Travail)", "Données 2015-2017",
  "https://www.francetravail.org/files/live/sites/peorg/files/documents/Statistiques-et-analyses/_Documentation/Fiche%20taux%20de%20remplacement.pdf",
  "Avant la réforme de 2021, environ « 21% des ouvertures de droit » avaient un taux de remplacement supérieur à 100 % du salaire mensuel moyen antérieur, en raison d'un calcul fondé sur les seuls jours travaillés, qui gonflait le ratio pour les parcours d'emploi très morcelés.",
  "Opérateur public de l'emploi (données anciennes)."))
UNEDIC_2021 = ('unedic_2021', src("Assurance chômage : ce qui entre en vigueur au 1er octobre", "Unédic", "1er octobre 2021",
  "https://www.unedic.org/actualites/assurance-chomage-ce-qui-entre-en-vigueur-au-1er-octobre",
  "À partir du 1er octobre 2021, le salaire journalier de référence est calculé en divisant le total des salaires par les jours calendaires de la période, travaillés et non travaillés, dans la limite d'un plafond de jours non travaillés.",
  "Organisme paritaire gestionnaire de l'assurance chômage."))
JUSTICE_INCARC = ('justice_incarc', src("Mesure de l'incarcération — indicateurs clés au 1er octobre 2026", "Ministère de la Justice (DGAP / SSER)", "Novembre 2026",
  "https://www.justice.gouv.fr/sites/default/files/2026-11/mesure_mensuelle_01102026.pdf",
  "Au 1er octobre 2026 : 90 937 personnes détenues pour 63 452 places opérationnelles ; densité carcérale de 143,3 %, et de 178,0 % en maisons d'arrêt ; 8 959 matelas au sol, contre 5 895 un an plus tôt ; 57 292 détenus hébergés dans une structure à plus de 150 % de densité.",
  "Statistique officielle du ministère de la Justice."))
SENAT_CGLPL = ('senat_cglpl', src("Rapport d'information n° 831 (2025-2026) sur le Contrôleur général des lieux de privation de liberté", "Sénat, commission des finances (Christopher Szczurek)", "1er juillet 2026",
  "https://www.senat.fr/rap/r25-831/r25-8311.pdf",
  "Par l'arrêt J.M.B. et autres c. France du 30 janvier 2020, la Cour européenne des droits de l'homme a condamné la France pour violation de l'article 3 (traitements inhumains ou dégradants) et de l'article 13 (droit à un recours effectif), sur 32 requêtes de détenus ; en 2025, 17 % des signalements reçus par le CGLPL portent sur les conditions matérielles de détention (hygiène, hébergement, restauration).",
  "Rapport parlementaire de contrôle."))
LCP_CGLPL = ('lcp_cglpl', src("Prisons : « Surveillants et détenus vivent pareillement l'abandon et l'inertie de l'État », alerte Dominique Simonnot", "LCP (Léonard Dermarkarian), d'après le rapport annuel 2023 du CGLPL", "18 septembre 2024",
  "https://lcp.fr/actualites/prisons-surveillants-et-detenus-vivent-pareillement-l-abandon-et-l-inertie-de-l-etat",
  "La Contrôleure générale des lieux de privation de liberté : « Surveillants et détenus vivent pareillement l'abandon, l'inertie de l'Etat » ; « invasion de punaises de lit » ; taux d'occupation moyen de 150 %, avec des pics à 250 %.",
  "Chaîne parlementaire rendant compte d'un rapport d'une autorité indépendante.", 'media'))
JUSTICE_DETENTION = ('justice_detention', src("La prise en charge en détention", "Ministère de la Justice", "Mise à jour du 4 avril 2025",
  "https://www.justice.gouv.fr/justice-france/prise-charge-personnes-condamnees-ou-prevenues/prise-charge-detention",
  "En détention, les personnes ont accès à des activités : travail, formation professionnelle, enseignement, sport et activités socio-culturelles.",
  "Ministère compétent."))
AN_SSD = ('an_ssd', src("Rapport d'information n° 1014 sur l'évaluation de l'action de l'État dans l'exercice de ses missions régaliennes en Seine-Saint-Denis", "Assemblée nationale (François Cornut-Gentille, Rodrigue Kokouendo)", "31 mai 2018",
  "https://www.assemblee-nationale.fr/15/pdf/rap-info/i1014.pdf",
  "Taux de remplacement des enseignants absents dans le premier degré : 51,26 % en 2015-2016, contre 62,50 % dans le Val-de-Marne et 78,41 % en France ; au tribunal d'instance d'Aubervilliers, délai d'audiencement « de douze mois, contre deux mois à Paris » ; le département est « 3e contributeur national de la TVA » ; le rapport écrit aussi que « l'État surinvestit humainement et financièrement dans ce département » au titre des dispositifs prioritaires, sans résultats suffisants.",
  "Rapport parlementaire transpartisan (un député LR, un député LREM) ; données anciennes."))
PS_SSD = ('ps_ssd', src("Un rapport parlementaire dénonce une « République en échec » en Seine-Saint-Denis", "Public Sénat (Tiphaine Le Liboux)", "31 mai 2018",
  "https://www.publicsenat.fr/actualites/politique/un-rapport-parlementaire-denonce-une-republique-en-echec-en-seine-saint-denis",
  "Selon le rapporteur, l'établissement scolaire « le moins bien doté de Paris reste mieux doté que le plus doté de Seine-Saint-Denis » ; part d'enseignants néo-titulaires : 21 % en France, 65 % en Seine-Saint-Denis ; policiers « moins nombreux, mais aussi moins expérimentés » ; « à besoins équivalents, la Seine-Saint-Denis n'est pas traitée de manière équitable ».",
  "Média parlementaire.", 'media'))
INSEE_TERR = ('insee_terr', src("Niveau de vie et pauvreté des territoires en 2021 (Insee Résultats)", "Insee", "29 janvier 2024",
  "https://www.insee.fr/fr/statistiques/7752770",
  "Taux de pauvreté de la Seine-Saint-Denis en 2021 : 28,4 %, contre 15,3 % pour l'ensemble du champ (métropole, Martinique et La Réunion) ; la pauvreté est la plus élevée à la Martinique, en Seine-Saint-Denis et à La Réunion.",
  "Statistique publique de référence."))
CAF93 = ('caf93', src("Portrait social 2025", "Caf de la Seine-Saint-Denis", "2025 (données au 30 juin 2024)",
  "https://www.caf.fr/sites/default/files/medias/931/Professionnels-Documents/Publications/PortraitSocial2025-Caf93_V5.pdf",
  "388 621 allocataires ; « 979 000 habitants sont couverts par au moins une prestation légale », soit 58 % de la population ; 83 300 foyers au RSA ; « 22 % des allocataires ont la totalité de leurs ressources financières composées de prestations légales », contre 15 % au niveau national.",
  "Organisme public de sécurité sociale."))
MONTAIGNE_AUDIO = ('montaigne_audio', src("Privatiser l'audiovisuel public (chiffrage Législatives 2024, Rassemblement national)", "Institut Montaigne", "Juin 2024",
  "https://www.institutmontaigne.org/legislatives-2024/rassemblement-national/privatiser-laudiovisuel-public",
  "Dépense publique pour l'audiovisuel : 3,93 Md€ en 2024 ; l'Institut ne retient qu'environ 2 Md€ d'économies par an, à un horizon de 3 à 5 ans ; recette de cession retenue d'environ 1,5 Md€ en une fois, qui réduit la dette mais pas le déficit ; obstacles : loi nécessaire avec risque de censure constitutionnelle (liberté de communication), règlement européen 2024/1083 sur la liberté des médias, recettes publicitaires en baisse, coûts sociaux possibles à la charge de l'État.",
  "Think tank libéral, chiffrage indépendant des programmes.", 'etude'))
OZAP_AUDIO = ('ozap_audio', src("Sébastien Chenu confirme que le Rassemblement national privatisera l'audiovisuel public en cas de victoire du RN aux législatives", "Puremédias (L. Galtier Lloret)", "10 juin 2024",
  "https://www.ozap.com/actu/sebastien-chenu-confirme-que-le-rassemblement-national-privatisera-l-audiovisuel-public-en-cas-de-victoire-du-rn-aux-legislatives/644353",
  "Le vice-président du RN confirme la privatisation de l'audiovisuel public « dans le cadre d'un mandat » et chiffre le gain à « 3 milliards d'euros ».",
  "Média spécialisé dans les médias.", 'media'))
SENAT_AUDIO = ('senat_audio', src("Réforme du financement de l'audiovisuel public (synthèse du rapport n° 40, commission des finances)", "Sénat (Jean-Raymond Hugonet, rapporteur)", "16 octobre 2024",
  "https://www.senat.fr/rap/l24-040/l24-040-syn.pdf",
  "La contribution à l'audiovisuel public, supprimée en 2022, s'élevait à 138 euros en métropole ; l'audiovisuel public est désormais financé par une fraction de TVA, dont la loi de finances pour 2024 a fixé le montant à 4,026 milliards d'euros ; le règlement européen sur la liberté des médias exige des ressources financières « suffisantes, durables et prévisibles ».",
  "Rapport parlementaire (rapporteur LR)."))
MONTAIGNE_AUDIO22 = ('montaigne_audio22', src("Supprimer la redevance audiovisuelle grâce à la privatisation des principales chaînes de l'audiovisuel public (chiffrage Présidentielle 2022, Marine Le Pen)", "Institut Montaigne", "14 février 2022",
  "https://www.institutmontaigne.org/presidentielle-2022/marine-le-pen/supprimer-la-redevance-audiovisuelle-grace-a-la-privatisation-des-principales-chaines-de-laudiovisuel-public",
  "La candidate proposait de « privatiser l'audiovisuel public pour supprimer les 138€ de redevance » ; selon l'Institut, la cession rapporterait une recette ponctuelle qui « n'améliore pas le déficit public ».",
  "Think tank libéral, chiffrage indépendant des programmes.", 'etude'))
AN_AUDIO = ('an_audio', src("Avis n° 472 sur le projet de loi de finances pour 2025, tome I : Audiovisuel public", "Assemblée nationale, commission des affaires culturelles (Aymeric Caron, rapporteur), d'après l'UER", "23 octobre 2024",
  "https://www.assemblee-nationale.fr/dyn/17/rapports/cion-cedu/l17b0472-ti_rapport-avis.pdf",
  "Selon les données de l'Union européenne de radio-télévision (2022), la France a dépensé « 62 euros par an par habitant pour financer l'audiovisuel public », contre « 120 euros » au Royaume-Uni, « 121 euros » en Allemagne, « 91 euros » au Danemark et « 114 euros » en Autriche ; crédits 2025 : 4 029,16 M€.",
  "Rapport parlementaire (rapporteur LFI) citant l'UER."))

FICHES = []

# 1 ── AME ───────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='ame-cout-sans-papiers', affirmation="L'aide médicale d'État soigne gratuitement les clandestins et coûte une fortune.", volet='immigration', sous_theme='Immigration et aides sociales',
 mots_cles=['aide médicale d état', 'ame', 'aide medicale', 'clandestins', 'sans papiers', 'soins gratuits', 'soigne gratuitement', 'coûte une fortune'],
 verdict='trompeur', fiabilite='etabli',
 resume="L'AME existe et prend en charge les soins sans reste à charge, pour environ 465 000 personnes sans papiers. Elle coûte un peu plus d'un milliard d'euros par an. Mais elle est réservée aux personnes présentes depuis plus de trois mois avec moins de 862 € par mois, et la dépense par bénéficiaire (2 699 € en 2024) est plus faible que pour la population générale (3 659 €). La mission Évin-Stefanini n'a trouvé ni abus structurel ni « appel d'air ».",
 contexte="L'AME revient à chaque débat sur l'immigration : sa suppression ou sa transformation en simple « aide médicale d'urgence » est demandée par le RN et une partie de la droite.",
 explication="L'AME est une couverture santé de l'État pour les étrangers en situation irrégulière à faibles ressources. Elle n'est pas automatique : il faut prouver trois mois de présence et des revenus très bas. La hausse de son coût suit surtout celle du nombre de bénéficiaires, pas celle de la dépense par personne.",
 sources=[SENAT_AME, SENAT_AME_SYN, LCP_AME],
 faits=[
  fait("Selon le Sénat, les dépenses réelles de l'AME de droit commun atteignent 1,255 milliard d'euros en 2024, pour 465 208 bénéficiaires fin 2024.", 'senat_ame', '2024', 'France', "C'est une dépense réelle et en hausse : il faut le reconnaître.", 'etabli', '1,255 Md€'),
  fait("Selon le Sénat, la dépense moyenne par bénéficiaire de l'AME est de 2 699 € en 2024, contre 3 659 € pour la population générale en 2023.", 'senat_ame', '2023-2024', 'France', "Les bénéficiaires de l'AME ne consomment pas plus de soins que les autres, au contraire.", 'etabli', '2 699 €'),
  fait("Selon le Sénat, l'AME est réservée aux étrangers vivant en France depuis au moins trois mois consécutifs en situation irrégulière, avec des ressources d'au plus 862 € par mois en 2025.", 'senat_ame_syn', '2025', 'France', "L'accès est conditionné : ce n'est pas un guichet ouvert à toute personne qui arrive.", 'etabli', '862 €'),
  fait("Selon la mission Évin-Stefanini (2023), le dispositif ne présente pas d'abus ou de fraudes structurelles, n'est pas un facteur d'attractivité, et environ la moitié des personnes qui y auraient droit ne le demandent pas.", 'lcp_ame', '2023', 'France', "Le « tourisme médical » n'est pas démontré ; le non-recours est massif.", 'estimation', '50 %'),
  fait("Selon la mission Évin-Stefanini, la consommation trimestrielle moyenne de soins par bénéficiaire est passée de 642 € en 2009 à 604 € en 2022.", 'lcp_ame', '2009-2022', 'France', "La hausse du coût vient du nombre de bénéficiaires, pas d'une explosion de la dépense par personne.", 'etabli', '604 €'),
 ],
 court="Trompeur : l'AME coûte environ 1,3 milliard d'euros par an, mais elle est réservée aux personnes présentes depuis plus de trois mois avec moins de 862 € par mois, et chaque bénéficiaire coûte moins qu'un assuré moyen (2 699 € contre 3 659 €).",
 moyen="L'AME existe et elle coûte de l'argent : environ 1,3 milliard d'euros en 2024, pour 465 000 personnes. Mais ce n'est pas une porte ouverte : il faut prouver trois mois de présence et moins de 862 € de revenus par mois.\n\nEt les bénéficiaires ne surconsomment pas : 2 699 € de dépense par personne en 2024, contre 3 659 € pour l'ensemble de la population. La mission Évin-Stefanini, commandée par le gouvernement, n'a trouvé ni fraude structurelle ni « appel d'air ». La moitié des personnes qui y auraient droit ne la demandent même pas.",
 detaille="L'aide médicale d'État prend en charge les soins de personnes étrangères en situation irrégulière, sans reste à charge. Selon le Sénat, ses dépenses réelles atteignent 1,255 milliard d'euros en 2024 (1,39 milliard en comptant l'ensemble du dispositif), pour environ 465 000 bénéficiaires. Le nombre de bénéficiaires a environ doublé depuis 2011 : c'est la principale raison de la hausse du coût.\n\nL'accès est encadré : trois mois de présence ininterrompue et des ressources inférieures à 862 € par mois en 2025. La dépense par bénéficiaire, 2 699 € en 2024, est inférieure à celle de la population générale (3 659 € en 2023). La consommation trimestrielle de soins par personne a même légèrement baissé entre 2009 et 2022.\n\nLa mission Évin-Stefanini (2023) a jugé le dispositif « utile » et « globalement maîtrisé », sans abus structurel, et a estimé que l'AME n'attire pas les migrants. Elle a proposé des ajustements, comme l'accord préalable pour certains soins. Le rapporteur LR du Sénat juge au contraire le dispositif mal maîtrisé : le débat sur la gestion est légitime. Mais soigner tôt évite aussi des urgences plus coûteuses et des risques sanitaires pour tous.",
 empathie="Je comprends qu'on se demande pourquoi l'État paie les soins de gens qui n'ont pas de papiers, quand on attend soi-même un rendez-vous. Mais l'AME est très encadrée, elle coûte moins par personne que la Sécu pour chacun de nous, et soigner tôt protège aussi tout le monde.",
 legitimes=["Le coût de l'AME augmente (le nombre de bénéficiaires a environ doublé depuis 2011).", "Le rapporteur LR du Sénat juge le dispositif mal maîtrisé, et la mission Évin-Stefanini elle-même propose des ajustements."],
 contre=[
  ("Les sans-papiers ont droit à tout, gratuitement.", "Il faut trois mois de présence et moins de 862 € par mois ; certains soins peuvent être soumis à accord préalable selon les propositions de la mission."),
  ("Il suffit de la remplacer par l'aide médicale d'urgence.", "La mission Évin-Stefanini juge sévèrement ce système, avec un risque important de renoncement aux soins, qui finissent souvent aux urgences, plus chères."),
 ],
 questions=["Savais-tu qu'un bénéficiaire de l'AME coûte en moyenne moins qu'un assuré ordinaire ?", "Qu'est-ce qui coûte le plus cher : soigner une maladie tôt ou la traiter aux urgences ?"],
 limites=["Les chiffres sont ceux de rapports parlementaires et d'une mission gouvernementale ; ils divergent légèrement selon le périmètre (AME de droit commun ou dispositif complet).", "La part de l'AME dans l'ensemble des dépenses d'assurance maladie n'a pas pu être chiffrée à partir des sources lues."],
 publics={'convaincus': "Regarde les chiffres du Sénat, pas ceux des réseaux : un bénéficiaire de l'AME coûte 2 699 € par an, moins qu'un assuré ordinaire. Si c'était le paradis du soin gratuit, ce serait l'inverse. Et la moitié des gens qui y ont droit ne la demandent même pas : drôle d'aspirateur à migrants.",
  'indecis': "Ta question sur le coût est légitime : environ 1,3 milliard d'euros par an, en hausse. Mais l'accès est encadré (trois mois de présence, moins de 862 € par mois) et la mission Évin-Stefanini n'a trouvé ni fraude massive ni appel d'air. Soigner tôt, c'est aussi éviter les épidémies et les urgences saturées."},
 a_actualiser='2027-06-30',
))

# 2 ── ASPA ──────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='minimum-vieillesse-etrangers', affirmation="Les étrangers touchent le minimum vieillesse sans avoir jamais cotisé.", volet='immigration', sous_theme='Immigration et aides sociales',
 mots_cles=['minimum vieillesse', 'aspa', 'retraite des étrangers', 'sans avoir cotisé', 'jamais cotisé', 'allocation de solidarité aux personnes âgées', 'étrangers retraités'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le minimum vieillesse (ASPA) n'est pas une retraite : c'est une allocation de solidarité, accessible sans cotisation à tous, Français compris. Mais un étranger non européen doit détenir depuis au moins dix ans un titre de séjour autorisant à travailler, résider en France au moins neuf mois par an, et les sommes sont récupérables sur la succession au-delà de 107 616 €.",
 contexte="Des messages affirment que des étrangers arrivés récemment toucheraient une « retraite » sans avoir jamais travaillé en France.",
 explication="Le minimum vieillesse garantit un revenu minimal aux personnes âgées pauvres, qu'elles aient cotisé ou non. Ce n'est pas une pension de retraite, et ce n'est pas réservé aux étrangers. Pour eux, la loi ajoute une condition de dix ans de séjour régulier.",
 sources=[DREES_ASPA, AN_ASPA],
 faits=[
  fait("Selon la DREES, fin 2023, 723 000 personnes perçoivent le minimum vieillesse, dont 606 600 au titre de l'ASPA.", 'drees_aspa', '2023', 'France', "C'est une aide pour les personnes âgées pauvres, toutes nationalités confondues.", 'etabli', '723 000'),
  fait("Selon la DREES, un étranger hors Espace économique européen et Suisse doit détenir depuis au moins dix ans un titre de séjour autorisant à travailler pour demander l'ASPA, et tout bénéficiaire doit résider en France au moins neuf mois par an.", 'drees_aspa', '2025', 'France', "On ne peut pas arriver en France à 65 ans et toucher l'ASPA.", 'etabli', '10 ans'),
  fait("Selon la DREES, les sommes versées sont récupérables sur la succession lorsque l'actif net dépasse 107 616 euros en métropole.", 'drees_aspa', '2025', 'France', "C'est une avance de solidarité, en partie récupérée.", 'etabli', '107 616 €'),
  fait("Selon le ministère des Solidarités, il n'existe pas de statistique de nationalité sur l'ensemble des allocataires ; en 2018, 154 900 bénéficiaires sur 396 100 interrogés par l'enquête BMS étaient nés à l'étranger (ce qui inclut des Français).", 'an_aspa', '2018', 'France', "Une partie importante des bénéficiaires est née à l'étranger, souvent après une vie de travail mal déclaré ou mal payé.", 'etabli', '154 900'),
 ],
 court="Trompeur : l'ASPA n'est pas une retraite, c'est une aide pour toutes les personnes âgées pauvres, Français compris. Un étranger hors UE doit avoir eu dix ans de titre de séjour avec droit au travail, vivre en France neuf mois par an, et l'aide est récupérable sur l'héritage.",
 moyen="Le minimum vieillesse n'est pas une retraite : c'est une aide de solidarité pour les personnes âgées pauvres, qui ne demande pas d'avoir cotisé. C'est vrai pour un Français comme pour un étranger.\n\nMais pour un étranger hors UE, la loi exige dix ans de titre de séjour autorisant à travailler. Il faut résider en France au moins neuf mois par an, et l'État récupère les sommes sur la succession au-delà de 107 616 €. On ne peut donc pas arriver à 65 ans et toucher l'ASPA.",
 detaille="L'allocation de solidarité aux personnes âgées (ASPA) garantit un revenu minimal, au plus 1 034,28 € par mois pour une personne seule en 2025, après déduction des autres ressources. Fin 2023, 723 000 personnes touchaient le minimum vieillesse selon la DREES.\n\nC'est une prestation non contributive : un Français qui n'a jamais cotisé peut aussi la toucher. Pour les étrangers non européens, la loi est plus stricte : dix ans de titre de séjour autorisant à travailler, sauf pour les réfugiés et apatrides. Tout bénéficiaire doit résider en France au moins neuf mois par an, et les sommes versées sont récupérables sur la succession au-delà de 107 616 €.\n\nIl n'existe pas de chiffre global récent sur la nationalité des allocataires. En 2018, environ 155 000 bénéficiaires sur 396 000 interrogés étaient nés à l'étranger, ce qui inclut des Français. Beaucoup sont d'anciens travailleurs immigrés aux carrières incomplètes ou mal déclarées.",
 empathie="Je comprends que ça choque l'idée qu'on puisse toucher sans avoir cotisé. Mais c'est le principe même du minimum vieillesse, pour tout le monde : éviter qu'une personne âgée vive dans la misère. Et pour les étrangers, il faut déjà dix ans de séjour régulier.",
 legitimes=["L'ASPA est effectivement non contributive : on peut la toucher sans avoir cotisé.", "Une part importante des bénéficiaires est née à l'étranger."],
 contre=[
  ("Ils arrivent à 65 ans et touchent tout de suite.", "C'est impossible pour un étranger hors UE : il faut dix ans de titre de séjour autorisant à travailler (hors réfugiés et apatrides)."),
  ("Ils repartent au pays avec l'argent.", "Il faut résider en France au moins neuf mois par an pour garder l'ASPA."),
 ],
 questions=["Savais-tu que le minimum vieillesse est aussi versé à des Français qui n'ont jamais cotisé ?", "Qui sont, selon toi, les vieux travailleurs immigrés qui touchent l'ASPA aujourd'hui ?"],
 limites=["Il n'existe pas de statistique récente sur la nationalité de l'ensemble des allocataires.", "Les données sur le lieu de naissance datent de 2018."],
 publics={'convaincus': "Si un étranger pouvait débarquer à 65 ans et toucher le minimum vieillesse, je serais d'accord pour dire que c'est un scandale. Mais la loi exige dix ans de séjour régulier avec droit au travail, neuf mois par an en France, et l'argent est repris sur l'héritage. Ceux qui le touchent sont surtout de vieux travailleurs aux carrières mal déclarées.",
  'indecis': "Le minimum vieillesse n'est pas une retraite : c'est un filet de sécurité pour toutes les personnes âgées pauvres, Français compris. Pour les étrangers non européens, il faut dix ans de séjour régulier. Il est normal de vouloir des règles strictes : elles existent déjà."},
 a_actualiser='2027-06-30',
))

# 3 ── MNA ───────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='mineurs-isoles-age', affirmation="Les mineurs étrangers isolés sont pour la plupart des majeurs qui mentent sur leur âge.", volet='immigration', sous_theme='Réfugiés et statuts administratifs',
 mots_cles=['mineurs non accompagnés', 'mna', 'mineurs isolés', 'faux mineurs', 'mentent sur leur âge', 'tests osseux', 'évaluation de minorité', 'majeurs'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Une majorité des jeunes qui se présentent comme mineurs isolés ne sont pas reconnus comme tels par les départements (taux d'acceptation de 30 à 40 % en 2017). Mais un refus ne prouve ni la majorité ni un mensonge : les évaluations varient selon les départements, les tests osseux ne distinguent pas 16 de 18 ans, et aucune statistique fiable ne permet d'affirmer que « la plupart mentent ».",
 contexte="L'expression « faux mineurs » circule après des faits divers impliquant de jeunes étrangers, pour mettre en doute l'ensemble des mineurs isolés pris en charge par l'aide sociale à l'enfance.",
 explication="Un jeune qui se dit mineur et isolé est évalué par le département. Un refus signifie que l'évaluation n'a pas retenu la minorité, pas que la personne a menti : beaucoup n'ont pas de papiers fiables, et les méthodes d'évaluation sont imprécises.",
 sources=[LOCALTIS_MNA, CC_MNA, ACADMED_MNA, DDD_MNA],
 faits=[
  fait("Selon le secrétaire d'État chargé de l'enfance (cité au Sénat), en 2017, 44 000 jeunes se sont déclarés mineurs non accompagnés et 14 000 ont été reconnus comme tels, soit un taux d'acceptation de 30 à 40 %.", 'localtis_mna', '2017', 'France', "Une majorité des demandes est refusée : c'est un fait.", 'etabli', '44 000'),
  fait("Selon le Conseil constitutionnel, les examens osseux comportent autour de 18 ans une marge d'erreur de 18 à 24 mois ; ils ne peuvent être l'unique fondement de la détermination de l'âge, et le doute doit profiter à la minorité.", 'cc_mna', '2019', 'France', "Il n'existe pas de test fiable pour démasquer un « faux mineur ».", 'etabli', '18 à 24 mois'),
  fait("Selon l'Académie nationale de médecine, la méthode radiologique de référence « ne permet pas de distinction nette entre seize et dix-huit ans ».", 'acadmed_mna', '2007', 'France', "Un jeune de 16 ans peut être déclaré majeur à tort.", 'etabli'),
  fait("Selon le Défenseur des droits, l'évaluation de la minorité est parfois entachée de représentations négatives, varie grandement d'un département à l'autre, et il n'existe pas de chiffres consolidés et fiables.", 'ddd_mna', '2022', 'France', "Les refus dépendent aussi du département, pas seulement de l'âge réel.", 'interpretation'),
 ],
 court="Trompeur : une majorité des jeunes évalués ne sont pas reconnus mineurs, mais un refus ne prouve pas un mensonge. Les tests osseux ne distinguent pas 16 de 18 ans (Académie de médecine), et le Conseil constitutionnel impose que le doute profite à la minorité.",
 moyen="Il est vrai que la plupart des jeunes qui se présentent ne sont pas reconnus mineurs : en 2017, 14 000 sur 44 000. Mais un refus du département ne veut pas dire que le jeune a menti.\n\nBeaucoup n'ont pas d'état civil fiable, et les méthodes d'évaluation sont imprécises : l'Académie de médecine explique que les radios ne distinguent pas 16 de 18 ans. Le Défenseur des droits constate que les résultats varient beaucoup d'un département à l'autre. Dire que « la plupart mentent », c'est transformer une incertitude administrative en accusation.",
 detaille="Les mineurs non accompagnés relèvent de la protection de l'enfance, confiée aux départements. Chaque jeune qui se déclare mineur et isolé est évalué. En 2017, selon le Gouvernement, 44 000 jeunes ont été évalués et 14 000 reconnus mineurs, soit un taux d'acceptation de 30 à 40 %.\n\nUn refus n'établit pas la majorité. Le Conseil constitutionnel relève que les examens osseux ont une marge d'erreur de 18 à 24 mois autour de 18 ans, qu'ils ne peuvent suffire à déterminer l'âge, et que le doute doit profiter à la minorité. L'Académie nationale de médecine indique qu'ils ne distinguent pas nettement 16 et 18 ans. Le Défenseur des droits constate des pratiques très variables entre départements et l'absence de chiffres consolidés.\n\nIl peut exister des fraudes sur l'âge. Mais aucune donnée fiable ne permet de dire que la plupart des jeunes mentent. L'accusation générale vise des enfants qui, s'ils sont mineurs, ont droit à la protection de l'enfance comme tout enfant.",
 empathie="Je comprends le doute quand on voit à la télé un « mineur » qui paraît plus âgé. Mais personne ne sait mesurer l'âge précisément, même les médecins. Si on se trompe, on laisse à la rue un enfant de 16 ans : c'est pour ça que la loi dit que le doute doit lui profiter.",
 legitimes=["Une majorité des jeunes évalués n'est pas reconnue mineure par les départements.", "Des fraudes sur l'âge peuvent exister, et la prise en charge pèse sur les départements."],
 contre=[
  ("Il suffit de faire des tests osseux.", "Ils ont une marge d'erreur de 18 à 24 mois autour de 18 ans et ne peuvent légalement suffire à eux seuls."),
  ("Puisqu'ils sont refusés, c'est qu'ils mentaient.", "Un refus traduit une évaluation incertaine, variable selon les départements, pas une preuve de mensonge."),
 ],
 questions=["Comment ferais-tu, toi, pour prouver ton âge sans papiers ?", "Si on se trompe dans un sens ou dans l'autre, quelle erreur est la plus grave : protéger un jeune adulte ou laisser à la rue un enfant ?"],
 limites=["Les chiffres d'évaluation datent de 2017 ; aucune statistique nationale récente et consolidée n'a pu être lue.", "Le nombre de jeunes reconnus mineurs après recours devant le juge n'est pas connu."],
 publics={'convaincus': "D'accord, beaucoup de jeunes ne sont pas reconnus mineurs. Mais refusé ne veut pas dire menteur : même l'Académie de médecine dit qu'on ne sait pas distinguer 16 et 18 ans à la radio. Accuser tout le monde de mentir, c'est accepter de mettre des enfants à la rue sur un coup de dés.",
  'indecis': "Le doute sur l'âge est compréhensible, et une majorité des demandes est refusée. Mais il n'existe aucune méthode fiable pour mesurer l'âge, et les évaluations varient d'un département à l'autre. C'est pour cela que le Conseil constitutionnel exige que le doute profite au mineur."},
 a_actualiser='2027-06-30',
))

# 4 ── Préférence nationale ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='preference-nationale-constitution', affirmation="La préférence nationale, il suffit d'une loi pour l'appliquer.", volet='immigration', sous_theme='Nationalité et accès aux droits',
 mots_cles=['préférence nationale', 'priorité nationale', 'constitution', 'conseil constitutionnel', 'il suffit d une loi', 'référendum', 'protection sociale des étrangers'],
 verdict='contredit', fiabilite='etabli',
 resume="Non. Depuis 1993, le Conseil constitutionnel juge que les étrangers en séjour stable et régulier ont droit à la protection sociale. En avril 2024, il a encore rejeté une proposition de référendum qui conditionnait des prestations à cinq ans de séjour. Une « préférence nationale » générale exigerait de réviser la Constitution, et se heurterait aussi aux engagements européens.",
 contexte="La « préférence » ou « priorité nationale » pour l'emploi, le logement et les aides est une proposition historique du FN puis du RN, présentée comme une simple question de volonté politique.",
 explication="Une loi ordinaire doit respecter la Constitution, qui protège l'égalité devant la loi et le droit à la protection sociale de ceux qui résident régulièrement en France. Le législateur peut fixer des conditions de durée de séjour raisonnables, mais pas exclure les étrangers en règle par principe.",
 sources=[CC_1993, CDJ_RIP, PS_REF_LP],
 faits=[
  fait("Selon la décision n° 93-325 DC du Conseil constitutionnel, « les étrangers jouissent des droits à la protection sociale, dès lors qu'ils résident de manière stable et régulière sur le territoire français ».", 'cc_1993', '1993', 'France', "Le principe est constitutionnel depuis plus de trente ans.", 'etabli'),
  fait("Selon une analyse du Club des juristes, le 11 avril 2024, le Conseil constitutionnel a rejeté une proposition de référendum conditionnant des prestations à 5 ans de séjour régulier ou 30 mois d'affiliation, jugeant ces durées disproportionnées ; une condition de durée raisonnable reste possible.", 'cdj_rip', '2024', 'France', "Même une version atténuée de la préférence nationale a été censurée.", 'etabli', '5 ans'),
  fait("Selon le constitutionnaliste Dominique Rousseau (Public Sénat, 2021), la priorité nationale ne peut pas passer par le référendum de l'article 11 : il faudrait d'abord réviser la Constitution par l'article 89, avec un vote identique des deux assemblées.", 'ps_ref_lp', '2021', 'France', "Le chemin juridique est long et passe par le Parlement entier.", 'interpretation'),
 ],
 court="Faux : depuis 1993, le Conseil constitutionnel protège le droit des étrangers en séjour régulier à la protection sociale, et il a encore censuré en avril 2024 une condition de cinq ans de séjour. Il faudrait réviser la Constitution.",
 moyen="Une loi ne peut pas faire ce que la Constitution interdit. Depuis 1993, le Conseil constitutionnel juge que les étrangers qui résident de façon stable et régulière ont droit à la protection sociale.\n\nEn avril 2024, il a même rejeté un projet de référendum qui exigeait cinq ans de séjour pour certaines aides. Une préférence nationale générale supposerait donc de réviser la Constitution, avec l'accord des deux assemblées, puis d'affronter le droit européen.",
 detaille="La « préférence nationale » consiste à réserver en priorité aux Français l'emploi, le logement social ou les prestations. Elle se heurte au bloc de constitutionnalité. Dans sa décision de 1993, le Conseil constitutionnel a jugé que le législateur, s'il peut prévoir des règles spécifiques pour les étrangers, doit respecter les droits fondamentaux de tous ceux qui résident sur le territoire, dont la protection sociale pour ceux qui y résident de manière stable et régulière.\n\nLe 11 avril 2024, il a rejeté une proposition de loi référendaire qui conditionnait certaines prestations à cinq ans de séjour régulier ou trente mois d'affiliation, jugeant ces durées disproportionnées. Une condition de durée raisonnable reste possible : le débat porte sur le curseur, pas sur l'exclusion.\n\nSelon des constitutionnalistes, la priorité nationale ne peut pas être imposée par le référendum de l'article 11 : il faudrait réviser la Constitution par l'article 89, ce qui suppose un vote identique de l'Assemblée et du Sénat. Elle entrerait aussi en conflit avec des traités européens. Ce n'est donc pas « une simple loi » : c'est un changement de régime des droits.",
 empathie="Je comprends l'envie que l'État s'occupe d'abord de ses citoyens. Mais en France, les droits sociaux sont liés au fait de vivre et de travailler ici légalement, pas à la nationalité. Changer ça, ce n'est pas une petite loi : c'est toucher à la Constitution.",
 legitimes=["Le législateur peut fixer des conditions de durée de résidence raisonnables pour certaines prestations.", "Une révision constitutionnelle est juridiquement possible si le Parlement l'adopte."],
 contre=[
  ("Il suffit d'un référendum.", "Selon des constitutionnalistes, l'article 11 ne permet pas un référendum sur ce sujet ; il faut d'abord réviser la Constitution par l'article 89."),
  ("Le Conseil constitutionnel n'a pas à décider à la place du peuple.", "Il applique une Constitution adoptée par le peuple en 1958, qui protège les droits de tous ceux qui vivent légalement ici."),
 ],
 questions=["Si une loi pouvait retirer des droits à une catégorie de personnes en règle, qui serait la prochaine ?", "Sais-tu ce qu'a décidé le Conseil constitutionnel en avril 2024 ?"],
 limites=["Une révision constitutionnelle pourrait changer l'état du droit ; la fiche décrit le droit en vigueur.", "Les obstacles liés au droit européen ne sont pas détaillés ici."],
 publics={'convaincus': "Admettons qu'on veuille la préférence nationale : il faut le dire franchement, ça ne se fait pas par une loi. Le Conseil constitutionnel l'a encore refusé en 2024, même pour une version adoucie. Ceux qui promettent de l'appliquer vite te vendent soit un mensonge, soit une réforme de la Constitution qui toucherait aux droits de tous.",
  'indecis': "La question « les Français d'abord » peut sembler de bon sens. Mais aujourd'hui, les droits sociaux reposent sur le séjour légal et le travail, et la Constitution protège ce principe depuis 1993. Le changer demanderait une révision de la Constitution, pas une simple loi."},
 stabilite='evolutive', a_actualiser='2027-06-30',
))

# 5 ── LFI et régularisation ─────────────────────────────────────────────────
FICHES.append(fiche(
 id='lfi-regulariser-sans-papiers', affirmation="La France insoumise veut régulariser tous les sans-papiers.", volet='politique', sous_theme='France insoumise',
 mots_cles=['régulariser', 'régularisation', 'sans papiers', 'tous les sans papiers', 'lfi', 'france insoumise', 'nfp', 'régularisation massive'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le programme du Nouveau Front populaire (2024) propose de « régulariser les travailleurs, étudiants, parents d'enfants scolarisés », et les députés LFI ont défendu la régularisation de tous les travailleurs sans papiers. C'est bien plus large qu'aujourd'hui, mais ce n'est pas une régularisation de tous, sans condition. En 2025, 28 610 personnes ont été régularisées.",
 contexte="L'accusation de vouloir « régulariser tout le monde » est souvent opposée à LFI et au NFP pour résumer leur programme sur l'immigration.",
 explication="Une régularisation consiste à donner un titre de séjour à une personne déjà présente sans papiers. Elle peut être générale ou réservée à certaines catégories (travailleurs, familles, étudiants). Le programme de la gauche choisit des catégories larges, liées au travail, aux études et aux enfants.",
 sources=[NFP_PROG, AN_CL737, PS_REGUL],
 faits=[
  fait("Selon le programme du Nouveau Front populaire (juin 2024), la coalition propose de « régulariser les travailleurs, étudiants, parents d'enfants scolarisés » et d'instituer la carte de séjour de dix ans comme titre de référence.", 'nfp_prog', '2024', 'France', "La proposition est large, mais elle vise des catégories, pas « tout le monde ».", 'etabli'),
  fait("Selon un amendement déposé par des députés LFI en novembre 2023, leur programme prévoit de « régulariser tous les travailleurs et travailleuses sans-papiers », avec un titre de séjour de plein droit sur preuve du travail.", 'an_cl737', '2023', 'France', "La régularisation est liée au travail : il faut le dire clairement.", 'etabli'),
  fait("Selon les chiffres de la direction générale des étrangers en France (Public Sénat), 28 610 étrangers ont été régularisés en 2025, en baisse de 10,1 %.", 'ps_regul', '2025', 'France', "La régularisation existe déjà au cas par cas ; la gauche propose de l'élargir.", 'etabli', '28 610'),
 ],
 court="Exagéré : le programme du NFP propose de régulariser les travailleurs, les étudiants et les parents d'enfants scolarisés, et LFI défend la régularisation de tous les travailleurs sans papiers. C'est beaucoup plus qu'aujourd'hui, mais pas « tous, sans condition ».",
 moyen="Il faut être honnête : LFI et le NFP veulent régulariser beaucoup plus qu'aujourd'hui. Le programme de 2024 cite les travailleurs, les étudiants et les parents d'enfants scolarisés, et les députés LFI défendent un titre de séjour de plein droit pour les travailleurs sans papiers.\n\nMais ce n'est pas « régulariser tout le monde » : la logique est celle du travail, des études et des enfants. L'argument de gauche est simple : un travailleur sans papiers est un travailleur sans droits, donc sous-payé, ce qui tire tout le monde vers le bas.",
 detaille="Le programme du Nouveau Front populaire de juin 2024 propose de « faciliter l'accès aux visas, régulariser les travailleurs, étudiants, parents d'enfants scolarisés », de faire de la carte de séjour de dix ans le titre de référence et d'abroger les lois immigration récentes. En 2023, des députés LFI ont défendu par amendement un titre de séjour de plein droit pour tous les travailleurs sans papiers, sur preuve de leur activité.\n\nC'est une rupture avec la politique actuelle : en 2025, selon le ministère de l'Intérieur, 28 610 personnes ont été régularisées, un chiffre en baisse après le durcissement des critères. Mais aucun texte lu ne propose de régulariser toutes les personnes sans papiers sans condition.\n\nLe débat est légitime : on peut contester l'ampleur de ces régularisations. Il doit porter sur ce qui est réellement proposé, et sur ses raisons : des centaines de milliers de personnes travaillent déjà, sans droits, dans le bâtiment, la restauration ou l'aide à domicile.",
 empathie="Je comprends que l'idée de régularisations fasse peur, on a l'impression qu'on ouvre les vannes. Mais ce que propose la gauche, c'est de donner des papiers à des gens qui travaillent déjà ici, souvent dans des métiers dont on a besoin, pour qu'ils ne soient plus exploités.",
 legitimes=["La gauche propose bien des régularisations beaucoup plus larges qu'aujourd'hui.", "On peut débattre des effets d'une régularisation large sur les flux migratoires."],
 contre=[
  ("Régulariser, c'est créer un appel d'air.", "La proposition vise des personnes déjà présentes et qui travaillent ; elle s'accompagne dans le programme d'autres mesures sur l'accueil, à juger sur pièces."),
  ("Tous les sans-papiers diront qu'ils travaillent.", "Le texte des députés LFI prévoit d'établir l'exercice professionnel : c'est une condition, pas une régularisation automatique."),
 ],
 questions=["As-tu lu ce que dit vraiment le programme sur la régularisation ?", "Un travailleur sans papiers, à qui profite le fait qu'il n'ait aucun droit ?"],
 limites=["Les programmes peuvent évoluer ; la fiche décrit le programme du NFP de 2024 et des positions LFI de 2023.", "Le nombre de personnes concernées par la proposition n'est pas chiffré dans les sources lues."],
 publics={'convaincus': "Tu peux être contre, c'est ton droit, mais critique ce qui est vraiment proposé : régulariser les gens qui travaillent, étudient ou ont des enfants à l'école, pas « tout le monde ». Et pose-toi la question : un sans-papiers qui travaille au noir, ça arrange surtout le patron qui le paie mal.",
  'indecis': "La gauche propose en effet plus de régularisations, pour des personnes qui travaillent déjà ici, des étudiants et des parents d'enfants scolarisés. C'est un vrai choix politique, qu'on peut discuter. Mais ce n'est pas « régulariser tout le monde » : ce sont des catégories précises."},
 a_actualiser='2027-06-30',
))

# 6 ── Contribution à l'UE ───────────────────────────────────────────────────
FICHES.append(fiche(
 id='france-contributeur-net-ue', affirmation="La France paie beaucoup plus à l'Union européenne qu'elle ne reçoit.", volet='politique', sous_theme='Union européenne',
 mots_cles=['contributeur net', 'budget européen', 'union européenne', 'ue', 'bruxelles', 'paie plus qu elle ne reçoit', 'contribution de la france', 'pac'],
 verdict='trompeur', fiabilite='etabli',
 resume="La France est bien contributrice nette au budget européen : environ 8 milliards d'euros par an hors plan de relance, deuxième contributeur net en 2023 (9,3 milliards). Mais en comptant le plan de relance, le solde tombe à environ 0,1 % du PIB, la France est la première bénéficiaire en volume (notamment de la PAC), et le marché unique lui rapporte bien plus : environ 3,4 % de PIB selon le CEPII.",
 contexte="L'argument du « chèque à Bruxelles » est utilisé pour plaider la baisse de la contribution française, voire la sortie de l'Union.",
 explication="Le solde net compare ce qu'un pays verse au budget européen et ce que l'Union dépense chez lui. Il ne compte pas les gains économiques du marché unique (commerce, investissements), qui ne passent pas par le budget.",
 sources=[SENAT_UE, TLE_UE, CEPII_UE],
 faits=[
  fait("Selon le Sénat, en 2023, la France était le deuxième contributeur net au budget de l'UE, avec un solde estimé à -9,333 milliards d'euros, derrière l'Allemagne (-19,8 milliards).", 'senat_ue', '2023', 'France et UE', "La France verse plus qu'elle ne reçoit : c'est exact.", 'etabli', '9,3 Md€'),
  fait("Selon le Sénat, la France est le premier bénéficiaire en volume des dépenses de l'UE, mais seulement 22e par habitant (242 euros) en 2023.", 'senat_ue', '2023', 'France et UE', "L'Europe dépense beaucoup en France, notamment pour l'agriculture.", 'etabli', '242 €'),
  fait("Selon Toute l'Europe, la contribution française est d'environ 24 milliards d'euros par an de 2021 à 2025, pour environ 16 milliards dépensés en France ; avec le plan de relance, le solde net tombe à environ 3 milliards par an, soit 0,1 % du PIB.", 'tle_ue', '2021-2025', 'France', "Le coût net est réel, mais faible rapporté à la richesse du pays.", 'estimation', '0,1 %'),
  fait("Selon le CEPII, l'intégration commerciale européenne a augmenté le PIB réel de la France de 3,4 %, et un retour en arrière entraînerait une perte symétrique.", 'cepii_ue', '2018', 'France', "Le gain du marché unique dépasse de loin le solde budgétaire.", 'estimation', '3,4 %'),
 ],
 court="Exact mais trompeur : la France est contributrice nette (environ 8 milliards par an hors plan de relance), mais avec le plan de relance le solde tombe à environ 0,1 % du PIB, elle est la première bénéficiaire en volume, et le marché unique lui rapporterait environ 3,4 % de PIB (CEPII).",
 moyen="Oui, la France verse plus au budget européen qu'elle ne reçoit : environ 24 milliards par an pour 16 milliards dépensés chez elle. Elle était le deuxième contributeur net en 2023.\n\nMais il faut regarder l'ensemble : la France est la première bénéficiaire en volume, notamment de la politique agricole, et le solde net, en comptant le plan de relance, ne représente qu'environ 0,1 % du PIB. Surtout, le marché unique augmente le PIB français d'environ 3,4 % selon le CEPII, soit bien plus que le chèque net.",
 detaille="Selon le Sénat, le prélèvement au profit du budget européen atteint 23,3 milliards d'euros pour 2025, et elle était en 2023 le deuxième contributeur net, avec un solde de -9,3 milliards, derrière l'Allemagne. Toute l'Europe estime le solde à environ 8 milliards par an hors plan de relance, et à environ 3 milliards par an (0,1 % du PIB) en comptant les subventions du plan de relance, qui prend fin en 2027.\n\nLa France est aussi la première bénéficiaire en volume des dépenses européennes, notamment de la PAC, même si elle n'est que 22e par habitant. Une partie de l'argent versé aux autres pays revient à des entreprises françaises qui remportent des marchés.\n\nLe solde budgétaire ne mesure pas l'essentiel : selon le CEPII, l'intégration commerciale européenne a augmenté le PIB réel de la France d'environ 3,4 %. On peut critiquer les politiques européennes, notamment leur orientation libérale ; mais réduire l'Union à un « chèque » donne une image fausse du bilan.",
 empathie="Je comprends l'impression de payer pour les autres. Le solde est réel. Mais nos agriculteurs touchent beaucoup d'argent européen, et nos entreprises vendent librement dans toute l'Europe : si on fait le compte complet, la France y gagne.",
 legitimes=["La France est effectivement contributrice nette au budget européen, et sa contribution augmente.", "On peut critiquer l'orientation des politiques européennes, indépendamment du solde budgétaire."],
 contre=[
  ("Avec ces milliards, on pourrait financer nos hôpitaux.", "Le solde net, d'environ 8 milliards par an hors plan de relance, pèse peu face au marché unique, qui augmenterait le PIB d'environ 3,4 % selon le CEPII : sortir coûterait plus cher que ça ne rapporterait."),
  ("L'argent part chez les autres pays.", "Une partie revient à des entreprises françaises qui remportent des contrats financés par l'Europe, et la France est la première bénéficiaire en volume."),
 ],
 questions=["Sais-tu combien la politique agricole commune rapporte aux agriculteurs français ?", "Si on sortait du marché unique, combien pèserait ce chèque face aux pertes de nos exportateurs ?"],
 limites=["L'estimation du CEPII date de 2018 et repose sur un modèle.", "Le solde varie selon l'année et le périmètre retenu (avec ou sans plan de relance)."],
 publics={'convaincus': "Oui, la France paie plus qu'elle ne reçoit, je ne vais pas te dire le contraire. Mais compare : environ 8 milliards de solde d'un côté, et selon le CEPII un marché unique qui augmente notre PIB d'environ 3,4 % de l'autre. Si on veut changer l'Europe, il faut changer ses politiques, pas croire qu'on s'enrichirait en partant.",
  'indecis': "Le solde net est réel : la France est le deuxième contributeur net. Mais elle est aussi la première bénéficiaire en volume, surtout grâce à la PAC, et elle gagne beaucoup au marché unique. La vraie question est ce que finance le budget européen, pas seulement combien il coûte."},
 a_actualiser='2027-06-30',
))

# 7 ── Impôts des entreprises ────────────────────────────────────────────────
FICHES.append(fiche(
 id='impots-entreprises-europe', affirmation="Les entreprises françaises paient les impôts les plus élevés d'Europe.", volet='economie', sous_theme='Fiscalité',
 mots_cles=['impôt sur les sociétés', 'impots des entreprises', 'entreprises surtaxées', 'les plus élevés d europe', 'impôts de production', 'is', 'charges des entreprises', 'aides aux entreprises'],
 verdict='trompeur', fiabilite='etabli',
 resume="Plus vrai aujourd'hui pour l'impôt sur les bénéfices : son taux normal est de 25 % depuis 2022 (25,8 % avec la contribution sociale), proche de la moyenne européenne et sous Malte, le Portugal ou l'Allemagne. Les impôts de production restent plus élevés qu'ailleurs (3,8 % du PIB en 2021). Mais les entreprises reçoivent aussi au moins 211 milliards d'euros d'aides publiques par an, selon le Sénat.",
 contexte="L'argument est utilisé contre toute hausse de la fiscalité des entreprises, au nom de la compétitivité.",
 explication="Les entreprises paient plusieurs types de prélèvements : l'impôt sur les bénéfices, les impôts de production (sur le chiffre d'affaires ou les locaux), et les cotisations sociales. Il faut aussi compter ce qu'elles reçoivent : exonérations de cotisations, crédits d'impôt, subventions.",
 sources=[TLE_IS, TLE_IS21, MONTAIGNE_PROD, PS_AIDES],
 faits=[
  fait("Selon Toute l'Europe, le taux légal de l'impôt sur les sociétés en France est de 25,8 % avec la contribution sociale, légèrement au-dessus de la moyenne européenne, et inférieur à ceux de Malte (35 %), du Portugal (31,5 %) et de l'Allemagne (29,8 %).", 'tle_is', '2023', 'Union européenne', "La France n'a plus le taux d'impôt sur les bénéfices le plus élevé d'Europe.", 'etabli', '25,8 %'),
  fait("Selon Toute l'Europe, en 2019, avant la baisse du taux légal de 33 % à 25 %, la France avait le taux effectif moyen d'impôt sur les sociétés le plus élevé d'Europe (30,3 %).", 'tle_is21', '2019', 'Europe', "L'affirmation était vraie il y a quelques années : elle ne l'est plus pour l'impôt sur les bénéfices.", 'etabli', '30,3 %'),
  fait("Selon Toute l'Europe, la France est le deuxième pays au monde où le taux légal de l'impôt sur les sociétés a le plus baissé entre 2021 et 2022.", 'tle_is', '2021-2022', 'Monde', "L'impôt sur les bénéfices a été fortement réduit ces dernières années.", 'etabli'),
  fait("Selon l'Institut Montaigne, les impôts de production représentaient en France 3,8 % du PIB en 2021 (95 milliards d'euros), contre 2,5 % en moyenne dans les 11 pays étudiés.", 'montaigne_prod', '2021', 'Europe', "Sur les impôts de production, la France reste plus élevée que ses voisins.", 'etabli', '3,8 %'),
  fait("Selon la commission d'enquête du Sénat, les aides publiques aux entreprises atteignaient au moins 211 milliards d'euros en 2023, dont environ 80 milliards d'allègements de cotisations et 43 milliards de dépenses fiscales.", 'ps_aides', '2023', 'France', "Les prélèvements sur les entreprises sont en partie compensés par des aides massives.", 'estimation', '211 Md€'),
 ],
 court="Trompeur : l'impôt sur les bénéfices est de 25 % depuis 2022, dans la moyenne européenne. Les impôts de production restent élevés, mais les entreprises reçoivent au moins 211 milliards d'euros d'aides publiques par an (Sénat).",
 moyen="Ce n'est plus vrai pour l'impôt sur les bénéfices : son taux est passé à 25 % en 2022 (25,8 % avec la contribution sociale), proche de la moyenne européenne et en dessous de l'Allemagne ou du Portugal.\n\nLes impôts de production restent plus lourds qu'ailleurs, c'est vrai. Mais il faut faire le compte complet : selon une commission d'enquête du Sénat, adoptée à l'unanimité, les entreprises ont reçu au moins 211 milliards d'euros d'aides publiques en 2023, dont 80 milliards d'exonérations de cotisations.",
 detaille="En 2019, la France avait encore le taux effectif d'impôt sur les sociétés le plus élevé d'Europe (30,3 %). Ce n'est plus le cas : le taux normal est de 25 % depuis 2022, 25,8 % avec la contribution sociale, proche de la moyenne européenne. Malte (35 %), le Portugal (31,5 %) et l'Allemagne (29,8 % avec la fiscalité locale) font plus. La France est le deuxième pays au monde où ce taux a le plus baissé entre 2021 et 2022.\n\nLes impôts de production, qui pèsent sur l'activité indépendamment des bénéfices, restent plus élevés qu'ailleurs : 3,8 % du PIB en 2021 contre 2,5 % en moyenne dans les pays étudiés par l'Institut Montaigne, même s'ils ont baissé.\n\nMais l'argent circule dans les deux sens : selon la commission d'enquête du Sénat, les aides publiques aux entreprises atteignaient au moins 211 milliards d'euros en 2023, dont 80 milliards d'allègements de cotisations et 43 milliards de niches fiscales. La vraie question est l'efficacité de ces aides et leur contrepartie en emplois et en salaires.",
 empathie="Je comprends que les chefs d'entreprise aient l'impression d'être étranglés, surtout les petits. Mais l'impôt sur les bénéfices a beaucoup baissé, et les grandes entreprises reçoivent énormément d'aides publiques : la question, c'est de savoir à qui elles profitent.",
 legitimes=["Les impôts de production restent plus élevés en France que chez ses voisins.", "Les cotisations sociales patronales sont importantes, même après les allègements."],
 contre=[
  ("Avec ces impôts, les entreprises vont partir.", "Le taux d'impôt sur les bénéfices est désormais dans la moyenne européenne, et les aides publiques dépassent 200 milliards d'euros par an."),
  ("Les aides ne sont qu'un juste retour des impôts.", "La commission d'enquête du Sénat, adoptée à l'unanimité, réclame justement un « choc de transparence » sur leur efficacité."),
 ],
 questions=["Sais-tu quel est le taux de l'impôt sur les sociétés en Allemagne ?", "Les 211 milliards d'aides, sais-tu ce qu'on demande aux entreprises en échange ?"],
 limites=["Aucune source lue ne propose un classement unique de la fiscalité totale des entreprises en Europe.", "Les données sur les impôts de production datent de 2021."],
 publics={'convaincus': "Si tu parles de l'impôt sur les bénéfices, regarde les chiffres : 25 % en France, presque 30 % en Allemagne. Et les entreprises touchent au moins 211 milliards d'aides publiques par an, selon une commission du Sénat votée à l'unanimité, droite comprise. Le problème n'est pas qu'on les taxe trop, c'est qu'on ne sait pas ce que deviennent ces aides.",
  'indecis': "Les entreprises françaises paient des impôts de production élevés, c'est vrai. Mais leur impôt sur les bénéfices est dans la moyenne européenne depuis 2022, et elles reçoivent des aides publiques considérables. Pour juger, il faut regarder les deux colonnes du compte."},
 a_actualiser='2027-06-30',
))

# 8 ── Pays le plus taxé ─────────────────────────────────────────────────────
FICHES.append(fiche(
 id='france-pays-plus-taxe', affirmation="La France est le pays le plus taxé du monde.", volet='economie', sous_theme='Fiscalité',
 mots_cles=['pays le plus taxé', 'le plus taxé du monde', 'champion des impôts', 'pression fiscale', 'prélèvements obligatoires', 'taxés', 'matraquage fiscal', 'recettes fiscales'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="La France est bien en tête ou presque : première de l'UE en 2025 selon Eurostat (46 % du PIB), deuxième de l'OCDE en 2024 derrière le Danemark (43,5 % contre 45,2 %). Mais ces prélèvements financent surtout des retraites et une assurance santé publiques, que d'autres pays paient par des assurances privées non comptées comme impôts.",
 contexte="Le « record du monde des impôts » est un argument fréquent contre les services publics, la Sécurité sociale et les propositions fiscales de la gauche.",
 explication="Le taux de prélèvements obligatoires mesure les impôts et cotisations sociales rapportés au PIB. Un pays où la retraite et la santé passent par des assurances privées a un taux plus bas, mais ses habitants paient quand même, autrement.",
 sources=[OCDE_RECETTES, TLE_PO, DREES_PROT, OCDE_SANTE],
 faits=[
  fait("Selon l'OCDE, en 2024, les recettes fiscales atteignaient 43,5 % du PIB en France, deuxième rang derrière le Danemark (45,2 %), pour une moyenne OCDE de 34,1 %.", 'ocde_recettes', '2024', 'OCDE', "La France est parmi les pays les plus taxés, mais pas toujours première.", 'etabli', '43,5 %'),
  fait("Selon Eurostat (cité par Toute l'Europe), en 2025, les impôts et cotisations sociales nettes ont atteint 46 % du PIB en France, premier rang de l'UE devant le Danemark (45,1 %), pour une moyenne de 40,7 %.", 'tle_po', '2025', 'Union européenne', "Selon les années et les méthodes, la France est première ou deuxième.", 'etabli', '46 %'),
  fait("Selon la DREES, les prestations de protection sociale atteignent 31,9 % du PIB en France en 2024, contre 27,3 % en moyenne dans l'UE, et la vieillesse et la santé en représentent 80 %.", 'drees_prot', '2024', 'France et UE', "L'essentiel des prélèvements revient aux ménages sous forme de retraites et de soins.", 'etabli', '80 %'),
  fait("Selon l'OCDE, en France, plus des trois quarts des dépenses de santé sont pris en charge par une assurance maladie obligatoire ; aux États-Unis, les régimes publics n'en couvrent qu'environ 28 %.", 'ocde_sante', '2023', 'OCDE', "Ailleurs, les ménages paient leur santé par des assurances privées qui ne comptent pas comme des impôts.", 'etabli', '28 %'),
 ],
 court="Presque : la France est 1re de l'UE en 2025 (46 % du PIB, Eurostat) et 2e de l'OCDE en 2024 derrière le Danemark. Mais 80 % des prestations sociales financent les retraites et la santé, que d'autres pays paient par des assurances privées.",
 moyen="C'est en grande partie vrai : la France fait partie des pays où les prélèvements sont les plus élevés, première de l'UE en 2025 selon Eurostat, deuxième de l'OCDE en 2024 derrière le Danemark.\n\nMais ce chiffre ne dit pas à quoi sert l'argent. 80 % des prestations sociales servent aux retraites et à la santé. Aux États-Unis, la plupart des gens paient leur santé par des assurances privées : ça ne compte pas comme un impôt, mais ça coûte quand même.",
 detaille="Selon l'OCDE, les recettes fiscales atteignaient 43,5 % du PIB en France en 2024, au deuxième rang derrière le Danemark (45,2 %), pour une moyenne de 34,1 %. Selon Eurostat, la France est passée au premier rang de l'Union européenne en 2025 avec 46 % du PIB. L'affirmation est donc proche de la réalité, même si le classement varie selon les années et les méthodes.\n\nCe niveau s'explique surtout par la protection sociale : 31,9 % du PIB en prestations en 2024, contre 27,3 % dans l'UE, dont 80 % pour la vieillesse et la santé. Les retraites, l'assurance maladie et l'hôpital sont largement publics en France. Dans d'autres pays, ces dépenses passent par des fonds de pension ou des assurances privées, qui ne sont pas comptées comme des prélèvements : aux États-Unis, les régimes publics ne couvrent qu'environ 28 % des dépenses de santé.\n\nLa question utile n'est donc pas seulement « combien », mais « pour quoi » et « qui paie » : les débats sur la justice fiscale portent sur la répartition de l'effort, notamment entre revenus du travail et du capital.",
 empathie="C'est vrai, on paie beaucoup, et on a le droit de trouver ça lourd. Mais une bonne partie revient sous forme de retraite et de remboursements de soins. Dans d'autres pays, les gens paient moins d'impôts, mais ils paient des assurances privées très chères.",
 legitimes=["La France est effectivement parmi les deux pays les plus taxés de l'OCDE et de l'UE.", "On peut légitimement débattre de l'efficacité de la dépense publique."],
 contre=[
  ("On paie tout ça pour rien.", "80 % des prestations sociales financent les retraites et la santé, qui sont largement publiques en France."),
  ("Les Américains paient moins d'impôts, ils sont plus libres.", "Ils paient leur santé et leur retraite par des assurances privées, qui ne sont pas comptées comme des impôts mais restent une dépense."),
 ],
 questions=["Combien coûterait ta retraite et ton assurance santé si tu devais les payer en privé ?", "Qui, selon toi, devrait payer davantage, et qui moins ?"],
 limites=["Les comparaisons dépendent des méthodes (OCDE, Eurostat, Insee) et des années.", "Les données 2024 de l'OCDE sont provisoires."],
 publics={'convaincus': "Tu as raison sur un point : la France est parmi les deux pays les plus taxés. Mais demande-toi à quoi servent ces impôts : surtout ta retraite et tes soins. Aux États-Unis, les impôts sont plus bas, mais les régimes publics ne couvrent qu'environ 28 % des dépenses de santé. La vraie question est : qui paie, et qui est exonéré ?",
  'indecis': "Les prélèvements sont parmi les plus élevés au monde, c'est un fait. Mais ils financent un système de retraites et de santé largement public, que d'autres pays financent par des assurances privées. Pour comparer, il faut comparer ce qu'on paie au total, pas seulement les impôts."},
 a_actualiser='2027-06-30',
))

# 9 ── Fonctionnaires ────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='trop-de-fonctionnaires', affirmation="Il y a trop de fonctionnaires en France.", volet='services', sous_theme='Fonction publique',
 mots_cles=['fonctionnaires', 'trop de fonctionnaires', 'fonction publique', 'agents publics', 'emploi public', 'supprimer des postes', 'administration'],
 verdict='opinion', fiabilite='interpretation',
 resume="« Trop » est un jugement politique. Les faits : 5,9 millions d'agents publics fin 2024, dont 1,25 million dans les hôpitaux. L'emploi public pèse plus en France que dans la moyenne de l'OCDE, mais bien moins que dans les pays nordiques, et la France externalise moins ses services que l'Allemagne ou les Pays-Bas, ce qui gonfle la comparaison des seuls effectifs.",
 contexte="La suppression de postes de fonctionnaires est une promesse récurrente pour réduire la dépense publique.",
 explication="Compter les fonctionnaires ne dit pas tout : un pays peut employer directement ses infirmières et ses enseignants, ou payer des entreprises et des associations pour le faire. Le nombre d'agents dépend donc de l'organisation des services, pas seulement de leur taille.",
 sources=[INSEE_FP, OCDE_EMPLOI_PUB, FS_EMPLOI_PUB],
 faits=[
  fait("Selon l'Insee, 5,9 millions d'agents travaillent dans la fonction publique fin 2024 : 2 587 400 dans la fonction publique de l'État, 2 039 400 dans la territoriale et 1 249 900 dans l'hospitalière.", 'insee_fp', '2024', 'France', "Une grande partie des agents sont des soignants, des enseignants ou des agents des collectivités.", 'etabli', '5,9 millions'),
  fait("Selon l'OCDE, l'emploi public représentait en moyenne 18,4 % de l'emploi total en 2023, contre 30,1 % en Norvège, 28,2 % en Suède et 27,3 % au Danemark.", 'ocde_emp', '2023', 'OCDE', "Des pays prospères ont beaucoup plus d'emplois publics que la France.", 'etabli', '18,4 %'),
  fait("Selon France Stratégie (2017), la France compte 89 emplois publics pour 1 000 habitants, un taux relativement élevé, mais l'écart se réduit si l'on compte les services achetés au privé : 6 % du PIB en France contre 8 % en Allemagne et 10 % aux Pays-Bas.", 'fs_emp', '2017', 'Pays de l\'OCDE', "Ailleurs, une partie des services publics est assurée par des prestataires payés sur fonds publics.", 'etabli', '89'),
 ],
 court="C'est un choix politique, pas un fait : la France a plus d'emplois publics que la moyenne de l'OCDE, mais bien moins que les pays nordiques, et elle sous-traite moins ses services que l'Allemagne ou les Pays-Bas. Sur 5,9 millions d'agents, 1,25 million travaillent à l'hôpital.",
 moyen="Il y a 5,9 millions d'agents publics en France. C'est au-dessus de la moyenne de l'OCDE, mais loin des pays nordiques, où l'emploi public dépasse 27 % de l'emploi total.\n\nEt la comparaison est trompeuse : la France emploie directement beaucoup de soignants et d'enseignants, quand d'autres pays paient des entreprises pour le faire. Selon France Stratégie, l'écart se réduit nettement quand on compte ces services achetés. La vraie question est : quels services veut-on, et qui les assure ?",
 detaille="Selon l'Insee, 5,9 millions de personnes travaillaient dans la fonction publique fin 2024 : 2,6 millions pour l'État (dont l'Éducation nationale), 2 millions dans les collectivités et 1,25 million dans les hôpitaux publics.\n\nLes comparaisons internationales montrent un emploi public plus élevé en France que la moyenne de l'OCDE (18,4 % de l'emploi total en 2023), mais bien inférieur à la Norvège, la Suède ou le Danemark, autour de 27 à 30 %. France Stratégie notait en 2017 89 emplois publics pour 1 000 habitants en France, un taux relativement élevé, et soulignait que l'écart se réduit si l'on compte les dépenses de services achetés au privé, plus fortes en Allemagne ou aux Pays-Bas.\n\nDire qu'il y en a « trop » suppose de dire lesquels supprimer : infirmières, enseignants, policiers, agents d'accueil ?",
 empathie="Je comprends l'agacement face à certaines lourdeurs administratives. Mais quand on parle de fonctionnaires, on parle aussi de l'infirmière de nuit, de la maîtresse de ton enfant ou du pompier : lesquels voudrais-tu supprimer ?",
 legitimes=["L'emploi public est plus élevé en France que la moyenne de l'OCDE et que l'Allemagne.", "Les effectifs continuent d'augmenter (+0,6 % en 2024)."],
 contre=[
  ("On pourrait supprimer des postes administratifs sans toucher aux services.", "Il faut alors les identifier précisément ; une grande partie des agents travaille à l'hôpital, à l'école ou dans les services des collectivités."),
  ("Le privé ferait mieux et moins cher.", "Dans les pays qui externalisent davantage, la dépense ne disparaît pas : elle passe par des achats de services, comptés ailleurs."),
 ],
 questions=["Quels fonctionnaires supprimerais-tu en premier, concrètement ?", "As-tu déjà attendu longtemps aux urgences ou pour un rendez-vous administratif ?"],
 limites=["La part française de l'emploi public la plus récente lue date de 2017 (France Stratégie) ; l'OCDE 2025 n'indique pour la France qu'une évolution.", "« Trop » ou « pas assez » relève d'un jugement politique."],
 publics={'convaincus': "D'accord, parlons-en : sur 5,9 millions d'agents, 1,25 million sont à l'hôpital, et des centaines de milliers à l'école. Les pays nordiques, qu'on cite souvent en modèle, ont bien plus d'emplois publics que nous. Alors dis-moi lesquels tu supprimes : l'infirmière, le prof ou le gendarme ?",
  'indecis': "La France a un peu plus de fonctionnaires que la moyenne de l'OCDE, mais beaucoup moins que les pays nordiques. Une partie de l'écart vient du fait que d'autres pays sous-traitent leurs services au privé. La vraie question, c'est quels services publics on veut garder."},
 a_actualiser='2027-06-30',
))

# 10 ── TVA sur l'énergie (RN) ───────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-tva-energie', affirmation="Baisser la TVA sur l'énergie, comme le propose le RN, c'est bon pour le pouvoir d'achat.", volet='politique', sous_theme='Programmes électoraux',
 mots_cles=['tva sur l énergie', 'baisse de la tva', 'tva à 5,5', 'carburants', 'rn', 'rassemblement national', 'prix de l essence', 'pouvoir d achat', 'bardella'],
 verdict='trompeur', fiabilite='estimation',
 resume="La baisse de la TVA à 5,5 % sur les carburants, l'électricité et le gaz, promise par le RN en 2024, baisserait les factures si elle est répercutée. Mais elle coûterait 11 à 17 milliards d'euros par an, profiterait en euros davantage aux ménages aisés (qui consomment plus d'énergie), et serait bloquée pour les carburants par le droit européen sans accord unanime des États.",
 contexte="La mesure était une promesse phare du RN pour les européennes puis les législatives de 2024, présentée comme la réponse à la vie chère.",
 explication="Une baisse générale de TVA profite à tous ceux qui consomment, proportionnellement à leur consommation : plus on consomme d'énergie, plus on y gagne en euros. Une aide ciblée, au contraire, va aux ménages qui en ont le plus besoin.",
 sources=[PS_TVA, MONTAIGNE_TVA, INSEE_ENERGIE],
 faits=[
  fait("Selon un chiffrage du ministère de l'Économie rapporté par Public Sénat, la baisse de la TVA à 5,5 % sur l'énergie promise par le RN coûterait 16,8 milliards d'euros par an, dont environ 10 milliards pour les carburants.", 'ps_tva', '2024', 'France', "La mesure est très coûteuse pour les finances publiques.", 'estimation', '16,8 Md€'),
  fait("Selon l'Institut Montaigne, la perte de recettes serait d'environ 11,3 milliards d'euros par an (entre 9 et 13,6 milliards), et la baisse sur les carburants exigerait de réviser la directive européenne sur la TVA à l'unanimité des États.", 'montaigne_tva', '2024', 'France et UE', "Même avec un chiffrage plus bas, le coût reste élevé, et la mesure n'est pas applicable seule.", 'estimation', '11,3 Md€'),
  fait("Selon l'Insee, le bouclier tarifaire et la remise carburant de 2022 ont fait gagner 420 € en moyenne aux 10 % les plus aisés, contre 180 € aux 10 % les plus modestes ; rapporté au revenu, le gain était plus fort pour les modestes (+0,7 % contre +0,4 %).", 'insee_energie', '2021-2022', 'France', "Une baisse générale des prix de l'énergie profite davantage en euros aux plus aisés.", 'estimation', '420 €'),
 ],
 court="Trompeur : la facture baisserait si la baisse est répercutée, mais la mesure coûterait 11 à 17 milliards par an, profiterait plus en euros aux ménages aisés (Insee) et serait bloquée pour les carburants par le droit européen.",
 moyen="Sur le papier, baisser la TVA fait baisser les prix, et ça soulagerait des ménages qui ont besoin de leur voiture. Mais c'est une mesure très chère : 11 à 17 milliards d'euros par an selon les chiffrages.\n\nEt elle n'est pas ciblée : plus on consomme d'énergie, plus on y gagne. Lors des aides comparables de 2022, les 10 % les plus aisés ont gagné 420 € en moyenne, contre 180 € pour les plus modestes. Pour les carburants, il faudrait en plus l'accord unanime des pays européens.",
 detaille="Le Rassemblement national a promis en 2024 de ramener la TVA de 20 % à 5,5 % sur les carburants, l'électricité, le gaz et le fioul. Le ministère de l'Économie chiffrait le coût à 16,8 milliards d'euros par an ; l'Institut Montaigne à environ 11,3 milliards.\n\nLes effets sur le pouvoir d'achat existent, si les distributeurs répercutent la baisse sur les prix. Mais une baisse générale profite à proportion de la consommation. L'Insee l'a mesuré pour les aides comparables de 2022 : 420 € en moyenne pour les 10 % les plus aisés contre 180 € pour les 10 % les plus modestes, même si, rapporté au revenu, le gain était plus fort pour les modestes.\n\nLa mesure se heurte aussi au droit européen : la directive TVA ne prévoit pas de taux réduit pour les carburants, et sa révision exige l'unanimité. Pour le même coût, des aides ciblées sur les ménages modestes et les ruraux dépendants de la voiture, et des investissements dans la rénovation et les transports, peuvent réduire durablement les factures.",
 empathie="Je comprends : quand le plein et les factures explosent, une baisse de la TVA paraît évidente. Mais pour le même argent, on pourrait aider beaucoup plus ceux qui en ont vraiment besoin, au lieu de donner davantage à ceux qui ont trois voitures et une grande maison.",
 legitimes=["Les dépenses d'énergie pèsent lourd pour les ménages modestes et ruraux.", "Rapporté au revenu, une baisse des prix de l'énergie aide un peu plus les modestes."],
 contre=[
  ("Au moins, tout le monde en profite.", "Oui, mais surtout ceux qui consomment le plus : en 2022, les 10 % les plus aisés ont gagné plus du double des 10 % les plus modestes."),
  ("L'Europe n'a pas à nous dicter nos taux de TVA.", "Les règles de TVA sont communes et ont été acceptées par la France ; les changer pour les carburants exige l'accord de tous les États."),
 ],
 questions=["Qui consomme le plus d'énergie : un ménage modeste ou un ménage aisé ?", "Avec 11 à 17 milliards d'euros par an, quelles autres aides pourrait-on financer ?"],
 limites=["Les chiffrages diffèrent selon les sources (11 à 17 milliards d'euros).", "Les effets redistributifs cités portent sur les aides de 2022, comparables mais pas identiques."],
 publics={'convaincus': "Je ne nie pas que l'essence et l'électricité coûtent trop cher. Mais regarde qui y gagnerait : en 2022, les aides du même genre ont rapporté 420 € aux plus riches et 180 € aux plus modestes. Et pour les carburants, il faudrait l'accord de tous les pays européens : c'est une promesse qui ne peut pas être tenue telle quelle.",
  'indecis': "L'idée part d'une vraie difficulté : les factures d'énergie. Mais une baisse générale de la TVA coûte très cher et profite plus, en euros, aux ménages aisés. Des aides ciblées et des investissements dans la rénovation font plus pour les ménages modestes, à coût égal."},
 a_actualiser='2027-06-30',
))

# 11 ── Climat ───────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rechauffement-origine-humaine', affirmation="Le réchauffement climatique n'est pas causé par l'homme, le climat a toujours changé.", volet='ecologie', sous_theme='Changement climatique',
 mots_cles=['réchauffement climatique', 'climat a toujours changé', 'pas causé par l homme', 'climatosceptique', 'giec', 'origine humaine', 'changement climatique', 'cycles naturels'],
 verdict='contredit', fiabilite='etabli',
 resume="Le climat a varié naturellement dans le passé, c'est vrai. Mais selon le GIEC, il est « sans équivoque » que l'influence humaine a réchauffé l'atmosphère, l'océan et les terres : sur 1,09 °C de réchauffement mondial, environ 1,07 °C est d'origine humaine, et le rythme depuis 1970 est inédit depuis au moins 2 000 ans. En France métropolitaine, le réchauffement atteint 1,9 °C depuis 1900.",
 contexte="Le climatoscepticisme progresse dans une partie de l'électorat, souvent associé au rejet des normes écologiques et des « écolos ».",
 explication="Les variations naturelles du climat (orbite de la Terre, volcans, soleil) se font en général sur des milliers d'années. Le réchauffement actuel est beaucoup plus rapide, et les scientifiques peuvent mesurer la part due aux gaz à effet de serre émis par les activités humaines.",
 sources=[GIEC, METEO_FR, MTE_ADAPT],
 faits=[
  fait("Selon le GIEC (2021), « il est sans équivoque que l'influence humaine a réchauffé l'atmosphère, l'océan et les terres ».", 'giec', '2021', 'Monde', "La cause humaine est la conclusion centrale de la science du climat.", 'etabli'),
  fait("Selon le GIEC, la température de surface était 1,09 °C plus élevée en 2011-2020 qu'en 1850-1900, et la part d'origine humaine est estimée à 1,07 °C (entre 0,8 et 1,3 °C).", 'giec', '2011-2020', 'Monde', "La quasi-totalité du réchauffement observé est due aux activités humaines.", 'etabli', '1,07 °C'),
  fait("Selon le GIEC, la température mondiale a augmenté plus vite depuis 1970 que pendant toute autre période de 50 ans depuis au moins 2 000 ans, et la concentration de CO2 en 2019 est la plus élevée depuis au moins 2 millions d'années.", 'giec', '1970-2019', 'Monde', "Le rythme actuel n'a rien à voir avec les variations naturelles récentes.", 'etabli'),
  fait("Selon le ministère de la Transition écologique, le réchauffement atteint déjà 1,9 °C en France métropolitaine sur la dernière décennie par rapport à 1900.", 'mte_adapt', '2026', 'France métropolitaine', "Le réchauffement est déjà très sensible en France.", 'etabli', '1,9 °C'),
  fait("Selon Météo-France, la tendance en France a été de +0,3 °C par décennie sur la période 1959-2009.", 'meteo_fr', '1959-2009', 'France', "L'accélération est mesurée depuis plusieurs décennies.", 'etabli', '0,3 °C'),
 ],
 court="Faux : le climat a déjà changé naturellement, mais selon le GIEC le réchauffement actuel est « sans équivoque » d'origine humaine (1,07 °C sur 1,09 °C) et son rythme est inédit depuis au moins 2 000 ans.",
 moyen="Oui, le climat a toujours varié, sur des milliers d'années. Mais ce qui se passe aujourd'hui est différent : le GIEC, qui synthétise des milliers d'études, juge « sans équivoque » le rôle humain, et attribue presque tout le réchauffement observé (1,07 °C sur 1,09 °C) aux activités humaines.\n\nLe rythme est inédit depuis au moins 2 000 ans. En France métropolitaine, il fait déjà 1,9 °C de plus qu'en 1900 : ce n'est plus de la théorie.",
 detaille="Le climat de la Terre a connu des variations naturelles importantes, comme les ères glaciaires. Personne ne le conteste. Mais ces variations sont lentes. Selon le GIEC (2021), le réchauffement depuis 1970 est plus rapide que pendant toute autre période de cinquante ans depuis au moins 2 000 ans, et la concentration de CO2 atteint un niveau inédit depuis au moins 2 millions d'années.\n\nLe GIEC conclut qu'il est « sans équivoque » que l'influence humaine a réchauffé l'atmosphère, l'océan et les terres. Sur 1,09 °C de réchauffement mondial entre 1850-1900 et 2011-2020, la part humaine est estimée à 1,07 °C. Les facteurs naturels pèsent très peu sur cette période.\n\nEn France, Météo-France mesurait 1,7 °C de hausse depuis 1900, et le ministère de la Transition écologique indique désormais 1,9 °C sur la dernière décennie. Reconnaître la cause humaine n'impose pas une politique unique ; mais c'est la condition pour en débattre sérieusement, y compris de la justice sociale de la transition.",
 empathie="Je comprends qu'on se méfie quand on a l'impression qu'on nous fait la morale avec le climat. Mais là-dessus, les scientifiques du monde entier sont d'accord, et beaucoup en constatent déjà les effets autour d'eux. On peut discuter de qui doit payer la transition, pas du thermomètre.",
 legitimes=["Le climat a effectivement varié naturellement dans le passé.", "Les politiques climatiques peuvent peser sur les ménages modestes si elles sont mal conçues."],
 contre=[
  ("Les scientifiques ne sont pas d'accord entre eux.", "Le rapport du GIEC synthétise des milliers d'études et son résumé est approuvé par les gouvernements ; il juge le rôle humain « sans équivoque »."),
  ("C'est le soleil.", "Le GIEC attribue la quasi-totalité du réchauffement observé (1,07 °C sur 1,09 °C) à l'influence humaine."),
 ],
 questions=["À quand remonte, selon toi, un réchauffement aussi rapide ?", "As-tu remarqué des changements autour de toi : canicules, sécheresses, hivers plus doux ?"],
 limites=["Les chiffres mondiaux du GIEC datent du rapport de 2021.", "Les projections futures dépendent des émissions, non traitées ici."],
 publics={'convaincus': "Tu as raison, le climat a toujours changé, mais en des milliers d'années. Là, selon le GIEC, on a pris plus d'un degré en un siècle, presque entièrement à cause de nous, à un rythme jamais vu depuis 2 000 ans. Tu peux refuser certaines mesures écologiques, mais nier le thermomètre ne protégera ni les paysans ni les gens qui étouffent l'été.",
  'indecis': "Le doute est normal sur un sujet aussi vaste. Le point de départ fiable, c'est le GIEC : le rôle humain est « sans équivoque », et la France s'est réchauffée de 1,9 °C depuis 1900. Le vrai débat porte sur les solutions et sur qui les paie."},
 stabilite='evolutive', a_actualiser='2027-06-30',
))

# 12 ── Éoliennes ────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='eoliennes-polluent', affirmation="Les éoliennes polluent plus qu'elles ne rapportent.", volet='ecologie', sous_theme='Énergies renouvelables',
 mots_cles=['éoliennes', 'eolien', 'polluent', 'bilan carbone', 'pales', 'recyclage', 'béton', 'terres rares', 'démantèlement'],
 verdict='contredit', fiabilite='etabli',
 resume="Sur tout son cycle de vie, l'éolien terrestre émet environ 12,7 g de CO2 par kWh, contre 469 g pour le gaz et 1 000 g pour le charbon (analyse de 2015 pour l'ADEME). La loi impose le démantèlement, l'excavation totale des fondations et le recyclage de 95 % de la masse. Les pales restent difficiles à recycler (environ 50 % de matière récupérée), et les installations terrestres actuelles ne contiennent plus de terres rares.",
 contexte="Les éoliennes sont une cible fréquente d'une partie de la droite et de l'extrême droite : bétonnage, pales enfouies, terres rares, paysages défigurés.",
 explication="Pour comparer des énergies, on calcule leurs émissions sur tout leur cycle de vie : fabrication, transport, fonctionnement et démantèlement. Une éolienne émet surtout lors de sa fabrication, puis produit pendant des années sans brûler de combustible.",
 sources=[AN_EOL, DREAL_EOL],
 faits=[
  fait("Selon une analyse de cycle de vie de 2015 réalisée pour l'ADEME (citée par le ministère de la Transition écologique), l'éolien terrestre émet 12,7 g de CO2 équivalent par kWh, contre 469 g pour le gaz naturel, 840 g pour le pétrole et 1 000 g pour le charbon.", 'an_eol', '2015', 'France', "Sur tout son cycle de vie, l'éolien est l'une des électricités les moins émettrices.", 'etabli', '12,7 g'),
  fait("Selon le ministère, l'arrêté du 22 juin 2020 impose l'excavation totale des fondations lors du démantèlement ; selon l'ADEME, moins de 30 % du parc contient des terres rares, et les installations terrestres actuelles n'en contiennent plus.", 'an_eol', '2020-2021', 'France', "Le béton et les terres rares ne sont pas le problème qu'on décrit.", 'etabli', '30 %'),
  fait("Selon la DREAL Auvergne-Rhône-Alpes, la réglementation impose de recycler ou réutiliser 95 % de la masse de l'éolienne et 55 % du rotor d'ici 2025 ; les pales en composites sont plus difficiles à recycler, avec environ 50 % de matière récupérée lors des premières opérations.", 'dreal_eol', '2023', 'France', "Le recyclage des pales est une vraie limite, en voie d'amélioration.", 'etabli', '95 %'),
 ],
 court="Faux : sur tout son cycle de vie, l'éolien émet environ 12,7 g de CO2 par kWh, contre 469 g pour le gaz (analyse pour l'ADEME). Le démantèlement et le recyclage de 95 % de la masse sont obligatoires ; seules les pales restent difficiles à recycler.",
 moyen="Une éolienne pollue surtout quand on la fabrique. Ensuite, elle produit pendant des années sans brûler de combustible. Résultat, sur tout son cycle de vie : environ 12,7 g de CO2 par kWh, contre 469 g pour le gaz et 1 000 g pour le charbon.\n\nLe démantèlement est obligatoire, avec l'enlèvement complet des fondations, et 95 % de la masse doit être recyclée. Le vrai point faible, ce sont les pales, recyclées à environ 50 % aujourd'hui. Quant aux terres rares, les éoliennes terrestres actuelles n'en contiennent plus.",
 detaille="Selon une analyse de cycle de vie de 2015 réalisée pour l'ADEME et citée par le ministère de la Transition écologique, l'éolien terrestre émet environ 12,7 g de CO2 équivalent par kWh produit, en comptant la fabrication, l'installation et le démantèlement. C'est des dizaines de fois moins que le gaz (469 g), le pétrole (840 g) ou le charbon (1 000 g).\n\nLa réglementation impose le démantèlement des éoliennes, des postes et des câbles, l'excavation totale des fondations depuis 2020, et des garanties financières pour le payer. Elle impose aussi de recycler ou réutiliser 95 % de la masse de l'éolienne. Selon l'ADEME, moins de 30 % du parc contient des terres rares et les installations terrestres actuelles n'en contiennent plus.\n\nIl reste des limites réelles : les pales en composites sont difficiles à recycler (environ 50 % de matière récupérée lors des premières opérations), et l'éolien pose des questions de paysage, d'avifaune et d'intermittence, qui méritent un débat honnête. Mais dire qu'elles « polluent plus qu'elles ne rapportent » est contraire aux mesures.",
 empathie="Je comprends qu'on n'ait pas envie de voir des éoliennes partout, et le paysage est une vraie question. Mais sur la pollution, les chiffres sont clairs : sur toute sa vie, une éolienne émet des dizaines de fois moins de CO2 qu'une centrale à gaz.",
 legitimes=["Les pales sont encore difficiles à recycler.", "L'éolien pose des questions de paysage, d'effet sur les oiseaux et d'intermittence de la production."],
 contre=[
  ("On enterre des tonnes de béton qui restent pour toujours.", "Depuis 2020, l'excavation totale des fondations est obligatoire lors du démantèlement."),
  ("Elles sont pleines de terres rares venues de Chine.", "Selon l'ADEME, moins de 30 % du parc en contient, et les installations terrestres actuelles n'en contiennent plus."),
 ],
 questions=["Combien de CO2 émet, selon toi, une centrale à gaz par rapport à une éolienne ?", "Qu'est-ce qui te gêne le plus : la pollution ou le paysage ?"],
 limites=["L'analyse de cycle de vie citée date de 2015.", "L'effet sur les oiseaux, l'intermittence et le temps de retour énergétique ne sont pas chiffrés à partir des sources lues."],
 publics={'convaincus': "Tu peux ne pas aimer les éoliennes dans le paysage, ça se discute. Mais dire qu'elles polluent plus qu'elles ne rapportent, c'est faux : 12,7 g de CO2 par kWh sur toute leur vie, contre 469 g pour le gaz. Et le béton, la loi oblige à l'enlever entièrement depuis 2020.",
  'indecis': "Les éoliennes ont des défauts réels : les pales se recyclent mal et elles ne produisent pas quand il n'y a pas de vent. Mais sur l'ensemble de leur vie, elles émettent très peu de CO2, et leur démantèlement est encadré par la loi. Le débat porte plutôt sur où et comment les installer."},
 a_actualiser='2027-06-30',
))

# 13 ── Voiture électrique ───────────────────────────────────────────────────
FICHES.append(fiche(
 id='voiture-electrique-pollue', affirmation="Les voitures électriques polluent plus que les voitures thermiques.", volet='ecologie', sous_theme='Transports',
 mots_cles=['voiture électrique', 'voitures électriques', 'véhicule électrique', 'batteries', 'polluent plus', 'thermique', 'lithium', 'bilan carbone'],
 verdict='contredit', fiabilite='etabli',
 resume="Sur toute sa durée de vie, une voiture électrique de taille raisonnable a un impact carbone 2 à 3 fois inférieur à une voiture thermique équivalente selon l'ADEME, et 3 à 4 fois inférieur en France selon Carbone 4, grâce à une électricité peu carbonée. Sa fabrication émet davantage, à cause de la batterie, et les très gros modèles perdent une grande partie de cet avantage.",
 contexte="L'idée que la voiture électrique serait une arnaque écologique circule largement, souvent en réaction à l'interdiction des ventes de voitures thermiques neuves en Europe.",
 explication="Une voiture électrique commence sa vie avec une « dette carbone » plus grande, liée à la batterie, puis émet beaucoup moins en roulant. Au-delà d'un certain kilométrage, elle devient nettement moins émettrice, d'autant plus que l'électricité du pays est peu carbonée.",
 sources=[ADEME_VE, ICCT_VE, C4_VE],
 faits=[
  fait("Selon l'ADEME, une voiture électrique à batterie raisonnable (moins de 60 kWh) a un impact carbone 2 à 3 fois inférieur à celui d'un modèle thermique similaire sur sa durée de vie.", 'ademe_ve', '2022', 'France', "Sur l'ensemble de sa vie, l'électrique est nettement moins émettrice.", 'etabli', '2 à 3 fois'),
  fait("Selon l'ADEME, la « dette carbone » de fabrication est amortie avant 20 000 km pour une citadine, vers 70 000 km pour une compacte, et au-delà de 100 000 km pour une batterie de 100 kWh.", 'ademe_ve', '2022', 'France', "La taille de la batterie compte : les gros modèles sont beaucoup moins intéressants.", 'etabli', '20 000 km'),
  fait("Selon l'ICCT, pour les voitures moyennes immatriculées en 2021, les émissions sur toute la durée de vie d'une voiture électrique sont inférieures de 66 à 69 % à celles d'une voiture essence comparable en Europe.", 'icct_ve', '2021', 'Europe', "Le résultat est confirmé à l'échelle européenne.", 'estimation', '66-69 %'),
  fait("Selon Carbone 4, en France, un véhicule électrique émet 3 à 4 fois moins de CO2 que son équivalent thermique sur sa durée de vie, mais sa fabrication émet davantage, essentiellement à cause de la batterie.", 'c4_ve', '2022', 'France', "La fabrication est plus polluante : c'est vrai, et c'est compensé ensuite.", 'estimation', '3 à 4 fois'),
  fait("Selon l'ADEME, les besoins en lithium devraient augmenter de 300 à 800 % par rapport à 2020, et les particules liées à l'usure des pneus et des freins sont accentuées par la masse des véhicules.", 'ademe_ve', '2022', 'Monde', "La voiture électrique n'est pas propre : elle est moins polluante, à condition de rester raisonnable en taille.", 'estimation', '300 à 800 %'),
 ],
 court="Faux sur l'ensemble de la vie du véhicule : une voiture électrique raisonnable émet 2 à 3 fois moins de CO2 qu'une thermique (ADEME), 3 à 4 fois moins en France (Carbone 4). Sa fabrication émet plus, et les très gros modèles perdent une partie de l'avantage.",
 moyen="Il y a un fond de vrai : fabriquer une voiture électrique, surtout sa batterie, émet plus que fabriquer une voiture thermique. Mais ensuite, elle émet beaucoup moins en roulant, surtout en France où l'électricité est peu carbonée.\n\nRésultat sur toute sa vie, selon l'ADEME : 2 à 3 fois moins de CO2 pour un modèle raisonnable. La « dette » de fabrication est remboursée avant 20 000 km pour une citadine. Le vrai problème, ce sont les gros SUV électriques à énorme batterie, et les métaux à extraire.",
 detaille="Les analyses de cycle de vie comparent les émissions de la fabrication, de l'usage et de la fin de vie. Selon l'ADEME, une voiture électrique à batterie raisonnable (moins de 60 kWh) a un impact carbone 2 à 3 fois inférieur à celui d'un modèle thermique similaire. Carbone 4 estime l'écart à 3 à 4 fois en France, et l'ICCT à 66 à 69 % de moins en Europe pour les voitures immatriculées en 2021.\n\nLa fabrication émet bien plus, à cause de la batterie : c'est la « dette carbone ». Elle est remboursée avant 20 000 km pour une citadine, vers 70 000 km pour une compacte, mais au-delà de 100 000 km pour une grosse batterie de 100 kWh. Un gros SUV électrique a ainsi une empreinte deux fois supérieure à celle d'une petite citadine électrique.\n\nLa voiture électrique a d'autres coûts : besoins en lithium multipliés, particules d'usure des pneus et des freins accentuées par le poids. Elle n'est donc pas « propre » ; mais elle pollue moins que la thermique, à condition de privilégier des modèles sobres, et de développer aussi les transports collectifs.",
 empathie="Je comprends le doute : on entend que les batteries sont une catastrophe, et c'est vrai qu'elles coûtent cher en énergie et en métaux. Mais sur toute la vie de la voiture, les études publiques montrent qu'une électrique de taille normale pollue deux à trois fois moins.",
 legitimes=["La fabrication d'une voiture électrique émet davantage, surtout à cause de la batterie.", "Les gros modèles électriques et l'extraction des métaux posent de vrais problèmes."],
 contre=[
  ("L'électricité vient du charbon.", "En France, l'électricité est très peu carbonée, ce qui réduit fortement les émissions à l'usage ; même en Europe, l'ICCT trouve 66 à 69 % d'émissions en moins."),
  ("Les batteries ne durent pas.", "Même en comptant la batterie, la dette carbone d'une citadine est remboursée avant 20 000 km selon l'ADEME."),
 ],
 questions=["Savais-tu que la batterie d'une citadine électrique est « remboursée » en carbone avant 20 000 km ?", "Un SUV électrique de deux tonnes, est-ce vraiment la même chose qu'une petite citadine ?"],
 limites=["Les chiffres de l'ADEME datent de 2022, ceux de l'ICCT de 2021 : les batteries et le mix électrique évoluent.", "Les autres impacts (eau, biodiversité, conditions d'extraction) ne sont pas chiffrés ici."],
 publics={'convaincus': "Tu as raison sur un point : la batterie pollue à la fabrication. Mais l'ADEME a fait le calcul complet : sur toute sa vie, une électrique raisonnable émet deux à trois fois moins qu'une thermique, et la dette de la batterie est remboursée avant 20 000 km pour une citadine. Le vrai scandale, ce sont les SUV de deux tonnes, électriques ou pas.",
  'indecis': "La voiture électrique n'est pas parfaite : batteries, métaux, poids. Mais les études publiques convergent : sur toute sa vie, elle émet nettement moins de CO2 qu'une thermique, surtout en France. Le choix d'un modèle sobre compte autant que le type de moteur."},
 a_actualiser='2027-06-30',
))

# 14 ── Cannabis ─────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='cannabis-legalisation-consommation', affirmation="Légaliser le cannabis ferait exploser la consommation.", volet='securite', sous_theme='Prévention et politiques publiques',
 mots_cles=['cannabis', 'légaliser', 'légalisation', 'drogue', 'shit', 'consommation', 'prohibition', 'dépénalisation'],
 verdict='trompeur', fiabilite='debat',
 resume="La France, avec l'une des législations les plus répressives, est déjà parmi les plus gros consommateurs de cannabis de l'UE : 10,8 % des 18-64 ans en ont consommé dans l'année en 2023. Au Canada, la consommation adulte a augmenté après la légalisation (de 14 % à 20 % sur trois mois entre 2018 et 2020) : la hausse existe, mais « exploser » n'est pas étayé, et le Conseil d'analyse économique juge la prohibition « coûteuse et inefficace ».",
 contexte="La légalisation du cannabis, défendue par une partie de la gauche et par certains économistes, est combattue par le RN et la droite au nom de la santé et de la sécurité.",
 explication="La prohibition n'empêche pas la consommation : elle la laisse au marché noir. Une légalisation encadrée change les règles (âge minimum, produits contrôlés, taxes), avec des effets qui dépendent de son organisation.",
 sources=[OFDT_CANNABIS, AN_CANNABIS, CAE_CANNABIS, STATCAN],
 faits=[
  fait("Selon l'OFDT, en 2023, 10,8 % des 18-64 ans ont consommé du cannabis dans l'année, un niveau stable depuis une dizaine d'années, et la consommation recule chez les jeunes.", 'ofdt_cannabis', '2023', 'France', "La consommation est élevée malgré la répression.", 'etabli', '10,8 %'),
  fait("Selon la mission d'information de l'Assemblée nationale (2021), la France est le plus gros consommateur de cannabis de l'Union européenne, avec 5 millions de consommateurs dans l'année et 900 000 usagers quotidiens ; le rapport fait le « constat d'un échec de la politique répressive ».", 'an_cannabis', '2021', 'France', "La prohibition n'a pas tenu sa promesse.", 'etabli', '900 000'),
  fait("Selon Statistique Canada, la part de la population ayant consommé du cannabis au cours des trois derniers mois est passée de 14 % avant la légalisation à 20 % fin 2020, et l'usage quotidien ou quasi quotidien de 5,4 % en 2018 à 7,9 % en 2020.", 'statcan', '2018-2020', 'Canada', "La légalisation peut augmenter la consommation adulte : il faut le reconnaître.", 'etabli', '20 %'),
  fait("Selon le Conseil d'analyse économique (2019), la prohibition française est « à la fois coûteuse et inefficace » ; la légalisation entraîne une hausse chez les consommateurs réguliers, mais peut réduire l'usage des plus jeunes si l'interdiction de vente aux mineurs est respectée.", 'cae_cannabis', '2019', 'France', "Tout dépend des règles : une légalisation encadrée peut mieux protéger les mineurs.", 'interpretation'),
 ],
 court="Trompeur : la France est déjà parmi les plus gros consommateurs de l'UE malgré la répression (10,8 % des adultes dans l'année). Au Canada, la consommation adulte a augmenté après la légalisation, mais « exploser » n'est pas étayé, et tout dépend de l'encadrement.",
 moyen="La France interdit le cannabis, et pourtant c'est l'un des pays d'Europe où l'on en consomme le plus : 900 000 usagers quotidiens selon l'Assemblée nationale. La prohibition n'a pas empêché la consommation, elle l'a laissée aux trafiquants.\n\nAu Canada, la consommation adulte a augmenté après la légalisation : de 14 % à 20 % de consommateurs sur trois mois. Il faut le dire. Mais le Conseil d'analyse économique souligne qu'une légalisation encadrée peut mieux protéger les mineurs. Le vrai débat porte sur les règles, pas sur une « explosion ».",
 detaille="Selon l'OFDT, 10,8 % des 18-64 ans ont consommé du cannabis dans l'année en 2023, un niveau stable depuis une dizaine d'années, et la consommation recule chez les jeunes. La mission d'information de l'Assemblée nationale (2021) note que la France est le plus gros consommateur de l'UE et fait le constat d'un échec de la politique répressive.\n\nLes expériences étrangères montrent des effets réels. Au Canada, la consommation sur trois mois est passée de 14 % à 20 % entre 2018 et 2020, et l'usage quotidien de 5,4 % à 7,9 %. Le Conseil d'analyse économique reconnaît une hausse chez les consommateurs réguliers, mais estime qu'un monopole encadré peut réduire l'usage des plus jeunes si l'interdiction de vente aux mineurs est respectée.\n\nLe choix est donc politique : santé publique, lutte contre les réseaux, prévention des jeunes. On peut s'opposer à la légalisation ; mais le statu quo, que l'on présente comme protecteur, s'accompagne déjà d'une consommation très élevée et d'un marché laissé aux trafiquants.",
 empathie="Je comprends l'inquiétude, surtout pour les jeunes : personne ne veut banaliser une drogue. Mais aujourd'hui, avec l'interdiction, la France est déjà championne d'Europe, et ce sont les dealers qui fixent les règles. La question, c'est quel système protège le mieux.",
 legitimes=["Au Canada, la consommation adulte et l'usage quotidien ont augmenté après la légalisation.", "Le cannabis présente des risques pour la santé, surtout chez les jeunes."],
 contre=[
  ("Légaliser, c'est dire aux jeunes que c'est sans danger.", "La légalisation encadrée inclut l'interdiction de vente aux mineurs et la prévention ; la prohibition actuelle n'empêche pas les mineurs d'acheter aux dealers."),
  ("Le trafic continuera de toute façon.", "C'est un risque réel, qui dépend du prix et de l'offre légale ; l'argument concerne l'organisation de la légalisation, pas le constat d'échec de la répression."),
 ],
 questions=["Sais-tu que la France, malgré l'interdiction, est parmi les plus gros consommateurs d'Europe ?", "Qui contrôle aujourd'hui ce que fument les jeunes, et à quel âge ?"],
 limites=["Les données canadiennes portent sur 2018-2020, les premières années après la légalisation.", "Aucune donnée chiffrée sur l'Uruguay ni comparaison européenne récente n'a été lue."],
 publics={'convaincus': "Regarde les faits : la France interdit tout et c'est l'un des pays d'Europe où l'on fume le plus. Au Canada, la consommation adulte a augmenté après la légalisation, c'est vrai, mais pas « explosé ». La question est simple : préfères-tu que les règles soient fixées par l'État ou par les trafiquants ?",
  'indecis': "La crainte d'une hausse n'est pas absurde : au Canada, la consommation adulte a augmenté. Mais la France consomme déjà beaucoup sous prohibition. Le débat sérieux porte sur l'encadrement : âge minimum, prévention, lutte contre les réseaux."},
 a_actualiser='2027-06-30',
))

# 15 ── IVG ──────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='ivg-contraception', affirmation="L'IVG est devenue un moyen de contraception.", volet='droits', sous_theme='Féminisme',
 mots_cles=['ivg', 'avortement', 'contraception', 'avortent par confort', 'moyen de contraception', 'interruption volontaire de grossesse', 'pilule'],
 verdict='contredit', fiabilite='etabli',
 resume="Non. La plupart des IVG font suite à un échec de contraception : selon la HAS, deux grossesses non prévues sur trois surviennent sous contraception, et le ministère de la Santé indiquait que deux tiers des IVG résultent d'échecs contraceptifs. Le nombre d'IVG augmente (251 270 en 2024, 17,3 pour 1 000 femmes), mais il baisse chez les moins de 20 ans par rapport à il y a dix ans.",
 contexte="L'idée que les femmes avorteraient « par confort » revient lors des débats sur l'IVG, notamment depuis son inscription dans la Constitution en 2024.",
 explication="Aucune méthode de contraception n'est efficace à 100 %, surtout en pratique (oubli de pilule, préservatif mal utilisé). Une IVG est une démarche médicale encadrée, pas une méthode choisie à la place de la contraception.",
 sources=[DREES_IVG, HAS_CONTRA, AN_IVG],
 faits=[
  fait("Selon la DREES, 251 270 IVG ont été réalisées en France en 2024, soit 7 000 de plus qu'en 2023, et le taux de recours atteint 17,3 pour 1 000 femmes de 15 à 49 ans.", 'drees_ivg', '2024', 'France', "Le nombre d'IVG augmente : c'est un fait à expliquer, pas à cacher.", 'etabli', '251 270'),
  fait("Selon la DREES, le taux d'IVG chez les moins de 20 ans est plus faible qu'il y a dix ans : 5,5 pour 1 000 contre 8,7.", 'drees_ivg', '2014-2024', 'France', "Chez les plus jeunes, le recours baisse.", 'etabli', '5,5 ‰'),
  fait("Selon la Haute Autorité de santé (2013), deux grossesses non prévues sur trois surviennent alors qu'une méthode contraceptive est utilisée.", 'has_contra', '2013', 'France', "La plupart des grossesses non prévues viennent d'un échec de contraception, pas de son absence.", 'etabli', '2 sur 3'),
  fait("Selon le ministère de la Santé (2011), « deux tiers des IVG sont le résultat d'échecs contraceptifs » ; un rapport de l'IGAS indiquait que 72 % des IVG concernaient des femmes sous contraception.", 'an_ivg', '2011', 'France', "Les femmes qui avortent utilisaient en majorité une contraception.", 'etabli', '72 %'),
 ],
 court="Faux : selon la HAS et le ministère de la Santé, environ deux tiers des grossesses non prévues et des IVG font suite à un échec de contraception. Le nombre d'IVG augmente (251 270 en 2024), mais pas parce que les femmes renonceraient à la contraception.",
 moyen="La plupart des femmes qui avortent utilisaient une contraception. Selon la Haute Autorité de santé, deux grossesses non prévues sur trois surviennent sous contraception : oubli de pilule, préservatif qui craque, méthode mal adaptée.\n\nLe nombre d'IVG augmente bien depuis quelques années, avec 251 270 en 2024. Mais chez les moins de 20 ans, il baisse par rapport à il y a dix ans. La réponse passe par une contraception mieux adaptée à chacune, pas par la culpabilisation.",
 detaille="Selon la DREES, 251 270 IVG ont été réalisées en France en 2024, 7 000 de plus qu'en 2023, soit un taux de 17,3 pour 1 000 femmes de 15 à 49 ans. Le taux le plus élevé concerne les 25-29 ans ; chez les moins de 20 ans, il est plus faible qu'il y a dix ans.\n\nL'idée d'une IVG « contraceptive » est contredite par les données disponibles. La Haute Autorité de santé indiquait en 2013 que deux grossesses non prévues sur trois surviennent alors qu'une méthode contraceptive est utilisée, et le ministère de la Santé que deux tiers des IVG résultent d'échecs contraceptifs. Un rapport de l'IGAS évaluait à 72 % la part des IVG concernant des femmes sous contraception.\n\nLa HAS en tirait une conclusion pratique : adapter la contraception au profil de chaque femme. Depuis mars 2024, la liberté de recourir à l'IVG est inscrite dans la Constitution ; la culpabilisation ne réduit pas les grossesses non désirées, l'accès à une contraception adaptée, si.",
 empathie="Je comprends qu'on puisse être mal à l'aise avec l'avortement. Mais la plupart des femmes concernées avaient une contraception qui a échoué : ce n'est jamais une décision prise à la légère. Ce qui réduit vraiment les IVG, c'est une contraception mieux adaptée.",
 legitimes=["Le nombre et le taux d'IVG augmentent depuis quelques années.", "L'IVG reste un sujet de conscience pour beaucoup de personnes."],
 contre=[
  ("Avec la pilule gratuite, il n'y a plus d'excuse.", "Selon la HAS, deux grossesses non prévues sur trois surviennent sous contraception : aucune méthode n'est infaillible en pratique."),
  ("Les jeunes avortent à tout va.", "Selon la DREES, le taux d'IVG des moins de 20 ans est plus faible qu'il y a dix ans."),
 ],
 questions=["Savais-tu que la plupart des IVG font suite à un échec de contraception ?", "Qu'est-ce qui, selon toi, réduirait vraiment les grossesses non désirées ?"],
 limites=["Les données sur l'usage d'une contraception au moment de la grossesse sont anciennes (2011-2013) ; aucune étude plus récente n'a pu être lue.", "Les causes de la hausse récente des IVG ne sont pas analysées ici."],
 publics={'convaincus': "Les chiffres de la Haute Autorité de santé disent l'inverse : deux grossesses non prévues sur trois arrivent sous contraception. Les femmes qui avortent n'ont pas « remplacé » la pilule par l'IVG, leur contraception a échoué. Si on veut moins d'IVG, il faut une meilleure contraception, pas de la honte.",
  'indecis': "La hausse des IVG est réelle et mérite d'être comprise. Mais la plupart des IVG font suite à un échec de contraception, selon la HAS et le ministère de la Santé. Une contraception mieux adaptée à chaque femme est la piste la plus efficace."},
 a_actualiser='2027-06-30',
))

# 16 ── Pétain et les Juifs ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='petain-juifs-francais', affirmation="Pétain a protégé les Juifs français.", volet='international', sous_theme='Guerres et conflits',
 mots_cles=['pétain', 'vichy', 'juifs français', 'protégé les juifs', 'sauvé les juifs', 'vel d hiv', 'statut des juifs', 'déportation', 'shoah', 'collaboration'],
 verdict='contredit', fiabilite='etabli', stabilite='historique',
 resume="Les historiens réfutent cette thèse. Le régime de Vichy a promulgué dès octobre 1940, sans y être contraint par l'occupant, un statut des Juifs qui visait aussi les Juifs français. Environ 74 500 Juifs ont été déportés de France, dont 24 500 Français. La rafle du Vél d'Hiv a été menée par la police française. Si une majorité des Juifs de France a survécu, c'est « en dépit de Vichy, pas grâce à Vichy » (Jacques Semelin).",
 contexte="L'idée que Pétain aurait « sacrifié les Juifs étrangers pour sauver les Juifs français » est reprise par des figures d'extrême droite pour réhabiliter Vichy.",
 explication="Vichy a fait la différence entre Juifs étrangers et Juifs français dans les arrestations, mais il a persécuté les deux : exclusion des emplois, recensements, spoliations. Les arrestations de Juifs étrangers ont été menées par la police française, et des Juifs français ont aussi été déportés.",
 sources=[JOLY_NANTES, MEMORIAL, APHG_JOLY, PS_SEMELIN, PS_CHIRAC],
 faits=[
  fait("Selon l'historien Laurent Joly (CNRS), le statut des Juifs promulgué le 3 octobre 1940 vise aussi les Juifs français, et le bilan des déportations est de 74 500 Juifs, dont 24 500 Français.", 'joly', '1940-1944', 'France', "Les Juifs français n'ont pas été protégés : environ un tiers des déportés étaient français.", 'etabli', '24 500'),
  fait("Selon le compte rendu de l'ouvrage de Laurent Joly par l'APHG, le statut des Juifs fut « un choix délibéré et non contraint par l'occupant ».", 'aphg_joly', '1940', 'France', "La persécution est une initiative du régime de Vichy, pas une simple obéissance.", 'etabli'),
  fait("Selon le Mémorial de la Shoah, 76 000 Juifs, dont plus de 11 000 enfants, ont été déportés de France par les nazis avec l'aide du gouvernement de Vichy, et 25 % de la population juive de France a été victime de la Shoah.", 'memorial', '1942-1944', 'France', "Les chiffres varient légèrement selon les sources, mais l'ampleur est la même.", 'etabli', '76 000'),
  fait("Selon Laurent Joly, la rafle du Vél d'Hiv a été organisée et menée par la police française, « sans la présence d'un seul Allemand », avec environ 4 500 policiers.", 'joly', '1942', 'Paris', "L'État français a lui-même arrêté des familles entières.", 'etabli', '4 500'),
  fait("Selon l'historien Jacques Semelin, « si tant de juifs ont survécu à l'occupation en France c'est en dépit de Vichy mais pas grâce à Vichy ».", 'ps_semelin', '2023', 'France', "La survie s'explique par d'autres facteurs que la politique de Vichy.", 'interpretation'),
  fait("Le 16 juillet 1995, le président Jacques Chirac a reconnu que « la folie criminelle de l'occupant a été secondée par des Français, par l'État français ».", 'ps_chirac', '1995', 'France', "La responsabilité de l'État français est officiellement reconnue.", 'etabli'),
 ],
 court="Faux : Vichy a promulgué en 1940, sans contrainte allemande, un statut des Juifs qui visait aussi les Juifs français, et 24 500 Juifs français ont été déportés (Laurent Joly, CNRS). Ceux qui ont survécu l'ont fait « en dépit de Vichy, pas grâce à Vichy ».",
 moyen="Les historiens sont clairs : Vichy a persécuté les Juifs, français compris. Le statut des Juifs d'octobre 1940, adopté sans demande allemande, les excluait de nombreux métiers. Sur environ 74 500 Juifs déportés de France, 24 500 étaient français.\n\nLa police française a elle-même organisé la rafle du Vél d'Hiv. Qu'une majorité des Juifs de France ait survécu est vrai, mais selon l'historien Jacques Semelin, c'est « en dépit de Vichy, pas grâce à Vichy ».",
 detaille="La thèse d'un Pétain « protecteur » des Juifs français est réfutée par les travaux historiques, dans la continuité de Robert Paxton et Michael Marrus. Le 3 octobre 1940, le régime de Vichy promulgue un statut des Juifs qui vise aussi les Juifs français ; l'historien Laurent Joly le décrit comme un choix délibéré, non contraint par l'occupant.\n\nEnviron 74 500 à 76 000 Juifs ont été déportés de France, dont plus de 11 000 enfants et 24 500 Juifs français, selon Laurent Joly et le Mémorial de la Shoah. À l'été 1942, la rafle du Vél d'Hiv a été menée par la police française, et Vichy a livré des Juifs étrangers de zone sud. En 1995, Jacques Chirac a reconnu que l'occupant avait été « secondé » par l'État français.\n\nIl est vrai que les Juifs français ont été moins arrêtés que les étrangers et qu'environ trois quarts des Juifs de France ont survécu. Mais selon Jacques Semelin, c'est « en dépit de Vichy », pas grâce à lui. Réhabiliter Pétain sur ce point, c'est effacer la responsabilité d'un État qui a choisi l'antisémitisme.",
 empathie="Je comprends qu'on ait envie de croire que la France n'a pas été complice de ça. Mais les historiens sont unanimes : Vichy a persécuté les Juifs, y compris français. Ce qui honore la France, ce sont ceux qui les ont cachés, pas ceux qui les ont livrés.",
 legitimes=["Les Juifs français ont été proportionnellement moins arrêtés que les Juifs étrangers.", "Environ trois quarts des Juifs de France ont survécu à la Shoah."],
 contre=[
  ("Vichy a livré les étrangers pour sauver les Français.", "Le statut des Juifs visait aussi les Français, et 24 500 Juifs français ont été déportés ; les historiens réfutent cette thèse."),
  ("C'étaient les Allemands, pas la France.", "La rafle du Vél d'Hiv a été menée par la police française, et l'État a reconnu sa responsabilité en 1995."),
 ],
 questions=["Savais-tu que le statut des Juifs de 1940 visait aussi les Juifs français ?", "Qui a vraiment sauvé des Juifs pendant l'Occupation, selon toi ?"],
 limites=["Les chiffres de déportation varient légèrement selon les sources (74 500 à 76 000).", "Certaines sources lues sont des comptes rendus ou des notes de conférence d'historiens, et non les ouvrages eux-mêmes."],
 publics={'convaincus': "Les historiens qui ont travaillé dans les archives disent le contraire : le statut des Juifs de 1940 visait aussi les Français, sans que les Allemands l'aient demandé, et 24 500 Juifs français ont été déportés. Défendre Pétain là-dessus, ce n'est pas défendre la France : c'est défendre ceux qui ont livré des enfants.",
  'indecis': "Cette idée circule beaucoup, mais elle ne tient pas face aux travaux historiques. Vichy a persécuté les Juifs, y compris français, et la police française a organisé la rafle du Vél d'Hiv. Selon l'historien Jacques Semelin, ceux qui ont survécu l'ont fait en dépit de Vichy, pas grâce à lui."},
 a_actualiser='2028-12-31', raison="Fait historique stable ; vérifier l'accessibilité des sources.",
))

# 17 ── Fondateurs du FN ─────────────────────────────────────────────────────
FICHES.append(fiche(
 id='fn-fondateurs-collaboration', affirmation="Le Front national n'a jamais eu de lien avec d'anciens collaborateurs.", volet='politique', sous_theme='Droite et extrême droite',
 mots_cles=['front national', 'fn', 'fondateurs du fn', 'waffen ss', 'collaborateurs', 'ordre nouveau', '1972', 'pierre bousquet', 'milice'],
 verdict='contredit', fiabilite='etabli', stabilite='historique',
 resume="Faux. Le Front national est né en 1972 à l'initiative du mouvement Ordre nouveau. Parmi ses fondateurs figurait Pierre Bousquet, ancien de la division SS Charlemagne, qui fut son premier trésorier selon l'historien Nicolas Lebourg ; d'autres anciens de la Waffen-SS et un ancien milicien ont joué un rôle dans ses débuts. Le RN d'aujourd'hui n'est pas dirigé par ces hommes, mais l'histoire de ses origines est documentée.",
 contexte="La « dédiabolisation » du RN s'accompagne d'une relecture de l'histoire du parti, présenté comme un mouvement patriote sans lien avec l'extrême droite collaborationniste.",
 explication="Un parti peut changer de dirigeants et de discours ; son histoire, elle, ne change pas. Rappeler les origines du FN ne dit pas ce que pense chaque électeur du RN aujourd'hui, mais répond à une affirmation historique fausse.",
 sources=[LEBOURG_FN, RTBF_FN, FJJ_ON],
 faits=[
  fait("Selon l'historien Nicolas Lebourg, l'ancien de la division SS Charlemagne Pierre Bousquet fut le premier trésorier du Front national.", 'lebourg', '1972', 'France', "Un ancien de la Waffen-SS a occupé une fonction clé dès la fondation.", 'etabli'),
  fait("Selon la RTBF, d'anciens de la Waffen-SS comme Pierre Bousquet ont joué un rôle actif dans la création du FN, et François Brigneau, ancien membre de la Milice française sous Vichy, a figuré parmi ses premiers dirigeants.", 'rtbf_fn', '1972', 'France', "Le lien avec des collaborateurs n'est pas un cas isolé.", 'etabli'),
  fait("Selon une présentation de la Fondation Jean-Jaurès, le mouvement Ordre nouveau « fonda le Front national en 1972 » et en fut la « véritable colonne vertébrale idéologique et militante », sous le patronage de « grands anciens » passés par les mouvements nationalistes d'avant 1940 ou par la Révolution nationale de Vichy.", 'fjj_on', '1972', 'France', "Les origines du FN plongent dans l'extrême droite d'avant-guerre et de Vichy.", 'etabli'),
 ],
 court="Faux : selon l'historien Nicolas Lebourg, le premier trésorier du FN, Pierre Bousquet, était un ancien de la division SS Charlemagne, et d'autres anciens de la Waffen-SS et un ancien milicien ont participé à ses débuts en 1972.",
 moyen="L'histoire est documentée par les historiens : le FN est fondé en 1972 par le mouvement Ordre nouveau. Son premier trésorier, Pierre Bousquet, était un ancien de la division SS Charlemagne, selon l'historien Nicolas Lebourg.\n\nD'autres anciens de la Waffen-SS et un ancien de la Milice de Vichy ont participé aux débuts du parti. Le RN d'aujourd'hui a changé de nom et de dirigeants, mais dire qu'il n'y a « jamais eu de lien », c'est réécrire son histoire.",
 detaille="Le Front national est créé en 1972 à l'initiative d'Ordre nouveau, un mouvement d'extrême droite radicale qui en fut, selon une présentation de la Fondation Jean-Jaurès, la « colonne vertébrale idéologique et militante ». Jean-Marie Le Pen en prend la présidence.\n\nParmi les fondateurs figurent des hommes passés par la collaboration. Selon l'historien Nicolas Lebourg, Pierre Bousquet, ancien de la division SS Charlemagne, fut le premier trésorier du FN, et animait auparavant une revue avec un autre ancien Waffen-SS. La RTBF cite d'autres anciens de la Waffen-SS parmi les fondateurs actifs et présente François Brigneau comme un ancien membre de la Milice.\n\nCes faits ne disent pas ce que pensent les électeurs actuels du RN, ni ses dirigeants d'aujourd'hui. Mais un parti qui revendique son histoire doit l'assumer entière : la normalisation ne peut pas passer par l'effacement de ses origines.",
 empathie="Je comprends que beaucoup d'électeurs du RN ne se reconnaissent absolument pas dans cette histoire, et je ne t'en accuse pas. Mais c'est un fait historique : des anciens SS ont fondé le FN. On peut voter pour un parti en connaissant son passé.",
 legitimes=["Le FN n'a pas été fondé uniquement par d'anciens collaborateurs : Ordre nouveau comptait aussi de jeunes militants.", "Les dirigeants actuels du RN ne sont pas ces fondateurs, aujourd'hui décédés."],
 contre=[
  ("C'est de l'histoire ancienne, ça ne dit rien du RN d'aujourd'hui.", "C'est vrai pour les électeurs ; mais l'affirmation porte sur l'histoire du parti, et elle est fausse."),
  ("La gauche aussi a eu des collaborateurs.", "Des parcours individuels existent dans tous les camps ; la question ici est celle des fondateurs d'un parti, documentée par les historiens."),
 ],
 questions=["Savais-tu qui était le premier trésorier du Front national ?", "Pourquoi, selon toi, le parti a-t-il changé de nom ?"],
 limites=["Les sources lues sont un article d'historien, un article de presse et une présentation d'ouvrage ; la date exacte de fondation varie selon les sources (octobre ou novembre 1972).", "Le passé milicien de François Brigneau n'est attesté ici que par la RTBF."],
 publics={'convaincus': "Je ne te traite pas de nazi, et la plupart des électeurs du RN n'ont rien à voir avec ça. Mais l'histoire, c'est l'histoire : le premier trésorier du FN était un ancien de la division SS Charlemagne, selon les historiens. Un parti qui veut tourner la page doit commencer par la lire.",
  'indecis': "Le RN se présente aujourd'hui comme un parti comme les autres. Ses origines sont pourtant documentées : le FN a été fondé en 1972 par un mouvement d'extrême droite radicale, avec d'anciens Waffen-SS parmi ses fondateurs. Le connaître aide à juger son évolution en connaissance de cause."},
 a_actualiser='2028-12-31', raison="Fait historique stable ; vérifier l'accessibilité des sources.",
))

# 18 ── Colonisation ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='colonisation-routes-ecoles', affirmation="La colonisation a apporté des routes, des écoles et des hôpitaux.", volet='international', sous_theme='Colonisation et décolonisation',
 mots_cles=['colonisation', 'colonies', 'aspects positifs', 'rôle positif', 'routes écoles hôpitaux', 'algérie française', 'empire colonial', 'indigénat'],
 verdict='trompeur', fiabilite='etabli', stabilite='historique',
 resume="Des infrastructures ont été construites, mais d'abord au service de la colonie et des Européens. En Algérie, en 1954, 16,7 % des enfants « indigènes » de 6 à 14 ans étaient scolarisés, contre 85,4 % des enfants européens (Kamel Kateb, INED). Le travail forcé n'a été aboli dans les territoires d'outre-mer qu'en 1946. L'article de loi de 2005 sur le « rôle positif » de la colonisation a été abrogé en 2006.",
 contexte="Le « bilan positif de la colonisation » revient régulièrement dans le débat public, notamment depuis la loi de 2005 et dans les discours de l'extrême droite.",
 explication="Juger la colonisation sur les routes construites revient à oublier pour qui elles l'étaient, et à quel prix : conquête, statut d'infériorité juridique, travail forcé, accès très inégal à l'école et aux soins.",
 sources=[KATEB_ALGERIE, AN_COLO, AN_TRAVAIL_FORCE],
 faits=[
  fait("Selon le démographe Kamel Kateb (INED), en 1954, 16,7 % des enfants « indigènes » de 6 à 14 ans étaient scolarisés en Algérie, contre 85,4 % des enfants européens d'Algérie et 97,6 % des enfants en France.", 'kateb', '1954', 'Algérie', "En 1954, plus de huit enfants algériens « indigènes » sur dix n'allaient pas à l'école.", 'etabli', '16,7 %'),
  fait("Selon la même étude, le taux de scolarisation des enfants « indigènes » était de 3,8 % en 1911, 7,9 % en 1936 et 9,8 % en 1948.", 'kateb', '1911-1948', 'Algérie', "Des écoles ont bien été construites, mais très lentement et très inégalement.", 'etabli', '3,8 %'),
  fait("Selon le ministère de l'Éducation nationale, l'alinéa de la loi du 23 février 2005 sur « le rôle positif de la présence française outre-mer » a été jugé réglementaire par le Conseil constitutionnel puis abrogé par décret le 15 février 2006.", 'an_colo', '2005-2006', 'France', "L'État a renoncé à imposer un « bilan positif » de la colonisation dans l'enseignement.", 'etabli'),
  fait("Selon un document de l'Assemblée nationale, la loi du 11 avril 1946, dite loi Houphouët-Boigny, a posé le principe de l'interdiction absolue du travail forcé dans les territoires d'outre-mer.", 'an_travail_force', '1946', 'Territoires d\'outre-mer', "Le travail forcé a existé dans les colonies françaises jusqu'en 1946.", 'etabli'),
 ],
 court="Trompeur : des routes et des écoles ont été construites, mais pour la colonie. En Algérie, en 1954, seuls 16,7 % des enfants « indigènes » allaient à l'école, contre 85,4 % des enfants européens (INED), et le travail forcé n'a été aboli qu'en 1946.",
 moyen="Des routes, des écoles et des hôpitaux ont été construits, personne ne le nie. Mais pour qui ? En Algérie, en 1954, seuls 16,7 % des enfants « indigènes » étaient scolarisés, contre 85,4 % des enfants européens.\n\nLes infrastructures servaient d'abord l'économie coloniale. Et elles allaient avec la conquête, l'inégalité des droits et, jusqu'en 1946, le travail forcé dans les territoires d'outre-mer. On ne fait pas le bilan d'un système en ne comptant que ses routes.",
 detaille="L'argument des « routes, écoles et hôpitaux » repose sur un fait réel : des infrastructures ont été construites dans les colonies. Mais il omet à qui elles profitaient. Le démographe Kamel Kateb (INED) montre qu'en Algérie, le taux de scolarisation des enfants « indigènes » de 6 à 14 ans était de 3,8 % en 1911, 9,8 % en 1948 et 16,7 % en 1954, contre 85,4 % pour les enfants européens d'Algérie.\n\nLa colonisation reposait sur une inégalité juridique : les colonisés n'avaient pas les mêmes droits, et le travail forcé n'a été aboli dans les territoires d'outre-mer que par la loi du 11 avril 1946. En 2005, une loi a voulu faire reconnaître dans les programmes scolaires le « rôle positif » de la présence française outre-mer ; après l'avis du Conseil constitutionnel, cet alinéa a été abrogé en 2006.\n\nLes historiens étudient la colonisation dans toutes ses dimensions, y compris les transformations qu'elle a entraînées. Mais la réduire à un bilan comptable de routes, c'est effacer les violences, l'exploitation et l'absence de droits des populations colonisées.",
 empathie="Je comprends que des familles, notamment de rapatriés, aient un attachement à ce passé et à ce qui a été construit. Mais il faut aussi regarder l'autre côté : en 1954, la grande majorité des enfants algériens n'allaient pas à l'école. Les deux mémoires méritent d'être entendues.",
 legitimes=["Des infrastructures, des écoles et des hôpitaux ont effectivement été construits dans les colonies.", "La scolarisation des enfants colonisés a progressé au XXe siècle, même lentement."],
 contre=[
  ("Sans la France, ils n'auraient rien eu.", "C'est une hypothèse invérifiable ; ce qui est documenté, c'est que l'accès à l'école est resté très inégal jusqu'à la fin de la colonisation."),
  ("Il faut arrêter la repentance.", "Connaître les faits n'est pas de la repentance : c'est la condition d'une histoire commune honnête."),
 ],
 questions=["Sais-tu quelle part des enfants algériens allait à l'école en 1954 ?", "Jusqu'à quand le travail forcé a-t-il existé dans les colonies françaises ?"],
 limites=["Les données de scolarisation portent sur l'Algérie et ne valent pas pour toutes les colonies.", "La fiche ne détaille pas les aspects sanitaires, faute de source lue sur ce point."],
 publics={'convaincus': "Les routes ont existé, d'accord. Mais en 1954, en Algérie, plus de huit enfants « indigènes » sur dix n'allaient pas à l'école, contre presque tous les enfants européens. Une école qu'on ne laisse pas fréquenter, ce n'est pas un cadeau, c'est une vitrine.",
  'indecis': "Il y a eu des constructions, c'est vrai, et la mémoire de ceux qui ont vécu là-bas compte. Mais les chiffres de l'INED montrent un accès à l'école très inégal, et le travail forcé n'a été aboli qu'en 1946. Un bilan honnête doit tout regarder."},
 a_actualiser='2028-12-31', raison="Fait historique stable ; vérifier l'accessibilité des sources.",
))

# 19 ── RN et Russie ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-russie-liens', affirmation="Les liens du RN avec la Russie, c'est de la propagande.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['rn', 'russie', 'poutine', 'prêt russe', 'banque russe', 'ingérences', 'crimée', 'marine le pen', 'rassemblement national'],
 verdict='contredit', fiabilite='etabli',
 resume="Les liens sont documentés par un rapport parlementaire de 2023 : un prêt de 9,4 millions d'euros contracté en 2014 auprès d'une banque tchéco-russe, racheté ensuite par une entreprise du complexe militaro-industriel russe, et des prises de position favorables à Moscou, notamment sur la Crimée. Le rapport n'établit pas de contrepartie prouvée, et le RN annonce avoir remboursé le prêt en 2023.",
 contexte="Depuis l'invasion de l'Ukraine en 2022, le RN rejette toute accusation de proximité avec le Kremlin et la présente comme une manœuvre de ses adversaires.",
 explication="Un lien financier ou politique n'est pas forcément une ingérence prouvée. Mais un parti qui emprunte à une banque russe et relaie des positions du Kremlin pose une question légitime d'indépendance.",
 sources=[AN_INGERENCES, LCP_INGERENCES, LOCAL_PRET],
 faits=[
  fait("Selon le rapport de la commission d'enquête de l'Assemblée nationale sur les ingérences étrangères (2023), le prêt de 9,4 millions d'euros contracté en 2014 auprès de la First Czech Russian Bank a été racheté par l'entreprise russe Aviazapchast, qui en a rééchelonné le remboursement jusqu'en 2028.", 'an_ingerences', '2014-2023', 'France', "Le financement russe du parti est un fait établi.", 'etabli', '9,4 M€'),
  fait("Selon le même rapport, cette entreprise appartient au complexe militaro-industriel russe, et la Commission nationale des comptes de campagne a jugé que ce prêt constituait un « avantage certain et conséquent ».", 'an_ingerences', '2023', 'France', "Le créancier n'était pas un acteur neutre.", 'etabli'),
  fait("Selon LCP, la rapporteure a qualifié le parti de « relais assez affirmé, assez constant » des positions russes, notamment sur l'annexion de la Crimée en 2014 ; le président RN de la commission a affirmé que « rien n'a permis d'établir une ingérence au cours des auditions ».", 'lcp_ingerences', '2023', 'France', "Le rapport documente un alignement politique, sans preuve de contrepartie.", 'interpretation'),
  fait("Selon l'AFP, le RN a annoncé en septembre 2023 avoir remboursé par anticipation les 6,1 millions d'euros restants du prêt.", 'local_pret', '2023', 'France', "Le prêt est remboursé, selon le parti.", 'etabli', '6,1 M€'),
 ],
 court="Faux : un rapport de l'Assemblée nationale (2023) documente un prêt de 9,4 millions d'euros d'une banque tchéco-russe, racheté par une entreprise du complexe militaro-industriel russe, et des positions alignées sur Moscou. Il n'établit pas de contrepartie, et le RN dit avoir remboursé en 2023.",
 moyen="Ce n'est pas une rumeur : en 2014, le Front national a emprunté 9,4 millions d'euros à une banque tchéco-russe. La dette a ensuite été rachetée par une entreprise du complexe militaro-industriel russe, selon un rapport de l'Assemblée nationale de 2023.\n\nLe même rapport décrit des positions du parti favorables à Moscou, notamment sur la Crimée. Il faut être précis : il n'établit pas de contrepartie prouvée, et le RN annonce avoir remboursé le prêt en 2023. Mais parler de « propagande », c'est nier des faits établis.",
 detaille="La commission d'enquête de l'Assemblée nationale sur les ingérences étrangères a publié son rapport en juin 2023. Elle y rappelle que le prêt de 9,4 millions d'euros contracté en 2014 par le Front national auprès de la First Czech Russian Bank, alors contrôlée par un oligarque russe, a été racheté après la faillite de la banque par Aviazapchast, entreprise du complexe militaro-industriel russe, qui en a rééchelonné le remboursement jusqu'en 2028. La CNCCFP y voyait un « avantage certain et conséquent ».\n\nLe rapport décrit aussi des prises de position et des déplacements d'élus favorables à Moscou, notamment sur l'annexion de la Crimée. La rapporteure parle d'un « relais assez affirmé, assez constant ». Le président de la commission, élu RN, conteste et affirme qu'aucune ingérence n'a été établie ; le rapport a été adopté par 11 voix contre 5.\n\nSelon l'AFP, le RN a annoncé en septembre 2023 avoir remboursé par anticipation le reste du prêt. La conclusion honnête : il n'y a pas de preuve publique de contrepartie, mais il y a bien eu un financement russe et un alignement politique documenté. Ce ne sont pas des inventions.",
 empathie="Je comprends que tu voies ça comme une attaque politique, et le rapport a été voté par les adversaires du RN. Mais le prêt russe, lui, est un fait reconnu par le parti lui-même. On peut en discuter sans parler de propagande.",
 legitimes=["Le rapport n'établit pas de contrepartie prouvée au prêt.", "Le RN affirme avoir remboursé le prêt en 2023, et le président de la commission conteste les conclusions."],
 contre=[
  ("Aucune banque française ne voulait leur prêter.", "C'est l'explication donnée par le parti ; elle ne change pas l'origine russe du créancier, ni l'alignement de positions décrit par le rapport."),
  ("Le rapport a été écrit par leurs adversaires.", "Il a été adopté par la commission, et le prêt est un fait reconnu par le RN lui-même."),
 ],
 questions=["Savais-tu que le prêt de 2014 a été racheté par une entreprise de l'armement russe ?", "Un parti qui dépend d'un créancier étranger est-il totalement libre ?"],
 limites=["Le rapport de 2023 est contesté par le RN et a été adopté par la majorité de l'époque.", "Les positions du RN sur la Russie ont évolué depuis 2022 ; la fiche ne les détaille pas."],
 publics={'convaincus': "Je ne dis pas que le RN est payé par Poutine, le rapport ne le prouve pas. Mais le prêt de 9,4 millions venu d'une banque russe, puis racheté par une entreprise de l'armement russe, ce n'est pas de la propagande : le parti l'a lui-même reconnu et remboursé. Tu as le droit de te demander si c'est compatible avec l'indépendance de la France.",
  'indecis': "Le sujet est souvent caricaturé des deux côtés. Les faits établis : un prêt russe de 9,4 millions d'euros en 2014 et des positions favorables à Moscou décrites par un rapport parlementaire. Aucune contrepartie n'est prouvée, et le RN dit avoir remboursé en 2023."},
 a_actualiser='2027-06-30',
))

# 20 ── Juges de gauche ──────────────────────────────────────────────────────
FICHES.append(fiche(
 id='juges-de-gauche', affirmation="Les juges sont tous de gauche.", volet='securite', sous_theme='Justice pénale',
 mots_cles=['juges', 'magistrats', 'juges rouges', 'juges de gauche', 'syndicat de la magistrature', 'gouvernement des juges', 'mur des cons', 'justice politisée'],
 verdict='contredit', fiabilite='etabli',
 resume="Non. Au moins la moitié des quelque 9 500 magistrats ne sont pas syndiqués. Aux élections professionnelles de février 2026, l'USM, syndicat majoritaire non classé à gauche, obtient 61 % des voix, le Syndicat de la magistrature (à gauche) 25 %, et Unité Magistrats-FO, aux positions conservatrices, 12,5 %. L'affaire du « mur des cons » est réelle et a valu une condamnation à l'ancienne présidente du SM, mais elle ne dit rien de l'ensemble des juges.",
 contexte="L'accusation de « juges rouges » ou de « gouvernement des juges » revient après des décisions visant des responsables politiques, notamment la condamnation de Marine Le Pen en 2025.",
 explication="Les magistrats ont le droit de se syndiquer, mais ils doivent juger avec impartialité, sous le contrôle des voies de recours et du Conseil supérieur de la magistrature. L'appartenance à un syndicat ne permet pas, à elle seule, de mettre en cause l'impartialité d'un juge.",
 sources=[JUSTICE_ELECTIONS, PS_SM, ACTU_JUR_MUR, PS_IMPART],
 faits=[
  fait("Selon le ministère de la Justice, aux élections professionnelles des magistrats de février 2026, l'USM a obtenu 60,99 % des voix, le Syndicat de la magistrature 25,03 %, Unité Magistrats-FO 12,51 % et la CFDT 1,46 %, avec une participation de 62,75 %.", 'justice_elec', '2026', 'France', "Le syndicat classé à gauche est minoritaire chez les magistrats.", 'etabli', '25 %'),
  fait("Selon Public Sénat, la France compte environ 9 500 magistrats, dont au moins la moitié ne sont pas syndiqués ; le Syndicat de la magistrature compte « pas beaucoup plus de 1000 » adhérents, l'USM environ 2 500.", 'ps_sm', '2025', 'France', "La grande majorité des juges n'adhère pas au syndicat de gauche.", 'estimation', '9 500'),
  fait("Selon Public Sénat, le Conseil supérieur de la magistrature affirme que la liberté syndicale est reconnue aux magistrats et que l'appartenance syndicale ne peut, à elle seule, fonder une remise en cause de l'impartialité ; le Sénat a rappelé en 2023 le respect du principe d'impartialité pour les magistrats syndiqués.", 'ps_impart', '2023', 'France', "L'impartialité s'impose à tous les juges, syndiqués ou non.", 'etabli'),
  fait("Selon Public Sénat, en 2013, un panneau de photos de personnalités, surtout de droite, a été découvert au local du Syndicat de la magistrature (« mur des cons ») ; selon Actu-Juridique, son ancienne présidente a été condamnée en 2019 pour injure publique envers un plaignant, les autres ayant été déboutés.", 'actujur_mur', '2013-2019', 'France', "Un fait réel, sanctionné, qui ne concerne qu'un syndicat minoritaire.", 'etabli'),
 ],
 court="Faux : au moins la moitié des magistrats ne sont pas syndiqués, et en 2026 le syndicat classé à gauche a obtenu 25 % des voix, contre 61 % à l'USM et 12,5 % à un syndicat conservateur (ministère de la Justice).",
 moyen="Les chiffres ne collent pas : sur environ 9 500 magistrats, au moins la moitié ne sont syndiqués nulle part. Aux élections professionnelles de 2026, le Syndicat de la magistrature, classé à gauche, a obtenu 25 % des voix ; l'USM, majoritaire, 61 % ; et un syndicat conservateur, 12,5 %, en forte progression.\n\nL'affaire du « mur des cons » a bien existé et a été sanctionnée par la justice elle-même. Mais elle concerne un syndicat minoritaire. Et un jugement se conteste en appel, pas en accusant les juges d'être « rouges ».",
 detaille="La France compte environ 9 500 magistrats, dont au moins la moitié ne sont pas syndiqués selon Public Sénat. Aux élections professionnelles de février 2026, l'Union syndicale des magistrats (USM), majoritaire, a obtenu 60,99 % des voix ; le Syndicat de la magistrature (SM), classé à gauche, 25,03 % ; Unité Magistrats-FO, aux positions conservatrices, 12,51 %. Aux élections au Conseil supérieur de la magistrature de 2022, le SM avait obtenu un tiers des voix.\n\nL'image des « juges rouges » s'appuie sur des faits réels : le SM existe et prend des positions politiques, et l'affaire du « mur des cons » (2013) a valu à son ancienne présidente une condamnation pour injure publique. Mais ce syndicat est minoritaire, et l'appartenance syndicale ne permet pas, selon le Conseil supérieur de la magistrature, de mettre en cause à elle seule l'impartialité d'un juge.\n\nLes décisions de justice peuvent être critiquées et contestées par les voies de recours. Discréditer l'ensemble des juges parce qu'une décision déplaît fragilise l'indépendance de la justice, qui protège aussi ceux qui l'attaquent.",
 empathie="Je comprends qu'on soit choqué quand un juge prend une décision qui semble aller contre ses idées. Mais les chiffres montrent que la plupart des juges ne sont pas de gauche, et beaucoup ne sont syndiqués nulle part. Si on n'est pas d'accord avec une décision, il y a l'appel.",
 legitimes=["Le Syndicat de la magistrature, classé à gauche, représente environ un quart des voix aux élections professionnelles.", "L'affaire du « mur des cons » a donné lieu à une condamnation définitive de l'ancienne présidente du SM."],
 contre=[
  ("Les décisions contre la droite prouvent qu'ils sont de gauche.", "Les décisions sont prises par des formations de juges souvent non syndiqués et peuvent être contestées en appel puis en cassation."),
  ("Le mur des cons prouve tout.", "Il concerne un syndicat minoritaire, et son auteure a été condamnée par d'autres juges."),
 ],
 questions=["Sais-tu combien de magistrats votent pour le Syndicat de la magistrature ?", "Si un juge ne pouvait plus juger un responsable politique sans être accusé d'être partisan, qui en profiterait ?"],
 limites=["Aucune enquête fiable sur les opinions politiques individuelles des magistrats n'a été trouvée.", "Les résultats électoraux mesurent les votes syndicaux, pas les opinions."],
 publics={'convaincus': "Si les juges étaient tous de gauche, le syndicat de gauche ne ferait pas 25 % aux élections de 2026, derrière l'USM à 61 %, avec un syndicat conservateur qui progresse. Le « mur des cons » était une faute, et la justice l'a sanctionnée. Une décision te déplaît ? C'est à ça que sert l'appel.",
  'indecis': "La défiance envers la justice se comprend après des décisions médiatisées. Mais les magistrats ne forment pas un bloc : le syndicat classé à gauche est minoritaire, et au moins la moitié des juges ne sont pas syndiqués. Leur impartialité est contrôlée par l'appel et le Conseil supérieur de la magistrature."},
 a_actualiser='2027-06-30',
))

# 21 ── Niveau scolaire ──────────────────────────────────────────────────────
FICHES.append(fiche(
 id='niveau-scolaire-effondre', affirmation="Le niveau scolaire s'effondre.", volet='services', sous_theme='École publique',
 mots_cles=['niveau scolaire', 'niveau baisse', 's effondre', 'pisa', 'élèves', 'mathématiques', 'école', 'baisse du niveau', 'timss'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="La baisse est réelle : en mathématiques, la chute observée en France entre 2018 et 2022 est « sans précédent » selon l'OCDE (-21 points), et 17 % des élèves de 4e n'atteignent pas le niveau bas de TIMSS en 2023, contre 3 % en 1995. Mais la baisse touche presque toute l'OCDE, la France reste dans la moyenne de PISA, et le fait le plus marquant est le poids de l'origine sociale, plus fort en France qu'ailleurs.",
 contexte="Le déclin de l'école est un thème fort de la droite et de l'extrême droite, souvent associé à l'immigration, au « pédagogisme » ou au « wokisme ».",
 explication="Les enquêtes internationales (PISA pour les jeunes de 15 ans, TIMSS en 4e) mesurent les compétences des élèves avec les mêmes tests d'un pays et d'une année à l'autre. Elles permettent de comparer, mais pas, à elles seules, d'identifier les causes.",
 sources=[OCDE_PISA, PS_PISA, DEPP_TIMSS],
 faits=[
  fait("Selon l'OCDE, les résultats PISA 2022 de la France sont en baisse en mathématiques et en compréhension de l'écrit par rapport à 2018, et parmi les plus bas jamais mesurés ; en mathématiques, la baisse récente est « sans précédent ».", 'ocde_pisa', '2022', 'France', "La baisse du niveau est documentée.", 'etabli'),
  fait("Selon Public Sénat, d'après l'OCDE, le score français en mathématiques a chuté de 21 points, à 474, quand la moyenne de l'OCDE perdait 15 points, à 472 ; la baisse n'est attribuable qu'en partie à la pandémie.", 'ps_pisa', '2018-2022', 'France et OCDE', "La France baisse plus que la moyenne, mais reste à son niveau.", 'etabli', '474'),
  fait("Selon la DEPP, en 2023, 17 % des élèves de 4e n'atteignent pas le niveau bas de TIMSS en mathématiques, contre 3 % en 1995 et 12 % en 2019 ; la France obtient 479 points, sous la moyenne des pays de l'OCDE et de l'UE participants (507).", 'depp_timss', '1995-2023', 'France', "La part des élèves en grande difficulté augmente.", 'etabli', '17 %'),
  fait("Selon l'OCDE, en mathématiques, l'écart entre élèves favorisés et défavorisés atteint 113 points en France, contre 93 en moyenne dans l'OCDE.", 'ocde_pisa', '2022', 'France et OCDE', "L'école française reproduit fortement les inégalités sociales.", 'etabli', '113 points'),
 ],
 court="En partie vrai : la chute en mathématiques est « sans précédent » selon l'OCDE, et 17 % des élèves de 4e sont sous le niveau bas de TIMSS. Mais la baisse touche presque toute l'OCDE, et le problème le plus marquant en France est le poids de l'origine sociale.",
 moyen="La baisse est réelle, il ne faut pas la nier : en mathématiques, la France a perdu 21 points dans PISA entre 2018 et 2022, une chute « sans précédent » selon l'OCDE. En 4e, la part d'élèves très faibles est passée de 3 % en 1995 à 17 % en 2023.\n\nMais deux nuances comptent. La baisse touche presque tous les pays de l'OCDE, et la France reste dans la moyenne. Surtout, l'écart entre enfants favorisés et défavorisés est plus fort en France qu'ailleurs : c'est là qu'il faut agir.",
 detaille="Les enquêtes internationales confirment un recul. Selon l'OCDE, les résultats PISA 2022 de la France sont parmi les plus bas jamais mesurés, avec une baisse « sans précédent » en mathématiques : -21 points, à 474, et -19 points en compréhension de l'écrit. La baisse n'est due qu'en partie à la pandémie. En 4e, l'enquête TIMSS 2023 place la France à 479 points, sous la moyenne des pays européens et de l'OCDE participants (507), avec 17 % d'élèves sous le niveau bas, contre 3 % en 1995.\n\nCette baisse n'est pas propre à la France : la moyenne de l'OCDE a perdu 15 points en mathématiques, et la France reste dans la moyenne de PISA. Ce qui distingue la France, c'est le poids de l'origine sociale : 113 points d'écart entre élèves favorisés et défavorisés en mathématiques, contre 93 en moyenne dans l'OCDE.\n\nLes causes font débat et ne sont pas établies par les sources lues, qui ne désignent pas l'immigration comme cause. La réponse passe par les moyens donnés aux écoles qui accueillent les élèves les plus défavorisés.",
 empathie="Tu as raison de t'inquiéter, les chiffres montrent une vraie baisse, surtout en maths. Mais ce n'est pas une fatalité française : presque tous les pays baissent. Ce qui est propre à la France, c'est que l'école dépend beaucoup trop du milieu social des parents.",
 legitimes=["La baisse du niveau en mathématiques est réelle et sans précédent selon l'OCDE.", "La part des élèves en grande difficulté augmente en 4e."],
 contre=[
  ("C'est à cause de l'immigration.", "Les sources lues désignent d'abord le poids de l'origine sociale ; aucune n'établit l'immigration comme cause de la baisse."),
  ("C'est la faute des profs.", "La baisse touche presque toute l'OCDE ; les causes font débat et ne se résument pas à un groupe professionnel."),
 ],
 questions=["Savais-tu que presque tous les pays de l'OCDE ont reculé en mathématiques ?", "Pourquoi, selon toi, le milieu social pèse-t-il plus en France qu'ailleurs ?"],
 limites=["Les enquêtes mesurent des compétences précises, pas l'ensemble des apprentissages.", "Les causes de la baisse ne sont pas établies par les sources lues."],
 publics={'convaincus': "Tu as raison, le niveau baisse, surtout en maths, et l'OCDE parle d'une chute sans précédent. Mais elle touche presque tous les pays riches, et ce qui distingue la France, c'est l'écart entre enfants riches et pauvres. Si tu veux remonter le niveau, il faut des moyens là où les élèves en ont le plus besoin, pas des boucs émissaires.",
  'indecis': "L'inquiétude est fondée : les enquêtes PISA et TIMSS montrent une vraie baisse. Mais la France reste dans la moyenne de l'OCDE, où presque tous les pays reculent. Le point faible français, c'est le poids de l'origine sociale sur les résultats."},
 a_actualiser='2027-06-30',
))

# 22 ── Chômeurs indemnisés ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='indemnisation-chomage-salaire', affirmation="Les chômeurs indemnisés gagnent plus qu'en travaillant.", volet='social', sous_theme='Chômage',
 mots_cles=['allocation chômage', 'chômeurs indemnisés', 'gagnent plus qu en travaillant', 'gagnent plus au chômage', 'indemnisation chômage', 'unédic', 'allocation supérieure au salaire'],
 verdict='trompeur', fiabilite='etabli',
 resume="Non en règle générale : l'allocation représente 57 à 75 % du salaire de référence, elle est en moyenne de 1 040 € nets par mois fin 2025, et une majorité d'allocataires touche moins que le SMIC net. Moins de la moitié des inscrits à France Travail sont indemnisés. Avant la réforme de 2021, certains parcours très morcelés pouvaient donner une allocation supérieure au salaire mensuel moyen antérieur : ce calcul a été changé.",
 contexte="L'idée que le chômage « paierait mieux que le travail » est utilisée pour justifier les réformes de l'assurance chômage et le durcissement des règles.",
 explication="L'allocation chômage est calculée sur l'ancien salaire : elle ne peut pas, en règle générale, le dépasser. Elle est temporaire, et seuls ceux qui ont assez travaillé y ont droit.",
 sources=[UNEDIC_MONTANT, UNEDIC_CALCUL, UNEDIC_INSCRITS, FT_TAUX, UNEDIC_2021],
 faits=[
  fait("Selon l'Unédic, l'allocation chômage est en moyenne de 1 040 € nets par mois au 4e trimestre 2025 ; 54 % des allocataires touchent moins de 1 000 € et une majorité touche moins que le SMIC net (1 426,30 €).", 'unedic_montant', '2025', 'France', "La plupart des chômeurs indemnisés touchent moins que le SMIC.", 'etabli', '1 040 €'),
  fait("Selon l'Unédic, l'allocation équivaut à 75 % du salaire journalier de référence pour les plus bas salaires et à 57 % pour les plus élevés, avec une dégressivité pouvant atteindre 30 % après six mois pour les allocations élevées des moins de 55 ans.", 'unedic_calcul', '2025', 'France', "On touche toujours moins que son ancien salaire de référence.", 'etabli', '57 à 75 %'),
  fait("Selon l'Unédic, en 2025, sur 5,7 millions de demandeurs d'emploi inscrits à France Travail, 2,6 millions étaient indemnisés.", 'unedic_inscrits', '2025', 'France', "Moins de la moitié des inscrits touchent une allocation.", 'etabli', '2,6 millions'),
  fait("Selon France Travail, avant la réforme de 2021, environ 21 % des ouvertures de droit donnaient une allocation mensuelle supérieure au salaire mensuel moyen antérieur, pour des parcours d'emploi très morcelés, en raison d'un calcul fondé sur les seuls jours travaillés.", 'ft_taux', '2015-2017', 'France', "Un cas particulier a existé : il faut le reconnaître.", 'etabli', '21 %'),
  fait("Selon l'Unédic, depuis le 1er octobre 2021, le salaire de référence est calculé sur les jours travaillés et non travaillés de la période, ce qui a changé ce mode de calcul.", 'unedic_2021', '2021', 'France', "Le cas des parcours morcelés a été modifié par la réforme.", 'etabli'),
 ],
 court="Faux en général : l'allocation vaut 57 à 75 % du salaire de référence, 1 040 € en moyenne fin 2025, et la majorité des allocataires touche moins que le SMIC net (Unédic). Un cas particulier pour des contrats très morcelés existait avant 2021 ; il a été corrigé.",
 moyen="L'allocation chômage est calculée sur l'ancien salaire et vaut entre 57 % et 75 % du salaire de référence. Fin 2025, elle était en moyenne de 1 040 € par mois, et plus de la moitié des allocataires touchait moins de 1 000 €.\n\nEt beaucoup de chômeurs ne touchent rien : 2,6 millions d'indemnisés sur 5,7 millions d'inscrits. Avant 2021, des personnes aux contrats très courts et dispersés pouvaient toucher plus que leur salaire mensuel moyen ; la réforme a changé ce calcul. Ce n'était pas le cas général.",
 detaille="L'allocation d'aide au retour à l'emploi est calculée sur le salaire journalier de référence. Selon l'Unédic, elle équivaut à 75 % de ce salaire pour les plus bas revenus et à 57 % pour les plus hauts, avec une dégressivité pour les allocations élevées après six mois. Au 4e trimestre 2025, l'allocation moyenne était de 1 040 € nets par mois ; 54 % des allocataires touchaient moins de 1 000 €, et une majorité moins que le SMIC net.\n\nLe chômage n'est pas un revenu garanti : en 2025, sur 5,7 millions d'inscrits à France Travail, 2,6 millions étaient indemnisés. Les autres n'ont pas ou plus de droits, ou travaillent en partie.\n\nIl a existé un cas particulier : avant 2021, le calcul fondé sur les seuls jours travaillés pouvait donner, pour des parcours très morcelés, une allocation supérieure au salaire mensuel moyen antérieur, pour environ 21 % des ouvertures de droit selon France Travail. La réforme de 2021 a modifié ce calcul. Généraliser ce cas pour dire que « le chômage paie mieux » est faux, et sert à justifier des baisses de droits qui touchent tous les chômeurs.",
 empathie="Je comprends qu'on puisse avoir l'impression que certains s'en sortent mieux au chômage. Mais en moyenne, un chômeur indemnisé touche 1 040 € par mois, moins que le SMIC, et pendant une durée limitée. Personne ne s'enrichit au chômage.",
 legitimes=["Avant 2021, certains parcours très morcelés donnaient une allocation supérieure au salaire mensuel moyen antérieur.", "Une petite part des allocataires (2 %) touche 3 000 € ou plus, d'anciens hauts salaires."],
 contre=[
  ("Mon voisin touche plus au chômage qu'en travaillant.", "C'était possible dans certains cas de contrats très courts avant 2021 ; le calcul a changé, et en règle générale l'allocation vaut 57 à 75 % du salaire de référence."),
  ("Les chômeurs touchent des fortunes.", "Seuls 2 % touchent 3 000 € ou plus, d'anciens cadres, avec une dégressivité de 30 % après six mois."),
 ],
 questions=["Sais-tu combien touche en moyenne un chômeur indemnisé ?", "Savais-tu que moins de la moitié des inscrits à France Travail sont indemnisés ?"],
 limites=["Aucune source lue ne chiffre la part actuelle des allocataires dont l'allocation dépasse le salaire mensuel antérieur.", "Les données sur les taux de remplacement supérieurs à 100 % datent de 2015-2017."],
 publics={'convaincus': "Regarde les chiffres de l'Unédic : 1 040 € par mois en moyenne, et plus de la moitié des chômeurs indemnisés touchent moins de 1 000 €. Le cas du chômeur qui gagne plus qu'en travaillant a existé pour des contrats très courts, et il a été supprimé en 2021. Si le chômage payait si bien, pourquoi moins de la moitié des inscrits touchent-ils quelque chose ?",
  'indecis': "Il a pu exister des cas où l'allocation dépassait le salaire moyen, pour des contrats très morcelés, avant la réforme de 2021. Mais en règle générale, l'allocation vaut 57 à 75 % de l'ancien salaire, et la majorité touche moins que le SMIC. Le chômage reste une perte de revenu."},
 a_actualiser='2027-06-30',
))

# 23 ── Prisons hôtels ───────────────────────────────────────────────────────
FICHES.append(fiche(
 id='prisons-hotels', affirmation="Les prisons françaises sont des hôtels.", volet='securite', sous_theme='Prisons',
 mots_cles=['prisons', 'prison', 'hôtels', 'club med', 'détenus', 'surpopulation carcérale', 'matelas au sol', 'télévision en prison', 'conditions de détention'],
 verdict='contredit', fiabilite='etabli',
 resume="Non. Au 1er octobre 2026, 90 937 personnes sont détenues pour 63 452 places : la densité atteint 143 % en moyenne et 178 % en maisons d'arrêt, et 8 959 détenus dorment sur un matelas au sol. En 2020, la Cour européenne des droits de l'homme a condamné la France pour traitements inhumains ou dégradants dans ses prisons. Les détenus peuvent louer une télévision et faire des achats, mais à leurs frais.",
 contexte="L'image de prisons confortables, avec télévision et salle de sport, est souvent opposée à toute amélioration des conditions de détention.",
 explication="Les détenus ont accès à certaines activités (travail, formation, sport) prévues par la loi pour préparer leur sortie. Mais la plupart vivent dans des maisons d'arrêt surpeuplées, à plusieurs dans des cellules prévues pour moins de personnes.",
 sources=[JUSTICE_INCARC, SENAT_CGLPL, LCP_CGLPL, JUSTICE_DETENTION],
 faits=[
  fait("Selon le ministère de la Justice, au 1er octobre 2026, 90 937 personnes sont détenues pour 63 452 places opérationnelles ; la densité carcérale est de 143,3 %, et de 178,0 % en maisons d'arrêt.", 'justice_incarc', '2026', 'France', "Les prisons sont pleines bien au-delà de leur capacité.", 'etabli', '143,3 %'),
  fait("Selon le ministère de la Justice, 8 959 détenus dorment sur un matelas au sol au 1er octobre 2026, contre 5 895 un an plus tôt.", 'justice_incarc', '2025-2026', 'France', "La surpopulation s'aggrave rapidement.", 'etabli', '8 959'),
  fait("Selon le Sénat, la Cour européenne des droits de l'homme a condamné la France le 30 janvier 2020 (J.M.B. et autres c. France) pour traitements inhumains ou dégradants dans ses prisons et pour absence de recours effectif.", 'senat_cglpl', '2020', 'France', "Une juridiction internationale a jugé les conditions de détention indignes.", 'etabli'),
  fait("Selon la Contrôleure générale des lieux de privation de liberté (rapport 2023, rapporté par LCP), surveillants et détenus vivent « l'abandon, l'inertie de l'Etat », avec des taux d'occupation atteignant 250 % dans certains établissements et des invasions de punaises de lit.", 'lcp_cglpl', '2023', 'France', "Les conditions dégradent aussi le travail des surveillants.", 'etabli', '250 %'),
  fait("Selon le ministère de la Justice, les personnes détenues ont accès à des activités : travail, formation professionnelle, enseignement, sport et activités socio-culturelles.", 'justice_detention', '2025', 'France', "Ces activités existent et visent la réinsertion, mais elles ne font pas des prisons des hôtels.", 'etabli'),
 ],
 court="Faux : 90 937 détenus pour 63 452 places au 1er octobre 2026, 178 % de densité en maisons d'arrêt et 8 959 matelas au sol (ministère de la Justice). La France a été condamnée en 2020 par la CEDH pour traitements inhumains ou dégradants.",
 moyen="Les chiffres du ministère de la Justice disent l'inverse : au 1er octobre 2026, il y a 90 937 détenus pour 63 452 places, et 8 959 personnes dorment sur un matelas posé par terre. Dans les maisons d'arrêt, la densité atteint 178 %.\n\nEn 2020, la Cour européenne des droits de l'homme a condamné la France pour traitements inhumains ou dégradants dans ses prisons. Oui, les détenus peuvent avoir une télévision ou faire du sport, mais ils paient la télévision, et ces activités servent à préparer leur sortie.",
 detaille="Au 1er octobre 2026, selon le ministère de la Justice, 90 937 personnes sont détenues pour 63 452 places opérationnelles, soit une densité de 143,3 %, et de 178 % dans les maisons d'arrêt, où sont les prévenus et les courtes peines. 8 959 détenus dorment sur un matelas au sol, contre 5 895 un an plus tôt, et 57 292 sont hébergés dans un établissement occupé à plus de 150 %.\n\nLa Cour européenne des droits de l'homme a condamné la France le 30 janvier 2020 pour violation de l'interdiction des traitements inhumains ou dégradants et pour absence de recours effectif. La Contrôleure générale des lieux de privation de liberté décrit des établissements à 250 % d'occupation, des punaises de lit, et des surveillants qui vivent comme les détenus « l'abandon » de l'État.\n\nLes détenus ont accès au travail, à la formation, à l'enseignement et au sport, prévus par la loi pour préparer la réinsertion ; la location d'une télévision et les achats sont à leur charge. Des prisons indignes ne rendent pas la société plus sûre : elles abîment les détenus, les surveillants, et préparent mal la sortie.",
 empathie="Je comprends la colère quand on pense aux victimes et qu'on entend parler de télé en cellule. Mais la réalité, c'est des cellules surpeuplées, des matelas par terre, et une condamnation par la Cour européenne. Et ces détenus ressortiront un jour : mieux vaut qu'ils sortent préparés.",
 legitimes=["Les détenus ont accès à des activités, au sport et peuvent louer une télévision.", "La colère des victimes face à certaines peines est compréhensible."],
 contre=[
  ("Ils ont la télé et la salle de sport.", "La télévision est louée à leurs frais, et les activités prévues par la loi visent la réinsertion ; la majorité vit dans des établissements surpeuplés."),
  ("Ils n'ont qu'à ne pas commettre de crimes.", "La peine, c'est la privation de liberté ; des conditions indignes ont été jugées contraires aux droits fondamentaux par la CEDH."),
 ],
 questions=["Savais-tu que près de 9 000 détenus dorment sur un matelas au sol ?", "Dans quel état veux-tu qu'un détenu sorte de prison, puisqu'il en sortira ?"],
 limites=["Les conditions varient beaucoup entre maisons d'arrêt et établissements pour peine.", "Le prix de location d'une télévision n'a pas pu être vérifié dans une source officielle lue."],
 publics={'convaincus': "Un hôtel où des milliers de clients dorment sur un matelas posé par terre, je n'en connais pas. Ce sont les chiffres du ministère de la Justice : près de 9 000 matelas au sol. Et la France a été condamnée par la Cour européenne pour traitements dégradants. Vouloir des peines fermes, c'est une chose ; croire qu'elles sont douces, c'en est une autre.",
  'indecis': "On entend souvent parler de la télé en prison, et elle existe, payée par les détenus. Mais la surpopulation atteint 178 % dans les maisons d'arrêt, et la France a été condamnée par la Cour européenne des droits de l'homme. Des prisons indignes préparent mal la sortie, et donc la sécurité de tous."},
 a_actualiser='2027-03-31', raison="Statistiques mensuelles de la population carcérale.",
))

# 24 ── Seine-Saint-Denis ────────────────────────────────────────────────────
FICHES.append(fiche(
 id='seine-saint-denis-aides', affirmation="La Seine-Saint-Denis vit des aides de l'État.", volet='services', sous_theme='Services publics locaux',
 mots_cles=['seine saint denis', '93', 'neuf trois', 'banlieue', 'vit des aides', 'quartiers', 'assistés', 'département le plus pauvre'],
 verdict='trompeur', fiabilite='interpretation',
 resume="La Seine-Saint-Denis est le département le plus pauvre de métropole (28,4 % de pauvreté en 2021), et 22 % des allocataires de la Caf y vivent uniquement de prestations, contre 15 % en France. Mais un rapport parlementaire de 2018 montre qu'à besoins égaux, l'État y est moins présent : moins d'enseignants remplacés, policiers moins expérimentés, délais de justice beaucoup plus longs. Et le département était le 3e contributeur national de TVA.",
 contexte="Le « 93 » sert souvent de symbole des banlieues « assistées » dans les discours sur l'immigration et l'insécurité.",
 explication="Un territoire pauvre reçoit davantage de prestations sociales, qui dépendent des revenus de ses habitants. Mais les services publics (écoles, police, justice) relèvent de choix de l'État, et ils peuvent être moins bien dotés là où les besoins sont les plus grands.",
 sources=[INSEE_TERR, CAF93, AN_SSD, PS_SSD],
 faits=[
  fait("Selon l'Insee, le taux de pauvreté de la Seine-Saint-Denis était de 28,4 % en 2021, contre 15,3 % pour l'ensemble du champ étudié.", 'insee_terr', '2021', 'Seine-Saint-Denis', "C'est le département le plus pauvre de métropole.", 'etabli', '28,4 %'),
  fait("Selon la Caf de la Seine-Saint-Denis, 58 % de la population est couverte par au moins une prestation légale, et 22 % des allocataires ont des ressources composées en totalité de prestations, contre 15 % au niveau national.", 'caf93', '2024', 'Seine-Saint-Denis', "La dépendance aux prestations est plus forte qu'ailleurs : c'est un fait.", 'etabli', '22 %'),
  fait("Selon le rapport parlementaire Cornut-Gentille et Kokouendo (2018), 51 % des absences d'enseignants du premier degré étaient remplacées en Seine-Saint-Denis en 2015-2016, contre 78 % en France, et le délai d'audiencement au tribunal d'instance d'Aubervilliers était de douze mois, contre deux à Paris.", 'an_ssd', '2015-2018', 'Seine-Saint-Denis', "À besoins plus élevés, les services de l'État y sont moins présents.", 'etabli', '51 %'),
  fait("Selon le même rapport, la Seine-Saint-Denis est le 3e contributeur national de TVA ; il note aussi que l'État y « surinvestit » dans certains dispositifs prioritaires, sans résultats suffisants.", 'an_ssd', '2018', 'Seine-Saint-Denis', "Le département produit beaucoup de richesse, et l'action de l'État y est à la fois insuffisante et mal ciblée.", 'etabli'),
  fait("Selon le rapporteur (Public Sénat), « à besoins équivalents, la Seine-Saint-Denis n'est pas traitée de manière équitable » : 65 % d'enseignants néo-titulaires contre 21 % en France, et des policiers « moins nombreux, mais aussi moins expérimentés ».", 'ps_ssd', '2018', 'Seine-Saint-Denis', "Le département a moins de moyens expérimentés là où il en faudrait plus.", 'etabli', '65 %'),
 ],
 court="Trompeur : la Seine-Saint-Denis est le département le plus pauvre de métropole, donc ses habitants touchent plus de prestations. Mais un rapport parlementaire de 2018 montre qu'à besoins égaux, l'État y est moins présent (écoles, police, justice), et le département était 3e contributeur national de TVA.",
 moyen="C'est vrai, la Seine-Saint-Denis est pauvre : 28,4 % de pauvreté, et beaucoup de familles dépendent des prestations. Mais « vivre des aides » oublie l'autre moitié du tableau.\n\nUn rapport parlementaire de 2018, écrit par un député LR et un député de la majorité, montre qu'à besoins égaux, l'État y est moins présent : enseignants moins remplacés et moins expérimentés, policiers moins nombreux, un an d'attente au tribunal contre deux mois à Paris. Et le département était le 3e contributeur national de TVA.",
 detaille="La Seine-Saint-Denis est le département le plus pauvre de métropole : 28,4 % de pauvreté en 2021 selon l'Insee. Selon la Caf, 58 % de la population est couverte par au moins une prestation, et 22 % des allocataires vivent uniquement de prestations, contre 15 % en moyenne. Ces chiffres traduisent la pauvreté de ses habitants : les prestations dépendent des revenus.\n\nLe rapport parlementaire de François Cornut-Gentille (LR) et Rodrigue Kokouendo (LREM), en 2018, montre que les services de l'État y sont moins bien dotés à besoins égaux : remplacement des enseignants absents à 51 % contre 78 % en France, 65 % d'enseignants néo-titulaires contre 21 %, policiers moins nombreux et moins expérimentés, douze mois de délai au tribunal d'Aubervilliers contre deux à Paris. Le rapport parle d'une République « en échec » et d'un traitement inéquitable.\n\nLe même rapport note que l'État « surinvestit » dans certains dispositifs prioritaires sans résultats suffisants : l'argent n'est pas toujours là où il faudrait. Il rappelle aussi que le département est le 3e contributeur national de TVA. Ce n'est pas un territoire qui vit des autres : c'est un territoire pauvre, actif, et mal servi.",
 empathie="Je comprends que l'image du 93 fasse peur ou agace. Mais les habitants y ont moins de profs expérimentés, moins de policiers et des tribunaux engorgés, selon un rapport écrit par un député de droite. On ne peut pas leur reprocher de mal s'en sortir si l'État ne fait pas sa part.",
 legitimes=["La part des habitants dépendant des prestations est nettement plus élevée qu'ailleurs.", "Le rapport de 2018 note aussi que l'État « surinvestit » dans certains dispositifs sans résultats suffisants."],
 contre=[
  ("Avec tout l'argent qu'on y met, ça devrait aller mieux.", "Le rapport de 2018 montre qu'à besoins égaux, les services régaliens (école, police, justice) y sont moins bien dotés, même si certains dispositifs sont coûteux et peu efficaces."),
  ("Ils ne travaillent pas.", "Le département est le 3e contributeur national de TVA ; la pauvreté de ses habitants n'en fait pas un territoire inactif."),
 ],
 questions=["Savais-tu qu'un rapport d'un député LR concluait que la Seine-Saint-Denis était moins bien traitée par l'État ?", "Si l'école y a les enseignants les moins expérimentés, à qui la faute ?"],
 limites=["Le rapport parlementaire date de 2018 ; ses données (2015-2017) ne sont peut-être plus à jour.", "Aucune donnée fiable sur la création d'entreprises n'a été lue."],
 publics={'convaincus': "Les gens du 93 touchent plus d'aides parce qu'ils sont plus pauvres, c'est mécanique. Mais un député LR a montré en 2018 qu'à besoins égaux, l'État y met moins de profs expérimentés, moins de policiers et des tribunaux saturés. Si tu veux plus d'ordre dans le 93, commence par exiger que l'État y fasse son travail.",
  'indecis': "La Seine-Saint-Denis est pauvre, et beaucoup de familles y dépendent des prestations. Mais un rapport parlementaire transpartisan montre que l'État y est moins présent qu'ailleurs à besoins égaux. Ce n'est pas un territoire « assisté », c'est un territoire mal servi."},
 a_actualiser='2027-06-30',
))

# 25 ── Audiovisuel public ───────────────────────────────────────────────────
FICHES.append(fiche(
 id='privatiser-audiovisuel-public', affirmation="Privatiser l'audiovisuel public, comme le veut le RN, fera économiser de l'argent.", volet='politique', sous_theme='Médias',
 mots_cles=['audiovisuel public', 'privatiser', 'privatisation', 'france télévisions', 'radio france', 'redevance', 'rn', 'service public de l information'],
 verdict='trompeur', fiabilite='estimation',
 resume="Une privatisation réduirait la dépense annuelle, mais beaucoup moins que les 3 milliards annoncés par le RN : l'Institut Montaigne retient environ 2 milliards par an, et seulement dans 3 à 5 ans. La vente rapporterait environ 1,5 milliard une seule fois, qui réduit la dette mais pas le déficit. Elle se heurterait au droit européen et constitutionnel, et la France dépense déjà deux fois moins par habitant que l'Allemagne ou le Royaume-Uni pour son audiovisuel public.",
 contexte="Le RN a promis en 2022 puis en 2024 de privatiser l'audiovisuel public, en dehors de l'audiovisuel extérieur, au nom des économies et de la neutralité.",
 explication="L'audiovisuel public (France Télévisions, Radio France…) est financé depuis 2022 par une part de TVA, après la suppression de la redevance. Le vendre supprimerait cette dépense, mais impliquerait des coûts de transition, une recette de vente incertaine et la perte d'un service.",
 sources=[MONTAIGNE_AUDIO, OZAP_AUDIO, AN_AUDIO, SENAT_AUDIO, MONTAIGNE_AUDIO22],
 faits=[
  fait("Selon Puremédias, le vice-président du RN a confirmé en juin 2024 que le parti privatiserait l'audiovisuel public en cas de victoire, en chiffrant le gain à 3 milliards d'euros.", 'ozap_audio', '2024', 'France', "La promesse est explicite et chiffrée par le parti.", 'etabli', '3 Md€'),
  fait("Selon l'Institut Montaigne, la dépense publique pour l'audiovisuel était de 3,93 milliards d'euros en 2024, mais l'économie réaliste d'une privatisation serait d'environ 2 milliards par an, à un horizon de 3 à 5 ans.", 'montaigne_audio', '2024', 'France', "L'économie annoncée est surestimée et différée.", 'estimation', '2 Md€'),
  fait("Selon l'Institut Montaigne, la vente rapporterait environ 1,5 milliard d'euros une seule fois, ce qui réduit la dette mais pas le déficit, et la privatisation se heurterait au droit constitutionnel, au règlement européen sur la liberté des médias et à un marché publicitaire en baisse.", 'montaigne_audio', '2024', 'France et UE', "Les obstacles juridiques et économiques sont sérieux.", 'estimation', '1,5 Md€'),
  fait("Selon le Sénat, la contribution à l'audiovisuel public (138 euros en métropole) a été supprimée en 2022 et remplacée par une fraction de TVA, fixée à 4,026 milliards d'euros pour 2024 ; le règlement européen sur la liberté des médias exige des ressources « suffisantes, durables et prévisibles ».", 'senat_audio', '2022-2024', 'France et UE', "La redevance a déjà disparu ; le droit européen protège le financement du service public.", 'etabli', '138 €'),
  fait("Selon un rapport de l'Assemblée nationale citant l'Union européenne de radio-télévision, la France a dépensé 62 euros par habitant pour son audiovisuel public en 2022, contre 121 euros en Allemagne et 120 euros au Royaume-Uni.", 'an_audio', '2022', 'Europe', "Le service public français est déjà moins financé que chez nos voisins.", 'etabli', '62 €'),
 ],
 court="Trompeur : l'Institut Montaigne estime l'économie à environ 2 milliards par an dans 3 à 5 ans, pas 3 milliards, et la vente ne rapporterait qu'environ 1,5 milliard une fois. Le projet se heurte au droit européen, et la France finance déjà son audiovisuel public deux fois moins par habitant que l'Allemagne.",
 moyen="Le RN promet 3 milliards d'économies. L'Institut Montaigne, qui n'est pas de gauche, retient plutôt 2 milliards par an, et seulement au bout de 3 à 5 ans. La vente elle-même rapporterait environ 1,5 milliard, une seule fois.\n\nIl faudrait aussi surmonter le droit européen sur la liberté des médias et trouver des acheteurs sur un marché publicitaire en baisse. Et la France dépense déjà 62 € par habitant pour son audiovisuel public, contre 121 € en Allemagne. La question n'est pas seulement l'argent : c'est qui contrôle l'information.",
 detaille="Le RN a proposé en 2022 de privatiser l'audiovisuel public pour supprimer la redevance, puis a confirmé en 2024 vouloir le faire au cours d'un mandat, en chiffrant le gain à 3 milliards d'euros. La redevance a été supprimée en 2022 et remplacée par une fraction de TVA ; la dépense publique pour l'audiovisuel atteignait 3,93 milliards d'euros en 2024.\n\nL'Institut Montaigne estime l'économie réaliste à environ 2 milliards par an, à un horizon de 3 à 5 ans, et la recette de cession à environ 1,5 milliard une seule fois, qui réduirait la dette mais pas le déficit. Il relève des obstacles : une loi exposée à la censure constitutionnelle au nom de la liberté de communication, le règlement européen de 2024 sur la liberté des médias, des recettes publicitaires en baisse, des coûts sociaux et la disparition probable d'antennes régionales.\n\nSelon les données de l'UER citées par l'Assemblée nationale, la France dépensait en 2022 62 euros par habitant pour son audiovisuel public, contre 121 en Allemagne et 120 au Royaume-Uni. Privatiser le service public, c'est aussi poser la question du pluralisme : qui possédera ces médias ensuite ?",
 empathie="Je comprends qu'on n'aime pas payer pour des chaînes qu'on trouve biaisées ou qu'on ne regarde pas. Mais l'économie est bien plus faible que promis, et on perdrait les radios locales et l'info régionale. Et la France dépense déjà deux fois moins que l'Allemagne pour son service public.",
 legitimes=["Une privatisation réduirait effectivement la dépense budgétaire annuelle, à terme.", "On peut critiquer le traitement de l'information par certains médias publics."],
 contre=[
  ("L'audiovisuel public est de gauche, ce n'est pas à nous de le payer.", "Le privatiser ne garantirait pas la neutralité : il confierait ces chaînes et radios à des acheteurs privés."),
  ("On économise 3 milliards.", "L'Institut Montaigne retient environ 2 milliards par an, dans 3 à 5 ans, avec des coûts sociaux et des obstacles juridiques."),
 ],
 questions=["Sais-tu combien la France dépense par habitant pour son audiovisuel public, comparé à l'Allemagne ?", "Si France 3 et France Bleu étaient vendues, qui assurerait l'information locale ?"],
 limites=["La position du RN en 2026 n'a pas pu être confirmée par une source fiable ; la fiche porte sur ses propositions de 2022 et 2024.", "La comparaison par habitant vient d'un rapport d'un député LFI citant l'UER ; elle porte sur 2022."],
 publics={'convaincus': "Même l'Institut Montaigne, qui est libéral, dit que les 3 milliards du RN sont surestimés : environ 2 milliards par an, et pas avant 3 à 5 ans. Et on dépense déjà deux fois moins que les Allemands pour notre service public. Si tu trouves France Inter partiale, la solution n'est pas de vendre l'info à un milliardaire.",
  'indecis': "La privatisation ferait économiser de l'argent public, mais moins que promis, et avec des obstacles juridiques sérieux. La France finance déjà son audiovisuel public moins que ses voisins. La vraie question est celle du pluralisme : qui possédera les médias ensuite ?"},
 a_actualiser='2027-06-30',
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
