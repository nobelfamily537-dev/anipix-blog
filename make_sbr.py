#!/usr/bin/env python3
import re, html as H
TPL = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
TPL_TITLE = "Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog"
TPL_DESC = ("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale "
            "and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.")
SLUG="steel-ball-run-fall-2026-week-6-rankings"
TITLE="Steel Ball Run Is Topping Every Chart: Fall 2026 Week 6 Rankings Explained"
DESC=("Steel Ball Run has won two weeks running in the Fall 2026 community rankings. The full Week 6 top 10, "
      "the three shows splitting the season, and why the three anime charts disagree.")
HERO="sbr-cover.webp"

def fig(name,cap,w=760):
    return (f'<figure style="max-width:{w}px;margin:32px auto">'
            f'<img src="../assets/img/{name}" alt="{cap}" loading="lazy" decoding="async">'
            f'<figcaption style="text-align:center">{cap}</figcaption></figure>')

BODY=f"""
<p>Six weeks into the Fall 2026 season, one show has separated itself from the pack, and it is not the one most people would have guessed in September.</p>
<p><strong>STEEL BALL RUN JoJo's Bizarre Adventure 2nd &ndash; 3rd STAGE</strong> took first place in the Week 6 community rankings with <strong>7.47%</strong> of the vote. It is the second week in a row it has finished on top, and the margin is not close: second place sits more than a full point behind.</p>
<p>This is the ranking for the week ending 13 November 2026, and it says something interesting about a season that has been unusually competitive at the top and unusually thin further down.</p>

{fig("sbr-week6.webp","Fall 2026 Week 6 community rankings. Source: Anime Corner weekly poll.",820)}

<h2>What Steel Ball Run actually is</h2>
<p>For anyone who has not followed the series for twenty years, the naming is confusing. Steel Ball Run began in 2004 as the seventh part of <em>JoJo's Bizarre Adventure</em>, written and drawn by Hirohiko Araki. It ran in Weekly Shonen Jump until 2011, when it moved to Ultra Jump and was eventually reclassified as Part 7, with the two parts that follow renumbered around it.</p>
<p>The story is a reset. After Part 6 ended the original continuity, Araki restarted the series in a new universe with familiar names attached to different people. Steel Ball Run is set in 1890 and follows a continent-spanning horse race across the United States, with a prize of fifty million dollars, a cast of competitors who are all hiding something, and a supernatural MacGuffin in the form of scattered holy relics.</p>
<p>Its two leads are <strong>Johnny Joestar</strong>, a former racing prodigy left paralysed, and <strong>Gyro Zeppeli</strong>, an executioner's son who races with steel balls he can spin to strange effect. Their partnership is the best-written relationship Araki has done, and it is the reason the part has a reputation among long-time fans as the series' high point.</p>
<p>The anime adaptation has been released in stages rather than as one continuous season, which is why the current entry is titled <em>2nd &ndash; 3rd STAGE</em>. It covers the middle of the race rather than the beginning.</p>

<h2>Why it is winning</h2>
<p>Three reasons, and only one of them is about quality.</p>
<p><strong>The structure suits weekly viewing.</strong> A race is a natural episodic engine. Every stage has a start, an obstacle, a finish and a new location, so each episode delivers a complete unit of tension. Most seasonal anime cannot do that: they are adapting a continuous story and have to break it wherever the episode happens to end.</p>
<p><strong>It has a built-in audience that has waited a long time.</strong> Steel Ball Run is the part JoJo readers have been asking for since the anime began. The people voting in these polls are largely the people who already loved the manga, and they are motivated in a way that viewers of a new show are not.</p>
<p><strong>It is genuinely well made.</strong> The animation has held up across the run, the colour work is doing the heavy lifting Araki's art demands, and the adaptation has been willing to cut rather than pad. That last point matters more than it sounds &mdash; a bad Steel Ball Run adaptation would have been a scandal, and it is not one.</p>

<h2>The rest of the top five</h2>
<p><strong>Firefly Wedding</strong> returned to second with 5.60%, up one place. It has now finished in the top three for five consecutive weeks, which is the most consistent run in the season and has gone almost unnoticed because it has never actually won.</p>
<p><strong>Even the Student Council Has Its Holes!</strong> dropped to third at 5.58% &mdash; a gap of two hundredths of a percentage point from second place. The two shows have now swapped positions twice.</p>
<p><strong>The Apothecary Diaries Season 3</strong> sits fourth at 5.44%. On a different chart it is first: by raw audience numbers on LiveChart it is the most-watched show of the season, ahead of everything else airing. It is the clearest example this season of the gap between "most people watching" and "most people voting in a poll".</p>
<p><strong>Black Clover Season 2</strong> rounds out the top five at 5.28%, and it holds the season's highest average score at 88. A show that finished years ago, brought back for a continuation, currently rated best of the season.</p>

{fig("sbr-winners.webp","Six weeks, three winners. Source: Anime Corner weekly polls, Weeks 1-6.",820)}

<h2>Six weeks, three winners</h2>
<p>The season has split cleanly. <em>Even the Student Council Has Its Holes!</em> won Weeks 1 and 2. <em>Bleach: Thousand-Year Blood War &ndash; The Calamity</em> took Weeks 3 and 4. Steel Ball Run has now taken Weeks 5 and 6.</p>
<p>That pattern is worth watching. The first six weeks produced three two-week runs and nothing longer. If Steel Ball Run wins Week 7, it becomes the first show this season to hold the top spot for three consecutive weeks, and the season starts to look like a one-horse race in the literal sense.</p>

<h2>Three charts, three different answers</h2>
<p>The most useful thing about this season is how badly the charts disagree, because the disagreement tells you what each one measures.</p>
<p><strong>Weekly vote share</strong> measures enthusiasm. It rewards shows with a passionate, organised audience, which is why a long-awaited adaptation like Steel Ball Run can beat a show with five times its viewership.</p>
<p><strong>Total members on a tracking site</strong> measures accumulated audience. ONE PIECE leads that by an enormous margin &mdash; around 769,000 users, roughly seven times the second-place show &mdash; and it is not even airing new episodes right now.</p>
<p><strong>Average score</strong> measures satisfaction among the people who watched. Black Clover Season 2 leads that with 88.</p>
<p>None of these is wrong. A show can be the most-watched, the most-loved and the least-voted-for all at once, and this season has examples of each.</p>

{fig("sbr-popularity.webp","Popularity is a different race. Source: AniList member counts, 14 November 2026.",820)}

<h2>Where the season stands further down</h2>
<p>Below the top ten the numbers fall away fast. Tenth place is under 2%, and the drop from fifth to tenth is steeper than the drop from first to fifth.</p>
<p>The Detective Is Already Dead Season 2 sits at 17th with 1.60%, which is a fair reflection of how that sequel has landed: a devoted core audience, a much larger group who bounced off the first season, and very little movement in between. Blue Box Season 2 is eighth at 2.57%, comfortably the strongest of the romance sequels.</p>

<h2>What is airing this week</h2>
<p>If you want to catch up before the next poll closes, these are the episodes landing in the next few days, Japan time:</p>
<ul>
<li><strong>Black Clover Season 2</strong> &mdash; episode 7, 14 November, 23:00</li>
<li><strong>Blue Box Season 2</strong> &mdash; episode 6, 15 November, 16:30</li>
<li><strong>Overgeared</strong> &mdash; episode 8, 15 November, 23:30</li>
<li><strong>Reincarnated as a Sword Season 2</strong> &mdash; episode 8, 19 November, 00:30</li>
<li><strong>The Apothecary Diaries Season 3</strong> &mdash; episode 8, 20 November, 23:00</li>
<li><strong>Firefly Wedding</strong> &mdash; episode 7, 20 November, 23:30</li>
</ul>

<h2>The short version</h2>
<p>Steel Ball Run is winning because it is a well-made adaptation of the most-loved part of a forty-year-old series, released into a season where nothing else has managed to hold the top spot for more than a fortnight. That is a real achievement and it is also partly a scheduling accident.</p>
<p>The Apothecary Diaries Season 3 is probably the better show by most measures. Black Clover Season 2 is the best-rated. ONE PIECE is the biggest by a factor of seven. And the poll is being won by the one with the loudest fans.</p>
<p>All four of those statements are true at once, which is what makes following the season week to week more interesting than any single ranking suggests.</p>
"""

