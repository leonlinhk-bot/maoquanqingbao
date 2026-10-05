import re, html, glob, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def cliptxt(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

for f in sorted(glob.glob(CACHE + 'gn_*.txt')):
    name = os.path.basename(f)
    data = open(f, encoding='utf-8', errors='replace').read()
    items = re.findall(r'<item>(.*?)</item>', data, re.S)
    print(f'===== {name}  ({len(items)} items) =====')
    for b in items[:10]:
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        s = re.search(r'<source[^>]*>(.*?)</source>', b, re.S)
        l = re.search(r'<link>(.*?)</link>', b, re.S)
        print('  ', (d.group(1) if d else '?').strip()[:31], '|', cliptxt(s.group(1) if s else '')[:22], '|', cliptxt(t.group(1) if t else '')[:95])
    print()
