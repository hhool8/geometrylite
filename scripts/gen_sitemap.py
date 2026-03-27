#!/usr/bin/env python3
"""
gen_sitemap.py — Regenerate sitemap.xml with lastmod from git commit dates.

Each URL is mapped to its corresponding HTML file. lastmod is taken from
`git log -1 --format=%ci <file>` so it reflects the actual last-modified commit.
Falls back to today's date for untracked files.

Usage:
    python3 scripts/gen_sitemap.py [--domain https://geometrylite.poki2.online]
"""
import os, subprocess, sys
from datetime import date

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ── Read domain from .domain file or CLI arg
def get_domain():
    for arg in sys.argv[1:]:
        if arg.startswith("--domain"):
            parts = arg.split("=", 1)
            if len(parts) == 2:
                return parts[1].rstrip("/")
            # --domain https://...
            idx = sys.argv.index(arg)
            if idx + 1 < len(sys.argv):
                return sys.argv[idx + 1].rstrip("/")
    domain_file = os.path.join(BASE, ".domain")
    if os.path.exists(domain_file):
        d = open(domain_file).read().strip().rstrip("/")
        if not d.startswith("http"):
            d = "https://" + d
        return d
    return "https://geometrylite.poki2.online"

DOMAIN = get_domain()

# ── URL → (local_file, changefreq, priority)
# local_file is relative to BASE; use the primary HTML file that represents the page
PAGES = [
    ("/",                   "index.html",                    "daily",   "1.0"),
    ("/geometry-dash-lite", "game/geometry-dash/index.html", "weekly",  "0.9"),
    ("/geometry-lite-classic", "geometry-lite-classic.html", "weekly",  "0.8"),
    ("/geometry-jump",      "geometry-jump.html",            "weekly",  "0.8"),
    ("/geometry-game-3d",   "geometry-game-3d.html",         "weekly",  "0.8"),
    ("/tap-road-beat",      "tap-road-beat.html",            "weekly",  "0.7"),
    ("/wave-dash",          "wave-dash.html",                "weekly",  "0.7"),
    ("/egg-dash",           "egg-dash.html",                 "weekly",  "0.7"),
    ("/spooky-dash",        "spooky-dash.html",              "weekly",  "0.7"),
    ("/xmas-dash",          "xmas-dash.html",                "weekly",  "0.7"),
    ("/new-games",          "index.html",                    "daily",   "0.6"),
    ("/hot-games",          "index.html",                    "daily",   "0.6"),
    ("/top-popular",        "index.html",                    "daily",   "0.6"),
    ("/about-us",           "about-us.html",                 "monthly", "0.3"),
    ("/contact-us",         "contact-us.html",               "monthly", "0.3"),
    ("/dmca",               "dmca.html",                     "monthly", "0.2"),
    ("/privacy-policy",     "privacy-policy.html",           "monthly", "0.2"),
    ("/terms-of-service",   "terms-of-service.html",         "monthly", "0.2"),
]

def git_lastmod(rel_path):
    """Return YYYY-MM-DD of the last git commit touching rel_path, or today."""
    abs_path = os.path.join(BASE, rel_path)
    if not os.path.exists(abs_path):
        return str(date.today())
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%ci", "--", rel_path],
            cwd=BASE,
            capture_output=True, text=True, timeout=10
        )
        line = result.stdout.strip()
        if line:
            return line[:10]  # "YYYY-MM-DD"
    except Exception:
        pass
    return str(date.today())

# ── Build XML
lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
    ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"'
    ' xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9'
    ' http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">',
]

for path, local_file, changefreq, priority in PAGES:
    lastmod = git_lastmod(local_file)
    loc = DOMAIN + path
    lines.append(
        f'  <url>'
        f'<loc>{loc}</loc>'
        f'<lastmod>{lastmod}</lastmod>'
        f'<changefreq>{changefreq}</changefreq>'
        f'<priority>{priority}</priority>'
        f'</url>'
    )

lines.append("</urlset>")

out = "\n".join(lines) + "\n"
out_path = os.path.join(BASE, "sitemap.xml")
with open(out_path, "w") as f:
    f.write(out)

print(f"Generated {out_path}  ({len(PAGES)} URLs, domain={DOMAIN})")
for path, local_file, changefreq, priority in PAGES:
    print(f"  {path:<30}  lastmod={git_lastmod(local_file)}  ({local_file})")
