# Rapport v8 — Refonte du moteur d'intelligence argumentative

## Ce qui change pour l'utilisateur

Quand on écrit une phrase (réponse express, questionnaire ou conversation), l'application ne cherche plus « la fiche qui contient les mêmes mots ». Elle analyse la phrase, puis :

- elle repère **le ou les arguments** qu'elle contient (une phrase peut en contenir plusieurs) ;
- pour chacun, elle retient **la fiche qui y répond vraiment**, ou elle dit clairement qu'aucune fiche ne répond (« lacune reconnue ») au lieu de proposer une fiche voisine ;
- elle affiche un panneau **« Ce que contient la phrase »** :
  - l'argument principal et les arguments secondaires ;
  - pour chaque argument secondaire, une réponse courte, une donnée sourcée et un lien vers sa fiche ;
  - le sous-entendu possible et le lien de cause affirmé ;
  - les émotions possibles, avec une réponse au ressenti ;
  - les procédés possibles, avec une explication, ce qu'il faut vérifier et une question ;
  - une phrase marquante adaptée au mode (« gagner » ou « convaincre ») ;
  - les fiches écartées, et pourquoi.
- En conversation, le changement de sujet passe par la même analyse. Les pronoms (« les juges **les** protègent ») sont rattachés au sujet de la conversation. Le ressenti est signalé sous la réponse, et une lacune est annoncée comme telle.

Tout fonctionne hors ligne, sans modèle d'IA : ce sont des règles explicites, consultables dans `public/js/cartographie.js`.

## Fonctionnement : les 9 couches

