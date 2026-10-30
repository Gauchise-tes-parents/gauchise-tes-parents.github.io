# Publier et partager « Gauchise tes parents »

Ce guide explique, étape par étape, comment rendre l'application accessible à tous avec un lien. **Rien n'a été publié à ta place** : il n'existe pas encore d'adresse publique. Les étapes qui restent à ta charge sont signalées par « À faire ».

Limites et tarifs relevés le 29 octobre 2026 dans la documentation officielle des hébergeurs (liens en fin de document). Ils peuvent changer : vérifie-les au moment de publier.

---

## 0. Publication express (environ 10 minutes, gratuit)

Le site public le plus simple est le **mode autonome sur GitHub Pages** : aucune clé, aucun serveur, aucun coût, ouvert à tous sans compte. La bibliothèque, les argumentaires sur mesure et la **conversation continue** (moteur local) y fonctionnent, y compris hors ligne après la première visite.

1. Crée un compte sur <https://github.com> (gratuit). *À faire.*
2. Installe l'outil GitHub en ligne de commande : <https://cli.github.com>. *À faire.*
3. Dans un terminal, dans le dossier du projet : `gh auth login` (choisir GitHub.com, HTTPS, connexion par le navigateur). *À faire.*
4. Toujours dans le dossier du projet : `bash scripts/publier-github.sh`. Le script vérifie qu'aucun secret n'est publié, lance les tests, crée le dépôt public `gauchise-tes-parents`, envoie le code, active GitHub Pages et déclenche la publication. *À faire.*
5. Attends la coche verte dans l'onglet *Actions* du dépôt (1 à 3 minutes). L'adresse publique est affichée par le script : `https://TON-COMPTE.github.io/gauchise-tes-parents/`. Ouvre-la sur ton téléphone en 4G pour vérifier.

Mises à jour ensuite : `git add -A && git commit -m "…" && git push` → le site se republie tout seul.

Si le script ne parvient pas à activer Pages (droits du compte), fais-le à la main : *Settings → Pages → Source : GitHub Actions*, puis *Actions → Publier sur GitHub Pages → Run workflow*.

