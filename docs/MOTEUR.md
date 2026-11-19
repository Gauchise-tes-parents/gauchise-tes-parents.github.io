# Moteur interne de fiches (sans IA, sans Claude)

Le moteur crée, **à la demande et gratuitement** (GitHub Actions), des fiches pour les questions restées
sans réponse. Il n'utilise **aucune IA** : il assemble des sources structurées, avec des garde-fous stricts.
Rien n'est publié sans toi : les fiches arrivent dans une *pull request* ; **valider = fusionner**.

## Ce qu'il fait à chaque lancement (manuel depuis le 19 novembre 2026 : Actions > « Moteur interne de fiches » > Run workflow ; `.github/workflows/moteur.yml`)

1. **Programme L'Avenir en commun** (une fois par semaine) : il parcourt la table des matières de
   `melenchon2027.fr/programme/livre/`, chapitre par chapitre, et recopie les sections, les mesures clés et les
   mesures à puces → `data/moteur/aec.json`. Un relevé incomplet (site changé, panne) est refusé : la version
   précédente est gardée.
2. **Chiffres officiels** : neuf indicateurs Eurostat (chômage, inflation, dette, déficit, pauvreté, inégalités,
   emploi, renouvelables, gaz à effet de serre) → `data/moteur/chiffres.json`. Un indicateur illisible garde sa
   dernière valeur ; aucun chiffre n'est inventé. Les changements sont listés dans le compte rendu.
3. **Questions sans réponse** : celles envoyées depuis le site (bouton « Envoyer anonymement ma question », si le
   collecteur est installé) et celles que tu écris dans `data/moteur/questions.txt` (une par ligne).
4. **Fiches** : pour chaque question (10 par nuit au plus), si une fiche y répond déjà, la question est marquée
   « couverte ». Sinon, le moteur assemble une **fiche de repères** :
   - les mesures du programme qui traitent du sujet, **citées mot pour mot** avec le lien du chapitre ;
   - un ou deux chiffres officiels pertinents (Eurostat), avec la période et le lien ;
   - les réponses « électeur convaincu » / « indécis », la lecture de gauche, les limites ;
   - **sans verdict** : la fiche dit franchement qu'elle ne vérifie pas l'affirmation.
5. **Garde-fous** avant d'ajouter une fiche à la bibliothèque : règles de validation de l'application, politique
   documentaire, la question doit mener à la nouvelle fiche, et **aucune** des ~600 phrases de contrôle (affirmations
   de la bibliothèque, questions du journal, questions des tests) ne doit changer de réponse. Puis **tous les tests**
   de l'application tournent ; s'ils échouent, les fiches redeviennent des brouillons (`data/brouillons/`).
6. **Compte rendu** : `data/moteur/rapport.md` (aussi texte de la pull request) : fiches créées, brouillons et
   pourquoi, questions à écrire à la main, chiffres qui ont changé, alertes.

Suivi de chaque question : `data/moteur/file.json` (statuts : `en_attente`, `couverte`, `fiche`, `brouillon`,
`a_ecrire`). Pour relancer une question, remets son statut à `en_attente`.

## À faire une fois (5 minutes)

1. Dépôt GitHub → **Settings → Actions → General → Workflow permissions** : cocher
   « **Allow GitHub Actions to create and approve pull requests** ». Sans cela, la branche `moteur/fiches-…` est
   bien poussée, mais la pull request n'est pas ouverte automatiquement.
2. Lancer un premier passage tout de suite : onglet **Actions → Moteur interne de fiches → Run workflow**.

## Collecteur de questions du site (facultatif, gratuit, Cloudflare)

Sans collecteur, le site ne fait **aucune** requête et le bouton n'apparaît pas. Avec lui, la personne qui n'a pas
trouvé de fiche peut cliquer « Envoyer anonymement ma question » : **seul le texte de la question part**, nettoyé
(adresses e-mail, téléphones et liens retirés), sans adresse IP, sans cookie, effacé après 90 jours.

Installation (Worker **séparé** de l'IA Gemini, dossier `worker-questions/`) :

```
cd worker-questions
npx wrangler kv namespace create QUESTIONS     # recopier l'id dans wrangler.toml
npx wrangler secret put EXPORT_TOKEN           # un long jeton aléatoire
npx wrangler secret put SEL                    # une autre chaîne aléatoire
npx wrangler deploy                            # donne l'URL https://gauchise-questions.<compte>.workers.dev
```

Puis dans GitHub → Settings → Secrets and variables → Actions :
- variable **`GTP_QUESTIONS_BASE`** = l'URL du Worker (le site affichera alors le bouton) ;
- secret **`GTP_QUESTIONS_TOKEN`** = le même jeton que `EXPORT_TOKEN`.

Penser à mentionner cette collecte facultative sur la page Confidentialité du site.

## Ce que le moteur ne fait pas (et qui reste humain, ou Claude ponctuellement)

- Il ne **réfute** pas une affirmation : sans IA, il ne peut pas lire des études et en tirer une démonstration.
  Les questions qu'il ne sait pas traiter sont listées dans le compte rendu (« à écrire »).
- Il ne rattache pas une question à la cartographie des arguments quand une autre fiche « capte » la phrase : la
  fiche reste alors en brouillon avec l'explication.
- Il ne met pas à jour les chiffres **dans les fiches existantes** : il signale les changements.

## Commandes utiles

- `node scripts/moteur/index.js` : passage complet (réseau nécessaire).
- `node scripts/moteur/index.js --hors-ligne` : sans réseau, avec le programme et les chiffres déjà relevés.
- `node scripts/moteur/index.js --repli` : remet en brouillon les fiches du dernier passage.
- Tests : `node --test tests/unit/moteur.test.js` (pages fictives, aucun accès réseau).
