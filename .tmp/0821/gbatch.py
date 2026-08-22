#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch Google News RSS queries with after: date filter."""
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

def gnews(query, hl, n=14):
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
        rows.append((pub, fresh, title, link))
    rows.sort(reverse=True)
    for pub, fresh, title, link in rows[:n]:
        print(f"[{fresh}] {pub} | {title[:85]}\n        {link[:140]}")

queries_zh = [
    ('保监局 OR 保險業監管局 after:2026-08-20', 'zh-HK'),
    ('宏利 OR Manulife 香港 after:2026-08-20', 'zh-HK'),
    ('保誠 OR Prudential 香港 after:2026-08-20', 'zh-HK'),
    ('安盛 OR AXA 香港 after:2026-08-20', 'zh-HK'),
    ('永明 OR SunLife 香港 after:2026-08-20', 'zh-HK'),
    ('友邦 OR AIA 香港 after:2026-08-20', 'zh-HK'),
    ('金融监管总局 保险 after:2026-08-20', 'zh-CN'),
    ('保险 香港 8月21日 after:2026-08-20', 'zh-HK'),
]
queries_en = [
    ('"Insurance Authority" Hong Kong after:2026-08-20', 'en'),
    ('Hong Kong insurance after:2026-08-20', 'en'),
    ('Hong Kong life insurance regulator after:2026-08-20', 'en'),
]

for q, hl in queries_zh:
    gnews(q, hl)
for q, hl in queries_en:
    gnews(q, hl)