**Version complète avec IA (facultative, payante à l'usage)** : sur <https://render.com>, *New → Blueprint*, choisis le dépôt : le fichier `render.yaml` configure le service (interface + serveur, quotas par IP et globaux, plafonds de budget). Saisis `ANTHROPIC_API_KEY` dans le tableau de bord Render (jamais dans le dépôt) et **fixe aussi un plafond de dépenses dans la console Anthropic**, car le disque gratuit de Render est éphémère (le compteur de budget du serveur repart de zéro à chaque redémarrage). L'adresse sera du type `https://gauchise-tes-parents.onrender.com` (mise en veille après 15 minutes sans visite, réveil d'environ une minute).

**Protections en place pour un accès public** : aucune clé dans le navigateur ; limitation par adresse IP (analyses, stratégies, tours de conversation) et plafond global de tours de conversation par heure ; plafonds de dépenses journalier et mensuel ; taille des messages bornée (1 000 caractères) ; le mode autonome, utilisé par défaut, ne coûte rien.

---

## 1. Où se trouve le projet

```
gauchise-tes-parents/
  public/                 l'interface (HTML, CSS, JavaScript sans dépendance)
    index.html            point d'entrée (chemins relatifs : fonctionne aussi dans un sous-dossier)
    config.js             adresse du serveur du mode connecté (null = même origine ou aucun)
    sw.js                 service worker : hors-ligne après la première visite
    js/                   app.js (écrans), kbstore.js (base locale), composer.js (argumentaires hors ligne),
                          profile.js (questionnaire), kbsearch.js (recherche locale), store.js (données de l'appareil)
  data/library/*.json     la base de connaissances (une fiche par fichier)
  data/watch/             état, journal et comptes rendus de la veille (créé à la première veille)
  data/library-history/   sauvegardes des fiches avant toute modification par la veille
  server/                 serveur Node du mode connecté (API, recherche web, veille)
  scripts/                build-static.js (site statique), veille.js (veille en ligne de commande),
                          build-preview.js (aperçu en un seul fichier), fiches/*.py (génération traçable des fiches)
  .github/workflows/      pages.yml (publication GitHub Pages), veille.yml (veille planifiée)
  tests/                  tests unitaires et navigateur
```

**Dépendances** : aucune bibliothèque à installer. Il faut seulement **Node.js 22 ou plus récent** (le projet utilise `node:test`, `fetch` et les modules ES natifs). Les tests navigateur utilisent Playwright s'il est présent (facultatif).

**Commandes**

| Commande | Effet |
|---|---|
| `npm start` | serveur local sur http://localhost:3000 (modes autonome et connecté) |
| `npm test` | tests unitaires et d'intégration |
| `npm run test:e2e` | tests dans un vrai navigateur (Playwright requis) |
| `npm run build:static` | produit le site statique dans `dist/site/` |
| `npm run build:preview` | aperçu en un seul fichier HTML (`dist/apercu-statique.html`) |
| `npm run veille` | un cycle de veille (clé API requise) ; `npm run veille:statut` pour l'état |

**Configuration** : copier `.env.example` en `.env` (jamais publié, déjà ignoré par Git). Variables utiles :

| Variable | Rôle |
|---|---|
| `ANTHROPIC_API_KEY` | active le mode connecté (recherche web, IA) et la veille. **Secret** |
| `DAILY_BUDGET_USD`, `MONTHLY_BUDGET_USD` | plafonds de dépenses mesurées par le serveur |
| `PER_IP_*` | limitation des abus par adresse IP |
| `CORS_ORIGIN` | adresse https du site statique si l'interface et le serveur sont sur deux domaines |
| `GTP_API_BASE` | (au moment de `build:static`) adresse https du serveur du mode connecté |
| `WATCH_ENABLED`, `WATCH_INTERVAL_HOURS` (24 à 48), `WATCH_MAX_USD_PER_RUN`, `WATCH_AUTO_APPLY`, `WATCH_ADMIN_TOKEN`, `WATCH_WEBHOOK_URL`, `WATCH_EXTERNAL_SCHEDULE` | veille automatique (section 6) |

---

## 2. Quelle architecture choisir

| | Mode autonome seul | Mode autonome + connecté |
|---|---|---|
| Ce qui marche | bibliothèque, recherche locale, fiches, questionnaire, deux stratégies composées, adaptation après chaque échange, historique, hors-ligne | tout cela **plus** recherche web en direct, rédaction par IA, veille automatique déclenchable depuis le serveur |
| Hébergement | statique : GitHub Pages ou Cloudflare Pages | statique pour l'interface **et** un serveur Node (Render, Railway, Fly.io, petit VPS…) |
| Coût | gratuit dans les limites des offres | serveur gratuit ou quelques euros par mois + **API d'IA facturée à l'usage** |
| Secrets | aucun | clé API **uniquement** sur le serveur |

**Recommandation pour une première version** : publier le mode autonome sur GitHub Pages (gratuit, sans serveur, sans clé). Le mode connecté pourra être ajouté ensuite sans rien changer à l'interface.

---

## 3. Publier gratuitement sur GitHub Pages (mode autonome)

1. **Créer un compte GitHub** (gratuit) si tu n'en as pas. *À faire.*
2. **Créer un dépôt public** : sur github.com, « New repository », nom par exemple `gauchise-tes-parents`, visibilité **Public** (GitHub Pages gratuit exige un dépôt public). Ne coche aucune option d'initialisation. *À faire.*
3. **Envoyer le code** depuis le dossier du projet :
   ```bash
   cd gauchise-tes-parents
   git init
   git add .
   git commit -m "Première version"
   git branch -M main
   git remote add origin https://github.com/TON-COMPTE/gauchise-tes-parents.git
   git push -u origin main
   ```
   Vérifie avant l'envoi que `git status` ne montre ni `.env`, ni `data/feedback`, ni `data/usage` (ils sont dans `.gitignore`).
4. **Activer Pages** : dans le dépôt, *Settings → Pages → Build and deployment → Source : GitHub Actions*. *À faire.*
5. **Compilation** : déjà configurée dans `.github/workflows/pages.yml`. À chaque envoi sur `main`, GitHub exécute `npm test`, puis `node scripts/build-static.js`, et publie le dossier de sortie **`dist/site`**. Rien d'autre à installer.
6. **Obtenir l'URL publique** : onglet *Actions* → attendre la coche verte du flux « Publier sur GitHub Pages » ; l'adresse apparaît dans *Settings → Pages*, sous la forme `https://TON-COMPTE.github.io/gauchise-tes-parents/`.
7. **Tester depuis un autre téléphone et un autre réseau** : ouvre l'adresse en 4G (Wi-Fi coupé) sur un autre appareil ; consulte deux fiches ; puis active le mode avion et recharge : la bibliothèque et les argumentaires doivent rester disponibles.
8. **Mettre à jour** : modifie le code ou ajoute une fiche, puis `git add . && git commit -m "..." && git push`. Le site se republie tout seul en quelques minutes ; les visiteurs reçoivent la nouvelle base à leur prochaine connexion (après vérification de son intégrité).

**Alternative : Cloudflare Pages.** *Workers & Pages → Create → Pages → Connect to Git*, choisir le dépôt ; **commande de compilation** : `node scripts/build-static.js` ; **dossier de sortie** : `dist/site` ; variable d'environnement `NODE_VERSION=22`. L'URL fournie est en `*.pages.dev`.

---

## 4. Ajouter le mode connecté (serveur Node)

Le serveur garde la clé API secrète, applique les plafonds de dépenses et la limitation par IP.

**Exemple avec Render** (offre gratuite) :
1. *New → Web Service*, connecter le dépôt. **Build command** : `npm install --omit=dev || true` (aucune dépendance) ; **Start command** : `node server/index.js`. *À faire.*
2. Variables d'environnement : `ANTHROPIC_API_KEY` (secret), `HOST=0.0.0.0`, `TRUST_PROXY=1`, `DAILY_BUDGET_USD=2`, `MONTHLY_BUDGET_USD=20`, `CORS_ORIGIN=https://TON-COMPTE.github.io`.
3. Dans le dépôt GitHub : *Settings → Secrets and variables → Actions → Variables* : `GTP_API_BASE` = l'adresse https du service Render. Le prochain déploiement Pages pointera l'interface vers ce serveur.
4. Limites de l'offre gratuite de Render (documentation officielle) : mise en veille après **15 minutes** sans trafic, réveil d'environ **une minute**, **750 heures** d'instance par mois, **système de fichiers éphémère** (les fichiers locaux — budget, retours, état de la veille — sont perdus au redémarrage : sur cette offre, la veille doit tourner via GitHub Actions, section 6).

Tu peux aussi tout héberger sur le serveur Node seul (il sert aussi l'interface) : une seule adresse, pas de `CORS_ORIGIN` ni de `GTP_API_BASE`.

---

## 5. Coûts et contraintes

| Élément | Gratuit ? | Limites connues (à revérifier) | Compte requis |
|---|---|---|---|
| GitHub Pages | oui, dépôt public | site publié ≤ 1 Go, bande passante « souple » de 100 Go/mois, déploiement ≤ 10 min, usage commercial restreint | GitHub |
| Cloudflare Pages | oui | 500 compilations/mois, 1 compilation à la fois, 20 000 fichiers, 25 Mio par fichier | Cloudflare |
| GitHub Actions (veille, publication) | oui pour un dépôt public (exécuteurs standards) | dans un dépôt public, **les tâches planifiées sont désactivées après 60 jours sans activité du dépôt** | GitHub |
| Render (serveur) | offre gratuite | voir section 4 ; dépassements facturés si un moyen de paiement est enregistré | Render |
| Nom de domaine | **non** | facultatif ; prix annuel variable selon l'extension et le registraire | registraire |
| API d'IA (recherche web, rédaction, veille) | **non** | facturée à l'usage : jetons + recherches web (10 $ pour 1 000 recherches) | Anthropic |

**Éviter une facture inattendue**
- Fixer un **plafond de dépenses dans la console du fournisseur d'IA** (en plus des plafonds du serveur).
- Garder `DAILY_BUDGET_USD` et `MONTHLY_BUDGET_USD` bas au début (par exemple 2 $ et 20 $) ; le serveur refuse toute analyse au-delà.
- Veille : `WATCH_MAX_USD_PER_RUN` (1,5 $ par défaut, soit au plus environ 45 $/mois à une veille par jour dans le pire cas) ; commencer avec `WATCH_CATEGORIES=economie,societe` pour réduire.
- Ne jamais enregistrer de moyen de paiement sur un hébergeur si tu veux que les dépassements suspendent le service au lieu d'être facturés.
- Le mode autonome, lui, ne coûte rien : aucun appel payant.

---

## 6. Veille automatique (toutes les 24 à 48 heures)

Le module (`server/watch/veille.js`) collecte les évolutions utiles aux arguments, les vérifie par des **règles explicites**, conserve les anciennes versions, produit un compte rendu et alimente la base téléchargée par l'application.

**Deux planificateurs possibles** (un seul suffit) :

1. **GitHub Actions** (recommandé avec un hébergement statique) — déjà prêt dans `.github/workflows/veille.yml` :
   - *Settings → Secrets → Actions* : ajouter `ANTHROPIC_API_KEY` (et facultativement `WATCH_WEBHOOK_URL` pour être prévenu des échecs). *À faire.*
   - *Variables* : `WATCH_EXTERNAL_SCHEDULE` = `GitHub Actions, tous les jours à 04:17 UTC` (affiché dans le tableau de bord), éventuellement `WATCH_MAX_USD_PER_RUN`, `WATCH_AUTO_APPLY`.
   - Fréquence : `cron: '17 4 * * *'` (24 h). Pour 48 h : `'17 4 */2 * *'`.
   - « Actualiser maintenant » : onglet *Actions → Veille automatique → Run workflow*.
   - Après chaque cycle, le flux exécute les tests, enregistre rapports, fiches et sauvegardes dans Git, puis la publication Pages se relance : les visiteurs reçoivent la nouvelle base.
2. **Serveur Node** (hébergement avec disque persistant) : `WATCH_ENABLED=1`, `WATCH_INTERVAL_HOURS=24`. Le serveur planifie lui-même les cycles, avec reprise après échec (1 h, 2 h, 4 h…). Lancement manuel depuis la page *Veille et actualisations* avec le jeton `WATCH_ADMIN_TOKEN`.

**Garanties** : verrou contre les exécutions simultanées ; nouvelles tentatives par catégorie ; une source indisponible n'arrête pas le cycle ; plafond de coût par cycle ; journal (`data/watch/veille.log.jsonl`) ; comptes rendus (`data/watch/rapports/`) ; file de validation humaine (`data/watch/a-valider.jsonl`) ; notification facultative en cas d'échec.

**Règles de validation** : une information n'est retenue que si son URL a réellement été obtenue pendant la recherche, avec une date de publication valide et au moins une fiche concernée. Elle est « vérifiée » si sa source est institutionnelle ou scientifique, ou confirmée par deux sources indépendantes ; sinon elle reste « en attente ». Les sujets sensibles (déclarations, citations, accusations, rubriques Mélenchon/LFI et islamo-gauchisme) restent **toujours en attente de validation humaine**. Le contenu des pages est traité comme des données, jamais comme des instructions.

**Modifications automatiques** : désactivées par défaut. Avec `WATCH_AUTO_APPLY=1`, la seule modification possible ajoute à une fiche une **nouvelle valeur officielle à côté de l'ancienne** (avec périodes, source, dates de publication et de consultation), si le chiffre figure dans le document officiel consulté ; la fiche est sauvegardée avant, revalidée après, et marquée « à actualiser » pour que l'équipe révise ses argumentaires. Le texte des argumentaires n'est jamais réécrit automatiquement.

**Revenir en arrière** : `node scripts/veille.js --retour <id-fiche> [horodatage]` (ou `git revert` du commit de veille).

**Valider une proposition en attente** : relire `data/watch/a-valider.jsonl` et le compte rendu, modifier la fiche à la main (ou via un script de `scripts/fiches/`), lancer `npm test`, puis publier.

---

## 7. Sécuriser la publication

- Aucune clé dans le code du navigateur : `public/` ne contient aucun secret ; la clé n'existe que dans les variables du serveur ou les secrets GitHub.
- Ne jamais committer `.env`, `data/feedback/`, `data/usage/` (déjà ignorés). Vérifier `git status` avant chaque envoi.
- Les retours des visiteurs sont stockés sans adresse IP ; les données personnelles des visiteurs (historique, argumentaires, profils d'interlocuteur) restent **sur leur appareil**.
- Anti-abus : limitation par IP, plafonds financiers, jeton pour la veille manuelle (comparaison à temps constant).
- Le mode autonome ne fait aucun appel payant ; il ne peut pas générer de dépenses.

---

## 8. Rendre le partage simple

- La page *Publier et partager* de l'application affiche l'adresse courante avec un bouton « Copier » et, sur téléphone, « Partager ». Elle prévient si l'adresse est locale (non partageable).
- Une fois le site publié, partage l'adresse `https://…github.io/…/` : la page d'accueil présente le projet et ses deux modes.

## 9. Checklist finale

- [ ] Le site s'ouvre sur un téléphone, en 4G, depuis un autre appareil.
- [ ] Après une première visite, il fonctionne en mode avion (bibliothèque, fiches, argumentaires, historique).
- [ ] Les liens des sources s'ouvrent.
- [ ] Une question couverte affiche les deux stratégies (« Gagner le débat », « Convaincre avec empathie ») et la version solide de l'argument adverse.
- [ ] Aucun message d'erreur lié à un serveur volontairement absent ; la pastille indique « Autonome » ou « Connecté · non configuré ».
- [ ] `git status` ne montre ni `.env` ni données privées ; aucune clé dans `dist/site` (`grep -r "sk-ant" dist/site` ne renvoie rien).
- [ ] Plafonds de dépenses réglés (console du fournisseur, serveur, veille).
- [ ] Si la veille est activée : un premier « Run workflow » réussi, compte rendu lisible dans `data/watch/rapports/`.

## Sources des limites citées

- GitHub Pages : <https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits>
- Cloudflare Pages : <https://developers.cloudflare.com/pages/platform/limits>
- Render, offre gratuite : <https://render.com/docs/free>
- GitHub Actions, facturation : <https://docs.github.com/en/actions/concepts/billing-and-usage>
- GitHub Actions, désactivation des tâches planifiées : <https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows>
