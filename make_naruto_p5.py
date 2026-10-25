#!/usr/bin/env python3
"""Naruto Shippuden Part 5 - Seasons 6+7 (Episodes 113-151)."""
import os, re, urllib.request
from PIL import Image

SLUG = "naruto-shippuden-part-5-seasons-6-7"
TITLE = "Naruto Shippuden Part 5: Seasons 6-7 (Episodes 113-151) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Seasons 6 and 7 - the Itachi Pursuit Mission, the "
        "Kakashi Gaiden flashback and the Sasuke-Itachi fight, all 39 episodes.")
DATE = "20 October 2026"
READ = "19 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-4-seasons-4-5"
PREV_LABEL = "Part 4: Seasons 4-5"
NEXT_SLUG = "naruto-shippuden-part-6-seasons-8-9"
NEXT_LABEL = "Part 6: Seasons 8-9 (Episodes 152-196)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"
BASE = "https://raw.githubusercontent.com/nobelfamily537-dev/AniPix-Walls/main/anime"
PICKS = [("anime_naruto1.jpg", "naruto-p5-1.webp"), ("anx_madara_naruto.jpg", "naruto-p5-2.webp")]
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
 (113,"The Serpent's Pupil","Orochimaru, still weakened, is looked after by Kabuto while Sasuke trains. Sasuke begins to assemble a team - the people who will become Taka.","A calm-before-the-storm episode that quietly sets up the rest of the season."),
 (114,"Eye of the Hawk","Sasuke approaches Suigetsu and frees him. The tone is set: this is a colder, more calculating Sasuke than the one we last saw at the Tenchi Bridge.","The best introduction of the arc."),
 (115,"Zabuza's Blade","Sasuke recruits Karin, and Suigetsu goes after Zabuza's sword. The team starts to take shape.","A nice callback to Part 1 of the original series."),
 (116,"Guardian of the Iron Wall","Sasuke goes after Jugo, who is locked up for a reason - his rages are uncontrollable.","Jugo is the most interesting of the new characters."),
 (117,"Jugo of the Northern Hideout","Sasuke persuades Jugo to join him, using Kimimaro's name. Team Taka is now complete.","The team-building arc closes cleanly."),
 (118,"Formation!","Sasuke names his team Taka - 'hawk' - and sets them on a single goal: finding Itachi. Konoha simultaneously starts its own hunt for Itachi.","Two hunts begin at once, and the season's engine starts."),
 (119,"Kakashi Chronicles: A Boy's Life on the Battlefield, Part 1","A flashback to the Third Great Ninja War, when Kakashi was a young jonin and Obito was his teammate. Kakashi's father's story is told.","Kakashi Gaiden is one of the best pieces of storytelling in the whole series."),
 (120,"Kakashi Chronicles: A Boy's Life on the Battlefield, Part 2","Obito's death and the origin of Kakashi's Sharingan. It reframes everything you know about Kakashi.","Essential. Do not skip these two episodes."),
 (121,"Assemble","Back in the present, Naruto, Sakura, Sai, Yamato and Kakashi prepare to move against Itachi.","Sets the pieces in place."),
 (122,"The Hunt","Both hunts converge. Sasuke's team and Konoha's team are chasing the same man for completely different reasons.","Good tension, well paced."),
 (123,"Clash!","The first real fights of the arc break out, and the Akatsuki's remaining members move.","Action picks up sharply here."),
 (124,"Art","Deidara faces Sasuke. Deidara's art-versus-genius conflict comes to a head.","Deidara's last fight, and he goes out his own way."),
 (125,"Disappearance","Deidara's final attack. Sasuke survives, barely, by a method that becomes important later.","A big, loud set-piece."),
 (126,"Twilight","The fallout. Tobi is revealed to be far more than he appears.","The first real hint about Tobi."),
 (127,"Tales of a Gutsy Ninja ~Jiraiya Ninja Scroll~ Part 1","Jiraiya's past is told, including how he met Tsunade and Orochimaru and what the Toad Sage told him about a child of prophecy.","Quietly one of the most important episodes in the series."),
 (128,"Tales of a Gutsy Ninja ~Jiraiya Ninja Scroll~ Part 2","The prophecy thread continues, and Jiraiya decides to chase the Akatsuki's leader himself.","Sets up the tragedy that follows."),
 (129,"Infiltrate! The Village Hidden in the Rain","Jiraiya infiltrates Amegakure alone and finds the organisation that runs it.","Tense, patient build-up."),
 (130,"The Man Who Became God","Jiraiya learns who Pain is, and the reveal connects back to his own past.","The reveal lands exactly as it should."),
 (131,"Honored Sage Mode!","Jiraiya enters Sage Mode and fights Pain for the first time.","The animation in this fight is a step up from everything before it."),
 (132,"In Attendance, the Six Paths of Pain","The six Paths of Pain are explained, and Jiraiya works out the truth about them.","The best-constructed fight of the arc."),
 (133,"The Tale of Jiraiya the Gallant","Jiraiya loses. He dies sending one final coded message back to Konoha.","Widely considered the best episode in all of Naruto Shippuden. It earns that."),
 (134,"Banquet Invitation","Itachi and Sasuke finally meet. Before the fight, Itachi does something unexpected with Naruto.","A short, strange episode that pays off much later."),
 (135,"The Longest Moment","The Sasuke versus Itachi fight begins - a battle fought almost entirely on genjutsu.","Slow on purpose, and the payoff justifies it."),
 (136,"The Light & Dark of the Mangekyo Sharingan","Itachi's Mangekyo abilities are laid out, including Tsukuyomi and Amaterasu.","The most technical fight in the series."),
 (137,"Amaterasu!","Sasuke breaks out of Tsukuyomi with sheer will, and Itachi's own techniques start to take a toll on him.","Sasuke's best moment in the arc."),
 (138,"The End","The fight ends. Itachi walks toward Sasuke, taps his forehead, and dies.","One of the most famous scenes in anime."),
 (139,"The Mystery of Tobi","Tobi reveals himself as 'Madara Uchiha' and tells Sasuke the story of the Uchiha clan.","The reveal that changes the entire series."),
 (140,"Fate","Sasuke learns the truth about Itachi, and it breaks him. He renames his team and changes his goal entirely.","The emotional core of the season."),
 (141,"Truth","Sasuke sets his sights on Konoha itself. The season's whole direction changes.","A hard turn that sets up everything after."),
 (142,"Battle of Unraikyo","The Eight-Tails and Killer B are introduced, and Sasuke's team is sent after him.","Introduces one of the best characters in the series."),
 (143,"The Eight Tails Vs. Sasuke","Sasuke fights Killer B and loses badly. His team barely escapes with their lives.","A great reality check - Sasuke is not as strong as he thinks."),
 (144,"Wanderer","Naruto is told about Jiraiya's death. He takes it badly, and Iruka and Shikamaru try to reach him.","A quiet, heavy episode."),
 (145,"Successor of the Forbidden Jutsu","A filler arc begins about a forbidden technique and the people fighting over it.","The tone shift is jarring after the Itachi arc."),
 (146,"The Successor's Wish","The filler arc continues, exploring the would-be successor of the technique.","Watchable, but skippable."),
 (147,"Rogue Ninja's Past","The backstory of the rogue ninja tied to the technique is told.","Character work is fine, the plot is thin."),
 (148,"Heir to Darkness","The antagonist's plan comes together and the arc moves toward its fights.","Standard filler pacing."),
 (149,"Separation","Alliances break apart and the characters are forced to choose sides.","The arc's better half."),
 (150,"The Forbidden Jutsu Released","The forbidden technique is used, and the arc reaches its climax.","A decent action finish."),
 (151,"Master and Student","The arc closes. Naruto returns to training and to the question of what he is fighting for.","A soft landing before the biggest arc in the series."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG2}" alt="Naruto Shippuden Part 5" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 5</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Seasons 6 and 7 - Episodes 113 to 151</strong>. It contains two of the most important stretches in the entire series: the <strong>Itachi Pursuit Mission</strong> and the <strong>Fated Battle Between Brothers</strong>, with the Kakashi Gaiden flashback tucked in the middle.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 113-151 (39 episodes)</li>
