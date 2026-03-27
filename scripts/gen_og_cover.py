#!/usr/bin/env python3
"""
Generate a 1200x630 OG cover image for geometrylite.poki2.online.
Output: data/image/options/og-cover.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

W, H = 1200, 630

# ── background: dark gradient-like solid (deep navy)
bg = Image.new("RGBA", (W, H), (15, 15, 35, 255))
draw = ImageDraw.Draw(bg)

# subtle horizontal bands to mimic gradient
for y in range(H):
    t = y / H
    r = int(15 + t * 10)
    g = int(15 + t * 5)
    b = int(35 + t * 25)
    draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

# ── game thumbnail (186×186 → upscale to ~320×320)
thumb_path = os.path.join(BASE, "data/image/game/geometry-dash/geometry-lite-game.png")
thumb = Image.open(thumb_path).convert("RGBA")
thumb_size = 320
thumb = thumb.resize((thumb_size, thumb_size), Image.LANCZOS)

# center thumbnail slightly left of center
thumb_x = (W // 2 - thumb_size) // 2 + 40
thumb_y = (H - thumb_size) // 2
bg.paste(thumb, (thumb_x, thumb_y), thumb)

# ── logo image (218×80 → scale to ~360×132)
logo_path = os.path.join(BASE, "cache/data/image/options/geometry-lite.io-f200x80.png")
logo = Image.open(logo_path).convert("RGBA")
logo_w, logo_h = 360, int(360 * 80 / 218)
logo = logo.resize((logo_w, logo_h), Image.LANCZOS)

text_area_x = W // 2 + 40
logo_x = text_area_x
logo_y = H // 2 - logo_h - 30

bg.paste(logo, (logo_x, logo_y), logo)

# ── tagline text below logo
draw2 = ImageDraw.Draw(bg)

# Try to load a system font; fall back to default
try:
    font_lg = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    font_sm = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 26)
except Exception:
    font_lg = ImageFont.load_default()
    font_sm = font_lg

tagline = "Play Free Unblocked Games"
sub     = "No download · Works at school · Chromebook"

# tagline
tl_x = text_area_x
tl_y = logo_y + logo_h + 20
draw2.text((tl_x, tl_y), tagline, font=font_lg, fill=(200, 230, 255, 255))

# subtitle
draw2.text((tl_x, tl_y + 52), sub, font=font_sm, fill=(140, 180, 220, 255))

# thin accent line between logo and text
draw2.line([(text_area_x, logo_y + logo_h + 14),
            (text_area_x + logo_w, logo_y + logo_h + 14)],
           fill=(80, 140, 220, 180), width=2)

# ── save
out_dir = os.path.join(BASE, "data/image/options")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "og-cover.png")
bg.convert("RGB").save(out_path, "PNG", optimize=True)
print(f"Saved: {out_path}  size: {Image.open(out_path).size}")
