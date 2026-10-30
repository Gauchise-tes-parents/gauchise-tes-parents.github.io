"""Fiches de la base générale (économie, immigration, sécurité, histoire, écologie, médias et démocratie).

Toutes les sources citées ont été ouvertes et lues le 29 octobre 2026.
Usage : python3 scripts/fiches/base_generale.py  (écrit dans data/library/)
"""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'library')
TODAY = '2026-10-29'

def src(titre, organisme, date, url, passage, pertinence, type_='primaire', consultee=True):
    return dict(titre=titre, organisme=organisme, date_publication=date, url=url,
                passage=passage, pertinence=pertinence, type=type_, consultee=consultee)

def fait(texte, source, periode, perimetre, explication, fiabilite='etabli', chiffre=None):
    d = dict(fait=texte, periode=periode, perimetre=perimetre, explication=explication, source=source, fiabilite=fiabilite)
    if chiffre: d['chiffre'] = chiffre
    return d

def fiche(**k):
    sources = k.pop('sources')
    keys = [s[0] for s in sources]
    idx = {key: i for i, key in enumerate(keys)}
    d = dict(
        id=k['id'], type=k.get('type', 'idee_recue'), affirmation=k['affirmation'], volet=k['volet'], sous_theme=k['sous_theme'],
        rubriques=k.get('rubriques', []), mots_cles=k['mots_cles'], verdict=k.get('verdict'), fiabilite=k['fiabilite'],
        stabilite=k['stabilite'], resume=k['resume'], contexte=k['contexte'], explication=k['explication'],
        faits=[{**f, 'source': idx[f['source']]} for f in k['faits']],
        argumentaires=dict(court=k['court'], moyen=k['moyen'], detaille=k['detaille'], empathie=k['empathie']),
        contre_arguments=[dict(objection=o, reponse=r) for o, r in k['contre']],
        questions=k['questions'], limites=k['limites'],
        sources=[s[1] for s in sources],
        derniere_verification=TODAY, a_actualiser_le=k['a_actualiser'], raison_actualisation=k['raison'],
    )
    return d

FICHES = []

# ── Immigration : chiffres et définitions ─────────────────────────────────────
INSEE_IMMI = ('insee_immi', src("Immigrés et descendants d'immigrés (France, portrait social, édition 2025)", "Insee (Insee Références)", "18 novembre 2025",
  "https://www.insee.fr/fr/statistiques/8612512",
  "France hors Mayotte, 2024 (provisoire) : 7 615 000 immigrés, soit 11,2 % de la population (10,6 % en 2023) ; 7 987 000 descendants d'immigrés, soit 12 % de la population en logement ordinaire, dont 55 % n'ont qu'un parent immigré ; 34 % des immigrés sont de nationalité française ; nés en Afrique 48,1 % (Maghreb 29,4 %), en Europe 31,3 %, en Asie 14,5 %, Amérique-Océanie 6,0 %. Définitions de l'immigré et du descendant d'immigré.",
  "Statistique publique de référence."))
FICHES.append(fiche(
 id='immigration-chiffres-definitions', affirmation="Les immigrés, c'est déjà un tiers de la population.",
 volet='immigration', sous_theme='Immigration et démographie', mots_cles=['immigrés', 'immigration', 'étrangers', 'descendants d immigrés', 'grand remplacement', 'submersion', 'insee', 'chiffres', 'définition', 'naturalisés'],
 verdict='contredit', fiabilite='etabli', stabilite='evolutive',
 resume="Selon l'Insee, la France comptait en 2024 environ 7,6 millions d'immigrés, soit 11,2 % de la population, et environ 8 millions de descendants d'immigrés (12 %), dont plus de la moitié n'ont qu'un seul parent immigré. Un tiers des immigrés sont devenus français. On est loin d'« un tiers d'immigrés », et additionner immigrés et descendants revient à compter comme « immigrés » des Français nés en France.",
 contexte="Les débats sur l'immigration mélangent souvent des catégories différentes : immigrés, étrangers, descendants d'immigrés, demandeurs d'asile. Chacune a une définition précise dans la statistique publique.",
 explication="Un immigré est né étranger à l'étranger et réside en France ; il le reste même s'il devient français. Un étranger est une personne qui n'a pas la nationalité française (il peut être né en France). Un descendant d'immigré est né en France d'au moins un parent immigré : il n'est pas immigré lui-même. Un demandeur d'asile demande une protection internationale ; il ne représente qu'une partie des entrées.",
 sources=[INSEE_IMMI],
 faits=[
  fait("En 2024, 7 615 000 immigrés vivent en France (hors Mayotte), soit 11,2 % de la population, contre 10,6 % en 2023.", 'insee_immi', '2024 (provisoire)', 'France hors Mayotte', "La part des immigrés augmente, mais reste d'environ un habitant sur neuf.", 'etabli', '7,6 millions ; 11,2 %'),
  fait("Les descendants d'immigrés (nés en France d'au moins un parent immigré) sont 7 987 000, soit 12 % de la population en logement ordinaire ; 55 % d'entre eux n'ont qu'un seul parent immigré.", 'insee_immi', '2024', 'Population en logement ordinaire', "Ce sont des personnes nées en France, très majoritairement françaises.", 'etabli', '8 millions ; 12 %'),
  fait("34 % des immigrés ont la nationalité française.", 'insee_immi', '2024', 'Immigrés', "« Immigré » et « étranger » ne sont pas synonymes.", 'etabli', '34 %'),
  fait("48,1 % des immigrés sont nés en Afrique (dont 29,4 % au Maghreb), 31,3 % en Europe, 14,5 % en Asie et 6,0 % en Amérique ou en Océanie.", 'insee_immi', '2024', 'Immigrés par région de naissance', "Près d'un immigré sur trois est né en Europe.", 'etabli'),
 ],
 court="Selon l'Insee, les immigrés représentent 11,2 % de la population en 2024, environ 7,6 millions de personnes, et un tiers d'entre eux sont devenus français. On est loin d'un tiers.",
 moyen="Il faut s'entendre sur les mots. Un immigré, c'est quelqu'un né étranger à l'étranger. Selon l'Insee, ils sont 7,6 millions en 2024, soit 11,2 % de la population, et un tiers ont la nationalité française. Les enfants d'immigrés nés en France, eux, ne sont pas immigrés : ils sont 8 millions, et plus de la moitié ont un seul parent immigré. Les additionner pour dire « un tiers d'immigrés », c'est compter comme étrangers des Français nés ici. Et un immigré sur trois est né en Europe.",
 detaille="Les chiffres de l'immigration sont souvent gonflés par confusion des catégories. L'Insee publie chaque année des données précises.\n\nEn 2024, la France (hors Mayotte) compte 7 615 000 immigrés, c'est-à-dire des personnes nées étrangères à l'étranger et résidant en France. Cela représente 11,2 % de la population, en hausse par rapport à 2023 (10,6 %). Un tiers d'entre eux (34 %) ont acquis la nationalité française, tout en restant comptés comme immigrés.\n\nLes descendants d'immigrés sont une autre catégorie : nés en France d'au moins un parent immigré, ils sont 7 987 000, soit 12 % de la population vivant en logement ordinaire. Plus de la moitié (55 %) n'ont qu'un seul parent immigré. Ce ne sont pas des immigrés, et la plupart sont français de naissance.\n\nQuant aux origines, 48,1 % des immigrés sont nés en Afrique (dont 29,4 % au Maghreb), 31,3 % en Europe, 14,5 % en Asie.\n\nLa hausse de la part des immigrés est réelle et légitime à discuter. Mais « un tiers d'immigrés » n'est vrai qu'en additionnant des catégories qui n'ont rien à voir, et en comptant comme étrangers des Français nés en France.",
 empathie="Je comprends que tu aies l'impression que ça change vite ; la part des immigrés augmente, c'est vrai. Mais les chiffres de l'Insee sont plus bas que ce qu'on entend souvent. Et beaucoup de ceux qu'on appelle « immigrés » sont en fait des Français nés ici.",
 contre=[
  ("Si on compte les petits-enfants, ça fait beaucoup plus.", "La statistique ne compte pas les petits-enfants comme immigrés, et c'est logique : ce sont des Français nés de parents nés en France. Les compter, c'est juger les gens sur leurs ancêtres."),
  ("Les chiffres officiels sous-estiment l'immigration clandestine.", "Les sans-papiers sont difficiles à compter, c'est vrai ; mais aucune estimation sérieuse ne permet d'arriver à un tiers de la population."),
 ],
 questions=["Quelqu'un né en France de parents nés en France, mais avec un grand-père algérien, est-il immigré selon toi ?", "Quel chiffre aurais-tu donné avant de voir celui de l'Insee ?"],
 limites=["Données 2023 et 2024 provisoires ; Mayotte exclue.", "La fiche ne traite pas des flux annuels (titres de séjour, demandes d'asile), qui relèvent d'autres sources (ministère de l'Intérieur, OFPRA)."],
 a_actualiser='2026-12-31', raison="L'Insee publie une mise à jour annuelle (novembre).",
))

