# Rapport v10 — Identité politique, éditoriale et documentaire

Gauchise tes parents assume des **valeurs** de gauche (humanistes, universalistes, sociales, démocratiques, antifascistes) et une exigence de vérité sans compromis sur les **faits**. Ces règles ne sont pas un texte de présentation : elles sont codées dans un module unique, `public/js/ligne-editoriale.js`, que le moteur hors ligne et le mode connecté utilisent tous les deux.

## 1. Règles éditoriales ajoutées

- **17 principes défendus**, chacun avec une phrase d'explication réutilisée dans les réponses :
  - égalité réelle et universalité des droits ;
  - solidarité, dignité, antiracisme et antifascisme ;
  - libertés publiques et services publics ;
  - émancipation, démocratie et souveraineté populaire ;
  - internationalisme ;
  - égalité femmes-hommes et lutte contre les discriminations ;
  - protection des travailleurs et répartition des richesses ;
  - protection des personnes vulnérables ;
  - paix et droit international.
- **8 règles de vérité** non négociables :
  - ne rien inventer ;
  - ne cacher aucun résultat contraire ;
  - ne pas sélectionner les seuls chiffres favorables ;
  - ne jamais utiliser une source militante comme preuve statistique unique ;
  - signaler les limites ;
  - distinguer faits, interprétations, valeurs et propositions ;
  - quand une étude contredit un argument de gauche, le dire et expliquer comment l'intégrer.
- **Lecture de gauche** dans chaque argumentaire. C'est une nouvelle partie 3, placée après la réponse et les preuves, dans les deux modes. Elle contient :
  - les mécanismes, les conséquences humaines et l'enjeu démocratique ;
  - les valeurs en jeu ;
  - « Ce que la gauche propose », explicitement étiqueté *propositions politiques : des choix assumés, pas des faits* ;
  - « Ce qui ne va pas dans notre sens », avec le fait gênant et la manière de l'intégrer honnêtement.

  L'ordre devient : 1. la réponse, 2. les preuves, 3. la lecture de gauche, 4. comment présenter l'argument, 5. comment aborder la discussion.
- **Garde-fou de dignité humaine.**
  - Il repère la déshumanisation, les appels à la violence ou à la mort, l'exclusion collective d'une population et l'antisémitisme.
  - Il affiche alors un encadré ferme : « Ce propos n'est pas une opinion comme une autre ». Il n'y a pas de faux équilibre.
  - Il distingue explicitement la critique d'une politique, qui est légitime et n'est pas signalée (testé), de l'attaque contre une population.
- **Patriotisme ≠ souveraineté ≠ nationalisme ≠ xénophobie** : ces quatre notions sont distinguées dans les consignes et dans la fiche `patriotisme-nationalisme`.
- **Comparaisons historiques** : les mécanismes communs (judéo-bolchevisme et « islamo-gauchisme ») sont analysés sans équivalence automatique.

## 2. Politique documentaire et sources prioritaires

Chaque source est classée automatiquement (`classerSource`) et reçoit un rôle :

