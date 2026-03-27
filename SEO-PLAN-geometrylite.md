# SEO Plan for geometrylite.poki2.online

## Objective
Boost the Google ranking of the subdomain geometrylite.poki2.online for the following keywords:
- unblocked games g+
- unblocked games g plus
- unblocked games 66
- unblocked games 76
- unblocked games 77
- Geometry Dash Lite
- games unblocked

## 1. Current Status Analysis & Goal Setting

### ✅ Analysis Completed (2026-03-27)

| Area | Status | Finding |
|---|---|---|
| robots.txt | ✅ Fixed | Created at root — allows all, blocks /embed/, points to sitemap |
| sitemap.xml | ✅ Fixed | Expanded from 11 → 18 URLs, added all game pages with priority weights |
| canonical URL | ✅ Fixed | All game pages updated from relative to absolute (geometrylite.poki2.online) |
| og:url | ✅ Fixed | index.html and all game pages now use absolute domain URLs |
| Target keywords | ✅ Fixed | Added unblocked games g+, 66, 76, 77, g plus to index.html meta keywords |
| Google Analytics | ✅ Active | G-KKVKM3C6FM deployed on all pages |
| GSC Verification | ✅ Active | meta google-site-verification present on all pages |
| about-us domain | ✅ Fixed | Replaced geometrylite.github.io → geometrylite.poki2.online |
| Schema/Structured Data | ✅ Fixed | VideoGame JSON-LD on all 9 game pages; WebSite + FAQPage schema on homepage |
| Font | ✅ Fixed | Replaced Dosis with Nunito (self-hosted woff2, latin subset 32 K) |
| github.io links | ✅ Fixed | All `geometrylite.github.io` refs replaced with `poki2.online` across all pages incl. 404.html |
| Game thumbnails | ✅ Fixed | 10 PNG images committed to `data/image/game/`; 36 og:image/twitter:image HTML refs migrated |
| OG cover image | ✅ Fixed | 1200×630 `data/image/options/og-cover.png` generated; homepage og:image/twitter:image updated |
| Sitemap lastmod | ✅ Fixed | Dynamic generation via `gen_sitemap.py` — reads `git log` per file |

### ✅ Keyword Priority & Target Rankings (2026-03-27)

| Keyword | Est. Monthly Searches | Competition | Priority | Target Rank |
|---|---|---|---|---|
| Geometry Dash Lite | 100K+ | Medium | P1 — Primary | Top 5 |
| unblocked games g+ | 10K–50K | Medium-Low | P1 — Primary | Top 5 |
| unblocked games g plus | 10K–50K | Medium-Low | P1 — Primary | Top 5 |
| unblocked games 66 | 100K+ | High | P2 — Secondary | Top 10 |
| games unblocked | 50K+ | High | P2 — Secondary | Top 10 |
| unblocked games 76 | 10K–50K | Medium | P2 — Secondary | Top 10 |
| unblocked games 77 | 10K–50K | Medium | P3 — Long-tail | Top 20 |

**Rationale:** "Geometry Dash Lite" and "unblocked games g+" have medium competition and a natural brand fit — highest ROI. "unblocked games 66/76/77" are high-volume but dominated by branded competitors; target via long-tail variations.

### ✅ Competitor Research (2026-03-27)

**unblockedgames66.io** (ranks for unblocked games 66):
- H1: "Online Games at Unblocked Games 66" — keyword in H1
- H2s explain site value: "Why Choose…", "How to Access…"
- Hundreds of games; publishes new games weekly
- Social links: Facebook, Twitter, Instagram, Pinterest
- Clean URL structure: `/game/{slug}`
- No schema markup detected

**geometrylite.github.io** (our upstream):
- H1: "Geometry Dash Lite" — missing "unblocked"
- Good H2/H3 content hierarchy (rhythm, gameplay, controls)
- No GameApplication/VideoGame schema
- No social links
- Footer links still point to old github.io domain (fixed ✅)

