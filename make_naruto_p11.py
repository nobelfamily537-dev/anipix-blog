#!/usr/bin/env python3
"""Naruto Shippuden Part 11 - Seasons 18+19 (Episodes 373-413)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-11-seasons-18-19"
TITLE = "Naruto Shippuden Part 11: Seasons 18-19 (Episodes 373-413) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 18 and 19 - Team 7 reunited, the fight against "
        "Obito and Madara, and the Chunin Exams arc, all 41 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "20 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-10-seasons-16-17"
PREV_LABEL = "Part 10: Seasons 16-17"
NEXT_SLUG = "naruto-shippuden-part-12-seasons-20-21"
NEXT_LABEL = "Part 12: Seasons 20-21 (Episodes 414-479)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("anime_narutosasuke1.jpg", "naruto-p11-1.webp"), ("d19_sasuke.jpg", "naruto-p11-2.webp")]
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
 (373,"Team 7, Assemble!","Sasuke rejoins Naruto and Sakura, and Team 7 fights together for the first time in years.","The moment fans waited hundreds of episodes for."),
 (374,"The New Three-Way Deadlock","The reunited Team 7 takes on the Ten-Tails and its masters.","Great action."),
 (375,"Kakashi vs. Obito","Kakashi and Obito fight in the other dimension, one on one.","One of the best fights of the war."),
 (376,"The Directive to Take the Nine-Tails!","Madara's plan to capture the Nine-Tails is set in motion.","Escalation."),
 (377,"Naruto vs. Mecha Naruto","A light filler episode featuring a mechanical Naruto.","Silly, and aware of it."),
 (378,"The Jinchuriki of the Ten Tails","Obito becomes the Ten-Tails' jinchuriki, and his power changes completely.","A terrifying turn."),
 (379,"An Opening","The Alliance searches for a weakness in Obito's new form.","Tense."),
 (380,"The Day Naruto Was Born","The full story of the night Naruto was born is finally told.","Essential. One of the best episodes."),
 (381,"Divine Tree","The Divine Tree and the history of the Ten-Tails are explained.","Big lore."),
 (382,"A Shinobi's Dream","The war's themes are tied back to what each character wants the world to be.","Thematic."),
 (383,"Pursuing Hope","The Alliance pushes on despite everything.","Uplifting."),
 (384,"A Heart Filled With Comrades","Naruto's strength is shown to be the people around him.","The core of the character."),
 (385,"Obito Uchiha","Obito's full story is told, and it reframes everything about the masked man.","A major payoff."),
 (386,"I'm Always Watching","Obito's connection to Rin and Kakashi is explored.","Tragic."),
 (387,"The Promise That Was Kept","A promise from the past is finally honoured.","Emotional."),
 (388,"My First Friend","Obito and Kakashi's friendship is revisited one last time.","A quiet, strong episode."),
 (389,"The Adored Elder Sister","A side-story about Hinata's clan and her sister Hanabi.","Filler, but sweet."),
 (390,"Hanabi's Decision","The Hyuga clan story continues.","Decent filler."),
 (391,"Madara Uchiha Arises","Madara is properly revived and takes the stage himself.","The villain gets real."),
 (392,"One's True Heart","The war's moral questions come to a head.","Strong."),
 (393,"A True Ending","The season closes on a major turning point in the war.","A big cliffhanger."),
 (394,"The New Chunin Exams","A filler arc begins, set around a new Chunin Exams during the war.","Filler, but fun."),
 (395,"The Chunin Exams Begin","The exam starts, with familiar faces as proctors.","Nostalgic."),
 (396,"The Three Questions","The written test and its three questions return.","A nice callback."),
 (397,"One Worthy as a Leader","The exam explores what makes a leader.","Thematic."),
 (398,"The Night Before the Second Exam","The night before the second stage is spent with the characters.","Light."),
 (399,"Demon Desert Survival","The second exam takes place in a harsh desert.","Good action filler."),
 (400,"As a Taijutsu User","A taijutsu-focused episode.","Fun."),
 (401,"The Ultimate","A character's ultimate technique is put to the test.","Solid."),
 (402,"Escape vs. Pursuit","A chase sequence drives the episode.","Fast-paced."),
 (403,"Unwavering Gutsiness","The theme of never giving up is hammered home.","On brand."),
 (404,"Tenten's Troubles","Tenten gets a spotlight episode.","Rare, and welcome."),
 (405,"The Imprisoned Pair","Two characters are captured and have to work together.","Decent."),
 (406,"The Place Where I Belong","A character decides where they truly belong.","Sentimental."),
 (407,"The Yamanaka Clan: Secret Ninjutsu","The Yamanaka clan's techniques are explored.","Lore."),
 (408,"The Cursed Puppet","A cursed puppet causes trouble.","Action filler."),
 (409,"Their Backs","The exam's final stage approaches, and the theme of trust returns.","Setup."),
 (410,"The Hidden Plot Set Into Motion","A plot behind the exam is revealed.","The arc gets a real story."),
 (411,"The Targeted Tailed Beast","The exam arc connects back to the war's stakes.","Good."),
 (412,"Neji's Judgment","Neji's role in the arc is resolved.","A fitting moment for him."),
 (413,"Hopes Entrusted to the Future","The Chunin Exams arc closes, and hope passes to the next generation.","A warm ending."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG3}" alt="Naruto Shippuden Part 11" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 11</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Seasons 18 and 19 - Episodes 373 to 413</strong>. Season 18 is the emotional climax of the Obito story and one of the best runs of the war. Season 19 is a 20-episode filler arc built around a new Chunin Exams.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 373-413 (41 episodes)</li>
<li><strong>Season 18:</strong> The Fourth Great Ninja War: Naruto and Sasuke - episodes 373-393 - <strong>manga canon</strong></li>
<li><strong>Season 19:</strong> Naruto's Childhood / The New Chunin Exams - episodes 394-413 - <strong>filler</strong></li>
<li><strong>Aired:</strong> 21 August 2014 - 25 December 2014</li>
<li><strong>Season 18 score:</strong> 9.5/10 &nbsp;·&nbsp; <strong>Season 19 score:</strong> 5/10</li>
</ul>

<p>Season 18 is the payoff for years of setup. Team 7 finally fighting together again, Kakashi versus Obito, and the truth about the night Naruto was born all land in the same run of episodes. Season 19 is a long filler detour that arrives at an awkward time.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p11-1.webp", "Naruto and Sasuke - Team 7 is whole again.")}

<h2>Part 11 verdict</h2>
<p>Watch 373 to 393. Episode 375, where Kakashi and Obito fight alone in another dimension, is one of the best-directed fights in Shippuden. Episode 380, the night Naruto was born, is the emotional keystone of the entire war. And Obito's story across 385 to 388 makes him the most human villain the series ever had.</p>
<p>Season 19 is filler. It is not bad filler - the Chunin Exams are always fun, and Tenten and Neji both get real moments - but it arrives in the middle of the war's climax, which makes it hard to sit through. Read the summaries and move on.</p>
<p><strong>Overall: 8.5/10.</strong> A superb canon season followed by a long filler arc.</p>

{fig("naruto-p11-2.webp", "Sasuke Uchiha - back on the same side, for now.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-10-seasons-16-17.html">Part 10: Seasons 16-17 (Episodes 349-372)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", IMG3)
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = tpl[tpl.find("</article>"):]
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("part 11 written")

CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{IMG3}" alt="" loading="lazy" decoding="async"></div>'
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
