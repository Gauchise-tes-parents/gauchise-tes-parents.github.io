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

Il faut Node.js 22 et un compte Cloudflare gratuit.

```bash
npm run worker:kb                      # intègre la bibliothèque vérifiée au Worker (worker/src/kb.json)
cd worker
npx wrangler login                     # ouvre le navigateur pour te connecter à Cloudflare
npx wrangler secret put GEMINI_API_KEY # colle la NOUVELLE clé quand c'est demandé (rien ne s'affiche)
npx wrangler deploy                    # publie ; note l'adresse affichée, ex. https://gauchise-tes-parents-ia.<toi>.workers.dev
```

Vérification : ouvre `https://<adresse-du-worker>/api/ia/statut` → tu dois lire `"disponible": true`.

## 2. Brancher le site sur le Worker

GitHub → dépôt du site → *Settings* → *Secrets and variables* → *Actions* → onglet **Variables** →
*New repository variable* : `GTP_IA_BASE` = l'adresse du Worker (sans `/` final). Ce n'est pas un secret.
Puis relance le déploiement (*Actions* → *Publier sur GitHub Pages* → *Run workflow*). La politique de sécurité
du site autorise alors cette seule adresse.

## 3. Réglages (worker/wrangler.toml, sans toucher au code)

| Variable | Rôle | Valeur par défaut |
|---|---|---|
| `GEMINI_MODEL` | modèle Gemini (liste : https://ai.google.dev/gemini-api/docs/models) | `gemini-3.8-flash` |
| `GEMINI_RECHERCHE` | recherche Google (« grounding ») : `1` oui, `0` non | `1` |
| `ALLOWED_ORIGINS` | sites autorisés à appeler le Worker | `https://gauchise-tes-parents.github.io` |
| `LIMITE_PAR_VISITEUR` / `FENETRE_MINUTES` | anti-abus par visiteur | 12 demandes / 10 min |
| `PLAFOND_QUOTIDIEN` | nombre maximal de réponses IA par jour pour tout le site | 800 |

Après une modification : `npm run worker:deploy` (qui réintègre aussi la bibliothèque à jour).

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
