#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse InsuranceAsia RSS + InsuranceBusiness breaking news with dates."""
import re, html, json, subprocess, datetime

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
tz8 = datetime.timezone(datetime.timedelta(hours=8))

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                              capture_output=True, text=True, timeout=40).stdout
    except Exception:
        return ""

def parse_rss(raw):
    items = re.findall(r"<item>(.*?)</item>", raw, re.S)
    out = []
    for it in items:
        t = re.search(r"<title>(.*?)</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
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
        out.append({"title": html.unescape(t.group(1)).strip() if t else "",
                    "link": html.unescape(l.group(1)).strip() if l else "",
                    "dt": pd})
    return out

raw = fetch("https://insuranceasia.com/rss.xml")
items = parse_rss(raw)
print(f"=== InsuranceAsia RSS: {len(items)} items ===")
for it in items[:25]:
    dts = it["dt"].astimezone(tz8).strftime("%m-%d %H:%M") if it["dt"] else "?"
    print(f"* [{dts}] {it['title'][:95]}")
    print(f"  {it['link'][:130]}")

# InsuranceBusiness: extract story links with dates
raw2 = fetch("https://www.insurancebusinessmag.com/asia/news/breaking-news/")
# look for date patterns near links
print("\n=== InsuranceBusiness (raw links) ===")
links = re.findall(r'href="(https://www\.insurancebusinessmag\.com/asia/news/[^"]+)"', raw2)
uniq = []
seen = set()
for u in links:
    if u not in seen and 'breaking-news' not in u and 'category' not in u:
        seen.add(u)
        uniq.append(u)
for u in uniq[:20]:
    print("-", u[:140])
