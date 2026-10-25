#!/usr/bin/env python3
"""Naruto Shippuden Part 1 - Season 1 (Episodes 1-32)."""
import os, re
from PIL import Image, ImageDraw, ImageFont

SLUG = "naruto-shippuden-part-1-season-1"
TITLE = "Naruto Shippuden Part 1: Season 1 (Episodes 1-32) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Season 1 - all 32 episodes of the Kazekage Rescue arc, "
        "with a summary and review of each one.")
DATE = "20 October 2026"
READ = "16 min read"
CAT = "Anime"
NEXT_SLUG = "naruto-shippuden-part-2-season-2"
NEXT_LABEL = "Part 2: Season 2 (Episodes 33-53)"

os.makedirs("assets/img", exist_ok=True)
COVER = f"assets/img/{SLUG}-cover.webp"

W, H = 1200, 675
img = Image.new("RGB", (W, H), (14, 12, 20)); d = ImageDraw.Draw(img)
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(int(20 + 62 * t), int(14 + 30 * t), int(34 + 40 * t)))
for i in range(380):
    a = int(52 * (1 - i / 380))
    d.ellipse([W - 420 - i, -150 - i, W - 20 + i, 250 + i], outline=(a + 30, a + 12, a + 8))
d.rectangle([0, H - 6, W, H], fill=(214, 120, 40))
def font(sz, bold=True):
    for q in ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
              "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]:
        if os.path.exists(q):
            try: return ImageFont.truetype(q, sz)
            except Exception: pass
    return ImageFont.load_default()
d.text((70, 88), "ANIPIX BLOG", font=font(26), fill=(158, 152, 178))
y = 196
for ln in ["Naruto Shippuden", "Part 1 - Season 1"]:
    d.text((70, y), ln, font=font(74), fill=(255, 255, 255)); y += 90
d.text((70, y + 24), "Episodes 1-32  \u00b7  Kazekage Rescue arc", font=font(29, False), fill=(204, 198, 220))
img.save(COVER, "WEBP", quality=86, method=6)
print("cover ok")

