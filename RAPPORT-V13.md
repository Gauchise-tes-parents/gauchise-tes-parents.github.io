# Rapport v13 — Intégration de Gemini et confidentialité totale

## 1. Ce que j'ai trouvé en examinant le projet

- Le site public est **statique** (GitHub Pages) : il ne peut pas garder de secret. Une clé Gemini dans le code du site serait lisible par n'importe qui. Il fallait un **backend** séparé.
- Le serveur Node existant (mode connecté) fonctionne avec Anthropic et n'est **pas déployé**. J'ai choisi un **Cloudflare Worker** dédié à Gemini, plus simple à héberger, gratuit au départ, sans toucher au serveur Node.
- Le moteur de compréhension (repérage des thèmes, choix strict des fiches) est en JavaScript sans dépendance : le Worker **réutilise exactement le même code** que l'application, donc les mêmes garde-fous contre les amalgames.
- Point juridique trouvé dans les conditions de l'API Gemini : pour un service ouvert à des utilisateurs de l'Espace économique européen, **seuls les services payants** peuvent être utilisés. En service gratuit, Google peut aussi utiliser les questions pour améliorer ses produits. **La facturation Google doit donc être activée.**

## 2. Fonctionnement (bibliothèque + Gemini)

1. L'utilisateur pose sa question ; la **bibliothèque répond d'abord**, sur son appareil.
2. Si elle n'a pas de fiche, l'application appelle l'IA **automatiquement** ; sinon, l'IA est proposée par des boutons : Coup express, Gagner le débat, Convaincre avec empathie, Approfondir. C'est un appel par clic, jamais en double.
3. Le **Worker** repère les thèmes, choisit lui-même les fiches qui répondent vraiment (jamais une fiche voisine forcée ; le navigateur ne peut pas lui imposer de « contexte »), et envoie à Gemini :
   - les consignes de l'application (identité, règles de vérité, structure du mode) ;
   - les extraits vérifiés, avec leurs sources numérotées B1, B2… ;
   - la question, isolée comme une donnée (protection contre l'injection d'instructions).
4. Gemini peut lancer une **recherche Google** (« grounding »).
5. Le Worker **contrôle la réponse** :
   - toute adresse web écrite par le modèle est supprimée ;
   - seuls s'affichent les documents de la bibliothèque réellement cités et les pages que Google a réellement consultées ;
   - un « fait » sans source vérifiable devient « Non vérifié ».
6. L'interface affiche l'**origine** (fiche de la bibliothèque / rédigé par Gemini / recherche Google effectuée ou non) et le **statut** de chaque élément : fait établi, estimation, interprétation, opinion politique, non vérifié. Boutons disponibles : Relancer, Plus court, Plus percutant, Approfondir, Version empathie.

## 3. Fichiers

**Créés :**
- `worker/src/handler.js` — parcours complet de la demande.
- `worker/src/gemini.js` — fournisseur Gemini, interface commune pour un second fournisseur.
- `worker/src/prompt.js` — consignes par mode.
- `worker/src/parse.js` — contrôle de la réponse.
- `worker/src/limits.js` — anti-abus.
- `worker/src/index.js`, `wrangler.toml` (racine), `worker/README.md` — configuration et guide de mise en service.
- `scripts/build-worker-kb.js` — intègre la bibliothèque au Worker.
- `tests/unit/ia-gemini.test.js` (23 tests), `tests/unit/confidentialite.test.js` (12 tests), `tests/e2e/ia-confidentialite.test.js` (4 parcours).
- `AUDIT-CONFIDENTIALITE.md`, ce rapport.

**Modifiés :**
- `public/js/app.js` : bloc IA, mentions de transmission, nouvelle page « Confidentialité et sécurité », suppression de l'historique et de la conservation des conversations.
- `public/js/api.js`, `public/js/store.js`, `public/js/cartographie.js` — deux faux positifs corrigés :
  - « protège les riches » était lu comme « la justice protège les délinquants » ;
  - « les bénéficiaires du RSA ne veulent pas travailler » partait vers la fiche sur les chômeurs.
