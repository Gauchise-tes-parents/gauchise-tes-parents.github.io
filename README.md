# Gauchise tes parents

> Ils ont leurs certitudes. Tu as les sources.

Application web d'éducation populaire et de préparation au débat, assistée par IA, créée par **Marty Ducanda**.
Soutenir le projet : <https://fr.tipeee.com/martyducanda/>

L'utilisateur choisit une stratégie, un sujet, saisit l'affirmation entendue ; l'application **cherche en direct sur le Web**, ouvre les documents officiels, vérifie les références, puis construit la réponse :

- **GAGNER LE DÉBAT** : thèse, réplique immédiate, démonstration en 3 points, données qui marquent, réponses aux objections, raisonnements fallacieux, questions qui renversent la perspective, conclusion mémorable, dossier de preuves, démonstration orale de 30 s / 1 min / 3 min.
- **CONVAINCRE SANS BRAQUER** : hypothèses sur la préoccupation, reconnaissance sincère, terrain d'accord, faits un par un, pont vers une autre interprétation, solutions (avantages, limites, conditions), question ouverte, savoir s'arrêter.

Les deux modes partagent **le même dossier documentaire vérifié** : on passe de l'un à l'autre sans relancer la recherche.

Ligne éditoriale assumée de gauche, avec une règle non négociable : aucun fait, chiffre, titre, date, URL ou référence juridique inventé ; les données gênantes sont montrées ; les jugements de valeur et propositions politiques sont étiquetés comme tels.

---

## Nouveautés v14 (alpha)

- **Deux publics remplacent les deux stratégies** : « Électeur d'extrême droite convaincu » et « Indécis ». Chaque fiche est présentée selon le public choisi ; les nouvelles fiches contiennent en plus une réponse rédigée pour chacun (`publics`).
- **IA Gemini débranchée** (aucune dépense Google) : les nouvelles fiches sont rédigées chaque jour par Claude, avec des sources ouvertes et lues, et publiées après les tests. Journal : `rapports/journal-quotidien.md`. Outil : `node scripts/verifier-couverture.mjs`.

## Nouveautés v13

- **IA Gemini** : backend Cloudflare Worker (`worker/`) qui garde la clé `GEMINI_API_KEY` en secret, choisit lui-même les fiches pertinentes de la bibliothèque, appelle Gemini avec la recherche Google, et contrôle la réponse (aucun lien inventé, statut de chaque élément). Mise en service : `worker/README.md`. Tant que `GTP_IA_BASE` n'est pas renseigné, le site fonctionne comme avant, sans IA.
- **Confidentialité** : aucune géolocalisation, aucun historique automatique, aucune question conservée ni journalisée ; page « Confidentialité et sécurité » ; CSP dans la page statique. Audit : `AUDIT-CONFIDENTIALITE.md`. Rapport : `RAPPORT-V13.md`.

## Nouveautés v12

- **Les 20 questions fréquentes de la demande reçoivent une vraie réponse** (fiche qui répond au sujet, jamais une fiche voisine), dans les deux modes : `npm run rapport:v12` → `rapports/tests-20-questions.md`.
- **14 nouvelles fiches sourcées** : cartes Vitale, SMIC, héritage, fraude sociale et fiscale, temps de travail, retraite à 64 ans, emploi après 50 ans, syndicats, nationalité, accès à la propriété, location sans CDI, pauvreté et efforts, la gauche et les travailleurs, « grand remplacement ».
- **Domaines mobilisés** : une phrase peut toucher plusieurs domaines ; ils sont affichés dans l'analyse.
- **Sans fiche, la limite est dite** : analyse étiquetée « sans données sourcées », et rappel que la réponse documentée hors bibliothèque demande le mode connecté, qui n'est pas actif sur le site public.
- **Seules les phrases prêtes à l'emploi sont proposées** (fiche vérifiée) ; les autres sont comptées « en préparation ». Voir `RAPPORT-V12.md`.

## Nouveautés v11

