import re, html, glob, os
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'
HK = timezone(timedelta(hours=8))


def cliptxt(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


CUT = datetime(2026, 10, 5, 2, 0, tzinfo=HK)
allit = []
for f in sorted(glob.glob(CACHE + 'gn_*.xml')):
    name = os.path.basename(f)
    if name == 'gn_ia_site1.xml':
        continue
    data = open(f, encoding='utf-8', errors='replace').read()
    blocks = re.findall(r'<item>(.*?)</item>', data, re.S)
    n = 0
    for b in blocks:
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', b, re.S)
        l = re.search(r'<link>(.*?)</link>', b, re.S)
        title = cliptxt(t.group(1)) if t else ''
        src = cliptxt(s.group(1)) if s else ''
        dt = None
        if d:
            try:
                dt = parsedate_to_datetime(d.group(1).strip()).astimezone(HK)
            except Exception:
                pass
        if dt and dt >= CUT:
            n += 1
            allit.append((dt, src, name, title, l.group(1) if l else ''))
    print(f'{name}: {n} in window of {len(blocks)}')

print('\n===== ALL IN WINDOW (newest first) =====')
seen = set()
for dt, src, name, title, link in sorted(allit, key=lambda x: x[0], reverse=True):
    k = title[:50]
    if k in seen:
        continue
    seen.add(k)
    print(dt.strftime('%m-%d %H:%M'), '|', src[:22].ljust(22), '|', title[:105])
