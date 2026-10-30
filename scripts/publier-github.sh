#!/usr/bin/env bash
# Publie le site (mode autonome, gratuit) sur GitHub Pages en une commande.
# Prérequis : git et l'outil GitHub « gh » (https://cli.github.com), puis `gh auth login` une fois.
# Usage : bash scripts/publier-github.sh [nom-du-depot]
set -euo pipefail
REPO="${1:-gauchise-tes-parents}"
cd "$(dirname "$0")/.."

command -v gh >/dev/null || { echo "Installe d'abord l'outil GitHub : https://cli.github.com"; exit 1; }
gh auth status >/dev/null 2>&1 || gh auth login
OWNER="$(gh api user --jq .login)"

# Garde-fous : aucun secret ni donnée personnelle dans le dépôt public
for f in .env data/usage data/feedback; do
  if [ -e "$f" ] && ! git check-ignore -q "$f" 2>/dev/null && [ -d .git ]; then echo "Refus : $f ne doit pas être publié."; exit 1; fi
done
if grep -RIl --exclude-dir=node_modules --exclude-dir=.git -E "sk-ant-[A-Za-z0-9_-]{20,}" . >/dev/null 2>&1; then echo "Refus : une clé API semble présente dans les fichiers."; exit 1; fi

npm test

[ -d .git ] || git init -b main
git add -A
git -c user.name="${GIT_NAME:-$OWNER}" -c user.email="${GIT_EMAIL:-$OWNER@users.noreply.github.com}" commit -m "Publication de Gauchise tes parents" || true

if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  git remote get-url origin >/dev/null 2>&1 || git remote add origin "https://github.com/$OWNER/$REPO.git"
  git push -u origin main
else
  gh repo create "$REPO" --public --source=. --remote=origin --push --description "Gauchise tes parents — éducation populaire et préparation au débat, sources vérifiées"
fi

# Active GitHub Pages avec « GitHub Actions » comme source (sans effet si déjà actif)
gh api -X POST "repos/$OWNER/$REPO/pages" -f build_type=workflow >/dev/null 2>&1 || gh api -X PUT "repos/$OWNER/$REPO/pages" -f build_type=workflow >/dev/null 2>&1 || true
gh workflow run pages.yml --repo "$OWNER/$REPO" >/dev/null 2>&1 || true

echo
echo "Publication lancée. Suis-la ici : https://github.com/$OWNER/$REPO/actions"
echo "Adresse publique (active après la coche verte, en général 1 à 3 minutes) :"
echo "  https://$OWNER.github.io/$REPO/"
echo "Mises à jour ensuite : git add -A && git commit -m \"...\" && git push"
