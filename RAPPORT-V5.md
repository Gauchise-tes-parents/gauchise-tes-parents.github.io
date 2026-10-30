# Rapport v5 — Audit et refonte du moteur de personnalisation

Date : 29 octobre 2026. Toutes les vérifications ci-dessous ont été **réellement exécutées** dans l’environnement de développement, sans clé API et sans réseau pour le mode autonome.

Documents liés :
- [`docs/MOTEUR-PERSONNALISATION.md`](docs/MOTEUR-PERSONNALISATION.md) : fonctionnement, table de décision complète, exemples imposés, référentiel scientifique (généré depuis le code par `npm run doc:moteur`).
- [`rapports/tests-personnalisation.md`](rapports/tests-personnalisation.md) : les 150 scénarios avec leurs résultats réels, les mesures de diversité et les exemples comparatifs (généré par `npm run rapport:personnalisation`).

---

## 1. Problèmes découverts

### Lors de l’audit initial (code v4)

| # | Problème | Conséquence |
|---|---|---|
| 1 | **15 options du questionnaire sans aucun effet** sur la réponse : confiance dans les institutions, les 4 options « rapport au changement », désabusé, peu informé, ouvert, ami, collègue, simple connaissance, tête-à-tête, repas de famille, riposter, corriger. | Options décoratives : l’utilisateur croyait personnaliser. |
| 2 | Deux effets prévus (`concret`, `correction`) calculés mais jamais utilisés. | Code mort. |
| 3 | Le **mode** (gagner / convaincre) ne changeait que l’onglet ouvert, pas le contenu. | Deux modes en apparence seulement. |
| 4 | **Structure de réponse identique pour tous les profils** : mêmes blocs dans le même ordre ; seules quelques phrases changeaient. | Différences superficielles. |
| 5 | Pas de niveau de connaissance, pas de profil « hésitant », pas de saisie des arguments déjà avancés. | Information utile impossible à donner. |
| 6 | Retours insuffisants : rien pour « statistiques truquées », « d’accord sur le constat mais pas les causes », « d’accord sur le problème mais pas la solution », « hésite » ; pas de texte libre. | Échanges successifs non couverts. |
| 7 | Pas de comparaison d’approches ; pas d’explication de la stratégie choisie. | Aucun moyen de comprendre ou contester le choix. |
| 8 | Volet et sous-thème ignorés pour départager les correspondances hors ligne. | Mauvaise fiche possible quand deux fiches sont proches. |
| 9 | Gestionnaire de profils prédéfinis (`PROFILS`) mort dans l’interface. | Code mort. |
| 10 | Formulaires de retour et de signalement qui échouaient sans serveur ; libellé « Revérifier en direct » trompeur hors ligne. | Fausses promesses en mode autonome. |
| 11 | Fiches scientifiques sans auteurs, année, conditions, limites ni niveau de confiance. | Référentiel incomplet. |

### Découverts par les nouveaux tests pendant la refonte (et corrigés)

| # | Problème | Comment il a été détecté |
|---|---|---|
| 12 | Ton par défaut du mode empathique « rappelle le lien avant le désaccord » même sans lien déclaré. | Lecture des exemples comparatifs du rapport, puis attente ajoutée. |
| 13 | La question de conclusion répétait une question déjà posée dans la même réponse. | Nouveau critère « aucun texte répété dans une même réponse ». |
| 14 | Une entrée « j’aimerais comprendre ton point de vue » suivie des faits avant les questions. | Exemples comparatifs, puis attente ajoutée. |
| 15 | **Correspondance abusive** : « Les extraterrestres contrôlent la Banque centrale » renvoyait à la fiche sur les chômeurs (un seul mot commun). | Scénario « question hors base ». |
| 16 | « Confrontation » + « méfiance » donnait 2 preuves alors que la confrontation en exige une. | Test de bout en bout. |
| 17 | L’ancienneté des données n’était plus affichée pour les fiches historiques dans l’argumentaire (régression de la refonte). | Test hors ligne (« mode avion »). |
| 18 | Réponse à « chiffres truqués » qui répétait la preuve deux fois à l’écran. | Captures d’écran sur mobile. |
| 19 | « Confrontation » et « hésitant » produisaient presque le même plan en mode débat (19 paires de profils ne différaient que sur une dimension). | Mesure de diversité. |
| 20 | Les nouvelles métadonnées scientifiques n’étaient pas affichées dans les fiches ; texte « Trois rubriques » alors qu’il y en a quatre. | Audit de l’interface. |

