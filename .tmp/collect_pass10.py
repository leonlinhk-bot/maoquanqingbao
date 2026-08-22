#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pass 10: find Hengda original + aastocks UBS content + silver bond details."""
import re, html, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

# Google News RSS for hengda with various queries to find source outlets
def gnews(q):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl=zh-HK&gl=HK&ceid=HK:zh-HK"
    raw = fetch(url)
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    out = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        out.append((html.unescape(t.group(1)).strip() if t else "",
                    html.unescape(s.group(1)).strip() if s else "",
                    html.unescape(l.group(1)).strip() if l else ""))
    return out

print("=== gnews hengda ===")
for t, s, l in gnews("恒大人寿 吊销")[:10]:
    print(f"* [{s}] {t[:80]}\n  {l[:120]}")

print("\n=== gnews hengda2 ===")
for t, s, l in gnews("恒大人寿 保险 许可证")[:10]:
    print(f"* [{s}] {t[:80]}\n  {l[:120]}")

# aastocks AIA news - extract links
print("\n=== aastocks AIA news links ===")
raw = fetch("https://www.aastocks.com/tc/stocks/market/stock-news.aspx?symbol=01299")
links = re.findall(r'href="(/tc/stocks/market/stock-news[^"]*)"[^>]*>([^<]{10,100})</a>', raw)
seen = set()
for u, t in links:
    t = html.unescape(t).strip()
    if t in seen:
        continue
    seen.add(t)
    print(f"- {t[:80]} | https://www.aastocks.com{u[:110]}")
