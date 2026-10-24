#!/usr/bin/env python3
"""Round 3: HK financial media RSS (Mingpao / HKEJ / AAStocks / HK01 / ETNet)."""
import json, os, re, urllib.request, urllib.parse, gzip
from datetime import datetime, timedelta, timezone
import xml.etree.ElementTree as ET

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0052'
HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 24, 0, 0, tzinfo=HKT)
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36',
      'Accept-Language': 'zh-HK,zh;q=0.9,en;q=0.8'}

def get(url, name, timeout=40):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
            if r.headers.get('Content-Encoding') == 'gzip':
                data = gzip.decompress(data)
        open(f'{OUT}/{name}', 'wb').write(data)
        return data.decode('utf-8', 'replace')
    except Exception as e:
        print(f'[FAIL] {name}: {type(e).__name__} {str(e)[:100]}')
        return ''

def pdate(s):
    if not s: return None
    s = s.strip().replace('T', ' ')
    for f in ['%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z', '%Y-%m-%d %H:%M:%S%z',
              '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%d/%m/%Y %H:%M']:
        try:
            d = datetime.strptime(s, f)
            if d.tzinfo is None: d = d.replace(tzinfo=HKT)
            return d.astimezone(HKT)
        except Exception: pass
    return None

KW = re.compile(r'保險|保監|投保|保費|年金|危疾|醫保|強積金|MPF|再保|理賠|承保|保險業|policy|insur|annuit|underwrit|reinsur', re.I)
items = []
def rss(txt, src, kw=False):
    if not txt: return 0
    try:
        root = ET.fromstring(txt.replace('\ufeff', '').encode('utf-8'))
    except Exception as e:
        print(f'[XML fail] {src}: {e}'); return 0
    n = 0
    for it in root.iter('item'):
        t = it.findtext('title') or ''
        de = it.findtext('description') or ''
        if kw and not KW.search(t + de):
            continue
        d = pdate(it.findtext('pubDate') or '')
        items.append({'src': src, 'title': t, 'link': it.findtext('link') or '',
                      'dt': d.isoformat() if d else '', 'desc': re.sub(r'<[^>]+>', ' ', de)[:350]})
        n += 1
    return n

feeds = [
    ('https://news.mingpao.com/rss/pns/s00004.xml', 'mingpao_fin.xml', 'mingpao', True),
    ('https://www1.hkej.com/rss/onlinenews.xml', 'hkej.xml', 'hkej', True),
    ('http://www.aastocks.com/rss/news.xml', 'aastocks.xml', 'aastocks', True),
    ('https://www.hk01.com/rss/finance', 'hk01_fin.xml', 'hk01', True),
    ('https://www.etnet.com.hk/www/tc/rss/news.xml', 'etnet.xml', 'etnet', True),
    ('https://www.stheadline.com/rss/finance', 'sthead.xml', 'stheadline', True),
    ('https://www.hkfi.org.hk/en/media-centre/press-release/rss', 'hkfi.xml', 'hkfi', False),
]
for u, n, s, kw in feeds:
    c = rss(get(u, n), s, kw)
    print(f'[ok] {s}: {c} kw-matched')

win = [i for i in items if i['dt'] and datetime.fromisoformat(i['dt']) >= CUT]
win.sort(key=lambda x: x['dt'], reverse=True)
print(f'\n=== matched {len(items)}, in-window {len(win)} ===')
for i in win:
    print(f"{i['dt'][:16]} | {i['src']:12} | {i['title'][:95]}")
json.dump(items, open(f'{OUT}/all3.json', 'w'), ensure_ascii=False, indent=1)