# ── Pauvreté ─────────────────────────────────────────────────────────────────
INSEE_PAUV = ('insee_pauv', src("Niveau de vie et pauvreté en 2024 (Insee Première n° 2117)", "Insee (Christelle Rieg, Arnaud Rousset)", "9 juillet 2026",
  "https://insee.fr/fr/statistiques/9019316",
  "France métropolitaine, 2024 : taux de pauvreté 15,4 % (stable, plus haut niveau depuis 1996) ; 9 817 000 personnes pauvres ; seuil 1 337 € par mois et par unité de consommation ; indice de Gini 0,302, plus haut depuis 1996.",
  "Statistique publique de référence."))
FICHES.append(fiche(
 id='pauvrete-france', affirmation="Avec toutes nos aides, il n'y a plus vraiment de pauvres en France.",
 volet='social', sous_theme='Pauvreté', mots_cles=['pauvreté', 'pauvres', 'taux de pauvreté', 'seuil de pauvreté', 'inégalités', 'gini', 'niveau de vie', 'insee'],
 verdict='contredit', fiabilite='etabli', stabilite='evolutive',
 resume="Selon l'Insee, 9,8 millions de personnes vivaient sous le seuil de pauvreté en 2024, soit 15,4 % de la population : le plus haut niveau depuis le début de la série en 1996. Le seuil est de 1 337 € par mois pour une personne seule. Les inégalités mesurées par l'indice de Gini sont aussi à leur plus haut depuis 1996.",
 contexte="Le système français de protection sociale réduit fortement la pauvreté par rapport à ce qu'elle serait sans aides ; mais il ne la supprime pas, et le taux de pauvreté monétaire a progressé ces dernières années.",
 explication="Le taux de pauvreté monétaire mesure la part des personnes dont le niveau de vie est inférieur à 60 % du niveau de vie médian. C'est une mesure relative : elle indique qui décroche du reste de la société, après impôts et prestations sociales.",
 sources=[INSEE_PAUV],
 faits=[
  fait("En 2024, 15,4 % de la population de France métropolitaine vit sous le seuil de pauvreté, comme en 2023 : c'est le plus haut niveau depuis 1996.", 'insee_pauv', '2024', 'France métropolitaine, logements ordinaires', "Le chiffre est mesuré après les aides sociales.", 'etabli', '15,4 %'),
  fait("Cela représente 9 817 000 personnes ; le seuil de pauvreté est de 1 337 € par mois et par unité de consommation.", 'insee_pauv', '2024', 'France métropolitaine', "Près d'une personne sur six.", 'etabli', '9,8 millions ; 1 337 €'),
  fait("L'indice de Gini atteint 0,302, en hausse de 0,005 point, son plus haut niveau depuis 1996.", 'insee_pauv', '2024', 'Inégalités de niveau de vie', "Les inégalités progressent malgré la hausse des niveaux de vie.", 'etabli', '0,302'),
 ],
 court="Selon l'Insee, 9,8 millions de personnes sont sous le seuil de pauvreté en 2024, après les aides : 15,4 %, le plus haut niveau depuis 1996. Les aides limitent la pauvreté, elles ne la font pas disparaître.",
 moyen="Les aides font beaucoup, mais elles ne suffisent pas. Selon l'Insee, en 2024, 15,4 % des gens vivent sous le seuil de pauvreté, soit 9,8 millions de personnes, et c'est calculé après les aides. C'est le niveau le plus élevé depuis 1996. Le seuil, c'est 1 337 € par mois pour une personne seule : pas de quoi vivre confortablement. Et les inégalités sont aussi à leur plus haut depuis 1996. Donc oui, il y a encore beaucoup de pauvres, et leur nombre ne baisse pas.",
 detaille="L'idée que les aides auraient fait disparaître la pauvreté ne résiste pas aux chiffres de l'Insee.\n\nEn 2024, 9 817 000 personnes vivent sous le seuil de pauvreté en France métropolitaine, soit 15,4 % de la population. Ce taux est stable par rapport à 2023, mais il s'agit du plus haut niveau depuis le début de la série en 1996. Le seuil de pauvreté correspond à 1 337 € par mois pour une personne seule.\n\nCe calcul est fait après impôts et après prestations sociales : il tient donc compte du RSA, des allocations logement, de la prime d'activité. Les aides réduisent beaucoup la pauvreté, mais elles ne la suppriment pas.\n\nLes inégalités progressent aussi : l'indice de Gini atteint 0,302, son plus haut niveau depuis 1996.\n\nLa pauvreté monétaire est une mesure relative, qu'on peut discuter. Mais elle dit quelque chose de simple : près d'une personne sur six vit avec beaucoup moins que la plupart des gens, et cette proportion n'a pas baissé.",
 empathie="Je comprends qu'on ait l'impression que les aides règlent tout : on en entend beaucoup parler. Mais il y a aujourd'hui près de 10 millions de personnes sous le seuil de pauvreté, aides comprises. Ce sont souvent des travailleurs pauvres, des retraités, des familles monoparentales.",
 contre=[
  ("Être pauvre en France, ce n'est pas être pauvre en Afrique.", "C'est vrai, c'est pourquoi la mesure est relative : elle dit qui décroche du niveau de vie de son pays, où se loger et se nourrir coûte ce que ça coûte ici."),
  ("Le taux de pauvreté monte quand les riches s'enrichissent, c'est un artifice.", "Le seuil dépend du niveau de vie médian, pas des plus riches. Et l'indice de Gini, qui mesure les écarts, monte lui aussi."),
 ],
 questions=["Avec 1 337 € par mois, comment ferais-tu pour te loger dans ta ville ?", "Qui sont, selon toi, les pauvres aujourd'hui en France ?"],
 limites=["Données de France métropolitaine, logements ordinaires (hors sans-abri, personnes en institution).", "La pauvreté monétaire ne mesure pas les privations matérielles, suivies par d'autres indicateurs."],
 a_actualiser='2027-07-31', raison="L'Insee publie ces données chaque année en été.",
))

# ── Justice / prison ─────────────────────────────────────────────────────────
RSJ = ('rsj', src("Références statistiques Justice, édition 2026 — 12.2 Le milieu fermé : les personnes écrouées", "Ministère de la Justice", "Juillet 2026",
  "https://www.justice.gouv.fr/sites/default/files/2026-07/RSJ2026%2012_2.pdf",
  "Au 1er janvier 2026 : 102 347 personnes écrouées (+7,3 %), dont environ 78 % condamnées et 22 % prévenues ; 84 741 personnes détenues (68 359 en 2022) ; densité carcérale 136,1 % (114,5 % en 2022), 163,4 % en maison d'arrêt ; 107 283 incarcérations en 2025.",
  "Statistique officielle du ministère."))
CDJ = ('cdj', src("Nouveau record : le taux de densité carcérale atteint 137 %", "Le Club des juristes (d'après des données du ministère de la Justice relayées par l'AFP)", "3 mars 2026",
  "https://www.leclubdesjuristes.com/en-bref/nouveau-record-le-taux-de-densite-carcerale-atteint-137-14769/",
  "86 645 détenus au 1er février 2026 pour 63 289 places ; densité 136,9 % ; plus de 200 % dans 25 établissements ; 6 596 détenus dormant sur un matelas au sol.",
  "Synthèse juridique de données officielles.", 'media'))
