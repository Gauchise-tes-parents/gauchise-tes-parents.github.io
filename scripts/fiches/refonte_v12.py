"""Fiches v12 : questions fréquentes qui n'avaient pas de réponse documentée (ou une fiche voisine).

Cartes Vitale, SMIC, héritage, fraude sociale et fiscale, temps de travail, retraite à 64 ans, emploi après 50 ans,
syndicats, nationalité, accès à la propriété, location sans CDI, pauvreté et efforts, la gauche et les travailleurs.
Toutes les sources ont été ouvertes et lues les 29 et 30 octobre 2026 (consultee=True) ; aucun chiffre ne vient
d'ailleurs que du passage cité. Les données anciennes sont signalées comme telles dans les limites.
Usage : python3 scripts/fiches/refonte_v12.py  (puis npm run fiches:corriger et npm run enrichir)
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from reponses_directes import src, fait, fiche, OUT, INSEE_PAUV

def reprise(fiche_id, index, cle):
    """Réutilise telle quelle une source déjà vérifiée d'une fiche existante."""
    with open(os.path.join(OUT, fiche_id + '.json'), encoding='utf-8') as fh:
        s = json.load(fh)['sources'][index]
    return (cle, s)

# ── Sources ────────────────────────────────────────────────────────────────
SENAT_VITALE = ('senat_vitale', src("Cartes Vitale surnuméraires (question orale n° 1231S, réponse du Gouvernement)", "Sénat / ministère des Solidarités et de la Santé", "22 juillet 2020",
  "https://www.senat.fr/questions/base/2020/qSEQ20061231S.html",
  "Au 1er janvier 2020, 58,4 millions de cartes Vitale actives ; 609 000 cartes surnuméraires fin 2019 ; 1,6 million de cartes sorties du parc en 2019 ; 347 664 cartes surnuméraires fin mai 2020.",
  "Réponse officielle du Gouvernement devant le Parlement."))
AN_VITALE = ('an_vitale', src("Réponse du ministère de la Santé à la question écrite n° 3638 (cartes Vitale)", "Assemblée nationale / ministère du Travail, de la Santé, des Solidarités et des Familles", "10 juin 2025",
  "https://questions.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE3638.pdf",
  "L'excédent de cartes était de 2,2 millions en 2018 ; « depuis avril 2024, il n'y a plus de carte surnuméraire sur l'ensemble des régimes » ; une carte Vitale n'ouvre aucun remboursement si les droits sont fermés dans les bases de l'Assurance maladie.",
  "Réponse officielle du ministère compétent."))
UCL_SMIC = ('ucl_smic', src("German minimum wage drove workers to more productive firms (étude de Christian Dustmann et Attila Lindner, CReAM)", "University College London (UCL)", "18 février 2020",
  "https://www.ucl.ac.uk/news/2020/feb/german-minimum-wage-drove-workers-more-productive-firms",
  "Introduction du salaire minimum allemand en 2015 : « we do not find that it reduced employment » ; hausse de salaire d'environ 6,7 % pour les salariés payés moins de 8,50 € de l'heure ; une partie des salariés est passée vers des entreprises plus productives, ce qui explique environ 25 % de la hausse des salaires.",
  "Présentation d'une étude universitaire (document de discussion du CReAM).", 'etude'))
INSEE_PAUV_ACT = ('insee_pauv_act', src("Pauvreté monétaire (France, portrait social, édition 2025)", "Insee (Insee Références)", "18 novembre 2025",
  "https://www.insee.fr/fr/statistiques/8612540",
  "Données 2023 : taux de pauvreté monétaire 15,4 % ; actifs occupés 8,3 % (salariés 6,6 %, indépendants 19,2 %) ; chômeurs 36,1 % ; retraités 11,1 % ; inactifs de 18 ans ou plus 18,3 % ; familles monoparentales 34,3 % ; enfants de moins de 18 ans 21,9 %.",
  "Statistique publique de référence."))
CAE_HERITAGE = ('cae_her', src("Repenser l'héritage (Les notes du Conseil d'analyse économique n° 69)", "Conseil d'analyse économique (Clément Dherbécourt, Gabrielle Fack, Camille Landais, Stefanie Stantcheva)", "Décembre 2021",
  "https://cae-eco.fr/static/pdf/cae-note069.pdf",
  "Le patrimoine hérité représente 60 % du patrimoine total, contre environ 35 % au début des années 1970 ; la moitié d'une génération reçoit moins de 70 000 € ; le top 1 % reçoit plus de 4,2 millions d'euros et le top 0,1 % environ 13 millions, soit 180 fois l'héritage médian ; le top 0,1 % paie un taux effectif d'environ 10 % ; les droits de succession et de donation rapportent environ 15 milliards d'euros (0,6 % du PIB, contre environ 0,3 % en moyenne dans l'OCDE) ; la part du top 1 % dans le patrimoine est passée de 15 % à 25 % entre 1985 et 2015.",
  "Organisme public d'expertise économique placé auprès du Premier ministre.", 'etude'))
INSEE_PROPRIO = ('insee_proprio', src("Rôle des aides familiales et des revenus dans l'accès à la propriété (Économie et Statistique n° 500-501-502)", "Insee (Carole Bonnet, Bertrand Garbinti, Sébastien Grobon)", "Octobre 2018",
  "https://www.insee.fr/fr/statistiques/3622011",
  "Parmi les jeunes ménages modestes, 32 % étaient propriétaires en 1973 contre 16 % en 2013 ; dans les années 2000, environ 4 propriétaires récents sur 10 ont reçu une aide familiale, et ces aides ont fortement augmenté chez les ménages aisés.",
  "Revue de la statistique publique.", 'etude'))
PS_FRAUDE = ('ps_fraude', src("« Une corruption lente et insidieuse » : un rapport évalue la fraude sociale à 13 milliards d'euros par an", "Public Sénat, d'après le rapport du Haut Conseil du financement de la protection sociale (HCFiPS)", "27 septembre 2024",
  "https://www.publicsenat.fr/actualites/economie/une-corruption-lente-et-insidieuse-un-rapport-evalue-la-fraude-sociale-a-13-milliards-deuros-par-an",
  "Fraude sociale : environ 13 milliards d'euros par an de « potentiel théorique » (environ 1,9 % des prestations) ; 2,1 milliards détectés, 600 millions recouvrés ; travail dissimulé (cotisations non versées) : 6,9 milliards ; indus de RSA : 1,54 milliard ; Assurance maladie : 1,71 milliard ; 56 % du fait des entreprises ou des indépendants, 34 % des assurés, 10 % des professionnels de santé.",
  "Média parlementaire rendant compte d'un rapport d'un organisme public.", 'media'))
AN_FRAUDE_FISC = ('an_fisc', src("Réponse du ministère de l'Économie à la question écrite n° 8208 (fraude fiscale et sociale)", "Assemblée nationale / ministère de l'Économie, des Finances et de la Souveraineté industrielle et numérique", "21 novembre 2023",
  "https://questions.assemblee-nationale.fr/dyn/16/questions/QANR5L16QE8208.pdf",
  "Selon l'Insee, la TVA non recouvrée serait comprise « entre 20 Md€ et 25 Md€ » (estimations comportant des biais méthodologiques) ; écart de TVA en 2019 : « 7,4 % soit 13,8 Md€ », contre une moyenne européenne de 3 %, écart qui n'est qu'en partie dû à la fraude ; contrôle fiscal 2022 : 14,6 Md€ de droits et pénalités mis en recouvrement, 10,6 Md€ encaissés.",
  "Réponse officielle du ministère compétent."))
PS_TEMPS = ('ps_temps', src("« Les Français ne travaillent pas assez » : François Bayrou a-t-il raison ?", "Public Sénat (Marius Texier), d'après Eurostat", "17 avril 2025",
  "https://www.publicsenat.fr/actualites/economie/les-francais-ne-travaillent-pas-assez-francois-bayrou-a-t-il-raison",
  "Eurostat, 2024 : un salarié à temps complet travaille 39,9 heures par semaine en France, contre 40,3 heures dans l'Union européenne et 40,2 heures en Allemagne ; temps partiel : 16,8 % des emplois en France contre 17,8 % dans l'UE ; ensemble des emplois (2023) : 36 heures contre 36,1 heures ; 10 % des salariés travaillent 49 heures ou plus, contre 7,4 % dans l'UE ; en durée annuelle effective, la France est avant-dernière de l'UE (2022).",
  "Média parlementaire, vérification à partir des données d'Eurostat.", 'media'))
COR_2025 = ('cor25', src("Évolutions et perspectives des retraites en France — synthèse du rapport annuel", "Conseil d'orientation des retraites (COR)", "Juin 2025",
  "https://www.cor-retraites.fr/sites/default/files/2025-06/Synth%C3%A8se_Def_.pdf",
  "Solde du système de retraite : -1,7 milliard d'euros en 2024 (-0,1 % du PIB) ; -0,2 % du PIB en 2030 (environ 6,6 milliards) ; -1,4 % du PIB en 2070 ; dépenses : 13,9 % du PIB en 2024 et 14,2 % en 2070 ; ressources : 13,9 % du PIB en 2024 et 12,8 % en 2070 ; âge moyen de départ : 62,9 ans en 2023, 64,6 ans en 2070.",
  "Organisme public d'expertise sur les retraites, pluraliste (parlementaires, partenaires sociaux, administrations)."))
COR_2026 = ('cor26', src("Rapport annuel 2026 — partie 4, chapitre 1 : l'emploi des seniors", "Conseil d'orientation des retraites (COR)", "Juin 2026",
  "https://www.cor-retraites.fr/sites/default/files/2026-06/RA_Part4_Chap1.pdf",
  "Taux d'emploi des 55-64 ans : 61,7 % en 2025 (41 % en 2010) ; 55-59 ans : 78,8 % ; 60-64 ans : 44,4 % ; Suède : 78,3 %, Japon : 79,8 % ; à 61 ans, 24,5 % des personnes ne sont ni en emploi ni à la retraite, dont 14,5 % en mauvaise santé ; ce statut est « le plus souvent subi pour des raisons de santé ou de handicap ».",
  "Organisme public d'expertise sur les retraites."))
DARES_SYND = ('dares_synd', src("La syndicalisation en France : des salariés deux fois plus syndiqués dans la fonction publique (Dares Analyses n° 025)", "Dares (Maria Teresa Pignoni)", "Mai 2016",
  "https://www.fonction-publique.gouv.fr/files/files/ArchivePortailFP/www.fonction-publique.gouv.fr/files/files/statistiques/Hors_collection/Dares-2016-025.pdf",
  "En 2013, 11 % des salariés adhèrent à un syndicat (20 % dans la fonction publique, 9 % dans le secteur marchand et associatif) ; 5 % dans les établissements marchands de moins de 50 salariés ; 1 % des intérimaires, 2 % des CDD ; moyenne de l'Union européenne : 23 % ; les conventions collectives couvrent plus de 90 % des salariés du secteur marchand et associatif, et les syndicats négocient au nom de l'ensemble des salariés.",
  "Service statistique du ministère du Travail (données de 2013)."))
DARES_2004 = ('dares_04', src("Mythes et réalités de la syndicalisation en France (Premières Synthèses n° 44.2)", "Dares (Thomas Amossé)", "Octobre 2004",
  "https://dares.travail-emploi.gouv.fr/sites/default/files/f8f5153e516232a6f1f20818645b63a1/Dares_Mythes%20et%20r%C3%A9alit%C3%A9s%20de%20la%20syndicalisation%20en%20France.pdf",
  "Taux de syndicalisation de 8,2 % en 2003, l'un des plus faibles des pays industrialisés ; environ 40 % des salariés déclarent une présence syndicale sur leur lieu de travail ; plus de 90 % sont couverts par une convention collective.",
  "Service statistique du ministère du Travail (données anciennes)."))
INSEE_NAT = ('insee_nat', src("Acquisitions de la nationalité française (Immigrés et descendants d'immigrés, Insee Références)", "Insee", "30 mars 2023",
  "https://www.insee.fr/fr/statistiques/6793254",
  "En 2021 : 130 385 acquisitions de la nationalité française ; 75 249 par décret (naturalisation, 58 %) ; 52 764 par déclaration, dont 17 280 par mariage et 32 727 déclarations anticipées de jeunes de 13 à 17 ans nés en France ; 2 372 sans formalité ; la naturalisation est ouverte à « tout étranger qui réside régulièrement en France » sous conditions (articles 21-15 à 21-27 du Code civil) ; un jeune né en France de parents étrangers devient français à 18 ans sous condition de résidence.",
  "Statistique publique de référence."))
ANIL_VISALE = ('anil_visale', src("Garantie Visale : ce qui change au 6 janvier 2026", "ADIL des Hautes-Pyrénées (réseau ANIL, agence nationale d'information sur le logement)", "Mise à jour 2026",
  "https://www.anil.org/adil-65/toutes-nos-actualites/details/garantie-visale/",
  "Visale est un cautionnement gratuit porté par Action Logement, qui remplace un garant physique et couvre les impayés de loyers et de charges ; à partir du 6 janvier 2026, plafond de ressources des salariés de plus de 30 ans du privé porté à 1 710 € nets par mois (contre 1 500 €) ; plafonds de loyer : 1 940 € en Île-de-France, 1 575 € en zone II, 1 365 € en zone III ; garantie limitée au bail initial, 3 ans au maximum.",
  "Réseau public d'information juridique sur le logement."))
