#!/usr/bin/env python3
"""Naruto Shippuden Part 13 - Season 22 (Episodes 480-500). FINAL PART."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-13-season-22"
TITLE = "Naruto Shippuden Part 13: Season 22 (Episodes 480-500) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Season 22 - the final season, from Sasuke Shinden to "
        "Naruto's wedding, all 21 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "13 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-12-seasons-20-21"
PREV_LABEL = "Part 12: Seasons 20-21"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("d19_naruto.jpg", "naruto-p13-1.webp"), ("anime_naruto5.jpg", "naruto-p13-2.webp")]
os.makedirs("/scratch/work/nimg", exist_ok=True)
for src, out in PICKS:
    p = f"/scratch/work/nimg/{src}"
    try:
        if not os.path.exists(p):
            urllib.request.urlretrieve(f"{BASE}/{src}", p)
        im = Image.open(p).convert("RGB")
        if im.width > 900:
            im = im.resize((900, int(im.height * 900 / im.width)), Image.LANCZOS)
        im.save(f"assets/img/{out}", "WEBP", quality=86, method=6)
        print("img", out, im.size, os.path.getsize(f"assets/img/{out}") // 1024, "KB")
    except Exception as e:
        print("img fail", out, type(e).__name__)

def fig(name, cap):
    return (f'<figure style="max-width:520px;margin-left:auto;margin-right:auto">'
            f'<img src="../assets/img/{name}" alt="{cap}" loading="lazy" decoding="async">'
            f'<figcaption>{cap}</figcaption></figure>')

EPS = [
 (480,"Naruto and Hinata","A gentle episode following a young Naruto and Hinata on the day they first met.","A lovely, quiet opening to the final season."),
 (481,"Sasuke and Sakura","Sasuke and Sakura's early days are shown from a different angle.","Character work."),
 (482,"Gaara and Shikamaru","Gaara's childhood and Shikamaru's school days are shown side by side.","Makes you appreciate how far they came."),
 (483,"Jiraiya and Kakashi","Jiraiya's dreams and young Kakashi's loneliness are explored.","Bittersweet, knowing what happens later."),
 (484,"Part 1: The Exploding Human","The Sasuke Shinden arc begins. Sasuke investigates a wave of exploding humans attacking villages.","Sasuke's post-war work as a wandering protector."),
 (485,"Part 2: Coliseum","Sasuke travels to a coliseum where wealthy owners make shinobi fight for sport.","Good worldbuilding."),
 (486,"Part 3: Fushin","The mystery deepens and a hidden kekkei genkai is revealed.","Solid mystery."),
 (487,"Part 4: The Ketsuryugan","The Ketsuryugan, a rare eye technique, is explained along with a clan's tragedy.","Great lore."),
 (488,"Part 5: The Last One","The arc concludes with Sasuke choosing to return to Konoha.","A fitting close for Sasuke's redemption."),
 (489,"Part 1: The State of Affairs","The Shikamaru Hiden arc begins. Shikamaru works a desk job and investigates the Land of Silence.","A quieter, more political story."),
 (490,"Part 2: Dark Clouds","Shikamaru's investigation deepens and the danger grows.","Tense."),
 (491,"Part 3: Recklessness","Shikamaru takes a risky approach.","Shows Shikamaru's flaws, which is good."),
 (492,"Part 4: Cloud of Suspicion","Suspicion spreads through the villages.","Political intrigue."),
 (493,"Part 5: Dawn","The arc resolves, and Shikamaru makes peace with his role.","A strong ending."),
 (494,"Part 1: Naruto's Wedding","The Konoha Hiden arc begins - everyone scrambles to find the perfect wedding gift for Naruto.","Pure warmth."),
 (495,"Part 2: A Full-Powered Wedding Gift","Guy and Lee try to make the most over-the-top gift possible.","Genuinely funny."),
 (496,"Part 3: Steam and Food Pills","A light episode about a hot spring and food pills.","Comedy."),
 (497,"Part 4: The Kazekage's Wedding Gift","Gaara decides what to give Naruto.","Sweet."),
 (498,"Part 5: The Last Mission","A secret mission becomes the framework for the final stretch.","Sets up the ending."),
 (499,"Part 6: The Outcome of the Secret Mission","The mission's results are revealed, and everything comes together.","Payoff."),
 (500,"Part 7: The Message","The series ends with Naruto's wedding and a message to everyone who watched.","A perfect final episode."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG2}" alt="Naruto Shippuden Part 13" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 13</strong> - the final part of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Season 22 - Episodes 480 to 500</strong>. After the war ended, Shippuden spent its last season on light novels: Sasuke's mission, Shikamaru's investigation, and finally Naruto's wedding.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 480-500 (21 episodes)</li>
<li><strong>Season 22:</strong> Nostalgic Days / Sasuke Shinden / Shikamaru Hiden / Konoha Hiden - <strong>light novel adaptations</strong></li>
<li><strong>Aired:</strong> 20 October 2016 - 23 March 2017</li>
<li><strong>Season 22 score:</strong> 7.5/10</li>
<li><strong>Series status:</strong> complete at 500 episodes</li>
</ul>

<p>This season is not action - it is an epilogue. It is about what everyone does once the fighting is over, and it ends with Naruto finally getting the ordinary life he spent the whole series fighting for. If you have come this far, you owe it to yourself to finish it.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p13-1.webp", "Naruto Uzumaki - the boy who became Hokage.")}

<h2>Part 13 verdict</h2>
<p>The first four episodes, which follow Naruto and Hinata, Sasuke and Sakura, Gaara and Shikamaru, and Jiraiya and Kakashi on ordinary days, are quietly the best thing here. They are not plot; they are payoffs for people you have watched grow up for 500 episodes.</p>
<p>The three novel arcs that follow are uneven but warm. Sasuke Shinden gives Sasuke a proper post-redemption role. Konoha Hiden, the wedding arc, is pure fan service in the best sense - it is a long goodbye to a cast the audience loves.</p>
<p><strong>Overall: 7.5/10.</strong> A gentle, satisfying ending to a 500-episode journey.</p>

{fig("naruto-p13-2.webp", "The end of Naruto Shippuden - and the start of Boruto.")}

<div class="next" style="margin-top:34px"><h3>You have finished the series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">That is all 500 episodes of Naruto Shippuden. Here is what to read next.</p>
<div class="chips"><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide (All 500 Episodes)</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-part-1-season-1.html">Back to Part 1</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-12-seasons-20-21.html">Part 12: Seasons 20-21 (Episodes 414-479)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", IMG2)
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = re.sub(r'</article><div class="related">.*?</div>', '', tpl[tpl.find("</article>"):], count=1, flags=re.S)
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("part 13 written")

CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{IMG2}" alt="" loading="lazy" decoding="async"></div>'
        f'<span class="chip">{CAT}</span><h3><a href="articles/{SLUG}.html">{TITLE}</a></h3><p>{DESC}</p>'
        f'<div class="meta"><span>{DATE}</span><i></i><span>{READ}</span></div></div>')
for page in ["anime.html", "index.html"]:
    s = open(page, encoding="utf-8").read()
    if SLUG in s:
        print("already", page); continue
    m = re.search(r'<div class="cards[^"]*">', s)
    s = (s[:m.end()] + CARD + s[m.end():]) if m else (s[:s.find('<div class="card">')] + CARD + s[s.find('<div class="card">'):])
    open(page, "w", encoding="utf-8").write(s); print("card ->", page)

sm = open("sitemap.xml", encoding="utf-8").read()
url = f"https://blog.anipix.me/articles/{SLUG}.html"
if url not in sm:
    entry = f'  <url><loc>{url}</loc><lastmod>2026-10-20</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n'
    sm = sm.replace("</urlset>", entry + "</urlset>")
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
print("sitemap urls:", sm.count("<url>"))
