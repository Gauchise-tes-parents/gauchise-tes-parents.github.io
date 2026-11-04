# Audit de confidentialité et de sécurité — v13 (4 novembre 2026)

Principe appliqué : la personne vient utiliser l'application, rien de plus. Chaque point ci-dessous a été **vérifié
dans le code**, et les vérifications sont rejouées automatiquement par `tests/unit/confidentialite.test.js`
(12 tests), `tests/unit/ia-gemini.test.js` (23 tests) et `tests/e2e/ia-confidentialite.test.js` (navigateur réel).

## Les 10 vérifications demandées

| # | Vérification | Résultat | Comment c'est vérifié |
|---|---|---|---|
| 1 | Aucune API de géolocalisation | ✅ Aucune | Recherche dans tout le code du navigateur, du serveur et du Worker ; le serveur envoie même `Permissions-Policy: geolocation=()` |
| 2 | Aucune coordonnée GPS collectée | ✅ Aucune | Idem ; dans le navigateur, aucune autorisation n'est accordée ni demandée (test e2e) |
| 3 | Aucune position déduite de l'adresse IP | ✅ Corrigé | **Trouvé et retiré** : le serveur du mode connecté ajoutait une localisation fixe (« FR », « Europe/Paris ») à chaque recherche web d'Anthropic. Ce n'était pas la position de l'utilisateur, mais la règle interdit toute information géographique ajoutée ; le périmètre « France » vient désormais du sujet, dans la consigne |
| 4 | Aucun compte ni identifiant | ✅ | Aucun champ e-mail, téléphone, mot de passe ni date de naissance ; aucune connexion |
| 5 | Aucun traceur publicitaire | ✅ | Aucun Google Analytics, pixel Meta ou TikTok, mesure d'audience, empreinte du navigateur ; aucun script, police ou image d'un site tiers ; test e2e : **zéro requête vers un autre site** pendant une session |
| 6 | Aucune clé d'API dans le navigateur | ✅ | Recherche de motifs de clés (Google, Anthropic, GitHub) dans le site, les scripts, le Worker, la configuration et **tout l'historique git publié** : aucune |
| 7 | Aucune conversation enregistrée automatiquement | ✅ Corrigé | **Trouvé et corrigé** : les fiches consultées étaient notées dans le stockage local (historique permanent), la conversation et le texte de la question étaient gardés dans le stockage de session. Désormais : mémoire vive uniquement ; les anciennes données sont effacées au premier chargement |
| 8 | Aucune question dans les journaux | ✅ Corrigé | **Trouvé et corrigé** : le serveur écrivait le texte de la question dans le fichier des propositions de mise à jour (`affirmation_soumise`), et un message d'erreur brut pouvait être journalisé. Test : une erreur provoquée avec un nom dans la question ne laisse ni le nom ni l'adresse IP dans les journaux (serveur Node et Worker) |
| 9 | Aucune donnée personnelle ajoutée aux recherches | ✅ | Requêtes vers Anthropic et vers Gemini contrôlées par test : ni identifiant, ni adresse IP, ni localisation ; seulement la question, la consigne et les extraits de la bibliothèque |
| 10 | Services externes identifiés et documentés | ✅ | Tableau ci-dessous et page « Confidentialité et sécurité » de l'application |

## Autres modifications

- **Page « Confidentialité et sécurité »** réécrite : ce qui est envoyé, à qui, selon le mode ; les limites dites honnêtement (hébergeur, fournisseurs d'IA).
- **Mention sous chaque champ de saisie** : la personne sait avant d'envoyer si sa phrase reste sur l'appareil ou part vers un prestataire.
- **Politique de sécurité du contenu (CSP)** ajoutée dans la page statique (GitHub Pages ne permet pas d'en-têtes HTTP) : aucun script en ligne ni extérieur ; seule l'adresse du backend IA, si elle est configurée, est autorisée en plus.
- **Durée en mémoire du serveur du mode connecté** ramenée de 12 heures à 1 heure.
- **« Mes données »** : plus d'historique ; seuls les argumentaires et profils que la personne choisit d'enregistrer, sur son appareil, supprimables.

## Ce qui est encore transmis à des prestataires

| Prestataire | Quand | Ce qu'il reçoit | Conservation (selon ses documents publiés) |
|---|---|---|---|
| **GitHub Pages** (hébergement du site) | à chaque visite | adresse IP, page demandée (comme tout hébergeur) | GitHub indique enregistrer l'adresse IP des visiteurs pour la sécurité |
| **Cloudflare** (backend IA, si configuré) | demande de réponse IA | adresse IP de la connexion, requête | selon la politique de Cloudflare ; notre code n'enregistre rien |
| **Google — Gemini et recherche Google** (si configuré) | demande de réponse IA | la question, le mode, les extraits de la bibliothèque, au plus 3 messages précédents de la conversation | service payant : pas d'utilisation pour améliorer les produits, journalisation limitée pour détecter les abus ; service gratuit : utilisation possible pour améliorer les produits et relecture humaine. Les conditions de Google imposent le service payant pour un service ouvert aux utilisateurs européens |
| **Anthropic** (mode connecté du serveur Node, non déployé) | analyse en mode connecté | la question et les choix du parcours | entrées et sorties supprimées sous 30 jours (jusqu'à 2 ans si signalées) ; pas d'entraînement sur les contenus selon ses conditions commerciales |
| **Tipeee** | seulement si la personne clique | ce que Tipeee collecte sur son propre site | politique de Tipeee |

## Ce qui est encore conservé

- **Sur l'appareil** : réglages techniques, bibliothèque (hors ligne), argumentaires et profils enregistrés volontairement ; pendant la visite, l'étape du questionnaire et les thèmes choisis (stockage de session, sans le texte saisi). Aucun cookie.
- **Serveur du mode connecté (non déployé)** : dossiers en mémoire vive 1 heure ; adresse IP hachée en mémoire quelques minutes ; signalements volontaires sans IP ; totaux de dépenses.
- **Backend IA** : adresse IP hachée avec un sel quotidien, en mémoire, le temps de la fenêtre anti-abus ; compteur quotidien global ; réponses génériques en cache une heure sous une clé hachée. Ni la question ni l'IP ne sont journalisées.

## Limites qui restent

- **Google et Cloudflare** reçoivent ce qui est nécessaire au traitement : on ne peut pas l'éviter si l'on veut des réponses d'IA. La garantie « pas d'utilisation pour améliorer les produits » dépend de l'activation de la **facturation Google** par l'administrateur du site.
- Les **journaux propres aux hébergeurs** (GitHub, Cloudflare) échappent à notre code.
- Les **suggestions de recherche de Google** (widget « Search suggestions ») ne sont pas affichées telles quelles : leur code HTML contient des styles en ligne interdits par notre politique de sécurité. Les requêtes réellement lancées et les pages consultées sont affichées à la place. Les conditions de Google sur l'affichage de ces suggestions sont à relire par l'administrateur avant une ouverture à grande échelle.
- Les liens des pages consultées par la recherche Google sont des **liens de redirection de Google** : en cliquant, la personne passe par Google.
