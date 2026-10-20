#!/usr/bin/env python3
"""Naruto Shippuden Part 2 - Season 2 (Episodes 33-53), + add series images to Part 1."""
import os, re

SLUG = "naruto-shippuden-part-2-season-2"
TITLE = "Naruto Shippuden Part 2: Season 2 (Episodes 33-53) - Every Episode Explained"
DESC = ("Episode-by-episode guide to Naruto Shippuden Season 2 - all 21 episodes of the Tenchi Bridge "
        "Reconnaissance arc, with a summary and review of each one.")
DATE = "20 October 2026"
READ = "13 min read"
CAT = "Anime"
PREV_SLUG = "naruto-shippuden-part-1-season-1"
PREV_LABEL = "Part 1: Season 1 (Episodes 1-32)"
NEXT_SLUG = "naruto-shippuden-part-3-season-3"
NEXT_LABEL = "Part 3: Season 3 (Episodes 54-71)"

IMG1, IMG2, IMG3 = "naruto-series-1.webp", "naruto-series-2.webp", "naruto-series-3.webp"

def fig(name, cap):
    return (f'<figure><img src="../assets/img/{name}" alt="{cap}" loading="lazy" decoding="async">'
            f'<figcaption>{cap}</figcaption></figure>')

EPS = [
 (33, "The New Target", "Sasori's dying words give Konoha its first real lead on Sasuke in years: an Akatsuki spy inside Orochimaru's organisation, with a meeting set at the Tenchi Bridge in ten days. Four days are already gone, so Naruto starts hunting for a fourth teammate.", "A quiet setup episode, but the clock it starts is the engine of the whole arc."),
 (34, "Formation! New Team Kakashi!", "Sai is forced onto the team as Danzo's condition. With Kakashi still in hospital, Tsunade assigns the ANBU operative Yamato as temporary captain. Naruto takes one look at Sai and decides he hates him.", "The new team is assembled in the least comfortable way possible. That tension is the point."),
 (35, "An Unnecessary Addition", "Yamato takes charge while Sai, who genuinely does not understand human feeling, insults both Naruto and Sakura. Jiraiya briefs Yamato on the Nine-Tails and the danger of Naruto losing control. The mission to intercept the spy begins.", "Sai is deliberately unlikeable here. It pays off much later."),
 (36, "The Fake Smile", "On the road, Naruto and Sakura snap at Sai for mocking Sasuke. Yamato uses Wood Style to build a cage and threatens to lock them in unless they learn to work together, then offers a night at a hot spring instead.", "Yamato's wood cage is a great visual gag with a real lesson behind it."),
 (37, "Untitled", "Sakura finds Sai drawing by a river and learns he is genuinely talented, but has never titled a single picture. The team changes route to avoid traps and camps in a house Yamato builds from wood, then plans how to capture the spy.", "The episode that first hints there is a person under Sai's blankness."),
 (38, "Simulation", "Yamato runs a mock version of the meeting to test how the team coordinates. Naruto is paired with Sai, it goes badly, and Sai later admits to Sakura that Root trained the emotion out of him.", "A training episode that quietly does character work. Better than it sounds."),
 (39, "The Tenchi Bridge", "Yamato disguises himself as Sasori inside the puppet Hiruko and meets the spy - who turns out to be Kabuto. Before the meeting can finish, Orochimaru arrives, sees through the disguise, and calls out the rest of the team.", "The reveal lands well, and Orochimaru's entrance resets the power level of the arc."),
 (40, "The Nine-Tails Unleashed", "Orochimaru taunts Naruto by comparing him to Sasuke, and the Nine-Tails chakra leaks out. Naruto climbs to a three-tailed cloak as Yamato remembers Jiraiya's warnings about how far this can go.", "The first real escalation of the arc, and it is genuinely tense."),
 (41, "The Top-Secret Mission Begins", "Naruto, now raging, throws Kabuto and accidentally takes Sakura out too. He wrecks the bridge and drags the fight into the forest. Sai flies off on an ink bird instead of catching the falling Sakura - and Naruto hits four tails.", "Sai's choice here tells you exactly what he is at this stage."),
 (42, "Orochimaru vs. Jinchuriki", "In his four-tailed form Naruto tears up the landscape. Almost nothing Orochimaru throws at him works, and he only survives because of his regeneration. Meanwhile Kabuto works out that Sasori is dead.", "One of the best fights in early Shippuden. The scale is a real step up."),
 (43, "Sakura's Tears", "Kabuto points out that this state exists because Naruto is desperate to bring Sasuke home. Sakura tries to reach him and gets hurt. Yamato pins Naruto down with chakra-suppressing wood and forces him back to normal.", "Sakura's reaction is the emotional centre of the arc."),
 (44, "The Secret of the Battle!", "Sakura's healing barely touches Naruto's wounds. Sai hands Orochimaru a letter from Danzo and leaves with him, tracked by Yamato's wood clone. The team recovers Sai's picture book, and Yamato starts to suspect Danzo's real aim.", "The arc turns from a fight into a mystery about who is actually loyal."),
 (45, "The Consequences of Betrayal", "Kabuto plants a fake corpse to slow the pursuit. The team presses on, but Sakura's injuries force a stop. Yamato tells Naruto the truth: it was Naruto himself, in that form, who hurt her.", "The hardest scene in the season for Naruto, and it is handled well."),
 (46, "The Unfinished Page", "Yamato warns Naruto not to lean on the Nine-Tails chakra when he is strong enough without it. The team studies Sai's book - a story of two boys whose meeting is left unfinished. In Orochimaru's hideout, Sai meets Sasuke.", "The picture book thread finally connects. Quietly devastating."),
 (47, "Infiltration: The Den of the Snake!", "Sasuke's Sharingan traps Sai in a genjutsu that genuinely frightens him. Sai tells Sasuke that Naruto thinks of him as a brother; Sasuke replies that he has only one brother, the one he intends to kill. The team tunnels into the hideout.", "Sasuke's answer is the coldest line of the season."),
 (48, "Bonds", "The team confronts Sai, who admits he was assigned both to help destroy Konoha and to spy on Orochimaru. Sakura gives him back his picture book and points out that he must feel something, or he would not keep it.", "Sai's turn begins here, and it is earned rather than sudden."),
 (49, "Something Important...", "Kabuto attacks and frees Sai, but Sai - wanting to understand the bond Naruto has with Sasuke - betrays Kabuto instead and helps capture him. The team splits up inside the hideout to search for Sasuke.", "Sai choosing a side is the payoff the arc has been building to."),
 (50, "The Picture Book's Story", "Naruto collapses from exhaustion. Sai realises what he always wanted to draw on the missing pages: himself and his brother, smiling. Orochimaru attacks, and Yamato finds Sai's bingo book - listing Sasuke as an assassination target.", "The reveal reframes Sai's entire assignment."),
 (51, "Reunion", "Yamato works out that Sai's real orders are to kill Sasuke. Sai finds Sasuke's room - but instead of carrying out the mission, he says he wants to protect Naruto and Sasuke's bond. Sasuke answers with an explosion that brings the whole team running.", "The reunion the arc promised, and it does not go the way anyone wanted."),
 (52, "The Power of Uchiha", "Naruto and Sakura finally stand in front of Sasuke again after two and a half years. It goes badly: Sasuke is faster, colder and far beyond them, and the gap between them has never been wider.", "The arc's thesis in one scene. Shippuden resets expectations here."),
 (53, "Title", "The team withdraws, having failed to bring Sasuke back. Naruto is left to face that failure, while Sakura tells him they will keep trying together. The arc closes on the picture book's missing page - and on Sai finally understanding something.", "A quiet, honest ending. Season 2 refuses to hand out a win."),
]