EPS = [
 (1, "Homecoming", "Naruto comes back to the Hidden Leaf after two and a half years of training with Jiraiya. He is taller, louder, and still in orange. Konoha has changed around him, and Tsunade is now the Hokage.", "A confident, warm reopening. It reminds you who everyone is without wasting time."),
 (2, "The Akatsuki Makes Its Move", "The Akatsuki begin hunting the tailed beasts in earnest. Deidara and Sasori set out for the Hidden Sand, where the One-Tail is sealed inside the Kazekage.", "The threat is established fast. Shippuden does not waste episodes on setup."),
 (3, "The Results of Training", "Naruto and Sakura show how far they have come in two and a half years. Sakura's medical training under Tsunade is revealed, and the old Team 7 dynamic is rebuilt around two people who have clearly grown.", "Sakura's reintroduction is the best thing in the episode. She is finally written as capable."),
 (4, "The Jinchuriki of the Sand", "Gaara, now the Kazekage, is the target. The Akatsuki slip into the Hidden Sand, and the village is caught completely unprepared.", "Gaara as Kazekage is a great payoff for Part 1 of the original series."),
 (5, "The Kazekage Stands Tall", "Gaara fights Deidara above his own village, using his sand to protect the people below. He is fighting to keep the battle away from them, and it costs him.", "The aerial fight is a strong visual change of pace for the series."),
 (6, "Mission Cleared", "The Akatsuki escape with Gaara. Suna is left reeling, and the news reaches Konoha. The rescue mission begins to take shape.", "Sets the clock running. Everyone now knows how serious this is."),
 (7, "Run, Kankuro", "Kankuro, poisoned in the earlier clash, collapses. Suna's medical ninja cannot treat the poison, and the situation becomes a race against time.", "Kankuro gets a rare moment of focus."),
 (8, "Team Kakashi, Deployed", "Team Kakashi - Naruto, Sakura and Kakashi - is sent to the Hidden Sand. They are joined by Team Guy, and the pursuit of the Akatsuki begins.", "Two teams, one mission. The arc opens up properly here."),
 (9, "The Jinchuriki's Tears", "Sakura uses her medical knowledge to analyse and counter Sasori's poison, saving Kankuro. Naruto struggles with what is happening to Gaara, who he understands better than anyone.", "Sakura's first real victory of the series, and it is earned."),
 (10, "Sealing Jutsu: Nine Phantom Dragons", "The Akatsuki begin the extraction ritual, pulling the One-Tail out of Gaara. Naruto and the others race to reach them before it is too late.", "The ritual scenes give the Akatsuki a proper sense of scale."),
 (11, "The Medical Ninja's Student", "Chiyo, the elderly puppet master of Suna, joins the mission. Her history with Sasori is established, and the personal stakes of the coming fight become clear.", "Chiyo is one of the best additions in the arc."),
 (12, "The Retired Granny's Determination", "Chiyo commits to the mission despite her age and her connection to Sasori. The teams close in on the Akatsuki hideout.", "Quiet, character-driven, and it pays off later."),
 (13, "A Meeting With Destiny", "The teams finally reach the Akatsuki's location. The confrontation everyone has been waiting for is set up.", "The arc shifts from pursuit to battle."),
 (14, "Naruto's Growth", "Naruto's improvement over the timeskip is shown in action. The Akatsuki reveal how far ahead of them he still is.", "Good to see the training actually matter."),
 (15, "The Secret Weapon is Called....", "The Akatsuki's abilities are laid out as the fight begins in full. Sasori's puppets and Deidara's clay both prove to be genuinely dangerous.", "The Akatsuki feel like real opponents again."),
 (16, "The Secret of Jinchuriki", "The truth about the tailed beasts and their hosts is explained - including what happens to a jinchuriki when the beast is removed.", "Important lore, delivered without a lecture."),
 (17, "The Death of Gaara!", "The extraction is completed, and Gaara dies. Naruto's reaction is the emotional centre of the arc.", "One of the most effective moments in early Shippuden."),
 (18, "Charge Tactic! Button Hook Entry!!", "The rescue teams break into the Akatsuki hideout and the battle splits into separate fights. Team Guy takes one front, Team Kakashi another.", "The split lets every character have something to do."),
 (19, "Traps Activate! Team Guy's Enemy", "Team Guy fights through traps and opponents to clear a path, while Kakashi and Naruto push towards Deidara.", "Team Guy finally get a proper showing."),
 (20, "Hiruko vs. Two Kunoichi!", "Sakura and Chiyo face Sasori and his first puppet, Hiruko. It is a fight built on reading your opponent rather than raw power.", "Sakura's fight scenes here are the best she has had."),
 (21, "Sasori's Real Face", "Sasori is revealed to be inside a puppet body of his own making. The fight turns and the stakes rise.", "A genuinely unsettling reveal."),
 (22, "Chiyo's Secret Skills", "Chiyo brings out her own puppet techniques to match Sasori, and the puppet battle becomes a duel between teacher and student.", "The puppet choreography is excellent."),
 (23, "Father and Mother", "The story of Sasori's parents and the puppets he made of them is told. It explains the person he became.", "Quiet backstory that lands hard in the middle of a fight."),
 (24, "The Third Kazekage", "Sasori reveals he turned the Third Kazekage into a puppet, and uses it against Sakura and Chiyo. Its iron sand is almost impossible to counter.", "The arc's best pure action sequence."),
 (25, "Three Minutes Between Life and Death", "Sakura takes a hit that should be fatal and keeps going, using an antidote she prepared herself. The fight comes down to a matter of seconds.", "Sakura's best moment in the entire series."),
 (26, "Puppet Fight: 10 vs. 100!", "Sasori brings out a hundred puppets at once. Chiyo answers with ten of her own, and the scale of the battle explodes.", "Spectacular, and it still reads clearly."),
 (27, "Impossible Dream", "Sasori is defeated. Before he dies, he gives up information about a spy inside Orochimaru's ranks - the thread that will drive the next arc.", "A well-handled villain exit."),
 (28, "Beasts: Alive Again!", "Naruto and Kakashi fight Deidara. Naruto's frustration and grief push him further than he should go.", "Sets up Naruto's emotional state for the rest of the arc."),
 (29, "Kakashi Enlightened!", "Kakashi uses his Mangekyo Sharingan for the first time in the series, warping away one of Deidara's explosions.", "A big moment, and it is treated as one."),
 (30, "Aesthetics of an Instant", "Deidara escapes, and the chance to recover Gaara's body slips away. The teams are left with nothing to show for the fight.", "The arc refuses the easy win, which is what makes it work."),
 (31, "The Legacy", "Chiyo uses a forbidden technique to bring Gaara back to life, giving her own life in exchange. It closes her story with Sasori and with Suna.", "The emotional payoff of the whole arc."),
 (32, "Return of the Kazekage", "Gaara returns to his village and his people. Team Kakashi goes home. The first arc of Shippuden ends on a genuine high.", "A strong, earned ending. Season 1 closes cleanly."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{SLUG}-cover.webp" alt="Naruto Shippuden Part 1" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 1</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Season 1: Episodes 1 to 32</strong> - the whole of the Kazekage Rescue arc, the story that opened Shippuden in 2007 and immediately proved the sequel was going to be worth it.</p>

<p>Every episode below has a short summary of what happens and a note on how it holds up. If you only want the arc-level overview, read the <a href="../articles/naruto-shippuden-complete-arc-guide.html">complete arc guide</a> instead.</p>

<h2>Season 1 at a glance</h2>
<ul>
<li><strong>Episodes:</strong> 1-32</li>
<li><strong>Arc:</strong> Kazekage Rescue Mission</li>
<li><strong>Type:</strong> Canon (no filler in this season)</li>
<li><strong>Aired:</strong> 15 February 2007 - 25 October 2007</li>
<li><strong>Season score:</strong> 9/10</li>
</ul>

<p>Season 1 is the cleanest run in the whole of Shippuden. Thirty-two episodes, no filler, one continuous story, and a proper emotional payoff at the end. If someone asked you to show them why Shippuden was good, this is the season you would put on.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

<h2>Season 1 verdict</h2>
<p>This is Shippuden at its most focused. The arc has a clear goal, a ticking clock, and a villain duo who feel genuinely threatening. It gives Sakura the arc she never got in the original series, gives Gaara a proper payoff, and introduces Chiyo - one of the best one-arc characters in the show.</p>
<p>The only real criticism is pacing: a few middle episodes stretch a single fight across multiple weeks. But nothing here is filler, and nothing is wasted.</p>
<p><strong>Season 1 score: 9/10.</strong> Start here. This is the season that made Shippuden.</p>

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li><li><a href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Anime: The Complete Watch List</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", f"{SLUG}-cover.webp")
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = re.sub(r'</article><div class="related">.*?</div>', '', tpl[tpl.find("</article>"):], count=1, flags=re.S)
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("article written")

CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{SLUG}-cover.webp" alt="" loading="lazy" decoding="async"></div>'
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
