import os, json, re, html
from datetime import datetime, timedelta, timezone
import xml.etree.ElementTree as ET

BASE = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044/'
HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 24, 0, 0, tzinfo=HKT)   # 只看 10-24 起

out = []

def add(src, title, link, dt=None, desc=''):
    if not title:
        return
    out.append({'src': src, 'title': html.unescape(re.sub(r'\s+', ' ', title)).strip(),
                'link': link, 'dt': dt.isoformat() if dt else '', 'desc': html.unescape(re.sub(r'<[^>]+>', ' ', desc or ''))[:300]})

def pdate(s):
    if not s:
        return None
    s = s.strip()
    fmts = ['%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z', '%Y-%m-%dT%H:%M:%S%z',
            '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d', '%a, %d %b %Y %H:%M %z']
    for f in fmts:
        try:
            d = datetime.strptime(s, f)
            if d.tzinfo is None:
                d = d.replace(tzinfo=HKT if 'T' in s or len(s) > 10 else HKT)
            return d.astimezone(HKT)
        except Exception:
            pass
    return None

# ---------- 1. RSS feeds ----------
def parse_rss(path, src):
    try:
        raw = open(BASE + path, encoding='utf-8', errors='replace').read().replace('\ufeff', '')
        root = ET.fromstring(raw.encode('utf-8'))
    except Exception as e:
        print(f'[RSS fail] {src}: {e}')
        return
    for it in root.iter('item'):
        t = it.findtext('title') or ''
        l = it.findtext('link') or (it.findtext('guid') or '')
        d = pdate(it.findtext('pubDate') or it.findtext('{http://purl.org/dc/elements/1.1/}date') or '')
        desc = it.findtext('description') or ''
        if d and d < CUT:
            continue
        add(src, t, l, d, desc)
    A = '{http://www.w3.org/2005/Atom}'
    for it in root.iter(A + 'entry'):
        t = it.findtext(A + 'title') or ''
        l = ''
        for le in it.findall(A + 'link'):
            if le.get('rel') in (None, 'alternate'):
                l = le.get('href'); break
        d = pdate(it.findtext(A + 'updated') or it.findtext(A + 'published') or '')
        desc = it.findtext(A + 'summary') or it.findtext(A + 'content') or ''
        if d and d < CUT:
            continue
        add(src, t, l, d, desc)

parse_rss('insuranceasia_1792860323.raw', 'insuranceasia')
parse_rss('ibm_asia_1792860326.raw', 'insurancebusinessmag')
parse_rss('artemis_1792860325.raw', 'artemis')
parse_rss('rn_ws_feed.raw', 'reinsurancenews')
parse_rss('scmp_biz_1792860327.raw', 'scmp')
parse_rss('ian_hk_1792860322.raw', 'insuranceasianews')
parse_rss('govhk_1792860314.raw', 'govhk')

# ---------- 2. insuranceasianews WP JSON ----------
try:
    posts = json.load(open(BASE + 'insuranceasianews_1792860320.raw', encoding='utf-8'))
    for p in posts[:60]:
        d = pdate((p.get('date') or '').strip())
        if d and d < CUT:
            continue
        add('insuranceasianews', p['title']['rendered'], p.get('link', ''), d,
            re.sub(r'<[^>]+>', ' ', p.get('excerpt', {}).get('rendered', '')))
except Exception as e:
    print('[WP fail]', e)

# ---------- 3. DeepSeek search ----------
try:
    ds = json.load(open(BASE + 'ds_search.json', encoding='utf-8'))
    for r in ds:
        d = pdate(r.get('date') or '')
        if not d or d < CUT - timedelta(hours=24):
            continue
        out.append({'src': 'ds_search', 'title': r['title'], 'link': r['url'],
                    'dt': d.isoformat(), 'desc': (r.get('snippet') or '')[:300],
                    'q': r.get('q', ''), 'auth': r.get('authority')})
except Exception as e:
    print('[DS fail]', e)

# ---------- 4. HKMA ----------
txt = open(BASE + 'hkma_press_0045.html', encoding='utf-8', errors='replace').read()
hk = re.findall(r'href="(/eng/news-and-media/press-releases/2026/[^"]+)"[^>]*>\s*([^<]{10,200})', txt)
print('[HKMA href hits]', len(hk))
for l, t in hk[:25]:
    print('  HKMA|', t.strip()[:80], '|', l)

# ---------- 5. insurer pages: find dates ----------
for f, src in [('aia_0045.html', 'aia'), ('prudential_0045.html', 'prudential'),
               ('axa_0045.html', 'axa'), ('sunlife_0045.html', 'sunlife')]:
    h = open(BASE + f, encoding='utf-8', errors='replace').read()
    ds = sorted(set(re.findall(r'2026[-/年]\s?10[-/月]\s?2[0-9]', h)))
    print(f'[{src}] date-like tokens:', ds[:10], 'len', len(h))

print('\n=== window items (>=10-24) ===')
out.sort(key=lambda x: x['dt'], reverse=True)
for o in out:
    print(f"{o['dt'][:16]:16} | {o['src']:20} | {o['title'][:95]}")
print('\ntotal', len(out))
json.dump(out, open('/Users/leonliang/maoquanqingbao/data/_raw_1025_0044/cands_1025.json', 'w'), ensure_ascii=False, indent=1)