head = TPL[:TPL.find("<body")]
head = head.replace(TPL_TITLE, TITLE).replace(TPL_DESC, DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html",
                    f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", HERO)
shell = TPL[TPL.find('<header class="site">'):TPL.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = re.sub(r'</article><div class="related">.*?</div>', '', TPL[TPL.find("</article>"):], count=1, flags=re.S)
post = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">Anime</span><span>14 November 2026</span><i></i><span>10 min read</span></div>
<div class="posthero"><img src="../assets/img/{HERO}" alt="Steel Ball Run topping the Fall 2026 rankings" loading="eager" fetchpriority="high" decoding="async"></div>
{BODY}
<div class="next" style="margin-top:34px"><h3>More from AniPix</h3>
<div class="chips"><a class="chip" href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Watch List</a><a class="chip" href="../articles/detective-is-already-dead-season-2-guide.html">Detective Is Already Dead S2</a><a class="chip" href="../articles/blue-box-season-2-complete-episode-guide.html">Blue Box Season 2</a></div></div>
<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Anime: The Complete Watch List</a></li><li><a href="../articles/detective-is-already-dead-season-2-guide.html">The Detective Is Already Dead Season 2 Guide</a></li><li><a href="../articles/blue-box-season-2-complete-episode-guide.html">Blue Box Season 2: Complete Episode Guide</a></li></ul></div></article>"""
open(f"articles/{SLUG}.html","w",encoding="utf-8").write(head+shell+post+tail)

CARD=(f'<div class="card"><div class="thumb"><img src="assets/img/{HERO}" alt="" loading="lazy" decoding="async"></div>'
      f'<span class="chip">Anime</span><h3><a href="articles/{SLUG}.html">{TITLE}</a></h3><p>{DESC}</p>'
      f'<div class="meta"><span>14 November 2026</span><i></i><span>10 min read</span></div></div>')
for page in ("anime.html","index.html"):
    s=open(page,encoding="utf-8").read()
    if SLUG in s: continue
    m=re.search(r'<div class="cards[^"]*">',s)
    s=(s[:m.end()]+CARD+s[m.end():]) if m else (s[:s.find('<div class="card">')]+CARD+s[s.find('<div class="card">'):])
    open(page,"w",encoding="utf-8").write(s)

sm=open("sitemap.xml",encoding="utf-8").read()
url=f"https://blog.anipix.me/articles/{SLUG}.html"
if url not in sm:
    sm=sm.replace("</urlset>",f'  <url><loc>{url}</loc><lastmod>2026-11-14</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>\n</urlset>')
    open("sitemap.xml","w",encoding="utf-8").write(sm)
print("words:",len(H.unescape(re.sub(r'<[^>]+>',' ',BODY)).split()))
print("sitemap:",sm.count("<url>"))