FICHES.append(fiche(
 id='justice-laxiste-prison', affirmation="La justice est laxiste, plus personne ne va en prison.",
 volet='securite', sous_theme='Prisons', mots_cles=['justice', 'laxiste', 'laxisme', 'prison', 'détenus', 'incarcération', 'surpopulation carcérale', 'peine', 'juges'],
 verdict='contredit', fiabilite='etabli', stabilite='evolutive',
 resume="Les prisons françaises n'ont jamais été aussi pleines : 84 741 personnes détenues au 1er janvier 2026, contre 68 359 en 2022, pour une densité de 136,1 % (163,4 % en maison d'arrêt). En 2025, 107 283 personnes ont été incarcérées. On peut débattre de l'exécution des peines ou des courtes peines, mais « plus personne ne va en prison » est contredit par les chiffres du ministère de la Justice.",
 contexte="Le sentiment de laxisme vient souvent de cas médiatisés, de peines aménagées ou non exécutées immédiatement. Dans le même temps, la population carcérale bat record sur record, et la surpopulation est dénoncée par les juridictions et les contrôleurs.",
 explication="Être « écroué » ne signifie pas toujours être en cellule : une partie des personnes écrouées sont placées sous surveillance électronique. Les « détenus » sont ceux qui dorment en prison. La densité carcérale rapporte le nombre de détenus au nombre de places.",
 sources=[RSJ, CDJ],
 faits=[
  fait("Au 1er janvier 2026, 84 741 personnes sont détenues, contre 68 359 au 1er janvier 2022.", 'rsj', '2022-2026', 'France entière', "Hausse de près de 24 % en quatre ans (calcul de la fiche).", 'etabli', '84 741'),
  fait("La densité carcérale atteint 136,1 % au 1er janvier 2026 (114,5 % en 2022) et 163,4 % dans les maisons d'arrêt.", 'rsj', '1er janvier 2026', 'Établissements pénitentiaires', "Les prisons sont surpeuplées.", 'etabli', '136,1 %'),
  fait("En 2025, 107 283 personnes ont été incarcérées ; 102 347 personnes étaient écrouées au 1er janvier 2026, dont environ 78 % condamnées et 22 % en détention provisoire.", 'rsj', '2025-2026', 'France entière', "La prison reste une réponse pénale massive.", 'etabli', '107 283'),
  fait("Au 1er février 2026, 6 596 détenus dorment sur un matelas au sol et la densité dépasse 200 % dans 25 établissements.", 'cdj', '1er février 2026', 'Données du ministère relayées par l\'AFP', "La surpopulation a des conséquences concrètes sur les conditions de détention.", 'etabli', '6 596'),
 ],
 court="Il n'y a jamais eu autant de détenus en France : 84 741 au 1er janvier 2026, contre 68 000 en 2022, avec des prisons pleines à 136 %. On peut discuter de l'efficacité des peines, mais pas dire que personne ne va en prison.",
 moyen="Les chiffres du ministère de la Justice disent l'inverse : au 1er janvier 2026, 84 741 personnes sont en prison, un record, contre 68 359 en 2022. Les prisons sont pleines à 136 %, à plus de 160 % dans les maisons d'arrêt, et des milliers de détenus dorment sur un matelas par terre. Plus de 100 000 personnes ont été incarcérées en 2025. On peut trouver que certaines peines tardent à être exécutées ou que les courtes peines sont mal appliquées, c'est un vrai débat. Mais la justice française n'a jamais autant emprisonné.",
 detaille="L'idée d'une justice qui ne met plus personne en prison est contredite par les statistiques officielles.\n\nAu 1er janvier 2026, 84 741 personnes sont détenues en France, contre 68 359 quatre ans plus tôt. Les prisons comptent environ 63 000 places : la densité carcérale atteint 136,1 %, et 163,4 % dans les maisons d'arrêt, où sont placés les prévenus et les condamnés à de courtes peines. Au 1er février 2026, 6 596 détenus dormaient sur un matelas au sol, et 25 établissements dépassaient 200 % d'occupation.\n\nLe flux est massif : 107 283 incarcérations en 2025. Parmi les personnes écrouées, environ 78 % sont condamnées et 22 % attendent leur jugement en détention provisoire.\n\nLe débat sur la justice reste légitime : délais de jugement, exécution des peines, aménagement des courtes peines, récidive. Mais il ne peut pas partir d'un constat faux. Le problème actuel est plutôt une prison saturée, dont les conditions dégradées compliquent la réinsertion et la prévention de la récidive.",
 empathie="Je comprends la colère quand on entend parler d'un délinquant relâché : ça choque, et ça arrive. Mais globalement, les prisons n'ont jamais été aussi pleines. La vraie question, c'est peut-être : est-ce que la prison, comme elle est aujourd'hui, empêche vraiment la récidive ?",
 contre=[
  ("Beaucoup de peines de prison ne sont jamais exécutées.", "Il existe des délais et des aménagements de peine, et le sujet mérite des chiffres précis ; cette fiche ne les contient pas encore. Mais cela n'empêche pas une population carcérale record."),
  ("S'il y a plus de détenus, c'est qu'il y a plus de délinquants.", "Ça peut jouer, mais la hausse reflète aussi des choix de politique pénale (détention provisoire, peines prononcées). On ne peut pas en même temps dire que la justice est laxiste et que les prisons débordent à cause d'elle."),
 ],
 questions=["Selon toi, combien de personnes sont en prison en France ?", "Qu'est-ce qui protège le mieux contre la récidive ?"],
 limites=["La fiche ne contient pas encore de données sur les condamnations prononcées et le taux d'exécution des peines.", "Les comparaisons internationales (taux de détention par habitant) ne sont pas traitées."],
 a_actualiser='2027-07-31', raison="Statistiques mensuelles et annuelles du ministère de la Justice.",
))

# ── Électricité : nucléaire et renouvelables ─────────────────────────────────
CDE = ('cde', src("95,2 % d'électricité bas carbone en 2025 (d'après le bilan électrique de RTE)", "Connaissance des Énergies", "2026",
  "https://www.connaissancedesenergies.org/la-production-electrique-bas-carbone-de-la-france-atteint-un-maximum-historique-en-2025",
  "Production 547,5 TWh ; nucléaire 373 TWh (68,1 %) ; hydraulique 62,4 TWh (11,4 %) ; éolien 49,6 TWh (9,1 %) ; solaire 32,9 TWh (6 %) ; bioénergies et déchets 10,9 TWh (2 %) ; fossiles 18,7 TWh dont gaz 16,4 TWh (3 %) ; 95,2 % bas carbone ; 19,6 gCO2eq/kWh contre 178 en moyenne européenne élargie.",
  "Site d'information spécialisé reprenant le bilan de RTE.", 'secondaire'))
RTE = ('rte', src("Bilan électrique 2025 — rapport complet", "RTE (gestionnaire du réseau de transport d'électricité)", "2026",
  "https://assets.rte-france.com/analyse-et-donnees/2026-03/BE2025%20-%20Rapport%20Complet.pdf",
  "Consommation corrigée 451,2 TWh (+0,4 %) (p. 6) ; solde exportateur commercial record de 92,3 TWh (p. 11-12) ; nucléaire 373,0 TWh, +11,3 TWh (p. 24) ; 95,2 % de production bas carbone (p. 22).",
  "Bilan officiel du gestionnaire de réseau."))
