#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Search helper: Google News RSS (primary) + Bing HTML (fallback). Usage: python3 gsearch.py 'query' [hl]"""
import subprocess, re, html, sys
from urllib.parse import quote
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"
TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
WIN = NOW - timedelta(hours=30)

def fetch(url):
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                           capture_output=True, text=True, timeout=35)
        return r.stdout
    except Exception as e:
        return ""

def gnews(query, hl="zh-HK", n=12):
    url = f"https://news.google.com/rss/search?q={quote(query)}&hl={hl}&gl=HK&ceid=HK:{hl}"
    raw = fetch(url)
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    print(f"--- GNews [{query}] hl={hl} hits={len(items)} ---")
    out = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        p = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<description>(.*?)</description>", it, re.S)
        if not (t and l):
            continue
        title = html.unescape(re.sub(r"<[^>]+>", "", t.group(1))).strip()
        link = html.unescape(l.group(1)).strip()
        pub = ""
        try:
            if p:
                pub = parsedate_to_datetime(p.group(1)).astimezone(TZ).strftime("%Y-%m-%d %H:%M")
        except Exception:
            pass
        # google news link is a redirect: extract real url if present
        m = re.search(r"url=([^&]+)", link)
        if m:
            from urllib.parse import unquote
            link = unquote(m.group(1))
        fresh = ""
        if pub:
            try:
                fresh = "NEW" if datetime.strptime(pub, "%Y-%m-%d %H:%M").replace(tzinfo=TZ) >= WIN else "old"
            except Exception:
                fresh = "?"
        out.append((pub, fresh, title, link))
        print(f"[{fresh}] {pub} | {title[:80]}\n        {link[:150]}")
    return out

def bing(query, n=10):
    url = f"https://www.bing.com/search?q={quote(query)}&count={n}"
    h = fetch(url)
    print(f"--- Bing [{query}] size={len(h)} ---")
    found = 0
    for m in re.finditer(r'<h2><a href="([^"]+)"[^>]*>(.*?)</a></h2>', h, re.S):
        u = html.unescape(m.group(1))
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        print(f"T: {t[:90]}\nU: {u[:160]}")
        found += 1
        if found >= n:
            break
    if found == 0:
        # fallback: any anchor
        for m in re.finditer(r'href="(https?://[^"]+)"[^>]*>(.*?)</a>', h, re.S):
            u = html.unescape(m.group(1))
            t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
            if len(t) > 25 and 'bing.com' not in u and 'microsoft' not in u:
                print(f"T: {t[:90]}\nU: {u[:160]}")
                found += 1
                if found >= n:
                    break

if __name__ == "__main__":
    q = sys.argv[1]
    hl = sys.argv[2] if len(sys.argv) > 2 else "zh-HK"
    gnews(q, hl)
    print()
    bing(q)
