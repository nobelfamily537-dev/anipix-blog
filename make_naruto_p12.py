#!/usr/bin/env python3
"""Naruto Shippuden Part 12 - Seasons 20+21 (Episodes 414-479)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-12-seasons-20-21"
TITLE = "Naruto Shippuden Part 12: Seasons 20-21 (Episodes 414-479) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 20 and 21 - the Infinite Tsukuyomi, Kaguya, "
        "and the final Naruto vs Sasuke battle, all 66 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "28 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-11-seasons-18-19"
PREV_LABEL = "Part 11: Seasons 18-19"
NEXT_SLUG = "naruto-shippuden-part-13-season-22"
NEXT_LABEL = "Part 13: Season 22 (Episodes 480-500)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("anime_naruto5.jpg", "naruto-p12-1.webp"), ("d19_naruto.jpg", "naruto-p12-2.webp")]
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
 (414,"On the Brink of Death","Naruto and Sasuke are both on the edge of death as Madara closes in.","The war's lowest point."),
 (415,"The Two Mangekyo","The two Mangekyo Sharingan are brought together.","Big lore."),
 (416,"The Formation of Team Minato","A flashback to the formation of Team Minato.","Kakashi's origin again, but from a different angle."),
 (417,"You'll Be My Backup","Obito's promise to Kakashi is revisited.","Tragic in hindsight."),
 (418,"The Blue Beast vs. Six Paths Madara","Might Guy takes on Madara alone.","One of the best fights in the entire series."),
 (419,"Papa's Youth","Guy's father and the Eight Inner Gates are explained.","Makes Guy's fight land harder."),
 (420,"The Eight Inner Gates Formation","Guy opens the final gate.","Legendary."),
 (421,"The Sage of Six Paths","Naruto and Sasuke meet the Sage of Six Paths.","The biggest lore episode in the series."),
 (422,"The Ones Who Will Inherit","The Sage explains what he is passing on.","Setup for the finale."),
 (423,"Naruto's Rival","Sasuke's role is defined against Naruto's.","Thematic."),
 (424,"To Rise Up","Naruto and Sasuke rise again with new power.","Hugely satisfying."),
 (425,"The Infinite Dream","The Infinite Tsukuyomi is activated.","Everything goes wrong at once."),
 (426,"The Infinite Tsukuyomi","The world is trapped in the dream.","Bleak."),
 (427,"To the Dreamworld","The dream worlds are explored.","Surreal."),
 (428,"Where Tenten Belongs","Tenten's dream world is shown.","Filler, but charming."),
 (429,"Killer B Rappuden: Part 1","A comedy two-parter starring Killer B.","Pure fun."),
 (430,"Killer B Rappuden: Part 2","The Killer B comedy continues.","Light relief."),
 (431,"To See That Smile, Just One More Time","A dream-world episode built around a single wish.","Sentimental."),
 (432,"The Loser Ninja","A dream world explores what could have been.","Bittersweet."),
 (433,"The Search Mission","A dream-world story about a search.","Filler."),
 (434,"Team Jiraiya","Jiraiya's team is revisited in a dream.","Nostalgic."),
 (435,"Order of Priority","A dream world tests the characters' priorities.","Decent."),
 (436,"The Masked Man","The masked man's identity is revisited.","Lore."),
 (437,"The Sealed Power","A sealed power is released.","Action."),
 (438,"The Rules or a Comrade","The old question of rules versus comrades returns.","Thematic."),
 (439,"The Child of Prophecy","The prophecy about Naruto is revisited one last time.","Payoff."),
 (440,"The Caged Bird","Neji and Hinata's clan history is revisited.","Emotional."),
 (441,"Returning Home","A dream world takes a character home.","Warm."),
 (442,"The Mutual Path","Two characters' paths are compared.","Thematic."),
 (443,"The Difference in Power","The gap in power between the heroes and the enemy is shown.","Tense."),
 (444,"Leaving the Village","A flashback arc begins, set before the original series.","Filler, but good."),
 (445,"Pursuers","The pursuit of a character's past begins.","Solid."),
 (446,"Collision","Two forces collide.","Action."),
 (447,"Another Moon","A different kind of moon is introduced.","Lore."),
 (448,"Comrade","The theme of comradeship is explored.","Thematic."),
 (449,"The Shinobi Unite","Shinobi from different places unite.","Good."),
 (450,"Rival","A rivalry is established.","Setup."),
 (451,"Birth and Death","A birth and a death frame the episode.","Emotional."),
 (452,"The Genius","A character's genius is examined.","Character work."),
 (453,"The Pain of Living","The cost of survival is explored.","Heavy."),
 (454,"Shisui's Request","Shisui Uchiha's story is told.","Important lore."),
 (455,"Moonlit Night","A quiet night sets up a tragedy.","Atmospheric."),
 (456,"The Darkness of the Akatsuki","The Akatsuki's origins are shown.","Excellent backstory."),
 (457,"Partner","The bond between Akatsuki partners is explored.","Good."),
 (458,"Truth","The truth about a long-running mystery is revealed.","Payoff."),
 (459,"She of the Beginning","Kaguya Ootsutsuki is introduced.","A shocking new villain."),
 (460,"Kaguya Ootsutsuki","Kaguya's power and origins are shown.","The final boss."),
 (461,"Hagoromo and Hamura","Kaguya's sons and their fight against her are told.","Foundational lore."),
 (462,"A Fabricated Past","The history of the ninja world is questioned.","Big."),
 (463,"The No. 1 Most Unpredictable Ninja","Naruto's defining trait becomes the key to victory.","Perfect."),
 (464,"Ninshu: The Ninja Creed","The original purpose of ninjutsu is explained.","Thematic payoff."),
 (465,"Ashura and Indra","The sons of the Sage and their endless conflict are shown.","The series' deepest lore."),
 (466,"The Tumultuous Journey","Ashura's journey is told.","Good."),
 (467,"Asura's Decision","Ashura chooses his path.","Thematic."),
 (468,"The Successor","The question of succession is answered.","Payoff."),
 (469,"A Special Mission","A special mission frames the episode.","Solid."),
 (470,"Connecting Thoughts","The idea of connecting people runs through the episode.","Thematic."),
 (471,"The Two of Them... Always","Naruto and Sasuke's bond is centred.","Emotional."),
 (472,"You Better...","A promise is finally made.","Payoff."),
 (473,"The Sharingan Revived","The Sharingan returns at a crucial moment.","Big."),
 (474,"Congratulations","A celebration after so much loss.","Warm."),
 (475,"The Valley of the End","Naruto and Sasuke return to where it all began.","The perfect setting for the finale."),
 (476,"The Final Battle","Naruto versus Sasuke, at last, with everything on the line.","The fight the whole series built to."),
 (477,"Naruto and Sasuke","The fight reaches its emotional core.","Devastating."),
 (478,"The Unison Sign","The two of them finally understand each other.","Beautiful."),
 (479,"Naruto Uzumaki!!","The series ends where it began - with Naruto Uzumaki.","A perfect ending."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG1}" alt="Naruto Shippuden Part 12" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 12</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Seasons 20 and 21 - Episodes 414 to 479</strong>. This is the end of the war, the arrival of Kaguya, and finally the Naruto versus Sasuke fight the entire series was built toward.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 414-479 (66 episodes)</li>
<li><strong>Season 20:</strong> The Fourth Great Ninja War: The End - episodes 414-443 - <strong>canon + dream filler</strong></li>
<li><strong>Season 21:</strong> Jiraiya Ninja Scrolls / Kaguya / The Final Battle - episodes 444-479 - <strong>canon + flashback filler</strong></li>
<li><strong>Aired:</strong> 28 May 2015 - 13 October 2016</li>
<li><strong>Season 20 score:</strong> 8.5/10 &nbsp;·&nbsp; <strong>Season 21 score:</strong> 8/10</li>
</ul>

<p>This is the longest part in the guide, because Shippuden's final stretch is enormous. It contains some of the best episodes in the franchise and also a very long stretch of dream-world filler. The rule is simple: watch the canon, read the summaries for the dreams.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p12-1.webp", "Naruto Uzumaki - the Number One Most Unpredictable Ninja.")}

<h2>Part 12 verdict</h2>
<p>Episodes 414 to 428 are outstanding. Might Guy's fight against Madara, Naruto and Sasuke receiving the Sage's power, and the Infinite Tsukuyomi all land. Episode 418 in particular is one of the greatest fights in the entire series.</p>
<p>Episodes 429 to 458 are mostly dream-world and flashback filler. Some of it is genuinely good - the Akatsuki's origin, Shisui's story, Jiraiya's team - but it is a long detour in the middle of the climax. Then 459 to 479 is the real ending, and it is worth every episode.</p>
<p><strong>Overall: 8.5/10.</strong> A long, uneven, but ultimately brilliant final stretch.</p>

{fig("naruto-p12-2.webp", "The Valley of the End - where it all began, and where it ends.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-11-seasons-18-19.html">Part 11: Seasons 18-19 (Episodes 373-413)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", IMG1)
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = tpl[tpl.find("</article>"):]
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("part 12 written")

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
