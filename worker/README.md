# Backend IA (Gemini) — mise en service

Le site public (GitHub Pages) ne peut pas contenir de clé secrète. Les appels à Gemini passent donc par ce petit
serveur, un **Cloudflare Worker**, qui garde la clé dans un **secret** chiffré (`GEMINI_API_KEY`). Le navigateur
ne voit jamais la clé : il connaît seulement l'adresse publique du Worker.

## 0. Avant tout : la clé exposée

La clé collée dans la conversation doit être **supprimée** dans Google AI Studio → *API keys*, puis remplacée par
une nouvelle clé. Ne colle jamais la nouvelle clé dans une conversation, un fichier ou un message : seulement dans
la commande `wrangler secret put` ci-dessous (ou dans le tableau de bord Cloudflare, rubrique *Variables and Secrets*).

**Facturation Google (important pour la France)** : les conditions de l'API Gemini prévoient que, pour mettre une
application à disposition d'utilisateurs de l'Espace économique européen, du Royaume-Uni ou de la Suisse, seuls les
*services payants* peuvent être utilisés. Les services payants ont aussi l'avantage que Google n'utilise pas les
questions pour améliorer ses produits. Active donc la facturation sur le projet Google de la clé, et fixe un
plafond de dépenses (Google Cloud → *Billing* → *Budgets & alerts*).

## 1. Créer le Worker (une fois)

**Méthode simple (sans terminal) : Cloudflare relié à GitHub.**
1. Cloudflare → *Workers & Pages* → *Create* → importer le dépôt GitHub du site. Laisser les réglages par défaut :
   répertoire racine `/`, commande de déploiement `npx wrangler deploy`. Le fichier `wrangler.toml` à la racine
   du dépôt dit à Cloudflare quoi construire (il intègre la bibliothèque au Worker avant chaque déploiement).
   Le nom du Worker dans Cloudflare doit être le même que `name` dans `wrangler.toml` (`gauchise-tes-parents-github-io`).
2. Dans le Worker : *Settings* → *Variables and Secrets* → *Add* → type **Secret**, nom `GEMINI_API_KEY`,
   valeur = la NOUVELLE clé Google. Enregistrer (*Deploy*).
3. Ensuite, chaque modification de la branche `main` redéploie le Worker automatiquement.

**Méthode avec terminal (équivalente)**, depuis la racine du dépôt, avec Node.js 22 :

```bash
npx wrangler login
npx wrangler secret put GEMINI_API_KEY   # colle la NOUVELLE clé quand c'est demandé (rien ne s'affiche)
npx wrangler deploy
```

Vérification : ouvre `https://<adresse-du-worker>/api/ia/statut` → tu dois lire `"disponible": true`.
L'adresse est visible dans Cloudflare (Worker → *Settings* → *Domains & Routes*, adresse en `workers.dev`).

## 2. Brancher le site sur le Worker

L'adresse publique du Worker est inscrite dans `deploiement.json` (champ `iaBase`, ce n'est pas un secret).
À chaque publication, le site l'utilise et sa politique de sécurité autorise cette seule adresse.
Pour la changer : modifier `deploiement.json`, ou créer la variable de dépôt GitHub `GTP_IA_BASE`, qui a priorité.

## 3. Réglages (wrangler.toml à la racine du dépôt, sans toucher au code)

| Variable | Rôle | Valeur par défaut |
|---|---|---|
| `GEMINI_MODEL` | modèle Gemini (liste : https://ai.google.dev/gemini-api/docs/models) | `gemini-3.8-flash` |
| `GEMINI_RECHERCHE` | recherche Google (« grounding ») : `1` oui, `0` non | `1` |
| `ALLOWED_ORIGINS` | sites autorisés à appeler le Worker | `https://gauchise-tes-parents.github.io` |
| `LIMITE_PAR_VISITEUR` / `FENETRE_MINUTES` | anti-abus par visiteur | 12 demandes / 10 min |
| `PLAFOND_QUOTIDIEN` | nombre maximal de réponses IA par jour pour tout le site | 800 |

Après une modification poussée sur GitHub, Cloudflare redéploie tout seul (ou `npx wrangler deploy`).

Recommandé avec beaucoup de trafic :
- un espace **KV** pour que le plafond quotidien soit commun à toutes les instances (voir la fin de `wrangler.toml`) ;
- une règle **Rate limiting** dans Cloudflare (*Security* → *WAF*) sur `/api/ia`.

## 4. Coûts

Chaque réponse IA = un appel au modèle, plus d'éventuelles requêtes de recherche Google, facturées séparément
selon la grille de Google. Le plafond quotidien du Worker et le budget Google sont tes deux garde-fous.
Les réponses génériques (question qui correspond à une fiche, sans contexte de conversation) sont gardées
une heure en cache pour éviter de payer deux fois la même réponse.

## 5. Ajouter un second fournisseur plus tard

`src/gemini.js` expose une interface simple, `generate({ system, user, search, maxTokens, temperature })`.
Un autre fournisseur (par exemple Anthropic, déjà utilisé par le serveur Node du projet) peut être ajouté avec la
même interface, puis choisi en secours dans `src/handler.js` quand Gemini renvoie une erreur de quota ou de service.