QC_VISALE = ('qc_visale', src("Location : la garantie Visale évolue en 2026", "UFC-Que Choisir (Rosine Maiolo)", "4 février 2026",
  "https://www.quechoisir.org/actualite-location-la-garantie-visale-evolue-en-2026-n174094/",
  "De 18 à 30 ans, Visale est accessible sans condition de ressources (étudiants, apprentis, salariés en CDD ou en période d'essai, demandeurs d'emploi…) ; au-delà de 30 ans, pour les salariés du privé gagnant au plus 1 710 € nets, embauchés depuis moins de 6 mois (CDD, intérim, CDI en période d'essai) ou en mutation ; le loyer ne doit pas dépasser 50 % des ressources ; « plus de 1,9 million de ménages » en ont bénéficié depuis sa création ; le dispositif est financé par la participation des employeurs à Action Logement.",
  "Association de consommateurs, article d'information.", 'media'))
FS_ORIGINE = ('fs_origine', src("Nés sous la même étoile ? Origine sociale et niveau de vie (Note d'analyse n° 68)", "France Stratégie (Clément Dherbécourt)", "Juillet 2018",
  "https://solidarites.gouv.fr/sites/solidarite/files/2023-03/nes_sous_la_meme_etoile_france_strategie.pdf",
  "À sexe, âge et origine migratoire identiques, l'écart moyen de niveau de vie entre un enfant de cadre et un enfant d'ouvrier non qualifié « s'élève à 1 000 euros par mois » ; un enfant de cadre supérieur a « 4,5 fois plus de chances » qu'un enfant d'ouvrier d'appartenir aux 20 % les plus aisés ; l'inégalité des chances éducatives contribue pour moitié à ces écarts ; à diplôme égal, « un écart demeure ».",
  "Organisme public d'expertise et de prospective.", 'etude'))

INSEE_EMPLOI_IMM = reprise('immigration-emploi', 0, 'insee_emploi_imm')
CEPII = reprise('immigration-emploi', 1, 'cepii')
EDO = reprise('immigration-emploi', 3, 'edo')
LCP_NFP = reprise('gauche-assistes-travailleurs', 1, 'lcp_nfp')
PS_VOTE = reprise('gauche-assistes-travailleurs', 5, 'ps_vote')
BMO = reprise('chomage-penurie-recrutement', 0, 'bmo')
INSEE_IMM = reprise('immigration-chiffres-definitions', 0, 'insee_imm')
INSEE_HIST = reprise('france-pays-immigration', 0, 'insee_hist')

FICHES = []

# 1 ── Cartes Vitale ─────────────────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "Le chiffre vient d'un vrai problème de 2018 : 2,2 millions de cartes non désactivées. Mais une carte sans droits ouverts ne rembourse rien, et le ministère de la Santé dit qu'il n'y a plus de carte en trop depuis avril 2024. Continuer à brandir ce chiffre, c'est viser un problème déjà réglé, pendant que la fraude des employeurs coûte bien plus.", 'indecis': "Il y a bien eu des cartes Vitale en trop, surtout des cartes jamais désactivées après un décès ou un départ. Mais l'Assurance maladie vérifie les droits à chaque remboursement, et selon le ministère, le fichier est nettoyé depuis 2024."},
 id='cartes-vitale-en-trop', affirmation="Il y a des millions de cartes Vitale en trop.", volet='social', sous_theme='Fraude sociale',
 mots_cles=['cartes vitale', 'carte vitale', 'vitale', 'surnuméraires', 'cartes en trop', 'millions de cartes', 'assurance maladie', 'fraude', 'sécu'],
 verdict='contredit', fiabilite='etabli',
 resume="Il y a eu des cartes Vitale en trop — 2,2 millions en 2018 — mais il s'agissait surtout de cartes non désactivées après un décès, un départ ou un changement de régime. Le ministère de la Santé indique que depuis avril 2024 il n'y a plus de carte surnuméraire, et qu'une carte n'ouvre aucun remboursement si les droits sont fermés.",
 contexte="Le chiffre de « millions de cartes Vitale en trop » circule depuis la fin des années 2010 pour suggérer une fraude massive, souvent attribuée aux étrangers.",
 explication="Une carte « surnuméraire » est une carte encore physiquement active alors que son titulaire n'a plus de droits ouverts, ou qu'il a une autre carte. Ce n'est pas un remboursement : l'Assurance maladie vérifie les droits dans ses bases à chaque feuille de soins.",
 sources=[AN_VITALE, SENAT_VITALE],
 faits=[
  fait("Selon le ministère de la Santé, l'excédent de cartes Vitale atteignait 2,2 millions en 2018 et, depuis avril 2024, il n'y a plus de carte surnuméraire sur l'ensemble des régimes.", 'an_vitale', '2018-2024', 'France', "Le problème a existé, il a été corrigé.", 'etabli', '2,2 millions'),
  fait("Selon le même ministère, une carte Vitale n'ouvre aucun remboursement si les droits de son titulaire sont fermés dans les bases de l'Assurance maladie.", 'an_vitale', '2025', 'France', "Une carte en trop n'est pas une dépense en trop.", 'etabli'),
  fait("Selon le Gouvernement, 609 000 cartes étaient surnuméraires fin 2019, puis 347 664 fin mai 2020, pour 58,4 millions de cartes actives ; 1,6 million de cartes ont été retirées du parc en 2019.", 'senat_vitale', '2019-2020', 'France', "Le nettoyage du fichier était déjà engagé en 2019-2020.", 'etabli', '609 000'),
 ],
 court="Faux aujourd'hui : il y a eu jusqu'à 2,2 millions de cartes en trop en 2018, surtout des cartes non désactivées, mais le ministère de la Santé indique qu'il n'y en a plus depuis avril 2024. Et une carte sans droits ouverts ne rembourse rien.",
 moyen="Le chiffre a une origine réelle : en 2018, il y avait 2,2 millions de cartes Vitale de trop, souvent des cartes de personnes décédées, parties à l'étranger ou passées dans un autre régime, qui n'avaient pas été désactivées.\n\nMais une carte n'est pas un chèque : l'Assurance maladie vérifie les droits à chaque remboursement, et une carte sans droits ouverts ne rapporte rien. Le fichier a été nettoyé : selon le ministère de la Santé, il n'y a plus de carte surnuméraire depuis avril 2024.",
 detaille="L'affirmation repose sur un problème réel de gestion. En 2018, l'excédent de cartes Vitale était de 2,2 millions. Fin 2019, le Gouvernement en comptait 609 000, puis 347 664 fin mai 2020, pour 58,4 millions de cartes actives ; 1,6 million de cartes avaient été retirées du parc en 2019.\n\nDans sa réponse de juin 2025 à l'Assemblée nationale, le ministère de la Santé indique que « depuis avril 2024, il n'y a plus de carte surnuméraire sur l'ensemble des régimes ». Il rappelle surtout qu'une carte n'ouvre aucun remboursement si les droits sont fermés dans les bases de l'Assurance maladie : une carte en trop n'est donc pas une dépense en trop.\n\nLa fraude à l'Assurance maladie existe, mais elle passe surtout par d'autres canaux, et une part importante est le fait de professionnels de santé. Désigner les cartes Vitale, c'est viser un problème déjà réglé.",
 empathie="Je comprends que ce chiffre choque, on l'a beaucoup entendu. Il y a bien eu des cartes en trop, surtout des cartes jamais désactivées. Mais elles ne remboursaient rien sans droits ouverts, et le ministère dit qu'il n'y en a plus depuis 2024.",
 legitimes=["Il y a bien eu plus de 2 millions de cartes en trop en 2018 : la gestion du fichier était défaillante.", "La fraude à l'Assurance maladie existe, même si elle ne passe pas principalement par les cartes surnuméraires."],
 contre=[
  ("Avec une carte en trop, on peut se faire soigner gratuitement.", "Non : le remboursement dépend des droits ouverts dans les bases de l'Assurance maladie, vérifiés à chaque feuille de soins, pas de la carte elle-même."),
  ("Le ministère ment pour cacher la fraude.", "Les chiffres viennent de réponses officielles au Parlement, qui engagent le ministère et peuvent être contestées par les parlementaires."),
 ],
 questions=["Sais-tu qu'une carte sans droits ouverts ne déclenche aucun remboursement ?", "D'où vient le chiffre de « millions de cartes » que tu as entendu, et de quelle année date-t-il ?"],
 limites=["Les sources sont des réponses ministérielles ; aucune évaluation indépendante du fichier n'est citée ici.", "Le montant de la fraude liée aux cartes elles-mêmes n'est pas chiffré dans ces sources."],
 a_actualiser='2027-06-30',
))

# 2 ── SMIC ──────────────────────────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "L'Allemagne a créé un salaire minimum en 2015 : l'étude de Dustmann et Lindner n'a pas trouvé de baisse de l'emploi, et les moins bien payés ont gagné environ 6,7 %. Ce n'est pas une loi de la nature, c'est un choix. Et aujourd'hui, 6,6 % des salariés vivent sous le seuil de pauvreté : le problème, ce sont les salaires trop bas.", 'indecis': "La crainte pour l'emploi se comprend, surtout pour les petites entreprises. Mais les études récentes, comme celle sur le salaire minimum allemand, ne trouvent pas de destruction d'emplois mesurable. L'effet dépend du niveau et du rythme des hausses : c'est un débat à mener avec des chiffres."},
 id='smic-detruit-emplois', affirmation="Augmenter le SMIC détruit des emplois.", volet='social', sous_theme='Emploi et salaires',
 mots_cles=['smic', 'salaire minimum', 'augmenter le smic', 'hausse du smic', 'coup de pouce', 'détruit des emplois', 'tue l emploi', 'coût du travail', 'bas salaires'],
 verdict='trompeur', fiabilite='debat',
 resume="Ce n'est pas automatique. Quand l'Allemagne a créé un salaire minimum en 2015, l'étude de Dustmann et Lindner n'a pas constaté de baisse de l'emploi : les salaires des moins bien payés ont augmenté d'environ 6,7 % et une partie des salariés est passée dans des entreprises plus productives. L'effet dépend du niveau et du rythme de la hausse : c'est un débat économique, pas une loi de la nature.",
 contexte="L'argument est opposé à chaque proposition de hausse du SMIC : un salaire minimum plus élevé rendrait le travail peu qualifié trop cher et pousserait les entreprises à embaucher moins.",
 explication="Une hausse du salaire minimum a deux effets possibles : elle augmente le coût du travail, mais elle augmente aussi le pouvoir d'achat et pousse les entreprises peu productives à s'améliorer ou à céder la place à d'autres. Les études récentes cherchent lequel l'emporte, selon le niveau du salaire minimum.",
 sources=[UCL_SMIC, INSEE_PAUV_ACT],
 faits=[
  fait("Selon l'étude de Christian Dustmann et Attila Lindner (UCL), l'introduction du salaire minimum allemand en 2015 n'a pas réduit l'emploi, tout en augmentant d'environ 6,7 % le salaire des salariés payés moins de 8,50 € de l'heure.", 'ucl_smic', '2015', 'Allemagne', "Un salaire minimum significatif peut être créé sans destruction d'emplois mesurable.", 'estimation', '6,7 %'),
  fait("Selon la même étude, une partie des salariés est passée vers des entreprises plus productives, ce qui explique environ 25 % de la hausse des salaires.", 'ucl_smic', '2015-2016', 'Allemagne', "Le salaire minimum a aussi réorganisé l'économie vers des emplois plus productifs.", 'estimation', '25 %'),
  fait("Selon l'Insee, 6,6 % des salariés vivaient sous le seuil de pauvreté en 2023.", 'insee_pauv_act', '2023', 'France', "Avoir un emploi ne protège pas toujours de la pauvreté : le niveau des bas salaires est un enjeu.", 'etabli', '6,6 %'),
 ],
 court="Pas automatiquement : quand l'Allemagne a créé son salaire minimum en 2015, l'étude de référence n'a pas trouvé de baisse de l'emploi, et les bas salaires ont gagné environ 6,7 %. Tout dépend du niveau et du rythme de la hausse.",
 moyen="L'idée paraît logique, mais les faits sont plus nuancés. L'Allemagne a introduit un salaire minimum en 2015 : l'étude de Dustmann et Lindner (UCL) n'a pas constaté de baisse de l'emploi, alors que les salariés concernés ont gagné environ 6,7 %.\n\nUne partie d'entre eux est passée dans des entreprises plus productives : le salaire minimum a poussé l'économie vers de meilleurs emplois. En France, 6,6 % des salariés vivent sous le seuil de pauvreté : la question n'est pas de savoir s'il faut mieux payer le travail, mais comment le faire.",
 detaille="L'argument suppose qu'un salaire plus élevé rend automatiquement certains emplois non rentables. Les études récentes nuancent fortement ce raisonnement. L'Allemagne n'avait pas de salaire minimum national avant 2015 ; l'étude de Christian Dustmann et Attila Lindner (UCL, CReAM) conclut qu'il n'a pas réduit l'emploi, et que les salariés payés moins de 8,50 € de l'heure ont vu leur salaire augmenter d'environ 6,7 %. Une partie de cette hausse, environ 25 %, vient de salariés passés vers des entreprises plus productives.\n\nCela ne prouve pas qu'on peut augmenter le salaire minimum sans limite : l'effet dépend du niveau atteint, de la vitesse de la hausse et des aides qui l'accompagnent pour les petites entreprises. C'est un vrai débat entre économistes.\n\nEn France, 6,6 % des salariés vivaient sous le seuil de pauvreté en 2023, selon l'Insee. Dire « augmenter le SMIC détruit des emplois » comme une évidence, c'est fermer un débat que les données laissent ouvert.",
 empathie="Je comprends l'inquiétude, surtout pour les petites entreprises. Mais quand l'Allemagne a créé son salaire minimum, les économistes n'ont pas vu l'emploi baisser. La vraie question, c'est le niveau et le rythme, et comment on aide les petits patrons.",
 legitimes=["Une hausse très forte et très rapide peut peser sur les petites entreprises à faible marge.", "L'étude citée porte sur l'Allemagne, dont le marché du travail diffère de celui de la France."],
 contre=[
  ("En France, le SMIC est déjà élevé, ce n'est pas comparable.", "C'est un argument sérieux : l'effet dépend du niveau. Mais il plaide pour discuter du rythme et des aides, pas pour présenter la destruction d'emplois comme automatique."),
  ("Les entreprises vont délocaliser.", "Une grande partie des emplois au salaire minimum (commerce, restauration, aide à domicile) ne peut pas être délocalisée."),
 ],
 questions=["Sais-tu ce qui s'est passé pour l'emploi quand l'Allemagne a créé son salaire minimum ?", "Si un emploi ne permet pas de sortir de la pauvreté, qui paie la différence ?"],
 limites=["La source principale porte sur l'Allemagne en 2015 ; aucune évaluation française récente n'a pu être lue pour cette fiche.", "Le rapport annuel du groupe d'experts sur le SMIC, qui est plus réservé sur les coups de pouce, n'a pas pu être consulté ; son avis n'est donc pas résumé ici."],
 a_actualiser='2027-06-30',
))

