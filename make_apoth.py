#!/usr/bin/env python3
"""Generate 'The Apothecary Diaries Season 3' post on the AniPix blog."""
import os, re
from PIL import Image, ImageDraw, ImageFont

SLUG = "apothecary-diaries-season-3-review"
TITLE = "The Apothecary Diaries Season 3: Review, Release Schedule and Where to Watch (2026)"
DESC = ("The Apothecary Diaries Season 3 is the most-watched anime of Fall 2026. What the new season "
        "covers, its episode schedule, scores from MAL and AniList, and whether it is worth watching.")
DATE = "19 October 2026"
READ = "9 min read"
CAT = "Anime"

os.makedirs("assets/img", exist_ok=True)
COVER = f"assets/img/{SLUG}-cover.webp"

# ---------------------------------------------------------------- cover image
W, H = 1200, 675
img = Image.new("RGB", (W, H), (16, 14, 26))
d = ImageDraw.Draw(img)
for y in range(H):                                   # vertical gradient
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(22 + 40 * t), int(16 + 26 * t), int(38 + 60 * t)))
for i in range(340):                                 # soft glow
    a = int(46 * (1 - i / 340))
    d.ellipse([W - 380 - i, -120 - i, W - 40 + i, 220 + i], outline=(a + 12, a + 8, a + 30))
d.rectangle([0, H - 5, W, H], fill=(196, 84, 84))

def font(sz, bold=True):
    for p in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, sz)
            except Exception:
                pass
    return ImageFont.load_default()

d.text((70, 96), "ANIPIX BLOG", font=font(26), fill=(150, 150, 175))
lines = ["The Apothecary", "Diaries Season 3"]
y = 210
for ln in lines:
    d.text((70, y), ln, font=font(76), fill=(255, 255, 255))
    y += 92
