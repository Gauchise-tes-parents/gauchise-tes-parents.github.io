# Rapport v3 — Base de connaissances historiques et argumentaires

Mise à jour réalisée le 29 octobre 2026 sur le projet existant (pas de réécriture). Tous les chiffres ci-dessous ont été comptés sur les fichiers, pas estimés.

## 1. Ce qui a changé

- **Base locale de 40 fiches** au schéma v3 (6 fiches v2 migrées + 34 nouvelles), dans `data/library/`.
- **Trois rubriques** : Patriotisme de gauche (8 fiches), « Islamo-gauchisme », laïcité et instrumentalisation (7, dont la fiche historique « judéo-bolchevisme » et la comparaison des mécanismes rhétoriques), « Mélenchon crie, il est agressif, il est dangereux » (11 fiches en cinq parties).
- **Base générale élargie** : immigration (chiffres et définitions Insee 2024), pauvreté (Insee 2024), justice et prisons (ministère de la Justice 2026), électricité nucléaire / renouvelables (RTE 2025), revenus agricoles, dividendes et salaires, concentration des médias, référendum et démocratie directe, Commune de Paris.
- **Base locale d'abord** : recherche locale immédiate, réponse sur fiche sans recherche web quand c'est justifié, complément web sinon, comparaison web ↔ fiche et propositions de mise à jour jamais appliquées automatiquement.
- **Fiches à sept onglets** : Réponse en 15 secondes, Argumentaire en 1 minute, Développement en 3 minutes, Sources et preuves, Contre-arguments, Contexte historique, Réponse avec empathie. Navigation clavier, mobile d'abord (onglets défilants au pouce).
- **Rubriques** sur la page Thématiques (`#/rubriques/:id`) ; filtres par rubrique et par fiabilité dans la Bibliothèque ; badges de fiabilité ; mention « Pas de verdict binaire » pour les débats.

## 2. Fichiers créés ou modifiés

**Créés**
- `public/js/kbsearch.js` — recherche locale partagée serveur / navigateur.
- `server/engine/knowledge.js` — décision fiche seule / complément web, comparaison, propositions.
- `tests/unit/knowledge.test.js` — 26 tests (schéma, rubriques, cinq parties, recherche, décision, comparaison, API).
- `scripts/fiches/melenchon_lfi.py`, `scripts/fiches/base_generale.py`, `scripts/fiches/migrer_v2.py` — génération traçable des fiches.
- 34 fiches `data/library/*.json` (liste au § 4), `RAPPORT-V3.md`.

**Modifiés**
- `public/js/taxonomy.js` (RUBRIQUES, FIABILITES, STABILITES, TYPES_FICHE, FICHE_TABS), `public/js/app.js` (vue fiche à onglets, rubriques, filtres, résultats locaux instantanés, blocs « base locale » et « comparaison »), `public/js/api.js`, `public/js/copy.js`, `public/css/styles.css`.
- `server/library.js` (schéma v3, refus des pages d'accueil, filtres), `server/app.js` (`GET /api/kb/search`, parcours local d'abord dans `POST /api/analyse`), `server/engine/pipeline.js` (pistes issues de la fiche, comparaison), `server/engine/strategy.js` (objections légitimes et citations vérifiées transmises), `server/engine/demo.js`, `server/config.js`.
- 6 fiches v2 migrées ; `tests/helpers.js`, `tests/unit/server.test.js`, `tests/e2e/ui.test.js` ; `scripts/build-preview.js` ; `README.md`, `.env.example`, `.gitignore`.

## 3. Structure d'une fiche (schéma v3)

