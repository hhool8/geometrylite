#!/usr/bin/env python3
"""
Add Core Web Vitals (LCP, CLS, INP) tracking to GA4 on all HTML pages.
Run from repo root: python3 scripts/add_cwv_tracking.py
"""
import os, re

CWV_SCRIPT = """<script>
// Core Web Vitals → GA4 custom events
(function(){
  if(!window.gtag || !('PerformanceObserver' in window)) return;
  // LCP
  try { new PerformanceObserver(function(l){
    var e=l.getEntries().slice(-1)[0];
    if(e) gtag('event','lcp',{value:Math.round(e.startTime),metric_id:'lcp'});
  }).observe({type:'largest-contentful-paint',buffered:true}); } catch(e){}
  // CLS
  try { var _cls=0; new PerformanceObserver(function(l){
    l.getEntries().forEach(function(e){ if(!e.hadRecentInput) _cls+=e.value; });
    gtag('event','cls',{value:Math.round(_cls*1000),metric_id:'cls'});
  }).observe({type:'layout-shift',buffered:true}); } catch(e){}
  // INP / FID
  try { new PerformanceObserver(function(l){
    var e=l.getEntries().slice(-1)[0];
    if(e) gtag('event','inp',{value:Math.round(e.processingStart-e.startTime),metric_id:'inp'});
  }).observe({type:'event',buffered:true,durationThreshold:40}); } catch(e){}
})();
</script>"""

ANCHOR = '</body>'

pages = [f for f in os.listdir('.') if f.endswith('.html')]
for filename in sorted(pages):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'metric_id' in content:
        print(f'SKIP (already has CWV): {filename}')
        continue
    if 'G-KKVKM3C6FM' not in content:
        print(f'SKIP (no GA tag): {filename}')
        continue
    if ANCHOR not in content:
        print(f'SKIP (no </body>): {filename}')
        continue
    content = content.replace(ANCHOR, CWV_SCRIPT + ANCHOR, 1)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated: {filename}')

print('Done.')
