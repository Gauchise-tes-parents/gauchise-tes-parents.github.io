# Rapport de tests du moteur de personnalisation (mode autonome)

Généré le 2026-10-30 par `node scripts/rapport-personnalisation.js` — exécution réelle de 166 scénarios en 1931 ms, sans réseau ni clé API.

> **Ce que ces tests prouvent et ne prouvent pas.** Ils vérifient que le moteur transmet les choix, applique la table de décision, ne modifie aucun fait, cite des sources consultées, signale les incertitudes, ne présente pas un profil comme un fait et ne bloque jamais. Ils **ne mesurent pas** l’efficacité persuasive sur de vraies personnes : aucune validation empirique n’a été faite.

## Synthèse

| Indicateur | Résultat |
|---|---|
| Scénarios exécutés | 166 (profils 144, échanges successifs 8, questions libres 8, données facultatives ou invalides 6) |
| Scénarios conformes aux 8 critères | 166 / 166 |
| Erreurs factuelles | 0 |
| Sources manquantes ou non consultées | 0 scénario(s), 0 preuve(s) |
| Réponses insuffisamment adaptées (attente du profil non respectée) | 0 |
| Stabilité factuelle (preuves identiques au texte de la fiche) | 609 / 609 |
| Réponse courte identique pour tous les profils d’une même fiche | oui, pour les 18 fiches |
| Paires de profils comparées (même fiche, même mode) | 1008 |
| … différences pertinentes (≥ 2 dimensions de fond) | 1008 (100 %) |
| … différences superficielles (une seule dimension, ou ton/contexte seulement) | 0 (0 %) |
| … plans identiques | 0 |

Les pourcentages ci-dessus décrivent les sorties du logiciel, pas un effet sur des personnes.

## Les huit critères vérifiés pour chaque scénario

1. **Choix transmis** : le profil nettoyé arrive au moteur (options invalides ignorées, « je ne connais pas » prioritaire).
2. **Stratégie conforme** : attentes explicites par option (ex. confrontation → une preuve et ton ferme ; se braque → questions avant contre-argument dans les deux modes ; public → conclusion adressée au public ; repas → proposition de pause). Une attente n’est pas exigée quand une option concurrente plus prioritaire l’emporte (règle documentée).
3. **Sources cohérentes** : chaque preuve renvoie à la source de son fait, marquée comme consultée, avec la même URL.
4. **Pas de duplication** : dans les échanges successifs, aucun fait déjà présenté n’est repris après « elle écoute », aucune réponse n’est répétée à l’identique.
5. **Faits non altérés** : le texte des preuves est identique à la fiche ; aucun nombre absent de la fiche n’apparaît dans les blocs ; la réponse courte n’est jamais réécrite.
6. **Incertitudes signalées** : ancienneté des données (fiches non historiques), caractère débattu ou interprétatif, correspondance seulement partielle.
7. **Profil non confondu avec un fait** : aucun texte du type « elle est susceptible » ; les hypothèses sont présentées comme telles.
8. **Parcours non bloqué** : aucune exception, deux stratégies non vides, profils vides/invalides acceptés, question hors base → page « pas dans la base » sans contenu inventé.

Un « test des tests » (`tests/unit/personnalisation.test.js`) injecte volontairement un fait modifié, un nombre ajouté, une source non consultée, un profil présenté comme un fait et une attente non respectée : chacun est bien détecté.

## Diversité, dimension par dimension

Nombre de paires (sur 1008) dont le plan diffère sur chaque dimension :

| Dimension | Paires différentes |
|---|---|
| Structure (ordre des blocs) | 852 (85 %) |
| Choix des preuves | 779 (77 %) |
| Ordre des preuves | 779 (77 %) |
| Questions posées | 864 (86 %) |
| Niveau de détail (et méthode affichée) | 702 (70 %) |
| Stratégie (approche / entrée / conclusion) | 958 (95 %) |
| Objection anticipée | 184 (18 %) |
| Adaptation au contexte (ton, public, lien, pause, angles) | 900 (89 %) |

L’objection anticipée varie peu : la plupart des fiches n’en contiennent qu’une ou deux. C’est une limite des données, pas un défaut à masquer par de la variété artificielle.

## Cas où le profil ne permet pas de justifier plus de différence

Aucune fiche testée ne limite la sélection des preuves à moins de trois combinaisons.

