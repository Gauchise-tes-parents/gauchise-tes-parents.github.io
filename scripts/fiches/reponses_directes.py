"""Fiches « réponses directes » (v9) : affirmations générales fréquentes sans fiche jusqu'ici.

- « On ne peut pas aider tout le monde. »
- « La France n'a plus les moyens de financer ses services publics. »
- « La gauche veut augmenter tous les impôts. »
- « Ce sont les riches qui créent les emplois. »

Sources ouvertes et lues le 30 octobre 2026 (consultee=True), sauf mention contraire dans le passage.
Les chiffres repris d'autres fiches proviennent des mêmes sources, déjà vérifiées.
Usage : python3 scripts/fiches/reponses_directes.py
"""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'library')
TODAY = '2026-10-30'

def src(titre, organisme, date, url, passage, pertinence, type_='primaire', consultee=True):
    return dict(titre=titre, organisme=organisme, date_publication=date, url=url, passage=passage, pertinence=pertinence, type=type_, consultee=consultee)

def fait(texte, source, periode, perimetre, explication, fiabilite='etabli', chiffre=None):
    d = dict(fait=texte, periode=periode, perimetre=perimetre, explication=explication, source=source, fiabilite=fiabilite)
    if chiffre: d['chiffre'] = chiffre
    return d

def fiche(**k):
    sources = k.pop('sources')
    idx = {key: i for i, (key, _) in enumerate(sources)}
    d = dict(
        id=k['id'], type=k.get('type', 'idee_recue'), affirmation=k['affirmation'], volet=k['volet'], sous_theme=k['sous_theme'],
        rubriques=k.get('rubriques', []), mots_cles=k['mots_cles'], verdict=k.get('verdict'), fiabilite=k['fiabilite'], stabilite=k.get('stabilite', 'evolutive'),
        resume=k['resume'], contexte=k['contexte'], explication=k['explication'],
        faits=[{**f, 'source': idx[f['source']]} for f in k['faits']],
        argumentaires=dict(court=k['court'], moyen=k['moyen'], detaille=k['detaille'], empathie=k['empathie']),
        contre_arguments=[dict(objection=o, reponse=r) for o, r in k['contre']],
        questions=k['questions'], limites=k['limites'], sources=[s for _, s in sources],
        derniere_verification=TODAY, a_actualiser_le=k.get('a_actualiser', '2027-06-30'), raison_actualisation=k.get('raison', "Nouvelles données annuelles."),
    )
    if k.get('legitimes'): d['objections_legitimes'] = k['legitimes']
    # v14 : réponses selon le public (électeur d'extrême droite convaincu / personne indécise)
    if k.get('publics'): d['publics'] = k['publics']
    return d

# ── Sources ────────────────────────────────────────────────────────────────
INSEE_REDIS = ('insee_redis', src("Redistribution monétaire (France, portrait social, édition 2025)", "Insee (Insee Références)", "18 novembre 2025",
  "https://www.insee.fr/fr/statistiques/8612544",
  "Données 2024 (enquête Revenus fiscaux et sociaux 2022 actualisée) : la redistribution augmente de 55 % le niveau de vie moyen des 20 % des personnes les plus modestes ; le rapport entre le niveau de vie moyen des 10 % les plus aisés et celui des 10 % les plus modestes passe de 21,1 avant redistribution à 6,2 après ; les prestations contribuent pour environ 60 % à la réduction des inégalités (prime d'activité et minima sociaux 27 %, prestations familiales 20 %, aides au logement 12 %), les prélèvements pour 40 %.",
  "Statistique publique de référence sur l'effet des impôts et prestations."))
OBS_INEG = ('obs_ineg', src("Les allocations réduisent le nombre de pauvres de cinq millions", "Observatoire des inégalités", "16 décembre 2025",
  "https://www.inegalites.fr/Les-allocations-reduisent-le-nombre-de-pauvres-de-cinq-millions",
  "Données 2022 (ministère des Solidarités / DREES, « La redistribution diminue d'un tiers le taux de pauvreté », juin 2025) : au seuil de 60 % du niveau de vie médian, le taux de pauvreté serait de 21,3 % avant redistribution et il est de 14,4 % après ; 13,5 millions de personnes pauvres avant, 9,1 millions après : le système social évite la pauvreté à 4,4 millions de personnes.",
  "Synthèse d'une association indépendante, à partir des données de la DREES.", 'secondaire'))
DREES_MINIMA = ('drees_minima', src("Minima sociaux et prestations de solidarité, édition 2025 — Fiche 07 : Les dépenses d'allocations", "DREES", "Décembre 2025",
  "https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-12/MS2025%20-%20Fiche%2007%20-%20Les%20d%C3%A9penses%20d%27allocations.pdf",
  "Minima sociaux : 31,6 Md€ en 2023, 1,1 % du PIB, 2,0 % des dépenses des administrations publiques ; RSA : 12,2 Md€, 0,4 % du PIB.",
  "Source statistique du ministère des Solidarités."))
