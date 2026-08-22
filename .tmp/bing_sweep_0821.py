#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bing RSS sweep + InsuranceAsia RSS check for window since 2026-08-20T21:14:53+08:00."""
import re, html, subprocess, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

def fetch(url, t=30):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                              capture_output=True, text=True, timeout=t+10).stdout
    except Exception as e:
        return f"ERR {e}"

def parse_rss(xml):
    out = []
    for it in re.findall(r"<item>(.*?)</item>", xml, re.S):
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        s = re.search(r"<source[^>]*>(.*?)</source>", it, re.S)
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
        out.append({"title": html.unescape(t.group(1)) if t else "",
                    "link": html.unescape(l.group(1)) if l else "",
                    "pubDate": d.group(1) if d else "", "dt": pd,
                    "src": html.unescape(s.group(1)) if s else ""})
    return out

# 1. InsuranceAsia RSS raw
raw = fetch("https://insuranceasia.com/insurance/rss.xml")
print("=== InsuranceAsia RSS raw (first 300 chars) ===")
print(raw[:300])
print("items:", len(re.findall(r"<item>", raw)))

# 2. Bing RSS sweep
QUERIES = [
    "Insurance Authority Hong Kong 2026", "HKMA press release",
    "AIA Hong Kong news", "Manulife Hong Kong news", "Prudential Hong Kong news",
    "AXA Hong Kong news", "Sun Life Hong Kong news",
    "Hong Kong insurance market August 2026", "香港 保險 8月21日",
    "insuranceasia.com", "Insurance Business Asia Hong Kong",
    "香港 保监局 通函", "香港 金管局 保險", "家族辦公室 保險 香港",
]
for q in QUERIES:
    url = f"https://www.bing.com/search?q={urllib.parse.quote(q)}&format=rss&count=30"
    try:
        items = parse_rss(fetch(url))
        fresh = [i for i in items if i["dt"] and i["dt"] >= LAST]
        print(f"\n[{q}] {len(fresh)} fresh / {len(items)} total")
        for i in fresh[:6]:
            print("   -", i["dt"].astimezone(datetime.timezone(datetime.timedelta(hours=8))).strftime("%m-%d %H:%M") if i["dt"] else "?",
                  "|", i["title"][:85])
            print("     ", i["link"][:140])
    except Exception as e:
        print(f"[{q}] ERR {e}")
