# Applications mobiles (App Store, Google Play) — pas à pas

État au 19 novembre 2026 : **tout est prêt sauf les comptes**. L'appli Android et le projet iOS sont construits
automatiquement par GitHub (flux « Applications mobiles »), les textes et les réponses aux formulaires sont dans
`mobile/store/FICHES-BOUTIQUES.md`, les captures d'écran dans `mobile/store/captures/`.
Il ne reste que les démarches à faire avec tes propres comptes.

## Ce qui est prêt

| Élément | Où |
|---|---|
| Appli Android (APK de test à installer sur un téléphone, AAB pour Google Play) | GitHub > onglet *Actions* > « Applications mobiles » > dernier run > *Artifacts* |
| Projet iOS vérifié (compile sur le simulateur) et archivé, prêt à ouvrir dans Xcode | même endroit, fichier `ios-…` |
| Envoi iOS vers TestFlight **sans Mac** | même flux, dès que la clé d'API App Store Connect est enregistrée (étape 4) |
| Textes des boutiques, réponses aux formulaires, notes pour l'examen d'Apple | `mobile/store/FICHES-BOUTIQUES.md` |
| Captures : iPhone 6,9 pouces, iPad 13 pouces, téléphone et tablette Android, bannière Google Play 1024 × 500 | `mobile/store/captures/` |
| Icônes : App Store 1024 px, Google Play 512 px, icône adaptative Android, écrans de lancement clair et sombre | `mobile/store/`, `mobile/assets/` |
| Partage natif et bouton retour Android | `public/js/natif.js` (sans effet sur le site) |
| Bandeau « Version bêta » sans Tipeee, lien et jauge Tipeee masqués | version appli seulement (`scripts/mobile/build-mobile.js`) |
| Clé d'envoi Android | remise au propriétaire le 19 novembre (fichier `cle-android-gauchise.zip`, **jamais dans le dépôt**) |

L'appli embarque la bibliothèque du jour de sa construction et fonctionne sans réseau ; elle ne fait aucune requête.
Pour publier les nouvelles fiches, on relance le flux et on envoie une nouvelle version (une fois par semaine ou par
mois suffit). Étape ultérieure possible : télécharger la base depuis le site (mécanisme `kbstore.js` déjà prêt).

## Le 21 novembre : Google Play (le plus urgent, à cause des 14 jours de test)

1. **Créer le compte développeur** sur https://play.google.com/console (frais d'inscription uniques ; vérifier le tarif
   affiché). Type de compte : *personnel*. Google vérifie l'identité (pièce d'identité) : compter quelques jours.
2. **Enregistrer la clé d'envoi dans GitHub** (5 minutes, une seule fois) : dépôt du site > *Settings* >
   *Secrets and variables* > *Actions* > *New repository secret*, quatre secrets dont les valeurs sont dans
   `LISEZ-MOI.txt` du fichier `cle-android-gauchise.zip` : `ANDROID_KEYSTORE_BASE64`, `ANDROID_KEYSTORE_PASSWORD`,
   `ANDROID_KEY_ALIAS`, `ANDROID_KEY_PASSWORD`. Garder une copie de sauvegarde du zip hors de l'ordinateur.
3. **Construire l'appli signée** : onglet *Actions* > « Applications mobiles » > *Run workflow* (version `1.0.0`).
   Au bout d'une vingtaine de minutes, télécharger l'artifact `android-…` : il contient
   `gauchise-tes-parents-google-play.aab` (pour la Play Console) et `gauchise-tes-parents-test.apk` (à installer
   directement sur ton téléphone pour essayer).
4. **Dans la Play Console, une fois le compte validé** : *Créer une application* (nom « Gauchise tes parents »,
   français, application, gratuite), puis remplir les rubriques avec `mobile/store/FICHES-BOUTIQUES.md`
   (fiche Play Store, classification, public cible, sécurité des données, annonces, accès).
   Accepter la *signature d'application par Google Play* (proposée par défaut).
5. **Test fermé** : *Tester* > *Test fermé* > créer une piste, ajouter la liste des testeurs (adresses Gmail),
   téléverser l'AAB, envoyer pour examen. Les testeurs reçoivent un lien d'inscription : ils doivent l'accepter,
   installer l'appli et la garder **14 jours**. Il faut au moins **12 testeurs inscrits en continu**.
6. **Après 14 jours** : *Demander l'accès à la production* (questionnaire sur le test), puis publier. Compter
   quelques jours d'examen : publication réaliste vers la mi-décembre.

## Le 22 novembre : App Store

1. **S'inscrire à l'Apple Developer Program** sur https://developer.apple.com/programs/ (abonnement annuel ; vérifier
   le tarif affiché). Il faut un identifiant Apple avec la double authentification ; la validation prend en général
   un à deux jours.
2. **Créer l'identifiant de l'appli** : sur developer.apple.com > *Certificates, Identifiers & Profiles* >
   *Identifiers* > `+` > *App IDs* > `fr.gauchisetesparents.app` (aucune capacité particulière à cocher).
