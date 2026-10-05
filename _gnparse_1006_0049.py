import re, html, glob, os
from datetime import datetime, timezone, timedelta

CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'
HK = timezone(timedelta(hours=8))


def cliptxt(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


CUT = datetime(2026, 10, 5, 2, 0, tzinfo=HK)   # last check Oct5 02:39
allit = []
for f in sorted(glob.glob(CACHE + 'gn_*.xml')):
    name = os.path.basename(f)
    data = open(f, encoding='utf-8', errors='replace').read()
    blocks = re.findall(r'<item>(.*?)</item>', data, re.S)
    print(f'===== {name}  ({len(blocks)} items) =====')
    for b in blocks:
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', b, re.S)
        l = re.search(r'<link>(.*?)</link>', b, re.S)
        title = cliptxt(t.group(1)) if t else ''
        src = cliptxt(s.group(1)) if s else ''
        ds = (d.group(1) if d else '').strip()
        try:
            dt = datetime.strptime(ds, '%a, %d %b %Y %H:%M:%S %z').astimezone(HK)
        except Exception:
            dt = None
        if dt and dt >= CUT:
            print('  *', dt.strftime('%m-%d %H:%M'), '|', src[:24], '|', title[:100])
            allit.append((dt, src, title, l.group(1) if l else ''))
    print()

print('===== ALL IN WINDOW (sorted) =====')
seen = set()
for dt, src, title, link in sorted(allit, key=lambda x: x[0], reverse=True):
    k = title[:60]
    if k in seen:
        continue
    seen.add(k)
    print(dt.strftime('%m-%d %H:%M'), '|', src[:26].ljust(26), '|', title[:110])
