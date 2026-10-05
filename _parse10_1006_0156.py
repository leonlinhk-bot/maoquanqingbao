import re, html, os
C = 'data/_cache1006_0156'
def clean(s):
    return html.unescape(re.sub(r'<[^>]+>', '', s or '')).strip()
def squash(s):
    return re.sub(r'\s+', ' ', s)

for fname, label, dom in [('reinasia.html', '(RE)IN ASIA', 'https://www.reinasia.com'),
                          ('air_news.html', 'ASIA INSURANCE REVIEW', 'https://www.asiainsurancereview.com')]:
    h = open(os.path.join(C, fname), encoding='utf-8', errors='ignore').read()
    print('=' * 74)
    print(label)
    rows = []
    for m in re.finditer(r'\b(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+2026)\b', h):
        seg = h[max(0, m.start() - 2500):m.start() + 300]
        links = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', seg, re.S)
        cand = [(u, clean(t)) for u, t in links if len(clean(t)) > 28 and 'javascript' not in u]
        if cand:
            u, t = cand[-1]
            rows.append((m.group(1), t, u))
    seen = set()
    for d, t, u in rows:
        k = (d, t[:40])
        if k in seen:
            continue
        seen.add(k)
        if re.search(r'\b(0?5|0?6|0?4)\s+Oct', d):
            print('  *', d, '|', t[:88], '|', u[:90])
    print('  --- all distinct recent ---')
    for d, t, u in rows[:0]:
        pass
    for d, t, u in rows[:25]:
        print('   ', d, '|', t[:75], '|', u[:70])
