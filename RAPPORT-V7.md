# Rapport v7 — Suggestions spécialisées, immigration, délinquance et prisons

Date : 30 octobre 2026. Tous les résultats ci-dessous viennent de tests réellement exécutés, hors ligne, sans clé API.

## 1. Ce qui posait problème

Sur l'écran de saisie, chaque thématique proposait toujours les deux mêmes exemples, quel que soit le sous-thème, le mode ou l'interlocuteur (`exemples` dans `taxonomy.js`, 2 phrases par volet, 0 pour « Autre sujet »). La page « Réponse express » n'en proposait aucun.

## 2. Suggestions par sous-thème

- **Volume** : 127 sous-thèmes audités, c'est-à-dire tous ceux de la taxonomie. **764 suggestions** au total :
  - 6 par sous-thème pour 125 sous-thèmes ;
  - 7 pour « Immigration, délinquance et prisons » et pour « Expulsion des étrangers condamnés » ;
  - 7 suggestions générales pour « Autre sujet ».
- **Deux registres** : chaque suggestion est classée soit comme formulation tranchée (riposte, 384), soit comme inquiétude ou question sincère (dialogue, 380). Certaines sont aussi marquées « argument chiffré » ou « argument fondé sur le vécu ».
- **Sélection contextuelle** (`public/js/suggestions.js`, `suggestionsPour`) : trois suggestions sont visibles à chaque arrivée. Le choix tient compte :
  - du **mode** : riposte d'abord pour « Gagner le débat », dialogue d'abord pour « Convaincre » ;
  - du **cadre** : un public ou les réseaux favorisent la riposte ; un repas ou un proche favorisent le dialogue ;
  - de l'**interlocuteur** : chiffres, vécu, valeurs de sécurité ;
  - du **sous-thème**. Sans sous-thème choisi, les suggestions alternent entre les sous-thèmes du volet.
- **« Autres affirmations »** : le bouton renouvelle les suggestions sans répéter celles déjà vues. Quand la liste est épuisée, un nouveau cycle commence.
- **Où elles apparaissent** :
  - dans le parcours « Débat » ;
  - dans « Réponse express », où elles suivent le sujet choisi ;
  - hors ligne, car elles sont incluses dans l'application.
- **Fiche vérifiée** : une étiquette « fiche vérifiée » signale les suggestions pour lesquelles la bibliothèque contient une fiche correspondante.
  - Couverture réelle : **121** suggestions sur 764 ont une fiche correspondante, et 306 un sujet voisin.
  - Les autres reçoivent, hors ligne, le message honnête « pas encore dans la bibliothèque » ; le mode connecté peut chercher.
- **Ni citation, ni attribution** : les suggestions sont des formulations génériques fréquemment entendues. Elles ne sont attribuées à personne, et l'interface le précise.

**Validation automatique** (`auditSuggestions`, exécutée par `npm test`). Elle signale :
- tout sous-thème qui a moins de 5 suggestions ;
- tout sous-thème qui a moins de 2 suggestions par registre ;
- tout doublon, même entre deux rubriques ;
- tout quasi-doublon (indice de Jaccard ≥ 0,7 sur les mots pleins), c'est-à-dire une reformulation recyclée ;
- tout sous-thème absent de la taxonomie.

Résultat actuel : **aucun problème**. Un « test du test » vérifie que le validateur détecte bien un sous-thème insuffisant et un doublon.

## 3. Nouvelle rubrique « Immigration, délinquance et prisons » : 11 fiches

Les formulations demandées sont analysées **séparément**, une fiche chacune. Le générateur est `scripts/fiches/immigration_prisons.py`.

| Fiche | Affirmation | Verdict |
|---|---|---|
| `etrangers-prisons` | Les étrangers remplissent les prisons françaises. | trompeur |
| `immigres-prisons-surrepresentation` | Les immigrés représentent une part disproportionnée de la population carcérale. | invérifiable avec les statistiques publiées |
| `delinquance-principalement-immigration` | La délinquance est principalement liée à l'immigration. | contredit |
| `france-plus-sure-moins-immigres` | La France serait plus sûre si elle accueillait moins d'immigrés. | invérifiable (hypothèse causale débattue) |
| `statistiques-prouvent-insecurite-immigration` | Les statistiques de délinquance démontrent que l'immigration augmente l'insécurité. | trompeur |
| `expulser-tous-etrangers-condamnes` | Tous les étrangers condamnés devraient être expulsés. | opinion |
| `etranger-crime-plus-sa-place` | Un étranger qui commet un crime n'a plus sa place en France. | opinion |
| `expulser-reduit-criminalite` | Il suffit d'expulser les délinquants étrangers pour réduire la criminalité. | trompeur |
| `criminels-etrangers-proteges-justice` | Les criminels étrangers sont protégés par la justice française. | trompeur |
| `renvoyer-tous-deja-condamnes` | Il faut renvoyer tous les étrangers qui ont déjà été condamnés. | opinion |
| `perte-automatique-droit-sejour` | Une personne étrangère condamnée devrait automatiquement perdre son droit de séjour. | opinion |

