#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Google News RSS targeted sweep for specific stories."""
import re, html, json, subprocess, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
TZ8 = datetime.timezone(datetime.timedelta(hours=8))

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "25", "-A", UA, url],
                              capture_output=True, text=True, timeout=35).stdout
    except Exception:
        return ""

def gnews(q, hl="zh-HK", gl="HK", n=25):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
    raw = fetch(url)
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    out = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        title = html.unescape(t.group(1)) if t else ""
        pd = None
        if d:
            for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
                try:
                    pd = datetime.datetime.strptime(d.group(1).strip(), fmt)
                    if pd.tzinfo is None:
                        pd = pd.replace(tzinfo=datetime.timezone.utc)
                    break
                except Exception:
                    continue
        out.append({"title": title, "link": html.unescape(l.group(1)) if l else "",
                    "dt": pd, "source": html.unescape(s.group(1)) if s else ""})
    return out

QUERIES = [
    ("pru-results", "Prudential plc interim results 2026"),
    ("pru-hk", "保诚 中期业绩 2026"),
    ("manulife-q2", "Manulife second quarter 2026 results"),
    ("manulife-hk", "宏利 业绩 2026年第二季"),
    ("ia-stats-h1", "保监局 2026年上半年 新造保费 统计"),
    ("ia-stats-en", "Hong Kong insurance authority statistics first half 2026 premiums"),
    ("pingan", "平安 2026 中期业绩 寿险"),
    ("aia-broker", "AIA broker access new business"),
    ("hk-ins-aug", "Hong Kong insurance August 21 2026"),
    ("axa-h1", "AXA first half 2026 results"),
]

for tag, q in QUERIES:
    try:
        res = gnews(q)
    except Exception as e:
        print(f"ERR {tag}: {e}")
        continue
    fresh = [r for r in res if r["dt"] and r["dt"] >= LAST.astimezone(datetime.timezone.utc)]
    print(f"\n=== GN[{tag}] '{q}': {len(res)} total, {len(fresh)} fresh ===")
    for r in (fresh[:8] if fresh else res[:5]):
        dt = r["dt"].astimezone(TZ8).strftime("%m-%d %H:%M") if r["dt"] else "????"
        print(f"- {dt} | {r['source'][:16]:16s} | {r['title'][:90]}")
