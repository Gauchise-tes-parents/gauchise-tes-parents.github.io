"""Génère les fiches de la rubrique « Mélenchon crie, il est agressif, il est dangereux ».

Chaque fiche suit la structure en cinq parties demandée :
  1. ce qui est reproché et l'origine du reproche  -> champ `reproche` (+ `contexte`)
  2. les faits vérifiables                           -> `faits`
  3. la réponse argumentée                           -> `argumentaires.moyen` / `detaille`
  4. les objections légitimes                        -> `objections_legitimes` (+ `contre_arguments`)
  5. une formulation simple à table                  -> `argumentaires.court` (= `formulation_table`)

Toutes les sources ci-dessous ont été ouvertes et lues le 29 octobre 2026.
Usage : python3 scripts/fiches/melenchon_lfi.py  (écrit dans data/library/)
"""
import json, os

OUT = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'library')
TODAY = '2026-10-29'

def src(titre, organisme, date, url, passage, pertinence, type_='media', consultee=True):
    return dict(titre=titre, organisme=organisme, date_publication=date, url=url,
                passage=passage, pertinence=pertinence, type=type_, consultee=consultee)

S = {
 'perq': src("Perquisition à LFI : Jean-Luc Mélenchon condamné à trois mois de prison avec sursis", "Public Sénat", "Décembre 2019",
   "https://www.publicsenat.fr/actualites/politique/perquisition-a-lfi-jean-luc-melenchon-condamne-a-trois-mois-de-prison-avec-sursis",
   "Condamnation par le tribunal correctionnel de Bobigny à trois mois d'emprisonnement avec sursis et 8 000 € d'amende pour rébellion et provocation, après la perquisition du 16 octobre 2018 ; « La République, c'est moi » ; appel à « enfoncer la porte ».",
   "Décision de justice rapportée par un média parlementaire."),
 'colere': src("Mélenchon prend le risque politique d'assumer ses colères (Lucile Malandain)", "Public Sénat", "6 décembre 2017",
   "https://www.publicsenat.fr/actualites/politique/melenchon-prend-le-risque-politique-d-assumer-ses-coleres-80549",
   "Billet du 4 décembre 2017 contre l'équipe de France 2 (« glapit en pleine hystérie », « équipe d'arsouilles ») ; proposition d'un « tribunal » professionnel remplacée le lendemain par « conseil de déontologie » ; stratégie assumée du « coup pour coup » ; étude Fondation Jean-Jaurès / Ifop : courageux pour ses soutiens, agressif ou arrogant pour ses critiques.",
   "Article factuel avec citations et études d'opinion."),
 'cautres': src("[Paroles de candidats] Mélenchon, celui qui était révolutionnaire mais se voulait rassembleur (Bruno Cautrès)", "Institut Montaigne", "17 juin 2026",
   "https://institutmontaigne.org/expressions/paroles-de-candidats-melenchon-celui-qui-etait-revolutionnaire-mais-se-voulait-rassembleur",
   "Analyse logométrique du discours de Saint-Denis du 7 juin 2026 : texte préparé lu en 52 minutes, lexique dense, vocabulaire du conflit (« guerre », « crime », « menace », « rupture ») ; reprise du portrait de « tribun hors pair » (Cécile Alduy, 2017).",
   "Analyse d'un politiste (think tank d'orientation libérale)."),
 'braunpivet': src("Déplacement en Israël : Yaël Braun-Pivet accuse Jean-Luc Mélenchon de lui mettre « une cible dans le dos »", "LCP Assemblée nationale", "Octobre 2023",
   "https://lcp.fr/actualites/deplacement-en-israel-yael-braun-pivet-accuse-jean-luc-melenchon-de-lui-mettre-une",
   "Message de Jean-Luc Mélenchon : la présidente de l'Assemblée « campe à Tel Aviv pour encourager le massacre » ; réponse : « C'est une nouvelle cible qu'on me met dans le dos » ; Mélenchon dénonce une « absurde police des mots ».",
   "Média parlementaire, citations des deux protagonistes."),
 'invest': src("Législatives 2024 : Adrien Quatennens investi par LFI, Raquel Garrido, Alexis Corbière et Danielle Simonnet écartés", "Europe 1", "14 juin 2024",
   "https://www.europe1.fr/politique/legislatives-2024-adrien-quatennens-investi-par-lfi-rasuel-garrido-alexis-corbiere-et-danielle-simonnet-ecartes-4252853",
   "Quatennens, condamné en décembre 2022 pour violences conjugales, investi ; Corbière, Garrido, Simonnet, Davi et Frédéric Mathieu non réinvestis ; réactions « La honte », « purge » ; critiques de François Ruffin.",
   "Récit factuel des investitures et des réactions."),
 'aec': src("L'Avenir en commun — programme abrégé (2022)", "Union populaire / La France insoumise (source partisane)", "Avril 2022",
   "https://melenchon.fr/wp-content/uploads/2022/04/programme-avenir-en-commun-abrege.pdf",
   "Assemblée constituante convoquée par référendum (art. 11), membres élus ou tirés au sort ; RIC législatif, abrogatoire, constitutionnel et révocatoire (p. 5) ; combattre « les communautarismes et l'usage politique des religions », supprimer le financement public des cultes en Alsace-Moselle (p. 5) ; SMIC à 1 400 € net (p. 6) ; retraite à 60 ans avec 40 annuités (p. 10) ; police de proximité, démantèlement des BAC, remplacement de l'IGPN par une autorité indépendante (p. 18).",
   "Texte du programme lui-même : il dit ce que LFI propose, pas ce qui est réalisable.", 'partisane'),
 'conseil_etat': src("Municipales : le Conseil d'État confirme le nuançage « aux extrêmes » de LFI et de l'UDR", "Banque des Territoires (Caisse des dépôts)", "2 mars 2026",
   "https://www.banquedesterritoires.fr/municipales-le-conseil-detat-confirme-le-nuancage-aux-extremes-de-lfi-et-de-ludr",
   "Rejet des recours de LFI et de l'UDR contre la circulaire de nuançage des municipales 2026 : pas d'« erreur manifeste d'appréciation » ; motifs avancés par le ministre de l'Intérieur : « remise en cause très forte de l'autorité judiciaire » et accusations systématiques contre la police ; LFI classée à gauche jusque-là (décision de 2024) ; décisions n° 512694, 512695, 512981 et 512983.",
   "Presse spécialisée des collectivités, références des décisions."),
 'afp7oct': src("Nombreuses condamnations du Hamas en France, LFI crée la polémique : « une constante du discours antisémite » (AFP)", "L'Avenir (dépêche AFP)", "7 octobre 2023",
   "https://www.lavenir.net/actu/monde/2023/10/07/nombreuses-condamnations-du-hamas-en-france-lfi-cree-la-polemique-une-constante-du-discours-antisemite-HCDBHOWH4JFPNEAPTYHLTUC2QQ/",
   "Communiqué du groupe LFI replaçant l'attaque dans le contexte de « l'intensification de la politique d'occupation israélienne » ; Mélenchon : « la violence ne produit et ne reproduit qu'elle-même » ; Laurence Rossignol (PS) : « C'est une constante du discours antisémite » ; François Ruffin condamne sans réserve.",
   "Dépêche d'agence du jour même."),
 'residuel': src("Pour Jean-Luc Mélenchon, l'antisémitisme reste « résiduel » en France", "Europe 1", "Juin 2024",
   "https://www.europe1.fr/politique/pour-jean-luc-melenchon-lantisemitisme-reste-residuel-en-france-4250482",
   "Billet de blog du 2 juin 2024 ; chiffres cités : 366 actes antisémites au premier trimestre 2024 selon le gouvernement (+300 %) ; selon le Crif, 436 actes en 2022 et 1 676 en 2023.",
   "Média généraliste reprenant les chiffres officiels et associatifs."),
 'faure': src("Élections européennes : Olivier Faure s'indigne d'un « dérapage incompréhensible » de Mélenchon", "Europe 1", "4 juin 2024",
   "https://www.europe1.fr/politique/elections-europeennes-olivier-faure-sindigne-dun-derapage-incomprehensible-de-melenchon-4250838",
   "Le premier secrétaire du PS se dit « heurté » : « Tout montre qu'il y a au contraire une explosion de l'antisémitisme ».",
   "Réaction d'un allié de gauche."),
 'thelocal': src("Explained: Why France's far-left leader is battling accusations of anti-Semitism", "The Local France", "2 mars 2026",
   "https://www.thelocal.fr/20260302/explained-why-frances-far-left-leader-is-battling-accusations-of-anti-semitism",
   "Plaisanterie sur « Epsteen » à Lyon, présentée comme ironique ; déformation du nom de Raphaël Glucksmann à Perpignan ; Mélenchon rejette toute accusation d'antisémitisme ; le reproche porte souvent sur le fait de ne pas prendre au sérieux ce type de rhétorique ; aucune décision de justice citée.",
   "Article explicatif en anglais, factuel."),
 'police': src("Propos de Jean-Luc Mélenchon sur la police : « Un Premier ministre ne devrait pas dire ça » (chronique de Nicolas Beytout)", "Europe 1 (chronique d'opinion)", "7 juin 2022",
   "https://www.europe1.fr/politique/propos-de-jean-luc-melenchon-sur-la-police-un-premier-ministre-ne-devrait-pas-dire-ca-4116080",
   "« La police tue » après des tirs policiers sur une voiture à Paris ayant tué une passagère ; Gérald Darmanin dénonce des insultes ; Manuel Bompard affirme que LFI n'est pas opposée à la police.",
   "Chronique d'opinion : les faits rapportés sont utilisés, pas le jugement du chroniqueur."),
 'nfp': src("Le Nouveau Front populaire chiffre son programme à 150 milliards d'ici à 2027", "LCP Assemblée nationale", "21 juin 2024",
   "https://lcp.fr/actualites/le-nouveau-front-populaire-chiffre-son-programme-a-150-milliards-d-ici-a-2027-assurant",
   "Environ 150 Md€ de dépenses supplémentaires d'ici 2027 ; mesures d'urgence de 25 Md€ en 2024 (abrogation des réformes des retraites et de l'assurance chômage, SMIC à 1 600 € net, point d'indice +10 %) ; environ 100 Md€ de recettes (ISF climatique, taxe sur les superprofits…) ; Gabriel Attal dénonce un « matraquage fiscal ».",
   "Présentation du chiffrage par ses auteurs et réactions."),
 'montaigne': src("Législatives 2024 : chiffrage global des programmes", "Institut Montaigne", "5 juillet 2024",
   "https://institutmontaigne.org/communiques-de-presse/legislatives-2024-chiffrage-global-des-programmes",
   "Coût annuel estimé : Nouveau Front populaire 179 Md€, Rassemblement national 71 Md€, Ensemble environ 21 Md€.",
   "Chiffrage d'un think tank d'orientation libérale, hypothèses contestées par les partis.", 'secondaire'),
 'ina92': src("Jean-Luc Mélenchon on the Maastricht Treaty", "INA (mediaclip)", "4 septembre 1992",
   "https://mediaclip.ina.fr/en/moc9209050002-jean-luc-melenchon-on-the-maastricht-treaty.html",
   "Le sénateur socialiste Jean-Luc Mélenchon soutient le traité, « base solide » pour le début d'une constitution européenne.",
   "Archive audiovisuelle.", 'primaire'),
 'tce2005': src("20 ans après, la plaie encore vive du référendum sur la Constitution européenne", "Public Sénat", "Mai 2025",
   "https://www.publicsenat.fr/actualites/politique/20-ans-apres-la-plaie-encore-vive-du-referendum-sur-la-constitution-europeenne",
   "Non à 54,67 % le 29 mai 2005 ; Jean-Luc Mélenchon, alors sénateur PS de l'Essonne, parmi les responsables « résolument hostiles au traité » ; départ du PS en 2008 et fondation du Parti de gauche.",
   "Article rétrospectif d'un média parlementaire."),
 'marche': src("La marche controversée contre l'islamophobie s'élance à Paris", "Public Sénat", "10 novembre 2019",
   "https://www.publicsenat.fr/actualites/politique/la-marche-controversee-contre-l-islamophobie-s-elance-a-paris-146979",
   "Appel publié dans Libération le 1er novembre 2019, après l'attaque d'une mosquée à Bayonne, soutenu notamment par le NPA et le Collectif contre l'islamophobie en France ; contestation du terme et de certains signataires ; présence de Jean-Luc Mélenchon et d'élus LFI ; PS et PRG absents ; « quelques milliers » de participants.",
   "Récit factuel du jour même."),
 'slate': src("Laïcité : comment Jean-Luc Mélenchon a changé de position (republication de The Conversation)", "Slate.fr / The Conversation", "Non précisée (vers 2021)",
   "https://www.slate.fr/story/201594/jean-luc-melenchon-laicite-fracture-gauche-france-insoumise-musulmans-racisme-polemique-islamophobie",
   "2004 : soutien à l'interdiction du voile à l'école ; 2015 : rejet du terme « islamophobie » ; 2019 : participation à la marche ; 2021 : opposition au projet de loi « séparatisme » ; critiques de Jean-Michel Blanquer, Henri Peña-Ruiz, Anne Hidalgo.",
   "Analyse d'un doctorant en science politique (auteur non nommé dans la version consultée).", 'secondaire'),
 'ipsos22': src("Présidentielle : âge, profession, lieu de résidence… quel est le profil des électeurs ?", "Public Sénat (enquête Ipsos-Sopra Steria)", "Avril 2022",
   "https://www.publicsenat.fr/actualites/politique/presidentielle-age-profession-lieu-de-residence-quel-est-le-profil-des-electeurs",
   "Premier tour 2022 : ouvriers, Le Pen 36 %, Mélenchon 23 % ; revenus < 1 250 €/mois, Le Pen 31 %, Mélenchon 28 % ; 18-24 ans, Mélenchon 31 %.",
   "Sondage sortie des urnes, marge d'erreur non précisée."),
 'drees_ms': src("Minima sociaux et prestations de solidarité, édition 2025 — Fiche 07 : les dépenses d'allocations", "DREES", "Décembre 2025",
   "https://www.drees.solidarites-sante.gouv.fr/sites/default/files/2025-12/MS2025%20-%20Fiche%2007%20-%20Les%20d%C3%A9penses%20d%27allocations.pdf",
   "Minima sociaux : 31,6 Md€ en 2023, 2,0 % des dépenses publiques ; RSA : 12,2 Md€, 0,4 % du PIB.",
   "Statistique publique.", 'primaire'),
 'drees_nr': src("Le non-recours au RSA concerne plus d'un tiers des foyers éligibles, confirme la Drees", "Banque des Territoires (Localtis), d'après la DREES", "6 mai 2026",
   "https://www.banquedesterritoires.fr/le-non-recours-au-rsa-concerne-plus-dun-tiers-des-foyers-eligibles-confirme-la-drees",
   "Environ 561 000 foyers éligibles, soit 33 % à 37 %, ne percevaient pas le RSA fin 2021.",
   "Compte rendu détaillé de l'étude DREES (la publication originale n'a pas pu être ouverte).", 'secondaire'),
 'ft': src("Bilan du contrôle de la recherche d'emploi en 2023 (communiqué)", "France Travail", "19 avril 2024",
   "https://www.francetravail.org/files/live/sites/peorg/files/documents/Communiqu%c3%a9%20de%20presse/2024/20240419%20-%20FRANCE%20TRAVAIL%20-%20CP%20-%20Bilan%20Le%20contr%c3%83%c2%b4le%20de%20la%20recherche%20d'emploi%20en%202023.pdf",
   "523 400 contrôles en 2023 ; 83 % concluent à une recherche active ou à une remobilisation ; 17 % de sanctions.",
   "Données de l'opérateur public.", 'primaire'),
}