# 3 ── Héritage ──────────────────────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "La moitié d'une génération hérite de moins de 70 000 €, et ces héritages sont déjà peu ou pas taxés. Ceux qui paient vraiment peu, ce sont les très gros héritiers : environ 10 % de taux effectif pour le top 0,1 %, selon le Conseil d'analyse économique. Défendre leur exonération au nom des petites familles, c'est se tromper de combat.", 'indecis': "Vouloir transmettre à ses enfants est légitime, et la plupart des héritages sont modestes. La question porte sur les très gros patrimoines, faiblement taxés, alors que l'héritage pèse de plus en plus dans le patrimoine total (60 % contre 35 % au début des années 1970)."},
 id='heritage-taxation', affirmation="L'héritage, c'est le fruit du travail des parents, il ne faut pas le taxer.", volet='social', sous_theme='Revenus du travail et du patrimoine',
 mots_cles=['héritage', 'heritage', 'succession', 'droits de succession', 'transmission', 'donation', 'hériter', 'taxer l héritage', 'impôt sur l héritage', 'patrimoine'],
 verdict='trompeur', fiabilite='interpretation',
 resume="La plupart des héritages sont modestes et déjà peu ou pas taxés : la moitié d'une génération reçoit moins de 70 000 €. Les très gros héritages, eux, sont faiblement imposés : le top 0,1 % reçoit environ 13 millions d'euros et paie un taux effectif d'environ 10 %, selon le Conseil d'analyse économique. Et l'héritage pèse de plus en plus : 60 % du patrimoine total, contre 35 % au début des années 1970.",
 contexte="L'impôt sur les successions est l'un des plus impopulaires. Beaucoup de familles modestes craignent de devoir payer, alors que le débat porte surtout sur les très gros patrimoines.",
 explication="Les droits de succession sont progressifs et comportent des abattements importants en ligne directe : la plupart des transmissions ne paient rien ou presque. La question politique porte sur la concentration croissante du patrimoine hérité et sur les exonérations dont profitent les plus gros patrimoines.",
 sources=[CAE_HERITAGE, INSEE_PROPRIO],
 faits=[
  fait("Selon le Conseil d'analyse économique, le patrimoine hérité représente 60 % du patrimoine total, contre environ 35 % au début des années 1970.", 'cae_her', '1970-2020', 'France', "La richesse vient de plus en plus de la naissance que du travail.", 'estimation', '60 %'),
  fait("Selon la même note, la moitié d'une génération reçoit moins de 70 000 €, tandis que le top 0,1 % reçoit environ 13 millions d'euros, soit 180 fois l'héritage médian, et paie un taux effectif d'environ 10 %.", 'cae_her', 'Génération actuelle', 'France', "Les héritages modestes sont peu concernés ; les très gros sont faiblement taxés.", 'estimation', '70 000 €'),
  fait("Selon la même note, les droits de succession et de donation rapportent environ 15 milliards d'euros, soit 0,6 % du PIB, contre environ 0,3 % en moyenne dans l'OCDE.", 'cae_her', 'Début des années 2020', 'France et OCDE', "La France taxe plus que la moyenne : c'est un argument des opposants, qui doit être intégré.", 'estimation', '0,6 %'),
  fait("Selon l'Insee, dans les années 2000, environ 4 propriétaires récents sur 10 avaient reçu une aide familiale, et ces aides ont fortement augmenté chez les ménages aisés.", 'insee_proprio', 'Années 2000', 'France', "Les transmissions familiales décident de plus en plus de l'accès au patrimoine.", 'estimation'),
 ],
 court="La moitié des héritiers reçoivent moins de 70 000 € et paient peu ou rien. Ceux qui reçoivent 13 millions paient environ 10 % effectifs (CAE). Taxer davantage les très gros héritages, ce n'est pas punir le travail des parents, c'est limiter une rente de naissance.",
 moyen="Les héritages modestes ne sont pas la cible : la moitié d'une génération reçoit moins de 70 000 €, et les abattements font que la plupart ne paient rien ou presque.\n\nLe problème est ailleurs : selon le Conseil d'analyse économique, le patrimoine hérité représente désormais 60 % du patrimoine total, contre 35 % au début des années 1970. Le top 0,1 % hérite d'environ 13 millions d'euros et paie un taux effectif d'environ 10 %. Plus l'héritage pèse, moins le mérite compte.",
 detaille="L'idée que l'héritage serait le fruit du travail des parents est juste pour la plupart des familles, et ce sont justement ces héritages-là qui sont peu ou pas taxés : la moitié d'une génération reçoit moins de 70 000 €.\n\nLe Conseil d'analyse économique (note n° 69, 2021) montre que le patrimoine hérité représente 60 % du patrimoine total, contre environ 35 % au début des années 1970, et que la part du 1 % le plus riche dans le patrimoine est passée de 15 % à 25 % entre 1985 et 2015. Le top 0,1 % des héritiers reçoit environ 13 millions d'euros, 180 fois l'héritage médian, mais paie un taux effectif d'environ 10 %, grâce aux exonérations et aux donations anticipées.\n\nIl faut être honnête : la France prélève plus que la moyenne de l'OCDE (0,6 % du PIB contre environ 0,3 %). Le débat porte donc moins sur le niveau global que sur sa répartition : des petits héritages parfois taxés, de très gros patrimoines qui échappent en partie à l'impôt.",
 empathie="Je comprends : on veut pouvoir laisser quelque chose à ses enfants, c'est profondément humain. Mais la plupart des héritages ne paient presque rien. Ce dont on parle, ce sont les héritages de plusieurs millions, qui sont étonnamment peu taxés.",
 legitimes=["Les droits de succession rapportent plus en France que dans la moyenne de l'OCDE.", "Certaines successions moyennes, notamment entre personnes sans lien de parenté direct, peuvent être lourdement taxées."],
 contre=[
  ("L'argent a déjà été taxé une fois.", "Pour l'héritier, c'est un revenu qu'il n'a pas gagné par son travail ; et une partie des plus-values transmises n'a jamais été imposée."),
  ("Les riches vont partir.", "Les droits dépendent de la résidence de l'héritier et du défunt, et de la localisation des biens ; c'est un argument pour coordonner la fiscalité, pas pour exonérer les très gros patrimoines."),
 ],
 questions=["Sais-tu combien hérite la moitié des Français ?", "Est-il juste qu'un héritage de 13 millions soit taxé à environ 10 % quand un salaire l'est souvent davantage ?"],
 limites=["Les chiffres datent de la note du CAE de 2021 ; ils reposent sur des données fiscales et des estimations.", "Le barème actuel des droits de succession n'est pas détaillé ici."],
 a_actualiser='2027-12-31',
))

# 4 ── Fraude sociale / fiscale ─────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "La fraude sociale existe, environ 13 milliards d'euros par an selon le HCFiPS. Mais plus de la moitié vient des entreprises et des indépendants, surtout par le travail dissimulé, pas des allocataires. Et la seule fraude à la TVA est estimée entre 20 et 25 milliards : si on veut récupérer de l'argent, il faut regarder partout.", 'indecis': "Il est normal de vouloir lutter contre toutes les fraudes. Les estimations publiques montrent que la fraude sociale vient surtout des entreprises, et que la fraude fiscale est au moins aussi importante, même si elle est plus difficile à mesurer."},
 id='fraude-sociale-fiscale', affirmation="La fraude sociale coûte plus cher que la fraude fiscale.", volet='social', sous_theme='Fraude sociale',
 mots_cles=['fraude sociale', 'fraude fiscale', 'fraudeurs', 'fraude aux allocations', 'fraude aux prestations', 'travail dissimulé', 'travail au noir', 'tva', 'évasion fiscale', 'fraude'],
 verdict='contredit', fiabilite='estimation',
 resume="La fraude sociale est estimée à environ 13 milliards d'euros par an, et plus de la moitié vient des entreprises et des indépendants, surtout par le travail dissimulé. Pour la seule TVA, l'Insee estime la fraude entre 20 et 25 milliards d'euros. La fraude fiscale n'est pas plus petite : elle est plus difficile à mesurer.",
 contexte="Le débat oppose souvent la fraude « des pauvres » aux allocations et la fraude « des riches » aux impôts, avec des chiffres très variables selon les sources.",
 explication="Les deux fraudes sont estimées par des méthodes différentes, avec de fortes incertitudes. Mais la fraude sociale comprend aussi les cotisations non versées par des employeurs, et la fraude fiscale ne se limite pas à la TVA.",
 sources=[PS_FRAUDE, AN_FRAUDE_FISC],
 faits=[
  fait("Selon le Haut Conseil du financement de la protection sociale (2024), la fraude sociale représente environ 13 milliards d'euros par an de potentiel théorique, environ 1,9 % des prestations.", 'ps_fraude', '2024', 'France', "Un montant réel, mais modeste au regard des prestations versées.", 'estimation', '13 milliards'),
  fait("Selon la même estimation, 56 % de cette fraude est le fait des entreprises ou des indépendants, 34 % des assurés et 10 % des professionnels de santé ; le travail dissimulé en représente 6,9 milliards.", 'ps_fraude', '2024', 'France', "La fraude sociale est d'abord une fraude d'employeurs, pas d'allocataires.", 'estimation', '56 %'),
  fait("Selon l'Insee, cité par le ministère de l'Économie, la seule TVA non recouvrée serait comprise entre 20 et 25 milliards d'euros par an, une estimation qui comporte des biais méthodologiques.", 'an_fisc', '2023', 'France', "La fraude à un seul impôt dépasse déjà l'estimation de toute la fraude sociale.", 'estimation', '20 Md€'),
  fait("Selon la même estimation du HCFiPS, les indus de RSA représentent environ 1,54 milliard d'euros.", 'ps_fraude', '2024', 'France', "La fraude des allocataires existe : il faut le reconnaître.", 'estimation', '1,54 milliard'),
 ],
 court="Faux : la fraude sociale est estimée à environ 13 milliards par an, dont plus de la moitié par des entreprises (travail dissimulé). La seule fraude à la TVA est estimée par l'Insee entre 20 et 25 milliards.",
 moyen="Les chiffres officiels disent l'inverse. La fraude sociale est estimée à environ 13 milliards d'euros par an, et 56 % vient des entreprises et des indépendants, surtout par le travail dissimulé : des cotisations que des employeurs ne versent pas.\n\nPour la fraude fiscale, l'Insee estime la seule TVA non recouvrée entre 20 et 25 milliards. Et ce n'est qu'un impôt. La fraude des allocataires existe, mais elle n'est ni la seule ni la plus coûteuse.",
 detaille="Comparer les deux fraudes demande de la prudence : les méthodes d'estimation diffèrent et les incertitudes sont fortes. Mais aucun chiffre officiel ne permet de dire que la fraude sociale serait plus coûteuse.\n\nLe Haut Conseil du financement de la protection sociale estime la fraude sociale à environ 13 milliards d'euros par an de potentiel théorique, environ 1,9 % des prestations. Seuls 2,1 milliards sont détectés et 600 millions recouvrés. Surtout, 56 % de cette fraude est le fait des entreprises ou des indépendants, dont 6,9 milliards de travail dissimulé ; les assurés en représentent 34 %, dont 1,54 milliard d'indus de RSA.\n\nCôté fiscal, le ministère de l'Économie cite une estimation de l'Insee : la seule TVA non recouvrée serait comprise entre 20 et 25 milliards d'euros. L'écart de TVA français (7,4 % en 2019) est plus du double de la moyenne européenne, même s'il n'est pas uniquement dû à la fraude. Il n'existe pas d'estimation officielle complète de la fraude fiscale, ce qui est en soi un choix politique.",
 empathie="Je comprends que la fraude aux aides révolte, c'est de l'argent commun. Mais quand on regarde les chiffres officiels, la plus grosse part de la fraude sociale vient d'employeurs qui ne déclarent pas, et la fraude à la seule TVA est encore plus importante.",
 legitimes=["La fraude des allocataires existe et représente plusieurs milliards d'euros, dont environ 1,5 milliard pour le RSA.", "Les estimations de fraude fiscale comportent de fortes incertitudes."],
 contre=[
  ("On parle de la fraude détectée, et les fraudeurs aux aides sont plus nombreux.", "Le nombre de fraudeurs ne dit rien des montants : quelques fraudes d'entreprises pèsent plus que beaucoup de petits indus."),
  ("La TVA, ce n'est pas vraiment de la fraude des riches.", "C'est vrai que la fraude à la TVA touche des entreprises de toutes tailles ; l'essentiel est qu'elle dépasse à elle seule l'estimation de toute la fraude sociale."),
 ],
 questions=["Sais-tu qui fraude le plus aux cotisations sociales : les assurés ou les employeurs ?", "Pourquoi n'existe-t-il pas d'estimation officielle complète de la fraude fiscale, selon toi ?"],
 limites=["L'estimation de la fraude sociale provient d'un compte rendu de presse du rapport du HCFiPS.", "Aucune estimation officielle de l'ensemble de la fraude fiscale n'est citée : seule la TVA est chiffrée ici. Les chiffres plus élevés qui circulent (parfois 60 à 100 milliards) ne sont pas repris faute de source officielle vérifiée."],
 a_actualiser='2027-06-30',
))

