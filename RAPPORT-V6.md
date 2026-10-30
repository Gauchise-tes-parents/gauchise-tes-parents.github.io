# Rapport v6 — Publication publique et conversation continue

Date : 30 octobre 2026. Tous les résultats ci-dessous viennent de tests **réellement exécutés** dans l’environnement de développement.

## 1. Publication : ce qui a été fait, ce qui bloque

**Aucune URL publique n’a été créée.** L’environnement de travail n’a aucun accès de déploiement :
- aucun compte GitHub n’est relié à la session ;
- le jeton GitHub disponible est invalide (`gh auth status` : « The token in GH_TOKEN is invalid ») ;
- les API de Netlify, Cloudflare, Vercel, Render et Surge sont injoignables depuis le poste de travail (réseau filtré).

Créer un compte d’hébergement au nom du propriétaire n’est ni possible ni souhaitable. Le projet a donc été préparé pour que la publication se fasse en une commande.

**Architecture vérifiée avant de choisir :**
- **Interface** : JavaScript natif, sans dépendance. Les chemins sont relatifs : le site fonctionne dans un sous-dossier, comme sur GitHub Pages.
- **Hors ligne** : assuré par un service worker.
- **Base de connaissances** : téléchargée, avec contrôle d’intégrité.
- **Serveur** : Node 22, sans dépendance. Il sert l’interface et l’API du mode connecté. La clé `ANTHROPIC_API_KEY` reste uniquement côté serveur.
- **Fonctions qui exigent un serveur** : recherche web, rédaction par IA, conversation en mode connecté, veille déclenchée par le serveur, retours d’utilisateurs.
- **Ce qui fonctionne sans serveur** : la bibliothèque, les argumentaires sur mesure et la **conversation continue**, grâce au moteur local.

**Deux options prêtes :**

| | A. GitHub Pages (recommandé pour commencer) | B. Render (version complète avec IA) |
|---|---|---|
| Fichiers | `scripts/publier-github.sh`, `.github/workflows/pages.yml` | `render.yaml` |
| Coût | gratuit | serveur gratuit + IA facturée à l’usage |
| Accès | ouvert à tous, sans compte | ouvert à tous, sans compte |
| URL | `https://COMPTE.github.io/gauchise-tes-parents/` | `https://gauchise-tes-parents.onrender.com` (selon le nom disponible) |
| Mise à jour | `git push` → republication automatique après les tests | `git push` → redéploiement automatique |

**Ce qui a été testé localement**
- **Script de publication** : exécuté sur une copie du projet, avec un outil GitHub simulé. Résultats :
  - les tests sont lancés ;
  - le dépôt Git est créé ;
  - `.env`, `data/usage` et `data/feedback` ne sont pas suivis ;
  - les commandes de création du dépôt et d’activation de Pages sont émises ;
  - l’URL est affichée.

  Il n’a pas pu être exécuté contre le vrai GitHub.
- **Site statique publié** (`dist/site`) : servi sous un sous-chemin `/depot/` comme sur GitHub Pages, dans deux contextes de navigateur neufs (équivalents à une navigation privée) :
  - téléphone (375 px), conversation de 5 échanges **hors ligne** puis bilan : aucune erreur, aucun débordement ;
  - ordinateur (1280 px), même parcours en ligne : aucune erreur, aucun débordement.
- **Fichiers de configuration** : `render.yaml` et les workflows sont des YAML valides. Le flux de veille ne s’exécute plus sans secret (avis au lieu d’un échec quotidien).

**Protections pour un accès public (mode connecté)**
- Aucune clé dans le navigateur ni dans le dépôt : le script refuse de publier s’il détecte une clé.
- Limitation par adresse IP : analyses, stratégies, et désormais tours de conversation (40 par fenêtre de 10 minutes par défaut).
- Plafond **global** de tours de conversation : 400 par heure par défaut, 300 dans `render.yaml`.
- Plafonds de budget journalier et mensuel.
- Messages limités à 1 000 caractères, résumé à 3 000 caractères, 6 derniers échanges au plus.
- Le mode autonome est utilisé par défaut et ne coûte rien.

Sur l’offre gratuite de Render, le disque est éphémère : le compteur de budget repart de zéro à chaque redémarrage. Il faut donc aussi un plafond dans la console Anthropic (indiqué dans `PUBLIER.md` et `render.yaml`).

## 2. Conversation continue : où était la limite

| Couche | Constat dans le code v5 | Correction |
|---|---|---|
| Moteur local (`suite()`) | « Se braque » une deuxième fois → « on s’arrête là » ; « change de sujet » une deuxième fois → abandon du sujet ; « elle écoute » → « tous les faits ont été présentés », sans suite. | Nouveau moteur `public/js/conversation.js` sans fin automatique. Si la bibliothèque est épuisée, il le dit et propose une question, un résumé, une recherche fraîche ou de conclure. La conversation reste ouverte. |
| Interface | Une liste de boutons de retour. Le texte libre non reconnu donnait « je n’ai pas reconnu », une impasse. Rien n’était conservé au rechargement. | Fil de conversation, saisie libre « Il ou elle m’a répondu… » et 6 raccourcis facultatifs. Tout texte reçoit une réponse : un argument inconnu est traité comme tel, honnêtement. La conversation survit à un rechargement. |
| Serveur et prompts | Aucune route de conversation à plusieurs tours en mode connecté. Aucune limite de tours côté serveur. | `POST /api/conversation` : un tour, envoyé avec un résumé évolutif et les 6 derniers échanges, sans aucune limite de tours. |
| API | Limites par IP sur l’analyse et la stratégie seulement. | Limites techniques dédiées (IP, global, budget, taille), annoncées clairement à l’utilisateur. |

