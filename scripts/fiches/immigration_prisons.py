"""Rubrique « Immigration, délinquance et prisons » : 5 formulations sur les prisons et la délinquance,
6 formulations sur l'expulsion des étrangers condamnés. Chaque formulation est analysée séparément.

Toutes les sources citées ont été ouvertes et lues le 30 octobre 2026 (consultee=True).
Règles : ne jamais utiliser « étranger » et « immigré » l'un pour l'autre ; une association statistique
n'est pas une cause ; les garanties juridiques sont expliquées, pas présentées comme une impunité.
Usage : python3 scripts/fiches/immigration_prisons.py  (écrit dans data/library/)
"""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'library')
TODAY = '2026-10-30'
ST_PRISON = 'Immigration, délinquance et prisons'
ST_EXPUL = 'Expulsion des étrangers condamnés'
RUB = ['immigration-prisons']

def src(titre, organisme, date, url, passage, pertinence, type_='primaire'):
    return dict(titre=titre, organisme=organisme, date_publication=date, url=url, passage=passage, pertinence=pertinence, type=type_, consultee=True)

def fait(texte, source, periode, perimetre, explication, fiabilite='etabli', chiffre=None):
    d = dict(fait=texte, periode=periode, perimetre=perimetre, explication=explication, source=source, fiabilite=fiabilite)
    if chiffre: d['chiffre'] = chiffre
    return d

def fiche(**k):
    sources = k.pop('sources')
    idx = {key: i for i, (key, _) in enumerate(sources)}
    d = dict(
        id=k['id'], type=k.get('type', 'idee_recue'), affirmation=k['affirmation'], volet='immigration', sous_theme=k['sous_theme'],
        rubriques=RUB, mots_cles=k['mots_cles'], verdict=k.get('verdict'), fiabilite=k['fiabilite'], stabilite=k.get('stabilite', 'evolutive'),
        resume=k['resume'], contexte=k['contexte'], explication=k['explication'],
        faits=[{**f, 'source': idx[f['source']]} for f in k['faits']],
        argumentaires=dict(court=k['court'], moyen=k['moyen'], detaille=k['detaille'], empathie=k['empathie']),
        contre_arguments=[dict(objection=o, reponse=r) for o, r in k['contre']],
        questions=k['questions'], limites=k['limites'],
        sources=[s for _, s in sources],
        derniere_verification=TODAY, a_actualiser_le=k.get('a_actualiser', '2027-06-30'), raison_actualisation=k.get('raison', "Nouvelles statistiques annuelles ou évolution de la législation."),
    )
    if k.get('legitimes'): d['objections_legitimes'] = k['legitimes']
    # v14 : réponses selon le public (électeur d'extrême droite convaincu / personne indécise)
    if k.get('publics'): d['publics'] = k['publics']
    return d

# ── Sources ────────────────────────────────────────────────────────────────
AN_DETENUS = ('an_detenus', src("Réponse du ministère de la Justice à la question écrite n° 12283 (M. Éric Pauget) sur la part des étrangers dans les procédures pénales et la population pénitentiaire", "Assemblée nationale / ministère de la Justice", "26 mai 2026 (JO p. 4636)",
  "https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE12283",
  "Au 1er avril 2026, 88 419 personnes détenues, dont 21 329 étrangères, soit 24,2 %. Proportion passée de 21 % en 2016 à 24,7 % au 1er janvier 2026 (valeurs annuelles de 22 % à 25 %). Statut pénal des détenus étrangers : 13 906 condamnés, 6 599 prévenus, 819 condamnés et prévenus. Nationalités les plus représentées : Algérie 5,9 %, Maroc 2,1 %, Tunisie 1,75 %, Roumanie 1,1 %, Portugal 0,6 %. Milieu ouvert au 1er janvier 2026 : 14 746 étrangers suivis, soit 8,2 %. Les outils statistiques ne permettent pas de déterminer la part des étrangers sous surveillance électronique.",
  "Chiffres officiels de l'administration pénitentiaire, communiqués au Parlement."))
INSEE_ETR = ('insee_etr', src("En 2024, 6,0 millions d'étrangers vivent en France, 0,9 million y sont nés (Insee Première n° 2076)", "Insee (Chloé Pariset, Pierre Tanneau)", "7 octobre 2025",
  "https://www.insee.fr/fr/statistiques/8651304",
  "2024 (provisoire) : 6,0 millions d'étrangers, soit 8,8 % de la population ; 7,7 millions d'immigrés, soit 11,3 % ; 0,9 million d'étrangers nés en France (1,3 %). Définitions : un étranger réside en France sans la nationalité française ; un immigré est né étranger à l'étranger et le reste même devenu français.",
  "Statistique publique de référence pour les dénominateurs."))
INSEE_AUT = ('insee_aut', src("Auteurs selon la nationalité (Insee Références « Sécurité et société », données SSMSI)", "Insee / SSMSI (ministère de l'Intérieur)", "9 décembre 2021",
  "https://www.insee.fr/fr/statistiques/5763585",
  "Part des étrangers parmi les personnes mises en cause en 2019 (hors infractions routières) : ensemble 17,7 % ; atteintes à la personne 13,1 % ; infractions à caractère sexuel 13,5 % ; vols 26,6 % ; destructions et dégradations 10,8 % ; stupéfiants 11,5 %. Avertissement : la nationalité ne peut pas toujours être vérifiée faute de pièce d'identité ; nationalité non renseignée pour 11 % des auteurs traités par les parquets. Part passée de 16 % en 2016 à 18 % en 2019.",
  "Seule série détaillée publiée par nationalité et par type d'infraction."))
INSEE_DOS = ('insee_dos', src("Dossier 1 : Depuis 2010, les phénomènes délinquants se transforment tandis que le sentiment d'insécurité reste globalement stable (Insee Références « Sécurité et société »)", "Insee / SSMSI", "9 décembre 2021",
  "https://www.insee.fr/fr/statistiques/fichier/6008710/INSEE-FP-IREF-SECURITE_DOSSIER1.pdf",
  "En 2019, les étrangers représentent 18 % des mis en cause alors qu'ils forment 7 % des personnes résidant en France ; 9 % des victimes d'atteintes personnelles sont étrangères (16 % pour les violences sexuelles). Les mis en cause sont des auteurs présumés, non des condamnés ; toutes les victimes ne portent pas plainte.",
  "Met en regard auteurs présumés, victimes et population."))
JUSTICE_IRJ = ('justice_irj', src("Au 1er juillet 2026, + 5,2 % de personnes détenues sur un an (Infos Rapides Justice n° 42)", "Ministère de la Justice (SSER)", "Juillet 2026",
  "https://www.justice.gouv.fr/sites/default/files/2026-07/Au%201er%20juillet%C2%A02026%2C%20%2B%C2%A05%2C2%20%25%20de%20personnes%20d%C3%A9tenues%20sur%20un%20an.pdf",
  "Au 1er juillet 2026, 88 000 personnes détenues (hors collectivités d'outre-mer), dont 23 800 prévenus et 64 200 condamnés.",
  "Statistique officielle de l'ensemble des personnes détenues."))
SPACE = ('space', src("SPACE I – 2024. Council of Europe Annual Penal Statistics: Prison populations", "Conseil de l'Europe / Université de Lausanne (Marcelo F. Aebi, Edoardo Cocco)", "15 décembre 2024 (mis en ligne en septembre 2025)",
  "https://wp.unil.ch/space/files/2025/09/250924_rapport-space-i-2024.pdf",
  "Médiane européenne : 16,0 % de détenus étrangers au 31 janvier 2024 (48 administrations pénitentiaires) ; la France est classée dans le groupe « très élevé » (plus de 25 % au-dessus de la médiane). Les différences de collecte créent des écarts artificiels entre pays : les comparaisons doivent être très prudentes.",
  "Comparaison européenne de référence."))
BBP = ('bbp', src("Do immigrants cause crime? (document de travail ; publié ensuite dans le Journal of the European Economic Association, 2012)", "Milo Bianchi, Paolo Buonanno, Paolo Pinotti (Paris School of Economics)", "2008",
  "https://www.parisschoolofeconomics.eu/en/publications-hal/do-immigrants-cause-crime",
  "Provinces italiennes, 1990-2003 : la population immigrée est corrélée aux atteintes aux biens et au taux global de délinquance ; avec une méthode de variables instrumentales, l'immigration n'augmente que les vols avec violence (robberies), et l'effet sur le taux global de délinquance n'est pas statistiquement différent de zéro.",
  "Étude universitaire distinguant corrélation et causalité.", 'etude'))
AN_EXPUL = ('an_expul', src("Proposition de loi visant à assouplir les conditions d'expulsion des étrangers constituant une menace grave pour l'ordre public (n° 265) — rapport d'étape de la commission des lois (rapporteure : Edwige Diaz)", "Assemblée nationale", "23 octobre 2024",
  "https://www.assemblee-nationale.fr/dyn/contenu/visualisation/863769/file/PPL%20265%20-%20EAT.pdf",
  "Droit en vigueur (CESEDA, après la loi n° 2024-42 du 26 janvier 2024) : L. 631-1, expulsion possible si la présence constitue une menace grave pour l'ordre public — une condamnation ne suffit pas à elle seule ; L. 631-2, protection relative (parents d'enfant français, conjoints de Français depuis trois ans, résidents réguliers depuis plus de dix ans…) levée notamment en cas de condamnation définitive pour un crime ou délit puni d'au moins trois ans ; L. 631-3, protection quasi absolue (arrivés avant 13 ans, résidents de plus de vingt ans…) levée en cas de condamnation définitive pour des faits punis d'au moins cinq ans (trois en récidive) ; L. 631-4, mineurs : protection absolue. Contrôle de proportionnalité au regard de l'article 8 de la Convention européenne des droits de l'homme. Dispositions de 2024 jugées conformes par le Conseil constitutionnel (décision n° 2023-863 DC du 25 janvier 2024). 2022 : 341 mesures d'expulsion prononcées, 167 exécutées ; 2023 : 58 arrêtés ministériels d'expulsion, exécutés à 63 %.",
  "Document parlementaire décrivant le droit en vigueur ; le texte soutient une proposition de durcissement, ce qui n'affecte pas la description du droit."))
CP_ITF = ('cp_itf', src("Code pénal, article 131-30 (interdiction du territoire français) — reproduction du texte en vigueur", "Légifrance (texte reproduit par TheTradeHub)", "Version en vigueur consultée le 30 octobre 2026",
  "https://www.thetradehub.eu/fr/reglementation/france/legislation/cibs/code-penal-art-131-30",
  "« La peine d'interdiction du territoire français peut être prononcée, dans les conditions prévues par la loi, à titre définitif ou pour une durée de dix ans au plus, à l'encontre de tout étranger coupable d'un crime ou d'un délit. » Elle « entraîne de plein droit la reconduite du condamné à la frontière, le cas échéant, à l'expiration de sa peine d'emprisonnement ou de réclusion ».",
  "Texte de loi (peine prononcée par un juge pénal).", 'secondaire'))
