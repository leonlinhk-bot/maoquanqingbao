import re, html, glob, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def txt(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

# google news links are redirects; print the encoded target if present, else link
for f in ('gn_aia.txt', 'gn_fam.txt', 'gn_hkins2.txt', 'gn_hk_ins.txt'):
    print('=====', f)
    d = open(CACHE+f, encoding='utf-8', errors='replace').read()
    for b in re.findall(r'<item>(.*?)</item>', d, re.S)[:12]:
        t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
        d2 = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
        l = re.search(r'<link>(.*?)</link>', b, re.S)
        print('  ', txt(t.group(1) if t else '')[:95])
        print('      ', (d2.group(1) if d2 else '')[:31], (l.group(1) if l else '')[:150])
    print()

print('===== NFRA =====")')
n = open(CACHE+'nfra.html', encoding='utf-8', errors='replace').read()
t = txt(n)
print(t[:1200])