def fait(texte, source, periode, perimetre, explication, fiabilite='etabli', chiffre=None):
    d = dict(fait=texte, periode=periode, perimetre=perimetre, explication=explication, source=source, fiabilite=fiabilite)
    if chiffre: d['chiffre'] = chiffre
    return d

def cit(auteur, texte, date, contexte, source):
    return dict(auteur=auteur, texte=texte, date=date, contexte=contexte, source=source)

def fiche(id, affirmation, reproche, resume, contexte, explication, sources, faits, court, moyen, detaille, empathie,
          objections, contre, questions, limites, mots_cles, citations=(), verdict=None, fiabilite='interpretation',
          stabilite='actualite', volet='politique', sous_theme='France insoumise', a_actualiser='2027-04-29',
          raison="Sujet d'actualité politique : vérifier les nouveaux faits, déclarations et décisions.", rubriques=('melenchon-lfi',)):
    keys = list(sources)
    idx = {k: i for i, k in enumerate(keys)}
    def ref(k): return idx[k]
    return dict(
        id=id, type='reponse_critique', affirmation=affirmation, volet=volet, sous_theme=sous_theme,
        rubriques=list(rubriques), mots_cles=mots_cles, verdict=verdict, fiabilite=fiabilite, stabilite=stabilite,
        reproche=reproche, resume=resume, contexte=contexte, explication=explication,
        faits=[{**f, 'source': ref(f['source'])} for f in faits],
        citations=[{**c, 'source': ref(c['source'])} for c in citations],
        argumentaires=dict(court=court, moyen=moyen, detaille=detaille, empathie=empathie),
        formulation_table=court,
        objections_legitimes=objections,
        contre_arguments=[dict(objection=o, reponse=r) for o, r in contre],
        questions=questions, limites=limites,
        sources=[S[k] for k in keys],
        derniere_verification=TODAY, a_actualiser_le=a_actualiser, raison_actualisation=raison,
    )

FICHES = []

# 1 ─────────────────────────────────────────────────────────────── crie
FICHES.append(fiche(
 'melenchon-crie', "Mélenchon crie tout le temps.",
 reproche="On reproche à Jean-Luc Mélenchon un ton constamment haussé. Le reproche s'appuie sur des scènes très diffusées, en particulier la vidéo de la perquisition du siège de LFI en octobre 2018, et sur des meetings au style de tribun.",
 resume="Il est exact que Jean-Luc Mélenchon hausse souvent la voix et qu'il l'assume : des scènes filmées le montrent, et son entourage revendique une stratégie du « coup pour coup ». « Tout le temps » est en revanche une exagération : ses grands discours sont des textes préparés et lus. Surtout, le volume ne dit rien de la justesse des propositions ; certains écarts de comportement restent, eux, légitimement critiquables.",
 contexte="Le style de tribun est une marque revendiquée : meetings longs, vocabulaire du conflit, interpellations. En 2017, son entourage expliquait que la colère est assumée comme une vertu auprès des classes populaires. La perquisition de 2018, filmée en direct, a fixé l'image d'un homme qui crie.",
 explication="Il faut distinguer quatre choses : le volume (il parle fort, c'est un fait), l'agressivité perçue (une impression, qui varie selon les publics), le contenu (ce qu'il propose) et les comportements condamnables (certains épisodes précis). Confondre les quatre empêche de discuter du fond.",
 sources=['perq', 'colere', 'cautres'],
 faits=[
  fait("Lors de la perquisition du siège de LFI le 16 octobre 2018, Jean-Luc Mélenchon, filmé, lance notamment « La République, c'est moi » ; il est condamné en décembre 2019 à trois mois de prison avec sursis et 8 000 € d'amende pour rébellion et provocation.", 'perq', '16 octobre 2018 - décembre 2019', 'Tribunal correctionnel de Bobigny', "La scène qui a le plus nourri l'image de « l'homme qui crie » a donné lieu à une condamnation."),
  fait("En décembre 2017, son entourage revendique de « rendre coup pour coup » ; une étude Fondation Jean-Jaurès / Ifop montre que ses soutiens le jugent courageux quand ses critiques le jugent agressif ou arrogant.", 'colere', 'Décembre 2017', 'Stratégie de communication et image publique', "Le ton est un choix assumé ; sa perception dépend de qui regarde.", 'interpretation'),
  fait("Son discours de lancement de campagne à Saint-Denis, le 7 juin 2026, est un texte préparé lu en 52 minutes, au lexique dense, qui mobilise un vocabulaire du conflit (« guerre », « crime », « menace », « rupture ») ; le politiste Bruno Cautrès reprend le portrait d'un « tribun hors pair ».", 'cautres', '7 juin 2026', 'Analyse logométrique', "Le registre est combatif, mais la forme est celle d'un discours écrit, pas d'un cri permanent.", 'interpretation'),
 ],
 citations=[cit('Jean-Luc Mélenchon', "La République, c'est moi", '16 octobre 2018', "Pendant la perquisition du siège de LFI, face aux policiers.", 'perq')],
 court="Oui, il hausse le ton, parfois trop : il a même été condamné après la perquisition de 2018. Mais parler fort ne dit pas si ce qu'il propose est juste ou faux. On regarde une mesure précise ensemble ?",
 moyen="C'est vrai qu'il parle fort, et il l'assume : son équipe parle de « rendre coup pour coup ». La vidéo de la perquisition de 2018 a marqué, et elle lui a valu une condamnation pour rébellion. Mais dire qu'il crie « tout le temps », c'est exagéré : ses grands discours sont des textes écrits et lus, longs et construits. Et surtout, le volume n'est pas un argument. Jaurès aussi était un tribun. La seule question utile, c'est : ses propositions sont-elles bonnes ou mauvaises ? Sur ça, on peut être d'accord ou pas, mais on parle du fond.",
 detaille="Le reproche contient une part de vrai. Jean-Luc Mélenchon pratique un style de tribun, et il l'assume : en 2017, ses proches revendiquaient une stratégie du « coup pour coup » face aux médias, jugée efficace auprès de son électorat. Certaines scènes ont durablement marqué, au premier rang desquelles la perquisition du siège de LFI en octobre 2018, filmée en direct, où il lance « La République, c'est moi ». Elle lui a valu une condamnation à trois mois de prison avec sursis et 8 000 € d'amende pour rébellion et provocation.\n\nMais « il crie tout le temps » est une généralisation. Ses grands discours sont des textes préparés : celui de Saint-Denis, le 7 juin 2026, a été lu en 52 minutes, avec un vocabulaire riche, selon l'analyse du politiste Bruno Cautrès. Le registre est combatif (« guerre », « menace », « rupture »), ce qui est un choix politique, pas un trouble de comportement.\n\nIl faut surtout séparer quatre niveaux : le volume de la voix, l'agressivité perçue (qui dépend du public : courageux pour ses soutiens, agressif pour ses critiques selon une étude Ifop), le contenu des propositions, et les comportements réellement critiquables. Ces derniers existent et peuvent être reprochés précisément. Mais le volume, à lui seul, ne réfute aucune idée.",
 empathie="Je comprends que ça te fatigue, ce ton-là. Moi aussi, il y a des moments où je trouve qu'il en fait trop. Mais si on le juge sur la voix, on ne parle jamais de ce qu'il propose. Tu veux qu'on prenne une mesure et qu'on regarde si elle tient ?",
 objections=[
  "Certains épisodes dépassent le simple style : la perquisition de 2018 a donné lieu à une condamnation pénale.",
  "Les attaques personnelles contre des journalistes en 2017 (« glapit en pleine hystérie ») relèvent de l'invective, pas du débat.",
  "Le ton peut faire fuir des électeurs qu'il faudrait convaincre ; c'est une critique stratégique légitime.",
 ],
 contre=[
  ("Un responsable politique doit rester calme, c'est une question de respect.", "On peut le penser et le lui reprocher. Mais le calme n'est pas une garantie de justesse : des politiques très posés ont défendu des mesures très contestables."),
  ("S'il crie, c'est qu'il n'a pas d'arguments.", "Ses propositions sont écrites et chiffrées dans un programme : on peut les contester une par une, ce qui est plus solide qu'un jugement sur sa voix."),
 ],
 questions=["Si la même proposition était dite calmement par quelqu'un d'autre, la trouverais-tu meilleure ?", "Quel comportement précis te choque le plus ?"],
 limites=["Aucune mesure objective de la fréquence de ses éclats de voix n'existe ; la fiche s'appuie sur des épisodes documentés et des analyses.", "Les perceptions du ton varient fortement selon les publics."],
 mots_cles=['mélenchon', 'crie', 'hurle', 'gueule', 'voix', 'ton', 'colère', 'tribun', 'perquisition', 'la république c est moi'],
 verdict='plutot_exact', fiabilite='interpretation', stabilite='evolutive',
))

