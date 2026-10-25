#!/usr/bin/env python3
"""Blue Box Season 1 - complete episode guide (10,000+ words)."""
import os, re
from bb_s1_data_a import EPS_A
from bb_s1_data_b import EPS_B
EPS = EPS_A + EPS_B

SLUG = "blue-box-season-1-complete-episode-guide"
TITLE = "Blue Box Season 1: Complete Episode Guide (All 25 Episodes Explained)"
DESC = ("Every episode of Blue Box Season 1 explained - all 25 episodes of Ao no Hako, from the first "
        "morning at the gym to the finale, plus characters, staff, music and where to watch.")
DATE = "25 October 2026"
READ = "48 min read"
CAT = "Anime"
HERO = "bluebox-s1-keyart.webp"
IMGA = "bluebox-s1-a.webp"
IMGB = "bluebox-s1-b.webp"
NEXT_SLUG = "blue-box-season-2-complete-episode-guide"
NEXT_LABEL = "Blue Box Season 2: Complete Episode Guide"

def fig(name, cap, w=760):
    return (f'<figure style="max-width:{w}px;margin:34px auto">'
            f'<img src="../assets/img/{name}" alt="" loading="lazy" decoding="async">'
            f'<figcaption style="text-align:center">{cap}</figcaption></figure>')

rows = []
for n, en, jp, date, *paras in EPS:
    block = [f'<h3 id="ep{n}">Episode {n} &mdash; {en}</h3>',
             f'<p class="epmeta" style="color:#8a8aa3;font-size:13px;margin:-4px 0 12px">'
             f'<em>{jp}</em> &middot; {date}</p>']
    for p in paras:
        block.append(f'<p>{p}</p>')
    rows.append("\n".join(block))
    if n == 5:
        rows.append(fig("bluebox-s1-chinatsu.webp", "Blue Box Season 1 &mdash; the aquarium arc.", 640))
    if n == 12:
        rows.append(fig("bluebox-s1-trio.webp", "Taiki, Hina and Chinatsu &mdash; Season 1's central trio.", 660))
    if n == 18:
        rows.append(fig("bluebox-s1-manga.webp", "Blue Box &mdash; the manga by Kouji Miura.", 640))

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{HERO}" alt="Blue Box Season 1" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p><strong>Blue Box</strong> &mdash; known in Japan as <em>Ao no Hako</em> &mdash; is a romance and sports anime adapted from Kouji Miura's manga. Its first season ran for 25 episodes across two cours, airing from October 2024 to March 2025 on TBS and streaming worldwide on Netflix. This guide walks through <strong>every single episode of Season 1</strong> in order, with what happens, why it matters, and what the show is doing underneath.</p>

<p>If you have not started yet, a quick warning: this page is a full recap and contains <strong>spoilers for the entire first season</strong>.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 25 (two cours)</li>
<li><strong>Aired:</strong> 3 October 2024 &ndash; 27 March 2025</li>
<li><strong>Studio:</strong> Telecom Animation Film (planned and produced by TMS Entertainment)</li>
<li><strong>Director:</strong> Yuichiro Yano</li>
<li><strong>Streaming:</strong> Netflix, worldwide</li>
<li><strong>Source:</strong> Kouji Miura's <em>Blue Box</em> manga (Shueisha, Weekly Shonen Jump)</li>
<li><strong>Season 2:</strong> premiered 4 October 2026</li>
</ul>

<h2>What Blue Box is actually about</h2>
<p>On paper, the premise is a rom-com. Taiki Inomata is a first-year badminton player who gets to the gym early every morning to watch Chinatsu Kano, the second-year ace of the basketball team, practise alone. When Chinatsu's family has to move abroad, an old friendship between their mothers means she ends up staying in the Inomata house &mdash; the boy with a crush and the girl he is crushing on, sharing a hallway, hiding it from the entire school.</p>
<p>What makes Blue Box worth 25 episodes is that it refuses to treat that setup as a joke or a gimmick. The show is far more interested in what it feels like to be sixteen and quietly serious about something. Taiki is not chasing a fantasy; he is trying to become good enough to stand in the same room as the person who inspired him to work harder. Chinatsu is not a prize; she is a competitive athlete with a goal of her own and a very real fear of losing it. The living arrangement is the hook. The discipline is the story.</p>
<p>The result is a romance that moves slowly on purpose. Blue Box is a show about two people being careful with each other, and almost all of its best moments are small: a scarf, a bracelet, a note left in a notebook, a nickname learned by accident. If you are looking for a fast, dramatic confession, this is not that show. If you are looking for one of the most honest portrayals of first love in recent anime, it is exactly that show.</p>