# 5 ── Temps de travail ──────────────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "Un salarié français à temps complet travaille 39,9 heures par semaine, contre 40,2 en Allemagne selon Eurostat : l'écart est minuscule. Ce qui manque, ce sont les emplois pour les jeunes et les seniors : à 61 ans, près d'une personne sur quatre n'est ni en emploi ni à la retraite, souvent pour raison de santé. Ce ne sont pas des paresseux.", 'indecis': "La durée annuelle du travail est plus basse en France, c'est vrai. Mais à temps complet, les Français travaillent presque autant que leurs voisins, et 10 % des salariés font 49 heures ou plus. La différence vient surtout du faible emploi des jeunes et des seniors."},
 id='francais-travaillent-pas-assez', affirmation="Les Français ne travaillent pas assez.", volet='social', sous_theme='Emploi et salaires',
 mots_cles=['ne travaillent pas assez', 'travailler plus', 'temps de travail', 'heures', 'durée du travail', 'paresseux', 'feignants', '35 heures', 'travaillent moins', 'productivité'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Un salarié à temps complet travaille 39,9 heures par semaine en France, contre 40,3 heures dans l'Union européenne et 40,2 heures en Allemagne (Eurostat, 2024) : l'écart est faible. Ce qui fait baisser la quantité totale de travail, c'est surtout que moins de jeunes et de seniors sont en emploi : à 61 ans, près d'une personne sur quatre n'est ni en emploi ni à la retraite, le plus souvent pour raison de santé.",
 contexte="L'idée revient dans les débats sur les retraites, les jours fériés ou les 35 heures, à partir de la durée annuelle effective du travail, où la France est en bas du classement européen.",
 explication="Il faut distinguer la durée de travail des personnes en emploi, qui est proche de la moyenne européenne, et la quantité totale de travail dans le pays, qui dépend aussi du nombre de personnes en emploi selon l'âge.",
 sources=[PS_TEMPS, COR_2026],
 faits=[
  fait("Selon Eurostat (2024), un salarié à temps complet travaille 39,9 heures par semaine en France, contre 40,3 heures dans l'Union européenne et 40,2 heures en Allemagne.", 'ps_temps', '2024', 'France, UE, Allemagne', "L'écart de durée hebdomadaire est faible.", 'etabli', '39,9 heures'),
  fait("Selon Eurostat, 10 % des salariés français travaillent 49 heures ou plus par semaine, contre 7,4 % dans l'Union européenne.", 'ps_temps', '2024', 'France et UE', "Une partie des salariés travaille même davantage qu'ailleurs.", 'etabli', '49 heures'),
  fait("Selon Eurostat, la France est avant-dernière de l'Union européenne pour la durée annuelle effective du travail (2022).", 'ps_temps', '2022', 'UE', "Ce chiffre défavorable existe : il s'explique notamment par les congés et le temps partiel.", 'etabli'),
  fait("Selon le Conseil d'orientation des retraites, le taux d'emploi des 60-64 ans est de 44,4 % en 2025, et à 61 ans 24,5 % des personnes ne sont ni en emploi ni à la retraite, un statut le plus souvent subi pour des raisons de santé ou de handicap.", 'cor26', '2025', 'France', "Le déficit d'heures vient surtout des personnes écartées de l'emploi, pas de la paresse.", 'etabli', '44,4 %'),
 ],
 court="Faux pour ceux qui travaillent : un salarié à temps complet fait 39,9 heures par semaine, contre 40,3 heures en moyenne dans l'UE (Eurostat). Le vrai problème, ce sont les seniors et les jeunes écartés de l'emploi.",
 moyen="Pour ceux qui ont un emploi, la différence est minime : 39,9 heures par semaine à temps complet en France, 40,3 heures dans l'Union européenne, 40,2 heures en Allemagne. Et 10 % des salariés français dépassent 49 heures, plus que la moyenne européenne.\n\nCe qui manque, ce sont des emplois pour certains âges : seuls 44,4 % des 60-64 ans travaillent, et à 61 ans près d'une personne sur quatre n'est ni en emploi ni à la retraite, souvent pour raison de santé. Ce n'est pas un problème de paresse, c'est un problème d'emploi et de conditions de travail.",
 detaille="L'affirmation mélange deux choses. D'abord la durée du travail des personnes en emploi : selon Eurostat (2024), un salarié à temps complet travaille 39,9 heures par semaine en France, contre 40,3 heures dans l'Union européenne et 40,2 heures en Allemagne. La part du temps partiel est même un peu plus faible qu'en moyenne (16,8 % contre 17,8 %), et 10 % des salariés travaillent 49 heures ou plus, contre 7,4 % dans l'UE.\n\nEnsuite la quantité totale de travail : en durée annuelle effective, la France est avant-dernière de l'Union européenne (2022), en raison notamment des congés. Et le taux d'emploi est plus faible aux âges extrêmes : selon le Conseil d'orientation des retraites, 44,4 % des 60-64 ans sont en emploi en 2025, et à 61 ans 24,5 % des personnes ne sont ni en emploi ni à la retraite, le plus souvent pour des raisons de santé ou de handicap.\n\nLa conclusion honnête n'est donc pas que les Français seraient paresseux, mais que le pays laisse de côté une partie de ceux qui voudraient ou pourraient travailler dans de bonnes conditions.",
 empathie="Je comprends qu'on ait cette impression avec les 35 heures et les congés. Mais un salarié à temps plein travaille à peu près autant qu'ailleurs en Europe. Ce qui manque surtout, ce sont des emplois tenables pour les plus âgés, dont beaucoup sont usés ou malades.",
 legitimes=["En durée annuelle effective, la France est avant-dernière de l'Union européenne.", "Le taux d'emploi des 60-64 ans reste nettement plus faible que dans des pays comme la Suède ou le Japon."],
 contre=[
  ("Avec les RTT et les congés, on travaille beaucoup moins.", "C'est vrai sur la durée annuelle ; mais la durée hebdomadaire est proche de la moyenne, et une part plus importante de salariés fait de très longues semaines."),
  ("Les autres pays travaillent plus et s'en sortent mieux.", "La quantité d'heures ne suffit pas : ce qui compte aussi, c'est ce que produit chaque heure travaillée et le nombre de personnes qui ont un emploi."),
 ],
 questions=["Sais-tu combien d'heures fait un salarié à temps plein en France par rapport à l'Allemagne ?", "À 61 ans, pourquoi près d'une personne sur quatre n'est-elle ni en emploi ni à la retraite ?"],
 limites=["Les données d'Eurostat sont citées à partir d'un article de Public Sénat.", "La productivité horaire n'est pas chiffrée dans cette fiche."],
 a_actualiser='2027-06-30',
))

# 6 ── Retraite à 64 ans ─────────────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "Selon le Conseil d'orientation des retraites, le déficit était de 0,1 % du PIB en 2024 et les dépenses resteraient presque stables jusqu'en 2070. Ce n'est pas une faillite : c'est la baisse des ressources qui crée le déficit. Reculer l'âge est un choix politique, pas une obligation, surtout quand un quart des gens ne sont plus en emploi à 61 ans.", 'indecis': "Le financement des retraites est une vraie question. Les chiffres du COR montrent un déficit limité et des dépenses à peu près stables : reculer l'âge est une option parmi d'autres, qui pèse surtout sur ceux dont la santé ne permet pas de travailler plus longtemps."},
 id='retraite-64-ans', affirmation="La retraite à 64 ans est indispensable.", volet='droits', sous_theme='Droits des travailleurs',
 mots_cles=['retraite', 'retraites', '64 ans', 'âge de départ', 'réforme des retraites', 'report de l âge', 'système de retraite', 'cor', 'répartition', 'déficit des retraites'],
 verdict='opinion', fiabilite='interpretation',
 resume="Selon le Conseil d'orientation des retraites, le déficit était de 1,7 milliard d'euros en 2024, soit 0,1 % du PIB, et atteindrait 0,2 % du PIB en 2030. Ce n'est pas une explosion des dépenses : elles passeraient de 13,9 % à 14,2 % du PIB d'ici 2070. Le déficit vient surtout de la baisse des ressources. Reporter l'âge est un choix parmi d'autres : on peut aussi agir sur les recettes.",
 contexte="La réforme de 2023 a porté progressivement l'âge légal de départ de 62 à 64 ans. Ses partisans la jugent indispensable pour équilibrer le système.",
 explication="Le COR projette l'équilibre du système à partir d'hypothèses de croissance, d'emploi et de règles. Le solde dépend autant des recettes (cotisations, contributions de l'État) que des dépenses.",
 sources=[COR_2025, COR_2026],
 faits=[
  fait("Selon le Conseil d'orientation des retraites, le solde du système de retraite était de -1,7 milliard d'euros en 2024, soit -0,1 % du PIB, et serait de -0,2 % du PIB en 2030.", 'cor25', '2024-2030', 'France', "Le déficit existe, mais il est limité à court terme.", 'estimation', '1,7 milliard'),
  fait("Selon la même synthèse, les dépenses de retraite passeraient de 13,9 % du PIB en 2024 à 14,2 % en 2070, tandis que les ressources baisseraient de 13,9 % à 12,8 % du PIB.", 'cor25', '2024-2070', 'France', "Le déséquilibre vient surtout de ressources en baisse, pas de dépenses hors de contrôle.", 'estimation', '14,2 %'),
  fait("Selon la même synthèse, le déficit atteindrait 1,4 % du PIB en 2070.", 'cor25', '2070', 'France', "À long terme, le besoin de financement est réel : il faut le dire.", 'estimation', '1,4 %'),
  fait("Selon le COR, à 61 ans, 24,5 % des personnes ne sont ni en emploi ni à la retraite, dont 14,5 % en mauvaise santé.", 'cor26', '2025', 'France', "Reculer l'âge sans emploi des seniors reporte une partie du coût vers le chômage, la maladie ou les minima sociaux.", 'etabli', '24,5 %'),
 ],
 court="« Indispensable », non : c'est un choix. Le déficit était de 0,1 % du PIB en 2024 selon le COR, et vient surtout de ressources en baisse. D'autres financements sont possibles, et à 61 ans une personne sur quatre n'est déjà ni en emploi ni à la retraite.",
 moyen="Le Conseil d'orientation des retraites ne décrit pas un système en faillite : le déficit était de 1,7 milliard d'euros en 2024, soit 0,1 % du PIB. Les dépenses resteraient presque stables d'ici 2070 (de 13,9 % à 14,2 % du PIB) ; ce sont surtout les ressources qui baisseraient.\n\nReporter l'âge, c'est un choix politique parmi d'autres : on peut aussi augmenter les recettes. Et à 61 ans, près d'une personne sur quatre n'est ni en emploi ni à la retraite, souvent pour raison de santé : reculer l'âge les laisse plus longtemps dans cette situation.",
 detaille="La retraite à 64 ans est présentée comme une nécessité comptable. Les projections du Conseil d'orientation des retraites (juin 2025) montrent un déficit réel mais limité à court terme : -1,7 milliard d'euros en 2024 (-0,1 % du PIB), environ -0,2 % du PIB en 2030. À long terme, le besoin de financement est plus important (-1,4 % du PIB en 2070), et il faut le reconnaître.\n\nMais l'origine du déséquilibre compte : les dépenses passeraient de 13,9 % à 14,2 % du PIB entre 2024 et 2070, tandis que les ressources baisseraient de 13,9 % à 12,8 %. Le problème n'est donc pas une explosion des pensions, mais une baisse des recettes, qui dépend de choix politiques (exonérations, contributions de l'État, niveau des cotisations).\n\nReculer l'âge a aussi un coût humain : selon le COR, à 61 ans, 24,5 % des personnes ne sont ni en emploi ni à la retraite, dont 14,5 % en mauvaise santé. Dire que 64 ans est « indispensable » transforme un choix entre plusieurs options en obligation.",
 empathie="Je comprends qu'on veuille protéger le système, c'est important pour tout le monde. Mais le COR montre que le déficit est surtout un problème de recettes. Il y a d'autres façons de financer les retraites que de faire travailler plus longtemps des gens déjà usés.",
 legitimes=["Le système est en déficit et le besoin de financement augmente à long terme selon le COR.", "Le vieillissement de la population pèse réellement sur l'équilibre du système."],
 contre=[
  ("Il y a de moins en moins d'actifs pour payer les retraites.", "C'est vrai, et c'est une question de partage de la richesse produite : les dépenses restent presque stables en part du PIB selon le COR, ce sont les recettes qui baissent."),
  ("Augmenter les cotisations, ça tue l'emploi.", "C'est un débat ; mais c'est un arbitrage entre plusieurs options, ce qui contredit l'idée d'une solution unique « indispensable »."),
 ],
 questions=["Sais-tu si le déficit des retraites vient plutôt des dépenses ou des recettes, selon le COR ?", "Que deviennent ceux qui ne sont plus en emploi à 61 ans quand on recule l'âge de départ ?"],
 limites=["Les projections du COR dépendent d'hypothèses de croissance et d'emploi.", "Cette fiche ne chiffre pas les autres options de financement."],
 a_actualiser='2027-06-30',
))

