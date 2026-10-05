import os, re, html
import xml.etree.ElementTree as ET
C = 'data/_cache1006_0156'
def clean(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()

t = ET.parse(os.path.join(C, 'insuranceasia.xml'))
print('===== INSURANCEASIA rss items =====')
for it in t.getroot().iter('item'):
    pd = (it.findtext('pubDate') or '').strip()
    if 'Oct 2026' in pd or 'Sep 2026' in pd:
        print(pd, '|', clean(it.findtext('title'))[:95], '|', (it.findtext('link') or '').strip())

# scmp items with links, newest
s = ET.parse(os.path.join(C, 'scmp_ins.xml'))
print('===== SCMP top 8 =====')
for it in list(s.getroot().iter('item'))[:8]:
    print((it.findtext('pubDate') or '').strip(), '|', clean(it.findtext('title'))[:88], '|', (it.findtext('link') or '').strip()[:100])

# IBM full hrefs
h = open(os.path.join(C, 'ibm.html'), encoding='utf-8', errors='ignore').read()
print('===== IBM full hrefs =====')
for u, tt in re.findall(r'href="(/asia/news/[^"]+)"[^>]*>(.*?)</a>', h, re.S):
    tt = clean(tt)
    if len(tt) > 25:
        print('https://www.insurancebusinessmag.com' + u, '||', tt[:80])