3. **Créer la fiche** dans https://appstoreconnect.apple.com > *Apps* > `+` > *Nouvelle app* : plateforme iOS,
   nom « Gauchise tes parents », langue française, identifiant `fr.gauchisetesparents.app`, SKU `gauchise-001`.
   Remplir avec `mobile/store/FICHES-BOUTIQUES.md` et téléverser les captures `iphone-6.9-pouces` et `ipad-13-pouces`.
4. **Envoyer l'appli sans Mac** (recommandé) : App Store Connect > *Utilisateurs et accès* > *Intégrations* >
   *Clés d'API de l'App Store Connect* > générer une clé avec le rôle **Admin**, télécharger le fichier `.p8`
   (téléchargeable une seule fois). Puis dans GitHub, quatre secrets :
   - `APPSTORE_KEY_P8_BASE64` : le contenu du fichier `.p8` encodé en base64
     (Mac : `base64 -i AuthKey_XXXX.p8 | pbcopy` ; Windows PowerShell :
     `[Convert]::ToBase64String([IO.File]::ReadAllBytes("AuthKey_XXXX.p8")) | Set-Clipboard`) ;
   - `APPSTORE_KEY_ID` : l'identifiant de la clé ; `APPSTORE_ISSUER_ID` : l'identifiant de l'émetteur (en haut de la page des clés) ;
   - `APPLE_TEAM_ID` : l'identifiant d'équipe (developer.apple.com > *Membership details*).
   Relancer « Applications mobiles » : l'appli est signée et envoyée sur TestFlight automatiquement.
   **Avec un Mac** (autre possibilité) : ouvrir `ios/App/App.xcworkspace` (fichier `ios-…` de l'artifact, ou
   `bash scripts/mobile/preparer-natif.sh ios` sur le Mac), choisir l'équipe dans *Signing & Capabilities*,
   puis *Product* > *Archive* > *Distribute App*.
5. **TestFlight** (facultatif mais conseillé) : inviter quelques testeurs par e-mail pour vérifier l'appli.
6. **Soumettre à l'examen** : choisir la version envoyée, vérifier les textes et les notes pour l'examinateur,
   *Soumettre pour vérification*. Examen en général en un à trois jours.

## Risques connus et parades

- **Refus « simple site emballé » (règle 4.2 d'Apple)** : l'appli fonctionne sans connexion avec sa bibliothèque
  embarquée, la recherche se fait sur l'appareil, le partage et le bouton retour sont natifs ; ces points sont dans
  les notes pour l'examinateur. En cas de refus, répondre dans le Centre de résolution en les rappelant ; si
  nécessaire, on ajoutera une fonction propre à l'appli (par exemple des favoris ou des notifications de nouvelles fiches).
- **Contenu politique** : Apple accepte tous les points de vue « tant que les applis respectent les utilisateurs aux
  opinions différentes » (introduction des règles). Le ton des fiches (répondre sans humilier) va dans ce sens.
- **Dons** : Tipeee reste masqué dans l'appli (règles 3.1.1 et 3.2.1 d'Apple, version du 16 octobre 2026). Ne pas
  utiliser `--avec-soutien` sans vérifier les règles en vigueur des deux boutiques.
- **Identifiant `fr.gauchisetesparents.app`** : définitif après la première publication ; à changer avant le 21 si
  tu en préfères un autre (dans `capacitor.config.json`).

## Rythme des mises à jour (décidé le 19 novembre 2026)

- **Site (GitHub Pages)** : mis à jour à chaque modification (environ 30 minutes, le temps des tests). C'est la
  version de suivi, celle des soutiens.
- **Applis** : une version tous les 3 jours, construite automatiquement par le flux « Applications mobiles », qui
  regroupe toutes les modifications faites entre-temps. Une version n'arrive au public qu'après l'envoi dans les
  boutiques et leur examen (Apple : en général 1 à 3 jours) : on ne soumet pas de nouvelle version tant que la
  précédente est en cours d'examen.
- Les nouvelles fiches pourront arriver dans les applis sans nouvelle version, une fois le téléchargement de la base
  depuis le site mis en place.

## Fonctionnement technique

- `scripts/mobile/build-mobile.js` : dossier web de l'appli (`dist/mobile/www`), base embarquée, sans service worker,
  sans IA ni serveur, Tipeee masqué (`--avec-soutien` pour l'afficher).
- `scripts/mobile/preparer-natif.sh android|ios [build] [version]` : installe Capacitor 7 (sans l'ajouter au
  `package.json` du site), génère le projet natif, les icônes et écrans de lancement (`mobile/assets/`) et règle
  les numéros de version. Les dossiers `android/` et `ios/` ne sont pas versionnés.
- `.github/workflows/applis.yml` : construit tout sur les serveurs de GitHub (Linux pour Android, macOS pour iOS),
  tous les 3 jours ou à la demande ; signe et envoie seulement si les secrets existent.
  Le numéro de build augmente tout seul (100 + numéro du run), comme l'exigent les deux boutiques.
- Captures d'écran : régénérables avec Playwright à partir de `dist/mobile/www` (aux tailles indiquées dans les noms
  des dossiers de `mobile/store/captures/`).
