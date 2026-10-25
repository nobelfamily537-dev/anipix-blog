#!/usr/bin/env python3
"""Blue Box Season 2 - guide to the currently airing season."""
import os, re, html as _h
from bb_s2_extra import EXTRA
from bb_s2_extra2 import EXTRA2
from bb_s2_extra3 import EXTRA3
from bb_s2_extra4 import EXTRA4
from bb_s2_extra5 import EXTRA5

SLUG = "blue-box-season-2-complete-episode-guide"
TITLE = "Blue Box Season 2: Complete Episode Guide (Airing Now, 2026)"
DESC = ("Everything about Blue Box Season 2 - the new studio, the new characters, the Winter Cup arc and "
        "an episode-by-episode guide to the season as it airs, updated through episode 4.")
DATE = "25 October 2026"
READ = "38 min read"
CAT = "Anime"
HERO = "bluebox-s2-banner.webp"
IMGA = "bluebox-s2-a.webp"
IMGB = "bluebox-s2-b.webp"
PREV_SLUG = "blue-box-season-1-complete-episode-guide"
PREV_LABEL = "Blue Box Season 1: Complete Episode Guide"

def fig(name, cap, w=760):
    return (f'<figure style="max-width:{w}px;margin:34px auto">'
            f'<img src="../assets/img/{name}" alt="" loading="lazy" decoding="async">'
            f'<figcaption style="text-align:center">{cap}</figcaption></figure>')