| Rôle | Classes | Peut établir un fait ? |
|---|---|---|
| Autorité | Recherche et statistique publiques (Insee, DREES, Dares, INED, CNRS, France Stratégie, OFCE, CEPII, universités, revues à comité de lecture) ; institutions (Parlement, Légifrance, Conseil d'État, Défenseur des droits, Cour des comptes, CNCDH, ONU, OIM, Conseil de l'Europe…) ; histoire et mémoire (Mémorial de la Shoah, archives, musées) | Oui |
| Complément | Presse de référence (Le Monde, Libération, Mediapart, L'Humanité, Franceinfo, France Culture, AFP, Alternatives économiques, Arrêt sur images, Public Sénat…) ; associations (LDH, SOS Racisme, Amnesty, HRW, observatoires) ; vulgarisation ; encyclopédies | Seulement si le fait est attribué, et jamais par une encyclopédie seule |
| Origine | Médias et think tanks de droite (iFRAP, Institut Montaigne, Europe 1, CNews, Figaro…) ; sources partisanes de tout bord (LFI, PCF, RN…) | Non : on les consulte pour savoir ce qui a été dit, et on les cite toujours en les attribuant (« selon… ») |

Un **audit automatique** (`auditFiche`) vérifie chaque fiche. Il est exécuté par les tests et par le script de corrections :

| | Résultat |
|---|---|
| Avant corrections | 18 fiches non conformes sur 58 |
| Après corrections | 0 sur 74 fiches thématiques |

Le mode connecté reçoit la même politique dans ses consignes : documentaliste, stratégie, conversation et discours.

## 3. Fiches enrichies et corrigées

**Quatre nouvelles fiches**, toutes à partir de sources lues :
- **`discriminations-embauche`** : testing Dares, IPP et ISM Corum (2021) ; Insee 2023.
- **`egalite-salariale`** : Insee Focus n° 377, février 2026.
- **`migrants-mediterranee`** : article 98 de la Convention des Nations unies sur le droit de la mer (présentation DOALOS) ; OIM via ONU Info, avril 2026 ; Institut universitaire européen (Cusumano et Villa, 2019).
- **`antisemitisme-aujourdhui`** : CNCDH (rapports 2024 et 2025) ; analyse de Nonna Mayer (Sciences Po et CNRS) ; Mémorial de la Shoah.

**24 fiches dotées d'une lecture de gauche** : les 15 sujets obligatoires, ainsi que les fiches sur les salaires, la délinquance, la nation, le CNR, les dividendes, l'aide sociale, la fiscalité de gauche et LFI.

**Corrections documentaires** (`scripts/corrections-v10.js`, idempotent) :
- **« Islamo-gauchisme »** :
  - les deux faits qui reposaient sur Wikipédia sont maintenant sourcés par l'analyse du Politoscope (CNRS, David Chavalarias) et par un article évalué par les pairs (Philippe Marlière, *French Cultural Studies*, 2023) ;
  - une erreur a été trouvée et corrigée : la fiche situait la hausse d'usage du terme en octobre 2019, alors que la source la situe en **octobre 2020**, après les interventions de ministres.
- **Comparaison judéo-bolchevisme / islamo-gauchisme** : le fait tiré de Wikipédia est réécrit à partir de la source AOC, et la source encyclopédique est retirée.
- **Commune de Paris** : deux faits tirés de Wikipédia sont ré-sourcés par la Ville de Paris. Le fait défavorable aux communards (exécution d'environ cent otages, dont l'archevêque Darboy) est **conservé**.
- **Judéo-bolchevisme** : ajout du bilan de la persécution d'après le Mémorial de la Shoah (76 000 Juifs de France déportés et assassinés).
- **Attributions** : 15 faits appuyés sur une source de vulgarisation, partisane ou de droite sont désormais explicitement attribués (« Selon l'Institut Montaigne… », « Selon Europe 1… »), au lieu d'être présentés comme établis par une autorité.

**Cartographie** :
- 5 nouveaux concepts : Sécurité sociale, discriminations, égalité femmes-hommes, sauvetage en mer, antisémitisme (devenu central) ;
- 5 nouveaux arguments ;
- 5 nouvelles formules marquantes.

## 4. Faits défavorables désormais affichés (exemples)

- **Antisémitisme** : selon Nonna Mayer, à partir des données de la CNCDH, les préjugés antisémites ont progressé de 10 points en trois ans chez les sympathisants de LFI. Intégration proposée : « l'antifascisme ne se divise pas ».
- **Égalité salariale** : à poste comparable dans le même établissement, l'écart n'est que de 3,6 %. Intégration : l'inégalité est surtout structurelle (temps partiel, métiers féminisés sous-payés).
- **Immigration et emploi** : une étude trouve un effet négatif à court terme pour les travailleurs directement en concurrence. Intégration : protéger tous les travailleurs, avec les mêmes droits et des contrôles des employeurs.
- **Riches et emplois** : l'évaluation de France Stratégie note un effet positif de la réforme de 2018 sur la création d'entreprises.
- **Mélenchon** : condamnation après la perquisition de 2018.
- **Islamo-gauchisme** : des convergences précises sont décrites par certains auteurs. Les critiquer est légitime ; l'accusation générale ne l'est pas.

## 5. Avant / après (capturé dans le navigateur, v9 puis v10, mode « Gagner »)

| Phrase | v9 | v10 |
|---|---|---|
| Les immigrés sont des parasites. | « J'ai compris l'argument (immigration), pas de fiche » : réponse neutre | Encadré « Ce propos n'est pas une opinion comme une autre » (déshumanisation), titre « Pas un argument : une atteinte à la dignité », puis pistes de fiches sur les vraies inquiétudes (emploi, aides, prisons) |
| L'égalité salariale, c'est réglé. | Pas de fiche | « Non : en 2024, les femmes gagnent 21,8 % de moins que les hommes sur l'année, et 14 % de moins à temps de travail égal (Insee)… » + lecture de gauche |
| Il ne faut pas secourir les migrants en mer, ça crée un appel d'air. | Pas de fiche | « Secourir quelqu'un qui se noie est une obligation du droit de la mer… Plus de 82 000 morts et disparus depuis 2014 (OIM)… aucune relation entre la présence des ONG et les départs… » |
| L'antisémitisme, c'est un faux problème pour faire taire la gauche. | « Je n'ai pas reconnu de sujet » | « Non : 1 570 actes antisémites en 2024, 1 320 en 2025… Être de gauche, c'est combattre l'antisémitisme partout, y compris chez nous… » |
| L'islamo-gauchisme gangrène l'université. | Réponse sur une fiche dont deux faits reposaient sur Wikipédia (dont une date erronée) | Même réponse, mais faits ré-sourcés, date corrigée, et lecture de gauche avec la question des convergences réelles |

## 6. Tests exécutés

- **15 sujets obligatoires**, un test par sujet. Chacun vérifie :
  - la bonne fiche ;
  - la conformité des sources à la politique documentaire ;
  - au moins une source d'autorité (ou de presse de référence pour la communication politique) ;
  - aucune source encyclopédique ;
  - une lecture de gauche complète (valeurs, mécanismes, enjeu démocratique, propositions) ;
  - au moins un fait défavorable avec son intégration ;
  - aucun chiffre de la lecture absent des faits sourcés ;
  - la lecture présente dans les deux modes, après les preuves.
- **Audit global** : les 74 fiches thématiques sont conformes, aucun fait ne repose sur une encyclopédie, et toute source de droite ou partisane est attribuée.
- **Dignité** : 8 propos détectés, et 6 critiques légitimes non signalées (réduire l'immigration, justice laxiste, critique du gouvernement israélien, critique d'une religion, expulsion de criminels, phrase neutre contenant « virus »).
- **Mode connecté** : la signature éditoriale, les règles de vérité et la politique documentaire sont présentes dans toutes les consignes.
- **Totaux** : 391 tests unitaires réussis ; 30 parcours dans le navigateur réussis, dont un nouveau test v10 (lecture de gauche dans les deux modes, encadré de dignité, absence d'alerte sur une critique de politique, lecture sur la page de fiche) ; 193 phrases de compréhension réussies.

## 7. Limites

- **Classement automatique des sources** : il repose sur le nom de l'organisme et le domaine. C'est une aide, pas un jugement : une association peut publier une étude solide, et un grand média une erreur. Les articles restent à juger sur leur méthode.
- **Attributions ajoutées automatiquement** : elles rendent les fiches honnêtes, mais certaines gagneraient à être ré-sourcées directement auprès d'une autorité. Cela concerne la Sécurité sociale (Herodote.net), l'électricité (Connaissance des Énergies) et le SMIC (La finance pour tous) ; le site service-public.fr n'était pas accessible depuis l'outil.
- **Détection des atteintes à la dignité** : elle repose sur des formulations. Un propos déshumanisant formulé autrement peut passer, et l'encadré décrit les mots employés, pas l'intention de la personne.
- **Fiche antisémitisme** : les comparaisons par proximité partisane reposent sur des sous-échantillons d'un baromètre d'environ un millier de personnes ; c'est signalé dans la fiche.
- **Lectures de gauche** : il s'agit de propositions politiques rédigées pour l'application. Elles sont étiquetées comme telles et ne contiennent aucun chiffre.
- **Ordre des scripts** : relancer un générateur de fiches Python écrase les corrections. Il faut donc toujours enchaîner : générateurs, puis `npm run fiches:corriger`, puis `npm run enrichir`.