| Champ | Contenu |
|---|---|
| `id`, `type` | identifiant ; idée reçue / fiche de référence / réponse à une critique / fiche historique |
| `volet`, `sous_theme`, `rubriques[]`, `mots_cles[]` | classement et recherche |
| `affirmation`, `reproche` (réponses aux critiques) | ce qui est dit ou reproché, et son origine |
| `resume`, `contexte`, `explication` | conclusion, contexte historique, explication grand public |
| `faits[]` | fait, chiffre, période, périmètre, explication, **source** (index d'une source consultée), fiabilité |
| `citations[]` | auteur, texte, date, contexte, source consultée |
| `argumentaires` | `court` (15 s), `moyen` (1 min), `detaille` (3 min), `empathie` |
| `objections_legitimes[]`, `contre_arguments[]` | critiques à reconnaître ; objections et réponses |
| `questions[]`, `limites[]` | questions ouvertes ; ce qu'on ne sait pas, limites des sources |
| `sources[]` | titre, organisme, date, URL précise, passage utilisé, pertinence, type (primaire / secondaire / média / partisane), `consultee` |
| `verdict` (facultatif), `fiabilite`, `stabilite` | établi / estimation / interprétation / débat ; historique / évolutive / actualité |
| `derniere_verification`, `a_actualiser_le`, `raison_actualisation` | traçabilité temporelle |

Règles vérifiées automatiquement au chargement et par les tests : chaque fait et chaque citation renvoient à une source **réellement consultée** ; aucune URL de page d'accueil (chemin vide ou « / ») n'est acceptée comme source ; 3 mots-clés minimum ; quatre argumentaires et au moins un contre-argument ; dates au format AAAA-MM-JJ.

## 4. Inventaire réel des fiches

**40 fiches · 150 faits · 8 citations · 114 sources, dont 111 consultées.** Les 150 faits reposent tous sur une source consultée. **37 fiches** n'ont que des sources consultées ; 3 fiches citent en plus une référence non ouverte, signalée comme telle (`consultee: false`) et jamais utilisée comme preuve : `laicite-loi-1905` (texte de la loi de 2004 non ouvert), `resistance-communistes-etrangers` (article de J.-P. Besse), `rsa-profiteurs` (publication DREES bloquée, chiffres repris via la Banque des Territoires).

Par type : 14 idées reçues, 12 réponses à des critiques, 8 fiches historiques, 6 fiches de référence. Par fiabilité : 23 établies, 8 débats, 7 interprétations, 2 estimations. Par stabilité : 14 historiques, 23 évolutives, 3 d'actualité.

| Fiche | Rubriques | Volet | Fiabilité | Stabilité | Sources (consultées) | À actualiser le |
|---|---|---|---|---|---|---|
| agriculteurs-revenus | — | ecologie | etabli | evolutive | 1 (1) | 2027-01-31 |
| chomeurs-travailler | — | social | etabli | evolutive | 2 (2) | 2026-04-30 |
| commune-paris-1871 | — | international | debat | historique | 2 (2) | 2029-10-29 |
| delinquance-partout | — | securite | etabli | evolutive | 1 (1) | 2027-07-15 |
| dividendes-salaires | — | economie | estimation | actualite | 2 (2) | 2027-03-31 |
| electricite-nucleaire-renouvelables | — | ecologie | etabli | evolutive | 2 (2) | 2027-03-31 |
| front-populaire-1936 | patriotisme-de-gauche | international | etabli | historique | 1 (1) | 2029-10-29 |
| gauche-assistes-travailleurs | melenchon-lfi | social | etabli | evolutive | 6 (6) | 2027-04-29 |
| gauche-laicite-debats | islamo-gauchisme-laicite | droits | debat | evolutive | 3 (3) | 2027-10-29 |
| gauche-nation-debats | patriotisme-de-gauche | politique | interpretation | historique | 3 (3) | 2029-10-29 |
| immigration-chiffres-definitions | — | immigration | etabli | evolutive | 1 (1) | 2026-12-31 |
| immigres-aides | — | immigration | etabli | evolutive | 4 (4) | 2027-10-29 |
| impots-assistanat | — | social | etabli | evolutive | 2 (2) | 2027-02-15 |
| islamo-gauchisme-judeo-bolchevisme-comparaison | islamo-gauchisme-laicite | politique | debat | historique | 4 (4) | 2028-10-29 |
| islamo-gauchisme-origine-usages | islamo-gauchisme-laicite | droits | debat | historique | 5 (5) | 2027-10-29 |
| judeo-bolchevisme-histoire | islamo-gauchisme-laicite | international | etabli | historique | 3 (3) | 2029-10-29 |
| justice-laxiste-prison | — | securite | etabli | evolutive | 2 (2) | 2027-07-31 |
| laicite-loi-1905 | islamo-gauchisme-laicite | droits | etabli | historique | 5 (4) | 2028-10-29 |
| lfi-antisemite | melenchon-lfi | politique | debat | actualite | 5 (5) | 2027-01-29 |
| lfi-communautarisme | melenchon-lfi, islamo-gauchisme-laicite | politique | debat | evolutive | 3 (3) | 2027-04-29 |
| lfi-contre-police | melenchon-lfi | securite | interpretation | evolutive | 3 (3) | 2027-04-29 |
| medias-concentration | — | politique | interpretation | evolutive | 3 (3) | 2027-04-29 |
| melenchon-agressif | melenchon-lfi | politique | etabli | evolutive | 4 (4) | 2027-04-29 |
| melenchon-autoritaire | melenchon-lfi | politique | interpretation | evolutive | 3 (3) | 2027-04-29 |
| melenchon-change-avis | melenchon-lfi | politique | etabli | historique | 3 (3) | 2028-10-29 |
| melenchon-crie | melenchon-lfi | politique | interpretation | evolutive | 3 (3) | 2027-04-29 |
| melenchon-dangereux-democratie | melenchon-lfi | politique | interpretation | actualite | 3 (3) | 2027-04-29 |
| melenchon-ruiner-france | melenchon-lfi | economie | debat | evolutive | 2 (2) | 2027-04-29 |
| musulmans-amalgames | islamo-gauchisme-laicite | immigration | etabli | evolutive | 1 (1) | 2028-03-30 |
| patriotisme-nationalisme | patriotisme-de-gauche | politique | interpretation | historique | 3 (3) | 2029-10-29 |
| pauvrete-france | — | social | etabli | evolutive | 1 (1) | 2027-07-31 |
| programme-cnr-1944 | patriotisme-de-gauche | international | etabli | historique | 3 (3) | 2029-10-29 |
| programme-irrealisable | melenchon-lfi | politique | debat | evolutive | 3 (3) | 2027-04-29 |
| referendum-democratie-directe | — | politique | etabli | historique | 4 (4) | 2028-10-29 |
| resistance-communistes-etrangers | patriotisme-de-gauche | international | etabli | historique | 4 (3) | 2029-10-29 |
| rsa-profiteurs | — | social | estimation | evolutive | 2 (1) | 2027-05-06 |
| rsa-smic | — | social | etabli | evolutive | 3 (3) | 2027-01-01 |
| securite-sociale-1945 | patriotisme-de-gauche | services | etabli | historique | 3 (3) | 2029-10-29 |
| souverainete-industrielle-alimentaire-energetique | patriotisme-de-gauche | economie | etabli | evolutive | 3 (3) | 2027-04-30 |
| souverainete-populaire | patriotisme-de-gauche | politique | etabli | historique | 3 (3) | 2029-10-29 |

## 5. Fiches à compléter (ce qui manque, honnêtement)

- **Immigration et délinquance** : non traitée. La publication Interstats sur la nationalité des mis en cause n'a pas pu être ouverte (accès automatisé refusé par le site) ; aucune fiche n'a été écrite sans elle.
- **Immigration : flux** (titres de séjour, asile, OFPRA) et **emploi / finances publiques** récents : à ajouter avec les publications du ministère de l'Intérieur et de l'OCDE.
- **Sécurité** : taux d'élucidation, condamnations prononcées et exécution des peines (les Références statistiques Justice 2026 n'ont été lues que pour le chapitre prisons).
- **Histoire** : Révolution française, mouvement ouvrier du XIXᵉ siècle, décolonisations, évolution gauche / droite / extrême droite. La fiche Commune ne détaille pas les mesures de la Commune, faute de source lue.
- **Écologie** : coûts comparés des filières, émissions totales de la France, justice climatique.
- **Médias** : opinions des journalistes (aucune enquête récente vérifiée), propriété détaillée (carte du Monde diplomatique / Acrimed consultée via une reprise).
- **Démocratie** : votes exacts du Congrès de 2008, référendum d'initiative partagée.
- **Fiches à actualiser en priorité** : `chomeurs-travailler` (signalée « À actualiser » depuis avril 2026), `immigration-chiffres-definitions` (nouvelle édition Insee attendue en novembre), `agriculteurs-revenus` (données 2018-2022), `lfi-antisemite` (actualité, chiffres d'actes antisémites de 2024 à remplacer par les bilans récents).
- Plusieurs fiches s'appuient sur des sources secondaires (presse, Wikipédia pour la comparaison islamo-gauchisme / judéo-bolchevisme et pour les estimations de la Semaine sanglante) : c'est indiqué dans leurs limites ; les ouvrages originaux restent à lire.

## 6. Garde-fous éditoriaux appliqués

- Aucune référence, citation, URL, statistique ou décision de justice inventée : chaque élément vient d'une page ouverte le 29 octobre 2026 ; ce qui n'a pas pu être vérifié a été retiré ou signalé dans les limites.
- Statistiques datées et périmètre indiqué ; données anciennes signalées avec une date d'actualisation.
- **Mélenchon / LFI** : chaque fiche distingue style, perception, fond et comportements critiquables. La fiche « crie » admet qu'il hausse le ton et rappelle la condamnation de 2019. La fiche « antisémitisme » n'a pas de verdict (débat), rapporte les critiques venues de la gauche (Rossignol, Faure, Ruffin) et pose deux règles : critiquer le gouvernement israélien n'est pas antisémite ; se présenter comme critique politique n'exonère pas un propos.
- **Comparaison « islamo-gauchisme » / « judéo-bolchevisme »** : les deux expressions ne sont jamais présentées comme identiques ; la fiche porte sur des mécanismes démontrés et détaille les différences de contexte, de cibles, de fonction et de gravité (un test automatique vérifie cette formulation).
- **Patriotisme de gauche** : avertissement affiché dans la rubrique (pas de monopole de la gauche, droite non présentée comme hostile en bloc).

## 7. Tests exécutés (29 octobre 2026)

- `npm test` : **86 tests, 86 réussis** (dont 24 nouveaux : schéma v3, rubriques, cinq parties, recherche locale avec et sans accents, absence de correspondance, filtres, décision fiche / web dans les cinq cas, comparaison web ↔ fiche, API `kb/search`, démo, réponse directe sans recherche web, recherche fraîche avec comparaison et proposition, sujet d'actualité, panne de la recherche web).
- `npm run test:e2e` (Chromium, formats téléphone 320 à 412 px et bureau) : **20 tests, 20 réussis** (dont 4 nouveaux : sept onglets et clavier, puces des cinq parties, fiche sans verdict, rubriques, démo « base locale d'abord », réponse directe sur fiche en mode réel simulé ; filtres rubrique et fiabilité ; aucun débordement horizontal à 360 px ; aucune erreur JavaScript).
- **Vérification manuelle** : captures d'écran sur téléphone (390 px) de la fiche « Mélenchon crie », de l'onglet Sources (citations vérifiées), de la page Thématiques et de la Bibliothèque ; aperçu statique (sans serveur) contrôlé : 40 fiches, recherche locale « la police tue » → fiche correspondante, sept onglets, aucune erreur.
- **Non testé** : la recherche web réelle (pas de clé API dans cet environnement) ; le mode réel est validé avec un service d'IA simulé, au format documenté.

## 8. Enrichir la base

1. **Lire la source** : ouvrir le document précis (page de publication, PDF, texte de loi). Jamais une page d'accueil.
2. **Créer la fiche** `data/library/<id>.json` (minuscules, chiffres, tirets), ou l'ajouter à un script de `scripts/fiches/` pour garder la trace des sources.
3. **Remplir** chaque champ du § 3. Chaque fait pointe vers une source `"consultee": true` ; une référence trouvée mais non lue reste `"consultee": false` et ne soutient aucun fait.
4. **Dater** : `derniere_verification` (jour de lecture) et `a_actualiser_le` (date de la prochaine publication attendue pour une donnée évolutive ; deux à trois ans pour un fait historique).
5. **Classer** : volet et sous-thème existants (`public/js/taxonomy.js`), rubriques, mots-clés (expressions entières utiles : « la police tue », « loi de 1905 »).
6. **Vérifier** : `npm test` (une fiche invalide fait échouer le test de chargement et indique le champ fautif).
7. **Relire les propositions** de `data/updates/proposals.jsonl` produites par le mode réel : chaque ligne indique la fiche, les nouvelles sources et les chiffres non retrouvés. Mettre la fiche à jour à la main, puis supprimer la ligne.

## 9. Limites techniques et documentaires

- La recherche locale est lexicale (mots et expressions-clés, sans accents) : une question formulée avec un vocabulaire très différent peut ne pas trouver la bonne fiche ; elle déclenche alors la recherche web en mode réel. Les seuils de « correspondance forte » sont réglés sur les tests, pas sur un usage réel.
- La comparaison web ↔ fiche repère des écarts (verdict, sources, nombres), pas des contradictions de fond : c'est un signal pour une relecture humaine.
- Une réponse construite sur une fiche reprend la formulation de la fiche ; si l'utilisateur pose une question voisine mais différente, il peut relancer une recherche fraîche.
- La base reflète l'état des sources au 29 octobre 2026 ; les fiches d'actualité vieillissent vite.
- Le coût réel par analyse en mode réel n'a pas pu être mesuré (pas de clé) ; la réponse directe sur fiche évite la phase de recherche web (la plus coûteuse) et ne facture que la phase de stratégie.
