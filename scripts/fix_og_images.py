#!/usr/bin/env python3
"""Fix 404.html github.io image ref + update homepage og:image to 1200x630 cover."""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── 404.html: replace github.io image URL
path_404 = os.path.join(BASE, "404.html")
with open(path_404) as f:
    c404 = f.read()

old_404 = "https://geometrylite.github.io//data/image/options/geometry-lite.io.png"
new_404 = "https://geometrylite.poki2.online/data/image/options/og-cover.png"
cnt = c404.count(old_404)
c404_new = c404.replace(old_404, new_404)
with open(path_404, "w") as f:
    f.write(c404_new)
print(f"404.html: {cnt} replacements (github.io → og-cover.png)")

# ── index.html: update og:image / twitter:image / link rel=image_src
#    from 186×186 game thumbnail → 1200×630 og-cover
#    keep VideoGame schema image pointing to the game thumbnail
path_idx = os.path.join(BASE, "index.html")
with open(path_idx) as f:
    cidx = f.read()

old_thumb = "https://geometrylite.poki2.online/data/image/game/geometry-dash/geometry-lite-game.png"
new_cover = "https://geometrylite.poki2.online/data/image/options/og-cover.png"

# replace only in meta og:image, twitter:image, and link rel=image_src
patterns = [
    (r'(property="og:image"\s+content=")' + re.escape(old_thumb) + '"',
     r'\g<1>' + new_cover + '"'),
    (r'(name="twitter:image"\s+content=")' + re.escape(old_thumb) + '"',
     r'\g<1>' + new_cover + '"'),
    (r'(rel="image_src"\s+href=")' + re.escape(old_thumb) + '"',
     r'\g<1>' + new_cover + '"'),
]
cidx_new = cidx
total = 0
for pattern, repl in patterns:
    cidx_new, n = re.subn(pattern, repl, cidx_new)
    total += n

with open(path_idx, "w") as f:
    f.write(cidx_new)
remaining = cidx_new.count(old_thumb)
print(f"index.html: {total} meta og/twitter/image_src replaced  |  {remaining} schema refs kept as-is")
