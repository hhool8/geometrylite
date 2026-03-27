#!/usr/bin/env python3
import json, os

DOMAIN = "https://geometrylite.poki2.online"
CDN    = "https://geometrylite.github.io"

pages = {
    "egg-dash.html": {
        "name": "Egg Dash", "slug": "egg-dash",
        "desc": "Play Egg Dash Unblocked free online! A fun Easter platformer with rhythm-based gameplay. Glide through danger and tackle every map now.",
        "img_path": "/data/image/game/egg-dash/egg-dash.png",
        "genres": ["Platformer","Arcade"]
    },
    "wave-dash.html": {
        "name": "Wave Dash", "slug": "wave-dash",
        "desc": "Play Wave Dash Unblocked free online! Guide your cube through perilous tunnels in this rhythm platformer. Conquer all dangers now.",
        "img_path": "/data/image/game/wave-dash/wave-dash.png",
        "genres": ["Platformer","Rhythm","Arcade"]
    },
    "geometry-lite-classic.html": {
        "name": "Geometry Lite Classic", "slug": "geometry-lite-classic",
        "desc": "Play Geometry Lite Classic Unblocked free online! Master every jump where timing and reflexes meet music. Race through each challenge today.",
        "img_path": "/data/image/game/geometry-lite-classic/geometry-lite-classic.png",
        "genres": ["Platformer","Rhythm","Arcade"]
    },
    "geometry-jump.html": {
        "name": "Geometry Jump", "slug": "geometry-jump",
        "desc": "Play Geometry Jump Unblocked free online! A fast-paced rhythm platformer. Jump through obstacles and beat every level.",
        "img_path": "/data/image/game/geometry-jump/geometry-jump.png",
        "genres": ["Platformer","Arcade"]
    },
    "geometry-game-3d.html": {
        "name": "Geometry Game 3D", "slug": "geometry-game-3d",
        "desc": "Play Geometry Game 3D Unblocked free online! Experience geometry-based gameplay in stunning 3D. Dash through obstacles now.",
        "img_path": "/data/image/game/geometry-game-3d/geometry-game-3d.png",
        "genres": ["Platformer","3D","Arcade"]
    },
    "spooky-dash.html": {
        "name": "Spooky Dash", "slug": "spooky-dash",
        "desc": "Play Spooky Dash Unblocked free online! A Halloween platformer — dash through creepy tunnels and avoid obstacles now.",
        "img_path": "/data/image/game/spooky-dash/spooky-dash.png",
        "genres": ["Platformer","Arcade"]
    },
    "tap-road-beat.html": {
        "name": "Tap Road Beat", "slug": "tap-road-beat",
        "desc": "Play Tap Road Beat Unblocked free online! Sync your taps to the beat in this addictive rhythm game. Hit every note now.",
        "img_path": "/data/image/game/tap-road-beat/tap-road-beat.png",
        "genres": ["Rhythm","Arcade"]
    },
    "xmas-dash.html": {
        "name": "Xmas Dash", "slug": "xmas-dash",
        "desc": "Play Xmas Dash Unblocked free online! A Christmas-themed rhythm platformer. Dash through festive obstacles now.",
        "img_path": "/data/image/game/xmas-dash/xmas-dash.png",
        "genres": ["Platformer","Arcade"]
    },
}

MARKER = '<meta name="google-site-verification"'

for filename, info in pages.items():
    if not os.path.exists(filename):
        print(f"SKIP (not found): {filename}")
        continue
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    if '"@type":"VideoGame"' in content:
        print(f"SKIP (schema exists): {filename}")
        continue
    schema = {
        "@context": "https://schema.org",
        "@type": "VideoGame",
        "name": info["name"],
        "alternateName": [f"{info['name']} Unblocked", f"{info['name']} Unblocked Games"],
        "description": info["desc"],
        "url": f"{DOMAIN}/{info['slug']}",
        "image": f"{CDN}{info['img_path']}",
        "applicationCategory": "Game",
        "genre": info["genres"],
        "operatingSystem": "Web Browser",
        "gamePlatform": "Web Browser",
        "isFamilyFriendly": True,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "publisher": {"@type": "Organization", "name": "Geometry Lite", "url": DOMAIN}
    }
    schema_tag = f'<script type="application/ld+json">{json.dumps(schema, separators=(",",":"))}</script>'
    new_content = content.replace(MARKER, schema_tag + MARKER, 1)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Updated: {filename}")

print("Done.")