NONRECOURS = ('nonrecours', src("Le non-recours au RSA concerne plus d'un tiers des foyers éligibles, confirme la Drees", "Banque des Territoires (Localtis)", "6 mai 2026",
  "https://www.banquedesterritoires.fr/le-non-recours-au-rsa-concerne-plus-dun-tiers-des-foyers-eligibles-confirme-la-drees",
  "Environ 561 000 foyers éligibles non recourants fin 2021, soit 33 % à 37 % ; 34 % en 2018 ; surcoût d'environ 2,5 Md€ sur une année en cas de recours complet.",
  "Compte rendu d'une étude de la DREES.", 'secondaire'))
INSEE_PAUV = ('insee_pauv', src("Niveau de vie et pauvreté en 2024 (Insee Première n° 2117)", "Insee (Christelle Rieg, Arnaud Rousset)", "9 juillet 2026",
  "https://insee.fr/fr/statistiques/9019316",
  "France métropolitaine, 2024 : taux de pauvreté 15,4 % (stable, plus haut niveau depuis 1996) ; 9 817 000 personnes pauvres ; seuil 1 337 € par mois et par unité de consommation.",
  "Statistique publique de référence."))
INSEE_DEP = ('insee_dep', src("Usage de l'argent public : les dépenses publiques par fonction en 2024 (Insee Première n° 2093)", "Insee", "5 février 2026",
  "https://www.insee.fr/fr/statistiques/8735252",
  "Dépenses publiques 1 672 Md€ (57,0 % du PIB) en 2024, +64 Md€ ; protection sociale 693 Md€ (dont retraites +23 Md€) ; santé 261 Md€ ; enseignement 149 Md€ ; charge d'intérêts de la dette 60 Md€ (+13,8 %).",
  "Statistique publique de référence."))
INSEE_APU = ('insee_apu', src("Le compte des administrations publiques en 2024 (Insee Première n° 2054)", "Insee", "28 mai 2025",
  "https://www.insee.fr/fr/statistiques/8574492",
  "« Les recettes moins dynamiques que les dépenses, le déficit augmente ». Déficit public : 168,6 Md€, soit 5,8 % du PIB (5,4 % en 2023) ; dette publique : 113,2 % du PIB ; taux de prélèvements obligatoires : 42,8 % du PIB, en baisse de 0,4 point ; « les recettes des prélèvements obligatoires augmentent moins vite que l'activité en valeur ».",
  "Comptes nationaux officiels."))
SENAT = ('senat', src("Dégradation des finances publiques depuis 2023 (rapport d'information n° 153, commission des finances, rapporteur Jean-François Husson)", "Sénat", "19 novembre 2024",
  "https://senat.fr/rap/r24-153/r24-1531.pdf",
  "Le projet de loi de finances de fin de gestion pour 2024 prévoit « un écart en recettes par rapport aux prévisions du PLF pour 2024 de 41,5 milliards d'euros » ; l'élasticité des recettes prévue à 1,1 serait de 0,71 ; le rapport juge que les erreurs de prévision et les choix politiques ont aussi joué.",
  "Rapport parlementaire de contrôle."))
PS_FISC = ('ps_fisc', src("Programme du Nouveau Front populaire : les pistes de la gauche pour augmenter les recettes fiscales et redistribuer les richesses", "Public Sénat (Hugo Ruaud)", "19 juin 2024",
  "https://www.publicsenat.fr/actualites/politique/programme-du-nouveau-front-populaire-les-pistes-de-la-gauche-pour-augmenter-les-recettes-fiscales-et-redistribuer-les-richesses",
  "Mesures : impôt sur le revenu plus progressif à quatorze tranches au lieu de cinq ; CSG plus progressive ; rétablissement de l'ISF ; impôt sur l'héritage plus progressif ; suppression possible de la flat tax et rétablissement de l'exit tax. Le barème définitif n'est pas détaillé.",
  "Média parlementaire ; présentation du programme.", 'media'))
PS_COUT = ('ps_cout', src("150 milliards de dépenses supplémentaires d'ici fin 2027 : le Nouveau Front populaire détaille le coût de son programme", "Public Sénat", "21 juin 2024",
  "https://www.publicsenat.fr/actualites/economie/150-milliards-de-depenses-supplementaires-dici-fin-2027-le-nouveau-front-populaire-detaille-le-cout-de-son-programme",
  "Recettes annoncées : taxe sur les superprofits 15 Md€ ; ISF jusqu'à 15 Md€ ; suppression de niches fiscales 25 Md€ ; réforme des successions 17 Md€ ; suppression de la flat tax 2,7 Md€ ; barème à 14 tranches et CSG progressive 5,5 Md€.",
  "Média parlementaire ; chiffrages présentés par le NFP.", 'media'))
