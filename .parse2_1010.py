import re, os
D = 'data/_raw_1010_0110'
h = open(os.path.join(D, 'hkma.out'), encoding='utf-8', errors='replace').read()
rows = re.findall(r'<li>(\d{2} \w{3} \d{4})</li><li><a href="([^"]+)"[^>]*>(.*?)</a>', h)
print('hkma rows', len(rows))
for d, u, t in rows[:15]:
    print(d, '|', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', t))[:110], '|', u)

print('=== nfra dates ===')
n = open(os.path.join(D, 'nfra.out'), encoding='utf-8', errors='replace').read()
for m in re.finditer(r'(2026[-年]\s*\d{1,2}[-月]\s*\d{1,2})', n):
    print(m.group(1), '|', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', n[m.start():m.start()+200]))[:150])
    if m.start() > 40000: break

print('=== hkfi hunt ===')
k = open(os.path.join(D, 'hkfi.out'), encoding='utf-8', errors='replace').read()
for m in list(re.finditer(r'Press Release|新聞稿|新聞發佈|media-centre', k))[:6]:
    print('...', re.sub(r'\s+', ' ', k[max(0, m.start()-250):m.start()+250])[:500])
    print('---')

print('=== aia hunt ===')
a = open(os.path.join(D, 'aia.out'), encoding='utf-8', errors='replace').read()
for m in list(re.finditer(r'media-centre/press-releases/[^"\\]+', a))[:15]:
    print(a[m.start():m.start()+120])