# 7 ── Emploi après 50 ans ───────────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "La difficulté est réelle : l'emploi chute après 60 ans (44,4 % des 60-64 ans), et à 61 ans près d'une personne sur quatre n'est ni en emploi ni à la retraite, le plus souvent pour raison de santé. Ce ne sont pas les immigrés ni les jeunes qui en sont la cause : c'est l'usure au travail et les pratiques des employeurs.", 'indecis': "L'emploi des seniors progresse (61,7 % des 55-64 ans en 2025, contre 41 % en 2010), mais il reste bas après 60 ans. La Suède et le Japon font beaucoup mieux : la santé au travail et l'attitude des employeurs sont des leviers concrets."},
 id='emploi-apres-50-ans', affirmation="Pourquoi est-il si difficile de retrouver du travail après 50 ans ?", volet='social', sous_theme='Chômage',
 mots_cles=['après 50 ans', 'seniors', 'plus de 50 ans', 'cinquante ans', 'âge', 'retrouver du travail', 'licenciés', 'trop vieux', 'emploi des seniors', '55 ans'],
 type='reference', verdict=None, fiabilite='etabli',
 resume="L'emploi des seniors progresse : 61,7 % des 55-64 ans travaillent en 2025, contre 41 % en 2010. Mais il chute après 60 ans (44,4 % des 60-64 ans), et à 61 ans près d'une personne sur quatre n'est ni en emploi ni à la retraite, le plus souvent pour des raisons de santé ou de handicap. La difficulté est réelle : elle tient à la santé, à l'usure au travail et aux pratiques des employeurs.",
 contexte="Les licenciements et les ruptures de fin de carrière laissent beaucoup de personnes de plus de 50 ans au chômage longtemps, alors que l'âge de départ recule.",
 explication="Le taux d'emploi des seniors dépend de leur état de santé, de leurs conditions de travail passées et de la volonté des employeurs de les garder ou de les embaucher.",
 sources=[COR_2026, COR_2025],
 faits=[
  fait("Selon le Conseil d'orientation des retraites, 61,7 % des 55-64 ans étaient en emploi en 2025, contre 41 % en 2010 ; 78,8 % des 55-59 ans mais 44,4 % des 60-64 ans.", 'cor26', '2010-2025', 'France', "L'emploi des seniors progresse, mais s'effondre après 60 ans.", 'etabli', '61,7 %'),
  fait("Selon le COR, la Suède atteint 78,3 % et le Japon 79,8 % d'emploi des 55-64 ans.", 'cor26', '2025', 'Comparaison internationale', "D'autres pays font beaucoup mieux : ce n'est pas une fatalité.", 'etabli', '78,3 %'),
  fait("Selon le COR, à 61 ans, 24,5 % des personnes ne sont ni en emploi ni à la retraite, dont 14,5 % en mauvaise santé ; ce statut est le plus souvent subi pour des raisons de santé ou de handicap.", 'cor26', '2025', 'France', "Beaucoup de seniors sans emploi ne l'ont pas choisi.", 'etabli', '14,5 %'),
 ],
 court="Parce qu'après 60 ans, l'emploi s'effondre : 44,4 % des 60-64 ans travaillent, et à 61 ans près d'une personne sur quatre n'est ni en emploi ni à la retraite, souvent pour raison de santé (COR, 2026). Ce n'est pas la volonté qui manque, ce sont des emplois adaptés.",
 moyen="Les chiffres du Conseil d'orientation des retraites confirment ton impression : 78,8 % des 55-59 ans travaillent, mais seulement 44,4 % des 60-64 ans. Et à 61 ans, 24,5 % des personnes ne sont ni en emploi ni à la retraite, le plus souvent pour des raisons de santé ou de handicap.\n\nD'autres pays font beaucoup mieux, comme la Suède ou le Japon, autour de 80 % pour les 55-64 ans. Cela suppose d'adapter les postes, de prévenir l'usure et d'obliger les employeurs à garder et à embaucher des seniors.",
 detaille="La difficulté est bien réelle. Selon le Conseil d'orientation des retraites (rapport 2026), l'emploi des 55-64 ans a beaucoup progressé, de 41 % en 2010 à 61,7 % en 2025, notamment parce que l'âge de départ a reculé. Mais il chute après 60 ans : 78,8 % des 55-59 ans sont en emploi, 44,4 % des 60-64 ans.\n\nÀ 61 ans, 24,5 % des personnes ne sont ni en emploi ni à la retraite, dont 14,5 % en mauvaise santé ; le COR souligne que ce statut est le plus souvent subi pour des raisons de santé ou de handicap. La Suède (78,3 %) et le Japon (79,8 %) montrent que ce n'est pas une fatalité.\n\nLa réponse passe par la prévention de l'usure au travail, l'aménagement des postes et des fins de carrière, et des obligations pour les employeurs, plutôt que par le seul recul de l'âge de départ.",
 empathie="C'est une vraie injustice, et beaucoup de gens la vivent : on vous demande de travailler plus longtemps, mais on ne vous embauche plus. Les chiffres montrent que ce n'est pas toi, c'est un problème général, surtout après 60 ans.",
 legitimes=["L'emploi des 55-64 ans a beaucoup progressé depuis 2010.", "Une partie des seniors sans emploi ont choisi de cesser leur activité."],
 contre=[
  ("Les seniors coûtent trop cher.", "Si c'est le cas, c'est un argument pour aider l'emploi des seniors, pas pour les laisser sans revenus jusqu'à la retraite."),
  ("Ils n'ont qu'à se former.", "Une grande partie des seniors sans emploi sont en mauvaise santé ou handicapés : la formation ne règle pas l'usure."),
 ],
 questions=["Que deviennent les gens usés par leur travail quand on recule l'âge de la retraite ?", "Pourquoi la Suède arrive-t-elle à faire travailler 78 % de ses 55-64 ans ?"],
 limites=["Les sources ne détaillent pas les discriminations à l'embauche liées à l'âge.", "Les comparaisons internationales dépendent aussi de l'âge de départ dans chaque pays."],
 a_actualiser='2027-06-30',
))

# 8 ── Syndicats ─────────────────────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "Les syndicats français sont parmi les plus faibles d'Europe : 11 % de salariés syndiqués, 5 % dans les petites entreprises, contre 23 % en moyenne dans l'UE. Ils ne bloquent pas l'économie : ils négocient les conventions collectives qui couvrent plus de 90 % des salariés du privé, y compris toi.", 'indecis': "Les grèves dans les transports gênent vraiment les usagers, c'est compréhensible d'être agacé. Mais l'essentiel du travail syndical, c'est la négociation des salaires minimaux de branche, des primes et des congés, dont profitent presque tous les salariés."},
 id='syndicats-bloquent', affirmation="Les syndicats empêchent les entreprises de fonctionner.", volet='droits', sous_theme='Droits des travailleurs',
 mots_cles=['syndicats', 'syndicat', 'syndicalistes', 'cgt', 'grèves', 'grève', 'bloquent', 'syndiqués', 'conventions collectives', 'dialogue social'],
 verdict='trompeur', fiabilite='interpretation',
 resume="La France est l'un des pays d'Europe où les salariés sont le moins syndiqués : 11 % en 2013, contre 23 % en moyenne dans l'Union européenne, et 5 % dans les petites entreprises du privé. Pourtant, plus de 90 % des salariés du privé sont couverts par une convention collective négociée par les syndicats. Ils ne bloquent pas l'économie : ils négocient les règles qui s'appliquent à presque tous.",
 contexte="Les grèves dans les transports ou lors des réformes des retraites donnent l'image de syndicats tout-puissants qui paralyseraient le pays.",
 explication="Le taux de syndicalisation mesure les adhérents ; la couverture conventionnelle mesure les salariés qui bénéficient des accords négociés. En France, les deux sont très éloignés : peu d'adhérents, mais des accords qui s'appliquent à presque tous.",
 sources=[DARES_SYND, DARES_2004],
 faits=[
  fait("Selon la Dares, 11 % des salariés adhéraient à un syndicat en 2013 : 20 % dans la fonction publique et 9 % dans le secteur marchand et associatif, contre une moyenne de 23 % dans l'Union européenne.", 'dares_synd', '2013', 'France et UE', "Les syndicats français sont faibles en adhérents, pas tout-puissants.", 'etabli', '11 %'),
  fait("Selon la même étude, la syndicalisation tombe à 5 % dans les établissements marchands de moins de 50 salariés, 2 % chez les salariés en CDD et 1 % chez les intérimaires.", 'dares_synd', '2013', 'France', "Dans la plupart des petites entreprises, il n'y a tout simplement pas de syndicat.", 'etabli', '5 %'),
  fait("Selon la Dares, les conventions collectives couvrent plus de 90 % des salariés du secteur marchand et associatif, et les syndicats négocient au nom de l'ensemble des salariés.", 'dares_synd', '2013', 'France', "Ce que négocient les syndicats profite à presque tous les salariés, syndiqués ou non.", 'etabli', '90 %'),
  fait("Selon la Dares, le taux de syndicalisation est de 18 % dans les transports, l'un des plus élevés du secteur marchand.", 'dares_synd', '2013', 'France', "Les grèves les plus visibles viennent de secteurs où les syndicats sont plus implantés.", 'etabli', '18 %'),
 ],
 court="Faux : seuls 11 % des salariés sont syndiqués, l'un des taux les plus faibles d'Europe, et 5 % dans les petites entreprises. Mais les accords qu'ils négocient couvrent plus de 90 % des salariés du privé (Dares).",
 moyen="Les syndicats français sont parmi les plus faibles d'Europe : 11 % de salariés syndiqués, contre 23 % en moyenne dans l'UE, et seulement 5 % dans les petites entreprises du privé. Dans la plupart des entreprises, il n'y a pas de syndicat du tout.\n\nCe qu'ils font surtout, c'est négocier : les conventions collectives couvrent plus de 90 % des salariés du privé. Les salaires minimaux de branche, les primes, les congés, ça vient de là. Les grèves les plus médiatisées concernent quelques secteurs, comme les transports.",
 detaille="L'image de syndicats qui paralyseraient les entreprises ne correspond pas aux données. Selon la Dares (2016), 11 % des salariés adhéraient à un syndicat en 2013, 9 % dans le secteur marchand, contre 23 % en moyenne dans l'Union européenne. Dans les établissements de moins de 50 salariés du privé, le taux tombe à 5 %, et à 1 ou 2 % chez les intérimaires et les CDD. Une étude plus ancienne de la Dares (2004) situait la France parmi les pays industrialisés les moins syndiqués.\n\nEn revanche, les conventions collectives négociées par les syndicats couvrent plus de 90 % des salariés du secteur marchand et associatif : salaires minimaux de branche, classifications, primes, congés supplémentaires. Ce rôle est discret mais essentiel.\n\nLes grèves les plus visibles se concentrent dans quelques secteurs plus syndiqués, comme les transports (18 %). Elles peuvent gêner les usagers : c'est le prix d'un droit constitutionnel, qui reste l'un des rares moyens de pression des salariés.",
 empathie="Je comprends l'agacement quand une grève bloque les trains. Mais en réalité, les syndicats sont très faibles en France : dans la plupart des entreprises, il n'y en a même pas. Et ce sont eux qui négocient les conventions collectives dont profitent presque tous les salariés.",
 legitimes=["Les grèves dans certains secteurs, comme les transports, gênent réellement les usagers.", "Les chiffres de syndicalisation cités datent de 2013 et de 2003."],
 contre=[
  ("Les syndicats ne font que de la politique.", "La plus grande partie de leur activité est la négociation d'accords de branche et d'entreprise, qui couvrent plus de 90 % des salariés du privé."),
  ("Sans syndicats, les entreprises embaucheraient plus.", "La plupart des petites entreprises n'ont déjà aucun syndicat ; ce n'est donc pas ce qui les empêche d'embaucher."),
 ],
 questions=["Sais-tu combien de salariés sont syndiqués en France, comparé à nos voisins ?", "D'où viennent, selon toi, les salaires minimaux de ta branche professionnelle ?"],
 limites=["Les données de syndicalisation datent de 2013 (Dares, 2016) et de 2003 (Dares, 2004) ; des chiffres plus récents n'ont pas pu être lus pour cette fiche.", "Le nombre de jours de grève n'est pas chiffré ici."],
 a_actualiser='2027-06-30',
))

