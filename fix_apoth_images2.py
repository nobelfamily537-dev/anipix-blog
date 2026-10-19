#!/usr/bin/env python3
"""Keep all 4 photos; crop only the watermark/credit/text areas. Re-add the poster."""
import os, re
from PIL import Image

SLUG = "apothecary-diaries-season-3-review"
IMG = "assets/img"

# (src, out, crop_top, crop_bottom, max_w, quality, caption)
JOBS = [
    ("1000020535.jpg", f"{SLUG}-cover.webp", 0.00, 0.00, 1200, 88,
     None),
    ("1000020534.jpg", f"{SLUG}-1.webp", 0.00, 0.055, 900, 86,
     "The Apothecary Diaries Season 3 key visual."),
    ("1000020536.jpg", f"{SLUG}-2.webp", 0.00, 0.200, 588, 90,
     "Maomao and Jinshi &mdash; one of the series' quieter moments."),
    ("1000020537.jpg", f"{SLUG}-3.webp", 0.115, 0.320, 495, 90,
     "The new seasonal poster for The Apothecary Diaries Season 3."),
]

for src, out, ct, cb, maxw, q, cap in JOBS:
    im = Image.open(f"/scratch/input/{src}").convert("RGB")
    t = int(im.height * ct); b = int(im.height * cb)
    if t or b:
        im = im.crop((0, t, im.width, im.height - b))
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(os.path.join(IMG, out), "WEBP", quality=q, method=6)
    print(f"{out:44s} {im.width}x{im.height}  {os.path.getsize(os.path.join(IMG,out))//1024} KB")

# ---- re-add the poster figure to the article ----
p = f"articles/{SLUG}.html"
s = open(p, encoding="utf-8").read()

if f"{SLUG}-3.webp" not in s:
    cap = JOBS[3][6]
    figure = (f'<figure style="margin:26px 0">'
              f'<img src="../assets/img/{SLUG}-3.webp" alt="{cap}" loading="lazy" decoding="async" '
              f'style="width:100%;height:auto;border-radius:14px;max-width:430px;display:block;margin:0 auto">'
              f'<figcaption style="font-size:13.5px;color:#8a8aa3;margin-top:8px;text-align:center">{cap}</figcaption>'
              f'</figure>')
    anchor = "<h2>Episode schedule and length</h2>"
    if anchor in s:
        s = s.replace(anchor, figure + anchor, 1)
        open(p, "w", encoding="utf-8").write(s)
        print("\nposter figure re-added")
    else:
        print("\nanchor not found!")
else:
    print("\nposter already present")

print("figures in article:", len(re.findall(r"<figure", s)))
for n in ["cover", "1", "2", "3"]:
    print(f"  {SLUG}-{n}.webp referenced:", f"{SLUG}-{n}.webp" in s)
