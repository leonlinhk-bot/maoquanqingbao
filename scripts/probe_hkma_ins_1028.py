import os, re, html
D = '.cache1028_1010'

def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

# ---- HKMA press releases
t = open(f'{D}/hkma.raw', encoding='utf-8', errors='replace').read()
print('=== HKMA ===')
# find rows: date + link + title
blocks = re.findall(r'(20\d\d-\d\d-\d\d|2[0-9] \w+ 20\d\d).{0,400}?href="([^"]*press-releases/[^"]*)".{0,300}?>(.*?)</a>', t, re.S)
seen = set()
for d, href, title in blocks[:40]:
    ti = clean(title)
    if not ti or ti in seen:
        continue
    seen.add(ti)
    print(f'  {d} | {ti[:80]} | {href}')
if not blocks:
    idx = [m.start() for m in re.finditer(r'press-releases/2026', t)][:5]
    print('no structured match; sample around first occurrence:')
    for i in idx:
        print(repr(t[max(0, i-400):i+200]))

print()
print('=== insurer pages: count of 2026-10 dates found ===')
for f in ['aia', 'prudential', 'axa', 'sunlife', 'manulife']:
    p = f'{D}/{f}.raw'
    if not os.path.exists(p):
        print(f'-- {f}: NOT FETCHED')
        continue
    s = open(p, encoding='utf-8', errors='replace').read()
    dates = re.findall(r'(20\d\d[-/年]\s?\d{1,2}[-/月]\s?\d{1,2})', s)
    from collections import Counter
    c = Counter(dates)
    print(f'-- {f}: len={len(s)} distinct dates={len(c)} top={c.most_common(6)}')
