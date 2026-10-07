import re, os, html
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
def rd(n):
    return open(os.path.join(RAW, n), encoding='utf-8', errors='ignore').read()
def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

t = rd('ia_press.html')
print('=== ia_press: any 2026 mention ===')
for m in re.finditer(r'.{120}202[456].{160}', t):
    print(' *', clean(m.group(0))[:280])
print('--- total len', len(t))

print()
print('=== ibm full item blocks ===')
t = rd('ibm_asia.html')
idx = [m.start() for m in re.finditer(r'content-list__item__title', t)]
for i in idx[:14]:
    seg = t[max(0,i-1200):i+400]
    href = re.findall(r'href="(/asia/news/[^"]+\.aspx)"', seg)
    dt = re.findall(r'(\d{2} \w{3} 2026)', seg)
    title = clean(t[i:i+400].split('</')[0])
    print(' -', (dt[-1] if dt else '?'), '|', title[:110], '||', href[-1] if href else '')
