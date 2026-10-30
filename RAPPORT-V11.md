# Rapport v11 — Test de cohérence dans tous les domaines

## Ce qui a été testé

L'application propose **764 affirmations** réparties sur les **127 sous-thèmes** des 9 domaines. Le nouveau script `scripts/audit-coherence.js` les traite **toutes**, exactement comme l'application, puis vérifie que la fiche obtenue relève du même domaine (même volet, même sous-thème ou concept commun).

Chaque affirmation couverte est ensuite composée avec plusieurs **choix différents** : 2 modes (« gagner », « convaincre ») et 3 profils d'interlocuteur (inconnu ; compétitif et attaché aux chiffres ; susceptible, parent, attaché à la sécurité). Cela fait **2 622 réponses** vérifiées une par une : la réponse vient en premier, les preuves sont sourcées, la lecture de gauche est présente quand la fiche en a une, et les deux modes sont bien distincts.

## Résultats

| | Avant | Après |
|---|---:|---:|
| Affirmations qui mènent à une fiche cohérente | 395 | **437** |
| Affirmations envoyées vers une fiche d'un autre domaine | **15** | **0** |
| Affirmations sans fiche (la lacune est annoncée honnêtement) | 354 | 327 |
| Sous-thèmes sans aucune affirmation couverte | 11 | **3** |
| Fiches dans la bibliothèque | 78 | **88** |

## Erreurs trouvées et corrigées

**1. Quinze affirmations renvoyaient vers une fiche hors sujet.** La cause : une correspondance par mots acceptait une fiche voisine. Exemples :
- « Quel est vraiment le taux de récidive en France ? » renvoyait à la fiche sur la pauvreté ;
- « Les Français ne travaillent pas assez » renvoyait à la fiche sur l'immigration et l'emploi ;
- « Le RN a changé, ce n'est plus l'extrême droite » renvoyait à la fiche sur l'« islamo-gauchisme » ;
- « On ne peut plus croire personne, tout le monde ment » renvoyait à la fiche sur l'aide sociale.

La correction est une nouvelle règle (`ficheCompatible`) : une fiche trouvée par ressemblance de mots n'est acceptée que si la phrase contient les notions de l'argument auquel la fiche répond. Par exemple, la fiche sur l'immigration et l'emploi exige à la fois l'immigration et l'emploi. Cette règle s'applique à la réponse express, au questionnaire et à l'audit. Elle a aussi supprimé de fausses « couvertures » : la Constitution renvoyait à des fiches sur Mélenchon, le Venezuela à la fiche du CNR.

**2. Des affirmations pertinentes n'étaient pas reconnues.** Exemples : « Les étrangers sont plus souvent mis en cause », « détention provisoire », « plus d'offres d'emploi que de chômeurs », « les féministes », « les inégalités », « la récidive », « les programmes de gauche sont irréalisables ». J'ai ajouté les mots-clés et les arguments correspondants.

**3. Les suggestions affichées en premier n'avaient parfois pas de réponse.** Désormais, dans chaque sous-thème, les affirmations qui ont une fiche passent devant, quel que soit le mode ou le profil. L'étiquette « fiche vérifiée » repose sur la même logique que la réponse elle-même : elle ne peut plus annoncer une fiche que la réponse n'utilise pas.

## Dix nouvelles fiches sourcées (sous-thèmes qui n'en avaient aucune)

| Sous-thème | Fiche | Sources lues |
|---|---|---|
| Homicides | « Il n'y a jamais eu autant de meurtres » | CESDIP (CNRS) ; ministère de l'Intérieur (réponse parlementaire 2023) |
| Loyers | « L'encadrement des loyers ne sert à rien » | Évaluation APUR (juin 2025) |
| Rénovation thermique | « Interdire de louer les passoires va vider le marché » | SDES (novembre 2025) |
| Handicap | « L'AAH, c'est assez pour vivre » | Mon Parcours Handicap (avril 2026) ; Insee (seuil de pauvreté) |
| Désinformation | « Les ingérences étrangères, c'est du fantasme » | Rapport d'activité VIGINUM / SGDSN 2024 |
| Sondages | « Un sondage sur mille personnes ne veut rien dire » | Public Sénat (marge d'erreur, loi de 2016) |
| Abstention | « L'abstention, c'est un choix individuel » | Insee Première n° 1928 |
| Histoire politique | « La gauche n'a jamais rien fait de bien au pouvoir » | Sénat (abolition de 1981) ; COR (retraite à 60 ans) ; Insee (35 heures) ; Assemblée nationale (rapport de 2014) |
| Histoire des migrations | « La France n'a jamais été un pays d'immigration » | Insee (2023) |
| Droits des travailleurs | « Les accidents du travail, c'est un problème du passé » | Réponse du ministère du Travail (mars 2026) |

Chaque fiche :
- respecte la politique documentaire (audit à 0 problème) ;
- comporte une lecture de gauche ;
- présente au moins un fait défavorable. Exemples : « plus de 4 annonces sur 10 dépassent encore le plafond » ; « les 35 heures ont créé moins d'emplois que les 700 000 espérés » ; « hausse des homicides enregistrés en 2021-2022 ».

## Tests exécutés

- **`tests/unit/coherence.test.js`**. Il vérifie :
  - aucune des 764 affirmations ne renvoie vers un autre domaine ;
  - au moins 435 sont couvertes ;
  - chaque sous-thème (hors les 3 lacunes ci-dessous) a au moins une affirmation couverte ;
  - les suggestions affichées en premier mènent à une fiche dans les 2 modes et pour les 3 profils ;
  - les 2 622 compositions sont conformes.
- **Nouveau parcours dans le navigateur.** Six parcours complets, chacun avec un domaine, un sous-thème, un mode et un profil différents :
  - Homicides / gagner ;
  - Rénovation thermique / convaincre, profil susceptible ;
  - Abstention / gagner, profil compétitif ;
  - Handicap / convaincre ;
  - RSA / gagner ;
  - Histoire des migrations / convaincre.

  Dans chaque cas, la première suggestion est marquée « fiche vérifiée » et elle mène à une réponse sourcée, dans le bon mode, d'une fiche du même domaine.
- **Non-régression** : 396 tests unitaires réussis, 31 parcours dans le navigateur réussis, 193 phrases de compréhension réussies.

## Ce qui reste à faire

- **Trois sous-thèmes sans fiche** : Émancipation, Institutions françaises (Parlement, 49.3, Sénat), Constitution (VIe République, Conseil constitutionnel). Pour ces sujets, l'application dit honnêtement qu'elle n'a pas de fiche, et les suggestions sans fiche apparaissent sans l'étiquette « fiche vérifiée ».
- **327 affirmations suggérées restent sans fiche**, surtout dans les domaines International (60), Politique (51) et Services publics (38). Elles n'aboutissent plus jamais à une fiche hors sujet, mais il faudrait des fiches sourcées pour y répondre. Le script `npm run audit:coherence` en donne la liste à jour.
- **Critère de cohérence** : il est automatique (domaine, sous-thème ou concept commun). Il garantit qu'aucune réponse ne part dans un autre domaine, pas que chaque fiche réponde parfaitement à chaque nuance de la question.
