#!/usr/bin/env python3
"""Naruto Shippuden Part 7 - Seasons 10+11 (Episodes 197-242)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-7-seasons-10-11"
TITLE = "Naruto Shippuden Part 7: Seasons 10-11 (Episodes 197-242) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 10 and 11 - the Five Kage Summit and the "
        "Paradise Life on a Boat arc, all 46 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "21 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-6-seasons-8-9"
PREV_LABEL = "Part 6: Seasons 8-9"
NEXT_SLUG = "naruto-shippuden-part-8-seasons-12-13"
NEXT_LABEL = "Part 8: Seasons 12-13 (Episodes 243-295)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("anime_narutosasuke1.jpg", "naruto-p7-1.webp"), ("d19_naruto.jpg", "naruto-p7-2.webp")]
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
 (197,"The Sixth Hokage Danzo","Danzo is named the Sixth Hokage while Tsunade lies in a coma after Pain's attack. Konoha's leadership changes at the worst possible moment.","Danzo taking power is a genuinely unsettling turn."),
 (198,"Five Kage Summit's Eve","The Five Kage Summit is called. Naruto learns about it and decides he has to be there.","Sets the stage for the biggest political arc in the series."),
 (199,"Enter the Five Kage!","All five Kage meet in one room for the first time. Each is characterised instantly.","A great introduction of five major figures at once."),
 (200,"Naruto's Plea","Naruto asks the Raikage to spare Sasuke. The Raikage refuses, and his reasoning is impossible to argue with.","One of the best-written conversations in the series."),
 (201,"Painful Decision","Naruto is forced to accept that saving Sasuke may not be possible, or even right.","The arc starts breaking Naruto's certainty down."),
 (202,"Racing Lightning","Sasuke's team attacks the summit. The Raikage fights Sasuke directly.","Fast, brutal action."),
 (203,"Sasuke's Ninja Way","Sasuke reveals how far he has gone. Gaara tries to talk him down.","Gaara's speech to Sasuke is a standout."),
 (204,"Power of the Five Kage","The Kage show why they are the strongest in the world, and Sasuke is outmatched.","A good reality check on Sasuke's power level."),
 (205,"Declaration of War","Tobi appears at the summit and declares the Fourth Great Ninja War. The room goes silent.","One of the most iconic scenes in the franchise."),
 (206,"Sakura's Feelings","Sakura confronts her feelings about Sasuke and Naruto, and makes a decision that is hard to watch.","Divisive, but honest about how messy it all is."),
 (207,"The Tailed Beast vs. The Tailless Tailed Beast","Kisame fights Killer B in a battle between two very different kinds of monster.","Kisame gets his best showing here."),
 (208,"As One's Friend","Sasuke's path and Naruto's path are compared directly, and the theme of the series comes into focus.","Thematic payoff."),
 (209,"Danzo's Right Arm","Danzo is revealed to have a Sharingan arm and a stolen eye. His methods are laid bare.","The most disturbing reveal of the arc."),
 (210,"The Forbidden Visual Jutsu","Danzo uses Izanagi, a forbidden technique that rewrites reality for a few seconds.","A genuinely clever power."),
 (211,"Danzo Shimura","Danzo's past and philosophy are explored, making him more than a simple villain.","A villain who believes he is right."),
 (212,"Sakura's Resolve","Sakura decides to take the burden of dealing with Sasuke onto herself.","Sakura finally acts on her own judgement."),
 (213,"Lost Bonds","The bonds between Team 7 are examined as the group splinters.","Quiet, and effective."),
 (214,"The Burden","Naruto carries the weight of what he has to do. The arc's theme comes to a head.","Sets up the coming war."),
 (215,"Two Fates","Sasuke's and Naruto's fates are laid out against each other.","Classic Naruto-Sasuke mirroring."),
 (216,"High-Level Shinobi","The summit's aftermath and the start of war preparations.","Transition episode."),
 (217,"The Infiltrator","A spy is discovered among the allied forces.","Builds the war's tension."),
 (218,"The Five Great Nations Mobilize","The five nations form a single allied army - something that has never happened before.","A big, satisfying moment."),
 (219,"Kakashi Hatake, the Hokage","Kakashi is considered for Hokage while Danzo's actions are scrutinised.","Kakashi getting the recognition he deserves."),
 (220,"Prophecy of the Great Lord Elder","The Great Lord Elder's prophecy about Naruto is revisited as war approaches.","Ties back to the Jiraiya episodes."),
 (221,"Storage","The season closes with the war about to begin.","A clean stopping point."),
 (222,"The Five Kage's Decision","The filler arc opens. Naruto and Killer B are sent to a secret island, told it is a mission.","The boat arc begins. It is very long."),
 (223,"The Young Man and the Sea","Naruto helps a fisherman catch a giant marlin.","Harmless, and better than most of what follows."),
 (224,"The Ninja of Benisu","Naruto runs into Sakura and the others gathering medical supplies.","Standard filler."),
 (225,"The Cursed Ghost Ship","Naruto boards a supposedly haunted ship and helps a cabin boy.","Actually has a decent twist."),
 (226,"Battleship Island","Naruto and the crew take on pirates holding an island.","Action filler, watchable."),
 (227,"The Forgotten Island","The crew lands on an island full of summoning animals.","Odd, but not boring."),
 (228,"Fight! Rock Lee!","A Rock Lee spotlight episode.","Lee fans get their moment."),
 (229,"Eat or Die! Mushrooms from Hell!","A comedy episode about poisonous mushrooms.","Pure comedy filler."),
 (230,"Revenge of the Shadow Clones","Naruto's shadow clones turn on him in a comedy setup.","Silly."),
 (231,"The Closed Route","The boat is forced onto a different path.","Padding."),
 (232,"The Girls' Get-Together","A light episode about the kunoichi of Konoha.","Nice to see the female cast together."),
 (233,"Naruto's Imposter","Someone is pretending to be Naruto.","Filler."),
 (234,"Naruto's Favorite Student","Naruto takes on a young student.","A gentle episode."),
 (235,"The Kunoichi of Nadeshiko Village","A village of kunoichi and their traditions are introduced.","Decent filler."),
 (236,"Friends You Can Count On","A story about the team backing each other up.","Standard."),
 (237,"Ah, My Hero Lady Tsunade!","A Tsunade-focused comedy episode.","Light relief."),
 (238,"Sai's Day Off","Sai spends a day off, and the show does something quiet with him.","One of the better filler episodes."),
 (239,"The Legendary Ino-Shika-Cho Trio","The Ino-Shika-Cho formation's history is explored.","Team 10 fans will like it."),
 (240,"Kiba's Determination","Kiba gets a spotlight episode.","Rare Kiba focus."),
 (241,"Kakashi, My Eternal Rival!","Guy and Kakashi's rivalry gets a full episode.","Genuinely funny."),
 (242,"Naruto's Vow","The boat arc ends and Naruto makes a promise about the war.","Finally back to the plot."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG1}" alt="Naruto Shippuden Part 7" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 7</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Seasons 10 and 11 - Episodes 197 to 242</strong>. Season 10 is the <strong>Five Kage Summit</strong>, where the series turns fully political and Tobi declares war. Season 11 is the infamous <strong>Paradise Life on a Boat</strong> filler arc.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 197-242 (46 episodes)</li>
<li><strong>Season 10:</strong> The Gathering of the Five Kage - episodes 197-221 - <strong>manga canon</strong></li>
<li><strong>Season 11:</strong> Paradise Life on a Boat - episodes 222-242 - <strong>filler</strong></li>
<li><strong>Aired:</strong> 10 February 2011 - 28 December 2011</li>
<li><strong>Season 10 score:</strong> 9/10 &nbsp;·&nbsp; <strong>Season 11 score:</strong> 3.5/10</li>
</ul>

<p>Season 10 is the last great canon stretch before the war. It gives Danzo his arc, brings all five Kage into one room, and ends with Tobi declaring war on the world. Season 11 is 21 episodes of Naruto on a boat, and it is the single most skipped block in Shippuden for good reason.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p7-1.webp", "Naruto and Sasuke - the two fates the arc keeps circling.")}

<h2>Part 7 verdict</h2>
<p>Watch 197 to 221. The Five Kage Summit is a political thriller with the best villain monologue in the series at the end of it, and Danzo is a far more interesting antagonist than he first appears. Naruto's plea to the Raikage is also one of the best scenes in the show.</p>
<p>Episodes 222 to 242 are the boat arc. It exists because the anime caught up with the manga, and it shows. A handful of episodes (Sai's day off, the Guy-Kakashi rivalry, the Ino-Shika-Cho history) are worth watching on their own. The rest is skippable without losing anything.</p>
<p><strong>Overall: 7/10.</strong> A great canon season with a long filler tail.</p>

{fig("naruto-p7-2.webp", "Naruto Uzumaki - the war is next.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-6-seasons-8-9.html">Part 6: Seasons 8-9 (Episodes 152-196)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

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
print("part 7 written")

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
