import json, re, html

d = json.load(open('data/_raw_1004_0037.json'))

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

for k in ['artemis', 'ibm_asia']:
    t = d[k]['text']
    print('###', k)
    # look for any 'Oct' near '2026'
    for m in list(re.finditer(r'(October|Sep|Sept|Oct)\D{0,12}2026', t))[:10]:
        print('  m:', clean(t[max(0, m.start()-120):m.start()+120]))
    # look for time datetime attrs
    attrs = re.findall(r'(?:datetime|datePublished|data-date)="([^"]+)"', t)[:12]
    print('  attrs:', attrs)
    print()
