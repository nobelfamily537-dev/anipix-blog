#!/usr/bin/env python3
"""The Detective Is Already Dead - Season 1 and Season 2 posts."""
import os, re, html as _h

TPL = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
TPL_TITLE = "Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog"
TPL_DESC = ("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale "
            "and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.")

def fig(name, cap, w=760):
    return (f'<figure style="max-width:{w}px;margin:34px auto">'
            f'<img src="../assets/img/{name}" alt="" loading="lazy" decoding="async">'
            f'<figcaption style="text-align:center">{cap}</figcaption></figure>')

def ep(n, title, date, body, img=None):
    s = [f'<h3 id="ep{n}">Episode {n} &mdash; {title}</h3>',
         f'<p class="epmeta" style="color:#8a8aa3;font-size:13px;margin:-4px 0 12px">{date}</p>']
    for p in body:
        s.append(f'<p>{p}</p>')
    if img:
        s.append(fig(*img))
    return "\n".join(s)

def build(slug, title, desc, date, read, hero, body_html, cards_pages=("anime.html","index.html")):
    head = TPL[:TPL.find("<body")]
    head = head.replace(TPL_TITLE, title).replace(TPL_DESC, desc)
    head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html",
                        f"https://blog.anipix.me/articles/{slug}.html")
    head = head.replace("fall-2026-anime-watch-list-cover.webp", hero)
    shell = TPL[TPL.find('<header class="site">'):TPL.find('<article class="post">')]
    shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
    tail = re.sub(r'</article><div class="related">.*?</div>', '',
                  TPL[TPL.find("</article>"):], count=1, flags=re.S)
    out = head + shell + body_html + tail
    open(f"articles/{slug}.html", "w", encoding="utf-8").write(out)

    CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{hero}" alt="" loading="lazy" decoding="async"></div>'
            f'<span class="chip">Anime</span><h3><a href="articles/{slug}.html">{title}</a></h3><p>{desc}</p>'
            f'<div class="meta"><span>{date}</span><i></i><span>{read}</span></div></div>')
    for page in cards_pages:
        s = open(page, encoding="utf-8").read()
        if slug in s:
            continue
        m = re.search(r'<div class="cards[^"]*">', s)
        s = (s[:m.end()] + CARD + s[m.end():]) if m else (s[:s.find('<div class="card">')] + CARD + s[s.find('<div class="card">'):])
        open(page, "w", encoding="utf-8").write(s)

    sm = open("sitemap.xml", encoding="utf-8").read()
    url = f"https://blog.anipix.me/articles/{slug}.html"
    if url not in sm:
        sm = sm.replace("</urlset>", f'  <url><loc>{url}</loc><lastmod>2026-11-05</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n</urlset>')
        open("sitemap.xml", "w", encoding="utf-8").write(sm)
    txt = _h.unescape(re.sub(r'<[^>]+>', ' ', body_html))
    print(f"{slug}: {len(txt.split())} words")

# ============================ SEASON 1 ============================
S1 = "detective-is-already-dead-season-1-guide"
S1_T = "The Detective Is Already Dead Season 1: Complete Guide and Review (All 12 Episodes)"
S1_D = ("Every episode of The Detective Is Already Dead Season 1 explained &mdash; Siesta, Kimihiko, "
        "the case that started it all, and why the 2021 anime divided its audience.")
S1_HERO = "detective-plane.webp"

