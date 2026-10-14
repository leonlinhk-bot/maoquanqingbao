#!/usr/bin/env python3
"""Parse raw feeds fetched at 21:34 for the window 2026-10-14T02:11 -> now."""
import json, re, html, os
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import xml.etree.ElementTree as ET

HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 14, 2, 11, tzinfo=HKT)
D = '/Users/leonliang/maoquanqingbao/data/_1014_2108'


def hk(dt):
    return dt.astimezone(HKT)


def report(name, recs):
    print(f'\n===== {name}  ({len(recs)} in window) =====')
    for t, title, url in recs:
        print(f'  {t}  {title[:110]}')
        print(f'        {url[:130]}')


def rss_items(path):
    out = []
    try:
        raw = open(path, encoding='utf-8', errors='replace').read()
    except FileNotFoundError:
        return out
    try:
        root = ET.fromstring(raw)
    except Exception as e:
        print(f'  [xml error {path}: {e}]')
        return out
    for it in root.iter():
        tag = it.tag.split('}')[-1]
        if tag not in ('item', 'entry'):
            continue
        title = pub = link = ''
        for ch in it:
            t = ch.tag.split('}')[-1]
            if t == 'title':
                title = (ch.text or '').strip()
            elif t in ('pubDate', 'published', 'updated', 'date'):
                pub = (ch.text or '').strip()
            elif t == 'link':
                link = (ch.text or ch.attrib.get('href', '')).strip()
        dt = None
        if pub:
            try:
                dt = parsedate_to_datetime(pub)
            except Exception:
                try:
                    dt = datetime.fromisoformat(pub.replace('Z', '+00:00'))
                except Exception:
                    dt = None
        if dt and dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        if dt and hk(dt) >= CUT:
            out.append((hk(dt).strftime('%m-%d %H:%M'), html.unescape(re.sub('<[^>]+>', '', title)), link))
    out.sort(reverse=True)
    return out


for k in ['artemis', 'insuranceasia', 'insurancebusinessmag', 'scmp', 'govhk']:
    report(k, rss_items(f'{D}/{k}.raw'))

# insuranceasianews = WP JSON
try:
    j = json.load(open(f'{D}/insuranceasianews.raw', encoding='utf-8'))
    recs = []
    for p in j:
        dt = datetime.fromisoformat(p['date_gmt']).replace(tzinfo=timezone.utc)
        if hk(dt) >= CUT:
            recs.append((hk(dt).strftime('%m-%d %H:%M'), html.unescape(re.sub('<[^>]+>', '', p['title']['rendered'])), p['link']))
    recs.sort(reverse=True)
    report('insuranceasianews', recs)
except Exception as e:
    print('ian error', e)

# asiainsurancereview HTML
try:
    raw = open(f'{D}/asiainsurancereview.raw', encoding='utf-8', errors='replace').read()
    recs = []
    for m in re.finditer(r'href="(/News/ViewNewsLetterArticle[^"]+)"[^>]*>([^<]{15,200})<', raw):
        recs.append(m.group(2).strip())
    print(f'\n===== asiainsurancereview ({len(recs)} links) =====')
    for r in recs[:15]:
        print('  ', r[:120])
except Exception as e:
    print('air error', e)

# IA circular via web_extract result saved? check jina files sizes
for f in ['ia_press_jina', 'ia_circular_jina']:
    p = f'{D}/{f}.raw'
    print(f'\n--- {f}: {os.path.getsize(p) if os.path.exists(p) else "missing"} bytes')
