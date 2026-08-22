#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse fetched pages for candidates since 2026-08-20T21:14+08:00."""
import re, html, json, datetime

LAST = datetime.datetime(2026, 8, 20, 21, 14, 53, tzinfo=datetime.timezone(datetime.timedelta(hours=8)))
TZ8 = datetime.timezone(datetime.timedelta(hours=8))

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

def parse_rss(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    out = []
    for m in re.finditer(r"<item>(.*?)</item>", raw, re.S):
        it = m.group(1)
        t = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", it, re.S)
        l = re.search(r"<link>(.*?)</link>", it, re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", it, re.S)
        desc = re.search(r"<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>", it, re.S)
        out.append({
            "title": unq(t.group(1)) if t else "",
            "link": unq(l.group(1)) if l else "",
            "pubDate": unq(d.group(1)) if d else "",
            "desc": unq(desc.group(1))[:300] if desc else "",
        })
    return out

def parse_hkma(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    out = []
    for m in re.finditer(r'href="(/eng/news-and-media/press-releases/\d{4}/\d{2}/[^"]+)"[^>]*>([^<]{10,160})</a>', raw):
        url = "https://www.hkma.gov.hk" + m.group(1)
        title = unq(m.group(2))
        dm = re.search(r"/(\d{4})/(\d{2})/(\d{8})", m.group(1))
        date = ""
        if dm:
            date = f"{dm.group(1)}-{dm.group(2)}-{dm.group(3)[6:8]}"
        out.append({"title": title, "url": url, "date": date})
    return out

def show(tag, items, n=18):
    print(f"\n===== {tag}: {len(items)} =====")
    for it in items[:n]:
        d = it.get("date") or it.get("pubDate") or ""
        print(f"- {d} | {it.get('title','')[:90]} | {it.get('link','')[:110]}")

# RSS
iaa = parse_rss("data/_raw/t0822-iaa-rss.html")
show("InsuranceAsia RSS", iaa)
json.dump(iaa, open(".tmp/iaa-0822.json", "w"), ensure_ascii=False, indent=1)

# HKMA
hkma = parse_hkma("data/_raw/t0822-hkma.html")
show("HKMA", hkma)
json.dump(hkma, open(".tmp/hkma-0822.json", "w"), ensure_ascii=False, indent=1)
