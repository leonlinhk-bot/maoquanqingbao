import os, re, json, html
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone, timedelta

D = '.cache1028_1010'
CUTOFF = datetime(2026, 10, 27, 21, 12, tzinfo=timezone(timedelta(hours=8)))

def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def parse_rss(path, label):
    if not os.path.exists(path):
        return []
    t = open(path, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item[ >].*?</item>', t, re.S) or re.findall(r'<entry[ >].*?</entry>', t, re.S)
    rows = []
    for it in items:
        title = clean(re.search(r'<title[^>]*>(.*?)</title>', it, re.S).group(1)) if re.search(r'<title[^>]*>(.*?)</title>', it, re.S) else ''
        link = re.search(r'<link[^>]*href="([^"]+)"', it)
        link = link.group(1) if link else ''
        if not link:
            m = re.search(r'<link[^>]*>(.*?)</link>', it, re.S)
            link = clean(m.group(1)) if m else ''
        d = ''
        for pat in [r'<pubDate[^>]*>(.*?)</pubDate>', r'<published[^>]*>(.*?)</published>', r'<updated[^>]*>(.*?)</updated>', r'<dc:date[^>]*>(.*?)</dc:date>']:
            m = re.search(pat, it, re.S)
            if m:
                d = clean(m.group(1))
                break
        desc = ''
        for pat in [r'<description[^>]*>(.*?)</description>', r'<summary[^>]*>(.*?)</summary>', r'<content:encoded[^>]*>(.*?)</content:encoded>']:
            m = re.search(pat, it, re.S)
            if m:
                desc = clean(m.group(1))
                break
        rows.append({'src': label, 'title': title, 'url': link, 'date': d, 'desc': desc[:300]})
    return rows

def when(s):
    s = (s or '').strip()
    if not s:
        return None
    try:
        dt = parsedate_to_datetime(s)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone(timedelta(hours=8)))
    except Exception:
        pass
    for fmt in ('%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d'):
        try:
            dt = datetime.strptime(s.replace('Z', '+0000') if fmt.endswith('%z') else s, fmt)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone(timedelta(hours=8)))
            return dt.astimezone(timezone(timedelta(hours=8)))
        except Exception:
            continue
    return None

allrows = []
for f, lab in [('insuranceasia2', 'insuranceasia'), ('ibm_asia', 'ibm'), ('artemis', 'artemis'),
               ('rn', 'reinsurancenews'), ('scmp', 'scmp'), ('govhk_zh', 'govhk'), ('govhk_en', 'govhk')]:
    allrows += parse_rss(f'{D}/{f}.raw', lab)

# ian = wp json
try:
    posts = json.load(open(f'{D}/ian.raw', encoding='utf-8'))
    for p in posts:
        allrows.append({'src': 'ian', 'title': clean(p.get('title', {}).get('rendered', '')),
                        'url': p.get('link', ''), 'date': p.get('date', ''),
                        'desc': clean(re.sub(r'<[^>]+>', '', p.get('excerpt', {}).get('rendered', '')))[:300]})
except Exception as e:
    print('ian parse fail', e)

print('=== parsed rows by source (with dates) ===')
for r in allrows:
    r['dt'] = when(r['date'])
fresh = [r for r in allrows if r['dt'] and r['dt'] >= CUTOFF]
print('total rows', len(allrows), '| fresh since cutoff', len(fresh))
print()
print('=== FRESH ITEMS (since 2026-10-27 21:12 HKT) ===')
for r in sorted(fresh, key=lambda x: x['dt']):
    print(f"[{r['src']}] {r['dt'].strftime('%m-%d %H:%M')} | {r['title'][:95]}")
    print(f"    {r['url']}")
print()
print('=== per-source newest 3 (for coverage audit) ===')
from collections import defaultdict
by = defaultdict(list)
for r in allrows:
    by[r['src']].append(r)
for s, rs in by.items():
    rs2 = sorted([x for x in rs if x['dt']], key=lambda x: x['dt'], reverse=True)[:3]
    print(f'-- {s} ({len(rs)} rows)')
    for r in rs2:
        print(f"   {r['dt'].strftime('%Y-%m-%d %H:%M')} | {r['title'][:80]}")
json.dump([{k: (v.strftime('%Y-%m-%dT%H:%M:%S+08:00') if k == 'dt' and v else v) for k, v in r.items()} for r in allrows],
          open(f'{D}/_parsed.json', 'w'), ensure_ascii=False, indent=1)
