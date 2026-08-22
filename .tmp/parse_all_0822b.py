#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse all t0822b pages for entries dated 2026-08-20 21:00+ (window since last check)."""
import re, html, os, glob

def unq(s):
    return html.unescape(re.sub(r"\s+", " ", s or "")).strip()

DATE_RE = re.compile(r"(2026-08-(?:19|20|21|22))|((?:19|20|21|22)\s+(?:Aug|August)\s+2026)|((?:19|20|21|22)\s*/\s*08\s*/\s*2026)")
MONTH_DAY = re.compile(r"(19|20|21|22)\s*(?:Aug|August)", re.I)

def has_recent_date(s):
    s2 = s[:200]
    if DATE_RE.search(s2):
        return True
    m = MONTH_DAY.search(s2)
    return bool(m)

def parse_html_links(path, name, maxn=40):
    try:
        raw = open(path, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        print(f"{name}: ERR {e}"); return []
    text = re.sub(r"<script.*?</script>", " ", raw, flags=re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
    out, seen = [], set()
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', text, flags=re.S):
        href = m.group(1)
        inner = unq(re.sub(r"<[^>]+>", " ", m.group(2)))
        if len(inner) < 8:
            continue
        key = (href[:100], inner[:50])
        if key in seen: continue
        seen.add(key)
        if has_recent_date(href + " " + inner) or any(d in inner for d in ["2026-08-2", "Aug 2026"]):
            out.append((inner[:90], href[:120]))
    return out[:maxn]

def parse_rss(path, name, maxn=40):
    try:
        raw = open(path, encoding="utf-8", errors="ignore").read()
    except Exception as e:
        print(f"{name}: ERR {e}"); return []
    out, seen = [], set()
    for m in re.finditer(r"<item>(.*?)</item>", raw, flags=re.S):
        block = m.group(1)
        t = re.search(r"<title>(.*?)</title>", block, flags=re.S)
        l = re.search(r"<link>(.*?)</link>", block, flags=re.S)
        d = re.search(r"<pubDate>(.*?)</pubDate>", block, flags=re.S)
        title = unq(re.sub(r"<[^>]+>", "", t.group(1) if t else ""))
        link = unq(l.group(1) if l else "")
        date = unq(d.group(1) if d else "")
        if not title or title in seen: continue
        seen.add(title)
        recent = bool(re.search(r"20 Aug 2026|21 Aug 2026|22 Aug 2026|19 Aug 2026", date)) or bool(re.search(r"2026-08-2[0-2]", title + date))
        if recent:
            out.append((title[:90], link[:130], date))
    return out[:maxn]

files = {
    "IA-press(wb2)": "data/_raw/t0822b/wb-ia-press2.html",
    "IA-circ(wb)": "data/_raw/t0822b/wb-ia-circ.html",
    "IAA-rss(wb)": "data/_raw/t0822b/wb-iaa-rss.html",
    "Manulife(wb)": "data/_raw/t0822b/wb-manulife.html",
    "FSTB-press(wb)": "data/_raw/t0822b/wb-fstb-press.html",
    "HKMA": "data/_raw/t0822b/hkma-press.html",
    "IBMAG": "data/_raw/t0822b/ibmag.html",
    "SCMP": "data/_raw/t0822b/scmp.html",
    "AIA": "data/_raw/t0822b/aia.html",
    "Prudential": "data/_raw/t0822b/prudential.html",
    "AXA": "data/_raw/t0822b/axa.html",
    "SunLife": "data/_raw/t0822b/sunlife.html",
}
for name, path in files.items():
    if name == "IAA-rss(wb)":
        res = parse_rss(path, name)
        print(f"\n===== {name} ({len(res)} recent) =====")
        for t, l, d in res:
            print(f"  [{d}] {t}  ->  {l}")
    else:
        res = parse_html_links(path, name)
        print(f"\n===== {name} ({len(res)} recent-ish) =====")
        for t, l in res:
            print(f"  {t:85s} {l}")