FICHES.append(fiche(
 id='electricite-nucleaire-renouvelables', affirmation="Notre électricité propre, c'est le nucléaire ; les renouvelables ne servent à rien.",
 volet='ecologie', sous_theme='Énergies renouvelables', mots_cles=['électricité', 'nucléaire', 'renouvelables', 'éolien', 'solaire', 'hydraulique', 'mix énergétique', 'rte', 'émissions', 'co2', 'exportations'],
 verdict='trompeur', fiabilite='etabli', stabilite='evolutive',
 resume="Le nucléaire fournit l'essentiel de l'électricité française : 68,1 % en 2025 (373 TWh) selon RTE. Mais les renouvelables en produisent plus d'un quart (hydraulique 11,4 %, éolien 9,1 %, solaire 6 %, bioénergies 2 %). Ensemble, ils portent la production bas carbone à un record de 95,2 %, avec 19,6 g de CO2 par kWh, contre 178 en moyenne européenne. La France a aussi exporté un solde record de 92,3 TWh.",
 contexte="Le débat oppose souvent nucléaire et renouvelables comme s'il fallait choisir. En pratique, les deux coexistent dans le mix français, et les scénarios de RTE pour 2050 combinent différentes proportions.",
 explication="Le « mix électrique » est la répartition de la production d'électricité par source. Il ne faut pas le confondre avec le mix énergétique total, qui inclut le pétrole et le gaz utilisés dans les transports, le chauffage et l'industrie.",
 sources=[CDE, RTE],
 faits=[
  fait("En 2025, le nucléaire produit 373 TWh, soit 68,1 % de la production d'électricité française (547,5 TWh).", 'cde', '2025', 'France métropolitaine', "Le nucléaire reste de loin la première source.", 'etabli', '68,1 %'),
  fait("L'hydraulique (11,4 %), l'éolien (9,1 %), le solaire (6 %) et les bioénergies (2 %) produisent ensemble plus d'un quart de l'électricité.", 'cde', '2025', 'France métropolitaine', "Les renouvelables ne sont pas marginaux.", 'etabli', '≈ 28,5 % (somme de la fiche)'),
  fait("La production bas carbone atteint un record de 95,2 % ; l'intensité carbone est de 19,6 gCO2eq/kWh, contre 178 en moyenne pour l'Union européenne, la Suisse, la Norvège et le Royaume-Uni.", 'cde', '2025', 'Comparaison européenne', "L'électricité française est parmi les moins carbonées d'Europe.", 'etabli', '95,2 % ; 19,6 g/kWh'),
  fait("Le solde exportateur commercial atteint un record de 92,3 TWh, pour une consommation corrigée de 451,2 TWh.", 'rte', '2025', 'Échanges aux frontières', "La France produit plus qu'elle ne consomme.", 'etabli', '92,3 TWh'),
 ],
 court="Le nucléaire, c'est 68 % de notre électricité en 2025, c'est vrai. Mais l'hydraulique, l'éolien et le solaire en font plus d'un quart. Ensemble, ils nous donnent une électricité à 95 % bas carbone.",
 moyen="Le nucléaire est la base, personne ne le conteste : 68 % de notre électricité en 2025 selon RTE. Mais les renouvelables, ce n'est pas rien : barrages, éoliennes et panneaux solaires produisent plus d'un quart du courant. C'est la combinaison des deux qui donne une électricité à 95 % bas carbone, dix fois moins émettrice que la moyenne européenne. Et on a même exporté un record de 92 TWh. Le vrai débat, c'est comment remplacer le pétrole et le gaz dans les transports et le chauffage, et pour ça il faudra beaucoup plus d'électricité, de toutes les sources bas carbone.",
 detaille="Le bilan électrique 2025 de RTE donne une photographie précise.\n\nLe nucléaire a produit 373 TWh, soit 68,1 % de l'électricité française, en hausse de 3 % sur un an. C'est la colonne vertébrale du système.\n\nMais les renouvelables ont produit plus d'un quart de l'électricité : 62,4 TWh d'hydraulique (11,4 %), 49,6 TWh d'éolien (9,1 %), 32,9 TWh de solaire (6 %) et 10,9 TWh de bioénergies et déchets (2 %). Les énergies fossiles ne représentent plus que 18,7 TWh, dont 16,4 TWh de gaz.\n\nRésultat : 95,2 % de la production est bas carbone, un record historique, et l'intensité carbone tombe à 19,6 g de CO2 par kWh, contre 178 en moyenne pour l'Europe élargie. La France a aussi dégagé un solde exportateur record de 92,3 TWh pour une consommation corrigée de 451,2 TWh.\n\nLe débat utile n'est donc pas « nucléaire contre renouvelables » pour l'électricité d'aujourd'hui, mais la manière d'électrifier les usages qui dépendent encore du pétrole et du gaz, à quel coût et avec quel équilibre entre les sources.",
 empathie="Je suis d'accord avec toi sur un point : le nucléaire est un atout énorme pour la France. Mais on n'est pas obligés de choisir un camp. Les barrages, les éoliennes et le solaire font déjà plus d'un quart du boulot.",
 contre=[
  ("Les éoliennes ne produisent que quand il y a du vent.", "C'est vrai, leur production est variable ; c'est pourquoi on les combine avec le nucléaire, l'hydraulique et les échanges. Sur l'année, elles ont fourni 9,1 % de l'électricité."),
  ("Les renouvelables coûtent cher en subventions.", "Le coût des différentes filières est un vrai débat, qui n'est pas traité dans cette fiche ; il faut le comparer au coût des nouveaux réacteurs, lui aussi élevé."),
 ],
 questions=["Sais-tu quelle part de notre électricité vient des barrages ?", "Selon toi, d'où viendra l'électricité pour les voitures et les pompes à chaleur ?"],
 limites=["La fiche porte sur l'électricité, pas sur l'énergie totale consommée (où pétrole et gaz dominent).", "Les coûts comparés des filières ne sont pas traités."],
 a_actualiser='2027-03-31', raison="RTE publie un bilan électrique chaque année au printemps.",
))

# ── Agriculteurs ─────────────────────────────────────────────────────────────
INSEE_AGRI = ('insee_agri', src("Note presse documentaire — Les agriculteurs", "Insee", "9 février 2024",
  "https://www.insee.fr/fr/information/7765136",
  "2018 (Filosofi) : niveau de vie médian des ménages agricoles 22 200 € par an ; taux de pauvreté 18,1 % contre 15,1 % pour l'ensemble ; 2021 : revenu moyen d'activité 1 860 € par mois pour les non-salariés agricoles au régime réel, 15,6 % de revenus nuls ou négatifs ; pension moyenne fin 2021 des anciens exploitants : 840 € ; patrimoine brut médian des ménages d'agriculteurs actifs début 2018 : 613 700 € ; 2022 : 346 000 non-salariés agricoles.",
  "Synthèse officielle renvoyant aux études de l'Insee, de la DREES et d'Agreste."))
FICHES.append(fiche(
 id='agriculteurs-revenus', affirmation="Les agriculteurs se plaignent, mais avec les subventions ils vivent très bien.",
 volet='ecologie', sous_theme='Agriculture', mots_cles=['agriculteurs', 'paysans', 'revenus agricoles', 'subventions', 'pac', 'pauvreté', 'retraite agricole', 'élevage', 'maraîchage'],
 verdict='trompeur', fiabilite='etabli', stabilite='evolutive',
 resume="Les revenus agricoles sont très inégaux. Selon l'Insee, le taux de pauvreté des ménages agricoles était de 18,1 % en 2018, contre 15,1 % pour l'ensemble des ménages ; en 2021, 15,6 % des exploitants au régime réel déclaraient un revenu nul ou négatif, et la pension moyenne des anciens exploitants était de 840 € fin 2021. Mais les agriculteurs détiennent souvent un patrimoine professionnel important (patrimoine brut médian de 613 700 € en 2018), qui n'est pas un revenu disponible.",
 contexte="Les mobilisations agricoles de 2024 ont remis en lumière la question des revenus. Le secteur est très hétérogène : grandes cultures, viticulture, élevage, maraîchage n'ont pas les mêmes résultats.",
 explication="Le revenu agricole varie fortement d'une année et d'une filière à l'autre. Le patrimoine (terres, bâtiments, matériel) sert à produire : il est souvent financé par l'emprunt et ne se transforme en revenu qu'à la vente, en général au départ en retraite.",
 sources=[INSEE_AGRI],
 faits=[
  fait("En 2018, le taux de pauvreté des ménages agricoles était de 18,1 %, contre 15,1 % pour l'ensemble des ménages ; la moitié d'entre eux avaient un niveau de vie inférieur à 22 200 € par an.", 'insee_agri', '2018', 'Ménages agricoles (Filosofi)', "La pauvreté est plus fréquente chez les agriculteurs que dans la population.", 'etabli', '18,1 %'),
  fait("En 2021, les non-salariés agricoles au régime réel gagnaient en moyenne 1 860 € par mois de leur activité ; 15,6 % déclaraient un revenu nul ou négatif.", 'insee_agri', '2021', 'Environ 290 000 non-salariés agricoles au régime réel', "Un exploitant sur six ne dégage aucun revenu certaines années.", 'etabli', '1 860 € ; 15,6 %'),
  fait("Fin 2021, la pension moyenne des anciens exploitants agricoles (à titre principal) était de 840 € par mois, et de 930 € pour une carrière complète.", 'insee_agri', 'Fin 2021', 'Retraités anciens exploitants (DREES)', "Les retraites agricoles sont parmi les plus faibles.", 'etabli', '840 €'),
  fait("Début 2018, la moitié des ménages d'agriculteurs actifs détenaient un patrimoine brut supérieur à 613 700 €, en grande partie professionnel.", 'insee_agri', 'Début 2018', 'Ménages d\'agriculteurs actifs', "Un patrimoine élevé peut coexister avec un faible revenu.", 'etabli', '613 700 €'),
 ],
 court="Selon l'Insee, les agriculteurs sont plus souvent pauvres que la moyenne, un sur six n'a aucun revenu certaines années, et la retraite moyenne d'un ancien exploitant tourne autour de 840 €. Il y a des agriculteurs aisés, mais beaucoup vivent mal.",
 moyen="Ça dépend énormément des agriculteurs. Selon l'Insee, 18 % des ménages agricoles étaient pauvres en 2018, plus que la moyenne. En 2021, un exploitant sur six déclarait un revenu nul ou négatif, et la retraite moyenne d'un ancien exploitant était de 840 € par mois. Les subventions de la PAC existent, mais elles ne suffisent pas à garantir un revenu à tous. C'est vrai que beaucoup d'agriculteurs ont un patrimoine important, mais ce sont des terres, des bâtiments et des machines, souvent achetés à crédit : ça ne paie pas les courses.",
 detaille="Les revenus agricoles sont parmi les plus inégaux et les plus instables de la société française.\n\nSelon l'Insee, en 2018, le taux de pauvreté des ménages agricoles atteignait 18,1 %, contre 15,1 % pour l'ensemble des ménages. En 2021, les exploitants au régime réel tiraient en moyenne 1 860 € par mois de leur activité, mais 15,6 % déclaraient un revenu nul ou négatif. Les situations varient selon les filières : en 2022, la part d'exploitations à l'excédent brut négatif était bien plus élevée dans le maraîchage et la viticulture que la moyenne, selon le ministère de l'Agriculture.\n\nÀ la retraite, la pension moyenne d'un ancien exploitant était de 840 € fin 2021.\n\nIl serait faux de dire que tous les agriculteurs sont pauvres : certains, notamment dans les grandes exploitations, gagnent bien leur vie, et la moitié des ménages d'agriculteurs actifs détenaient en 2018 un patrimoine brut de plus de 613 700 €. Mais ce patrimoine est l'outil de travail, souvent endetté.\n\nLa question de fond est celle des prix payés aux producteurs et du partage de la valeur avec l'industrie agroalimentaire et la grande distribution, qui dépasse le seul sujet des subventions.",
 empathie="Je comprends qu'on entende beaucoup parler des subventions. Mais quand on regarde les chiffres, beaucoup d'agriculteurs ont du mal à se payer, et leurs retraites sont très faibles. Ce sont eux qui nous nourrissent.",
 contre=[
  ("Les gros céréaliers touchent l'essentiel des aides.", "La répartition des aides de la PAC est un vrai sujet de débat ; elle n'est pas chiffrée dans cette fiche. Elle illustre justement les inégalités au sein du monde agricole."),
  ("Avec leur patrimoine, ils sont riches.", "Le patrimoine professionnel sert à produire et est souvent financé par l'emprunt : il ne se dépense pas au quotidien."),
 ],
 questions=["Sais-tu combien touche un agriculteur à la retraite ?", "Qui, selon toi, capte la valeur entre le champ et le supermarché ?"],
 limites=["Les données datent de 2018 à 2022 : elles doivent être actualisées avec les publications plus récentes de l'Insee et d'Agreste.", "Les définitions de l'agriculteur diffèrent selon les études (revenu fiscal agricole ou profession déclarée)."],
 a_actualiser='2027-01-31', raison="Données anciennes (2018-2022) à actualiser en priorité.",
))