Différences superficielles : aucune paire ne diffère sur une seule dimension. Lors d’une première exécution, 19 paires étaient dans ce cas (« confrontation » et « hésitant » en mode débat ; « neutre » et « méfiant » en mode empathique). Deux corrections ont suivi : la méthode affichée est désormais comptée comme une différence de fond, et le profil « hésitant » commence par demander ce qui le fait hésiter. **Attention :** les 12 profils de test ont été choisis pour être contrastés, et la mesure ne compte que des dimensions structurelles ; elle ne juge pas la qualité du texte.

**Profils qui ne justifient pas de différence** (paires témoins : le moteur doit produire une réponse strictement identique, sur 8 fiches et dans les deux modes) :

| Paire | Raison | Résultat |
|---|---|---|
| `{"debat":"calme"}` / `{"debat":"calme","connaissance":"moyenne"}` | connaissance « un peu » est la valeur par défaut | identique |
| `{"lien":"parent"}` / `{"lien":"conjoint"}` | deux proches : même consigne de lien | identique |
| `{"valeurs":["justice_sociale"]}` / `{"valeurs":["egalite"]}` | même angle de valeur (justice) | identique |
| `{"valeurs":["securite","ordre"]}` / `{"valeurs":["ordre","securite"]}` | ordre de saisie des valeurs | identique |
| `{"inconnu":true}` / `{"inconnu":true,"debat":"competitif","faits":"chiffres"}` | « je ne connais pas » annule les autres hypothèses | identique |
| `{"debat":"calme"}` / `{"debat":"calme","religion":"x","nom":"Jean"}` | champs hors questionnaire ignorés (aucune donnée personnelle) | identique |


Questions hors base (bibliothèque insuffisante) : « Le prix du pain au Moyen Âge », « Les extraterrestres contrôlent la Banque centrale » → l’application affiche « pas dans la base » et propose le mode connecté ou un signalement, sans réponse inventée.

## Exemples comparatifs

### Une affirmation, trois profils

Affirmation : « Les impôts ne servent qu'à payer l'assistanat. » (fiche `impots-assistanat`)

| Profil (hypothèse) | Approche | Entrée | Détail | Ton | Preuves (index) | Ordre (débat public) | Conclusion |
|---|---|---|---|---|---|---|---|
| chiffres — chiffres et statistiques · beaucoup | factuelle | fait | approfondi | assure | 0, 1, 2 | entree → replique → preuves → objection → developpement → conclusion | synthese |
| méfiance envers les institutions — se méfie des institutions | factuelle | fait | standard | assure | 0, 1, 3 | entree → replique → preuves → objection → developpement → conclusion | synthese |
| se braque — susceptible | valeurs | reformulation | standard | calme | 1, 3 | entree → question → replique → preuves → objection → conclusion | synthese |

**chiffres — mode « convaincre » (texte réellement produit)**

