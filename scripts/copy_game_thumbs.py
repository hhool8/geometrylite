"""Copy m186x186 cache thumbs into data/image/game/ as og:image sources."""
import shutil, os

ROOT = "/Users/yanmenghou/Desktop/h5games/geometrylite"

copies = [
    ("cache/data/image/game/egg-dash/egg-dash-m186x186.png",
     "data/image/game/egg-dash/egg-dash.png"),
    ("cache/data/image/game/geometry-dash/geometry-lite-game-m186x186.png",
     "data/image/game/geometry-dash/geometry-lite-game.png"),
    ("cache/data/image/game/geometry-game-3d/geometry-game-3d-m186x186.png",
     "data/image/game/geometry-game-3d/geometry-game-3d.png"),
    ("cache/data/image/game/geometry-jump/geometry-jump-m186x186.png",
     "data/image/game/geometry-jump/geometry-jump.png"),
    ("cache/data/image/game/geometry-lite-classic/geometry-lite-classic-m186x186.png",
     "data/image/game/geometry-lite-classic/geometry-lite-classic.png"),
    ("cache/data/image/game/spooky-dash/spooky-dash-m186x186.png",
     "data/image/game/spooky-dash/spooky-dash.png"),
    ("cache/data/image/game/tap-road-beat/tap-road-beat-game-m186x186.png",
     "data/image/game/tap-road-beat/tap-road-beat-game.png"),
    ("cache/data/image/game/tap-road-beat/tap-road-beat-game-m186x186.png",
     "data/image/game/tap-road-beat/tap-road-beat.png"),
    ("cache/data/image/game/wave-dash/wave-dash-m186x186.png",
     "data/image/game/wave-dash/wave-dash.png"),
    ("cache/data/image/game/xmas-dash/xmas-dash-m186x186.png",
     "data/image/game/xmas-dash/xmas-dash.png"),
]

for src_rel, dst_rel in copies:
    src = os.path.join(ROOT, src_rel)
    dst = os.path.join(ROOT, dst_rel)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    size_kb = os.path.getsize(dst) // 1024
    print(f"  OK ({size_kb}K): {dst_rel}")

print("\nDone.")
