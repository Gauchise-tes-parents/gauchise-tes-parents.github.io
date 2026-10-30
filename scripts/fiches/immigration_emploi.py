"""Fiches « immigration et emploi » : concurrence sur le marché du travail, salaires, chômage et pénurie.

Toutes les sources ont été ouvertes et lues le 30 octobre 2026 (consultee=True).
Règle : ne pas répondre à une question d'emploi avec des données sur le RSA ; présenter honnêtement
les résultats contrastés des études (effets moyens nuls ou positifs, effets possibles sur certains groupes).
Usage : python3 scripts/fiches/immigration_emploi.py
"""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'library')
TODAY = '2026-10-30'

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
    return d

INSEE_EMPLOI = ('insee_emploi', src("Emploi (France, portrait social, édition 2025)", "Insee (Insee Références)", "18 novembre 2025",
  "https://www.insee.fr/fr/statistiques/8612530",
  "Taux d'emploi des 15-64 ans en 2024 : immigrés 62,4 % ; descendants d'immigrés 58,1 % ; personnes sans ascendance migratoire directe 71,4 %. En 2015 : 55,8 %, 59,2 % et 66,5 %. Une partie de l'écart des descendants s'explique par leur âge plus jeune.",
  "Statistique publique de référence."))
CEPII = ('cepii', src("Métiers essentiels : quelle contribution des travailleurs immigrés ? (La Lettre du CEPII n° 424)", "CEPII (Anthony Edo, Sonia Louhab, Lionel Ragot)", "Février 2022",
  "https://imap.cepii.fr/PDF_PUB/lettre/2022/let424.pdf",
  "Les immigrés représentent 10,5 % des travailleurs des métiers essentiels, pour 10,3 % de l'emploi total. Ils sont surreprésentés dans les métiers essentiels peu qualifiés : 23 % des agents d'entretien et des aides à domicile, souvent avec des conditions de travail difficiles (horaires atypiques, pénibilité). Environ 17 % des médecins hospitaliers sont immigrés. En Île-de-France, ils occupent près de 30 % des emplois essentiels et plus de 60 % des emplois d'agents d'entretien et d'aides à domicile.",
  "Centre de recherche public en économie internationale."))
BDF = ('bdf', src("Immigration and the Occupational Choice of Natives: A Factor Proportions Approach (Document de travail n° 335)", "Banque de France (Javier Ortega, Gregory Verdugo)", "Juillet 2011",
  "https://publications.banque-france.fr/sites/default/files/medias/documents/working-paper_335_2011.pdf",
  "France, 1962-1999 : une hausse de 10 % de la part des immigrés est associée à des salaires des natifs plus élevés d'environ 3 % et à un taux d'emploi plus élevé d'environ 3 %. Mécanisme principal : les natifs se réorientent vers des professions mieux payées ; immigrés et natifs sont des substituts imparfaits, les immigrés étant surtout en concurrence entre eux. Les effets diminuent ou deviennent non significatifs dans certaines spécifications.",
  "Étude économétrique publiée par la Banque de France.", 'etude'))
EDO = ('edo', src("Immigration, wages and employment: Evidence from France (thèse de doctorat)", "Anthony Edo, université Paris 1 Panthéon-Sorbonne (Paris School of Economics)", "2014",
  "https://www.parisschoolofeconomics.eu/en/publications-hal/immigration-salaires-et-emplois-quels-effets-en-france",
  "France, 1990-2010 : à court terme, effet très faible sur les salaires des natifs de qualification proche, mais une hausse de 10 % de la part des immigrés est associée à une baisse d'environ 3 % du taux d'emploi de ces natifs « en concurrence » ; à long terme, pas d'effet défavorable sur le salaire moyen des natifs ; les natifs peu diplômés ont vu leurs salaires relatifs progresser.",
  "Travail universitaire montrant des effets différenciés selon l'horizon et les groupes.", 'etude'))