# 2 ─────────────────────────────────────────────────────────────── agressif
FICHES.append(fiche(
 'melenchon-agressif', "Mélenchon est agressif.",
 reproche="On reproche à Jean-Luc Mélenchon une agressivité envers les journalistes, ses adversaires et parfois ses alliés. Le reproche s'appuie sur des invectives publiques, la perquisition de 2018 et des messages visant nommément des responsables.",
 resume="Plusieurs épisodes documentés relèvent d'une agressivité réelle et critiquable : condamnation pour rébellion et provocation en 2019, invectives contre des journalistes en 2017, message accusant la présidente de l'Assemblée d'« encourager le massacre » en 2023. Son camp présente la conflictualité comme une stratégie assumée. Reconnaître ces faits n'empêche pas de juger ses propositions sur le fond.",
 contexte="La conflictualité est un choix revendiqué par LFI, qui estime que le consensus profite aux puissants. Ses adversaires y voient une brutalisation du débat. Le reproche a pris de l'ampleur avec la perquisition de 2018, puis avec les polémiques autour du conflit israélo-palestinien depuis octobre 2023.",
 explication="L'agressivité perçue et le comportement fautif ne sont pas la même chose. Hausser le ton dans un débat est un style ; s'en prendre nommément à une personne au point qu'elle dise se sentir visée est un comportement qu'on peut reprocher précisément.",
 sources=['perq', 'colere', 'braunpivet', 'cautres'],
 faits=[
  fait("Après la perquisition du 16 octobre 2018, il est condamné en décembre 2019 à trois mois d'emprisonnement avec sursis et 8 000 € d'amende pour rébellion et provocation.", 'perq', '2018-2019', 'Tribunal correctionnel de Bobigny', "Un épisode d'agressivité a été qualifié pénalement."),
  fait("En décembre 2017, il écrit qu'une journaliste « glapit en pleine hystérie » et propose un « tribunal » professionnel des journalistes ; le mot est remplacé le lendemain par « conseil de déontologie ».", 'colere', 'Décembre 2017', 'Relations avec les médias', "L'invective personnelle a été en partie retirée par son propre camp."),
  fait("En octobre 2023, il écrit que Yaël Braun-Pivet « campe à Tel Aviv pour encourager le massacre » ; elle répond : « C'est une nouvelle cible qu'on me met dans le dos ». Il dénonce une « absurde police des mots ».", 'braunpivet', 'Octobre 2023', 'Conflit Israël-Hamas', "Une accusation grave visant nommément une responsable, contestée bien au-delà de ses adversaires habituels."),
  fait("Son discours de campagne du 7 juin 2026 mobilise un vocabulaire du conflit (« guerre », « crime », « menace », « rupture »).", 'cautres', 'Juin 2026', 'Analyse lexicale', "La conflictualité fait partie de sa stratégie de discours.", 'interpretation'),
 ],
 citations=[
  cit('Jean-Luc Mélenchon', "campe à Tel Aviv pour encourager le massacre", 'Octobre 2023', "Message visant la présidente de l'Assemblée nationale lors de sa visite en Israël.", 'braunpivet'),
  cit('Yaël Braun-Pivet', "C'est une nouvelle cible qu'on me met dans le dos", 'Octobre 2023', 'Réponse au message de Jean-Luc Mélenchon.', 'braunpivet'),
 ],
 court="Certaines de ses sorties sont agressives, je ne vais pas le nier : il a été condamné en 2019 et des gens de gauche l'ont critiqué. Mais ça ne règle pas la question de ses idées. On parle d'une mesure précise ?",
 moyen="Il y a des épisodes où il a clairement dépassé les bornes : la perquisition de 2018, qui lui a valu une condamnation ; des insultes contre des journalistes en 2017 ; ou ce message accusant la présidente de l'Assemblée d'« encourager le massacre » en 2023. Ça, on peut le lui reprocher, et je ne le défends pas. Mais il faut distinguer : un style combatif, qu'il assume comme stratégie, et des fautes précises. Et aucun de ces épisodes ne dit si le SMIC à 1 400 € ou la retraite à 60 ans sont de bonnes idées. Si on veut être juste, on critique les fautes et on discute les propositions.",
 detaille="Le reproche s'appuie sur des faits réels. En octobre 2018, lors de la perquisition du siège de LFI, il s'en prend aux policiers et au magistrat ; il est condamné en décembre 2019 pour rébellion et provocation. En décembre 2017, il écrit d'une journaliste qu'elle « glapit en pleine hystérie » et propose un « tribunal » des journalistes, avant que son propre camp ne remplace le mot. En octobre 2023, il accuse la présidente de l'Assemblée nationale de « camper à Tel Aviv pour encourager le massacre », ce qu'elle vit comme une cible dans le dos.\n\nSon camp explique cette conflictualité par une stratégie : refuser le consensus mou, nommer les adversaires, « rendre coup pour coup ». Une étude Ifop citée en 2017 montre que cette posture est vue comme du courage par ses soutiens et comme de l'agressivité par ses critiques.\n\nPour être honnête, il faut donc distinguer trois niveaux. Le style combatif, qui relève d'un choix politique et peut plaire ou déplaire. Les fautes précises (attaques personnelles, condamnation), qui sont légitimement critiquables, y compris par ses électeurs. Et le contenu des propositions, qui doit être discuté pour lui-même. Rejeter un programme parce que son porte-parole est jugé agressif, c'est se priver d'un débat ; défendre chaque sortie parce qu'on approuve le programme, c'est perdre en crédibilité.",
 empathie="Je comprends que certaines de ses sorties te choquent ; il y en a qui me gênent aussi. Je ne vais pas tout défendre. Ce que je te propose, c'est qu'on sépare l'homme et ses excès de ce qu'il propose concrètement.",
 objections=[
  "La condamnation de 2019 est un fait judiciaire, pas une impression.",
  "Accuser nommément une responsable d'« encourager le massacre » expose à des menaces : la critique est fondée.",
  "La stratégie du « coup pour coup » peut abîmer le débat public, quel que soit le camp qui la pratique.",
 ],
 contre=[
  ("Un homme agressif ne devrait pas gouverner.", "C'est un critère légitime pour voter. Mais il vaut pour tous les responsables, et il ne dispense pas d'examiner les propositions des uns et des autres."),
  ("Ses électeurs approuvent cette violence verbale.", "Une partie apprécie la combativité, d'autres la regrettent : le jugement sur le style n'est pas le même que l'adhésion au programme."),
 ],
 questions=["Quelle différence fais-tu entre un ton combatif et une attaque personnelle ?", "Est-ce que le même critère s'applique aux autres responsables politiques ?"],
 limites=["La fiche ne recense pas tous les épisodes ; elle retient les plus documentés.", "La suite judiciaire de la condamnation de 2019 (appel éventuel) n'est pas détaillée dans la source consultée."],
 mots_cles=['mélenchon', 'agressif', 'agressivité', 'violent', 'insultes', 'journalistes', 'braun-pivet', 'perquisition', 'invective'],
 verdict='plutot_exact', fiabilite='etabli', stabilite='evolutive',
))

# 3 ─────────────────────────────────────────────────────────────── autoritaire
FICHES.append(fiche(
 'melenchon-autoritaire', "Mélenchon est autoritaire.",
 reproche="On reproche à Jean-Luc Mélenchon un fonctionnement autoritaire, au sein de LFI comme dans son rapport aux institutions. Le reproche s'appuie notamment sur les non-réinvestitures de juin 2024, qualifiées de « purge » par les intéressés, et sur la phrase « La République, c'est moi » en 2018.",
 resume="Le reproche est sérieux pour la gestion interne : en juin 2024, des députés sortants critiques (Corbière, Garrido, Simonnet…) n'ont pas été réinvestis tandis qu'Adrien Quatennens, condamné pour violences conjugales, l'était, ce que les écartés ont appelé une « purge ». En revanche, le programme institutionnel de LFI (Constituante, référendum d'initiative citoyenne y compris révocatoire) va dans le sens d'un contrôle accru des élus par les citoyens, pas d'une concentration des pouvoirs.",
 contexte="LFI est un mouvement sans structure de parti classique, souvent décrit comme très centralisé autour de son fondateur. Les crises internes de 2024, puis les départs de figures comme François Ruffin, ont relancé le débat.",
 explication="Il faut distinguer la gestion d'un parti, qui peut être critiquée, et le projet institutionnel proposé au pays, qui se juge sur ses textes. On peut à la fois critiquer un fonctionnement interne vertical et constater qu'un programme propose plus de démocratie directe.",
 sources=['invest', 'perq', 'aec'],
 faits=[
  fait("Le 14 juin 2024, LFI investit Adrien Quatennens, condamné en décembre 2022 pour violences conjugales, et ne réinvestit pas plusieurs députés sortants critiques, dont Alexis Corbière, Raquel Garrido et Danielle Simonnet ; les intéressés et leurs soutiens parlent de « purge ».", 'invest', 'Juin 2024', 'Investitures aux législatives anticipées', "Un épisode documenté de mise à l'écart de voix critiques."),
  fait("Lors de la perquisition de 2018, il lance « La République, c'est moi » ; il est condamné en 2019 pour rébellion et provocation.", 'perq', '2018-2019', "Rapport à l'autorité judiciaire", "Une phrase souvent citée comme symbole d'un rapport personnel au pouvoir."),
  fait("Le programme L'Avenir en commun (2022) propose une Assemblée constituante convoquée par référendum, composée de citoyens élus ou tirés au sort, et un référendum d'initiative citoyenne permettant de proposer ou d'abroger une loi, de modifier la Constitution et de révoquer des élus.", 'aec', '2022', 'Programme présidentiel (source partisane)', "Le projet institutionnel affiché prévoit plus de pouvoir aux citoyens, y compris contre les élus.", 'etabli'),
 ],
 citations=[cit('Jean-Luc Mélenchon', "La République, c'est moi", '16 octobre 2018', 'Pendant la perquisition du siège de LFI.', 'perq')],
 court="Sur la façon dont il gère son mouvement, il y a de vraies critiques, y compris à gauche : en 2024, des députés critiques ont été écartés. Mais son programme propose qu'on puisse révoquer les élus par référendum : c'est l'inverse d'un projet autoritaire.",
 moyen="Je ne vais pas te dire que LFI est un modèle de démocratie interne : en juin 2024, Corbière, Garrido ou Simonnet ont été écartés des investitures, et eux-mêmes ont parlé de purge. Ça, c'est une critique sérieuse. Mais il faut regarder aussi ce qu'il propose pour le pays : une Constituante élue ou tirée au sort et validée par référendum, et un référendum d'initiative citoyenne qui permettrait même de révoquer les élus, lui compris. On peut trouver ça irréaliste, mais ce n'est pas un projet de concentration du pouvoir.",
 detaille="Le reproche d'autoritarisme mélange deux choses qu'il vaut mieux séparer.\n\nLa première est le fonctionnement interne de LFI. Ici, la critique est documentée : en juin 2024, lors des législatives anticipées, plusieurs députés sortants connus pour leurs désaccords (Alexis Corbière, Raquel Garrido, Danielle Simonnet, mais aussi Hendrik Davi et Frédéric Mathieu) n'ont pas été réinvestis, tandis qu'Adrien Quatennens, condamné pour violences conjugales, l'était. Les intéressés ont dénoncé une « purge », et François Ruffin a critiqué la décision. Sur ce point, défendre LFI coûte que coûte n'est pas crédible.\n\nLa seconde est le projet institutionnel proposé au pays. Le programme L'Avenir en commun prévoit une Assemblée constituante convoquée par référendum, composée de citoyens élus ou tirés au sort, et un référendum d'initiative citoyenne permettant de proposer ou d'abroger une loi, de modifier la Constitution et de révoquer les élus. On peut juger ces propositions risquées ou irréalistes, mais elles vont dans le sens d'un contrôle accru des gouvernants par les citoyens.\n\nLa phrase « La République, c'est moi », prononcée en 2018 face aux policiers, est souvent citée comme symbole. Elle a été dite dans un contexte où il défendait son statut de parlementaire ; elle reste une formule malheureuse qui a nourri le soupçon.",
 empathie="Tu as raison sur un point : la façon dont certains députés ont été écartés en 2024 m'a gêné aussi. Ce que je te propose, c'est de séparer le chef de parti, qu'on peut critiquer, et les règles qu'il propose pour le pays, qu'on peut lire.",
 objections=[
  "Les non-réinvestitures de 2024 visant des voix critiques sont un fait documenté.",
  "Investir un député condamné pour violences conjugales tout en écartant des opposants internes pose une question de cohérence.",
  "Un programme démocratique sur le papier ne garantit pas une pratique démocratique au pouvoir ; la critique vaut pour tous les partis.",
 ],
 contre=[
  ("Le RIC révocatoire servirait surtout à mettre la pression sur les élus.", "C'est un débat légitime sur la démocratie directe ; mais c'est un outil donné aux citoyens, pas au chef de l'État."),
  ("La Constituante, c'est un saut dans l'inconnu.", "C'est une critique de fond recevable ; elle porte sur le risque d'instabilité, pas sur une dérive autoritaire."),
 ],
 questions=["Qu'est-ce qui te semble le plus autoritaire : la gestion du parti ou les propositions pour le pays ?", "Qui pourrait révoquer les élus avec le RIC, selon toi ?"],
 limites=["Le fonctionnement interne de LFI n'est documenté ici que par l'épisode de juin 2024.", "Le programme cité est la version abrégée de 2022 ; le programme de 2027 n'a pas été consulté."],
 mots_cles=['mélenchon', 'autoritaire', 'dictateur', 'purge', 'investitures', 'corbière', 'garrido', 'quatennens', 'ric', 'constituante', 'chef'],
 verdict='trompeur', fiabilite='interpretation', stabilite='evolutive',
))

