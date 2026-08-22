#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-08-22 daily collection: HKMA parse + Google News RSS sweep, time-filtered since lastCheck."""
import re, html, json, subprocess, urllib.parse, datetime, sys

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"
LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
print(f"Window: {LAST.isoformat()} -> {NOW.isoformat()}")

def fetch(url):
    try:
        return subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url],
                              capture_output=True, text=True, timeout=40).stdout
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
        out.append({
            "title": title,
            "link": html.unescape(l.group(1)) if l else "",
            "pubDate": d.group(1) if d else "",
            "dt": pd,
            "source": html.unescape(s.group(1)) if s else ""
        })
    return out

def parse_hkma(raw):
    out = []
    for m in re.finditer(r'href="(/eng/news-and-media/press-releases/\d{4}/\d{2}/[^"]+)"[^>]*>([^<]{10,140})</a>', raw):
        url = "https://www.hkma.gov.hk" + m.group(1)
        title = html.unescape(m.group(2)).strip()
        # extract date from URL like /2026/08/20260821-4/
        dm = re.search(r'/(\d{4})/(\d{2})/(\d{8})', m.group(1))
        date = ""
        if dm:
            date = f"{dm.group(1)}-{dm.group(2)}-{dm.group(3)[6:8]}"
        out.append({"title": title, "url": url, "date": date})
    return out

# ---- 1. HKMA ----
hkma_raw = fetch("https://www.hkma.gov.hk/eng/news-and-media/press-releases/")
hkma_items = parse_hkma(hkma_raw)
print(f"\n=== HKMA page: {len(hkma_items)} entries ===")
for it in hkma_items[:15]:
    print("-", it["date"], "|", it["title"][:80], "|", it["url"])

# ---- 2. Google News sweep ----
QUERIES = [
    ("ia", "Hong Kong Insurance Authority"),
    ("ia_cn", "香港保监局"),
    ("hkma", "HKMA Hong Kong Monetary Authority"),
    ("aia", "AIA Hong Kong"),
    ("manulife", "Manulife Hong Kong"),
    ("prudential", "Prudential Hong Kong"),
    ("axa", "AXA Hong Kong"),
    ("sunlife", "Sun Life Hong Kong"),
    ("insuranceasia", "insuranceasia.com"),
    ("ibmag", "Insurance Business Asia"),
    ("scmp", "SCMP Hong Kong insurance"),
    ("nfra", "国家金融监督管理总局"),
    ("familyoffice", "香港 家族办公室 保险"),
    ("insurtech", "香港 保险科技 InsurTech"),
    ("hkins", "香港保險"),
    ("hkins_en", "Hong Kong insurance market news"),
    ("ia_circular", "保监局 通函"),
]
all_cands = {}
for tag, q in QUERIES:
    try:
        res = gnews(q)
    except Exception as e:
        print(f"ERR {tag}: {e}")
        continue
    fresh = [r for r in res if r["dt"] and r["dt"] >= LAST.astimezone(datetime.timezone.utc)]
    all_cands[tag] = fresh
    print(f"\n=== GN[{tag}] '{q}': {len(res)} total, {len(fresh)} fresh ===")
    for r in fresh[:10]:
        print("-", r["dt"].astimezone(datetime.timezone(datetime.timedelta(hours=8))).strftime("%m-%d %H:%M"), "|", r["source"][:18], "|", r["title"][:85])

json.dump({k: v for k, v in all_cands.items()}, open(".tmp/cands.json", "w"), ensure_ascii=False, indent=1, default=str)
json.dump(hkma_items, open(".tmp/hkma_items.json", "w"), ensure_ascii=False, indent=1)
print("\nSaved .tmp/cands.json + .tmp/hkma_items.json")
