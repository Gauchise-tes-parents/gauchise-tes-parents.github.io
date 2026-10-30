# Rapport v9 — La réponse avant la méthode

## Le problème constaté et ses causes réelles (code inspecté)

Testé en mode express avec « On ne peut pas aider tout le monde. » (mode « Gagner le débat »), la v8 affichait :
- comme fiche utilisée, « Pour aider quelqu'un à changer, il faut le confronter à ses contradictions » (sujet voisin) ;
- comme premier bloc, « Pour commencer : Avant de te répondre, j'aimerais comprendre ton point de vue », suivi de « Une question d'abord : Qu'est-ce qui t'amène à penser ça ? » ;
- comme réponse courte, un conseil d'écoute ;
- comme preuves, deux études sur l'entretien motivationnel.

J'ai trouvé trois causes, toutes corrigées :

1. **Mauvaise sélection en mode express** (`public/js/app.js`, `launchLocal`).
   - Le volet par défaut de l'express (« autre ») faisait entrer les fiches de *science du dialogue* (comment parler) parmi les réponses possibles. Le mot « aider » suffisait à faire remonter une fiche de méthode.
   - Une correspondance faible (« sujet voisin ») était acceptée comme réponse.
2. **Méthode imposée en mode « gagner »** (`public/js/composer.js`, `planifier`). Pour un interlocuteur inconnu, le planificateur ajoutait « Qu'est-ce qui t'amène à penser ça ? » et choisissait une entrée par question ouverte, même en mode « gagner ».
3. **Ordre d'affichage** (`composer.js`, `blocs` ; `app.js`, `viewArgumentaire`).
   - Chaque argumentaire commençait par « Comment le dire », puis « Pour commencer ».
   - La page affichait avant la réponse l'analyse, les avertissements, « L'argument d'en face » et une ligne « Stratégie ».

Le mode connecté (avec IA) n'est pas actif sur le site public. Ce sont donc bien ces trois couches qui produisaient la réponse.

## Modifications

- **Sélection.**
  - Les fiches de science du dialogue ne servent plus jamais de réponse à une affirmation.
  - Si aucun argument n'est reconnu, seule une correspondance forte est acceptée. Sinon, la page le dit et demande de préciser le sujet (question de clarification, uniquement dans ce cas).
- **Ordre unique en 4 parties, dans les deux modes** (`blocs`) :
  1. **La réponse** : « Ce que tu peux répondre », puis « Les arguments solides ».
  2. **Les preuves** : chaque preuve avec sa source et une ligne « Ce que ça montre ».
  3. **Comment présenter l'argument.**
  4. **Comment aborder la discussion** : ton et conseils, toujours en dernier.
- **Mode « Gagner le débat »** (partie 3) :
  - « La riposte qui fait réfléchir » (formule propre à l'argument) et « La question qui met le raisonnement à l'épreuve » ;
  - jusqu'à deux objections (« S'il te répond ceci ») ;
  - une entrée par le fond (fait, correction, cadre ou concession), jamais par une écoute de principe ;
  - en partie 4, « Pour ne pas te disperser » ;
  - aucun bloc d'empathie.
- **Mode « Convaincre avec empathie »** : les mêmes faits et les mêmes sources en parties 1 et 2, puis :
  - « Pour l'introduire sans braquer » et les questions pour comprendre son point de vue ;
  - « Ce qu'il faut reconnaître » ;
  - « La même réponse, dite avec empathie ».
- **Page de résultat** :
  - la réponse vient juste après la phrase saisie ;
  - l'analyse, les avertissements, la version solide de l'argument adverse et la stratégie passent dessous.
- **Accueil** : le mode choisi est visible et modifiable dans la réponse express. Avant, il était caché et hérité de la dernière visite.
- **4 nouvelles fiches sourcées**, avec les arguments correspondants dans la cartographie :
  - `aider-tout-le-monde`. Sources : Insee, *France, portrait social* 2025 « Redistribution monétaire » ; Observatoire des inégalités d'après la DREES ; DREES pour les minima sociaux et le non-recours ; Insee pour la pauvreté 2024.
  - `services-publics-moyens`. Sources : Insee Première n° 2054 et n° 2093 ; rapport du Sénat n° 153 (2024).
  - `gauche-augmenter-impots`. Sources : Public Sénat (deux articles de juin 2024) et la simulation de l'iFRAP (juillet 2024), opposée au programme. L'évaluation de France Stratégie est aussi citée.
  - `riches-creent-emplois`. Sources : Insee, catégories d'entreprises (2021), et compte rendu de l'évaluation de France Stratégie (2023) sur la réforme de l'ISF et la flat tax.
- **Formules marquantes** ajoutées pour 14 arguments qui n'en avaient pas (solidarité, services publics, gauche et impôts, riches et emplois, assistanat, etc.).

## Avant / après (mode « Gagner le débat », capturé dans le navigateur sur le code v8 puis v9)

