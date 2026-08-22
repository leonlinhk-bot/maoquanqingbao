#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-08-21 catch-up sweep: RSS + official pages, window since 2026-08-20T21:14:53+08:00."""
import re, html, json, subprocess, urllib.parse, datetime, sys

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
print(f"Window: {LAST.isoformat()} -> {NOW.isoformat()}", flush=True)

def fetch(url, t=30):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", str(t), "-A", UA, url],
                              capture_output=True, text=True, timeout=t+10).stdout
    except Exception as e:
        return f"ERR {e}"

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
                    "pubDate": d.group(1) if d else "", "dt": pd,
                    "source": html.unescape(s.group(1)) if s else ""})
    return out

QUERIES = [
    ("ia", "Insurance Authority Hong Kong"), ("ia_cn", "香港保监局"),
    ("hkma", "Hong Kong Monetary Authority"), ("aia", "AIA Hong Kong"),
    ("manulife", "Manulife Hong Kong"), ("prudential", "Prudential Hong Kong"),
    ("axa", "AXA Hong Kong"), ("sunlife", "Sun Life Hong Kong"),
    ("insuranceasia", "insuranceasia.com"), ("ibmag", "Insurance Business Asia"),
    ("scmp", "SCMP insurance Hong Kong"), ("nfra", "国家金融监督管理总局"),
    ("familyoffice", "香港 家族办公室 保险"), ("insurtech", "香港 保险科技"),
    ("hkins", "香港保險"), ("hkins_en", "Hong Kong insurance"),
]

results = {}
for key, q in QUERIES:
    try:
        items = gnews(q)
        fresh = [i for i in items if i["dt"] and i["dt"] >= LAST]
        results[key] = fresh
        print(f"[{key}] {len(fresh)} fresh / {len(items)} total")
        for i in fresh[:6]:
            print("   -", i["dt"].astimezone(datetime.timezone(datetime.timedelta(hours=8))).strftime("%m-%d %H:%M") if i["dt"] else "?",
                  "|", i["title"][:90])
            print("     ", i["link"][:150], "| src:", i["source"])
    except Exception as e:
        print(f"[{key}] ERR {e}")

json.dump({k: [{"title": i["title"], "link": i["link"], "dt": i["dt"].isoformat() if i["dt"] else "", "source": i["source"]} for i in v]
           for k, v in results.items()}, open(".tmp/sweep-gnews-0821.json", "w"), ensure_ascii=False, indent=1)
print("saved .tmp/sweep-gnews-0821.json")