PUBSEN = ('pubsen', src("Loi immigration : OQTF, expulsions, tout comprendre sur les mesures administratives d'éloignement", "Public Sénat (Simon Barbarit)", "27 octobre 2023 (mis à jour le 2 novembre 2023)",
  "https://www.publicsenat.fr/actualites/politique/loi-immigration-oqtf-expulsions-tout-comprendre-sur-les-mesures-administratives-deloignement",
  "L'OQTF est une mesure administrative du préfet (départ sous 30 jours) ; l'arrêté d'expulsion est exécutoire immédiatement et peut être pris sans condamnation ; l'ITF est une peine complémentaire prononcée par un juge, définitive ou jusqu'à dix ans. Selon le rapport de la commission des lois du Sénat : au premier semestre 2022, 65 076 OQTF prononcées et 4 474 exécutées, soit 6,9 %. Obstacles : refus de laissez-passer consulaires, décisions de justice, centres de rétention saturés.",
  "Synthèse journalistique de la chaîne parlementaire, citant le rapport du Sénat.", 'media'))
CDC = ('cdc', src("La politique de lutte contre l'immigration irrégulière (rapport public thématique)", "Cour des comptes", "Janvier 2024",
  "https://www.vie-publique.fr/files/rapport/pdf/292560.pdf",
  "447 257 OQTF prononcées de 2019 à 2022 ; seule une petite minorité, autour de 10 %, est exécutée. Éloignements forcés : 18 915 en 2019, 11 409 en 2022 (Eurostat). 22 centres de rétention, 1 717 places ; environ 5 % des personnes sous OQTF placées en rétention, dont près de la moitié éloignées. Difficultés : identification, réticence de nombreux pays d'origine à délivrer des laissez-passer consulaires, refus d'embarquer. Coût moyen d'un éloignement forcé : 4 414 €.",
  "Juridiction financière : constat sur l'exécution réelle des mesures."))
CEDH = ('cedh', src("Üner c. Pays-Bas (Cour européenne des droits de l'homme, Grande Chambre) — fiche de jurisprudence", "Inimõiguste Keskus (résumé de l'arrêt CEDH du 18 octobre 2006)", "Arrêt du 18 octobre 2006",
  "https://www.inimoigustegiid.ee/en/case-law/uener-v-the-netherlands",
  "Critères pour l'expulsion d'un étranger installé et condamné : gravité de l'infraction, durée du séjour, vie familiale (notamment avec les enfants), intérêt et capacité d'adaptation des enfants, liens avec le pays d'origine. Conclusion : pas de violation de l'article 8 ; la mesure était proportionnée à une condamnation pour homicide.",
  "Jurisprudence européenne fixant les critères de proportionnalité.", 'secondaire'))
CE2026 = ('ce2026', src("Expulsion des étrangers protégés : trois décisions du Conseil d'État du 9 juin 2026 sur le contrôle de proportionnalité", "Cabinet Kohen Avocats (commentaire)", "2026",
  "https://kohenavocats.com/tr/trilogie-conseil-etat-9-juin-2026-expulsion-etrangers-proportionnalite/",
  "Conseil d'État, 9 juin 2026, n° 506729, n° 504383 et n° 505954 (à publier au Recueil) : trois illustrations du contrôle de proportionnalité entre l'atteinte à la vie familiale et la protection de l'ordre public. L. 631-3 : expulsion des étrangers les plus protégés en cas de comportements portant atteinte aux intérêts fondamentaux de l'État, liés au terrorisme ou de provocation explicite à la haine ou à la violence.",
  "Commentaire d'avocat de décisions récentes ; à lire comme une source secondaire.", 'secondaire'))

FICHES = []

# ═════════════ A. « Les étrangers remplissent les prisons françaises. » ═════════════
FICHES.append(fiche(
 id='etrangers-prisons', affirmation="Les étrangers remplissent les prisons françaises.", sous_theme=ST_PRISON,
 mots_cles=['étrangers', 'prisons', 'prison', 'détenus', 'population carcérale', 'remplissent', 'nationalité', 'surreprésentés', 'surreprésentation', 'incarcérés', 'détention'],
 verdict='trompeur', fiabilite='etabli',
 resume="Les étrangers représentent environ un quart des personnes détenues (24,2 % au 1er avril 2026, selon le ministère de la Justice), alors qu'ils forment 8,8 % de la population (Insee, 2024). Ils sont donc nettement surreprésentés. Mais « remplir » les prisons est faux : trois détenus sur quatre sont français.",
 contexte="Ce chiffre est souvent cité, parfois gonflé, parfois nié. Il est exact et publié par le ministère de la Justice. Le débat porte sur ce qu'il signifie : surreprésentation réelle, mais aussi effets de l'âge, du sexe, de la précarité, de la détention provisoire et de certaines infractions propres aux étrangers.",
 explication="La statistique pénitentiaire compte la NATIONALITÉ : un étranger n'a pas la nationalité française (il peut être né en France). Elle ne compte pas les immigrés (nés étrangers à l'étranger, dont un tiers sont devenus français). Les deux chiffres ne sont pas interchangeables. Une surreprésentation est une association statistique : elle ne dit pas, à elle seule, pourquoi elle existe.",
 sources=[AN_DETENUS, INSEE_ETR, JUSTICE_IRJ, SPACE],
 faits=[
  fait("Au 1er avril 2026, 21 329 des 88 419 personnes détenues sont étrangères, soit 24,2 %.", 'an_detenus', '1er avril 2026', 'Personnes détenues, France', "Environ un détenu sur quatre est étranger ; trois sur quatre sont français.", 'etabli', '24,2 %'),
  fait("Les étrangers représentent 8,8 % de la population en 2024 (6,0 millions de personnes).", 'insee_etr', '2024 (provisoire)', 'Population résidant en France', "C'est le bon dénominateur pour comparer : même définition (nationalité) que la statistique pénitentiaire.", 'etabli', '8,8 %'),
  fait("La part des étrangers parmi les détenus est passée de 21 % en 2016 à 24,7 % au 1er janvier 2026.", 'an_detenus', '2016-2026', 'Personnes détenues', "Hausse modérée sur dix ans, à un niveau élevé.", 'etabli', '21 % → 24,7 %'),
  fait("Parmi les détenus étrangers, 13 906 sont condamnés et 6 599 sont prévenus (en attente de jugement), soit environ 31 % de prévenus.", 'an_detenus', '1er avril 2026', 'Détenus étrangers', "La part de prévenus est un peu plus forte que pour l'ensemble des détenus : ce ne sont pas tous des condamnés.", 'etabli'),
  fait("Pour l'ensemble des détenus, on compte 23 800 prévenus sur 88 000 personnes au 1er juillet 2026, soit environ 27 %.", 'justice_irj', '1er juillet 2026', 'Ensemble des personnes détenues (hors COM)', "Comparaison à date proche, pas identique.", 'etabli'),
  fait("La médiane européenne est de 16,0 % de détenus étrangers au 31 janvier 2024 ; la France fait partie des pays où la part est « très élevée ».", 'space', '31 janvier 2024', '48 administrations pénitentiaires européennes', "Les définitions et collectes diffèrent selon les pays : comparaison prudente.", 'estimation', '16,0 %'),
 ],
 court="Les étrangers sont environ un quart des détenus (24,2 %) pour 8,8 % de la population : ils sont surreprésentés, c'est vrai. Mais trois détenus sur quatre sont français : « remplir les prisons », c'est faux.",
 moyen="Le chiffre exact, c'est le ministère de la Justice qui le donne : au 1er avril 2026, 24,2 % des détenus sont étrangers, alors que les étrangers sont 8,8 % de la population. Il y a donc une surreprésentation réelle, et il ne sert à rien de la nier. Mais trois détenus sur quatre sont français. Et ce chiffre compte la nationalité, pas les « immigrés » : ce ne sont pas les mêmes personnes. Enfin, près d'un tiers de ces détenus étrangers attendent encore leur jugement.",
 detaille="Commençons par reconnaître ce qui est exact. Selon le ministère de la Justice, au 1er avril 2026, 21 329 des 88 419 personnes détenues sont étrangères, soit 24,2 %. Selon l'Insee, les étrangers représentent 8,8 % de la population. La surreprésentation est réelle, et elle a un peu augmenté en dix ans (21 % en 2016, 24,7 % au 1er janvier 2026).\n\nCe chiffre dit-il que les étrangers « remplissent » les prisons ? Non : 75 % des détenus sont français. Il ne dit pas non plus que les « immigrés » sont en prison : la statistique compte la nationalité. Un immigré devenu français est compté comme français ; un enfant étranger né en France est compté comme étranger.\n\nIl faut ensuite regarder qui est détenu. Parmi les détenus étrangers, environ 31 % sont prévenus, c'est-à-dire en attente de jugement, contre environ 27 % pour l'ensemble des détenus (à une date proche). Une explication souvent avancée est l'absence de domicile stable ou de garanties de représentation, qui rend la détention provisoire plus fréquente ; ce mécanisme n'est pas mesuré par ces chiffres.\n\nEnfin, une comparaison brute ignore l'âge et le sexe (la prison concerne surtout de jeunes hommes), la précarité, et certaines infractions liées au séjour qui ne peuvent concerner que des étrangers. Ces facteurs ne font pas disparaître l'écart, mais ils empêchent d'en conclure que la nationalité serait la cause.\n\nEn Europe, la médiane est de 16 % de détenus étrangers ; la France fait partie des pays où la part est élevée, avec la prudence qu'imposent des définitions différentes d'un pays à l'autre.",
 empathie="Je comprends que ce chiffre t'interpelle : un quart des détenus sont étrangers, c'est beaucoup, et c'est vrai. Mais ça veut aussi dire que trois sur quatre sont français. Si on veut une prison qui protège vraiment, il faut regarder tout le tableau, pas seulement la nationalité.",
 legitimes=["Les étrangers sont réellement surreprésentés parmi les détenus : environ trois fois leur part dans la population.", "La part des étrangers en détention a augmenté sur dix ans."],
 contre=[
  ("Même si tous ne sont pas étrangers, les étrangers sont surreprésentés dans les prisons.", "Oui, et c'est exact : 24,2 % des détenus pour 8,8 % de la population. La vraie question est de comparer ce qui est comparable : à âge, sexe et conditions sociales proches, l'écart se réduit, et une partie des détenus étrangers attendent leur jugement. La surreprésentation est un fait ; elle ne dit pas à elle seule que la nationalité en est la cause."),
  ("Les chiffres officiels sont minimisés.", "Ils viennent des fichiers de l'administration pénitentiaire, communiqués au Parlement en mai 2026. Ils montrent justement une surreprésentation importante : ils ne la cachent pas."),
  ("Peu importe les statistiques, il faut tous les renvoyer chez eux.", "C'est un autre débat : celui de l'expulsion. Le droit permet déjà d'expulser ou d'interdire du territoire des étrangers condamnés, avec des protections pour ceux qui ont grandi en France, et l'exécution réelle de ces mesures est le principal problème. Voir la fiche « Tous les étrangers condamnés devraient être expulsés »."),
 ],
 questions=["À ton avis, quelle part des détenus est étrangère ? Et quelle part de la population ?", "Est-ce que tu comparerais les détenus à toute la population, ou plutôt aux hommes jeunes du même milieu social ?"],
 limites=["Les chiffres comptent la nationalité, pas le statut d'immigré ni le pays de naissance.", "Les dates de comparaison (1er avril et 1er juillet 2026) diffèrent légèrement.", "Le ministère ne publie pas, dans cette réponse, la répartition par type d'infraction ni la récidive."],
 publics={'convaincus': "Tu as raison sur un point : les étrangers sont surreprésentés en prison, environ un quart des détenus (24,2 %) pour 8,8 % de la population. Mais trois détenus sur quatre sont français : dire qu'ils « remplissent » les prisons est faux. Et la comparaison brute ignore l'âge, le sexe, la précarité et la détention provisoire.",
  'indecis': "Les chiffres du ministère de la Justice montrent une surreprésentation réelle : 24,2 % des détenus sont étrangers. Mais la grande majorité des détenus sont français. Pour comprendre l'écart, il faut tenir compte de l'âge et du sexe des détenus, de la précarité et d'un recours plus fréquent à la détention provisoire : ces facteurs n'effacent pas l'écart, mais empêchent d'en faire une question de nationalité."},
 a_actualiser='2027-06-30', raison="Les chiffres de la population carcérale évoluent chaque mois.",
))

