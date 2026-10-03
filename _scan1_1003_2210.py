import json, re, datetime, xml.etree.ElementTree as ET, html

raw = json.load(open('data/_raw_1003_2210.json'))

def clean(s):
    return html.unescape(re.sub('<[^>]+>', ' ', s)).strip()

print('###### HKMA all rows ######')
txt = raw['hkma_press']['text']
rows = re.findall(r'(\d{1,2}\s+\w+\s+20\d\d)(.{0,400}?)href="(/eng/news-and-media/press-releases/2026/\d\d/[^"]+)"[^>]*>([^<]{5,160})<', txt, re.S)
for d, _, u, t in rows:
    print(f'  {d} | {t.strip()[:95]} | {u}')

print('\n###### GOVHK zh RSS ######')
txt = raw['govhk_zh']['text']
root = ET.fromstring(txt)
for it in list(root.iter('item')):
    title = clean(it.findtext('title') or '')
    pub = (it.findtext('pubDate') or '').strip()
    link = (it.findtext('link') or '').strip()
    print(f'  {pub} | {title[:90]}')

print('\n###### NFRA ######')
txt = raw['nfra']['text']
for m in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', txt, re.S)[:60]:
    t = clean(m[1])
    if len(t) > 8:
        print(f'  {t[:90]} | {m[0][:90]}')