# 9 ── Nationalité ───────────────────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "La nationalité ne se donne pas : en 2021, 58 % des acquisitions étaient des naturalisations, une décision de l'État réservée aux étrangers en séjour régulier qui remplissent les conditions du Code civil. Un enfant né en France de parents étrangers ne devient français qu'à 18 ans, s'il a grandi ici. Dire « n'importe qui », c'est faux.", 'indecis': "Il est normal de vouloir que la nationalité ait du sens. Les règles existent : naturalisation sous conditions, mariage, ou jeunes nés et élevés en France. En 2021, 130 385 personnes sont devenues françaises, selon l'Insee."},
 id='nationalite-trop-facile', affirmation="Les étrangers obtiennent la nationalité française trop facilement.", volet='immigration', sous_theme='Nationalité et accès aux droits',
 mots_cles=['nationalité', 'naturalisation', 'naturalisés', 'devenir français', 'papiers français', 'droit du sol', 'naturaliser', 'donne la nationalité', 'code civil', 'acquisition de la nationalité'],
 verdict='trompeur', fiabilite='etabli',
 resume="La nationalité ne se donne pas « à n'importe qui ». En 2021, 130 385 personnes l'ont acquise : 58 % par naturalisation, une décision de l'État réservée aux étrangers qui résident régulièrement en France et remplissent des conditions fixées par le Code civil ; les autres surtout par déclaration (mariage, ou jeunes nés et élevés en France).",
 contexte="L'accès à la nationalité est régulièrement présenté comme trop facile, en particulier le « droit du sol » et les naturalisations.",
 explication="Il existe plusieurs voies : la naturalisation par décret, qui est une décision discrétionnaire de l'État ; la déclaration (mariage, jeunes nés en France) ; et l'acquisition automatique à 18 ans pour un jeune né en France qui y a résidé. Le droit du sol français n'est pas automatique à la naissance.",
 sources=[INSEE_NAT, INSEE_IMM],
 faits=[
  fait("Selon l'Insee, 130 385 personnes ont acquis la nationalité française en 2021, dont 75 249 par décret de naturalisation (58 %).", 'insee_nat', '2021', 'France', "Plus de la moitié des acquisitions passent par une décision de l'État.", 'etabli', '130 385'),
  fait("Selon l'Insee, 52 764 personnes sont devenues françaises par déclaration en 2021, dont 17 280 par mariage et 32 727 par déclaration anticipée de jeunes de 13 à 17 ans nés en France.", 'insee_nat', '2021', 'France', "Une grande partie concerne des jeunes nés et élevés en France.", 'etabli', '32 727'),
  fait("Selon l'Insee, la naturalisation est ouverte à « tout étranger qui réside régulièrement en France », sous les conditions des articles 21-15 à 21-27 du Code civil, et un jeune né en France de parents étrangers ne devient français qu'à 18 ans, sous condition de résidence.", 'insee_nat', 'Droit en vigueur en 2023', 'France', "Le droit du sol n'est ni automatique ni immédiat.", 'etabli'),
  fait("Selon l'Insee, 7 615 000 immigrés vivaient en France en 2024, soit 11,2 % de la population.", 'insee_imm', '2024', 'France hors Mayotte', "Les acquisitions annuelles restent faibles au regard de la population immigrée.", 'etabli', '11,2 %'),
 ],
 court="Faux : la naturalisation est une décision de l'État, réservée à ceux qui résident régulièrement en France et remplissent les conditions du Code civil. Un enfant né en France de parents étrangers n'est pas français à la naissance : il peut le devenir à 18 ans s'il y a vécu.",
 moyen="La nationalité ne se distribue pas. En 2021, 130 385 personnes l'ont acquise : 58 % par naturalisation, une décision de l'État qui peut refuser, réservée aux étrangers en situation régulière et soumise aux conditions du Code civil.\n\nLes autres sont surtout des conjoints de Français et des jeunes nés en France : 32 727 déclarations anticipées de 13 à 17 ans. Et contrairement à une idée reçue, naître en France ne rend pas français à la naissance : il faut y avoir vécu, et cela se fait au plus tôt à l'adolescence.",
 detaille="L'idée d'une nationalité trop facile repose souvent sur une mauvaise connaissance des règles. Selon l'Insee, 130 385 personnes ont acquis la nationalité française en 2021. La majorité (75 249, soit 58 %) l'a obtenue par décret de naturalisation : une décision de l'État, réservée à « tout étranger qui réside régulièrement en France » et soumise aux conditions des articles 21-15 à 21-27 du Code civil.\n\nLes autres acquisitions passent surtout par déclaration : 17 280 par mariage avec un Français et 32 727 déclarations anticipées de jeunes de 13 à 17 ans nés en France. Un enfant né en France de parents étrangers ne devient pas français à la naissance : il le devient à 18 ans s'il a résidé en France, ou plus tôt par déclaration.\n\nOn peut débattre des conditions ; mais présenter la nationalité comme donnée sans contrôle est faux.",
 empathie="Je comprends que la question de qui devient français compte beaucoup, c'est ce qui nous relie. Mais la naturalisation est une décision de l'État, avec des conditions, et une bonne partie de ceux qui deviennent français sont des jeunes nés et élevés ici.",
 legitimes=["Le nombre d'acquisitions de la nationalité varie selon les années et selon les choix administratifs.", "Les conditions précises (langue, durée de résidence) relèvent d'un débat politique légitime."],
 contre=[
  ("Avec le droit du sol, il suffit de naître en France.", "Non : un enfant né en France de parents étrangers ne devient français qu'à 18 ans s'il y a résidé, ou plus tôt par déclaration."),
  ("On naturalise des gens qui n'aiment pas la France.", "La naturalisation est une décision au cas par cas, que l'État peut refuser ; l'accusation générale ne repose sur aucune donnée."),
 ],
 questions=["Sais-tu que la naturalisation est une décision que l'État peut refuser ?", "Un enfant né et élevé en France, qui y a fait toute sa scolarité, devrait-il rester étranger ?"],
 limites=["Les chiffres datent de 2021 ; les conditions précises de la naturalisation ne sont pas détaillées ici.", "Les modifications législatives postérieures à 2023 ne sont pas couvertes par cette fiche."],
 a_actualiser='2027-03-31',
))

# 10 ── Accès à la propriété ─────────────────────────────────────────────────
FICHES.append(fiche(
 id='devenir-proprietaire', affirmation="Peut-on encore devenir propriétaire en vivant de son salaire ?", volet='social', sous_theme='Revenus du travail et du patrimoine',
 mots_cles=['propriétaire', 'devenir propriétaire', 'acheter', 'achat immobilier', 'accession', 'immobilier', 'crédit immobilier', 'apport', 'aide familiale'],
 type='reference', verdict=None, fiabilite='estimation',
 resume="C'est devenu beaucoup plus difficile pour les ménages modestes : 32 % des jeunes ménages modestes étaient propriétaires en 1973, contre 16 % en 2013, selon l'Insee. L'aide de la famille compte de plus en plus : dans les années 2000, environ 4 propriétaires récents sur 10 en avaient reçu une. L'accès à la propriété dépend de plus en plus de l'héritage et de moins en moins du salaire.",
 contexte="La hausse des prix de l'immobilier et des taux d'intérêt rend l'achat d'un logement difficile pour beaucoup de jeunes actifs.",
 explication="L'Insee étudie l'accès à la propriété selon les revenus et selon les aides familiales reçues (donations, prêts, héritages). La comparaison sur quarante ans montre une divergence croissante entre ménages modestes et aisés.",
 sources=[INSEE_PROPRIO, CAE_HERITAGE],
 faits=[
  fait("Selon l'Insee, parmi les jeunes ménages modestes, 32 % étaient propriétaires en 1973 contre 16 % en 2013.", 'insee_proprio', '1973-2013', 'France', "L'accès à la propriété des jeunes modestes a été divisé par deux.", 'estimation', '16 %'),
  fait("Selon l'Insee, dans les années 2000, environ 4 propriétaires récents sur 10 avaient reçu une aide familiale, et ces aides ont fortement augmenté chez les ménages aisés.", 'insee_proprio', 'Années 2000', 'France', "La famille, plus que le salaire, fait de plus en plus la différence.", 'estimation'),
  fait("Selon le Conseil d'analyse économique, le patrimoine hérité représente 60 % du patrimoine total, contre environ 35 % au début des années 1970.", 'cae_her', '1970-2020', 'France', "La transmission familiale pèse de plus en plus dans le patrimoine.", 'estimation', '60 %'),
 ],
 court="De plus en plus difficilement : 32 % des jeunes ménages modestes étaient propriétaires en 1973, 16 % en 2013 (Insee). Aujourd'hui, ce qui fait souvent la différence, c'est l'aide de la famille, pas le salaire.",
 moyen="Ton impression est confirmée par l'Insee : parmi les jeunes ménages modestes, la part de propriétaires est passée de 32 % en 1973 à 16 % en 2013.\n\nDans le même temps, l'aide familiale est devenue décisive : environ 4 propriétaires récents sur 10 en avaient reçu une dans les années 2000, et ces aides ont fortement augmenté chez les ménages aisés. Devenir propriétaire dépend de plus en plus de ce qu'on reçoit de ses parents.",
 detaille="Les données de l'Insee (Bonnet, Garbinti et Grobon, 2018) montrent un recul net : parmi les jeunes ménages modestes, 32 % étaient propriétaires en 1973, contre 16 % en 2013. La hausse des prix de l'immobilier a été plus rapide que celle des revenus, et les ménages sans apport ont été écartés.\n\nL'aide familiale est devenue un facteur clé : dans les années 2000, environ 4 propriétaires récents sur 10 avaient reçu une aide de leur famille, et ces aides ont fortement augmenté chez les ménages aisés. Plus largement, le Conseil d'analyse économique estime que le patrimoine hérité représente 60 % du patrimoine total, contre environ 35 % au début des années 1970.\n\nPour un salaire moyen sans aide familiale, l'accès à la propriété est donc beaucoup plus difficile qu'il y a quarante ans. C'est une question de logement abordable et de répartition du patrimoine, pas de mérite individuel.",
 empathie="Tu n'es pas seul à le ressentir : beaucoup de gens qui travaillent ne peuvent plus acheter sans l'aide de leurs parents. Les chiffres de l'Insee montrent que c'est devenu deux fois plus rare pour les jeunes modestes.",
 legitimes=["Les données de l'Insee s'arrêtent en 2013.", "L'accès à la propriété dépend aussi fortement des taux d'intérêt et de la région."],
 contre=[
  ("Il suffit d'épargner.", "Quand les prix augmentent plus vite que les salaires, l'épargne ne suffit plus ; les aides familiales font la différence."),
  ("Il y a des aides publiques pour acheter.", "Elles existent, mais n'ont pas empêché la part de propriétaires parmi les jeunes modestes d'être divisée par deux."),
 ],
 questions=["Combien de propriétaires autour de toi ont acheté sans aucune aide de leur famille ?", "Est-ce normal qu'on dépende de ses parents pour se loger quand on travaille ?"],
 limites=["Les données principales datent de 2013 ; les prix et les taux ont beaucoup évolué depuis.", "Les écarts entre régions ne sont pas détaillés ici."],
 publics={'convaincus': "Tu as raison de trouver que c'est devenu dur : selon l'Insee, 32 % des jeunes ménages modestes étaient propriétaires en 1973, contre 16 % en 2013. Ce qui fait de plus en plus la différence, c'est l'aide de la famille et l'héritage, pas le mérite ni le salaire. Le problème n'est pas que les gens travaillent moins, c'est que le travail ne suffit plus à acheter.",
  'indecis': "Ce n'est pas une impression : la part de jeunes ménages modestes propriétaires a été divisée par deux entre 1973 et 2013. Dans les années 2000, environ quatre propriétaires récents sur dix avaient reçu une aide de leur famille. La question devient celle de l'héritage et du prix du logement plus que celle de l'effort individuel."},
 a_actualiser='2027-12-31',
))