rows = []
for n, title, summ, note in EPS:
    rows.append(f'<h3>Episode {n}: {title}</h3>\n<p>{summ}</p>\n<p><em>Note:</em> {note}</p>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{IMG2}" alt="Naruto Shippuden Part 2" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>This is <strong>Part 2</strong> of the complete Naruto Shippuden episode-by-episode guide, covering <strong>Season 2: Episodes 33 to 53</strong> - the Tenchi Bridge Reconnaissance arc, where Shippuden introduces Sai and Yamato and then uses both of them to take the series apart.</p>

<p>Every episode below has a short summary of what happens and a note on how it holds up. For the arc-level overview, see the <a href="../articles/naruto-shippuden-complete-arc-guide.html">complete arc guide</a>.</p>

{fig(IMG1, "Naruto Uzumaki - the series returns to the Tenchi Bridge in Season 2.")}

<h2>Season 2 at a glance</h2>
<ul>
<li><strong>Episodes:</strong> 33-53</li>
<li><strong>Arc:</strong> Tenchi Bridge Reconnaissance Mission</li>
<li><strong>Type:</strong> Canon (no filler in this season)</li>
<li><strong>Aired:</strong> 8 November 2007 - 3 April 2008</li>
<li><strong>Season score:</strong> 8/10</li>
</ul>

<p>Season 2 is the awkward season, and deliberately so. It puts two strangers into Team 7 and spends most of its run asking whether the team can function at all. Then it ends with Sasuke casually proving that none of it was enough. It is a slower season than the first, but the character work on Sai is some of the best in the show.</p>

<h2>Every episode explained</h2>
{chr(10).join(rows)}

{fig(IMG3, "Kakashi Hatake - the team's usual captain sits this mission out.")}

<h2>Season 2 verdict</h2>
<p>This arc is a character study wearing the clothes of an action arc. Sai is the best thing in it: a boy trained to feel nothing, slowly noticing that he does. Yamato is a solid, steadying addition. And the Nine-Tails fight in the middle is one of the most memorable sequences in early Shippuden.</p>
<p>The weakness is pacing. A few episodes spin their wheels on the road to the bridge, and the middle section repeats the same team-tension beat more than once. It is also, by design, a season where the heroes lose.</p>
<p><strong>Season 2 score: 8/10.</strong> Not as tight as Season 1, but the payoff at the end is worth the slower start.</p>

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue the episode-by-episode guide with the next part.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Complete Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Shippuden: Complete Arc Guide (All 500 Episodes)</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li><li><a href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Anime: The Complete Watch List</a></li></ul></div></article>"""

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
print("part 2 written")

# ---- add the series images to Part 1 as well ----
p1 = "articles/naruto-shippuden-part-1-season-1.html"
s1 = open(p1, encoding="utf-8").read()
s1 = s1.replace(f'<img src="../assets/img/naruto-shippuden-part-1-season-1-cover.webp"',
                f'<img src="../assets/img/{IMG1}"')
anchor = '<h2>Every episode explained</h2>'
if anchor in s1 and IMG2 not in s1:
    s1 = s1.replace(anchor, fig(IMG2, "Naruto Shippuden - the series that follows Naruto after the timeskip.") + "\n" + anchor, 1)
anchor2 = '<h2>Season 1 verdict</h2>'
if anchor2 in s1 and IMG3 not in s1:
    s1 = s1.replace(anchor2, fig(IMG3, "Kakashi Hatake, captain of Team 7.") + "\n" + anchor2, 1)
open(p1, "w", encoding="utf-8").write(s1)
print("part 1 images added")

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