<li><strong>Season 6:</strong> Itachi Pursuit Mission + Kakashi Gaiden + Fated Battle Between Brothers - <strong>manga canon</strong></li>
<li><strong>Season 7:</strong> Six-Tails Unleashed - <strong>filler</strong></li>
<li><strong>Aired:</strong> 11 June 2009 - 11 March 2010</li>
<li><strong>Season 6 score:</strong> 10/10 &nbsp;·&nbsp; <strong>Season 7 score:</strong> 5/10</li>
</ul>

<p>Season 6 is the best season of Shippuden and it is not close. It contains Jiraiya's final mission, the Sasuke-Itachi fight, the Kakashi Gaiden flashback and the truth about Itachi - four of the biggest moments in the franchise, back to back. Season 7 is eight filler episodes that nobody needed. Watch 113 to 143, then skip to 152.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig("naruto-p5-1.webp", "Naruto Uzumaki - the series is about to change around him.")}

<h2>Part 5 verdict</h2>
<p>Episodes 129 to 141 are the peak of Naruto Shippuden. The Jiraiya infiltration and death, the Sasuke-Itachi fight, and the truth about Itachi form a run of episodes that most long-running anime never manage even once. Episode 133 in particular is the episode people point to when they argue Shippuden is better than the original series.</p>
<p>Episodes 144 to 151 are the opposite. The Six-Tails arc is filler, it arrives immediately after the biggest emotional moment in the show, and the tonal whiplash is severe. Skip it.</p>
<p><strong>Overall: 9/10.</strong> Essential viewing with a filler tail you can ignore.</p>

{fig("naruto-p5-2.webp", "Madara - the name that changes everything.")}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-shippuden-part-4-seasons-4-5.html">Part 4: Seasons 4-5 (Episodes 72-112)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", IMG2)
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = re.sub(r'</article><div class="related">.*?</div>', '', tpl[tpl.find("</article>"):], count=1, flags=re.S)
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("part 5 written")

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
