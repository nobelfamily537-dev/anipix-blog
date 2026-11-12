#!/usr/bin/env python3
"""Rebuild the blog homepage card sections from the newest articles."""
import re, glob, os, html as H
from datetime import datetime

MONTHS = {m: i for i, m in enumerate(
    ["january","february","march","april","may","june","july","august",
     "september","october","november","december"], 1)}

def parse_date(s):
    m = re.search(r'(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})', s)
    if not m: return None
    mon = MONTHS.get(m.group(2).lower())
    return datetime(int(m.group(3)), mon, int(m.group(1))) if mon else None

posts = []
for f in sorted(glob.glob("articles/*.html")):
    t = open(f, encoding="utf-8").read()
    h1   = re.search(r'<h1>(.*?)</h1>', t, re.S)
    meta = re.search(r'<div class="post-meta">(.*?)</div>', t, re.S)
    hero = re.search(r'<div class="posthero"><img src="([^"]+)"', t)
    desc = re.search(r'<meta name="description" content="([^"]*)"', t)
    if not (h1 and meta and hero and desc): continue
    spans = re.findall(r'<span[^>]*>(.*?)</span>', meta.group(1), re.S)
    date_s = next((s for s in spans if parse_date(s)), "")
    read   = next((s for s in spans if 'read' in s.lower()), "")
    chip   = next((s for s in spans if s.strip() and parse_date(s) is None and 'read' not in s.lower()), "Anime")
    dt = parse_date(date_s)
    if not dt: continue
    posts.append(dict(slug=os.path.basename(f)[:-5], title=h1.group(1).strip(),
                      desc=H.escape(desc.group(1), quote=False),
                      hero=hero.group(1).replace("../", ""), chip=chip.strip(),
                      date=date_s.strip(), read=read.strip(), dt=dt))
posts.sort(key=lambda p: (p["dt"], p["slug"]), reverse=True)
print(f"articles parsed: {len(posts)}")

def card(p):
    return (f'<div class="card"><div class="thumb"><img src="{p["hero"]}" alt="" loading="lazy"></div>'
            f'<span class="chip">{p["chip"]}</span>'
            f'<h3><a href="articles/{p["slug"]}.html">{p["title"]}</a></h3>'
            f'<p>{p["desc"]}</p>'
            f'<div class="meta"><span>{p["date"]}</span><i></i><span>{p["read"]}</span></div></div>')

def find_cards_block(t, start):
    """Return (open_idx, close_idx_end) of the <div class="cards"> that follows `start`,
    matched by counting nested <div> tags."""
    i = t.find('<div class="cards">', start)
    if i < 0: return None
    depth = 0; k = i
    while k < len(t):
        if t.startswith('<div', k):
            depth += 1; k += 4
        elif t.startswith('</div>', k):
            depth -= 1
            if depth == 0: return (i, k + 6)
            k += 6
        else:
            k += 1
    return None

GROUPS = [("Latest news", "New", posts[:3]),
          ("Latest articles", f"{min(7, max(0,len(posts)-3))} posts", posts[3:10]),
          ("More from the blog", "Archive", posts[10:])]

t = open("index.html", encoding="utf-8").read()
for name, label, group in GROUPS:
    hpos = t.find(f'<h2>{name}</h2>')
    if hpos < 0:
        print(f"  !! section not found: {name}"); continue
    # update the label span right after the h2
    t = re.sub(r'(<h2>' + re.escape(name) + r'</h2><span>)(.*?)(</span>)',
               lambda m: m.group(1) + label + m.group(3), t, count=1, flags=re.S)
    blk = find_cards_block(t, t.find(f'<h2>{name}</h2>'))
    if not blk:
        print(f"  !! cards block not found for {name}"); continue
    a, b = blk
    t = t[:a] + '<div class="cards">' + "".join(card(p) for p in group) + '</div>' + t[b:]
    print(f"  {name:<20} -> {len(group)} cards")

open("index.html", "w", encoding="utf-8").write(t)
print(f"\ntotal cards: {t.count('<div class=\"card\">')} | div balance: {t.count('<div')-t.count('</div>')}")
print("top 4:")
for p in posts[:4]: print(f"   {p['date']:<18} {p['title'][:58]}")