# ═════════════ B. « Les immigrés représentent une part disproportionnée de la population carcérale. » ═════════════
FICHES.append(fiche(
 id='immigres-prisons-surrepresentation', affirmation="Les immigrés représentent une part disproportionnée de la population carcérale.", sous_theme=ST_PRISON,
 mots_cles=['immigrés', 'immigrés en prison', 'immigrés remplissent les prisons', 'remplissent', 'prisons', 'disproportionnée', 'surreprésentation', 'surreprésentés', 'dénominateur', 'pays de naissance', 'population carcérale', 'facteurs', 'âge', 'précarité'],
 verdict='inverifiable', fiabilite='interpretation',
 resume="La statistique pénitentiaire régulière compte la nationalité, pas le statut d'immigré. On sait que les ÉTRANGERS sont surreprésentés (24,2 % des détenus pour 8,8 % de la population), mais on ne peut pas en déduire la part des IMMIGRÉS : un tiers des immigrés sont français, et certains étrangers sont nés en France.",
 contexte="Les mots « immigré » et « étranger » sont souvent employés l'un pour l'autre. Ils désignent des populations différentes : 7,7 millions d'immigrés et 6,0 millions d'étrangers en 2024 (Insee), qui ne se recouvrent qu'en partie.",
 explication="Pour parler de « part disproportionnée », il faut un numérateur (les détenus d'une catégorie) et un dénominateur (la même catégorie dans la population). Pour les étrangers, les deux existent. Pour les immigrés, le numérateur n'est pas publié régulièrement. Et même une surreprésentation mesurée devrait être comparée à structure d'âge, de sexe et de situation sociale proche avant d'être interprétée.",
 sources=[INSEE_ETR, AN_DETENUS, INSEE_DOS],
 faits=[
  fait("En 2024, la France compte 7,7 millions d'immigrés (11,3 % de la population) et 6,0 millions d'étrangers (8,8 %) ; 0,9 million d'étrangers sont nés en France.", 'insee_etr', '2024 (provisoire)', 'Population résidant en France', "Immigrés et étrangers ne sont pas la même population.", 'etabli', '11,3 % / 8,8 %'),
  fait("La part des étrangers parmi les détenus est de 24,2 % au 1er avril 2026 ; les données proviennent des applicatifs de l'administration pénitentiaire, fondés sur la nationalité.", 'an_detenus', '1er avril 2026', 'Personnes détenues', "Aucune donnée régulière sur le pays de naissance ou le statut d'immigré des détenus n'est communiquée.", 'etabli', '24,2 %'),
  fait("Les mis en cause sont des auteurs présumés et non des condamnés ; toutes les victimes ne portent pas plainte.", 'insee_dos', '2019', 'Statistiques de police et de gendarmerie', "Chaque étape de la chaîne pénale filtre différemment les personnes.", 'etabli'),
 ],
 court="Les chiffres officiels comptent les étrangers (24,2 % des détenus), pas les immigrés. Un tiers des immigrés sont français : on ne peut pas utiliser un chiffre pour l'autre.",
 moyen="Sur les étrangers, le chiffre existe : environ un quart des détenus, pour 8,8 % de la population. C'est une surreprésentation réelle. Sur les immigrés, en revanche, la statistique pénitentiaire régulière ne dit rien : elle compte la nationalité. Or un immigré sur trois est devenu français, et des étrangers sont nés en France. Dire « les immigrés » à partir d'un chiffre sur les étrangers, c'est changer de population en cours de route. Et pour parler de disproportion, il faudrait aussi comparer à âge, sexe et milieu social égaux.",
 detaille="La phrase mélange souvent deux catégories. Les étrangers sont les personnes qui n'ont pas la nationalité française : 6,0 millions en 2024, dont 0,9 million nés en France. Les immigrés sont les personnes nées étrangères à l'étranger : 7,7 millions, dont un tiers ont acquis la nationalité française (Insee).\n\nPour les étrangers, on sait mesurer la surreprésentation : 24,2 % des détenus au 1er avril 2026, pour 8,8 % de la population. Pour les immigrés, l'administration pénitentiaire ne publie pas de chiffre régulier : ses fichiers enregistrent la nationalité, pas le pays de naissance.\n\nMême pour les étrangers, « disproportionné » mérite d'être précisé. Une comparaison brute ignore l'âge et le sexe (les détenus sont très majoritairement des hommes jeunes), les conditions sociales, la détention provisoire plus fréquente faute de garanties de représentation, et les infractions liées au séjour. Ces facteurs ne nient pas l'écart ; ils empêchent d'en tirer une explication par l'origine.\n\nEnfin, chaque étape de la chaîne pénale (mise en cause, poursuite, condamnation, incarcération) a ses propres filtres : un chiffre sur les mis en cause ne dit pas la même chose qu'un chiffre sur les détenus.",
 empathie="C'est une vraie question, et il y a un chiffre exact derrière : les étrangers sont surreprésentés en prison. Mais « immigrés », ce n'est pas la même chose, et les statistiques officielles ne permettent pas de répondre pour eux. Je préfère te dire ce qu'on sait vraiment que de lancer un chiffre au hasard.",
 legitimes=["Les étrangers, qui sont une partie des immigrés, sont nettement surreprésentés parmi les détenus."],
 contre=[
  ("C'est pareil, étrangers ou immigrés.", "Non : un tiers des immigrés sont français, et 0,9 million d'étrangers sont nés en France. Ce sont deux populations différentes, de tailles différentes, et les statistiques ne permettent pas de passer de l'une à l'autre."),
  ("Si on comptait les binationaux et les naturalisés, ce serait encore pire.", "Peut-être, peut-être pas : aucune donnée officielle publiée ne permet de le dire. Affirmer un chiffre qu'on n'a pas, c'est remplacer la statistique par une impression."),
 ],
 questions=["Quand tu dis « immigrés », tu penses aux personnes de nationalité étrangère, ou aussi aux Français nés à l'étranger ?", "Quelle comparaison te semblerait juste : avec toute la population, ou avec des hommes du même âge et du même milieu ?"],
 limites=["Aucune statistique pénitentiaire régulière n'est publiée selon le pays de naissance ou le statut d'immigré.", "Les comparaisons à structure d'âge et de sexe égale ne sont pas publiées dans ces sources."],
 a_actualiser='2027-06-30', raison="Nouvelles données Insee et pénitentiaires annuelles.",
))

# ═════════════ C. « La délinquance est principalement liée à l'immigration. » ═════════════
FICHES.append(fiche(
 id='delinquance-principalement-immigration', affirmation="La délinquance est principalement liée à l'immigration.", sous_theme=ST_PRISON,
 mots_cles=['délinquance', 'principalement', 'immigration', 'étrangers', 'mis en cause', 'auteurs', 'vols', 'violences', 'insécurité', 'criminalité'],
 verdict='contredit', fiabilite='etabli',
 resume="En 2019, les étrangers représentaient 17,7 % des personnes mises en cause par la police et la gendarmerie (dernière série détaillée publiée) : plus de huit auteurs présumés sur dix étaient français. Les étrangers sont surreprésentés, surtout pour les vols, mais la délinquance n'est pas « principalement » le fait d'étrangers.",
 contexte="« Principalement » signifie plus de la moitié. Les données publiques du ministère de l'Intérieur permettent de vérifier cette idée pour les étrangers (nationalité), pas pour les immigrés.",
 explication="Les mis en cause sont des personnes soupçonnées par la police ou la gendarmerie, pas des condamnés. Leur nationalité n'est pas toujours vérifiable. La part des étrangers varie beaucoup selon l'infraction : forte pour certains vols, plus faible pour les atteintes à la personne ou les dégradations.",
 sources=[INSEE_AUT, INSEE_DOS, INSEE_ETR],
 faits=[
  fait("En 2019, les étrangers représentent 17,7 % des personnes mises en cause (hors infractions routières).", 'insee_aut', '2019', 'France, mis en cause pour crimes et délits', "Plus de 82 % des auteurs présumés sont français.", 'etabli', '17,7 %'),
  fait("La part des étrangers parmi les mis en cause est de 26,6 % pour les vols, 13,1 % pour les atteintes à la personne, 13,5 % pour les infractions sexuelles, 11,5 % pour les stupéfiants et 10,8 % pour les destructions et dégradations.", 'insee_aut', '2019', 'Mis en cause par type d’infraction', "La surreprésentation est très variable selon les infractions.", 'etabli'),
  fait("En 2019, les étrangers forment 7 % des personnes résidant en France et 18 % des mis en cause ; 9 % des victimes d'atteintes personnelles sont étrangères.", 'insee_dos', '2019', 'France', "Les étrangers sont aussi surreprésentés parmi certaines victimes (16 % pour les violences sexuelles).", 'etabli', '7 % / 18 %'),
  fait("La nationalité ne peut pas toujours être vérifiée par les services faute de pièce d'identité ; elle n'est pas renseignée pour 11 % des auteurs traités par les parquets.", 'insee_aut', '2019', 'Méthodologie', "Les chiffres par nationalité sont à manier avec précaution.", 'etabli'),
 ],
 court="Selon le ministère de l'Intérieur, les étrangers représentaient 17,7 % des mis en cause en 2019 : plus de huit auteurs présumés sur dix sont français. Surreprésentés, oui ; « principalement », non.",
 moyen="Regardons les chiffres du ministère de l'Intérieur. En 2019, les étrangers étaient 7 % de la population et 17,7 % des personnes mises en cause : c'est une surreprésentation, surtout pour les vols (26,6 %). Mais ça veut dire que plus de 82 % des auteurs présumés étaient français. La délinquance n'est donc pas « principalement » liée aux étrangers. Et sur les immigrés, ces chiffres ne disent rien : ils comptent la nationalité.",
 detaille="Le mot « principalement » se vérifie facilement : il faudrait que plus de la moitié des auteurs soient étrangers. Ce n'est pas le cas.\n\nSelon la dernière série détaillée publiée par l'Insee à partir des données du ministère de l'Intérieur, les étrangers représentaient 17,7 % des personnes mises en cause en 2019 (hors infractions routières), alors qu'ils formaient 7 % de la population. Plus de huit auteurs présumés sur dix étaient donc français.\n\nLa surreprésentation est réelle et varie selon les infractions : 26,6 % pour les vols, mais 13,1 % pour les atteintes à la personne et 10,8 % pour les destructions et dégradations. Les étrangers sont aussi surreprésentés parmi certaines victimes : 16 % des victimes de violences sexuelles.\n\nTrois précautions. Les mis en cause ne sont pas des condamnés. Leur nationalité n'est pas toujours vérifiable. Et ces chiffres portent sur les étrangers, pas sur les immigrés, dont un tiers sont français.\n\nOn peut donc discuter d'une surreprésentation sur certaines infractions, de ses causes et des politiques adaptées. Mais dire que la délinquance est « principalement » liée à l'immigration ne correspond pas aux données publiques.",
 empathie="Je comprends l'inquiétude : certaines infractions, comme les vols, sont commises plus souvent par des étrangers, et c'est dans les chiffres. Mais la grande majorité des délits sont commis par des Français. Si on ne regarde qu'une partie, on se trompe de cible et on protège moins bien.",
 legitimes=["Les étrangers sont surreprésentés parmi les mis en cause, en particulier pour les vols."],
 contre=[
  ("Les chiffres de 2019 sont anciens, ça a empiré.", "C'est la dernière série détaillée publiée par nationalité et par infraction. La part des étrangers était en hausse entre 2016 et 2019 (de 16 % à 18 %) : même en supposant une hausse depuis, on est très loin de la moitié."),
  ("Dans ma ville, ce sont toujours des étrangers.", "Ce que tu vois autour de toi est réel pour toi, et la situation varie selon les quartiers et les infractions. Mais au niveau national, plus de huit auteurs présumés sur dix sont français."),
 ],
 questions=["Quelle part des auteurs aurais-tu estimée avant de voir le chiffre ?", "Si la majorité des auteurs sont français, quelle politique protégerait le mieux les victimes ?"],
 limites=["Dernière série détaillée par nationalité : données 2019.", "Mis en cause ≠ condamnés ; nationalité parfois non vérifiée.", "Aucune donnée comparable n'est publiée pour les immigrés."],
 publics={'convaincus': "Selon le ministère de l'Intérieur, plus de huit personnes mises en cause sur dix étaient françaises en 2019. Les étrangers sont surreprésentés, surtout pour les vols, c'est vrai. Mais « principalement », non : l'essentiel de la délinquance est le fait de Français.",
  'indecis': "Il est légitime de regarder les chiffres : en 2019, les étrangers représentaient 17,7 % des personnes mises en cause, plus que leur part dans la population. Mais plus de 80 % des auteurs présumés étaient français. Lutter contre la délinquance suppose donc d'en traiter les causes pour tout le monde."},
 a_actualiser='2027-06-30', raison="Une série plus récente par nationalité pourrait être publiée par le SSMSI.",
))