IFRAP = ('ifrap', src("Le programme fiscal du NFP ferait monter de 20 % les impôts directs des ménages", "Fondation iFRAP (Gilles Koleda)", "9 juillet 2024",
  "https://www.ifrap.org/budget-et-fiscalite/le-programme-fiscal-du-nfp-ferait-monter-de-20-les-impots-directs-des-menages",
  "Simulation : prélèvements directs des ménages +20 % (de 314 à 377 Md€) ; la hausse serait entièrement supportée par les ménages au-dessus d'environ 46 450 € de revenu par an (surtout les trois derniers déciles), le dernier décile (+100 000 € par an) voyant ses impôts directs augmenter de 46 % ; les déciles 6 et 7 ne seraient pas touchés et les déciles inférieurs verraient leur taux baisser.",
  "Think tank libéral, critique du programme : sa propre simulation montre qui paierait.", 'secondaire'))
INSEE_CAT = ('insee_cat', src("Catégories d'entreprises (Les entreprises en France, édition 2023)", "Insee (Insee Références)", "6 décembre 2023",
  "https://www.insee.fr/fr/statistiques/7678530",
  "Données 2021, secteurs marchands non agricoles et non financiers, salariés en équivalent temps plein : microentreprises 2,6 millions (17 %) ; PME hors microentreprises 4,3 millions (29 %) ; ETI 3,7 millions (25 %) ; grandes entreprises 4,2 millions (28 %).",
  "Statistique publique de référence."))
FS_ISF = ('fs_isf', src("Taxation du capital : le bilan 5 ans après la réforme", "Actu-Juridique", "2023",
  "https://www.actu-juridique.fr/fiscalite/fiscal-finances/taxation-du-capital-le-bilan-5-ans-apres-la-reforme/",
  "Compte rendu du rapport final (octobre 2023) du comité d'évaluation des réformes de la fiscalité du capital (France Stratégie) : les dividendes distribués aux ménages passent d'environ 14 Md€ par an (2013-2017) à 23 Md€ (2018-2020) ; les ménages ayant reçu un choc de liquidités « ne les ont pas réinvestis sous forme de participation significative » dans d'autres sociétés ; « légère augmentation du taux d'investissement dans les autres sociétés détenues » ; effet positif sur la décision d'entreprendre.",
  "Compte rendu d'une évaluation publique officielle ; rapport original de France Stratégie.", 'media'))

FICHES = []

