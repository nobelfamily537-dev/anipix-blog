#!/usr/bin/env python3
"""Re-encode the Apothecary Diaries images with the credit/watermark areas cropped out,
and drop the heavily-overlaid poster image from the article."""
import os, re
from PIL import Image

SLUG = "apothecary-diaries-season-3-review"
IMG = "assets/img"

# (source, out name, crop-bottom fraction, max width, quality)
JOBS = [
    ("1000020535.jpg", f"{SLUG}-cover.webp", 0.00, 1200, 88),   # clean night art
    ("1000020534.jpg", f"{SLUG}-1.webp",     0.055, 900, 86),   # key visual - credit line off
    ("1000020536.jpg", f"{SLUG}-2.webp",     0.200, 588, 90),   # field art - title off
]

for src, out, frac, maxw, q in JOBS:
    im = Image.open(f"/scratch/input/{src}").convert("RGB")
    if frac:
        im = im.crop((0, 0, im.width, im.height - int(im.height * frac)))
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(os.path.join(IMG, out), "WEBP", quality=q, method=6)
    print(f"{out:44s} {im.width}x{im.height}  {os.path.getsize(os.path.join(IMG,out))//1024} KB")

# ---- remove the poster image (too much overlay/watermark) from the article ----
p = f"articles/{SLUG}.html"
s = open(p, encoding="utf-8").read()
before = s
s = re.sub(r'<figure[^>]*>\s*<img[^>]*' + re.escape(f"{SLUG}-3.webp") + r'[^>]*>.*?</figure>',
           "", s, flags=re.S)
s = s.replace(f"{SLUG}-3.webp", "")          # belt & braces
open(p, "w", encoding="utf-8").write(s)
print("\nposter figure removed:", s != before)

# delete the unused webp
f3 = os.path.join(IMG, f"{SLUG}-3.webp")
if os.path.exists(f3):
    os.remove(f3); print("deleted", f3)

print("\nfigures left:", len(re.findall(r"<figure", s)))
for n in ["cover", "1", "2", "3"]:
    print(f"  {SLUG}-{n}.webp referenced:", f"{SLUG}-{n}.webp" in s)
