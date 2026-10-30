# Compte rendu — version 2 (29 octobre 2026)

## 1. Audit du MVP v1 : problèmes constatés

| # | Constat | Correction |
|---|---|---|
| 1 | Pas de modes « gagner » / « convaincre » : un seul ton paramétré par 9 « styles » | Deux modes complets, même dossier de preuves, structures et tons distincts |
| 2 | 16 petites catégories, sans sous-thèmes | 10 volets, 123 sous-thèmes, saisie libre ; taxonomie unique partagée serveur/client |
| 3 | Navigation par menu « burger » en haut, parcours en 5 étapes | Barre d'onglets en bas (Accueil, Débat, Thématiques, Bibliothèque), parcours en 3 étapes, réponse express en 1 écran |
| 4 | Moteur monolithique : un seul appel mêle recherche et rédaction ; documents jamais ouverts | Pipeline séparé : fournisseur → recherche + consultation (web_fetch) → vérification des preuves → stratégie sans recherche → présentation |
| 5 | Une source « consultée » = simple résultat de recherche | Distinction « document consulté » / « extrait de recherche seulement » / « ouverture impossible » |
| 6 | Aucun contrôle des chiffres | Chaque chiffre est recherché dans le texte réellement lu ; « non retrouvé » signalé |
| 7 | Plafond = nombre de requêtes par jour (pas financier) | Budget journalier et mensuel en dollars, sur la consommation mesurée, persistant |
| 8 | Pas de cache ; changer de ton relance tout | Cache des dossiers (TTL) ; changement de mode, démonstration et reformulation sans nouvelle recherche |
| 9 | Recherche en panne → résultat « inverifiable » qui ressemble à une analyse | Erreur explicite 503 + bouton « Relancer » ; aucun résultat affiché |
| 10 | Données contradictoires non mises en avant ; rien quand l'interlocuteur a raison | Sections « Ce qui complique notre argument », « Ce qui relève des valeurs », alerte + reformulation solide |
| 11 | Reformulation : le client envoyait lui-même les « faits » | Reformulation côté serveur à partir du dossier vérifié (identifiant d'analyse) |
| 12 | Bibliothèque sans volets ni fraîcheur | Fiches rattachées à un volet/sous-thème, date de révision, badge « À actualiser » |
| 13 | Fichiers statiques non compressés, pas de zones de sécurité iOS/Android | Gzip en mémoire, `viewport-fit=cover` et `env(safe-area-inset-*)` |
| 14 | Taxonomie dupliquée front/back | `public/js/taxonomy.js`, importé des deux côtés |

## 2. Fichiers

**Créés** : `server/engine/providers/anthropic.js`, `research.js`, `evidence.js`, `strategy.js`, `speech.js`, `pipeline.js`, `cost.js`, `util.js` ; `public/js/taxonomy.js`, `public/js/copy.js` ; `tests/unit/engine.test.js` ; `RAPPORT-V2.md`.
**Réécrits** : `server/app.js`, `server/library.js`, `server/config.js`, `server/engine/options.js`, `server/engine/demo.js`, `public/index.html`, `public/js/app.js`, `public/js/api.js`, `public/css/styles.css`, `tests/helpers.js`, `tests/unit/server.test.js`, `tests/unit/library.test.js`, `tests/e2e/ui.test.js`, `README.md`, `.env.example`.
**Modifiés** : `server/feedback.js`, `server/index.js`, `public/js/art.js` (illustrations des deux modes, icônes des volets et des onglets), `scripts/build-preview.js`, les 6 fiches `data/library/*.json`.
**Supprimés** (remplacés) : `server/engine/anthropic.js`, `factcheck.js`, `prompts.js`, `validate.js`, `public/js/data.js`, `tests/unit/validate.test.js`.

Fonction retirée volontairement : l'ancien outil séparé « Préparer le débat » et le choix parmi 9 styles. Raison : les deux modes couvrent tous leurs contenus (faits, arguments, objections, désaccords de valeurs, questions, conclusion) et les styles contredisaient le ton propre à chaque mode tout en rallongeant le parcours mobile. Les anciennes adresses (`#/verifier`, `#/idees-recues`) redirigent.

## 3. Tests réellement exécutés

`npm run test:all` — Node 22, Chromium (Playwright 1.63) : **78 tests, 78 réussis, 0 ignoré.**

- Moteur (13) : URL, nombres au format français, preuves (recherche, documents ouverts, échecs de consultation, PDF, citations), tri des sources, contrôle des chiffres, dossier, rétrogradation du verdict, stratégies des deux modes (références, nature, chiffres inventés), coûts (dont palier Haiku), budget persistant, cache.
- Bibliothèque et taxonomie (9) : 10 volets et sous-thèmes, libellés des modes, validité et sourcing des fiches, fraîcheur, filtres, validation des requêtes, URL Tipeee exacte.
- Serveur et configuration (23) : démo (aucune recherche ni verdict), compression, traversée de répertoire, erreurs 400/413/415, bibliothèque, retours sans IP ; réel simulé : outils demandés (6 recherches + 3 consultations, 3 + 1 en express), stratégie sans outil, accès aux sources, chiffres contrôlés, contradictions, changement de mode sans nouvelle recherche, démonstration, reformulation, analyse expirée, cache et recherche fraîche, recherche indisponible, sources insuffisantes, alerte, erreurs fournisseur sans fuite, `pause_turn`, budget financier, limite par IP, stratégie depuis une fiche, chiffre inventé dans la démonstration, statut, secret jamais renvoyé.
- Contrastes (17 couples WCAG AA).
- Navigateur (16) : accueil téléphone (deux modes, barre en bas), 3 petits écrans 320/360/412 px sur 8 pages sans débordement, cibles ≥ 44 px, bureau, liens Tipeee (accueil, pied de page, À propos), parcours complet avec retour et changement de mode, conservation après rechargement, thématiques et sous-thèmes, bibliothèque (filtres, état vide, fiche à actualiser, liens, copie), réponse express, résultat réel simulé (ordre mobile, sections dépliables, démonstration, changement de mode sans recherche, reformulation, copie, partage, signalement, avis), riposte depuis une fiche, recherche en panne puis « Relancer », aucune erreur JavaScript.

**Non testé : la recherche Web réelle.** Aucune clé API n'était disponible dans l'environnement. Les tests « mode réel » utilisent des réponses simulées au format documenté par Anthropic ; ils ne valident pas la qualité des recherches. L'ouverture effective du site Tipeee n'a pas pu être testée depuis l'environnement (URL et attributs vérifiés).

## 4. Services externes et coûts

Un seul service : API Anthropic (Claude + outils serveur web_search et web_fetch). Tarifs et estimation détaillés dans le README (« Coûts ») : environ 0,15 à 0,25 $ par analyse complète avec Sonnet (estimation), quelques centimes pour un changement de mode. Le coût réel est mesuré à chaque appel.

## 5. Limitations restantes

- Prompts non éprouvés sur l'API réelle : à ajuster après les premiers essais.
- Le contrôle des chiffres ne lit pas les PDF (signalé « contrôle automatique impossible ») ni les pages trop dynamiques.
- Mémoire des analyses, cache et limites en mémoire vive : une seule instance de serveur.
- Pas de progression réelle pendant la recherche (étapes indicatives, présentées comme telles).
- Bibliothèque limitée à 6 fiches dans 3 volets ; une fiche est déjà « à actualiser ».
- Aucun hébergement public n'a été configuré.
