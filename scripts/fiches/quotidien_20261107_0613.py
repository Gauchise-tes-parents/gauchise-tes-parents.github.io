"""Fiches quotidiennes du 7 novembre 2026, passage de 06 h 13 (UTC) — phase alpha.

25 questions qui circulent (extrême droite, clichés sur la gauche, programmes) et qui n'avaient pas de fiche
qui leur réponde vraiment. Toutes les sources ont été ouvertes et lues le 7 novembre 2026 (consultee=True) ;
les chiffres viennent uniquement des passages cités. Données anciennes signalées dans les limites.
Chaque fiche contient les réponses selon le public (« publics » : électeur d'extrême droite convaincu / indécis).
Usage : python3 scripts/fiches/quotidien_20261107_0613.py  (puis node scripts/corrections-v10.js et node scripts/enrichir-fiches.js)
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche as _fiche, OUT

TODAY = '2026-11-07'

def fiche(**k):
    d = _fiche(**k)
    d['derniere_verification'] = TODAY
    return d

# ── Sources : immigration et asile ─────────────────────────────────────────
ONU_GCM = ('onu_gcm', src("Global Compact for Safe, Orderly and Regular Migration — Final Draft", "Nations unies", "11 juillet 2018",
  "https://www.un.org/pga/72/wp-content/uploads/sites/51/2018/07/migration.pdf",
  "Le paragraphe 7 présente le pacte comme un « non-legally binding, cooperative framework » (cadre de coopération juridiquement non contraignant) ; le principe de souveraineté nationale (§ 15) « reaffirms the sovereign right of States to determine their national migration policy » ; le texte fixe 23 objectifs.",
  "Texte du pacte lui-même (projet final, adopté ensuite en décembre 2018)."))
AN_QE15251 = ('an_qe15251', src("Question écrite n° 15251 (pacte mondial sur les migrations) et réponse du ministère de l'Europe et des Affaires étrangères", "Assemblée nationale / ministère de l'Europe et des Affaires étrangères", "23 avril 2019",
  "https://questions.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE15251.pdf",
  "« Ce Pacte n'est pas juridiquement contraignant » ; il « ne crée pas d'obligations juridiques autres que celles auxquelles un Etat a déjà souscrit » ; « L'adoption du Pacte n'aura pas d'impact sur notre souveraineté nationale. »",
  "Réponse officielle du ministère compétent."))
CDJ_GCM = ('cdj_gcm', src("Pacte mondial pour des migrations sûres, ordonnées et régulières : beaucoup de bruit pour rien ?", "Le Club des juristes (Thibaut Fleury Graff, professeur de droit, université de Rennes 1)", "11 décembre 2018",
  "https://www.leclubdesjuristes.com/archives-cdj/pacte-mondial-pour-des-migrations-sures-ordonnees-et-regulieres-beaucoup-de-bruit-pour-rien-2294/",
  "Le pacte « n'est pas contraignant juridiquement » : il s'agit de « souhaits ou de recommandations et non de contraintes juridiques » ; « aucun État ne pourra se faire dicter une ligne de conduite ou une politique migratoire » ; le seul suivi prévu est un forum intergouvernemental tous les quatre ans : « Il ne s'agit donc nullement de contrôle ou de surveillance ».",
  "Analyse juridique universitaire.", 'etude'))
PS_GCM = ('ps_gcm', src("RN, LR et DLF dénoncent l'approbation du pacte mondial sur les migrations par la France", "Public Sénat", "10 décembre 2018",
  "https://www.publicsenat.fr/actualites/non-classe/rn-lr-et-dlf-denoncent-l-approbation-du-pacte-mondial-sur-les-migrations-par-la",
  "Le pacte, « non contraignant », recense des principes existants et fixe 23 objectifs ; il a été approuvé à Marrakech par « quelque 150 pays », dont la France ; ses opposants avancent des effets indirects possibles « à terme » sur la souveraineté ou les expulsions, par la jurisprudence.",
  "Média parlementaire.", 'media'))
CONSEIL_PACTE = ('conseil_pacte', src("Politique migratoire : le Conseil parvient à un accord sur les principales lois en matière d'asile et de migration (communiqué 423/23)", "Conseil de l'Union européenne", "8 juin 2023",
  "https://www.consilium.europa.eu/fr/press/press-releases/2023/06/08/migration-policy-council-reaches-agreement-on-key-asylum-and-migration-laws/pdf/",
  "Nombre annuel minimum de relocalisations : « Ce nombre est fixé à 30 000 » ; contribution financière de « 20 000 euros par relocalisation » ; « Les États membres ont toute latitude quant au type de solidarité qu'ils apportent » ; « Aucun État membre ne sera obligé de procéder à des relocalisations. »",
  "Institution européenne (accord du Conseil avant le texte final)."))
UE_RESERVE26 = ('ue_reserve26', src("Décision d'exécution (UE) 2025/2642 du Conseil du 19 décembre 2025 établissant la réserve annuelle de solidarité pour 2026 (texte français relayé par le Réseau européen des migrations, Belgique)", "Conseil de l'Union européenne", "19 décembre 2025",
  "https://emnbelgium.be/sites/default/files/attachments/R%C3%A9serve%20annuelle%20de%20solidarit%C3%A9%202026_FR_TXT.pdf",
  "Réserve 2026 : 21 000 relocalisations et 420 000 000 EUR de contributions financières ; la France figure parmi les États « qui risquent de subir une pression migratoire » ; sa clé de répartition est de 16,0021 %, soit environ 3 361 « relocalisations ou autres formes de soutien au titre de la solidarité ».",
  "Acte juridique de l'Union européenne."))
EURONEWS_PACTE = ('euronews_pacte', src("Non, l'UE n'infligera pas d'amendes aux États qui refusent d'accueillir des migrants", "Euronews (The Cube, Noa Schumann)", "16 juin 2026",
  "https://fr.euronews.com/2026/06/16/non-lue-ninfligera-pas-damendes-aux-etats-qui-refusent-daccueillir-des-migrants",
  "Le mécanisme est une « solidarité obligatoire mais flexible » : la relocalisation n'est qu'une option parmi d'autres (appui opérationnel, financement, contribution de 20 000 € par personne non accueillie) ; « Ce paiement ne constitue donc pas une amende » ; les États ont promis moins de 9 000 relocalisations pour 2026.",
  "Rubrique de vérification d'un média européen.", 'media'))
EURONEWS_PACTE2 = ('euronews_pacte2', src("How EU countries watered down 'solidarity' plans to relocate asylum seekers", "Euronews (Vincenzo Genovese)", "12 juin 2026",
  "https://www.euronews.com/2026/06/12/how-eu-countries-watered-down-solidarity-plans-to-relocate-asylum-seekers",
  "Les pays non soumis à une pression migratoire ont promis 8 878 relocalisations et 76,3 M€ ; moins de 1 000 demandeurs d'asile devraient être réellement transférés en 2026 ; selon un diplomate, la France déduit de sa part les demandeurs qu'elle accueille déjà (« responsibility offset »).",
  "Média européen.", 'media'))
LCP_ALGERIE68 = ('lcp_algerie68', src("Accord franco-algérien de 1968 : un rapport parlementaire propose la dénonciation de l'accord", "LCP (Maxence Kagni, avec l'AFP)", "15 octobre 2025",
  "https://lcp.fr/actualites/accord-franco-algerien-de-1968-un-rapport-parlementaire-propose-la-denonciation-de-l",
  "Le rapport des députés Charles Rodwell et Mathieu Lefèvre (EPR) estime le surcoût à environ 2 milliards d'euros tout en admettant que « l'estimation de ces surcoûts pour les finances publiques est imprécise » ; il cite un titre de dix ans obtenu par une procédure accélérée et un regroupement familial possible après 12 mois (18 mois dans le droit commun) ; un député PS critique l'absence de tableaux étayant le chiffre.",
  "Média parlementaire rendant compte d'un rapport.", 'media'))
PS_ALGERIE68 = ('ps_algerie68', src("Accord franco-algérien de 1968 : de quoi parle-t-on ?", "Public Sénat (Henri Clavier)", "7 décembre 2023",
  "https://www.publicsenat.fr/actualites/societe/accord-franco-algerien-de-1968-de-quoi-parle-t-on",
  "Avantages : certificat de résidence de 10 ans pour les parents d'enfants français et les conjoints de Français (1 an dans le droit commun), regroupement familial « au bout d'un an contre 18 mois » ; désavantages : « Certains titres de séjours ne sont pas accessibles, notamment ceux créés par les lois de 2003, 2016 et 2018 » (dont la carte pluriannuelle) et pas d'admission exceptionnelle au séjour ; les mesures d'éloignement relèvent du droit commun.",
  "Média parlementaire (article antérieur à la loi immigration de 2024).", 'media'))
UM_ALGERIE68 = ('um_algerie68', src("L'accord franco-algérien de 1968 est-il en sursis ?", "Université de Montpellier (Hocine Zeghbib, université Paul-Valéry, repris de The Conversation)", "15 août 2023",
  "https://www.umontpellier.fr/en/articles/laccord-franco-algerien-de-1968-est-il-en-sursis",
  "L'accord a été modifié en 1985, 1994 et 2001 ; avantages : création d'entreprise sans preuve de viabilité, titre plus rapide ; désavantages : régularisation par le travail ou pour motif humanitaire seulement à titre exceptionnel, étudiants obligés de renouveler leur titre chaque année avec moins d'heures de travail autorisées, 15 ans de présence exigés pour une régularisation contre 10 ans pour les autres étrangers.",
  "Analyse universitaire.", 'etude'))
AN_QE4014 = ('an_qe4014', src("Question écrite n° 4014 (aide publique au développement à l'Algérie) et réponse du ministère de l'Europe et des Affaires étrangères", "Assemblée nationale / ministère de l'Europe et des Affaires étrangères", "6 mai 2025",
  "https://questions.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE4014.pdf",
  "L'APD bilatérale « a atteint 136 millions d'euros en 2023, un montant stable par rapport à 2022 (131 millions d'euros) » ; elle « consiste principalement en des bourses à destination d'élèves algériens étudiant en France » : 128 M€, dont 16,1 M€ de bourses et 111,8 M€ de coûts imputés ; aucun projet ne sera financé en 2025 par le don-projet de l'AFD en Algérie.",
  "Réponse officielle du ministère compétent."))
FOCUS_ALGERIE = ('focus_algerie', src("Décryptage d'une fake news : non, l'aide publique au développement de la France ne finance ni l'Algérie ni la Chine", "Focus 2030", "Juillet 2026",
  "https://focus2030.org/wp-content/uploads/2026/07/3.-APD-Chine-Algerie-Focus-2030.pdf",
  "Selon les données de l'OCDE pour 2024, l'APD vers l'Algérie atteint « 140 millions d'euros », dont « 132,5 millions d'euros correspondent aux frais de scolarité des étudiants algériens en France » ; 5,3 M€ de transferts directs ; sur 2018-2024, moyenne de 116 M€ par an (environ 800 M€ au total), dont 95 % de frais de scolarité et frais administratifs ; 96 % des montants sont dépensés en France.",
  "Association spécialisée dans l'aide au développement, d'après les données de l'OCDE.", 'secondaire'))
SENAT_ASILE26 = ('senat_asile26', src("Les coûts de l'asile en France (rapport d'information n° 874)", "Sénat, commission des finances (Marie-Carole Ciuntu, rapporteur spécial)", "8 juillet 2026",
  "https://www.senat.fr/rap/r25-874/r25-8741.pdf",
  "Les éloignements de déboutés après une OQTF « ne dépassent guère 3 000 cas par an entre 2019 et 2025 » ; le taux d'exécution de ces OQTF est « entre 3 et 8 % sur la période » (5,5 % en moyenne), contre 10 % pour l'ensemble des étrangers ; la DGEF a fourni « des données incohérentes et contradictoires » ; « près d'un quart des demandeurs d'asile sont finalement admis au séjour pour un autre motif », deux à cinq ans après le rejet.",
  "Rapport parlementaire de contrôle (rapporteure de droite)."))
SENAT_ASILE26_SYN = ('senat_asile26_syn', src("Asile : faire la lumière sur les coûts, redéfinir les protections (L'essentiel)", "Sénat, commission des finances", "8 juillet 2026",
  "https://www.senat.fr/fileadmin/cru-1783325159/Commissions/Finances/2025-2026/Controles/Essentiel_post-commission_couts_de_l_asile.pdf",
  "« la France est ainsi le troisième pays d'accueil des primo-demandeurs d'asile en 2025 », derrière l'Espagne et l'Italie ; plus de 145 000 demandes déposées à l'OFPRA en 2025 (environ -5 %) ; le taux de protection, recours devant la CNDA inclus, « atteint désormais 52,1 % en 2025 » ; le rapport parle d'un « taux infinitésimal d'exécution des OQTF des déboutés de l'asile ».",
  "Synthèse d'un rapport parlementaire."))
CDC_IRREG = ('cdc_irreg', src("La politique de lutte contre l'immigration irrégulière (rapport public thématique)", "Cour des comptes (hébergé par Vie publique)", "Janvier 2024",
  "https://www.vie-publique.fr/files/rapport/pdf/292560.pdf",
  "« Le nombre de demandes d'asile rejetées après tous les recours est d'environ 60 000 à 70 000 par an depuis 2016 » ; « seule une petite minorité – autour de 10 % – des obligations de quitter le territoire français sont exécutées » ; 11 409 éloignements forcés en 2022, 18 915 en 2019.",
  "Juridiction financière."))
AP_ASILE15 = ('ap_asile15', src("La politique de l'asile est coûteuse et peu efficace, selon la Cour des comptes", "Acteurs publics (Bruno Botella)", "20 octobre 2015",
  "https://acteurspublics.fr/articles/la-politique-de-lasile-est-couteuse-et-peu-efficace-selon-la-cour-des-comptes/",
  "Selon la Cour des comptes, « plus de 96 % des personnes déboutées resteraient en France », chiffre fondé sur 1 432 éloignements pour 40 206 déboutés en 2014 ; le Premier ministre a répondu que la Cour ne comptait ni les titres de séjour accordés ensuite ni les départs volontaires.",
  "Presse spécialisée sur l'action publique (données de 2014).", 'media'))
EUAA_2026 = ('euaa_2026', src("Asylum Report 2026 — Executive summary : Managing access to international protection", "Agence de l'Union européenne pour l'asile (EUAA)", "2026",
  "https://www.euaa.europa.eu/asylum-report-2026-executive-summary/managing-access-international-protection-0",
  "« In 2025, the number of asylum applications lodged in EU+ countries declined for a second year in a row to 822,000 » ; en volume : Allemagne 163 000, France 152 000, Espagne 143 000, Italie 134 000 ; moyenne d'environ 1 800 demandes par million d'habitants, avec en tête la Grèce (5 900), Chypre (4 500), puis l'Espagne, la Belgique et la Suisse (environ 2 900 chacune).",
  "Agence de l'Union européenne."))
EUROSTAT_ASILE = ('eurostat_asile', src("27% drop in first-time asylum applications in 2025", "Eurostat", "25 mars 2026",
  "https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260325-2",
  "669 400 primo-demandeurs d'asile dans l'UE en 2025, contre 912 400 en 2024 (-27 %) ; Espagne 141 000 (21 %), Italie 126 600 (19 %), France 116 400 (17 %), Allemagne 113 200 (17 %) ; pour 1 000 habitants : moyenne de l'UE 1,5, Grèce 5,3, Chypre et Espagne 2,9.",
  "Office statistique de l'Union européenne."))
EUAA_OFPRA = ('euaa_ofpra', src("OFPRA publishes its annual report for 2025", "Agence de l'Union européenne pour l'asile (plateforme d'information)", "27 juillet 2026",
  "https://dip.euaa.europa.eu/node/13714",
  "145 270 demandes en 2025 (-5,5 %), dont -14,4 % de premières demandes ; 156 509 décisions, un record ; taux de protection de l'OFPRA : 41 %, contre 39 % en 2024 ; les réexamens ont augmenté de 43 %.",
  "Agence de l'Union européenne, d'après le rapport de l'OFPRA."))
MTE_HLM = ('mte_hlm', src("L'attribution des logements locatifs sociaux : objectifs, enjeux, acteurs et outils", "Ministère de la Transition écologique (DGALN/DHUP)", "Juin 2024",
  "https://www.ecologie.gouv.fr/sites/default/files/documents/Lattribution%20des%20logements%20locatifs%20sociaux%202024.pdf",
  "Les attributions vont d'abord aux ménages reconnus prioritaires au titre du DALO, puis aux publics de l'article L. 441-1 du code de la construction : personnes handicapées, mal logées, hébergées, victimes de violences conjugales, personnes sans logement ou menacées d'expulsion, jeunes sortant de l'aide sociale à l'enfance, etc. ; le droit au logement vise toute personne « résidant sur le territoire français de façon régulière et dans des conditions de permanence » ; 72 % des ménages sont éligibles au logement social. Aucun critère de nationalité ou d'origine n'est prévu.",
  "Document officiel du ministère du Logement."))
INSEE_LOGIMM = ('insee_logimm', src("Conditions de logement (Immigrés et descendants d'immigrés en France, édition 2023)", "Insee (Insee Références), d'après l'enquête Trajectoires et Origines 2 (Ined-Insee)", "30 mars 2023",
  "https://www.insee.fr/fr/statistiques/6793286",
  "35 % des immigrés de 18 à 59 ans vivent dans le secteur social, contre 11 % des personnes sans ascendance migratoire ; « Cette surreprésentation en logement social est largement liée aux moindres revenus et à l'âge plus jeune des immigrés » ; 26 % des immigrés vivent dans un logement suroccupé, contre 8 % des personnes sans ascendance migratoire.",
  "Statistique publique de référence (données 2019-2020)."))
UT1_HLM = ('ut1_hlm', src("Inégalités d'accès au logement social : peut-on parler de discrimination ? (Économie et Statistique)", "Liliane Bonnal, Rachid Boumahdi, Pascal Favard (Insee / université Toulouse Capitole)", "Avril 2014",
  "https://publications.ut-capitole.fr/15889",
  "À caractéristiques égales, les ménages non européens ont des délais d'accès au logement social plus longs (« longer access times ») et « a significant part of this difference may be due to discrimination ».",
  "Étude universitaire publiée dans la revue de l'Insee (données de l'enquête Logement 2006).", 'etude'))
LCP_HLM = ('lcp_hlm', src("Réserver les logements HLM aux Français : la proposition de Marine Le Pen provoque une levée de boucliers", "LCP (Raphaël Marchal)", "14 septembre 2026",
  "https://lcp.fr/actualites/reserver-les-logements-hlm-aux-francais-la-proposition-de-marine-le-pen-provoque-une",
  "Selon l'Union sociale pour l'habitat, les étrangers représentent 15 % des locataires du parc social ; sa présidente, Emmanuelle Cosse : « Les étrangers ne sont pas favorisés dans l'entrée dans le logement social. »",
  "Média parlementaire.", 'media'))
SENAT_PADHUE = ('senat_padhue', src("Question écrite n° 04446 (praticiens à diplôme hors Union européenne) et réponse du ministère de la Santé", "Sénat / ministère de la Santé", "18 juin 2026",
  "https://www.senat.fr/questions/base/2025/qSEQ250504446.html",
  "Les PADHUE passent des épreuves de vérification des connaissances (EVC), organisées comme un concours dont les jurys fixent la barre d'admissibilité, puis un parcours de consolidation des compétences de deux ans ; une voie interne existe depuis l'automne 2025 (attestation du chef de service et une épreuve à choix multiples) ; « 3 873 PADHUE ont réussi le concours en 2024 » pour 4 000 postes ; ils « participent à la continuité des soins ».",
  "Réponse officielle du ministère compétent."))
ANM_PADHUE = ('anm_padhue', src("Avis de l'Académie nationale de médecine concernant le droit de plein exercice des PADHUE", "Académie nationale de médecine", "15 janvier 2026",
  "https://www.academie-medecine.fr/avis-de-lanm-concernant-le-droit-de-plein-exercice-des-padhue-praticiens-a-diplome-hors-union-europeenne/",
  "Les candidats doivent « passer une épreuve de vérification des connaissances médicales (EVC) », prouver leur maîtrise du français, puis voir leurs compétences « validées par une commission nationale pour chaque spécialité » ; environ 8 % des médecins de plein exercice ont été formés hors d'Europe ; l'Académie demande de renforcer l'évaluation (écrit anonyme, français B2 à C1, simulation des gestes techniques).",
  "Institution scientifique de référence."))
SM_PADHUE = ('sm_padhue', src("Praticiens à diplôme hors Union européenne : 9 % exercent en psychiatrie", "Santé mentale (Valérie Westphal), d'après le Conseil national de l'Ordre des médecins", "7 mars 2025",
  "https://www.santementale.fr/2025/02/quel-exercice-pour-les-anciens-padhue/",
  "Au 1er janvier 2025, 19 154 anciens PADHUE sont inscrits à l'Ordre, dont 15 972 en activité régulière : « Ces praticiens représentent désormais 8 % du corps médical en activité régulière » ; leur nombre a augmenté de 141 % depuis 2010 ; 52,7 % exercent comme salariés à l'hôpital ; ils représentent 14,1 % des pédiatres et 10,7 % des gynécologues.",
  "Presse professionnelle, d'après les données de l'Ordre des médecins.", 'media'))
BMJ_IMG = ('bmj_img', src("Quality of Care Delivered by General Internists in US Hospitals Who Graduated from Foreign Versus US Medical Schools (BMJ)", "Harvard Medical School (Tsugawa, Jena, Orav, Jha)", "2 février 2017",
  "https://hcp.hms.harvard.edu/publication/quality-care-delivered-general-internists-us-hospitals-who-graduated-foreign-versus-us",
  "Sur 1 215 490 hospitalisations de patients Medicare (2011-2014), la mortalité ajustée à 30 jours est de « 11.2% v 11.6% » pour les patients des médecins diplômés à l'étranger par rapport à ceux des diplômés américains.",
  "Étude universitaire publiée dans une revue médicale de référence (États-Unis).", 'etude'))

# ── Sources : international et sécurité ────────────────────────────────────
PS_UKR_LECORNU = ('ps_ukr_lecornu', src("Ukraine : avec le dégel des avoirs russes, la France aura accordé près de 3 milliards d'euros d'aides en 2024, annonce Sébastien Lecornu", "Public Sénat (Romain David)", "15 octobre 2024",
  "https://www.publicsenat.fr/actualites/international/ukraine-avec-le-degel-des-avoirs-russes-la-france-aura-accorde-pres-de-3-milliards-deuros-daides-en-2024-annonce-sebastien-lecornu",
  "Devant le Sénat, le ministre des Armées chiffre l'aide militaire (matériel valorisé) à 1,7 Md€ en 2022, 2,1 Md€ en 2023 et « plus près de trois » milliards en 2024, dont près de 300 M€ issus des avoirs russes gelés ; « Il n'est pas question de déprogrammer des choses dans la LPM pour aider l'Ukraine ».",
  "Média parlementaire rendant compte d'une audition.", 'media'))
MINARM_AVOIRS = ('minarm_avoirs', src("Mobilisation des avoirs russes par le ministère des Armées au profit de l'Ukraine (communiqué)", "Ministère des Armées", "6 septembre 2024",
  "https://prod-site-internet-minarm-admin.cloud.defense.gouv.fr/sites/default/files/ministere-armees/Communiqu%C3%A9_Mobilisation%20des%20avoirs%20russes%20par%20le%20minist%C3%A8re%20des%20Arm%C3%A9es%20au%20profit%20de%20l%E2%80%99Ukraine.pdf",
  "1,4 Md€ issus des revenus des avoirs russes immobilisés sont affectés, via la Facilité européenne pour la paix, à l'achat de matériel pour l'Ukraine ; 300 M€ vont à l'industrie française en 2024 (munitions, artillerie, défense aérienne) ; « Il s'agit d'une opportunité pour poursuivre la montée en cadence de l'industrie française en soutien à l'Ukraine. »",
  "Communiqué ministériel."))
PS_UKR_KIEL = ('ps_ukr_kiel', src("Soutien financier à l'Ukraine : qui des Européens ou des Américains a fourni l'aide la plus importante ?", "Public Sénat (Guillaume Jacquot), d'après l'Institut de Kiel", "25 février 2025",
  "https://www.publicsenat.fr/actualites/international/soutien-financier-a-lukraine-qui-des-europeens-ou-des-americains-a-fourni-laide-la-plus-importante",
  "Selon l'Institut de Kiel, l'ensemble des Européens (UE, États membres, Royaume-Uni, Suisse, Norvège, Islande) avaient déboursé « 132,3 milliards d'euros au 31 décembre » 2024, et les États-Unis « l'équivalent de 114,2 milliards d'euros ».",
  "Média parlementaire, d'après un institut de recherche.", 'media'))
STATISTA_UKR = ('statista_ukr', src("Quels pays ont fourni le plus d'aides à l'Ukraine ?", "Statista (Valentine Fourreau), d'après l'Institut de Kiel, repris par L'Écho du Mardi", "25 février 2025",
  "https://www.echodumardi.com/actualite/quels-pays-ont-fourni-le-plus-daides-a-lukraine-2/?print=pdf",
  "Selon les données de l'Institut de Kiel, la France a « un montant total annoncé de 4,9 milliards d'euros du 24 janvier 2022 au 31 décembre 2024 », dont environ 3,5 milliards d'aide militaire, ce qui la place au 10e rang ; États-Unis environ 114 Md€, institutions de l'UE environ 49 Md€.",
  "Infographie d'un éditeur de données, d'après un institut de recherche.", 'secondaire'))
CE_UKR = ('ce_ukr', src("Soutien financier de l'UE à l'Ukraine", "Commission européenne", "14 octobre 2026",
  "https://commission.europa.eu/topics/eu-solidarity-ukraine/eu-assistance-ukraine/eu-financial-support-ukraine_fr",
  "La Facilité pour l'Ukraine prévoit « jusqu'à 50 milliards d'euros » pour 2024-2027 ; l'UE a versé « 43,3 milliards d'euros d'assistance macrofinancière », sous forme de « prêts consentis à des conditions favorables » ; un « prêt de 90 milliards d'euros » pour 2026-2027 est financé par l'emprunt de l'UE ; un mécanisme de prêt est « financé par des recettes exceptionnelles provenant d'actifs souverains russes immobilisés ».",
  "Institution européenne."))
FC_UKR = ('fc_ukr', src("The Facts on 'De-Nazifying' Ukraine", "FactCheck.org (Annenberg Public Policy Center, université de Pennsylvanie, Robert Farley)", "31 mars 2022",
  "https://www.factcheck.org/2022/03/the-facts-on-de-nazifying-ukraine/",
  "Le parti d'extrême droite Svoboda a obtenu 2,15 % aux législatives de 2019 et un seul siège ; Volodymyr Zelensky, juif, a été élu en 2019 avec 73 % des voix ; le bataillon Azov, fondé par des membres de groupes néonazis, a été intégré à la Garde nationale fin 2014 ; pour un chercheur de l'université Johns Hopkins, ces groupes sont « numerically small, marginal and their political influence at the state level is non-existent ».",
  "Fact-checker universitaire reconnu.", 'media'))
ADL_UKR = ('adl_ukr', src("Why is Putin Calling the Ukrainian Government a Bunch of Nazis?", "Anti-Defamation League (Andrew Srulevitch)", "4 mars 2022",
  "https://www.adl.org/resources/blog/why-putin-calling-ukrainian-government-bunch-nazis",
  "Selon l'historien David Fishman, « The political parties which the ultra-nationalists support received just over 2 percent of the vote in the 2019 elections » ; l'Ukraine est « a flawed democracy, but unquestionably a democracy, and in no way a Nazi regime » ; la propagande russe est « an attempt to delegitimize Ukraine in the eyes of the Russian public ».",
  "Organisation de lutte contre l'antisémitisme.", 'secondaire'))
EUVSD_UKR = ('euvsd_ukr', src("Zelenskyy is only a marketing operation, a Jewish face for a Nazi regime (fiche de désinformation)", "EUvsDisinfo (Service européen pour l'action extérieure)", "Non datée",
  "https://www.euvsdisinfo.eu/report/zelenskyy-is-only-a-marketing-operation-a-jewish-face-for-a-nazi-regime/",
  "Il s'agit d'un « Recurring pro-Kremlin disinformation narrative » ; « In 2015 Ukraine issued a ban on Nazi and Communist ideologies » ; en 2019, le front uni des partis de droite radicale n'a obtenu que « 2.15% of the vote », loin du seuil de 5 %.",
  "Service de l'Union européenne chargé de documenter la désinformation."))
PS_ULTRA23 = ('ps_ultra23', src("Maintien de l'ordre : « Le sujet n'est pas les manifestations, mais l'ultragauche », pour Gérald Darmanin", "Public Sénat (Simon Barbarit)", "5 avril 2023",
  "https://www.publicsenat.fr/article/politique/maintien-de-l-ordre-le-sujet-n-est-pas-les-manifestations-mais-l-ultragauche-pour",
  "Depuis 2017, le ministre de l'Intérieur cite 9 attentats d'ultradroite déjoués et 1 d'ultragauche ; il attribue à l'ultragauche les violences de certaines manifestations ; un sénateur cite le directeur de la DGSI, pour qui la menace d'ultradroite est « aujourd'hui la principale menace » pour les démocraties occidentales.",
  "Média parlementaire rendant compte d'une audition.", 'media'))
AN_QE10244 = ('an_qe10244', src("Question écrite n° 10244 (ultradroite) et réponse du ministère de l'Intérieur", "Assemblée nationale / ministère de l'Intérieur", "9 avril 2024",
  "https://www.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE10244.pdf",
  "Le ministère indique avoir déjoué « 12 projets d'action terroriste depuis 2017, dont 2 en 2023 » liés à l'ultradroite et évoque des « dissolutions administratives de groupes d'ultra-droite » ; la question cite la DGSI : une ultradroite agissante de « près de 2 000 individus ».",
  "Réponse officielle du ministère compétent."))
AN_TACHE = ('an_tache', src("Proposition de loi n° 877 — État des lieux de la menace terroriste d'extrême droite (document de travail du rapporteur)", "Assemblée nationale (Aurélien Taché, rapporteur)", "28 mars 2023",
  "https://www.assemblee-nationale.fr/dyn/contenu/visualisation/600883/file/EAT%20PPL%20877%20-%20%C3%89tat%20des%20lieux%20terrorisme%20d%27extr%C3%AAme-droite.pdf",
  "Selon Europol (TE-SAT 2022), « la France comptabilise 45 % de l'ensemble des arrestations réalisées dans l'Union européenne » pour terrorisme d'extrême droite (29 en 2021) ; selon les chercheurs Sommier, Crettiez et Audigier (2021), depuis 1986, « l'ultra gauche serait ainsi responsable de 7 morts, contre 55 pour l'ultra droite » ; « l'État n'effectue aucun suivi des infractions en fonction des motivations idéologiques ».",
  "Document parlementaire (rapporteur de gauche) citant Europol et des travaux universitaires."))
PS_VIORAMIL = ('ps_vioramil', src("Groupuscules d'ultradroite : « Gérald Darmanin ne s'attaque au problème que lorsque celui-ci devient incontrôlable »", "Public Sénat (Romain David)", "28 novembre 2023",
  "https://www.publicsenat.fr/actualites/politique/groupuscules-dultradroite-gerald-darmanin-ne-sattaque-au-probleme-que-lorsque-celui-ci-devient-incontrolable",
  "L'étude ANR « Vioramil » recense environ 10 000 faits de violence militante ; selon la sociologue Isabelle Sommier, « 70 % des agressions, c'est-à-dire des atteintes aux personnes, sont le fait de groupes d'ultradroite ».",
  "Média parlementaire, d'après une recherche universitaire.", 'media'))
AN_CE_MANIF = ('an_ce_manif', src("Rapport n° 1824 de la commission d'enquête sur la structuration, le financement, les moyens et les modalités d'action des groupuscules à l'origine des violences lors des manifestations (16 mars - 3 mai 2023)", "Assemblée nationale (Patrick Hetzel, président ; Florent Boudié, rapporteur)", "7 novembre 2023",
  "https://www.assemblee-nationale.fr/dyn/16/rapports/cegrvimani/l16b1824-t1_rapport-enquete.pdf",
  "Sur la période, 1 518 policiers et gendarmes et 546 manifestants ont été blessés, avec 3 339 interpellations pour environ 3,56 millions de manifestants ; à Bordeaux, les groupes violents comptaient de 15 à 200 personnes ; le rapporteur estime que les violences n'ont pas été « planifiées et orchestrées » par des organisations centralisées.",
  "Rapport parlementaire d'enquête."))
PS_LYON26 = ('ps_lyon26', src("Mort d'un militant nationaliste à Lyon : le parquet requiert la mise en examen pour « homicide volontaire » de sept suspects", "Public Sénat (avec l'AFP)", "19 février 2026",
  "https://www.publicsenat.fr/actualites/politique/mort-de-quentin-deranque-le-parquet-requiert-la-mise-en-examen-pour-homicide-volontaire-de-sept-suspects",
  "Un militant « nationaliste et identitaire » est mort après une bagarre à Lyon entre « groupuscules fasciste et antifasciste » ; onze personnes ont été placées en garde à vue et le parquet a requis sept mises en examen pour « homicide volontaire ».",
  "Média parlementaire, avec l'AFP.", 'media'))
MININT_ANTIREL = ('minint_antirel', src("Bilan des actes antireligieux 2025", "Ministère de l'Intérieur (document hébergé par la préfecture de la région Île-de-France)", "Avril 2026",
  "https://www.prefectures-regions.gouv.fr/ile-de-france/irecontenu/telechargement/139847/1018971/file/Bilan_actes_anti_religieux_2025.pdf",
  "« 843 faits antichrétiens ont été recensés en 2025 » (+9 %), dont 734 atteintes aux biens (87 %) : vols ou tentatives 362 (43 %), dégradations 254 (30 %), inscriptions 81 (10 %), « incendies (45 faits, 5 %) » ; 109 atteintes aux personnes (+70 %), dont un homicide ; « 1320 faits antisémites » (-16 %) et 326 faits antimusulmans (+88 %).",
  "Statistique officielle du ministère de l'Intérieur."))
AN_QE10636 = ('an_qe10636', src("Question écrite n° 10636 (actes antichrétiens) et réponse du ministère de l'Intérieur", "Assemblée nationale / ministère de l'Intérieur", "8 septembre 2026",
  "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE10636",
  "« 843 actes antichrétiens ont été recensés par la direction nationale du renseignement territorial (DNRT) » en 2025, soit 34 % des faits antireligieux, dont 817 visant des catholiques ; « Les atteintes aux biens dominent, avec 734 faits en 2025 », dont 627 visant des lieux de culte.",
  "Réponse officielle du ministère compétent."))
LM_EGLISES = ('lm_eglises', src("Dégradations d'églises : une hausse réelle, des intentions variées", "Le Monde, Les Décodeurs (Mathilde Damgé, Anne-Aël Durand)", "23 avril 2019",
  "https://www.patrimoine-religieux.fr/wp-content/uploads/2024/01/Degradations-deglises.-Une-hausse-reelle-des-intentions-variees.pdf",
  "1 063 actes antichrétiens en 2018, environ trois par jour ; la CNCDH juge « extrêmement délicat de différencier les actes qui ont une réelle motivation raciste, des vols ou actes de pur vandalisme ».",
  "Rubrique de vérification d'un quotidien de référence (données de 2018).", 'media'))
LP_EGLISES = ('lp_eglises', src("Incendies volontaires d'églises en France : attention aux fake news", "Le Parisien", "20 juillet 2020",
  "https://www.patrimoine-religieux.fr/wp-content/uploads/2024/01/Incendies-volontaires-en-France-attention-aux-fake-news.pdf",
  "Sur une liste virale de 11 incendies, deux étaient accidentels, deux commis par des adolescents et un au Canada ; seuls deux cas se rapprochent d'actes antichrétiens ; selon l'Observatoire du patrimoine religieux, « il y a certainement des actes anti-chrétiens, mais on ne peut pas quantifier le phénomène ».",
  "Quotidien national (données de 2020).", 'media'))

# ── Sources : école, santé, écologie ───────────────────────────────────────
BO_EVARS = ('bo_evars', src("Programme d'éducation à la vie affective et relationnelle, et à la sexualité (Bulletin officiel n° 6 du 6 février 2025)", "Ministère de l'Éducation nationale", "6 février 2025",
  "https://www.education.gouv.fr/sites/default/files/document/Bulletin%20officiel%20n%C2%B0%206%20du%206%20f%C3%A9vrier%202025-405369.pdf",
  "Programme appliqué « à la rentrée de l'année scolaire 2025-2026 », avec « au moins trois séances annuelles et par groupes d'âge homogène » et des contenus « progressifs et adaptés à l'âge et à la maturité des élèves » ; à l'école primaire, il s'agit d'une « éducation à la vie affective et relationnelle » (corps, émotions, intimité, consentement, puberté en CM1-CM2) ; le mot « genre » y apparaît pour « repérer des discriminations issues de stéréotypes, notamment de genre » ; l'expression « théorie du genre » n'apparaît pas.",
  "Texte officiel du programme."))
ETUDIANT_EVARS = ('etudiant_evars', src("Que contient le nouveau programme d'éducation à la sexualité qui doit être mis en place à la rentrée 2025 ?", "L'Étudiant (Rachel Rodrigues)", "6 février 2025",
  "https://www.letudiant.fr/lycee/que-contient-le-nouveau-programme-deducation-a-la-sexualite-qui-doit-etre-mis-en-place-a-la-rentree-2025.html",
  "La sexualité n'est pas abordée avant le collège ; en 5e, les élèves apprennent à distinguer sexe, genre et orientation sexuelle ; l'identité de genre est introduite en seconde ; dans les versions antérieures, elle figurait au collège et le ministère l'a déplacée au lycée ; le programme a été approuvé par 60 voix contre 0 au Conseil supérieur de l'éducation ; selon le CESE, moins de 15 % des élèves bénéficient réellement des trois séances.",
  "Média spécialisé dans l'éducation.", 'media'))
PS_EVARS = ('ps_evars', src("Éducation sexuelle : le ministre Alexandre Portier recadré par Anne Genetet sur « la théorie du genre »", "Public Sénat (Romain David)", "28 novembre 2024",
  "https://www.publicsenat.fr/actualites/education/education-sexuelle-le-ministre-alexandre-portier-recadre-par-anne-genetet-sur-la-theorie-du-genre",
  "Le ministre délégué voulait empêcher l'entrée de « la théorie du genre » à l'école ; la ministre de l'Éducation nationale a répondu : « ce programme n'a pas d'idéologie » et « la théorie du genre n'existe pas » ; l'expression est contestée par des associations et des universitaires.",
  "Média parlementaire.", 'media'))
AN_QE4168 = ('an_qe4168', src("Question écrite n° 4168 (programme d'éducation à la sexualité) et réponse du ministère de l'Éducation nationale", "Assemblée nationale / ministère de l'Éducation nationale", "28 octobre 2025",
  "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE4168.pdf",
  "La députée relève que l'identité de genre était « mentionnée 17 fois dans la version initiale » ; le ministère répond qu'au secondaire la notion sert à sensibiliser à la diversité et à lutter contre les discriminations (article 225-1 du code pénal), qu'au primaire seuls les stéréotypes de genre sont présentés et que la progression est « adaptée à l'âge et à la maturité des élèves ».",
  "Réponse officielle du ministère compétent."))
EPIPHARE_ARN = ('epiphare_arn', src("Vaccination par ARNm contre la COVID-19 et mortalité toute cause à 4 ans chez 28 millions d'individus âgés de 18 à 59 ans", "EPI-PHARE (ANSM-Assurance maladie)", "4 décembre 2025",
  "https://www.epi-phare.fr/app/uploads/2025/12/EPI-PHARE_rapport_mortalite_vaccination_covid_20251204.pdf",
  "Cohorte de 22 767 546 personnes vaccinées et 5 932 443 non vaccinées, suivies 45 mois en médiane ; 98 429 décès (0,4 %) chez les vaccinés contre 32 662 (0,6 %) chez les non-vaccinés ; risque de décès toute cause environ 25 % plus faible chez les vaccinés (environ 20 % après correction) ; « Ces résultats excluent donc un risque accru de mortalité toute cause à 4 ans chez les individus vaccinés » ; les auteurs signalent les limites d'une étude observationnelle.",
  "Groupement scientifique public de pharmaco-épidémiologie."))
ANSM_MYO = ('ansm_myo', src("Le risque de myocardite et péricardite après la vaccination Covid-19 est confirmé mais peu fréquent et d'évolution favorable", "ANSM (étude EPI-PHARE)", "8 novembre 2021 (mis à jour le 8 avril 2022)",
  "https://ansm.sante.fr/actualites/le-risque-de-myocardite-et-pericardite-apres-la-vaccination-Covid-19-est-confirme-mais-peu-frequent-et-devolution-favorable",
  "Étude de 919 myocardites chez les 12-50 ans : risque le plus élevé chez les hommes de moins de 30 ans, surtout avec Spikevax (environ 132 cas en excès par million de doses) ; « l'évolution clinique […] apparaît généralement favorable » ; aucun décès chez les patients hospitalisés de l'étude ; la balance bénéfice-risque n'est pas remise en cause.",
  "Agence publique de sécurité du médicament."))
SPF_DECES21 = ('spf_deces21', src("Grandes causes de décès en France en 2021", "Santé publique France", "19 décembre 2023",
  "https://www.santepubliquefrance.fr/presse/grandes-causes-de-deces-en-france-en-2021",
  "« La Covid-19 a directement causé le décès de 60 895 personnes en France en 2021 », troisième cause de décès (9,2 %).",
  "Agence nationale de santé publique."))
AD_COVID = ('ad_covid', src("Le seuil des 160 000 morts du covid franchi en France", "AlloDocteurs (France Télévisions), avec l'AFP", "14 décembre 2022",
  "https://www.allodocteurs.fr/le-seuil-des-160-000-morts-du-covid-franchi-en-france-33844.html",
  "Selon Santé publique France, 160 008 personnes sont mortes du covid en France depuis mars 2020, dont 130 617 à l'hôpital.",
  "Média de santé du service public, d'après Santé publique France (données de 2022).", 'media'))
OMS_VACC = ('oms_vacc', src("Les vaccinations contre la COVID-19 ont sauvé plus de 1,4 million de vies dans la Région européenne de l'OMS", "Organisation mondiale de la santé (bureau régional de l'Europe)", "16 janvier 2024",
  "https://www.who.int/europe/fr/news/item/16-01-2024-covid-19-vaccinations-have-saved-more-than-1.4-million-lives-in-the-who-european-region--a-new-study-finds",
  "Entre 2020 et mars 2023, la vaccination a sauvé plus de 1,4 million de vies dans la Région européenne de l'OMS et réduit les décès d'au moins 57 %.",
  "Organisation internationale de santé."))
CIRC_GLY = ('circ_gly', src("IARC Monograph on Glyphosate", "Centre international de recherche sur le cancer (CIRC, OMS)", "20 mars 2015",
  "https://www.iarc.who.int/featured-news/media-centre-iarc-news-glyphosate/",
  "Le glyphosate est classé dans le groupe 2A, « probably carcinogenic to humans » : preuves « limited » chez l'humain (lymphome non hodgkinien), « sufficient » chez l'animal ; le classement porte sur le danger, pas sur le risque lié au niveau d'exposition.",
  "Agence de recherche de l'OMS."))
EFSA_GLY = ('efsa_gly', src("Glyphosate: no critical areas of concern; data gaps identified", "Autorité européenne de sécurité des aliments (EFSA)", "6 juillet 2023",
  "https://www.efsa.europa.eu/en/news/glyphosate-no-critical-areas-concern-data-gaps-identified",
  "L'ECHA a conclu en 2022 que le glyphosate ne remplit pas les critères pour être classé cancérogène, mutagène ou reprotoxique ; l'EFSA « did not identify critical areas of concern » mais relève des lacunes de données ; un « high long-term risk to mammals » est identifié pour 12 des 23 usages proposés, et aucune conclusion ferme n'est possible sur la biodiversité.",
  "Agence européenne d'évaluation des risques."))
INSERM_PEST = ('inserm_pest', src("Pesticides et effets sur la santé : nouvelles données (expertise collective)", "Inserm", "30 juin 2021",
  "https://presse.inserm.fr/publication-de-lexpertise-collective-inserm-pesticides-et-effets-sur-la-sante-nouvelles-donnees/43303/",
  "L'expertise retient pour le glyphosate « une présomption moyenne de lien avec les lymphomes non hodgkiniens ».",
  "Institut public de recherche médicale."))
CE_GLY = ('ce_gly', src("Glyphosate : les États membres n'ont pas atteint la majorité qualifiée pour renouveler ou rejeter son approbation", "Commission européenne (représentation en France)", "16 novembre 2023",
  "https://france.representation.ec.europa.eu/informations/glyphosate-les-etats-membres-nont-pas-atteint-la-majorite-qualifiee-pour-renouveler-ou-rejeter-son-2023-11-16_fr",
  "« la Commission va maintenant procéder au renouvellement de l'approbation du glyphosate pour une période de 10 ans », avec des conditions, dont « l'interdiction d'utiliser le glyphosate comme dessiccant avant la récolte ».",
  "Institution européenne."))
MTE_FEUX = ('mte_feux', src("Prévention des feux de forêt", "Ministère de la Transition écologique", "10 juillet 2026",
  "https://www.ecologie.gouv.fr/politiques-publiques/prevention-feux-foret",
  "« 90 % des départs de feux de forêt ont pour origine les activités humaines » ; « La moitié des départs de feux sont dus à des imprudences et à des comportements dangereux » ; la malveillance représente environ un quart des départs ; « Les effets du changement climatique peuvent aggraver le risque d'incendie de forêt et de végétation » ; en 2022, plus de 70 000 hectares ont brûlé.",
  "Page officielle du ministère."))
MTE_FEUX_DP = ('mte_feux_dp', src("Campagne de prévention des feux de forêt et de végétation 2026 (dossier de presse)", "Ministère de la Transition écologique", "Juin 2026",
  "https://www.ecologie.gouv.fr/sites/default/files/documents/09062026_DP_Feux_0.pdf",
  "« 9 feux sur 10 sont d'origine humaine » ; « Plus de la moitié des feux d'origine humaine est due à des imprudences ou des comportements dangereux » ; le changement climatique, en allongeant et intensifiant les sécheresses, favorise l'éclosion et le développement des feux ; en 2025, 30 500 ha ont brûlé.",
  "Document officiel du ministère."))
MF_FEUX = ('mf_feux', src("Changement climatique : quel impact sur les feux de forêt ?", "Météo-France", "21 mai 2026",
  "https://meteofrance.com/le-changement-climatique/quel-climat-futur/changement-climatique-quel-impact-sur-les-feux-de-foret",
  "La hausse des températures assèche la végétation et le danger de feu progresse vers le nord ; en région méditerranéenne, les jours de danger très élevé passeraient d'environ 40 à plus de 80 par an ; à +4 °C, « Le risque de feu se généralise à l'ensemble du pays » et la saison à risque s'allongerait de 1 à 2 mois.",
  "Service public de météorologie."))
GIEC_FEUX = ('giec_feux', src("AR6, groupe de travail I — Résumé à l'intention des décideurs", "GIEC", "2021",
  "https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/",
  "A.3.5 : l'influence humaine a probablement augmenté les événements composés, dont le « fire weather in some regions of all inhabited continents » (confiance moyenne) ; C.2.4 : le GIEC projette des « increases in fire weather » dans certaines régions.",
  "Organisme scientifique international de référence."))
SDES_ZFE = ('sdes_zfe', src("Quels ménages possèdent des voitures Crit'Air 3 ou plus dans les métropoles du Grand Paris et de Lyon ?", "SDES (service statistique du ministère de la Transition écologique)", "3 juillet 2025",
  "https://www.statistiques.developpement-durable.gouv.fr/quels-menages-possedent-des-voitures-critair-3-ou-plus-dans-les-metropoles-du-grand-paris-et-de",
  "Les voitures Crit'Air 3 ou plus représentent « un peu plus d'une voiture sur quatre du parc automobile des ménages » dans les deux métropoles, mais « environ 4 voitures sur 10 du parc automobile des 20 % de ménages les plus modestes » (42 % dans le Grand Paris, 46 % à Lyon sous le 2e décile).",
  "Statistique publique."))
SPF_AIR = ('spf_air', src("Pollution de l'air ambiant : nouvelles estimations de son impact sur la santé des Français", "Santé publique France", "14 avril 2021",
  "https://www.santepubliquefrance.fr/presse/pollution-de-lair-ambiant-nouvelles-estimations-de-son-impact-sur-la-sante-des-francais",
  "« près de 40 000 décès seraient attribuables à une exposition » aux particules fines PM2,5 chez les 30 ans et plus (période 2016-2019), soit « 7% de la mortalité totale ».",
  "Agence nationale de santé publique."))
LCP_ZFE = ('lcp_zfe', src("ZFE : le Conseil constitutionnel censure la suppression des zones à faibles émissions", "LCP (Raphaël Marchal)", "21 mai 2026",
  "https://lcp.fr/actualites/zfe-le-conseil-constitutionnel-censure-la-suppression-des-zones-a-faibles-emissions",
  "La suppression des ZFE, ajoutée par amendements RN et Droite républicaine avec le soutien de LFI et confirmée au vote final le 14 avril 2026, est censurée par la décision n° 2026-903 DC comme « cavalier législatif », faute de lien suffisant avec le texte initial ; le fond n'est pas examiné et les ZFE sont maintenues.",
  "Média parlementaire.", 'media'))
AN_QE3069 = ('an_qe3069', src("Question écrite n° 3069 (zones à faibles émissions) et réponse du ministère des Transports", "Assemblée nationale / ministère des Transports", "20 décembre 2022",
  "https://www.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE3069.pdf",
  "Aides alors en vigueur : prime à la conversion jusqu'à 6 000 € (électrique) pour un ménage modeste qui habite ou travaille en ZFE, microcrédit jusqu'à 8 000 €, prêt à taux zéro expérimental en 2023, leasing social prévu, dérogations locales possibles ; le ministère cite « plus de 47 000 décès par an » imputables à la pollution atmosphérique.",
  "Réponse officielle du ministère compétent (données de 2022)."))
OI_AIR = ('oi_air', src("Les enfants de familles aisées sont plus exposés à la pollution, mais leur santé en souffre moins", "Observatoire des inégalités, d'après la DREES (Études et résultats n° 1292)", "15 février 2024",
  "https://www.inegalites.fr/Les-enfants-de-familles-aisees-sont-plus-exposes-a-la-pollution-mais-leur-sante",
  "Les enfants nés en 2016 dans les familles les plus aisées sont un peu plus exposés aux particules fines, mais avant 2 ans 5 % des enfants des familles les plus pauvres ont été hospitalisés pour bronchiolite, contre 2,4 % des plus riches.",
  "Association indépendante, d'après une étude de la DREES.", 'secondaire'))
OEIL_2035 = ('oeil_2035', src("Normes d'émissions de CO2 pour les voitures et les camionnettes (procédure 2021/0197(COD))", "Parlement européen (Observatoire législatif)", "25 avril 2023",
  "https://oeil.europarl.europa.eu/oeil/fr/document-summary?id=1741896",
  "Le règlement (UE) 2023/851 prévoit « une réduction des émissions de CO2 de 100% tant pour les voitures neuves que pour les camionnettes neuves à partir de 2035 » ; la Commission doit proposer l'immatriculation, après 2035, des véhicules roulant exclusivement aux « carburants neutres en CO2 » ; « en 2026, la Commission évaluera de manière approfondie les progrès accomplis ».",
  "Institution européenne."))
CE_2035 = ('ce_2035', src("Cars and vans (CO2 emission performance standards)", "Commission européenne (DG Climat)", "30 janvier 2026",
  "https://climate.ec.europa.eu/areas-action/transport-decarbonisation/road-transport/cars-and-vans_en",
  "Selon la proposition de révision de décembre 2025, « from 2035 onwards, carmakers will need to comply with a 90% tailpipe emissions reduction target », les 10 % restants devant être compensés par de l'acier bas carbone produit dans l'Union, des carburants de synthèse ou des biocarburants ; hybrides rechargeables et moteurs thermiques pourraient ainsi encore être vendus après 2035. Il s'agit d'une proposition.",
  "Institution européenne."))
JA_2035 = ('ja_2035', src("Industrie automobile : le Parlement européen assouplit les objectifs de CO2 pour 2035", "Journal de l'Automobile (C. Leroy)", "4 novembre 2026",
  "https://journalauto.com/industrie/industrie-automobile-le-parlement-europeen-assouplit-les-objectifs-de-co2-pour-2035/",
  "La commission de l'environnement du Parlement européen a voté le 4 novembre 2026 (48 voix pour, 30 contre, 2 abstentions) un objectif de -87,5 % en 2035, compensable jusqu'à 7,5 points ; le vote en plénière est prévu mi-décembre 2026 et le Conseil doit encore se prononcer.",
  "Presse professionnelle spécialisée.", 'media'))
LCP_2035 = ('lcp_2035', src("Fin de la vente des voitures thermiques neuves en 2035 : l'Assemblée s'y oppose lors d'un vote, contre la volonté du gouvernement", "LCP (Raphaël Marchal)", "18 février 2025",
  "https://lcp.fr/actualites/fin-de-la-vente-des-voitures-thermiques-neuves-en-2035-l-assemblee-s-y-oppose-lors-d-un",
  "Le 17 février 2025, les députés ont supprimé par 34 voix contre 30 l'article qui transposait l'échéance de 2035 ; cette date « doit s'imposer à la France » en vertu de la primauté du droit européen.",
  "Média parlementaire.", 'media'))
CE_MERCOSUR = ('ce_mercosur', src("Accord commercial UE-Mercosur : distinguer le vrai du faux", "Commission européenne (représentation en France)", "27 avril 2026",
  "https://france.representation.ec.europa.eu/informations/accord-commercial-ue-mercosur-distinguer-le-vrai-du-faux-2025-10-14_fr",
  "Quotas : « 99 000 tonnes de viande bovine » à 7,5 % de droits, soit « 1,6% de la production totale » de l'UE ; « 180 000 tonnes de volaille » (1,4 %) ; clause de sauvegarde en cas de hausse des importations ou de baisse des prix de 5 % ; « Toutes les conditions sanitaires en vigueur au sein de l'Union européenne restent en place. »",
  "Institution européenne, partie prenante de l'accord."))
PS_MERCOSUR = ('ps_mercosur', src("Viande de bœuf, poulet, fromage, automobiles… Quels sont les produits concernés par l'accord UE-Mercosur ?", "Public Sénat (Romain David)", "12 décembre 2024",
  "https://www.publicsenat.fr/actualites/international/viande-de-boeuf-poulet-fromage-automobiles-quels-sont-les-produits-concernes-par-laccord-ue-mercosur",
  "Bœuf : quota de 99 000 tonnes, droit ramené d'environ 40 % à 7,5 % sur six ans ; volaille : 180 000 tonnes ; côté européen, gagnants attendus : vins (droits de 27 %), voitures (35 %), fromages (30 000 tonnes).",
  "Média parlementaire.", 'media'))
DELORS_MERCOSUR = ('delors_mercosur', src("Décrypter l'accord UE-Mercosur : ambitions, résistances et nouvelle géopolitique commerciale", "Institut Jacques Delors (avec Antoine Bouët, directeur du CEPII)", "2026",
  "https://institutdelors.eu/content/uploads/2026/07/MERCOSUR.pdf",
  "Selon l'étude Gohin et Matthews, la perte de revenu des éleveurs bovins de l'UE serait de 0,6 % ; les quotas représentent environ 1,5 % de la consommation de l'UE ; l'application provisoire a débuté le 1er mai 2026.",
  "Think tank européen, avec le directeur d'un centre public de recherche.", 'etude'))
LCP_MERCOSUR = ('lcp_mercosur', src("Mercosur : l'Assemblée nationale s'oppose très largement au projet d'accord lors d'un vote consultatif", "LCP (Raphaël Marchal)", "26 novembre 2024",
  "https://lcp.fr/actualites/mercosur-l-assemblee-nationale-s-oppose-tres-largement-au-projet-d-accord-lors-d-un-vote",
  "484 voix pour la déclaration du gouvernement hostile à l'accord, 70 contre ; les députés LFI ont voté contre la déclaration parce qu'ils refusent l'accord sans condition (« nous refusons l'accord tout court ») ; écologistes et communistes ont aussi exprimé leur opposition à l'accord.",
  "Média parlementaire.", 'media'))
CDJ_MERCOSUR = ('cdj_mercosur', src("Mercosur : le Parlement européen saisit la Cour de justice", "Le Club des juristes (Christine Kaddous, université de Genève)", "30 janvier 2026",
  "https://www.leclubdesjuristes.com/international/mercosur-le-parlement-europeen-saisit-la-cour-de-justice-14073/",
  "Le Conseil a autorisé la signature le 9 janvier 2026 malgré l'opposition de la France, qui n'a pas réuni de minorité de blocage ; l'accord intérimaire a été signé le 17 janvier 2026 ; le 21 janvier, le Parlement européen a saisi la Cour de justice de l'UE par 334 voix contre 324.",
  "Analyse juridique universitaire.", 'etude'))
SENAT_ISLAM16 = ('senat_islam16', src("De l'islam en France à un islam de France (brochure de la mission d'information)", "Sénat (Corinne Féret, Nathalie Goulet, André Reichardt)", "Juillet 2016",
  "https://www.senat.fr/fileadmin/Fichiers/Images/commission/missions/islam_en_france/14-Brochure_Mission_Islam.pdf",
  "Le culte musulman « serait essentiellement financé, comme les autres cultes, par les fidèles eux-mêmes » ; financements étatiques étrangers : Maroc environ 6 M€ en 2016, Algérie 2 M€ (Grande Mosquée de Paris), Arabie saoudite 3,8 M€ depuis 2011, Turquie indirectement via la rémunération des imams ; 301 imams détachés ; « Il est impossible de connaître les financements par des personnes privées étrangères. »",
  "Rapport parlementaire transpartisan (données de 2016)."))
LOCALTIS_ISLAM = ('localtis_islam', src("Un islam de France largement influencé par l'étranger", "Banque des Territoires (Localtis, M. Tendil)", "7 juillet 2016",
  "https://www.banquedesterritoires.fr/un-islam-de-france-largement-influence-par-letranger",
  "Le rapport sénatorial adopté le 5 juillet 2016 recense 301 imams détachés pour environ 2 500 lieux de culte ; seuls 20 à 30 % des imams seraient de nationalité française.",
  "Média public spécialisé rendant compte d'un rapport.", 'media'))
SP_CULTE = ('sp_culte', src("Comment une association cultuelle doit déclarer des financements étrangers du culte ?", "Service-public.fr (Direction de l'information légale et administrative)", "5 décembre 2025",
  "https://www.service-public.gouv.fr/associations/vosdroits/F36412",
  "Les associations cultuelles doivent déclarer les avantages et ressources venant de l'étranger d'un « montant supérieur à 15 300 € » par exercice (loi n° 2021-1109 du 24 août 2021, décret n° 2022-619) ; le ministre de l'Intérieur peut s'y opposer en cas de « menace réelle actuelle et suffisamment grave ».",
  "Site officiel de l'administration."))
MEE_IMAMS = ('mee_imams', src("France : l'interdiction des imams détachés bouleverse le culte musulman", "Middle East Eye (S. Lokmane)", "4 janvier 2024",
  "https://www.middleeasteye.net/fr/actu-et-enquetes/france-interdiction-imams-detaches-culte-musulman",
  "Le ministre de l'Intérieur a annoncé qu'il n'y aurait plus de nouveaux imams détachés à partir du 1er janvier 2024 et qu'un cadre serait créé pour que les associations emploient directement leurs imams ; selon le CFCM, les imams détachés ne représentaient que 8 % des imams.",
  "Média international.", 'media'))

# ── Sources : économie, programmes, institutions ───────────────────────────
CAE_EXIL = ('cae_exil', src("Fiscalité du capital : quels sont les effets de l'exil fiscal sur l'économie ? (Focus n° 118, communiqué)", "Conseil d'analyse économique (L. Bach, A. Bozio, N. Grimprel, A. Guillouzouic, C. Landais, C. Malgouyres)", "25 juillet 2025",
  "https://cae-eco.fr/static/pdf/Communique-de-presse_f118_exil_fiscal.pdf",
  "La hausse d'impôt de 2013 a augmenté les départs nets de 0,04 à 0,09 point chez les plus touchés, soit au plus 350 foyers par an sur environ 385 000 foyers du top 1 % ; quand un actionnaire important s'expatrie, son entreprise perd 15 % de chiffre d'affaires, mais une hausse de 4 Md€ de la fiscalité du top 1 % ne réduirait le chiffre d'affaires et la masse salariale nationaux que d'environ 0,03 % ; « la fiscalité du patrimoine a bien un impact significatif sur l'exil fiscal des plus hauts patrimoines ».",
  "Organisme public d'expertise économique placé auprès du Premier ministre."))
PS_ZUCMAN_ARG = ('ps_zucman_arg', src("Taxe Zucman : quels sont les arguments pour, et les arguments contre ?", "Public Sénat (Romain David)", "12 septembre 2025",
  "https://www.publicsenat.fr/actualites/economie/taxe-zucman-quels-sont-les-arguments-pour-et-les-arguments-contre",
  "Impôt plancher de 2 % au-delà de 100 M€ de patrimoine, touchant environ 0,01 % des foyers (environ 1 800 personnes selon la ministre des Comptes publics) ; rendement avancé par Gabriel Zucman : 20 Md€ par an, à plus ou moins 5 Md€ ; texte adopté à l'Assemblée le 20 février 2025, rejeté au Sénat le 12 juin 2025 par 188 voix contre 129.",
  "Média parlementaire.", 'media'))
SENAT_ZUCMAN = ('senat_zucman', src("L'essentiel sur la proposition de loi instaurant un impôt plancher de 2 % sur les très hauts patrimoines", "Sénat, commission des finances (Emmanuel Capus, rapporteur)", "4 juin 2025",
  "https://www.senat.fr/fileadmin/cru-1750816532/Commissions/Finances/2024-2025/Textes_legislatifs/Essentiel_PPL_IPF_Post_com.pdf",
  "Selon le rapporteur, le rendement « pourrait ne plus représenter que 2 à 3 milliards d'euros » dans son hypothèse ; « L'impôt pourrait entraîner un exil fiscal dont il est impossible d'anticiper l'ampleur » ; la base inclut les biens professionnels, et une jeune pousse très valorisée sans revenu courant pourrait obliger ses actionnaires à vendre des titres.",
  "Rapport parlementaire (majorité sénatoriale de droite, opposée au texte)."))
LCP_ZUCMAN = ('lcp_zucman', src("Taxation des ultrariches : Gabriel Zucman exhorte les députés à ne pas reproduire les erreurs du passé", "LCP (Maxence Kagni)", "1er octobre 2025",
  "https://lcp.fr/actualites/taxation-des-ultrariches-gabriel-zucman-exhorte-les-deputes-a-ne-pas-reproduire-les",
  "Gabriel Zucman propose un paiement en nature, « avec des actions de l'entreprise », en cas de manque de liquidités ; selon lui, « exonérer les biens professionnels voudrait simplement dire exonérer les milliardaires » ; il juge l'expatriation « limitée » et propose une taxation au moment du départ.",
  "Média parlementaire.", 'media'))
LCP_ZUCMAN_REJET = ('lcp_zucman_rejet', src("Budget 2026 : la taxe Zucman rejetée par l'Assemblée nationale", "LCP (Ludovic Fau)", "31 octobre 2025",
  "https://lcp.fr/actualites/budget-2026-la-taxe-zucman-rejetee-par-l-assemblee-nationale-413632",
  "Les amendements ont été rejetés par 228 voix contre 172 : la gauche a voté pour ; EPR, MoDem, Horizons, LR et RN ont voté contre ; une version du PS (« un impôt minimum de 3% à partir de 10 millions d'euros », excluant les entreprises innovantes et familiales) a aussi été rejetée.",
  "Média parlementaire.", 'media'))
MONTAIGNE_RN30 = ('montaigne_rn30', src("[Présidentielle – Chiffrage 2022] Marine Le Pen propose d'exonérer d'impôt sur le revenu « tous les jeunes » de moins de 30 ans", "Institut Montaigne (Victor Poirier)", "14 janvier 2022",
  "https://www.institutmontaigne.org/expressions/presidentielle-chiffrage-2022-marine-le-pen-propose-dexonerer-dimpot-sur-le-revenu-tous-les-jeunes",
  "Le RN chiffre la mesure à environ 2 Md€ par an ; l'Institut Montaigne l'estime à un peu plus de 3,6 Md€ par an ; les 18-25 ans gagnent trop peu pour être imposés, les bénéficiaires seraient surtout les actifs de 26 à 30 ans, pour un gain moyen de 374 € par an et par contribuable concerné ; la mesure serait « probablement inconstitutionnelle » et créerait « une différence de traitement injustifiée vis-à-vis du reste de la population active ».",
  "Think tank libéral (chiffrage de programme, 2022).", 'etude'))
PS_RN_PROG24 = ('ps_rn_prog24', src("Réforme des retraites, impôts, prix planchers… Comment le RN réajuste son programme au fil de la campagne", "Public Sénat (Romain David)", "27 juin 2024",
  "https://www.publicsenat.fr/actualites/politique/reforme-des-retraites-impots-prix-planchers-comment-le-rn-reajuste-son-programme-au-fil-de-la-campagne",
  "Le programme 2024 veut « supprimer l'impôt sur le revenu des jeunes de moins de 30 ans » ; face aux critiques, un vice-président du RN déclare : « Tout cela peut se moduler, il peut y avoir de plafonds » ; sur les retraites, un député RN : « ceux qui ont travaillé entre 17 et 20 ans : retraite à 60 ans, avec 40 annuités » ; Jordan Bardella lie l'engagement à la situation budgétaire.",
  "Média parlementaire.", 'media'))
LCP_RN_JEUNES = ('lcp_rn_jeunes', src("Permis de conduire gratuit, exonération d'impôt jusqu'à 30 ans... Comment le RN veut convaincre les jeunes", "LCP (Raphaël Marchal)", "6 octobre 2026",
  "https://lcp.fr/actualites/permis-de-conduire-gratuit-exoneration-d-impot-jusqu-a-30-ans-comment-le-rn-veut",
  "Marine Le Pen reprend l'exonération d'impôt sur le revenu des moins de 30 ans avec une limite « jusqu'à quatre fois le Smic » ; la mesure « coûterait 2 milliards d'euros aux finances publiques chaque année ».",
  "Média parlementaire.", 'media'))
MONEYVOX_RN30 = ('moneyvox_rn30', src("Impôt sur le revenu : Le Pen peut-elle vraiment exonérer les jeunes de moins de 30 ans ?", "MoneyVox (Samuel Auffray)", "13 avril 2022",
  "https://www.moneyvox.fr/impot/actualites/88012/impot-sur-le-revenu-le-pen-peut-elle-vraiment-exonerer-les-jeunes-de-moins-de-30-ans",
  "Sans condition de revenus, un footballeur millionnaire bénéficierait de la même exonération qu'un jeune au Smic, qui paie probablement peu d'impôt, « comme la majorité des jeunes en début de carrière » ; un juriste estime qu'au minimum « une condition de revenus devrait être introduite ».",
  "Presse économique grand public (2022).", 'media'))
PS_RN_RETR22 = ('ps_rn_retr22', src("Retraite à 60 ans : Marine Le Pen corrige sa copie", "Public Sénat (Louis Dubar)", "17 février 2022 (mis à jour le 4 avril 2022)",
  "https://www.publicsenat.fr/actualites/non-classe/retraite-a-60-ans-marine-le-pen-corrige-sa-copie-193936",
  "Le RN promettait auparavant une retraite à taux plein dès 60 ans pour tous ; il passe en 2022 à un système progressif : 60 ans et 160 trimestres pour ceux qui ont commencé à travailler entre 17 et 20 ans, puis davantage de trimestres pour les autres (au moins 42 annuités à partir de 25 ans) ; la retraite à 60 ans n'est donc « plus pour tout le monde ».",
  "Média parlementaire.", 'media'))
LCP_RN_RETR24 = ('lcp_rn_retr24', src("Législatives 2024 : le Rassemblement national et le Nouveau Front populaire précisent leurs projets sur les retraites", "LCP (Maxence Kagni)", "26 juin 2024",
  "https://lcp.fr/actualites/legislatives-2024-le-rassemblement-national-et-le-nouveau-front-populaire-precisent",
  "Le RN propose 60 ans pour les carrières commencées avant 20 ans, avec « 40 annuités de cotisation » ; pour les autres, âge pivot de 62 ans et 42 annuités (exemple : début à 24 ans, taux plein à 66 ans, ou départ à 62 ans avec décote) ; le volet « avant 20 ans » est chiffré à « 1,6 milliard d'euros ».",
  "Média parlementaire.", 'media'))
MONTAIGNE_RN_RETR = ('montaigne_rn_retr', src("Législatives 2024 — Rassemblement national : abroger la réforme des retraites et, pour ceux ayant commencé à travailler avant 20 ans, partir à 40 annuités de cotisations", "Institut Montaigne", "24 juin 2024",
  "https://www.institutmontaigne.org/legislatives-2024/rassemblement-national/abroger-la-reforme-des-retraites-et-pour-ceux-ayant-commence-a-travailler-avant-20-ans-partir-a-40-annuites-de-cotisations",
  "Coût estimé à 34,7 Md€ par an (fourchette de 31,5 à 44,7 Md€) ; la deuxième étape (62 ans et jusqu'à 42 annuités) serait décidée après un audit des comptes.",
  "Think tank libéral (chiffrage de programme).", 'etude'))
PS_RN_RETR26 = ('ps_rn_retr26', src("Retraites : le RN réfléchit à supprimer l'âge légal de départ, mais « ce n'est pas aussi simple », estime Jean-Philippe Tanguy", "Public Sénat (Louis Mollier-Sabet)", "27 mai 2026",
  "https://www.publicsenat.fr/actualites/economie/retraites-le-rn-reflechit-a-supprimer-lage-legal-de-depart-mais-ce-nest-pas-aussi-simple-estime-jean-philippe-tanguy-rn",
  "Un député RN : « Nous reviendrons sur la réforme Borne », « on revient sur 62 ans et 42 annuités » ; le RN étudierait la suppression de l'âge légal, ce qui « n'est pas si simple » ; Jordan Bardella dit « examiner » un éventuel report de l'âge légal.",
  "Média parlementaire.", 'media'))
DATAN_SMIC44 = ('datan_smic44', src("Scrutin n° 44 (16e législature) : amendement n° 94 « Augmenter le SMIC à 1500 euros net mensuel » (projet de loi pouvoir d'achat)", "Datan, d'après les scrutins publics de l'Assemblée nationale", "20 juillet 2022",
  "https://datan.fr/votes/legislature-16/vote_44",
  "Amendement rejeté par 255 voix contre 121 ; groupe RN : 69 contre, 1 abstention, 0 pour.",
  "Site d'analyse des votes reprenant les scrutins publics officiels.", 'secondaire'))
DATAN_SMIC42 = ('datan_smic42', src("Scrutin n° 42 (16e législature) : amendement n° 938 sur l'indexation des salaires du privé sur l'inflation", "Datan, d'après les scrutins publics de l'Assemblée nationale", "20 juillet 2022",
  "https://datan.fr/votes/legislature-16/vote_42",
  "Amendement rejeté par 269 voix contre 108 ; groupe RN : 69 contre, 0 pour.",
  "Site d'analyse des votes reprenant les scrutins publics officiels.", 'secondaire'))
DATAN_SMIC38 = ('datan_smic38', src("Scrutin n° 38 (16e législature) : amendement n° 116 conditionnant les exonérations de cotisations au respect du SMIC dans les grilles de branche", "Datan, d'après les scrutins publics de l'Assemblée nationale", "20 juillet 2022",
  "https://datan.fr/votes/legislature-16/vote_38",
  "Amendement rejeté par 183 voix contre 181 ; groupe RN : 69 pour.",
  "Site d'analyse des votes reprenant les scrutins publics officiels.", 'secondaire'))
LCP_RN_SAL = ('lcp_rn_sal', src("Salaires : la proposition de loi du Rassemblement national recalée par l'Assemblée", "LCP (Maxence Kagni)", "12 janvier 2023",
  "https://lcp.fr/actualites/salaires-la-proposition-de-loi-du-rassemblement-national-recalee-par-l-assemblee-160427",
  "La proposition RN permettait aux entreprises volontaires d'augmenter les salaires nets de 10 %, hausses exonérées de « l'essentiel des charges » pour « tous les salaires jusqu'à trois fois le Smic » ; Marine Le Pen oppose ce dispositif à une hausse du Smic, qui « peut mettre en difficulté quelques entreprises » ; un député Renaissance juge la mesure « budgétairement coûteuse, économiquement inefficace ».",
  "Média parlementaire.", 'media'))
DATAN_LEG24 = ('datan_leg24', src("Législatives 2024 : la gauche en tête d'une Assemblée nationale fragmentée et sans majorité", "Datan", "8 juillet 2024",
  "https://datan.fr/blog/actualite-politique/legislatives-2024-la-gauche-en-tete-dune-assemblee-nationale-fragmentee-et-sans-majorite",
  "Sièges : Nouveau Front populaire 182, Ensemble 168, RN 143 ; la majorité absolue est de 289 sièges et il manque « plus de 100 sièges » au NFP ; « Trois blocs politiques et aucune majorité. »",
  "Site d'analyse parlementaire.", 'secondaire'))
LEGI_ART8 = ('legi_art8', src("Constitution du 4 octobre 1958, article 8", "Légifrance", "4 octobre 1958 (version en vigueur)",
  "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/2017-07-23",
  "« Le Président de la République nomme le Premier ministre. Il met fin à ses fonctions sur la présentation par celui-ci de la démission du Gouvernement. »",
  "Texte constitutionnel."))
PS_CASTETS = ('ps_castets', src("Refus de nommer Lucie Castets : est-ce une « faute institutionnelle » comme le prétend François Hollande ?", "Public Sénat (Henri Clavier)", "28 août 2024",
  "https://www.publicsenat.fr/actualites/institutions/refus-de-nommer-lucie-castets-est-ce-une-faute-institutionnelle-comme-le-pretend-francois-hollande",
  "Pour un constitutionnaliste de l'université Paris Cité, « il peut nommer qui il veut, c'est ensuite à l'Assemblée nationale de censurer » ; pour un autre, de l'université Paris Nanterre, « il n'a plus un pouvoir discrétionnaire de nomination du Premier ministre » ; l'article rappelle qu'aucune règle n'oblige à choisir le Premier ministre dans le parti qui a le plus de voix.",
  "Média parlementaire, avec avis de constitutionnalistes.", 'media'))
LCP_NFP_REJET = ('lcp_nfp_rejet', src("Rejet du Nouveau Front populaire à Matignon par Emmanuel Macron : les réactions à l'Assemblée", "LCP (L. Dermarkarian)", "27 août 2024",
  "https://lcp.fr/actualites/rejet-du-nouveau-front-populaire-a-matignon-par-emmanuel-macron-a-l-assemblee-reactions",
  "Selon l'Élysée, un gouvernement NFP « serait immédiatement censuré par l'ensemble des autres groupes » ; le communiqué qualifie le NFP d'« alliance regroupant le plus de députés ».",
  "Média parlementaire.", 'media'))
LCP_BARNIER = ('lcp_barnier', src("Nouveau gouvernement : Michel Barnier nommé Premier ministre", "LCP (S. Bonvarlet)", "5 septembre 2024",
  "https://lcp.fr/index%2Ephp/actualites/nouveau-gouvernement-michel-barnier-nomme-premier-ministre-309194",
  "Michel Barnier (LR) a été nommé Premier ministre « près de deux mois après le résultat des élections législatives ».",
  "Média parlementaire.", 'media'))

FICHES = []

# 1 ── Pacte de Marrakech ─────────────────────────────────────────────────────
FICHES.append(fiche(
 id='pacte-marrakech-onu', affirmation="Le pacte de Marrakech de l'ONU oblige la France à accepter une immigration massive.", volet='immigration', sous_theme='Immigration et asile',
 mots_cles=['pacte de marrakech', 'marrakech', 'pacte mondial sur les migrations', 'pacte mondial', 'pacte de l onu', 'onu migrations', 'migrations sures ordonnees'],
 verdict='contredit', fiabilite='etabli',
 resume="Le pacte mondial pour des migrations sûres, ordonnées et régulières, approuvé à Marrakech en décembre 2018 par environ 150 pays, se définit lui-même comme « non contraignant ». Il réaffirme le droit souverain de chaque État de fixer sa politique migratoire, ne crée aucune obligation juridique nouvelle et ne prévoit ni quota ni sanction.",
 contexte="Le pacte a été présenté en 2018 par le RN, une partie de LR et Debout la France comme un abandon de souveraineté. Il revient régulièrement sur les réseaux sociaux comme preuve d'une immigration « organisée ».",
 explication="Un pacte de ce type est un texte politique de coopération (de la « soft law »), pas un traité qui s'impose aux États. Il fixe 23 objectifs (statistiques, lutte contre les passeurs, retours, droits des migrants), mais chaque pays reste libre de ses choix.",
 sources=[ONU_GCM, AN_QE15251, CDJ_GCM, PS_GCM],
 faits=[
  fait("Le texte du pacte se définit comme un « cadre de coopération juridiquement non contraignant ».", 'onu_gcm', '2018', 'Monde', "C'est écrit noir sur blanc dans le pacte lui-même.", 'etabli'),
  fait("Le pacte « réaffirme le droit souverain des États de déterminer leur politique migratoire nationale » (§ 15).", 'onu_gcm', '2018', 'Monde', "La souveraineté est un principe directeur du texte, pas une victime.", 'etabli'),
  fait("Selon le ministère des Affaires étrangères, le pacte « ne crée pas d'obligations juridiques autres que celles auxquelles un Etat a déjà souscrit » et n'a « pas d'impact sur notre souveraineté nationale ».", 'an_qe15251', '2019', 'France', "La position officielle de la France est sans ambiguïté.", 'etabli'),
  fait("Selon un professeur de droit, le seul suivi prévu est un forum intergouvernemental tous les quatre ans : « Il ne s'agit donc nullement de contrôle ou de surveillance ».", 'cdj_gcm', '2018', 'Monde', "Aucun mécanisme ne peut forcer la France à accueillir qui que ce soit.", 'etabli'),
  fait("Selon Public Sénat, des opposants au pacte ont évoqué des effets indirects possibles « à terme », par la jurisprudence, sur la souveraineté ou les expulsions.", 'ps_gcm', '2018', 'France', "C'est un scénario avancé par des responsables politiques, pas un effet observé.", 'interpretation'),
 ],
 court="Faux : le pacte de Marrakech se dit lui-même « juridiquement non contraignant », réaffirme le droit de chaque État de fixer sa politique migratoire et ne prévoit aucun quota ni aucune sanction.",
 moyen="Le pacte de Marrakech (2018) est un texte de coopération signé par environ 150 pays. Il se définit lui-même comme « non contraignant » et réaffirme que chaque État fixe souverainement sa politique migratoire.\n\nLe ministère des Affaires étrangères l'a confirmé : il ne crée aucune obligation nouvelle. Il n'y a ni quota, ni tribunal, ni sanction ; seulement un forum tous les quatre ans. Rien dans le texte n'empêche la France de choisir sa propre politique migratoire, plus ouverte ou plus restrictive.",
 detaille="Le pacte mondial pour des migrations sûres, ordonnées et régulières a été approuvé à Marrakech en décembre 2018 par environ 150 pays. Il fixe 23 objectifs : améliorer les données, lutter contre les passeurs, organiser les retours, respecter les droits des personnes migrantes.\n\nSon paragraphe 7 le définit comme un « cadre de coopération juridiquement non contraignant », et son principe de souveraineté nationale réaffirme le droit de chaque État de déterminer sa politique migratoire. En réponse à une question écrite, le ministère des Affaires étrangères a indiqué qu'il ne crée pas d'obligations juridiques nouvelles et n'a pas d'impact sur la souveraineté nationale.\n\nPour le juriste Thibaut Fleury Graff, il s'agit de « souhaits ou de recommandations », sans contrôle ni surveillance. Ses opposants avancent que des juges pourraient s'en inspirer ; ce scénario reste une hypothèse. Le vrai débat porte sur les politiques que chaque pays choisit, pas sur ce texte.",
 empathie="Je comprends qu'un texte de l'ONU sur les migrations inquiète, surtout quand on entend qu'il nous « oblige ». Mais le texte dit lui-même qu'il n'oblige à rien et que chaque pays reste maître de sa politique.",
 legitimes=["Le pacte est un texte politique qui oriente les politiques migratoires, même sans contrainte juridique.", "Il a été peu débattu publiquement en France avant sa signature, ce qui a nourri la méfiance."],
 contre=[
  ("Les juges finiront par l'appliquer.", "C'est une hypothèse de ses opposants ; aucune source lue ne montre une décision qui l'aurait imposé à la France."),
  ("Pourquoi signer un texte qui ne sert à rien ?", "Il sert à coopérer (données, lutte contre les passeurs, retours) : coopérer n'est pas obéir."),
 ],
 questions=["Peux-tu me montrer l'article du pacte qui obligerait la France à accueillir des migrants ?", "Qu'est-ce qui, dans le texte, empêcherait la France de durcir ses lois sur l'immigration ?"],
 limites=["Les sources datent de 2018-2019 ; le texte lu est le projet final du pacte, très proche du texte adopté.", "Les effets indirects du pacte sur la jurisprudence n'ont pas été étudiés par les sources lues."],
 publics={'convaincus': "Le texte dit lui-même, au paragraphe 7, qu'il est « non contraignant », et au paragraphe 15 qu'il respecte le droit de chaque pays de fixer sa politique migratoire. Il n'y a ni quota, ni tribunal, ni sanction : rien n'oblige la France à accueillir qui que ce soit.",
  'indecis': "Ce pacte est un texte de coopération entre environ 150 pays, pas un traité qui s'impose. Il ne contient ni quota ni sanction, et la France l'a confirmé officiellement. On peut débattre de la politique migratoire, mais elle se décide ici, pas à Marrakech."},
 a_actualiser='2027-12-31',
))

# 2 ── Pacte européen ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='pacte-europeen-migration-asile', affirmation="Le pacte européen sur la migration et l'asile va imposer des milliers de migrants à la France.", volet='immigration', sous_theme='Immigration et asile',
 mots_cles=['pacte europeen', 'pacte asile et migration', 'pacte sur la migration et l asile', 'relocalisation', 'relocalisations', 'solidarite obligatoire', '20 000 euros par migrant', 'amende de 20 000'],
 verdict='trompeur', fiabilite='etabli',
 resume="Le pacte européen, appliqué depuis juin 2026, crée une solidarité obligatoire mais flexible : chaque État choisit entre accueillir des demandeurs d'asile relocalisés, payer 20 000 € par personne non accueillie ou fournir un autre soutien, et « aucun État membre ne sera obligé de procéder à des relocalisations ». Pour 2026, la part indicative de la France est d'environ 3 361 « relocalisations ou autres formes de soutien », et moins de 1 000 transferts réels sont attendus dans toute l'Union.",
 contexte="Le RN présente le pacte comme une obligation d'accueillir des migrants ou de payer une « amende ». Le texte est entré en application complète en juin 2026.",
 explication="Le pacte réforme les règles de l'asile dans l'UE (filtrage aux frontières, procédures, solidarité entre pays). Son volet « solidarité » est obligatoire dans son principe, mais chaque pays choisit la forme de sa contribution et peut déduire les demandeurs qu'il accueille déjà.",
 sources=[CONSEIL_PACTE, UE_RESERVE26, EURONEWS_PACTE, EURONEWS_PACTE2],
 faits=[
  fait("Selon le Conseil de l'UE, le nombre annuel minimum de relocalisations est fixé à 30 000 dans l'Union, avec une contribution de 20 000 euros par relocalisation non effectuée ; « Aucun État membre ne sera obligé de procéder à des relocalisations. »", 'conseil_pacte', '2023', 'Union européenne', "Accueillir n'est qu'une option parmi d'autres.", 'etabli', '30 000'),
  fait("Selon la décision du Conseil pour 2026, la réserve de solidarité est de 21 000 relocalisations et 420 millions d'euros pour toute l'Union ; la part de la France (16 %) correspond à environ 3 361 « relocalisations ou autres formes de soutien ».", 'ue_reserve26', '2026', 'Union européenne', "Il y a bien une contribution française obligatoire, mais pas forcément sous forme d'accueil.", 'etabli', '3 361'),
  fait("Selon Euronews, le paiement de 20 000 € par personne non accueillie « ne constitue donc pas une amende » : c'est une forme de solidarité au choix de l'État.", 'euronews_pacte', '2026', 'Union européenne', "Le mot « amende » est trompeur.", 'etabli', '20 000 €'),
  fait("Selon Euronews, les pays non soumis à une pression migratoire ont promis 8 878 relocalisations, et moins de 1 000 demandeurs d'asile devraient être réellement transférés en 2026 ; la France déduit de sa part les demandeurs qu'elle accueille déjà.", 'euronews_pacte2', '2026', 'Union européenne', "En pratique, les transferts sont très limités.", 'estimation', '1 000'),
 ],
 court="Trompeur : le pacte rend la solidarité obligatoire mais laisse chaque pays choisir sa forme ; « aucun État membre ne sera obligé de procéder à des relocalisations », et moins de 1 000 transferts réels sont attendus dans toute l'Union en 2026.",
 moyen="Le pacte européen oblige chaque pays à être solidaire, mais pas à accueillir. On peut accueillir des demandeurs relocalisés, payer 20 000 € par personne non accueillie ou fournir un autre soutien. Le Conseil de l'UE l'écrit : « Aucun État membre ne sera obligé de procéder à des relocalisations. »\n\nPour 2026, la part de la France est d'environ 3 361 « relocalisations ou autres formes de soutien », et elle déduit les demandeurs qu'elle accueille déjà. Dans toute l'Union, moins de 1 000 personnes devraient être réellement transférées cette année.",
 detaille="Adopté en 2024 et appliqué depuis juin 2026, le pacte européen sur la migration et l'asile réforme le filtrage aux frontières, les procédures d'asile et la répartition des responsabilités. Son volet solidarité prévoit chaque année au moins 30 000 relocalisations dans l'Union, ou des contributions de 20 000 € par relocalisation non effectuée, ou d'autres soutiens (appui opérationnel, équipements).\n\nPour 2026, le Conseil a fixé une réserve de 21 000 relocalisations et 420 millions d'euros. La part de la France, 16 %, correspond à environ 3 361 « relocalisations ou autres formes de soutien » ; la France est classée parmi les pays « qui risquent de subir une pression migratoire », ce qui lui permet de déduire les demandeurs qu'elle accueille déjà.\n\nLes États ont promis moins de 9 000 relocalisations, et moins de 1 000 transferts réels sont attendus. On peut critiquer le pacte, y compris à gauche pour le filtrage et la détention aux frontières ; mais il n'« impose » pas des milliers de migrants à la France.",
 empathie="Je comprends qu'on se méfie quand on entend que Bruxelles va nous « imposer » des migrants. Mais le pacte laisse chaque pays choisir sa façon d'aider, et la France peut compter les demandeurs qu'elle accueille déjà.",
 legitimes=["La contribution de la France est obligatoire dans son principe et se chiffre en milliers d'unités de solidarité.", "On peut contester le pacte pour d'autres raisons (procédures accélérées et rétention aux frontières, critiquées par des associations de défense des droits)."],
 contre=[
  ("Si on refuse, on paie une amende de 20 000 € par migrant.", "C'est une contribution au choix, pas une sanction ; Euronews montre que ce n'est pas une amende."),
  ("Les chiffres vont augmenter chaque année.", "Pour 2026, la réserve fixée (21 000) est inférieure au minimum de référence (30 000), et les promesses réelles sont encore plus basses."),
 ],
 questions=["Savais-tu qu'un pays peut choisir de ne relocaliser personne et de contribuer autrement ?", "Combien de personnes crois-tu que l'UE va réellement transférer en 2026 ?"],
 limites=["La répartition exacte de la part française entre relocalisations et autres soutiens n'a pas été confirmée sur EUR-Lex ; le chiffre de 3 361 vient d'une version relayée de la décision.", "Le vote de la France sur le pacte en 2024 n'a pas pu être vérifié à partir des sources lues."],
 publics={'convaincus': "Lis le texte du Conseil : « Aucun État membre ne sera obligé de procéder à des relocalisations. » Les 20 000 € ne sont pas une amende, c'est une option parmi d'autres. Et en 2026, moins de 1 000 personnes seront transférées dans toute l'Europe : on est loin de l'invasion annoncée.",
  'indecis': "Le pacte oblige les pays à s'entraider, mais chacun choisit comment : accueillir, payer ou fournir du matériel. La part de la France pour 2026 tourne autour de 3 000 unités de solidarité, et elle peut y déduire les demandeurs déjà présents. On peut critiquer ce pacte, mais pas pour cette raison-là."},
 a_actualiser='2027-06-30',
))

# 3 ── Accord franco-algérien ─────────────────────────────────────────────────
FICHES.append(fiche(
 id='accord-franco-algerien-1968', affirmation="L'accord franco-algérien de 1968 donne des privilèges aux Algériens.", volet='immigration', sous_theme='Réfugiés et statuts administratifs',
 mots_cles=['accord franco algerien', 'accords de 1968', 'accord de 1968', 'algeriens privileges', 'algeriens', 'algerie 1968', 'denoncer l accord'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="En partie : l'accord de 1968, modifié en 1985, 1994 et 2001, donne aux Algériens certains avantages (regroupement familial après 12 mois au lieu de 18, accès plus rapide au titre de 10 ans), mais il les prive aussi de plusieurs titres du droit commun (carte pluriannuelle, admission exceptionnelle au séjour) et rend leur régularisation plus difficile. Le surcoût d'environ 2 milliards avancé par un rapport parlementaire de 2025 est jugé « imprécis » par ses auteurs eux-mêmes.",
 contexte="Le RN et une partie de la droite demandent la dénonciation de l'accord ; l'Assemblée a adopté le 30 octobre 2025 une résolution en ce sens, sans valeur contraignante pour le gouvernement.",
 explication="L'accord fixe un régime spécial d'entrée et de séjour pour les Algériens, à la place du code des étrangers (CESEDA). Selon les situations, ce régime est plus favorable ou plus défavorable que le droit commun.",
 sources=[LCP_ALGERIE68, PS_ALGERIE68, UM_ALGERIE68],
 faits=[
  fait("Selon Public Sénat et LCP, les Algériens peuvent demander le regroupement familial au bout d'un an de séjour, contre 18 mois dans le droit commun.", 'ps_algerie68', '2023-2025', 'France', "C'est un avantage réel, qu'il faut reconnaître.", 'etabli', '12 mois'),
  fait("Selon Public Sénat, les parents d'enfants français et les conjoints de Français algériens obtiennent un certificat de résidence de 10 ans, contre un titre d'un an dans le droit commun.", 'ps_algerie68', '2023', 'France', "Autre avantage, pour les familles de Français.", 'etabli', '10 ans'),
  fait("Selon Public Sénat, les Algériens n'ont pas accès à certains titres créés par les lois de 2003, 2016 et 2018, dont la carte pluriannuelle, ni à l'admission exceptionnelle au séjour ; les expulsions relèvent du droit commun.", 'ps_algerie68', '2023', 'France', "L'accord comporte aussi des désavantages.", 'etabli'),
  fait("Selon un juriste de l'université Paul-Valéry, les étudiants algériens doivent renouveler leur titre chaque année avec moins d'heures de travail autorisées, et 15 ans de présence sont exigés pour une régularisation, contre 10 ans pour les autres étrangers.", 'um_algerie68', '2023', 'France', "Sur la régularisation, les Algériens sont moins bien traités.", 'etabli', '15 ans'),
  fait("Selon LCP, le rapport des députés Rodwell et Lefèvre (2025) estime le surcoût à environ 2 milliards d'euros, tout en admettant que cette estimation « est imprécise ».", 'lcp_algerie68', '2025', 'France', "Le chiffre souvent repris n'est pas solidement établi.", 'estimation', '2 Md€'),
 ],
 court="En partie vrai : l'accord donne quelques avantages aux Algériens (regroupement familial après 12 mois au lieu de 18, titre de 10 ans plus rapide), mais il leur ferme aussi plusieurs titres du droit commun et rend leur régularisation plus difficile (15 ans de présence au lieu de 10).",
 moyen="Oui, l'accord de 1968 donne certains avantages : regroupement familial après un an au lieu de 18 mois, titre de dix ans plus rapide pour les conjoints et parents de Français.\n\nMais il a aussi des désavantages : pas d'accès à la carte pluriannuelle ni à l'admission exceptionnelle au séjour, des étudiants plus contraints, et 15 ans de présence exigés pour une régularisation au lieu de 10. Et le chiffre de 2 milliards de surcoût est jugé « imprécis » par les députés qui l'avancent. Parler de « privilèges » en bloc, c'est ne raconter que la moitié de l'histoire.",
 detaille="Signé six ans après l'indépendance, l'accord du 27 décembre 1968 organise un régime spécial pour les Algériens. Il a été modifié en 1985, 1994 et 2001, ce qui l'a rapproché du droit commun.\n\nCertains points sont plus favorables : regroupement familial au bout d'un an de séjour (18 mois sinon), certificat de résidence de dix ans pour les conjoints et parents de Français, création d'entreprise sans preuve de viabilité. D'autres sont plus défavorables : pas d'accès à plusieurs titres créés depuis 2003 (dont la carte pluriannuelle et l'admission exceptionnelle au séjour), étudiants obligés de renouveler leur titre chaque année, régularisation après 15 ans de présence au lieu de 10. Les expulsions relèvent du droit commun.\n\nUn rapport parlementaire de 2025 chiffre le surcoût à environ 2 milliards d'euros, mais ses auteurs reconnaissent que l'estimation est « imprécise ». La résolution adoptée par l'Assemblée en octobre 2025 n'oblige pas le gouvernement. On peut vouloir renégocier l'accord ; encore faut-il le faire sur des faits complets.",
 empathie="Je comprends qu'on trouve injuste qu'une nationalité ait un régime à part. C'est vrai qu'il y a quelques avantages. Mais il y a aussi des règles plus dures, et le coût annoncé n'est pas solide.",
 legitimes=["L'accord contient de vrais avantages par rapport au droit commun (regroupement familial, titre de 10 ans).", "Le rapport parlementaire de 2025 souligne une absence de réciprocité ; c'est un argument de négociation recevable."],
 contre=[
  ("Ça coûte 2 milliards par an.", "Les auteurs du rapport eux-mêmes jugent leur estimation « imprécise », et un député a relevé l'absence de tableaux pour l'étayer."),
  ("Il suffit de le dénoncer.", "L'accord ne contient pas de clause de dénonciation, et la résolution de l'Assemblée n'a qu'une valeur d'appel."),
 ],
 questions=["Savais-tu qu'un Algérien sans papiers doit prouver 15 ans de présence pour être régularisé, contre 10 ans pour les autres étrangers ?", "Sur quoi repose exactement le chiffre de 2 milliards ?"],
 limites=["Les sources ne concordent pas sur le délai d'accès au titre de dix ans dans le cas général ; la fiche ne le chiffre pas.", "Le rapport parlementaire de 2025 n'a pas été lu directement, seulement sa présentation par LCP ; l'article de Public Sénat est antérieur à la loi immigration de 2024."],
 publics={'convaincus': "Tu as raison sur un point : il y a quelques avantages, comme le regroupement familial plus rapide. Mais l'accord est aussi plus dur que le droit commun : un Algérien sans papiers doit prouver 15 ans de présence pour être régularisé, au lieu de 10 pour les autres. Et les 2 milliards, même les députés qui les avancent disent que c'est « imprécis ».",
  'indecis': "L'accord de 1968 n'est ni un privilège total ni un détail : il mélange des règles plus favorables et d'autres plus sévères que pour les autres étrangers. Le coût souvent cité n'est pas solidement établi. C'est un sujet de négociation diplomatique, pas une preuve que la France serait « soumise »."},
 a_actualiser='2027-06-30',
))

# 4 ── Aide au développement Algérie ──────────────────────────────────────────
FICHES.append(fiche(
 id='aide-developpement-algerie', affirmation="La France verse des milliards d'aide au développement à l'Algérie.", volet='international', sous_theme='Relations internationales',
 mots_cles=['aide au developpement', 'aide publique au developpement', 'apd', 'aide a l algerie', 'algerie aide', '800 millions', 'milliards a l algerie'],
 verdict='contredit', fiabilite='etabli',
 resume="Non : l'aide publique au développement de la France vers l'Algérie est d'environ 131 à 140 millions d'euros par an (2022-2024), et environ 95 % correspondent aux frais de scolarité et coûts imputés d'étudiants algériens en France, dépensés en France. Les transferts directs sont de l'ordre de quelques millions. Le chiffre de 800 millions qui circule est un cumul sur 2018-2024.",
 contexte="Lors des tensions diplomatiques avec l'Algérie en 2024-2025, des responsables politiques ont affirmé que la France « donnait » des centaines de millions, voire des milliards, à l'Algérie.",
 explication="L'aide publique au développement (APD) déclarée à l'OCDE inclut des dépenses faites en France, comme le coût des étudiants étrangers dans les universités françaises. Ce n'est pas de l'argent versé au gouvernement algérien.",
 sources=[AN_QE4014, FOCUS_ALGERIE],
 faits=[
  fait("Selon le ministère des Affaires étrangères, l'APD bilatérale vers l'Algérie a atteint 136 millions d'euros en 2023 (131 millions en 2022).", 'an_qe4014', '2022-2023', 'France-Algérie', "On est à environ un dixième de milliard par an.", 'etabli', '136 M€'),
  fait("Selon le ministère, cette aide consiste principalement en bourses et coûts imputés d'élèves algériens étudiant en France : 128 millions d'euros en 2023.", 'an_qe4014', '2023', 'France', "L'argent est dépensé dans les universités françaises.", 'etabli', '128 M€'),
  fait("Selon Focus 2030, d'après l'OCDE, l'APD vers l'Algérie était de 140 millions d'euros en 2024, dont 132,5 millions de frais de scolarité, et seulement 5,3 millions de transferts directs.", 'focus_algerie', '2024', 'France-Algérie', "Ce qui part réellement en Algérie se compte en millions.", 'etabli', '5,3 M€'),
  fait("Selon Focus 2030, sur 2018-2024, l'APD vers l'Algérie a été en moyenne de 116 millions d'euros par an, soit environ 800 millions au total, dont 96 % dépensés en France.", 'focus_algerie', '2018-2024', 'France-Algérie', "Le chiffre de 800 millions est un cumul sur sept ans, pas un montant annuel.", 'etabli', '800 M€'),
  fait("Selon le ministère, aucun projet ne sera financé en 2025 par le don-projet de l'AFD en Algérie.", 'an_qe4014', '2025', 'France-Algérie', "Il n'y a pas de grands projets financés par des dons.", 'etabli'),
 ],
 court="Faux : l'aide française comptée vers l'Algérie est d'environ 140 millions d'euros par an, et 95 % correspondent au coût d'étudiants algériens dans les universités françaises. Ce qui est réellement versé en Algérie se compte en quelques millions.",
 moyen="On est très loin des milliards : environ 136 millions d'euros en 2023 et 140 millions en 2024, selon le ministère et l'OCDE.\n\nEt surtout, presque tout reste en France : ce sont les frais de scolarité et le coût des étudiants algériens dans nos universités, que la France déclare comme « aide au développement ». Les transferts directs vers l'Algérie sont d'environ 5 millions par an. Le chiffre de 800 millions qui circule est un total sur sept ans.",
 detaille="Selon la réponse du ministère des Affaires étrangères à une question écrite de 2025, l'aide publique au développement bilatérale vers l'Algérie a atteint 136 millions d'euros en 2023, après 131 millions en 2022. Elle consiste principalement en bourses et en coûts imputés d'élèves algériens étudiant en France (128 millions d'euros). L'AFD ne financera aucun projet par don en Algérie en 2025.\n\nD'après les données de l'OCDE analysées par Focus 2030, l'APD vers l'Algérie était de 140 millions d'euros en 2024, dont 132,5 millions de frais de scolarité ; les transferts directs ne représentaient que 5,3 millions. Sur 2018-2024, la moyenne est de 116 millions par an, soit environ 800 millions au total, dont 96 % dépensés en France.\n\nCes étudiants contribuent aussi à la vie scientifique et économique française. On peut débattre de la manière de comptabiliser l'aide au développement, mais présenter cette somme comme des milliards versés au régime algérien est faux.",
 empathie="Je comprends qu'on se demande pourquoi la France aiderait un pays avec lequel les relations sont tendues. Mais il ne s'agit pas d'argent donné au gouvernement algérien : c'est surtout le coût d'étudiants dans nos universités.",
 legitimes=["L'Algérie figure bien parmi les bénéficiaires de l'aide française déclarée à l'OCDE.", "On peut discuter du fait de compter les étudiants étrangers dans l'aide au développement."],
 contre=[
  ("Il paraît que c'est 800 millions.", "C'est un total sur 2018-2024, soit environ 116 millions par an, presque entièrement dépensés en France."),
  ("Il faut couper cette aide pour faire pression.", "Couper l'essentiel reviendrait à fermer nos universités à des étudiants algériens, pas à priver le gouvernement algérien d'argent."),
 ],
 questions=["Savais-tu que l'essentiel de cette « aide » est dépensé dans les universités françaises ?", "D'où vient le chiffre de « milliards » que tu as entendu ?"],
 limites=["Les données portent sur 2022-2024 ; la fiche de Focus 2030 n'a pas d'auteur individuel.", "Une partie de l'aide européenne et multilatérale à l'Algérie, à laquelle la France contribue, n'est pas comptée ici."],
 publics={'convaincus': "Le ministère lui-même donne les chiffres : 136 millions en 2023, pas des milliards, et c'est surtout le coût d'étudiants algériens dans nos facs. Ce qui part réellement en Algérie, c'est environ 5 millions par an. Le gouvernement algérien ne touche pas ce que les réseaux racontent.",
  'indecis': "L'aide au développement vers l'Algérie existe, mais elle est faible (environ 140 millions par an) et elle reste presque entièrement en France, dans les universités. Le chiffre de 800 millions est un total sur sept ans. C'est un bon exemple de chiffre vrai sorti de son contexte."},
 a_actualiser='2027-06-30',
))

# 5 ── Aide à l'Ukraine ───────────────────────────────────────────────────────
FICHES.append(fiche(
 id='aide-ukraine-montant', affirmation="La France envoie des centaines de milliards à l'Ukraine pendant que les Français se serrent la ceinture.", volet='international', sous_theme='Guerres et conflits',
 mots_cles=['ukraine', 'aide a l ukraine', 'milliards a l ukraine', 'centaines de milliards', 'zelensky argent', 'armes ukraine', 'aide militaire'],
 verdict='contredit', fiabilite='etabli',
 resume="Non : selon le ministre des Armées, l'aide militaire française à l'Ukraine a été d'environ 1,7 milliard d'euros en 2022, 2,1 milliards en 2023 et près de 3 milliards en 2024, dont une partie financée par les revenus des avoirs russes gelés. L'Institut de Kiel comptait environ 4,9 milliards d'aide française annoncée fin 2024, ce qui plaçait la France au 10e rang. Les « centaines de milliards » correspondent à l'aide de tous les Européens réunis, en bonne partie sous forme de prêts.",
 contexte="Le coût de l'aide à l'Ukraine est souvent opposé aux difficultés budgétaires et sociales des Français, notamment par le RN et LFI sous des angles différents.",
 explication="L'aide à l'Ukraine prend plusieurs formes : matériel militaire (souvent prélevé sur les stocks ou commandé à l'industrie française), aide humanitaire, prêts et fonds européens. Les montants varient selon ce que l'on compte.",
 sources=[PS_UKR_LECORNU, MINARM_AVOIRS, STATISTA_UKR, PS_UKR_KIEL, CE_UKR],
 faits=[
  fait("Selon le ministre des Armées, l'aide militaire française (matériel valorisé) a été de 1,7 milliard d'euros en 2022, 2,1 milliards en 2023 et près de 3 milliards en 2024.", 'ps_ukr_lecornu', '2022-2024', 'France', "Environ 7 milliards en trois ans : loin des centaines de milliards.", 'etabli', '1,7 / 2,1 / 3 Md€'),
  fait("Selon le ministère des Armées, 300 millions d'euros de l'aide 2024 viennent des revenus des avoirs russes immobilisés et sont dépensés auprès de l'industrie française.", 'minarm_avoirs', '2024', 'France', "Une partie de l'aide est payée par l'argent russe gelé et fait travailler des usines françaises.", 'etabli', '300 M€'),
  fait("Selon les données de l'Institut de Kiel reprises par Statista, la France avait annoncé 4,9 milliards d'euros d'aide de janvier 2022 à fin 2024, dont environ 3,5 milliards militaires, au 10e rang des donateurs.", 'statista_ukr', '2022-2024', 'Monde', "La France n'est pas le principal financeur.", 'estimation', '4,9 Md€'),
  fait("Selon l'Institut de Kiel cité par Public Sénat, l'ensemble des Européens avaient versé 132,3 milliards d'euros à fin 2024.", 'ps_ukr_kiel', '2022-2024', 'Europe', "Les « centaines de milliards » sont l'aide de tous les pays européens réunis.", 'estimation', '132,3 Md€'),
  fait("Selon la Commission européenne, l'UE a versé 43,3 milliards d'euros d'assistance macrofinancière sous forme de « prêts consentis à des conditions favorables », et un prêt de 90 milliards pour 2026-2027 est financé par l'emprunt de l'UE.", 'ce_ukr', '2022-2026', 'Union européenne', "Une grande part de l'aide européenne est prêtée, pas donnée.", 'etabli', '43,3 Md€'),
 ],
 court="Faux : l'aide militaire française a été d'environ 1,7, 2,1 puis près de 3 milliards d'euros par an de 2022 à 2024, en partie payée par les avoirs russes gelés. Les « centaines de milliards » correspondent à l'aide de toute l'Europe, souvent en prêts.",
 moyen="Le ministre des Armées a donné les chiffres : 1,7 milliard en 2022, 2,1 milliards en 2023, près de 3 milliards en 2024. Une partie vient des revenus des avoirs russes gelés et est dépensée dans nos usines d'armement.\n\nSelon l'Institut de Kiel, la France n'était que 10e donateur fin 2024. Les montants de plus de 100 milliards correspondent à l'ensemble des Européens, et une grande part prend la forme de prêts. On peut débattre de l'effort, mais pas avec un chiffre cent fois trop gros.",
 detaille="Devant le Sénat, le ministre des Armées a chiffré l'aide militaire française, valorisée, à 1,7 milliard d'euros en 2022, 2,1 milliards en 2023 et près de 3 milliards en 2024. En 2024, près de 300 millions venaient des revenus des avoirs russes immobilisés, dépensés auprès de l'industrie française (munitions, artillerie, défense aérienne).\n\nSelon les données de l'Institut de Kiel, la France avait annoncé environ 4,9 milliards d'euros d'aide de 2022 à fin 2024, dont 3,5 milliards militaires, au 10e rang des donateurs. L'ensemble des Européens avaient versé 132,3 milliards, les États-Unis environ 114 milliards. Au niveau de l'Union, une grande partie de l'aide prend la forme de prêts (43,3 milliards d'assistance macrofinancière, un prêt de 90 milliards pour 2026-2027).\n\nLa France contribue aussi via le budget européen, ce qui augmente son effort réel. Mais l'aide à l'Ukraine, de quelques milliards par an, n'explique pas à elle seule l'austérité : le débat sur les choix budgétaires doit porter sur l'ensemble des dépenses et des recettes, y compris les impôts des plus riches.",
 empathie="Je comprends qu'on ait du mal à accepter qu'on aide un autre pays quand on doit soi-même compter chaque euro. Mais les chiffres réels sont de quelques milliards par an, pas des centaines, et une partie est payée par l'argent russe gelé.",
 legitimes=["L'aide française augmente (près de 3 milliards en 2024) et s'ajoute à la contribution française au budget européen.", "Le débat sur le niveau et la forme de l'aide, et sur la recherche de la paix, est légitime."],
 contre=[
  ("Avec cet argent on pourrait sauver l'hôpital.", "Les montants sont réels mais de quelques milliards par an, en partie payés par les avoirs russes ; les vrais arbitrages budgétaires sont ailleurs."),
  ("On vide nos stocks d'armes.", "Une partie de l'aide finance des commandes à l'industrie française, et le ministre affirme ne rien déprogrammer de la loi de programmation militaire."),
 ],
 questions=["Sais-tu à quel rang des donateurs se trouve la France ?", "D'où vient le chiffre de « centaines de milliards » : la France seule ou toute l'Europe ?"],
 limites=["Les données de l'Institut de Kiel n'ont pas pu être lues sur son site : elles viennent d'une infographie Statista et de Public Sénat ; les chiffres français pour 2025-2026 ne sont pas disponibles dans les sources lues.", "La part française des aides européennes n'a pas été chiffrée."],
 publics={'convaincus': "Le ministre des Armées l'a dit au Sénat : environ 7 milliards d'aide militaire en trois ans, pas des centaines. Une partie est payée avec l'argent russe gelé et fait tourner des usines françaises. Les grosses sommes que tu vois, c'est toute l'Europe réunie, et souvent des prêts.",
  'indecis': "La France aide l'Ukraine à hauteur de quelques milliards par an, et elle n'est que 10e donateur. Ce n'est pas rien, et on peut en débattre, mais ce n'est pas ce qui explique l'austérité. Les vrais choix budgétaires se jouent sur les impôts et les aides aux entreprises."},
 a_actualiser='2027-03-31',
))

# 6 ── Ukraine « nazie » ──────────────────────────────────────────────────────
FICHES.append(fiche(
 id='ukraine-gouvernement-nazis', affirmation="Le gouvernement ukrainien est dirigé par des nazis.", volet='international', sous_theme='Russie',
 mots_cles=['ukraine nazie', 'nazis ukrainiens', 'denazification', 'denazifier', 'azov', 'zelensky nazi', 'neonazis ukraine', 'gouvernement ukrainien nazi'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux : aux législatives ukrainiennes de 2019, l'extrême droite unie n'a obtenu que 2,15 % des voix et un seul siège. Le président Volodymyr Zelensky, juif, a été élu avec 73 % des voix, et l'Ukraine a interdit les idéologies nazie et communiste en 2015. Le bataillon Azov a bien été fondé par des néonazis en 2014, mais les historiens jugent l'influence de l'extrême droite sur l'État ukrainien « inexistante ». Le thème de la « dénazification » est un récit de propagande du Kremlin.",
 contexte="La Russie a justifié l'invasion de février 2022 par la « dénazification » de l'Ukraine ; ce récit circule aussi en France, à l'extrême droite comme dans une partie de la gauche radicale.",
 explication="L'Ukraine a, comme beaucoup de pays européens, des groupes d'extrême droite. La question est de savoir s'ils dirigent le pays : les résultats électoraux et la composition du pouvoir montrent que non.",
 sources=[FC_UKR, ADL_UKR, EUVSD_UKR],
 faits=[
  fait("Selon FactCheck.org et EUvsDisinfo, le front uni des partis d'extrême droite a obtenu 2,15 % des voix aux législatives ukrainiennes de 2019, sous le seuil de 5 %, et un seul siège.", 'fc_ukr', '2019', 'Ukraine', "L'extrême droite pèse beaucoup moins en Ukraine qu'en France.", 'etabli', '2,15 %'),
  fait("Selon FactCheck.org, Volodymyr Zelensky, qui est juif, a été élu président en 2019 avec 73 % des voix.", 'fc_ukr', '2019', 'Ukraine', "Un « régime nazi » dirigé par un président juif élu massivement est une contradiction.", 'etabli', '73 %'),
  fait("Selon EUvsDisinfo, l'Ukraine a interdit les idéologies nazie et communiste en 2015.", 'euvsd_ukr', '2015', 'Ukraine', "La loi ukrainienne condamne le nazisme.", 'etabli'),
  fait("Selon FactCheck.org, le bataillon Azov a été fondé par des membres de groupes néonazis et intégré à la Garde nationale fin 2014 ; pour un chercheur de l'université Johns Hopkins, l'influence politique de ces groupes au niveau de l'État est « inexistante ».", 'fc_ukr', '2014-2022', 'Ukraine', "Le problème d'Azov est réel, mais il ne fait pas un gouvernement nazi.", 'etabli'),
  fait("Selon l'historien David Fishman cité par l'ADL, l'Ukraine est « une démocratie imparfaite, mais incontestablement une démocratie, et en aucun cas un régime nazi », et la propagande russe vise à délégitimer l'Ukraine auprès des Russes.", 'adl_ukr', '2022', 'Ukraine', "Le récit sert un objectif de guerre.", 'interpretation'),
 ],
 court="Faux : l'extrême droite ukrainienne a obtenu 2,15 % des voix en 2019, le président Zelensky, juif, a été élu avec 73 %, et le nazisme est interdit en Ukraine depuis 2015. La « dénazification » est un prétexte de propagande du Kremlin.",
 moyen="Aux législatives de 2019, l'extrême droite ukrainienne unie a fait 2,15 % et obtenu un seul siège. Le président, Volodymyr Zelensky, est juif et a été élu avec 73 % des voix. L'Ukraine a même interdit l'idéologie nazie en 2015.\n\nIl existe des groupes néonazis en Ukraine, et le bataillon Azov en est issu : il ne faut pas le nier. Mais les historiens jugent leur influence sur l'État « inexistante ». La « dénazification » est un prétexte inventé par le Kremlin pour justifier une invasion.",
 detaille="La Russie a justifié l'invasion de février 2022 par la volonté de « dénazifier » l'Ukraine. Les faits contredisent ce récit. Aux législatives de 2019, le front uni des partis de droite radicale a obtenu 2,15 % des voix, loin du seuil de 5 %, et le parti Svoboda un seul siège. Volodymyr Zelensky, issu d'une famille juive, a été élu la même année avec 73 % des voix. L'Ukraine a interdit les idéologies nazie et communiste en 2015.\n\nLe bataillon Azov a bien été fondé en 2014 par des membres de groupes néonazis, avant d'être intégré à la Garde nationale ; des soldats arborent parfois des symboles nazis, ce qui est inacceptable. Mais des spécialistes comme Eugene Finkel ou Jared McBride jugent ces groupes marginaux et leur influence politique au niveau de l'État inexistante.\n\nEUvsDisinfo classe ce récit parmi les narratifs récurrents de la désinformation pro-Kremlin. Pour un antifasciste, combattre l'extrême droite partout, y compris en Ukraine, ne signifie pas reprendre la propagande d'un pouvoir qui envahit son voisin.",
 empathie="Je comprends qu'on ait vu passer des images de soldats avec des symboles nazis : elles existent et elles choquent. Mais un pays où l'extrême droite fait 2 % et dont le président est juif n'est pas dirigé par des nazis.",
 legitimes=["Le bataillon Azov a été fondé par des néonazis, et des symboles nazis apparaissent chez certains soldats.", "L'Ukraine est décrite comme une « démocratie imparfaite » : la critiquer n'est pas interdit."],
 contre=[
  ("Azov, ce sont des nazis.", "Il a été fondé par des néonazis ; mais il ne gouverne pas le pays, où l'extrême droite a fait 2,15 % aux élections."),
  ("Les médias occidentaux cachent la vérité.", "Les résultats électoraux de 2019 sont publics, et la loi ukrainienne de 2015 interdit l'idéologie nazie."),
 ],
 questions=["Combien de voix l'extrême droite a-t-elle obtenues en Ukraine en 2019, comparé à la France ?", "Comment un régime nazi aurait-il élu un président juif avec 73 % des voix ?"],
 limites=["Les sources lues sont américaines ou européennes ; aucun fact-check français n'a été ouvert.", "Les données électorales datent de 2019 ; il n'y a pas eu d'élection nationale depuis, en raison de la loi martiale."],
 publics={'convaincus': "En 2019, l'extrême droite ukrainienne a fait 2,15 %, et un seul député. Le président est juif et a été élu avec 73 %. Si tu détestes les nazis, et tu as raison, alors regarde qui utilise ce mot pour justifier l'invasion d'un pays voisin.",
  'indecis': "Il existe des néonazis en Ukraine, comme dans beaucoup de pays, et le bataillon Azov en est issu. Mais ils pèsent très peu politiquement, et le nazisme y est interdit depuis 2015. La « dénazification » est un argument de guerre de la Russie, pas une description de la réalité."},
 a_actualiser='2027-12-31',
))

# 7 ── Ultragauche / ultradroite ──────────────────────────────────────────────
FICHES.append(fiche(
 id='ultragauche-ultradroite-violence', affirmation="Les antifas sont plus violents et plus dangereux que l'ultradroite.", volet='politique', sous_theme='Droite et extrême droite',
 mots_cles=['antifas', 'antifa', 'ultragauche', 'ultra gauche', 'ultradroite', 'ultra droite', 'black bloc', 'black blocs', 'extreme gauche violente', 'groupuscules'],
 verdict='contredit', fiabilite='etabli',
 resume="Les données disponibles disent l'inverse pour les violences les plus graves : depuis 2017, le ministère de l'Intérieur compte 12 projets d'attentat d'ultradroite déjoués (jusqu'en 2023), contre 1 pour l'ultragauche selon le ministre en 2023 ; des chercheurs attribuent depuis 1986 55 morts à l'ultradroite et 7 à l'ultragauche, et 70 % des agressions militantes à l'ultradroite. L'ultragauche est en revanche très présente dans les violences en manifestation, et la mort d'un militant nationaliste à Lyon en 2026 a mis en cause des militants antifascistes.",
 contexte="Après les violences de manifestations (retraites, Sainte-Soline) puis l'affaire de Lyon en 2026, une partie de la droite et de l'extrême droite présente « les antifas » comme la principale menace.",
 explication="Il faut distinguer les dégradations et affrontements en manifestation, où l'ultragauche est très présente, des projets d'attentat et des agressions contre des personnes, où l'ultradroite domine selon les données disponibles. L'État ne publie pas de statistique complète par idéologie.",
 sources=[AN_QE10244, PS_ULTRA23, AN_TACHE, PS_VIORAMIL, AN_CE_MANIF, PS_LYON26],
 faits=[
  fait("Selon le ministère de l'Intérieur, 12 projets d'action terroriste liés à l'ultradroite ont été déjoués depuis 2017, dont 2 en 2023 ; la DGSI estime l'ultradroite agissante à près de 2 000 personnes.", 'an_qe10244', '2017-2023', 'France', "Les projets d'attentat viennent surtout de l'ultradroite.", 'etabli', '12'),
  fait("Selon Public Sénat, le ministre de l'Intérieur citait en 2023 9 attentats d'ultradroite déjoués depuis 2017 et 1 d'ultragauche, et le directeur de la DGSI qualifiait la menace d'ultradroite de « principale menace » pour les démocraties occidentales.", 'ps_ultra23', '2017-2023', 'France', "Même un ministre très critique de l'ultragauche reconnaît ce déséquilibre.", 'etabli', '9 contre 1'),
  fait("Selon des chercheurs cités dans un document de l'Assemblée nationale, depuis 1986, l'ultragauche serait responsable de 7 morts et l'ultradroite de 55 ; en 2021, la France représentait 45 % des arrestations de l'UE pour terrorisme d'extrême droite (Europol).", 'an_tache', '1986-2021', 'France et UE', "Sur les violences mortelles, l'écart est massif.", 'estimation', '55 contre 7'),
  fait("Selon l'étude universitaire Vioramil citée par Public Sénat, 70 % des agressions militantes contre des personnes sont le fait de groupes d'ultradroite.", 'ps_vioramil', '1986-2023', 'France', "L'ultradroite s'attaque davantage aux personnes.", 'estimation', '70 %'),
  fait("Selon la commission d'enquête de l'Assemblée, 1 518 policiers et gendarmes ont été blessés lors des manifestations du printemps 2023, avec des groupes violents de 15 à 200 personnes ; le rapporteur estime que ces violences n'étaient pas « planifiées et orchestrées » par des organisations centralisées.", 'an_ce_manif', '2023', 'France', "Les violences en manifestation sont réelles et graves.", 'etabli', '1 518'),
  fait("Selon Public Sénat et l'AFP, un militant nationaliste est mort à Lyon en février 2026 après une bagarre entre groupuscules fasciste et antifasciste ; le parquet a requis sept mises en examen pour homicide volontaire.", 'ps_lyon26', '2026', 'France', "La violence peut aussi venir de militants antifascistes ; l'enquête était en cours.", 'etabli'),
 ],
 court="Faux pour les violences les plus graves : depuis 2017, 12 projets d'attentat d'ultradroite ont été déjoués (contre 1 d'ultragauche selon le ministre), et des chercheurs comptent 55 morts dus à l'ultradroite depuis 1986 contre 7 pour l'ultragauche. L'ultragauche est en revanche très présente dans les violences de manifestation.",
 moyen="Les chiffres officiels vont dans l'autre sens. Le ministère de l'Intérieur compte 12 projets d'attentat d'ultradroite déjoués depuis 2017 ; le ministre en citait 1 pour l'ultragauche. Des chercheurs attribuent 55 morts à l'ultradroite depuis 1986, contre 7 à l'ultragauche, et 70 % des agressions militantes à l'ultradroite.\n\nCela ne veut pas dire que l'ultragauche est pacifique : elle est très présente dans les violences en manifestation, et la mort d'un militant nationaliste à Lyon en 2026 a mis en cause des antifascistes. Toute violence politique doit être condamnée. Mais dire que la menace principale vient des « antifas » est contraire à ce que dit la DGSI.",
 detaille="L'État ne publie pas de statistique complète des violences selon l'idéologie de leurs auteurs. Les données disponibles convergent pourtant. Le ministère de l'Intérieur indique avoir déjoué 12 projets d'action terroriste liés à l'ultradroite depuis 2017 ; en 2023, le ministre en citait 9 contre 1 pour l'ultragauche. Le directeur de la DGSI qualifiait l'ultradroite de « principale menace » parmi les mouvances radicales. Selon Europol, la France représentait 45 % des arrestations de l'UE pour terrorisme d'extrême droite en 2021.\n\nSur le long terme, des chercheurs (Sommier, Crettiez, Audigier) attribuent depuis 1986 55 morts à l'ultradroite et 7 à l'ultragauche ; l'étude Vioramil attribue à l'ultradroite 70 % des agressions militantes contre des personnes.\n\nL'ultragauche est, elle, très présente dans les affrontements et dégradations en manifestation : 1 518 policiers et gendarmes ont été blessés au printemps 2023. En février 2026, la mort d'un militant nationaliste à Lyon, après une rixe entre groupuscules, a conduit le parquet à requérir des mises en examen pour homicide volontaire visant des militants antifascistes. La gauche doit condamner cette violence sans ambiguïté ; elle peut en même temps rappeler où se trouve, selon les services de renseignement, la menace la plus meurtrière.",
 empathie="Je comprends que les images de black blocs ou le drame de Lyon fassent peur, et ces violences doivent être condamnées. Mais pour les attentats et les agressions contre des personnes, les services de renseignement disent que la menace principale vient de l'ultradroite.",
 legitimes=["L'ultragauche est très présente dans les violences en manifestation, avec de nombreux policiers blessés.", "La mort d'un militant nationaliste à Lyon en 2026 met en cause des militants antifascistes ; aucune violence politique n'est acceptable."],
 contre=[
  ("On n'entend parler que des violences d'extrême droite pour cacher celles de l'extrême gauche.", "Les chiffres cités viennent du ministère de l'Intérieur, de la DGSI, d'Europol et de chercheurs, pas de militants de gauche."),
  ("Les black blocs cassent tout à chaque manifestation.", "C'est un problème réel ; mais casser des vitrines et préparer des attentats ne sont pas le même niveau de danger."),
 ],
 questions=["Sais-tu combien de projets d'attentat d'ultradroite ont été déjoués depuis 2017 ?", "Qui, selon la DGSI, représente la principale menace parmi les mouvances radicales ?"],
 limites=["L'État ne suit pas les infractions selon la motivation idéologique : les comparaisons reposent sur des déclarations ministérielles et des travaux de chercheurs.", "Les sections du rapport d'enquête de 2023 consacrées à l'ultradroite n'ont pas pu être lues ; l'enquête sur la mort survenue à Lyon était en cours à la date de la source."],
 publics={'convaincus': "Ce n'est pas la gauche qui le dit : c'est le ministère de l'Intérieur, avec 12 projets d'attentat d'ultradroite déjoués depuis 2017, et la DGSI qui parle de « principale menace ». Des chercheurs comptent 55 morts dus à l'ultradroite depuis 1986, contre 7 pour l'ultragauche. Condamner les violences d'où qu'elles viennent, oui ; inverser les chiffres, non.",
  'indecis': "Les deux extrêmes ont leurs violents, et la mort d'un militant à Lyon en 2026 le rappelle. Mais ils ne sont pas dangereux de la même façon : l'ultragauche est surtout présente dans les affrontements de manifestation, l'ultradroite dans les projets d'attentat et les agressions contre des personnes, selon les services de l'État."},
 a_actualiser='2027-06-30',
))

# 8 ── Actes antichrétiens ────────────────────────────────────────────────────
FICHES.append(fiche(
 id='actes-antichretiens-eglises', affirmation="Il y a des actes antichrétiens tous les jours et on brûle nos églises dans l'indifférence.", volet='droits', sous_theme='Laïcité',
 mots_cles=['antichretien', 'antichretiens', 'anti chretiens', 'eglises brulees', 'eglises incendiees', 'on brule nos eglises', 'profanation', 'profanations', 'christianophobie', 'eglises vandalisees'],
 verdict='trompeur', fiabilite='etabli',
 resume="En partie : le ministère de l'Intérieur a recensé 843 faits antichrétiens en 2025 (+9 %), soit un peu plus de deux par jour en moyenne. Mais 87 % sont des atteintes aux biens, surtout des vols (43 %) et des dégradations (30 %) ; les incendies représentent 45 faits (5 %). Le motif antichrétien est souvent difficile à établir, et les listes virales d'« églises brûlées » mélangent accidents et cas sans lien. Les faits antisémites (1 320) restent plus nombreux, et les faits antimusulmans ont fortement augmenté (+88 %).",
 contexte="Des listes d'églises incendiées circulent régulièrement sur les réseaux sociaux pour dénoncer une « christianophobie » ignorée par les médias et les pouvoirs publics.",
 explication="Les « actes antichrétiens » recensés par le renseignement territorial incluent des vols dans les églises, des tags, des dégradations et des atteintes aux personnes. Tous ne visent pas la foi chrétienne : beaucoup sont des vols ou du vandalisme.",
 sources=[MININT_ANTIREL, AN_QE10636, LM_EGLISES, LP_EGLISES],
 faits=[
  fait("Selon le ministère de l'Intérieur, 843 faits antichrétiens ont été recensés en 2025 (+9 %), dont 734 atteintes aux biens (87 %) et 109 atteintes aux personnes (+70 %), dont un homicide.", 'minint_antirel', '2025', 'France', "Le phénomène existe et augmente ; il faut le dire.", 'etabli', '843'),
  fait("Selon le ministère, parmi les atteintes aux biens, on compte 362 vols ou tentatives (43 %), 254 dégradations (30 %), 81 inscriptions (10 %) et 45 incendies (5 %).", 'minint_antirel', '2025', 'France', "L'image d'églises brûlées en série ne correspond pas aux chiffres.", 'etabli', '45 incendies'),
  fait("Selon le ministère, 1 320 faits antisémites (-16 %) et 326 faits antimusulmans (+88 %) ont été recensés en 2025.", 'minint_antirel', '2025', 'France', "Toutes les religions sont visées ; les Juifs, très minoritaires, restent les plus touchés.", 'etabli', '1 320'),
  fait("Selon Le Monde, la Commission nationale consultative des droits de l'homme juge « extrêmement délicat » de distinguer les actes à motivation réellement antireligieuse des vols ou du vandalisme.", 'lm_eglises', '2019', 'France', "Une partie des faits n'a pas de motif religieux.", 'etabli'),
  fait("Selon Le Parisien, sur une liste virale de 11 incendies d'églises, deux étaient accidentels, deux commis par des adolescents et un au Canada ; seuls deux cas se rapprochaient d'actes antichrétiens.", 'lp_eglises', '2020', 'France', "Les listes qui circulent gonflent le phénomène.", 'etabli'),
 ],
 court="Trompeur : 843 faits antichrétiens ont été recensés en 2025, mais 87 % sont des atteintes aux biens, surtout des vols, et les incendies sont 45 (5 %). Le ministère publie ces chiffres chaque année : ce n'est pas de l'indifférence.",
 moyen="Il y a bien des actes antichrétiens : 843 en 2025, en hausse de 9 %, avec des agressions en forte hausse et même un homicide. Il faut le prendre au sérieux.\n\nMais l'image d'églises brûlées en masse est fausse : 43 % de ces faits sont des vols, 30 % des dégradations, et 5 % des incendies. Les listes virales mélangent souvent accidents et faits sans lien. Et le ministère publie ces chiffres chaque année, avec ceux des actes antisémites (1 320) et antimusulmans (326, en hausse de 88 %) : toutes les croyances méritent la même protection.",
 detaille="Le ministère de l'Intérieur a recensé 843 faits antichrétiens en 2025, en hausse de 9 %, soit environ 34 % des faits antireligieux ; 817 visaient des catholiques. Les atteintes aux biens dominent (734 faits, dont 627 visant des lieux de culte) : vols ou tentatives (43 %), dégradations (30 %), inscriptions (10 %) et incendies (45 faits, 5 %). Les atteintes aux personnes ont fortement augmenté (109 faits, +70 %), dont un homicide.\n\nLe motif est souvent difficile à établir : la CNCDH juge délicat de distinguer une motivation antireligieuse d'un vol ou de vandalisme. Les listes d'églises incendiées qui circulent mêlent incendies accidentels, actes d'adolescents et faits survenus à l'étranger. Le phénomène existe, mais il est moins spectaculaire que ce que montrent les réseaux.\n\nLa même année, le ministère a recensé 1 320 faits antisémites et 326 faits antimusulmans (+88 %). Défendre la liberté de culte, c'est protéger les églises comme les synagogues et les mosquées, sans hiérarchiser les victimes.",
 empathie="Je comprends que voir une église dégradée ou incendiée blesse, surtout quand on y est attaché. Ces actes existent et augmentent. Mais ils sont surtout des vols et des dégradations, et l'État les compte et les publie.",
 legitimes=["Les faits antichrétiens augmentent (+9 % en 2025), et les atteintes aux personnes ont bondi de 70 %, avec un homicide.", "Des incendies criminels d'églises existent bel et bien."],
 contre=[
  ("Les médias n'en parlent jamais.", "Le ministère publie un bilan national détaillé chaque année et répond aux questions des députés sur ce sujet."),
  ("On protège les autres religions mais pas la nôtre.", "Le même bilan recense les trois types d'actes ; l'objectif doit être de protéger tous les lieux de culte."),
 ],
 questions=["Sais-tu quelle part des actes antichrétiens sont des vols ?", "Combien d'incendies d'églises ont été recensés en 2025, selon le ministère ?"],
 limites=["Les articles de vérification sur les listes virales datent de 2019-2020 ; ils ont été lus dans des copies PDF hébergées par l'Observatoire du patrimoine religieux.", "La ventilation exacte des faits antimusulmans est incohérente dans le document du ministère ; la fiche ne retient que le total."],
 publics={'convaincus': "Les chiffres du ministère sont publics : 843 faits antichrétiens en 2025, et ce n'est pas rien. Mais 43 % sont des vols, 30 % des dégradations, et seulement 5 % des incendies. Les listes qui tournent sur les réseaux mélangent des accidents et des faits à l'étranger : elles desservent la cause qu'elles prétendent défendre.",
  'indecis': "Les actes contre les églises existent et augmentent, notamment les agressions. Mais ce sont surtout des vols et des dégradations, pas une vague d'incendies. L'État les compte, comme les actes antisémites et antimusulmans : toutes les croyances méritent la même protection."},
 a_actualiser='2027-04-30',
))

# 9 ── Éducation à la sexualité ───────────────────────────────────────────────
FICHES.append(fiche(
 id='education-sexualite-genre', affirmation="L'éducation à la sexualité à l'école apprend la théorie du genre aux enfants.", volet='services', sous_theme='École publique',
 mots_cles=['theorie du genre', 'education sexuelle', 'education a la sexualite', 'evars', 'education a la vie affective', 'programme d education sexuelle', 'genre a l ecole', 'ideologie du genre'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur : le programme d'éducation à la vie affective et relationnelle, et à la sexualité (EVARS), publié en février 2025, ne contient pas l'expression « théorie du genre ». À l'école primaire, il ne parle pas de sexualité mais du corps, des émotions, de l'intimité et du consentement, et le mot « genre » n'y sert qu'à repérer les stéréotypes. La distinction entre sexe, genre et orientation sexuelle est abordée en 5e, l'identité de genre au lycée, sous l'angle de la lutte contre les discriminations.",
 contexte="Le programme a fait l'objet d'une forte controverse en 2024-2025, un ministre délégué ayant déclaré vouloir empêcher l'entrée de la « théorie du genre » à l'école. Il a été adopté par le Conseil supérieur de l'éducation (60 voix contre 0).",
 explication="L'obligation d'au moins trois séances par an existe depuis une loi de 2001, mais elle était peu appliquée. Le programme de 2025 fixe un contenu progressif, adapté à l'âge, de la maternelle au lycée.",
 sources=[BO_EVARS, ETUDIANT_EVARS, PS_EVARS, AN_QE4168],
 faits=[
  fait("Selon le Bulletin officiel, le programme prévoit au moins trois séances par an, avec des contenus « progressifs et adaptés à l'âge et à la maturité des élèves » ; à l'école primaire, il s'agit d'une éducation à la vie affective et relationnelle (corps, émotions, intimité, consentement).", 'bo_evars', '2025', 'France', "La sexualité n'est pas abordée avec les jeunes enfants.", 'etabli', '3 séances'),
  fait("Selon le Bulletin officiel, au primaire, le mot « genre » apparaît pour « repérer des discriminations issues de stéréotypes, notamment de genre » ; l'expression « théorie du genre » n'apparaît pas dans le programme.", 'bo_evars', '2025', 'France', "Il s'agit de lutter contre les clichés, pas d'enseigner une théorie.", 'etabli'),
  fait("Selon L'Étudiant, la distinction entre sexe, genre et orientation sexuelle est abordée en 5e, l'identité de genre en seconde ; dans les versions antérieures, elle figurait au collège et le ministère l'a déplacée au lycée.", 'etudiant_evars', '2025', 'France', "Le genre est bien abordé, mais avec des adolescents.", 'etabli'),
  fait("Selon Public Sénat, la ministre de l'Éducation nationale a déclaré en 2024 que « ce programme n'a pas d'idéologie » et que « la théorie du genre n'existe pas ».", 'ps_evars', '2024', 'France', "Une ministre d'un gouvernement de droite récuse l'accusation.", 'etabli'),
  fait("Selon L'Étudiant, citant le CESE, moins de 15 % des élèves bénéficient réellement des trois séances annuelles prévues par la loi.", 'etudiant_evars', '2025', 'France', "Le vrai problème est plutôt l'absence de séances.", 'estimation', '15 %'),
 ],
 court="Trompeur : l'expression « théorie du genre » ne figure pas dans le programme ; au primaire, on parle du corps, des émotions et du consentement, et le genre n'y apparaît que pour repérer les stéréotypes. L'identité de genre est abordée au lycée, pour lutter contre les discriminations.",
 moyen="Le programme publié en février 2025 ne contient pas l'expression « théorie du genre ». À l'école primaire, il n'y a pas de cours de sexualité : on parle du corps, des émotions, de l'intimité et du consentement, pour apprendre aux enfants à dire non et à signaler une violence.\n\nLe genre est abordé, mais progressivement : les stéréotypes au primaire, la différence entre sexe, genre et orientation sexuelle en 5e, l'identité de genre au lycée. Même la ministre d'un gouvernement de droite a déclaré que « la théorie du genre n'existe pas ». Et moins de 15 % des élèves ont réellement les trois séances prévues par la loi depuis 2001.",
 detaille="La loi de 2001 prévoit au moins trois séances annuelles d'éducation à la sexualité, mais selon le CESE moins de 15 % des élèves en bénéficient. Le programme publié au Bulletin officiel du 6 février 2025, appliqué depuis la rentrée 2025, fixe pour la première fois un contenu détaillé, « progressif et adapté à l'âge ».\n\nÀ l'école primaire, il s'agit d'une « éducation à la vie affective et relationnelle » : connaître son corps, ses émotions, l'intimité, le consentement, puis la puberté en CM1-CM2. Le mot « genre » y apparaît pour repérer les discriminations issues de stéréotypes. Au collège, les élèves apprennent en 5e à distinguer sexe, genre et orientation sexuelle ; l'identité de genre est abordée en seconde. Après la controverse, ses mentions ont été réduites et déplacées au lycée ; selon le ministère, la notion sert à lutter contre les discriminations prévues par le code pénal.\n\nL'expression « théorie du genre » ne figure pas dans le texte, et la ministre a déclaré qu'elle « n'existe pas ». Apprendre aux enfants que leur corps leur appartient protège contre les violences sexuelles ; c'est l'un des premiers objectifs du programme.",
 empathie="Je comprends qu'un parent veuille savoir ce qu'on dit à son enfant sur un sujet aussi intime. C'est légitime de demander. Mais le programme est public : au primaire, il parle du corps, des émotions et du consentement, pas de sexualité.",
 legitimes=["Les parents ont le droit d'être informés : le ministère prévoit qu'ils soient informés des objectifs annuels.", "La notion d'identité de genre est bien présente au lycée, et la première version du texte la mentionnait davantage."],
 contre=[
  ("On va apprendre aux enfants qu'ils peuvent changer de sexe.", "Au primaire, le programme ne traite que des stéréotypes ; l'identité de genre n'est abordée qu'en seconde, sous l'angle des discriminations."),
  ("Ce n'est pas le rôle de l'école.", "La loi l'impose depuis 2001, et apprendre le consentement aide les enfants à repérer et signaler les violences."),
 ],
 questions=["As-tu lu ce que le programme prévoit pour l'école primaire ?", "Savais-tu que la loi impose ces séances depuis 2001, mais que moins de 15 % des élèves les ont vraiment ?"],
 limites=["La partie collège-lycée du programme n'a été vérifiée qu'à travers L'Étudiant et la réponse du ministère, le texte extrait du Bulletin officiel s'arrêtant au CM2.", "Le contenu réel des séances dépend des enseignants et des intervenants ; les sources lues ne l'évaluent pas."],
 publics={'convaincus': "Le programme est public, tu peux le lire : l'expression « théorie du genre » n'y figure pas. Au primaire, on parle du corps, des émotions et du consentement, pour que les enfants sachent dire non. Même la ministre d'un gouvernement de droite a dit que cette théorie « n'existe pas ».",
  'indecis': "C'est normal de vouloir savoir ce qu'on enseigne à ses enfants. Le programme est progressif : les émotions et le consentement en primaire, la différence entre sexe et genre en 5e, l'identité de genre au lycée. Son premier objectif est de protéger les enfants contre les violences."},
 a_actualiser='2027-06-30',
))

# 10 ── Taxe Zucman ───────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='taxe-zucman-exil', affirmation="La taxe Zucman ferait fuir les riches et tuerait les start-up.", volet='economie', sous_theme='Fiscalité',
 mots_cles=['taxe zucman', 'zucman', 'impot plancher', 'impot minimum', 'ultra riches', 'ultrariches', '2 %', 'exil fiscal', 'start up', 'startups', 'fuir les riches'],
 verdict='trompeur', fiabilite='debat',
 resume="La taxe Zucman, un impôt plancher de 2 % sur les patrimoines de plus de 100 millions d'euros, concernerait environ 1 800 foyers (0,01 %). Le Conseil d'analyse économique mesure un exil fiscal réel mais limité après la hausse d'impôts de 2013 (au plus 350 foyers par an sur 385 000 du top 1 %), avec un effet macroéconomique d'environ 0,03 %. Le vrai point dur concerne les fondateurs de start-up très valorisées sans revenus : un problème de liquidités, auquel Gabriel Zucman répond par un paiement possible en actions. Aucune source ne démontre qu'elle « tuerait » les start-up.",
 contexte="Adoptée à l'Assemblée en février 2025, la proposition a été rejetée au Sénat en juin 2025, puis à l'Assemblée lors du budget 2026 en octobre 2025, la gauche votant pour et le centre, LR et le RN contre.",
 explication="L'impôt plancher ne s'ajoute pas forcément : il oblige les très grandes fortunes à payer au total au moins 2 % de leur patrimoine par an en impôts, en tenant compte de ce qu'elles paient déjà. La base inclut les actions de leurs entreprises.",
 sources=[CAE_EXIL, PS_ZUCMAN_ARG, SENAT_ZUCMAN, LCP_ZUCMAN, LCP_ZUCMAN_REJET],
 faits=[
  fait("Selon Public Sénat, la taxe Zucman vise les patrimoines de plus de 100 millions d'euros, soit environ 0,01 % des foyers (environ 1 800 personnes selon la ministre des Comptes publics), pour un rendement avancé par Gabriel Zucman de 20 milliards d'euros par an, à plus ou moins 5 milliards.", 'ps_zucman_arg', '2025', 'France', "Seule une poignée de très grandes fortunes est concernée.", 'estimation', '1 800 foyers'),
  fait("Selon le Conseil d'analyse économique, la hausse d'impôt de 2013 a provoqué au plus 350 départs supplémentaires par an sur environ 385 000 foyers du top 1 %, et une hausse de 4 milliards de la fiscalité du top 1 % ne réduirait le chiffre d'affaires et la masse salariale nationaux que d'environ 0,03 %.", 'cae_exil', '2013-2025', 'France', "L'exil existe, mais son effet économique est minime.", 'estimation', '0,03 %'),
  fait("Selon le CAE, quand un actionnaire important s'expatrie, son entreprise perd en moyenne 15 % de chiffre d'affaires, et la fiscalité du patrimoine a « un impact significatif sur l'exil fiscal des plus hauts patrimoines ».", 'cae_exil', '2025', 'France', "C'est l'argument sérieux des opposants : il faut le reconnaître.", 'estimation', '15 %'),
  fait("Selon le rapporteur LR du Sénat, la base inclut les biens professionnels, et une jeune pousse très valorisée sans revenus pourrait obliger ses actionnaires à vendre des titres ; dans son hypothèse, le rendement tomberait à 2 à 3 milliards d'euros.", 'senat_zucman', '2025', 'France', "Le problème des start-up est un problème de liquidités, et le rendement est contesté.", 'interpretation', '2 à 3 Md€'),
  fait("Selon LCP, Gabriel Zucman propose de payer en actions en cas de manque de liquidités et estime que « exonérer les biens professionnels voudrait simplement dire exonérer les milliardaires ».", 'lcp_zucman', '2025', 'France', "Une réponse existe au problème des fondateurs de start-up.", 'etabli'),
  fait("Selon LCP, les amendements Zucman ont été rejetés à l'Assemblée le 31 octobre 2025 par 228 voix contre 172 ; le RN a voté contre, comme le centre et LR.", 'lcp_zucman_rejet', '2025', 'France', "Le RN, qui se dit du côté du peuple, a refusé de taxer les milliardaires.", 'etabli', '228 contre 172'),
 ],
 court="Trompeur : la taxe ne vise qu'environ 1 800 foyers, et le Conseil d'analyse économique mesure un exil fiscal limité, à l'effet économique d'environ 0,03 %. Le problème des fondateurs de start-up est réel mais c'est un problème de liquidités, qu'un paiement en actions peut résoudre.",
 moyen="La taxe Zucman ne concerne que les patrimoines au-dessus de 100 millions d'euros : environ 1 800 foyers. Elle leur demande de payer au moins 2 % de leur fortune par an, tous impôts compris.\n\nL'exil fiscal existe, mais il est limité : selon le Conseil d'analyse économique, au plus 350 départs supplémentaires par an après la hausse d'impôts de 2013, avec un effet économique d'environ 0,03 %. Pour les fondateurs de start-up très valorisées mais sans revenus, il y a un vrai problème de trésorerie ; Gabriel Zucman propose qu'ils puissent payer en actions. Aucune étude ne montre que la taxe « tuerait » les start-up.",
 detaille="La proposition, inspirée des travaux de l'économiste Gabriel Zucman, instaure un impôt plancher de 2 % sur les patrimoines de plus de 100 millions d'euros : les très riches devraient payer au moins 2 % de leur fortune par an, en tenant compte des impôts déjà payés. Environ 1 800 foyers seraient concernés. Le rendement est débattu : 20 milliards d'euros par an selon Gabriel Zucman, 2 à 3 milliards dans l'hypothèse défavorable du rapporteur LR du Sénat.\n\nSur l'exil, le Conseil d'analyse économique, organisme public, a étudié la hausse d'impôts de 2013 : elle a provoqué au plus 350 départs supplémentaires par an parmi les 385 000 foyers du top 1 %. Quand un gros actionnaire part, son entreprise perd en moyenne 15 % de chiffre d'affaires ; mais à l'échelle du pays, une hausse de 4 milliards de la fiscalité du top 1 % ne réduirait l'activité que d'environ 0,03 %. Gabriel Zucman propose aussi de taxer au moment du départ.\n\nLe vrai point dur concerne les jeunes pousses très valorisées sans revenus, dont les fondateurs devraient vendre des titres : le paiement en actions ou un report peuvent y répondre. Le texte a été rejeté au Sénat puis à l'Assemblée, avec les voix du RN. La question de fond demeure : faut-il que les plus grandes fortunes paient au moins 2 % de leur patrimoine par an, tous impôts compris ?",
 empathie="Je comprends qu'on ait peur de voir partir des entrepreneurs et des emplois. C'est une vraie question. Mais les études montrent que les départs sont limités, et la taxe ne touche que les fortunes de plus de 100 millions d'euros.",
 legitimes=["Le CAE mesure un effet réel de la fiscalité du patrimoine sur l'exil des plus hauts patrimoines.", "Le traitement des fondateurs de start-up sans liquidités est une difficulté technique réelle, et le rendement de la taxe est débattu."],
 contre=[
  ("Les riches partiront tous en Suisse.", "Après 2013, le CAE mesure au plus 350 départs supplémentaires par an sur 385 000 foyers du top 1 %, et Gabriel Zucman propose de taxer au moment du départ."),
  ("Les fondateurs devront vendre leur entreprise.", "Le paiement en actions ou un report permettent de payer sans vendre ; le problème est la liquidité, pas la survie de l'entreprise."),
 ],
 questions=["Sais-tu combien de foyers ont un patrimoine de plus de 100 millions d'euros en France ?", "Selon toi, est-il juste de demander aux fortunes de plus de 100 millions d'euros de payer au moins 2 % par an, tous impôts compris ?"],
 limites=["L'étude du CAE porte sur la réforme de 2013, pas directement sur la taxe Zucman ; ses effets sont des estimations.", "Le rendement réel de la taxe est très incertain (de 2 à 25 milliards selon les hypothèses)."],
 publics={'convaincus': "On parle de 1 800 foyers qui ont plus de 100 millions d'euros, pas de ton voisin artisan. Le Conseil d'analyse économique a mesuré l'exil après 2013 : quelques centaines de départs par an, un effet de 0,03 % sur l'économie. Et le RN, qui dit défendre le peuple, a voté contre la taxation des milliardaires.",
  'indecis': "C'est une vraie question de savoir si taxer les plus riches fait partir des entrepreneurs. Les études publiques montrent un effet réel mais limité. Pour les start-up, il existe des solutions comme le paiement en actions. Le débat porte surtout sur la justice : faut-il que les plus grandes fortunes paient au moins 2 % par an ?"},
 a_actualiser='2027-06-30',
))

# 11 ── RN : impôt des moins de 30 ans ────────────────────────────────────────
FICHES.append(fiche(
 id='rn-impot-moins-30-ans', affirmation="Le RN veut supprimer l'impôt sur le revenu pour les moins de 30 ans, c'est une bonne mesure pour la jeunesse.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['moins de 30 ans', 'impot des jeunes', 'exonerer les jeunes', 'exoneration d impot', 'impot sur le revenu des jeunes', 'jeunes impot', 'exoneration jeunes'],
 verdict='opinion', fiabilite='etabli',
 resume="La proposition existe : elle figure dans les programmes du RN de 2022 et 2024 et a été reprise en 2026 avec un plafond de quatre fois le Smic. Mais elle profite peu à la majorité des jeunes : les 18-25 ans gagnent trop peu pour payer l'impôt sur le revenu, et les bénéficiaires seraient surtout les actifs de 26 à 30 ans imposables, pour un gain moyen estimé à 374 € par an. Son coût est estimé entre 2 et 3,6 milliards par an, et plusieurs juristes la jugent probablement contraire à l'égalité devant l'impôt.",
 contexte="Le RN met en avant cette mesure pour séduire les jeunes actifs et limiter le départ des jeunes diplômés à l'étranger.",
 explication="Juger la mesure « bonne » ou non est un choix politique. Les faits permettent de dire qui en profiterait et combien elle coûterait.",
 sources=[MONTAIGNE_RN30, PS_RN_PROG24, LCP_RN_JEUNES, MONEYVOX_RN30],
 faits=[
  fait("Selon Public Sénat, le programme du RN de 2024 prévoit de « supprimer l'impôt sur le revenu des jeunes de moins de 30 ans » ; un vice-président du parti ajoutait que « Tout cela peut se moduler, il peut y avoir de plafonds ».", 'ps_rn_prog24', '2024', 'France', "La proposition est réelle et assumée.", 'etabli'),
  fait("Selon LCP, Marine Le Pen reprend la mesure en 2026 avec une limite « jusqu'à quatre fois le Smic », pour un coût de 2 milliards d'euros par an.", 'lcp_rn_jeunes', '2026', 'France', "Même plafonnée, elle profite à des jeunes qui gagnent bien leur vie.", 'estimation', '2 Md€'),
  fait("Selon l'Institut Montaigne, les 18-25 ans gagnent trop peu pour être imposés : les bénéficiaires seraient surtout les actifs de 26 à 30 ans, pour un gain moyen de 374 € par an et par contribuable concerné ; le coût de la version 2022 était estimé à 3,6 milliards par an.", 'montaigne_rn30', '2022', 'France', "Les jeunes les plus modestes ne gagneraient rien.", 'estimation', '374 €'),
  fait("Selon l'Institut Montaigne, la mesure serait « probablement inconstitutionnelle », car elle crée « une différence de traitement injustifiée » avec le reste de la population active.", 'montaigne_rn30', '2022', 'France', "Elle risque de ne jamais pouvoir s'appliquer.", 'interpretation'),
  fait("Selon MoneyVox, la majorité des jeunes en début de carrière paient peu ou pas d'impôt sur le revenu, et un jeune footballeur millionnaire aurait bénéficié de la version sans plafond.", 'moneyvox_rn30', '2022', 'France', "L'avantage croît avec le revenu.", 'interpretation'),
 ],
 court="C'est un choix politique, mais les faits montrent qu'elle profiterait surtout aux 26-30 ans qui gagnent bien leur vie (gain moyen estimé à 374 € par an), pas aux jeunes précaires qui ne paient pas l'impôt sur le revenu. Elle coûterait de 2 à 3,6 milliards par an et serait probablement inconstitutionnelle.",
 moyen="La mesure existe bien : le RN la propose depuis 2022, et Marine Le Pen l'a reprise en 2026 avec un plafond de quatre fois le Smic.\n\nMais qui en profiterait ? Pas les étudiants, les apprentis ni les jeunes au Smic, qui ne paient pas ou presque pas d'impôt sur le revenu. Elle profiterait surtout aux 26-30 ans qui gagnent bien leur vie, pour un gain moyen estimé à 374 € par an. Coût : 2 à 3,6 milliards par an. Pour la même somme, on pourrait aider directement les jeunes qui en ont le plus besoin.",
 detaille="Le RN propose depuis 2022 d'exonérer d'impôt sur le revenu les moins de 30 ans, notamment pour limiter le départ des jeunes diplômés. En 2026, Marine Le Pen reprend la mesure avec une limite à quatre fois le Smic ; LCP la chiffre à 2 milliards d'euros par an. L'Institut Montaigne estimait la version 2022, sans plafond, à environ 3,6 milliards par an.\n\nLa mesure profite selon le revenu : les 18-25 ans gagnent généralement trop peu pour être imposés, et les bénéficiaires seraient surtout les actifs de 26 à 30 ans imposables, pour un gain moyen estimé à 374 € par an. Plus on gagne, plus on y gagne, dans la limite du plafond. Les jeunes précaires, au chômage ou étudiants n'en verraient pas la couleur.\n\nPlusieurs juristes estiment qu'une exonération fondée sur l'âge serait contraire au principe d'égalité devant l'impôt. Pour la jeunesse, d'autres choix existent : revenu étudiant, accès au logement, hausse des bas salaires.",
 empathie="Je comprends qu'on veuille aider les jeunes, qui ont du mal à se loger et à démarrer dans la vie. L'intention peut sembler bonne. Mais cette mesure aiderait surtout les jeunes qui gagnent déjà bien leur vie, pas ceux qui galèrent.",
 legitimes=["La mesure augmenterait le revenu net des jeunes actifs imposables.", "Le départ de jeunes diplômés à l'étranger est un sujet de préoccupation réel."],
 contre=[
  ("C'est enfin une mesure pour les jeunes.", "Les jeunes les plus modestes ne paient pas d'impôt sur le revenu : ils ne gagneraient rien."),
  ("Avec le plafond à quatre Smic, c'est juste.", "Un jeune à trois Smic gagnerait beaucoup plus qu'un jeune au Smic, qui ne paie presque rien ; l'avantage reste croissant avec le revenu."),
 ],
 questions=["Sais-tu combien d'impôt sur le revenu paie un jeune au Smic ?", "Pour aider les jeunes en difficulté, vaut-il mieux baisser un impôt qu'ils ne paient pas ou les aider directement ?"],
 limites=["Les chiffrages datent de 2022 (Institut Montaigne) et de 2026 (LCP, chiffre attribué au RN) ; la version 2026 plafonnée n'a pas été chiffrée par un organisme indépendant dans les sources lues.", "Aucune donnée publique lue ne donne la part exacte des moins de 30 ans imposables."],
 publics={'convaincus': "Pose-toi la question : combien d'impôt sur le revenu paie un jeune au Smic, un apprenti ou un étudiant ? Presque rien. Cette mesure profiterait surtout aux jeunes cadres, pour environ 374 € par an en moyenne, et coûterait au moins 2 milliards. Ce n'est pas la jeunesse populaire qui y gagnerait.",
  'indecis': "La mesure part d'une bonne intention, aider les jeunes, mais elle est mal ciblée : elle profite surtout à ceux qui gagnent déjà bien leur vie. Elle coûterait 2 à 3,6 milliards par an et risque d'être jugée contraire à l'égalité devant l'impôt. D'autres aides toucheraient mieux les jeunes en difficulté."},
 a_actualiser='2027-06-30',
))

# 12 ── RN : retraite à 60 ans ────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-retraite-60-ans', affirmation="Le RN promet la retraite à 60 ans pour tout le monde.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['retraite a 60 ans', '60 ans', 'rn retraite', 'retraites rn', 'le pen retraite', 'bardella retraite', 'abroger la reforme des retraites', '40 annuites'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux depuis 2022 : le RN ne promet plus la retraite à 60 ans pour tous, mais seulement pour ceux qui ont commencé à travailler avant 20 ans, avec 40 annuités. Pour les autres, son programme de 2024 prévoyait 62 ans et jusqu'à 42 annuités (un début à 24 ans menant au taux plein à 66 ans). Depuis, ses dirigeants ont conditionné l'abrogation de la réforme de 2023 à la situation budgétaire et évoqué en 2026 d'autres pistes, comme la suppression de l'âge légal.",
 contexte="La retraite à 60 ans a longtemps été une promesse phare du RN auprès des classes populaires ; elle a été progressivement réduite à partir de 2022.",
 explication="Une retraite « à 60 ans » peut vouloir dire un âge légal pour tous ou un départ anticipé pour les carrières longues. Le RN est passé de la première à la seconde version.",
 sources=[PS_RN_RETR22, LCP_RN_RETR24, MONTAIGNE_RN_RETR, PS_RN_PROG24, PS_RN_RETR26],
 faits=[
  fait("Selon Public Sénat, le RN promettait auparavant la retraite à taux plein dès 60 ans pour tous, puis il est passé en 2022 à un système où 60 ans ne vaut que pour ceux qui ont commencé à travailler entre 17 et 20 ans : la retraite à 60 ans n'est « plus pour tout le monde ».", 'ps_rn_retr22', '2022', 'France', "La promesse a été réduite dès 2022.", 'etabli'),
  fait("Selon LCP, le programme de 2024 prévoit 60 ans avec 40 annuités pour les carrières commencées avant 20 ans et, pour les autres, un âge pivot de 62 ans et 42 annuités : un début à 24 ans mène au taux plein à 66 ans.", 'lcp_rn_retr24', '2024', 'France', "Pour la plupart des salariés, ce n'est pas 60 ans.", 'etabli', '66 ans'),
  fait("Selon l'Institut Montaigne, le dispositif complet coûterait 34,7 milliards d'euros par an, et sa deuxième étape serait décidée après un audit des comptes.", 'montaigne_rn_retr', '2024', 'France', "Même la version réduite reste conditionnée.", 'estimation', '34,7 Md€'),
  fait("Selon Public Sénat, Jordan Bardella lie en 2024 l'engagement sur les retraites à la situation budgétaire.", 'ps_rn_prog24', '2024', 'France', "La promesse devient conditionnelle.", 'etabli'),
  fait("Selon Public Sénat, en 2026, le RN étudie la suppression de l'âge légal et Jordan Bardella dit « examiner » un éventuel report de l'âge légal.", 'ps_rn_retr26', '2026', 'France', "La position actuelle s'éloigne encore de la retraite à 60 ans.", 'etabli'),
 ],
 court="Faux : depuis 2022, le RN ne promet 60 ans qu'à ceux qui ont commencé à travailler avant 20 ans. Pour les autres, son programme de 2024 prévoyait 62 ans et jusqu'à 42 annuités, et ses dirigeants évoquent désormais d'autres pistes, comme un report de l'âge légal.",
 moyen="Le RN a longtemps promis la retraite à 60 ans pour tous. Mais dès 2022, il a réduit sa promesse : 60 ans seulement pour ceux qui ont commencé à travailler avant 20 ans, avec 40 annuités.\n\nEn 2024, pour tous les autres, c'était 62 ans et jusqu'à 42 annuités : quelqu'un qui commence à 24 ans partirait à taux plein à 66 ans. Puis Jordan Bardella a conditionné l'abrogation à l'état des finances, et en 2026 il dit « examiner » un report de l'âge légal. La retraite à 60 ans pour tous n'est plus au programme.",
 detaille="La retraite à 60 ans pour tous a longtemps figuré dans le programme du FN puis du RN. En 2022, Marine Le Pen a changé de système : 60 ans et 160 trimestres pour ceux qui ont commencé à travailler entre 17 et 20 ans, puis davantage de trimestres pour les autres (au moins 42 annuités à partir d'un début à 25 ans).\n\nEn 2024, le programme prévoyait de revenir sur la réforme de 2023 : 60 ans avec 40 annuités pour les carrières commencées avant 20 ans, chiffré à 1,6 milliard d'euros pour ce seul volet ; pour les autres, un âge pivot de 62 ans et 42 annuités. L'Institut Montaigne chiffrait l'ensemble à 34,7 milliards par an. Jordan Bardella a ensuite lié l'engagement à la situation budgétaire.\n\nEn 2026, un député RN affirme encore vouloir revenir sur la réforme Borne, mais le parti étudie la suppression de l'âge légal et Jordan Bardella dit examiner un éventuel report. Pour les ouvriers et les employés qui ont cru à la retraite à 60 ans, la promesse a fondu.",
 empathie="Je comprends que la retraite à 60 ans fasse rêver, surtout quand on a un métier dur. C'est une revendication légitime. Mais le RN ne la promet plus qu'à ceux qui ont commencé avant 20 ans, et il hésite même sur le reste.",
 legitimes=["Le RN maintient le départ à 60 ans pour les carrières commencées avant 20 ans.", "Il a bien promis 60 ans pour tous avant 2022, ce qui explique la persistance de l'idée."],
 contre=[
  ("Le RN est le seul à défendre la retraite à 60 ans.", "Son programme de 2024 prévoyait 62 ans et jusqu'à 42 annuités pour la plupart des salariés."),
  ("Bardella a dit qu'il abrogerait la réforme.", "Il a conditionné l'engagement à la situation budgétaire, et dit en 2026 examiner un report de l'âge légal."),
 ],
 questions=["Sais-tu à quel âge partirait, avec le programme RN de 2024, quelqu'un qui a commencé à travailler à 24 ans ?", "Pourquoi le RN a-t-il réduit sa promesse dès 2022 ?"],
 limites=["La position du RN pour 2027 n'est pas officiellement arrêtée à la date des sources lues (mai 2026).", "Le chiffrage de l'Institut Montaigne est celui d'un think tank libéral."],
 publics={'convaincus': "Regarde le programme 2024 du RN : 60 ans seulement si tu as commencé avant 20 ans. Si tu as commencé à 24 ans, c'est taux plein à 66 ans. Et en 2026, Bardella dit qu'il « examine » un report de l'âge légal : ce n'est plus la retraite à 60 ans qu'on t'a vendue.",
  'indecis': "Le RN a longtemps promis 60 ans pour tous, mais il a réduit cette promesse dès 2022 aux seules carrières commencées avant 20 ans. Pour la majorité, son programme prévoyait 62 ans et jusqu'à 42 annuités. Avant de voter sur ce sujet, mieux vaut comparer les programmes actuels, pas les souvenirs."},
 a_actualiser='2027-03-31',
))

# 13 ── Feux de forêt ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='feux-foret-pyromanes', affirmation="Les feux de forêt sont causés par des pyromanes, pas par le réchauffement climatique.", volet='ecologie', sous_theme='Changement climatique',
 mots_cles=['feux de foret', 'incendies de foret', 'pyromanes', 'pyromane', 'incendiaires', 'feux', 'incendies', 'mega feux', 'megafeux'],
 verdict='trompeur', fiabilite='etabli',
 resume="Fausse alternative : 9 départs de feu sur 10 sont d'origine humaine, mais surtout par imprudence (environ la moitié), la malveillance représentant environ un quart des départs. Le climat n'allume pas les feux : il crée les conditions de leur départ et de leur propagation. Selon Météo-France, le danger de feu progresse vers le nord, et les jours de danger très élevé pourraient doubler en région méditerranéenne.",
 contexte="Après les grands incendies de 2022 (plus de 70 000 hectares brûlés), puis ceux des étés suivants, l'idée que « ce sont des pyromanes » circule pour nier le rôle du réchauffement.",
 explication="Pour qu'un feu se déclare et s'étende, il faut une étincelle (presque toujours humaine) et une végétation sèche, de la chaleur et du vent. Le réchauffement agit sur la seconde condition, en allongeant et en intensifiant les sécheresses.",
 sources=[MTE_FEUX, MTE_FEUX_DP, MF_FEUX, GIEC_FEUX],
 faits=[
  fait("Selon le ministère de la Transition écologique, 90 % des départs de feux de forêt ont pour origine les activités humaines, et la moitié sont dus à des imprudences et à des comportements dangereux.", 'mte_feux', '2026', 'France', "L'homme allume les feux, mais surtout par imprudence.", 'etabli', '90 %'),
  fait("Selon le ministère, la malveillance représente environ un quart des départs de feux.", 'mte_feux', '2026', 'France', "Les incendies volontaires existent, mais ils ne sont pas majoritaires.", 'estimation', '25 %'),
  fait("Selon Météo-France, la hausse des températures assèche la végétation et le danger de feu progresse vers le nord ; en région méditerranéenne, les jours de danger très élevé passeraient d'environ 40 à plus de 80 par an, et à +4 °C le risque se généraliserait à tout le pays.", 'mf_feux', '2026', 'France', "Le climat multiplie les jours où une étincelle devient un incendie.", 'estimation', '40 à 80 jours'),
  fait("Selon le GIEC, l'influence humaine a probablement augmenté les conditions météorologiques propices aux feux dans certaines régions de tous les continents habités (confiance moyenne).", 'giec_feux', '2021', 'Monde', "Le consensus scientifique relie réchauffement et danger de feu.", 'estimation'),
  fait("Selon le ministère, le changement climatique, en allongeant et intensifiant les sécheresses, favorise l'éclosion et le développement des feux ; 30 500 hectares ont brûlé en 2025.", 'mte_feux_dp', '2025-2026', 'France', "Les deux causes s'additionnent.", 'etabli', '30 500 ha'),
 ],
 court="Fausse alternative : 9 feux sur 10 sont d'origine humaine, mais surtout par imprudence, la malveillance ne représentant qu'environ un quart des départs. Et le réchauffement crée les conditions qui transforment une étincelle en incendie : selon Météo-France, les jours de danger très élevé pourraient doubler dans le Sud.",
 moyen="C'est vrai : presque tous les feux sont allumés par l'homme. Mais surtout par imprudence (une cigarette, des travaux, un barbecue), pas par des pyromanes : la malveillance représente environ un quart des départs.\n\nEt une étincelle ne devient un incendie que si la végétation est sèche et qu'il fait chaud. C'est là qu'intervient le réchauffement : selon Météo-France, les jours de danger très élevé pourraient passer de 40 à plus de 80 par an dans le Sud, et le risque s'étend vers le nord. Il faut à la fois prévenir les imprudences et lutter contre le réchauffement.",
 detaille="Selon le ministère de la Transition écologique, 90 % des départs de feux de forêt ont une origine humaine. La moitié sont dus à des imprudences ou à des comportements dangereux (travaux, mégots, brûlages), et la malveillance représente environ un quart des départs. Les vrais pyromanes, au sens médical, sont une petite minorité des incendiaires.\n\nMais un départ de feu ne devient un grand incendie que si la végétation est sèche, la température élevée et le vent fort. C'est ce que mesure l'indice de danger météorologique de Météo-France : avec le réchauffement, les jours de danger très élevé en région méditerranéenne passeraient d'environ 40 à plus de 80 par an, la saison à risque s'allongerait d'un à deux mois et le danger progresse vers le nord. Le GIEC constate que l'influence humaine a probablement déjà augmenté ces conditions dans certaines régions.\n\nLes deux causes ne s'opposent pas : elles s'additionnent. Punir les incendiaires est nécessaire, mais ne suffira pas si chaque été offre davantage de jours où une simple étincelle suffit.",
 empathie="Je comprends la colère contre ceux qui mettent le feu volontairement : elle est légitime. Mais la plupart des feux viennent d'imprudences, et c'est le climat plus sec qui les rend si difficiles à arrêter.",
 legitimes=["L'homme est bien à l'origine de l'immense majorité des départs de feux, et la foudre est rare.", "La malveillance existe réellement (environ un quart des départs selon le ministère)."],
 contre=[
  ("Il y a toujours eu des incendies l'été.", "Oui, mais Météo-France montre que les jours de danger très élevé augmentent et que le risque gagne des régions jusqu'ici épargnées."),
  ("Il suffit d'arrêter les pyromanes.", "La moitié des départs viennent d'imprudences ; et plus la saison est sèche, plus chaque imprudence devient dangereuse."),
 ],
 questions=["Sais-tu quelle part des feux est due à des imprudences plutôt qu'à des incendiaires ?", "Pourquoi, selon toi, des régions du nord de la France connaissent-elles désormais des feux de forêt ?"],
 limites=["Les estimations de la part des feux volontaires varient selon les sources ; la page du ministère ne présente pas une ventilation entièrement cohérente.", "L'indice de Météo-France mesure un danger météorologique, pas le nombre de départs de feu."],
 publics={'convaincus': "Tu as raison sur un point : c'est presque toujours l'homme qui allume le feu. Mais selon le ministère, c'est surtout par imprudence, et la malveillance, c'est environ un quart. Et Météo-France montre que les jours où une étincelle suffit vont doubler dans le Sud : les deux problèmes s'additionnent.",
  'indecis': "Les feux de forêt ont deux causes qui s'ajoutent : une étincelle, presque toujours humaine et souvent accidentelle, et une végétation desséchée par la chaleur. Le réchauffement rend la seconde de plus en plus fréquente. Prévenir les imprudences et lutter contre le réchauffement vont donc ensemble."},
 a_actualiser='2027-06-30',
))

# 14 ── ZFE ───────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='zfe-menages-modestes', affirmation="Les zones à faibles émissions punissent les pauvres qui ne peuvent pas changer de voiture.", volet='ecologie', sous_theme='Transports',
 mots_cles=['zfe', 'zones a faibles emissions', 'zone a faibles emissions', 'crit air', 'critair', 'vignette crit air', 'zfe m', 'interdire les vieilles voitures'],
 verdict='plutot_exact', fiabilite='etabli',
 resume="En partie vrai : dans les métropoles du Grand Paris et de Lyon, les voitures Crit'Air 3 ou plus représentent environ 4 voitures sur 10 chez les 20 % de ménages les plus modestes, contre un peu plus d'une sur quatre en moyenne ; la contrainte pèse donc plus lourd sur eux. Mais la pollution de l'air cause environ 40 000 décès par an en France, et les enfants des familles pauvres en souffrent davantage. La suppression des ZFE votée en 2026 a été censurée par le Conseil constitutionnel pour une raison de procédure : elles sont maintenues.",
 contexte="La suppression des ZFE a été votée au printemps 2026 par le RN, la Droite républicaine et LFI, avant d'être censurée en mai 2026 comme « cavalier législatif ».",
 explication="Une ZFE interdit progressivement la circulation des véhicules les plus polluants dans certaines agglomérations. L'objectif est sanitaire ; le problème est social, car les ménages modestes ont plus souvent de vieilles voitures et moins de moyens pour en changer.",
 sources=[SDES_ZFE, SPF_AIR, OI_AIR, LCP_ZFE, AN_QE3069],
 faits=[
  fait("Selon le service statistique du ministère, les voitures Crit'Air 3 ou plus représentent environ 4 voitures sur 10 chez les 20 % de ménages les plus modestes du Grand Paris et de Lyon, contre un peu plus d'une voiture sur quatre pour l'ensemble des ménages.", 'sdes_zfe', '2025', 'Grand Paris et Lyon', "La contrainte pèse réellement plus sur les ménages modestes motorisés.", 'etabli', '4 sur 10'),
  fait("Selon Santé publique France, près de 40 000 décès par an sont attribuables aux particules fines chez les 30 ans et plus (2016-2019), soit 7 % de la mortalité totale.", 'spf_air', '2016-2019', 'France', "La pollution de l'air tue massivement ; l'objectif des ZFE est sanitaire.", 'estimation', '40 000'),
  fait("Selon l'Observatoire des inégalités, d'après la DREES, avant 2 ans, 5 % des enfants des familles les plus pauvres ont été hospitalisés pour bronchiolite, contre 2,4 % des plus riches.", 'oi_air', '2016-2018', 'France', "Les familles modestes subissent plus les effets de la pollution sur la santé.", 'etabli', '5 % contre 2,4 %'),
  fait("Selon le ministère des Transports en 2022, des aides existaient pour les ménages modestes en ZFE : prime à la conversion jusqu'à 6 000 € pour un véhicule électrique, microcrédit jusqu'à 8 000 €, leasing social prévu, dérogations locales.", 'an_qe3069', '2022', 'France', "Des aides existent, mais elles ne couvrent pas tout le coût d'un véhicule.", 'etabli', '6 000 €'),
  fait("Selon LCP, la suppression des ZFE votée en avril 2026 (amendements RN et Droite républicaine, avec le soutien de LFI) a été censurée par le Conseil constitutionnel le 21 mai 2026 comme cavalier législatif ; les ZFE sont maintenues.", 'lcp_zfe', '2026', 'France', "Le débat est transpartisan et reste ouvert.", 'etabli'),
 ],
 court="En partie vrai : les ménages modestes ont deux fois plus souvent des voitures Crit'Air 3 ou plus. Mais la pollution de l'air cause environ 40 000 décès par an, et les familles pauvres en souffrent davantage : la solution est d'aider fortement à changer de véhicule et de développer les transports publics, pas de renoncer à l'air pur.",
 moyen="Il y a du vrai : dans le Grand Paris et à Lyon, 4 voitures sur 10 des ménages les plus modestes sont des Crit'Air 3 ou plus, contre un peu plus d'une sur quatre en moyenne. Interdire ces voitures sans alternative pèse d'abord sur eux.\n\nMais la pollution de l'air cause environ 40 000 décès par an en France, et ce sont aussi les enfants pauvres qui en souffrent le plus : deux fois plus d'hospitalisations pour bronchiolite. La question n'est donc pas « ZFE ou pas », mais qui paie la transition : aides massives, leasing social, transports en commun.",
 detaille="Selon le service statistique du ministère, les voitures Crit'Air 3 ou plus représentent un peu plus d'une voiture sur quatre des ménages du Grand Paris et de Lyon, mais environ 4 sur 10 chez les 20 % les plus modestes. Les ZFE pèsent donc plus sur les ménages modestes qui ont besoin de leur voiture. Des aides existaient en 2022 (prime à la conversion majorée, microcrédit, leasing social), mais elles ne suffisent pas toujours à acheter un véhicule récent.\n\nL'objectif est pourtant vital : Santé publique France attribue près de 40 000 décès par an aux particules fines. Et les inégalités jouent aussi dans l'autre sens : selon la DREES, les enfants des familles les plus pauvres sont deux fois plus souvent hospitalisés pour bronchiolite avant 2 ans que ceux des plus riches.\n\nEn 2026, le Parlement a voté la suppression des ZFE, avec le RN, la Droite républicaine et LFI ; le Conseil constitutionnel l'a censurée pour une raison de procédure. Une écologie populaire refuse de faire payer la transition aux plus modestes : elle exige des aides à la hauteur, des transports publics et des dérogations, plutôt que l'abandon de l'air pur.",
 empathie="Je comprends parfaitement la colère de quelqu'un qui a besoin de sa vieille voiture pour aller travailler et qui ne peut pas en acheter une neuve. C'est une injustice réelle. Mais la pollution tue aussi, et souvent les mêmes familles.",
 legitimes=["Les ménages modestes possèdent proportionnellement plus de véhicules concernés par les interdictions.", "Les aides existantes ne couvrent pas tout le coût d'un véhicule récent, et les transports publics manquent hors des centres."],
 contre=[
  ("La pollution, c'est exagéré.", "Santé publique France attribue près de 40 000 décès par an aux particules fines."),
  ("Les ZFE, c'est l'écologie des riches.", "La critique sociale est juste, mais ce sont aussi les enfants pauvres qui souffrent le plus de la pollution : il faut changer qui paie, pas renoncer."),
 ],
 questions=["Qu'est-ce qui t'aiderait concrètement à changer de véhicule ou à t'en passer ?", "Savais-tu que les enfants des familles pauvres sont deux fois plus souvent hospitalisés pour bronchiolite ?"],
 limites=["Les données sur les aides datent de 2022 ; leur montant en 2026 n'a pas pu être vérifié.", "Les données sur les voitures Crit'Air ne concernent que le Grand Paris et Lyon ; la part des ménages modestes sans voiture n'a pas été chiffrée."],
 publics={'convaincus': "Tu as raison sur un point : ce sont les ménages modestes qui ont le plus de vieilles voitures, et les aides ne suffisent pas. Mais la pollution de l'air, c'est environ 40 000 morts par an, et ce sont aussi les enfants pauvres qui finissent à l'hôpital. Exige qu'on t'aide à changer de voiture et qu'on développe les bus, pas qu'on laisse l'air empoisonné.",
  'indecis': "Les ZFE posent un vrai problème social : les ménages modestes ont plus souvent des voitures concernées. Mais elles répondent à un vrai problème de santé publique. Le bon débat porte sur les aides, les transports en commun et les dérogations, pour que la transition ne pèse pas sur les plus pauvres."},
 a_actualiser='2027-06-30',
))

# 15 ── Vaccins ARN ───────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='vaccins-arn-mortalite', affirmation="Les vaccins à ARN messager ont fait plus de morts que le covid.", volet='politique', sous_theme='Désinformation',
 mots_cles=['vaccins arn', 'arn messager', 'arnm', 'vaccin covid', 'vaccins covid', 'pfizer', 'moderna', 'morts du vaccin', 'effets secondaires vaccin', 'vaccin tue'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux : le covid a fait plus de 160 000 morts en France entre mars 2020 et décembre 2022, dont 60 895 sur la seule année 2021. Une étude d'EPI-PHARE sur 28 millions de personnes de 18 à 59 ans montre une mortalité toute cause plus basse de 20 à 25 % chez les vaccinés sur quatre ans, et « exclut » un risque accru de décès. Les vaccins ont des effets indésirables réels, comme les myocardites chez les jeunes hommes, rares et d'évolution généralement favorable.",
 contexte="Depuis 2021, des affirmations sur une surmortalité due aux vaccins à ARN circulent sur les réseaux sociaux, relayées par des milieux antivaccins et une partie de l'extrême droite.",
 explication="Pour savoir si un vaccin tue, on compare la mortalité de très grands groupes de personnes vaccinées et non vaccinées, et on suit les effets indésirables déclarés (pharmacovigilance).",
 sources=[EPIPHARE_ARN, ANSM_MYO, SPF_DECES21, AD_COVID, OMS_VACC],
 faits=[
  fait("Selon Santé publique France, relayée par l'AFP, plus de 160 000 personnes sont mortes du covid en France entre mars 2020 et décembre 2022.", 'ad_covid', '2020-2022', 'France', "Le covid a été une catastrophe sanitaire.", 'etabli', '160 008'),
  fait("Selon Santé publique France, le covid a directement causé 60 895 décès en France en 2021, troisième cause de décès cette année-là.", 'spf_deces21', '2021', 'France', "Une seule année de covid a tué plus de 60 000 personnes.", 'etabli', '60 895'),
  fait("Selon EPI-PHARE, sur près de 29 millions de personnes de 18 à 59 ans suivies quatre ans, la mortalité toute cause est environ 20 à 25 % plus faible chez les vaccinés ; les résultats « excluent donc un risque accru de mortalité toute cause à 4 ans chez les individus vaccinés ».", 'epiphare_arn', '2021-2025', 'France', "Si le vaccin tuait massivement, les vaccinés mourraient davantage : c'est l'inverse.", 'etabli', '-20 à -25 %'),
  fait("Selon l'ANSM, le risque de myocardite après vaccination est confirmé, surtout chez les hommes de moins de 30 ans avec Spikevax (environ 132 cas en excès par million de doses), avec une évolution généralement favorable et aucun décès chez les patients hospitalisés de l'étude.", 'ansm_myo', '2021-2022', 'France', "Les effets indésirables existent ; ils sont rares et ont été rendus publics.", 'etabli', '132 par million'),
  fait("Selon l'OMS, la vaccination a sauvé plus de 1,4 million de vies dans la région Europe entre 2020 et mars 2023.", 'oms_vacc', '2020-2023', 'Europe', "Le bilan est très largement positif.", 'estimation', '1,4 million'),
 ],
 court="Faux : le covid a tué plus de 160 000 personnes en France de 2020 à 2022, et une étude sur 28 millions de Français montre une mortalité plus basse de 20 à 25 % chez les vaccinés sur quatre ans. Les effets indésirables graves existent mais sont rares.",
 moyen="Le covid a fait plus de 160 000 morts en France de mars 2020 à fin 2022, dont près de 61 000 en 2021. Si les vaccins avaient fait encore plus de morts, ça se verrait : on aurait des centaines de milliers de décès inexpliqués.\n\nOr EPI-PHARE a suivi près de 29 millions de Français de 18 à 59 ans pendant quatre ans : les vaccinés meurent 20 à 25 % moins que les non-vaccinés. Il y a des effets indésirables réels, comme les myocardites chez de jeunes hommes ; ils sont rares, guérissent en général, et l'ANSM les a publiés.",
 detaille="Selon Santé publique France, plus de 160 000 personnes sont mortes du covid en France entre mars 2020 et décembre 2022 ; en 2021, le covid a directement causé 60 895 décès. L'OMS estime que la vaccination a sauvé plus de 1,4 million de vies en Europe entre 2020 et mars 2023.\n\nEn décembre 2025, EPI-PHARE (ANSM et Assurance maladie) a publié une étude sur près de 29 millions de personnes de 18 à 59 ans suivies pendant 45 mois en médiane. Les vaccinés à ARN ont un risque de décès toute cause environ 25 % plus faible (20 % après correction des biais). Les auteurs concluent que ces résultats excluent un risque accru de mortalité, tout en signalant les limites d'une étude observationnelle.\n\nLes vaccins ont des effets indésirables : l'ANSM a confirmé dès 2021 un risque de myocardite, surtout chez les hommes de moins de 30 ans, rare et d'évolution généralement favorable. Ce suivi public montre justement que les effets indésirables sont recherchés et publiés. Les chiffres disent clairement que le covid a tué beaucoup plus que les vaccins.",
 empathie="Je comprends qu'on se méfie d'un vaccin développé vite, et qu'on connaisse quelqu'un qui a eu des effets secondaires. Ça existe. Mais les études sur des millions de Français montrent que les vaccinés sont moins morts, pas plus.",
 legitimes=["Les vaccins à ARN ont des effets indésirables graves réels, comme les myocardites, surtout chez les jeunes hommes.", "Les déclarations de pharmacovigilance ne sont pas exhaustives, et l'étude EPI-PHARE est observationnelle."],
 contre=[
  ("On cache les morts du vaccin.", "L'ANSM publie les effets indésirables, y compris les myocardites ; et une étude sur 28 millions de personnes ne montre aucune surmortalité."),
  ("Le covid ne tuait que les personnes âgées.", "Il a surtout tué des personnes âgées, mais plus de 160 000 morts restent un bilan énorme, et l'étude EPI-PHARE porte justement sur les 18-59 ans."),
 ],
 questions=["Combien de morts du covid y a-t-il eu en France, selon toi ?", "Si le vaccin tuait plus que le covid, pourquoi les vaccinés mourraient-ils moins dans une étude sur 28 millions de personnes ?"],
 limites=["Le décompte de 160 000 morts date de décembre 2022 ; il a augmenté depuis.", "L'étude EPI-PHARE ne porte que sur les 18-59 ans et présente une incohérence de chiffre sur le risque de covid sévère entre son résumé et son texte."],
 publics={'convaincus': "Plus de 160 000 morts du covid en France en moins de trois ans : si les vaccins avaient tué davantage, il y aurait des centaines de milliers de morts inexpliqués. L'étude sur 28 millions de Français montre au contraire que les vaccinés sont morts moins. Les myocardites existent, et c'est l'ANSM elle-même qui les a rendues publiques.",
  'indecis': "La méfiance envers un vaccin nouveau est compréhensible, et les effets indésirables existent, comme de rares myocardites. Mais les grandes études françaises sont claires : la vaccination n'augmente pas la mortalité, et le covid a tué plus de 160 000 personnes. Le bilan reste très largement en faveur du vaccin."},
 a_actualiser='2027-12-31',
))

# 16 ── NFP et législatives 2024 ──────────────────────────────────────────────
FICHES.append(fiche(
 id='nfp-legislatives-2024', affirmation="Le Nouveau Front populaire n'a pas gagné les législatives de 2024, il n'avait aucune légitimité pour gouverner.", volet='politique', sous_theme='Gauche et pluralisme politique',
 mots_cles=['nouveau front populaire', 'nfp', 'legislatives 2024', 'legislatives de 2024', 'gagne les legislatives', 'lucie castets', 'matignon', 'legitimite pour gouverner'],
 verdict='opinion', fiabilite='etabli',
 resume="Le NFP est arrivé en tête aux législatives de juillet 2024 avec 182 sièges, devant Ensemble (168) et le RN (143), mais loin de la majorité absolue (289). Aucun bloc n'avait de majorité. La Constitution laisse au président le choix du Premier ministre, sous le contrôle de l'Assemblée qui peut censurer ; le président a écarté le NFP en invoquant une censure annoncée, puis nommé Michel Barnier (LR), issu d'un parti qui ne faisait pas partie des trois premiers blocs. Dire que le NFP n'avait « aucune légitimité » relève de l'opinion.",
 contexte="Le refus de nommer Lucie Castets, candidate du NFP, puis la nomination de Michel Barnier en septembre 2024 ont nourri un débat durable sur la « victoire » de la gauche et le respect du vote.",
 explication="Arriver en tête ne donne pas automatiquement le pouvoir dans un régime parlementaire sans majorité : il faut trouver un gouvernement qui ne soit pas renversé. Mais l'usage veut souvent que la force arrivée en tête soit appelée la première.",
 sources=[DATAN_LEG24, LEGI_ART8, PS_CASTETS, LCP_NFP_REJET, LCP_BARNIER],
 faits=[
  fait("Selon Datan, aux législatives de juillet 2024, le NFP a obtenu 182 sièges, Ensemble 168 et le RN 143 ; il manquait plus de 100 sièges au NFP pour la majorité absolue (289).", 'datan_leg24', '2024', 'France', "Le NFP était premier, sans majorité, comme tous les autres blocs.", 'etabli', '182 sièges'),
  fait("Selon l'article 8 de la Constitution, « Le Président de la République nomme le Premier ministre ».", 'legi_art8', '1958', 'France', "Le texte ne dit pas qu'il faut choisir le groupe arrivé en tête.", 'etabli'),
  fait("Selon Public Sénat, des constitutionnalistes divergent : pour l'un, le président « peut nommer qui il veut, c'est ensuite à l'Assemblée nationale de censurer » ; pour un autre, il « n'a plus un pouvoir discrétionnaire » de nomination.", 'ps_castets', '2024', 'France', "La question de la légitimité est débattue par les juristes eux-mêmes.", 'debat'),
  fait("Selon LCP, l'Élysée a justifié le refus d'un gouvernement NFP par le fait qu'il « serait immédiatement censuré par l'ensemble des autres groupes », tout en qualifiant le NFP d'« alliance regroupant le plus de députés ».", 'lcp_nfp_rejet', '2024', 'France', "Le président lui-même reconnaissait que le NFP était le premier bloc.", 'etabli'),
  fait("Selon LCP, Michel Barnier (LR) a été nommé Premier ministre près de deux mois après les élections.", 'lcp_barnier', '2024', 'France', "Le gouvernement a été confié à un parti extérieur aux trois premiers blocs.", 'etabli'),
 ],
 court="C'est une opinion : le NFP n'a pas eu de majorité (182 sièges sur 289 nécessaires), mais il est arrivé en tête, et aucun autre bloc n'avait de majorité. Le président a finalement nommé un Premier ministre issu de LR, qui ne faisait pas partie des trois premiers blocs.",
 moyen="Le NFP n'a pas « gagné » au sens d'une majorité : 182 sièges, quand il en faut 289. Mais il est arrivé en tête, devant le camp présidentiel (168) et le RN (143), et l'Élysée lui-même l'a reconnu comme « l'alliance regroupant le plus de députés ».\n\nLa Constitution laisse le choix du Premier ministre au président, et l'Assemblée peut censurer. Le président a écarté le NFP au nom d'une censure annoncée, puis a nommé Michel Barnier, issu de LR, qui ne faisait pas partie des trois premiers blocs. On peut juger ce choix légal ; dire que le premier bloc n'avait « aucune légitimité », c'est une opinion.",
 detaille="Au soir du 7 juillet 2024, l'Assemblée nationale est divisée en trois blocs sans majorité : 182 sièges pour le Nouveau Front populaire, 168 pour Ensemble, 143 pour le RN, selon le décompte de Datan ; la majorité absolue est de 289. Le NFP est donc premier, mais loin d'une majorité.\n\nL'article 8 de la Constitution laisse au président le choix du Premier ministre. Les constitutionnalistes divergent : pour certains, il peut nommer qui il veut, l'Assemblée pouvant censurer ; pour d'autres, il doit tenir compte du résultat. Fin août 2024, l'Élysée a écarté un gouvernement NFP, qui serait selon lui immédiatement censuré, tout en reconnaissant que le NFP était l'alliance regroupant le plus de députés.\n\nMichel Barnier, issu de LR, qui ne faisait pas partie des trois premiers blocs, a été nommé près de deux mois après les élections. Le NFP n'avait pas de majorité pour gouverner seul ; mais aucun autre bloc n'en avait. La légitimité d'un gouvernement dans une Assemblée sans majorité est une question politique, pas un fait.",
 empathie="Je comprends qu'on dise que la gauche n'avait pas gagné : elle était loin d'une majorité, c'est vrai. Mais elle était arrivée première, et le gouvernement a été donné à un parti qui ne faisait pas partie des trois premiers blocs.",
 legitimes=["Le NFP n'avait pas de majorité absolue, et un gouvernement NFP était exposé à une censure annoncée.", "La Constitution laisse au président le choix du Premier ministre."],
 contre=[
  ("Le RN a eu plus de voix que le NFP.", "Les sources lues portent sur les sièges ; c'est en sièges que se décide qui peut gouverner dans l'Assemblée."),
  ("Le NFP aurait été censuré tout de suite.", "C'est l'argument de l'Élysée ; il n'a pas été vérifié par un vote, et aucun autre bloc n'avait non plus de majorité."),
 ],
 questions=["Quel bloc avait une majorité absolue en juillet 2024 ?", "Est-il plus légitime de confier le gouvernement au premier bloc ou à un parti qui ne faisait pas partie des trois premiers ?"],
 limites=["Le décompte des sièges vient de Datan, site d'analyse parlementaire ; les résultats officiels du ministère de l'Intérieur n'ont pas pu être lus.", "La comparaison en nombre de voix entre blocs n'a pas été vérifiée dans les sources lues."],
 publics={'convaincus': "Personne n'avait de majorité en 2024 : le NFP avait 182 sièges, le camp Macron 168, le RN 143. Le NFP était premier, l'Élysée l'a reconnu. Si arriver premier sans majorité ne donne « aucune légitimité », alors celle d'un Premier ministre venu d'un parti extérieur aux trois premiers blocs pose encore plus question.",
  'indecis': "Le NFP n'a pas eu de majorité, mais aucun bloc n'en avait. La Constitution laisse le président choisir, sous le contrôle de l'Assemblée. On peut juger la décision du président légale tout en se demandant si elle respectait l'esprit du vote : c'est là un débat politique légitime."},
 a_actualiser='2027-12-31',
))

# 17 ── RN et salaires ────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='rn-salaires-votes', affirmation="Le RN défend les travailleurs et vote pour la hausse des salaires.", volet='politique', sous_theme='Rassemblement national',
 mots_cles=['rn salaires', 'rn smic', 'vote du rn', 'rn vote contre le smic', 'hausse des salaires', 'augmenter le smic', 'indexation des salaires', 'rn travailleurs', 'parti des travailleurs'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur : le 20 juillet 2022, les 69 députés RN présents ont voté contre deux amendements portant le Smic à 1 500 € net et contre l'indexation des salaires sur l'inflation. Marine Le Pen s'oppose à une hausse du Smic, qui « peut mettre en difficulté quelques entreprises ». Le RN propose à la place une hausse facultative de 10 % des salaires, décidée par les employeurs volontaires et financée par des exonérations de cotisations. Il a en revanche voté pour un amendement conditionnant les exonérations au respect du Smic dans les branches.",
 contexte="Le RN se présente comme le premier parti des ouvriers et revendique la défense du pouvoir d'achat ; ses votes à l'Assemblée sur les salaires sont souvent cités par la gauche pour le contester.",
 explication="Il existe deux façons d'augmenter les salaires : les imposer (hausse du Smic, indexation) ou inciter les employeurs (exonérations de cotisations). Le RN choisit la seconde, qui laisse la décision aux entreprises et réduit les ressources de la Sécurité sociale.",
 sources=[DATAN_SMIC44, DATAN_SMIC42, DATAN_SMIC38, LCP_RN_SAL],
 faits=[
  fait("Selon les scrutins publics repris par Datan, le 20 juillet 2022, l'amendement portant le Smic à 1 500 € net a été rejeté par 255 voix contre 121 ; groupe RN : 69 contre, 1 abstention, 0 pour.", 'datan_smic44', '2022', 'France', "Le RN a voté contre la hausse du Smic.", 'etabli', '69 contre'),
  fait("Selon les scrutins publics repris par Datan, le même jour, l'amendement indexant les salaires du privé sur l'inflation a été rejeté par 269 voix contre 108 ; groupe RN : 69 contre, 0 pour.", 'datan_smic42', '2022', 'France', "Le RN a refusé que les salaires suivent les prix.", 'etabli', '69 contre'),
  fait("Selon LCP, Marine Le Pen oppose sa proposition à une hausse du Smic, qui « peut mettre en difficulté quelques entreprises ».", 'lcp_rn_sal', '2023', 'France', "Le RN reprend l'argument patronal contre le Smic.", 'etabli'),
  fait("Selon LCP, la proposition de loi RN de janvier 2023 permettait aux entreprises volontaires d'augmenter les salaires de 10 %, hausses exonérées de « l'essentiel des charges » jusqu'à trois Smic ; elle a été rejetée.", 'lcp_rn_sal', '2023', 'France', "La hausse dépendrait du bon vouloir des patrons et serait payée par moins de cotisations.", 'etabli', '10 %'),
  fait("Selon les scrutins publics repris par Datan, le groupe RN a voté pour (69 voix) un amendement conditionnant les exonérations de cotisations au respect du Smic dans les grilles de branche, rejeté par 183 voix contre 181.", 'datan_smic38', '2022', 'France', "Le RN a soutenu au moins une mesure en faveur des bas salaires.", 'etabli', '69 pour'),
 ],
 court="Trompeur : en juillet 2022, le RN a voté contre le Smic à 1 500 € net et contre l'indexation des salaires sur l'inflation. Il propose à la place une hausse facultative, décidée par les patrons et payée par moins de cotisations sociales.",
 moyen="Les votes sont publics. Le 20 juillet 2022, les 69 députés RN présents ont voté contre le Smic à 1 500 € net et contre l'indexation des salaires sur l'inflation. Marine Le Pen dit qu'une hausse du Smic « peut mettre en difficulté quelques entreprises » : c'est l'argument du patronat.\n\nLe RN propose à la place que les entreprises qui le veulent augmentent les salaires de 10 %, en échange de moins de cotisations. Autrement dit : la hausse dépend du patron, et c'est la Sécurité sociale qui paie. Il a soutenu un amendement sur le respect du Smic dans les branches, mais pas les hausses obligatoires.",
 detaille="Lors de l'examen du projet de loi sur le pouvoir d'achat, le 20 juillet 2022, plusieurs amendements de gauche proposaient de relever les salaires. Selon les scrutins publics, les 69 députés RN présents ont voté contre deux amendements portant le Smic à 1 500 € net (l'un avec une caisse de péréquation pour les PME) et contre l'indexation des salaires du privé sur l'inflation.\n\nLe RN défend une autre méthode : sa proposition de loi de janvier 2023 permettait aux entreprises volontaires d'augmenter les salaires de 10 %, en exonérant ces hausses de l'essentiel des cotisations jusqu'à trois Smic. Marine Le Pen l'opposait à une hausse du Smic, qui peut selon elle mettre en difficulté des entreprises. Le texte a été rejeté ; un député de la majorité de l'époque le jugeait coûteux et inefficace.\n\nLe RN a toutefois voté pour un amendement conditionnant les exonérations de cotisations au respect du Smic dans les grilles de branche, rejeté à deux voix près. Défendre les travailleurs, c'est voter des hausses qu'ils obtiennent de plein droit ; une hausse laissée au bon vouloir des employeurs, financée par moins de cotisations, revient à affaiblir la Sécurité sociale qui les protège.",
 empathie="Je comprends qu'on ait le sentiment que le RN parle des fins de mois, et c'est vrai qu'il en parle. Mais quand il a fallu voter le Smic à 1 500 € ou l'indexation des salaires, ses députés ont voté contre.",
 legitimes=["Le RN a déposé une proposition de loi visant à augmenter les salaires, même facultativement.", "Il a voté pour un amendement en faveur du respect du Smic dans les grilles de branche."],
 contre=[
  ("Augmenter le Smic tuerait les petites entreprises.", "L'un des amendements rejetés prévoyait justement une caisse de péréquation pour aider les PME ; le RN a voté contre aussi."),
  ("Sa proposition de 10 % est meilleure.", "Elle dépend du bon vouloir des employeurs et réduit les cotisations qui financent la Sécurité sociale des salariés."),
 ],
 questions=["Sais-tu comment ont voté les députés RN sur le Smic à 1 500 € en juillet 2022 ?", "Une hausse de salaire que ton patron peut refuser, est-ce vraiment une hausse ?"],
 limites=["Les votes vérifiés datent de juillet 2022 ; les votes RN de 2023 à 2026 sur le Smic n'ont pas été vérifiés.", "Les scrutins ont été lus sur Datan, qui reprend les scrutins publics de l'Assemblée, et non sur le site de l'Assemblée."],
 publics={'convaincus': "Les votes sont publics, tu peux les vérifier : le 20 juillet 2022, les 69 députés RN ont voté contre le Smic à 1 500 € net et contre l'indexation des salaires sur les prix. Leur proposition, c'est une hausse que ton patron peut refuser, payée par moins de cotisations pour ta Sécu. Ce n'est pas ce qu'on attend d'un parti qui dit défendre les travailleurs.",
  'indecis': "Le RN parle beaucoup de pouvoir d'achat, mais ses votes montrent un choix précis : pas de hausse obligatoire du Smic ni d'indexation, plutôt des incitations aux employeurs. C'est un choix politique, proche de celui de la droite. À chacun de juger, à partir des votes plutôt que des slogans."},
 a_actualiser='2027-06-30',
))

# 18 ── Voitures thermiques 2035 ──────────────────────────────────────────────
FICHES.append(fiche(
 id='voitures-thermiques-2035', affirmation="L'Europe nous interdit de vendre des voitures thermiques en 2035.", volet='ecologie', sous_theme='Transports',
 mots_cles=['2035', 'voitures thermiques', 'voiture thermique', 'fin du thermique', 'interdiction des voitures thermiques', 'moteurs thermiques', 'bruxelles voiture', 'interdire les voitures essence'],
 verdict='trompeur', fiabilite='etabli',
 resume="Trompeur et dépassé : le règlement européen de 2023 fixe pour 2035 une réduction de 100 % des émissions de CO2 des voitures neuves, ce qui revenait en pratique à arrêter la vente de voitures neuves émettant du CO2 à l'échappement. Il ne vise pas les voitures déjà en circulation ni l'occasion, et prévoit une exception pour les carburants neutres en CO2. Depuis décembre 2025, la Commission propose de ramener l'objectif à 90 %, ce qui permettrait encore de vendre des hybrides et des moteurs thermiques après 2035 ; le texte est en discussion en novembre 2026.",
 contexte="La date de 2035 est devenue un symbole de l'« écologie punitive » venue de Bruxelles, notamment pour le RN ; en février 2025, l'Assemblée a voté contre sa transposition, sans effet sur le droit européen.",
 explication="Le règlement ne liste pas des voitures interdites : il fixe des objectifs d'émissions de CO2 pour l'ensemble des voitures neuves vendues par chaque constructeur. Avec un objectif de 100 %, seuls les véhicules sans émission à l'échappement pouvaient être vendus neufs.",
 sources=[OEIL_2035, CE_2035, JA_2035, LCP_2035],
 faits=[
  fait("Selon le Parlement européen, le règlement (UE) 2023/851 prévoit une réduction de 100 % des émissions de CO2 pour les voitures et camionnettes neuves à partir de 2035.", 'oeil_2035', '2023', 'Union européenne', "La règle concerne les voitures neuves, pas celles qui roulent déjà.", 'etabli', '100 %'),
  fait("Selon le même texte, la Commission doit proposer l'immatriculation, après 2035, des véhicules roulant exclusivement aux carburants neutres en CO2, et réévaluer l'objectif en 2026.", 'oeil_2035', '2023', 'Union européenne', "Des exceptions et une clause de révision étaient prévues dès le départ.", 'etabli'),
  fait("Selon la Commission européenne, sa proposition de décembre 2025 fixe un objectif de 90 % à partir de 2035, les 10 % restants étant compensés par de l'acier bas carbone, des carburants de synthèse ou des biocarburants : hybrides et moteurs thermiques pourraient encore être vendus.", 'ce_2035', '2025-2026', 'Union européenne', "La fin des ventes de thermiques neufs n'est plus totale dans la proposition.", 'etabli', '90 %'),
  fait("Selon le Journal de l'Automobile, la commission de l'environnement du Parlement européen a voté le 4 novembre 2026 un objectif de -87,5 % en 2035 ; le vote en plénière et l'accord du Conseil restent à venir.", 'ja_2035', '2026', 'Union européenne', "Le texte est en cours de révision.", 'etabli', '-87,5 %'),
  fait("Selon LCP, en février 2025, les députés ont supprimé par 34 voix contre 30 l'article transposant l'échéance de 2035, mais cette date s'impose à la France en vertu du droit européen.", 'lcp_2035', '2025', 'France', "Le vote de l'Assemblée était symbolique.", 'etabli'),
 ],
 court="Trompeur : la règle de 2023 vise les voitures neuves, pas celles qui roulent ni l'occasion, et prévoit des exceptions. Surtout, elle est en cours de révision : la Commission propose depuis fin 2025 un objectif de 90 %, qui laisserait vendre des hybrides et des thermiques après 2035.",
 moyen="Le règlement européen de 2023 prévoit qu'à partir de 2035, les voitures neuves vendues n'émettent plus de CO2 à l'échappement. Il ne touche ni les voitures qui roulent déjà ni le marché de l'occasion : personne ne devra jeter sa voiture en 2035.\n\nEt la règle évolue : fin 2025, la Commission a proposé de passer à 90 % de réduction, ce qui permettrait encore de vendre des hybrides et des moteurs thermiques. En novembre 2026, le Parlement européen discute d'un objectif de -87,5 %. On peut débattre du rythme, mais dire que l'Europe interdit les thermiques, c'est déjà dépassé.",
 detaille="Le règlement (UE) 2023/851, adopté en 2023, fixe pour 2035 une réduction de 100 % des émissions de CO2 des voitures et camionnettes neuves. En pratique, cela revenait à réserver le marché du neuf aux véhicules sans émission à l'échappement. Le texte ne concerne ni le parc existant ni l'occasion ; il prévoyait une exception pour les véhicules roulant exclusivement aux carburants neutres en CO2 et une réévaluation en 2026.\n\nEn décembre 2025, la Commission a proposé de ramener l'objectif à 90 %, les 10 % restants étant compensés par de l'acier bas carbone, des carburants de synthèse ou des biocarburants. Hybrides rechargeables et moteurs thermiques pourraient donc encore être vendus après 2035. Le 4 novembre 2026, la commission de l'environnement du Parlement européen a voté un objectif de -87,5 % ; la plénière et le Conseil doivent encore se prononcer.\n\nLe vrai enjeu social est ailleurs : permettre aux ménages modestes d'accéder à des véhicules propres, développer les transports publics et protéger les emplois de l'automobile pendant la transition.",
 empathie="Je comprends qu'on ait peur de ne plus pouvoir acheter une voiture abordable, ou de devoir changer la sienne. Mais la règle ne concerne que les voitures neuves, pas celle que tu as, et elle est en train d'être assouplie.",
 legitimes=["L'objectif de 100 % adopté en 2023 revenait bien à arrêter la vente de voitures neuves émettant du CO2 à l'échappement.", "Ce règlement reste en vigueur tant que la révision n'est pas adoptée."],
 contre=[
  ("On va devoir mettre nos voitures à la casse.", "Le règlement ne vise que les voitures neuves ; les voitures en circulation et l'occasion ne sont pas concernées."),
  ("C'est Bruxelles qui décide de tout.", "Le texte a été adopté par le Parlement européen et les États membres, et il est en cours de révision par les mêmes institutions."),
 ],
 questions=["Savais-tu que la règle ne concerne que les voitures neuves ?", "As-tu entendu parler de la révision proposée par la Commission fin 2025 ?"],
 limites=["L'état du texte évolue : à la date de la fiche (novembre 2026), la révision n'est pas adoptée.", "Le vote en commission du Parlement européen est rapporté par la presse spécialisée."],
 publics={'convaincus': "Personne ne va venir prendre ta voiture en 2035 : la règle ne concerne que les voitures neuves, pas l'occasion. Et elle est en train d'être assouplie : la Commission propose 90 %, ce qui laisserait vendre des hybrides et des thermiques. La vraie question, c'est comment chacun pourra se payer une voiture propre.",
  'indecis': "La règle de 2035 ne concerne que les voitures neuves et elle est en cours de révision : la Commission propose désormais 90 % de réduction au lieu de 100 %. Le débat porte sur le rythme de la transition et sur les aides pour que les ménages modestes ne soient pas laissés de côté."},
 a_actualiser='2027-03-31',
))

# 19 ── Glyphosate ────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='glyphosate-danger', affirmation="Le glyphosate n'est pas dangereux, les écolos font peur pour rien.", volet='ecologie', sous_theme='Pesticides',
 mots_cles=['glyphosate', 'roundup', 'desherbant', 'herbicide', 'pesticide', 'pesticides', 'cancerogene'],
 verdict='trompeur', fiabilite='debat',
 resume="Trompeur : le danger du glyphosate n'est pas tranché, mais il n'est pas nul. Le Centre international de recherche sur le cancer (OMS) l'a classé en 2015 « cancérogène probable », et l'Inserm retient en 2021 une « présomption moyenne » de lien avec les lymphomes non hodgkiniens. Les agences européennes ne le classent pas cancérogène et ont permis son renouvellement pour dix ans en 2023, mais l'EFSA identifie des lacunes de données et un risque élevé à long terme pour les mammifères dans 12 usages sur 23.",
 contexte="Le renouvellement de l'autorisation européenne du glyphosate en 2023 a relancé le débat ; une partie de la droite et de l'extrême droite accuse les écologistes d'alarmisme.",
 explication="Le CIRC évalue un danger (le produit peut-il causer un cancer ?), les agences réglementaires un risque (en cause-t-il aux niveaux d'exposition réels ?). Les deux approches peuvent aboutir à des conclusions différentes sans que l'une mente.",
 sources=[CIRC_GLY, INSERM_PEST, EFSA_GLY, CE_GLY],
 faits=[
  fait("Selon le CIRC (OMS), le glyphosate est classé en 2015 « probablement cancérogène pour l'homme » (groupe 2A), avec des preuves limitées chez l'humain (lymphome non hodgkinien) et suffisantes chez l'animal.", 'circ_gly', '2015', 'Monde', "Une agence de l'OMS a identifié un danger.", 'etabli'),
  fait("Selon l'Inserm, l'expertise collective de 2021 retient pour le glyphosate « une présomption moyenne de lien avec les lymphomes non hodgkiniens ».", 'inserm_pest', '2021', 'France', "L'institut public français de recherche médicale prend le risque au sérieux.", 'etabli'),
  fait("Selon l'EFSA, l'Agence européenne des produits chimiques a conclu en 2022 que le glyphosate ne remplit pas les critères pour être classé cancérogène, et l'EFSA n'a pas identifié de « domaine critique de préoccupation ».", 'efsa_gly', '2022-2023', 'Union européenne', "Les agences réglementaires européennes sont plus rassurantes : il faut le dire.", 'etabli'),
  fait("Selon l'EFSA, des lacunes de données subsistent, et un risque élevé à long terme pour les mammifères est identifié pour 12 des 23 usages proposés ; aucune conclusion ferme n'est possible sur la biodiversité.", 'efsa_gly', '2023', 'Union européenne', "Même l'évaluation favorable signale des risques environnementaux.", 'etabli', '12 sur 23'),
  fait("Selon la Commission européenne, l'autorisation du glyphosate a été renouvelée pour dix ans en 2023, avec des conditions, dont l'interdiction de l'utiliser comme dessiccant avant la récolte.", 'ce_gly', '2023', 'Union européenne', "Le renouvellement s'accompagne de restrictions, signe que le produit n'est pas anodin.", 'etabli', '10 ans'),
 ],
 court="Trompeur : l'Inserm retient une « présomption moyenne » de lien avec certains cancers, et le CIRC le classe « cancérogène probable ». Les agences européennes sont plus rassurantes, mais signalent des lacunes de données et des risques pour la faune : le débat est réel, la prudence n'est pas une lubie.",
 moyen="Il n'y a pas de consensus pour dire que le glyphosate est inoffensif. Le CIRC, agence de l'OMS, l'a classé « cancérogène probable » en 2015, et l'Inserm retient une « présomption moyenne » de lien avec les lymphomes non hodgkiniens.\n\nC'est vrai, les agences européennes ne le classent pas cancérogène, et l'UE l'a réautorisé pour dix ans. Mais l'EFSA elle-même signale des données manquantes et un risque élevé pour les mammifères dans plus de la moitié des usages. Demander de la prudence, surtout pour les agriculteurs exposés, n'est pas faire peur pour rien.",
 detaille="Le glyphosate est l'herbicide le plus utilisé au monde. En 2015, le Centre international de recherche sur le cancer (OMS) l'a classé « probablement cancérogène pour l'homme », sur la base de preuves limitées chez l'humain, suffisantes chez l'animal et fortes pour la génotoxicité. Ce classement porte sur le danger, pas sur le niveau d'exposition.\n\nEn France, l'expertise collective de l'Inserm (2021) retient une présomption moyenne de lien entre le glyphosate et les lymphomes non hodgkiniens, notamment chez les personnes exposées professionnellement. Au niveau européen, l'ECHA ne le classe pas cancérogène et l'EFSA n'a pas identifié de domaine critique de préoccupation ; elle relève toutefois des lacunes de données et un risque élevé à long terme pour les mammifères dans 12 des 23 usages évalués.\n\nL'Union a renouvelé l'autorisation pour dix ans en 2023, avec des restrictions. De nouvelles études sont en cours d'évaluation depuis 2025. Les agriculteurs, premiers exposés, ont intérêt à ce que le principe de précaution s'applique et à être accompagnés vers des alternatives.",
 empathie="Je comprends qu'un agriculteur se sente accusé quand on parle du glyphosate, alors qu'il en a besoin pour travailler. Mais les premiers exposés, ce sont justement les agriculteurs, et l'Inserm prend ce risque au sérieux.",
 legitimes=["Les agences réglementaires européennes ne classent pas le glyphosate cancérogène et n'ont pas identifié de domaine critique de préoccupation.", "L'Union européenne a renouvelé son autorisation pour dix ans."],
 contre=[
  ("Les agences européennes disent qu'il n'est pas dangereux.", "Elles ne le classent pas cancérogène, mais l'EFSA signale des lacunes de données et des risques pour les mammifères ; l'Inserm et le CIRC concluent différemment."),
  ("Sans glyphosate, l'agriculture s'effondre.", "La question est l'accompagnement des agriculteurs vers des alternatives, pas le déni du risque."),
 ],
 questions=["Savais-tu que l'Inserm retient une présomption de lien avec certains cancers chez les personnes exposées ?", "Qui est le plus exposé au glyphosate, à ton avis ?"],
 limites=["Le classement du CIRC date de 2015 ; de nouvelles données (étude Ramazzini de 2025) sont en cours d'évaluation et ne sont pas tranchées.", "Le débat scientifique est réel : la fiche ne conclut pas à une cancérogénicité avérée."],
 publics={'convaincus': "Ce ne sont pas des écolos qui le disent : c'est l'Inserm, l'institut public de recherche médicale, qui retient une présomption de lien avec certains cancers. Et même l'agence européenne qui l'a réautorisé signale un risque élevé pour les mammifères dans plus de la moitié des usages. Les premiers à payer le prix, ce sont les agriculteurs.",
  'indecis': "Le glyphosate fait l'objet d'un vrai débat scientifique : certaines institutions le jugent probablement cancérogène, d'autres non. Dans ce cas, la prudence est raisonnable, surtout pour les agriculteurs exposés. Il ne s'agit pas d'accuser ceux qui l'utilisent, mais de les aider à s'en passer."},
 a_actualiser='2027-06-30',
))

# 20 ── Mosquées et financement étranger ──────────────────────────────────────
FICHES.append(fiche(
 id='mosquees-financement-etranger', affirmation="Les mosquées en France sont financées par l'étranger.", volet='droits', sous_theme='Laïcité',
 mots_cles=['mosquees', 'mosquee', 'financement etranger', 'financees par l etranger', 'qatar', 'arabie saoudite', 'imams detaches', 'financement des mosquees', 'islam financement'],
 verdict='trompeur', fiabilite='etabli',
 resume="Généralisation abusive : selon le rapport du Sénat de 2016, le culte musulman est « essentiellement financé, comme les autres cultes, par les fidèles eux-mêmes ». Des financements d'États étrangers existaient (environ 6 M€ du Maroc en 2016, 2 M€ de l'Algérie, 3,8 M€ de l'Arabie saoudite depuis 2011) et 301 imams étaient détachés par des pays étrangers pour environ 2 500 lieux de culte. Depuis la loi de 2021, les financements étrangers de plus de 15 300 € doivent être déclarés, et les nouveaux imams détachés sont interdits depuis 2024.",
 contexte="Le financement étranger des mosquées revient régulièrement dans les débats sur l'islam en France, souvent pour suggérer une influence étrangère généralisée sur les musulmans français.",
 explication="Comme les églises et les synagogues, les mosquées sont surtout financées par les dons des fidèles. L'influence étrangère passait surtout par des subventions d'États à quelques grandes institutions et par des imams envoyés par des pays d'origine.",
 sources=[SENAT_ISLAM16, LOCALTIS_ISLAM, SP_CULTE, MEE_IMAMS],
 faits=[
  fait("Selon le Sénat (2016), le culte musulman « serait essentiellement financé, comme les autres cultes, par les fidèles eux-mêmes ».", 'senat_islam16', '2016', 'France', "La grande majorité de l'argent vient des musulmans de France.", 'etabli'),
  fait("Selon le Sénat, les financements d'États étrangers étaient de l'ordre de quelques millions d'euros par an : environ 6 M€ du Maroc en 2016, 2 M€ de l'Algérie pour la Grande Mosquée de Paris, 3,8 M€ de l'Arabie saoudite depuis 2011.", 'senat_islam16', '2011-2016', 'France', "Les financements étrangers étaient réels mais limités.", 'etabli', '6 M€'),
  fait("Selon le rapport sénatorial, 301 imams étaient détachés par des pays étrangers pour environ 2 500 lieux de culte, et seuls 20 à 30 % des imams seraient de nationalité française.", 'localtis_islam', '2016', 'France', "L'influence étrangère passait surtout par les imams.", 'etabli', '301'),
  fait("Selon Service-public.fr, depuis la loi du 24 août 2021, les associations cultuelles doivent déclarer les ressources venant de l'étranger supérieures à 15 300 € par an, et le ministre de l'Intérieur peut s'y opposer en cas de menace grave.", 'sp_culte', '2021-2025', 'France', "L'État contrôle désormais ces financements.", 'etabli', '15 300 €'),
  fait("Selon Middle East Eye, le ministre de l'Intérieur a interdit les nouveaux imams détachés à partir du 1er janvier 2024 ; selon le CFCM, ils ne représentaient que 8 % des imams.", 'mee_imams', '2024', 'France', "Le système des imams envoyés par des États étrangers a pris fin.", 'etabli', '8 %'),
 ],
 court="Trompeur : selon le Sénat, les mosquées sont « essentiellement » financées par les fidèles, comme les autres cultes. Des financements d'États étrangers existaient, de l'ordre de quelques millions par an, mais ils sont contrôlés depuis 2021 et les imams détachés sont interdits depuis 2024.",
 moyen="Le Sénat a enquêté en 2016 : l'islam en France est « essentiellement financé, comme les autres cultes, par les fidèles eux-mêmes ». Il y avait aussi des financements d'États étrangers, de l'ordre de quelques millions d'euros par an (Maroc, Algérie, Arabie saoudite), et environ 300 imams envoyés par des pays étrangers.\n\nDepuis, les règles ont changé : la loi de 2021 oblige à déclarer tout financement étranger de plus de 15 300 € par an, et les nouveaux imams détachés sont interdits depuis 2024. Dire que les mosquées sont financées par l'étranger, c'est présenter les musulmans français comme des agents de l'étranger, alors qu'ils paient leurs lieux de culte eux-mêmes.",
 detaille="La mission d'information du Sénat de 2016, transpartisane, a conclu que le culte musulman était essentiellement financé par les fidèles, comme les autres cultes. Elle a chiffré les financements d'États étrangers : environ 6 millions d'euros du Maroc en 2016, 2 millions de l'Algérie pour la Grande Mosquée de Paris, 3,8 millions de l'Arabie saoudite depuis 2011, et une contribution indirecte de la Turquie via la rémunération d'imams. Elle comptait 301 imams détachés pour environ 2 500 lieux de culte, et reconnaissait qu'il est « impossible de connaître les financements par des personnes privées étrangères ».\n\nDepuis, la loi du 24 août 2021 impose aux associations cultuelles de déclarer les ressources étrangères de plus de 15 300 € par an, et le ministre de l'Intérieur peut s'y opposer en cas de menace grave. Les nouveaux imams détachés sont interdits depuis janvier 2024 ; selon le CFCM, ils représentaient 8 % des imams.\n\nL'influence d'États étrangers sur certaines institutions musulmanes est un sujet légitime. Mais elle ne concerne qu'une petite part du financement, et la laïcité suppose de traiter tous les cultes de la même façon, sans soupçonner une religion entière.",
 empathie="Je comprends qu'on s'inquiète de l'influence de pays étrangers sur l'islam en France. C'est un sujet sérieux, et le Sénat l'a étudié. Mais il a conclu que les mosquées sont surtout payées par les fidèles, comme les églises.",
 legitimes=["Des financements d'États étrangers et des imams détachés ont existé et ont été documentés par le Sénat.", "Une partie des financements privés étrangers reste inconnue."],
 contre=[
  ("Le Qatar et l'Arabie saoudite financent tout.", "Le Sénat chiffrait les financements saoudiens à 3,8 M€ depuis 2011 et concluait que les fidèles financent l'essentiel."),
  ("L'État ne contrôle rien.", "Depuis 2021, tout financement étranger de plus de 15 300 € doit être déclaré et peut être bloqué par le ministre de l'Intérieur."),
 ],
 questions=["Qui finance, selon toi, la construction d'une église ou d'une synagogue en France ?", "Savais-tu que les imams envoyés par des États étrangers sont interdits depuis 2024 ?"],
 limites=["Les chiffres de financement datent de 2016 ; aucun bilan officiel des déclarations depuis 2021 n'a été trouvé dans les sources lues.", "La part des financements privés étrangers n'est pas connue."],
 publics={'convaincus': "Le Sénat, pas une association, a enquêté : les mosquées sont « essentiellement » financées par les fidèles, comme les églises. Les États étrangers donnaient quelques millions par an, et depuis 2021 chaque don de plus de 15 300 € doit être déclaré. Les imams envoyés par l'étranger sont interdits depuis 2024.",
  'indecis': "L'influence étrangère sur l'islam de France a existé et a été documentée, surtout par les imams détachés et quelques subventions. Mais l'essentiel du financement vient des fidèles, et l'État contrôle désormais les dons étrangers. On peut être vigilant sans soupçonner tous les musulmans."},
 a_actualiser='2027-06-30',
))

# 21 ── Déboutés de l'asile ───────────────────────────────────────────────────
FICHES.append(fiche(
 id='deboutes-asile-restent', affirmation="Les déboutés du droit d'asile restent presque tous en France.", volet='immigration', sous_theme='Immigration et asile',
 mots_cles=['deboutes', 'deboute', 'deboutes du droit d asile', 'demandeurs d asile deboutes', 'restent en france', '96 %', 'rejet de l asile', 'asile rejete'],
 verdict='plutot_exact', fiabilite='estimation',
 resume="En grande partie vrai : selon le Sénat (2026), les éloignements de déboutés de l'asile ne dépassent guère 3 000 par an entre 2019 et 2025, et seules 3 à 8 % de leurs OQTF sont exécutées, pour environ 60 000 à 70 000 rejets définitifs par an. Mais « rester » ne veut pas dire rester sans papiers : près d'un quart des demandeurs d'asile obtiennent ensuite un titre de séjour pour un autre motif, et les départs volontaires ne sont pas comptés. Le chiffre de « 96 % » qui circule date de 2014.",
 contexte="Le faible taux d'éloignement des déboutés est un argument central pour durcir le droit d'asile ; il est repris aussi bien par la droite que par l'extrême droite.",
 explication="Un débouté est une personne dont la demande d'asile a été définitivement rejetée. Elle reçoit en général une obligation de quitter le territoire (OQTF). Elle peut partir d'elle-même sans être comptée, être éloignée, rester en situation irrégulière ou obtenir plus tard un autre titre (travail, famille).",
 sources=[SENAT_ASILE26, CDC_IRREG, AP_ASILE15],
 faits=[
  fait("Selon le Sénat, les éloignements de déboutés de l'asile après une OQTF ne dépassent guère 3 000 par an entre 2019 et 2025, et le taux d'exécution de ces OQTF est de 3 à 8 % (5,5 % en moyenne), contre 10 % pour l'ensemble des étrangers.", 'senat_asile26', '2019-2025', 'France', "L'éloignement effectif des déboutés est très faible : c'est un fait.", 'estimation', '5,5 %'),
  fait("Selon la Cour des comptes, environ 60 000 à 70 000 demandes d'asile sont définitivement rejetées chaque année depuis 2016, et environ 10 % des OQTF sont exécutées.", 'cdc_irreg', '2016-2022', 'France', "La grande majorité des déboutés ne sont pas éloignés par l'État.", 'etabli', '60 000 à 70 000'),
  fait("Selon le Sénat, près d'un quart des demandeurs d'asile sont finalement admis au séjour pour un autre motif, deux à cinq ans après le rejet, surtout pour raisons familiales ou de travail.", 'senat_asile26', '2026', 'France', "Une partie de ceux qui « restent » sont en situation régulière.", 'estimation', 'un quart'),
  fait("Selon le Sénat, la direction générale des étrangers en France a fourni des « données incohérentes et contradictoires » sur ces éloignements.", 'senat_asile26', '2026', 'France', "Le chiffre exact de déboutés encore présents n'est pas connu.", 'etabli'),
  fait("Selon Acteurs publics, la Cour des comptes estimait en 2015 que plus de 96 % des déboutés resteraient en France, à partir de 1 432 éloignements pour 40 206 déboutés en 2014 ; le gouvernement objectait que la Cour ne comptait ni les titres accordés ensuite ni les départs volontaires.", 'ap_asile15', '2014', 'France', "Le chiffre de 96 % est ancien et contesté dans son interprétation.", 'estimation', '96 %'),
 ],
 court="En grande partie vrai : seules 3 à 8 % des OQTF visant des déboutés sont exécutées, soit environ 3 000 éloignements par an. Mais près d'un quart des demandeurs obtiennent ensuite un titre pour un autre motif, et les départs volontaires ne sont pas comptés : on ne sait pas combien restent sans papiers.",
 moyen="C'est vrai que l'État éloigne très peu de déboutés : selon le Sénat, environ 3 000 par an, avec un taux d'exécution des OQTF de 3 à 8 %, pour 60 000 à 70 000 rejets par an.\n\nMais « rester » ne veut pas dire « rester sans papiers » : près d'un quart des demandeurs obtiennent ensuite un titre de séjour, souvent parce qu'ils travaillent ou ont fondé une famille. Les départs volontaires ne sont pas comptés, et le Sénat juge les données de l'administration « incohérentes ». Le chiffre de 96 % date de 2014. Le constat d'échec est réel ; la solution ne se résume pas à expulser plus.",
 detaille="Chaque année depuis 2016, environ 60 000 à 70 000 demandes d'asile sont définitivement rejetées, selon la Cour des comptes. Les déboutés reçoivent en principe une obligation de quitter le territoire. Selon le rapport du Sénat de juillet 2026, les éloignements de déboutés ne dépassent guère 3 000 par an entre 2019 et 2025, et le taux d'exécution de leurs OQTF est de 3 à 8 %, contre environ 10 % pour l'ensemble des étrangers.\n\nCela ne signifie pas que tous restent en situation irrégulière. Le Sénat indique que près d'un quart des demandeurs d'asile obtiennent ensuite un titre pour un autre motif, deux à cinq ans après le rejet. Les départs volontaires non accompagnés ne sont pas mesurés, et les données de l'administration sont jugées incohérentes. Le chiffre de « 96 % » souvent cité vient d'un rapport de la Cour des comptes de 2015 sur des données de 2014.\n\nLe constat est réel : la procédure aboutit pour beaucoup à des années de précarité, sans droits, souvent dans le travail non déclaré. Des procédures plus rapides, un accompagnement au retour et des voies de régularisation pour ceux qui travaillent et vivent ici depuis longtemps répondent mieux à ce constat que la promesse d'expulsions massives jamais tenue.",
 empathie="Je comprends qu'on trouve absurde qu'une décision de justice ne soit presque jamais appliquée. Le constat est juste. Mais beaucoup de ceux qui restent finissent par être régularisés parce qu'ils travaillent ou ont une famille ici.",
 legitimes=["Le taux d'éloignement des déboutés est réellement très faible (environ 5,5 % des OQTF exécutées).", "Les données de l'administration sont lacunaires, ce qui empêche un pilotage sérieux."],
 contre=[
  ("96 % des déboutés restent, c'est la Cour des comptes qui le dit.", "Ce chiffre porte sur 2014 et ne compte ni les départs volontaires ni les titres accordés ensuite."),
  ("Il suffit d'expulser tous les déboutés.", "Aucun gouvernement n'y est parvenu : l'exécution des OQTF reste autour de 10 % pour l'ensemble des étrangers selon la Cour des comptes, et encore plus faible pour les déboutés."),
 ],
 questions=["Sais-tu quelle part des demandeurs d'asile obtiennent ensuite un titre de séjour pour un autre motif ?", "Que faire de quelqu'un qui travaille ici depuis cinq ans mais a été débouté ?"],
 limites=["Les chiffres reposent sur des données de l'administration jugées incohérentes par le Sénat ; le nombre exact de déboutés encore présents n'est pas connu.", "Le chiffre de 96 % date de 2014 ; le rapport de la Cour des comptes de 2024 exclut l'asile de son champ."],
 publics={'convaincus': "Tu as raison sur le constat : l'État exécute très peu d'OQTF de déboutés, environ 3 000 par an. Mais les promesses d'expulsions massives n'ont jamais été tenues, par aucun gouvernement. Et un quart des demandeurs finissent régularisés, souvent parce qu'ils travaillent dans des métiers dont on a besoin.",
  'indecis': "Il est vrai que la plupart des déboutés de l'asile ne sont pas éloignés. Mais ils ne restent pas tous sans papiers : environ un quart obtiennent plus tard un titre, et les départs volontaires ne sont pas comptés. Le vrai problème est une procédure longue qui laisse des gens des années sans droits."},
 a_actualiser='2027-06-30',
))

# 22 ── Logements sociaux ─────────────────────────────────────────────────────
FICHES.append(fiche(
 id='logements-sociaux-immigres', affirmation="Les logements sociaux sont attribués en priorité aux immigrés.", volet='immigration', sous_theme='Logement',
 mots_cles=['logements sociaux', 'logement social', 'hlm', 'attribution des logements', 'priorite aux immigres', 'logements aux etrangers', 'hlm aux immigres', 'hlm aux etrangers', 'passent devant'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux : la loi ne prévoit aucune priorité liée à la nationalité ou à l'origine. Les priorités sont sociales : ménages reconnus au titre du droit au logement opposable (DALO), personnes handicapées, mal logées, sans logement, victimes de violences. Les immigrés sont plus souvent locataires HLM (35 % contre 11 % des personnes sans ascendance migratoire), ce que l'Insee explique surtout par des revenus plus faibles et un âge plus jeune. À caractéristiques égales, les ménages non européens attendent même plus longtemps.",
 contexte="Marine Le Pen a proposé en 2026 de réserver les logements HLM aux Français ; l'idée que les immigrés « passent devant » est ancienne.",
 explication="Pour obtenir un HLM, il faut résider régulièrement en France et avoir des revenus sous un plafond (72 % des ménages sont éligibles). Les commissions attribuent ensuite selon l'urgence sociale. Les ménages pauvres, mal logés ou suroccupés, parmi lesquels les immigrés sont surreprésentés, sont donc plus souvent prioritaires.",
 sources=[MTE_HLM, INSEE_LOGIMM, UT1_HLM, LCP_HLM],
 faits=[
  fait("Selon le ministère du Logement, les attributions vont d'abord aux ménages reconnus prioritaires au titre du DALO, puis aux publics définis par la loi : personnes handicapées, mal logées, hébergées, victimes de violences conjugales, sans logement ou menacées d'expulsion ; aucun critère de nationalité ou d'origine n'est prévu.", 'mte_hlm', '2024', 'France', "Les priorités sont sociales, pas ethniques.", 'etabli'),
  fait("Selon le ministère, 72 % des ménages sont éligibles au logement social, à condition de résider régulièrement et durablement en France.", 'mte_hlm', '2024', 'France', "Le logement social s'adresse à la grande majorité des ménages, Français compris.", 'etabli', '72 %'),
  fait("Selon l'Insee, 35 % des immigrés de 18 à 59 ans vivent en logement social, contre 11 % des personnes sans ascendance migratoire ; cette surreprésentation est « largement liée aux moindres revenus et à l'âge plus jeune des immigrés ».", 'insee_logimm', '2019-2020', 'France', "Les immigrés sont plus souvent en HLM parce qu'ils sont plus souvent pauvres.", 'etabli', '35 %'),
  fait("Selon l'Insee, 26 % des immigrés vivent dans un logement suroccupé, contre 8 % des personnes sans ascendance migratoire.", 'insee_logimm', '2019-2020', 'France', "Ils sont aussi plus souvent mal logés, un critère de priorité.", 'etabli', '26 %'),
  fait("Selon une étude publiée dans la revue de l'Insee, à caractéristiques égales, les ménages non européens attendent plus longtemps un logement social, et une part importante de cet écart peut être due à des discriminations.", 'ut1_hlm', '2006', 'France', "Loin d'être favorisés, ils sont plutôt désavantagés à situation égale.", 'estimation'),
  fait("Selon l'Union sociale pour l'habitat citée par LCP, les étrangers représentent 15 % des locataires du parc social ; sa présidente affirme qu'ils « ne sont pas favorisés dans l'entrée dans le logement social ».", 'lcp_hlm', '2026', 'France', "Les bailleurs sociaux démentent toute priorité.", 'etabli', '15 %'),
 ],
 court="Faux : la loi ne prévoit aucune priorité liée à l'origine ; les priorités sont sociales (DALO, handicap, mal-logement, violences). Les immigrés sont plus souvent en HLM parce qu'ils sont plus souvent pauvres, et à situation égale ils attendent même plus longtemps.",
 moyen="Il n'existe aucune priorité pour les immigrés dans la loi. Les HLM vont d'abord aux personnes reconnues au titre du droit au logement opposable, puis aux personnes handicapées, sans logement, mal logées ou victimes de violences, quelle que soit leur origine.\n\nC'est vrai que les immigrés sont plus souvent en HLM (35 % contre 11 %). Mais l'Insee explique pourquoi : ils ont en moyenne des revenus plus faibles et sont plus jeunes. Et à situation égale, une étude montre que les ménages non européens attendent plus longtemps. Le vrai problème, c'est qu'on ne construit pas assez de logements sociaux pour tous ceux qui y ont droit.",
 detaille="Selon le ministère du Logement, 72 % des ménages sont éligibles au logement social, à condition de résider régulièrement et durablement en France et d'avoir des revenus sous un plafond. Les attributions vont d'abord aux ménages reconnus prioritaires au titre du droit au logement opposable, puis aux publics définis par le code de la construction : personnes handicapées, mal logées, hébergées, victimes de violences conjugales, sans logement ou menacées d'expulsion, jeunes sortant de l'aide sociale à l'enfance. Aucun critère de nationalité ou d'origine n'existe.\n\nSelon l'enquête Trajectoires et Origines de l'Ined et de l'Insee, 35 % des immigrés de 18 à 59 ans vivent en logement social, contre 11 % des personnes sans ascendance migratoire ; l'Insee l'explique surtout par des revenus plus faibles et un âge plus jeune. Ils vivent aussi trois fois plus souvent dans un logement suroccupé. Selon l'Union sociale pour l'habitat, les étrangers représentent 15 % des locataires HLM.\n\nUne étude publiée dans la revue de l'Insee montre qu'à caractéristiques égales, les ménages non européens attendent plus longtemps un logement social, en partie à cause de discriminations. Opposer Français et immigrés détourne du vrai problème : le manque de logements sociaux pour tous les ménages modestes.",
 empathie="Je comprends la colère de quelqu'un qui attend un HLM depuis des années et qui voit d'autres l'obtenir avant lui. Cette attente est injuste. Mais elle vient du manque de logements, pas d'une priorité donnée aux immigrés, qui n'existe pas dans la loi.",
 legitimes=["Les immigrés sont surreprésentés dans le logement social (35 % contre 11 %).", "Les délais d'attente sont très longs, et le sentiment d'injustice des demandeurs est réel."],
 contre=[
  ("J'en connais qui ont eu un HLM tout de suite en arrivant.", "Il faut résider régulièrement et durablement en France ; les priorités dépendent de l'urgence sociale, pas de l'origine."),
  ("Il faut réserver les HLM aux Français.", "Cela ne créerait aucun logement de plus et se heurterait au principe d'égalité ; le problème est le nombre de logements disponibles."),
 ],
 questions=["Sais-tu quels sont les critères de priorité pour obtenir un HLM ?", "Si les immigrés sont plus souvent pauvres, est-il étonnant qu'ils soient plus souvent en HLM ?"],
 limites=["Les données de l'Insee portent sur 2019-2020 ; l'étude sur les délais d'attente repose sur l'enquête Logement de 2006.", "Le texte de l'article L. 441-1 n'a pas pu être lu sur Légifrance ; la liste des publics prioritaires vient du document du ministère."],
 publics={'convaincus': "Cherche dans la loi : il n'y a aucune priorité pour les immigrés. Les HLM vont aux plus mal logés, aux personnes handicapées, aux victimes de violences, quelle que soit leur origine. Et une étude montre qu'à situation égale, les ménages non européens attendent même plus longtemps. Si tu attends un logement, ton problème, c'est qu'on n'en construit pas assez.",
  'indecis': "Les immigrés sont plus souvent en HLM, c'est vrai, mais parce qu'ils sont plus souvent pauvres et mal logés, selon l'Insee. La loi n'accorde aucune priorité selon l'origine. La longue attente que connaissent beaucoup de familles vient d'abord du manque de logements sociaux."},
 a_actualiser='2027-06-30',
))

# 23 ── Médecins diplômés à l'étranger ────────────────────────────────────────
FICHES.append(fiche(
 id='medecins-diplome-etranger', affirmation="Les médecins étrangers sont moins compétents que les médecins français.", volet='services', sous_theme='Médecins et déserts médicaux',
 mots_cles=['medecins etrangers', 'medecin etranger', 'padhue', 'diplome etranger', 'diplomes hors union europeenne', 'medecins diplomes a l etranger', 'medecins algeriens', 'medecins africains'],
 verdict='trompeur', fiabilite='etabli',
 resume="Généralisation non étayée : un médecin diplômé hors de l'Union européenne ne peut exercer pleinement en France qu'après un concours sélectif (épreuves de vérification des connaissances), une preuve de maîtrise du français, deux ans de consolidation des compétences et une validation par une commission nationale de spécialité. Ces praticiens représentent environ 8 % des médecins en activité, surtout à l'hôpital. Aucune source ne mesure en France une compétence moindre ; aux États-Unis, une grande étude a même trouvé une mortalité légèrement plus basse chez leurs patients.",
 contexte="Le recours aux praticiens à diplôme hors Union européenne (PADHUE) dans les hôpitaux suscite des remarques sur leur niveau, alors que l'Académie de médecine demande de renforcer leur évaluation.",
 explication="« Médecins étrangers » mélange plusieurs situations : diplômés de l'Union européenne (reconnus automatiquement), diplômés hors Union (soumis à des épreuves), et médecins de nationalité étrangère formés en France. Les contrôles visent justement à garantir le niveau de ceux qui ont étudié hors d'Europe.",
 sources=[SENAT_PADHUE, ANM_PADHUE, SM_PADHUE, BMJ_IMG],
 faits=[
  fait("Selon le ministère de la Santé, les PADHUE passent des épreuves de vérification des connaissances organisées comme un concours, puis un parcours de consolidation des compétences de deux ans ; 3 873 ont réussi le concours en 2024 pour 4 000 postes.", 'senat_padhue', '2024-2026', 'France', "L'accès au plein exercice est sélectif et encadré.", 'etabli', '3 873'),
  fait("Selon l'Académie nationale de médecine, les candidats doivent aussi prouver leur maîtrise du français et voir leurs compétences validées par une commission nationale pour chaque spécialité.", 'anm_padhue', '2026', 'France', "Plusieurs filtres successifs vérifient le niveau.", 'etabli'),
  fait("Selon les données de l'Ordre des médecins, 15 972 anciens PADHUE sont en activité régulière au 1er janvier 2025, soit 8 % des médecins ; 52,7 % exercent à l'hôpital, et ils représentent 14,1 % des pédiatres.", 'sm_padhue', '2025', 'France', "Ils tiennent une part importante de l'hôpital public.", 'etabli', '8 %'),
  fait("Selon une étude de Harvard publiée dans le BMJ, sur 1,2 million d'hospitalisations aux États-Unis, la mortalité à 30 jours des patients était de 11,2 % avec des médecins diplômés à l'étranger, contre 11,6 % avec des diplômés américains.", 'bmj_img', '2011-2014', 'États-Unis', "Là où on l'a mesuré, les médecins formés à l'étranger soignent aussi bien.", 'etabli', '11,2 % contre 11,6 %'),
  fait("Selon l'Académie de médecine, l'évaluation des PADHUE devrait être renforcée (écrit anonyme, niveau de français plus exigeant, simulation des gestes techniques).", 'anm_padhue', '2026', 'France', "Le système est perfectible : la question du niveau mérite d'être posée sérieusement.", 'etabli'),
 ],
 court="Trompeur : un médecin diplômé hors d'Europe doit réussir un concours, prouver son français, faire deux ans de consolidation et être validé par une commission de spécialité. Aucune étude française ne montre qu'ils soignent moins bien, et une grande étude américaine trouve même une mortalité légèrement plus basse chez leurs patients.",
 moyen="Un médecin diplômé hors de l'Union européenne ne s'installe pas comme ça. Il doit réussir un concours sélectif, prouver qu'il maîtrise le français, passer deux ans de consolidation à l'hôpital et être validé par une commission nationale de sa spécialité.\n\nIls sont environ 16 000 en activité, 8 % des médecins, et 14 % des pédiatres : sans eux, beaucoup d'hôpitaux fermeraient des services. Aucune étude française ne montre qu'ils soignent moins bien ; aux États-Unis, une étude sur 1,2 million d'hospitalisations trouve même une mortalité un peu plus faible chez leurs patients.",
 detaille="Les praticiens à diplôme hors Union européenne (PADHUE) doivent, pour obtenir le plein exercice, réussir des épreuves de vérification des connaissances organisées comme un concours, prouver leur maîtrise du français, accomplir un parcours de consolidation des compétences de deux ans, puis être validés par une commission nationale de leur spécialité. En 2024, 3 873 ont réussi le concours pour 4 000 postes ; une voie interne, plus légère, existe depuis 2025 pour ceux qui exercent déjà à l'hôpital.\n\nSelon l'Ordre des médecins, environ 16 000 anciens PADHUE sont en activité régulière, soit 8 % des médecins ; plus de la moitié travaillent à l'hôpital, et ils représentent 14,1 % des pédiatres et 10,7 % des gynécologues. Le ministère souligne qu'ils participent à la continuité des soins.\n\nAucune source lue ne mesure en France une compétence moindre. Aux États-Unis, une étude de Harvard sur plus d'un million d'hospitalisations a trouvé une mortalité à 30 jours de 11,2 % avec des médecins diplômés à l'étranger, contre 11,6 % avec des diplômés américains. L'Académie de médecine demande toutefois de renforcer l'évaluation : on peut exiger un haut niveau pour tous sans jeter le soupçon sur ceux qui font tourner l'hôpital.",
 empathie="Je comprends qu'on veuille être soigné par quelqu'un dont on est sûr du niveau, et qu'on s'inquiète quand on comprend mal un médecin. C'est légitime. Mais ces médecins passent un concours et plusieurs contrôles, et rien ne montre qu'ils soignent moins bien.",
 legitimes=["Les formations hors Union européenne sont de niveau inégal, ce qui justifie les épreuves de vérification.", "L'Académie de médecine juge l'évaluation perfectible, et la nouvelle voie interne allège l'épreuve."],
 contre=[
  ("Ils ne parlent même pas bien français.", "Une preuve de maîtrise du français est exigée ; l'Académie de médecine demande de relever ce niveau."),
  ("Il faudrait former plus de médecins français plutôt.", "C'est souhaitable, mais il faut dix ans pour former un médecin ; en attendant, ces praticiens tiennent des services entiers."),
 ],
 questions=["Sais-tu quelles épreuves doit passer un médecin diplômé hors d'Europe pour exercer en France ?", "Qui, dans ton hôpital le plus proche, assure les gardes de nuit ?"],
 limites=["Aucune étude française comparant la qualité des soins selon le pays de diplôme n'a été trouvée ; l'étude citée est américaine et ne se transpose pas directement.", "Les données de l'Ordre sont reprises par un média professionnel ; l'Atlas 2025 de l'Ordre n'a pas pu être lu sur ce point."],
 publics={'convaincus': "Un médecin diplômé hors d'Europe passe un concours, prouve son français, fait deux ans de consolidation et doit être validé par une commission de sa spécialité. Ils sont 8 % des médecins et 14 % des pédiatres : sans eux, des urgences fermeraient. Et là où on a mesuré, aux États-Unis, leurs patients ne meurent pas plus, plutôt un peu moins.",
  'indecis': "Ta question sur le niveau est légitime, et l'Académie de médecine veut d'ailleurs renforcer les contrôles. Mais ces médecins passent déjà plusieurs épreuves, et aucune étude ne montre qu'ils soignent moins bien. Ils sont aujourd'hui indispensables à de nombreux hôpitaux."},
 a_actualiser='2027-06-30',
))

# 24 ── Mercosur ──────────────────────────────────────────────────────────────
FICHES.append(fiche(
 id='mercosur-agriculteurs', affirmation="L'accord avec le Mercosur va tuer nos agriculteurs et le RN est le seul à s'y opposer.", volet='ecologie', sous_theme='Agriculture',
 mots_cles=['mercosur', 'accord ue mercosur', 'accord avec le mercosur', 'libre echange', 'boeuf bresilien', 'viande argentine', 'accord commercial'],
 verdict='trompeur', fiabilite='etabli',
 resume="Double erreur : le RN n'est pas seul, puisque l'Assemblée s'est opposée à l'accord par 484 voix contre 70 en novembre 2024, que LFI, les écologistes et les communistes refusent l'accord, et que le gouvernement français s'y est opposé au Conseil européen. Sur le fond, l'élevage bovin et la volaille sont bien exposés, avec des quotas de 99 000 tonnes de bœuf et 180 000 tonnes de volaille, mais les études citées estiment l'effet à environ -0,6 % de revenu pour les éleveurs bovins européens. L'accord s'applique provisoirement depuis le 1er mai 2026.",
 contexte="L'accord entre l'Union européenne et le Mercosur (Brésil, Argentine, Uruguay, Paraguay) a été signé en janvier 2026 malgré l'opposition de la France, et le Parlement européen a saisi la Cour de justice.",
 explication="Un accord de libre-échange baisse les droits de douane dans les deux sens. Pour l'agriculture, il ouvre des quotas d'importation à droits réduits ; les critiques portent sur la concurrence de produits obtenus avec des normes différentes et sur l'impact climatique.",
 sources=[LCP_MERCOSUR, CDJ_MERCOSUR, CE_MERCOSUR, PS_MERCOSUR, DELORS_MERCOSUR],
 faits=[
  fait("Selon LCP, l'Assemblée nationale a soutenu la position du gouvernement hostile à l'accord par 484 voix contre 70 en novembre 2024 ; les députés LFI ont voté contre la déclaration parce qu'ils refusent l'accord sans condition, et les écologistes et communistes ont aussi exprimé leur opposition.", 'lcp_mercosur', '2024', 'France', "Presque toute la classe politique française s'oppose à l'accord.", 'etabli', '484 contre 70'),
  fait("Selon le Club des juristes, le Conseil a autorisé la signature le 9 janvier 2026 malgré l'opposition de la France, et le Parlement européen a saisi la Cour de justice de l'UE le 21 janvier 2026 par 334 voix contre 324.", 'cdj_mercosur', '2026', 'Union européenne', "Le gouvernement français lui-même a voté contre.", 'etabli', '334 contre 324'),
  fait("Selon la Commission européenne, les quotas sont de 99 000 tonnes de viande bovine à 7,5 % de droits, soit 1,6 % de la production européenne, et de 180 000 tonnes de volaille (1,4 %), avec une clause de sauvegarde.", 'ce_mercosur', '2026', 'Union européenne', "Les volumes sont limités, mais concentrés sur des filières fragiles.", 'etabli', '99 000 t'),
  fait("Selon Public Sénat, le droit de douane sur le bœuf passe d'environ 40 % à 7,5 % dans le quota, tandis que les vins, voitures et fromages européens gagnent des débouchés.", 'ps_mercosur', '2024', 'Union européenne', "Il y a des gagnants et des perdants, et l'élevage est du côté des perdants.", 'etabli', '7,5 %'),
  fait("Selon l'Institut Jacques Delors, l'étude Gohin et Matthews estime la perte de revenu des éleveurs bovins de l'UE à 0,6 %, et l'accord s'applique provisoirement depuis le 1er mai 2026.", 'delors_mercosur', '2026', 'Union européenne', "L'effet moyen estimé est modéré, ce qui n'exclut pas des pertes locales.", 'estimation', '-0,6 %'),
 ],
 court="Trompeur : le RN n'est pas seul, puisque l'Assemblée a rejeté l'accord par 484 voix contre 70, que LFI, les écologistes et les communistes le refusent et que le gouvernement a voté contre à Bruxelles. L'élevage est bien exposé, mais les études citées estiment l'effet à environ -0,6 % de revenu pour les éleveurs bovins.",
 moyen="Le RN n'est pas seul contre le Mercosur : en novembre 2024, l'Assemblée a soutenu la position hostile du gouvernement par 484 voix contre 70. LFI a même voté contre cette déclaration parce qu'elle jugeait la position du gouvernement trop molle : elle refuse l'accord « tout court ». Écologistes et communistes s'y opposent aussi, et la France a voté contre au Conseil européen.\n\nSur le fond, l'inquiétude des éleveurs est légitime : le droit sur le bœuf passe de 40 % à 7,5 % pour 99 000 tonnes. Mais les études estiment la perte moyenne à environ 0,6 % du revenu des éleveurs bovins européens. Le vrai combat, c'est d'imposer les mêmes normes aux produits importés.",
 detaille="Signé en janvier 2026 et appliqué provisoirement depuis le 1er mai 2026, l'accord entre l'Union européenne et le Mercosur ouvre des quotas d'importation à droits réduits : 99 000 tonnes de bœuf à 7,5 % (contre environ 40 % hors quota), soit 1,6 % de la production européenne, et 180 000 tonnes de volaille sans droit. En échange, les vins, voitures et fromages européens gagnent des débouchés. Une clause de sauvegarde est prévue en cas de hausse des importations ou de baisse des prix.\n\nL'opposition est très large en France. En novembre 2024, l'Assemblée a soutenu la déclaration hostile du gouvernement par 484 voix contre 70 ; parmi les voix contre figuraient les députés LFI, qui jugeaient la position du gouvernement insuffisante et refusent l'accord sans condition. Écologistes et communistes s'y opposent aussi. En janvier 2026, la France a voté contre au Conseil, sans réunir de minorité de blocage, et le Parlement européen a saisi la Cour de justice.\n\nLes études citées par l'Institut Jacques Delors estiment la perte de revenu des éleveurs bovins européens à environ 0,6 %, un effet moyen qui peut masquer des difficultés fortes dans certaines exploitations. La gauche critique l'accord au nom des normes sociales et environnementales, du climat et de la souveraineté alimentaire : ce combat n'appartient pas au RN.",
 empathie="Je comprends la colère des éleveurs qui ont l'impression qu'on les sacrifie pour vendre des voitures. Leur inquiétude est fondée. Mais presque tous les partis français, à commencer par la gauche, s'opposent à cet accord.",
 legitimes=["L'élevage bovin et la volaille sont bien les filières exposées, avec une forte baisse des droits de douane.", "Les chiffres d'impact viennent en partie de la Commission, partie prenante de l'accord."],
 contre=[
  ("La gauche a voté pour le Mercosur.", "LFI a voté contre la déclaration du gouvernement parce qu'elle refuse l'accord sans condition, pas parce qu'elle le soutient."),
  ("Ça va tuer l'élevage français.", "Les études citées estiment une perte moyenne de 0,6 % du revenu des éleveurs bovins ; c'est un coup dur pour certains, pas la disparition de la filière."),
 ],
 questions=["Sais-tu comment a voté l'Assemblée nationale sur le Mercosur en novembre 2024 ?", "Pourquoi, selon toi, LFI a-t-elle voté contre la déclaration du gouvernement ?"],
 limites=["Les estimations d'impact proviennent en partie de la Commission européenne, partie prenante, et d'une synthèse de l'Institut Jacques Delors ; l'étude d'impact du CEPII n'a pas été lue directement.", "Le détail des votes des eurodéputés français sur la saisine de la Cour de justice n'a pas été vérifié."],
 publics={'convaincus': "Le RN n'est pas seul : l'Assemblée a rejeté l'accord par 484 voix contre 70, et LFI a voté contre la déclaration parce qu'elle trouvait le gouvernement trop mou. Écologistes et communistes sont contre aussi. Défendre les éleveurs n'est pas le monopole d'un parti.",
  'indecis': "L'inquiétude des éleveurs face au Mercosur est fondée, surtout pour le bœuf et la volaille, même si l'impact moyen estimé est modéré. Presque tous les partis français s'y opposent, et la France a voté contre à Bruxelles. Le vrai débat porte sur les normes imposées aux produits importés."},
 a_actualiser='2027-03-31',
))

# 25 ── Premier pays d'asile ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='france-premier-pays-asile', affirmation="La France est le pays d'Europe qui accueille le plus de demandeurs d'asile.", volet='immigration', sous_theme='Comparaisons européennes',
 mots_cles=['demandeurs d asile', 'demandes d asile', 'premier pays d asile', 'le plus de demandeurs', 'champion de l asile', 'asile europe', 'pays d accueil'],
 verdict='contredit', fiabilite='etabli',
 resume="Faux : en 2025, la France est deuxième de l'Union européenne pour le nombre total de demandes d'asile (152 000, derrière l'Allemagne avec 163 000) et troisième pour les premières demandes (116 400, derrière l'Espagne et l'Italie). Rapportée à sa population, elle est loin du sommet : la Grèce, Chypre, l'Espagne, la Belgique et la Suisse reçoivent bien plus de demandes par habitant. Le nombre de demandes a baissé en 2025 dans l'Union (-27 % pour les premières demandes).",
 contexte="L'idée que la France serait la destination principale des demandeurs d'asile en Europe est fréquente dans les discours sur l'« appel d'air ».",
 explication="On peut compter toutes les demandes (y compris les réexamens) ou seulement les premières demandes, et en volume ou par habitant. La France est parmi les premiers pays en volume, parce qu'elle est très peuplée, mais pas par habitant.",
 sources=[EUAA_2026, EUROSTAT_ASILE, SENAT_ASILE26_SYN, EUAA_OFPRA],
 faits=[
  fait("Selon l'Agence de l'UE pour l'asile, en 2025, l'Allemagne a reçu 163 000 demandes d'asile, la France 152 000, l'Espagne 143 000 et l'Italie 134 000.", 'euaa_2026', '2025', 'Union européenne et pays associés', "La France est deuxième en volume, pas première.", 'etabli', '152 000'),
  fait("Selon Eurostat, pour les premières demandes en 2025, l'Espagne (141 000) et l'Italie (126 600) devancent la France (116 400) et l'Allemagne (113 200).", 'eurostat_asile', '2025', 'Union européenne', "En primo-demandes, la France est troisième.", 'etabli', '116 400'),
  fait("Selon l'Agence de l'UE pour l'asile, la moyenne est d'environ 1 800 demandes par million d'habitants ; la Grèce (5 900), Chypre (4 500), l'Espagne, la Belgique et la Suisse (environ 2 900 chacune) sont en tête.", 'euaa_2026', '2025', 'Union européenne et pays associés', "Par habitant, d'autres pays accueillent bien plus.", 'etabli', '1 800 par million'),
  fait("Selon le Sénat, la France est « le troisième pays d'accueil des primo-demandeurs d'asile en 2025 », avec plus de 145 000 demandes déposées à l'OFPRA (environ -5 %), et un taux de protection de 52,1 % recours compris.", 'senat_asile26_syn', '2025', 'France', "Un rapport de droite confirme le classement.", 'etabli', '52,1 %'),
  fait("Selon Eurostat, les premières demandes d'asile ont baissé de 27 % dans l'UE en 2025 (669 400 contre 912 400 en 2024).", 'eurostat_asile', '2024-2025', 'Union européenne', "La tendance est à la baisse.", 'etabli', '-27 %'),
 ],
 court="Faux : en 2025, la France est deuxième derrière l'Allemagne pour l'ensemble des demandes d'asile, et troisième derrière l'Espagne et l'Italie pour les premières demandes. Rapportée à sa population, elle est loin derrière la Grèce, Chypre, l'Espagne ou la Belgique.",
 moyen="La France n'est pas première. En 2025, l'Allemagne a reçu plus de demandes d'asile (163 000 contre 152 000), et pour les premières demandes, l'Espagne et l'Italie passent devant la France.\n\nSurtout, la France est un grand pays : rapporté au nombre d'habitants, la Grèce, Chypre, l'Espagne, la Belgique ou la Suisse en reçoivent bien plus. Et les demandes ont baissé en 2025 dans toute l'Union. La France fait partie des principaux pays d'accueil, ce qui est normal pour un pays aussi peuplé, mais elle n'est pas « le » pays de l'asile.",
 detaille="Selon l'Agence de l'Union européenne pour l'asile, 822 000 demandes d'asile ont été déposées en 2025 dans l'Union et les pays associés, en baisse pour la deuxième année consécutive. En volume, l'Allemagne arrive en tête (163 000), devant la France (152 000), l'Espagne (143 000) et l'Italie (134 000). Pour les premières demandes, Eurostat classe l'Espagne (141 000) et l'Italie (126 600) devant la France (116 400) ; le Sénat confirme que la France est le troisième pays d'accueil des primo-demandeurs.\n\nPar habitant, la moyenne est d'environ 1 800 demandes par million d'habitants. La Grèce (5 900), Chypre (4 500), puis l'Espagne, la Belgique et la Suisse (environ 2 900) arrivent en tête ; la France n'en fait pas partie.\n\nEn France, l'OFPRA a reçu 145 270 demandes en 2025 (-5,5 %) et a accordé une protection dans 41 % des cas, 52,1 % en comptant les recours. Environ une demande sur deux aboutit donc à une protection, accordée à des personnes dont les craintes de persécution ont été reconnues.",
 empathie="Je comprends qu'on ait l'impression que tout le monde vient en France, vu ce qu'on entend. Mais les chiffres européens montrent que d'autres pays reçoivent plus, surtout par habitant, et que les demandes baissent.",
 legitimes=["La France fait partie des trois ou quatre principaux pays d'accueil en volume (deuxième en 2025 pour l'ensemble des demandes).", "Les réexamens de demandes ont fortement augmenté en France en 2025 (+43 % selon l'OFPRA)."],
 contre=[
  ("La France est la plus généreuse, donc tout le monde vient ici.", "Par habitant, la Grèce, Chypre, l'Espagne et la Belgique reçoivent bien plus de demandes."),
  ("Ce sont de faux réfugiés.", "En 2025, plus d'une demande sur deux a abouti à une protection, recours compris."),
 ],
 questions=["Sais-tu quel pays européen a reçu le plus de demandes d'asile en 2025 ?", "Combien de demandes par habitant reçoit la France comparée à la Belgique ?"],
 limites=["Le chiffre par habitant de la France n'est pas donné explicitement par les sources lues ; la fiche indique seulement qu'elle ne figure pas parmi les premiers.", "Les données de 2024 n'ont pas été vérifiées séparément."],
 publics={'convaincus': "Les chiffres européens sont clairs : en 2025, l'Allemagne a reçu plus de demandes que la France, et l'Espagne et l'Italie plus de premières demandes. Par habitant, la Belgique ou la Grèce en reçoivent bien plus. Et plus d'une demande sur deux aboutit à une protection : ce sont des gens qui fuient vraiment quelque chose.",
  'indecis': "La France est l'un des principaux pays d'asile en Europe, c'est normal pour un pays de sa taille, mais elle n'est pas la première. Par habitant, d'autres pays accueillent beaucoup plus, et les demandes baissent en 2025. Ces repères aident à mesurer la situation sans l'exagérer."},
 a_actualiser='2027-06-30',
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
