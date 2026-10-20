#!/usr/bin/env python3
"""Naruto Shippuden Part 9 - Seasons 14+15 (Episodes 296-348)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-9-seasons-14-15"
TITLE = "Naruto Shippuden Part 9: Seasons 14-15 (Episodes 296-348) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 14 and 15 - Madara Uchiha arrives, the Five "
        "Kage fight, and the truth about Itachi, all 53 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "23 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-8-seasons-12-13"
PREV_LABEL = "Part 8: Seasons 12-13"
NEXT_SLUG = "naruto-shippuden-part-10-seasons-16-17"
NEXT_LABEL = "Part 10: Seasons 16-17 (Episodes 349-372)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("anx_madara_naruto.jpg", "naruto-p9-1.webp"), ("d19_itachi.jpg", "naruto-p9-2.webp")]
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
 (296,"Naruto Enters the Battle!","Naruto arrives on the battlefield in Sage Mode and turns the tide against the White Zetsu army.","One of the most satisfying entrances in the war."),
 (297,"A Father's Hope, A Mother's Love","The theme of the war is tied back to Naruto's parents and what they believed about him.","Quiet and effective."),
 (298,"Contact! Naruto vs. Itachi","Naruto meets the reanimated Itachi, and the two of them talk rather than fight.","A great conversation between two people who understand each other."),
 (299,"The Acknowledged One","Naruto's growth is measured against everyone who doubted him.","A nice payoff for a long-running thread."),
 (300,"The Mizukage, the Giant Clam, and the Mirage","The Mizukage fights a reanimated Kage and a giant clam.","Surreal, and fun."),
 (301,"Paradox","The war's contradictions - fighting people you love - are laid bare.","Strong theme work."),
 (302,"Terror: The Steam Imp","A reanimated Kage's steam technique causes real damage.","Good action."),
 (303,"Ghosts from the Past","Reanimated enemies force the heroes to confront their pasts.","Solid."),
 (304,"The Underworld Transfer Jutsu","A forbidden technique is explained and used.","Lore-heavy."),
 (305,"The Vengeful","A character driven by revenge faces the consequences.","Dark."),
 (306,"The Heart's Eye","The theme of seeing people truly is explored.","Quiet."),
 (307,"Fade into the Moonlight","A sombre episode about a character's death.","Well-handled."),
 (308,"Crescent Moonlight","The follow-up, dealing with grief and memory.","Emotional."),
 (309,"The A-Rank Mission: Food Fight","A light filler episode about a mission that turns into a cooking contest.","Comedy relief."),
 (310,"The Fallen Castle","A filler story set around a castle under siege.","Watchable."),
 (311,"Prologue of Road to Ninja","A tie-in episode for the Road to Ninja film.","Filler, but it has a point."),
 (312,"The Old Master and the Dragon's Eye","A filler episode about an old man and a legendary eye.","Standalone."),
 (313,"Rain Followed by Snow, with Some Lightning","A filler episode with three linked weather-themed stories.","Odd but charming."),
 (314,"The Sad Sun Shower","A filler story about a strange kind of weather.","Light."),
 (315,"Lingering Snow","A filler story about a memory that will not fade.","Sentimental."),
 (316,"The Reanimated Allied Forces!","The reanimation jutsu is turned on the Alliance's own dead.","The darkest turn of the war."),
 (317,"Shino vs. Torune!","Shino faces a reanimated member of his own clan.","Shino finally gets a real fight."),
 (318,"A Hole in the Heart: The Other Jinchuriki","The reanimated jinchuriki are explored, and the tragedy of what they are is shown.","A strong emotional beat."),
 (319,"The Soul Living Inside the Puppet","A puppet master's reanimated puppet fights on.","Good action."),
 (320,"Run, Omoi!","Omoi gets a spotlight episode.","Fun."),
 (321,"Reinforcements Arrive","Reinforcements reach the battlefield, and the scale grows again.","Big."),
 (322,"Madara Uchiha","The real Madara Uchiha is reanimated and enters the war. He is unlike anything the Alliance has faced.","One of the best villain reveals in the series."),
 (323,"The Five Kage Assemble","All five Kage gather to fight Madara together.","A huge moment."),
 (324,"The Unbreakable Mask and the Shattered Bubble","The Kage fight Madara, and his power is shown to be absurd.","Brilliant action."),
 (325,"Jinchuriki tai Jinchuriki!!","Naruto and Killer B face the reanimated jinchuriki.","A clash of equals."),
 (326,"Four Tails, the King of Sage Monkeys","Son Goku, the Four-Tails, is introduced and befriended.","A great new character."),
 (327,"Nine Tails","Naruto fights the Nine-Tails inside himself for full control.","The core of Naruto's arc."),
 (328,"Kurama","The Nine-Tails finally names itself and accepts Naruto. One of the biggest payoffs in the series.","Essential. One of the best episodes."),
 (329,"Two-Man Team","Naruto and Kurama fight as partners for the first time.","Hugely satisfying."),
 (330,"The Promise of Victory","The Alliance gains hope as Naruto's power turns the war.","Uplifting."),
 (331,"Eyes That See in the Dark","Madara's plans and the Eye of the Moon are explored.","Lore-heavy."),
 (332,"A Will of Stone","Onoki's past and his will are told.","Character work."),
 (333,"The Risks of the Reanimation Jutsu","The weaknesses of the reanimation jutsu are found.","Setup."),
 (334,"Sibling Tag Team","Sasuke and Itachi fight together against Kabuto.","A dream pairing."),
 (335,"To Each Their Own Leaf","The brothers' differing ideas of the village are compared.","Thematic."),
 (336,"Kabuto Yakushi","Kabuto's past and his obsession with identity are told.","Makes the villain understandable."),
 (337,"The Izanami Activated","Itachi uses Izanami, a technique that traps the target in a loop.","A clever power."),
 (338,"Izanagi and Izanami","The history of the two forbidden techniques is explained.","Important lore."),
 (339,"I Will Love You Always","Itachi says goodbye to Sasuke. One of the most famous scenes in the franchise.","Devastating, and earned."),
 (340,"Reanimation Jutsu: Release!","Itachi releases the reanimation jutsu, and the reanimated dead finally rest.","A huge, moving sequence."),
 (341,"Orochimaru's Return","Orochimaru is brought back, and the story turns toward the truth about Konoha.","A great return."),
 (342,"Secret of the Transportation Technique","The mystery of the masked man's space-time technique is explored.","Plot-heavy."),
 (343,"Who Are You?","The masked man's identity starts to crack.","Big reveal territory."),
 (344,"Obito and Madara","The relationship between Obito and Madara is explained.","The full picture."),
 (345,"I'm in Hell","Obito's past and his fall are told in full.","Tragic."),
 (346,"World of Dreams","Obito's plan for the Eye of the Moon is laid out.","Sets up everything after."),
 (347,"Creeping Shadow","The war's shadow spreads further.","Setup."),
 (348,"The New Akatsuki","The season closes on a new version of the Akatsuki taking shape.","A strong cliffhanger."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG2}" alt="Naruto Shippuden Part 9" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 9</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Seasons 14 and 15 - Episodes 296 to 348</strong>. This is the middle of the <strong>Fourth Great Ninja War</strong>, and it contains two of the biggest moments in the whole franchise: Madara Uchiha's arrival, and Itachi's farewell to Sasuke.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 296-348 (53 episodes)</li>
<li><strong>Season 14:</strong> The Fourth Great Ninja War: Assailants From Afar - episodes 296-320 - <strong>canon + a little filler</strong></li>
<li><strong>Season 15:</strong> The Fourth Great Ninja War: Sasuke and Itachi - episodes 321-348 - <strong>canon</strong></li>
<li><strong>Aired:</strong> 17 January 2013 - 30 January 2014</li>
<li><strong>Season 14 score:</strong> 8/10 &nbsp;·&nbsp; <strong>Season 15 score:</strong> 9.5/10</li>
</ul>

<p>Season 15 is one of the strongest stretches in Shippuden. Naruto and Kurama finally becoming partners, Madara wiping out an army on his own, and Itachi's goodbye are all here. Season 14 is slightly thinner - it has some filler episodes in the middle - but its back half is excellent.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p9-1.webp", "Madara Uchiha - the villain the whole war was waiting for.")}

<h2>Part 9 verdict</h2>
<p>Episodes 322 to 330 are the peak of this part. Madara arriving and immediately showing that the entire Allied army is not enough is one of the best villain introductions ever written, and then Naruto and Kurama finally becoming partners is the payoff the series has been building since Episode 1.</p>
<p>Episodes 334 to 340 are the other peak. Sasuke and Itachi fighting side by side, Kabuto's past, and then Itachi's final words to his brother make up the most emotional run in Shippuden outside of Jiraiya's death.</p>
<p><strong>Overall: 9/10.</strong> Essential war episodes with two enormous payoffs.</p>

{fig("naruto-p9-2.webp", "Itachi Uchiha - his story closes here.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-8-seasons-12-13.html">Part 8: Seasons 12-13 (Episodes 243-295)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", IMG2)
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = tpl[tpl.find("</article>"):]
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("part 9 written")

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