# 4 ─────────────────────────────────────────────────────────────── dangereux démocratie
FICHES.append(fiche(
 'melenchon-dangereux-democratie', "Mélenchon est dangereux pour la démocratie.",
 reproche="On présente Jean-Luc Mélenchon et LFI comme une menace pour les institutions démocratiques. L'argument s'est appuyé en 2026 sur le classement de LFI à « l'extrême gauche » par le ministère de l'Intérieur pour les municipales, validé par le Conseil d'État.",
 resume="En février 2026, le Conseil d'État a jugé que classer LFI à « l'extrême gauche » dans la grille de présentation des résultats des municipales n'était pas une « erreur manifeste d'appréciation ». Le ministre invoquait une « remise en cause très forte de l'autorité judiciaire » et des accusations systématiques contre la police. Ce contrôle restreint ne juge pas le caractère démocratique du mouvement. LFI se présente aux élections et propose de changer la Constitution par référendum ; ses attaques contre la justice et la police sont, elles, légitimement discutables.",
 contexte="La grille de « nuances » politiques sert au ministère de l'Intérieur à présenter les résultats électoraux. En 2024, le Conseil d'État avait validé le classement de LFI à gauche ; pour les municipales de 2026, le ministère l'a déplacée à « l'extrême gauche ».",
 explication="Un classement statistique n'est ni une interdiction ni un verdict sur la démocratie. Le Conseil d'État vérifie seulement que l'administration ne commet pas d'erreur grossière. La question démocratique se juge sur les faits : respect des élections, des décisions de justice, des libertés.",
 sources=['conseil_etat', 'aec', 'perq'],
 faits=[
  fait("Le Conseil d'État rejette en février 2026 les recours de LFI et de l'UDR contre leur classement respectif à « l'extrême gauche » et à « l'extrême droite » pour les municipales, faute d'« erreur manifeste d'appréciation » (décisions n° 512694, 512695, 512981 et 512983).", 'conseil_etat', 'Février 2026', 'Grille de nuances des municipales 2026', "Le contrôle porte sur une erreur grossière, pas sur le caractère démocratique."),
  fait("Le ministre de l'Intérieur, Laurent Nuñez, justifiait ce classement par une « remise en cause très forte de l'autorité judiciaire » et des accusations systématiques contre la police ; LFI était classée à gauche jusque-là, ce qu'avait confirmé une décision de 2024.", 'conseil_etat', '2024-2026', 'Motifs administratifs', "Le classement repose sur des prises de position, pas sur une remise en cause des élections."),
  fait("Le programme L'Avenir en commun propose de changer de Constitution par une Assemblée constituante convoquée par référendum et un référendum d'initiative citoyenne.", 'aec', '2022', 'Programme (source partisane)', "Les changements institutionnels proposés passent par le vote."),
  fait("En 2019, Jean-Luc Mélenchon a été condamné pour rébellion et provocation après s'être opposé à une perquisition judiciaire en 2018.", 'perq', '2018-2019', "Rapport à l'autorité judiciaire", "Un épisode concret qui nourrit le reproche de défiance envers la justice."),
 ],
 court="Le Conseil d'État a validé un classement « extrême gauche » pour présenter les résultats des municipales, mais il n'a pas dit que LFI était antidémocratique. LFI va aux élections et veut changer la Constitution par référendum. Ses attaques contre les juges, elles, se discutent.",
 moyen="Il faut être précis. En 2026, le ministère de l'Intérieur a classé LFI à « l'extrême gauche » pour présenter les résultats des municipales, et le Conseil d'État a jugé que ce n'était pas une erreur grossière. Le ministre reprochait à LFI de remettre en cause l'autorité judiciaire et d'accuser la police. C'est un vrai sujet de débat, et l'épisode de la perquisition de 2018 n'a pas aidé. Mais le Conseil d'État n'a pas jugé que LFI était antidémocratique : ce n'était pas la question. LFI se présente aux élections, siège à l'Assemblée et propose de changer la Constitution par référendum. On peut critiquer ses positions sur la justice sans en faire une menace pour la démocratie.",
 detaille="Le reproche s'est appuyé en 2026 sur une décision du Conseil d'État. Pour les élections municipales, le ministère de l'Intérieur a classé LFI dans le bloc « extrême gauche » de sa grille de nuances, qui sert à agréger les résultats. LFI a contesté. Le Conseil d'État a rejeté le recours en février 2026, estimant que ce classement ne relevait pas d'une « erreur manifeste d'appréciation ». Le ministre justifiait sa décision par une « remise en cause très forte de l'autorité judiciaire » et des accusations systématiques contre la police.\n\nCette décision a une portée limitée : le juge vérifie seulement que l'administration ne s'est pas grossièrement trompée. Il ne se prononce pas sur le caractère démocratique du mouvement, et il avait validé en 2024 le classement de LFI à gauche.\n\nSur le fond, les critiques ont des appuis : la perquisition de 2018, qui a valu une condamnation à Jean-Luc Mélenchon, ou des déclarations mettant en cause la justice et la police. Elles méritent d'être discutées précisément. Mais le projet institutionnel de LFI passe par les urnes : Assemblée constituante convoquée par référendum, référendum d'initiative citoyenne. On peut le juger risqué ou irréaliste, il ne propose pas de supprimer les élections ni les libertés publiques.",
 empathie="Je comprends l'inquiétude, surtout quand on entend des attaques contre les juges. Je ne trouve pas ça bien non plus. Mais je crois qu'il faut garder le mot « dangereux pour la démocratie » pour ceux qui veulent supprimer des élections ou des libertés. Est-ce que tu as un exemple de ce genre ?",
 objections=[
  "Remettre en cause des décisions de justice ou la légitimité des magistrats fragilise l'État de droit, quel que soit le parti.",
  "Le classement « extrême gauche » a été jugé non manifestement erroné par la plus haute juridiction administrative.",
  "Un projet de Constituante comporte des incertitudes réelles sur la stabilité des institutions.",
 ],
 contre=[
  ("Le Conseil d'État a confirmé que LFI est d'extrême gauche.", "Il a confirmé qu'un classement administratif n'était pas manifestement erroné. Ce n'est ni une interdiction, ni une décision sur le respect de la démocratie."),
  ("Ils veulent une révolution.", "Le programme décrit une révolution par les urnes : référendum, Constituante, RIC. On peut contester ces outils, mais ce sont des procédures électorales."),
 ],
 questions=["Qu'est-ce qui, selon toi, rendrait un parti vraiment dangereux pour la démocratie ?", "Le même critère s'applique-t-il aux autres partis classés aux extrêmes ?"],
 limites=["La décision du Conseil d'État est connue par un article de presse spécialisée, pas par la lecture intégrale des décisions.", "La date exacte de la décision (fin février 2026) est déduite de l'article."],
 mots_cles=['mélenchon', 'lfi', 'dangereux', 'démocratie', 'extrême gauche', 'conseil d état', 'nuançage', 'justice', 'juges', 'constituante', 'vie république'],
 verdict='trompeur', fiabilite='interpretation', stabilite='actualite',
))

