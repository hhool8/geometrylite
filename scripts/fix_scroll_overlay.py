"""
Add scroll-pass-through overlay to game pages.
Fixes: mouse wheel / Mac trackpad scroll having no effect in game player area.

How it works:
- A transparent div sits above the iframe (z-index:2)
- Wheel events on it are forwarded to window.scrollBy() so the page scrolls normally
- When user clicks to play, the overlay steps aside (pointer-events:none, z-index:-1)
- When mouse leaves the game area, the overlay is restored so page scrolling works again
"""
import glob

OVERLAY_JS = """
 // Scroll-pass-through overlay: forward wheel to page until user clicks to play
 var $overlay = $('<div id="game-scroll-overlay" style="position:absolute;inset:0;z-index:2;cursor:pointer;"></div>');
 var $gameWrap = $("#frame-container").parent();
 $gameWrap.append($overlay);
 $overlay[0].addEventListener("wheel", function(e) {
   window.scrollBy({top: e.deltaY, behavior: "auto"});
 }, {passive: true});
 $overlay.on("click", function() {
   $(this).css({"pointer-events": "none", "z-index": "-1"});
   document.getElementById("game-area").focus();
 });
 $gameWrap.on("mouseleave", function() {
   $overlay.css({"pointer-events": "auto", "z-index": "2"});
 });
"""

files = glob.glob("*.html")
patched = 0
for f in files:
    txt = open(f, encoding="utf-8").read()
    if "frame-container" not in txt:
        continue
    if "game-scroll-overlay" in txt:
        print(f"  Already patched: {f}")
        continue
    old = ' $("#frame-container").html(game_frame);\n })'
    new = ' $("#frame-container").html(game_frame);' + OVERLAY_JS + ' })'
    if old not in txt:
        print(f"  Pattern not found: {f}")
        continue
    txt = txt.replace(old, new)
    open(f, "w", encoding="utf-8").write(txt)
    print(f"Patched: {f}")
    patched += 1

print(f"\nTotal patched: {patched}")
