#!/usr/bin/env python3
"""Convert the new Apothecary Diaries images to high-quality WebP and place them in the post."""
import os, re
from PIL import Image

SLUG = "apothecary-diaries-season-3-review"
IMG = "assets/img"

# (src, out, crop_top, crop_bottom, max_w, quality, caption)
JOBS = [
    ("1000020535-2.jpg", f"{SLUG}-cover.webp", 0.00, 0.00, 1200, 88, None),
    ("1000020551.png",   f"{SLUG}-1.webp",     0.00, 0.00,  900, 86,
     "The Apothecary Diaries Season 3 key visual."),
    ("1000020536-2.jpg", f"{SLUG}-2.webp",     0.00, 0.20,  588, 90,
     "Maomao and Jinshi &mdash; one of the series' quieter moments."),
    ("1000020554.png",   f"{SLUG}-3.webp",     0.11, 0.33,  700, 88,
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


def fig(name, cap, extra=""):
    return (f'<figure style="margin:26px 0">'
            f'<img src="../assets/img/{name}" alt="{cap}" loading="lazy" decoding="async" '
            f'style="width:100%;height:auto;border-radius:14px;{extra}">'
            f'<figcaption style="font-size:13.5px;color:#8a8aa3;margin-top:8px;text-align:center">{cap}</figcaption>'
            f'</figure>')


p = f"articles/{SLUG}.html"
s = open(p, encoding="utf-8").read()

if f"{SLUG}-2.webp" not in s:
    a1 = "<h2>What happens in Season 3?</h2>"
    s = s.replace(a1, fig(f"{SLUG}-2.webp", JOBS[2][6]) + a1, 1)

if f"{SLUG}-1.webp" not in s:
    a2 = "<h2>Episode schedule and length</h2>"
    block = (fig(f"{SLUG}-1.webp", JOBS[1][6], "max-width:520px;display:block;margin:0 auto")
             + fig(f"{SLUG}-3.webp", JOBS[3][6], "max-width:560px;display:block;margin:0 auto"))
    s = s.replace(a2, block + a2, 1)

open(p, "w", encoding="utf-8").write(s)
print("\nfigures in article:", len(re.findall(r"<figure", s)))
for n in ["cover", "1", "2", "3"]:
    print(f"  {SLUG}-{n}.webp:", f"{SLUG}-{n}.webp" in s)