| Affirmation | Avant (v8) : fiche et premier bloc | Après (v9) : fiche et premier bloc « Ce que tu peux répondre » |
|---|---|---|
| On ne peut pas aider tout le monde. | Fiche de méthode sur l'entretien motivationnel ; « Avant de te répondre, j'aimerais comprendre ton point de vue. » | `aider-tout-le-monde` : « Personne ne propose d'aider tout le monde sans limite : les aides sont déjà sous conditions et budgétées. Et elles marchent : sans elles, 21 % de la population serait pauvre, contre 14 % (DREES, 2022)… » |
| Les immigrés prennent le travail des Français. | Bonne fiche, mais « Avant de te répondre, j'aimerais comprendre… » | « Le travail n'est pas un gâteau fixe. Les immigrés sont moins souvent en emploi que les autres (62,4 % contre 71,4 %)… » |
| Les Français ne veulent plus travailler. | « Avant de te répondre… » | « France Travail contrôle des centaines de milliers de chômeurs chaque année. En 2023, plus de 8 contrôles sur 10… » |
| Les riches créent les emplois. | Fiche voisine (salaires et dividendes) ; « Avant de te répondre… » | `riches-creent-emplois` : « Les emplois, ce sont les entreprises qui les créent quand elles ont des clients… » |
| La gauche veut augmenter tous les impôts. | Fiche « Mélenchon veut ruiner la France » ; « Avant de te répondre… » | `gauche-augmenter-impots` : « Faux : le programme de la gauche en 2024 visait les niches fiscales, l'ISF, les superprofits et les grosses successions. Même l'iFRAP… » |
| Il faut renvoyer tous les criminels étrangers. | « Avant de te répondre… » | « Une condamnation passée ne suffit pas, à elle seule, à expulser… » |
| La France n'a plus les moyens de financer ses services publics. | « Pas encore dans la bibliothèque » | `services-publics-moyens` : « Le déficit est réel, mais « plus les moyens », c'est un choix déguisé en fatalité… » |
| Mélenchon crie tout le temps, il est dangereux. | « Avant de te répondre… » | « Oui, il hausse le ton, parfois trop… Mais parler fort ne dit pas si ce qu'il propose est juste ou faux. » |
| Les aides sociales encouragent les gens à ne pas travailler. | Fiche « Tout le monde se jette sur le RSA » ; « Avant de te répondre… » | `rsa-smic` : « Le RSA pour une personne seule, c'est 651 € par mois au maximum. Un SMIC à temps plein, c'est environ 1 443 € net… » |
| La France doit d'abord s'occuper de ses propres citoyens. | Fiche sur le nucléaire (sujet voisin) ; « Avant de te répondre… » | `immigres-aides` (réponse partielle, signalée) : « Pour le RSA, un étranger hors UE doit en général avoir un titre de séjour depuis au moins cinq ans… » |

## Différence concrète entre les deux modes (même affirmation, mêmes preuves)

| | Gagner le débat | Convaincre avec empathie |
|---|---|---|
| 1. La réponse | Identique : réponse directe et arguments | Identique |
| 2. Les preuves | Identiques : sources et « Ce que ça montre » | Identiques, présentées une par une (« Un premier élément », « Ensuite ») |
| 3. Présenter | Riposte, question piège, 2 objections, entrée par le fond | Entrée sans braquer, questions pour comprendre, ce qu'il faut reconnaître, 1 objection |
| 4. Communication | Ton assuré, « Pour ne pas te disperser » | Ton bienveillant, la même réponse dite avec empathie, conclusion ouverte |

## Tests exécutés

- **Parcours dans le navigateur** : 10 affirmations, chacune testée par 3 parcours (express depuis l'accueil sans thème, express « gagner », express « convaincre »), soit 30 parcours, tous réussis. Pour chaque parcours, le test vérifie :
  - le mode choisi est ouvert ;
  - la bonne fiche est utilisée ;
  - le premier bloc est « Ce que tu peux répondre » ;
  - des sources sont présentes ;
  - aucun conseil générique n'apparaît avant la réponse et les preuves ;
  - la communication vient en dernier ;
  - en « gagner », il y a une riposte et aucun bloc d'empathie ;
  - en « convaincre », il y a une présentation adaptée et une version empathique ;
  - les deux modes sont visiblement différents, avec les mêmes sources.
- **Non-régression** :
  - 370 tests unitaires réussis, dont les 166 scénarios de personnalisation, la conversation, les suggestions et le contrôle « aucun chiffre absent de la fiche » ;
  - 29 tests de bout en bout réussis ;
  - 193 phrases de compréhension réussies (180 de la v8 et 13 nouvelles).
- **Tests mis à jour**, parce que l'ancien comportement est précisément celui qu'il fallait corriger :
  - « profil susceptible en mode gagner → entrée par reformulation » ;
  - « questions avant les faits en mode empathique ».

  Les nouvelles versions vérifient l'inverse : la réponse et les faits d'abord, et la reformulation réservée au mode empathique.

## Problèmes encore présents

- « La France doit d'abord s'occuper de ses propres citoyens » est rattachée à la fiche sur l'accès des étrangers aux aides : c'est une réponse partielle, signalée comme telle. Une fiche dédiée à la « préférence nationale » (droit, Constitution, coût) serait plus juste.
- Certaines réponses courtes existantes gardent un ton conciliant, même en mode « gagner » (par exemple la fin de la fiche Mélenchon : « On regarde une mesure précise ensemble ? »). Ce sont des textes de fiches à réécrire au cas par cas.
- La fiche `riches-creent-emplois` s'appuie sur un compte rendu (Actu-Juridique) du rapport de France Stratégie : le site de France Stratégie n'était pas accessible depuis l'outil de vérification.
- Les chiffres des nouvelles fiches datent de 2024 et 2025 (dernières données publiées). Ils sont à actualiser en 2027.