# ═════════════ D. « La France serait plus sûre si elle accueillait moins d'immigrés. » ═════════════
FICHES.append(fiche(
 id='france-plus-sure-moins-immigres', affirmation="La France serait plus sûre si elle accueillait moins d'immigrés.", sous_theme=ST_PRISON,
 mots_cles=['plus sûre', 'moins d immigrés', 'accueillir moins', 'réduire l immigration', 'sécurité', 'causalité', 'immigration et criminalité', 'études', 'insécurité'],
 verdict='inverifiable', fiabilite='debat',
 resume="C'est une hypothèse causale, pas un constat. Les étrangers sont surreprésentés parmi les mis en cause et les détenus, mais cela ne prouve pas que réduire l'immigration réduirait la délinquance. Une étude de référence sur l'Italie montre une corrélation, mais un effet causal limité aux vols avec violence et un effet global non significatif.",
 contexte="L'affirmation porte sur ce qui se passerait si une politique changeait. Pour y répondre, il faut des études qui isolent l'effet de l'immigration des autres facteurs (âge, pauvreté, urbanisation, conditions d'accueil).",
 explication="Corrélation n'est pas causalité. Les territoires qui attirent les immigrés sont souvent urbains, jeunes et plus touchés par certaines délinquances, pour d'autres raisons. Les économistes utilisent des méthodes (variables instrumentales, expériences naturelles) pour séparer ces effets. Leurs résultats varient selon les pays, les périodes, le statut légal des migrants et le type d'infraction.",
 sources=[BBP, INSEE_AUT, AN_DETENUS],
 faits=[
  fait("Dans les provinces italiennes (1990-2003), la population immigrée est corrélée à la délinquance, mais l'effet causal estimé ne porte que sur les vols avec violence ; l'effet sur le taux global de délinquance n'est pas statistiquement différent de zéro.", 'bbp', '1990-2003', 'Provinces italiennes', "Une corrélation peut disparaître quand on isole la causalité.", 'estimation'),
  fait("En France, les étrangers représentaient 17,7 % des mis en cause en 2019.", 'insee_aut', '2019', 'France, mis en cause', "Même une forte baisse du nombre d'étrangers laisserait la grande majorité de la délinquance inchangée.", 'etabli', '17,7 %'),
  fait("Les étrangers représentent 24,2 % des détenus au 1er avril 2026.", 'an_detenus', '1er avril 2026', 'Personnes détenues', "Surreprésentation réelle, dont les causes ne sont pas établies par ce chiffre.", 'etabli', '24,2 %'),
 ],
 court="C'est une hypothèse, pas un fait : être surreprésenté n'est pas être la cause. Une étude de référence sur l'Italie trouve un effet de l'immigration limité aux vols avec violence, et nul sur la délinquance globale.",
 moyen="Il faut distinguer deux choses. Oui, les étrangers sont surreprésentés parmi les mis en cause et les détenus. Mais « la France serait plus sûre avec moins d'immigrés » suppose une cause. Les études qui cherchent vraiment cet effet trouvent des résultats nuancés : en Italie, par exemple, l'effet causal de l'immigration ne concerne que les vols avec violence, et l'effet sur la délinquance totale n'est pas significatif. Et en France, plus de huit auteurs présumés sur dix sont français.",
 detaille="Cette phrase est une prédiction : elle dit ce qui arriverait si on changeait une politique. Les statistiques actuelles ne suffisent pas à la démontrer.\n\nCe qu'on sait : les étrangers sont surreprésentés parmi les mis en cause (17,7 % en 2019) et parmi les détenus (24,2 % en 2026). Ce qu'on ne sait pas avec ces seuls chiffres : si cette surreprésentation vient de la nationalité ou de facteurs qui l'accompagnent (âge, sexe, pauvreté, logement, isolement, statut administratif précaire).\n\nLes économistes ont étudié cette question. Une étude souvent citée (Bianchi, Buonanno et Pinotti) sur les provinces italiennes trouve une corrélation entre immigration et délinquance ; mais en isolant l'effet causal, seul celui sur les vols avec violence subsiste, et l'effet sur le taux global de délinquance n'est pas statistiquement différent de zéro. D'autres travaux, dans d'autres pays, trouvent des effets différents selon le type de migration, le statut légal et l'accès à l'emploi.\n\nEnfin, l'arithmétique compte : si plus de 80 % des auteurs présumés sont français, réduire l'immigration ne toucherait au mieux qu'une minorité de la délinquance. Les politiques de sécurité qui fonctionnent ciblent les infractions, les lieux et les parcours, quelle que soit la nationalité.",
 empathie="Tu veux qu'on soit plus en sécurité, et je le veux aussi. La question, c'est ce qui marche vraiment. Les études montrent que ce n'est pas si simple que « moins d'immigrés, moins de délits ». Si on se trompe de remède, on n'est pas mieux protégés.",
 legitimes=["Certaines formes de délinquance sont associées à des parcours migratoires précaires ou à des filières criminelles organisées.", "Les étrangers sont surreprésentés parmi les mis en cause et les détenus."],
 contre=[
  ("C'est du bon sens : moins d'étrangers, moins d'étrangers délinquants.", "Arithmétiquement, oui pour les étrangers ; mais la délinquance totale dépend surtout des 80 % d'auteurs français et des conditions sociales. Les études qui mesurent l'effet global trouvent souvent un effet faible ou nul."),
  ("Une étude italienne ne dit rien de la France.", "C'est juste : elle illustre la différence entre corrélation et causalité, elle ne prouve rien pour la France. Mais c'est justement pourquoi on ne peut pas affirmer l'inverse sans étude française du même type."),
 ],
 questions=["Qu'est-ce qui, selon toi, ferait le plus baisser la délinquance dans ta ville ?", "Si on réduisait l'immigration de moitié, quelle part des délits disparaîtrait à ton avis ?"],
 limites=["Il n'existe pas, dans les sources citées, d'étude causale récente portant sur la France entière.", "Les résultats des études varient selon les pays, les périodes et les types de migration."],
 a_actualiser='2027-10-30', raison="Nouvelles publications académiques sur le sujet.",
))

