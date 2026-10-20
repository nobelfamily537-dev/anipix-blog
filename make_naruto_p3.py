#!/usr/bin/env python3
"""Naruto Shippuden Part 3 - Season 3 (Episodes 54-71), images pulled from the AniPix app repo."""
import os, re
from PIL import Image

SLUG = "naruto-shippuden-part-3-season-3"
TITLE = "Naruto Shippuden Part 3: Season 3 (Episodes 54-71) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Season 3 - all 18 episodes of the Twelve Guardian "
        "Ninja arc, the anime-only season that gives Naruto his wind training.")
DATE = "20 October 2026"
READ = "12 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-2-season-2"
PREV_LABEL = "Part 2: Season 2 (Episodes 33-53)"
NEXT_SLUG = "naruto-shippuden-part-4-season-4"
NEXT_LABEL = "Part 4: Season 4 (Episodes 72-88)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"

# --- pull three Naruto wallpapers from the AniPix app repo and convert to WebP ---
SRC = "/scratch/work/nimg"
PICKS = [("d19_naruto.jpg", "naruto-p3-1.webp"), ("d28_naruto_fire.jpg", "naruto-p3-2.webp"),
         ("d19_kakashi.jpg", "naruto-p3-3.webp")]
for src, out in PICKS:
    p = os.path.join(SRC, src)
    if os.path.exists(p):
        im = Image.open(p).convert("RGB")
        if im.width > 900:
            im = im.resize((900, int(im.height * 900 / im.width)), Image.LANCZOS)
        im.save(f"assets/img/{out}", "WEBP", quality=86, method=6)
        print("img", out, im.size, os.path.getsize(f"assets/img/{out}") // 1024, "KB")

def fig(name, cap, portrait=False):
    style = ' style="max-width:520px;margin-left:auto;margin-right:auto"' if portrait else ""
    return (f'<figure{style}><img src="../assets/img/{name}" alt="{cap}" loading="lazy" decoding="async">'
            f'<figcaption>{cap}</figcaption></figure>')

EPS = [
 (54, "Nightmare", "Naruto wakes from a nightmare about his own Version 2 form tearing through everything around him. Sai, meanwhile, is in the village library reading up on how friendships actually work - and promptly calls Sakura \"ugly\". Kakashi tells Naruto they are going to build a brand new jutsu, stronger than the Rasengan, that only Naruto can use.", "A reset episode after the Tenchi Bridge. The wind-training promise it plants pays off later in the season."),
 (55, "Wind", "Training begins. Kakashi explains nature transformation - how a ninja learns which element their chakra leans towards, and how to add it to an existing technique. Naruto finds out his affinity is wind, which sets the whole season's goal: a wind-style Rasengan.", "The most important setup episode of the arc, and a genuinely good explanation of how chakra works."),
 (56, "Squirm", "Naruto keeps grinding at his wind training while a separate thread opens: graves are being robbed outside the village, and the culprits are looking for something specific. Asuma's own history starts to surface.", "The season shifts from training to plot. It takes its time getting there."),
 (57, "Deprived of Eternal Sleep", "The grave robbers' target becomes clearer - the tombs of the Twelve Guardian Ninja, the twelve warriors who once protected the Feudal Lord. Konoha's team is sent to the Fire Temple, where they meet a young monk named Sora.", "Sora's introduction is the real start of the arc."),
 (58, "Loneliness", "Sora is angry, prickly and clearly out of place - and Naruto recognises the feeling immediately, because he grew up the same way. The two of them rub each other the wrong way.", "The Naruto-Sora parallel is the emotional core of the season, and it lands."),
 (59, "A New Enemy", "A group calling itself Team Furido steps forward as the force behind the grave robbing. They are not after money - they have a political target in mind.", "Finally gives the arc a face to fight."),
 (60, "Impermanence", "The Fire Temple is attacked and the tombs are raided. Sora is caught in the middle of it, and the reason he is being targeted becomes clearer.", "The arc's first proper action beat."),
 (61, "Contact", "Naruto and Sora clash directly, and Sora's rage proves to be far more dangerous than anyone expected. There is something unusual about his chakra.", "Sets up the season's real mystery."),
 (62, "Teammate", "Forced to work together, Naruto and Sora slowly start to function as a unit rather than as two people shouting at each other.", "A quieter episode, but the character work is solid."),
 (63, "The Two Kings", "The past of the Twelve Guardian Ninja is laid out, and with it Asuma's connection to them. The arc's central idea appears: the pull between the Feudal Lord's authority and the Hokage's.", "The most interesting thematic episode of the season."),
 (64, "Jet Black Signal Fire", "Team Furido's plan moves into its next phase, and Konoha itself becomes the target rather than the temple.", "Raises the stakes from a local dispute to a village-level threat."),
 (65, "Lockdown of Darkness", "The village goes into lockdown as the enemy moves inside it. The team is split up and forced to react.", "A tense middle episode that keeps the arc moving."),
 (66, "Revived Souls", "The enemy's technique brings back fighters who should not be on the battlefield at all, and Konoha's ninja find themselves facing people they know.", "A genuinely unsettling turn for a filler arc."),
 (67, "Everyone's Struggle to the Death", "The fights spread out across the village, with each member of the team taking on their own opponent. Nobody gets an easy win.", "One of the better action episodes of the season."),
 (68, "Moment of Awakening", "Naruto's wind training finally starts to click, and Sora's power surfaces in full. The two threads of the season meet.", "The payoff episode for everything the season has been building."),
 (69, "Despair", "The situation turns badly against Konoha, and the team is pushed to the edge of what they can handle.", "Bleak, and effective for it."),
 (70, "Resonance", "Sora's chakra resonates with something inside Naruto - the same thing that has defined Naruto's whole life. It forces both of them to confront what they actually are.", "The emotional peak of the arc."),
 (71, "My Friend", "The arc closes. Sora makes his choice and leaves, and Naruto's wind training reaches the point where the new jutsu becomes possible. The season ends on Naruto calling Sora a friend.", "A warm ending that earns its place, even in a filler season."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG3}" alt="Naruto Shippuden Part 3" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 3</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Season 3: Episodes 54 to 71</strong> - the Twelve Guardian Ninja arc. This is the first <strong>anime-only season</strong> of Shippuden, and the one where Naruto actually learns to use wind release.</p>

<p>Every episode below has a short summary and a note on how it holds up. For the arc-level overview, see the <a href="../articles/naruto-shippuden-complete-arc-guide.html">complete arc guide</a>.</p>

{fig(IMG1, "Naruto Uzumaki - Season 3 is where his wind training begins.")}

<h2>Season 3 at a glance</h2>
<ul>
<li><strong>Episodes:</strong> 54-71</li>
<li><strong>Arc:</strong> Twelve Guardian Ninja</li>
<li><strong>Type:</strong> Anime-only (filler), but it contains the wind-training setup that matters later</li>
<li><strong>Aired:</strong> 3 April - 14 August 2008</li>
<li><strong>Opening theme:</strong> "Blue Bird" by Ikimono-gakari</li>
<li><strong>Season score:</strong> 6.5/10</li>
</ul>

<p>Let us be honest about this one: Season 3 is filler. It is not in the manga, it does not advance the Akatsuki plot, and if you skip it you will still understand everything that follows. But it is not pointless filler either. The wind-release training that runs through it is what eventually makes the Rasen Shuriken possible, and the arc introduces Sora - a character built to mirror Naruto - which gives the season a real emotional thread.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p3-1.webp", "Naruto - the wind training of Season 3 leads directly to the Rasen Shuriken.", portrait=True)}

<h2>Season 3 verdict</h2>
<p>This is the season people argue about. On one hand, it is a detour: 18 episodes that the manga never needed, and the middle stretch moves slowly. On the other hand, the wind training is genuinely important, Sora is a better character than most filler gets, and the theme - what makes a king, and what a village owes the people it protects - is more thoughtful than the arc gets credit for.</p>
<p>If you are watching Shippuden for the first time and want the essential run, you can skip most of this season and read a summary. If you are watching for the characters, it is worth the time.</p>
<p><strong>Season 3 score: 6.5/10.</strong> Skippable, but not bad.</p>

{fig("naruto-p3-2.webp", "Naruto in his chakra cloak.", portrait=True)}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-1-season-1.html">Part 1: Season 1 (Episodes 1-32)</a></li><li><a href="../articles/naruto-shippuden-part-2-season-2.html">Part 2: Season 2 (Episodes 33-53)</a></li></ul></div></article>"""

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
print("part 3 written")

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
