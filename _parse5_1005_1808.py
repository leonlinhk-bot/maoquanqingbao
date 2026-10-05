import re, html
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def txt(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

print('=== IA sitemap: press-release / circular URLs referencing 2026-09/10 ===')
sm = open(CACHE+'ia_sitemap.xml', encoding='utf-8', errors='replace').read()
locs = re.findall(r'<loc>(.*?)</loc>', sm)
print('total locs:', len(locs))
for u in locs:
    if re.search(r'2026(09|10)', u):
        print('  ', u)