# ═════════════ E. « Les statistiques de délinquance démontrent que l'immigration augmente l'insécurité. » ═════════════
FICHES.append(fiche(
 id='statistiques-prouvent-insecurite-immigration', affirmation="Les statistiques de délinquance démontrent que l'immigration augmente l'insécurité.", sous_theme=ST_PRISON,
 mots_cles=['statistiques', 'démontrent', 'prouvent', 'immigration augmente', 'insécurité', 'corrélation', 'causalité', 'mis en cause', 'chiffres de la délinquance'],
 verdict='trompeur', fiabilite='etabli',
 resume="Les statistiques montrent une association : les étrangers sont surreprésentés parmi les mis en cause (17,7 % pour 7 % de la population en 2019). Elles ne démontrent pas une causalité : elles ne contrôlent ni l'âge, ni le sexe, ni la situation sociale, et elles comptent les auteurs présumés, pas les coupables.",
 contexte="Le verbe « démontrer » est central. Une statistique descriptive peut établir un écart ; seule une étude conçue pour cela peut établir une cause.",
 explication="Les statistiques de police enregistrent des procédures et des personnes mises en cause. Elles dépendent des plaintes, des contrôles et des priorités des services. Elles décrivent qui est mis en cause, pas pourquoi. Pour parler de cause, il faut comparer des groupes semblables sur tout le reste, ou utiliser des méthodes adaptées.",
 sources=[INSEE_DOS, INSEE_AUT, BBP],
 faits=[
  fait("En 2019, les étrangers représentent 18 % des mis en cause pour 7 % des résidents.", 'insee_dos', '2019', 'France', "C'est une association statistique, exacte.", 'etabli', '18 % / 7 %'),
  fait("Les mis en cause sont des auteurs présumés, non des condamnés, et les procédures enregistrées ne reflètent que partiellement les infractions commises.", 'insee_dos', '2019', 'Méthodologie', "Le chiffre dépend aussi de l'activité des services et des plaintes.", 'etabli'),
  fait("La nationalité des mis en cause ne peut pas toujours être vérifiée.", 'insee_aut', '2019', 'Méthodologie', "Précaution supplémentaire avant toute conclusion.", 'etabli'),
  fait("Une étude italienne trouve une corrélation entre immigration et délinquance, mais un effet causal limité aux vols avec violence et non significatif sur la délinquance globale.", 'bbp', '1990-2003', 'Italie', "La corrélation et la cause ne coïncident pas forcément.", 'estimation'),
 ],
 court="Les statistiques montrent une surreprésentation, pas une cause : elles ne tiennent compte ni de l'âge, ni du sexe, ni de la pauvreté, et comptent des suspects, pas des coupables.",
 moyen="Le chiffre est vrai : en 2019, les étrangers sont 18 % des mis en cause pour 7 % de la population. Mais ce chiffre décrit, il ne démontre pas. Il ne compare pas des gens du même âge, du même sexe et du même milieu. Il compte des suspects, pas des condamnés. Et il dépend des plaintes et des contrôles. Pour dire « l'immigration augmente l'insécurité », il faut des études conçues pour isoler une cause ; celles qui existent trouvent des effets limités ou nuls sur la délinquance globale.",
 detaille="Il y a une différence entre montrer et démontrer.\n\nCe que les statistiques montrent : en 2019, les étrangers représentaient 18 % des personnes mises en cause par la police et la gendarmerie, alors qu'ils formaient 7 % de la population. Cette surreprésentation est exacte.\n\nCe qu'elles ne démontrent pas : que la nationalité ou l'immigration en soit la cause. Une comparaison brute ne tient pas compte de l'âge et du sexe (la délinquance enregistrée est surtout le fait d'hommes jeunes), de la pauvreté, du lieu de résidence, de la précarité administrative. Elle compte des auteurs présumés, pas des coupables, et dépend des plaintes et de l'activité des services. La nationalité elle-même n'est pas toujours vérifiable.\n\nPour établir une cause, les chercheurs utilisent des méthodes spécifiques. Une étude de référence sur l'Italie trouve une corrélation, mais un effet causal limité aux vols avec violence, et nul sur la délinquance globale. D'autres études trouvent d'autres résultats selon les contextes.\n\nConclusion honnête : la surreprésentation est un fait à prendre au sérieux ; la causalité, elle, n'est pas démontrée par ces statistiques.",
 empathie="Le chiffre que tu cites est vrai, et c'est normal qu'il fasse réagir. Simplement, un chiffre peut montrer un écart sans en expliquer la cause. Si on veut des solutions efficaces, il faut savoir ce qui produit vraiment la délinquance.",
 legitimes=["La surreprésentation des étrangers parmi les mis en cause est un fait statistique exact."],
 contre=[
  ("Les chiffres parlent d'eux-mêmes.", "Ils disent qui est mis en cause, pas pourquoi. Les hommes jeunes sont aussi très surreprésentés : personne n'en conclut que « être un homme » est la cause unique de la délinquance."),
  ("Même en tenant compte de l'âge, l'écart reste.", "C'est possible pour certaines infractions ; les sources citées ne publient pas ce calcul. Même un écart restant ne serait pas une preuve de cause : il resterait la pauvreté, le logement, le statut administratif, les contrôles."),
 ],
 questions=["Pour toi, quelle différence y a-t-il entre « les étrangers sont plus souvent mis en cause » et « l'immigration crée l'insécurité » ?", "Quelle information te convaincrait que c'est une cause, et pas seulement une coïncidence ?"],
 limites=["Les sources citées ne publient pas de comparaison à structure d'âge et de sexe identique.", "Données détaillées par nationalité : 2019."],
 a_actualiser='2027-06-30', raison="Nouvelles séries statistiques ou études causales.",
))

# ═════════════ F. « Tous les étrangers condamnés devraient être expulsés. » ═════════════
FICHES.append(fiche(
 id='expulser-tous-etrangers-condamnes', type='reponse_critique', affirmation="Tous les étrangers condamnés devraient être expulsés.", sous_theme=ST_EXPUL,
 mots_cles=['expulser', 'expulsion', 'expulsés', 'renvoyer', 'renvoyer chez eux', 'étrangers condamnés', 'OQTF', 'interdiction du territoire', 'ITF', 'double peine', 'tous les renvoyer'],
 verdict='opinion', fiabilite='etabli',
 resume="C'est une proposition politique. Le droit actuel permet déjà d'éloigner beaucoup d'étrangers condamnés : interdiction du territoire prononcée par le juge, expulsion administrative en cas de menace grave, avec des protections renforcées pour les personnes ayant de fortes attaches en France, elles-mêmes levées pour les condamnations graves depuis 2024. Le principal obstacle est l'exécution : environ 10 % des OQTF sont exécutées.",
 contexte="Le mot « condamné » recouvre des situations très différentes : contravention, délit mineur, crime grave. Le droit distingue aussi la peine prononcée par un juge (l'interdiction du territoire) et les mesures administratives décidées par le préfet ou le ministre (OQTF, expulsion).",
 explication="L'OQTF est une décision administrative (départ sous 30 jours). L'arrêté d'expulsion vise une personne dont la présence constitue une menace grave pour l'ordre public ; une condamnation ne suffit pas à elle seule. L'interdiction du territoire français (ITF) est une peine complémentaire décidée par un juge pénal, définitive ou jusqu'à dix ans, exécutée à la fin de la peine de prison. L'extradition, enfin, est la remise d'une personne à un autre État qui la poursuit : c'est une autre procédure. Un crime (jugé par une cour d'assises ou criminelle) est plus grave qu'un délit (tribunal correctionnel), lui-même plus grave qu'une contravention.",
 sources=[AN_EXPUL, CP_ITF, PUBSEN, CDC, CEDH],
 faits=[
  fait("L'interdiction du territoire français peut être prononcée par le juge, à titre définitif ou pour dix ans au plus, contre tout étranger coupable d'un crime ou d'un délit ; elle entraîne de plein droit la reconduite à la frontière, le cas échéant à l'expiration de la peine de prison.", 'cp_itf', 'Droit en vigueur', 'Code pénal, article 131-30', "La possibilité d'éloigner un étranger condamné existe déjà dans la loi pénale.", 'etabli'),
  fait("Le CESEDA permet l'expulsion d'un étranger dont la présence constitue une menace grave pour l'ordre public ; depuis la loi du 26 janvier 2024, les protections des étrangers ayant de fortes attaches sont levées en cas de condamnation définitive pour des faits punis d'au moins trois ans (protection relative) ou cinq ans (protection renforcée, trois ans en récidive) ; les mineurs restent protégés.", 'an_expul', 'Droit en vigueur depuis 2024', 'CESEDA, articles L. 631-1 à L. 631-4', "Les protections existent, mais elles ne couvrent plus les condamnations graves.", 'etabli'),
  fait("Sur 447 257 OQTF prononcées de 2019 à 2022, seule une petite minorité, autour de 10 %, est exécutée ; de nombreux pays d'origine sont réticents à délivrer les laissez-passer consulaires.", 'cdc', '2019-2022', 'France', "Le problème principal n'est pas l'absence de décision, mais son exécution.", 'etabli', '≈ 10 %'),
  fait("En 2022, 341 mesures d'expulsion ont été prononcées et 167 exécutées ; en 2023, 58 arrêtés ministériels d'expulsion ont été exécutés à 63 %.", 'an_expul', '2022-2023', 'Arrêtés d’expulsion', "L'expulsion pour menace grave est exécutée bien plus souvent que l'OQTF ordinaire.", 'etabli'),
  fait("La Cour européenne des droits de l'homme admet l'expulsion d'un étranger condamné, mais exige une mise en balance : gravité de l'infraction, durée du séjour, vie familiale, intérêt des enfants, liens avec le pays d'origine.", 'cedh', '18 octobre 2006', 'CEDH, Üner c. Pays-Bas', "L'automatisme est exclu, pas l'expulsion.", 'etabli'),
 ],
 court="La loi permet déjà d'expulser ou d'interdire du territoire des étrangers condamnés, surtout pour les faits graves. Le vrai problème, c'est l'exécution : environ 10 % des OQTF sont exécutées, faute notamment de laissez-passer des pays d'origine.",
 moyen="On peut vouloir plus d'expulsions, c'est un choix politique. Mais il faut savoir ce qui existe déjà. Un juge peut prononcer une interdiction du territoire, définitive ou jusqu'à dix ans, exécutée après la prison. Le préfet ou le ministre peut expulser quelqu'un qui représente une menace grave. Depuis 2024, même les étrangers qui ont de fortes attaches en France perdent leur protection en cas de condamnation grave. Ce qui bloque surtout, c'est l'exécution : la Cour des comptes estime qu'environ 10 % des OQTF sont exécutées. Et « tous les condamnés », ça inclut aussi des délits mineurs, ou des gens arrivés enfants en France.",
 detaille="Cette proposition mélange trois questions : faut-il éloigner ? qui ? et est-ce faisable ?\n\nCe que dit déjà le droit. Le juge pénal peut prononcer une interdiction du territoire français contre tout étranger coupable d'un crime ou d'un délit, définitive ou pour dix ans au plus ; elle est exécutée à la fin de la peine de prison. Le préfet ou le ministre peut, par ailleurs, expulser un étranger dont la présence constitue une menace grave pour l'ordre public. Certaines personnes sont protégées en raison de leurs attaches (arrivées enfants, parents d'enfants français, résidents de longue date) ; depuis la loi du 26 janvier 2024, ces protections sont levées pour les condamnations à des faits punis d'au moins trois ou cinq ans. Les mineurs restent protégés.\n\nCe que la proposition changerait. « Tous les condamnés » inclurait des délits mineurs et des personnes ayant grandi en France, sans examen individuel. Or la Cour européenne des droits de l'homme admet l'expulsion d'étrangers condamnés, mais exige une mise en balance (gravité des faits, durée du séjour, famille, enfants, liens avec le pays d'origine). Un automatisme total serait très probablement jugé contraire à ces exigences.\n\nCe qui bloque en pratique. Selon la Cour des comptes, environ 10 % des OQTF sont exécutées : identification difficile, réticence de nombreux pays à délivrer des laissez-passer consulaires, refus d'embarquer. L'expulsion pour menace grave est mieux exécutée (63 % des arrêtés ministériels en 2023), justement parce qu'elle est ciblée.\n\nLa question honnête n'est donc pas « expulser ou ne rien faire », mais : quelles personnes, avec quelles garanties, et comment rendre les décisions réellement exécutables, tout en protégeant les victimes ?",
 empathie="Je comprends parfaitement qu'on ne veuille pas que quelqu'un qui a commis un crime grave reste en France ; c'est une demande de justice. La loi le permet déjà dans beaucoup de cas. Ce qui coince surtout, c'est que les renvois ne sont pas exécutés. C'est là-dessus qu'on pourrait être d'accord pour agir.",
 legitimes=["Les mesures d'éloignement, en particulier les OQTF, sont très peu exécutées.", "Protéger les victimes et prévenir la récidive est une exigence légitime."],
 contre=[
  ("Les protections, c'est de l'impunité.", "Non : la personne est jugée et purge sa peine en France. Les protections encadrent seulement l'éloignement des personnes qui ont toute leur vie ici, et elles sont levées pour les condamnations graves depuis 2024."),
  ("Si on expulsait vraiment, il y aurait moins de délinquance.", "En 2019, plus de 80 % des mis en cause étaient français. L'expulsion peut retirer du territoire des auteurs graves, mais elle ne peut pas, à elle seule, réduire fortement la délinquance totale."),
  ("Pourquoi garder en France quelqu'un qui a commis un crime ?", "Souvent, on ne le garde pas : le juge peut prononcer une interdiction du territoire. Quand la personne est protégée, c'est qu'elle a grandi en France ou y a sa famille ; depuis 2024, même cette protection tombe pour les crimes graves. Et la peine de prison est d'abord purgée en France, ce qui protège aussi les victimes."),
 ],
 questions=["Pour toi, faut-il traiter de la même façon un vol à l'étalage et un crime violent ?", "Si un pays refuse de reprendre la personne, que proposes-tu concrètement ?"],
 limites=["Les chiffres d'exécution datent de 2022-2023 ; la loi de 2024 a pu les modifier.", "Les textes de loi évoluent : vérifier la version en vigueur sur Légifrance avant toute affirmation juridique précise.", "Les données ne permettent pas de mesurer l'effet des expulsions sur la récidive."],
 a_actualiser='2027-04-30', raison="Législation sur l'immigration en évolution fréquente ; nouvelles données d'exécution.",
))