| Couche | Rôle |
|---|---|
| 1. Normalisation | minuscules, accents, apostrophes, ponctuation (fautes et langage familier inclus) |
| 2. Concepts | 38 concepts reconnus par 428 mots-clés, expressions, synonymes et fautes fréquentes |
| 3. Découpage | « et en plus », « mais », « alors que », « pendant ce temps », virgule suivie de « on/ils »… ; le sujet d'une proposition vaut pour les pronoms des suivantes |
| 4. Arguments | 37 arguments définis par des concepts requis, des concepts exclus et des formulations typiques ; un argument qui relie deux propositions (« On n'a plus de travail **mais** on fait venir des étrangers ») est reconnu |
| 5. Causes | « à cause de », « plus… moins », verbes de cause, juxtapositions qui suggèrent un lien |
| 6. Émotions | 9 émotions (peur, colère, injustice, déclassement, perte de repères, abandon, ressentiment, peur de l'avenir, défiance envers les institutions) |
| 7. Procédés | 12 procédés (généralisation, corrélation présentée comme une cause, amalgame, faux dilemme, appel à la peur, anecdote, comparaison entre périodes, charge de la preuve, homme de paille, autorité, attaque contre la personne, tension interne), toujours présentés comme des hypothèses |
| 8. Sélection documentaire | la fiche doit répondre à l'argument (liste explicite des fiches qui y répondent, départage par formulation) ; les fiches voisines sont écartées avec leur raison ; s'il n'y a pas de fiche, c'est une lacune |
| 9. Réponse | phrase marquante (sans chiffre), question, sous-entendus, éléments à vérifier ; la réponse détaillée reste celle du moteur de personnalisation (v5 à v7) |

## Démonstration : « Plus il y a d'immigrés, moins il y a de travail pour les Français. »

- **Avant (v7)** : `immigres-aides` (fiche sur les aides sociales). Les mots « immigrés » et « Français » suffisaient.
- **Après** :
  - concepts : Immigration et Emploi ;
  - cause affirmée : immigration → emploi (« plus… moins ») ;
  - argument : concurrence sur le marché du travail ;
  - fiche retenue : `immigration-emploi` ;
  - procédé possible : corrélation présentée comme une cause ;
  - question : « Comment sait-on que c'est la cause ? ».
- **Fiches écartées** :
  - `immigres-aides` : elle traite des prestations sociales et du coût, pas de l'emploi ;
  - `rsa-smic` : elle traite des salaires et des prestations, pas d'immigration ;
  - `rsa-profiteurs`, `chomeurs-travailler`, `impots-assistanat` : pour des raisons du même type.

Le détail calculé figure dans `rapports/tests-comprehension.md`.

## Fichiers

- `public/js/cartographie.js` (nouveau) : concepts, arguments, émotions, procédés et phrases marquantes.
- `public/js/analyse.js` (nouveau) : le moteur `analyserPhrase()`.
- `public/js/app.js` : la réponse express et le questionnaire passent par l'analyse ; ajout du panneau « Ce que contient la phrase » et d'une page « Pas encore dans la bibliothèque » plus explicite ; ressenti et lacunes affichés en conversation.
- `public/js/conversation.js` : la détection du changement de sujet passe par l'analyse et tient compte du contexte de la conversation.
- `public/css/styles.css` : styles du panneau, lisibles sur mobile.
- `scripts/fiches/immigration_emploi.py` : 3 fiches sourcées.
  - `immigration-emploi` ;
  - `immigration-salaires` ;
  - `chomage-penurie-recrutement`.
  - Sources : Insee, CEPII, Banque de France, thèse d'Anthony Edo (PSE), France Travail BMO 2025.
- `scripts/enrichir-fiches.js` (`npm run enrichir`) : il ajoute à chacune des 70 fiches `concepts`, `repond_a`, `ne_repond_pas` et `synonymes`. Au total : 182 rattachements à des concepts, 72 liens « répond à » et 20 exclusions explicites. Le script ne modifie aucun fait, aucune source et aucun argumentaire.
- Tests :
  - `tests/comprehension/phrases.js` : 180 phrases ;
  - `tests/comprehension/evaluer.js` ;
  - `tests/unit/comprehension.test.js` ;
  - un nouveau parcours e2e.
- `scripts/rapport-comprehension.js` (`npm run rapport:comprehension`) écrit `rapports/tests-comprehension.md`.

## Résultats des tests (exécutés)

- **Compréhension : 180 phrases.**
  - Chaque phrase définit l'argument principal attendu, la fiche attendue (ou l'absence de fiche), les arguments secondaires, les fiches à exclure, les émotions et les procédés.
  - **Nouveau moteur : 180/180.**
  - Ancienne correspondance par mots :
    - sur la bibliothèque v7 : 87/180 ;
    - sur la bibliothèque actuelle : 109/180.
  - 93 erreurs corrigées.
  - **Honnêteté sur ce score.** 148 phrases ont servi à régler le moteur. Les attentes ont été écrites avant les réglages, mais le moteur a ensuite été ajusté jusqu'à ce qu'elles passent. Pour mesurer la compréhension sur du neuf, j'ai écrit un **lot de validation de 32 phrases après les réglages**. Au premier passage, il a obtenu **28/32 (87,5 %)**. Les 4 échecs :
    - « Ces gens-là viennent juste pour les allocations » ;
    - « Mélenchon soutient les islamistes » ;
    - « Les insoumis, ce sont des extrémistes » ;
    - « Avant, au moins, il y avait du respect ».

    Ils ont ensuite été corrigés. **87 % sur des phrases inédites est l'estimation la plus réaliste de la compréhension.**
- **Tests unitaires** : 357/357. Ils comprennent les 180 phrases, les 166 scénarios de personnalisation, la conversation, les suggestions et la bibliothèque.
- **Tests de bout en bout** (navigateur) : 28/28. Le nouveau parcours vérifie trois cas :
  - l'emploi n'est pas confondu avec les aides ;
  - une phrase à deux arguments donne deux cartes sourcées ;
  - le logement est signalé comme lacune ;
  - le tout sans débordement sur mobile.

## Limites

- **Lacunes de la bibliothèque**, désormais signalées au lieu d'être masquées : logement (et immigration et logement), liberté d'expression (y compris sur l'islam), nostalgie, défiance envers les élus et corruption. Il faudrait des fiches sourcées sur ces sujets.
- **Méthode** : ce sont des règles, pas un modèle de langue. Une formulation très éloignée des motifs connus (ironie, double négation, sous-entendu sans mot-clé) peut ne pas être reconnue. Dans ce cas, le moteur retombe sur l'ancienne correspondance, et uniquement si elle est forte et couvre les concepts centraux de la phrase.
- **Lecture de la phrase** : les émotions et procédés sont des **hypothèses** (« peut-être »), jamais des diagnostics. Une origine supposée (« arabe ») est traitée comme une possible allusion à l'immigration, et l'amalgame est signalé.
- **Ce que l'analyse ne crée pas** : aucun chiffre. Les phrases marquantes n'en contiennent jamais, et les données viennent toujours des fiches avec leur source.
- **Mode connecté** : il reste inchangé (le serveur n'a pas de clé configurée sur l'hébergement statique). Le moteur d'analyse fonctionne côté navigateur.
