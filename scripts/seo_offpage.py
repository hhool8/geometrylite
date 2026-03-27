#!/usr/bin/env python3
"""
SEO Off-Page Setup: injects Twitter Card meta tags and fixes share modal URL.
Run from repo root: python3 scripts/seo_offpage.py
"""
import re, os

DOMAIN = open('.domain').read().strip()

# Map each HTML file → its canonical URL path
PAGES = {
    'index.html':               f'https://{DOMAIN}',
    'egg-dash.html':            f'https://{DOMAIN}/egg-dash',
    'wave-dash.html':           f'https://{DOMAIN}/wave-dash',
    'geometry-lite-classic.html': f'https://{DOMAIN}/geometry-lite-classic',
    'geometry-jump.html':       f'https://{DOMAIN}/geometry-jump',
    'geometry-game-3d.html':    f'https://{DOMAIN}/geometry-game-3d',
    'spooky-dash.html':         f'https://{DOMAIN}/spooky-dash',
    'tap-road-beat.html':       f'https://{DOMAIN}/tap-road-beat',
    'xmas-dash.html':           f'https://{DOMAIN}/xmas-dash',
    'about-us.html':            f'https://{DOMAIN}/about-us',
    'contact-us.html':          f'https://{DOMAIN}/contact-us',
    'dmca.html':                f'https://{DOMAIN}/dmca',
    'privacy-policy.html':      f'https://{DOMAIN}/privacy-policy',
    'terms-of-service.html':    f'https://{DOMAIN}/terms-of-service',
    '404.html':                 f'https://{DOMAIN}/404',
    'favorite.html':            f'https://{DOMAIN}/favorite',
}

def extract_og(content, prop):
    m = re.search(rf'<meta property="og:{prop}" content="([^"]*)"', content)
    return m.group(1) if m else ''

def add_twitter_cards(content, title, description, image):
    if 'name="twitter:card"' in content:
        return content  # already present
    twitter_tags = (
        f'<meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:title" content="{title}">'
        f'<meta name="twitter:description" content="{description}">'
        f'<meta name="twitter:image" content="{image}">'
        f'<meta name="twitter:site" content="@geometrylite">'
    )
    # Insert after last og: meta tag
    insert_after = '<meta property="og:image"'
    idx = content.rfind(insert_after)
    if idx == -1:
        # fallback: insert before </head> or viewport
        idx = content.find('<meta name="viewport"')
        if idx == -1:
            return content
        return content[:idx] + twitter_tags + content[idx:]
    end = content.find('>', idx) + 1
    return content[:end] + twitter_tags + content[end:]

def fix_share_url(content, page_url):
    # Fix hardcoded github.io share URL in share modal
    fixed = re.sub(
        r'(id="share_link_input"\s+value=")[^"]*(")',
        rf'\g<1>{page_url}\g<2>',
        content
    )
    return fixed

for filename, page_url in PAGES.items():
    if not os.path.exists(filename):
        print(f'SKIP (not found): {filename}')
        continue

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    title = extract_og(content, 'title') or 'Geometry Dash Lite Unblocked'
    description = extract_og(content, 'description') or 'Play Geometry Dash Lite Unblocked free online.'
    image = extract_og(content, 'image') or f'https://{DOMAIN}/cache/data/image/options/favicon-s512x512.png'

    content = add_twitter_cards(content, title, description, image)
    content = fix_share_url(content, page_url)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated: {filename}')

print('Done.')
