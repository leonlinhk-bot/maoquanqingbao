import re, os
D = 'data/_raw_1010_0110'

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = s.replace('&#34;', '"').replace('&#39;', "'").replace('&amp;', '&').replace('&#x27;', "'")
    return re.sub(r'\s+', ' ', s).strip()

print('===== AIA 2026 page =====')
a = open(os.path.join(D, 'aia2026.out'), encoding='utf-8', errors='replace').read()
# look for list items with dates
for m in list(re.finditer(r'(cmp-list__item|press-release)', a))[:0]:
    pass
hits = re.findall(r'<a[^>]+href="([^"]*press-releases[^"]*)"[^>]*>(.{0,300}?)</a>', a, re.S)
seen = set()
for u, t in hits:
    t2 = clean(t)
    if not t2 or len(t2) < 6: continue
    if u in seen: continue
    seen.add(u)
    print(' *', u[:110], '||', t2[:120])
print('n=', len(seen))

print('===== Sunlife 2026 page =====')
s = open(os.path.join(D, 'sunlife2026.out'), encoding='utf-8', errors='replace').read()
hits = re.findall(r'<a[^>]+href="([^"]*news-releases/2026[^"]*)"[^>]*>(.{0,400}?)</a>', s, re.S)
seen = set()
for u, t in hits:
    t2 = clean(t)
    if not t2 or len(t2) < 8 or u in seen: continue
    seen.add(u)
    print(' *', u[:120], '||', t2[:150])
print('n=', len(seen))

print('===== Prudential newsroom =====')
p = open(os.path.join(D, 'prudential.out'), encoding='utf-8', errors='replace').read()
hits = re.findall(r'href="([^"]*newsroom[^"]*)"[^>]*>(.{0,300}?)</a>', p, re.S)
seen = set()
for u, t in hits:
    t2 = clean(t)
    if not t2 or len(t2) < 15 or u in seen: continue
    seen.add(u)
    print(' *', u[:120], '||', t2[:150])
print('n=', len(seen))

print('===== AXA items =====')
x = open(os.path.join(D, 'axa.out'), encoding='utf-8', errors='replace').read()
for m in re.finditer(r'axa-hk-article-list-article-date"><p>([^<]+)</p>.*?<h5>(.*?)</h5>', x, re.S):
    print(' *', m.group(1), '||', clean(m.group(2))[:130])

print('===== nfra_list =====')
n = open(os.path.join(D, 'nfra_list.out'), encoding='utf-8', errors='replace').read()
print(clean(n)[:800])
