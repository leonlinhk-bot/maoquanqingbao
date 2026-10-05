import json, re, os
from datetime import datetime, timezone, timedelta

BASE = '/Users/leonliang/maoquanqingbao'
CACHE = os.path.join(BASE, 'data/_cache1006_0049')
HK = timezone(timedelta(hours=8))

live = json.load(open(os.path.join(BASE, 'data/live-items.json')))
items = live['items']
exist_ids = set()
exist_urls = set()
exist_titles = set()
for it in items:
    exist_ids.add(it.get('id', ''))
    u = (it.get('originalUrl') or '').strip().rstrip('/')
    if u:
        exist_urls.add(u)
    t = it.get('title', {})
    if isinstance(t, dict):
        exist_titles.add((t.get('sc') or '').strip()[:40])
print('existing items:', len(items), 'urls:', len(exist_urls))

def cmp(u):
    return u.strip().rstrip('/')

# ---------- insuranceasia RSS ----------
import xml.etree.ElementTree as ET
out = []
tree = ET.parse(os.path.join(CACHE, 'insuranceasia.xml'))
for it in tree.iter('item'):
    title = (it.findtext('title') or '').strip()
    link = (it.findtext('link') or '').strip()
    pd = (it.findtext('pubDate') or '').strip()
    try:
        dt = datetime.strptime(pd, '%a, %d %b %Y %H:%M:%S %z')
    except Exception:
        dt = None
    out.append(('insuranceasia', dt, title, link))

# ---------- insuranceasianews WP API ----------
try:
    posts = json.load(open(os.path.join(CACHE, 'ian.json')))
    for p in posts:
        title = re.sub('<[^>]+>', '', (p.get('title', {}) or {}).get('rendered', '')).strip()
        link = p.get('link', '')
        d = p.get('date_gmt') or p.get('date')
        dt = None
        if d:
            dt = datetime.fromisoformat(d.replace('Z', '+00:00')).astimezone(HK)
        out.append(('insuranceasianews', dt, title, link))
except Exception as e:
    print('ian err', e)

# ---------- HKMA press ----------
html = open(os.path.join(CACHE, 'hkma_press.html'), encoding='utf-8', errors='ignore').read()
hkma = re.findall(r'href="(/eng/news-and-media/press-releases/[^"]+)"[^>]*>\s*([^<]{5,300})', html)
seen = set()
for href, txt in hkma:
    t = re.sub(r'\s+', ' ', txt).strip()
    if href in seen or len(t) < 8:
        continue
    seen.add(href)
    out.append(('hkma', None, t, 'https://www.hkma.gov.hk' + href))

# ---------- info.gov.hk RSS ----------
for fn, lang in (('govhk_zh.xml', 'zh'), ('govhk_en.xml', 'en')):
    try:
        tr = ET.parse(os.path.join(CACHE, fn))
        for it in tr.iter('item'):
            title = (it.findtext('title') or '').strip()
            link = (it.findtext('link') or '').strip()
            pd = (it.findtext('pubDate') or '').strip()
            dt = None
            for fmt in ('%a, %d %b %Y %H:%M:%S %z', '%Y-%m-%dT%H:%M:%S%z'):
                try:
                    dt = datetime.strptime(pd, fmt); break
                except Exception:
                    pass
            out.append(('govhk_' + lang, dt, title, link))
    except Exception as e:
        print('govhk err', fn, e)

# ---------- artemis ----------
html = open(os.path.join(CACHE, 'artemis.html'), encoding='utf-8', errors='ignore').read()
art = re.findall(r'<a[^>]+href="(https://www\.artemis\.bm/news/[^"]+)"[^>]*>([^<]{10,200})</a>', html)
seen = set()
for href, txt in art:
    t = re.sub(r'\s+', ' ', txt).strip()
    if href in seen:
        continue
    seen.add(href)
    out.append(('artemis', None, t, href))

# ---------- insurancebusinessmag ----------
html = open(os.path.join(CACHE, 'ibm.html'), encoding='utf-8', errors='ignore').read()
ibm = re.findall(r'href="(/asia/news/[^"]+)"[^>]*>\s*([^<]{10,250})', html)
seen = set()
for href, txt in ibm:
    t = re.sub(r'\s+', ' ', txt).strip()
    if href in seen or len(t) < 15:
        continue
    seen.add(href)
    out.append(('insurancebusinessmag', None, t, 'https://www.insurancebusinessmag.com' + href))

new = []
for src, dt, title, link in out:
    c = cmp(link)
    ts = dt.astimezone(HK).strftime('%Y-%m-%d %H:%M') if dt else ''
    fresh = c not in exist_urls
    if fresh:
        new.append((src, ts, title[:120], link))

print('\n===== newest per source (all fetched) =====')
from collections import defaultdict
by = defaultdict(list)
for src, dt, title, link in out:
    by[src].append((dt, title, link))
for src, arr in by.items():
    arr.sort(key=lambda x: (x[0] is not None, x[0] or datetime(1970,1,1,tzinfo=HK)), reverse=True)
    print(f'--- {src} ({len(arr)}) ---')
    for dt, title, link in arr[:8]:
        ts = dt.astimezone(HK).strftime('%Y-%m-%d %H:%M') if dt else '----'
        flag = 'NEW' if cmp(link) not in exist_urls else '   '
        print(f'  {flag} {ts} | {title[:95]} | {link[:110]}')

print('\n===== NEW CANDIDATES =====', len(new))