## 2. Corrections apportées

- **Nouveau moteur** (`public/js/composer.js`) : une table de décision exécutable (`EFFETS`) donne à chaque option des effets sur l’approche, le détail, le ton, le point d’entrée, la conclusion, le nombre et le type de preuves, la source mise en avant, l’objection, les questions et l’ordre des blocs. `planifier()` calcule un plan explicite et justifié, `blocs()` le rend. **Toutes les options ont un effet mesuré**, sauf « connaît un peu le sujet », neutre par conception et documentée comme telle.
- **Le mode change réellement le contenu** : ordre des blocs, entrée, conclusion, ton, nombre de questions, inflexion de l’approche.
- **Questionnaire progressif** : 10 dimensions (ajout du niveau de connaissance et de l’option « hésite »). Seules les 3 questions essentielles sont visibles. La « question qui changerait le plus la réponse » est calculée en simulant l’effet de chaque dimension sur le plan. Le reste est replié. L’option « Je ne connais pas assez cette personne » annule toutes les hypothèses. Les hypothèses sont affichées comme telles et corrigeables à tout moment, depuis l’argumentaire.
- **Arguments déjà avancés** : l’utilisateur les coche, et le moteur ne les repropose pas.
- **Dix retours**, en boutons ou en texte libre interprété localement par mots-clés. Pendant la discussion, le moteur garde en mémoire les faits présentés, les objections traitées et les questions posées : rien n’est répété. Quand tout a été dit, il le signale.
- **Comparaison de 2 ou 3 approches** : public visé, raison, preuves, risques, limites, questions. Scores qualitatifs seulement, aucune promesse de persuasion.
- **« Pourquoi cette stratégie »** : chaque choix est accompagné de sa raison et, le cas échéant, de sa fiche scientifique. Chaque consigne est marquée « recherche » ou « bonne pratique ».
- **Correspondance hors ligne** : départage par volet et sous-thème. Un seul mot commun dans une phrase de quatre mots ou plus ne suffit plus.
- **Référentiel scientifique** : 16 fiches, dont 2 nouvelles (communication non violente, polarisation de groupe). Chacune comporte une référence, des auteurs, une année, un lien, des conditions, des limites, un niveau de confiance et des notions. Ces informations sont affichées dans la fiche.
- Corrections 12 à 20 ci-dessus. Formulaires dépendant du serveur masqués en mode autonome. Libellés honnêtes.

## 3. Fichiers modifiés ou créés

| Fichier | Nature |
|---|---|
| `public/js/composer.js` | réécrit : moteur (EFFETS, planifier, blocs, comparerApproches, suite, interpreterRetour, questionsUtiles) |
| `public/js/profile.js` | réécrit : nettoyage, 36 consignes avec fondement, table DECISIONS |
| `public/js/taxonomy.js` | 10 dimensions, 10 retours |
| `public/js/app.js` | questionnaire progressif, vue argumentaire (blocs, hypothèses, déjà avancés, approches, pourquoi, retour libre), référentiel dans les fiches, ancienneté toujours affichée |
| `public/js/kbsearch.js` | seuil de correspondance plus strict |
| `public/css/styles.css` | styles v5 |
| `scripts/fiches/science_dialogue.py`, `data/library/sci-*.json` | 16 fiches scientifiques avec métadonnées |
| `tests/personnalisation/scenarios.js` | **nouveau** : 150 scénarios, 8 critères, diversité, paires témoins |
| `tests/unit/personnalisation.test.js` | **nouveau** : 11 tests (dont le « test des tests ») |
| `tests/unit/composer.test.js` | réécrit pour la nouvelle API |
| `tests/e2e/ui.test.js` | mis à jour ; nouveau test de bout en bout du moteur v5 |
| `scripts/rapport-personnalisation.js` | **nouveau** : exécute les scénarios et écrit le rapport |
| `scripts/doc-moteur.js` | **nouveau** : génère la documentation depuis le code |
| `docs/MOTEUR-PERSONNALISATION.md`, `rapports/tests-personnalisation.md` / `.json` | **nouveaux** (générés) |
| `README.md`, `package.json` (0.5.0, trois scripts npm) | mis à jour |