## 3. Le moteur conversationnel

**Boucle.** Elle suit cinq étapes :
1. Le sujet et l’argumentaire existants servent de premier échange.
2. L’utilisateur rapporte la réaction de son interlocuteur.
3. Le moteur l’analyse à la lumière de l’historique.
4. Il propose la prochaine intervention.
5. Le cycle recommence, jusqu’à ce que l’utilisateur appuie sur « Conversation terminée ».

**Réactions reconnues** (lecture par mots-clés, présentée comme approximative) :
- demande de source ;
- chiffre ou méthode contestés ;
- objection nouvelle ou déjà discutée ;
- désaccord partiel : sur les causes, sur la solution, ou « oui, mais… » ;
- reconnaissance d’un point ;
- changement de sujet ;
- provocation ;
- incompréhension ;
- hésitation ;
- évolution de l’opinion ;
- essoufflement ;
- volonté de clore ;
- braquage ;
- désaccord général ;
- argument non répertorié ;
- « je ne sais pas quoi répondre ».

Une relance comme « encore une ? » est rattachée à la demande précédente.

**Adaptation à chaque réaction :**
- **Demande de preuve** : une nouvelle source, avec ce qu’elle démontre et ses limites. Quand il n’en reste plus, le moteur le dit au lieu d’en inventer.
- **Chiffre contesté** : définition, période, périmètre et organisme du fait visé. Ce fait est retrouvé grâce au nombre cité, à l’organisme nommé ou aux mots employés.
- **« Oui, mais… »** : la partie acceptée est enregistrée comme point d’accord, sans être répétée ; la discussion porte sur la réserve. Si la réserve correspond à une autre fiche, celle-ci est proposée.
- **Problème admis, solution contestée** : passage à la comparaison des solutions et de leurs limites.
- **Braquage** : formulation apaisée, puis pause, puis écoute. La conversation n’est jamais fermée.
- **Changement de sujet** : deux choix, répondre au nouveau sujet (une fiche trouvée) ou revenir au point initial. Le sujet initial reste dans l’historique.
- **Objection répertoriée** : la réponse vérifiée de la fiche, et le point légitime à reconnaître.
- **Provocation** : réponse ferme, courte, un seul fait, sans escalade.

Le mode choisi (« Gagner le débat » ou « Convaincre avec empathie ») change la formulation à chaque tour. Il suit l’onglet ouvert.

**Mémoire structurée.** La conversation retient :
- le sujet initial ;
- l’objectif ;
- les hypothèses sur l’interlocuteur, séparées et marquées « non vérifiées » ;
- les informations données par l’utilisateur ;
- les propos rapportés, séparés des faits ;
- les arguments présentés ;
- les sources citées ;
- les objections ;
- les points d’accord, avec leur origine : rapporté ou déduit ;
- les points contestés ;
- les questions posées ;
- les incertitudes ;
- les corrections d’hypothèses.

Anti-répétition : une même intervention n’est jamais proposée deux fois. Envoyer deux fois de suite le même message demande une confirmation, pour éviter les boucles involontaires.

**Résumé évolutif.** Il est recalculé à chaque tour et limité à 2 500 caractères. En mode connecté, le serveur reçoit ce résumé et les 6 derniers échanges, pas tout l’historique : la taille de la requête reste stable, même après 40 échanges.

**Mode connecté.** Les faits, chiffres et sources affichés sont reconstruits à partir de la bibliothèque, pas à partir du texte du modèle. Un chiffre absent des sources vérifiées est **signalé** à l’utilisateur. En cas d’erreur :
- le vrai message d’erreur s’affiche ;
- le message saisi est conservé ;
- deux boutons sont proposés : « Réessayer » et « Continuer avec le moteur hors ligne ».

Aucune réponse n’est simulée.

**Clôture.** Le bouton « Conversation terminée » est discret : c’est un bouton secondaire, accompagné de la mention « Quand tu veux : rien ne s’arrête tout seul ». Il n’est jamais déclenché automatiquement.

Le message de clôture est personnalisé :
- **discussion constructive** : il valorise le dialogue ;
- **sources citées** : il souligne l’importance des faits ;
- **point reconnu** : il le cite, sans l’exagérer ;
- **discussion tendue** : il félicite l’utilisateur d’avoir essayé et rappelle qu’on peut poser des limites ;
- **désaccord persistant** : il rappelle que ce n’est pas un échec.

Il n’affirme jamais un changement d’avis.

