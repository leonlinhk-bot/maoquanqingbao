#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, re, html, subprocess, urllib.parse

d = json.load(open('data/live-items.json'))
items = d['items']
print("=== 平安/PingAn entries ===")
for it in items:
    txt = it['id'] + ' ' + it['title']['sc']
    if 'ping' in txt.lower() or '平安' in txt:
        print(' ', it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it['title']['sc'][:80])
print("=== 中报季 entries (h1-2026 / 中期 / 中报) ===")
for it in items:
    txt = it['id'] + ' ' + it['title']['sc']
    if ('h1-2026' in txt.lower() or '中期' in txt or '中报' in txt or 'interim' in txt.lower()) and '2026' in it.get('publishedAt',''):
        print(' ', it['id'], '|', it.get('sourceKey'), '|', it.get('publishedAt'), '|', it['title']['sc'][:80])

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                              capture_output=True, text=True, timeout=35).stdout
    except Exception:
        return ""

# HKET Ping An article
raw = fetch("https://www.hket.com/article/3870000")
print("\nHKET fetch len:", len(raw))

# GN RSS: site search for IBMAG AIA article
def gnews(q, hl="en-US", gl="US"):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
    raw = fetch(url)
    out = []
    for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        out.append((html.unescape(t.group(1)) if t else "", html.unescape(l.group(1)) if l else "", d.group(1) if d else ""))
    return out

print("\n=== GN: insurancebusinessmag AIA ===")
for t, l, d in gnews("insurancebusinessmag AIA broker")[:8]:
    print("-", d[:25], "|", t[:90])
    print("   ", l[:120])