EPS1 = [
 (1, "Attention Passengers: Is There a Detective on Board? / Commence Adolescent Romantic Comedy", "4 July 2021 &middot; double-length premiere",
  ["Kimihiko Kimizuka has one talent and it is a bad one: he is a magnet for trouble. On a flight ten thousand metres above the ground the plane is hijacked, and instead of hiding he ends up in the middle of it.",
   "That is where he meets <strong>Siesta</strong>, a silver-haired girl a year younger than him who introduces herself as a great detective and asks him a question that changes his life: will he be her assistant?",
   "The premiere ran at roughly double length because it has two jobs to do. The first is the hijacking itself, a contained action set piece. The second is to establish the show's real shape, which is not a mystery series at all but a story about the aftermath of one."],
  ("detective-roses.webp", "Siesta &mdash; the great detective whose story the whole series is built around.")),
 (2, "I Still Remember, After All This Time", "11 July 2021",
  ["The three years between the hijacking and the present are compressed into one episode, and it is the most important episode of the season.",
   "Kimihiko and Siesta travel the world taking on cases, chasing an organisation they call the world's enemy, and slowly becoming the kind of partners who finish each other's sentences.",
   "Then Siesta dies. The show does not soften it, and it does not undo it. Everything after this episode is Kimihiko trying to live in a world where the person who gave his life a shape is not in it."], None),
 (3, "That's Yui-nya Quality", "18 July 2021",
  ["A year after Siesta's death Kimihiko is drifting through school when a client finds him: <strong>Yui Saikawa</strong>, a wildly popular idol who is convinced someone is going to kill her.",
   "The episode is the show's lightest, and deliberately so. After the funeral it needs to prove it can still be funny, and Yui's energy does most of that work."],
  ("detective-sakura.webp", "Yui Saikawa's arc gives Season 1 its comedy before the darker second half.")),
 (4, "What I See in That Eye", "25 July 2021",
  ["The Saikawa case turns serious. What looked like a stalker turns out to be something organised, and Kimihiko's habit of walking into danger pays off badly.",
   "This is where the show starts dropping the pieces it will need later: the people behind the threat are connected to the same organisation Siesta spent three years fighting."], None),
 (5, "That Was Directed at One Year in the Future", "1 August 2021",
  ["A request arrives that seems to be aimed a year ahead rather than at the present, and it forces Kimihiko to think about what he is actually doing with his life now that he is not an assistant any more.",
   "The episode is the hinge of the season. Everything before it is Kimihiko reacting, and everything after it is Kimihiko choosing."], None),
 (6, "Crimson Devil, Ice Queen", "8 August 2021",
  ["<strong>Charlotte Arisaka Anderson</strong> arrives, and she is not friendly. A young operative with a very direct way of solving problems, she treats Kimihiko as either a suspect or an obstacle depending on the minute.",
   "Her introduction doubles the cast and finally gives the show someone who can trade blows with Kimihiko's passivity. She also brings the first real information about what Siesta was actually up against."], None),
 (7, "In Time, You Will Recall This Day", "15 August 2021",
  ["The middle episode does the quiet work: memory, grief, and the question the title asks, which is whether the past is something you remember or something that happens to you again.",
   "It is the episode most likely to divide viewers. Those who came for a mystery find it slow; those who stayed for the characters find it the most honest episode in the run."], None),
 (8, "With That, We Set Out on a Journey Once Again", "22 August 2021",
  ["<strong>Nagisa Natsunagi</strong> hires Kimihiko, and the show restarts itself. She is a client, then a partner, and then something more complicated, because Nagisa is alive only because she received Siesta's heart.",
   "The episode is the season's second pilot. It re-establishes the assistant-and-detective structure with a different detective, and it asks whether Kimihiko is helping Nagisa or just trying to get Siesta back."], None),
 (9, "SPES", "29 August 2021",
  ["The organisation finally has a name: <strong>SPES</strong>. The scattered threats of the first half stop looking like coincidence.",
   "Naming the enemy changes the show's tone. What was a character drama with cases attached becomes a conspiracy story, and the final stretch is built on that."], None),
 (10, "So I Can't Become a Detective", "5 September 2021",
  ["Kimihiko confronts the thing he has been avoiding since episode two: he is not Siesta, he will never be Siesta, and pretending otherwise is not a tribute to her.",
   "The title is his answer to the question the whole series keeps asking him. It is also the moment the show stops being about a dead detective and starts being about the people she left behind."],
  ("detective-night.webp", "Season 1 moves from grief into a conspiracy in its final stretch.")),
 (11, "A Light in the Midst of Hope", "12 September 2021",
  ["The penultimate episode gathers everyone &mdash; Nagisa, Yui, Charlotte, Fuubi Kase and the rest &mdash; for the confrontation the season has been building towards.",
   "It also starts answering the question the premise has been dangling since the first minute: what was Siesta actually doing in those three years, and what did it cost?"], None),
 (12, "Those Dizzying Three Years I Spent with You", "19 September 2021",
  ["The finale is a goodbye, not a victory. The conspiracy is addressed, but the emotional work is Kimihiko finally accepting that the three years were real, that they are over, and that he is allowed to keep going.",
   "It ends on a note that satisfied some viewers and frustrated others, and the split says a lot about what the season was trying to do."],
  ("detective-duo.webp", "Kimihiko and Siesta &mdash; the partnership the series is named after.")),
]