# 5 ─────────────────────────────────────────────────────────────── antisémitisme
FICHES.append(fiche(
 'lfi-antisemite', "LFI est antisémite.",
 reproche="Depuis le 7 octobre 2023, LFI et Jean-Luc Mélenchon sont accusés d'antisémitisme, par leurs adversaires mais aussi par des responsables de gauche. Les accusations portent sur des déclarations précises : le communiqué du 7 octobre, l'attaque contre Yaël Braun-Pivet, le qualificatif « résiduel » appliqué à l'antisémitisme en 2024, des jeux de mots sur des noms en 2026.",
 resume="Le sujet ne se règle ni par une absolution ni par une étiquette globale. Plusieurs déclarations ont été jugées graves, y compris à gauche : Laurence Rossignol (PS) a parlé d'« une constante du discours antisémite » à propos du communiqué du 7 octobre 2023, Olivier Faure s'est dit « heurté » quand Mélenchon a qualifié l'antisémitisme de « résiduel » alors que les actes recensés explosaient. Mélenchon et LFI rejettent toute accusation d'antisémitisme. Critiquer le gouvernement israélien n'est pas antisémite ; mais présenter un propos comme une critique politique ne suffit pas à l'en exonérer : chaque déclaration doit être examinée.",
 contexte="Les actes antisémites recensés ont fortement augmenté après le 7 octobre 2023. LFI a fait du soutien aux Palestiniens un axe majeur. Les accusations portent moins sur le programme que sur des déclarations, des ambiguïtés et, selon certains observateurs, une difficulté à prendre au sérieux certains discours.",
 explication="Trois questions distinctes : une critique de la politique israélienne est-elle légitime ? (oui, comme toute critique d'un gouvernement). Une déclaration précise reprend-elle des stéréotypes antisémites ou minimise-t-elle l'antisémitisme ? (à examiner au cas par cas). Un parti est-il antisémite dans son ensemble ? (affirmation globale qu'aucune décision de justice citée ici n'établit, mais qui ne peut pas servir à évacuer les déclarations problématiques).",
 sources=['afp7oct', 'braunpivet', 'residuel', 'faure', 'thelocal'],
 faits=[
  fait("Le 7 octobre 2023, le communiqué du groupe LFI replace l'attaque du Hamas dans le contexte de « l'intensification de la politique d'occupation israélienne » ; Laurence Rossignol (PS) y voit « une constante du discours antisémite » ; François Ruffin condamne l'attaque sans réserve.", 'afp7oct', '7 octobre 2023', 'Réactions au massacre du 7 octobre', "La critique est venue aussi de la gauche, et de l'intérieur de LFI."),
  fait("En octobre 2023, Jean-Luc Mélenchon écrit que la présidente de l'Assemblée « campe à Tel Aviv pour encourager le massacre » ; elle répond qu'on lui met « une nouvelle cible dans le dos ».", 'braunpivet', 'Octobre 2023', 'Visite de Yaël Braun-Pivet en Israël', "Le message a été largement critiqué, y compris pour ses effets possibles sur la sécurité de l'intéressée."),
  fait("Le 2 juin 2024, il écrit que l'antisémitisme « reste résiduel en France », alors que le gouvernement recense 366 actes antisémites au premier trimestre 2024 (+300 %) et que le Crif en compte 1 676 en 2023 contre 436 en 2022.", 'residuel', '2022-2024', 'Actes antisémites recensés (sources gouvernementale et associative)', "Le terme a été jugé en contradiction avec les données disponibles.", 'etabli', '366 actes au T1 2024 ; 1 676 en 2023 (Crif)'),
  fait("Olivier Faure (PS) se dit « heurté » : « Tout montre qu'il y a au contraire une explosion de l'antisémitisme ».", 'faure', '4 juin 2024', "Réaction d'un allié", "Un responsable de la même coalition conteste frontalement le propos."),
  fait("Début 2026, une plaisanterie sur « Epsteen » à Lyon, présentée comme ironique, et la déformation du nom de Raphaël Glucksmann relancent les accusations ; Mélenchon rejette toute accusation d'antisémitisme. Selon The Local, le reproche porte souvent sur le fait de ne pas prendre au sérieux ce type de rhétorique ; l'article ne cite aucune décision de justice.", 'thelocal', 'Février-mars 2026', 'Campagne municipale', "Les polémiques portent sur des propos et leur réception, pas sur une condamnation."),
 ],
 citations=[
  cit('Laurence Rossignol (PS)', "C'est une constante du discours antisémite", '7 octobre 2023', 'À propos du communiqué du groupe LFI.', 'afp7oct'),
  cit('Jean-Luc Mélenchon', "l'antisémitisme reste résiduel en France", '2 juin 2024', 'Billet de blog.', 'residuel'),
  cit('Olivier Faure (PS)', "Tout montre qu'il y a au contraire une explosion de l'antisémitisme", '4 juin 2024', 'Réaction au billet de Jean-Luc Mélenchon.', 'faure'),
 ],
 court="Je ne vais pas balayer ça : certaines déclarations de Mélenchon ont été jugées graves, y compris par des gens de gauche, et dire que l'antisémitisme est « résiduel » quand les actes explosent, c'est une faute. Critiquer le gouvernement israélien n'est pas antisémite. On peut regarder les déclarations une par une ?",
 moyen="C'est un sujet sérieux, et je ne vais pas te dire que tout va bien. Le 7 octobre 2023, le communiqué de LFI a été dénoncé jusqu'au PS comme reprenant « une constante du discours antisémite ». En 2024, Mélenchon a écrit que l'antisémitisme était « résiduel », alors que les actes recensés avaient explosé ; Olivier Faure s'est dit « heurté ». En 2026, des jeux de mots sur des noms ont relancé la polémique. Lui et LFI rejettent toute accusation d'antisémitisme. Ce que je pense : critiquer la politique du gouvernement israélien est légitime, mais ça ne rend pas automatiquement innocente une phrase qui se présente comme une critique. Il faut juger chaque déclaration sur ce qu'elle dit, et des gens de gauche le font.",
 detaille="L'accusation d'antisémitisme visant LFI s'est imposée après le 7 octobre 2023. Elle mérite mieux qu'un réflexe de défense ou qu'une étiquette globale.\n\nLes faits d'abord. Le jour même de l'attaque du Hamas, le communiqué du groupe LFI la replace dans le contexte de « l'intensification de la politique d'occupation israélienne » ; la sénatrice socialiste Laurence Rossignol y voit « une constante du discours antisémite », tandis que François Ruffin condamne sans réserve. Quelques jours plus tard, Jean-Luc Mélenchon accuse la présidente de l'Assemblée de « camper à Tel Aviv pour encourager le massacre ». En juin 2024, il écrit que l'antisémitisme « reste résiduel », alors que le gouvernement recense 366 actes au premier trimestre (+300 %) et que le Crif en compte 1 676 en 2023 contre 436 en 2022 ; Olivier Faure, allié du Nouveau Front populaire, se dit « heurté ». En 2026, une plaisanterie sur « Epsteen » et la déformation du nom de Raphaël Glucksmann relancent la polémique.\n\nMélenchon et LFI rejettent toute accusation d'antisémitisme et affirment combattre le racisme sous toutes ses formes. Aucune décision de justice citée dans les sources consultées ne qualifie ces propos.\n\nDeux règles permettent de rester honnête. Premièrement, critiquer le gouvernement israélien, sa politique à Gaza ou la colonisation n'est pas de l'antisémitisme ; confondre les deux interdit tout débat sur le Proche-Orient. Deuxièmement, présenter un propos comme une critique politique ne suffit pas à l'exonérer : minimiser l'antisémitisme quand il augmente, jouer sur des noms ou viser nommément des personnalités juives appellent un examen précis. C'est exactement ce que font des responsables de gauche qui critiquent ces déclarations sans renoncer à défendre les Palestiniens.",
 empathie="Je comprends que ça t'inquiète, et c'est normal : l'antisémitisme a augmenté, ce n'est pas un sujet secondaire. Je ne vais pas défendre toutes les phrases de Mélenchon. Je voudrais juste qu'on distingue ce qui est critiquable dans ses déclarations de la cause palestinienne elle-même.",
 objections=[
  "Qualifier l'antisémitisme de « résiduel » au moment d'une forte hausse des actes recensés minimise un danger réel.",
  "Des responsables de gauche (Rossignol, Faure, Ruffin) ont eux-mêmes critiqué ces prises de position : ce n'est pas qu'une attaque de la droite.",
  "Jouer sur des noms de personnalités juives, même présenté comme ironique, reprend des codes qu'on ne peut pas ignorer.",
  "La répétition des polémiques pose une question politique, même en l'absence de décision de justice.",
 ],
 contre=[
  ("Défendre les Palestiniens, c'est forcément antisémite.", "Non. Critiquer un gouvernement et défendre les droits d'un peuple sont légitimes ; c'est la manière de le faire, dans chaque déclaration, qui doit être examinée."),
  ("C'est une campagne de calomnies orchestrée.", "Certaines accusations sont instrumentalisées, mais d'autres viennent d'alliés de gauche et portent sur des propos précis : les rejeter toutes en bloc n'est pas crédible."),
 ],
 questions=["Quelle déclaration précise te pose problème ? Regardons ce qu'elle dit exactement.", "Comment distingues-tu une critique d'Israël d'un propos antisémite ?"],
 limites=["La fiche ne recense pas toutes les déclarations ni toutes les réponses de LFI.", "Les chiffres d'actes antisémites cités sont ceux rapportés par la presse en juin 2024 ; ils doivent être actualisés avec les bilans officiels plus récents.", "Aucune décision de justice n'a été trouvée dans les sources consultées ; cela ne préjuge pas de procédures éventuelles."],
 mots_cles=['lfi', 'mélenchon', 'antisémite', 'antisémitisme', 'juifs', '7 octobre', 'israël', 'gaza', 'hamas', 'palestine', 'résiduel', 'glucksmann', 'crif'],
 verdict=None, fiabilite='debat', stabilite='actualite', a_actualiser='2027-01-29',
))

# 6 ─────────────────────────────────────────────────────────────── communautarisme
FICHES.append(fiche(
 'lfi-communautarisme', "LFI fait du communautarisme.",
 reproche="On reproche à LFI de flatter un électorat musulman et de céder sur la laïcité. Le reproche s'appuie notamment sur la participation de Jean-Luc Mélenchon à la marche contre l'islamophobie du 10 novembre 2019 et sur son opposition à la loi « séparatisme » en 2021.",
 resume="Le programme de LFI affiche le contraire : il propose de « combattre les communautarismes et l'usage politique des religions » et de supprimer le financement public des cultes en Alsace-Moselle. Mais la position de Jean-Luc Mélenchon a évolué : il soutenait l'interdiction du voile à l'école en 2004 et rejetait le mot « islamophobie » en 2015, avant de participer à la marche de 2019, organisée notamment avec le CCIF et contestée pour certains signataires. Ce changement est critiqué (Blanquer, Peña-Ruiz, Hidalgo) et défendu comme une lutte contre les discriminations.",
 contexte="La marche du 10 novembre 2019 suit l'attaque d'une mosquée à Bayonne. Une partie de la gauche (PS, PRG) refuse d'y aller, en raison du terme « islamophobie » et de l'identité de certains signataires. Depuis, le débat sur la laïcité divise profondément la gauche.",
 explication="Le communautarisme désigne le fait de faire passer l'appartenance à un groupe avant la loi commune. Lutter contre les discriminations visant des croyants n'est pas du communautarisme ; s'associer à des organisations contestées ou adapter ses positions à des considérations électorales peut, en revanche, être critiqué.",
 sources=['aec', 'marche', 'slate'],
 faits=[
  fait("Le programme L'Avenir en commun (2022) propose de « combattre les communautarismes et l'usage politique des religions » et de supprimer le financement public des cultes en Alsace-Moselle.", 'aec', '2022', 'Programme (source partisane)', "Sur le papier, la position est laïque et même plus stricte que le droit actuel sur le Concordat."),
  fait("La marche contre l'islamophobie du 10 novembre 2019, appelée après l'attaque d'une mosquée à Bayonne et soutenue notamment par le NPA et le Collectif contre l'islamophobie en France (CCIF), réunit quelques milliers de personnes ; Mélenchon y participe, le PS et le PRG non ; le terme et certains signataires sont contestés.", 'marche', '10 novembre 2019', 'Paris', "C'est l'épisode le plus cité à l'appui du reproche."),
  fait("En 2004, Mélenchon soutient l'interdiction du voile à l'école ; en 2015, il rejette le terme « islamophobie » ; en 2019, il participe à la marche ; en 2021, il s'oppose au projet de loi « séparatisme ».", 'slate', '2004-2021', "Analyse d'un chercheur en science politique", "L'évolution est réelle ; ses critiques y voient un glissement, lui une adaptation à la montée des discriminations.", 'interpretation'),
 ],
 court="Le programme de LFI dit noir sur blanc qu'il faut combattre les communautarismes et l'usage politique des religions. Après, la participation de Mélenchon à la marche de 2019 a été critiquée, même à gauche, et ça se discute. Mais défendre des croyants contre les discriminations, ce n'est pas du communautarisme.",
 moyen="Regardons les deux côtés. Le programme de LFI propose de combattre les communautarismes et l'usage politique des religions, et même de supprimer le financement des cultes en Alsace-Moselle : c'est plus laïque que la loi actuelle. En même temps, Mélenchon a changé : il soutenait l'interdiction du voile à l'école en 2004, il refusait le mot « islamophobie » en 2015, puis il a participé à la marche de 2019, avec des organisateurs contestés, alors que le PS a refusé d'y aller. Ses critiques y voient de l'électoralisme ; lui dit qu'il défend des citoyens visés par la haine. Les deux lectures existent. Mais lutter contre les discriminations, en soi, ce n'est pas faire passer une communauté avant la loi.",
 detaille="Le reproche de communautarisme vise surtout l'évolution de Jean-Luc Mélenchon sur l'islam et la laïcité.\n\nCette évolution est documentée. Sénateur en 2004, il soutient l'interdiction du voile à l'école. En 2015, après l'attentat contre Charlie Hebdo, il rejette le terme « islamophobie ». En novembre 2019, il participe pourtant à la marche contre l'islamophobie, appelée après l'attaque d'une mosquée à Bayonne et soutenue notamment par le NPA et le CCIF ; le terme et certains signataires sont contestés, et le PS comme le PRG refusent de venir. En 2021, il s'oppose au projet de loi « séparatisme », qui selon lui alimenterait la haine envers les musulmans.\n\nSes critiques (Jean-Michel Blanquer, le philosophe Henri Peña-Ruiz, Anne Hidalgo) y voient un abandon de l'universalisme républicain. Lui défend une laïcité de séparation stricte qui protège la liberté de conscience et n'est pas une hostilité envers une religion.\n\nLe programme, lui, est clair : « combattre les communautarismes et l'usage politique des religions », supprimer le financement public des cultes en Alsace-Moselle. On peut donc discuter de la cohérence entre ce programme et certaines alliances ou présences dans des manifestations. Mais assimiler la lutte contre les discriminations visant des musulmans à du communautarisme, c'est confondre la défense de droits égaux avec la revendication de règles séparées.",
 empathie="Je comprends que la marche de 2019 t'ait choqué ; elle a aussi divisé la gauche. Ce qui compte pour moi, c'est que la même loi s'applique à tous et que personne ne soit visé à cause de sa religion. Sur ça, on est peut-être d'accord ?",
 objections=[
  "Participer à une marche co-organisée par des structures contestées pose une question de choix d'alliés.",
  "Le changement de position entre 2015 et 2019 peut être lu comme électoraliste : c'est une interprétation défendue par des observateurs.",
  "Le terme « islamophobie » est contesté par des laïques de gauche, qui craignent qu'il serve à disqualifier la critique de la religion.",
 ],
 contre=[
  ("LFI fait campagne dans les quartiers pour le vote musulman.", "Faire campagne auprès d'électeurs n'est pas du communautarisme ; la question est de savoir si on leur promet des règles à part. Le programme ne le fait pas."),
  ("Le PS n'est pas allé à la marche, preuve que c'était problématique.", "C'est un argument sérieux : la gauche elle-même était divisée. Le désaccord porte sur un événement, pas sur un projet de société."),
 ],
 questions=["Quelle différence fais-tu entre défendre des croyants contre le racisme et défendre une communauté contre la loi ?", "La suppression du Concordat en Alsace-Moselle, c'est plus ou moins de laïcité selon toi ?"],
 limites=["L'article analysant l'évolution de Mélenchon est une republication de The Conversation dont la date et l'auteur n'apparaissent pas dans la version consultée.", "Le devenir judiciaire du CCIF n'est pas traité dans les sources consultées."],
 mots_cles=['lfi', 'mélenchon', 'communautarisme', 'communautariste', 'islamophobie', 'marche', 'musulmans', 'laïcité', 'séparatisme', 'ccif', 'voile', 'clientélisme'],
 rubriques=('melenchon-lfi', 'islamo-gauchisme-laicite'),
 verdict='trompeur', fiabilite='debat', stabilite='evolutive',
))