- `public/js/ligne-editoriale.js`, `public/index.html` (CSP), `public/config.js`, `public/css/styles.css`.
- `scripts/build-static.js`, `scripts/build-preview.js`, `.github/workflows/pages.yml` (variable `GTP_IA_BASE`).
- `server/app.js`, `server/config.js`, `server/engine/knowledge.js`, `server/engine/pipeline.js`, `server/engine/providers/anthropic.js`.
- `.env.example`, `.gitignore`, `package.json` (0.13.0), `README.md`, deux tests e2e adaptés à la nouvelle règle de non-conservation.

## 4. Tests réellement exécutés

- **Tests unitaires : 465 sur 465.**
- **Parcours dans le navigateur : les 2 tests adaptés à la nouvelle règle repassés, les 4 nouveaux réussis**, dont :
  - réponse IA automatique sans fiche ;
  - version courte ;
  - IA à la demande avec fiche ;
  - aucune requête vers un site tiers ;
  - aucune question dans le stockage du navigateur.
- **Les 8 affirmations demandées** : sujet repéré et fiches transmises à Gemini vérifiés, sans amalgame.

| Affirmation | Fiches transmises à Gemini | Ce qui ne doit PAS être transmis (vérifié) |
|---|---|---|
| L'immigration prend le travail des Français | immigration et emploi | aides sociales, RSA |
| Des millions de fausses cartes Vitale | cartes Vitale | RSA, aides aux étrangers |
| Les bénéficiaires du RSA ne veulent pas travailler | RSA et SMIC | cartes Vitale, immigration et emploi |
| Les immigrés coûtent plus cher qu'ils ne rapportent | immigrés et aides (contribution budgétaire) | RSA, cartes Vitale |
| La France est submergée par l'immigration | « grand remplacement » | aides, RSA |
| Le gouvernement protège les riches et fait payer les pauvres | dividendes et salaires, pauvreté | fiches justice (faux positif corrigé) |
| Les étrangers ont davantage d'aides que les Français | immigrés et aides | immigration et emploi, cartes Vitale |
| Question mêlant emploi, RSA et cartes Vitale | les trois fiches correspondantes | — |

- **Contrôle de la réponse** : lien inventé supprimé, référence inconnue retirée, « fait » sans source rétrogradé. En mode express : 2 arguments au plus et une réponse courte.
- **Erreurs** : quota, fréquence, clé refusée, modèle absent, réseau, réponse inexploitable, clé absente — chaque cas renvoie un message en français.
- **Abus et sécurité** : entrées bornées, limite par visiteur, plafond quotidien, origine non autorisée refusée, journaux sans question ni IP, cache limité aux réponses génériques.

**Ce que je n'ai PAS pu tester :**
- **Les réponses réelles de Gemini.** Je n'ai pas utilisé la clé que tu as collée : elle est exposée et doit être révoquée. Je n'ai pas de clé valide. Dans les tests, l'API de Google est simulée au format qu'elle documente. Tout notre code est donc vérifié, mais pas la qualité rédactionnelle réelle de Gemini, ni le comportement exact de sa recherche.
- **Le déploiement Cloudflare.** L'outil `wrangler` n'a pas pu être installé ici (registre npm injoignable depuis mon environnement). Le Worker s'importe et fonctionne dans Node, mais son empaquetage par Cloudflare n'a pas été essayé.
- **L'affichage progressif mot à mot** n'est pas fait. La réponse arrive d'un bloc, avec un indicateur discret, parce que la réponse doit être contrôlée en entier (sources, liens) avant d'être affichée.

## 5. Ce qui demande encore ta configuration

1. Révoquer la clé exposée, en créer une nouvelle, **activer la facturation** et un budget sur Google Cloud.
2. Créer le Worker et y déposer la clé : `worker/README.md`, étape 1.
3. Renseigner la variable de dépôt GitHub `GTP_IA_BASE` : étape 2.
4. Faire les premiers vrais tests avec les 8 affirmations, et ajuster si besoin `GEMINI_MODEL` et les limites.

Tant que ces étapes ne sont pas faites, le site public fonctionne exactement comme avant, sans IA, et n'affiche aucun bouton IA.