## 4. Fonctionnement du moteur (résumé)

Le profil est nettoyé, puis les effets de chaque option s’additionnent pour les approches et se résolvent par priorité pour l’entrée, le ton et la conclusion. Le plan est ensuite calculé : il choisit les preuves (score selon l’approche, les angles de valeur, le type de preuve demandé, le type de source, en excluant ce qui a déjà été dit), puis l’objection, les questions, la conclusion et l’ordre. Le rendu ne fait que **sélectionner et ordonner** du contenu vérifié. Les seuls textes ajoutés sont des formules de liaison sans fait. Même contexte → même réponse : il n’y a pas de hasard, donc pas de variété artificielle. La variété vient du contexte, des faits déjà utilisés et des fiches récemment consultées. Le détail complet et la table de décision option par option se trouvent dans `docs/MOTEUR-PERSONNALISATION.md`.

**Exemples imposés** (extraits de la documentation générée) :
- *Méfiance envers les médias et les institutions*, sur « Les impôts ne servent qu’à payer l’assistanat » :
  - la méthode (période, périmètre, organisme) est affichée pour chaque preuve ;
  - une preuve d’un autre organisme est ajoutée (Insee + DREES) ;
  - le moteur demande « Quelle source te paraîtrait fiable ? » ;
  - il prépare la réponse à « chiffres truqués ».

  Les données publiques ne sont pas écartées.
- *Repas de famille* :
  - en mode empathique : une proposition de pause (« Si ça monte… ») ;
  - en mode débat : le détail est réduit et l’entrée se fait par une question ;
  - avec « c’est un parent » en plus : ton chaleureux et conclusion « ça ne change rien entre nous ».

## 5. Sources scientifiques

Pour chaque notion, la fiche donne les conditions, les limites et le résumé (voir la documentation). Toutes les URL ont été consultées pendant la constitution des fiches (v4 et v5).

| Notion | Référence principale | Confiance |
|---|---|---|
| Réactance | Rains (2013), méta-analyse, *Human Communication Research* | élevée |
| Autonomie, autodétermination | Ryan et Deci (2000) | moyenne |
| Raisonnement motivé | Ditto et al. (2019) ; Kahan et al. | moyenne |
| Effet « retour de flamme » (rare) | Wood et Porter (2019) | élevée |
| Effets modestes de la persuasion | Kalla et Broockman (2020) | élevée |
| Identité sociale et politique | Tajfel et Turner ; synthèse Jetten (2025) | élevée |
| Valeurs morales (recadrage) | Feinberg et Willer (2015) | moyenne |
| Menace et orientation politique (non répliqué) | Bakker et al. (2020) | moyenne |
| Entretien motivationnel, écoute | Lundahl et al. (2010) ; Itzchakov et al. | moyenne |
| Dissonance cognitive | Harmon-Jones et Harmon-Jones (2007) | moyenne |
| Socialisation familiale | Jennings, Stoker et Bowers (2009) | élevée |
| Désinformation et confiance | Ecker et al. (2022) | élevée |
| Délibération | Fishkin (sondages délibératifs) ; synthèse encyclopédique | moyenne |
| Persuasion et manipulation | Noggle (2018), *Stanford Encyclopedia of Philosophy* | élevée |
| Communication non violente | Pereira et Durgante (2025), revue | **faible** |
| Polarisation de groupe | Strandberg, Himmelroos et Grönlund (2019) | moyenne |

Faiblesses à connaître :
- La fiche « délibération » s’appuie sur une synthèse encyclopédique, faute de source primaire consultable.
- Les preuves sur la communication non violente sont faibles, et la fiche le dit.
- Deux références envisagées (une méta-analyse sur la crédibilité des sources, des chiffres OCDE sur la confiance) n’ont pas pu être vérifiées. Elles n’ont donc **pas** été utilisées.

## 6. Les scénarios et leurs résultats réels

Exécution : `npm run rapport:personnalisation` (environ 0,8 s, sans réseau).

- **150 scénarios** :
  - 128 combinaisons fiche × profil, sur 16 fiches de 7 volets, avec 12 profils, des contextes privés et publics et 3 niveaux de connaissance, dans les deux modes ;
  - 8 échanges successifs, de 2 à 5 retours, avec objections, demandes de preuves, braquages, diversions, hésitations et concessions ;
  - 8 questions saisies librement, dont 2 hors base ;
  - 6 profils absents, invalides ou contradictoires.
