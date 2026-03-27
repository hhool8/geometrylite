#!/usr/bin/env python3
"""
add_homepage_schema.py — Inject FAQPage + WebSite JSON-LD into index.html
Inserts two <script type="application/ld+json"> blocks immediately after the
existing VideoGame schema block.
"""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(BASE, "index.html")
DOMAIN = "https://geometrylite.poki2.online"

WEBSITE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Geometry Lite",
    "url": DOMAIN,
    "description": "Free unblocked Geometry Dash games — play Geometry Dash Lite, Geometry Jump, Wave Dash and more. No download, works on school Chromebook.",
    "potentialAction": {
        "@type": "SearchAction",
        "target": {
            "@type": "EntryPoint",
            "urlTemplate": DOMAIN + "/search?q={search_term_string}"
        },
        "query-input": "required name=search_term_string"
    }
}

FAQPAGE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "What is Geometry Dash Lite Unblocked?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Geometry Dash Lite Unblocked is the free browser version of the popular rhythm platformer Geometry Dash. It runs entirely in your browser with no download or installation required, and is accessible on school networks and Chromebook."
            }
        },
        {
            "@type": "Question",
            "name": "Is Geometry Lite safe for school?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Geometry Lite is a safe, ad-minimal browser game site designed for students. All games run in-browser with no plugins, and the site contains no malware or inappropriate content."
            }
        },
        {
            "@type": "Question",
            "name": "How is Geometry Lite different from Unblocked Games 66 or 76?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Geometry Lite focuses exclusively on Geometry Dash variants with a clean, fast interface and structured schema markup. Unlike unblocked games 66 or 76, there are no heavy ads and every game page is fully optimized for Chromebook and school Wi-Fi."
            }
        },
        {
            "@type": "Question",
            "name": "Can I play Geometry Dash Lite on a Chromebook?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Every game on Geometry Lite runs in Chrome and Chrome OS without any extensions or admin permissions. Just open the site and click Play."
            }
        },
        {
            "@type": "Question",
            "name": "Do I need a VPN to play Geometry Lite at school?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "No VPN is required. Geometry Lite is hosted to remain accessible on most school and office networks. Simply visit geometrylite.poki2.online in your browser."
            }
        }
    ]
}

# Injection anchor: right after the closing </script> of the VideoGame schema
ANCHOR = '"publisher":{"@type":"Organization","name":"Geometry Lite","url":"' + DOMAIN + '"}}</script>'

INJECT = (
    ANCHOR
    + '<script type="application/ld+json">' + json.dumps(WEBSITE_SCHEMA, separators=(',', ':')) + '</script>'
    + '<script type="application/ld+json">' + json.dumps(FAQPAGE_SCHEMA, separators=(',', ':')) + '</script>'
)

with open(INDEX) as f:
    content = f.read()

if '"@type":"WebSite"' in content:
    print("WebSite schema already present — nothing to do.")
else:
    count = content.count(ANCHOR)
    if count != 1:
        print(f"ERROR: anchor found {count} times (expected 1). Aborting.")
        exit(1)
    new_content = content.replace(ANCHOR, INJECT)
    with open(INDEX, "w") as f:
        f.write(new_content)
    print("Injected WebSite + FAQPage schema into index.html")
    # verify
    ws = new_content.count('"@type":"WebSite"')
    faq = new_content.count('"@type":"FAQPage"')
    print(f"  WebSite blocks: {ws}  |  FAQPage blocks: {faq}")
