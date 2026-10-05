import re, html, os
C = 'data/_cache1006_0156'
def clean(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()

def scan(fname, label, pat, maxn=30):
    p = os.path.join(C, fname)
    if not os.path.exists(p):
        print('MISSING', fname); return
    h = open(p, encoding='utf-8', errors='ignore').read()
    print('=' * 72)
    print(label, fname)
    seen = set()
    n = 0
    for m in re.finditer(pat, h, re.S):
        u = m.group(1); t = clean(m.group(2))
        extra = clean(m.group(3)) if m.lastindex and m.lastindex >= 3 else ''
        if len(t) < 22 or u in seen:
            continue
        seen.add(u)
        print('  ', t[:92], '|', extra[:22], '|', u[:95])
        n += 1
        if n >= maxn:
            break

scan('air_news.html', 'ASIA INSURANCE REVIEW',
     r'href="(/News/[^"]+)"[^>]*>(.*?)</a>(.{0,300}?)(\d{1,2}\s+\w+\s+2026|\w{3}\s+\d{1,2},\s*2026|\d{4}-\d{2}-\d{2})')
print('--- air date tokens ---')
a = open(os.path.join(C, 'air_news.html'), encoding='utf-8', errors='ignore').read()
print(sorted(set(re.findall(r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s*\,?\s*2026', a)))[:30])

scan('reinasia.html', '(RE)IN ASIA',
     r'href="(https://www\.reinasia\.com/[^"]+)"[^>]*>(.*?)</a>')
print('--- reinasia date tokens ---')
r = open(os.path.join(C, 'reinasia.html'), encoding='utf-8', errors='ignore').read()
print(sorted(set(re.findall(r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s*\,?\s*2026', r)))[:30])
print(sorted(set(re.findall(r'2026-\d{2}-\d{2}', r)))[:30])

scan('iaasia_home.html', 'INSURANCEASIA HOME',
     r'href="(https://insuranceasia\.com/[^"]+)"[^>]*>(.*?)</a>', 25)
