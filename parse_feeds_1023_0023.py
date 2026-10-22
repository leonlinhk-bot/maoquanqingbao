import re, os, sys, html, json
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime
import xml.etree.ElementTree as ET

D = '/Users/leonliang/maoquanqingbao/.cache1023_0023'
HKT = timezone(timedelta(hours=8))
NOW = datetime.now(HKT)
CUT = NOW - timedelta(hours=30)

def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    return html.unescape(re.sub(r'\s+', ' ', t)).strip()

def parse_rss(path):
    raw = open(path, 'rb').read()
    raw = re.sub(rb'^\s*<\?xml[^>]*\?>', b'', raw)
    try:
        root = ET.fromstring(raw)
    except Exception as e:
        print(f'  !! parse fail {path}: {e}')
        return []
    out = []
    ns = {'content': 'http://purl.org/rss/1.0/modules/content/'}
    for it in root.iter('item'):
        title = strip((it.findtext('title') or ''))
        link = (it.findtext('link') or '').strip()
        date = it.findtext('pubDate') or it.findtext('{http://purl.org/dc/elements/1.1/}date') or ''
        desc = strip(it.findtext('description') or '')
        c = it.findtext('content:encoded', namespaces=ns) or ''
        cat = [strip(x.text or '') for x in it.findall('category')]
        dt = None
        if date:
            try:
                dt = parsedate_to_datetime(date)
            except Exception:
                for f in ('%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%SZ', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d'):
                    try:
                        dt = datetime.strptime(date.strip(), f); break
                    except Exception: pass
        if dt and dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        out.append({'title': title, 'link': link, 'dt': dt.astimezone(HKT) if dt else None,
                    'desc': desc, 'content': strip(c), 'cat': cat})
    for it in root.iter('{http://www.w3.org/2005/Atom}entry'):
        title = strip(it.findtext('{http://www.w3.org/2005/Atom}title') or '')
        link = ''
        for l in it.findall('{http://www.w3.org/2005/Atom}link'):
            if l.get('rel') in (None, 'alternate'):
                link = l.get('href') or ''; break
        date = it.findtext('{http://www.w3.org/2005/Atom}published') or it.findtext('{http://www.w3.org/2005/Atom}updated') or ''
        desc = strip(it.findtext('{http://www.w3.org/2005/Atom}summary') or '')
        c = it.findtext('{http://www.w3.org/2005/Atom}content') or ''
        dt = None
        if date:
            try:
                dt = datetime.fromisoformat(date.replace('Z', '+00:00'))
            except Exception: pass
        if dt and dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        out.append({'title': title, 'link': link, 'dt': dt.astimezone(HKT) if dt else None,
                    'desc': desc, 'content': strip(c), 'cat': []})
    return out

files = {
 'ian_hk.xml': 'insuranceasianews', 'ian_all.xml': 'insuranceasianews',
 'ibm_asia.xml': 'insurancebusinessmag', 'iaasia.xml': 'insuranceasia',
 'govhk.xml': 'govhk', 'artemis.xml': 'artemis', 'scmp.xml': 'scmp',
}
for f, key in files.items():
    p = os.path.join(D, f)
    if not os.path.exists(p): continue
    items = parse_rss(p)
    fresh = [i for i in items if i['dt'] and i['dt'] >= CUT]
    fresh.sort(key=lambda x: x['dt'], reverse=True)
    print(f'\n=== {f} [{key}]  total {len(items)}  within30h {len(fresh)}')
    for i in fresh[:14]:
        print(f"  {i['dt'].strftime('%m-%d %H:%M')} | {i['title'][:80]}")
        print(f"      {i['link']}")
