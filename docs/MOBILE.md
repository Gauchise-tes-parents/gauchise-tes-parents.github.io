# Site et applications mobiles (App Store, Google Play) — préparation

État au 18 novembre 2026 : **tout est prêt côté code** pour emballer l'application avec Capacitor. Le projet
« applis mobiles » prévu dans deux semaines n'aura plus qu'à installer Capacitor, générer les projets natifs et
remplir les fiches des boutiques.

## Ce qui est déjà en place

| Élément | Où | Rôle |
|---|---|---|
| Site installable (PWA) | `public/manifest.webmanifest`, `public/sw.js` | Installation depuis le navigateur (Android, ordinateur), hors ligne après la première visite. |
| Icônes PNG | `public/img/icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `apple-touch-icon.png` | Icônes du site installé (Android adaptatif, écran d'accueil iPhone). |
| Icônes des boutiques | `mobile/store/icon-1024.png` (App Store, sans transparence), `mobile/store/icon-play-512.png` (Google Play) | À téléverser dans App Store Connect et la Play Console. |
| Générateur d'icônes | `npm run build:icones` | À relancer si le logo (`public/img/icon.svg`) change. |
| Dossier web de l'appli | `npm run build:mobile -- --plateforme ios` (ou `android`) → `dist/mobile/www` | Même application que le site, base de fiches embarquée (fonctionne sans réseau), sans service worker, sans IA ni serveur, **lien Tipeee masqué par défaut** (`--avec-soutien` pour l'afficher). |
| Configuration Capacitor | `capacitor.config.json` | Identifiant `fr.gauchisetesparents.app` (à confirmer : il ne pourra plus changer après la première publication), nom, dossier web. |
| Écran mobile | `viewport-fit=cover`, zones sûres (`env(safe-area-inset-*)`), barre d'onglets en bas | Déjà adapté aux iPhone à encoche et aux Android. |

## Le jour J (environ une demi-journée de mise en place)

1. Comptes : Apple Developer Program (payant, annuel) et Google Play Console (payant, une fois) — vérifier les tarifs
   du moment. Il faut un Mac avec Xcode pour publier sur l'App Store ; Android Studio suffit pour Google Play.
2. Installer Capacitor dans le dépôt :
   `npm i @capacitor/core @capacitor/app @capacitor/share && npm i -D @capacitor/cli @capacitor/ios @capacitor/android`
3. `npm run build:mobile -- --plateforme ios` puis `npx cap add ios` (et `android`), puis `npx cap sync`.
4. Ouvrir `npx cap open ios` / `npx cap open android`, régler signature, version, icônes et écran de lancement
   (outil conseillé : `@capacitor/assets` à partir de `mobile/store/icon-1024.png`).
5. Tester sur de vrais téléphones : recherche, bibliothèque, partage, liens externes (ils s'ouvrent dans le navigateur
   du téléphone), mode sans réseau.

## Points à décider ou vérifier avant de soumettre

- **Dons (Tipeee).** Les deux boutiques encadrent les liens vers des paiements ou des dons extérieurs. La version
  appli masque donc Tipeee par défaut. Vérifier les règles en vigueur (App Store Review Guidelines, section 3 ;
  règles de paiement de Google Play) avant d'utiliser `--avec-soutien`. Le bandeau « version alpha réservée aux
  soutiens Tipeee » de l'accueil devra aussi être reformulé pour l'appli.
- **« Simple site emballé ».** Apple refuse parfois les applis qui ne font qu'afficher un site. Arguments à mettre en
  avant : base de fiches embarquée et utilisable hors ligne, partage natif, recherche locale. Ajouter le partage natif
  (`@capacitor/share`) et le bouton retour Android (`@capacitor/app`) le jour J.
- **Politique de confidentialité.** Les boutiques exigent une URL publique : la page `#/confidentialite` du site peut
  servir ; remplir les « étiquettes de confidentialité » (App Store) et la « sécurité des données » (Play) : l'appli
  ne collecte rien. Si la remontée anonyme des questions (moteur interne, opt-in) est activée dans l'appli, il faudra
  la déclarer.
- **Contenu politique.** Catégorie conseillée : Éducation (ou Actualités). Préparer des captures d'écran
  (6,7 et 5,5 pouces pour l'iPhone, téléphone et tablette pour Android) et une description.
- **Mises à jour des fiches.** L'appli embarque la base du jour de sa compilation. Pour profiter des fiches
  quotidiennes sans republier l'appli, une étape du projet sera de laisser l'appli télécharger `kb/base.json` depuis
  le site (le mécanisme de mise à jour vérifiée par empreinte existe déjà dans `public/js/kbstore.js`) : il faudra
  ajouter l'origine du site dans la politique de sécurité (CSP, `connect-src`) de la version appli.
- **Politique de sécurité (CSP) et Capacitor.** Vérifier au premier lancement qu'aucun script de Capacitor n'est
  bloqué par la balise CSP de `index.html` ; l'assouplir uniquement pour la version appli si besoin.
