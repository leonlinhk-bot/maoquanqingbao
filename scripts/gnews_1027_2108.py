#!/usr/bin/env python3
"""Google News RSS sweep for last-24h HK insurance signals."""
import re, urllib.request, urllib.parse, html

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0"}
queries = [
 "site:ia.org.hk",
 "香港 保險 監管",
 "香港保險 保監局",
 "Hong Kong insurance regulator",
]
for q in queries:
    u = "https://news.google.com/rss/search?q=" + urllib.parse.quote(q) + "&hl=zh-HK&gl=HK&ceid=HK:zh-Hant"
    print("\n=== ", q)
    try:
        req = urllib.request.Request(u, headers=UA)
        x = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', 'ignore')
        items = re.findall(r'<item>(.*?)</item>', x, re.S)[:8]
        for it in items:
            t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
            d = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
            print(" ", (d.group(1).strip() if d else '')[:22], "|", html.unescape(t.group(1)).strip()[:90] if t else '')
    except Exception as e:
        print("  ERR", type(e).__name__, e)