EPISODES = [
(1, "Déjà Vu", "デジャブ", "4 October 2026",
["Season 2 opens on an outing, and it opens deliberately quietly. Taiki and Chinatsu are at a sports shop together, and the show takes its time with how much that ordinary afternoon means to him. There is no crisis, no dramatic music, no confession hanging in the air. It is just two people who live in the same house choosing to spend a free day in the same place, and Taiki is visibly, almost painfully happy about how casual it is. After a full season of careful near-misses, the series is letting the audience feel how far these two have come simply by letting them be comfortable.",
"Then the outing gets a third wheel. At a cafe they run into Kazuma Matsuoka, a popular Eimei student and basketball player who has just returned from America. Matsuoka is confident, socially fluent and immediately interested in Chinatsu, and he slots himself into the conversation without being invited. Taiki is annoyed in the specific, teenage way of someone who cannot say why he is annoyed, and the show plays the awkwardness for exactly what it is rather than inflating it into a rivalry yet.",
"Matsuoka also does something much sharper than simply intruding. Privately, he tells Taiki that he has no real place pursuing anything romantic with Chinatsu given how far behind his badminton is. It is a cruel line, and the show is careful about how it lands: Matsuoka is not a cartoon villain, he is a confident athlete stating what he genuinely believes about the gap between them. It is the first time in the series that someone has said out loud what Taiki has been quietly afraid of since episode one, and it hits hard precisely because it is not entirely wrong.",
"The episode then makes a choice that defines the season's tone. Rather than fighting Matsuoka, Taiki encourages Chinatsu to go and watch a college basketball game with him, because it would be good experience for her. It is the most mature thing he has done in the entire series, and it costs him. Chinatsu goes, then comes back to him, having changed her mind, and the two of them end up watching the sunset from a rooftop deck.",
"That scene is the heart of the premiere. Chinatsu points out how much the outing resembles the first time they properly met, which is the show deliberately drawing a line between the beginning of Season 1 and the beginning of Season 2. Then she tells him something he has never known: she had already noticed him as a hardworking person before they ever spoke. For twenty-five episodes the audience has understood that Taiki noticed Chinatsu first. Here the series quietly reveals that it was mutual, and earlier than he realised.",
"Which is, of course, exactly when Taiki tries to confess. The moment builds, the show leans into it, and then it is interrupted by Chinatsu's former basketball teammate, Yumeka Kido. Yumeka does not merely walk in. She mocks Chinatsu for giving up basketball and the nationals to pursue romance, and the accusation lands like a slap. The season's central conflict arrives in its final seconds: not a rival for Taiki's affection, but a rival for Chinatsu's sense of who she is supposed to be."]),
(2, "Admiration", "憧れ", "11 October 2026",
["Yumeka leaves, and the episode spends its opening letting Taiki process what he just heard. He remembers Yumeka from middle school, where he saw her play with the basketball team, and the memory gives her a weight the audience did not have before. Whatever is going on between her and Chinatsu, it is not new, and it is not small. Taiki, being Taiki, responds to this by reassuring Chinatsu that she is capable of reaching the nationals. It is the right thing to say and the wrong thing to lead with, and the episode knows it.",
"The season then settles into its structure: both clubs begin training for the upcoming matches, including the Christmas training period, and Blue Box gives the badminton and basketball enough room that neither feels like a side plot. This is one of the things Season 2 does better than Season 1, and it is worth noting early. The first season often used the sports as a language for the romance. The second season is more willing to let the sports exist as sports, with their own pacing and their own stakes, and then let the romance happen inside them.",
"The episode's real work is Yumeka. Taiki learns from Haryu that Chinatsu holds a deep admiration for Yumeka, that the two of them were once long-time friends, and that the relationship mattered enormously to Chinatsu. Then he runs into Yumeka again, this time at a dental clinic, and the friction between them is immediately obvious. Yumeka tells him plainly that she hates Chinatsu, and that she became bored with basketball. The statement is so blunt that Taiki does not know what to do with it, and the show leaves him there, wondering what happened to a friendship that clearly meant something.",
"So he asks. During an evening walk, Taiki asks Chinatsu about her past with Yumeka, and the episode gives the audience the flashback the season has been building toward. Chinatsu explains that in elementary school she wanted to reach Yumeka's level, that Yumeka tutored her and helped her improve her form, and that this made their peers resentful. The two of them kept playing as a unit into middle school, until Yumeka quit, citing frustration that Chinatsu relied on her too much. It is a simple story and a devastating one: Chinatsu's entire competitive drive traces back to a person who eventually found that drive exhausting.",
"The episode closes on the confrontation the premiere promised. Taiki finds Yumeka playing basketball, and Yumeka insists there is no value in pouring yourself into a sport when you lose constantly. Taiki, who has spent the entire series losing and continuing anyway, tells her she wasted her talent because she was afraid of failing. It is the sharpest thing he has ever said to anyone, and it is not entirely fair. Yumeka slaps him and tells him he does not understand, and the show does not let him be right. It lets him be hurt, and it lets her be hurt, and it lets both of them be partly correct."]),
(3, "They're One and the Same", "1つのことだよ", "18 October 2026",
["The third episode opens with Yumeka blurting out something that cuts against everything she said the week before: if Chinatsu still aims for the nationals, she should not be faltering in practice. It is a strange, contradictory thing for someone who claims to hate Chinatsu to say, and Taiki notices. The show is beginning to reveal that Yumeka's hostility is not the whole picture, and it is doing it slowly, which is the right pace.",
"Back at school, Taiki watches Chinatsu practise with her team for the Winter Cup, and the episode gives us a complication that Season 1 only hinted at: Hina is still avoiding him. The two threads run alongside each other through the whole episode, and the show is careful not to let one swallow the other. Hina's distance is not a subplot here, it is a consequence, and it is treated with the seriousness it has earned.",
"Then the basketball team has a bad practice, and it is the best scene of the season so far. One of Chinatsu's teammates snaps at her out of stress, accusing her of forcing the rest of the team to adapt to her level of skill. It is unfair and it is also, from the teammate's side, understandable, and the show does not pick a winner. What matters is what it does to Chinatsu. The accusation lands directly on her oldest wound: she has been the person who works harder than everyone else since she was a child, and she has been reminded, again, of the cost of that. She remembers sacrificing rest for nonstop practice to catch up to Yumeka, and the pattern is suddenly visible to her.",
"So she asks Taiki something unexpected: what if she skipped practice? It is a question that sounds small and is enormous, because Chinatsu has never once considered it. Taiki is thrown by it, and the episode uses his reaction to show how much he has grown too. A year ago he would have panicked. Here he simply wonders, out loud, whether she has ever let herself consider it. It is the kind of conversation the show does better than almost anything else: two careful people admitting that the way they have been living might not be sustainable.",
"Meanwhile, the Taiki-Matsuoka tension escalates in a way that is very Blue Box. Both of them want an extra ticket to Chinatsu's Winter Cup game, and rather than settling it with a fight, they settle it with a shuttle run. The show plays the absurdity straight, and it works, because it is exactly what two competitive teenage athletes would do. Matsuoka uses the moment to dare Taiki to give up on pursuing Chinatsu, and Taiki does not answer, which is itself an answer.",
"The episode's closing scene belongs to Chinatsu and Yumeka, and it is the most important scene of the season so far. They meet again at the clinic, and Yumeka finally says the thing that explains her. She reveals that she secretly admired Chinatsu's determination, and that she was offended watching Chinatsu waste that determination by hanging out with Taiki. It is a confession dressed as an insult, and it reframes the entire conflict: Yumeka does not hate Chinatsu, she hates what she thinks Chinatsu has given up. Chinatsu does not accept the framing. She tells Yumeka plainly that Taiki has become her source of strength in reaching her goals. It is the first time she has said anything like that out loud to anyone, and the episode ends on it."]),
(4, "Love is the Most Powerful Feeling", "好きは最強の感情", "25 October 2026",
["The fourth episode aired on 25 October 2026, and it is the point at which this guide currently ends. Its title, &ldquo;Love is the Most Powerful Feeling&rdquo;, signals that the season is moving from setup into the emotional payoff of the Yumeka arc, following directly on from Chinatsu's declaration that Taiki is her source of strength. This section will be updated with a full recap once the episode has been widely seen, so that the guide stays accurate rather than speculative.",
"What can be said now is structural. The first three episodes did the work of establishing Season 2's two engines: Yumeka's resentment of Chinatsu, and Matsuoka's challenge to Taiki. Both are now in position, and both are pointed at the Winter Cup. Episode four is where the show typically starts converting that setup into consequence, and given the title, the smart money is on the Yumeka arc reaching its first real turning point."]),
]