« Les immigrés remplissent les prisons françaises » est rattachée à la fiche sur les immigrés, pas à celle sur les étrangers.

Chaque fiche comporte :
- une réponse courte, une explication accessible et un développement ;
- les sources et les limites des chiffres ;
- des contre-arguments avec leurs réponses ;
- les points légitimes à reconnaître ;
- des questions pour poursuivre ;
- une réponse avec empathie.

La réponse adaptée au profil de l'interlocuteur est produite par le moteur de personnalisation existant.

**Règles appliquées et testées :**
- Les chiffres de la statistique pénitentiaire et policière portent sur la **nationalité**. Ils ne sont jamais attribués aux « immigrés » ; un test le vérifie.
- La statistique exacte est reconnue : les étrangers représentent 24,2 % des détenus pour 8,8 % de la population. Les fiches expliquent ensuite ce que ce chiffre démontre et ce qu'il ne démontre pas : association ou causalité, mis en cause, condamnés ou détenus, détention provisoire, âge et sexe.
- Les garanties juridiques sont expliquées (fonction, portée, limites). Elles ne sont jamais présentées comme une impunité ; un test le vérifie.

**Sources intégrées** (toutes ouvertes et lues le 30 octobre 2026) :
- **Population carcérale** : réponse du ministère de la Justice à la question écrite n° 12283 (JO du 26 mai 2026). Au 1er avril 2026, 24,2 % des détenus sont étrangers ; la part est passée de 21 % en 2016 à 24,7 % au 1er janvier 2026 ; la réponse donne aussi le statut pénal et les nationalités.
- **Ensemble des détenus** : *Infos Rapides Justice* n° 42 (juillet 2026), avec la répartition entre prévenus et condamnés.
- **Étrangers et immigrés dans la population** : Insee Première n° 2076 (7 octobre 2025). En 2024, 6,0 millions d'étrangers (8,8 %) et 7,7 millions d'immigrés (11,3 %).
- **Personnes mises en cause** : Insee / SSMSI, « Auteurs selon la nationalité » et dossier « Sécurité et société » (décembre 2021). En 2019, les étrangers représentent 17,7 % des mis en cause, avec le détail par infraction et les avertissements méthodologiques.
- **Comparaison européenne** : Conseil de l'Europe, SPACE I 2024. La médiane européenne est de 16,0 % de détenus étrangers, avec une mise en garde sur la comparabilité.
- **Corrélation et causalité** : Bianchi, Buonanno et Pinotti, *Do immigrants cause crime?* (PSE, 2008 ; publié en 2012).
- **Droit en vigueur** : rapport d'étape de la commission des lois de l'Assemblée nationale sur la proposition de loi n° 265 (23 octobre 2024). Il décrit les articles L. 631-1 à L. 631-4 du CESEDA après la loi du 26 janvier 2024 (seuils de 3 et 5 ans) et mentionne la décision n° 2023-863 DC du Conseil constitutionnel ; il donne aussi les expulsions prononcées et exécutées en 2022 et 2023.
- **Interdiction du territoire français** : article 131-30 du Code pénal, dans une reproduction du texte en vigueur (source secondaire).
- **Exécution des mesures d'éloignement** : Cour des comptes, *La politique de lutte contre l'immigration irrégulière* (janvier 2024). Environ 10 % des OQTF sont exécutées ; le rapport traite aussi des laissez-passer consulaires, de la rétention et des coûts.
- **Distinctions entre mesures** : Public Sénat (2023), sur la différence entre OQTF, expulsion et ITF, avec un taux d'exécution de 6,9 % au premier semestre 2022 selon le Sénat.
- **Critères de la CEDH** : arrêt *Üner c. Pays-Bas* (18 octobre 2006), via une fiche de jurisprudence (source secondaire).
- **Contrôle de proportionnalité** : trois décisions du Conseil d'État du 9 juin 2026, via un commentaire d'avocat (source secondaire).

## 4. Rebonds de conversation, dans toute l'application

