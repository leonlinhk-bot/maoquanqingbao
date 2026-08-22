#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse insurer newsroom pages for items published Aug 20-22 2026."""
import re, html, json
from datetime import datetime, timezone, timedelta
HKT = timezone(timedelta(hours=8))

def clean(t):
    t = re.sub(r"<[^>]+>", " ", t)
    t = html.unescape(t)
    return re.sub(r"\s+", " ", t).strip()

def parse_aia(raw):
    # JSON blobs with dc:date and dc:title
    out = []
    for m in re.finditer(r'"dc:title":"(.*?)".{0,300}?"dc:date":"(.*?)"', raw, re.S):
        title = m.group(1).replace('\\u002D', '-').replace('\\"', '"')
        date = m.group(2)
        out.append((date, title))
    for m in re.finditer(r'"dc:date":"(.*?)".{0,300}?"dc:title":"(.*?)"', raw, re.S):
        date, title = m.group(1), m.group(2).replace('\\u002D', '-')
        out.append((date, title))
    return out

def parse_prudential(raw):
    out = []
    for m in re.finditer(r'"datePublished":"(.*?)".{0,400}?"headline":"(.*?)"', raw, re.S):
        out.append((m.group(1), m.group(2)))
    for m in re.finditer(r'"headline":"(.*?)".{0,400}?"datePublished":"(.*?)"', raw, re.S):
        out.append((m.group(2), m.group(1)))
    return out

def parse_axa(raw):
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*<h[23][^>]*>(.*?)</h[23]>', raw, re.S):
        out.append(('', clean(m.group(2))))
    for m in re.finditer(r'([0-3]?\d (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4})', raw):
        pass
    # axa newsroom: find links with /news/ and nearby date
    for m in re.finditer(r'href="(/[^"]*news[^"]*)"[^>]*>(.*?)</a>', raw, re.S):
        txt = clean(m.group(2))
        if len(txt) > 12:
            out.append(('', txt))
    return out

def parse_sunlife(raw):
    out = []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        href, txt = m.group(1), clean(m.group(2))
        if len(txt) > 15 and ('news' in href.lower() or 'release' in href.lower()):
            out.append(('', txt))
    for m in re.finditer(r'(\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* 2026)', raw):
        pass
    return out

for name in ['aia', 'prudential', 'axa', 'sunlife']:
    raw = open(f'.tmp/raw/nr_{name}.html', encoding='utf-8', errors='replace').read()
    fn = {'aia': parse_aia, 'prudential': parse_prudential, 'axa': parse_axa, 'sunlife': parse_sunlife}[name]
    res = fn(raw)
    # dedupe
    seen = set(); uniq = []
    for d, t in res:
        if t in seen: continue
        seen.add(t); uniq.append((d, t))
    print(f"\n===== {name.upper()} ({len(uniq)} unique) =====")
    for d, t in uniq[:25]:
        print(f"  {d[:19]:20s} | {t[:80]}")
