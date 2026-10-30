# Rapport v4 — Mode hors ligne, argumentation sur mesure, publication et veille

Mise à jour du projet existant, réalisée le 29 octobre 2026. Les chiffres ci-dessous ont été comptés sur les fichiers et les tests ont été réellement exécutés.

## 1. Ce qui a été fait

### Mode autonome — sans Internet
- **Choix d'architecture** : moteur de recherche et de composition fondé sur la bibliothèque locale (options 1 et 2 de la demande). **Aucun modèle de langage n'est embarqué** : un modèle exécuté dans le navigateur pèserait plusieurs centaines de mégaoctets, serait lent sur téléphone et pourrait inventer des faits, ce qui contredit la règle du projet. Architecture hybride : la bibliothèque et les argumentaires composés marchent hors ligne ; la recherche web et la rédaction par IA restent en mode connecté.
- **Base locale** : `kb/base.json` (54 fiches, empreinte SHA-256 dans `kb/manifest.json`), servie par le serveur ou par le site statique, mise en cache par un service worker avec l'interface (`public/sw.js`, liste des fichiers dans `asset-manifest.json`).
- **Mise à jour de la base** : vérification de la version quand le réseau est là ; téléchargement ; contrôle de l'empreinte et de la structure (faits rattachés à des sources consultées) ; remplacement seulement après validation. L'ancienne base n'est jamais supprimée avant. Réglage « installer automatiquement », date de dernière actualisation affichée.
- **Fonctions hors ligne** : bibliothèque et filtres, recherche locale instantanée, fiches à sept onglets, questionnaire, deux stratégies composées, adaptation après chaque échange, historique des fiches consultées, argumentaires et profils enregistrés (sur l'appareil, supprimables).
- **Ancienneté des données** : chaque argumentaire indique « fait historique stable », « statistiques vérifiées le … : elles ont pu évoluer » ou « données à actualiser ».
- **Question non couverte** : « La bibliothèque locale ne contient pas encore cette information », sans fausse erreur de connexion.

### Argumentation personnalisée
- **Bibliothèque « Science du dialogue »** : 14 fiches, 23 sources consultées, 27 faits (réactance, autodétermination, raisonnement motivé, effet boomerang, effets modestes de la persuasion, identité sociale, valeurs morales, menace et « biologie » des opinions, entretien motivationnel et écoute, dissonance, socialisation familiale, désinformation et confiance, délibération, persuasion et manipulation). Chaque fiche indique sa **robustesse** : 9 robustes, 3 modérées, 2 discutées. Les controverses sont signalées (biais égal entre camps contesté ; réplication qui invalide l'étude de 2008 sur la « biologie » des conservateurs ; révision de la théorie des fondements moraux).
- **Questionnaire** : 9 dimensions (rapport au débat, aux faits, aux institutions, au changement, valeurs prioritaires, rapport à la politique, lien, contexte, objectif), toutes facultatives, plus « Je ne connais pas assez cette personne » (profil neutre et questions ouvertes d'abord). Présenté comme des hypothèses de travail.
- **Consignes** : 18 règles (`public/js/profile.js`) ; chacune renvoie à une fiche scientifique qui la justifie, consultable depuis l'argumentaire (« Pourquoi cette stratégie »).
- **Deux stratégies toujours produites** : « Gagner le débat » (réponse courte, preuve(s), charge de la preuve, phrase pour le public, recentrage, conclusion) et « Convaincre avec empathie » (questions d'abord, reformulation, valeur commune, faits un par un, ce qu'il faut reconnaître, autonomie, sortie). Les deux commencent par **la version la plus solide de l'argument adverse**, tirée de la fiche.
- **Adaptation progressive** : six retours (a écouté, s'est braquée, a demandé des preuves, a changé de sujet, a reconnu un point, discussion terminée) ; la proposition suivante s'appuie uniquement sur cette observation, avec la mention « indication approximative ».
- **Mode connecté** : le profil est transmis au moteur IA sous forme de consignes (validées en listes fermées).

### Messages d'erreur liés au serveur
- Supprimés : le bandeau « Mode démonstration / le serveur ne répond pas » et toute alerte quand le serveur est volontairement absent. Le serveur n'est interrogé qu'en mode connecté.
- Remplacés par une pastille d'état : « Autonome », « Connecté » ou « Connecté · non configuré ». Les vraies erreurs (panne après déploiement, échec de sauvegarde, refus d'une base corrompue) restent affichées.

### Publication et partage
- Page **« Publier et partager »** dans l'application (adresse à copier, bouton de partage, avertissement si l'adresse est locale, checklist, coûts) et guide développeur **`PUBLIER.md`** (structure, commandes, variables, GitHub Pages pas à pas, Cloudflare Pages, serveur Render, coûts et quotas vérifiés dans la documentation des hébergeurs, sécurité, checklist).
- `npm run build:static` → `dist/site/` (chemins relatifs : fonctionne dans un sous-dossier GitHub Pages ; `.nojekyll`, `404.html`, `config.js` pour l'adresse facultative du serveur).
- Flux GitHub Actions : `.github/workflows/pages.yml` (tests puis publication) et `.github/workflows/veille.yml` (veille planifiée).
- **Rien n'a été publié** : aucune adresse publique n'existe encore (étapes restantes au § 6).

### Veille automatique
- Module `server/watch/veille.js`, ligne de commande `scripts/veille.js`, tableau de bord « Veille et actualisations ».
- Détails au § 3.

## 2. Fichiers créés ou modifiés

**Créés** : `public/sw.js`, `public/config.js`, `public/js/kbstore.js`, `public/js/store.js`, `public/js/profile.js`, `public/js/composer.js`, `server/kbexport.js`, `server/watch/veille.js`, `scripts/build-static.js`, `scripts/veille.js`, `scripts/fiches/science_dialogue.py`, 14 fiches `data/library/sci-*.json`, `.github/workflows/pages.yml`, `.github/workflows/veille.yml`, `tests/unit/composer.test.js`, `tests/unit/veille.test.js`, `tests/unit/build.test.js`, `PUBLIER.md`, `RAPPORT-V4.md`.

**Modifiés** : `public/index.html` (chemins relatifs, pastille de mode, liens), `public/manifest.webmanifest`, `public/css/styles.css`, `public/js/app.js` (mode autonome, questionnaire, argumentaire composé, pages Mode / Mes données / Publier / Veille), `public/js/api.js` (bibliothèque toujours locale, serveur facultatif), `public/js/kbsearch.js` (fraîcheur partagée), `public/js/taxonomy.js` (rubrique « Science du dialogue », questionnaire, retours, robustesse), `server/app.js` (base téléchargeable, API de veille, planificateur, CORS facultatif), `server/library.js`, `server/engine/{options,strategy,pipeline}.js`, `scripts/build-preview.js`, `package.json`, `.env.example`, `.gitignore`, `README.md`, tests existants (`helpers`, `knowledge`, `e2e/ui`).

## 3. Veille : mécanisme réellement mis en place

| Élément | Réalisation |
|---|---|
| Planification | **Deux options prêtes, aucune active ici** : (1) GitHub Actions `veille.yml`, `cron: '17 4 * * *'` = toutes les 24 h (48 h : `'17 4 */2 * *'`) ; (2) planificateur intégré au serveur Node (`WATCH_ENABLED=1`, `WATCH_INTERVAL_HOURS` borné à 24-48). |
| Fréquence réelle | **Aucune pour l'instant** : le projet n'est pas déployé et aucun planificateur n'est configuré. Cible par défaut : 24 h. |
| Catégories surveillées | politique française, politique européenne, géopolitique, économie, société, écologie et énergie, histoire et mémoire, sciences sociales (`WATCH_CATEGORIES` pour restreindre). |
| Sources privilégiées | institutionnelles (Insee, DREES, DARES, Eurostat, OCDE, Assemblée, Sénat, Légifrance, Conseil constitutionnel, ministères…), puis scientifiques, puis médias fiables ; partisanes identifiées comme telles. |
| Données conservées | titre, organisme, URL exacte, date de publication, date de consultation, période des faits, résumé factuel, fiabilité, limites, fiches concernées, effet sur l'argument. |
| Règles de validation | URL réellement obtenue pendant la recherche ; date valide et non future ; fiche concernée ; « vérifiée » si source institutionnelle ou scientifique, ou deux sources indépendantes obtenues ; sinon « en attente » ; sujets sensibles (déclarations, citations, accusations, rubriques Mélenchon/LFI et islamo-gauchisme) **toujours en attente de validation humaine**. |
| Modifications | désactivées par défaut. `WATCH_AUTO_APPLY=1` : ajout d'une nouvelle valeur officielle **à côté de l'ancienne**, seulement si le chiffre figure dans le document officiel consulté ; sauvegarde préalable, revalidation, fiche marquée « à actualiser ». Le texte des argumentaires n'est jamais réécrit automatiquement (« statistiques remplacées » reste à 0 tant qu'un humain ne l'a pas fait). |
| Robustesse | verrou anti-exécutions simultanées (repris s'il est abandonné), nouvelles tentatives par catégorie, catégorie en échec isolée, reprise après échec (1 h, 2 h, 4 h…), dédoublonnage par URL. |
| Coûts | plafond par cycle (`WATCH_MAX_USD_PER_RUN`, 1,5 $ par défaut), plafonds journalier et mensuel du serveur, coût mesuré inscrit dans chaque compte rendu. |
| Traces | journal `data/watch/veille.log.jsonl`, comptes rendus JSON et Markdown, file `a-valider.jsonl`, état `state.json`, notification facultative en cas d'échec. |
| Retour arrière | `node scripts/veille.js --retour <fiche> [horodatage]` ; sauvegardes dans `data/library-history/` ; historique Git avec GitHub Actions. |
| Sécurité | pages web traitées comme des données ; seuls les champs attendus sont lus et tronqués ; identifiants de fiche inconnus ignorés ; lancement manuel protégé par jeton (comparaison à temps constant). |
| Hors ligne | la base mise à jour est publiée avec une nouvelle version et une empreinte ; l'application la vérifie avant de remplacer l'ancienne. |

## 4. Tests exécutés (29 octobre 2026)

- **`npm test` : 112 tests, 112 réussis** (dont 26 nouveaux : 10 compositeur et questionnaire, 14 veille, 2 publication).
  - Compositeur : neuf dimensions et nettoyage des valeurs hors liste ; chaque consigne renvoie à une fiche scientifique existante ; profils contrastés → consignes différentes ; **aucun chiffre inventé** (tous les nombres des argumentaires composés figurent dans la fiche, pour les 54 fiches et trois profils) ; deux stratégies et version solide pour chaque fiche ; adaptation pour les six retours ; profil transmis au moteur connecté ; contrôle d'intégrité de la base.
  - Veille : règles de rejet, de vérification et de validation renforcée ; **exécution manuelle complète avec un fournisseur simulé** (3 éléments collectés : 1 page inventée rejetée, 2 vérifiés, 1 nouvelle valeur ajoutée avec ancienne valeur conservée, sauvegarde, compte rendu, file de validation, état) ; second passage = doublons ignorés ; retour arrière ; aucune modification sans `WATCH_AUTO_APPLY` ; verrou ; source indisponible avec nouvelles tentatives et notification ; plafond de coût ; calcul de la prochaine exécution ; API protégée par jeton ; empreinte de la base téléchargeable.
  - Publication : `build:static` produit un site complet, chemins relatifs, empreinte vérifiable, aucun secret dans les fichiers publiés ; adresse de serveur invalide refusée.
- **`npm run test:e2e` (Chromium) : 23 tests, 23 réussis**, dont : parcours complet en mode autonome avec questionnaire ; argumentaire (deux stratégies, consignes justifiées, retours, enregistrement puis suppression) ; question non couverte sans message de connexion ; passage au mode connecté sans serveur (signalé, non bloquant) ; pages Publier et Veille ; **hors ligne réel avec service worker** (mode avion : accueil, 54 fiches, argumentaire) ; mode connecté simulé (recherche web, changement de stratégie, relance après panne) ; aucun débordement horizontal de 320 à 412 px ; aucune erreur JavaScript.
- **Vérifications manuelles** : site statique servi **dans un sous-dossier** comme sur GitHub Pages, puis mode avion → bibliothèque et argumentaire disponibles ; mise à jour de la base **refusée** avec un manifeste falsifié (« empreinte invalide : base conservée ») et **acceptée** pour une version légitime (« intégrité vérifiée ») ; captures d'écran sur téléphone (argumentaire, questionnaire, page Mode).
- **Exécution manuelle de la veille réelle** : `node scripts/veille.js` a été lancé ; faute de clé API dans cet environnement, il s'arrête avec le message « Veille non exécutée : aucune clé ANTHROPIC_API_KEY configurée. Rien n'est simulé. » (code 2). Le cycle complet n'a donc été exécuté qu'avec un fournisseur simulé ; aucune recherche web réelle n'a été faite par la veille.

## 5. Limites

- Le compositeur hors ligne assemble des contenus existants : il ne reformule pas librement et ne répond pas à une question absente de la bibliothèque (54 fiches). La recherche locale est lexicale.
- Les profils d'interlocuteur décrivent des tendances moyennes issues d'études souvent américaines ; ils orientent la manière de discuter, sans garantie d'effet.
- Plusieurs fiches scientifiques s'appuient sur des résumés d'articles ou des présentations (signalé dans leurs limites).
- Le hors-ligne exige une première visite en ligne sur un navigateur compatible avec les service workers, et un site servi en https (ou localhost) ; il n'est pas disponible dans l'aperçu en un seul fichier.
- Sur un hébergement statique, la veille dépend de GitHub Actions : dans un dépôt public, les tâches planifiées sont désactivées après 60 jours sans activité du dépôt.
- Validation humaine nécessaire pour tout ce qui est « en attente » et pour réécrire un argumentaire après une nouvelle statistique.

## 6. Étapes restant à ta charge

1. Créer le dépôt GitHub public et envoyer le code (`PUBLIER.md`, § 3).
2. Activer GitHub Pages (Source : GitHub Actions) et récupérer l'adresse publique.
3. Tester depuis un autre téléphone et un autre réseau, puis en mode avion.
4. (Facultatif, mode connecté) déployer le serveur Node, renseigner `ANTHROPIC_API_KEY`, `CORS_ORIGIN`, puis la variable `GTP_API_BASE` du dépôt.
5. (Facultatif, veille) ajouter le secret `ANTHROPIC_API_KEY` au dépôt, régler `WATCH_MAX_USD_PER_RUN`, lancer une première fois *Actions → Veille automatique → Run workflow*, puis relire le compte rendu et la file `data/watch/a-valider.jsonl`.
6. Fixer un plafond de dépenses dans la console du fournisseur d'IA.
