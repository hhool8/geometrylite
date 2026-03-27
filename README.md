# Geometry Dash Lite — geometrylite.poki2.online

Free unblocked H5 game site hosted on GitHub Pages.
Live: **https://geometrylite.poki2.online**

---

## Quick Start

```bash
# Migrate to a new domain (updates all HTML, sitemap, robots.txt, CNAME, scripts)
bash scripts/set-domain.sh your-new-domain.com

# Run full SEO audit (outputs docs/seo-audit-report.md)
python3 scripts/seo_verify.py
```

---

## Site Structure

| Path | Description |
|---|---|
| `index.html` | Homepage — Geometry Dash Lite (main game) |
| `egg-dash.html` … `xmas-dash.html` | 8 game pages with VideoGame JSON-LD schema |
| `about-us.html` … `404.html` | 7 support / legal pages |
| `embed/*.html` | Embeddable iframes for each game |
| `game/*/index.html` | Standalone game viewer pages |
| `hot-games/`, `new-games/`, `top-popular/` | Curated game list pages |
| `resources/css/style.min.css` | Single minified stylesheet (Tailwind + custom) |
| `resources/fonts/` | Self-hosted woff2: Nunito-Regular (32 K) + Orbitron-Bold (9 K) |
| `robots.txt` | Allows all; disallows `/embed/`; points to sitemap |
| `sitemap.xml` | 18 URLs with priorities and dynamic lastmod (git-based) |
| `data/image/game/` | 10 game thumbnails (186×186 PNG) for og:image / twitter:image |
| `data/image/options/og-cover.png` | 1200×630 brand cover image for homepage og:image / Twitter Card |
| `CNAME` | `geometrylite.poki2.online` |
| `.domain` | Active domain used by `set-domain.sh` |

---

## Scripts