# ── Dividendes et salaires ───────────────────────────────────────────────────
INSEE_CN = ('insee_cn', src("Les comptes de la Nation en 2025 (Insee Première n° 2105)", "Insee", "29 mai 2026",
  "https://www.insee.fr/fr/statistiques/8996855",
  "Croissance +0,8 % en 2025 ; taux de marge des sociétés non financières 32,2 % (−0,5 point) ; dividendes versés par les SNF −6,4 Md€ en 2025 après +8,3 Md€ en 2024 ; dividendes reçus par les ménages −10,5 Md€ après +13,9 Md€ (anticipation de la contribution sur les hauts revenus) ; rémunérations versées par les SNF +20,0 Md€ ; pouvoir d'achat par unité de consommation −0,7 %.",
  "Comptabilité nationale officielle."))
JANUS = ('janus', src("Dividendes : la France numéro 1 en Europe et numéro 2 mondial au deuxième trimestre 2026", "Toutsurmesfinances.com (d'après l'étude trimestrielle de Janus Henderson)", "16 septembre 2026",
  "https://www.toutsurmesfinances.com/actualites/?p=1934",
  "Deuxième trimestre 2026 : 70,4 Md$ (environ 61 Md€) de dividendes versés par les entreprises françaises cotées, +7,2 % sur un an (−0,8 % hors effets exceptionnels) ; 29 % des dividendes européens hors Royaume-Uni ; dividende exceptionnel de Bolloré SE.",
  "Étude d'un gestionnaire d'actifs reprise par la presse financière ; périmètre : grandes entreprises cotées.", 'media'))
FICHES.append(fiche(
 id='dividendes-salaires', affirmation="Les entreprises n'ont pas les moyens d'augmenter les salaires.",
 volet='economie', sous_theme='Dividendes', mots_cles=['dividendes', 'salaires', 'actionnaires', 'profits', 'taux de marge', 'valeur ajoutée', 'partage de la valeur', 'cac 40', 'pouvoir d achat'],
 verdict='trompeur', fiabilite='estimation', stabilite='actualite',
 resume="La situation dépend des entreprises. Les grandes entreprises cotées françaises ont versé environ 61 Md€ de dividendes au seul deuxième trimestre 2026 (étude Janus Henderson), un niveau qui place la France en tête en Europe. Pour l'ensemble des sociétés non financières, le taux de marge reste élevé (32,2 % en 2025 selon l'Insee), en léger recul. Beaucoup de petites entreprises ont des marges faibles ; mais « les entreprises » en général ne manquent pas toutes de moyens.",
 contexte="Le débat sur le partage de la valeur oppose rémunération du travail (salaires) et du capital (dividendes, investissement). En 2025, le pouvoir d'achat par unité de consommation a reculé de 0,7 % selon l'Insee.",
 explication="Le taux de marge mesure la part de la valeur ajoutée qui reste à l'entreprise après avoir payé salaires et impôts sur la production ; il sert à investir, rembourser, payer des impôts et verser des dividendes. Les dividendes sont la part des profits distribuée aux actionnaires.",
 sources=[JANUS, INSEE_CN],
 faits=[
  fait("Au deuxième trimestre 2026, les entreprises françaises cotées ont versé 70,4 Md$ (environ 61 Md€) de dividendes, +7,2 % sur un an, soit 29 % des dividendes européens hors Royaume-Uni.", 'janus', 'T2 2026', 'Grandes entreprises cotées (étude Janus Henderson)', "Les grands groupes distribuent des montants très élevés.", 'estimation', '≈ 61 Md€ en un trimestre'),
  fait("Hors effets exceptionnels (dont un dividende exceptionnel de Bolloré SE), la progression sous-jacente est de −0,8 %.", 'janus', 'T2 2026', 'Même étude', "Le niveau est élevé, mais pas en hausse continue.", 'estimation'),
  fait("En 2025, le taux de marge des sociétés non financières est de 32,2 %, en baisse de 0,5 point ; leurs dividendes versés reculent de 6,4 Md€ après +8,3 Md€ en 2024, et leurs rémunérations versées augmentent de 20,0 Md€.", 'insee_cn', '2025', 'Sociétés non financières (comptabilité nationale)', "Les marges restent substantielles en moyenne, avec des évolutions contrastées.", 'etabli', '32,2 %'),
  fait("Le pouvoir d'achat du revenu disponible par unité de consommation recule de 0,7 % en 2025.", 'insee_cn', '2025', 'Ménages', "Les ménages ont perdu du pouvoir d'achat cette année-là.", 'etabli', '−0,7 %'),
 ],
 court="Les grandes entreprises françaises ont versé environ 61 milliards d'euros de dividendes en un seul trimestre de 2026. Toutes les PME ne sont pas riches, mais dire que « les entreprises » n'ont pas les moyens, c'est faux pour les plus grandes.",
 moyen="Ça dépend de quelles entreprises on parle. Pour une petite boulangerie, augmenter les salaires peut être dur, c'est vrai. Mais les grandes entreprises cotées françaises ont versé environ 61 milliards d'euros de dividendes au deuxième trimestre 2026, plus que n'importe quel autre pays européen. Et en moyenne, les sociétés gardent une marge d'environ un tiers de leur valeur ajoutée selon l'Insee. Pendant ce temps, le pouvoir d'achat des ménages a reculé en 2025. La question n'est donc pas seulement « ont-elles les moyens ? », mais « comment la richesse produite est-elle partagée ? ».",
 detaille="L'argument mélange des entreprises très différentes.\n\nDu côté des grands groupes, les chiffres sont élevés : selon l'étude trimestrielle de Janus Henderson, les entreprises françaises cotées ont versé 70,4 Md$, soit environ 61 Md€, de dividendes au deuxième trimestre 2026, plaçant la France en tête en Europe (29 % des dividendes européens hors Royaume-Uni). Une partie vient d'un dividende exceptionnel ; hors effets exceptionnels, la tendance sous-jacente est stable (−0,8 %).\n\nPour l'ensemble des sociétés non financières, l'Insee mesure un taux de marge de 32,2 % en 2025, en léger recul. En 2025, les dividendes versés par ces sociétés ont baissé de 6,4 Md€ après une hausse de 8,3 Md€ en 2024, tandis que les rémunérations versées ont progressé de 20 Md€. Le pouvoir d'achat par unité de consommation a reculé de 0,7 %.\n\nCes données ne disent pas que toutes les entreprises peuvent augmenter les salaires : beaucoup de PME ont des marges faibles. Elles montrent en revanche que, pour une partie importante de l'économie, la question est un choix de partage entre salaires, investissement et rémunération des actionnaires. C'est précisément l'objet du débat politique.",
 empathie="Je comprends qu'on pense d'abord aux petits patrons qui galèrent ; certains n'ont vraiment pas les moyens. Mais les très grandes entreprises, elles, versent des dizaines de milliards aux actionnaires. On peut aider les petites et demander plus aux grandes.",
 contre=[
  ("Les dividendes rémunèrent le risque et financent les retraites des épargnants.", "C'est leur fonction ; mais une part importante va à des actionnaires fortunés ou étrangers, et le niveau de distribution par rapport aux salaires reste un choix discutable."),
  ("Si on taxe les dividendes, les entreprises investiront moins.", "C'est un argument sérieux et débattu par les économistes ; les effets dépendent de la mesure exacte."),
 ],
 questions=["Selon toi, qui devrait profiter en priorité des bénéfices d'une entreprise ?", "Faut-il traiter de la même façon une PME et un grand groupe du CAC 40 ?"],
 limites=["Le chiffre trimestriel de dividendes porte sur les grandes entreprises cotées et provient d'un gestionnaire d'actifs privé, via la presse financière.", "La fiche ne contient pas l'évolution longue du partage de la valeur ajoutée entre salaires et profits."],
 a_actualiser='2027-03-31', raison="Données trimestrielles et annuelles qui évoluent vite.",
))