# 7 ─────────────────────────────────────────────────────────────── ruiner la France
FICHES.append(fiche(
 'melenchon-ruiner-france', "Mélenchon veut ruiner la France.",
 reproche="On accuse le programme de Jean-Luc Mélenchon, puis celui du Nouveau Front populaire, de mener le pays à la faillite par l'explosion des dépenses et des impôts. L'argument s'appuie sur les chiffrages de 2024.",
 resume="Le programme est coûteux : le NFP l'a lui-même chiffré à environ 150 Md€ de dépenses supplémentaires d'ici 2027, financées à hauteur d'environ 100 Md€ par de nouvelles recettes ; l'Institut Montaigne l'estimait à 179 Md€ par an (contre 71 Md€ pour le RN). Le coût et le financement se discutent sérieusement. Mais « ruiner » est un jugement : il s'agit d'un choix de redistribution, financé principalement par des impôts sur les plus aisés et les grandes entreprises, dont les effets économiques sont débattus.",
 contexte="Lors des législatives anticipées de 2024, les chiffrages des programmes sont devenus un enjeu central. La majorité sortante a dénoncé un « matraquage fiscal » ; le NFP a présenté son propre chiffrage le 21 juin 2024.",
 explication="Un chiffrage repose sur des hypothèses (croissance, rendement des impôts, comportements). Les écarts entre le chiffrage du NFP et celui de l'Institut Montaigne viennent en partie de ces hypothèses. Pour donner un ordre de grandeur, 150 Md€ représentent environ 9 % des 1 672 Md€ de dépenses publiques de 2024 (calcul de la fiche).",
 sources=['nfp', 'montaigne'],
 faits=[
  fait("Le NFP chiffre son programme à environ 150 Md€ de dépenses supplémentaires d'ici 2027, avec 25 Md€ de mesures d'urgence en 2024 (abrogation des réformes des retraites et de l'assurance chômage, SMIC à 1 600 € net, hausse de 10 % du point d'indice) et environ 100 Md€ de recettes nouvelles (ISF climatique, taxe sur les superprofits…).", 'nfp', '21 juin 2024', 'Chiffrage présenté par le NFP', "Les auteurs du programme reconnaissent eux-mêmes un coût élevé, en partie financé.", 'estimation', '≈ 150 Md€ / ≈ 100 Md€ de recettes'),
  fait("Gabriel Attal, alors Premier ministre, dénonce un « matraquage fiscal ».", 'nfp', 'Juin 2024', 'Réactions', "La critique porte sur la fiscalité, pas seulement sur la dépense.", 'etabli'),
  fait("L'Institut Montaigne estime le coût annuel du programme du NFP à 179 Md€, contre 71 Md€ pour le RN et environ 21 Md€ pour Ensemble.", 'montaigne', '5 juillet 2024', 'Chiffrage indépendant (think tank libéral)', "Le programme est le plus coûteux selon ce chiffrage, contesté par ses auteurs.", 'estimation', '179 Md€/an'),
 ],
 court="Le programme coûte cher, c'est vrai : le NFP lui-même parlait de 150 milliards d'ici 2027, avec 100 milliards de recettes nouvelles. On peut discuter du financement. Mais taxer davantage les plus riches pour augmenter les salaires, c'est un choix politique, pas une volonté de ruiner le pays.",
 moyen="Soyons honnêtes : le programme du Nouveau Front populaire était coûteux. Ses auteurs l'ont chiffré à environ 150 milliards d'ici 2027, l'Institut Montaigne, qui est plutôt libéral, à 179 milliards par an. Il y a donc un vrai débat sur le financement et sur la dette. Mais le NFP prévoyait aussi environ 100 milliards de recettes, surtout en taxant les gros patrimoines et les superprofits. « Ruiner la France », c'est un jugement : pour les uns, ces impôts feraient fuir les capitaux ; pour les autres, augmenter les salaires et les services publics renforce l'économie. C'est un désaccord de choix, pas un projet de faillite.",
 detaille="Le reproche s'appuie sur un fait : le programme porté par LFI au sein du Nouveau Front populaire en 2024 prévoyait des dépenses importantes. Ses auteurs l'ont chiffré, le 21 juin 2024, à environ 150 Md€ supplémentaires d'ici 2027, dont 25 Md€ de mesures d'urgence dès 2024 : abrogation des réformes des retraites et de l'assurance chômage, SMIC porté à 1 600 € net, hausse de 10 % du point d'indice des fonctionnaires. L'Institut Montaigne, think tank d'orientation libérale, l'a estimé à 179 Md€ par an, contre 71 Md€ pour le RN et environ 21 Md€ pour Ensemble.\n\nCes chiffres justifient un vrai débat : faisabilité dans le contexte de la dette publique, effets des hausses d'impôts sur l'investissement, respect des règles budgétaires européennes. Ce sont des objections sérieuses.\n\nMais le programme prévoyait aussi environ 100 Md€ de recettes nouvelles : rétablissement d'un ISF à composante climatique, taxation des superprofits, entre autres. Il s'agit donc d'un choix de redistribution, où l'on taxe davantage les plus aisés et les grandes entreprises pour financer salaires, retraites et services publics. Pour donner un ordre de grandeur, 150 Md€ correspondent à environ 9 % des dépenses publiques de 2024.\n\n« Vouloir ruiner la France » prête une intention ; la question honnête est : ce choix de répartition est-il soutenable, et à quelles conditions ?",
 empathie="Je comprends que les gros chiffres fassent peur, surtout avec la dette qu'on a. Moi aussi je me pose la question du financement. Mais je ne crois pas que ceux qui proposent ça veuillent couler le pays : ils pensent qu'on peut le financer autrement, en faisant payer ceux qui ont le plus. On peut en discuter sur les chiffres ?",
 objections=[
  "Le coût du programme est élevé selon tous les chiffrages, y compris celui de ses auteurs.",
  "Le rendement des nouvelles recettes (ISF, superprofits) est incertain et dépend des comportements des contribuables.",
  "Le contexte de dette publique élevée et les règles budgétaires européennes limitent les marges de manœuvre.",
 ],
 contre=[
  ("Les riches partiront tous.", "Le risque d'exil fiscal existe et fait l'objet d'études ; son ampleur est débattue. C'est un argument à discuter avec des chiffres, pas une certitude."),
  ("L'Institut Montaigne dit 179 milliards, pas 150.", "Les chiffrages divergent selon les hypothèses ; le think tank est d'orientation libérale et le NFP conteste sa méthode. Les deux montants sont des estimations."),
 ],
 questions=["Qui devrait payer en priorité, selon toi, pour financer les retraites et les services publics ?", "Quel chiffrage te semble le plus fiable, et pourquoi ?"],
 limites=["Les chiffrages portent sur le programme du NFP de 2024 ; le programme de LFI pour 2027 n'a pas été chiffré dans les sources consultées.", "Le calcul d'ordre de grandeur (≈ 9 % des dépenses publiques) rapporte un coût cumulé à un montant annuel : il est indicatif."],
 mots_cles=['mélenchon', 'lfi', 'nfp', 'ruiner', 'faillite', 'dette', 'coût', 'chiffrage', 'impôts', 'matraquage fiscal', 'programme', 'milliards'],
 rubriques=('melenchon-lfi',), volet='economie', sous_theme='Dette publique',
 verdict='opinion', fiabilite='debat', stabilite='evolutive',
))

# 8 ─────────────────────────────────────────────────────────────── irréalisable
FICHES.append(fiche(
 'programme-irrealisable', "Le programme de Mélenchon est irréalisable.",
 reproche="On qualifie le programme de LFI d'utopique : SMIC fortement augmenté, retraite à 60 ans, nouvelle Constitution, le tout jugé impossible à financer ou à mettre en œuvre.",
 resume="« Irréalisable » mélange deux questions. Certaines mesures sont techniquement simples à décider (hausse du SMIC, retour de l'âge de départ à 60 ans, rétablissement d'un impôt sur la fortune), mais coûteuses et contestées dans leurs effets. D'autres supposent des conditions politiques lourdes (Constituante, renégociation européenne). Le vrai débat porte sur le coût, le financement et les effets économiques, chiffrés de façon très différente selon les sources.",
 contexte="Le programme L'Avenir en commun (2022) prévoyait un SMIC à 1 400 € net et la retraite à 60 ans avec 40 annuités ; le Nouveau Front populaire, en 2024, proposait un SMIC à 1 600 € net et l'abrogation de la réforme des retraites.",
 explication="Une mesure est irréalisable si elle est juridiquement ou matériellement impossible. Une mesure coûteuse ou risquée est réalisable mais discutable. Distinguer les deux permet d'avoir un débat utile.",
 sources=['aec', 'nfp', 'montaigne'],
 faits=[
  fait("L'Avenir en commun (2022) propose un SMIC à 1 400 € net et la retraite à 60 ans avec 40 annuités de cotisation.", 'aec', '2022', 'Programme (source partisane)', "Ces mesures relèvent de décisions législatives ou réglementaires classiques."),
  fait("En 2024, le NFP chiffre ses mesures d'urgence à 25 Md€ pour 2024 et son programme à environ 150 Md€ d'ici 2027, avec environ 100 Md€ de recettes nouvelles.", 'nfp', 'Juin 2024', 'Chiffrage du NFP', "Les auteurs ont produit un chiffrage, contestable mais existant.", 'estimation'),
  fait("L'Institut Montaigne estime le coût annuel du programme du NFP à 179 Md€.", 'montaigne', 'Juillet 2024', 'Chiffrage indépendant (think tank libéral)', "L'écart entre chiffrages montre le poids des hypothèses.", 'estimation'),
 ],
 court="Augmenter le SMIC ou revenir à la retraite à 60 ans, techniquement, un gouvernement peut le décider : c'est déjà arrivé. La vraie question, c'est le coût et qui paie. Là-dessus, on peut débattre chiffres en main.",
 moyen="« Irréalisable », ça veut dire impossible. Or augmenter le SMIC, rétablir un impôt sur la fortune ou ramener l'âge de départ à 60 ans, ce sont des décisions qu'un gouvernement peut prendre ; la retraite à 60 ans a même existé. Ce qui se discute vraiment, c'est le coût et les effets : le NFP chiffrait son programme à 150 milliards d'ici 2027, l'Institut Montaigne à 179 milliards par an. On peut penser que c'est trop cher ou que ça pèsera sur l'emploi ; d'autres pensent que ça relancera la consommation. C'est un désaccord sur des choix et des hypothèses, pas une impossibilité.",
 detaille="Le reproche d'irréalisme recouvre en réalité plusieurs critiques.\n\nCertaines mesures sont simples à décider. Le programme L'Avenir en commun de 2022 prévoyait un SMIC à 1 400 € net et la retraite à 60 ans avec 40 annuités ; le Nouveau Front populaire, en 2024, un SMIC à 1 600 € net et l'abrogation de la réforme des retraites. Juridiquement, ce sont des décisions de loi ou de décret. La question n'est pas de savoir si on peut les prendre, mais ce qu'elles coûtent et ce qu'elles produisent.\n\nSur le coût, les chiffrages divergent : environ 150 Md€ d'ici 2027 selon le NFP, avec environ 100 Md€ de recettes nouvelles ; 179 Md€ par an selon l'Institut Montaigne. Ces écarts tiennent aux hypothèses (croissance, rendement des impôts, comportements des entreprises).\n\nD'autres propositions demandent des conditions politiques lourdes : une Assemblée constituante suppose un référendum gagné ; certaines mesures se heurtent aux règles européennes et supposent une négociation ou un conflit avec les partenaires.\n\nLe débat honnête porte donc sur trois points : le financement est-il crédible, les effets sur l'emploi et l'investissement sont-ils maîtrisés, et les conditions politiques sont-elles réunies ? Ce sont des objections réelles ; « irréalisable » les écrase en un mot.",
 empathie="Je comprends le doute : quand on entend « 60 ans » et « SMIC à 1 600 », ça paraît trop beau. Moi aussi je veux savoir comment on paie. Mais la retraite à 60 ans a existé en France : la question, c'est combien ça coûte et qui paie.",
 objections=[
  "Le coût est très élevé selon tous les chiffrages disponibles.",
  "Une hausse rapide du SMIC peut peser sur les petites entreprises ; l'ampleur de l'effet est débattue.",
  "Certaines mesures se heurtent aux règles budgétaires européennes, ce qui suppose un rapport de force incertain.",
 ],
 contre=[
  ("Aucun pays ne fait ça.", "Il faudrait examiner mesure par mesure : la comparaison internationale est utile, mais elle ne prouve pas l'impossibilité."),
  ("Le chiffrage est bidon.", "Tout chiffrage repose sur des hypothèses, y compris ceux des autres partis : il faut comparer les hypothèses plutôt que les rejeter en bloc."),
 ],
 questions=["Quelle mesure précise te semble impossible, et pourquoi ?", "Si c'était financé, est-ce que tu serais d'accord sur le principe ?"],
 limites=["Le programme 2027 de LFI n'a pas été consulté.", "Les effets économiques des mesures (emploi, croissance) ne sont pas évalués dans les sources retenues."],
 mots_cles=['mélenchon', 'lfi', 'programme', 'irréalisable', 'utopique', 'smic', 'retraite à 60 ans', 'chiffrage', 'avenir en commun', 'nfp'],
 rubriques=('melenchon-lfi',), sous_theme='Programmes électoraux',
 verdict='trompeur', fiabilite='debat', stabilite='evolutive',
))