BMO = ('bmo', src("Besoins en main-d'œuvre 2025 : résultats de l'enquête (communiqué)", "France Travail", "11 avril 2025",
  "https://www.francetravail.org/accueil/communiques/2025/besoins-en-main-d-oeuvre-bmo-2025.html?type=article",
  "Environ 2,43 millions de projets de recrutement en 2025 (en baisse de 12,5 %) ; 50,1 % jugés difficiles par les employeurs ; difficultés les plus fortes dans le commerce et la réparation automobile (69,7 %), la construction (66,1 %) et la santé et l'action sociale (63 %) ; principale cause : manque de candidats ou candidats inadaptés ; 27 % des employeurs anticipant des difficultés citent aussi un manque de moyens financiers.",
  "Enquête annuelle de référence auprès des employeurs."))

FICHES = []

FICHES.append(fiche(
 id='immigration-emploi', affirmation="Les immigrés prennent le travail des Français.", volet='immigration', sous_theme='Immigration et travail',
 mots_cles=['prennent le travail', 'travail des français', 'emplois', 'emploi', 'chômage', 'immigration crée du chômage', 'plus d immigrés moins de travail', 'concurrence', 'marché du travail', 'boulot', 'embauche', 'faire venir des étrangers'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Le nombre d'emplois n'est pas un gâteau fixe : les immigrés occupent des emplois, mais ils consomment, créent de l'activité et occupent souvent des métiers peu attractifs. Les études sur la France trouvent un effet moyen nul ou positif sur l'emploi des natifs à long terme, avec des effets négatifs possibles à court terme pour les travailleurs directement en concurrence. Et le taux d'emploi des immigrés (62,4 %) est inférieur à celui des personnes sans ascendance migratoire (71,4 %).",
 contexte="L'idée repose sur une image intuitive : s'il y a un nombre fixe d'emplois, chaque emploi occupé par un immigré serait retiré à un Français. Les économistes appellent cela l'erreur de la « masse fixe de travail ».",
 explication="Les immigrés ne font pas qu'occuper des postes : ils consomment, paient des cotisations, créent parfois des entreprises et occupent des métiers où les employeurs peinent à recruter. Leur effet dépend du degré de concurrence avec les natifs : quand ils exercent des métiers différents, ils peuvent être complémentaires. Quand ils sont en concurrence directe, des effets négatifs locaux et temporaires sont possibles.",
 sources=[INSEE_EMPLOI, CEPII, BDF, EDO],
 faits=[
  fait("En 2024, le taux d'emploi des immigrés de 15 à 64 ans est de 62,4 %, contre 71,4 % pour les personnes sans ascendance migratoire directe.", 'insee_emploi', '2024', 'France, 15-64 ans', "Les immigrés sont moins souvent en emploi que les autres : ils ne « raflent » pas les emplois.", 'etabli', '62,4 % / 71,4 %'),
  fait("Les immigrés représentent 10,3 % de l'emploi total, mais 23 % des agents d'entretien et des aides à domicile, des métiers souvent pénibles et à horaires atypiques.", 'cepii', '2022 (données récentes)', 'France', "Ils sont concentrés dans des métiers peu recherchés par les autres travailleurs.", 'etabli', '10,3 % / 23 %'),
  fait("Sur la période 1962-1999, une hausse de 10 % de la part des immigrés est associée à un taux d'emploi des natifs plus élevé d'environ 3 %, les natifs se réorientant vers des métiers mieux payés.", 'bdf', '1962-1999', 'France', "Une étude de long terme trouve un effet favorable en moyenne.", 'estimation'),
  fait("Sur 1990-2010, une hausse de 10 % de la part des immigrés est associée à une baisse d'environ 3 % du taux d'emploi des natifs directement en concurrence, à court terme ; à long terme, pas d'effet défavorable sur le salaire moyen des natifs.", 'edo', '1990-2010', 'France', "Des effets négatifs existent pour certains groupes à court terme : il faut le reconnaître.", 'estimation'),
 ],
 court="Le travail n'est pas un gâteau fixe. Les immigrés sont moins souvent en emploi que les autres (62,4 % contre 71,4 %), et les études trouvent un effet moyen nul ou positif sur l'emploi des Français à long terme.",
 moyen="Cette idée suppose qu'il y a un nombre fixe d'emplois. Ce n'est pas comme ça que marche l'économie : les immigrés consomment, cotisent, et occupent souvent des métiers où l'on manque de bras, comme l'entretien ou l'aide à domicile (23 % d'immigrés). D'ailleurs, ils sont moins souvent en emploi que les autres : 62,4 % contre 71,4 % selon l'Insee. Les études sérieuses ne trouvent pas d'effet négatif moyen à long terme ; certaines trouvent un effet négatif à court terme pour les travailleurs directement en concurrence. C'est là qu'il faut agir : formation, salaires, conditions de travail.",
 detaille="L'affirmation repose sur l'idée d'une « masse fixe de travail » : si un immigré a un emploi, un Français en aurait un de moins. Or l'emploi n'est pas une quantité fixe. Les immigrés consomment, paient des cotisations, créent des entreprises et occupent des postes qui permettent à d'autres activités de fonctionner.\n\nLes chiffres de l'Insee montrent d'abord que les immigrés sont moins souvent en emploi que les autres : 62,4 % des 15-64 ans en 2024, contre 71,4 % pour les personnes sans ascendance migratoire directe. Le CEPII montre aussi qu'ils sont surreprésentés dans des métiers essentiels peu qualifiés et souvent pénibles : 23 % des agents d'entretien et des aides à domicile.\n\nQue disent les études sur l'effet de l'immigration sur l'emploi des natifs ? Sur une longue période (1962-1999), une étude de la Banque de France trouve un effet favorable : les natifs se sont orientés vers des métiers mieux payés. Une thèse portant sur 1990-2010 trouve, à court terme, une baisse du taux d'emploi des natifs directement en concurrence, et pas d'effet défavorable à long terme sur le salaire moyen.\n\nConclusion honnête : l'immigration ne « prend » pas le travail des Français en général. Mais des tensions locales et temporaires peuvent exister pour certains travailleurs. La réponse utile passe par la formation, les salaires, la lutte contre le travail illégal et les conditions de travail, pas par la désignation d'un groupe.",
 empathie="Je comprends l'inquiétude : quand on cherche du travail et qu'on n'en trouve pas, on cherche une explication. Mais les chiffres montrent que les immigrés sont plutôt moins souvent en emploi que les autres, et qu'ils occupent souvent des métiers que peu de gens veulent faire. Le problème de l'emploi est réel ; je ne crois pas que ce soit la bonne cause.",
 legitimes=["Des effets négatifs à court terme sur l'emploi de certains travailleurs directement en concurrence sont mis en évidence par certaines études.", "Le travail illégal peut tirer les conditions de travail vers le bas dans certains secteurs."],
 contre=[
  ("Il n'y a déjà pas assez de travail pour tout le monde.", "Le nombre d'emplois n'est pas fixe : en 2025, les employeurs prévoyaient encore environ 2,4 millions de projets de recrutement, dont la moitié jugés difficiles. Le chômage vient surtout de l'inadéquation entre postes, qualifications, lieux et conditions de travail."),
  ("Les entreprises préfèrent embaucher des étrangers.", "Certaines études observent qu'à court terme des employeurs substituent des immigrés à des natifs de qualification proche, souvent parce qu'ils acceptent des conditions plus dures. Le problème est alors l'exploitation et les conditions de travail, qui pèsent sur tous les salariés."),
  ("Pourquoi faire venir des étrangers alors qu'il y a du chômage ?", "Parce que les chômeurs et les postes vacants ne se trouvent pas toujours au même endroit, dans les mêmes métiers, avec les mêmes qualifications. La question utile est : pourquoi ces postes ne trouvent-ils pas preneur ?"),
 ],
 questions=["Si les immigrés prenaient le travail des Français, pourquoi sont-ils eux-mêmes moins souvent en emploi ?", "Dans les métiers où l'on manque de bras, qu'est-ce qui ferait venir plus de candidats : des salaires plus hauts, de meilleures conditions ?"],
 limites=["Les études économétriques citées portent sur des périodes anciennes (1962-1999, 1990-2010).", "Les effets dépendent des métiers, des régions et de la conjoncture : il n'existe pas de chiffre unique valable partout."],
 a_actualiser='2027-01-31', raison="Nouvelles données Insee (novembre) et nouvelles études.",
))

FICHES.append(fiche(
 id='immigration-salaires', affirmation="Les immigrés font baisser les salaires des Français.", volet='immigration', sous_theme='Immigration et travail',
 mots_cles=['salaires', 'font baisser les salaires', 'paient moins', 'payés moins', 'dumping', 'patrons préfèrent', 'main d oeuvre bon marché', 'moins cher', 'exploitation', 'tirer les salaires vers le bas'],
 verdict='trompeur', fiabilite='interpretation',
 resume="Les études sur la France ne trouvent pas de baisse du salaire moyen des natifs liée à l'immigration : une étude trouve même un effet positif sur 1962-1999, une autre un effet très faible à court terme pour les natifs directement en concurrence, et aucun effet défavorable à long terme. Le vrai sujet est l'exploitation et le travail non déclaré, qui pèsent sur tous les salariés.",
 contexte="L'argument s'appuie sur la loi de l'offre et de la demande : plus de travailleurs, des salaires plus bas. En pratique, l'effet dépend de la concurrence réelle entre travailleurs, du salaire minimum, des conventions collectives et de la demande supplémentaire créée.",
 explication="Les salaires en France sont encadrés par le SMIC et les conventions collectives, ce qui limite les baisses directes. Quand immigrés et natifs n'occupent pas les mêmes métiers, ils peuvent être complémentaires. Les employeurs qui exploitent des travailleurs vulnérables, notamment non déclarés, créent une concurrence déloyale : c'est un problème de droit du travail.",
 sources=[BDF, EDO, CEPII],
 faits=[
  fait("Sur 1962-1999, une hausse de 10 % de la part des immigrés est associée à des salaires des natifs plus élevés d'environ 3 %.", 'bdf', '1962-1999', 'France', "L'effet moyen estimé est favorable, grâce à la réorientation des natifs vers des métiers mieux payés.", 'estimation', '+3 %'),
  fait("Sur 1990-2010, l'immigration a un effet très faible sur les salaires des natifs de qualification proche à court terme, et pas d'effet défavorable sur le salaire moyen des natifs à long terme ; les natifs peu diplômés ont vu leurs salaires relatifs progresser.", 'edo', '1990-2010', 'France', "Les rigidités salariales (SMIC, conventions) limitent les baisses de salaire.", 'estimation'),
  fait("Les immigrés sont surreprésentés dans des métiers essentiels peu qualifiés aux conditions difficiles : 23 % des agents d'entretien et des aides à domicile ; des travaux cités indiquent qu'ils acceptent plus souvent des horaires atypiques.", 'cepii', '2022', 'France', "La pression porte d'abord sur les conditions de travail dans ces métiers.", 'etabli', '23 %'),
 ],
 court="Les études sur la France ne trouvent pas de baisse du salaire moyen des Français due à l'immigration ; l'une trouve même +3 % sur 1962-1999. Le vrai problème, c'est l'exploitation, qui tire tout le monde vers le bas.",
 moyen="Intuitivement, plus de travailleurs devrait faire baisser les salaires. Mais en France, le SMIC et les conventions collectives encadrent les salaires, et immigrés et natifs n'exercent souvent pas les mêmes métiers. Résultat : une étude de la Banque de France trouve des salaires des natifs plus élevés de 3 % pour une hausse de 10 % de la part des immigrés, sur 1962-1999 ; une thèse trouve un effet très faible à court terme et aucun effet défavorable à long terme. Si des patrons paient moins certains immigrés, c'est souvent par l'exploitation et le travail non déclaré : la solution, c'est de faire respecter le droit du travail.",
 detaille="L'argument a une logique apparente : davantage de travailleurs, donc des salaires plus bas. Mais l'effet réel dépend de trois choses : la concurrence effective entre travailleurs, les règles salariales et la demande supplémentaire créée par l'immigration.\n\nEn France, les salaires sont encadrés par le SMIC et les conventions collectives. Les études disponibles trouvent donc peu d'effets négatifs sur les salaires. Sur 1962-1999, une étude de la Banque de France estime qu'une hausse de 10 % de la part des immigrés est associée à des salaires des natifs supérieurs d'environ 3 % : les natifs se sont orientés vers des métiers mieux rémunérés. Sur 1990-2010, une thèse trouve un effet très faible à court terme pour les natifs de qualification proche, et aucun effet défavorable à long terme sur le salaire moyen ; les moins diplômés ont même vu leurs salaires relatifs progresser.\n\nCe qui existe réellement, c'est la pression sur les conditions de travail dans certains métiers pénibles, où les immigrés sont nombreux, et l'exploitation de travailleurs vulnérables, notamment sans titre de séjour. Ce sont des problèmes de droit du travail et de contrôle des employeurs.\n\nSi l'on veut défendre les salaires, les leviers sont connus : SMIC, négociations collectives, contrôles, lutte contre le travail non déclaré.",
 empathie="Je comprends : quand ton salaire ne suit pas les prix, c'est rageant, et on cherche un responsable. Mais les études ne montrent pas que l'immigration fasse baisser les salaires en moyenne. Ceux qui paient mal, ce sont des employeurs ; c'est eux qu'il faut regarder.",
 legitimes=["L'exploitation de travailleurs sans papiers ou non déclarés exerce une pression déloyale sur certains secteurs.", "Des effets faibles à court terme existent pour des travailleurs directement en concurrence."],
 contre=[
  ("Les patrons préfèrent les immigrés parce qu'ils les paient moins.", "Payer moins que le minimum légal ou les conventions, c'est illégal. Quand ça arrive, c'est l'employeur qui fraude, souvent avec des travailleurs vulnérables. Défendre les salaires, c'est contrôler et sanctionner ces employeurs, et régulariser pour que tous aient les mêmes droits."),
  ("Les études datent, aujourd'hui c'est différent.", "C'est juste : les études citées portent sur 1962-2010. Aucune ne permet d'affirmer l'inverse pour aujourd'hui sans nouvelles données ; c'est un point à surveiller honnêtement."),
 ],
 questions=["Qui décide des salaires dans une entreprise : les immigrés ou les employeurs ?", "Qu'est-ce qui protège le mieux ton salaire : moins d'immigrés ou des règles mieux appliquées ?"],
 limites=["Les études portent sur 1962-2010.", "L'effet du travail non déclaré n'est pas mesuré par ces études."],
 a_actualiser='2027-06-30', raison="Nouvelles études économiques.",
))

FICHES.append(fiche(
 id='chomage-penurie-recrutement', type='reference', affirmation="Il y a du chômage, mais les entreprises disent qu'elles ne trouvent personne.", volet='social', sous_theme='Chômage',
 mots_cles=['ne trouvent personne', 'pénurie', 'métiers en tension', 'difficultés de recrutement', 'emplois vacants', 'chômage et pénurie', 'offres non pourvues', 'recrutement', 'manque de main d oeuvre'],
 verdict=None, fiabilite='etabli',
 resume="Les deux sont vrais en même temps : en 2025, la moitié des 2,43 millions de projets de recrutement sont jugés difficiles par les employeurs (France Travail), alors que le chômage persiste. Ce n'est pas une contradiction : les postes, les chômeurs, les qualifications, les lieux et les conditions de travail ne coïncident pas toujours.",
 contexte="Cette phrase sert souvent à dire que « les chômeurs ne veulent pas travailler », ou au contraire que « les entreprises mentent ». Les données montrent une réalité plus simple : un décalage entre offres et demandes d'emploi.",
 explication="Les difficultés de recrutement portent sur des secteurs précis (commerce et réparation automobile, construction, santé et action sociale) et ont plusieurs causes : manque de candidats formés, éloignement géographique, horaires et pénibilité, salaires peu attractifs, moyens financiers limités des employeurs.",
 sources=[BMO, CEPII],
 faits=[
  fait("En 2025, les employeurs prévoient environ 2,43 millions de projets de recrutement, dont 50,1 % jugés difficiles.", 'bmo', '2025', 'France, établissements employeurs', "La moitié des embauches prévues sont jugées difficiles, un niveau revenu à celui de 2019.", 'etabli', '2,43 millions ; 50,1 %'),
  fait("Les difficultés sont les plus fortes dans le commerce et la réparation automobile (69,7 %), la construction (66,1 %) et la santé et l'action sociale (63 %).", 'bmo', '2025', 'France', "Les tensions sont concentrées dans certains secteurs.", 'etabli'),
  fait("La première cause de difficulté citée est le manque de candidats ou de candidats adaptés ; 27 % des employeurs anticipant des difficultés citent aussi un manque de moyens financiers.", 'bmo', '2025', 'France', "Les difficultés tiennent aussi aux moyens et aux conditions proposées.", 'etabli', '27 %'),
  fait("Les métiers essentiels peu qualifiés, comme l'entretien et l'aide à domicile, cumulent souvent pénibilité et horaires atypiques.", 'cepii', '2022', 'France', "Les conditions de travail pèsent sur l'attractivité de certains métiers.", 'etabli'),
 ],
 court="Les deux sont vrais : la moitié des recrutements prévus en 2025 sont jugés difficiles (France Travail), et le chômage persiste. C'est un décalage entre postes, compétences, lieux et conditions de travail, pas une preuve que les chômeurs ne veulent pas travailler.",
 moyen="Ce n'est pas une contradiction. Selon France Travail, 50,1 % des 2,43 millions de projets de recrutement de 2025 sont jugés difficiles, surtout dans le commerce et l'automobile, le bâtiment et la santé. Pendant ce temps, des chômeurs ne trouvent pas d'emploi. Pourquoi ? Les postes ne sont pas forcément là où vivent les chômeurs, ne demandent pas les mêmes qualifications, et certains offrent des horaires et des salaires peu attractifs. Les employeurs eux-mêmes citent aussi le manque de moyens.",
 detaille="La phrase pointe un vrai paradoxe apparent. Les deux constats sont exacts.\n\nD'un côté, l'enquête Besoins en main-d'œuvre de France Travail recense environ 2,43 millions de projets de recrutement pour 2025, dont 50,1 % jugés difficiles. Les difficultés sont fortes dans le commerce et la réparation automobile (69,7 %), la construction (66,1 %) et la santé et l'action sociale (63 %). De l'autre, le chômage persiste.\n\nL'explication tient au décalage entre offres et demandes : qualifications différentes, éloignement géographique, contraintes de mobilité ou de garde d'enfants, horaires atypiques, pénibilité, salaires peu attractifs. Les employeurs citent d'abord le manque de candidats adaptés, mais 27 % évoquent aussi leurs propres moyens financiers limités.\n\nCe constat ne prouve ni que les chômeurs « ne veulent pas travailler », ni que les entreprises mentent. Il appelle des réponses concrètes : formation, mobilité, logement, salaires et conditions de travail dans les métiers concernés.",
 empathie="Tu as raison, c'est déroutant : des patrons qui cherchent, des gens qui cherchent aussi. En regardant de près, ils ne se cherchent pas au même endroit, ni pour les mêmes métiers, ni aux mêmes conditions. Ce n'est la faute ni des uns ni des autres en bloc.",
 contre=[
  ("C'est la preuve que les chômeurs ne veulent pas travailler.", "Non : les difficultés sont concentrées dans certains secteurs et tiennent aussi aux qualifications, à la distance, aux horaires et aux salaires. Et 27 % des employeurs évoquent leur propre manque de moyens."),
  ("Il suffit de faire venir des immigrés pour ces postes.", "C'est une réponse possible pour certains métiers, mais elle ne règle pas les causes : conditions de travail, salaires, formation. Ces leviers concernent aussi les travailleurs déjà présents."),
 ],
 questions=["Si un poste reste vacant, qu'est-ce qui le rendrait plus attractif selon toi ?", "Les chômeurs de ta région ont-ils les qualifications demandées par les entreprises qui recrutent ?"],
 limites=["Un projet jugé difficile n'est pas forcément un poste non pourvu.", "L'enquête porte sur des intentions d'embauche déclarées par les employeurs."],
 a_actualiser='2027-04-30', raison="Nouvelle enquête BMO chaque printemps.",
))

if __name__ == '__main__':
    for f in FICHES:
        with open(os.path.join(OUT, f"{f['id']}.json"), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2)
            fh.write('\n')
    print(f"{len(FICHES)} fiches écrites")