s1_body = f"""<article class="post"><h1>{S1_T}</h1>
<div class="post-meta"><span class="chip">Anime</span><span>5 November 2026</span><i></i><span>14 min read</span></div>
<div class="posthero"><img src="../assets/img/{S1_HERO}" alt="The Detective Is Already Dead Season 1" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> 5 November 2026</p>

<p><strong>The Detective Is Already Dead</strong> &mdash; <em>Tantei wa Mou, Shindeiru.</em>, usually shortened to <em>Tanmoshi</em> &mdash; is one of the strangest premises a light novel adaptation has been given in years. The title is not a hook. It is a spoiler the story tells you on purpose, in the first episode, and then spends twelve episodes dealing with.</p>

<p>This guide walks through <strong>all 12 episodes of Season 1</strong> with titles and air dates, explains what the show is actually doing, and is honest about where it stumbles. Full spoilers for the entire season below.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 12</li>
<li><strong>Aired:</strong> 4 July &ndash; 19 September 2021 (Summer 2021)</li>
<li><strong>Studio:</strong> ENGI</li>
<li><strong>Director:</strong> Manabu Kurihara</li>
<li><strong>Series composition:</strong> Deko Akao</li>
<li><strong>Character design:</strong> Y&#333;suke It&#333;</li>
<li><strong>Source:</strong> Nigoj&#363;'s light novels, art by Umib&#333;zu (MF Bunko J / Kadokawa)</li>
<li><strong>Streaming:</strong> Crunchyroll (Funimation held it originally)</li>
<li><strong>Season 2:</strong> premiered 7 October 2026, 13 episodes</li>
</ul>

<h2>What the show actually is</h2>
<p>The pitch sounds like a detective series. It is not. There is almost no mystery for the audience to solve, and the cases are rarely the point.</p>

<p>What <em>Tanmoshi</em> actually is, is a story about grief told through the structure of a detective show. Kimihiko Kimizuka spent three years as the assistant to a girl who called herself the world's greatest detective. She died. The series opens after that, and every case he takes is really him trying to work out what he is supposed to be now.</p>

<p>The framing device matters. Because Siesta is dead before the story starts, she can only appear in flashback, in memory, and in the ways other people carry her. The show is unusually disciplined about this, and it is the reason the premise works at all.</p>

<h2>The main characters</h2>
<p><strong>Kimihiko Kimizuka</strong> is the narrator and the assistant. His defining trait is a talent for being in the wrong place at the wrong time, which the show treats as both a joke and a curse.</p>

<p><strong>Siesta</strong> is the detective. Silver hair, blue eyes, absolute confidence, and a habit of being right about everything except the cost to the people around her.</p>

<p><strong>Nagisa Natsunagi</strong> is the client who becomes a partner. She is alive because she received Siesta's heart, which is the kind of detail this series throws at you casually and then builds an entire season on.</p>

<p><strong>Yui Saikawa</strong> is the idol with a death threat and the show's comic engine. <strong>Charlotte Arisaka Anderson</strong> is the operative who arrives to make everything more dangerous. <strong>Fuubi Kase</strong> is the adult who knows more than she says.</p>

{fig("detective-trio.webp","The central trio &mdash; and the mirror that keeps appearing between them.",700)}

<h2>Episode guide</h2>
<p>All twelve episodes, in order, with the original air dates.</p>

{"".join(ep(*e) for e in EPS1)}

{fig("detective-wedding.webp","The image the finale leaves you with &mdash; and the one the whole season was building towards.",700)}

<h2>The music</h2>
<p>The opening theme is <strong>&ldquo;Koko de Ikiteru.&rdquo;</strong> (ここで生きてる。) by MARY &times; jon-YAKITORY. The ending theme is <strong>&ldquo;Kod&#333;&rdquo;</strong> (鼓動, &ldquo;Heartbeat&rdquo;) by Nana Kagura, written and arranged by 40mP.</p>

<p>There is a detail worth knowing: the first and final episodes both use &ldquo;Koko de Ikiteru.&rdquo; as the ending song instead of &ldquo;Kod&#333;&rdquo;. Bookending the season with the same track is not an accident &mdash; it is the show telling you the story has closed a loop.</p>

<h2>Where it stumbles</h2>
<p>Season 1 adapts roughly four light novel volumes into twelve episodes, and it shows. The first half moves quickly enough to feel rushed, then the middle slows down for material that did not need a full episode.</p>

<p>The bigger problem is that the anime front-loads the emotional payoff. Siesta dies in episode two, so the audience is asked to grieve a character they have known for about forty minutes. The light novels earn that over a much longer stretch. The anime asks you to take it on trust, and not every viewer was willing.</p>

<p>Action scenes are the other weak point. ENGI's production is competent rather than impressive, and several confrontations in the final third land flatter than the script deserves.</p>

<h2>Why it is still worth watching</h2>
<p>Because when it works, it works on a level most anime do not attempt. Episode 10, in which Kimihiko finally admits he cannot become the person Siesta was, is a better piece of character writing than the show has any right to deliver.</p>

<p>The premise also pays off in a way that rewards patience. The title is a promise, and by the finale the show has actually kept it: the detective is dead, she stays dead, and the story is about what the living do next. Very few series have the nerve to follow through on that.</p>

<h2>Where to watch</h2>
<p>Season 1 streams on <strong>Crunchyroll</strong>. It was originally licensed by Funimation, and the Crunchyroll listing is the current home for it in most regions.</p>

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Season 2 is airing right now. Here is the full episode list and weekly schedule.</p>
<div class="chips"><a class="chip" href="../articles/detective-is-already-dead-season-2-guide.html">Season 2 Guide &amp; Schedule &rarr;</a><a class="chip" href="../articles/blue-box-season-1-complete-episode-guide.html">Blue Box Season 1 Guide</a><a class="chip" href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Watch List</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/detective-is-already-dead-season-2-guide.html">The Detective Is Already Dead Season 2: Episode Guide and Schedule</a></li><li><a href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Anime: The Complete Watch List</a></li><li><a href="../articles/blue-box-season-1-complete-episode-guide.html">Blue Box Season 1: Complete Episode Guide</a></li></ul></div></article>"""