# ═════════════ G. « Un étranger qui commet un crime n'a plus sa place en France. » ═════════════
FICHES.append(fiche(
 id='etranger-crime-plus-sa-place', type='reponse_critique', affirmation="Un étranger qui commet un crime n'a plus sa place en France.", sous_theme=ST_EXPUL,
 mots_cles=['commet un crime', 'plus sa place', 'garder en france', 'pourquoi garder', 'criminel étranger', 'crime', 'commis un crime', 'expulser', 'victimes'],
 verdict='opinion', fiabilite='etabli',
 resume="C'est un jugement moral, que le droit reprend en partie : pour un crime, le juge peut prononcer une interdiction du territoire et le préfet peut expulser une personne menaçante. Depuis 2024, même les étrangers très attachés à la France perdent leur protection pour les condamnations graves. La peine est d'abord purgée en France.",
 contexte="Un crime, au sens juridique, est l'infraction la plus grave (meurtre, viol, vol à main armée…), jugée par une cour d'assises ou une cour criminelle. Le langage courant appelle souvent « crime » des délits.",
 explication="La réponse pénale (le procès et la peine) et l'éloignement (l'expulsion ou l'interdiction du territoire) sont deux choses distinctes. La première sanctionne et protège la société ; la seconde décide si la personne peut rester sur le territoire après. Les deux peuvent se cumuler.",
 sources=[CP_ITF, AN_EXPUL, CEDH, CE2026],
 faits=[
  fait("Le juge peut prononcer une interdiction du territoire contre tout étranger coupable d'un crime ou d'un délit ; elle entraîne la reconduite à la frontière à l'expiration de la peine de prison.", 'cp_itf', 'Droit en vigueur', 'Code pénal, article 131-30', "La peine de prison est purgée, puis l'éloignement intervient.", 'etabli'),
  fait("Les étrangers les plus protégés (arrivés avant 13 ans, résidents de plus de vingt ans…) peuvent être expulsés en cas de condamnation définitive pour des faits punis d'au moins cinq ans (trois en récidive), depuis la loi du 26 janvier 2024.", 'an_expul', 'Depuis 2024', 'CESEDA, article L. 631-3', "Pour les crimes, la protection n'empêche plus l'expulsion.", 'etabli'),
  fait("La CEDH admet l'expulsion d'un étranger installé condamné pour homicide, en jugeant la mesure proportionnée à la gravité des faits.", 'cedh', '18 octobre 2006', 'CEDH, Üner c. Pays-Bas', "Le droit européen n'interdit pas d'expulser des criminels ; il exige un examen individuel.", 'etabli'),
  fait("Le 9 juin 2026, le Conseil d'État a rendu trois décisions illustrant le contrôle de proportionnalité entre vie familiale et protection de l'ordre public dans l'expulsion d'étrangers protégés.", 'ce2026', '9 juin 2026', "Conseil d'État, n° 506729, 504383, 505954", "Le juge vérifie, au cas par cas, l'équilibre entre ces deux exigences.", 'etabli'),
 ],
 court="Pour un crime, la loi permet déjà d'interdire le territoire ou d'expulser, même les étrangers très attachés à la France depuis 2024. Le juge examine chaque cas, et la peine est d'abord purgée ici.",
 moyen="Sur le fond, beaucoup de gens sont d'accord, et la loi va déjà dans ce sens. Pour un crime, le juge peut ajouter une interdiction du territoire à la peine de prison : la personne est renvoyée à la fin de sa peine. Depuis 2024, même ceux qui sont arrivés enfants ou vivent ici depuis vingt ans peuvent être expulsés après une condamnation grave. Ce qui reste, c'est un examen au cas par cas, exigé par la Cour européenne des droits de l'homme, qui a d'ailleurs validé l'expulsion d'un homme condamné pour homicide.",
 detaille="La phrase exprime une exigence de justice que le droit français reprend largement.\n\nD'abord, la sanction : un étranger qui commet un crime est jugé et condamné comme n'importe qui ; il purge sa peine en France. Ensuite, l'éloignement : le juge peut prononcer une interdiction du territoire français, définitive ou jusqu'à dix ans, qui entraîne la reconduite à la frontière à la fin de la peine. L'administration peut aussi prendre un arrêté d'expulsion si la présence de la personne constitue une menace grave.\n\nLes protections existent pour les personnes qui ont toute leur vie en France (arrivées avant 13 ans, résidentes depuis plus de vingt ans, parents d'enfants français). Depuis la loi du 26 janvier 2024, elles sont levées en cas de condamnation pour des faits punis d'au moins cinq ans (trois en récidive) : c'est le cas des crimes.\n\nCe qui demeure, c'est l'examen individuel. La Cour européenne des droits de l'homme ne protège pas les criminels contre l'expulsion : elle demande qu'on mette en balance la gravité des faits, la durée du séjour et la famille. Dans l'affaire Üner, elle a validé l'expulsion d'un homme condamné pour homicide. En 2026 encore, le Conseil d'État a rappelé ce contrôle de proportionnalité.\n\nLa vraie difficulté est souvent ailleurs : certains pays refusent ou retardent le retour de leurs ressortissants. Une décision d'éloignement n'est utile que si elle est exécutable.",
 empathie="Je partage l'idée qu'un crime grave doit avoir des conséquences lourdes, et les victimes ont droit à cette fermeté. La loi le permet déjà, y compris pour des gens installés depuis longtemps. Ce qu'on peut discuter, c'est comment rendre ces décisions vraiment applicables.",
 legitimes=["Pour un crime grave, l'éloignement après la peine est une demande largement partagée et juridiquement possible."],
 contre=[
  ("Et s'il est arrivé bébé en France ?", "C'est justement le cas où la loi protégeait le plus. Depuis 2024, cette protection tombe pour les condamnations graves ; reste un examen individuel, car la personne n'a parfois aucun lien avec le pays de sa nationalité."),
  ("Pourquoi garder en France quelqu'un qui a commis un crime ?", "On ne le garde pas forcément : il purge sa peine, puis il peut être interdit du territoire ou expulsé. Quand il reste, c'est souvent parce que son pays refuse de le reprendre, ou parce qu'un juge a estimé, au cas par cas, que ses attaches l'emportaient."),
 ],
 questions=["Pour toi, la peine de prison doit-elle être purgée avant le renvoi, ou à la place ?", "Que faire si le pays d'origine refuse de reprendre la personne ?"],
 limites=["Le commentaire des décisions du Conseil d'État de 2026 est une source secondaire.", "Vérifier la version en vigueur du CESEDA sur Légifrance."],
 a_actualiser='2027-04-30', raison="Législation et jurisprudence en évolution.",
))

# ═════════════ H. « Il suffit d'expulser les délinquants étrangers pour réduire la criminalité. » ═════════════
FICHES.append(fiche(
 id='expulser-reduit-criminalite', affirmation="Il suffit d'expulser les délinquants étrangers pour réduire la criminalité.", sous_theme=ST_EXPUL,
 mots_cles=['il suffit', 'expulser', 'réduire la criminalité', 'baisser la délinquance', 'délinquants étrangers', 'efficacité', 'récidive', 'sécurité'],
 verdict='trompeur', fiabilite='etabli',
 resume="Expulser des auteurs dangereux peut avoir un effet sur certains faits, mais « il suffit » est faux : en 2019, plus de 80 % des personnes mises en cause étaient françaises, et seule une petite minorité des OQTF (environ 10 %) est exécutée. Aucune donnée publique ne mesure l'effet des expulsions sur la récidive.",
 contexte="La formule promet une solution simple à un problème multiple. Elle mérite d'être vérifiée sur trois plans : l'ampleur (quelle part de la délinquance ?), la faisabilité (les mesures sont-elles exécutées ?) et l'effet (empêchent-elles de nouveaux faits ?).",
 explication="Une politique de sécurité combine prévention, enquête, sanction, réinsertion et, pour les étrangers, éventuellement l'éloignement. L'éloignement retire une personne du territoire ; il ne traite ni les causes de la délinquance des autres auteurs, ni les réseaux qui recrutent de nouveaux auteurs.",
 sources=[INSEE_AUT, CDC, AN_EXPUL],
 faits=[
  fait("Les étrangers représentaient 17,7 % des personnes mises en cause en 2019.", 'insee_aut', '2019', 'France, mis en cause', "Même une expulsion totale ne toucherait qu'une minorité des auteurs.", 'etabli', '17,7 %'),
  fait("Autour de 10 % des OQTF sont exécutées ; les éloignements forcés sont passés de 18 915 en 2019 à 11 409 en 2022.", 'cdc', '2019-2022', 'France', "Prononcer une mesure ne suffit pas : il faut pouvoir l'exécuter.", 'etabli', '≈ 10 %'),
  fait("Un éloignement forcé coûte en moyenne 4 414 € et une journée de rétention environ 602 € ; les centres de rétention comptent 1 717 places.", 'cdc', '2022-2023', 'France', "Les moyens disponibles limitent le nombre d'éloignements possibles.", 'etabli'),
  fait("En 2023, 58 arrêtés ministériels d'expulsion ont été exécutés à 63 %.", 'an_expul', '2023', 'Arrêtés ministériels', "Les mesures ciblées sur les personnes dangereuses sont mieux exécutées.", 'etabli'),
 ],
 court="Plus de 80 % des mis en cause sont français, et environ 10 % des OQTF sont exécutées. Expulser des auteurs dangereux peut aider, mais ça ne « suffit » pas.",
 moyen="Expulser un délinquant dangereux, ça peut éviter des faits, personne ne le nie. Mais « il suffit » ne tient pas. D'abord parce que plus de huit auteurs présumés sur dix sont français : la majorité de la délinquance resterait. Ensuite parce que les mesures sont peu exécutées : environ 10 % des OQTF selon la Cour des comptes, faute notamment de laissez-passer des pays d'origine. Enfin, on n'a aucune donnée publique sur l'effet réel des expulsions sur la récidive.",
 detaille="La formule « il suffit » appelle trois vérifications.\n\nL'ampleur. Selon les données du ministère de l'Intérieur publiées par l'Insee, les étrangers représentaient 17,7 % des personnes mises en cause en 2019. Même si l'on éloignait tous les auteurs étrangers, plus de huit auteurs présumés sur dix resteraient concernés.\n\nLa faisabilité. La Cour des comptes constate qu'autour de 10 % des OQTF sont exécutées. Les éloignements forcés ont même baissé, de 18 915 en 2019 à 11 409 en 2022. Les obstacles sont concrets : identification, refus ou retards des pays d'origine pour délivrer des laissez-passer, places de rétention limitées (1 717), coût (4 414 € en moyenne par éloignement forcé). Les mesures ciblées sur les personnes dangereuses fonctionnent mieux : 63 % des arrêtés ministériels exécutés en 2023.\n\nL'effet. Aucune donnée publique ne mesure si les personnes éloignées auraient récidivé, ni si d'autres auteurs les remplacent dans les réseaux. Une politique de sécurité efficace combine prévention, enquête, sanction et, le cas échéant, éloignement ciblé.\n\nOn peut donc défendre un éloignement plus efficace des auteurs dangereux ; présenter l'expulsion comme une solution qui « suffit » est trompeur.",
 empathie="Je comprends qu'on cherche une solution rapide : la délinquance, ça pourrit la vie. Expulser les plus dangereux peut faire partie de la réponse. Mais si on croit que ça suffit, on oublie la grande majorité des délits, et les victimes avec.",
 legitimes=["L'éloignement des auteurs dangereux, quand il est exécuté, retire effectivement ces personnes du territoire.", "La faible exécution des OQTF est un vrai problème de crédibilité de l'État."],
 contre=[
  ("Si on les expulse, ils ne récidivent pas en France.", "Ceux qui sont réellement éloignés et ne reviennent pas, non. Mais aucune donnée publique ne mesure cet effet, et seule une minorité des mesures est exécutée. Ça ne touche pas les 80 % d'auteurs français."),
  ("Il suffit de mettre la pression sur les pays qui refusent.", "C'est une piste réelle, discutée par la Cour des comptes et le Parlement. Mais c'est une négociation diplomatique longue, pas une solution qui suffit à réduire la criminalité."),
 ],
 questions=["Selon toi, que deviendraient les réseaux de délinquance si on expulsait certains de leurs membres ?", "Qu'est-ce qui ferait baisser la délinquance des auteurs français, qui sont la majorité ?"],
 limites=["Aucune donnée publique sur la récidive après éloignement.", "Chiffres d'exécution antérieurs aux effets de la loi de 2024."],
 a_actualiser='2027-04-30', raison="Nouvelles données d'éloignement et effets de la loi de 2024.",
))

