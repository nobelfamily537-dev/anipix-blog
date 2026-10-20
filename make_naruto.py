#!/usr/bin/env python3
"""Generate the Naruto Shippuden complete arc guide post for the AniPix blog."""
import os, re
from PIL import Image, ImageDraw, ImageFont

SLUG = "naruto-shippuden-complete-arc-guide"
TITLE = "Naruto Shippuden: Complete Arc Guide, Every Episode Explained and Full Review (2026)"
DESC = ("Every Naruto Shippuden arc in order, with episode ranges, what happens, which arcs are filler, "
        "and a review of all 500 episodes. A complete watch guide.")
DATE = "20 October 2026"
READ = "22 min read"
CAT = "Anime"

os.makedirs("assets/img", exist_ok=True)
COVER = f"assets/img/{SLUG}-cover.webp"

# ---------------------------------------------------------------- cover
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
            try:
                return ImageFont.truetype(q, sz)
            except Exception:
                pass
    return ImageFont.load_default()

d.text((70, 88), "ANIPIX BLOG", font=font(26), fill=(158, 152, 178))
y = 196
for ln in ["Naruto Shippuden", "Complete Arc Guide"]:
    d.text((70, y), ln, font=font(74), fill=(255, 255, 255)); y += 90
d.text((70, y + 24), "All 500 episodes  ·  22 arcs  ·  full review", font=font(29, False), fill=(204, 198, 220))
img.save(COVER, "WEBP", quality=86, method=6)
print("cover:", os.path.getsize(COVER) // 1024, "KB")

# ---------------------------------------------------------------- template
tpl = open("articles/fall-2026-anime-watch-list.html", encoding="utf-8").read()
head = tpl[:tpl.find("<body")]
head = head.replace("Fall 2026 Anime: The Complete Watch List and Release Dates | AniPix Blog", TITLE)
head = head.replace("Every major anime airing in October 2026 &mdash; JoJo's Steel Ball Run, the Bleach finale and The Apothecary Diaries Season 3 &mdash; with release dates and how to plan your watchlist.", DESC)
head = head.replace("https://blog.anipix.me/articles/fall-2026-anime-watch-list.html",
                    f"https://blog.anipix.me/articles/{SLUG}.html")
head = head.replace("fall-2026-anime-watch-list-cover.webp", f"{SLUG}-cover.webp")
shell = tpl[tpl.find('<header class="site">'):tpl.find('<article class="post">')]
shell = shell.replace('<a href="../news.html">News</a></p>', '<a href="../anime.html">Anime</a></p>')
tail = tpl[tpl.find("</article>"):]

ARCS = [
 ("1", "Kazekage Rescue Mission", "1&ndash;32", "Canon", 9.0,
  "Two and a half years after leaving with Jiraiya, Naruto comes home &mdash; taller, stronger, and still wearing orange. Almost immediately the Akatsuki kidnap Gaara, now the Kazekage of the Hidden Sand, to extract the One-Tail. Team Kakashi races to Suna, and Sakura finally gets the fight she deserved, taking on the puppet master Sasori alongside the elderly Chiyo.",
  "The best possible way to open a sequel. It re-establishes everyone, introduces the Akatsuki as a real threat, and gives Sakura her best arc in the whole series."),
 ("2", "Tenchi Bridge Reconnaissance Mission", "33&ndash;53", "Canon", 8.0,
  "Team Kakashi gets a new captain, Yamato, and a new member: Sai, a blunt, socially hopeless Root operative with a fake smile. Their mission is to meet a spy inside Orochimaru's ranks at the Tenchi Bridge. It ends the way everyone feared &mdash; with Naruto losing control of the Nine-Tails and finally seeing Sasuke again, who makes it very clear he wants nothing to do with them.",
  "Sai's introduction is great, and the reunion scene is genuinely painful to watch. The middle stretch drags a little."),
 ("3", "Twelve Guardian Ninja", "54&ndash;71", "Filler", 6.0,
  "An anime-original arc about the former twelve elite bodyguards of the Land of Fire and a mystery tied to Asuma's past. It sets up Asuma's connection to the Akatsuki members he is about to face, which is genuinely useful, but the arc itself wanders.",
  "Skip it if you are in a hurry. The one thing worth knowing &mdash; Asuma's history &mdash; is explained again later anyway."),
 ("4", "Akatsuki Suppression Mission", "72&ndash;88", "Canon", 9.5,
  "The immortal duo Hidan and Kakuzu hunt the Two-Tails' jinchuriki, and Team 10 is sent after them. Asuma does not come back from that fight. What follows is Shikamaru's arc: a grieving, furious, brilliantly cold revenge story, and Naruto's debut of the Rasenshuriken.",
  "One of the best arcs in the series. Asuma's death is handled with real weight, and Shikamaru's growth from lazy genius to team leader is the payoff the character had been building towards since Part 1."),
 ("5", "Three-Tails' Appearance", "89&ndash;112", "Filler", 5.5,
  "A long anime-original arc about capturing the Three-Tails, introducing the crystal-user Guren and a boy named Yūkimaru. It is the longest filler block in the first half of the show.",
  "The most skippable arc in Shippuden. Twenty-four episodes of padding in the middle of a canon hot streak."),
 ("6", "Itachi Pursuit Mission", "113&ndash;118", "Canon", 8.0,
  "Sasuke assembles his own team &mdash; Hebi, with Suigetsu, Karin and Jugo &mdash; with one goal: find and kill Itachi. Meanwhile Konoha launches its own pursuit, hoping to reach Sasuke first.",
  "Short and focused. Team Hebi is a fun, strange addition, and it sets up everything that follows."),
 ("7", "Tale of Jiraiya the Gallant", "127&ndash;133", "Canon", 10.0,
  "Jiraiya goes alone into the Hidden Rain to find out who Pain really is. He does find out. He also fights the Six Paths of Pain, loses, and sends one last coded message home. The arc is framed by the story of the book he wrote &mdash; the one Naruto is named after.",
  "The emotional high point of the entire series. Seven episodes, no wasted scenes, and one of the best character send-offs in anime."),
 ("8", "Fated Battle Between Brothers", "134&ndash;143", "Canon", 9.5,
  "Sasuke finally faces Itachi. It is a long, brutal fight built on genjutsu, and Sasuke wins. Then Tobi tells him the truth about the Uchiha massacre &mdash; and everything Sasuke believed about his brother, and about his own life, collapses.",
  "The reveal lands like a truck. It re-colours the entire series retroactively, which is a very hard trick to pull off."),
 ("9", "Pain's Assault", "152&ndash;175", "Canon", 10.0,
  "Pain levels Konoha. The village is destroyed, Kakashi is killed, and Naruto returns to fight the strongest opponent he has faced. Hinata confesses her feelings mid-battle and is cut down in front of him, which finally breaks the seal on the Nine-Tails. The arc ends with Naruto choosing to forgive Nagato rather than kill him &mdash; and Nagato bringing everyone back.",
  "The peak of Shippuden. The scale, the animation, the emotional beats, and the fact that the hero wins by refusing revenge rather than by being stronger."),
 ("10", "Past Arc: The Locus of Konoha", "176&ndash;196", "Filler", 6.5,
  "A set of standalone episodes set while Konoha rebuilds. Flashbacks and side stories about Iruka, Kakashi, Inari, and others.",
  "Filler, but unusually good filler. If you like the supporting cast, these are worth watching between the big arcs."),
 ("11", "Five Kage Summit", "197&ndash;214", "Canon", 8.5,
  "All five great nations meet to decide what to do about the Akatsuki. Sasuke crashes the summit, fights the Kage, and kills Danzo. Naruto, meanwhile, has to confront a question he has been avoiding: what do you do when your friend cannot be saved?",
  "Politically the most interesting arc. It also gives Sasuke his darkest moment and Naruto his hardest decision."),
 ("12", "Fourth Great Ninja War: Countdown", "215&ndash;222 &amp; 243&ndash;256", "Mixed", 7.5,
  "The Allied Shinobi Forces form. Naruto is hidden away on an island to train with Killer Bee and learn to control the Nine-Tails, while the war preparations roll on around him.",
  "Necessary setup. The training sequence is good; the filler detours around it are not."),
 ("13", "Fourth Great Ninja War: Confrontation", "261&ndash;289 &amp; 296&ndash;321", "Mixed", 8.0,
  "The war begins in earnest. The Allied Forces fight an army of White Zetsu clones and reanimated legends, including the resurrected Kage and former Akatsuki members. Itachi, brought back by Kabuto's jutsu, breaks free and teams up with Naruto to stop it.",
  "Huge in scale and full of great individual fights. It is also where the pacing starts to become a problem."),
 ("14", "Power Arc", "290&ndash;295", "Filler", 7.0,
  "A short, high-budget filler arc made to mark 500 total Naruto episodes. Team Kakashi investigates a massacre in Tonika Village and fights a resurrected Kabuto's creation.",
  "Genuinely well animated, and short enough not to hurt. One of the better filler arcs."),
 ("15", "Fourth Great Ninja War: Climax", "322&ndash;348 &amp; 362&ndash;375", "Mixed", 8.5,
  "Naruto joins the battlefield properly. Tobi's identity is finally revealed, and the reanimated Madara Uchiha appears and single-handedly changes the course of the war.",
  "Madara's entrance is one of the great anime moments. The arc around it is uneven but the highs are very high."),
 ("16", "Kakashi's Anbu Arc", "349&ndash;361", "Filler", 8.0,
  "A flashback arc covering Kakashi's years in the Anbu Black Ops, his relationship with a young Itachi, and the years between the Kannabi Bridge and the start of the series.",
  "The best filler arc in Shippuden. It fills a real gap in the story and treats Kakashi like the main character he arguably is."),
 ("17", "Birth of the Ten-Tails' Jinchuriki", "378&ndash;388 &amp; 391&ndash;413", "Canon", 8.5,
  "Obito becomes the Ten-Tails' jinchuriki. The entire Allied Force &mdash; including a reformed Team 7 fighting side by side for the first time in years &mdash; has to stop him.",
  "The Team 7 reunion on the battlefield is exactly what the whole series was building towards."),
 ("18", "Kaguya Otsutsuki Strikes", "414&ndash;479", "Mixed", 7.0,
  "Just as Madara seems finished, Black Zetsu betrays him and revives Kaguya Otsutsuki, the original source of chakra. Team 7 is thrown across dimensions in a final battle to stop the Infinite Tsukuyomi.",
  "Kaguya's arrival is divisive. The fight is spectacular; the villain switch is not what most fans wanted."),
 ("19", "Childhood Arc", "480&ndash;483", "Filler", 7.0,
  "Short flashback episodes showing the main cast as children at the academy.",
  "Light, warm, and easy to watch after the war. Nothing essential."),
 ("20", "Sasuke's Story: Sunrise", "484&ndash;488", "Canon", 8.0,
  "Adapted from a light novel. Sasuke travels alone on a path of redemption, investigating a mystery involving people who explode and a shadowy organisation.",
  "A quieter, more mature Sasuke. It is a good epilogue to his character."),
 ("21", "Shikamaru's Story", "489&ndash;493", "Canon", 7.5,
  "Years after the war, Shikamaru takes a dangerous mission in the Land of Silence while dealing with what it means to be a leader in a shinobi world that is changing.",
  "Another novel adaptation, and a solid one. Shikamaru has earned his own story."),
 ("22", "Konoha Hiden: The Perfect Day for a Wedding", "494&ndash;500", "Canon", 8.5,
  "The final arc. Kakashi sends everyone on the hardest mission of their lives: finding the perfect wedding gift for Naruto and Hinata. It ends with the wedding, and with Iruka narrating the story of the boy nobody wanted, who became the Seventh Hokage.",
  "A soft, funny, deeply satisfying ending. After 500 episodes, the show earns its happy ending."),
]

rows = []
for n, name, eps, kind, score, what, verdict in ARCS:
    rows.append(f"""
<h2>Arc {n}: {name} <span style="font-size:0.62em;color:#8a8aa3">(Episodes {eps})</span></h2>
<p><strong>Type:</strong> {kind} &nbsp;·&nbsp; <strong>Score:</strong> {score}/10</p>
<p>{what}</p>
<p><strong>Verdict:</strong> {verdict}</p>""")

BODY = f"""<article class="post"><h1>Naruto Shippuden: Complete Arc Guide, Every Episode Explained and Full Review</h1>
<div class="post-meta"><span class="chip">{CAT}</span><span>{DATE}</span><i></i><span>{READ}</span></div>
<div class="sharebar"><span class="sharelabel">Share</span><button class="sbtn" type="button" onclick="sharePost()">Share this article</button><button class="sbtn" type="button" onclick="copyLink()">Copy link</button></div>
<div class="posthero"><img src="../assets/img/{SLUG}-cover.webp" alt="Naruto Shippuden complete arc guide" loading="eager" fetchpriority="high" decoding="async"></div>

<p><strong>Last updated:</strong> {DATE}</p>

<p>Naruto Shippuden ran for ten years, from February 2007 to March 2017, and finished at exactly 500 episodes. That is a lot of television &mdash; and a big part of why so many people who start it never finish it. This guide breaks all 500 episodes into the 22 story arcs they actually belong to, tells you what happens in each, which ones are filler, and gives every arc a score.</p>

<p>If you are watching for the first time, or coming back after years away, this is the map. Arc boundaries are listed as they are most commonly given &mdash; different sources draw the lines slightly differently, because the anime ran year-round and mixed canon and filler inside single seasons.</p>

<h2>Quick facts</h2>
<ul>
<li><strong>Episodes:</strong> 500</li>
<li><strong>Ran:</strong> 15 February 2007 &ndash; 23 March 2017</li>
<li><strong>Studio:</strong> Pierrot</li>
<li><strong>Director:</strong> Hayato Date</li>
<li><strong>Story arcs:</strong> 22 (29 by the anime's own count, which splits some arcs further)</li>
<li><strong>Source:</strong> Part II of Masashi Kishimoto's manga, plus a significant amount of anime-original material</li>
</ul>

<h2>Canon vs filler &mdash; the short version</h2>

<p>Shippuden has a lot of filler, and it is not evenly spread. The first 175 episodes are mostly canon with two filler blocks. The war arc, which runs from roughly episode 215 to 479, is where the filler problem becomes real.</p>

<p>If you want the main story only, the arcs marked <strong>Canon</strong> below are the ones to watch. Arcs marked <strong>Filler</strong> can be skipped without losing the plot. Arcs marked <strong>Mixed</strong> contain both, and are harder to skip cleanly.</p>

<p>Two filler arcs are genuinely worth your time: <strong>Kakashi's Anbu Arc</strong> (349&ndash;361) and the <strong>Power Arc</strong> (290&ndash;295). Everything else is optional.</p>
{''.join(rows)}

<h2>The best arcs, ranked</h2>

<ol>
<li><strong>Tale of Jiraiya the Gallant (127&ndash;133)</strong> &mdash; seven episodes, one gut punch</li>
<li><strong>Pain's Assault (152&ndash;175)</strong> &mdash; the peak of the series</li>
<li><strong>Akatsuki Suppression Mission (72&ndash;88)</strong> &mdash; Shikamaru's revenge</li>
<li><strong>Fated Battle Between Brothers (134&ndash;143)</strong> &mdash; the reveal that changes everything</li>
<li><strong>Kazekage Rescue Mission (1&ndash;32)</strong> &mdash; the perfect opening</li>
</ol>

<h2>Overall review</h2>

<p>Shippuden is two shows in one. The first half &mdash; roughly episodes 1 to 175 &mdash; is one of the best stretches of shonen anime ever made. It is tight, it is emotional, it pays off things the original series set up years earlier, and it repeatedly puts Naruto in situations where being strong is not the answer. Jiraiya's death, Pain's assault, Shikamaru's revenge: these are the episodes people remember, and they hold up.</p>

<p>The second half is a different story. The Fourth Great Ninja War is enormous, and enormous is the problem. Hundreds of episodes of fighting, a rotating cast of resurrected characters, and filler blocks dropped into the middle of the climax. The highs are still very high &mdash; Madara's entrance, the Team 7 reunion, Kakashi's past &mdash; but they are further apart, and the pacing asks a lot of the viewer.</p>

<p>The ending, though, is right. Kaguya is a divisive final villain, and many fans would have preferred Madara to stay the final boss. But the last few arcs &mdash; Sasuke's redemption, Shikamaru's story, and the wedding &mdash; bring the series down gently. The final episode, with Iruka narrating the life of the boy nobody wanted, is exactly the ending the show had earned.</p>

<p><strong>Final score: 8.5/10.</strong> Watch the canon arcs. Skip most of the filler. Do not skip Jiraiya.</p>

<h2>Should you watch it in 2026?</h2>

<p>Yes, with a caveat. Shippuden is still one of the defining shonen series, and the first 175 episodes are essential viewing for anyone who likes the genre. But it is also 500 episodes, and the second half is a serious commitment. If you are short on time, watch the canon arcs, look up the filler list, and skip the war arc's side stories. You will still get the whole story.</p>

<h2>FAQ</h2>

<h3>How many episodes does Naruto Shippuden have?</h3>
<p>Exactly 500, aired between February 2007 and March 2017.</p>

<h3>Can I skip the filler?</h3>
<p>Yes. The filler arcs are marked above. The main story still makes sense without them, though a few characters introduced in filler show up again later.</p>

<h3>Which arc is the best?</h3>
<p>Tale of Jiraiya the Gallant (127&ndash;133) and Pain's Assault (152&ndash;175). Most fans would put those two at the top.</p>

<h3>Does it have a proper ending?</h3>
<p>Yes. The series ends with Naruto and Hinata's wedding, and the story continues in Boruto: Naruto Next Generations.</p>

<div class="related"><h2>Related reading</h2><ul><li><a href="../articles/fall-2026-anime-watch-list.html">Fall 2026 Anime: The Complete Watch List and Release Dates</a></li><li><a href="../articles/apothecary-diaries-season-3-review.html">The Apothecary Diaries Season 3: Review and Release Schedule</a></li><li><a href="../articles/naruto-boruto-wallpapers-guide.html">Naruto and Boruto Wallpapers: The Complete Guide</a></li></ul></div></article>"""

open(f"articles/{SLUG}.html", "w", encoding="utf-8").write(head + shell + BODY + tail)
print("article written:", len((head + shell + BODY + tail)) // 1024, "KB")

CARD = (f'<div class="card"><div class="thumb"><img src="assets/img/{SLUG}-cover.webp" alt="" '
        f'loading="lazy" decoding="async"></div><span class="chip">{CAT}</span>'
        f'<h3><a href="articles/{SLUG}.html">{TITLE}</a></h3><p>{DESC}</p>'
        f'<div class="meta"><span>{DATE}</span><i></i><span>{READ}</span></div></div>')

for page in ["anime.html", "index.html"]:
    s = open(page, encoding="utf-8").read()
    if SLUG in s:
        print("already on", page); continue
    m = re.search(r'<div class="cards[^"]*">', s)
    s = (s[:m.end()] + CARD + s[m.end():]) if m else (s[:s.find('<div class="card">')] + CARD + s[s.find('<div class="card">'):])
    open(page, "w", encoding="utf-8").write(s)
    print("card added ->", page)

sm = open("sitemap.xml", encoding="utf-8").read()
url = f"https://blog.anipix.me/articles/{SLUG}.html"
if url not in sm:
    entry = f"  <url><loc>{url}</loc><lastmod>2026-10-20</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n"
    sm = sm.replace("</urlset>", entry + "</urlset>")
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
print("sitemap urls:", sm.count("<url>"))