build(S1, S1_T, S1_D, "5 November 2026", "14 min read", S1_HERO, s1_body)

# ============================ SEASON 2 ============================
S2 = "detective-is-already-dead-season-2-guide"
S2_T = "The Detective Is Already Dead Season 2: Episode Guide, Schedule and Review (2026)"
S2_D = ("Season 2 is airing now. Full episode list, weekly release schedule, new cast, the official "
        "story setup and where to watch The Detective Is Already Dead Season 2.")
S2_HERO = "detective-s2-key.webp"

EPS2 = [
 (1, "To See You Once More", "7 October 2026 &middot; premiere", None),
 (2, "A Story of That Day That No One Knows", "14 October 2026", None),
 (3, "An Easy Way to Support Your Favorite By Being an Idol Producer", "21 October 2026", None),
 (4, "Episode 4", "28 October 2026 &middot; title not yet listed", None),
 (5, "Episode 5", "4 November 2026 &middot; title not yet listed", None),
]

s2_eps = []
for n, t, d, _ in EPS2:
    s2_eps.append(f'<tr><td style="padding:8px 10px;border-bottom:1px solid #2a2a3d">{n}</td>'
                  f'<td style="padding:8px 10px;border-bottom:1px solid #2a2a3d">{t}</td>'
                  f'<td style="padding:8px 10px;border-bottom:1px solid #2a2a3d">{d}</td></tr>')
for n in range(6, 14):
    from datetime import date, timedelta
    dt = date(2026, 11, 4) + timedelta(days=7 * (n - 5))
    s2_eps.append(f'<tr><td style="padding:8px 10px;border-bottom:1px solid #2a2a3d">{n}</td>'
                  f'<td style="padding:8px 10px;border-bottom:1px solid #2a2a3d">To be announced</td>'
                  f'<td style="padding:8px 10px;border-bottom:1px solid #2a2a3d">{dt.day} {dt.strftime("%B %Y")} (scheduled)</td></tr>')

