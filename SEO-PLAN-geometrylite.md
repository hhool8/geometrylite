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
| Schema/Structured Data | ❌ Missing | No GameApplication or WebPage schema — next priority |

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
| robots.txt | ✅ Done | Created fresh; allows all, disallows /embed/, points to sitemap |
| sitemap.xml | ✅ Done | Expanded 11 → 18 URLs with priorities; lastmod updated 2026-03-27 |
| FAQ / Unblocked Content Section | ✅ Done | Added "WHY PLAY UNBLOCKED GAMES HERE?" H2 + 4-question FAQ with keywords unblocked games 66/76/g+ |
| Domain migration script | ✅ Done | `.domain` file + `scripts/set-domain.sh` for one-command migration |
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
- geometrylite/ (site content, pages, static assets)
- h5games_poki2/, h5games_poki2_geodash/ (shared templates or SEO configs)
- public/ (robots.txt, sitemap.xml)
- scripts/ (SEO automation scripts)

## Verification
- Check indexing with: site:geometrylite.poki2.online
- Track keyword rankings (Ahrefs, SEMrush, Search Console, etc.)
- Review meta tags, structured data, internal links, and content quality
- Monitor backlink quantity and quality
- Test page speed and mobile compatibility

## Decisions
- Focus on unblocked games and Geometry Dash Lite keywords, including long-tail variations
- Prioritize homepage and main game pages for SEO
- Execute on-page and off-page optimizations in parallel, with ongoing monitoring

## Further Considerations
- Multilingual/multi-region SEO? (Recommendation: start with English)
- Content originality vs. aggregation? (Recommendation: prioritize original content, avoid copyright risks)
- Backlink resources or budget? (Recommendation: focus on organic links, consider paid promotion if needed)
