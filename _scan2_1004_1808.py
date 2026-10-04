import json, re, html

d = json.load(open('data/_raw_1004_1808.json'))

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

for key in ['artemis', 'ibm_asia', 'hkma_press', 'aia_news', 'prudential_news', 'axa_news', 'sunlife_news', 'nfra', 'insuranceasia_list']:
    t = d.get(key, {}).get('text', '')
    print('#' * 78)
    print('###', key, 'len', len(t))
    c = clean(t)
    # find all Oct occurrences
    hits = [(m.start(), m.group(0)) for m in re.finditer(r'(?:October|Oct\.?)\s*\d{1,2}', c)]
    for pos, g in hits[:25]:
        print('  ~', g, '::', c[max(0,pos-180):pos+180])
    if not hits:
        # print first 1200 chars cleaned
        print('  HEAD:', c[:1500])
