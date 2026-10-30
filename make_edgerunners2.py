#!/usr/bin/env python3
"""Blog post: Cyberpunk: Edgerunners 2 review/guide."""
import os, re

SLUG = "cyberpunk-edgerunners-2-review"
TITLE = "Cyberpunk: Edgerunners 2 Review: Night City Burns Again"
DESC = ("Cyberpunk: Edgerunners 2 is out now on Netflix - all 10 episodes. A standalone story with a new crew, "
        "a new director and The Cure on the opening credits. Here is everything you need to know.")
DATE = "30 October 2026"
READ = "11 min read"
CAT = "Anime"
HERO = "edgerunners2-1.webp"

def fig(name, cap, w=760):
    return (f'<figure style="max-width:{w}px;margin:34px auto">'
            f'<img src="../assets/img/{name}" alt="" loading="lazy" decoding="async">'
            f'<figcaption style="text-align:center">{cap}</figcaption></figure>')

BODY = f"""<article class="post"><h1>{TITLE}</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="posthero"><img src="../assets/img/{HERO}" alt="Cyberpunk: Edgerunners 2" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>Four years after David Martinez ran into the light, Night City is back — and it has not calmed down at all. <strong>Cyberpunk: Edgerunners 2</strong> arrived on Netflix on <strong>20 October 2026</strong>, all ten episodes at once, and within ten days it had climbed to the top of AniList's trending chart with more than 109,000 members and an average score of 84.</p>

<p>That is a remarkable number for a sequel that deliberately throws away its own protagonist. So what is it, who is in it, and does it hold up? Here is the full picture.</p>

{fig("edgerunners2-3.webp", "The official Cyberpunk: Edgerunners wordmark.", 460)}

<h2>The most important thing to know: it is not a season 2</h2>

<p>If you finished the 2022 series and are waiting to find out what happened next, this is not that show.</p>

<p>CD PROJEKT RED and Netflix have been explicit about it: Edgerunners 2 is a <strong>standalone anthology entry</strong>, not a continuation. David's story ended. The new series follows an entirely different crew with their own problems, and it is written so that someone who has never seen the first series can start here.</p>

<p>What carries over is the setting, the studio, and the attitude. Night City is the same city — corporate towers, gang territory, cheap chrome, expensive consequences. Everything else is new.</p>

<h2>The new crew</h2>

<p>Four characters anchor the story, and the show is built around how their paths cross.</p>

<p><strong>Weak "King" Kingsley</strong> is a washed-up veteran edgerunner now living without chrome, searching for a sense of purpose in a world that has moved past him. The premise is quietly brutal: in Night City, a mercenary who cannot afford implants is not just old, he is obsolete.</p>

<p><strong>D</strong> is a Snake Nation netrunner on a revenge arc, hunting whoever wiped out his clan. His trail leads him toward corporate secrets he was never supposed to find — which is how a personal vendetta turns into something much bigger.</p>

<p><strong>Roman Carax</strong> is a young cinephile who documents Night City with a camcorder in a culture that has traded cinema for neurodance. He is the closest thing the series has to an audience surrogate, and the show's own tagline — "when the world is blinded by spectacle, what extremes do you have to go to make your story matter?" — clearly belongs to him.</p>

<p><strong>Talia Yang</strong> grew up in the corporate towers but was hardened by trials inside the Maelstrom gang. Fiercely independent, deeply attached to her crew's chrome, and the character most likely to complicate everyone else's plan.</p>

{fig("edgerunners2-4.webp", "Lucy remains the most recognisable face of the Edgerunners universe — cosplay at Made In Asia 2023.", 560)}

<h2>The people who made it</h2>

<p>The staff list is the strongest argument that this is not a quick cash-in.</p>

<p><strong>Kai Ikarashi</strong> directs, and it is his directorial debut. That sounds like a risk until you look at what he did on the first series: storyboard artist, animation director, animator, prop designer. He has been inside this show's visual language from the beginning, and the promotion is the kind of thing animation fans usually ask for and rarely get.</p>

<p><strong>Bartosz Sztybor</strong> returns as showrunner, story writer and producer. He is a Hugo Award winner and one of the people who built the original's story. <strong>Masahiko Otsuka</strong> is back on scripts, and <strong>Ichigo Kanno</strong> — an animation director and key animator on the first series — takes over as lead character designer.</p>

<p>The one name that is new in a very visible way is composer <strong>Tsuneo Imahori</strong>. Music carried an enormous amount of the first series' reputation, so this was always going to be the most scrutinised change.</p>

<h2>The tone has changed on purpose</h2>

<p>CD PROJEKT RED has described the shift bluntly. If the 2022 series played like a Michael Bay film, this one is aiming closer to Martin Scorsese.</p>

<p>That is a real difference and it explains most of the creative decisions. The first series was a rocket: a kid with nothing straps on military-grade chrome and burns out in ten episodes. It was loud, fast and operatic, and it worked because it committed completely.</p>

<p>Edgerunners 2 sounds like it is trading that for something slower and more character-driven — a heist that goes wrong, a revenge plot that keeps expanding, and four people whose damage is psychological rather than cybernetic. Whether that is better is a matter of taste. It is definitely not the same show twice.</p>

{fig("edgerunners2-5.webp", "Cyberpunk cosplay at Fanime 2023 — Rebecca and Lucy have become convention staples.")}

<h2>The music</h2>

<p>The opening theme is <strong>"10:15 Saturday Night" by The Cure</strong>. That is a genuinely surprising needle drop for a cyberpunk anime, and it says a lot about the tone the show is going for — cold, post-punk melancholy rather than aggressive synth metal.</p>

<p>The ending theme is <strong>"Watson" by Petite Meller</strong>. Watson is also the district of Night City where a lot of the series takes place, which is a nice touch if you know the map.</p>

<h2>What it is actually about</h2>

<p>Strip away the chrome and the gunfights, and the throughline CD PROJEKT RED keeps describing is this: <strong>family, obsession, legacy, and how your lens reflects the stories of the people around you</strong>.</p>

<p>That last phrase is doing real work. With Roman as a filmmaker and D as a man chasing a ghost, the series seems to be asking what it means to document a city that is designed to consume the people in it. The first series asked whether a nobody could matter. This one appears to be asking who gets to decide that a story was worth telling.</p>

<p>There is also a quieter theme that runs through all of Cyberpunk: the chrome. Weak is defined by not having it. Talia is defined by being attached to it. D's enemies are defined by what they can afford. In this universe, your implants are your class.</p>

<h2>The game tie-in</h2>

<p>On the same day the anime premiered, CD PROJEKT RED announced the <strong>Edgerunners 2 Update</strong> — also called <strong>Update 2.5</strong> — for Cyberpunk 2077. It released on <strong>22 October 2026</strong> for PC, PlayStation 5 and Xbox Series X|S, with a Nintendo Switch 2 version following shortly after.</p>

<p>The update is free and includes content inspired by the anime alongside other new items and features. If you play the game, it is the smoothest possible way to stay in the world after the credits roll.</p>

{fig("edgerunners2-6.webp", "Fanime 2023: Edgerunners cosplayers, four years after the original series.")}

<h2>How it compares to the 2022 original</h2>

<p>The original Edgerunners is one of the rare game adaptations that stands entirely on its own — a tight ten-episode tragedy that people still recommend without caveats. It also set a very high bar, and the sequel's decision not to try to clear it the same way is smart.</p>

<p>What you get instead is an anthology: same city, same rules, different story. That structure has advantages. It means no character is safe, no backstory is assumed, and the writers are not obliged to keep anyone alive for a sequel. It also means the emotional investment has to be rebuilt from scratch — which is the main risk.</p>

{fig("edgerunners2-2.webp", "Edgerunners livery on display at Anime Las Vegas 2025.")}

<p>The early audience numbers suggest the bet is landing. Being the most-trending anime on AniList on 29 October, a week and a half after release, is not the profile of a show people are bouncing off.</p>

<h2>Who should watch it</h2>

<p><strong>Watch it if</strong> you liked the first series and want more of Night City without a rehash; if you like heist stories with a revenge spine; or if you are interested in what Studio TRIGGER looks like under a new director with a deliberately restrained brief.</p>

<p><strong>Skip it if</strong> you specifically want David, Lucy and the 2022 crew — they are not here. And if you bounced off the original's bleakness, this one is described as even more grounded, which usually means even less comfort.</p>

<h2>Where to watch</h2>

<p>All ten episodes are streaming <strong>exclusively on Netflix</strong>, released together rather than weekly. Both Edgerunners series are on the same platform, so you can watch the original first if you want the full context — though it is not required.</p>

<h2>Verdict</h2>

<p>Cyberpunk: Edgerunners 2 does the harder thing. It could have brought back a beloved cast and coasted. Instead it built a new crew, handed the director's chair to someone who earned it inside the production, changed the composer, changed the tone, and asked the audience to start over.</p>

<p>Not every sequel gets away with that. This one appears to, and the numbers back it up: 109,000 AniList members, a score of 84, and the top of the trending chart within ten days. For a ten-episode anime based on a video game, in a season crowded with Black Clover, The Apothecary Diaries and JoJo's Steel Ball Run, that is a strong result.</p>

<p><strong>Score: 8.5/10.</strong> A colder, more patient Night City — and it suits the place.</p>

<div class="related"><h2>Related reading</h2><ul>
<li><a href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Anime: The Complete Watch List and Release Dates</a></li>
<li><a href="../articles/apothecary-diaries-season-3-review.html">The Apothecary Diaries Season 3 Review</a></li>
<li><a href="../articles/blue-box-season-1-and-2-overview.html">Blue Box Season 1 &amp; 2: A Short Overview</a></li>
</ul></div></article>"""

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
print("post written")

CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{HERO}" alt="" loading="lazy" decoding="async"></div>'
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
    sm = sm.replace("</urlset>", f'  <url><loc>{url}</loc><lastmod>2026-10-30</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n</urlset>')
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
print("sitemap urls:", sm.count("<url>"))