rows = []
for n, en, jp, date, paras in EPISODES:
    rows.append(f'<h3 id="ep{n}">Episode {n} (Season 2, Episode {n}) &mdash; {en}</h3>')
    rows.append(f'<p class="epmeta" style="color:#8a8aa3;font-size:13px;margin:-4px 0 12px"><em>{jp}</em> &middot; {date}</p>')
    for p in paras:
        rows.append(f'<p>{p}</p>')
    if n == 1:
        rows.append(fig("bluebox-s2-netflix.webp", "Blue Box Season 2 is streaming now on Netflix.", 540))
    if n == 3:
        rows.append(fig("bluebox-s2-snowglobe.webp", "Blue Box Season 2 &mdash; the winter training arc."))

SCHEDULE = [
("1", "Déjà Vu", "4 October 2026", True), ("2", "Admiration", "11 October 2026", True),
("3", "They're One and the Same", "18 October 2026", True), ("4", "Love is the Most Powerful Feeling", "25 October 2026", True),
("5", "TBA", "1 November 2026", False), ("6", "TBA", "8 November 2026", False),
("7", "TBA", "15 November 2026", False), ("8", "TBA", "22 November 2026", False),
("9", "TBA", "29 November 2026", False), ("10", "TBA", "6 December 2026", False),
("11", "TBA", "13 December 2026", False), ("12", "TBA", "20 December 2026", False),
]
sched = "\n".join(
    f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{"Aired" if d else "Upcoming"}</td></tr>' for a, b, c, d in SCHEDULE)

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{HERO}" alt="Blue Box Season 2" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p><strong>Blue Box Season 2</strong> premiered on 4 October 2026 and is airing weekly. It picks up exactly where the first season left off, with twelve episodes planned, a new director at the helm and a brand-new studio behind the animation. This guide covers everything about the season: the production changes, the new characters, the arc it is adapting, and an episode-by-episode breakdown as it airs.</p>

<p>Because the season is still running, this page is written to stay accurate rather than speculative. Episodes are covered in full once they have aired, and upcoming episodes are listed by date only.</p>

<h2>At a glance</h2>
<ul>
<li><strong>Episodes:</strong> 12 (planned)</li>
<li><strong>Premiere:</strong> 4 October 2026</li>
<li><strong>Broadcast:</strong> TBS and 28 affiliated stations, Sundays at 16:30 JST</li>
<li><strong>Streaming:</strong> Netflix, worldwide, shortly after broadcast</li>
<li><strong>Director:</strong> Daisuke Sako (replacing Yuichiro Yano)</li>
<li><strong>Animation:</strong> Electric Circus (replacing Telecom Animation Film)</li>
<li><strong>Opening theme:</strong> &ldquo;Anata no Hana no Iro&rdquo; by Aiko</li>
<li><strong>Ending theme:</strong> &ldquo;Blue In&rdquo; by elsewhere kikou</li>
<li><strong>New cast:</strong> Yoshino Aoyama as Yumeka Kido</li>
</ul>

<h2>Where Season 2 picks up</h2>
<p>The first season ended with Taiki finally asking Chinatsu out, breaking a pattern of careful silences that had lasted twenty-five episodes. Season 2 does not reset that. It starts from the assumption that the two of them have acknowledged something, and it spends its opening episode showing how ordinary and how loaded that can feel at the same time. The outing at the sports shop, the cafe, the rooftop sunset &mdash; none of it is dramatic, and all of it matters, because the show is now writing from a different emotional starting point.</p>
<p>What Season 2 does with that is introduce two new pressures. The first is Kazuma Matsuoka, a confident basketball player back from America who tells Taiki plainly that he has no place pursuing Chinatsu. The second, and the bigger one, is Yumeka Kido: a former teammate and once-close friend of Chinatsu's who believes Chinatsu has thrown away her basketball career for a boy. Neither is a traditional love rival. Both are tests of whether the thing Taiki and Chinatsu built in Season 1 can survive contact with the outside world.</p>

<h2>New studio, new director: what changed</h2>
<p>The biggest behind-the-scenes change between seasons is the animation team. Season 1 was directed by <strong>Yuichiro Yano</strong> and animated by <strong>Telecom Animation Film</strong>, with Miho Tanino as chief animation director and character designer. Season 2 hands directing duties to <strong>Daisuke Sako</strong> and animation production to <strong>Electric Circus</strong>.</p>
<p>Studio changes in anime are always worth paying attention to, and this one is meaningful for two reasons. First, it is rare for a successful series to switch animation studios between seasons; the fact that it happened here means the production committee had a reason, and the most common one is scheduling. Season 1 aired in two consecutive cours and ended in March 2025, while Season 2 arrived in October 2026 &mdash; an eighteen-month gap. Second, Electric Circus is a younger studio, and a change of house almost always produces a visible shift in how a show moves.</p>
<p>What has not changed is the thing that mattered most. Miho Tanino remains as character designer and chief animation director, and the character work in the first three episodes is immediately recognisable as the same show. The faces, the small physical details of two people being nervous near each other, the restraint in the direction &mdash; all of it survives the studio change intact. If anything, Season 2 is slightly more confident in its framing, and the rooftop scene in episode one is composed with a stillness Season 1 rarely reached.</p>

<h2>Who is new in Season 2</h2>
<p><strong>Yumeka Kido</strong>, voiced by Yoshino Aoyama, is the most important addition to the cast. She is a former basketball teammate of Chinatsu's and, before that, her closest friend and the person she most wanted to catch up to. Yumeka is not written as a rival to be defeated. She is written as someone whose relationship with the sport collapsed, and who cannot stand watching someone she admires keep going. The season uses her to interrogate the thing Blue Box has always been about: what it costs to be the person who refuses to give up.</p>
<p><strong>Kazuma Matsuoka</strong> is the other new arrival, a popular Eimei student and basketball player who has returned from America. He is the season's most conventional source of tension and the show knows it, which is why it uses him primarily as a mirror rather than a threat. Matsuoka is what Taiki might look like if he were confident instead of stubborn, and the fact that he tells Taiki the truth about the gap in their abilities makes him more interesting than a simple antagonist would be.</p>

<h2>Music: the new opening and ending</h2>
<p>Season 2 opens with <strong>&ldquo;Anata no Hana no Iro&rdquo;</strong> by <strong>Aiko</strong>, and closes with <strong>&ldquo;Blue In&rdquo;</strong> by <strong>elsewhere kikou</strong>. The shift in musical identity is deliberate and matches the season's change of mood. Season 1's first cours used Official Hige Dandism and Eve, and its second cours moved to Macaroni Empitsu and Tomoo, so the show has always treated each block as its own chapter. Season 2's pair is warmer and slightly more wistful, which fits a story that has stopped being about whether two people will notice each other and started being about what happens next.</p>

<h2>Season 2 episode guide (as it airs)</h2>
<p>The guide below covers every episode that has aired. Upcoming episodes are listed by date in the schedule further down.</p>

{chr(10).join(rows)}

<h2>Season 2 release schedule</h2>
<p>Season 2 airs on Sundays. In India, episodes land at roughly <strong>1:00 PM IST</strong> on Netflix, shortly after the Japanese broadcast.</p>
<table style="width:100%;border-collapse:collapse;margin:18px 0;font-size:14.5px">
<thead><tr style="text-align:left;border-bottom:2px solid #e4e9f2"><th style="padding:9px 6px">Ep</th><th style="padding:9px 6px">Title</th><th style="padding:9px 6px">Date</th><th style="padding:9px 6px">Status</th></tr></thead>
<tbody>{sched}</tbody></table>
<p style="color:#8a8aa3;font-size:13px">Episode titles for 5&ndash;12 are not yet announced. Dates are the scheduled broadcast dates and can shift.</p>

<h2>What Season 2 is adapting</h2>
<p>Season 2 continues the adaptation of Kouji Miura's <em>Blue Box</em> manga, picking up from where the first season's twenty-five episodes ended. The arc it is built around is the one the first season spent its second half pointing at: the <strong>Winter Cup</strong>, and the return of Yumeka Kido into Chinatsu's life.</p>
<p>The Winter Cup matters because it is the first major tournament Chinatsu faces as a third-year, which means it is the last one she can realistically reach before graduating. Season 1 established that basketball is not a hobby for her; it is the thing she has organised her entire life around. Season 2 takes that established fact and puts pressure on it from two directions at once. The tournament itself raises the stakes of every practice. And Yumeka, who quit the sport, forces Chinatsu to defend her choice to keep going.</p>
<p>The Yumeka arc is the season's spine. What makes it work is that it is not a rivalry in the sports-anime sense. Yumeka is not better than Chinatsu, and the show is not interested in who would win a one-on-one. She is the person who showed Chinatsu what excellence looked like, and then walked away from it, and her hostility is really grief. Blue Box has always been strongest when it treats its characters' failures with respect, and this is the most sustained example of it in the series so far.</p>

{fig("bluebox-s2-manga.webp", "Blue Box &mdash; Kouji Miura's manga, which Season 2 continues to adapt.", 540)}

<h2>How Season 2 is different from Season 1</h2>
<p>The first season was about two people trying to become worthy of each other, and almost all of its tension was internal. Taiki hid his feelings out of respect. Chinatsu treated hers as a complication to be managed. The whole thing ran on careful silences and small gestures, and it worked because the show trusted the audience to read a scarf or a bracelet correctly.</p>
<p>Season 2 keeps that language but changes what it is pointed at. The conflict is no longer inside the two of them; it has moved outside. Matsuoka says the quiet part out loud. Yumeka attacks the premise of Chinatsu's life. Both of them force Taiki and Chinatsu to defend something they had never had to defend before, and the season is noticeably more willing to let them argue. It is a natural progression for a romance that has already crossed its first threshold, and it is the right one: a second season that simply repeated the first season's pattern would feel like stalling.</p>
<p>The sports have also been given more room. Season 1 often used badminton and basketball as a language for the romance. Season 2 is happier to let the matches exist on their own terms, and the Winter Cup setup gives the basketball side a genuine competitive structure to sit inside.</p>

{EXTRA}

{EXTRA2}

{EXTRA3}

{EXTRA4}

{EXTRA5}

<h2>Common questions</h2>
<p><strong>How many episodes will Season 2 have?</strong> Twelve are planned, which is roughly half the length of Season 1's twenty-five. If the series continues to adapt the manga, a third season would be the natural follow-up.</p>
<p><strong>Do I need to watch Season 1 first?</strong> Yes. Season 2 opens mid-relationship and assumes you know why the rooftop scene in episode one carries the weight it does. The full guide to Season 1 is linked at the end of this article.</p>
<p><strong>Is Season 2 on Netflix?</strong> Yes, worldwide, with episodes arriving shortly after the Japanese broadcast on Sundays.</p>
<p><strong>Is Blue Box Season 2 the final season?</strong> Not announced as such. The manga continues well past this point, so there is plenty of source material left.</p>

{fig(IMGB, "Yumeka Kido &mdash; the rival from Chinatsu's past who changes everything.")}

<h2>Season 2 verdict so far</h2>
<p><strong>Score so far: 8.5/10.</strong> Three episodes in, Season 2 has done the hardest thing a second season can do: it has changed the shape of the story without breaking it. The studio change is invisible where it matters, the new characters are genuinely interesting rather than obstacles, and the Yumeka arc is the most emotionally sophisticated material Blue Box has attempted.</p>
<p>The one thing to watch is pacing. Twelve episodes is a tight runway for the Winter Cup, the Yumeka arc and the Matsuoka thread, and there is a real risk that the season has to rush one of them. So far it has managed its time well. This page will be updated as the season continues.</p>

{fig(IMGA, "Blue Box Season 2 &mdash; airing now on TBS and Netflix.")}

<div class="next" style="margin-top:34px"><h3>Read next</h3>
<p style="color:#8a8aa3;font-size:15px;margin:0 0 14px">Catch up on Season 1, or read the short overview of both seasons.</p>
<div class="chips"><a class="chip" href="../articles/{PREV_SLUG}.html">&larr; {PREV_LABEL}</a><a class="chip" href="../articles/blue-box-season-1-and-2-overview.html">Season 1 &amp; 2 Overview</a><a class="chip" href="../articles/naruto-shippuden-complete-arc-guide.html">Naruto Arc Guide</a></div></div>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/blue-box-season-1-complete-episode-guide.html">Blue Box Season 1: Complete Episode Guide (All 25 Episodes)</a></li><li><a href="../articles/blue-box-season-1-and-2-overview.html">Blue Box Season 1 &amp; 2: A Short Overview</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

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
    sm = sm.replace("</urlset>", f'  <url><loc>{url}</loc><lastmod>2026-10-25</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n</urlset>')
    open("sitemap.xml", "w", encoding="utf-8").write(sm)

txt = _h.unescape(re.sub(r'<[^>]+>', ' ', BODY))
print("S2 words:", len(txt.split()), "| eps:", BODY.count('<h3 id="ep'))
