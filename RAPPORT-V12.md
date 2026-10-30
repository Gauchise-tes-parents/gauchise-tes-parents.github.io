# Rapport v12 — Transformer le moteur de réponse

## Le problème constaté

Avant toute modification, j'ai fait passer les 20 questions de la demande dans le moteur, tel qu'il est utilisé par l'application :

| Résultat avant la v12 | Questions |
|---|---|
| Bonne fiche (7) | immigrés et travail, étrangers et aides, immigration et insécurité, entreprises et salaires, grand remplacement (fiche générale sur les chiffres), services publics, misère du monde |
| **Fiche hors sujet (4)** | héritage → fiche sur les impôts et l'assistanat ; syndicats → fiche sur les dividendes ; fraude sociale → fiche sur les impôts et l'assistanat ; nationalité → fiche sur le patriotisme |
| Réponse partielle (2) | « pauvres sans efforts » et « la France dépense trop pour les pauvres » → fiche générale sur la pauvreté |
| **Aucune réponse (7)** | cartes Vitale, SMIC, temps de travail, louer sans CDI, retraite à 64 ans, traverser la rue, la gauche et les immigrés |

## Les causes

1. **Pas de fiche sur des sujets très fréquents.** La bibliothèque ne couvrait ni les cartes Vitale, ni le SMIC, ni les retraites, ni les syndicats, ni la nationalité.
2. **Pas de concept pour les reconnaître.** Sans les notions « héritage », « fraude » ou « syndicats », la phrase n'était rattachée qu'à un concept large (« impôts », « entreprises ») et donc à la fiche la plus proche de ce concept.
3. **Un motif trop large.** Le motif « nation… » du concept « patriotisme » reconnaissait aussi « nationalité » et « nationalisations » : la nationalité partait vers la fiche sur le patriotisme, et « Les nationalisations ont été des échecs » était compté à tort comme une question couverte.
4. **La ressemblance de mots réintroduisait des fiches écartées.** Quand l'analyse avait volontairement écarté un argument faute de formulation précise, la recherche par mots pouvait le réintroduire.
5. **Des suggestions sans réponse** étaient encore proposées comme sujets à examiner.

## Ce qui a été modifié dans le code

- **Moteur de compréhension** (`cartographie.js`, `analyse.js`) :
  - **12 nouveaux concepts** : cartes Vitale, héritage, fraude, salaire minimum, temps de travail, retraites, seniors, syndicats, nationalité, propriété, location, « traverser la rue ».
  - **16 nouveaux arguments**, chacun relié à la fiche qui y répond vraiment. Les arguments ambigus exigent une formulation précise. Exemple : « Que propose le RN pour les retraites ? » ne déclenche pas la fiche sur la retraite à 64 ans.
  - **Formules adaptées aux deux modes** pour chaque nouvel argument.
  - **Motif « nation » corrigé**, ce qui supprime le faux positif sur « nationalisations ».
  - **Règle de compatibilité renforcée** : un argument écarté par l'analyse ne peut plus revenir par ressemblance de mots.
- **Classification multiple** : chaque concept relève d'un ou de plusieurs domaines. Une phrase peut ainsi toucher l'immigration, le social et la sécurité à la fois, et les **domaines mobilisés** sont affichés dans l'analyse.
- **Sans fiche, la limite est annoncée** :
  - la page s'intitule « Pas de fiche vérifiée sur ce point » ;
  - l'analyse est étiquetée « Analyse sans données sourcées » ;
  - un texte rappelle que répondre avec des sources à une question hors bibliothèque demande le mode connecté (intelligence artificielle et recherche web), **qui n'est pas actif sur ce site public**, et qu'aucune recherche n'a été lancée ;
  - aucun bouton de recherche n'apparaît sans mode connecté, et aucune fiche voisine n'est présentée comme une réponse.
- **Suggestions prêtes à l'emploi seulement** : une phrase n'est proposée que si l'application y répond avec une fiche vérifiée. Les autres sont comptées « en préparation » et ne sont pas affichées comme des sujets prêts.
- **Consignes du mode connecté** (côté serveur), qui reprennent la demande :
  - l'identité de l'outil ;
  - la distinction fait / interprétation / proposition / jugement de valeur ;
  - l'ordre obligatoire en 5 temps ;
  - le ressenti distingué du fond ;
  - les clichés d'extrême droite reconnus sous des formulations inédites ;
  - les sources prioritaires (IRES, Eurostat, OCDE, HCFP, COR, Service-Public…).

## 14 nouvelles fiches, toutes lues à la source

