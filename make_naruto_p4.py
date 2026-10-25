#!/usr/bin/env python3
"""Naruto Shippuden Part 4 - Seasons 4+5 (Episodes 72-112)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-4-seasons-4-5"
TITLE = "Naruto Shippuden Part 4: Seasons 4-5 (Episodes 72-112) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 4 and 5 - the Akatsuki Suppression Mission "
        "and the Three-Tails arc, all 41 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "20 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-3-season-3"
PREV_LABEL = "Part 3: Seasons 3"
NEXT_SLUG = "naruto-shippuden-part-5-seasons-6-7"
NEXT_LABEL = "Part 5: Seasons 6-7 (Episodes 113-151)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"

# --- two more Naruto wallpapers from the AniPix app repo ---
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("d19_sasuke.jpg", "naruto-p4-1.webp"), ("d19_itachi.jpg", "naruto-p4-2.webp")]
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
 (72,"The Quietly Approaching Threat","Kakuzu and Hidan begin moving toward Konoha. Kakashi tells Naruto the mission to capture Sasori's spy is over and a new one is starting - the Akatsuki are closing in on the village.","Canon resumes. After 18 filler episodes the plot finally restarts."),
 (73,"Akatsuki's Invasion","The Akatsuki pair reaches the Land of Fire. Asuma leads a team out to intercept them, unaware of exactly what they are walking into.","Sets up the best character arc of the season."),
 (74,"Under the Starry Sky","Asuma, Shikamaru, Izumo and Kotetsu engage Hidan and Kakuzu. Hidan's immortality makes him almost impossible to fight normally.","The first real Akatsuki fight since Sasori, and it is brutal."),
 (75,"The Old Monk's Prayer","The fight goes badly. Asuma is mortally wounded by Hidan's curse technique. The team is left trying to get him home.","The most consequential episode of the season. It lands hard."),
 (76,"The Next Step","Asuma dies. Before he goes he tells Shikamaru something that will define Shikamaru for the rest of the series.","Quietly one of the most important scenes in Shippuden."),
 (77,"Climbing Silver","Shikamaru puts Asuma's strategy into motion - a plan built like a shogi game, with himself as the piece that is meant to be sacrificed.","Shikamaru's shogi metaphor pays off here and it is excellent."),
 (78,"The Judgment","Shikamaru faces Hidan with the trap already set. Kakashi and the others deal with Kakuzu.","The plan is tight and the execution is satisfying."),
 (79,"Unfulfilled Scream","Hidan is destroyed and buried. Shikamaru finally allows himself to grieve for Asuma.","The arc's emotional release."),
 (80,"Last Words","Kakuzu's five hearts are explained - he has been keeping himself alive by stealing the hearts of others, and each one gives him a separate elemental attack.","The most interesting villain power of the arc."),
 (81,"Sad News","News of Asuma's death spreads through the village. Kurenai, who was expecting his child, takes it hardest.","A necessary, painful episode."),
 (82,"Team Ten","Shikamaru, Choji and Ino resolve to carry Asuma's legacy. Meanwhile Naruto's wind training continues with Yamato and Kakashi.","Brings the team back together."),
 (83,"Target: Locked On","Kakuzu is still alive and Team Kakashi is sent after him. Naruto arrives with a new technique and something to prove.","Sets up the payoff of the wind training."),
 (84,"Kakuzu's Abilities","Kakuzu uses his four remaining hearts in sequence, forcing the team to adapt to each element.","A strong, technical fight."),
 (85,"The Terrifying Secret","The fight narrows down to Naruto and Kakuzu. Naruto gets ready to use the technique he has spent the season building.","The tension here is real."),
 (86,"Shikamaru's Genius","Shikamaru's plan is shown in full and Kakuzu is left exposed. The arc's two threads meet.","Good payoff for both plotlines."),
 (87,"When You Curse Someone, You Dig Your Own Grave","Hidan's fate is sealed permanently, and Shikamaru walks away having done exactly what he said he would.","A dark, quiet ending to a dark arc."),
 (88,"Wind Style: Rasen Shuriken!","Naruto debuts the Rasen Shuriken - a wind-style Rasengan that hits at a cellular level. It works, but it costs him.","One of the biggest moments in all of Shippuden. Worth the 18 filler episodes."),
 (89,"The Price of Power","The Rasen Shuriken leaves Naruto's arm badly damaged. Tsunade warns him not to use it again. A new threat is detected: Orochimaru's hideout.","A grounded follow-up that stops the new technique feeling like a free win."),
 (90,"A Shinobi's Determination","Naruto, Sakura, Sai and Yamato are sent to investigate Orochimaru's hideout. They meet a girl named Guren who can control crystal.","The Three-Tails arc begins."),
 (91,"Orochimaru's Hideout Discovered","The team enters the hideout area and finds traces of experiments. Guren is working for Orochimaru and has her own agenda.","Slower, but it sets up the arc's villain."),
 (92,"Encounter","The team meets Yūkimaru, a young boy with a strange connection to the Three-Tails. Guren takes an interest in him.","Yūkimaru is the emotional hook of the arc."),
 (93,"Connecting Hearts","Naruto tries to reach Yūkimaru, who has been used and abandoned by the people around him.","The Naruto-and-a-lonely-child beat, done again, but it works."),
 (94,"A Night of Rain","The Akatsuki also move toward the Three-Tails. Three sides are now chasing the same target.","Raises the stakes by adding a third faction."),
 (95,"The Two Charms","Yūkimaru's charm and Guren's past are explored, showing why she is protecting him.","Guren gets actual depth, which filler villains rarely do."),
 (96,"The Unseeing Enemy","The team fights an enemy they cannot see, and Kabuto reappears in the middle of it.","A solid action episode."),
 (97,"The Labyrinth of Distorted Reflection","The team is trapped in a maze of mirrors and reflections, forcing them to fight without being able to trust their own eyes.","One of the better filler set-pieces."),
 (98,"The Target Appears","The Three-Tails surfaces, and all three groups converge on it at once.","The arc's midpoint."),
 (99,"The Rampaging Tailed Beast","The Three-Tails goes on a rampage. Its sheer size makes it a completely different problem from the other tailed beasts.","Good escalation."),
 (100,"Inside the Mist","The team is separated in the mist and forced into individual fights.","A classic Shippuden structure, executed fine."),
 (101,"Everyone's Feelings","Yūkimaru's feelings about Guren and about being used come to the surface.","The character thread peaks here."),
 (102,"Regroup!","The team pulls back and reorganises for a second attempt at sealing the Three-Tails.","Necessary setup."),
 (103,"The Four-Corner Sealing Barrier","The sealing team sets up the four-corner barrier to trap the Three-Tails, with each member holding a corner.","A tense, well-built sequence."),
 (104,"Breaking the Crystal Style","Guren's crystal style is finally countered, and her position becomes impossible.","The best Guren episode."),
 (105,"The Battle Over the Barrier","The fight swings back and forth over the barrier. Holding it costs the team dearly.","Solid action."),
 (106,"Red Camellia","Guren's backstory is told in full, including the camellia that ties her to Yūkimaru.","The arc's most emotional episode."),
 (107,"Strange Bedfellows","Enemies are forced to cooperate against a common threat, which is exactly as uncomfortable as it sounds.","A nice change of pace."),
 (108,"Guidepost of the Camellia","Yūkimaru follows the camellia to find Guren, and the two finally reach each other.","Pays off the thread the arc has been building."),
 (109,"Counterattack of the Curse Mark","A curse mark returns as a weapon, and the team has to deal with an enemy powered by something they have seen before.","Good callback."),
 (110,"Memory of Guilt","Guren is forced to confront what she has done and what it cost.","Quieter, character-focused."),
 (111,"Shattered Promise","The promise between Guren and Yūkimaru is broken, and the arc heads toward its close.","Bleak, but earned."),
 (112,"A Place to Return To","The arc ends. Guren makes her choice and Yūkimaru finds somewhere to belong. The Three-Tails is dealt with, and the story turns back toward the main plot.","A warm ending to a long filler arc."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG1}" alt="Naruto Shippuden Part 4" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 4</strong> of the complete Naruto Shippuden episode-by-episode guide. From here on each part covers <strong>two seasons</strong>. This one covers <strong>Season 4 and Season 5 - Episodes 72 to 112</strong>: the Akatsuki Suppression Mission (all manga canon) and the Three-Tails' Appearance arc (mostly anime-only).</p>

<p>It is the biggest swing in the series so far - one of the best arcs in all of Shippuden, followed by one of its longest filler stretches.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 72-112 (41 episodes)</li>
<li><strong>Season 4:</strong> Akatsuki Suppression Mission - episodes 72-88 - <strong>manga canon</strong></li>
<li><strong>Season 5:</strong> Three-Tails' Appearance - episodes 89-112 - <strong>mostly filler</strong></li>
<li><strong>Aired:</strong> 21 August 2008 - 4 June 2009</li>
<li><strong>Season 4 score:</strong> 9.5/10 &nbsp;·&nbsp; <strong>Season 5 score:</strong> 5.5/10</li>
</ul>

<p>Season 4 is one of the best runs in Shippuden. It gives Shikamaru the arc that turns him from a side character into one of the best-written people in the show, and it ends with Naruto's first genuinely new technique. Season 5 is the price you pay for it: 24 episodes of filler about a turtle.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p4-1.webp", "Sasuke Uchiha - the Akatsuki plot keeps circling back to him.")}

<h2>Part 4 verdict</h2>
<p>Watch episodes 72 to 88 without skipping anything. The Asuma arc, Shikamaru's shogi plan and the debut of the Rasen Shuriken are three of the strongest stretches in the whole series, and they all sit inside 17 episodes.</p>
<p>Episodes 89 to 112 are the opposite. The Three-Tails arc is long, it is anime-only, and it takes a tailed beast - something the show usually treats as a serious threat - and turns it into a background problem. Guren and Yūkimaru are better written than filler usually gets, and if you like the characters it is watchable. But if you are watching for the plot, this is the one part of Shippuden you can safely skip.</p>
<p><strong>Overall: 8/10.</strong> Half of it is essential, half of it is optional.</p>

{fig("naruto-p4-2.webp", "Itachi Uchiha - the Itachi Pursuit Mission is next.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-3-season-3.html">Part 3: Season 3 (Episodes 54-71)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

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
print("part 4 written")

# point Part 3's "next" at the real Part 4 slug
p3 = "articles/naruto-shippuden-part-3-season-3.html"
s3 = open(p3, encoding="utf-8").read()
s3 = s3.replace("naruto-shippuden-part-4-season-4.html", f"{SLUG}.html")
s3 = s3.replace("Part 4: Season 4 (Episodes 72-88)", "Part 4: Seasons 4-5 (Episodes 72-112)")
open(p3, "w", encoding="utf-8").write(s3)
print("part 3 next-link fixed")

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