# ═════════════ I. « Les criminels étrangers sont protégés par la justice française. » ═════════════
FICHES.append(fiche(
 id='criminels-etrangers-proteges-justice', affirmation="Les criminels étrangers sont protégés par la justice française.", sous_theme=ST_EXPUL,
 mots_cles=['protégés', 'justice protège', 'laxisme', 'impunité', 'juges', 'criminels étrangers', 'garanties', 'recours', 'droits de l homme', 'CEDH'],
 verdict='trompeur', fiabilite='etabli',
 resume="Les étrangers sont jugés, condamnés et incarcérés : au 1er avril 2026, 13 906 étrangers détenus étaient condamnés. Le juge peut prononcer une interdiction du territoire. Les protections contre l'expulsion concernent l'éloignement de personnes ayant de fortes attaches en France, pas la sanction, et elles sont levées pour les condamnations graves depuis 2024. La principale difficulté est l'exécution des renvois.",
 contexte="Le sentiment d'impunité naît souvent de cas médiatisés : une personne sous OQTF commet une nouvelle infraction. Ces cas révèlent surtout des mesures non exécutées, plus qu'une protection accordée par les juges.",
 explication="Une garantie juridique n'est pas une impunité : le droit au recours, l'examen individuel et le respect de la vie familiale encadrent les décisions de l'État pour éviter les erreurs et l'arbitraire. Ils s'appliquent après la sanction pénale, pas à sa place.",
 sources=[AN_DETENUS, CP_ITF, AN_EXPUL, CDC],
 faits=[
  fait("Au 1er avril 2026, les détenus étrangers comprenaient 13 906 condamnés et 6 599 prévenus.", 'an_detenus', '1er avril 2026', 'Détenus étrangers', "Les étrangers sont jugés et incarcérés comme les autres.", 'etabli'),
  fait("Le juge pénal peut prononcer une interdiction du territoire, définitive ou de dix ans au plus, contre tout étranger coupable d'un crime ou d'un délit.", 'cp_itf', 'Droit en vigueur', 'Code pénal, article 131-30', "La justice dispose d'une peine spécifique d'éloignement.", 'etabli'),
  fait("Les protections contre l'expulsion (attaches familiales, arrivée dans l'enfance, long séjour) sont levées depuis 2024 en cas de condamnation définitive pour des faits punis d'au moins trois ou cinq ans ; les mineurs restent protégés.", 'an_expul', 'Depuis 2024', 'CESEDA, articles L. 631-2 à L. 631-4', "Les protections ont été réduites pour les faits graves.", 'etabli'),
  fait("Les difficultés d'éloignement tiennent surtout à l'identification, à la réticence des pays d'origine à délivrer des laissez-passer consulaires et aux refus d'embarquer.", 'cdc', '2019-2022', 'France', "L'obstacle principal est pratique et diplomatique.", 'etabli'),
 ],
 court="Les étrangers sont jugés et emprisonnés : près de 14 000 condamnés étrangers sont détenus. Ce qui bloque surtout, ce n'est pas la justice, c'est l'exécution des renvois, faute de laissez-passer des pays d'origine.",
 moyen="Regardons les faits. Au 1er avril 2026, près de 14 000 étrangers condamnés étaient en prison : ils ne sont pas protégés de la sanction. Le juge peut même ajouter une interdiction du territoire. Les protections dont on parle concernent seulement l'expulsion de gens qui ont grandi en France ou y ont leur famille, et depuis 2024 elles tombent pour les condamnations graves. Quand une décision de renvoi n'est pas appliquée, c'est le plus souvent parce que le pays d'origine refuse le retour, selon la Cour des comptes.",
 detaille="Le mot « protégés » recouvre deux idées différentes.\n\nProtégés de la sanction ? Non. Les étrangers sont poursuivis, jugés et condamnés comme les Français. Au 1er avril 2026, 13 906 détenus étrangers purgeaient une condamnation, et 6 599 attendaient leur jugement en détention. Le juge dispose même d'une peine supplémentaire réservée aux étrangers : l'interdiction du territoire, définitive ou de dix ans au plus.\n\nProtégés de l'expulsion ? Partiellement, et de moins en moins. Le droit protège certaines personnes en raison de leurs attaches : arrivées avant 13 ans, résidentes depuis vingt ans, parents d'enfants français. Depuis la loi du 26 janvier 2024, ces protections sont levées pour les condamnations à des faits punis d'au moins trois ou cinq ans. Les mineurs restent protégés.\n\nCes garanties ont une fonction : éviter qu'une personne qui n'a jamais vécu ailleurs soit envoyée dans un pays qu'elle ne connaît pas sans examen de sa situation, comme l'exige la Cour européenne des droits de l'homme. Elles ont des limites et peuvent être débattues.\n\nMais la principale raison pour laquelle des personnes condamnées restent en France, selon la Cour des comptes, est pratique : identification difficile, refus ou retards des pays d'origine pour délivrer des laissez-passer, refus d'embarquer. Ce n'est pas la justice qui protège, c'est l'exécution qui échoue.",
 empathie="Je comprends ce sentiment d'injustice, surtout quand on entend parler de quelqu'un qui récidive alors qu'il devait partir. Ça choque, et ça doit être corrigé. Mais dans la plupart de ces cas, ce n'est pas un juge qui l'a protégé : c'est le renvoi qui n'a pas pu être exécuté.",
 legitimes=["Des personnes sous mesure d'éloignement non exécutée commettent parfois de nouvelles infractions.", "Les garanties juridiques allongent les procédures."],
 contre=[
  ("Les juges annulent les expulsions.", "Le juge administratif contrôle la légalité et la proportionnalité des décisions, comme pour toute décision de l'État ; c'est sa fonction. Les données publiques citées ne permettent pas de chiffrer la part des mesures annulées par rapport à celles qui ne sont pas exécutées pour des raisons pratiques."),
  ("La Cour européenne des droits de l'homme empêche d'expulser.", "Non : elle a validé l'expulsion d'un étranger installé condamné pour homicide (Üner c. Pays-Bas, 2006). Elle exige seulement une mise en balance au cas par cas."),
 ],
 questions=["Si une personne a grandi en France depuis l'âge de deux ans, faut-il examiner sa situation avant de l'expulser ?", "Pour toi, qui est responsable quand un pays refuse de reprendre son ressortissant ?"],
 limites=["Pas de donnée publique dans ces sources sur le nombre de mesures annulées par les juges.", "Vérifier la version en vigueur du CESEDA sur Légifrance."],
 a_actualiser='2027-04-30', raison="Législation et données d'exécution en évolution.",
))

