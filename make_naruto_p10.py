#!/usr/bin/env python3
"""Naruto Shippuden Part 10 - Seasons 16+17 (Episodes 349-372)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-10-seasons-16-17"
TITLE = "Naruto Shippuden Part 10: Seasons 16-17 (Episodes 349-372) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 16 and 17 - the Kakashi ANBU arc and the "
        "return of Team 7, all 24 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "16 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-9-seasons-14-15"
PREV_LABEL = "Part 9: Seasons 14-15"
NEXT_SLUG = "naruto-shippuden-part-11-seasons-18-19"
NEXT_LABEL = "Part 11: Seasons 18-19 (Episodes 373-413)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("d19_kakashi.jpg", "naruto-p10-1.webp"), ("anime_naruto1.jpg", "naruto-p10-2.webp")]
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
 (349,"The Mask That Hides the Heart","The Kakashi ANBU arc begins, set after Minato's death as Kakashi joins the ANBU Black Ops.","A slower, darker change of pace."),
 (350,"Minato's Death","The aftermath of Minato and Kushina's deaths is shown, and how it shaped Konoha.","Bleak, and well done."),
 (351,"Hashirama's Cells","The history of Hashirama's cells and the experiments around them is told.","Ties together a lot of lore."),
 (352,"The Rogue Ninja Orochimaru","Orochimaru's fall from Konoha shinobi to rogue ninja is shown.","A good origin for a great villain."),
 (353,"Orochimaru's Test Subject","Orochimaru's experiments are explored, and how far he had already gone.","Dark."),
 (354,"Their Own Paths","Kakashi and his former teammates take different roads.","Character work."),
 (355,"The Targeted Sharingan","The Sharingan becomes a target, and Kakashi is drawn into the politics of it.","Plot-heavy."),
 (356,"A Shinobi of the Leaf","What it means to be a shinobi of the Leaf is examined through Kakashi's service.","Thematic."),
 (357,"An Uchiha ANBU","Itachi joins the ANBU and works alongside Kakashi.","A great pairing."),
 (358,"Coup d'Etat","The Uchiha clan's planned coup is set in motion.","The tragedy starts to close in."),
 (359,"The Night of the Tragedy","The Uchiha massacre, from Kakashi's side of it.","One of the heaviest episodes."),
 (360,"Jonin Leader","Kakashi becomes a jonin leader and the arc looks ahead to Team 7.","A bridge to the main story."),
 (361,"Team 7","Team 7 is formed for the first time. The arc closes where the series began.","A lovely full-circle ending."),
 (362,"Kakashi's Resolve","Back in the war, Kakashi finds his resolve and helps turn the fight against Obito.","Strong return to canon."),
 (363,"The Allied Shinobi Forces Jutsu","The whole Alliance fights as one against the Ten-Tails.","A huge team moment."),
 (364,"The Ties That Bind","The Ten-Tails transforms, and the Alliance suffers a devastating loss.","One of the saddest episodes of the war."),
 (365,"Those Who Dance in the Shadows","Sasuke and Orochimaru move on Konoha while the war rages.","Two plots at once."),
 (366,"The All-Knowing","Sasuke revives the previous Hokage and asks them the truth about the village.","A huge lore episode."),
 (367,"Hashirama and Madara","Hashirama tells the story of how he and Madara met as children.","Excellent backstory."),
 (368,"The Era of Warring States","The world before the villages is shown, and why the village system exists.","Foundational lore."),
 (369,"My True Dream","Hashirama and Madara's shared dream of peace is told, and how it broke.","Tragic."),
 (370,"Sasuke's Answer","Sasuke decides what he believes and what he will fight for.","The point of the whole arc."),
 (371,"Hole","Sasuke reflects on the hole in his heart left by Itachi.","Quiet, and effective."),
 (372,"Something to Fill the Hole","Sasuke decides what will fill it, and rejoins the war on his own terms.","A satisfying turn."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG1}" alt="Naruto Shippuden Part 10" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 10</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Seasons 16 and 17 - Episodes 349 to 372</strong>. It is two things at once: a 13-episode anime-original flashback about Kakashi's years in the ANBU, and then the war's biggest lore reveal as Sasuke learns the truth about the village.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 349-372 (24 episodes)</li>
<li><strong>Season 16:</strong> Kakashi: Shadow of the ANBU Black Ops - episodes 349-361 - <strong>anime-original</strong></li>
<li><strong>Season 17:</strong> The Fourth Great Ninja War: The Return of Team 7 - episodes 362-372 - <strong>manga canon</strong></li>
<li><strong>Aired:</strong> 6 February 2014 - 14 August 2014</li>
<li><strong>Season 16 score:</strong> 7.5/10 &nbsp;·&nbsp; <strong>Season 17 score:</strong> 9/10</li>
</ul>

<p>The Kakashi ANBU arc is filler, but it is filler with a purpose - it fills in the gap between Minato's death and the start of the original series, and it ends exactly where Naruto begins. Season 17 then returns to the war and delivers the biggest information dump in the franchise.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p10-1.webp", "Kakashi Hatake - the ANBU years fill the gap before Team 7.")}

<h2>Part 10 verdict</h2>
<p>The Kakashi ANBU arc is the best filler stretch in Shippuden. It gives the Sharingan, Orochimaru's defection and the Uchiha massacre proper context, and ending it on the formation of Team 7 is a genuinely lovely touch. If you normally skip filler, this is the one to make an exception for.</p>
<p>Season 17 is essential. Episodes 366 to 372, where Sasuke revives the Hokage and learns why the village exists at all, are the philosophical heart of the entire series. Sasuke's decision at the end is the payoff the whole franchise was building toward.</p>
<p><strong>Overall: 8.5/10.</strong> Great filler plus a canon season that explains everything.</p>

{fig("naruto-p10-2.webp", "Naruto Uzumaki - Team 7 is coming back together.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-9-seasons-14-15.html">Part 9: Seasons 14-15 (Episodes 296-348)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", IMG1)
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = re.sub(r'</article><div class="related">.*?</div>', '', tpl[tpl.find("</article>"):], count=1, flags=re.S)
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("part 10 written")

CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{IMG1}" alt="" loading="lazy" decoding="async"></div>'
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
