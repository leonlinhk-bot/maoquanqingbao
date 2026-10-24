import json, re, glob, os
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

HK = timezone(timedelta(hours=8))
D = 'data/_raw_1025_0205/'

def to_hk(dt):
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(HK)

def parse_rss(path, src):
    out = []
    try:
        tree = ET.parse(path)
    except Exception as e:
        print('!! parse fail', path, e)
        return out
    root = tree.getroot()
    for it in root.iter():
        tag = it.tag.split('}')[-1]
        if tag not in ('item', 'entry'):
            continue
        d = {}
        for ch in it:
            t = ch.tag.split('}')[-1]
            txt = (ch.text or '').strip()
            if t == 'link':
                d['link'] = txt or ch.get('href', '')
            elif t in ('title', 'pubDate', 'updated', 'published', 'description', 'summary'):
                d[t] = txt
            elif t == 'link' and ch.get('href'):
                d['link'] = ch.get('href')
        raw_date = d.get('pubDate') or d.get('published') or d.get('updated') or ''
        dt = None
        try:
            dt = to_hk(parsedate_to_datetime(raw_date))
        except Exception:
            for fmt in ('%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d'):
                try:
                    dt = to_hk(datetime.strptime(raw_date, fmt))
                    break
                except Exception:
                    pass
        if dt is None:
            continue
        out.append({'src': src, 'dt': dt.isoformat(), 'title': re.sub(r'<[^>]+>', '', d.get('title', '')),
                    'link': d.get('link', ''), 'desc': re.sub(r'<[^>]+>', ' ', d.get('description', '') or d.get('summary', ''))[:400]})
    return out

items = []
for f, s in [('artemis.xml', 'artemis'), ('ibm_rss.xml', 'ibm'), ('reins.xml', 'reinsurancene'),
             ('govhk.xml', 'govhk'), ('scmp.xml', 'scmp'), ('sthead.xml', 'stheadline'), ('aastocks.xml', 'aastocks')]:
    p = D + f
    if os.path.exists(p):
        items += parse_rss(p, s)

# insuranceasianews WP JSON
try:
    d = json.load(open(D + 'ian.json'))
    for p in d:
        dt = to_hk(datetime.strptime(p['date'], '%Y-%m-%dT%H:%M:%S'))
        items.append({'src': 'ian', 'dt': dt.isoformat(), 'title': re.sub(r'<[^>]+>', '', p['title']['rendered']),
                      'link': p['link'], 'desc': re.sub(r'<[^>]+>', ' ', p.get('excerpt', {}).get('rendered', ''))[:400]})
except Exception as e:
    print('!! ian fail', e)

# hkma api
try:
    d = json.load(open(D + 'hkma_api.json'))
    for r in d.get('result', {}).get('records', []):
        raw = r.get('date') or ''
        dt = None
        for fmt in ('%Y-%m-%d', '%d/%m/%Y'):
            try:
                dt = datetime.strptime(raw, fmt).replace(tzinfo=HK)
                break
            except Exception:
                pass
        if not dt:
            continue
        items.append({'src': 'hkma', 'dt': dt.isoformat(), 'title': (r.get('title') or '')[:160],
                      'link': r.get('link') or '', 'desc': ''})
except Exception as e:
    print('!! hkma fail', e)

items.sort(key=lambda x: x['dt'], reverse=True)
print('total parsed:', len(items), ' newest:', items[0]['dt'] if items else None)
print('=== items since 2026-10-24 00:00 ===')
for i in items:
    if i['dt'] >= '2026-10-24T00:00':
        print(i['dt'][:16], '|', i['src'][:12], '|', i['title'][:100])
        print('     ', i['link'][:120])
json.dump(items, open(D + 'parsed.json', 'w'), ensure_ascii=False, indent=1)
