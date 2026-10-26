import json, re, os
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET

CUT = datetime(2026, 10, 25, 18, 12, tzinfo=timezone(timedelta(hours=8)))
DAY0 = datetime(2026, 10, 23, 0, 0, tzinfo=timezone(timedelta(hours=8)))

def parse_date(s):
    if not s:
        return None
    s = s.strip()
    fmts = ['%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z', '%Y-%m-%dT%H:%M:%S%z',
            '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d']
    for f in fmts:
        try:
            d = datetime.strptime(s, f)
            if d.tzinfo is None:
                d = d.replace(tzinfo=timezone(timedelta(hours=8)))
            return d
        except Exception:
            pass
    return None

def strip_tags(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def parse_rss(path, label):
    raw = open(path, encoding='utf-8', errors='replace').read()
    rows = []
    try:
        root = ET.fromstring(raw.encode('utf-8'))
    except Exception as e:
        print(f'  {label}: XML parse error {e}')
        return rows
    for it in root.iter():
        tag = it.tag.split('}')[-1]
        if tag not in ('item', 'entry'):
            continue
        d = {}
        for ch in it:
            k = ch.tag.split('}')[-1]
            if k == 'link':
                d['link'] = (ch.text or ch.attrib.get('href') or '').strip()
            elif k in ('title', 'description', 'summary', 'content', 'pubDate', 'published', 'updated', 'date', 'encoded'):
                d[k] = strip_tags(ch.text if ch.text else ''.join(ch.itertext()))
        dt = parse_date(d.get('pubDate') or d.get('published') or d.get('updated') or d.get('date') or '')
        rows.append({'src': label, 'date': dt, 'title': d.get('title', ''), 'link': d.get('link', ''),
                     'desc': (d.get('description') or d.get('summary') or d.get('content') or '')[:300]})
    return rows

feeds = [('insuranceasia2', 'insuranceasia'), ('ibm_asia', 'insurancebusinessmag'),
         ('artemis', 'artemis'), ('rn', 'reinsurancenews'), ('govhk_zh', 'govhk'),
         ('govhk_en', 'govhk_en'), ('scmp', 'scmp')]

allrows = []
for f, label in feeds:
    p = f'.cache1025_2108/{f}.raw'
    if not os.path.exists(p):
        continue
    rows = parse_rss(p, label)
    dated = [r for r in rows if r['date']]
    recent = [r for r in dated if r['date'] >= DAY0]
    print(f'{label:20s} items={len(rows):3d} dated={len(dated):3d} since23rd={len(recent):3d}', end='  ')
    if dated:
        print('newest=', max(r['date'] for r in dated).strftime('%Y-%m-%d %H:%M'))
    else:
        print()
    allrows += recent

# IAN wp-json
p = '.cache1025_2108/ian.raw'
if os.path.exists(p):
    try:
        data = json.loads(open(p, encoding='utf-8', errors='replace').read())
        for post in data:
            dt = parse_date(post.get('date_gmt', '').replace('T', ' '))
            if dt:
                dt = dt.replace(tzinfo=timezone.utc)
            allrows.append({'src': 'ian', 'date': dt, 'title': strip_tags(post.get('title', {}).get('rendered', '')),
                            'link': post.get('link', ''), 'desc': strip_tags(post.get('excerpt', {}).get('rendered', ''))[:300]})
        print('ian posts', len(data), 'newest', max(x['date'] for x in allrows if x['src'] == 'ian').astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M'))
    except Exception as e:
        print('ian parse fail', e)

print('\n=== SINCE 2026-10-25 18:12 ===')
n = 0
for r in sorted([x for x in allrows if x['date'] and x['date'] >= CUT], key=lambda x: x['date'], reverse=True):
    n += 1
    print(r['date'].astimezone(timezone(timedelta(hours=8))).strftime('%m-%d %H:%M'), '|', r['src'], '|', r['title'][:95], '|', r['link'][:100])
print('count', n)

print('\n=== ALL DATED SINCE 10-23 (for context) ===')
for r in sorted([x for x in allrows if x['date'] and x['date'] >= DAY0], key=lambda x: x['date'], reverse=True):
    print(r['date'].astimezone(timezone(timedelta(hours=8))).strftime('%m-%d %H:%M'), '|', r['src'], '|', r['title'][:90])

json.dump([{**r, 'date': r['date'].isoformat() if r['date'] else None} for r in allrows],
          open('.cache1025_2108/rows.json', 'w'), ensure_ascii=False, indent=1)