# 9 ─────────────────────────────────────────────────────────────── contre la police
FICHES.append(fiche(
 'lfi-contre-police', "LFI est contre la police.",
 reproche="On reproche à LFI d'être hostile aux forces de l'ordre. Le reproche s'appuie sur la formule « La police tue » de Jean-Luc Mélenchon en juin 2022, et sur les accusations systématiques contre la police citées par le ministre de l'Intérieur en 2026.",
 resume="Le programme de LFI ne propose pas de supprimer la police : il propose une police de proximité, le démantèlement des BAC et le remplacement de l'IGPN par une autorité indépendante. Mais certaines déclarations, comme « La police tue » en 2022, généralisent et ont été vivement dénoncées ; en 2026, le ministre de l'Intérieur a cité des accusations systématiques contre la police pour justifier le classement de LFI à l'extrême gauche.",
 contexte="En juin 2022, à Paris, des policiers tirent sur une voiture qui refusait d'obtempérer, tuant une passagère. Jean-Luc Mélenchon réagit par « La police tue ». Le débat sur les violences policières et les refus d'obtempérer est récurrent depuis.",
 explication="Critiquer des pratiques policières ou demander un contrôle indépendant n'est pas être contre la police. Généraliser à toute l'institution des faits individuels est, en revanche, un raccourci critiquable.",
 sources=['aec', 'police', 'conseil_etat'],
 faits=[
  fait("Le programme L'Avenir en commun (2022) propose une police de proximité, le démantèlement des brigades anticriminalité (BAC) et le remplacement de l'IGPN par une institution indépendante.", 'aec', '2022', 'Programme (source partisane)', "Le programme réforme la police, il ne la supprime pas."),
  fait("En juin 2022, après des tirs policiers à Paris ayant tué une passagère, Jean-Luc Mélenchon déclare « La police tue » ; Gérald Darmanin dénonce des insultes ; Manuel Bompard affirme que LFI n'est pas opposée à la police.", 'police', 'Juin 2022', 'Paris', "Une formule générale qui a nourri le reproche."),
  fait("En 2026, le ministre de l'Intérieur justifie le classement de LFI à « l'extrême gauche » notamment par des accusations systématiques contre la police ; le Conseil d'État juge ce classement non manifestement erroné.", 'conseil_etat', 'Février 2026', 'Nuançage des municipales', "L'administration retient ce trait comme un marqueur politique.", 'etabli'),
 ],
 citations=[cit('Jean-Luc Mélenchon', 'La police tue', 'Juin 2022', 'Après des tirs policiers sur une voiture à Paris ayant tué une passagère.', 'police')],
 court="LFI ne propose pas de supprimer la police, mais de la réorganiser : police de proximité et contrôle indépendant. Dire « la police tue », par contre, c'est une généralisation que je trouve injuste pour les policiers qui font bien leur travail.",
 moyen="Le programme de LFI ne dit pas « moins de police » : il propose une police de proximité, la fin des BAC et un organisme indépendant pour contrôler les policiers, à la place de l'IGPN qui dépend du ministère. On peut être d'accord ou pas, mais c'est une réforme. Par contre, quand Mélenchon dit « La police tue » en 2022, il généralise à toute l'institution un drame précis, et ça a choqué, y compris des gens qui veulent qu'on enquête sur les violences policières. On peut demander que les bavures soient sanctionnées sans mettre tous les policiers dans le même sac.",
 detaille="Le reproche s'appuie sur des déclarations réelles. En juin 2022, après que des policiers ont tiré sur une voiture à Paris, tuant une passagère, Jean-Luc Mélenchon lance : « La police tue ». Gérald Darmanin dénonce des insultes ; Manuel Bompard répond que LFI n'est pas opposée à la police. En 2026, le ministre de l'Intérieur Laurent Nuñez cite des accusations systématiques contre la police parmi les raisons de classer LFI à « l'extrême gauche » pour les municipales.\n\nLe programme, lui, ne propose pas de supprimer les forces de l'ordre. L'Avenir en commun prévoit une police de proximité, le démantèlement des BAC, dont les méthodes sont critiquées, et le remplacement de l'IGPN, qui dépend du ministère, par une institution indépendante chargée d'enquêter sur les policiers. Ce sont des réformes discutables, mais ce sont des réformes.\n\nPour rester juste, il faut distinguer trois choses : la critique de pratiques précises, légitime dans une démocratie ; la demande de contrôle indépendant, qui existe dans d'autres pays ; et les formules qui généralisent un drame à toute l'institution, qui blessent les policiers et rendent le débat plus difficile.",
 empathie="Je comprends que ça te mette en colère : beaucoup de policiers font un travail dur et dangereux. Je pense aussi que « la police tue » est une formule injuste. Mais vouloir qu'un organisme indépendant enquête sur les bavures, c'est aussi protéger les policiers honnêtes.",
 objections=[
  "« La police tue » généralise à toute une institution des faits individuels.",
  "Démanteler les BAC sans alternative précise pourrait affaiblir la lutte contre certaines formes de délinquance ; c'est une objection de politique publique.",
  "Le ministre de l'Intérieur et le Conseil d'État ont retenu des accusations systématiques contre la police comme un marqueur politique.",
 ],
 contre=[
  ("Ils ne soutiennent jamais les policiers blessés.", "La fiche ne dispose pas de recensement des réactions de LFI à ce sujet ; il faudrait vérifier au cas par cas plutôt que généraliser."),
  ("Un contrôle indépendant, c'est de la défiance.", "C'est un débat : ses partisans y voient une garantie d'impartialité qui renforce la confiance envers la police."),
 ],
 questions=["Qui devrait enquêter sur une bavure : la police elle-même ou un organisme indépendant ?", "Peut-on soutenir la police et critiquer certaines pratiques en même temps ?"],
 limites=["La source sur « La police tue » est une chronique d'opinion ; seuls les faits qu'elle rapporte sont repris.", "Les positions de LFI sur la police après 2022 ne sont documentées ici que par les motifs du ministère en 2026."],
 mots_cles=['lfi', 'mélenchon', 'police', 'la police tue', 'policiers', 'violences policières', 'bac', 'igpn', 'refus d obtempérer', 'anti-flic'],
 rubriques=('melenchon-lfi',), volet='securite', sous_theme=None,
 verdict='trompeur', fiabilite='interpretation', stabilite='evolutive',
))