s2_body = f"""<article class="post"><h1>{S2_T}</h1>
<div class="post-meta"><span class="chip">Anime</span><span>5 November 2026</span><i></i><span>12 min read</span></div>
<div class="posthero"><img src="../assets/img/{S2_HERO}" alt="The Detective Is Already Dead Season 2 key visual" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> 5 November 2026</p>

<p>Five years after the first season ended on a note that split its audience down the middle, <strong>The Detective Is Already Dead Season 2</strong> is airing. It started on 7 October 2026, it runs for 13 episodes, and it is the season that finally has to answer the question Season 1 only asked.</p>

<p>This page keeps the episode list, the weekly schedule, the cast and the story setup in one place, and updates as the season goes.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 13</li>
<li><strong>Premiere:</strong> 7 October 2026</li>
<li><strong>Season:</strong> Fall 2026, airing now</li>
<li><strong>Studio:</strong> ENGI</li>
<li><strong>Director:</strong> Manabu Kurihara (returning)</li>
<li><strong>Series composition:</strong> Deko Akao (returning)</li>
<li><strong>Character design:</strong> Y&#333;suke It&#333; (returning)</li>
<li><strong>Music:</strong> 40mP and Yuuyu</li>
<li><strong>Broadcast:</strong> TOKYO MX, BS Nippon TV, AT-X (Japan)</li>
<li><strong>Streaming:</strong> Crunchyroll (worldwide, simulcast)</li>
<li><strong>Source:</strong> Nigoj&#363;'s light novels, art by Umib&#333;zu</li>
</ul>

<h2>Where Season 1 left things</h2>
<p>If you have not watched Season 1, this is the short version. Kimihiko Kimizuka was recruited as the assistant to Siesta, a self-described great detective, during a plane hijacking. They spent three years travelling the world together before she was killed. A year later Kimihiko met Nagisa Natsunagi, a girl alive because she had received Siesta's heart, and the two of them began working together.</p>

<p>By the end of Season 1 the surface story was resolved and the emotional one was not. Kimihiko had accepted that he could not become Siesta, and the show had confirmed that she was staying dead. What it had not done was explain why she died.</p>

{fig("detective-plane.webp","Where it started: the flight that made Kimihiko an assistant.",760)}

<h2>What Season 2 is adapting</h2>
<p>The official story setup for Season 2 picks up exactly there. Having reached the truth of the great detective's death, Kimihiko and the people around him learn something harder: that a detective described as flawless made a mistake, and what inheriting her dying wish actually means.</p>

<p>The tagline the season is running with translates roughly as <em>&ldquo;And so, that dying wish will never die.&rdquo;</em> That is a much more forward-looking promise than Season 1's premise, which was entirely about something that had already happened.</p>

<p>The official synopsis ends with a line worth quoting: the detective is already dead, the truth of her death has been revealed, <em>but it is still too early for the epilogue.</em> That is the season's whole thesis in one sentence.</p>

{fig("detective-roses.webp","Siesta remains the centre of the story even when she is not in the scene.",680)}

<h2>Episode list and schedule</h2>
<p>New episodes land weekly on Wednesdays. Episode 5 aired on 4 November 2026.</p>

<table style="width:100%;border-collapse:collapse;margin:24px 0;font-size:14.5px">
<thead><tr>
<th style="text-align:left;padding:8px 10px;border-bottom:1px solid #3a3a52">#</th>
<th style="text-align:left;padding:8px 10px;border-bottom:1px solid #3a3a52">Title</th>
<th style="text-align:left;padding:8px 10px;border-bottom:1px solid #3a3a52">Date</th>
</tr></thead>
<tbody>{"".join(s2_eps)}</tbody></table>

<p>At 13 episodes running weekly from 7 October, the season is scheduled to finish at the end of December 2026. Titles for episodes four onwards had not been published at the time of writing, so this table fills them in as they appear.</p>

<h2>Cast</h2>
<p>The core cast returns. <strong>Arata Nagai</strong> as Kimihiko Kimizuka, <strong>Saki Miyashita</strong> as Siesta, <strong>Ayana Taketatsu</strong> as Nagisa Natsunagi, <strong>Kanon Takao</strong> as Yui Saikawa, <strong>Saho Shirasu</strong> as Charlotte Arisaka Anderson and <strong>Mai Fuchigami</strong> as Fuubi Kase.</p>

<p>Season 2 adds a group of characters the first season only gestured at: <strong>Hel</strong> (Yumiri Hanamori), <strong>Alicia</strong> (Maria Naganawa), <strong>Noches</strong> (Saki Miyashita), <strong>Mia Whitlock</strong> (Akari Komiyama) and <strong>Scarlett</strong> (Nobuhiko Okamoto). If the light novels are any guide, these are not side characters &mdash; the back half of the season depends on them.</p>

{fig("detective-trio.webp","Siesta, Nagisa and Kimihiko &mdash; the three the story keeps circling.",700)}

{fig("detective-duo.webp","Kimihiko and Siesta. Season 2 is the first time the show has to work without her in the present tense.",700)}

<h2>Staff and music</h2>
<p>Continuity is the headline here. Manabu Kurihara returns to direct, Deko Akao returns for series composition, and Y&#333;suke It&#333; returns for character design, all at ENGI. For a show whose first season was criticised for uneven production, keeping the same team is either reassuring or worrying depending on which side of that argument you were on.</p>

<p>The music is where it changes. <strong>40mP</strong> and <strong>Yuuyu</strong> handle the score, and they also wrote, composed and arranged both theme songs. The opening is <strong>&ldquo;Kono Shinzou ni Hanataba o&rdquo;</strong> (この心臓に花束を, roughly &ldquo;a bouquet for this heart&rdquo;) by <strong>Koume</strong>. The ending is <strong>&ldquo;Hakuch&#363;mu&rdquo;</strong> (白昼夢, &ldquo;daydream&rdquo;) by <strong>Nana Kagura</strong>, who sang the first season's ending too.</p>

<p>That opening title is not subtle. &ldquo;A bouquet for this heart&rdquo; is a direct reference to the fact that Nagisa is walking around with Siesta's heart in her chest, which tells you what the season is going to be about before a single frame plays.</p>

<h2>What to expect</h2>
<p>Season 1 was a story about grief with a detective show wrapped around it. Season 2 looks like it is flipping that: the conspiracy and the organisation called SPES move to the front, and the character work has to happen inside a plot that is now running.</p>

<p>Whether that is an improvement depends on what you wanted. Viewers who found the first season too slow and too sad should find this one more eventful. Viewers who loved it precisely because it was slow and sad may find the shift jarring.</p>

{fig("detective-night.webp","Season 2 pushes the SPES storyline into the foreground.",700)}

<h2>Where to watch</h2>
<p><strong>Crunchyroll</strong> streams Season 2 as it airs, simulcast with Japan. In Japan it broadcasts on TOKYO MX on Wednesdays at 22:30, on BS Nippon TV at 24:30, and on AT-X at 21:30, with d Anime Store handling the earliest streaming.</p>

<p>Season 1 is also on Crunchyroll, so the whole thing is available in one place.</p>

{fig("detective-sakura.webp","Siesta, as the series most often remembers her.",680)}

{fig("detective-wedding.webp","The image Season 1's finale leaves you with &mdash; Season 2 keeps returning to it.",700)}

<div class="next" style="margin-top:34px"><h3>Next in this series</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Catching up first? Here is the complete Season 1 guide.</p>
<div class="chips"><a class="chip" href="../articles/detective-is-already-dead-season-1-guide.html">Season 1 Complete Guide &rarr;</a><a class="chip" href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Watch List</a><a class="chip" href="../articles/blue-box-season-2-complete-episode-guide.html">Blue Box Season 2 Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/detective-is-already-dead-season-1-guide.html">The Detective Is Already Dead Season 1: Complete Guide</a></li><li><a href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Anime: The Complete Watch List</a></li><li><a href="../articles/blue-box-season-2-complete-episode-guide.html">Blue Box Season 2: Complete Episode Guide</a></li></ul></div></article>"""

build(S2, S2_T, S2_D, "5 November 2026", "12 min read", S2_HERO, s2_body)
print("done")