# ═════════════ J. « Il faut renvoyer tous les étrangers qui ont déjà été condamnés. » ═════════════
FICHES.append(fiche(
 id='renvoyer-tous-deja-condamnes', type='reponse_critique', affirmation="Il faut renvoyer tous les étrangers qui ont déjà été condamnés.", sous_theme=ST_EXPUL,
 mots_cles=['déjà été condamnés', 'déjà condamnés', 'renvoyer tous', 'casier judiciaire', 'anciennes condamnations', 'peine purgée', 'rétroactif', 'menace actuelle', 'renvoyer chez eux'],
 verdict='opinion', fiabilite='etabli',
 resume="La proposition vise aussi des personnes ayant déjà purgé leur peine, parfois pour des faits mineurs ou anciens. Le droit actuel exige, pour une expulsion administrative, une menace grave pour l'ordre public : une condamnation passée ne suffit pas à elle seule. Le renvoi systématique se heurterait au contrôle de proportionnalité et, surtout, aux difficultés d'exécution.",
 contexte="« Déjà condamné » peut désigner une amende d'il y a vingt ans comme un crime récent. Le droit distingue la peine (prononcée au moment du jugement) et l'éloignement administratif décidé ensuite, qui doit tenir compte de la situation présente.",
 explication="Une interdiction du territoire est décidée par le juge lors du procès. Après la peine, l'administration peut expulser si la personne représente une menace grave et actuelle. Revenir sur toutes les condamnations passées supposerait d'éloigner des personnes qui ont purgé leur peine et dont la situation a pu changer, ce que la jurisprudence européenne demande d'examiner au cas par cas.",
 sources=[AN_EXPUL, CP_ITF, CEDH, CDC],
 faits=[
  fait("L'expulsion administrative suppose que la présence de la personne constitue une menace grave pour l'ordre public ; une condamnation ne suffit pas à elle seule.", 'an_expul', 'Droit en vigueur', 'CESEDA, article L. 631-1', "C'est le comportement présent qui est apprécié, pas seulement le casier.", 'etabli'),
  fait("L'interdiction du territoire est prononcée par le juge au moment de la condamnation, à titre définitif ou pour dix ans au plus.", 'cp_itf', 'Droit en vigueur', 'Code pénal, article 131-30', "C'est au procès que l'éloignement peut être décidé comme peine.", 'etabli'),
  fait("La CEDH examine la gravité de l'infraction, la durée du séjour, la vie familiale, l'intérêt des enfants et les liens avec le pays d'origine.", 'cedh', '18 octobre 2006', 'CEDH, Üner c. Pays-Bas', "Le temps écoulé et la situation actuelle comptent.", 'etabli'),
  fait("Autour de 10 % des OQTF sont exécutées.", 'cdc', '2019-2022', 'France', "Élargir le nombre de personnes visées sans moyens d'exécution aggraverait l'écart entre décisions et renvois.", 'etabli', '≈ 10 %'),
 ],
 court="Une condamnation passée ne suffit pas, à elle seule, à expulser : il faut une menace grave et actuelle. Et avec environ 10 % des OQTF exécutées, viser plus de monde sans pouvoir renvoyer ne changerait rien.",
 moyen="Il faut distinguer. Au moment du procès, le juge peut déjà interdire le territoire. Après la peine, l'administration peut expulser quelqu'un qui reste dangereux. Mais « tous ceux qui ont déjà été condamnés », ça vise aussi quelqu'un condamné pour un petit délit il y a quinze ans, qui a purgé sa peine et a une famille ici. La loi demande qu'on regarde la menace actuelle, et la Cour européenne des droits de l'homme exige un examen au cas par cas. Et en pratique, avec environ 10 % des OQTF exécutées, multiplier les décisions sans pouvoir les appliquer ne protège personne.",
 detaille="La proposition soulève quatre questions.\n\nQuelles condamnations ? Une contravention, un délit mineur ou un crime n'appellent pas la même réponse. Le mot « tous » efface ces différences.\n\nQuand ? Le droit prévoit que le juge peut prononcer une interdiction du territoire au moment du jugement. Après la peine, l'expulsion administrative suppose une menace grave pour l'ordre public : une condamnation passée ne suffit pas à elle seule. Revenir sur des peines purgées, parfois anciennes, reviendrait à ajouter une conséquence nouvelle à des faits déjà jugés.\n\nAvec quel examen ? La Cour européenne des droits de l'homme admet l'expulsion d'étrangers condamnés, mais selon des critères : gravité des faits, durée du séjour, famille, enfants, liens avec le pays d'origine. Un renvoi systématique, sans examen, serait très probablement contraire à ces exigences.\n\nAvec quels moyens ? Selon la Cour des comptes, environ 10 % des OQTF sont exécutées. Élargir massivement le nombre de personnes visées sans résoudre les obstacles (laissez-passer consulaires, identification, places de rétention) creuserait l'écart entre les décisions et les renvois.\n\nUne position défendable consiste à cibler les personnes dangereuses et à rendre les décisions exécutables ; le renvoi de toutes les personnes déjà condamnées pose des problèmes juridiques et pratiques majeurs.",
 empathie="Je comprends l'envie de fermeté : on se dit que quelqu'un qui a déjà fauté a perdu sa chance. Pour les personnes dangereuses, la loi le permet. Mais quelqu'un qui a payé une amende il y a quinze ans et élève ses enfants ici, ce n'est pas la même chose. On peut être ferme et juste à la fois.",
 legitimes=["Les personnes condamnées qui restent dangereuses doivent pouvoir être éloignées effectivement."],
 contre=[
  ("Il a été condamné, il a perdu ses droits.", "Il a perdu sa liberté le temps de sa peine. L'éloignement est une décision supplémentaire, qui doit tenir compte de sa dangerosité actuelle et de ses attaches, selon la loi et la jurisprudence européenne."),
  ("Peu importe les statistiques, il faut tous les renvoyer chez eux.", "On peut défendre plus de fermeté ; mais même avec une volonté totale, environ 10 % des OQTF sont exécutées aujourd'hui. Le débat utile porte sur qui renvoyer en priorité et comment rendre les renvois possibles."),
 ],
 questions=["Une amende ancienne et un crime récent doivent-ils avoir la même conséquence ?", "Que proposes-tu pour que les renvois décidés soient vraiment exécutés ?"],
 limites=["Les textes évoluent : vérifier la version en vigueur sur Légifrance.", "Pas de données publiques sur le nombre d'étrangers ayant une condamnation ancienne."],
 a_actualiser='2027-04-30', raison="Législation en évolution.",
))

# ═════════════ K. « Une personne étrangère condamnée devrait automatiquement perdre son droit de séjour. » ═════════════
FICHES.append(fiche(
 id='perte-automatique-droit-sejour', type='reponse_critique', affirmation="Une personne étrangère condamnée devrait automatiquement perdre son droit de séjour.", sous_theme=ST_EXPUL,
 mots_cles=['automatiquement', 'automatique', 'perdre son droit de séjour', 'titre de séjour', 'retrait', 'condamnée', 'proportionnalité', 'examen individuel', 'carte de séjour'],
 verdict='opinion', fiabilite='etabli',
 resume="Le droit français et européen exige un examen individuel avant d'éloigner un étranger installé : gravité des faits, durée du séjour, famille, enfants. Un retrait automatique, sans cet examen, se heurterait à la jurisprudence de la CEDH et au contrôle du Conseil d'État. Depuis 2024, les protections sont toutefois levées pour les condamnations graves.",
 contexte="L'automatisme est séduisant parce qu'il paraît simple et ferme. Le droit privilégie l'examen au cas par cas, pour éviter de traiter de la même manière des situations très différentes.",
 explication="Le contrôle de proportionnalité consiste à vérifier qu'une mesure n'est pas excessive au regard de son objectif. Il ne garantit pas que l'étranger reste : il oblige l'administration à justifier sa décision et permet au juge de vérifier l'équilibre entre ordre public et vie familiale.",
 sources=[CEDH, CE2026, AN_EXPUL, CP_ITF],
 faits=[
  fait("La CEDH impose de mettre en balance la gravité de l'infraction, la durée du séjour, la vie familiale, l'intérêt des enfants et les liens avec le pays d'origine ; elle a jugé proportionnée l'expulsion d'un étranger condamné pour homicide.", 'cedh', '18 octobre 2006', 'CEDH, Üner c. Pays-Bas', "Un examen individuel est exigé ; il peut aboutir à l'éloignement.", 'etabli'),
  fait("Le Conseil d'État a rendu le 9 juin 2026 trois décisions illustrant ce contrôle de proportionnalité dans l'expulsion d'étrangers protégés.", 'ce2026', '9 juin 2026', "Conseil d'État", "Le juge français applique ce contrôle au cas par cas.", 'etabli'),
  fait("Depuis la loi du 26 janvier 2024, les protections contre l'expulsion sont levées en cas de condamnation définitive pour des faits punis d'au moins trois ans (protection relative) ou cinq ans (protection renforcée, trois en récidive).", 'an_expul', 'Depuis 2024', 'CESEDA, articles L. 631-2 et L. 631-3', "La loi a déjà rapproché condamnation grave et perte de protection, sans automatisme.", 'etabli'),
  fait("L'interdiction du territoire, peine prononcée par le juge, peut être définitive ou durer dix ans au plus.", 'cp_itf', 'Droit en vigueur', 'Code pénal, article 131-30', "Le juge peut déjà retirer le droit de rester, après examen.", 'etabli'),
 ],
 court="Le droit exige d'examiner chaque situation avant d'éloigner quelqu'un d'installé ; un retrait automatique serait contraire à la jurisprudence européenne. Mais depuis 2024, une condamnation grave fait déjà tomber les protections.",
 moyen="L'idée paraît simple, mais « automatiquement » pose problème. Une amende et un viol ne peuvent pas avoir la même conséquence. Le droit européen demande qu'on regarde chaque cas : gravité des faits, durée du séjour, enfants. Ça ne protège pas les criminels : la Cour européenne a validé l'expulsion d'un homme condamné pour homicide. Et depuis 2024, en France, une condamnation grave fait tomber les protections, même pour ceux qui sont là depuis longtemps. Le juge peut aussi prononcer une interdiction du territoire. Ce qu'on refuse, c'est l'automatisme, pas la fermeté.",
 detaille="La différence entre ce qui existe et ce qui est proposé tient en un mot : automatiquement.\n\nCe qui existe. Le juge pénal peut prononcer une interdiction du territoire, définitive ou de dix ans au plus. L'administration peut expulser une personne qui représente une menace grave. Depuis la loi du 26 janvier 2024, les protections liées aux attaches familiales ou à la durée du séjour sont levées pour les condamnations à des faits punis d'au moins trois ou cinq ans.\n\nCe que l'automatisme changerait. Toute condamnation, même mineure, entraînerait la perte du droit de séjour, sans examen. Or la Cour européenne des droits de l'homme exige une mise en balance de la gravité des faits, de la durée du séjour, de la vie familiale, de l'intérêt des enfants et des liens avec le pays d'origine. Elle n'interdit pas l'expulsion : elle a jugé proportionnée celle d'un étranger condamné pour homicide. Le Conseil d'État applique ce contrôle, comme l'illustrent trois décisions du 9 juin 2026.\n\nPourquoi ce contrôle ? Pour éviter d'éloigner, pour une faute mineure, une personne arrivée enfant, sans lien avec le pays de sa nationalité, ou de séparer des enfants de leur parent sans examen. Ce contrôle a un coût (des procédures plus longues) et peut être débattu ; il n'est pas une impunité.\n\nUne voie intermédiaire existe déjà : fermeté pour les condamnations graves, examen individuel pour le reste.",
 empathie="Je comprends le besoin de règles claires : on a l'impression que tout se discute sans fin. Pour les faits graves, la loi est déjà devenue plus ferme. Mais traiter une petite infraction comme un crime grave, sans regarder la situation, ce serait injuste, y compris pour des enfants français.",
 legitimes=["Les procédures d'examen individuel allongent les délais et peuvent sembler opaques.", "Pour les condamnations graves, la perte du droit au séjour est une demande légitime, déjà largement prise en compte par la loi de 2024."],
 contre=[
  ("D'autres pays le font.", "Les pays membres du Conseil de l'Europe sont soumis aux mêmes exigences de la Convention européenne des droits de l'homme. Les règles précises varient, mais l'examen individuel est la norme imposée par la jurisprudence."),
  ("L'examen au cas par cas, c'est une usine à recours.", "Les recours allongent les délais, c'est vrai. Mais l'obstacle principal à l'exécution, selon la Cour des comptes, reste pratique : identification et laissez-passer consulaires."),
 ],
 questions=["Une personne arrivée en France à deux ans, sans lien avec son pays de nationalité, doit-elle être traitée comme un délinquant de passage ?", "Pour toi, où passe la limite entre une infraction qui justifie le retrait et une qui ne le justifie pas ?"],
 limites=["Le commentaire des décisions du Conseil d'État est une source secondaire.", "Vérifier la version en vigueur du CESEDA sur Légifrance."],
 a_actualiser='2027-04-30', raison="Législation et jurisprudence en évolution.",
))

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    for f in FICHES:
        with open(os.path.join(OUT, f"{f['id']}.json"), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2)
            fh.write('\n')
    print(f"{len(FICHES)} fiches écrites dans {os.path.normpath(OUT)}")
