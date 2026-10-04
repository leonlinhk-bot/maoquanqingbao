import json, re, html
d = json.load(open('data/_raw_1004_1808.json'))
def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s); s = html.unescape(s); return re.sub(r'\s+', ' ', s).strip()
for key in ['scmp_insurance', 'aia_news', 'sunlife_news', 'prudential_news', 'axa_news']:
    t = clean(d.get(key, {}).get('text', ''))
    print('#' * 70)
    print('###', key, 'len', len(t))
    # broad: any date-ish token around Oct
    seen = set()
    for m in re.finditer(r'(October|Oct\.?|\u5341\u6708)\s*\d{1,2}', t):
        g = m.group(0)
        ctx = t[max(0, m.start()-120): m.start()+160]
        print('  ~', g, '::', ctx)
        seen.add(g)
    for m in re.finditer(r'\d{1,2}\s*(?:days?|hours?|mins?|minutes?)\s*ago', t):
        print('  rel ~', m.group(0), '::', t[max(0, m.start()-120): m.start()+120])
    for m in list(re.finditer(r'2026-10-0[34]', t))[:8]:
        print('  iso ~', m.group(0), '::', t[max(0, m.start()-150): m.start()+150])