- **150 / 150 conformes aux 8 critères** : choix transmis, stratégie conforme, sources cohérentes, pas de duplication, faits non altérés, incertitudes signalées, profil non confondu avec un fait, parcours non bloqué.
- **Erreurs factuelles : 0.** Stabilité factuelle : 543 preuves sur 543 identiques au texte de la fiche. La réponse courte est identique pour tous les profils d’une même fiche.
- **Sources manquantes : 0** preuve sans source consultée.
- **Diversité** : sur 896 paires de profils (même fiche, même mode), 896 diffèrent sur au moins deux dimensions de fond, et aucune n’est identique. Le chiffre était de 877 avant la correction n° 19. L’objection anticipée ne varie que dans 16 % des paires, faute de contre-arguments multiples dans les fiches. C’est une limite des données.
- **Paires témoins** (profils qui ne doivent PAS changer la réponse) : 6 sur 6 identiques. Exemples : parent et conjoint, ordre de saisie des valeurs, « je ne connais pas » plus d’autres options, champs personnels hors questionnaire.
- **Test des tests** : un fait modifié, un nombre ajouté, une source non consultée, un profil présenté comme un fait et une attente non respectée sont injectés volontairement. Chacun est détecté.

Limite de la mesure : les 12 profils de test ont été choisis contrastés, et la diversité est mesurée sur des dimensions structurelles. Elle **ne juge pas** la qualité rédactionnelle, et ces tests **ne valident pas** l’efficacité persuasive sur de vraies personnes.

## 7. Exemples comparatifs

Voir la section « Exemples comparatifs » du rapport de tests, qui reproduit le texte réellement produit pour :
- « Les impôts ne servent qu’à payer l’assistanat », selon trois profils : chiffres, méfiance, se braque ;
- « La délinquance augmente partout », selon trois situations : repas de famille avec un parent, provocation sur les réseaux, personne sensible à la sécurité.

Pour une même affirmation, les faits sont identiques. Ce qui change : l’approche, l’entrée, le nombre et le choix des preuves, la méthode affichée, l’ordre, les questions, le ton et la conclusion.

## 8. Tests de non-régression

| Suite | Commande | Résultat |
|---|---|---|
| Unitaires et intégration (dont 150 scénarios) | `npm test` | **123 / 123 réussis** |
| Navigateur (Playwright, Chromium) : téléphone 320 à 412 px, ordinateur, parcours, bibliothèque, fiches, argumentaire hors ligne, moteur v5, mode connecté sans serveur, service d’IA simulé, mode avion par service worker | `npm run test:e2e` | **24 / 24 réussis** |

Les tests v4 conservés couvrent notamment :
- le lien Tipeee exact ;
- l’absence de débordement horizontal ;
- l’absence d’erreur JavaScript ;
- l’intégrité de la base téléchargée ;
- la veille (règles, sauvegardes, retour arrière, jeton) ;
- la sécurité du serveur (pas de clé dans le code client, CSP).

## 9. Limites et ce qui reste à faire

- **Mode connecté non testé avec une vraie clé API.** La recherche web et la rédaction par IA ne sont testées qu’avec un service simulé. Le profil y est transmis sous forme de consignes (test unitaire), mais la qualité réelle des réponses générées n’a pas été évaluée.
- **Pas de validation empirique.** Aucune mesure de l’effet sur de vraies personnes. Les règles reposent sur des tendances moyennes, souvent modestes, et dépendantes du contexte.
- **La variété est bornée par les fiches.** Une fiche de trois faits ou d’un seul contre-argument limite les choix possibles. Le moteur ne compense pas en inventant.
- **Texte libre des retours** : l’interprétation par mots-clés peut se tromper. Les boutons restent disponibles.
- **Correspondance hors ligne** : le seuil est heuristique. Une question formulée très différemment d’une fiche peut ne pas être reconnue, ou être rattachée à un sujet voisin, signalé comme tel.
- **Pas de modèle d’IA local** : le mode autonome est un moteur de règles et ne reformule pas librement.
- Déploiement et veille automatique : inchangés depuis la v4. Rien n’est publié tant que le propriétaire n’a pas suivi `PUBLIER.md`.