| Fiche | Sources principales |
|---|---|
| Cartes Vitale en trop | Réponse du ministère de la Santé à l'Assemblée (juin 2025) ; réponse du Gouvernement au Sénat (2020) |
| SMIC et emploi | Étude Dustmann et Lindner (UCL, 2020) ; Insee, pauvreté selon l'activité (2025) |
| Héritage | Conseil d'analyse économique, note n° 69 (2021) ; Insee (aides familiales et propriété) |
| Fraude sociale et fiscale | HCFiPS (via Public Sénat, 2024) ; ministère de l'Économie, estimation Insee de la fraude à la TVA (2023) |
| Temps de travail | Eurostat (via Public Sénat, 2025) ; COR, emploi des seniors (2026) |
| Retraite à 64 ans | COR, rapport 2025 ; COR, rapport 2026 |
| Emploi après 50 ans | COR, rapport 2026 ; COR, rapport 2025 |
| Syndicats | Dares (2016, données 2013) ; Dares (2004) |
| Nationalité | Insee (acquisitions de la nationalité, 2023) ; Insee (immigrés, 2025) |
| Accès à la propriété | Insee, Économie et Statistique (2018) ; CAE (2021) |
| Louer sans CDI | Réseau ANIL (2026) ; UFC-Que Choisir (2026) |
| Pauvreté et efforts | Insee (2025 et 2026) ; France Stratégie, « Nés sous la même étoile ? » (2018) |
| La gauche, les immigrés et les travailleurs | Insee ; CEPII ; LCP (programme de 2024) ; sondage Ipsos ; thèse d'A. Edo |
| « Grand remplacement » | Insee (immigrés et descendants, 2025) ; Insee (histoire des migrations, 2023) |

Chaque fiche comprend :
- une réponse courte ;
- un argumentaire en trois longueurs ;
- au moins deux sources ;
- les objections et leur réfutation ;
- une lecture de gauche (mécanismes, conséquences, enjeux démocratiques, propositions présentées comme des choix politiques) ;
- au moins un **fait défavorable** intégré honnêtement. Exemples : la France taxe davantage les successions que la moyenne de l'OCDE ; le COR projette un besoin de financement à long terme ; une partie des ouvriers vote pour l'extrême droite ; la part des immigrés augmente.

J'ai aussi ajouté une lecture de gauche à trois fiches qui en manquaient et qui répondent à des questions de la liste : statistiques et insécurité, pénurie de main-d'œuvre, grand remplacement.

**Ce qui n'a pas été repris, faute de source vérifiée :**
- les estimations de la fraude fiscale à 60-100 milliards ;
- l'avis du groupe d'experts sur le SMIC, que je n'ai pas pu ouvrir.

Les fiches le signalent dans leurs limites.

## Résultats des tests (exécutés)

| | Avant | Après |
|---|---:|---:|
| Questions de la demande qui reçoivent la fiche qui leur répond | 7 / 20 | **20 / 20** |
| … dans les deux modes, avec la réponse d'abord, puis les preuves, puis la lecture de gauche | — | **20 / 20 × 2 modes** |
| Fiches hors sujet parmi ces 20 questions | 4 | **0** |
| Affirmations suggérées (764) menant à une fiche cohérente | 437 | **447** |
| Affirmations suggérées envoyées vers un autre domaine | 0 | **0** |
| Fiches dans la bibliothèque | 88 | **102** |

Le détail des 20 réponses se trouve dans `rapports/tests-20-questions.md` (commande `npm run rapport:v12`).

**Tests ajoutés :**

- **`tests/unit/v12-questions.test.js`**, 35 tests :
  - les 20 questions et 7 variantes (dont des formulations familières : « les syndicats ils bloquent tout », « on nous remplace », « les fraudeurs aux allocs ») ;
  - pour chaque question : bonne fiche, réponse courte, faits sourcés, au moins deux sources, réfutation, proposition, audit documentaire ;
  - dans chaque mode : ordre réponse → preuves → lecture, et modes non mélangés ;
  - classification multiple ;
  - lacunes honnêtes ;
  - **non-régression du RSA** (les questions sur le RSA vont aux fiches RSA ; aucune des 20 questions ne reçoit une fiche RSA ; une source RSA n'apparaît que si la fiche établit un lien précis) ;
  - suggestions toutes prêtes à l'emploi.
- **Parcours dans le navigateur** :
  - les 20 questions dans les deux modes, soit 40 parcours (réponse, preuves, lecture de gauche, sources cliquables, domaines) ;
  - une phrase sans fiche, avec la limite annoncée et sans bouton de recherche ;
  - suggestions, toutes marquées « fiche vérifiée ».

Résultat de l'exécution : voir la section finale.

## Limites qui restent

- **Hors bibliothèque, pas de réponse documentée sur le site public.** L'application analyse la phrase et le dit clairement, mais elle ne peut pas chercher de sources. Pour cela, il faut héberger le serveur (`server/`) avec une clé d'API gardée côté serveur et un budget plafonné. Ce n'est pas configuré, et rien ne le simule.
- **317 affirmations suggérées restent sans fiche** (327 en v11). Quelques faux positifs supprimés (« nationalisations », « grèves de 1936 », « retraite par répartition ») sont désormais annoncés comme des lacunes au lieu de recevoir une fiche voisine. Ces affirmations ne sont plus proposées comme sujets prêts ; elles sont comptées « en préparation ».
- **Le sous-thème « Histoire économique »** n'a plus de réponse : son unique « couverture » était un faux positif.
- **Certaines données sont anciennes** et sont signalées comme telles dans les fiches : syndicalisation (2013), accès à la propriété (2013), France Stratégie (2018).

## Exécution finale (30 octobre 2026)

- `npm test` : **431 tests réussis sur 431** (396 avant la v12 ; 35 ajoutés).
- Parcours dans le navigateur (Chromium, format téléphone) : **32 sur 32**, dont le nouveau parcours des 20 questions dans les 2 modes.
- Compréhension : **193 phrases sur 193**.
- Audit de cohérence : 764 affirmations ; 447 cohérentes, 0 hors domaine.
- Politique documentaire : 0 fiche non conforme.
