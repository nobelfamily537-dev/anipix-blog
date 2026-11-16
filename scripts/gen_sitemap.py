#!/usr/bin/env python3
"""Rebuild sitemap.xml with accurate <lastmod> dates taken from git history.

Why this exists: Google decides what to recrawl by comparing a URL's <lastmod>
in the sitemap against the last time it crawled that URL. A sitemap that keeps
saying a page was last changed in October, for a page that changed in November,
tells Google there is nothing new to fetch - so the page is never recrawled and
sits in "Crawled - currently not indexed" forever.

Run this from a FULL clone (git fetch --unshallow), not a --depth 1 clone,
otherwise every file resolves to the same single commit.
"""
import os, re, subprocess, sys, glob

BASE = "https://blog.anipix.me/"
ROOT_PRIORITY = {
    "index.html": ("weekly", "1.0"),
    "anime.html": ("weekly", "0.7"), "games.html": ("weekly", "0.7"),
    "guides.html": ("weekly", "0.7"), "news.html": ("weekly", "0.7"),
    "all-posts.html": ("weekly", "0.7"),
    "privacy.html": ("yearly", "0.3"), "disclaimer.html": ("yearly", "0.3"),
}

def last_commit(path):
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%ad", "--date=short", "--", path],
            capture_output=True, text=True, check=True).stdout.strip()
        return out or None
    except Exception:
        return None

def main():
    files = sorted(glob.glob("articles/*.html")) + \
            sorted(f for f in glob.glob("*.html"))
    rows, missing = [], 0
    for f in files:
        d = last_commit(f)
        if not d:
            missing += 1
            continue
        loc = BASE if f == "index.html" else BASE + f
        if f in ROOT_PRIORITY:
            cf, pr = ROOT_PRIORITY[f]
        elif f.startswith("articles/"):
            cf, pr = "monthly", "0.8"
        else:
            cf, pr = "yearly", "0.5"
        rows.append((loc, d, cf, pr))

    rows.sort(key=lambda r: (0 if r[0] == BASE else 1 if "/articles/" not in r[0] else 2, r[0]))
    body = "\n".join(
        f'  <url><loc>{l}</loc><lastmod>{d}</lastmod>'
        f'<changefreq>{c}</changefreq><priority>{p}</priority></url>'
        for l, d, c, p in rows)
    open("sitemap.xml", "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + body + "\n</urlset>\n")

    print(f"sitemap.xml written: {len(rows)} urls, {missing} without a git date")
    from collections import Counter
    for d, n in Counter(r[1] for r in rows).most_common(5):
        print(f"   {d}  {n}")

if __name__ == "__main__":
    main()