# ── Médias ───────────────────────────────────────────────────────────────────
SENAT_MED = ('senat_med', src("Concentration des médias : divisés, les sénateurs s'accordent malgré tout sur les préconisations du rapport", "Public Sénat", "31 mars 2022",
  "https://www.publicsenat.fr/actualites/politique/concentration-des-medias-les-senateurs-se-divisent-sur-les-preconisations",
  "Rapport de la commission d'enquête du Sénat (président Laurent Lafon, rapporteur David Assouline), 380 pages, adopté à l'unanimité, 32 propositions ; auditions de Vincent Bolloré, Bernard Arnault, Arnaud Lagardère, Patrick Drahi, Xavier Niel, Martin Bouygues ; Bernard Arnault : « Je n'ai pas envie de financer un journal qui devienne le support de l'extrême droite ou de l'extrême gauche. »",
  "Média parlementaire rendant compte du rapport.", 'media'))
CE_CNEWS = ('ce_cnews', src("Pluralisme et indépendance de l'information : l'Arcom devra se prononcer à nouveau sur le respect par CNews de ses obligations", "Conseil d'État", "13 février 2024",
  "https://conseil-etat.fr/actualites/pluralisme-et-independance-de-l-information-l-arcom-devra-se-prononcer-a-nouveau-sur-le-respect-par-cnews-de-ses-obligations",
  "Décision n° 463162 : l'Arcom doit apprécier le pluralisme en tenant compte de la diversité des points de vue exprimés par l'ensemble des participants (« chroniqueurs, animateurs et invités »), pas seulement du temps de parole des personnalités politiques ; « Le Conseil d'État ne se prononce pas sur le respect par les programmes de la chaîne CNews » de ces exigences.",
  "Communiqué officiel de la juridiction."))
DIPLO = ('diplo', src("Médias français : qui possède quoi ? (version 21.1, décembre 2025)", "Le Monde diplomatique et Acrimed (reprise par Pressenza)", "8 août 2026",
  "https://www.pressenza.com/fr/2026/08/medias-francais-qui-possede-quoi-2/",
  "Carte des propriétaires des médias ; mention du contrôle de Vincent Bolloré sur Canal+, Europe 1 et Le Journal du dimanche.",
  "Travail de recensement d'un journal et d'une association critiques des médias (orientation à gauche).", 'partisane'))
FICHES.append(fiche(
 id='medias-concentration', affirmation="Les médias, c'est tous des gauchistes.",
 volet='politique', sous_theme='Médias', mots_cles=['médias', 'journalistes', 'gauchistes', 'concentration', 'milliardaires', 'bolloré', 'cnews', 'pluralisme', 'arcom', 'propriétaires'],
 verdict='trompeur', fiabilite='interpretation', stabilite='evolutive',
 resume="Les grands médias privés français appartiennent pour beaucoup à de grandes fortunes (Bolloré, Arnault, Drahi, Niel, Bouygues…), auditionnées en 2022 par une commission d'enquête du Sénat sur la concentration des médias. Vincent Bolloré contrôle notamment Canal+, Europe 1 et le JDD, dont la ligne est classée à droite. Les opinions des journalistes varient, mais l'idée de médias uniformément « de gauche » ne tient pas compte de la propriété ni de la diversité des lignes éditoriales. Le pluralisme est un vrai sujet, que le Conseil d'État a demandé en 2024 à l'Arcom d'apprécier plus largement.",
 contexte="Le reproche de « médias de gauche » est ancien ; à gauche, on reproche à l'inverse la concentration entre les mains de milliardaires. Le Sénat a enquêté sur la concentration en 2021-2022 ; la question du pluralisme sur CNews est allée jusqu'au Conseil d'État.",
 explication="Il faut distinguer les opinions personnelles des journalistes, les lignes éditoriales (choisies par les directions) et la propriété des médias. Les trois peuvent diverger.",
 sources=[SENAT_MED, CE_CNEWS, DIPLO],
 faits=[
  fait("En 2022, la commission d'enquête du Sénat sur la concentration des médias (rapporteur David Assouline, président Laurent Lafon) auditionne notamment Vincent Bolloré, Bernard Arnault, Arnaud Lagardère, Patrick Drahi, Xavier Niel et Martin Bouygues, et adopte à l'unanimité un rapport de 32 propositions.", 'senat_med', 'Mars 2022', 'Sénat', "La concentration est reconnue comme un enjeu, au-delà des clivages partisans.", 'etabli'),
  fait("Bernard Arnault déclare : « Je n'ai pas envie de financer un journal qui devienne le support de l'extrême droite ou de l'extrême gauche. »", 'senat_med', 'Mars 2022', 'Audition au Sénat', "Les propriétaires peuvent avoir des attentes sur la ligne de leurs médias.", 'etabli'),
  fait("Le 13 février 2024, le Conseil d'État demande à l'Arcom de réexaminer le respect par CNews de ses obligations, en tenant compte de l'ensemble des intervenants et pas seulement du temps de parole des politiques ; il ne se prononce pas lui-même sur ce respect.", 'ce_cnews', '13 février 2024', 'Décision n° 463162', "Le pluralisme d'une chaîne s'apprécie sur l'ensemble de ses programmes.", 'etabli'),
  fait("Selon la carte du Monde diplomatique et d'Acrimed (décembre 2025), Vincent Bolloré contrôle notamment Canal+, Europe 1 et Le Journal du dimanche.", 'diplo', 'Décembre 2025', 'Propriété des médias', "Des médias très influents appartiennent à un industriel classé à droite.", 'etabli'),
 ],
 court="Les grands médias privés appartiennent à des milliardaires comme Bolloré, Arnault ou Drahi, pas vraiment des gauchistes. Il y a des journalistes de gauche et des médias de droite : c'est plus varié que ça.",
 moyen="Regarde qui possède les médias : Bolloré, qui contrôle Canal+, CNews, Europe 1 et le JDD, Arnault, Drahi, Niel, Bouygues. Le Sénat a même fait une enquête sur cette concentration en 2022. Ce ne sont pas des militants de gauche. Bernard Arnault l'a dit lui-même : il ne veut pas financer un journal d'extrême gauche. Qu'il y ait des journalistes de gauche, oui ; qu'il y ait des médias marqués à gauche, aussi. Mais il y a aussi des médias très marqués à droite. Le vrai sujet, c'est le pluralisme et l'indépendance des rédactions.",
 detaille="Le reproche de « médias tous de gauche » confond plusieurs niveaux.\n\nLa propriété d'abord. Une grande partie des médias privés appartient à de grandes fortunes : Vincent Bolloré (Canal+, CNews, Europe 1, Le Journal du dimanche), Bernard Arnault, Patrick Drahi, Xavier Niel, Martin Bouygues, entre autres. En 2022, le Sénat a consacré une commission d'enquête à cette concentration ; son rapport, adopté à l'unanimité malgré de fortes divisions, formule 32 propositions sur l'indépendance des rédactions. Bernard Arnault y déclarait ne pas vouloir financer « un journal qui devienne le support de l'extrême droite ou de l'extrême gauche ».\n\nLes lignes éditoriales ensuite. Elles vont de la gauche à la droite, voire à l'extrême droite selon de nombreux observateurs pour certaines chaînes. En 2024, le Conseil d'État a demandé à l'Arcom de réexaminer le respect du pluralisme par CNews en tenant compte de tous les intervenants, et pas seulement des politiques ; il ne s'est pas prononcé lui-même sur la chaîne.\n\nLes opinions des journalistes enfin : elles sont diverses, et la fiche ne dispose pas d'enquête récente vérifiée à ce sujet.\n\nLe débat utile porte donc sur le pluralisme, l'indépendance des rédactions face aux propriétaires et la qualité de l'information.",
 empathie="Je comprends que certains journalistes t'agacent ; on a tous des émissions qu'on ne supporte plus. Mais les grands médias appartiennent à des milliardaires, et certains sont clairement à droite. Le vrai combat, c'est que les rédactions soient libres, quel que soit le propriétaire.",
 contre=[
  ("Les journalistes votent majoritairement à gauche.", "Des enquêtes l'ont suggéré par le passé, mais la fiche n'en dispose pas de récente vérifiée ; et l'opinion des journalistes ne fait pas la ligne d'un média, décidée par sa direction."),
  ("Le service public est de gauche.", "C'est un reproche fréquent, que l'Arcom et le Parlement examinent ; il porte sur des émissions précises et doit être documenté au cas par cas."),
 ],
 questions=["Sais-tu à qui appartient la chaîne que tu regardes le plus ?", "Qu'est-ce qui garantirait selon toi l'indépendance d'un journal ?"],
 limites=["La carte des propriétaires est l'œuvre d'un journal et d'une association critiques des médias, consultée via une reprise ; l'image complète de la carte n'a pas été lue.", "Aucune enquête récente sur les opinions des journalistes n'a été vérifiée."],
 a_actualiser='2027-04-29', raison="Paysage médiatique en évolution rapide (rachats, décisions de l'Arcom).",
))

