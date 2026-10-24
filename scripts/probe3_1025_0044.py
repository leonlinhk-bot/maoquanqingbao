#!/usr/bin/env python3
import os, re, urllib.request, html, json, email.utils
from datetime import datetime, timezone, timedelta

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044'
HKT = timezone(timedelta(hours=8))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36'
CUT = datetime(2026, 10, 24, 0, 0, tzinfo=HKT)

TARGETS = [
    ('rn_ws', 'https://www.reinsurancene.ws/feed/'),
    ('hk01_fin', 'https://www.hk01.com/rss/channel/%E8%B2%A1%E7%B6%93'),
    ('stheadline', 'https://www.stheadline.com/rss/finance'),
    ('mingpao_fin', 'https://news.mingpao.com/rss/pns/s00004.xml'),
    ('hkfi2', 'https://www.hkfi.org.hk/en/media-centre/press-release.html'),
    ('ibm_global', 'https://www.insurancebusinessmag.com/rss/'),
    ('fstb', 'https://www.fstb.gov.hk/eng/rss/press_releases.xml'),
]

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': '*/*'})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read()

def rss(raw):
    txt = raw.decode('utf-8', 'ignore')
    out = []
    for m in re.finditer(r'<(item|entry)>(.*?)</\1>', txt, re.S):
        b = m.group(2)
        def g(tag):
            mm = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', b, re.S)
            if not mm: return ''
            v = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', mm.group(1), flags=re.S)
            return html.unescape(re.sub(r'<[^>]+>', '', v)).strip()
        lk = re.search(r'<link[^>]*href="([^"]+)"', b)
        link = g('link') or (lk.group(1) if lk else '')
        out.append({'title': g('title'), 'link': link,
                    'date': g('pubDate') or g('published') or g('updated') or g('dc:date')})
    return out

def pd(s):
    s = (s or '').strip()
    if not s: return None
    for f in ('%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z',
              '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S'):
        try:
            d = datetime.strptime(s, f)
            if d.tzinfo is None: d = d.replace(tzinfo=HKT)
            return d.astimezone(HKT)
        except Exception: pass
    try:
        d = email.utils.parsedate_to_datetime(s)
        if d and d.tzinfo is None: d = d.replace(tzinfo=timezone.utc)
        return d.astimezone(HKT) if d else None
    except Exception: return None

keep = []
for key, url in TARGETS:
    try:
        raw = get(url)
    except Exception as e:
        print(f'FAIL {key:12s} {type(e).__name__}: {str(e)[:70]}'); continue
    open(os.path.join(OUT, f'{key}_feed.raw'), 'wb').write(raw)
    its = rss(raw)
    recent = []
    for it in its:
        d = pd(it['date'])
        if d and d >= CUT:
            recent.append((d, it))
    print(f'OK   {key:12s} {len(its):3d} items, {len(recent)} since 10-24')
    for d, it in recent[:8]:
        print(f"   {d.strftime('%Y-%m-%d %H:%M')} | {it['title'][:90]}")
        print(f"      {it['link'][:115]}")
        keep.append({'src': key, 'date': d.strftime('%Y-%m-%dT%H:%M:%S%z'),
                     'title': it['title'], 'link': it['link']})
json.dump(keep, open(os.path.join(OUT, 'feeds_recent2.json'), 'w'), ensure_ascii=False, indent=1)
print('\nkept', len(keep))
