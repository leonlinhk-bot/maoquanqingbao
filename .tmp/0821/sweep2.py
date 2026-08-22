#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Final coverage sweep queries."""
import subprocess, re, html
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

def gnews(query, hl, n=8):
    url = f"https://news.google.com/rss/search?q={quote(query)}&hl={hl}&gl=HK&ceid=HK:{hl}"
    raw = fetch(url)
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    print(f"\n### GNews[{hl}] {query} (hits={len(items)})")
    rows = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        p = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
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
        fresh = ""
        if pub:
            try:
                fresh = "NEW" if datetime.strptime(pub, "%Y-%m-%d %H:%M").replace(tzinfo=TZ) >= WIN else "old"
            except Exception:
                fresh = "?"
        rows.append((pub, fresh, title))
    rows.sort(reverse=True)
    for pub, fresh, title in rows[:n]:
        print(f"[{fresh}] {pub} | {title[:90]}")

queries = [
    ('"AXA" 香港 保险 after:2026-08-20', 'zh-HK'),
    ('"Sun Life" 香港 after:2026-08-20', 'zh-HK'),
    ('site:scmp.com insurance after:2026-08-20', 'en'),
    ('香港 保险科技 OR insurtech after:2026-08-20', 'zh-HK'),
    ('金融监管总局 after:2026-08-20', 'zh-CN'),
    ('"Hong Kong" insurance company announcement after:2026-08-20', 'en'),
    ('友邦 OR 宏利 OR 保誠 OR 安盛 OR 永明 保险 公告 after:2026-08-20', 'zh-HK'),
]
for q, hl in queries:
    gnews(q, hl)