<h2>Who is who</h2>
<p><strong>Taiki Inomata</strong> is the protagonist, a first-year badminton player with a stubborn streak and almost no self-pity. He is not naturally gifted. He is the kind of character who fixes things by doing them a thousand times, and the season is careful to show the cost of that &mdash; he trains until he is sick, he loses repeatedly, and he measures himself against people better than him without ever getting bitter about it.</p>
<p><strong>Chinatsu Kano</strong> is the second-year basketball ace and the emotional centre of the show. She is composed, capable and used to being depended on, which is exactly why the season spends so much time taking that composure apart. Chinatsu's arc is not about falling for Taiki; it is about admitting that she has, and working out what that costs a person who has organised her whole life around one goal.</p>
<p><strong>Hina Chono</strong> is a first-year gymnast, Taiki's friend and the third point of the triangle. She is the most transparently written character in the show and the one the series treats most gently. Hina's feelings arrive slowly, she understands them before Taiki does, and she never once tries to win by making anyone else lose. She is also carrying real pressure of her own in her sport, and Blue Box gives her that life rather than defining her entirely by her crush.</p>
<p><strong>Kyo Kasahara</strong> is Taiki's closest friend and the quiet engineer of the entire first season. He is the one who tells Taiki to keep the living situation secret, the one who arranges the aquarium outing, and the one who asks the questions nobody else will. He is the best-written supporting character in the show.</p>
<p><strong>Kengo Haryu</strong> is Taiki's badminton senior, a talented doubles player who spends the first few episodes seeming like a rival and turns out to be something much more useful: a mentor who teases Taiki mercilessly and then gives him genuinely good advice. His girlfriend <strong>Karen</strong> becomes important later in the season, and the two of them function as a portrait of what a relationship between two athletes actually looks like.</p>
<p><strong>Ayame Moriya</strong> is Hina's friend, a comic presence for most of the season who becomes an active agent in its final stretch, and <strong>Nagisa Funami</strong> is Chinatsu's basketball teammate. Together with Hina and Kyo they make up a supporting cast that feels like a real group of teenagers rather than a set of functions.</p>

<h2>Staff, studio and music</h2>
<p>The first season was directed by <strong>Yuichiro Yano</strong>, with <strong>Yuko Kakihara</strong> handling series composition and screenplay, and <strong>Miho Tanino</strong> serving as chief animation director and character designer. It was planned and produced by TMS Entertainment with animation production by Telecom Animation Film. The direction is one of the season's strengths: Blue Box is not a flashy show, and it does not try to be, but it has a very consistent eye for faces, for hands, and for the small physical details of two people being nervous around each other.</p>
<p>The music changes at the halfway mark, which gives each cours its own identity. The first cours opens with <strong>&ldquo;Same Blue&rdquo;</strong> by Official Hige Dandism and closes with <strong>&ldquo;Teenage Blue&rdquo;</strong> by Eve. The second cours swaps in <strong>&ldquo;Saraba&rdquo;</strong> by Macaroni Empitsu and <strong>&ldquo;Contrast&rdquo;</strong> by Tomoo. All four are good; the first-cours pair in particular has become strongly associated with the show.</p>

<h2>Season 1, episode by episode</h2>
<p>Below is the full guide, in order, from the first morning at the gym to the finale.</p>

{chr(10).join(rows)}

<h2>What Season 1 is really doing</h2>
<p>Blue Box is built on a single idea: that noticing someone is a form of work. Taiki starts training seriously because he watched Chinatsu keep practising after a failure, and Chinatsu starts paying attention to Taiki because he is visibly trying. The show never lets either of them be passive, and that is why the romance lands. Neither of them is waiting to be chosen. Both of them are trying to become the kind of person worth choosing, and the season is mostly about the gap between wanting that and achieving it.</p>
<p>The second idea is that being careful is not the same as being kind. Taiki spends most of the season hiding his feelings out of respect, and the show is honest that this is also a way of avoiding a conversation. Chinatsu spends most of the season deciding that her feelings are a complication to manage, and the show is honest that this is also a way of avoiding a decision. The finale works because both of them finally stop.</p>
<p>And the third idea, the one that separates Blue Box from most of its genre, is that the supporting characters get to have full lives. Hina's gymnastics, Karen and Haryu's relationship, Kyo's quiet competence, the basketball team's internal friction &mdash; none of it exists purely to serve the main couple. The season is generous with its cast, and that generosity is why the love triangle never becomes ugly.</p>