**Key Gaps vs Competitors:**
- Our H1/title/description missing "unblocked" keyword signal
- No structured data (schema.org GameApplication) — competitors also lack it, so this is a differentiator opportunity
- No social signals / share buttons beyond basic share modal

**Implemented Improvements:**
- Updated index.html title tag to include "Unblocked"
- Added VideoGame structured data (JSON-LD) to index.html
- Added "unblocked games" to meta description on index.html

## 2. On-Page Optimization ✅ COMPLETED

| Task | Status | Details |
|---|---|---|
| Keyword Placement (title / meta desc / keywords) | ✅ Done | title="Geometry Dash Lite Unblocked - Play Free Online Games Unblocked"; meta description & keywords include all P1/P2 terms |
| H1 Keyword | ✅ Done | H1 = "Geometry Dash Lite Unblocked" |
| Canonical / og:url | ✅ Done | All 8 game pages + homepage fixed to absolute `https://geometrylite.poki2.online/...` URLs |
| Schema / Structured Data (VideoGame JSON-LD) | ✅ Done | Added to index.html + all 8 game pages (egg-dash, wave-dash, geometry-lite-classic, geometry-jump, geometry-game-3d, spooky-dash, tap-road-beat, xmas-dash) |
| WebSite + FAQPage JSON-LD | ✅ Done | Injected into homepage — enables Sitelinks SearchBox + FAQ Rich Result |
| robots.txt | ✅ Done | Created fresh; allows all, disallows /embed/, points to sitemap |
| sitemap.xml | ✅ Done | 18 URLs; dynamic `lastmod` via `scripts/gen_sitemap.py` (`git log` per file) |
| FAQ / Unblocked Content Section | ✅ Done | Added "WHY PLAY UNBLOCKED GAMES HERE?" H2 + 4-question FAQ with keywords unblocked games 66/76/g+ |
| Domain migration script | ✅ Done | `.domain` file + `scripts/set-domain.sh` (full-depth, includes embed/, game/, scripts/*.py) |
| Font | ✅ Done | Replaced Dosis with Nunito self-hosted woff2, latin subset 32 K |
| github.io cleanup | ✅ Done | All residual `geometrylite.github.io` refs replaced across all HTML pages |
| Game thumbnails | ✅ Done | 10 PNG images in `data/image/game/`; 36 og:image/twitter:image refs updated |
| OG cover image | ✅ Done | 1200×630 `og-cover.png`; homepage og:image/twitter:image upgraded from 186×186 |
| Internal Linking | ⚠️ Partial | Footer + same-domain game links exist; deeper cross-linking TBD |

## 3. Off-Page Optimization ✅ TECHNICAL SETUP COMPLETE — ACTIONS PENDING

| Task | Status | Details |
|---|---|---|
| Twitter Card meta tags | ✅ Done | Added `twitter:card/title/description/image/site` to all 16 HTML pages via `scripts/seo_offpage.py` |
| Share modal URL fix | ✅ Done | Fixed hardcoded `github.io` URL → correct per-page URL on all 16 pages |
| Off-page action guide | ✅ Done | Full guide at `docs/off-page-guide.md` — directories, forums, social media, outreach templates |
| Game directory submissions | ❌ Manual action | Submit to CrazyGames, itch.io, Newgrounds, Poki — see `docs/off-page-guide.md` |
| Reddit posts | ❌ Manual action | Post in r/WebGames, r/geometrydash, r/teenagers |
| Social accounts | ❌ Manual action | Create @geometrylite on Twitter, Facebook, Instagram |
| Link exchange outreach | ❌ Manual action | Contact unblockedgames66.io, GitHub Pages repos |
| YouTube gameplay videos | ❌ Manual action | Upload walkthroughs — embeds create backlinks |

> Full actionable checklist: see [`docs/off-page-guide.md`](docs/off-page-guide.md)

## 4. Monitoring & Adjustment ✅ TECHNICAL SETUP COMPLETE

| Task | Status | Details |
|---|---|---|
| Google Analytics (GA4) | ✅ Active | G-KKVKM3C6FM on all 16 HTML pages |
| Google Search Console | ✅ Active | GSC verification meta tag on all pages; sitemap submitted |
| Core Web Vitals (GA4 events) | ✅ Done | LCP, CLS, INP reported as custom GA4 events via `scripts/add_cwv_tracking.py` |
| Ranking monitoring | ⚠️ Manual | Use GSC Performance tab weekly; check target keywords P1/P2/P3 |
| Backlink monitoring | ⚠️ Manual | Use Google Search Console → Links or Ahrefs free tools |
| Monthly review | ⚠️ Manual | Monthly: update content, fix broken links, refresh lastmod in sitemap |

**Key monitoring commands:**
```bash
# Check indexing status
site:geometrylite.poki2.online

# Verify new robots.txt / sitemap
curl https://geometrylite.poki2.online/robots.txt
curl https://geometrylite.poki2.online/sitemap.xml

# GSC index request
# → Google Search Console → URL Inspection → Request Indexing
```

## Relevant Files

### Site Pages (geometrylite/)
- `index.html` — Homepage + main game; fully SEO-optimised
- `egg-dash.html`, `wave-dash.html`, `geometry-lite-classic.html`, `geometry-jump.html`, `geometry-game-3d.html`, `spooky-dash.html`, `tap-road-beat.html`, `xmas-dash.html` — Game pages with VideoGame schema
- `about-us.html`, `contact-us.html`, `dmca.html`, `privacy-policy.html`, `terms-of-service.html`, `404.html`, `favorite.html` — Support pages
- `robots.txt` — Crawl directives; blocks /embed/, points to sitemap
- `sitemap.xml` — 18 URLs with priorities and dynamic lastmod (git-based via `gen_sitemap.py`)
- `data/image/game/` — 10 game thumbnails (186×186 PNG) for per-game og:image
- `data/image/options/og-cover.png` — 1200×630 brand cover for homepage og:image / Twitter Card
- `CNAME` — `geometrylite.poki2.online`
- `.domain` — Domain config for migration script

### Scripts (scripts/)
| Script | Purpose |
|---|---|
| `set-domain.sh` | One-command domain migration — full depth, includes embed/, game/, scripts/*.py |
| `add_schema.py` | Inject VideoGame JSON-LD schema into all game pages |
| `add_homepage_schema.py` | Inject WebSite + FAQPage JSON-LD into homepage |
| `seo_offpage.py` | Add Twitter Card meta tags + fix share modal URLs across all pages |
| `add_cwv_tracking.py` | Inject Core Web Vitals (LCP/CLS/INP) GA4 event tracking into all pages |
| `fix_support_pages.py` | Fix canonical + og:url on support/legal pages |
| `fix_github_io_links.py` | Replace residual github.io refs (favicon, nav, domain_url) |
| `fix_og_images.py` | Fix 404.html github.io image refs; update homepage og:image to cover |
| `gen_og_cover.py` | Generate 1200×630 og-cover.png (Pillow; use `.venv`) |
| `gen_sitemap.py` | Regenerate sitemap.xml with lastmod from `git log` per file |
| `copy_game_thumbs.py` | Copy cache/*-m186x186.png → data/image/game/ |
| `seo_verify.py` | Full SEO audit — outputs per-page tag status table to `docs/seo-audit-report.md` |

### Docs (docs/)
- `off-page-guide.md` — Game directory submission list, Reddit/social targets, outreach templates
- `seo-audit-report.md` — Latest generated SEO audit report (re-run: `python3 scripts/seo_verify.py`)

## Verification ✅ AUTOMATED + MANUAL CHECKLIST

### Automated (run locally)
```bash
# Full per-page SEO tag audit — saves report to docs/seo-audit-report.md
python3 scripts/seo_verify.py

# Verify robots.txt and sitemap are live
curl https://geometrylite.poki2.online/robots.txt
curl https://geometrylite.poki2.online/sitemap.xml
```

### Manual (browser / external tools)

| Check | Tool / URL | Frequency |
|---|---|---|
| Google indexing coverage | [`site:geometrylite.poki2.online`](https://www.google.com/search?q=site:geometrylite.poki2.online) in Google | Weekly |
| Keyword rankings (P1/P2/P3) | GSC → Performance → Queries | Weekly |
| Request indexing for new/changed pages | GSC → URL Inspection → Request Indexing | On each deploy |
| Submit / re-verify sitemap | GSC → Sitemaps → `https://geometrylite.poki2.online/sitemap.xml` | On sitemap change |
| Rich Results / Schema validity | [Rich Results Test](https://search.google.com/test/rich-results?url=https%3A%2F%2Fgeometrylite.poki2.online) | After schema changes |
| PageSpeed / Core Web Vitals (lab) | [PageSpeed Insights](https://pagespeed.web.dev/?url=https%3A%2F%2Fgeometrylite.poki2.online) | Monthly |
| Core Web Vitals (field data) | GSC → Core Web Vitals report | Monthly |
| Mobile-Friendly | [Mobile-Friendly Test](https://search.google.com/test/mobile-friendly?url=https%3A%2F%2Fgeometrylite.poki2.online) | On layout changes |
| Backlink count & quality | GSC → Links → External links | Monthly |
| Twitter Card preview | [Twitter Card Validator](https://cards-dev.twitter.com/validator) | After og: tag changes |

## Decisions ✅ IMPLEMENTED

| Decision | Rationale | Status |
|---|---|---|
| Focus on "Geometry Dash Lite" + "unblocked games g+" as P1 keywords | Medium competition, natural brand fit — highest ROI vs high-DA competitors owning "unblocked games 66" | ✅ Implemented in title, H1, meta desc, keywords |
| Use "unblocked games 66/76" as P2 via long-tail / FAQ content, not direct competition | These SERPs are dominated by branded sites with 100K+ backlinks; better to capture adjacent traffic | ✅ Implemented via FAQ section in index.html |
| VideoGame JSON-LD schema on all game pages | No competitor has it — differentiator for Rich Results eligibility | ✅ Implemented on 9 pages |
| WebSite + FAQPage JSON-LD on homepage | Enables Sitelinks SearchBox + FAQ Rich Result in SERP | ✅ Implemented |
| 1200×630 og-cover.png for homepage | Twitter/OG spec; game thumbnails are 186×186 — homepage card needed full-size cover | ✅ Implemented |
| Dynamic sitemap lastmod via `git log` | `lastmod` reflects actual last-commit date per file — more accurate signals to Googlebot | ✅ Implemented |
| Domain config via `.domain` + `set-domain.sh` — no hardcoded domain in source | Enables zero-friction migration if subdomain changes | ✅ Implemented |
| Absolute canonical + og:url on every page | Prevents Google treating relative-path pages as duplicate content | ✅ Implemented on all 16 pages |
| Twitter Card meta on all pages | Enables rich previews when any page is shared on Twitter/X, Reddit, Slack | ✅ Implemented on all 16 pages |
| CWV (LCP/CLS/INP) reported to GA4 as custom events | Field data feeds into Google ranking signals; baseline measurement before off-page work begins | ✅ Implemented on all 16 pages |
| English-only content (no i18n) | Audience is English-speaking school/office users; avoid thin multilingual content penalties | ✅ Decision confirmed |
| Original game descriptions — no copy from upstream geometrylite.github.io | Avoid duplicate content penalty from identical upstream text | ✅ All descriptions are original |
| Off-page: organic-first (directories, Reddit, YouTube) before paid promotion | Budget unknown; organic links have lasting value; revisit paid if organic growth stalls after 3 months | ❌ Pending manual actions |

## Further Considerations
- Multilingual/multi-region SEO? (Recommendation: start with English)
- Content originality vs. aggregation? (Recommendation: prioritize original content, avoid copyright risks)
- Backlink resources or budget? (Recommendation: focus on organic links, consider paid promotion if needed)
