#!/usr/bin/env python3
"""
Fix relative/wrong canonical + og:url on support pages.
Run from repo root: python3 scripts/fix_support_pages.py
"""
import re, os

domain = open('.domain').read().strip()

fixes = {
    'about-us.html':         '/about-us',
    'contact-us.html':       '/contact-us',
    'dmca.html':             '/dmca',
    'favorite.html':         '/favorite',
    'privacy-policy.html':   '/privacy-policy',
    'terms-of-service.html': '/terms-of-service',
}

for filename, slug in fixes.items():
    if not os.path.exists(filename):
        print(f'SKIP (not found): {filename}')
        continue
    with open(filename, encoding='utf-8') as f:
        c = f.read()

    full_url = f'https://{domain}{slug}'

    # Fix canonical href (relative or wrong domain)
    c = re.sub(r'(link rel="canonical" href=")[^"]*(")', rf'\g<1>{full_url}\g<2>', c)
    # Fix og:url content (relative or wrong domain)
    c = re.sub(r'(property="og:url" content=")[^"]*(")', rf'\g<1>{full_url}\g<2>', c)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f'Fixed: {filename} -> {full_url}')

# 404.html: canonical missing — inject before og:url meta tag; also fix og:url
filename = '404.html'
full_404 = f'https://{domain}/404'
with open(filename, encoding='utf-8') as f:
    c = f.read()

# Fix og:url
c = re.sub(r'(property="og:url" content=")[^"]*(")', rf'\g<1>{full_404}\g<2>', c)

# Insert canonical if absent
if 'rel="canonical"' not in c:
    c = c.replace(
        '<meta property="og:url"',
        f'<link rel="canonical" href="{full_404}" data-react-helmet="true"><meta property="og:url"',
        1
    )

with open(filename, 'w', encoding='utf-8') as f:
    f.write(c)
print(f'Fixed: {filename} -> {full_404}')

print('Done.')
