#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Google News RSS with description snippets. Usage: python3 gs2.py 'query' [hl]"""
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
    except Exception:
        return ""

def gnews(query, hl, n=10):
    url = f"https://news.google.com/rss/search?q={quote(query)}&hl={hl}&gl=HK&ceid=HK:{hl}"
    raw = fetch(url)
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    print(f"\n### GNews[{hl}] {query} (hits={len(items)})")
    rows = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        p = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        d = re.search(r"<description>(.*?)</description>", it, re.S)
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
        sn = ""
        if d:
            sn = html.unescape(re.sub(r"<[^>]+>", "", d.group(1))).strip()[:260]
        fresh = ""
        if pub:
            try:
                fresh = "NEW" if datetime.strptime(pub, "%Y-%m-%d %H:%M").replace(tzinfo=TZ) >= WIN else "old"
            except Exception:
                fresh = "?"
        rows.append((pub, fresh, title, sn, link))
    rows.sort(reverse=True)
    for pub, fresh, title, sn, link in rows[:n]:
        print(f"[{fresh}] {pub} | {title[:90]}")
        if sn:
            print(f"    SN: {sn}")
        print(f"    L: {link[:130]}")

q = sys.argv[1]
hl = sys.argv[2] if len(sys.argv) > 2 else "zh-HK"
gnews(q, hl)
