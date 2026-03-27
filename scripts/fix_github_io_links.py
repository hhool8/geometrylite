"""
Fix residual geometrylite.github.io references.
Safe replacements only — game thumbnail images (not in repo) are left untouched.
"""
import re
import glob

SAFE_REPLACEMENTS = [
    # 1. JS config variable domain_url
    ("domain_url: 'https://geometrylite.github.io',",
     "domain_url: 'https://geometrylite.poki2.online',"),
    # 2. favicon absolute URLs -> relative paths (files exist locally)
    ("https://geometrylite.github.io/favicon.ico?v=3",
     "/favicon.ico?v=3"),
    ("https://geometrylite.github.io/cache/data/image/options/favicon-s512x512.png",
     "/cache/data/image/options/favicon-s512x512.png"),
    # 3. navigation hrefs
    ("https://geometrylite.github.io/top-popular",
     "https://geometrylite.poki2.online/top-popular"),
    ("https://geometrylite.github.io/new-games",
     "https://geometrylite.poki2.online/new-games"),
    ("https://geometrylite.github.io/hot-games",
     "https://geometrylite.poki2.online/hot-games"),
    # 4. text links in legal pages
    ("https://geometrylite.github.io/privacy-policy",
     "https://geometrylite.poki2.online/privacy-policy"),
    ("https://geometrylite.github.io/contact-us",
     "https://geometrylite.poki2.online/contact-us"),
    # 5. game page hrefs in embed/game subdirectories
    ("https://geometrylite.github.io/game/geometry-lite-classic/",
     "https://geometrylite.poki2.online/game/geometry-lite-classic/"),
    ("https://geometrylite.github.io/game/geometry-game-3d/",
     "https://geometrylite.poki2.online/game/geometry-game-3d/"),
    # 6. geometry-dash link in game pages
    ("https://geometrylite.github.io/game/geometry-dash/",
     "https://geometrylite.poki2.online/game/geometry-dash/"),
]

html_files = glob.glob("**/*.html", recursive=True)
total_changes = 0

for fpath in sorted(html_files):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content
    for old, new in SAFE_REPLACEMENTS:
        count = new_content.count(old)
        if count:
            new_content = new_content.replace(old, new)
            print(f"  [{count}x] {fpath}: ...{old[30:70]}...")
            total_changes += count
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)

print(f"\nTotal replacements: {total_changes}")

print("\nRemaining geometrylite.github.io refs (image assets not in this repo — intentionally kept):")
remaining = set()
for fpath in html_files:
    with open(fpath, "r", encoding="utf-8") as f:
        for m in re.findall(r'geometrylite\.github\.io[^\s"\'<>]*', f.read()):
            remaining.add(m)
for r in sorted(remaining):
    print(f"  {r}")
