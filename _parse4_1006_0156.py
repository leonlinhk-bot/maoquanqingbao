import re, html, os

C = 'data/_cache1006_0156'
def clean(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()

# IBM: locate date per article
h = open(os.path.join(C, 'ibm.html'), encoding='utf-8', errors='ignore').read()
print('===== IBM article blocks with dates =====')
for m in re.finditer(r'(\d{2} \w{3} 2026)', h):
    seg = h[max(0, m.start() - 1400):m.start() + 200]
    titles = re.findall(r'href="(/asia/news/[^"]+)"[^>]*>(.*?)</a>', seg, re.S)
    if titles:
        t = [clean(x[1]) for x in titles if len(clean(x[1])) > 25]
        print(m.group(1), '|', (t[-1][:88] if t else ''))
print('===== IBM rows (title|date|url) =====')
for m in re.finditer(r'<a[^>]+href="(/asia/news/[^"]+)"[^>]*>(.*?)</a>(.{0,900}?)(\d{2} \w{3} 2026)', h, re.S):
    t = clean(m.group(2))
    if len(t) < 25:
        continue
    print(t[:85], '|', m.group(4), '|', m.group(1)[:70])

# artemis: raw snippet around first few titles
a = open(os.path.join(C, 'artemis.html'), encoding='utf-8', errors='ignore').read()
i = a.find('PICC P&C appears')
print('===== ARTEMIS raw around PICC =====')
print(re.sub(r'\s+', ' ', a[max(0, i - 900):i + 700]))
j = a.find('Best of Artemis')
print('===== ARTEMIS raw around Best of =====')
print(re.sub(r'\s+', ' ', a[max(0, j - 700):j + 500]))
