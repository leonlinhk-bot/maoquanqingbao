import json, re, os, html
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
HKT = timezone(timedelta(hours=8))
NOW = datetime(2026, 10, 20, 18, 8, tzinfo=HKT)
CUT = NOW - timedelta(hours=48)


def norm_date(s):
    s = s.strip()
    for fmt in ('%a, %d %b %Y %H:%M:%S %z', '%a, %d %b %Y %H:%M:%S %Z'):
        try:
            d = parsedate_to_datetime(s)
            if d.tzinfo is None:
                d = d.replace(tzinfo=timezone.utc)
            return d.astimezone(HKT)
        except Exception:
            pass
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})', s)
    if m:
        try:
            return datetime(*[int(x) for x in m.groups()], tzinfo=timezone.utc).astimezone(HKT)
        except Exception:
            pass
    return None


def rss_items(fn, label):
    p = os.path.join(BASE, fn)
    if not os.path.exists(p):
        return []
    txt = open(p, encoding='utf-8', errors='ignore').read()
    out = []
    for m in re.finditer(r'<item[ >].*?</item>', txt, re.S):
        block = m.group(0)
        t = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', block, re.S)
        l = re.search(r'<link[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</link>', block, re.S)
        d = re.search(r'<pubDate[^>]*>(.*?)</pubDate>', block, re.S)
        if not d:
            d = re.search(r'<dc:date[^>]*>(.*?)</dc:date>', block, re.S)
        if not (t and l and d):
            continue
        dt = norm_date(d.group(1))
        if not dt:
            continue
        out.append({'src': label, 'title': html.unescape(re.sub(r'<[^>]+>', '', t.group(1))).strip(),
                    'url': l.group(1).strip(), 'date': dt})
    return out


rows = []
rows += rss_items('insuranceasia.xml', 'insuranceasia')
rows += rss_items('ibm_rss.xml', 'insurancebusinessmag')
rows += rss_items('artemis.xml', 'artemis')
rows += rss_items('rn.xml', 'reinsurancenews')
rows += rss_items('govhk.xml', 'govhk')

# insuranceasianews wp json
p = os.path.join(BASE, 'ian.json')
if os.path.exists(p):
    try:
        js = json.load(open(p, encoding='utf-8'))
        for it in js:
            dt = norm_date(it.get('date_gmt', '') + 'Z') or norm_date(it.get('date', ''))
            if not dt:
                continue
            rows.append({'src': 'insuranceasianews',
                         'title': html.unescape(re.sub(r'<[^>]+>', '', it['title']['rendered'])).strip(),
                         'url': it['link'], 'date': dt})
    except Exception as e:
        print('ian err', e)

rows = [r for r in rows if r['date'] >= CUT]
rows.sort(key=lambda r: r['date'], reverse=True)
print('=== FEED ITEMS in 48h:', len(rows))
for r in rows:
    print(r['date'].strftime('%m-%d %H:%M'), '|', r['src'], '|', r['title'][:95])
    print('    ', r['url'])
