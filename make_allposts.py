#!/usr/bin/env python3
"""Build all-posts.html (every article) and add a 'View all posts' button under Latest."""
import os, re, glob, html, datetime

MONTHS = {m: i for i, m in enumerate(
    ["January","February","March","April","May","June","July","August","September","October","November","December"], 1)}

def parse_date(s):
    m = re.match(r"(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})", s.strip())
    if not m: return datetime.date(2000,1,1)
    d, mon, y = m.groups()
    return datetime.date(int(y), MONTHS.get(mon, 1), int(d))

rows = []
for path in glob.glob("articles/*.html"):
    h = open(path, encoding="utf-8").read()
    slug = os.path.basename(path)
    t = re.search(r"<h1>(.*?)</h1>", h, re.S)
    if not t: continue
    title = html.unescape(re.sub(r"<[^>]+>", "", t.group(1))).strip()
    hero = re.search(r'class="posthero"><img src="\.\./assets/img/([^"]+)"', h)
    chip = re.search(r'<div class="post-meta"><span class="chip">([^<]+)</span>', h)
    date = re.search(r'<div class="post-meta">.*?<span>([^<]+)</span><i></i><span>([^<]+)</span>', h, re.S)
    desc = re.search(r'<meta name="description" content="([^"]*)"', h)
    if not desc:
        desc = re.search(r'<meta property="og:description" content="([^"]*)"', h)
    d, read = (date.group(1), date.group(2)) if date else ("", "")
    rows.append({
        "slug": slug, "title": title,
        "hero": hero.group(1) if hero else "",
        "chip": chip.group(1) if chip else "Anime",
        "date": d, "read": read,
        "desc": html.unescape(desc.group(1)) if desc else "",
        "sort": parse_date(d),
    })

rows.sort(key=lambda r: (r["sort"], r["title"]), reverse=True)
print("articles found:", len(rows))

idx = open("index.html", encoding="utf-8").read()
header = idx[idx.find('<header class="site">'):idx.find("</header>") + 9]
footer = idx[idx.find('<footer class="site">'):idx.find("</footer>") + 9]
# grab the <head> shell from index and retarget it
head = idx[:idx.find("<body")]
head = head.replace("<title>", "<title>", 1)
head = re.sub(r"<title>.*?</title>", "<title>All Posts | AniPix Blog</title>", head, count=1, flags=re.S)
head = re.sub(r'<meta name="description" content="[^"]*"',
              '<meta name="description" content="Every article on the AniPix Blog in one place - anime guides, reviews, release dates and wallpaper advice, newest first.">',
              head, count=1)
head = re.sub(r'<link rel="canonical" href="[^"]*"', '<link rel="canonical" href="https://blog.anipix.me/all-posts.html"', head, count=1)
head = re.sub(r'<meta property="og:url" content="[^"]*"', '<meta property="og:url" content="https://blog.anipix.me/all-posts.html"', head, count=1)
head = re.sub(r'<meta property="og:title" content="[^"]*"', '<meta property="og:title" content="All Posts | AniPix Blog"', head, count=1)
head = re.sub(r'<meta property="og:image" content="[^"]*"', '<meta property="og:image" content="https://blog.anipix.me/assets/logo.png"', head, count=1)

def card(r):
    img = f'<img src="assets/img/{r["hero"]}" alt="" loading="lazy" decoding="async">' if r["hero"] else ""
    return (f'<div class="card"><div class="thumb">{img}</div>'
            f'<span class="chip">{html.escape(r["chip"])}</span>'
            f'<h3><a href="articles/{r["slug"]}">{html.escape(r["title"])}</a></h3>'
            f'<p>{html.escape(r["desc"])}</p>'
            f'<div class="meta"><span>{html.escape(r["date"])}</span><i></i><span>{html.escape(r["read"])}</span></div></div>')

cards_html = "\n".join(card(r) for r in rows)

