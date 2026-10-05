import json, re, html, os
from datetime import datetime, timezone, timedelta
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'
HK = timezone(timedelta(hours=8))


def cl(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


print('##### IAN WP API (newer than 2026-10-04 20:00 HK) #####')
posts = json.load(open(CACHE + 'ian.json'))
for p in posts:
    d = p.get('date_gmt')
    dt = datetime.fromisoformat(d.replace('Z', '+00:00')).astimezone(HK) if d else None
    if dt and dt >= datetime(2026, 10, 4, 20, 0, tzinfo=HK):
        print('---', dt.strftime('%Y-%m-%d %H:%M'), '|', cl(p['title']['rendered']))
        print('    URL:', p.get('link'))
        exc = cl((p.get('excerpt') or {}).get('rendered', ''))
        print('    EXC:', exc[:600])

print('\n##### SCMP feed #####')
import xml.etree.ElementTree as ET
tr = ET.parse(CACHE + 'scmp_ins.xml')
for it in tr.iter('item'):
    t = (it.findtext('title') or '').strip()
    l = (it.findtext('link') or '').strip()
    pd = (it.findtext('pubDate') or '').strip()
    try:
        dt = datetime.strptime(pd, '%a, %d %b %Y %H:%M:%S %z').astimezone(HK)
        ds = dt.strftime('%Y-%m-%d %H:%M')
    except Exception:
        ds = pd
    print(' ', ds, '|', t[:100])
    print('     ', l[:120])
