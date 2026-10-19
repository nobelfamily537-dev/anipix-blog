#!/usr/bin/env python3
"""Convert the 4 uploaded Apothecary Diaries images to high-quality WebP and
place them inside the Season 3 post where they fit best."""
import os
from PIL import Image

SLUG = "apothecary-diaries-season-3-review"
IMG = "assets/img"
os.makedirs(IMG, exist_ok=True)

# (source, output name, max width, quality, caption)
JOBS = [
    ("1000020535.jpg", f"{SLUG}-cover.webp", 1200, 88, None),                 # hero (wide)
    ("1000020534.jpg", f"{SLUG}-1.webp",      900, 86, "The Apothecary Diaries Season 3 key visual &mdash; Maomao and Jinshi."),
    ("1000020536.jpg", f"{SLUG}-2.webp",      588, 90, "Maomao and Jinshi &mdash; one of the series' quieter moments."),
    ("1000020537.jpg", f"{SLUG}-3.webp",      495, 90, "The new seasonal poster for The Apothecary Diaries Season 3."),
]

for src, out, maxw, q, cap in JOBS:
    im = Image.open(f"/scratch/input/{src}").convert("RGB")
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(os.path.join(IMG, out), "WEBP", quality=q, method=6)
    print(f"{out:44s} {im.width}x{im.height}  {os.path.getsize(os.path.join(IMG,out))//1024} KB")


def fig(name, cap, extra=""):
    return (f'<figure style="margin:26px 0">'
            f'<img src="../assets/img/{name}" alt="{cap}" loading="lazy" decoding="async" '
            f'style="width:100%;height:auto;border-radius:14px;{extra}">'
            f'<figcaption style="font-size:13.5px;color:#8a8aa3;margin-top:8px;text-align:center">{cap}</figcaption>'
            f'</figure>')


p = f"articles/{SLUG}.html"
s = open(p, encoding="utf-8").read()
orig = s

# 1) field image -> end of the "about" section
a1 = "<h2>What happens in Season 3?</h2>"
if a1 in s and f"{SLUG}-2.webp" not in s:
    s = s.replace(a1, fig(f"{SLUG}-2.webp", JOBS[2][4]) + a1, 1)

# 2) key visual + poster -> inside the Season 3 section
a2 = "<h2>Episode schedule and length</h2>"
if a2 in s and f"{SLUG}-1.webp" not in s:
    block = (fig(f"{SLUG}-1.webp", JOBS[1][4], "max-width:520px;display:block;margin:0 auto")
             + fig(f"{SLUG}-3.webp", JOBS[3][4], "max-width:430px;display:block;margin:0 auto"))
    s = s.replace(a2, block + a2, 1)

open(p, "w", encoding="utf-8").write(s)
print("\nimages inserted:", s != orig)
for n in ["cover", "1", "2", "3"]:
    print(f"  {SLUG}-{n}.webp  -> {'yes' if f'{SLUG}-{n}.webp' in s else 'no'}")