# 11 ── Louer sans CDI ──────────────────────────────────────────────────────
FICHES.append(fiche(
 id='louer-sans-cdi', affirmation="Pourquoi est-il si difficile de louer un logement sans CDI ?", volet='social', sous_theme='Précarité',
 mots_cles=['louer', 'location', 'sans cdi', 'cdi', 'cdd', 'intérim', 'garant', 'caution', 'visale', 'bailleur', 'dossier de location', 'propriétaires'],
 type='reference', verdict=None, fiabilite='etabli',
 resume="Parce que les bailleurs cherchent à se protéger des impayés et privilégient les CDI et les garants. Il existe une garantie publique gratuite, Visale, financée par les employeurs via Action Logement : ouverte sans condition de ressources de 18 à 30 ans, et au-delà pour les salariés récemment embauchés (CDD, intérim, période d'essai) ou gagnant au plus 1 710 € nets. Plus de 1,9 million de ménages en ont bénéficié.",
 contexte="Dans les villes où la demande est forte, les propriétaires choisissent parmi de nombreux dossiers, et les précaires sont souvent écartés.",
 explication="Visale remplace un garant physique : Action Logement paie le bailleur en cas d'impayé. Les bailleurs restent libres de choisir leur locataire, ce qui limite l'effet du dispositif quand le marché est tendu.",
 sources=[QC_VISALE, ANIL_VISALE],
 faits=[
  fait("Selon l'UFC-Que Choisir, la garantie Visale est accessible sans condition de ressources de 18 à 30 ans, y compris aux salariés en CDD, en période d'essai ou aux demandeurs d'emploi.", 'qc_visale', '2026', 'France', "Une solution publique existe pour les jeunes précaires.", 'etabli'),
  fait("Selon le réseau ANIL, depuis le 6 janvier 2026, les salariés du privé de plus de 30 ans y ont droit s'ils gagnent au plus 1 710 € nets par mois, contre 1 500 € auparavant.", 'anil_visale', '2026', 'France', "Le dispositif s'élargit, mais reste ciblé.", 'etabli', '1 710 €'),
  fait("Selon l'UFC-Que Choisir, plus de 1,9 million de ménages ont bénéficié de Visale depuis sa création.", 'qc_visale', '2026', 'France', "Le dispositif est utilisé à grande échelle.", 'etabli', '1,9 million'),
  fait("Selon le réseau ANIL, les plafonds de loyer couverts sont de 1 940 € en Île-de-France, 1 575 € en zone II et 1 365 € ailleurs, et la garantie est limitée au bail initial, 3 ans au maximum.", 'anil_visale', '2026', 'France', "La garantie a des limites de montant et de durée.", 'etabli', '1 940 €'),
 ],
 court="Parce que les bailleurs veulent des garanties et choisissent les CDI quand ils ont le choix. Une caution publique gratuite existe, Visale : sans condition de ressources jusqu'à 30 ans, et pour les salariés récemment embauchés ou modestes au-delà. Mais elle n'oblige pas le bailleur à accepter.",
 moyen="Le problème vient d'un marché où les propriétaires choisissent : face à plusieurs dossiers, ils prennent celui qui leur paraît le plus sûr, souvent un CDI avec un garant.\n\nIl existe pourtant une caution publique gratuite, Visale, financée par les employeurs via Action Logement : ouverte sans condition de ressources de 18 à 30 ans, et au-delà pour les salariés en CDD, en intérim, en période d'essai ou gagnant au plus 1 710 € nets. Plus de 1,9 million de ménages en ont bénéficié. Mais rien n'oblige un bailleur à l'accepter.",
 detaille="Dans les zones tendues, les bailleurs reçoivent de nombreux dossiers et écartent les profils jugés risqués : CDD, intérim, indépendants, personnes sans garant. Ce tri n'est pas une fatalité économique : il découle du déséquilibre entre l'offre et la demande de logements.\n\nUne garantie publique existe : Visale, cautionnement gratuit porté par Action Logement et financé par la participation des employeurs. Elle couvre les impayés de loyers et de charges. Selon l'UFC-Que Choisir, elle est ouverte sans condition de ressources de 18 à 30 ans, et au-delà aux salariés embauchés depuis moins de 6 mois (CDD, intérim, CDI en période d'essai), en mutation ou gagnant au plus 1 710 € nets par mois. Selon le réseau ANIL, les plafonds de loyer couverts ont été relevés en 2026 (1 940 € en Île-de-France) et la garantie dure au plus 3 ans. Plus de 1,9 million de ménages en ont bénéficié.\n\nSa limite principale : le bailleur reste libre de préférer un autre dossier. Pour que les précaires puissent se loger, il faut à la fois des logements abordables en nombre suffisant et des garanties que les bailleurs ne puissent pas écarter.",
 empathie="C'est une situation très frustrante : on travaille, on peut payer, mais on n'a pas le bon contrat. Il existe une caution publique gratuite, Visale, qui peut vraiment aider ; le problème, c'est que les propriétaires ne sont pas obligés de l'accepter.",
 legitimes=["Les bailleurs prennent un risque réel en cas d'impayé, surtout les petits propriétaires.", "Visale ne couvre pas tous les salariés de plus de 30 ans en CDI confirmé."],
 contre=[
  ("Les propriétaires ont le droit de choisir.", "Oui, mais quand tous font le même choix, les précaires sont exclus du logement ; c'est pour cela qu'une garantie publique a été créée."),
  ("Visale suffit, il n'y a plus de problème.", "Le dispositif aide beaucoup, mais il n'oblige pas le bailleur à l'accepter, et il ne crée pas de logements."),
 ],
 questions=["Connais-tu la garantie Visale ?", "Une garantie publique ne devrait-elle pas être acceptée par tous les bailleurs ?"],
 limites=["Les sources sont des articles d'information (ANIL, UFC-Que Choisir), pas le texte officiel des conditions de Visale.", "Aucune donnée chiffrée sur la sélection des locataires selon leur contrat n'est citée ici."],
 publics={'convaincus': "Les bailleurs préfèrent les CDI parce qu'ils craignent les impayés, c'est compréhensible. Mais une caution publique gratuite existe, Visale, dont plus de 1,9 million de ménages ont déjà bénéficié : sans condition de ressources jusqu'à 30 ans. Le vrai problème, c'est qu'elle n'oblige pas le bailleur à accepter.",
  'indecis': 'Pour louer sans CDI, la garantie Visale, gratuite et financée par Action Logement, peut remplacer un garant : sans condition de ressources de 18 à 30 ans, et au-delà pour les salariés récemment embauchés ou gagnant au plus 1 710 € nets. Elle ne règle pas tout, car le bailleur reste libre de choisir son locataire.'},
 a_actualiser='2027-01-31',
))

# 12 ── Pauvreté et efforts ──────────────────────────────────────────────────
FICHES.append(fiche(
 id='pauvres-efforts', affirmation="Les pauvres sont pauvres parce qu'ils ne font pas d'efforts.", volet='social', sous_theme='Pauvreté',
 mots_cles=['pauvres', 'efforts', 'pas d efforts', 'mérite', 'quand on veut on peut', 'responsabilité', 'pauvreté', 'faute', 'fainéants', 'origine sociale'],
 verdict='contredit', fiabilite='etabli',
 resume="La pauvreté ne frappe pas au hasard. Selon l'Insee, en 2023, 21,9 % des enfants vivent sous le seuil de pauvreté — des enfants, qui n'ont pas pu « ne pas faire d'efforts » — et 34,3 % des personnes en famille monoparentale. Et à sexe et âge égaux, un enfant de cadre vit en moyenne avec 1 000 € de plus par mois qu'un enfant d'ouvrier non qualifié, selon France Stratégie.",
 contexte="L'idée que la pauvreté serait une affaire de volonté individuelle revient souvent dans les discussions sur les aides sociales.",
 explication="Le risque de pauvreté dépend de la situation familiale, de l'emploi, de la santé et de l'origine sociale. Les efforts individuels comptent, mais les points de départ sont très inégaux.",
 sources=[INSEE_PAUV_ACT, FS_ORIGINE, INSEE_PAUV],
 faits=[
  fait("Selon l'Insee, en 2023, 21,9 % des enfants de moins de 18 ans et 34,3 % des personnes en famille monoparentale vivent sous le seuil de pauvreté.", 'insee_pauv_act', '2023', 'France', "Une grande partie des pauvres sont des enfants et des familles monoparentales.", 'etabli', '21,9 %'),
  fait("Selon l'Insee, 8,3 % des personnes en emploi vivent sous le seuil de pauvreté en 2023, dont 6,6 % des salariés et 19,2 % des indépendants.", 'insee_pauv_act', '2023', 'France', "Travailler ne suffit pas toujours à sortir de la pauvreté.", 'etabli', '8,3 %'),
  fait("Selon France Stratégie, à sexe, âge et origine migratoire identiques, l'écart moyen de niveau de vie entre un enfant de cadre et un enfant d'ouvrier non qualifié s'élève à 1 000 euros par mois, et un enfant de cadre supérieur a 4,5 fois plus de chances d'appartenir aux 20 % les plus aisés.", 'fs_origine', '2018', 'France', "Le point de départ pèse lourd sur la position d'arrivée.", 'estimation', '1 000 euros'),
  fait("Selon l'Insee, 9 817 000 personnes vivent sous le seuil de pauvreté en 2024 en France métropolitaine, soit 15,4 % de la population.", 'insee_pauv', '2024', 'France métropolitaine', "La pauvreté touche près d'une personne sur six.", 'etabli', '15,4 %'),
 ],
 court="Faux : plus d'un enfant sur cinq est pauvre en France (Insee, 2023), et des salariés aussi. Et à âge égal, un enfant de cadre vit avec 1 000 € de plus par mois qu'un enfant d'ouvrier (France Stratégie). L'effort compte, mais le point de départ pèse lourd.",
 moyen="Regarde qui est pauvre en France : selon l'Insee, 21,9 % des enfants, 34,3 % des personnes en famille monoparentale, et 8,3 % des personnes qui ont un emploi. Ce ne sont pas des gens qui refusent de faire des efforts.\n\nEt l'origine sociale pèse lourd : selon France Stratégie, un enfant de cadre a en moyenne 1 000 € de plus par mois qu'un enfant d'ouvrier non qualifié, et 4,5 fois plus de chances d'être parmi les 20 % les plus aisés. L'effort compte, mais on ne part pas tous de la même ligne.",
 detaille="L'idée que la pauvreté serait une question de volonté se heurte à la composition de la population pauvre. Selon l'Insee, 9 817 000 personnes vivent sous le seuil de pauvreté en France métropolitaine en 2024. En 2023, 21,9 % des enfants et 34,3 % des personnes en famille monoparentale sont pauvres ; 8,3 % des personnes en emploi aussi, et 36,1 % des chômeurs.\n\nL'origine sociale joue fortement : selon France Stratégie (2018), à sexe, âge et origine migratoire identiques, un enfant de cadre a en moyenne un niveau de vie supérieur de 1 000 € par mois à celui d'un enfant d'ouvrier non qualifié, et 4,5 fois plus de chances d'appartenir aux 20 % les plus aisés. La moitié de cet écart passe par l'inégalité des chances à l'école ; à diplôme égal, un écart demeure.\n\nL'effort individuel existe et compte. Mais présenter la pauvreté comme une faute ignore ce que montrent les données : elle dépend largement de la naissance, de la famille et de l'emploi disponible.",
 empathie="Je comprends : quand on s'est battu pour s'en sortir, on a envie de penser que tout le monde peut le faire. Mais plus d'un enfant sur cinq est pauvre en France, et beaucoup de pauvres travaillent. On ne part pas tous avec les mêmes cartes.",
 legitimes=["Les choix individuels, la formation et l'effort influencent réellement les trajectoires.", "Les données de France Stratégie datent de 2018."],
 contre=[
  ("Moi, je suis parti de rien et j'ai réussi.", "C'est possible et respectable, mais les données montrent que c'est beaucoup plus difficile pour un enfant d'ouvrier que pour un enfant de cadre."),
  ("Les aides découragent l'effort.", "Une grande partie des pauvres sont des enfants, des salariés ou des familles monoparentales : ce n'est pas un manque d'effort qui les rend pauvres."),
 ],
 questions=["Un enfant pauvre est-il pauvre parce qu'il ne fait pas d'efforts ?", "À ton avis, pourquoi un enfant de cadre a-t-il 4,5 fois plus de chances d'être parmi les plus aisés ?"],
 limites=["Les chiffres de France Stratégie datent de 2018.", "La pauvreté est mesurée ici de façon monétaire (seuil à 60 % du niveau de vie médian)."],
 publics={'convaincus': "Selon l'Insee, plus d'un enfant sur cinq vit sous le seuil de pauvreté en 2023 : un enfant de dix ans n'a pas « manqué d'efforts ». Et à âge égal, un enfant de cadre vit avec 1 000 € de plus par mois qu'un enfant d'ouvrier non qualifié, selon France Stratégie. L'effort compte, mais tout le monde ne part pas de la même ligne.",
  'indecis': "L'effort compte dans une vie, c'est vrai. Mais la pauvreté touche d'abord des enfants (21,9 % en 2023) et des familles monoparentales (34,3 %), selon l'Insee. Le milieu d'origine pèse lourd : c'est pour cela que l'école, les services publics et la redistribution comptent autant."},
 a_actualiser='2027-07-31',
))

