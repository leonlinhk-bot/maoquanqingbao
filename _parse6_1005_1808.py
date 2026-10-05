import re, html
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def txt(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

print('=== IA sitemap locs with 2026-09 / 2026-10 ===')
sm = open(CACHE+'ia_sitemap.xml', encoding='utf-8', errors='replace').read()
locs = re.findall(r'<loc>(.*?)</loc>', sm)
print('total locs:', len(locs))
hits = [u for u in locs if re.search(r'2026(09|10)', u)]
for u in hits:
    print('  ', u)

print()
print('=== IA circulars_on_regulatory_matters_2026 rows ===')
c = open(CACHE+'ia_circ2026.html', encoding='utf-8', errors='replace').read()
body = c
# find table rows
rows = re.findall(r'<tr[^>]*>(.*?)</tr>', body, re.S)
print('rows:', len(rows))
for r in rows:
    t = txt(r)
    if len(t) > 8:
        hrefs = re.findall(r'href="([^"]+)"', r)
        print('  ', t[:150], '||', hrefs[:1])