# ── Référendum et démocratie ─────────────────────────────────────────────────
CONST = ('const', src("Constitution du 4 octobre 1958", "Légifrance", "Version consolidée",
  "https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000571356/2017-07-23",
  "Art. 3 : « La souveraineté nationale appartient au peuple qui l'exerce par ses représentants et par la voie du référendum. » Art. 11 et 89 : référendum législatif et révision constitutionnelle (par référendum ou par le Parlement réuni en Congrès).",
  "Texte constitutionnel."))
TCE = ('tce', src("20 ans après, la plaie encore vive du référendum sur la Constitution européenne", "Public Sénat", "Mai 2025",
  "https://www.publicsenat.fr/actualites/politique/20-ans-apres-la-plaie-encore-vive-du-referendum-sur-la-constitution-europeenne",
  "Non à 54,67 % au référendum du 29 mai 2005 sur le traité établissant une Constitution pour l'Europe.",
  "Article rétrospectif d'un média parlementaire.", 'media'))
CONGRES = ('congres', src("Projet de loi constitutionnelle modifiant le titre XV de la Constitution (texte adopté par le Congrès)", "Sénat", "4 février 2008",
  "https://www.senat.fr/leg/tac07-001.html",
  "Adopté par le Parlement réuni en Congrès à Versailles (art. 89, al. 3) ; met en œuvre le traité de Lisbonne signé le 13 décembre 2007 ; abroge l'article 3 de la loi constitutionnelle de 2005.",
  "Texte officiel."))
AEC_RIC = ('aec', src("L'Avenir en commun — programme abrégé (2022)", "Union populaire / La France insoumise (source partisane)", "Avril 2022",
  "https://melenchon.fr/wp-content/uploads/2022/04/programme-avenir-en-commun-abrege.pdf",
  "Proposition d'un référendum d'initiative citoyenne (proposer ou abroger une loi, modifier la Constitution, révoquer des élus) (p. 5).",
  "Exemple de proposition de démocratie directe (source partisane).", 'partisane'))
FICHES.append(fiche(
 id='referendum-democratie-directe', type='reference', affirmation="De toute façon, on ne demande jamais l'avis du peuple.",
 volet='politique', sous_theme='Démocratie directe', mots_cles=['référendum', 'démocratie directe', 'peuple', 'ric', '2005', 'lisbonne', 'constitution', 'souveraineté', 'congrès'],
 verdict='plutot_exact', fiabilite='etabli', stabilite='historique',
 resume="La Constitution prévoit que le peuple exerce la souveraineté « par ses représentants et par la voie du référendum », mais l'initiative du référendum appartient pour l'essentiel aux gouvernants. Le dernier grand exemple reste le « non » à 54,67 % au traité constitutionnel européen en 2005 ; en 2008, le Parlement réuni en Congrès a révisé la Constitution pour permettre la ratification du traité de Lisbonne sans nouveau référendum. Des partis proposent un référendum d'initiative citoyenne (RIC) pour donner l'initiative aux citoyens.",
 contexte="Le sentiment de ne pas être consulté est fort depuis 2005. Il a resurgi lors du mouvement des Gilets jaunes, qui réclamait le RIC.",
 explication="Il existe plusieurs formes de démocratie : représentative (on élit des représentants), directe (on vote soi-même sur une loi), participative (on est consulté). La Ve République est surtout représentative, avec un référendum à l'initiative du pouvoir.",
 sources=[CONST, TCE, CONGRES, AEC_RIC],
 faits=[
  fait("L'article 3 de la Constitution dispose : « La souveraineté nationale appartient au peuple qui l'exerce par ses représentants et par la voie du référendum. »", 'const', 'Depuis 1958', 'Constitution', "Le référendum est prévu, mais il reste un outil à l'initiative des institutions.", 'etabli'),
  fait("Le 29 mai 2005, le traité établissant une Constitution pour l'Europe est rejeté par 54,67 % des votants.", 'tce', '2005', 'Référendum national', "Le dernier référendum national de grande portée.", 'etabli', '54,67 %'),
  fait("Le 4 février 2008, le Parlement réuni en Congrès adopte une révision constitutionnelle mettant en œuvre le traité de Lisbonne, signé le 13 décembre 2007.", 'congres', 'Février 2008', 'Congrès du Parlement', "La voie parlementaire a été choisie plutôt qu'un nouveau référendum.", 'etabli'),
  fait("Le programme de LFI propose un référendum d'initiative citoyenne permettant de proposer ou d'abroger une loi, de modifier la Constitution et de révoquer des élus.", 'aec', '2022', 'Programme (source partisane)', "Une proposition pour donner l'initiative aux citoyens.", 'etabli'),
 ],
 court="Le référendum existe dans la Constitution, mais ce sont les gouvernants qui décident quand on vote. En 2005, on a dit non à la Constitution européenne ; en 2008, le Parlement a ratifié le traité de Lisbonne sans nous redemander. D'où l'idée du référendum d'initiative citoyenne.",
 moyen="Il y a du vrai. La Constitution dit que le peuple est souverain, par ses élus et par référendum. Mais c'est le président, en pratique, qui décide d'organiser un référendum. En 2005, 54,67 % des votants ont dit non au traité constitutionnel européen ; en 2008, le Parlement réuni en Congrès a révisé la Constitution pour ratifier le traité de Lisbonne, sans nouveau référendum. Beaucoup l'ont vécu comme un contournement. C'est pour ça que certains proposent un référendum d'initiative citoyenne, où ce seraient les citoyens qui déclenchent le vote.",
 detaille="L'article 3 de la Constitution affirme que « la souveraineté nationale appartient au peuple qui l'exerce par ses représentants et par la voie du référendum ». En pratique, la Ve République est surtout représentative : l'initiative du référendum appartient au pouvoir exécutif ou passe par des procédures très encadrées.\n\nLe dernier grand référendum, le 29 mai 2005, a vu le « non » l'emporter avec 54,67 % des voix sur le traité établissant une Constitution pour l'Europe. Le traité de Lisbonne, signé en décembre 2007, a ensuite été rendu possible par une révision constitutionnelle adoptée par le Parlement réuni en Congrès le 4 février 2008, sans nouveau référendum. Les partisans de cette voie la jugeaient légale et justifiée par les différences entre les deux traités ; ses opposants y ont vu un désaveu du vote de 2005.\n\nCette histoire nourrit les revendications de démocratie directe, comme le référendum d'initiative citoyenne proposé par La France insoumise et réclamé par une partie des Gilets jaunes. Ses partisans y voient un moyen de redonner la parole aux citoyens ; ses critiques craignent la démagogie ou l'instabilité.\n\n« On ne demande jamais l'avis du peuple » est donc excessif, puisque les élections et le référendum existent ; mais le sentiment de ne pas avoir la main repose sur des faits.",
 empathie="Je comprends ce sentiment, et je le partage en partie : 2005, ça a laissé des traces. Plutôt que de se dire que ça ne sert à rien, on peut se demander comment donner plus de pouvoir aux citoyens. Tu serais pour un référendum d'initiative citoyenne ?",
 contre=[
  ("Le traité de Lisbonne n'était pas le même texte.", "C'était l'argument des partisans de la ratification parlementaire ; ses opposants estimaient qu'il reprenait l'essentiel du texte rejeté. Le débat reste vif."),
  ("Le RIC, ce serait le règne de la démagogie.", "C'est une objection sérieuse ; d'autres pays pratiquent des formes d'initiative populaire encadrées, ce qui permet d'en discuter concrètement."),
 ],
 questions=["Sur quel sujet aimerais-tu pouvoir voter directement ?", "Faut-il que les citoyens puissent déclencher eux-mêmes un référendum ?"],
 limites=["Les votes exacts du Congrès de 2008 ne figurent pas dans la source consultée.", "Le référendum d'initiative partagée (RIP), introduit en 2008, n'est pas détaillé faute de source consultée."],
 a_actualiser='2028-10-29', raison="Cadre constitutionnel stable ; à revoir en cas de réforme.",
))

