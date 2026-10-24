#!/usr/bin/env python3
"""Parse raw probes; print items with date >= 2026-10-23 (edge) for review."""
import os, re, json, glob, email.utils, html
from datetime import datetime, timezone, timedelta

OUT = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044'
CUT = datetime(2026, 10, 23, 0, 0, tzinfo=timezone(timedelta(hours=8)))

def fname(k):
    g = sorted(glob.glob(os.path.join(OUT, k + '_*.raw')))
    return g[-1] if g else None

def latest(k):
    p = fname(k)
    return open(p, 'rb').read() if p else b''

def rss_items(raw, key):
    txt = raw.decode('utf-8', 'ignore')
    out = []
    for m in re.finditer(r'<item>(.*?)</item>', txt, re.S):
        b = m.group(1)
        def g(tag):
            mm = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', b, re.S)
            if not mm: return ''
            v = mm.group(1)
            v = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', v, flags=re.S)
            return html.unescape(re.sub(r'<[^>]+>', '', v)).strip()
        out.append({'key': key, 'title': g('title'), 'link': g('link') or g('guid'),
                    'date': g('pubDate') or g('dc:date') or g('published') or g('updated'),
                    'desc': g('description')[:300]})
    if not out:  # atom
        for m in re.finditer(r'<entry>(.*?)</entry>', txt, re.S):
            b = m.group(1)
            def g(tag):
                mm = re.search(rf'<{tag}[^>]*>(.*?)</{tag}>', b, re.S)
                if not mm: return ''
                v = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', mm.group(1), flags=re.S)
                return html.unescape(re.sub(r'<[^>]+>', '', v)).strip()
            lk = re.search(r'<link[^>]*href="([^"]+)"', b)
            out.append({'key': key, 'title': g('title'), 'link': lk.group(1) if lk else '',
                        'date': g('published') or g('updated'), 'desc': g('summary')[:300]})
    return out

def parse_dt(s):
    s = (s or '').strip()
    if not s: return None
    for f in ('%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z', '%Y-%m-%dT%H:%M:%S%z',
              '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d'):
        try:
            d = datetime.strptime(s, f)
            if d.tzinfo is None:
                d = d.replace(tzinfo=timezone(timedelta(hours=8)))
            return d.astimezone(timezone(timedelta(hours=8)))
        except Exception:
            pass
    try:
        d = email.utils.parsedate_to_datetime(s)
        if d and d.tzinfo is None:
            d = d.replace(tzinfo=timezone.utc)
        return d.astimezone(timezone(timedelta(hours=8))) if d else None
    except Exception:
        return None

print('=' * 20, 'RSS/ATOM lanes')
allrows = []
for k in ('govhk', 'ian_hk', 'insuranceasia', 'artemis', 'ibm_asia', 'scmp_biz'):
    raw = latest(k)
    if not raw:
        print(f'-- {k}: no file'); continue
    its = rss_items(raw, k)
    print(f'-- {k}: {len(its)} items')
    for it in its:
        d = parse_dt(it['date'])
        it['dt'] = d
        if d and d >= CUT:
            allrows.append(it)
            print(f"   {d.strftime('%Y-%m-%d %H:%M')} | {it['title'][:95]}")
            print(f"      {it['link'][:120]}")
print('=' * 20, 'InsuranceAsiaNews WP API')
raw = latest('insuranceasianews')
if raw:
    try:
        j = json.loads(raw.decode('utf-8', 'ignore'))
        for p in j[:40]:
            d = parse_dt(p.get('date_gmt', '').replace('T', ' ')) if p.get('date_gmt') else None
            print(f"   {p.get('date','')[:16]} | {html.unescape(p['title']['rendered'])[:90]}")
            print(f"      {p['link']}")
    except Exception as e:
        print('parse fail', e)

json.dump([{k: (v.strftime('%Y-%m-%dT%H:%M:%S%z') if k == 'dt' and v else v) for k, v in r.items()} for r in allrows],
          open(os.path.join(OUT, 'rss_recent.json'), 'w'), ensure_ascii=False, indent=1)
print('\nsaved rss_recent.json', len(allrows))