- Comment le dire : Ton bienveillant : montre que tu prends son avis au sérieux avant de donner le tien.
- Ouvrir la discussion : Avant de te répondre, j’aimerais comprendre ton point de vue.
- Comprendre avant de répondre : Qu'est-ce que tu mets derrière le mot « assistanat » : le RSA, les allocations familiales, les retraites ? / Si on supprimait totalement le RSA, quelle part des dépenses publiques économiserait-on ?
- Les faits, un par un : « Les dépenses publiques totales atteignaient 1 672 Md€ en 2024, soit 57 % du PIB. » (Insee) ; « La protection sociale représente 693 Md€ (41 % du total) ; les retraites en sont le principal moteur de hausse (+23 Md€ en un an). » (Insee) ; « La santé (261 Md€), les services généraux dont la charge de la dette (181 Md€, dont 60 Md€ d'intérêts), l'enseignement (149 Md€), la défense (54 Md€) et l'ordre et la sécurité publics (52 Md€) sont d'autres postes majeurs. » (Insee)
- À dire avec empathie : Je comprends qu'on ait envie de savoir où va son argent ; c'est normal quand on paie beaucoup. Mais quand on regarde, la plus grande part va aux retraites, à la santé et à l'école. Le RSA, c'est moins que les intérêts de la dette.
- Pour conclure : Quelles dépenses publiques utilises-tu toi-même au quotidien ?

**méfiance envers les institutions — mode « convaincre » (texte réellement produit)**

- Comment le dire : Ton bienveillant : montre que tu prends son avis au sérieux avant de donner le tien.
- Ouvrir la discussion : Avant de te répondre, j’aimerais comprendre ton point de vue.
- Comprendre avant de répondre : Quelle source te paraîtrait fiable pour vérifier ça ? / Qu'est-ce que tu mets derrière le mot « assistanat » : le RSA, les allocations familiales, les retraites ?
- Les faits, un par un : « La protection sociale représente 693 Md€ (41 % du total) ; les retraites en sont le principal moteur de hausse (+23 Md€ en un an). » (Insee) ; « Les minima sociaux représentent 31,6 Md€, soit 2,0 % des dépenses publiques ; le RSA seul représente 12,2 Md€, soit 0,4 % du PIB. » (DREES)
- À dire avec empathie : Je comprends qu'on ait envie de savoir où va son argent ; c'est normal quand on paie beaucoup. Mais quand on regarde, la plus grande part va aux retraites, à la santé et à l'école. Le RSA, c'est moins que les intérêts de la dette.
- Pour conclure : Si on supprimait totalement le RSA, quelle part des dépenses publiques économiserait-on ?

**se braque — mode « convaincre » (texte réellement produit)**

- Comment le dire : Ton calme : ralentis, reformule, ne coupe pas la parole.
- Comprendre avant de répondre : Qu'est-ce que tu mets derrière le mot « assistanat » : le RSA, les allocations familiales, les retraites ? / Si on supprimait totalement le RSA, quelle part des dépenses publiques économiserait-on ?
- Ouvrir la discussion : Si je te comprends bien, tu penses que « Les impôts ne servent qu'à payer l'assistanat. ». C’est une idée qu’on entend souvent, et elle part souvent d’une vraie préoccupation.
- Les faits, un par un : « La protection sociale représente 693 Md€ (41 % du total) ; les retraites en sont le principal moteur de hausse (+23 Md€ en un an). » (Insee) ; « Les minima sociaux représentent 31,6 Md€, soit 2,0 % des dépenses publiques ; le RSA seul représente 12,2 Md€, soit 0,4 % du PIB. » (DREES)
- À dire avec empathie : Je comprends qu'on ait envie de savoir où va son argent ; c'est normal quand on paie beaucoup. Mais quand on regarde, la plus grande part va aux retraites, à la santé et à l'école. Le RSA, c'est moins que les intérêts de la dette.
- Pour conclure : Quelles dépenses publiques utilises-tu toi-même au quotidien ?


### Repas de famille contre débat public

Affirmation : « La délinquance augmente partout. » (fiche `delinquance-partout`)

| Profil (hypothèse) | Approche | Entrée | Détail | Ton | Preuves (index) | Ordre (débat public) | Conclusion |
|---|---|---|---|---|---|---|---|
| repas de famille avec un parent — évite le conflit · parent · repas de famille | valeurs | question | bref | calme | 0 | entree → question → replique → preuves → conclusion | lien |
| provocation sur les réseaux — provocateur · réseaux sociaux | factuelle | cadre | bref | ferme | 0 | entree → recentrage → replique → preuves → conclusion | public |
| sensible à la sécurité — prudent · sécurité, ordre | valeurs | preoccupation | standard | assure | 2, 4 | entree → replique → preuves → objection → developpement → conclusion | petit_pas |

**repas de famille avec un parent — mode « convaincre » (texte réellement produit)**

- Comment le dire : Ton calme : ralentis, reformule, ne coupe pas la parole.
- Ouvrir la discussion : Avant de te répondre, j’aimerais comprendre ton point de vue.
- Comprendre avant de répondre : Tu parles de quel type de délinquance : vols, violences, arnaques, drogue ? / Est-ce que c'est pareil dans ta ville et dans une grande agglomération ?
- Les faits, un par un : « Plusieurs atteintes aux biens baissent en 2025 : cambriolages de logement -3 %, vols avec armes -8 %, vols de véhicules -9 %. » (SSMSI, ministère de l'Intérieur) ; « Le nombre de victimes d'homicide est stable : 975 victimes en 2025. » (SSMSI, ministère de l'Intérieur)
- À dire avec empathie : Je comprends que tu te sentes moins en sécurité ; ce sentiment est réel et il compte. Mais les chiffres montrent que tout n'augmente pas. Ça aide à cibler les vrais problèmes, comme les violences sexuelles ou le trafic de drogue.
- Pour conclure : Quoi qu’on en pense chacun, ça ne change rien entre nous.
- Si ça monte : On peut en reparler plus tard, tranquillement. Ce n’est pas grave de ne pas être d’accord ce soir.

**provocation sur les réseaux — mode « convaincre » (texte réellement produit)**

- Comment le dire : Ton ferme et posé : phrases courtes, pas de digression, pas d’attaque personnelle.
- Ouvrir la discussion : Je vais répondre sur le fond, une seule fois, pour ceux qui nous écoutent.
- S’il détourne le sujet : On parlait de ce point précis ; je te réponds volontiers sur l’autre sujet ensuite.
- La preuve : « Plusieurs atteintes aux biens baissent en 2025 : cambriolages de logement -3 %, vols avec armes -8 %, vols de véhicules -9 %. » (SSMSI, ministère de l'Intérieur)
- Comprendre avant de répondre : Tu parles de quel type de délinquance : vols, violences, arnaques, drogue ?
- À dire avec empathie : Je comprends que tu te sentes moins en sécurité ; ce sentiment est réel et il compte. Mais les chiffres montrent que tout n'augmente pas. Ça aide à cibler les vrais problèmes, comme les violences sexuelles ou le trafic de drogue.
- Pour conclure : Pour ceux qui nous écoutent : Ça dépend vraiment de quoi on parle. Source : SSMSI, ministère de l'Intérieur, 9 juillet 2026.

**sensible à la sécurité — mode « convaincre » (texte réellement produit)**

- Comment le dire : Ton bienveillant : montre que tu prends son avis au sérieux avant de donner le tien.
- Ouvrir la discussion : Ta préoccupation est légitime, et je la partage. Regardons ce qui marche vraiment.
- Partir de ce qui compte pour lui : Si ce qui compte pour toi, c’est la sécurité, la vraie question est : qu’est-ce qui protège concrètement ? Regardons ce que disent les faits.
- Les faits, un par un : « Les violences sexuelles enregistrées augmentent fortement : 132 100 victimes en 2025 (+8 %), plus du double de 2016. » (SSMSI, ministère de l'Intérieur) ; « La délinquance enregistrée est très inégalement répartie : le taux de vols violents sans arme est environ 29 fois plus élevé dans l'unité urbaine de Paris qu'en dehors des unités urbaines. » (SSMSI, ministère de l'Intérieur)
- Comprendre avant de répondre : Qu’est-ce qui compte le plus pour toi dans cette question ? / Tu parles de quel type de délinquance : vols, violences, arnaques, drogue ?
- À dire avec empathie : Je comprends que tu te sentes moins en sécurité ; ce sentiment est réel et il compte. Mais les chiffres montrent que tout n'augmente pas. Ça aide à cibler les vrais problèmes, comme les violences sexuelles ou le trafic de drogue.
- Pour conclure : Pas besoin de tout changer d’un coup : si on est d’accord sur ce premier point, c’est déjà beaucoup.


## Résultats de tous les scénarios

| # | Scénario | Type | Résultat (gagner · convaincre, ou parcours) | Critères |
|---|---|---|---|---|
| 1 | `impots-assistanat/neutre` | profil | factuelle/question · valeurs/question | 8/8 |
| 2 | `impots-assistanat/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 3 | `impots-assistanat/mefiant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 4 | `impots-assistanat/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 5 | `impots-assistanat/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 6 | `impots-assistanat/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 7 | `impots-assistanat/hesitant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 8 | `impots-assistanat/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 9 | `rsa-smic/neutre` | profil | factuelle/question · valeurs/question | 8/8 |
| 10 | `rsa-smic/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 11 | `rsa-smic/mefiant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 12 | `rsa-smic/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 13 | `rsa-smic/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 14 | `rsa-smic/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 15 | `rsa-smic/hesitant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 16 | `rsa-smic/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 17 | `chomeurs-travailler/neutre` | profil | factuelle/question · factuelle/question | 8/8 |
| 18 | `chomeurs-travailler/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 19 | `chomeurs-travailler/mefiant` | profil | factuelle/fait · factuelle/question | 8/8 |
| 20 | `chomeurs-travailler/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 21 | `chomeurs-travailler/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 22 | `chomeurs-travailler/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 23 | `chomeurs-travailler/hesitant` | profil | factuelle/fait · factuelle/question | 8/8 |
| 24 | `chomeurs-travailler/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 25 | `delinquance-partout/neutre` | profil | factuelle/question · factuelle/question | 8/8 |
| 26 | `delinquance-partout/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 27 | `delinquance-partout/mefiant` | profil | factuelle/fait · factuelle/question | 8/8 |
| 28 | `delinquance-partout/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 29 | `delinquance-partout/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 30 | `delinquance-partout/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 31 | `delinquance-partout/hesitant` | profil | factuelle/fait · factuelle/question | 8/8 |
| 32 | `delinquance-partout/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 33 | `justice-laxiste-prison/neutre` | profil | factuelle/question · valeurs/question | 8/8 |
| 34 | `justice-laxiste-prison/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 35 | `justice-laxiste-prison/mefiant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 36 | `justice-laxiste-prison/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 37 | `justice-laxiste-prison/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 38 | `justice-laxiste-prison/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 39 | `justice-laxiste-prison/hesitant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 40 | `justice-laxiste-prison/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 41 | `immigration-chiffres-definitions/neutre` | profil | factuelle/question · factuelle/question | 8/8 |
| 42 | `immigration-chiffres-definitions/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 43 | `immigration-chiffres-definitions/mefiant` | profil | factuelle/fait · factuelle/question | 8/8 |
| 44 | `immigration-chiffres-definitions/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 45 | `immigration-chiffres-definitions/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 46 | `immigration-chiffres-definitions/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 47 | `immigration-chiffres-definitions/hesitant` | profil | factuelle/fait · factuelle/question | 8/8 |
| 48 | `immigration-chiffres-definitions/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 49 | `immigres-aides/neutre` | profil | factuelle/question · valeurs/question | 8/8 |
| 50 | `immigres-aides/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 51 | `immigres-aides/mefiant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 52 | `immigres-aides/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 53 | `immigres-aides/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 54 | `immigres-aides/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 55 | `immigres-aides/hesitant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 56 | `immigres-aides/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 57 | `electricite-nucleaire-renouvelables/neutre` | profil | factuelle/question · factuelle/question | 8/8 |
| 58 | `electricite-nucleaire-renouvelables/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 59 | `electricite-nucleaire-renouvelables/mefiant` | profil | factuelle/fait · factuelle/question | 8/8 |
| 60 | `electricite-nucleaire-renouvelables/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 61 | `electricite-nucleaire-renouvelables/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 62 | `electricite-nucleaire-renouvelables/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 63 | `electricite-nucleaire-renouvelables/hesitant` | profil | factuelle/fait · factuelle/question | 8/8 |
| 64 | `electricite-nucleaire-renouvelables/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 65 | `dividendes-salaires/neutre` | profil | factuelle/question · valeurs/question | 8/8 |
| 66 | `dividendes-salaires/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 67 | `dividendes-salaires/mefiant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 68 | `dividendes-salaires/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 69 | `dividendes-salaires/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 70 | `dividendes-salaires/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 71 | `dividendes-salaires/hesitant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 72 | `dividendes-salaires/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 73 | `securite-sociale-1945/neutre` | profil | historique/question · historique/question | 8/8 |
| 74 | `securite-sociale-1945/chiffres` | profil | historique/fait · historique/question | 8/8 |
| 75 | `securite-sociale-1945/mefiant` | profil | historique/fait · historique/question | 8/8 |
| 76 | `securite-sociale-1945/braque` | profil | historique/reformulation · historique/reformulation | 8/8 |
| 77 | `securite-sociale-1945/confrontation` | profil | historique/fait · historique/fait | 8/8 |
| 78 | `securite-sociale-1945/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 79 | `securite-sociale-1945/hesitant` | profil | historique/fait · historique/question | 8/8 |
| 80 | `securite-sociale-1945/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 81 | `front-populaire-1936/neutre` | profil | historique/question · historique/question | 8/8 |
| 82 | `front-populaire-1936/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 83 | `front-populaire-1936/mefiant` | profil | historique/fait · historique/question | 8/8 |
| 84 | `front-populaire-1936/braque` | profil | historique/reformulation · valeurs/reformulation | 8/8 |
| 85 | `front-populaire-1936/confrontation` | profil | historique/fait · historique/fait | 8/8 |
| 86 | `front-populaire-1936/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 87 | `front-populaire-1936/hesitant` | profil | historique/fait · historique/question | 8/8 |
| 88 | `front-populaire-1936/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 89 | `laicite-loi-1905/neutre` | profil | valeurs/question · valeurs/question | 8/8 |
| 90 | `laicite-loi-1905/chiffres` | profil | valeurs/fait · valeurs/question | 8/8 |
| 91 | `laicite-loi-1905/mefiant` | profil | valeurs/fait · valeurs/question | 8/8 |
| 92 | `laicite-loi-1905/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 93 | `laicite-loi-1905/confrontation` | profil | valeurs/fait · valeurs/fait | 8/8 |
| 94 | `laicite-loi-1905/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 95 | `laicite-loi-1905/hesitant` | profil | valeurs/fait · valeurs/question | 8/8 |
| 96 | `laicite-loi-1905/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 97 | `lfi-antisemite/neutre` | profil | factuelle/question · valeurs/question | 8/8 |
| 98 | `lfi-antisemite/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 99 | `lfi-antisemite/mefiant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 100 | `lfi-antisemite/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 101 | `lfi-antisemite/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 102 | `lfi-antisemite/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 103 | `lfi-antisemite/hesitant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 104 | `lfi-antisemite/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 105 | `melenchon-crie/neutre` | profil | valeurs/question · valeurs/question | 8/8 |
| 106 | `melenchon-crie/chiffres` | profil | valeurs/fait · valeurs/question | 8/8 |
| 107 | `melenchon-crie/mefiant` | profil | valeurs/fait · valeurs/question | 8/8 |
| 108 | `melenchon-crie/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 109 | `melenchon-crie/confrontation` | profil | valeurs/fait · valeurs/fait | 8/8 |
| 110 | `melenchon-crie/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 111 | `melenchon-crie/hesitant` | profil | valeurs/fait · valeurs/question | 8/8 |
| 112 | `melenchon-crie/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 113 | `gauche-laicite-debats/neutre` | profil | historique/question · historique/question | 8/8 |
| 114 | `gauche-laicite-debats/chiffres` | profil | historique/fait · historique/question | 8/8 |
| 115 | `gauche-laicite-debats/mefiant` | profil | historique/fait · historique/question | 8/8 |
| 116 | `gauche-laicite-debats/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 117 | `gauche-laicite-debats/confrontation` | profil | historique/fait · historique/fait | 8/8 |
| 118 | `gauche-laicite-debats/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 119 | `gauche-laicite-debats/hesitant` | profil | historique/fait · historique/question | 8/8 |
| 120 | `gauche-laicite-debats/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 121 | `commune-paris-1871/neutre` | profil | historique/question · historique/question | 8/8 |
| 122 | `commune-paris-1871/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 123 | `commune-paris-1871/mefiant` | profil | historique/fait · historique/question | 8/8 |
| 124 | `commune-paris-1871/braque` | profil | historique/reformulation · historique/reformulation | 8/8 |
| 125 | `commune-paris-1871/confrontation` | profil | historique/fait · historique/fait | 8/8 |
| 126 | `commune-paris-1871/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 127 | `commune-paris-1871/hesitant` | profil | historique/fait · historique/question | 8/8 |
| 128 | `commune-paris-1871/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 129 | `etrangers-prisons/neutre` | profil | factuelle/question · valeurs/question | 8/8 |
| 130 | `etrangers-prisons/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 131 | `etrangers-prisons/mefiant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 132 | `etrangers-prisons/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 133 | `etrangers-prisons/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 134 | `etrangers-prisons/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 135 | `etrangers-prisons/hesitant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 136 | `etrangers-prisons/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 137 | `expulser-tous-etrangers-condamnes/neutre` | profil | factuelle/question · valeurs/question | 8/8 |
| 138 | `expulser-tous-etrangers-condamnes/chiffres` | profil | factuelle/fait · factuelle/question | 8/8 |
| 139 | `expulser-tous-etrangers-condamnes/mefiant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 140 | `expulser-tous-etrangers-condamnes/braque` | profil | valeurs/reformulation · valeurs/reformulation | 8/8 |
| 141 | `expulser-tous-etrangers-condamnes/confrontation` | profil | factuelle/fait · factuelle/fait | 8/8 |
| 142 | `expulser-tous-etrangers-condamnes/vecu` | profil | valeurs/vecu · valeurs/vecu | 8/8 |
| 143 | `expulser-tous-etrangers-condamnes/hesitant` | profil | factuelle/fait · valeurs/question | 8/8 |
| 144 | `expulser-tous-etrangers-condamnes/patriote` | profil | historique/concession · historique/concession | 8/8 |
| 145 | `impots-assistanat/mefiant/truquees+preuves+ecoute+ecoute` | echange | Elle doute des chiffres : explique leur fabrication → Elle demande une source : montre-la, avec la méthode → Elle écoute : un élément de plus, pas dix → Elle écoute : un élément de plus, pas dix | 8/8 |
| 146 | `rsa-smic/braque/braque+braque` | echange | Elle s’est braquée : on ralentit → Elle se braque encore : propose une pause | 8/8 |
| 147 | `delinquance-partout/securitaire/causes+solution+concede` | echange | D’accord sur le constat, pas sur les causes → D’accord sur le problème, pas sur la solution → Elle a reconnu un point : consolide sans triompher | 8/8 |
| 148 | `chomeurs-travailler/confrontation/preuves+diversion+diversion` | echange | Elle demande une source : montre-la, avec la méthode → Elle a changé de sujet → Elle change encore de sujet | 8/8 |
| 149 | `lfi-antisemite/patriote/hesite+ecoute+fin` | echange | Elle hésite : propose des pistes, pas une conclusion → Elle écoute : un élément de plus, pas dix → La discussion est terminée | 8/8 |
| 150 | `electricite-nucleaire-renouvelables/chiffres/ecoute+ecoute+ecoute+ecoute+ecoute` | echange | Elle écoute : un élément de plus, pas dix → Elle écoute : un élément de plus, pas dix → Elle écoute : un élément de plus, pas dix → Elle écoute : un élément de plus, pas dix → Tous les faits de la fiche ont été présentés | 8/8 |
| 151 | `immigres-aides/vecu/truquees+causes+concede+fin` | echange | Elle doute des chiffres : explique leur fabrication → D’accord sur le constat, pas sur les causes → Elle a reconnu un point : consolide sans triompher → La discussion est terminée | 8/8 |
| 152 | `securite-sociale-1945/parent_repas/braque+hesite` | echange | Elle s’est braquée : on ralentit → Elle hésite : propose des pistes, pas une conclusion | 8/8 |
| 153 | `question:Les impôts servent à payer les assistés` | question | impots-assistanat (forte) | 8/8 |
| 154 | `question:la police tue` | question | lfi-contre-police (forte) | 8/8 |
| 155 | `question:Avec le RSA on gagne autant qu’en bossant` | question | rsa-smic (forte) | 8/8 |
| 156 | `question:Mélenchon gueule tout le temps` | question | melenchon-crie (forte) | 8/8 |
| 157 | `question:Le prix du pain au Moyen Âge` | question | non couvert | 8/8 |
| 158 | `question:Les extraterrestres contrôlent la Banque centrale` | question | non couvert | 8/8 |
| 159 | `question:La laïcité interdit les signes religieux dans la rue` | question | laicite-loi-1905 (forte) | 8/8 |
| 160 | `question:Les chômeurs profitent du système` | question | chomeurs-travailler (partielle) | 8/8 |
| 161 | `facultatif-0` | facultatif | factuelle/question · valeurs/question | 8/8 |
| 162 | `facultatif-1` | facultatif | factuelle/question · valeurs/question | 8/8 |
| 163 | `facultatif-2` | facultatif | valeurs/preoccupation · valeurs/preoccupation | 8/8 |
| 164 | `facultatif-3` | facultatif | factuelle/question · factuelle/question | 8/8 |
| 165 | `facultatif-4` | facultatif | factuelle/question · valeurs/question | 8/8 |
| 166 | `facultatif-5` | facultatif | factuelle/fait · factuelle/question | 8/8 |

## Ce qui reste à tester

- **Mode connecté** (recherche web et rédaction par un service d’IA) : testé uniquement avec un service simulé dans les tests de bout en bout ; aucun test avec une vraie clé API n’a été exécuté dans cet environnement.
- **Effet réel sur des personnes** : non mesuré. Les règles s’appuient sur des travaux publiés (voir docs/MOTEUR-PERSONNALISATION.md) dont les effets sont modestes et dépendants du contexte.
