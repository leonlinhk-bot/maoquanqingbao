#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inspect IBmag page: article links + titles; gnews site: queries for fresh items."""
import re, subprocess, html, urllib.parse, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))

def fetch(url, t=30):
    return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                          capture_output=True, text=True, timeout=t+10).stdout

def gnews(q, hl="en", gl="HK", n=25):
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(q)}&hl={hl}&gl={gl}&ceid={gl}:{hl}"
    raw = fetch(url)
    out = []
    for it in re.findall(r"<item>(.*?)</item>", raw, re.S):
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
                    "dt": pd, "src": html.unescape(s.group(1)) if s else ""})
    return out

# IBmag article links
raw = open(".tmp/ibmag-bn.html").read()
hrefs = re.findall(r'<a[^>]+href="([^"]+)"', raw)
arts = [h for h in hrefs if "/asia/news/" in h and "breaking-news" not in h]
uniq = list(dict.fromkeys(arts))
print("== IBmag article links:", len(uniq))
for u in uniq[:20]:
    print("  ", u[:130])

# gnews site: queries
for q in ["site:insuranceasia.com", "site:insurancebusinessmag.com/asia", "site:scmp.com insurance",
          "site:aia.com.hk", "site:manulife.com.hk", "site:prudential.com.hk"]:
    items = gnews(q)
    fresh = [i for i in items if i["dt"] and i["dt"] >= LAST]
    print(f"\n[{q}] {len(fresh)} fresh / {len(items)}")
    for i in (fresh or items[:3]):
        print("   -", i["dt"].astimezone(datetime.timezone(datetime.timedelta(hours=8))).strftime("%m-%d %H:%M") if i["dt"] else "?",
              "|", i["title"][:80], "|", i["src"])
