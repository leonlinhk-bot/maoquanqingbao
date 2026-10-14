#!/usr/bin/env python3
"""Parse fetched feeds (RSS + Atom), filter items published after last check."""
import re, html, json
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 14, 2, 11, tzinfo=HKT)


def parse_date(s):
    s = (s or '').strip()
    if not s:
        return None
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})[T ](\d{2}):(\d{2}):(\d{2})(?:\.\d+)?Z$', s)
    if m:
        return datetime(*[int(x) for x in m.groups()], tzinfo=timezone.utc).astimezone(HKT)
    for f in ('%a, %d %b %Y %H:%M:%S %z', '%Y-%m-%dT%H:%M:%S%z',
              '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d'):
        try:
            dt = datetime.strptime(s, f)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=HKT)
            return dt.astimezone(HKT)
        except Exception:
            continue
    return None


def strip(t):
    t = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', t or '', flags=re.S)
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', ' ', t)).replace('﻿', ' ').strip()


def items(raw):
    out = []
    blocks = re.findall(r'<item\b.*?</item>', raw, re.S) or re.findall(r'<entry\b.*?</entry>', raw, re.S)
    for blk in blocks:
        def g(tag):
            m = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', blk, re.S)
            return m.group(1) if m else ''
        t = strip(g('title'))
        l = strip(g('link'))
        if not l:
            l = strip(g('guid'))
        if not l:
            lm = re.search(r'<link[^>]*href="([^"]+)"', blk)
            l = lm.group(1) if lm else ''
        d = parse_date(g('pubDate') or g('published') or g('updated') or g('dc:date'))
        if t:
            out.append({'title': t, 'link': l, 'date': d, 'desc': strip(g('description') or g('summary'))[:300]})
    return out


allnew = {}
for key in ('insurancebusinessmag', 'scmp_business', 'insuranceasia', 'govhk'):
    raw = open(f'data/_1014/{key}.raw', encoding='utf-8').read()
    its = items(raw)
    new = [i for i in its if i['date'] and i['date'] > CUT]
    allnew[key] = new
    print(f"\n##### {key}: parsed {len(its)}, after-cut {len(new)}")
    for i in new:
        print(f"- {i['date']:%m-%d %H:%M} | {i['title'][:105]} | {i['link'][:110]}")

json.dump({k: [{**i, 'date': i['date'].isoformat() if i['date'] else None} for i in v] for k, v in allnew.items()},
          open('data/_1014/_new.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