# 13 ── La gauche, les immigrés et les travailleurs ──────────────────────────
FICHES.append(fiche(
 id='gauche-immigres-travailleurs', affirmation="La gauche défend davantage les immigrés que les travailleurs français.", volet='politique', sous_theme='Gauche et pluralisme politique',
 mots_cles=['la gauche', 'gauche', 'défend les immigrés', 'travailleurs français', 'ouvriers', 'classes populaires', 'préfère les immigrés', 'abandonné les ouvriers', 'immigrés', 'travailleurs'],
 verdict='trompeur', fiabilite='interpretation',
 resume="L'opposition est fausse : les immigrés sont eux-mêmes des travailleurs, en emploi à 62,4 % (Insee, 2024), surreprésentés dans les métiers essentiels les plus durs. Les mesures phares des programmes de gauche — SMIC à 1 600 € net, abrogation de la réforme des retraites, hausse du point d'indice — concernent tous les salariés, quelle que soit leur origine. Mais il est vrai qu'une partie des ouvriers vote aujourd'hui davantage pour l'extrême droite.",
 contexte="L'argument oppose « les immigrés » et « les travailleurs français », comme si la gauche avait choisi un camp contre l'autre.",
 explication="Défendre les droits des immigrés et défendre les salariés ne s'opposent pas : un travailleur sans droits est plus facile à sous-payer, ce qui tire les conditions de tous vers le bas. Les programmes se jugent sur les mesures qu'ils contiennent.",
 sources=[INSEE_EMPLOI_IMM, CEPII, LCP_NFP, PS_VOTE, EDO],
 faits=[
  fait("Selon l'Insee, en 2024, le taux d'emploi des immigrés de 15 à 64 ans est de 62,4 %, contre 71,4 % pour les personnes sans ascendance migratoire directe.", 'insee_emploi_imm', '2024', 'France', "Les immigrés sont en majorité des travailleurs.", 'etabli', '62,4 %'),
  fait("Selon le CEPII, les immigrés représentent 23 % des agents d'entretien et des aides à domicile, des métiers essentiels aux conditions de travail difficiles.", 'cepii', '2022', 'France', "Les immigrés sont souvent les travailleurs les plus exposés.", 'estimation', '23 %'),
  fait("Selon LCP, le programme du Nouveau Front populaire (2024) prévoyait le SMIC à 1 600 € net, l'abrogation des réformes des retraites et de l'assurance chômage, et une hausse de 10 % du point d'indice.", 'lcp_nfp', '2024', 'France', "Les mesures phares visent l'ensemble des salariés.", 'etabli', '1 600 €'),
  fait("Selon l'enquête Ipsos-Sopra Steria citée par Public Sénat, au premier tour de 2022, 36 % des ouvriers ont voté pour Marine Le Pen et 23 % pour Jean-Luc Mélenchon.", 'ps_vote', '2022', 'France', "Une partie des classes populaires ne se reconnaît plus dans la gauche : c'est un fait qu'il faut regarder en face.", 'estimation', '36 %'),
  fait("Selon les travaux d'Anthony Edo, une hausse de 10 % de la part des immigrés est associée à court terme à une baisse d'environ 3 % du taux d'emploi des natifs directement en concurrence.", 'edo', '1990-2010', 'France', "Une concurrence ponctuelle existe pour certains travailleurs : la réponse est l'égalité des droits, pas l'opposition entre salariés.", 'estimation', '3 %'),
 ],
 court="Faux choix : les immigrés sont eux-mêmes des travailleurs, en emploi à 62,4 % (Insee), et les mesures phares de la gauche — SMIC à 1 600 € net, retour sur la réforme des retraites — concernent tous les salariés. Un travailleur sans droits, c'est un moyen de faire baisser les salaires de tous.",
 moyen="L'argument suppose qu'il faut choisir entre immigrés et travailleurs. Mais la plupart des immigrés travaillent (62,4 % sont en emploi selon l'Insee), souvent dans les métiers les plus durs : 23 % des agents d'entretien et des aides à domicile.\n\nLes mesures phares du programme de gauche de 2024 — SMIC à 1 600 € net, abrogation de la réforme des retraites, hausse du point d'indice — s'adressent à tous les salariés. Il est vrai que beaucoup d'ouvriers votent aujourd'hui pour l'extrême droite : la gauche doit en tirer les leçons, mais opposer les travailleurs entre eux ne protège personne.",
 detaille="L'affirmation repose sur une opposition entre deux groupes qui se recoupent largement. Selon l'Insee, 62,4 % des immigrés de 15 à 64 ans sont en emploi en 2024. Selon le CEPII, ils sont surreprésentés dans les métiers essentiels peu qualifiés : 23 % des agents d'entretien et des aides à domicile.\n\nLes programmes se jugent sur leurs mesures. Celui du Nouveau Front populaire (2024), selon LCP, prévoyait le SMIC à 1 600 € net, l'abrogation des réformes des retraites et de l'assurance chômage, et une hausse de 10 % du point d'indice : des mesures pour l'ensemble des salariés, sans distinction d'origine.\n\nIl faut reconnaître deux réalités. D'abord, une concurrence ponctuelle existe pour certains travailleurs : les travaux d'Anthony Edo trouvent un effet négatif à court terme sur l'emploi des natifs directement en concurrence. La réponse de gauche est l'égalité des droits et le contrôle des employeurs, pour qu'aucun travailleur ne puisse être sous-payé. Ensuite, une partie des ouvriers vote pour l'extrême droite (36 % pour Marine Le Pen au premier tour de 2022, selon Ipsos) : c'est un défi politique réel pour la gauche.",
 empathie="Je comprends qu'on ait l'impression que la gauche parle plus des immigrés que des fins de mois. Mais quand on regarde ses mesures, SMIC, retraites, salaires, elles concernent tous les travailleurs. Et un immigré exploité, c'est un salaire tiré vers le bas pour tout le monde.",
 legitimes=["Une partie importante des ouvriers vote aujourd'hui pour l'extrême droite plutôt que pour la gauche.", "Une concurrence à court terme existe pour certains travailleurs peu qualifiés, selon des travaux de recherche."],
 contre=[
  ("La gauche parle tout le temps des migrants.", "Les mesures phares de ses programmes portent sur les salaires, les retraites et les services publics ; la perception dépend aussi de ce que retiennent les médias."),
  ("Les immigrés font baisser les salaires.", "Ce qui fait baisser les salaires, c'est le travail sans droits ; la réponse est l'égalité des droits et le contrôle des employeurs."),
 ],
 questions=["Une mesure comme le SMIC à 1 600 € profiterait-elle aux immigrés ou aux Français ?", "Qui a intérêt à ce que les travailleurs français et immigrés se voient comme des adversaires ?"],
 limites=["Les programmes sont présentés tels qu'ils ont été annoncés, pas tels qu'ils auraient été appliqués.", "Les données de vote proviennent d'un sondage à la sortie des urnes."],
 publics={'convaincus': "Les immigrés, ce sont aussi des travailleurs : 62,4 % sont en emploi selon l'Insee, souvent dans les métiers essentiels les plus durs. Le SMIC à 1 600 € net ou le retour sur la réforme des retraites concernent tous les salariés, quelle que soit leur origine. Un travailleur sans droits, c'est un moyen de faire baisser les salaires de tous.",
  'indecis': "Il est vrai qu'une partie des ouvriers vote aujourd'hui davantage pour l'extrême droite, et la gauche doit l'entendre. Mais ses mesures phares, comme la hausse du SMIC ou la retraite, visent tous les salariés. Opposer immigrés et travailleurs, c'est oublier que les premiers sont très souvent les seconds."},
 a_actualiser='2027-06-30',
))


# 14 ── « Grand remplacement » ─────────────────────────────────────────────
FICHES.append(fiche(
 publics={'convaincus': "Les immigrés représentent 11,2 % de la population selon l'Insee, et un tiers d'entre eux sont français. Plus de la moitié des enfants d'immigrés ont un parent qui ne l'est pas : c'est un mélange, pas un remplacement. Appeler « remplaçants » des enfants nés ici, c'est en faire des ennemis dans leur propre pays.", 'indecis': "L'impression que le pays change peut être réelle, surtout dans certains quartiers, et la part des immigrés augmente. Mais elle augmente lentement (6,6 % en 1931, 11,2 % en 2024), et les familles se mélangent. Le « grand remplacement » est une théorie du complot, pas une donnée démographique."},
 id='grand-remplacement', affirmation="Le grand remplacement est une réalité.", volet='immigration', sous_theme='Immigration et démographie',
 mots_cles=['grand remplacement', 'remplacement', 'remplacés', 'remplacer', 'submersion', 'invasion', 'disparition', 'population française', 'remigration', 'immigration'],
 verdict='contredit', fiabilite='etabli',
 resume="Non. L'idée d'un « grand remplacement » suppose qu'une population en remplacerait une autre, de façon organisée. Les chiffres disent autre chose : selon l'Insee, les immigrés représentent 11,2 % de la population en 2024, et parmi les descendants d'immigrés, 55 % n'ont qu'un seul parent immigré : ce n'est pas un remplacement, c'est un mélange. La part des immigrés augmente, mais progressivement : 6,6 % en 1931, 10,3 % en 2021.",
 contexte="L'expression circule notamment dans des discours d'extrême droite pour présenter l'immigration comme un projet de substitution de la population. Elle sert souvent de justification à des propositions de « remigration ».",
 explication="Un immigré est une personne née étrangère à l'étranger et résidant en France ; il peut devenir français. Un descendant d'immigré est né en France, et le plus souvent français. Additionner les deux et les présenter comme une population « de remplacement » revient à exclure de la nation des Français nés en France.",
 sources=[INSEE_IMM, INSEE_HIST],
 faits=[
  fait("Selon l'Insee, la France comptait 7 615 000 immigrés en 2024, soit 11,2 % de la population (10,6 % en 2023), dont 34 % sont de nationalité française.", 'insee_imm', '2024', 'France hors Mayotte', "La population immigrée est une minorité, et un tiers des immigrés sont devenus français.", 'etabli', '11,2 %'),
  fait("Selon l'Insee, 55 % des descendants d'immigrés n'ont qu'un seul parent immigré.", 'insee_imm', '2024', 'France', "Les familles se mélangent : c'est le contraire d'un remplacement.", 'etabli', '55 %'),
  fait("Selon l'Insee, la part des immigrés dans la population est passée de 2,8 % en 1911 à 6,6 % en 1931, 7,4 % en 1975 et 10,3 % en 2021.", 'insee_hist', '1911-2021', 'France', "L'immigration est ancienne et sa progression est lente.", 'etabli', '6,6 %'),
  fait("Selon l'Insee, la part des immigrés est passée de 10,6 % à 11,2 % de la population entre 2023 et 2024.", 'insee_imm', '2023-2024', 'France', "La part des immigrés augmente : il faut le dire, sans en faire un remplacement.", 'etabli', '10,6 %'),
 ],
 court="Non : les immigrés représentent 11,2 % de la population (Insee, 2024), et plus de la moitié des enfants d'immigrés ont un parent qui ne l'est pas. Ce n'est pas un remplacement, c'est un mélange, comme la France en connaît depuis plus d'un siècle.",
 moyen="Les chiffres de l'Insee sont clairs : 11,2 % d'immigrés en 2024, dont un tiers sont français. Et 55 % des descendants d'immigrés n'ont qu'un seul parent immigré : les familles se mélangent.\n\nLa part des immigrés augmente, mais lentement : 6,6 % en 1931, 10,3 % en 2021. Parler de « remplacement », c'est faire des enfants nés en France, souvent français, des étrangers dans leur propre pays.",
 detaille="L'idée d'un « grand remplacement » affirme qu'une population serait remplacée par une autre, de façon organisée. Elle ne résiste pas aux données. Selon l'Insee, la France comptait 7 615 000 immigrés en 2024, soit 11,2 % de la population, dont 34 % de nationalité française. Les descendants d'immigrés sont nés en France ; 55 % d'entre eux n'ont qu'un seul parent immigré.\n\nL'immigration est ancienne : les immigrés représentaient 2,8 % de la population en 1911, 6,6 % en 1931, 7,4 % en 1975 et 10,3 % en 2021. Leur part augmente, de 10,6 % à 11,2 % entre 2023 et 2024 : c'est un fait qu'il faut regarder en face, et qui pose des questions d'accueil, de logement et d'intégration.\n\nMais une hausse progressive n'est pas un « remplacement ». L'expression transforme des voisins, des collègues et des enfants nés en France en ennemis de l'intérieur ; elle relève de la théorie du complot, pas de la démographie.",
 empathie="Je comprends qu'on puisse avoir l'impression que le pays change vite, surtout dans certains quartiers. Mais les chiffres montrent une immigration qui progresse lentement et des familles qui se mélangent. Les enfants nés ici sont français, pas des remplaçants.",
 legitimes=["La part des immigrés dans la population augmente et atteint un niveau historiquement élevé.", "Dans certains territoires, la part des immigrés est bien plus élevée que la moyenne nationale."],
 contre=[
  ("Il suffit de regarder dans la rue.", "L'impression visuelle confond immigrés, descendants nés en France et Français d'outre-mer ; les chiffres de l'Insee mesurent la réalité."),
  ("Les immigrés font plus d'enfants.", "Les descendants d'immigrés sont pour plus de la moitié issus de couples mixtes, et ils sont nés en France : les compter comme des « remplaçants », c'est les exclure de la nation."),
 ],
 questions=["Un enfant né en France d'un parent immigré et d'un parent qui ne l'est pas, c'est un remplaçant ou un Français ?", "Sais-tu quelle était la part des immigrés dans les années 1930 ?"],
 limites=["Les données 2024 sont provisoires.", "Les écarts entre territoires ne sont pas détaillés ici."],
 a_actualiser='2027-03-31',
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
