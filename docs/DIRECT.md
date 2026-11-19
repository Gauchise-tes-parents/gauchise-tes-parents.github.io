# Onglet « Direct » (Twitch et YouTube)

Quand Marty Ducanda lance un live sur **Twitch** (`martyducanda`) ou sur **YouTube** (`@Martyducanda`), l'onglet « Direct » de l'application l'affiche automatiquement. Un point rouge clignote alors sur l'onglet. Sous le lecteur, le bouton **« Ouvrir le chat »** renvoie vers le chat de la plateforme du live.

## Comment ça marche

- Le site ne contacte **ni Twitch ni YouTube** pour savoir s'il y a un live. Il interroge seulement le **détecteur du projet** (`worker-direct/`, un Worker Cloudflare séparé du Worker Gemini, qui reste désactivé), au plus une fois par minute et seulement quand la page est visible.
- Le détecteur interroge l'API officielle de Twitch (application « gauchise tes parents app », type Confidentiel) et la page publique `youtube.com/@Martyducanda/live`. Il garde le résultat 60 secondes : quel que soit le nombre de visiteurs, Twitch et YouTube sont interrogés au plus une fois par minute.
- Pendant un live, l'onglet « Direct » charge le **lecteur officiel**. Pour YouTube, c'est la version « sans cookie » (`youtube-nocookie.com`). Le lecteur démarre son coupé, comme l'exigent les navigateurs. La politique de sécurité du site n'autorise que ces deux lecteurs (`frame-src`), et seulement quand le détecteur est configuré.
- Si les deux plateformes sont en direct en même temps, Twitch s'affiche d'abord, avec un bouton pour passer à YouTube.
- Sans détecteur configuré, l'onglet affiche simplement les liens vers les deux chaînes.

## Mise en service (une seule fois)

1. **Créer le Worker** dans le tableau de bord Cloudflare : *Workers & Pages* → *Créer* → *Importer un dépôt* → choisir `gauchise-tes-parents.github.io`.
   - Nom du Worker : `gauchise-direct`.
   - Dossier racine (*Root directory*) : `worker-direct`.
   - Commande de déploiement : `npx wrangler deploy` (par défaut).
   - Autre méthode, depuis un ordinateur : `cd worker-direct && npx wrangler deploy`.
2. **Ajouter le secret** : *Workers* → `gauchise-direct` → *Paramètres* → *Variables et secrets* → *Ajouter* → type **Secret**, nom `TWITCH_CLIENT_SECRET`, valeur : le secret de l'application Twitch. Autre méthode : `npx wrangler secret put TWITCH_CLIENT_SECRET`.
   - Le secret n'est **jamais** écrit dans le dépôt, qui est public.
   - L'identifiant client, qui n'est pas secret, est déjà dans `worker-direct/wrangler.toml`.
3. **Vérifier** : ouvrir `https://gauchise-direct.<ton-compte>.workers.dev/statut`. La page doit afficher `"enDirect": false` (ou `true` pendant un live), sans `"erreur"` pour Twitch.
4. **Brancher le site** : GitHub → *Settings* → *Secrets and variables* → *Actions* → onglet *Variables* → créer la variable `GTP_DIRECT_BASE` avec l'adresse du Worker (sans `/statut`). Autre méthode : renseigner `directBase` dans `deploiement.json`. La publication suivante active la détection.

## Limites

- La détection YouTube lit la page publique de la chaîne, sans clé d'API. Si YouTube change sa page, la détection YouTube peut cesser de fonctionner, sans gêner Twitch. Le champ `youtube.erreur` de `/statut` le signale.
- Un live apparaît au plus une minute environ après son lancement.
- Pendant un live, Twitch (Amazon) ou YouTube (Google) reçoivent l'adresse IP des personnes qui ouvrent l'onglet « Direct ». La page Confidentialité le dit.
