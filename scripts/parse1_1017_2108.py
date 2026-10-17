import re, json, os, html
from pathlib import Path

D = Path('.cache1017_2108')

def rd(n):
    p = D / n
    return p.read_text('utf-8', errors='ignore') if p.exists() else ''

def strip(t):
    t = re.sub(r'<[^>]+>', ' ', t or '')
    t = html.unescape(t)
    return re.sub(r'\s+', ' ', t).strip()

out = []

# RSS style
for fn, src in [('rn.xml','reinsurancenews'), ('artemis.xml','artemis'), ('ibm_rss.xml','insurancebusinessmag'), ('insuranceasia.xml','insuranceasia')]:
    x = rd(fn)
    blocks = re.findall(r'<item[ >].*?</item>', x, re.S)
    print(f'== {src} ({fn}) items={len(blocks)}')
    for b in blocks:
        tm = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        ti = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        lk = re.search(r'<link>(.*?)</link>', b, re.S)
        de = re.search(r'<description>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>', b, re.S)
        print(' ', (tm.group(1).strip() if tm else '?'), '|', strip(ti.group(1))[:90] if ti else '?', '|', (lk.group(1).strip() if lk else '?')[:100])
        print('    DESC:', strip(de.group(1))[:180] if de else '')

# govhk general rss
x = rd('govhk.xml')
blocks = re.findall(r'<item[ >].*?</item>', x, re.S)
print(f'== govhk items={len(blocks)}')
for b in blocks[:25]:
    tm = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
    ti = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
    lk = re.search(r'<link>(.*?)</link>', b, re.S)
    print(' ', (tm.group(1).strip() if tm else '?'), '|', strip(ti.group(1))[:90], '|', (lk.group(1).strip() if lk else '?')[:100])

# ian json
try:
    j = json.loads(rd('ian.json'))
    print(f'== ian posts={len(j)}')
    for p in j:
        print(' ', p.get('date'), '|', strip(p.get('title',{}).get('rendered',''))[:90], '|', p.get('link'))
except Exception as e:
    print('ian err', e)
