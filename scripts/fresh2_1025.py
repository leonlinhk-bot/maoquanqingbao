#!/usr/bin/env python3
"""Round 2: more sources for Sat 10-24 / Sun 10-25 early."""
import json, os, re, urllib.request, urllib.parse, gzip
from datetime import datetime, timedelta, timezone
import xml.etree.ElementTree as ET

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0052'
os.makedirs(OUT, exist_ok=True)
HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 24, 0, 0, tzinfo=HKT)
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'}

def get(url, name, timeout=45):
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = r.read()
            if r.headers.get('Content-Encoding') == 'gzip':
                data = gzip.decompress(data)
        open(f'{OUT}/{name}', 'wb').write(data)
        return data.decode('utf-8', 'replace')
    except Exception as e:
        print(f'[FAIL] {name}: {type(e).__name__} {str(e)[:110]}')
        return ''

def pdate(s):
    if not s: return None
    s = s.strip().replace('T', ' ')
    for f in ['%a, %d %b %Y %H:%M:%S %z', '%Y-%m-%d %H:%M:%S%z', '%Y-%m-%d %H:%M:%S',
              '%Y-%m-%d %H:%M', '%Y-%m-%d']:
        try:
            d = datetime.strptime(s, f)
            if d.tzinfo is None: d = d.replace(tzinfo=HKT)
            return d.astimezone(HKT)
        except Exception: pass
    return None

items = []
def rss(txt, src):
    if not txt: return
    try:
        root = ET.fromstring(txt.replace('\ufeff', '').encode('utf-8'))
    except Exception as e:
        print(f'[XML fail] {src}: {e}'); return
    for it in root.iter('item'):
        d = pdate(it.findtext('pubDate') or '')
        items.append({'src': src, 'title': it.findtext('title') or '', 'link': it.findtext('link') or '',
                      'dt': d.isoformat() if d else '', 'desc': re.sub(r'<[^>]+>', ' ', it.findtext('description') or '')[:400]})

# 1. insuranceasia correct rss
rss(get('https://insuranceasia.com/rss.xml', 'iaasia2.xml'), 'iaasia')
# 2. insuranceasianews 80 posts
txt = get('https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=80', 'ian80.json')
try:
    for p in json.loads(txt):
        d = pdate(p.get('date', ''))
        items.append({'src': 'ian', 'title': p['title']['rendered'], 'link': p.get('link', ''),
                      'dt': d.isoformat() if d else '',
                      'desc': re.sub(r'<[^>]+>', ' ', p.get('excerpt', {}).get('rendered', ''))[:400]})
except Exception as e: print('[ian80]', e)
# 3. IBM asia full list page
h = get('https://www.insurancebusinessmag.com/asia/news/breaking-news/', 'ibm_list.html')
if h:
    dts = sorted(set(re.findall(r'(2026-10-2[3-5])', h)))
    print('[IBM list] dates present:', dts, 'len', len(h))
# 4. google news per-source
gn = [
    ('site:mingpao.com 保險', 'gn_mingpao'),
    ('site:hket.com 保險', 'gn_hket'),
    ('site:mpfinance.com 保險', 'gn_mpf2'),
    ('site:hk01.com 保險', 'gn_hk01'),
    ('site:stheadline.com 保險', 'gn_sthead'),
    ('香港 保險 監管 新規', 'gn_hk_reg'),
    ('Hong Kong insurance regulator circular', 'gn_hk_circ'),
    ('insurance Hong Kong wealth management', 'gn_hk_wm'),
]
for q, name in gn:
    zh = any('\u4e00' <= c <= '\u9fff' for c in q)
    u = 'https://news.google.com/rss/search?' + urllib.parse.urlencode(
        {'q': q + ' when:4d', 'hl': 'zh-HK' if zh else 'en-US', 'gl': 'HK', 'ceid': 'HK:zh-Hant' if zh else 'HK:en'})
    rss(get(u, name + '.xml'), 'gnews:' + name)

# 5. NFRA
h = get('https://www.nfra.gov.cn/cn/view/pages/index/index.html', 'nfra2.html')
if h:
    links = re.findall(r'href="([^"]*item[^"]*\.html)"[^>]*>([^<]{8,80})', h)
    print('[NFRA links]', len(links))
    for l, t in links[:15]: print('   ', t.strip()[:60], '|', l[:80])

win = [i for i in items if i['dt'] and datetime.fromisoformat(i['dt']) >= CUT]
win.sort(key=lambda x: x['dt'], reverse=True)
print(f'\n=== total {len(items)}, in-window {len(win)} ===')
for i in win:
    print(f"{i['dt'][:16]} | {i['src']:22} | {i['title'][:92]}")
json.dump(items, open(f'{OUT}/all2.json', 'w'), ensure_ascii=False, indent=1)