- **Audit de cohérence** (`npm run audit:coherence`) : les 764 affirmations suggérées, traitées comme dans l'application ; plus aucune n'est envoyée vers une fiche d'un autre domaine (15 erreurs corrigées), 437 mènent à une fiche cohérente.
- **Règle de compatibilité** : une fiche trouvée par ressemblance de mots n'est retenue que si la phrase contient les notions de l'argument auquel elle répond.
- **Suggestions** : celles qui ont une fiche vérifiée passent devant, dans tous les modes et pour tous les profils.
- **10 nouvelles fiches sourcées** (homicides, loyers, passoires thermiques, AAH, ingérences, sondages, abstention, bilan de la gauche, histoire des migrations, accidents du travail). Voir `RAPPORT-V11.md`.

## Nouveautés v10

- **Ligne éditoriale assumée** (`public/js/ligne-editoriale.js`) : 17 principes de gauche (égalité, universalité des droits, solidarité, dignité, antiracisme, antifascisme…) et 8 règles de vérité, partagés par le moteur hors ligne et le mode connecté.
- **Lecture de gauche** dans chaque argumentaire : mécanismes, conséquences humaines, enjeu démocratique, valeurs, propositions (étiquetées comme telles) et faits défavorables honnêtement intégrés.
- **Fermeté sur la dignité humaine** : déshumanisation, appels à la violence, exclusion collective et antisémitisme sont signalés sans faux équilibre ; la critique d'une politique ne l'est pas.
- **Politique documentaire** : classement automatique des sources (autorité, complément, origine) et audit de chaque fiche ; les sources de droite ou partisanes ne valident jamais un fait sans attribution ; plus aucun fait ne repose sur une encyclopédie.
- **4 nouvelles fiches** (discriminations, égalité salariale, secours en mer, antisémitisme) et corrections documentaires. Ordre des scripts : générateurs → `npm run fiches:corriger` → `npm run enrichir`. Voir `RAPPORT-V10.md`.

## Nouveautés v9

- **La réponse avant la méthode** : chaque argumentaire suit le même ordre — 1. la réponse, 2. les preuves (avec « ce que ça montre »), 3. comment présenter l'argument, 4. comment aborder la discussion.
- **Deux modes réellement distincts** : « Gagner le débat » donne une riposte, une question piège et les objections, sans bloc d'empathie ; « Convaincre avec empathie » garde les mêmes faits et sources, puis propose une manière de les introduire sans braquer.
- **Express sans thématique** : les fiches de méthode (science du dialogue) ne servent plus jamais de réponse ; une correspondance faible n'est plus présentée comme une réponse ; le mode est visible sur l'accueil.
- **4 nouvelles fiches sourcées** : aider tout le monde, financement des services publics, la gauche et les impôts, les riches et l'emploi. Voir `RAPPORT-V9.md`.

## Nouveautés v8

- **Moteur d'analyse argumentative** (`public/js/analyse.js`, `public/js/cartographie.js`) : 38 concepts (428 mots-clés, expressions, synonymes, fautes), 37 arguments, 9 émotions, 12 procédés. Une phrase peut contenir plusieurs arguments ; chacun reçoit la fiche qui y répond vraiment, ou une lacune reconnue — jamais une fiche voisine présentée comme une réponse.
- **Panneau « Ce que contient la phrase »** : arguments, données sourcées, sous-entendus, liens de cause, émotions, procédés, phrase marquante, question, fiches écartées et pourquoi.
- **Métadonnées des fiches** (`npm run enrichir`) : concepts, arguments auxquels la fiche répond et ne répond pas, synonymes.
- **180 phrases de test** (`tests/comprehension/`, `npm run rapport:comprehension`) : voir `RAPPORT-V8.md` et `rapports/tests-comprehension.md`.

## Nouveautés v7