# ── 1. On ne peut pas aider tout le monde ─────────────────────────────────
FICHES.append(fiche(
 id='aider-tout-le-monde', affirmation="On ne peut pas aider tout le monde.", volet='social', sous_theme='Coût et efficacité des aides',
 mots_cles=['aider tout le monde', 'on ne peut pas aider', 'solidarité', 'toute la misère du monde', 'pas les moyens d aider', 'aides sociales', 'redistribution', 'assistanat', 'limites', 'protection sociale', 'pauvreté'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Personne ne propose d'aider tout le monde sans limite : la solidarité est déjà organisée, sous conditions, avec un budget. Et elle fonctionne : sans impôts ni prestations, 21,3 % de la population serait pauvre, contre 14,4 % après (données 2022). Les minima sociaux représentent 2 % des dépenses publiques, et un tiers des personnes qui ont droit au RSA ne le demandent pas.",
 contexte="La phrase est vraie au sens littéral : aucune société n'a des ressources illimitées. Mais elle sert souvent à dire autre chose : qu'on aiderait déjà « trop », ou « n'importe qui », ou qu'il faudrait choisir entre les pauvres d'ici et les autres.",
 explication="La vraie question n'est pas « aider tout le monde ou personne », mais qui aider, comment, et avec quel financement. En France, les aides sont conditionnées (ressources, durée de séjour, situation familiale) et budgétées. Leur effet est mesuré : elles réduisent d'un tiers la pauvreté et augmentent de 55 % le niveau de vie des 20 % les plus modestes. Leur coût est limité au regard des grandes masses de la dépense publique (retraites, santé, école).",
 sources=[OBS_INEG, INSEE_REDIS, DREES_MINIMA, NONRECOURS, INSEE_PAUV],
 faits=[
  fait("Sans redistribution, le taux de pauvreté serait de 21,3 % ; après impôts et prestations, il est de 14,4 % : le système social évite la pauvreté à 4,4 millions de personnes.", 'obs_ineg', '2022', 'France, seuil à 60 % du niveau de vie médian', "La solidarité n'aide pas « tout le monde » : elle sort des millions de personnes de la pauvreté. C'est mesuré.", 'etabli', '21,3 % → 14,4 %'),
  fait("La redistribution augmente de 55 % le niveau de vie moyen des 20 % les plus modestes ; l'écart entre les 10 % les plus aisés et les 10 % les plus modestes passe de 21 à 6.", 'insee_redis', '2024', 'France métropolitaine', "Les aides ciblent ceux qui en ont le plus besoin, et leur effet est massif.", 'etabli', '+55 %'),
  fait("Les minima sociaux (RSA, minimum vieillesse, AAH…) coûtent 31,6 Md€, soit 2,0 % des dépenses publiques.", 'drees_minima', '2023', 'France', "L'aide aux plus pauvres est une petite partie de la dépense publique.", 'etabli', '2,0 %'),
  fait("Entre 33 % et 37 % des foyers éligibles au RSA ne le percevaient pas fin 2021, soit environ 561 000 foyers.", 'nonrecours', 'Fin 2021', 'France', "On est loin d'aider « tout le monde » : beaucoup de gens qui ont droit à une aide ne la demandent pas.", 'etabli', '33 à 37 %'),
  fait("Malgré les aides, 15,4 % de la population vit sous le seuil de pauvreté en 2024, soit 9,8 millions de personnes, le plus haut niveau depuis 1996.", 'insee_pauv', '2024', 'France métropolitaine', "Le problème n'est pas qu'on aide trop : la pauvreté reste élevée.", 'etabli', '15,4 %'),
 ],
 court="Personne ne propose d'aider tout le monde sans limite : les aides sont déjà sous conditions et budgétées. Et elles marchent : sans elles, 21 % de la population serait pauvre, contre 14 % (DREES, 2022). Les minima sociaux, c'est 2 % des dépenses publiques, et un tiers des gens qui ont droit au RSA ne le demandent même pas.",
 moyen="« On ne peut pas aider tout le monde », c'est vrai, et personne ne le propose. La question, c'est qui on aide et comment. En France, les aides sont soumises à des conditions et à un budget, et leur effet est mesuré : sans impôts ni prestations, 21,3 % de la population serait pauvre ; avec, c'est 14,4 %. Ça représente 4,4 millions de personnes sorties de la pauvreté.\n\nCe n'est pas ruineux : les minima sociaux pèsent 2 % des dépenses publiques. Et on est loin d'aider « tout le monde » : un tiers des foyers qui ont droit au RSA ne le touchent pas. Malgré tout ça, il reste 9,8 millions de pauvres. Le vrai problème n'est pas qu'on aide trop.",
 detaille="La phrase est vraie au sens littéral : aucune société n'a des moyens illimités. Mais elle sert souvent à justifier qu'on aiderait déjà trop, ou qu'il faudrait choisir entre des pauvres « d'ici » et « d'ailleurs ». Or la solidarité n'est pas un guichet ouvert : elle est organisée, sous conditions (ressources, durée de séjour, situation familiale), et votée chaque année dans un budget.\n\nSon efficacité est mesurée. D'après les données 2022 de la DREES reprises par l'Observatoire des inégalités, la redistribution fait passer le taux de pauvreté de 21,3 % à 14,4 %. Selon l'Insee, elle augmente de 55 % le niveau de vie des 20 % les plus modestes, et les prestations comptent pour environ 60 % de la réduction des inégalités.\n\nSon coût est limité : 31,6 milliards pour les minima sociaux, soit 2 % des dépenses publiques. Les grandes masses de la dépense sont les retraites, la santé et l'école.\n\nEnfin, l'aide ne va pas à « tout le monde » : entre 33 et 37 % des foyers éligibles au RSA ne le demandent pas. Et malgré les aides, 15,4 % de la population vivait sous le seuil de pauvreté en 2024. La vraie discussion porte donc sur les priorités et sur le financement, pas sur un prétendu excès d'aide.",
 empathie="Je comprends qu'on se dise qu'on ne peut pas tout payer : moi aussi je veux que l'argent public soit bien utilisé. Mais les aides sont déjà sous conditions, et elles évitent la pauvreté à plus de 4 millions de personnes. Ce n'est pas aider tout le monde ; c'est éviter que des gens tombent.",
 legitimes=["Les ressources publiques sont limitées et toute dépense doit être financée.", "Le ciblage des aides fait l'objet de vrais débats (conditions, contreparties, simplicité)."],
 contre=[
  ("On paie déjà trop d'impôts pour ça.", "Les minima sociaux représentent 2 % des dépenses publiques. L'essentiel des impôts et cotisations finance les retraites, la santé et l'école, dont tout le monde profite."),
  ("Il y a plein de fraudeurs.", "La fraude existe et doit être combattue ; mais le non-recours est massif : environ un tiers des foyers qui ont droit au RSA ne le demandent pas."),
  ("Il faut d'abord s'occuper des nôtres.", "C'est déjà ce que fait le système : les aides sont soumises à des conditions de ressources et, pour les étrangers non européens, de durée de séjour. Et il reste 9,8 millions de pauvres en France : c'est d'eux qu'on parle."),
 ],
 questions=["Concrètement, qui faudrait-il arrêter d'aider ?", "Tu sais combien représentent les minima sociaux dans la dépense publique ?", "Si on supprimait ces aides, qu'est-ce qui se passerait pour les 4 millions de personnes qu'elles sortent de la pauvreté ?"],
 limites=["Le taux de pauvreté avant redistribution est une construction statistique : sans aides, les comportements seraient différents.", "Les chiffres de non-recours datent de 2021."],
))

# ── 2. Services publics : « plus les moyens » ─────────────────────────────
FICHES.append(fiche(
 id='services-publics-moyens', affirmation="La France n'a plus les moyens de financer ses services publics.", volet='economie', sous_theme='Services publics',
 mots_cles=['services publics', 'plus les moyens', 'pas les moyens', 'financer', 'dette', 'déficit', 'dépenses publiques', 'hôpital', 'école', 'recettes', 'impôts', 'prélèvements obligatoires', 'faillite'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Le déficit est réel (5,8 % du PIB en 2024) et la dette élevée (113,2 %). Mais « ne plus avoir les moyens » est un choix présenté comme une fatalité : en 2024, le taux de prélèvements obligatoires a baissé de 0,4 point et l'État a encaissé 41,5 milliards de moins que prévu. Les moyens dépendent de ce qu'on décide de prélever, et sur qui.",
 contexte="L'argument revient à chaque débat budgétaire, souvent pour justifier des fermetures de services ou des suppressions de postes.",
 explication="Les finances publiques ont deux côtés : les dépenses et les recettes. Le déficit s'est creusé en 2024 parce que les recettes ont progressé moins vite que l'activité, pas seulement parce que les dépenses ont augmenté. Le niveau des recettes dépend de décisions politiques (taux, niches, impôts supprimés ou créés).",
 sources=[INSEE_APU, INSEE_DEP, SENAT],
 faits=[
  fait("En 2024, le déficit public atteint 168,6 Md€, soit 5,8 % du PIB, et la dette 113,2 % du PIB.", 'insee_apu', '2024', 'France', "Le problème budgétaire est réel : il ne faut pas le nier.", 'etabli', '5,8 %'),
  fait("En 2024, le taux de prélèvements obligatoires baisse de 0,4 point, à 42,8 % du PIB : selon l'Insee, les recettes sont « moins dynamiques que les dépenses » et que l'activité.", 'insee_apu', '2024', 'France', "Le déficit vient aussi du côté des recettes.", 'etabli', '42,8 %'),
  fait("Pour 2024, l'écart de recettes par rapport aux prévisions du budget atteint 41,5 milliards d'euros.", 'senat', '2024', 'État', "Une partie du trou vient de recettes surestimées, selon le Sénat.", 'etabli', '41,5 Md€'),
  fait("Les dépenses publiques atteignent 1 672 Md€ en 2024 (57 % du PIB), dont 693 Md€ de protection sociale, 261 Md€ de santé, 149 Md€ d'enseignement et 60 Md€ d'intérêts de la dette.", 'insee_dep', '2024', 'France', "Où va l'argent : surtout les retraites, la santé et l'école.", 'etabli', '1 672 Md€'),
 ],
 court="Le déficit est réel, mais « plus les moyens », c'est un choix déguisé en fatalité : en 2024, les prélèvements obligatoires ont baissé (42,8 % du PIB) et l'État a encaissé 41,5 milliards de moins que prévu (Sénat). Les moyens, ça dépend de ce qu'on décide de prélever, et sur qui.",
 moyen="Oui, il y a un problème budgétaire : 5,8 % de déficit en 2024 et une dette à 113 % du PIB, selon l'Insee. Mais regarde l'autre côté du budget : le taux de prélèvements obligatoires a baissé de 0,4 point en 2024, et l'Insee note que les recettes sont « moins dynamiques que les dépenses ». Le Sénat a calculé que l'État a encaissé 41,5 milliards de moins que prévu.\n\nDonc la question n'est pas « est-ce qu'on a les moyens », mais « qui doit payer, et pour quels services ». Fermer un service public, c'est un choix politique, pas une loi de la nature.",
 detaille="Le constat de départ est juste : en 2024, le déficit public atteint 168,6 milliards d'euros (5,8 % du PIB) et la dette 113,2 % du PIB. Les intérêts de la dette coûtent 60 milliards par an, en forte hausse.\n\nMais un budget a deux côtés. Selon l'Insee, en 2024, « les recettes des prélèvements obligatoires augmentent moins vite que l'activité » : le taux de prélèvements obligatoires recule de 0,4 point, à 42,8 % du PIB. Le rapport du Sénat sur la dégradation des finances publiques relève un écart de 41,5 milliards de recettes par rapport aux prévisions du budget 2024, et souligne que les erreurs de prévision et les choix politiques ont joué.\n\nCôté dépenses, l'essentiel va à la protection sociale (693 milliards, surtout les retraites), à la santé (261 milliards) et à l'école (149 milliards). Dire qu'on « n'a plus les moyens » des services publics, c'est donc choisir de ne pas aller chercher de recettes, ou de les prendre ailleurs. C'est un débat légitime, mais c'est un choix, pas une fatalité.",
 empathie="Je comprends l'inquiétude sur la dette, elle est réelle. Mais le trou ne vient pas que des dépenses : en 2024, les recettes ont été bien plus faibles que prévu. Avant de fermer l'hôpital ou l'école du coin, on peut se demander qui pourrait contribuer davantage.",
 legitimes=["Le déficit (5,8 % du PIB) et la dette (113,2 % du PIB) sont élevés.", "La charge d'intérêts de la dette augmente fortement (60 Md€ en 2024)."],
 contre=[
  ("On a déjà les impôts les plus élevés du monde.", "Les prélèvements sont élevés, mais ils ont baissé en 2024 (42,8 % du PIB) ; et ils financent surtout les retraites et la santé, que d'autres pays paient via des assurances privées."),
  ("La dette, ce sont nos enfants qui vont la payer.", "La dette est un vrai sujet. Mais fermer des écoles ou des hôpitaux, c'est aussi un coût laissé à nos enfants. La question, c'est l'équilibre entre recettes et dépenses, et qui contribue."),
  ("Il suffit de couper dans le gaspillage.", "Les grosses dépenses sont les retraites, la santé et l'école : couper fortement sans toucher aux recettes, c'est forcément toucher à ces services."),
 ],
 questions=["Quand tu dis « plus les moyens », tu as regardé le côté des recettes ?", "Quels services faudrait-il fermer, concrètement ?", "Pourquoi les recettes ont-elles été inférieures de 41,5 milliards à ce qui était prévu ?"],
 limites=["Les chiffres 2025 et 2026 ne sont pas intégrés.", "Le coût total des baisses d'impôts depuis 2017 n'est pas chiffré dans les sources retenues."],
))

# ── 3. La gauche veut augmenter tous les impôts ───────────────────────────
FICHES.append(fiche(
 id='gauche-augmenter-impots', affirmation="La gauche veut augmenter tous les impôts.", volet='economie', sous_theme='Fiscalité',
 mots_cles=['gauche', 'augmenter les impôts', 'tous les impôts', 'matraquage fiscal', 'nfp', 'nouveau front populaire', 'isf', 'impôt sur le revenu', '14 tranches', 'héritage', 'flat tax', 'taxes', 'mélenchon', 'lfi'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Faux tel quel. Le programme du Nouveau Front populaire (2024) prévoyait de fortes hausses d'impôts, mais ciblées : ISF, superprofits, grosses successions, revenus du capital, niches fiscales et hauts revenus. Même l'iFRAP, très critique, calcule que la hausse serait supportée par les ménages au-dessus d'environ 46 450 € de revenu par an, et que les impôts des ménages modestes baisseraient.",
 contexte="Lors des législatives de 2024, le programme fiscal du NFP a été qualifié de « matraquage fiscal » par ses opposants. Il prévoyait des dizaines de milliards de recettes nouvelles.",
 explication="Il faut distinguer « augmenter les impôts au total » (vrai pour le programme NFP) et « augmenter tous les impôts de tout le monde » (faux). Les principales recettes visées étaient l'ISF, une taxe sur les superprofits, les successions importantes et la suppression de niches ; le barème de l'impôt sur le revenu devait devenir plus progressif.",
 sources=[PS_FISC, PS_COUT, IFRAP, FS_ISF],
 faits=[
  fait("Le programme du NFP prévoyait un impôt sur le revenu à 14 tranches au lieu de 5, une CSG plus progressive, le rétablissement de l'ISF, un impôt sur l'héritage plus progressif et la suppression de la flat tax.", 'ps_fisc', '2024', 'Programme du NFP', "La logique est de faire payer davantage les plus aisés, pas tout le monde.", 'etabli'),
  fait("Les recettes annoncées venaient surtout des niches fiscales (25 Md€), des successions (17 Md€), des superprofits (15 Md€) et de l'ISF (jusqu'à 15 Md€) ; le barème de l'impôt sur le revenu et la CSG ne comptaient que pour 5,5 Md€.", 'ps_cout', '2024', 'Programme du NFP (chiffrage du NFP)', "L'impôt payé par la majorité des ménages n'était pas la cible principale.", 'debat', '5,5 Md€'),
  fait("Selon la simulation critique de l'iFRAP, la hausse serait entièrement supportée par les ménages au-dessus d'environ 46 450 € de revenu par an ; les impôts directs du dernier décile augmenteraient de 46 %, ceux des déciles 6 et 7 ne bougeraient pas, et ceux des déciles inférieurs baisseraient.", 'ifrap', '2024', 'Simulation sur la répartition 2023', "Même un think tank opposé au programme montre que la hausse vise les plus aisés.", 'estimation', '46 450 €'),
 ],
 court="Faux : le programme de la gauche en 2024 visait les niches fiscales, l'ISF, les superprofits et les grosses successions. Même l'iFRAP, très critique, calcule que la hausse serait payée par les ménages au-dessus de 46 450 € par an, et que les impôts des ménages modestes baisseraient.",
 moyen="Il faut être précis : oui, le programme du Nouveau Front populaire prévoyait plus de recettes fiscales, et c'est un débat légitime. Mais « tous les impôts », c'est faux. Les grosses recettes venaient des niches fiscales, des successions importantes, des superprofits et de l'ISF. Le barème de l'impôt sur le revenu devenait plus progressif.\n\nEt ce n'est pas la gauche qui le dit : l'iFRAP, un think tank libéral très opposé au programme, a fait le calcul. Selon lui, la hausse retomberait entièrement sur les ménages au-dessus d'environ 46 450 € par an, et les ménages modestes paieraient moins.",
 detaille="L'affirmation mélange deux choses : augmenter les recettes au total, et augmenter les impôts de tout le monde.\n\nLe programme du NFP de 2024 prévoyait bien des hausses importantes. D'après Public Sénat, les recettes annoncées venaient surtout de la suppression de niches fiscales (25 milliards), de la réforme des successions (17 milliards), d'une taxe sur les superprofits (15 milliards) et du rétablissement de l'ISF (jusqu'à 15 milliards). Le nouveau barème de l'impôt sur le revenu à 14 tranches et la CSG progressive ne comptaient que pour 5,5 milliards.\n\nQui aurait payé ? La simulation de l'iFRAP, pourtant hostile au programme, conclut que la hausse serait supportée par les ménages au-dessus d'environ 46 450 € de revenu annuel, surtout les 30 % les plus aisés ; le dernier décile verrait ses impôts directs augmenter de 46 % ; les déciles 6 et 7 seraient inchangés et les plus modestes paieraient moins.\n\nOn peut contester ces choix, leur chiffrage ou leurs effets économiques. Mais dire que la gauche veut augmenter « tous les impôts » ne correspond pas au programme.",
 empathie="Je comprends qu'on se méfie quand on entend parler de milliards d'impôts nouveaux. Mais regarde qui est visé : même l'iFRAP, qui est contre ce programme, calcule que les ménages modestes et moyens ne paieraient pas plus, voire moins.",
 legitimes=["Le programme prévoyait une hausse globale importante des prélèvements.", "Les chiffrages des recettes sont contestés, et les effets économiques (départs, investissement) font débat."],
 contre=[
  ("Ils disent ça, mais au final c'est toujours la classe moyenne qui paie.", "La simulation de l'iFRAP, hostile au programme, place le seuil de hausse vers 46 450 € de revenu annuel et laisse les déciles 6 et 7 inchangés."),
  ("Les riches vont partir.", "Les évaluations de France Stratégie sur l'ISF montrent des départs très limités, et davantage de retours que de départs de contribuables à l'IFI depuis 2018. Le risque existe, mais il est souvent exagéré."),
  ("100 milliards d'impôts en plus, c'est forcément tout le monde.", "Non : les principales recettes visaient les niches, les successions importantes, les superprofits et les grandes fortunes."),
 ],
 questions=["Tu peux me citer un impôt payé par les ménages modestes que le programme augmentait ?", "Tu as vu qui paierait plus selon l'iFRAP, pourtant opposé au programme ?", "Tu préfères qu'on taxe les superprofits ou qu'on ferme des services publics ?"],
 limites=["Les programmes évoluent : il s'agit du programme du NFP de juin 2024.", "Les recettes annoncées sont des estimations du NFP ; la simulation de l'iFRAP repose sur ses propres hypothèses."],
 a_actualiser='2027-03-31', raison="Programmes de 2027 à intégrer.",
))

# ── 4. Les riches créent les emplois ──────────────────────────────────────
FICHES.append(fiche(
 id='riches-creent-emplois', affirmation="Ce sont les riches qui créent les emplois.", volet='economie', sous_theme='Répartition des richesses',
 mots_cles=['riches créent les emplois', 'créent les emplois', 'créateurs d emplois', 'ruissellement', 'premiers de cordée', 'isf', 'dividendes', 'investissement', 'entreprises', 'pme', 'patrons', 'baisse d impôts'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Les emplois sont créés par des entreprises qui ont des clients, et près de la moitié des salariés travaillent dans des microentreprises et des PME, pas chez des milliardaires. Quand on a baissé les impôts des plus riches en 2018 (ISF, flat tax), les dividendes versés aux ménages sont passés de 14 à 23 milliards par an ; l'évaluation officielle n'a pas constaté de réinvestissement massif dans de nouvelles entreprises.",
 contexte="L'argument du « ruissellement » ou des « premiers de cordée » a justifié la transformation de l'ISF en IFI et la création du prélèvement forfaitaire unique (flat tax) en 2018.",
 explication="Créer un emploi suppose une demande : une entreprise embauche quand elle a des commandes. Le capital compte, mais l'enrichissement des plus aisés ne se transforme pas automatiquement en investissement productif. L'évaluation des réformes de 2018 permet de vérifier ce qui s'est passé.",
 sources=[INSEE_CAT, FS_ISF],
 faits=[
  fait("En 2021, les microentreprises emploient 17 % des salariés (en équivalent temps plein) et les PME 29 % ; les grandes entreprises 28 %.", 'insee_cat', '2021', 'Secteurs marchands non agricoles et non financiers', "L'emploi est réparti dans des millions de petites entreprises, pas concentré chez quelques grandes fortunes.", 'etabli', '17 % + 29 %'),
  fait("Après les réformes de 2018 (ISF remplacé par l'IFI, flat tax), les dividendes versés aux ménages passent d'environ 14 Md€ par an (2013-2017) à 23 Md€ (2018-2020).", 'fs_isf', '2013-2020', 'France', "L'argent libéré a d'abord été distribué en dividendes.", 'etabli', '14 → 23 Md€'),
  fait("Selon l'évaluation officielle, les ménages ayant bénéficié de ces liquidités ne les ont pas réinvesties sous forme de participation significative dans d'autres sociétés ; elle note une légère hausse de l'investissement dans les sociétés qu'ils détenaient déjà, et un effet positif sur la décision d'entreprendre.", 'fs_isf', 'Rapport d\'octobre 2023', 'France', "Les effets existent mais restent modestes : on est loin du « ruissellement » promis.", 'estimation'),
 ],
 court="Les emplois, ce sont les entreprises qui les créent quand elles ont des clients, et près de la moitié des salariés travaillent dans des TPE et PME. Quand on a baissé les impôts des plus riches en 2018, les dividendes sont passés de 14 à 23 milliards par an, sans réinvestissement massif selon l'évaluation officielle.",
 moyen="Une entreprise embauche quand elle a des commandes, pas parce que ses actionnaires sont plus riches. Et l'emploi est très éclaté : selon l'Insee, les microentreprises et les PME emploient près de la moitié des salariés.\n\nOn a d'ailleurs fait l'expérience : en 2018, l'ISF a été remplacé par l'IFI et la flat tax a été créée. Résultat mesuré par le comité d'évaluation de France Stratégie : les dividendes versés aux ménages sont passés de 14 à 23 milliards par an, sans réinvestissement massif dans de nouvelles entreprises. Il y a eu un léger effet positif sur la création d'entreprises, mais rien qui ressemble au « ruissellement » promis.",
 detaille="L'idée part d'une intuition : il faut du capital pour créer une entreprise. C'est vrai. Mais il faut surtout des clients : une entreprise embauche quand elle a des commandes.\n\nEt l'emploi est très réparti. En 2021, selon l'Insee, les microentreprises emploient 17 % des salariés en équivalent temps plein, les PME 29 %, les ETI 25 % et les grandes entreprises 28 %.\n\nSurtout, l'argument a été testé. En 2018, l'ISF a été remplacé par un impôt sur la seule fortune immobilière et un prélèvement forfaitaire unique a allégé la taxation des revenus du capital. Le comité d'évaluation placé auprès de France Stratégie a constaté une forte hausse des dividendes versés aux ménages, d'environ 14 milliards par an à 23 milliards. Il n'a pas trouvé de réinvestissement sous forme de participations significatives dans d'autres sociétés, seulement une légère hausse de l'investissement dans les sociétés déjà détenues et un effet positif sur la création d'entreprises.\n\nConclusion : la richesse des plus aisés peut financer des projets, mais elle ne « crée » pas l'emploi à elle seule, et les baisses d'impôts qui leur sont accordées n'ont pas produit l'effet promis.",
 empathie="Je comprends l'idée : sans patrons ni capital, pas d'entreprises. Mais la plupart des emplois sont dans des petites entreprises, et quand on a baissé les impôts des plus riches en 2018, l'argent est surtout parti en dividendes. Ça vaut la peine de regarder ce qui a vraiment marché.",
 legitimes=["Le capital et l'esprit d'entreprise sont nécessaires à la création d'emplois.", "L'évaluation note un effet positif de la réforme de 2018 sur la décision d'entreprendre."],
 contre=[
  ("Sans patrons, il n'y aurait pas d'entreprises.", "Personne ne dit le contraire : mais les patrons de TPE et de PME ne sont pas « les riches » visés par l'ISF, et une entreprise embauche d'abord quand elle a des clients."),
  ("Si on taxe les riches, ils partent et les emplois avec.", "Les évaluations de France Stratégie montrent des départs très limités : depuis 2018, plus de retours que de départs de contribuables à l'IFI."),
  ("Les dividendes, c'est de l'argent réinvesti.", "Selon l'évaluation officielle des réformes de 2018, les ménages n'ont pas réinvesti ces liquidités sous forme de participations significatives dans d'autres sociétés."),
 ],
 questions=["Une entreprise embauche quand ses actionnaires s'enrichissent, ou quand elle a des commandes ?", "Tu sais ce qu'ont donné les baisses d'impôts pour les plus riches en 2018 ?", "Qui crée le plus d'emplois : les milliardaires ou les millions de PME ?"],
 limites=["L'évaluation de 2023 porte sur les premières années après la réforme.", "La source citée est un compte rendu du rapport de France Stratégie."],
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2); fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
