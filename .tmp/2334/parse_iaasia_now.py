import re, html, json, datetime

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

def parse_iaasia(fn):
    raw = open(fn, encoding='utf-8', errors='ignore').read()
    arts = []
    for m in re.finditer(r'<a[^>]+href="(https://insuranceasia\.com/insurance/(?:news|in-focus|exclusive|insights|features)/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        u, t = m.group(1), strip_tags(m.group(2))
        if not t or t in [x[1] for x in arts]: continue
        ctx = raw[m.end():m.end()+600]
        ago = re.findall(r'(\d+\s+(?:hour|day|week|month|minute)s?\s+ago|\d{4}-\d{2}-\d{2})', ctx)
        arts.append((u, t, ago[:1]))
    return arts

for fn in ['.tmp/2334/iaasia.html', '.tmp/iaasia-insurance.html']:
    print('=====', fn)
    arts = parse_iaasia(fn)
    seen = set()
    for u, t, ago in arts:
        if u in seen: continue
        seen.add(u)
        print(u.split('/')[-1][:58], '|', t[:52], '|', ago)