Le bilan présente aussi les arguments abordés, les points d’accord et de désaccord, et les sources (avec leurs liens). On peut y revoir tous les échanges, puis lancer une nouvelle conversation dans un contexte séparé ; une reprise est possible en cas de clic par erreur. L’historique n’est pas effacé avant la consultation du bilan.

## 4. Résultats des tests au-delà de deux échanges

`npm test` : **144 / 144 réussis**, dont 21 nouveaux tests de conversation. `npm run test:e2e` : **26 / 26 réussis**, exécuté deux fois de suite, dont 2 nouveaux tests de bout en bout.

| Scénario demandé | Test | Résultat |
|---|---|---|
| 1. Trois échanges | unitaire | réussi |
| 2. Cinq échanges | unitaire (mode empathique) | réussi |
| 3. Dix échanges | unitaire (15 échanges puis un 16e) et navigateur (12 échanges) | réussi |
| 4. Plusieurs changements d’argument | unitaire : 3 sujets successifs reconnus, bascule, sujet initial conservé | réussi |
| 5. Demandes de sources successives | unitaire : 5 demandes, jamais deux fois la même source, épuisement annoncé | réussi |
| 6. Reconnaît un point puis en conteste un autre | unitaire : accord enregistré, point accepté non répété, chiffre contesté retrouvé | réussi |
| 7. Reprise après une erreur temporaire | serveur (service d’IA simulé : 529 puis succès) et navigateur (bouton « Réessayer », message conservé, aucun tour simulé) | réussi |
| 8. Longue conversation, résumé actualisé | unitaire : 40 échanges, résumé différent à chaque tour, ≤ 2 500 caractères, charge serveur < 9 Ko | réussi |
| 9. Interruption volontaire | unitaire (reprise depuis l’état sérialisé) et navigateur (rechargement de l’onglet après 11 échanges, puis 12e échange) | réussi |
| 10. « Conversation terminée » | unitaire et navigateur : bilan fidèle (arguments, sources, accord, désaccord), nouvelle conversation vide | réussi |

**Vérifications transversales, toutes exécutées :**
- **Clôture non imposée** : le bouton n’est pas le bouton principal, et aucun bilan n’apparaît tant que l’utilisateur ne le demande pas.
- **Saisie toujours ouverte** : la zone de saisie reste disponible après chaque échange.
- **Prise en compte des nouveaux messages** : un message en plus produit un tour en plus, et son type est reconnu (15 cas testés).
- **Contexte initial conservé** : il figure dans le résumé et reste intact après un changement de sujet.
- **Aucune source inventée** :
  - chaque preuve affichée est identique au fait de la fiche ;
  - sa source est l’une des sources consultées ;
  - aucun nombre absent de la bibliothèque n’apparaît (contrôle fait à chaque tour de chaque scénario).
- **Bilan conforme à l’historique** : il est comparé élément par élément à la mémoire.
- **Conversations bien séparées** : la nouvelle a un autre identifiant, aucun tour, aucun argument et aucune source.
- **Limites techniques expliquées** :
  - message trop long → 400, avec un message clair ;
  - trop de demandes → 429, avec `Retry-After` ;
  - budget atteint → 503 « quota » ;
  - pas de clé → 503 « démo » ;
  - réponse illisible du modèle → 502, relançable.

**Non-régression.** Les 150 scénarios de personnalisation (v5) et tous les tests v4 et v5 passent. Les anciens tests de bout en bout sur les boutons de retour ont été adaptés à la nouvelle zone de conversation.

## 5. Limites restantes

- **Pas d’URL publique** tant que le propriétaire n’a pas suivi la section 0 de `PUBLIER.md`.
- **Lecture des réactions par mots-clés** en mode autonome : elle peut se tromper. Elle est présentée comme approximative, et les raccourcis permettent de préciser.
- **Bibliothèque épuisée** sur un sujet : le moteur local ne peut pas apporter de fait nouveau. Il le dit et propose une question, un résumé, le mode connecté ou la conclusion.
- **Mode connecté non testé avec une vraie clé API** : uniquement avec un service d’IA simulé. La qualité réelle des réponses générées reste à évaluer après le déploiement.
- **Render gratuit** : mise en veille après 15 minutes sans trafic, et budget du serveur remis à zéro à chaque redémarrage. D’où le plafond à fixer aussi chez Anthropic.
- **Conversation conservée dans l’onglet uniquement** (sessionStorage) : elle disparaît à la fermeture de l’onglet. C’est un choix volontaire de données minimales ; l’argumentaire peut être enregistré sur l’appareil.

## 6. Ce qu’il reste à faire (propriétaire)

1. Créer un compte GitHub et installer l’outil `gh` : <https://cli.github.com>.
2. Dans le dossier du projet : `gh auth login`, puis `bash scripts/publier-github.sh`.
3. Attendre la coche verte dans l’onglet *Actions*, puis ouvrir l’adresse affichée sur un téléphone en 4G.
4. Facultatif, pour l’IA : sur Render, *New → Blueprint*, choisir le dépôt, saisir `ANTHROPIC_API_KEY`. Fixer un plafond de dépenses dans la console Anthropic.