ALL = f"""{head}<body>
{header}
<main class="wrap">
<div class="hero"><p class="eyebrow">Archive</p><h1>All posts</h1>
<p>Every article on the AniPix Blog, newest first &mdash; {len(rows)} posts covering anime guides, reviews, release dates and wallpaper advice.</p></div>
<div class="sec-head"><h2>All articles</h2><span>{len(rows)} posts</span></div>
<div class="cards">
{cards_html}
</div>
<div class="viewall"><a class="btn" href="index.html">&larr; Back to home</a></div>
<div class="cta-band"><h2>Want the wallpapers without the hunting?</h2><p>AniPix is a free Android app with thousands of HD anime wallpapers, live wallpapers and daily updates.</p><a href="https://anipix.me/">Get the AniPix app</a></div>
</main>
{footer}
</body></html>"""
open("all-posts.html", "w", encoding="utf-8").write(ALL)
print("written all-posts.html")

# --- CSS for the button ---
css = open("assets/style.css", encoding="utf-8").read()
if ".viewall" not in css:
    css += """
/* view-all-posts button */
.viewall{display:flex;justify-content:center;margin:34px 0 10px}
.viewall .btn{display:inline-flex;align-items:center;gap:9px;padding:14px 30px;border-radius:999px;
  font-weight:700;font-size:15px;letter-spacing:.2px;text-decoration:none;
  background:linear-gradient(135deg,#6d5efc,#9a4bff);color:#fff;
  box-shadow:0 14px 30px -12px rgba(109,94,252,.65);transition:transform .16s ease,box-shadow .16s ease}
.viewall .btn:hover{transform:translateY(-2px);box-shadow:0 20px 38px -14px rgba(109,94,252,.8)}
.viewall .btn:active{transform:translateY(0)}
.viewall .btn span{font-size:18px;line-height:1}
@media(max-width:520px){.viewall .btn{padding:13px 24px;font-size:14px}}
"""
    open("assets/style.css", "w", encoding="utf-8").write(css)
    print("css added")

# --- add 'All posts' to nav on every top-level page + article pages ---
NAV_OLD = '<a href="news.html">News</a>'
NAV_NEW = '<a href="news.html">News</a>\n    <a href="all-posts.html">All posts</a>'
NAV_OLD_ART = '<a href="../news.html">News</a>'
NAV_NEW_ART = '<a href="../news.html">News</a>\n    <a href="../all-posts.html">All posts</a>'
changed = 0
for f in glob.glob("*.html") + glob.glob("articles/*.html"):
    s = open(f, encoding="utf-8").read()
    if "all-posts.html" in s and 'href="../all-posts.html"' not in s and 'href="all-posts.html"' not in s:
        pass
    if f.startswith("articles/"):
        if NAV_OLD_ART in s and "../all-posts.html" not in s:
            s = s.replace(NAV_OLD_ART, NAV_NEW_ART, 1); open(f, "w", encoding="utf-8").write(s); changed += 1
    else:
        if NAV_OLD in s and 'href="all-posts.html">All posts' not in s:
            s = s.replace(NAV_OLD, NAV_NEW, 1); open(f, "w", encoding="utf-8").write(s); changed += 1
print("nav updated on", changed, "files")

# --- insert the button on the homepage, under the Latest section ---
h = open("index.html", encoding="utf-8").read()
BTN = ('<div class="viewall"><a class="btn" href="all-posts.html">View all posts '
       f'<span>&rarr;</span></a></div>')
marker1 = '<div class="sec-head"><h2>Latest articles</h2>'
if marker1 in h and "View all posts" not in h:
    h = h.replace(marker1, BTN + "\n" + marker1, 1)
    print("button inserted under Latest news")
marker2 = '<div class="cta-band">'
if marker2 in h and h.count("View all posts") < 2:
    h = h.replace(marker2, BTN + "\n" + marker2, 1)
    print("button inserted under More from the blog")
open("index.html", "w", encoding="utf-8").write(h)

# --- sitemap ---
sm = open("sitemap.xml", encoding="utf-8").read()
u = "https://blog.anipix.me/all-posts.html"
if u not in sm:
    sm = sm.replace("</urlset>", f'  <url><loc>{u}</loc><lastmod>2026-10-30</lastmod><changefreq>weekly</changefreq><priority>0.9</priority></url>\n</urlset>')
    open("sitemap.xml", "w", encoding="utf-8").write(sm)
print("sitemap urls:", sm.count("<url>"))