# ── Commune de Paris ─────────────────────────────────────────────────────────
PARIS_COM = ('paris_com', src("Les 150 ans de la Commune : la fin sanglante et les conséquences (5/5)", "Ville de Paris", "2021",
  "https://www.paris.fr/pages/les-150-ans-de-la-commune-la-fin-sanglante-et-les-consequences-5-5-17210",
  "Semaine sanglante du 21 au 28 mai 1871 ; pas de consensus des historiens sur le nombre de morts : 3 000 à 5 000 fédérés tués au combat et environ 20 000 massacrés selon la page ; 500 à 800 tués côté versaillais ; une centaine d'otages exécutés par les fédérés ; environ 43 000 arrestations ; environ 3 800 déportés en Nouvelle-Calédonie ; loi d'amnistie de 1880.",
  "Dossier historique institutionnel.", 'secondaire'))
WIKI_SEM = ('wiki_sem', src("Semaine sanglante (article encyclopédique)", "Wikipédia (en anglais)", "Consulté le 29 octobre 2026",
  "https://en.wikipedia.org/wiki/Semaine_sanglante",
  "Estimations récentes fondées sur les registres des cimetières (Audin, Tombs) : 10 000 à 15 000 communards tués ; estimations anciennes : environ 30 000 (Pelletan, 1879), plus de 20 000 (Lissagaray) ; la plupart fusillés après des jugements sommaires selon Tombs ; environ 100 otages exécutés par la Commune, dont l'archevêque Darboy.",
  "Synthèse encyclopédique des estimations historiographiques.", 'secondaire'))
FICHES.append(fiche(
 id='commune-paris-1871', type='histoire', affirmation="La Commune de Paris, c'était une bande d'émeutiers vite remis à leur place.",
 volet='international', sous_theme='Histoire du mouvement ouvrier', rubriques=[], mots_cles=['commune de paris', '1871', 'semaine sanglante', 'communards', 'versaillais', 'louise michel', 'répression', 'amnistie', 'mouvement ouvrier'],
 verdict='trompeur', fiabilite='debat', stabilite='historique',
 resume="La Commune de Paris (mars-mai 1871) a été écrasée lors de la « Semaine sanglante » du 21 au 28 mai 1871. Le nombre de morts reste débattu : les estimations récentes fondées sur les registres des cimetières (Audin, Tombs) évoquent 10 000 à 15 000 communards tués, des estimations anciennes 20 000 à 30 000 ; la plupart auraient été fusillés après des jugements sommaires. Environ 43 000 personnes ont été arrêtées et quelque 3 800 déportées en Nouvelle-Calédonie, avant l'amnistie de 1880. Les communards ont eux aussi exécuté une centaine d'otages.",
 contexte="Après la défaite contre la Prusse et le siège de Paris, une partie de la population parisienne se soulève en mars 1871 contre le gouvernement installé à Versailles. La Commune devient un symbole majeur du mouvement ouvrier et socialiste.",
 explication="« Remettre à leur place » minimise une répression parmi les plus meurtrières de l'histoire de France contemporaine. Reconnaître sa violence n'oblige pas à idéaliser la Commune, qui a elle aussi exécuté des otages.",
 sources=[PARIS_COM, WIKI_SEM],
 faits=[
  fait("La Semaine sanglante se déroule du 21 au 28 mai 1871, de l'entrée des troupes versaillaises dans Paris à la chute des dernières barricades à Belleville.", 'paris_com', '21-28 mai 1871', 'Paris', "Une guerre urbaine d'une semaine.", 'etabli'),
  fait("Le nombre de communards tués est débattu : 10 000 à 15 000 selon des estimations récentes fondées sur les registres des cimetières (Audin, Tombs), contre plus de 20 000 à environ 30 000 selon des estimations anciennes ; la page de la Ville de Paris évoque environ 20 000 massacrés.", 'wiki_sem', '1871', 'Historiographie', "Même l'estimation basse correspond à des milliers d'exécutions.", 'debat'),
  fait("Environ 43 000 personnes sont arrêtées ; environ 3 800 sont déportées en Nouvelle-Calédonie entre 1872 et 1878, dont Louise Michel ; l'amnistie est votée en 1880.", 'paris_com', '1871-1880', 'Répression judiciaire', "La répression s'est prolongée pendant des années.", 'etabli', '43 000 ; 3 800'),
  fait("Les fédérés ont exécuté une centaine d'otages, dont l'archevêque de Paris Georges Darboy.", 'wiki_sem', 'Mai 1871', 'Paris', "La violence n'a pas été d'un seul côté, même si l'écart d'ampleur est considérable.", 'etabli'),
 ],
 court="La Commune a été écrasée dans le sang : des milliers de Parisiens tués en une semaine, 10 000 à 15 000 selon les estimations récentes, et 43 000 arrestations. On peut critiquer la Commune, mais pas dire qu'on a juste remis de l'ordre.",
 moyen="La Commune, c'est plus qu'une émeute. Après la défaite contre la Prusse, une partie de Paris s'est soulevée et s'est gouvernée pendant deux mois. Elle a été écrasée pendant la Semaine sanglante, fin mai 1871 : les historiens débattent du chiffre, mais même les estimations les plus récentes parlent de 10 000 à 15 000 morts, la plupart fusillés après des jugements sommaires. Il y a eu environ 43 000 arrestations et près de 4 000 déportés en Nouvelle-Calédonie. Les communards ont aussi exécuté une centaine d'otages, il faut le dire. Mais la répression a été d'une tout autre ampleur.",
 detaille="La Commune de Paris naît en mars 1871, dans une capitale épuisée par le siège prussien et hostile au gouvernement installé à Versailles. Pendant deux mois, une partie des Parisiens organise sa propre administration.\n\nElle est écrasée par l'armée versaillaise lors de la Semaine sanglante, du 21 au 28 mai 1871. Le bilan humain fait débat entre historiens. Les estimations anciennes, comme celle de Camille Pelletan en 1879, avancent environ 30 000 morts ; Prosper-Olivier Lissagaray, plus de 20 000. Des travaux plus récents, fondés sur les registres des cimetières (Michèle Audin, Robert Tombs), retiennent 10 000 à 15 000 communards tués. Selon Robert Tombs, la plupart ont été fusillés après des jugements expéditifs. Côté versaillais, on compte 500 à 800 morts.\n\nLa répression se prolonge : environ 43 000 arrestations, des milliers de condamnations, environ 3 800 déportations en Nouvelle-Calédonie, dont celle de Louise Michel. L'amnistie n'est votée qu'en 1880.\n\nLes communards ont eux aussi commis des violences, notamment l'exécution d'une centaine d'otages, dont l'archevêque de Paris. Une histoire honnête ne cache ni cette violence ni l'écart d'ampleur entre les deux camps.",
 empathie="C'est une histoire qu'on apprend peu, et elle est violente des deux côtés. Mais la répression a été terrible : des milliers de Parisiens fusillés en une semaine. Ça vaut la peine de la connaître, quel que soit le jugement qu'on porte sur la Commune.",
 contre=[
  ("Les communards ont incendié Paris et tué des otages.", "C'est vrai : des incendies (dont celui des Tuileries) et l'exécution d'une centaine d'otages. Cela n'efface pas l'ampleur d'une répression qui a tué des milliers de personnes, souvent sans jugement."),
  ("Les chiffres de morts sont exagérés par la gauche.", "Les historiens ont révisé à la baisse les estimations anciennes ; mais même les plus basses parlent de 10 000 à 15 000 morts."),
 ],
 questions=["Pourquoi, selon toi, la Commune est-elle si peu enseignée ?", "Peut-on condamner à la fois les otages exécutés et les fusillades de masse ?"],
 limites=["Les mesures politiques et sociales de la Commune ne sont pas détaillées faute de source consultée.", "Une des sources est une encyclopédie collaborative ; les estimations qu'elle attribue à Audin et Tombs n'ont pas été vérifiées dans les ouvrages."],
 a_actualiser='2029-10-29', raison="Fiche historique : relecture périodique.",
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2)
            fh.write('\n')
    print(len(FICHES), 'fiches écrites')
