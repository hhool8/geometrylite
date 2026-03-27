"""
Download game thumbnail images from geometrylite.github.io into local data/image/game/
and update all HTML references to use relative local paths.
"""
import os
import urllib.request
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

IMAGES = [
    ("data/image/game/egg-dash/egg-dash.png",
     "https://geometrylite.github.io/data/image/game/egg-dash/egg-dash.png"),
    ("data/image/game/geometry-dash/geometry-lite-game.png",
     "https://geometrylite.github.io/data/image/game/geometry-dash/geometry-lite-game.png"),
    ("data/image/game/geometry-game-3d/geometry-game-3d.png",
     "https://geometrylite.github.io/data/image/game/geometry-game-3d/geometry-game-3d.png"),
    ("data/image/game/geometry-jump/geometry-jump.png",
     "https://geometrylite.github.io/data/image/game/geometry-jump/geometry-jump.png"),
    ("data/image/game/geometry-lite-classic/geometry-lite-classic.png",
     "https://geometrylite.github.io/data/image/game/geometry-lite-classic/geometry-lite-classic.png"),
    ("data/image/game/geometry-lite-game.png",
     "https://geometrylite.github.io/data/image/game/geometry-lite-game.png"),
    ("data/image/game/spooky-dash/spooky-dash.png",
     "https://geometrylite.github.io/data/image/game/spooky-dash/spooky-dash.png"),
    ("data/image/game/tap-road-beat/tap-road-beat-game.png",
     "https://geometrylite.github.io/data/image/game/tap-road-beat/tap-road-beat-game.png"),
    ("data/image/game/tap-road-beat/tap-road-beat.png",
     "https://geometrylite.github.io/data/image/game/tap-road-beat/tap-road-beat.png"),
    ("data/image/game/wave-dash/wave-dash.png",
     "https://geometrylite.github.io/data/image/game/wave-dash/wave-dash.png"),
    ("data/image/game/xmas-dash/xmas-dash.png",
     "https://geometrylite.github.io/data/image/game/xmas-dash/xmas-dash.png"),
]

# --- Step 1: Download images ---
print("=== Downloading game thumbnails ===")
downloaded = []
for rel_path, url in IMAGES:
    dest = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 1000:
        print(f"  SKIP (exists): {rel_path}")
        downloaded.append(rel_path)
        continue
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        size_kb = os.path.getsize(dest) // 1024
        print(f"  OK  ({size_kb}K): {rel_path}")
        downloaded.append(rel_path)
    except Exception as e:
        print(f"  FAIL: {rel_path} — {e}")

# --- Step 2: Replace github.io image URLs with local absolute URLs ---
print("\n=== Updating HTML references ===")
BASE_URL = "https://geometrylite.poki2.online"
html_files = glob.glob(os.path.join(ROOT, "**/*.html"), recursive=True)
html_files += glob.glob(os.path.join(ROOT, "*.html"))
html_files = list(set(html_files))

total_changes = 0
for fpath in sorted(html_files):
    if "/.git/" in fpath or "/cache/" in fpath:
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content
    for rel_path, old_url in IMAGES:
        if old_url in new_content:
            new_url = BASE_URL + "/" + rel_path
            count = new_content.count(old_url)
            new_content = new_content.replace(old_url, new_url)
            print(f"  [{count}x] {os.path.relpath(fpath, ROOT)}: ...{rel_path}")
            total_changes += count
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)

print(f"\nTotal HTML replacements: {total_changes}")

# --- Step 3: Verify no more github.io game image refs ---
print("\n=== Remaining github.io/data/image/game refs ===")
remaining = []
for fpath in html_files:
    if "/.git/" in fpath or "/cache/" in fpath:
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        if "geometrylite.github.io/data/image/game" in f.read():
            remaining.append(os.path.relpath(fpath, ROOT))
if remaining:
    for r in sorted(remaining):
        print(f"  {r}")
else:
    print("  None — all game image refs migrated to poki2.online")
