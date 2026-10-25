#!/usr/bin/env python3
"""Naruto Shippuden Part 6 - Seasons 8+9 (Episodes 152-196)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-6-seasons-8-9"
TITLE = "Naruto Shippuden Part 6: Seasons 8-9 (Episodes 152-196) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 8 and 9 - Pain's Assault on Konoha and the "
        "Past Arc, all 45 episodes with a summary of each.")
DATE = "20 October 2026"
READ = "21 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-5-seasons-6-7"
PREV_LABEL = "Part 5: Seasons 6-7"
NEXT_SLUG = "naruto-shippuden-part-7-seasons-10-11"
NEXT_LABEL = "Part 7: Seasons 10-11 (Episodes 197-242)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("anime_naruto5.jpg", "naruto-p6-1.webp"), ("d28_naruto_fire.jpg", "naruto-p6-2.webp")]
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
 (152,"Somber News","News of Jiraiya's death reaches Konoha. Naruto is told, and he does not take it well.","A heavy, quiet opening. The grief is handled properly."),
 (153,"Following the Master's Shadow","Naruto works through his grief by chasing what Jiraiya left behind. Tsunade and the village begin decrypting Jiraiya's final message.","Turns mourning into a plot thread."),
 (154,"Decryption","The coded message on Fukasaku's back is cracked, pointing to Pain's true identity.","A rare mystery episode that actually pays off."),
 (155,"The First Challenge","Naruto trains on Mount Myoboku to learn Sage Mode, the technique Jiraiya could never fully master.","The start of the best training arc in the series."),
 (156,"Surpassing the Master","Naruto's sage training pushes past what Jiraiya achieved, thanks to a trick with shadow clones.","Naruto finally overtaking Jiraiya is a real moment."),
 (157,"Assault On the Leaf Village!","Pain attacks Konoha from the sky. The village is caught completely unprepared.","The scale jumps instantly. This is a war, not a fight."),
 (158,"Power to Believe","Konoha's ninja mobilise to defend the village. Naruto is still on Mount Myoboku.","Gives the side characters their due."),
 (159,"Pain Vs. Kakashi","Kakashi fights the Paths of Pain and is pushed further than we have ever seen him.","One of the best fights in the series, and it costs us."),
 (160,"Mystery of Pain","The mechanics of the Six Paths are explored as the village tries to work out how to beat something that cannot really die.","The most interesting villain design in the series."),
 (161,"Surname Is Sarutobi! Given Name, Konohamaru!","Konohamaru stands up to a Path of Pain on his own.","A small, brilliant moment that people still remember."),
 (162,"Pain to the World","Pain reveals his goal: to use the tailed beasts to force the world into peace through shared pain.","The villain's argument is genuinely unsettling because it makes sense."),
 (163,"Explosion! Sage Mode","Naruto arrives back in the village in Sage Mode and takes on the Paths directly.","The best entrance in the series."),
 (164,"Danger! Sage Mode Limit Reached","Naruto's Sage Mode has a hard time limit, and the fight pushes right up against it.","Tension that is built into the power itself."),
 (165,"Nine Tails, Captured!","Naruto is captured. The Nine-Tails begins to surface as he loses control.","The lowest point of the arc."),
 (166,"Confessions","Hinata steps in to help Naruto and finally says what she has been holding in since Part 1.","One of the most famous scenes in the franchise."),
 (167,"Planetary Devastation","Pain uses a technique that levels the entire village. Konoha is destroyed in seconds.","The single biggest moment of destruction in the series."),
 (168,"Fourth Hokage","Naruto breaks the seal and meets his father, Minato, inside his own mind.","The reveal that reframes Naruto's whole life."),
 (169,"The Two Students","Naruto and Pain - both students of Jiraiya - face each other as the answer to his question.","The thematic heart of the arc."),
 (170,"Big Adventure! The Quest for the Fourth Hokage's Legacy, Part 1","A short filler detour about a treasure hunt tied to the Fourth Hokage.","Out of place, but short."),
 (171,"Big Adventure! The Quest for the Fourth Hokage's Legacy, Part 2","The detour concludes.","Skippable."),
 (172,"Meeting","Naruto confronts Nagato directly and gives his answer to Pain's question.","The payoff the whole arc was built for."),
 (173,"Origin of Pain","Nagato's past is told - how a boy from Amegakure became Pain.","Makes the villain understandable without excusing him."),
 (174,"Tale of Naruto Uzumaki","Nagato chooses to believe in Naruto and gives his life to undo the destruction.","A rare ending where the hero wins by talking, and it works."),
 (175,"Hero of the Hidden Leaf","Konoha is rebuilt, and Naruto returns to a village that finally sees him for what he is.","The most satisfying ending in Shippuden."),
 (176,"Rookie Instructor Iruka","A filler arc begins, revisiting Iruka's early days as Naruto's teacher.","Filler, but warm."),
 (177,"Iruka's Ordeal","Iruka struggles with his own past and his feelings about the Nine-Tails.","Actually does something interesting with Iruka."),
 (178,"Iruka's Decision","Iruka makes the choice that defines his relationship with Naruto.","A nice little character piece."),
 (179,"Kakashi Hatake, the Jonin in Charge","Kakashi takes on a team of genin in a filler episode about what makes a leader.","Light, forgettable."),
 (180,"Inari's Courage Put to the Test","Inari returns from the Land of Waves, now older and braver.","A pleasant callback to Part 1."),
 (181,"Naruto's School of Revenge","Naruto teaches a lesson about revenge to a group of kids.","Pure filler."),
 (182,"Gaara's Bond","Gaara's relationship with Naruto is revisited through a filler story.","Fine, but it adds nothing new."),
 (183,"Naruto: Outbreak","A filler episode about a strange illness spreading.","One of the weaker ones."),
 (184,"Deploy! Team Tenten","Tenten finally gets a spotlight episode.","A rare Tenten focus, which fans appreciated."),
 (185,"Animal District","A light filler episode set in a district full of animals.","Harmless."),
 (186,"Ah, the Medicine of Youth","A Guy and Lee filler episode about training and youth.","Silly in a good way."),
 (187,"Gutsy Master and Student: The Training","A two-part filler about Jiraiya and Naruto's training days.","Nostalgic, and it lands better than the rest of the arc."),
 (188,"Record of the Gutsy Ninja Master and Student","The second half of the training flashback.","A decent farewell to Jiraiya."),
 (189,"Sasuke's Paw Encyclopedia","A comedy filler episode about Sasuke and cats.","Genuinely funny, which is rare for filler."),
 (190,"Naruto and the Old Soldier","Naruto befriends an old man with a war story.","Sentimental but effective."),
 (191,"Kakashi Love Song","A filler episode about Kakashi and a woman from his past.","Odd, but not bad."),
 (192,"Neji Chronicles","Neji gets a filler episode about his clan and his fate.","Neji deserved more than this."),
 (193,"The Man Who Died Twice","A filler story about a ninja who supposedly died and came back.","Standard filler."),
 (194,"The Worst Three-Legged Race","A comedy episode built around a three-legged race.","Pure light relief."),
 (195,"Team 10's Teamwork","Team 10 work together on a filler mission.","Shikamaru and Choji are always watchable."),
 (196,"Drive Towards Darkness","The filler arc closes, and the story turns back toward the war.","Finally back to the plot."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG3}" alt="Naruto Shippuden Part 6" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 6</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Seasons 8 and 9 - Episodes 152 to 196</strong>. Season 8 is <strong>Pain's Assault</strong>, the arc most people name as their favourite in the series. Season 9 is 21 episodes of filler.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 152-196 (45 episodes)</li>
<li><strong>Season 8:</strong> Pain's Assault - episodes 152-175 - <strong>manga canon</strong></li>
<li><strong>Season 9:</strong> Past Arc: The Locus of Konoha - episodes 176-196 - <strong>filler</strong></li>
<li><strong>Aired:</strong> 25 March 2010 - 27 January 2011</li>
<li><strong>Season 8 score:</strong> 10/10 &nbsp;·&nbsp; <strong>Season 9 score:</strong> 4/10</li>
</ul>

<p>If you watch one arc of Naruto Shippuden, watch 152 to 175. It is the point where everything the series has been building - Naruto's loneliness, Jiraiya's death, the tailed beasts, the Akatsuki - all arrive at once and pay off together. Then stop at 176 and jump to 197.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p6-1.webp", "Naruto Uzumaki - the hero of the Hidden Leaf.")}

<h2>Part 6 verdict</h2>
<p>Pain's Assault is the peak of the entire franchise. It has the best villain, the best entrance, the best destruction sequence and the most earned ending. Episode 166, 167 and 168 in particular are three of the most famous episodes in anime, and they are three in a row.</p>
<p>Season 9 is the longest filler block in Shippuden, arriving right after the best arc in the show. That placement makes it feel worse than it is - a few episodes (Iruka's, the Jiraiya training two-parter, Sasuke's paw encyclopedia) are genuinely worth watching. The rest is padding.</p>
<p><strong>Overall: 8.5/10.</strong> Watch 152-175 without skipping a single one, then read summaries for the rest.</p>

{fig("naruto-p6-2.webp", "Naruto in his chakra cloak - the Nine-Tails is never far away.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-5-seasons-6-7.html">Part 5: Seasons 6-7 (Episodes 113-151)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", IMG3)
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = re.sub(r'</article><div class="related">.*?</div>', '', tpl[tpl.find("</article>"):], count=1, flags=re.S)
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("part 6 written")

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
