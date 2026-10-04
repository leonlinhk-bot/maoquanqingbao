import json, re
d = json.load(open('data/live-items.json'))
ids = [it['id'] for it in d['items']]
for k in ['week-in-insurance', 'fwd-fined', 'manulife-closes', 'munich-re-ltc', 'long-term-care']:
    hits = [i for i in ids if k in i.lower()]
    print(f'[{k}] {len(hits)}: {hits[:8]}')
# HKMA html probe
raw = open('/tmp/hkma_t.txt', encoding='utf-8', errors='ignore').read()
print('--- hkma page probes ---')
for pat in [r'ajax', r'\.json', r'/api/', r'press-release[a-z-]*\.(?:json|xml)', r'url\s*:\s*["\'][^"\']+']:
    ms = re.findall(pat, raw)
    print(pat, '->', len(ms), ms[:5])
# look for date strings near press release titles
for m in re.finditer(r'(?:Oct|October)\s*\d{1,2},?\s*2026', raw):
    print('  date:', m.group(0), '::', re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', raw[max(0, m.start()-150):m.start()+150])))
