#!/usr/bin/env python3
"""Submit URLs to IndexNow (Bing, Yandex, Seznam, Naver).

Google has no equivalent: its Indexing API only accepts JobPosting and
BroadcastEvent pages, so blog posts cannot be pushed to Google this way.
IndexNow is the open protocol the other engines actually honour, and it
usually indexes a new URL within minutes rather than weeks.

Usage:
    python scripts/indexnow.py                 # every URL in sitemap.xml
    python scripts/indexnow.py URL [URL ...]   # just these URLs
"""
import json, os, re, sys, glob, urllib.request

HOST = "blog.anipix.me"
KEYFILE = glob.glob("[0-9a-f]" * 1 + "*.txt")
KEY = None
for f in glob.glob("*.txt"):
    stem = f[:-4]
    if re.fullmatch(r"[0-9a-f]{32}", stem):
        KEY = stem
        KEYFILE = f
        break
if not KEY:
    sys.exit("No IndexNow key file found (expected <32 hex chars>.txt in repo root)")

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
]

def sitemap_urls():
    if not os.path.exists("sitemap.xml"):
        return []
    return re.findall(r"<loc>(.*?)</loc>", open("sitemap.xml", encoding="utf-8").read())

def submit(urls):
    if not urls:
        print("nothing to submit")
        return 0
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": f"https://{HOST}/{KEYFILE}",
        "urlList": urls,
    }).encode()
    ok = 0
    for ep in ENDPOINTS:
        try:
            req = urllib.request.Request(ep, data=payload, method="POST",
                                         headers={"Content-Type": "application/json; charset=utf-8"})
            with urllib.request.urlopen(req, timeout=60) as r:
                print(f"  {ep} -> HTTP {r.status} ({len(urls)} urls)")
                if 200 <= r.status < 300:
                    ok += 1
        except Exception as e:
            print(f"  {ep} -> {type(e).__name__}: {e}")
    return ok

if __name__ == "__main__":
    urls = sys.argv[1:] or sitemap_urls()
    urls = [u for u in urls if u.startswith(f"https://{HOST}/")]
    print(f"IndexNow: {len(urls)} url(s), key {KEY[:8]}...")
    for chunk_start in range(0, len(urls), 10000):
        submit(urls[chunk_start:chunk_start + 10000])