# 10 ─────────────────────────────────────────────────────────────── change d'avis
FICHES.append(fiche(
 'melenchon-change-avis', "Mélenchon change tout le temps d'avis.",
 reproche="On reproche à Jean-Luc Mélenchon des revirements : favorable au traité de Maastricht en 1992 puis opposant à la Constitution européenne en 2005, partisan de l'interdiction du voile à l'école en 2004 puis participant à la marche contre l'islamophobie en 2019.",
 resume="Les évolutions sont réelles et documentées : sénateur socialiste, il soutient Maastricht en 1992 comme « base solide » d'une constitution européenne, puis milite pour le « non » en 2005 et quitte le PS en 2008. Sur l'islam et la laïcité, il passe du rejet du mot « islamophobie » (2015) à la marche de 2019. Changer d'avis n'est pas un défaut en soi ; la question est de savoir si le changement est expliqué et cohérent, ce que ses critiques contestent.",
 contexte="Jean-Luc Mélenchon est en politique depuis les années 1970 : il a été sénateur socialiste, ministre délégué, puis fondateur du Parti de gauche et de LFI. Sur une si longue carrière, les évolutions sont inévitables ; ce sont leurs raisons qui font débat.",
 explication="Un changement de position peut traduire un apprentissage (on tire les leçons d'une expérience), une adaptation électorale, ou une incohérence. Seul l'examen de chaque cas permet de trancher.",
 sources=['ina92', 'tce2005', 'slate'],
 faits=[
  fait("Le 4 septembre 1992, le sénateur socialiste Jean-Luc Mélenchon soutient le traité de Maastricht comme « base solide » pour le début d'une constitution européenne.", 'ina92', '1992', 'Archive INA', "Un engagement européen documenté."),
  fait("En 2005, alors sénateur PS de l'Essonne, il fait partie des responsables « résolument hostiles » au traité constitutionnel européen, rejeté à 54,67 % le 29 mai 2005 ; il quitte le PS en 2008 pour fonder le Parti de gauche.", 'tce2005', '2005-2008', 'Référendum et rupture avec le PS', "Le revirement sur l'Europe est réel et coïncide avec sa rupture avec le PS."),
  fait("Sur la laïcité : soutien à l'interdiction du voile à l'école en 2004, rejet du terme « islamophobie » en 2015, participation à la marche contre l'islamophobie en 2019.", 'slate', '2004-2019', "Analyse d'un chercheur", "Une évolution que ses critiques jugent électoraliste et qu'il présente comme une réponse à la montée des discriminations.", 'interpretation'),
 ],
 citations=[],
 court="Il a changé d'avis sur certains sujets, c'est vrai, comme sur l'Europe entre 1992 et 2005. Mais changer d'avis après avoir vu les effets d'un traité, ce n'est pas forcément de l'opportunisme. Ce qui compte, c'est s'il explique pourquoi.",
 moyen="Oui, il a évolué. En 1992, il soutenait le traité de Maastricht ; en 2005, il a fait campagne pour le « non » à la Constitution européenne, et il a quitté le PS en 2008. Sur la laïcité, il refusait le mot « islamophobie » en 2015 et il a marché contre l'islamophobie en 2019. On peut lui reprocher certaines de ces évolutions, et ses critiques ne s'en privent pas. Mais changer d'avis n'est pas un défaut en soi : on attend même d'un responsable qu'il tire les leçons de l'expérience. La vraie question, c'est : explique-t-il ses changements, et sont-ils cohérents avec ses idées de fond ?",
 detaille="Le reproche repose sur des évolutions réelles.\n\nSur l'Europe, le sénateur socialiste Jean-Luc Mélenchon défend en septembre 1992 le traité de Maastricht, qu'il présente comme une « base solide » pour le début d'une constitution européenne. Treize ans plus tard, il fait partie des responsables socialistes « résolument hostiles » au traité constitutionnel européen, rejeté par 54,67 % des votants le 29 mai 2005. Cette rupture le conduit à quitter le PS en 2008 pour fonder le Parti de gauche.\n\nSur la laïcité et l'islam, il soutient l'interdiction du voile à l'école en 2004, rejette le terme « islamophobie » en 2015, puis participe à la marche contre l'islamophobie en 2019 et s'oppose à la loi « séparatisme » en 2021.\n\nCes évolutions peuvent être lues de plusieurs façons. Ses critiques y voient de l'opportunisme électoral, notamment sur la laïcité. Ses défenseurs y voient la cohérence d'un homme qui a jugé l'Europe sur ses résultats, ou qui a réagi à la montée des discriminations.\n\nLe critère honnête n'est pas « a-t-il changé ? » (presque tous les responsables à longue carrière l'ont fait), mais « explique-t-il ses changements ? » et « sont-ils cohérents avec ses principes déclarés ? ». Sur ces deux points, le débat reste ouvert.",
 empathie="C'est vrai que ça peut donner une impression de girouette. Moi, je préfère quelqu'un qui reconnaît s'être trompé sur un traité plutôt que quelqu'un qui ne change jamais d'avis quoi qu'il arrive. Mais tu as raison de demander des explications.",
 objections=[
  "Le revirement sur l'Europe est spectaculaire et coïncide avec une rupture politique, ce qui peut nourrir le soupçon d'opportunisme.",
  "Sur la laïcité, des observateurs voient une adaptation à un électorat ; c'est une interprétation défendue sérieusement.",
  "D'autres évolutions (stratégie d'alliances, positions internationales) pourraient être examinées et ne le sont pas ici.",
 ],
 contre=[
  ("Un vrai homme politique a des convictions qui ne bougent pas.", "Les principes peuvent rester stables pendant que l'analyse d'un traité ou d'une situation évolue avec les faits."),
  ("Il change selon ce qui rapporte des voix.", "C'est possible pour certains sujets ; il faut le démontrer cas par cas, en comparant les dates et les contextes."),
 ],
 questions=["Est-ce que tu préfères quelqu'un qui ne change jamais d'avis ou quelqu'un qui explique pourquoi il a changé ?", "Sur quel sujet précis son changement te semble incohérent ?"],
 limites=["La fiche examine deux domaines (Europe, laïcité) ; d'autres évolutions ne sont pas traitées.", "Les explications données par Mélenchon lui-même sur ses revirements n'ont pas été consultées dans des sources primaires."],
 mots_cles=['mélenchon', 'change d avis', 'girouette', 'revirement', 'maastricht', '2005', 'constitution européenne', 'europe', 'parti socialiste', 'opportuniste', 'islamophobie'],
 verdict='plutot_exact', fiabilite='etabli', stabilite='historique', a_actualiser='2028-10-29', raison="Fiche à dominante historique : relecture périodique.",
))

# 11 ─────────────────────────────────────────────────────────────── assistés vs travailleurs
FICHES.append(fiche(
 'gauche-assistes-travailleurs', "La gauche défend les assistés plutôt que les travailleurs.",
 reproche="On reproche à la gauche, et à LFI en particulier, de s'occuper des allocataires plutôt que de ceux qui travaillent. L'argument s'appuie sur la défense des minima sociaux et sur le fait qu'une partie des ouvriers vote pour le RN.",
 resume="Les principales mesures du programme de LFI visent les actifs : SMIC à 1 400 € net (2022) puis 1 600 € net (NFP 2024), retraite à 60 ans, hausse du point d'indice. Les minima sociaux pèsent 31,6 Md€ (2,0 % des dépenses publiques en 2023), et un tiers des foyers éligibles au RSA ne le demandent pas. Mais il est exact que LFI ne capte pas la majorité du vote ouvrier : au premier tour de 2022, 36 % des ouvriers ont voté Le Pen contre 23 % pour Mélenchon.",
 contexte="L'opposition entre « travailleurs » et « assistés » est au cœur de nombreux discours, à droite comme à l'extrême droite. Elle s'appuie sur le sentiment que le travail paie mal comparé aux aides, alors même que le SMIC rapporte bien plus que le RSA.",
 explication="Opposer travailleurs et allocataires suppose deux groupes séparés. En réalité, beaucoup de personnes passent de l'un à l'autre au cours de leur vie (chômage, maladie, retraite). Les mesures sur les salaires et les retraites concernent directement les actifs.",
 sources=['aec', 'nfp', 'drees_ms', 'drees_nr', 'ft', 'ipsos22'],
 faits=[
  fait("L'Avenir en commun (2022) propose un SMIC à 1 400 € net et la retraite à 60 ans ; le NFP (2024) un SMIC à 1 600 € net et une hausse de 10 % du point d'indice.", 'aec', '2022-2024', 'Programmes (source partisane)', "Les mesures phares visent les revenus du travail et les retraites."),
  fait("Le chiffrage du NFP place parmi les mesures d'urgence l'abrogation de la réforme des retraites, le SMIC à 1 600 € net et la hausse du point d'indice des fonctionnaires.", 'nfp', 'Juin 2024', 'Chiffrage du NFP', "Les priorités budgétaires portent sur les actifs et les retraités."),
  fait("Les minima sociaux représentent 31,6 Md€ en 2023, soit 2,0 % des dépenses publiques ; le RSA seul représente 12,2 Md€, soit 0,4 % du PIB.", 'drees_ms', '2023', 'Ensemble des minima sociaux', "La part des minima sociaux dans la dépense publique est faible.", 'etabli', '31,6 Md€ ; 2,0 %'),
  fait("Fin 2021, environ un tiers des foyers éligibles au RSA (33 % à 37 %, soit environ 561 000 foyers) ne le percevaient pas.", 'drees_nr', 'Fin 2021', 'France métropolitaine', "L'image d'allocataires profitant massivement du système est contredite par l'ampleur du non-recours.", 'estimation', '33 % à 37 %'),
  fait("En 2023, 83 % des contrôles de la recherche d'emploi clôturés par France Travail concluent à une recherche active ou à une remobilisation.", 'ft', '2023', '523 400 contrôles', "La plupart des demandeurs d'emploi contrôlés cherchent du travail."),
  fait("Au premier tour de la présidentielle 2022, 36 % des ouvriers votent Marine Le Pen et 23 % Jean-Luc Mélenchon ; parmi les personnes gagnant moins de 1 250 € par mois, 31 % et 28 %.", 'ipsos22', 'Avril 2022', 'Sondage Ipsos-Sopra Steria', "La gauche ne convainc pas la majorité des ouvriers : c'est un fait politique à prendre au sérieux.", 'estimation', '36 % / 23 %'),
 ],
 court="Le SMIC à 1 600 €, la retraite à 60 ans, le point d'indice : ce sont des mesures pour ceux qui travaillent. Les minima sociaux, c'est 2 % des dépenses publiques. Mais c'est vrai que beaucoup d'ouvriers votent RN : la gauche doit se demander pourquoi.",
 moyen="Regarde le programme : SMIC à 1 400 puis 1 600 € net, retraite à 60 ans, hausse du salaire des fonctionnaires. Ce sont des mesures pour les gens qui bossent. À côté, les minima sociaux, c'est environ 2 % des dépenses publiques, et un tiers des gens qui ont droit au RSA ne le demandent même pas. Et la plupart des chômeurs contrôlés cherchent vraiment du travail. Par contre, je te l'accorde, en 2022, 36 % des ouvriers ont voté Le Pen et 23 % Mélenchon. Si la gauche défend les travailleurs, elle a un problème pour le leur faire sentir, et ça mérite qu'on en parle.",
 detaille="Le reproche oppose deux groupes : ceux qui travaillent et ceux qui vivent des aides. Les données montrent que cette opposition est fragile.\n\nD'abord, les mesures phares de LFI visent les actifs : un SMIC à 1 400 € net dans le programme de 2022, à 1 600 € net dans celui du Nouveau Front populaire en 2024, la retraite à 60 ans, une hausse de 10 % du point d'indice des fonctionnaires. Ce sont des mesures pour les salariés et les futurs retraités.\n\nEnsuite, le poids des aides est souvent surestimé. En 2023, les minima sociaux représentent 31,6 Md€, soit 2,0 % des dépenses publiques ; le RSA seul, 0,4 % du PIB. Environ un tiers des foyers éligibles au RSA ne le demandent pas. Et en 2023, 83 % des contrôles de recherche d'emploi menés par France Travail ont conclu à une recherche active ou à une remobilisation.\n\nEnfin, la frontière entre « travailleurs » et « assistés » est poreuse : on peut être salarié, puis chômeur, puis malade, puis retraité. Les aides sont aussi une assurance pour ceux qui travaillent.\n\nMais le reproche touche un point réel : au premier tour de 2022, 36 % des ouvriers ont voté Marine Le Pen, contre 23 % pour Jean-Luc Mélenchon. Que la gauche défende les salaires ne suffit pas à convaincre une partie du monde du travail, qui peut se sentir oubliée. C'est une question politique sérieuse, que la gauche ne peut pas balayer.",
 empathie="Je comprends ce sentiment : quand on se lève tôt pour un salaire qui ne suffit pas, voir quelqu'un toucher des aides peut révolter. Mais le vrai problème, c'est que le travail paie trop peu. C'est justement pour ça que la gauche propose d'augmenter les salaires.",
 objections=[
  "Une majorité d'ouvriers ne vote pas pour LFI : le reproche traduit un ressenti réel du monde du travail.",
  "Le discours de la gauche peut donner l'impression de parler davantage des aides que du travail, même si son programme contient des mesures salariales.",
  "Le non-recours et les contrôles n'empêchent pas l'existence de fraudes, qui doivent aussi être combattues.",
 ],
 contre=[
  ("Avec le RSA, on gagne presque autant qu'en travaillant.", "Pour une personne seule, le SMIC net rapporte plus du double du RSA, avant même la prime d'activité (voir la fiche RSA et SMIC)."),
  ("Les ouvriers votent RN, c'est donc que la gauche les a trahis.", "C'est un débat important ; le vote dépend aussi d'autres enjeux (immigration, sécurité, sentiment d'abandon) qu'il faut aborder sans mépris."),
 ],
 questions=["Selon toi, qu'est-ce qui aiderait le plus quelqu'un qui travaille au SMIC ?", "Combien de personnes de ton entourage ont touché une aide à un moment de leur vie ?"],
 limites=["Les données de vote sont un sondage sortie des urnes de 2022 ; la marge d'erreur n'est pas précisée.", "Le non-recours est mesuré fin 2021 ; la réforme du RSA sous conditions d'activité n'est pas évaluée ici."],
 mots_cles=['gauche', 'assistés', 'assistanat', 'travailleurs', 'ouvriers', 'rsa', 'smic', 'minima sociaux', 'vote ouvrier', 'rn', 'lfi', 'mélenchon'],
 rubriques=('melenchon-lfi',), volet='social', sous_theme='Coût et efficacité des aides',
 verdict='trompeur', fiabilite='etabli', stabilite='evolutive',
))

if __name__ == '__main__':
    for f in FICHES:
        if f['sous_theme'] is None:
            f['sous_theme'] = 'Police et gendarmerie'
        with open(os.path.join(OUT, f['id'] + '.json'), 'w', encoding='utf-8') as fh:
            json.dump(f, fh, ensure_ascii=False, indent=2)
            fh.write('\n')
    print(len(FICHES), 'fiches écrites')
