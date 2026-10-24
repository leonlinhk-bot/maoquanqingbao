#!/usr/bin/env python3
"""Fresh fetch of all feeds for 10-24/10-25 window."""
import json, os, re, urllib.request, urllib.parse, gzip, io
from datetime import datetime, timedelta, timezone
import xml.etree.ElementTree as ET

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0052'
os.makedirs(OUT, exist_ok=True)
HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 24, 0, 0, tzinfo=HKT)
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36'}

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
        print(f'[FAIL] {name}: {type(e).__name__} {str(e)[:120]}')
        return ''

def pdate(s):
    if not s: return None
    s = s.strip()
    for f in ['%a, %d %b %Y %H:%M:%S %z', '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%S',
              '%Y-%m-%d %H:%M:%S', '%Y-%m-%d', '%a, %d %b %Y %H:%M:%S %Z']:
        try:
            d = datetime.strptime(s, f)
            if d.tzinfo is None: d = d.replace(tzinfo=HKT)
            return d.astimezone(HKT)
        except Exception: pass
    return None

def rss_items(txt, src, tag=''):
    if not txt: return []
    res = []
    try:
        raw = txt.replace('\ufeff', '')
        root = ET.fromstring(raw.encode('utf-8'))
    except Exception as e:
        print(f'[XML fail] {src}{tag}: {e}'); return []
    for it in root.iter('item'):
        d = pdate(it.findtext('pubDate') or '')
        res.append({'src': src + tag, 'title': it.findtext('title') or '',
                    'link': it.findtext('link') or '', 'dt': d.isoformat() if d else '',
                    'desc': re.sub(r'<[^>]+>', ' ', it.findtext('description') or '')[:400]})
    A = '{http://www.w3.org/2005/Atom}'
    for it in root.iter(A + 'entry'):
        l = ''
        for le in it.findall(A + 'link'):
            if le.get('rel') in (None, 'alternate'): l = le.get('href'); break
        d = pdate(it.findtext(A + 'updated') or it.findtext(A + 'published') or '')
        res.append({'src': src + tag, 'title': it.findtext(A + 'title') or '', 'link': l,
                    'dt': d.isoformat() if d else '',
                    'desc': re.sub(r'<[^>]+>', ' ', (it.findtext(A + 'summary') or it.findtext(A + 'content') or ''))[:400]})
    return res

allitems = []

# --- Google News RSS (fresh, time-filtered) ---
gn = [
    ('香港保险 最新', 'gn_hk_zh'),
    ('Hong Kong insurance news', 'gn_hk_en'),
    ('保监局 保险业监管局', 'gn_ia'),
    ('Hong Kong family office', 'gn_fo'),
    ('insurance Asia reinsurance', 'gn_asia'),
    ('强积金 MPF 保险', 'gn_mpf'),
]
for q, name in gn:
    u = 'https://news.google.com/rss/search?' + urllib.parse.urlencode(
        {'q': q + ' when:3d', 'hl': 'zh-HK' if any('\u4e00' <= c <= '\u9fff' for c in q) else 'en-US',
         'gl': 'HK', 'ceid': 'HK:zh-Hant'})
    txt = get(u, name + '.xml')
    allitems += rss_items(txt, 'gnews', ':' + name)

# --- direct feeds ---
feeds = [
    ('https://www.insurancebusinessmag.com/asia/rss/', 'ibm_asia.xml', 'ibm'),
    ('https://insuranceasia.com/insurance/rss.xml', 'iaasia.xml', 'iaasia'),
    ('https://insuranceasianews.com/wp-json/wp/v2/posts?per_page=30', 'ian.json', 'ian'),
    ('https://www.artemis.bm/news/feed/', 'artemis.xml', 'artemis'),
    ('https://www.reinsurancene.ws/feed/', 'rnws.xml', 'rnws'),
    ('https://www.scmp.com/rss/92/feed', 'scmp_biz.xml', 'scmp'),
    ('https://www.info.gov.hk/gia/rss/general_zh.xml', 'govhk.xml', 'govhk'),
]
for u, name, src in feeds:
    if u.endswith('.json') or 'wp-json' in u:
        txt = get(u, name)
        try:
            posts = json.loads(txt)
            for p in posts:
                d = pdate(p.get('date', '').replace('T', ' '))
                allitems.append({'src': src, 'title': p['title']['rendered'], 'link': p.get('link', ''),
                                 'dt': d.isoformat() if d else '',
                                 'desc': re.sub(r'<[^>]+>', ' ', p.get('excerpt', {}).get('rendered', ''))[:400]})
        except Exception as e:
            print('[WP fail]', e)
    else:
        allitems += rss_items(get(u, name), src)

# --- IA RSS attempts ---
for u, name in [('https://www.ia.org.hk/en/infocenter/press_releases/rss.xml', 'ia_rss.xml'),
                ('https://www.ia.org.hk/en/rss/press_releases.xml', 'ia_rss2.xml')]:
    txt = get(u, name)
    if txt and '<' in txt and 'Just a moment' not in txt:
        print('[IA RSS OK]', name, len(txt))
        allitems += rss_items(txt, 'ia')
    else:
        print('[IA RSS blocked]', name, len(txt))

win = [i for i in allitems if i['dt'] and datetime.fromisoformat(i['dt']) >= CUT]
win.sort(key=lambda x: x['dt'], reverse=True)
print(f'\n=== total {len(allitems)}, in-window {len(win)} ===')
for i in win:
    print(f"{i['dt'][:16]} | {i['src']:24} | {i['title'][:90]}")
json.dump(allitems, open(f'{OUT}/all.json', 'w'), ensure_ascii=False, indent=1)
