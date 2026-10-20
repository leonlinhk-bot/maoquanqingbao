import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
p = os.path.join(BASE, 'iaasia.html')
t = open(p, encoding='utf-8', errors='ignore').read()
t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
# Get anchors with href containing /News/ and text
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', t, re.S):
    href, inner = m.group(1), m.group(2)
    txt = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', inner))).strip()
    if '/News/' in href and len(txt) > 25:
        print(txt[:130], '||', href[:120])
