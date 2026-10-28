import re, html, json
D = '.cache1028_1010'

def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

def show_around(s, pat, ctx=350, limit=6):
    n = 0
    for m in re.finditer(pat, s):
        print('...', repr(s[max(0, m.start()-ctx):m.start()+ctx]))
        print('-'*100)
        n += 1
        if n >= limit:
            break

print('### AIA ###')
s = open(f'{D}/aia.raw', encoding='utf-8', errors='replace').read()
show_around(s, r'2026-10-1[0-9]', 300, 4)

print()
print('### AXA ###')
s2 = open(f'{D}/axa.raw', encoding='utf-8', errors='replace').read()
show_around(s2, r'2026年10月2[0-9]', 300, 3)

print()
print('### SUNLIFE (structure) ###')
s3 = open(f'{D}/sunlife.raw', encoding='utf-8', errors='replace').read()
m = re.search(r'news-release', s3, re.I)
print(s3[:1200])
