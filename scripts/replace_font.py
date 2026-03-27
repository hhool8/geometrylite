#!/usr/bin/env python3
"""Replace Dosis font with Nunito in style.min.css."""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
css_path = os.path.join(BASE, "resources/css/style.min.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

old_400 = '@font-face{font-family:Dosis;src:url("../fonts/Dosis-Medium.woff2") format("woff2");font-weight:400;font-style:normal;font-display:swap;ascent-override:90%;descent-override:10%;line-gap-override:5%}'
new_400 = '@font-face{font-family:Nunito;src:url("../fonts/Nunito-Regular.woff2") format("woff2");font-weight:400;font-style:normal;font-display:swap}'

old_700 = '@font-face{font-family:Dosis;src:url("../fonts/Dosis-Bold.woff2") format("woff2");font-weight:700;font-style:normal;font-display:swap;ascent-override:90%;descent-override:10%;line-gap-override:5%}'
new_700 = '@font-face{font-family:Nunito;src:url("../fonts/Nunito-Regular.woff2") format("woff2");font-weight:700;font-style:normal;font-display:swap}'

css = css.replace(old_400, new_400)
css = css.replace(old_700, new_700)
css = css.replace('font-family:Dosis', 'font-family:Nunito')

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

nunito_count = len(re.findall(r'font-family:Nunito', css))
dosis_count = len(re.findall(r'Dosis', css))
print(f"Nunito font-family refs: {nunito_count}")
print(f"Remaining Dosis refs:    {dosis_count}")