- **Suggestions spécialisées** : 764 affirmations à examiner réparties sur les 127 sous-thèmes (au moins 6 par sous-thème), choisies selon le mode, le cadre et l'interlocuteur, renouvelables avec « Autres affirmations », disponibles hors ligne, validées automatiquement (`auditSuggestions`).
- **Rubrique « Immigration, délinquance et prisons »** : 11 fiches sourcées (population carcérale, étrangers ≠ immigrés, mis en cause, causalité, droit de l'expulsion, OQTF, interdiction du territoire, protections, exécution).
- **Rebonds de conversation** : quand l'interlocuteur change d'argument (« peu importe les chiffres… »), le moteur bascule sur le nouveau terrain au lieu de recommencer. Bilan : [`RAPPORT-V7.md`](RAPPORT-V7.md).

## Nouveautés v6

- **Conversation continue, sans limite de tours** : après chaque réponse de l'interlocuteur (saisie libre, raccourcis facultatifs), l'application analyse la réaction à la lumière de tout l'historique et propose la suite, sans répéter ce qui a été dit. Seul l'utilisateur termine, avec le bouton « Conversation terminée », qui affiche un bilan personnalisé (arguments, accords, désaccords, sources). Mode autonome : moteur de règles local (`public/js/conversation.js`) ; mode connecté : `POST /api/conversation`, avec un résumé évolutif borné au lieu de tout l'historique.
- **Publication publique prête** : `bash scripts/publier-github.sh` (GitHub Pages, gratuit) ou `render.yaml` (version complète avec IA). Voir la section 0 de [`PUBLIER.md`](PUBLIER.md). Bilan : [`RAPPORT-V6.md`](RAPPORT-V6.md).

## Nouveautés v5

- **Moteur de personnalisation refait** (mode autonome, sans IA) : un plan explicite choisit l'approche (factuelle, historique ou institutionnelle, valeurs et conséquences), le point d'entrée, les preuves et leur ordre, le niveau de détail, la source mise en avant, l'objection, les questions, le ton, la conclusion et la prochaine étape. Toutes les options du questionnaire ont désormais un effet mesurable (une seule est neutre par conception) ; les faits ne changent jamais.
- **Questionnaire progressif** (10 dimensions, dont le niveau de connaissance) : 3 questions essentielles, la « question qui changerait le plus la réponse », le reste replié ; hypothèses corrigeables à tout moment ; arguments déjà avancés ; comparaison de 2 ou 3 approches ; 10 types de retours, en boutons ou en texte libre.
- **Référentiel scientifique** : 16 fiches « Science du dialogue » avec référence, auteurs, année, lien, conditions, limites et niveau de confiance.
- **150 scénarios synthétiques** exécutés automatiquement : `npm run rapport:personnalisation` → [`rapports/tests-personnalisation.md`](rapports/tests-personnalisation.md). Table de décision générée depuis le code : [`docs/MOTEUR-PERSONNALISATION.md`](docs/MOTEUR-PERSONNALISATION.md). Bilan complet : [`RAPPORT-V5.md`](RAPPORT-V5.md).

## Nouveautés v4

- **Mode autonome — sans Internet** : la bibliothèque (54 fiches), la recherche locale, le questionnaire sur l'interlocuteur et les deux stratégies fonctionnent hors ligne après la première visite (service worker). Les argumentaires sont **composés par un moteur de règles** à partir des fiches vérifiées : il n'y a pas de modèle d'IA embarqué et aucun fait n'est inventé.
- **Argumentation personnalisée** : questionnaire facultatif (9 dimensions + « je ne connais pas assez cette personne »), consignes justifiées par une bibliothèque « Science du dialogue » (14 fiches sourcées), version solide de l'argument adverse, adaptation après chaque échange.
- **Mode connecté** facultatif (recherche web, IA) ; plus aucun message d'erreur quand le serveur est volontairement absent.
- **Publication** : `npm run build:static` → `dist/site` (GitHub Pages / Cloudflare Pages), flux GitHub Actions fournis ; guide complet dans [`PUBLIER.md`](PUBLIER.md).
- **Veille automatique** toutes les 24 à 48 h (serveur ou GitHub Actions), règles de validation explicites, sauvegardes et retour arrière, tableau de bord.
- Détails, tests et limites : [`RAPPORT-V4.md`](RAPPORT-V4.md).

## Démarrage

Prérequis : **Node.js 20 ou plus**. Aucune dépendance npm.

```bash
cp .env.example .env          # renseigner ANTHROPIC_API_KEY pour le mode réel
npm start                     # http://127.0.0.1:3000
```

Sans clé : **mode démonstration**, signalé par une bannière. Aucune recherche n'est simulée, aucun verdict ni aucune riposte n'est produit ; la bibliothèque (fiches vérifiées à la main) reste consultable.

### Passer en mode réel (étapes)

1. Créer un compte sur <https://console.anthropic.com>, ajouter un moyen de paiement, créer une clé API.
2. Dans la console, vérifier que les outils serveur **web search** et **web fetch** sont autorisés pour l'organisation.
3. Recommandé : si ton organisation y a accès, fixer aussi une limite de dépenses mensuelle côté fournisseur (limites d'organisation ou d'espace de travail ; d'après la documentation d'Anthropic, cette fonction est en accès anticipé, sur demande). Les plafonds de l'application restent actifs dans tous les cas.
4. Copier `.env.example` en `.env`, renseigner `ANTHROPIC_API_KEY`, ajuster `DAILY_BUDGET_USD` et `MONTHLY_BUDGET_USD`.
5. `npm start` : le terminal doit afficher « Moteur : RÉEL ».
6. Faire 3 ou 4 analyses réelles en relisant les sources, et surveiller les lignes `[coût]` du journal.

### Aperçu statique

`npm run build:preview` produit `dist/apercu-statique.html` (un seul fichier, sans serveur, bibliothèque seulement).

---

## Architecture

```
server/
  index.js                 démarrage
  app.js                   HTTP sans dépendance : API, fichiers statiques compressés (gzip), en-têtes de sécurité
  config.js                variables d'environnement (+ lecture de .env)
  library.js               fiches : validation du schéma v3 (refus des pages d'accueil comme preuve), fraîcheur, filtres
  feedback.js              retours (JSONL, sans IP)
  rateLimit.js             limitation par IP (hachée, en mémoire)
  engine/
    providers/anthropic.js SEUL module lié au fournisseur : appel API, outils web_search + web_fetch,
                           reprise « pause_turn », conversion des réponses en preuves neutres
    research.js            phase 1 — recherche documentaire (consignes, budget de recherche)
    evidence.js            vérification des preuves : sources réellement obtenues, document ouvert ou simple
                           extrait, contrôle des chiffres dans le texte consulté, verdict rétrogradé sans source
    strategy.js            phase 2 — stratégie « gagner » / « convaincre », sans recherche, à partir du dossier ;
                           références contrôlées, nature des arguments, chiffres inventés signalés
    speech.js              démonstration orale et reformulations (chiffres contrôlés)
    knowledge.js           base locale d'abord : décision fiche seule / complément web, comparaison web ↔ fiche,
                           propositions de mise à jour (data/updates/proposals.jsonl, jamais appliquées seules)
    pipeline.js            orchestration, cache des dossiers, mémoire des analyses, facturation mesurée
    cost.js                tarifs, calcul du coût réel, budget journalier/mensuel persistant
    options.js             validation des requêtes
    util.js, demo.js
public/
  index.html, css/styles.css   interface mobile d'abord (barre d'onglets en bas, zones de sécurité)
  js/taxonomy.js           SOURCE UNIQUE : modes, 10 volets, 3 rubriques, fiabilités, onglets de fiche (serveur + client)
  js/kbsearch.js           recherche locale partagée serveur / navigateur (accents, mots-clés, score, force)
  js/app.js                routeur, parcours, réponse express, résultats, thématiques, bibliothèque
  js/art.js                illustrations SVG originales ; js/copy.js microtextes ; js/api.js
data/library/*.json        base de connaissances : une fiche par fichier (40 fiches)
scripts/fiches/            scripts qui génèrent les fiches v3 depuis des sources lues (traçabilité)
tests/unit, tests/e2e      tests node:test et Playwright
```

**Remplacer le fournisseur** : écrire un module qui expose `complete({ model, system, user, tools, maxTokens })` et renvoie `{ text, evidence, requests }` (format neutre décrit dans `providers/anthropic.js`), puis le passer à `createApp`. Le reste (vérification, stratégie, interface) ne change pas.

### API

| Route | Rôle |
|---|---|
| `GET /api/status` | mode (démo/réel), outils, budget disponible |
| `POST /api/analyse` | `{affirmation, volet, sous_theme?, mode, profil?, contexte?, express?, fraiche?}` → dossier vérifié + stratégie |
| `POST /api/strategie` | `{analyse_id \| fiche_id, mode, profil?, contexte?}` → autre stratégie, **sans nouvelle recherche** |
| `POST /api/demonstration` | `{analyse_id, duree: 30\|60\|180, mode}` → texte oral + version spontanée |
| `POST /api/reformuler` | `{analyse_id, variante: variante\|pedagogique}` |
| `GET /api/kb/search?q=` | base locale : fiches correspondantes (force « forte » / « partielle ») et décision « complément web ou non », sans coût |
| `GET /api/library[?q&volet&sous_theme&rubrique&fiabilite]`, `GET /api/library/:id` | bibliothèque, avec fraîcheur |
| `POST /api/feedback` | avis, signalement de source, erreur |

---

## Variables d'environnement

Voir `.env.example` (toutes commentées). Principales :

| Variable | Défaut | Rôle |
|---|---|---|
| `ANTHROPIC_API_KEY` | vide | vide = démo ; jamais exposée au navigateur |
| `RESEARCH_MODEL` / `STRATEGY_MODEL` | `claude-sonnet-5-5` | modèles des deux phases |
| `MAX_SEARCHES_PER_ANALYSIS` / `MAX_FETCHES_PER_ANALYSIS` | 6 / 3 | recherches et documents ouverts par analyse |
| `MAX_SEARCHES_EXPRESS` / `MAX_FETCHES_EXPRESS` | 3 / 1 | idem en réponse express |
| `DAILY_BUDGET_USD` / `MONTHLY_BUDGET_USD` | 3 / 30 | **plafonds financiers** sur la consommation mesurée |
| `ESTIMATE_RESEARCH_USD` / `ESTIMATE_STRATEGY_USD` | 0,35 / 0,06 | marge vérifiée avant chaque appel |
| `CACHE_TTL_HOURS` | 12 | réutilisation d'un dossier identique |
| `PER_IP_ANALYSIS_LIMIT` / `PER_IP_STRATEGY_LIMIT` / `PER_IP_WINDOW_MINUTES` | 5 / 20 / 10 | anti-abus |
| `LIBRARY_STALE_DAYS` | 365 | ancienneté au-delà de laquelle une fiche est « à actualiser » |
| `KB_DIRECT_ANSWER` | 1 | 0 = toujours lancer la recherche web, même si une fiche forte et à jour existe |
| `UPDATES_FILE` / `STORE_UPDATES` | `data/updates/proposals.jsonl` / 1 | propositions de mise à jour des fiches |

---

## Coûts

Tarifs Anthropic relevés le 29 octobre 2026 (<https://platform.claude.com/docs/en/about-claude/pricing>) et intégrés dans `server/engine/cost.js` :

| | Entrée | Sortie |
|---|---|---|
| claude-sonnet-5-5 | 2 $ / M jetons | 10 $ / M jetons |
| claude-haiku-5-5 | 0,10 $ / M (0,50 $ au-delà de 100 000 jetons de prompt) | 0,50 $ / M (2,50 $) |
| claude-opus-5-5 | 4 $ / M | 20 $ / M |
| Recherche Web | 10 $ / 1 000 recherches | |
| Consultation de page (web fetch) | pas de supplément, seuls les jetons du contenu lu comptent | |

**Ordres de grandeur (estimation, non mesurée faute de clé)** pour une analyse complète avec Sonnet : 6 recherches (0,06 $) + 30 000 à 60 000 jetons d'entrée (pages lues, résultats, reprises) soit 0,06 à 0,12 $ + ~3 000 jetons de sortie (0,03 $), puis la stratégie (~0,02 à 0,03 $). Soit **environ 0,15 à 0,25 $ par analyse**, et quelques centimes pour un changement de mode, une démonstration ou une reformulation. Avec `STRATEGY_MODEL=claude-haiku-5-5`, la phase 2 devient quasi gratuite.

Le coût **réel** de chaque analyse est calculé à partir de la consommation renvoyée par l'API, affiché dans « Coulisses de la recherche », journalisé (`[coût] …`) et imputé au budget journalier/mensuel, qui survit aux redémarrages (`data/usage/budget.json`). Le cache évite de payer deux fois la même recherche.

---

## Base de connaissances

**67 fiches** vérifiées (51 fiches thématiques + 16 fiches « Science du dialogue ») (détail, méthode et limites : `RAPPORT-V3.md`). Trois rubriques transversales :
« Patriotisme de gauche » (8), « Islamo-gauchisme, laïcité et instrumentalisation » (7) et « Mélenchon crie, il est agressif, il est dangereux » (11, en cinq parties), plus des fiches générales (économie, immigration, sécurité, histoire, écologie, médias et démocratie).

Chaque fiche contient : type, volet et sous-thème, rubriques, mots-clés, affirmation, contexte, explication grand public, faits (avec niveau de fiabilité), argumentaires court / moyen / détaillé / avec empathie, contre-arguments et réponses, questions, limites, sources précises (titre, organisme, date, URL, passage, `consultee`), citations vérifiées le cas échéant, `fiabilite` (établi / estimation / interprétation / débat), `stabilite` (historique / évolutive / actualité), `derniere_verification`, `a_actualiser_le`. Le verdict est facultatif : un débat n'a pas toujours de verdict binaire.

**Parcours d'une question** : recherche dans la base locale (affichée tout de suite, même pendant l'analyse) → fiche forte et stable ou à jour : réponse construite sur la fiche, sans recherche web → sinon (actualité, fiche à actualiser, sujet mal couvert, « recherche fraîche ») : recherche web, avec les sources de la fiche comme pistes, puis comparaison web ↔ fiche (verdict, nouvelles sources, chiffres non retrouvés). Un écart produit une proposition dans `data/updates/proposals.jsonl` ; **aucune fiche n'est modifiée automatiquement**.

Ajouter ou enrichir une fiche : voir « Enrichir la base » dans `RAPPORT-V3.md`. Le schéma est validé au chargement et par `npm test` (une fiche invalide est ignorée et signalée dans les journaux).

---

## Tests

```bash
npm test          # unitaires + intégration (aucune dépendance)
npm run test:e2e  # navigateur (Playwright requis : npm i -D playwright && npx playwright install chromium)
npm run test:all
npm run test:personnalisation     # 150 scénarios du moteur de personnalisation
npm run rapport:personnalisation  # régénère rapports/tests-personnalisation.md
npm run doc:moteur                # régénère docs/MOTEUR-PERSONNALISATION.md
```

Les tests du mode réel utilisent un **service d'IA simulé** (réponses au format documenté). Ils valident tout le traitement côté serveur et l'interface, **pas** la qualité d'une recherche réelle.

---

## Sécurité et confidentialité

Clé uniquement côté serveur ; CSP stricte sans script en ligne ; entrées bornées et listes fermées ; erreurs sans détail technique ; pas de base de données, de cookie ni de traceur ; IP hachées en mémoire pour l'anti-abus ; dossiers d'analyse gardés en mémoire vive une heure au plus puis oubliés ; aucune question, conversation ni consultation conservée automatiquement (seuls les choix de parcours restent dans l'onglet) ; aucune géolocalisation ; journaux sans question ni IP ; retours sans IP. Audit complet : `AUDIT-CONFIDENTIALITE.md`. Politique lisible dans l'application (`#/confidentialite`).

---

## Crédits

Conception : Marty Ducanda. Illustrations originales générées en SVG (personnages fictifs). Police Poppins (SIL Open Font License 1.1).
