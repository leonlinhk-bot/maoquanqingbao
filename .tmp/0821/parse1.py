#!/usr/bin/env python3
"""Parse fetched RSS/HTML sources for items in the last 24h window."""
import re, html, sys
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

TZ = timezone(timedelta(hours=8))
NOW = datetime.now(TZ)
WIN_START = NOW - timedelta(hours=26)  # window: last 24h + slack
print(f"NOW={NOW.isoformat()}  window_start={WIN_START.isoformat()}")

def show(name, lines):
    print(f"\n===== {name} =====")
    for ln in lines[:40]:
        print(ln)

# ---- InsuranceAsia RSS ----
try:
    raw = open('.tmp/0821/insasia.xml', encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', raw, re.S)
    rows = []
    for it in items:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        p = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        if not (t and l): continue
        title = html.unescape(t.group(1)).strip()
        link = l.group(1).strip()
        pub = ''
        try:
            if p: pub = parsedate_to_datetime(p.group(1)).astimezone(TZ).isoformat()
        except Exception: pass
        rows.append((pub, title, link))
    rows.sort(reverse=True)
    print(f"insasia total={len(rows)}")
    for pub, title, link in rows[:15]:
        mark = '*' if (pub and pub >= WIN_START.isoformat()) else ' '
        print(f"{mark} {pub} | {title[:70]} | {link}")
except Exception as e:
    print("insasia parse error:", e)

# ---- IA press ----
try:
    raw = open('.tmp/0821/ia-press.html', encoding='utf-8', errors='replace').read()
    print(f"\nia-press size={len(raw)}")
    # strip tags, show first 1500 chars
    txt = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt)
    print("TEXT:", txt[:800])
except Exception as e:
    print("ia-press error:", e)

# ---- IA circular ----
try:
    raw = open('.tmp/0821/ia-circ.html', encoding='utf-8', errors='replace').read()
    print(f"\nia-circ size={len(raw)}")
    txt = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = re.sub(r'\s+', ' ', txt)
    print("TEXT:", txt[:800])
except Exception as e:
    print("ia-circ error:", e)
