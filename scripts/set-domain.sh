#!/usr/bin/env bash
# set-domain.sh — Replace all absolute domain references in the site.
# Usage: ./scripts/set-domain.sh <new-domain>
# Example: ./scripts/set-domain.sh geometrylite.example.com
#
# The current domain is read from the .domain file in the project root.
# After replacement, .domain is updated to the new domain.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
DOMAIN_FILE="$ROOT_DIR/.domain"

if [ $# -ne 1 ]; then
  echo "Usage: $0 <new-domain>"
  echo "Example: $0 geometrylite.example.com"
  exit 1
fi

NEW_DOMAIN="$1"

if [ ! -f "$DOMAIN_FILE" ]; then
  echo "Error: .domain file not found at $DOMAIN_FILE"
  exit 1
fi

OLD_DOMAIN="$(cat "$DOMAIN_FILE" | tr -d '[:space:]')"

if [ "$OLD_DOMAIN" = "$NEW_DOMAIN" ]; then
  echo "Domain is already set to: $NEW_DOMAIN — no changes needed."
  exit 0
fi

echo "Replacing: $OLD_DOMAIN  →  $NEW_DOMAIN"
echo ""

# Files to update: all HTML files, sitemap.xml, robots.txt, CNAME
FILES=$(find "$ROOT_DIR" \
  -maxdepth 2 \
  \( -name "*.html" -o -name "sitemap.xml" -o -name "robots.txt" -o -name "CNAME" \) \
  -not -path "*/.git/*" \
  -not -path "*/embed/*" \
  -not -path "*/cache/*")

COUNT=0
for f in $FILES; do
  if grep -q "$OLD_DOMAIN" "$f" 2>/dev/null; then
    sed -i '' "s|${OLD_DOMAIN}|${NEW_DOMAIN}|g" "$f"
    echo "  Updated: $(basename "$f")"
    COUNT=$((COUNT + 1))
  fi
done

# Update .domain file
echo "$NEW_DOMAIN" > "$DOMAIN_FILE"

echo ""
echo "Done. Updated $COUNT file(s). Active domain: $NEW_DOMAIN"
