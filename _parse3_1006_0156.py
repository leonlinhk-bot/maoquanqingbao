import re, html, os

C = 'data/_cache1006_0156'

def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return html.unescape(s).strip()

def dump_links(fname, pattern, label, minlen=18):
    p = os.path.join(C, fname)
    if not os.path.exists(p):
        print('MISSING', fname); return
    h = open(p, encoding='utf-8', errors='ignore').read()
    print('=' * 72)
    print(label, fname)
    rows = re.findall(pattern, h, re.S)
    seen = set()
    for row in rows:
        if isinstance(row, tuple):
            u, t = row[0], row[1]
            extra = row[2:] if len(row) > 2 else ()
        else:
            u, t, extra = row, '', ()
        t = clean(t)
        if len(t) < minlen or u in seen:
            continue
        seen.add(u)
        print('  ', ' | '.join([t[:95], u[:80]] + [clean(x)[:28] for x in extra]))

# Artemis: article blocks often carry a date
dump_links('artemis.html', r'<a[^>]+href="(https://www\.artemis\.bm/news/[^"]+)"[^>]*>(.*?)</a>', 'ARTEMIS')
# Look for dates near titles
h = open(os.path.join(C, 'artemis.html'), encoding='utf-8', errors='ignore').read()
print('--- artemis date tokens ---')
print(sorted(set(re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+2026', h)))[:40])

dump_links('ibm.html', r'href="(/asia/news/[^"]+)"[^>]*>(.*?)</a>', 'IBM', 25)
h2 = open(os.path.join(C, 'ibm.html'), encoding='utf-8', errors='ignore').read()
print('--- ibm date tokens ---')
print(sorted(set(re.findall(r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+2026', h2)))[:30])
print(sorted(set(re.findall(r'\b(?:Oct|Oct\.|October)\s+\d{1,2},?\s+2026', h2)))[:30])

dump_links('aia.html', r'href="([^"]*media-centre[^"]*)"[^>]*>(.*?)</a>', 'AIA', 15)
dump_links('prudential.html', r'href="([^"]*(?:newsroom|media|press)[^"]*)"[^>]*>(.*?)</a>', 'PRUDENTIAL', 15)
dump_links('axa.html', r'href="([^"]*(?:news|media|press)[^"]*)"[^>]*>(.*?)</a>', 'AXA', 15)
dump_links('sunlife.html', r'href="([^"]*(?:newsroom|media|news)[^"]*)"[^>]*>(.*?)</a>', 'SUNLIFE', 15)

# insurer pages: look for explicit dates
for f in ['aia.html', 'prudential.html', 'axa.html', 'sunlife.html']:
    p = os.path.join(C, f)
    if not os.path.exists(p):
        continue
    hh = open(p, encoding='utf-8', errors='ignore').read()
    d1 = sorted(set(re.findall(r'\b\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s*,?\s*2026', hh)))[-12:]
    d2 = sorted(set(re.findall(r'2026[年\-/]\d{1,2}[月\-/]\d{1,2}', hh)))[-12:]
    print('===', f, 'dates:', d1, d2)