d.text((70, y + 26), "Review, release schedule and where to watch", font=font(30, False), fill=(198, 198, 215))
img.save(COVER, "WEBP", quality=86, method=5)
print("cover:", COVER, os.path.getsize(COVER) // 1024, "KB")

# ---------------------------------------------------------------- article html
tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()

head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html",
                    f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", f"{SLUG}-cover.webp")

shell_start = tpl.find('<header class="site">')
shell_end = tpl.find('<article class="post">')
shell_head = tpl[shell_start:shell_end]
tail = re.sub(r'</article><div class="related">.*?</div>', '', tpl[tpl.find("</article>"):], count=1, flags=re.S)
shell_head = shell_head.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')

BODY = f"""<article class="post"><h1>The Apothecary Diaries Season 3: Review, Release Schedule and Where to Watch</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="sharebar"><span class="sharelabel">Share</span><button class="sbtn" type="button" onclick="sharePost()">Share this article</button><button class="sbtn" type="button" onclick="copyLink()">Copy link</button></div>
<div class="posthero"><img src="../assets/img/{SLUG}-cover.webp" alt="The Apothecary Diaries Season 3" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>The Apothecary Diaries is back, and it has walked straight back to the top. Season 3 premiered on 2 October 2026 and immediately took the number one spot on the Fall 2026 anime trending charts, ahead of Black Clover Season 2 and the JoJo Steel Ball Run adaptation. For a show that is mostly about a pharmacist noticing that something is slightly wrong with a breakfast, that is a remarkable thing to pull off.</p>

<p>This guide covers what the new season is about, how many episodes there are, where you can watch it, what the scores look like, and whether you should start here or go back to the beginning.</p>

<h2>What is The Apothecary Diaries about?</h2>

<p>Maomao is a young woman trained as an apothecary, raised in the pleasure district by her father. She is sharp, unsentimental, obsessed with poisons and medicines, and completely uninterested in court politics &mdash; which is unfortunate, because she is very good at noticing things the court would rather keep quiet.</p>

<p>The series follows her as she is pulled into the inner palace, then into the world around it, solving medical mysteries that keep turning out to be political ones. It is a mystery show wearing the clothes of a historical drama, and its real subject is the gap between what people say and what is actually happening.</p>

<h2>What happens in Season 3?</h2>

<p>Season 3 picks up after the Shi Clan rebellion. Things have finally settled, and Maomao has returned to her old life as a pharmacist in the pleasure district. But two threads immediately pull her back in.</p>

<p>The first is Jinshi, who has now revealed his true identity as the Emperor's brother and has begun to carry the weight of that role. He is troubled by the final message left by Loulan &mdash; a warning about a coming disaster that will strike the whole nation.</p>

<p>The second is stranger: rumours of a mysterious shrine maiden who is deceiving the people. As those rumours spread, the country of Li comes under a shadow again, and the story widens out from the inner court to the city streets and across foreign borders.</p>

<p>If Season 2 was about the palace, Season 3 looks set to be about the country. The stakes are noticeably bigger, and the world is noticeably larger.</p>

<h2>Episode schedule and length</h2>

<p>The season is listed at 12 episodes, roughly 24 minutes each, running weekly from 2 October 2026. That is the same shape as previous seasons, and the show has been consistent about using that time well &mdash; usually one main mystery with two or three smaller ones threaded through it.</p>

<p>Broadcast dates and episode counts do shift, so check the streaming page for the exact schedule in your region.</p>

<h2>Where to watch</h2>

<p>Outside Japan, The Apothecary Diaries streams on Crunchyroll, with new episodes going up shortly after the Japanese broadcast. In Japan it airs on Nippon TV and related channels. It is a light novel adaptation produced by Studio OLM.</p>

<h2>Scores and reception</h2>

<p>Scores move around during a season, so treat these as a snapshot rather than a verdict. As of mid-October 2026:</p>

<ul>
<li><strong>MyAnimeList:</strong> around 8.66, from roughly 206,000 members</li>
<li><strong>AniList:</strong> around 85/100</li>
<li><strong>Anime Trending:</strong> number 1 on the Fall 2026 Week 1 chart</li>
</ul>

<p>For comparison, the first two seasons sit at similar levels, which is unusual &mdash; most long-running shows drift downward as they go. The Apothecary Diaries has held its quality, and the new season has not damaged that record so far.</p>

<h2>Should you start with Season 3?</h2>

<p>No. This is a show where the mysteries build on each other and the character relationships carry most of the emotional weight. Starting at Season 3 means missing why Maomao is the way she is, why Jinshi's secret matters, and why the pleasure district scenes land the way they do.</p>

<p>Watch it in order:</p>

<ul>
<li><strong>Season 1</strong> &mdash; the inner palace arc, and the reason everyone fell for this show</li>
<li><strong>Season 2</strong> &mdash; the Shi Clan story, which sets up everything Season 3 is reacting to</li>
<li><strong>Season 3</strong> &mdash; the national arc, currently airing</li>
</ul>

<p>If you have already seen the first two, you can jump straight in. If you have not, Season 1 is a self-contained and genuinely excellent place to begin.</p>

<h2>Why it works</h2>

<p>Most mystery anime solve their cases with a clever deduction delivered in a dramatic pose. The Apothecary Diaries solves them with knowledge &mdash; actual, specific, sometimes deeply unpleasant medical knowledge &mdash; and then shows you the political consequences of having that knowledge in a court that does not want it known.</p>

<p>Maomao is the reason it holds together. She is not a chosen one, she has no special power, and she would genuinely rather be left alone with her herbs. She investigates because she cannot stop noticing. That is a much more interesting engine than destiny, and it is why the show has kept its audience for three seasons.</p>

<h2>Verdict</h2>

<p>Season 3 is the strongest-looking start of the three, and the number one trending spot is deserved. If you like slow-burn mystery, historical detail, and a protagonist who is quietly smarter than everyone in the room, this is one of the best things airing right now.</p>

<p>If you have been putting it off, there is no better moment to catch up &mdash; the first two seasons are complete, and the new one is running weekly.</p>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Anime: The Complete Watch List and Release Dates</a></li><li><a href="../articles/reincarnated-aristocrat-appraisal-skill-season-3-review.html">As a Reincarnated Aristocrat, I'll Use My Appraisal Skill Season 3 Review</a></li><li><a href="../articles/genshin-impact-7-1-banners.html">Genshin Impact 7.1 Banners: Vesna, Vodyanitsa and the Skirk Rerun</a></li></ul></div></article>"""

html = head + shell_head + BODY + tail
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(html)
print("article:", f"articles/{SLUG}.html", len(html) // 1024, "KB")

# ---------------------------------------------------------------- cards
CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{SLUG}-cover.webp" alt="" '
        f'loading="lazy" decoding="async"></div><span class="chip">{CAT}</span>'
        f'<h3><a href="articles/{SLUG}.html">{TITLE}</a></h3>'
        f'<p>{DESC}</p><div class="meta"><span>{DATE}</span><i></i><span>{READ}</span></div></div>')

for page in ["anime.html", "index.html"]:
    s = open(page, encoding="utf-8").read()
    if SLUG in s:
        print("already on", page); continue
    m = re.search(r'<div class="cards[^"]*">', s)
    if m:
        s = s[:m.end()] + CARD + s[m.end():]
    else:                                    # fall back: before the first existing card
        i = s.find('<div class="card">')
        s = s[:i] + CARD + s[i:]
    open(page, "w", encoding="utf-8").write(s)
    print("card added ->", page)

# ---------------------------------------------------------------- sitemap
sm = open("sitemap.xml", encoding="utf-8").read()
url = f"https://blog.anipix.me/articles/{SLUG}.html"
if url not in sm:
    entry = f"  <url><loc>{url}</loc><lastmod>2026-10-19</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n"
    sm = sm.replace("</urlset>", entry + "</urlset>")
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
print("sitemap urls:", sm.count("<url>"))