Le moteur reconnaît maintenant un **déplacement d'argument**, dans deux cas :
- l'interlocuteur écarte l'argument précédent (« peu importe les statistiques… », « on s'en fiche des chiffres… », « même si… ») et une autre fiche correspond à son nouvel argument ;
- ou bien son nouvel argument relève du même domaine (même sous-thème ou même rubrique).

Il procède alors ainsi :
1. Il identifie le changement (« Tu changes d'argument : on ne parle plus de X, mais de Y »).
2. Il bascule sur la fiche adaptée.
3. Il répond avec les éléments propres à ce sujet (juridiques, statistiques…).
4. Il propose une question pour poursuivre.
5. Il propose aussi de revenir au point précédent.

Le sujet initial reste conservé.

Cas testés :
- « Peu importe les statistiques, il faut tous les renvoyer chez eux » : passage des statistiques carcérales au droit de l'expulsion. La source suivante porte sur l'expulsion, plus sur les prisons.
- « Même si tous ne sont pas étrangers, les étrangers sont surreprésentés » : réponse spécifique sur la surreprésentation, les dénominateurs et les facteurs de confusion.
- « Pourquoi garder en France quelqu'un qui a commis un crime ? » : bascule vers la fiche sur la justice pénale et l'éloignement.
- Hors immigration : passage du RSA au chômage, et des impôts aux aides perçues par les immigrés.

Le moteur détecte aussi qu'un interlocuteur **répète son affirmation de départ** : c'est une insistance, pas une objection nouvelle.

Dans les deux modes, les faits et les sources restent identiques ; seule la formulation change.

## 5. Fichiers modifiés ou créés

| Fichier | Nature |
|---|---|
| `public/js/suggestions.js` | **nouveau** : bibliothèque, sélection contextuelle, audit |
| `public/js/app.js` | suggestions dans « Débat » et « Express », bouton « Autres affirmations », étiquette « fiche vérifiée » |
| `public/js/conversation.js` | détection des déplacements d'argument et de l'insistance, seuils de reconnaissance des objections plus stricts |
| `public/js/taxonomy.js` | sous-thèmes de l'immigration (17 au lieu de 13 : travail, aides sociales, asile, réfugiés et statuts, délinquance, prisons, expulsion…), rubrique `immigration-prisons` |
| `public/css/styles.css` | styles des suggestions |
| `scripts/fiches/immigration_prisons.py`, `data/library/*.json` | **11 nouvelles fiches** (la bibliothèque passe de 56 à 67 fiches) |
| `scripts/build-preview.js` | ajout du module de suggestions |
| `tests/unit/suggestions.test.js` | **nouveau** : 26 tests |
| `tests/unit/knowledge.test.js`, `tests/unit/conversation.test.js`, `tests/personnalisation/scenarios.js`, `tests/e2e/ui.test.js` | mis à jour ; nouveau test de bout en bout |

## 6. Tests réellement exécutés

| Suite | Résultat |
|---|---|
| `npm test` (unitaires, dont 166 scénarios de personnalisation et 26 nouveaux tests) | **170 / 170** |
| `npm run test:e2e` (navigateur Chromium, téléphone et ordinateur) | **27 / 27** |
| Scénarios de personnalisation (`npm run rapport:personnalisation`), avec deux nouvelles fiches | **166 / 166** conformes, 609 preuves identiques aux fiches |

Les 10 parcours demandés :
- **Parcours 1 à 6** (immigration et travail, aides sociales, asile, démographie, intégration, délinquance) : 3 suggestions distinctes et pertinentes dans chaque mode, contrôlées par mots-clés propres au sous-thème. Testé en unitaire, et dans le navigateur pour le travail et les prisons.
- **Parcours 7 et 8** (étrangers et population carcérale ; expulsion des étrangers condamnés) : les 11 formulations sont proposées, chacune mène à sa propre fiche, et aucune n'est traitée comme équivalente à une autre.
- **Parcours 9** (comparaison des modes) : pour chacun des 127 sous-thèmes, la sélection diffère entre « Gagner » et « Convaincre ».
- **Parcours 10** (passage des statistiques au droit) : testé en unitaire et dans le navigateur, avec plusieurs profils (chiffres, se braque, sécurité), les deux modes et sept rebondissements successifs, sans aucune répétition.

**Sources** : chaque source a été ouverte pendant la recherche. Il n'existe pas de test automatique d'accessibilité en ligne, car l'environnement de test n'a pas accès à Internet ; un lien peut donc devenir inaccessible plus tard sans qu'un test le signale.

## 7. Lacunes restantes

- **Couverture** : 84 % des suggestions n'ont pas de fiche dédiée. Elles sont signalées comme telles et ne reçoivent pas de réponse inventée. Pour les couvrir, il faudra écrire de nouvelles fiches, ce qui est un travail éditorial.
- **Données datées** :
  - les statistiques détaillées par nationalité des mis en cause datent de 2019 (dernière série publiée) ;
  - aucune statistique pénitentiaire régulière n'est publiée selon le statut d'immigré.
- **Sources secondaires** : quatre sources juridiques sont secondaires (article 131-30 du Code pénal reproduit hors de Légifrance, résumé de l'arrêt Üner, commentaire des décisions du Conseil d'État, synthèse de Public Sénat). Le texte du CESEDA en vigueur n'a pas pu être consulté directement sur Légifrance : il est décrit d'après un rapport de l'Assemblée nationale. Il faudra le vérifier lors de la prochaine actualisation.
- **Suggestions tirées de l'actualité** : en mode connecté, elles ne sont pas implémentées. Les suggestions viennent de la bibliothèque locale.
- **Reconnaissance des rebonds** : elle repose sur des mots-clés et sur la correspondance avec les fiches. Un rebond formulé de façon inhabituelle peut être lu comme un changement de sujet, auquel cas l'utilisateur peut basculer d'un clic, ou comme un nouvel argument.