| Script | Purpose |
|---|---|
| `scripts/set-domain.sh` | One-command domain migration — replaces domain in all HTML/xml/py files |
| `scripts/add_schema.py` | Inject VideoGame JSON-LD schema into all game pages |
| `scripts/seo_offpage.py` | Add Twitter Card meta tags + fix share modal URLs |
| `scripts/add_cwv_tracking.py` | Inject Core Web Vitals (LCP/CLS/INP) GA4 events |
| `scripts/fix_support_pages.py` | Fix canonical + og:url on support/legal pages |
| `scripts/fix_github_io_links.py` | Replace residual github.io refs (favicon, nav, domain_url) |
| `scripts/fix_og_images.py` | Fix 404.html github.io image refs; update homepage og:image to cover |
| `scripts/gen_og_cover.py` | Generate 1200×630 og-cover.png (Pillow; requires `.venv`) |
| `scripts/gen_sitemap.py` | Regenerate sitemap.xml with lastmod from `git log` per file |
| `scripts/copy_game_thumbs.py` | Copy cache/*-m186x186.png → data/image/game/ |
| `scripts/download_game_images.py` | Attempt download + HTML ref migration for game images |
| `scripts/seo_verify.py` | Full per-page SEO tag audit → `docs/seo-audit-report.md` |
| `scripts/replace_font.py` | Font replacement utility (Dosis → Nunito) |

---

## SEO — Completed Work

| Area | Detail |
|---|---|
| `robots.txt` | Allows all; `Disallow: /embed/`; links to sitemap |
| `sitemap.xml` | 18 URLs, priority weights, dynamic `lastmod` from `git log` per file |
| Canonical / og:url | Absolute `https://geometrylite.poki2.online/…` on all 16 pages |
| VideoGame JSON-LD | All 9 game pages (index + 8 games) |
| H1 / Title / Meta | "Geometry Dash Lite Unblocked" + all P1/P2 keywords |
| FAQ section | 4-question FAQ on homepage targeting unblocked 66/76/g+ |
| Twitter Cards | All 16 pages |
| Core Web Vitals | LCP/CLS/INP as custom GA4 events on all 16 pages |
| Internal links | Contextual cross-links on all 8 game pages |
| Font | Dosis → Nunito (self-hosted woff2, latin subset 32 K) |
| Domain links | All `geometrylite.github.io` refs replaced with `poki2.online` (all pages + 404.html) |
| Game thumbnails | 10 PNG committed to `data/image/game/`; 36 HTML refs migrated to poki2.online |
| OG cover image | 1200×630 `og-cover.png` — homepage og:image / twitter:image |
| GA4 | G-KKVKM3C6FM on all 16 pages |
| GSC | Verification meta tag on all pages |

## SEO — Needs Refinement

| Item | Detail |
|---|---|
| FAQPage + WebSite schema | Homepage has no `FAQPage` or `WebSite` JSON-LD yet — high impact for Rich Results |
| Game page og:image size | Each game page uses 186×186 thumbnails; Twitter/OG recommends 1200×630 (update when high-res assets available) |

## Off-Page — Pending (manual)

| Priority | Task |
|---|---|
| 🔴 High | Submit to CrazyGames, itch.io, Newgrounds, Poki — see `docs/off-page-guide.md` |
| 🔴 High | Reddit posts: r/WebGames, r/geometrydash, r/teenagers |
| 🟡 Medium | Create @geometrylite on Twitter, Facebook, Instagram |
| 🟡 Medium | Link exchange outreach: unblockedgames66.io and similar repos |
| 🟢 Low | YouTube gameplay videos (backlink generation) |

---

## Docs

- [`SEO-PLAN-geometrylite.md`](SEO-PLAN-geometrylite.md) — Full SEO strategy and implementation log
- [`docs/off-page-guide.md`](docs/off-page-guide.md) — Game directory submission list, Reddit/social templates
- [`docs/seo-audit-report.md`](docs/seo-audit-report.md) — Latest audit (regenerate: `python3 scripts/seo_verify.py`)

---

## Monitoring

| Check | Tool | Frequency |
|---|---|---|
| Indexing coverage | `site:geometrylite.poki2.online` in Google | Weekly |
| Keyword rankings | GSC → Performance → Queries | Weekly |
| Core Web Vitals | GSC → Core Web Vitals / GA4 custom events | Monthly |
| PageSpeed | https://pagespeed.web.dev/?url=https://geometrylite.poki2.online | Monthly |
| Schema validity | https://search.google.com/test/rich-results?url=https://geometrylite.poki2.online | After schema changes |

---

## Target Keywords

| Keyword | Priority | Target Rank |
|---|---|---|
| Geometry Dash Lite | P1 | Top 5 |
| unblocked games g+ / g plus | P1 | Top 5 |
| unblocked games 66 / 76 | P2 | Top 10 |
| games unblocked | P2 | Top 10 |
| unblocked games 77 | P3 | Top 20 |

---

## Work Status (as of 2026-03-27)

### ✅ Completed — All Technical Work Done

| Area | Detail |
|---|---|
| Title / H1 / Meta | "Geometry Dash Lite Unblocked" + all P1/P2/P3 keywords |
| VideoGame JSON-LD | All 9 game pages (homepage + 8 game pages) |
| WebSite + FAQPage JSON-LD | Homepage — enables Sitelinks SearchBox + FAQ Rich Result |
| Canonical / og:url | Absolute URLs on all 16 pages |
| Twitter Card | All 16 pages |
| OG cover image | 1200×630 `og-cover.png` for homepage; 186×186 thumbnails on game pages |
| Game thumbnails | 10 PNG files in `data/image/game/`; 36 HTML refs migrated to poki2.online |
| github.io cleanup | All residual refs replaced across all pages incl. 404.html |
| robots.txt / sitemap | 18 URLs; dynamic `lastmod` via `gen_sitemap.py` (git log per file) |
| Font | Nunito self-hosted woff2, latin subset 32 K |
| GA4 + CWV | G-KKVKM3C6FM + LCP/CLS/INP custom events on all 16 pages |
| Domain migration | `.domain` + `set-domain.sh` (full-depth, no hardcoded domain) |
| Documentation | README.md + SEO-PLAN-geometrylite.md both up to date |

### ⚠️ Needs Refinement

| Item | Current State | Suggestion |
|---|---|---|
| Game page og:image size | 186×186 px on 8 game pages | Replace files in `data/image/game/*/` with 1200×630 when high-res art is available — no HTML changes needed |
| Internal cross-linking | Only footer + same-domain nav links | Add 3 "related games" links on each game detail page |

### ❌ Not Started — Manual Off-Page Actions Only

| Priority | Task |
|---|---|
| 🔴 High | Submit to CrazyGames, itch.io, Newgrounds, Poki — see `docs/off-page-guide.md` |
| 🔴 High | Reddit posts: r/WebGames, r/geometrydash, r/teenagers |
| 🟡 Medium | Create @geometrylite on Twitter, Facebook, Instagram |
| 🟡 Medium | Link exchange outreach (unblockedgames66.io and similar) |
| 🟢 Low | YouTube gameplay recordings (backlink source) |

---

## Work Status Update (2026-03-27 — Session 2)

### ✅ Completed Since Last Summary

| Commit | What Was Done |
|---|---|
| `4501507` | **Browser console warnings fixed** — removed unrecognized iframe `allow` features (`focus-without-user-activation *`, `monetization`) and redundant `allowfullscreen="true"` across all 9 game pages |
| `13aeb03` | **Mac trackpad / mouse wheel scroll fix** — added transparent scroll-pass-through overlay to all 9 game player areas; wheel events forwarded to page until user clicks to play, restored on mouse-leave |
| `33a91ed` | **Search box hidden** — temporarily hidden via `display:none !important` in `style.css` (single-line change, trivial to re-enable) |

### ⚠️ Needs Refinement

| Item | Current State | Next Step |
|---|---|---|
| Search box | Hidden (`display:none`) | Implement game search backend or client-side filter, then re-enable |
| Game page og:image size | 186×186 px on 8 game detail pages | Replace `data/image/game/*/` files with 1200×630 versions when high-res art is available — no HTML changes needed |
| Internal cross-linking | Footer + nav links only | Add 3–5 "Related Games" links on each game detail page to improve crawl depth and dwell time |

### ❌ Not Started — Manual Off-Page Actions Only

| Priority | Task |
|---|---|
| 🔴 High | Game directory submissions: CrazyGames, itch.io, Newgrounds, Poki (see `docs/off-page-guide.md`) |
| 🔴 High | Reddit posts: r/WebGames, r/geometrydash, r/teenagers |
| 🟡 Medium | Create @geometrylite social accounts (Twitter/X, Facebook, Instagram) |
| 🟡 Medium | Link exchange outreach (unblockedgames66.io, similar GitHub Pages game sites) |
| 🟢 Low | YouTube gameplay walkthroughs (organic backlink source) |
