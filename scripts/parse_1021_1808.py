#!/usr/bin/env python3
"""2026-10-21 18:08 parse: show items newer than 2026-10-20T18:08 HKT."""
import json, re, html
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 20, 18, 8, tzinfo=HKT)
D = 'data/_1021_1808/'


def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def rss_items(path, title_re=r'<title>(.*?)</title>', link_re=r'<link>(.*?)</link>'):
    """Generic RSS/Atom item splitter."""
    raw = open(path, encoding='utf-8', errors='replace').read()
    blocks = re.split(r'<item[\s>]', raw)[1:]
    out = []
    for b in blocks:
        b = b.split('</item>')[0]
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        l = re.search(r'<link>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', b, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S) or re.search(r'<dc:date>(.*?)</dc:date>', b, re.S)
        desc = re.search(r'<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>', b, re.S)
        dt = None
        if d:
            try:
                dt = parsedate_to_datetime(clean(d.group(1)))
            except Exception:
                try:
                    dt = datetime.fromisoformat(clean(d.group(1)).replace('Z', '+00:00'))
                except Exception:
                    dt = None
        if dt and dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        out.append({'title': clean(t.group(1)) if t else '',
                    'url': clean(l.group(1)) if l else '',
                    'date': dt.astimezone(HKT) if dt else None,
                    'desc': clean(desc.group(1))[:400] if desc else ''})
    return out


def show(name, items, cut=CUT, limit=12):
    fresh = [i for i in items if i['date'] and i['date'] >= cut]
    fresh.sort(key=lambda x: x['date'], reverse=True)
    print(f"\n===== {name}  (window {len(items)}, fresh {len(fresh)}) =====")
    for i in fresh[:limit]:
        print(f"[{i['date']:%m-%d %H:%M}] {i['title'][:110]}")
        print(f"   {i['url']}")
        if i['desc']:
            print(f"   ~{i['desc'][:200]}")


show('Artemis', rss_items(D + 'artemis.xml'))
show('ReinsuranceNews', rss_items(D + 'reins.xml'))
show('InsuranceBusiness', rss_items(D + 'ibm_rss.xml'))
show('govhk-zh', rss_items(D + 'govhk.xml'))
show('SCMP-92', rss_items(D + 'scmp.xml'))

# InsuranceAsiaNews wp-json
try:
    ian = json.load(open(D + 'ian.json', encoding='utf-8'))
    items = []
    for p in ian:
        dt = datetime.fromisoformat(p['date']).replace(tzinfo=timezone(timedelta(hours=-4)))  # WP site tz assumed
        items.append({'title': clean(html.unescape(p['title']['rendered'])), 'url': p['link'],
                      'date': dt.astimezone(HKT), 'desc': clean(p['excerpt']['rendered'])[:400]})
    show('InsuranceAsiaNews', items)
except Exception as e:
    print('IAN parse error', e)

# HKMA API
try:
    hj = json.load(open(D + 'hkma_api.json', encoding='utf-8'))
    recs = hj['result']['records']
    print(f"\n===== HKMA API (window {len(recs)}) =====")
    cnt = 0
    for r in recs:
        ds = r.get('date') or ''
        try:
            dt = datetime.strptime(ds[:10], '%Y-%m-%d').replace(tzinfo=HKT)
        except Exception:
            continue
        if dt >= CUT:
            print(f"[{ds}] {r.get('title','')[:110]}")
            print(f"   {r.get('link','')}")
            cnt += 1
    print('fresh:', cnt)
except Exception as e:
    print('HKMA api error', e)
