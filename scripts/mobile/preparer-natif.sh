#!/usr/bin/env bash
# Génère le projet natif Android ou iOS (Capacitor) à partir du site : utilisé par le flux GitHub Actions
# « Applications mobiles » et utilisable tel quel sur un Mac (Node 20+, et Xcode + CocoaPods pour iOS).
# Usage : bash scripts/mobile/preparer-natif.sh android|ios [numéro de build] [version affichée]
# Les dossiers android/ et ios/ ne sont pas versionnés : ils sont régénérés à chaque fois (voir .gitignore).
set -euo pipefail
PLATEFORME="${1:?android ou ios}"
BUILD="${2:-1}"
VERSION="${3:-1.0.0}"
CAP=7   # version majeure de Capacitor (Node 20+, Java 21, Xcode 16)
cd "$(dirname "$0")/../.."

npm install --no-save --no-audit --no-fund \
  "@capacitor/core@^$CAP" "@capacitor/cli@^$CAP" "@capacitor/app@^$CAP" "@capacitor/share@^$CAP" \
  "@capacitor/$PLATEFORME@^$CAP" "@capacitor/assets@^3"

npm run build:mobile -- --plateforme "$PLATEFORME"
rm -rf "$PLATEFORME"
npx cap add "$PLATEFORME"
# icônes et écrans de lancement à partir de mobile/assets (icône, premier plan adaptatif Android, écrans clair/sombre)
npx capacitor-assets generate --"$PLATEFORME" --assetPath mobile/assets \
  --iconBackgroundColor '#2B1A5C' --iconBackgroundColorDark '#2B1A5C' \
  --splashBackgroundColor '#FFF7E6' --splashBackgroundColorDark '#2B1A5C'
npx cap sync "$PLATEFORME"

if [ "$PLATEFORME" = android ]; then
  G=android/app/build.gradle
  sed -i.bak -E "s/versionCode [0-9]+/versionCode $BUILD/; s/versionName \"[^\"]*\"/versionName \"$VERSION\"/" "$G" && rm -f "$G.bak"
  grep -E "versionCode|versionName|applicationId" "$G"
else
  P=ios/App/App.xcodeproj/project.pbxproj
  sed -i.bak -E "s/CURRENT_PROJECT_VERSION = [^;]+;/CURRENT_PROJECT_VERSION = $BUILD;/g; s/MARKETING_VERSION = [^;]+;/MARKETING_VERSION = $VERSION;/g" "$P" && rm -f "$P.bak"
  # pas de chiffrement propre à l'appli (HTTPS du système seulement) : évite la question d'exportation à chaque envoi
  /usr/libexec/PlistBuddy -c "Add :ITSAppUsesNonExemptEncryption bool false" ios/App/App/Info.plist 2>/dev/null \
    || /usr/libexec/PlistBuddy -c "Set :ITSAppUsesNonExemptEncryption false" ios/App/App/Info.plist
  /usr/libexec/PlistBuddy -c "Set :CFBundleDisplayName Gauchise tes parents" ios/App/App/Info.plist || true
  grep -E "CURRENT_PROJECT_VERSION|MARKETING_VERSION" "$P" | sort -u
fi
echo "Projet $PLATEFORME prêt (build $BUILD, version $VERSION)."
