#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Diagnose gnews pubDate parsing + check raw newest items across queries."""
import re, html, subprocess, urllib.parse, datetime

UA = 'Mozilla/5.0'
def fetch(url):
    return subprocess.run(['curl', '-sL', '--max-time', '25', '-A', UA, url],
                          capture_output=True, text=True).stdout

def gnews(q, hl="zh-HK", gl="HK", n=25):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
    raw = fetch(url)
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    out = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
        pd = None
        if d:
            for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z"):
                try:
                    pd = datetime.datetime.strptime(d.group(1).strip(), fmt)
                    break
                except Exception:
                    continue
        out.append({"title": html.unescape(t.group(1)) if t else "",
                    "pubDate": d.group(1) if d else "",
                    "dt": pd, "src": html.unescape(s.group(1)) if s else ""})
    return out

for q in ["AIA Hong Kong", "Insurance Authority Hong Kong", "香港保險", "Hong Kong insurance"]:
    items = gnews(q)
    parsed = sum(1 for i in items if i["dt"])
    print(f"== {q}: {len(items)} items, {parsed} parsed")
    # show the 5 newest regardless of parse
    withdt = [i for i in items if i["dt"]]
    withdt.sort(key=lambda x: x["dt"], reverse=True)
    for i in withdt[:5]:
        print("   ", i["dt"].strftime("%Y-%m-%d %H:%M"), "|", i["title"][:70], "|", i["src"])
    if not withdt:
        for i in items[:3]:
            print("   unparsed:", i["pubDate"], "|", i["title"][:60])