<h2>Five moments that define Season 1</h2>
<p><strong>1. The scarf.</strong> Early in episode one, Taiki gives Chinatsu his scarf on a cold morning and she responds by using his full name for the first time. It is a tiny exchange, and the show treats it as the foundation stone of everything that follows. Blue Box understands that in a real crush, the moments that matter are the ones that would look like nothing to anyone else.</p>
<p><strong>2. The bracelet.</strong> When Chinatsu learns Taiki has set himself the goal of reaching the nationals, she gives him a good-luck bracelet and shows him the matching one she wears. It is the first time the show says out loud what it has been implying: these two people have decided to carry each other, and neither of them has admitted it.</p>
<p><strong>3. The note in the notebook.</strong> After Taiki loses twice at the qualifiers, Chinatsu does not know what to say to him, so she finds his badminton notes and writes words of encouragement inside them. It is the single clearest expression of affection in the first cours, and it happens entirely without a conversation.</p>
<p><strong>4. Hina's request.</strong> When Hina asks Taiki to wish her luck before her qualifiers, she is asking for something small and getting something enormous. She goes on to take first place, and the show lets the audience understand what that support means to her without ever having her say it. It is the moment Hina stops being a supporting character.</p>
<p><strong>5. The finale.</strong> Taiki asks Chinatsu out. After twenty-four episodes of careful silences, notes, bracelets and near-misses, the show resolves its central tension with one honest sentence rather than a grand gesture, and it is exactly the right ending for this particular story.</p>

<h2>Common questions about Season 1</h2>
<p><strong>Is Blue Box a sports anime or a romance anime?</strong> Both, and it balances them better than most shows that attempt it. The badminton and basketball are not decoration; they are the language the characters use to talk to each other, and the matches carry real emotional weight. But the romance is the spine of the story.</p>
<p><strong>How many episodes is Season 1?</strong> Twenty-five, split into two cours. The first cours ran from October to December 2024, the second from January to March 2025.</p>
<p><strong>Do I need to read the manga first?</strong> No. The anime is a faithful and complete adaptation of the corresponding stretch of Kouji Miura's manga, and the first season works as a standalone introduction.</p>
<p><strong>Is there a Season 2?</strong> Yes. It was announced immediately after the Season 1 finale, premiered on 4 October 2026, and is airing weekly with twelve episodes planned.</p>

<h2>Where to watch Blue Box Season 1</h2>
<p>Blue Box streams worldwide on <strong>Netflix</strong>, which carries both cours of Season 1 and the currently airing Season 2. In Japan it aired on TBS and its affiliates. If you prefer physical media, Toho Animation released the season across six Blu-ray and DVD volumes in 2025.</p>

<h2>Season 1 verdict</h2>
<p><strong>Score: 9/10.</strong> Blue Box is one of the best romance anime of the decade, and the first season is a near-perfect introduction to it. The animation is understated and consistent, the writing trusts its audience, and the sports are treated with enough respect that the badminton and basketball matches actually carry emotional weight rather than functioning as filler between romantic beats.</p>
<p>Its only real flaw is pacing. The first cours moves deliberately, and viewers who want the relationship to progress faster will find the middle stretch slow. That patience is the point, though, and it pays off in the finale. If you stick with it, Season 1 rewards you with one of the most earned confessions in recent anime.</p>


<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Continue with Season 2, or read the short overview of both seasons.</p>
<div class="chips"><a class="chip" href="../articles/{NEXT_SLUG}.html">{NEXT_LABEL} &rarr;</a><a class="chip" href="../articles/blue-box-season-1-and-2-overview.html">Season 1 &amp; 2 Overview</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/blue-box-season-2-complete-episode-guide.html">Blue Box Season 2: Complete Episode Guide</a></li><li><a href="../articles/blue-box-season-1-and-2-overview.html">Blue Box Season 1 &amp; 2: A Short Overview</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html", f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", HERO)
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = re.sub(r'</article><div class="related">.*?</div>', '', tpl[tpl.find("</article>"):], count=1, flags=re.S)
open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)

CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{HERO}" alt="" loading="lazy" decoding="async"></div>'
        f'<span class="chip">{CAT}</span><h3><a href="articles/{SLUG}.html">{TITLE}</a></h3><p>{DESC}</p>'
        f'<div class="meta"><span>{DATE}</span><i></i><span>{READ}</span></div></div>')
for page in ["anime.html", "index.html"]:
    s = open(page, encoding="utf-8").read()
    if SLUG in s:
        continue
    m = re.search(r'<div class="cards[^"]*">', s)
    s = (s[:m.end()] + CARD + s[m.end():]) if m else (s[:s.find('<div class="card">')] + CARD + s[s.find('<div class="card">'):])
    open(page, "w", encoding="utf-8").write(s)

sm = open("sitemap.xml", encoding="utf-8").read()
url = f"https://blog.anipix.me/articles/{SLUG}.html"
if url not in sm:
    sm = sm.replace("</urlset>", f'  <url><loc>{url}</loc><lastmod>2026-10-25</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n</urlset>')
    open("sitemap.xml", "w", encoding="utf-8").write(sm)

import html as _h
txt = _h.unescape(re.sub(r'<[^>]+>', ' ', BODY))
print("S1 words:", len(txt.split()), "| eps:", BODY.count("<h3 id=\"ep"))
