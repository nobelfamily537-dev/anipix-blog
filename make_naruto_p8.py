#!/usr/bin/env python3
"""Naruto Shippuden Part 8 - Seasons 12+13 (Episodes 243-295)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-8-seasons-12-13"
TITLE = "Naruto Shippuden Part 8: Seasons 12-13 (Episodes 243-295) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 12 and 13 - the start of the Fourth Great "
        "Ninja War and the Seven Ninja Swordsmen, all 53 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "23 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-7-seasons-10-11"
PREV_LABEL = "Part 7: Seasons 10-11"
NEXT_SLUG = "naruto-shippuden-part-9-seasons-14-15"
NEXT_LABEL = "Part 9: Seasons 14-15 (Episodes 296-348)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("d19_kakashi.jpg", "naruto-p8-1.webp"), ("anime_naruto5.jpg", "naruto-p8-2.webp")]
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
 (243,"Land Ahoy! Is this the Paradise Island?","Naruto and Yamato reach the island Naruto has been told is his mission. It is not a mission.","The truth is kept from Naruto, which sets up his arc for the season."),
 (244,"Killer Bee and Motoi","Killer B is introduced properly, and Motoi's history with him is told.","Killer B is the best new character in the war arc."),
 (245,"The Next Challenge! Naruto vs. The Nine Tails","Naruto begins training to control the Nine-Tails with Killer B's help.","The start of the best training arc of the war."),
 (246,"The Orange Spark","Naruto struggles against the Nine-Tails' hatred, and the reason he keeps failing is explained.","Sets up the payoff."),
 (247,"Target: Nine Tails","The Nine-Tails fights back with everything it has.","A strong internal-conflict episode."),
 (248,"The Fourth Hokage's Death Match!","Naruto meets his mother, Kushina, inside his own mind, and she tells him the story of the night he was born.","One of the best episodes in the entire series."),
 (249,"Thank You","Kushina's story concludes and Naruto finally understands what his parents gave him.","The emotional peak of the season."),
 (250,"Battle in Paradise! Odd Beast vs. The Monster!","Kisame is revealed to have been hiding inside the sword.","A good twist."),
 (251,"The Man Named Kisame","Kisame's past and his loyalty to the Akatsuki are explored before his end.","A villain who earns his exit."),
 (252,"The Angelic Herald of Death","Konan's history and her decision are told.","Konan finally gets her due."),
 (253,"The Bridge to Peace","Konan fights Tobi over Nagato's legacy.","A short, sharp fight."),
 (254,"The Super Secret S-Rank Mission","A light episode about a mission the characters have to keep secret.","Filler relief before the war."),
 (255,"The Artist Returns","Deidara and Sasori are brought back by the reanimation jutsu.","A great callback."),
 (256,"Assemble! Allied Shinobi Forces!","The Allied Shinobi Forces assemble for the first time, and the war formally begins.","A big, satisfying moment."),
 (257,"Meeting","The first of four recap episodes looking back at Naruto and Sasuke from the original series.","Recap. Skippable if you remember Part 1."),
 (258,"Rivals","The recap continues.","Recap."),
 (259,"Rift","The recap continues.","Recap."),
 (260,"Parting","The recap concludes at the Valley of the End.","Recap."),
 (261,"For My Friend","The war's first real battle begins, and the stakes are set.","Back to the plot."),
 (262,"War Begins","The war opens properly across multiple fronts.","Good scale."),
 (263,"Sai and Shin","Sai faces his reanimated brother, Shin.","The best emotional beat of the early war."),
 (264,"Secrets of the Reanimation Jutsu","The mechanics of the reanimation jutsu are explained.","Important lore."),
 (265,"An Old Nemesis Returns","Zabuza and Haku are reanimated and forced to fight.","A painful callback to Part 1."),
 (266,"The First and Last Opponent","Kakashi faces Zabuza and Haku again, and the fight is handled with real care.","One of the best war episodes."),
 (267,"The Brilliant Military Advisor of the Hidden Leaf","Shikamaru takes command of a division and shows why he is the smartest person on the field.","Shikamaru in his element."),
 (268,"Battleground!","Multiple divisions fight across the battlefield at once.","Good breadth."),
 (269,"Forbidden Words","A squad is forced to fight without saying what they cannot say.","A clever premise."),
 (270,"Golden Bonds","Naruto's Nine-Tails chakra reaches the battlefield for the first time.","A big moment."),
 (271,"Road to Sakura","A side-story episode set outside the main war.","Filler, but short."),
 (272,"Mifune vs. Hanzo","Mifune faces the reanimated Hanzo, and their shared past is told.","A strong one-off fight."),
 (273,"True Kindness","The theme of the war - what kindness costs - is explored.","Quiet and effective."),
 (274,"The Complete Ino-Shika-Cho Formation!","Team 10 finally performs the complete Ino-Shika-Cho formation.","A payoff decades in the making."),
 (275,"A Message from the Heart","A letter ties together a soldier and his family.","Sentimental, but it works."),
 (276,"Attack of the Gedo Statue","The Gedo Statue enters the battlefield and changes the balance.","Escalation."),
 (277,"Unison Sign","The allied forces regroup and coordinate.","Setup."),
 (278,"Medic Ninja in Danger","Sakura and the medical corps come under attack.","Sakura gets real work to do."),
 (279,"White Zetsu's Trap","The White Zetsu infiltration is discovered.","Good paranoia."),
 (280,"Aesthetics of an Artist","Deidara fights again, still obsessed with his art.","Deidara remains entertaining."),
 (281,"The Allied Mom Force!!","A light episode about the mothers of Konoha defending the village.","Comedy filler."),
 (282,"The Secret Origin of the Ultimate Tag Team!","The origin of a famous duo is told.","Filler."),
 (283,"Two Suns","Two fighters who mirror each other face off.","Decent."),
 (284,"The Helmet Splitter: Jinin Akebino!","One of the Seven Ninja Swordsmen is reintroduced.","The Swordsmen arc begins."),
 (285,"User of the Scorch Style: Pakura of the Sand!","Pakura fights and her story is told.","One of the better Swordsmen episodes."),
 (286,"Things You Can't Get Back","The cost of the war is felt by the characters.","Sombre."),
 (287,"One Worth Betting On","A character proves their worth on the battlefield.","Solid."),
 (288,"Danger: Jinpachi and Kushimaru!","Two Swordsmen fight as a pair.","Action."),
 (289,"The Lightning Blade: Ameyuri Ringo!","Ameyuri Ringo faces Omoi, and their fight is one of the best of the arc.","A standout Swordsmen episode."),
 (290,"Power - Episode 1","A six-part anime-original story begins, set in a village built on a secret.","The Power arc is filler, but it is beautifully animated."),
 (291,"Power - Episode 2","The Power story continues.","Strong animation."),
 (292,"Power - Episode 3","The Power story continues.","Well-directed."),
 (293,"Power - Episode 4","The Power story continues.","One of the better filler arcs."),
 (294,"Power - Episode 5","The Power story continues.","Good."),
 (295,"Power - Final Episode","The Power arc concludes, and the story returns to the war.","A strong end to a rare good filler arc."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG3}" alt="Naruto Shippuden Part 8" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 8</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Seasons 12 and 13 - Episodes 243 to 295</strong>. This is where the <strong>Fourth Great Ninja War</strong> actually starts, after Naruto finally learns to control the Nine-Tails.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 243-295 (53 episodes)</li>
<li><strong>Season 12:</strong> Nine-Tails Taming and Karmic Encounters - episodes 243-275 - <strong>mostly canon</strong></li>
<li><strong>Season 13:</strong> The Seven Shinobi Swordsmen + Power arc - episodes 276-295 - <strong>mixed</strong></li>
<li><strong>Aired:</strong> 5 January 2012 - 10 January 2013</li>
<li><strong>Season 12 score:</strong> 9/10 &nbsp;·&nbsp; <strong>Season 13 score:</strong> 7/10</li>
</ul>

<p>Season 12 contains two of the best episodes in the entire franchise - Naruto meeting his parents - and then pivots straight into the war. Season 13 is uneven: the Seven Ninja Swordsmen stretch is solid, and the anime-original Power arc is unusually good for filler.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p8-1.webp", "Kakashi Hatake - he faces Zabuza and Haku one more time.")}

<h2>Part 8 verdict</h2>
<p>Episodes 245 to 249 are essential. Naruto meeting Kushina and learning what happened the night he was born is the emotional foundation the whole war arc rests on. Episodes 263 to 266, where Sai and Kakashi face reanimated people they loved, are the best war episodes of the season.</p>
<p>Episodes 257 to 260 are a recap of the original series, so skip them if you have already watched Part 1. The Power arc (290-295) is filler, but it is the best-looking filler in Shippuden and worth a look.</p>
<p><strong>Overall: 8.5/10.</strong> Strong canon with a well-animated filler detour.</p>

{fig("naruto-p8-2.webp", "Naruto Uzumaki - the war is fully underway.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-7-seasons-10-11.html">Part 7: Seasons 10-11 (Episodes 197-242)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

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
print("part 8 written")

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
