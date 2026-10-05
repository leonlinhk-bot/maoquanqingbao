import re, html, glob, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1006_0049/'
for f in sorted(glob.glob(CACHE + 'gn_*.xml')):
    name = os.path.basename(f)
    data = open(f, encoding='utf-8', errors='replace').read()
    blocks = re.findall(r'<item>(.*?)</item>', data, re.S)
    print(f'===== {name} ({len(blocks)}) =====')
    for b in blocks[:4]:
        print('   RAW:', re.sub(r'\s+', ' ', b)[:400])
    print()
