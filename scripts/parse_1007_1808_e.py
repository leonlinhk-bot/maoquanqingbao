import re, os, html
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
def rd(n):
    return open(os.path.join(RAW, n), encoding='utf-8', errors='ignore').read()
def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

t = rd('ia_press.html')
print('=== ia_press links ===')
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
    txt = clean(m.group(2))
    if txt and ('2026' in txt or 'press' in m.group(1).lower() or len(txt) > 12):
        print(' -', txt[:130], '||', m.group(1)[:110])
print()
print('=== hkma links 2026 ===')
t = rd('hkma_press.html')
for m in re.finditer(r'<a href="(/eng/news-and-media/press-releases/2026/[^"]+)"[^>]*>(.*?)</a>', t, re.S):
    print(' -', clean(m.group(2))[:140], '||', m.group(1))
print()
print('=== ibm items ===')
t = rd('ibm_asia.html')
for m in re.finditer(r'content-list__item__title[^>]*>(.*?)</', t, re.S):
    print(' -', clean(m.group(1))[:150])
print()
print('=== ibm hrefs+title attr ===')
for m in re.finditer(r'href="(/asia/news/[^"]+\.aspx)"[^>]*title="([^"]*)"', t):
    print(' -', m.group(2)[:130], '||', m.group(1)[:100])
