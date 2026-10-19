#!/usr/bin/env python3
"""Remove the uploaded Apothecary Diaries photos from the post; restore a clean cover."""
import os, re
from PIL import Image, ImageDraw, ImageFont

SLUG = "apothecary-diaries-season-3-review"
IMG = "assets/img"

# ---- 1) strip the in-article figures that use these photos ----
p = f"articles/{SLUG}.html"
s = open(p, encoding="utf-8").read()
before = s
s = re.sub(r'<figure[^>]*>(?:(?!</figure>).)*?' + re.escape(f"{SLUG}-") + r'(?:1|2|3)\.webp(?:(?!</figure>).)*?</figure>',
           "", s, flags=re.S)
open(p, "w", encoding="utf-8").write(s)
print("figures removed:", before.count("<figure") - s.count("<figure"), "| left:", s.count("<figure"))

# ---- 2) delete the photo files ----
for n in ["1", "2", "3"]:
    f = os.path.join(IMG, f"{SLUG}-{n}.webp")
    if os.path.exists(f):
        os.remove(f); print("deleted", f)

# ---- 3) restore the plain generated cover (hero + card keep working) ----
W, H = 1200, 675
img = Image.new("RGB", (W, H), (16, 14, 26))
d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(22 + 40 * t), int(16 + 26 * t), int(38 + 60 * t)))
for i in range(340):
    a = int(46 * (1 - i / 340))
    d.ellipse([W - 380 - i, -120 - i, W - 40 + i, 220 + i], outline=(a + 12, a + 8, a + 30))
d.rectangle([0, H - 5, W, H], fill=(196, 84, 84))

def font(sz):
    for q in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(q):
            try:
                return ImageFont.truetype(q, sz)
            except Exception:
                pass
    return ImageFont.load_default()

d.text((70, 96), "ANIPIX BLOG", font=font(26), fill=(150, 150, 175))
y = 210
for ln in ["The Apothecary", "Diaries Season 3"]:
    d.text((70, y), ln, font=font(76), fill=(255, 255, 255)); y += 92
d.text((70, y + 26), "Review, release schedule and where to watch", font=font(30), fill=(198, 198, 215))
img.save(os.path.join(IMG, f"{SLUG}-cover.webp"), "WEBP", quality=86, method=6)
print("cover regenerated:", os.path.getsize(os.path.join(IMG, f"{SLUG}-cover.webp")) // 1024, "KB")
