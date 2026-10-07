import re, os, html
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
def rd(n):
    return open(os.path.join(RAW, n), encoding='utf-8', errors='ignore').read()
def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

for f in ['aia.html','prudential.html','axa.html','sunlife.html','fwd.html','yflife.html','mpfa.html','fstb.html']:
    t = rd(f)
    print('#'*25, f, len(t))
    # find date mentions near 2026-10 / Oct 2026 / 2026年10月
    pat = r'(\d{1,2}\s+(?:Oct|October)\s+2026|2026-10-\d{2}|2026年10月\d{0,2}日?|10\s+Oct\s+2026|Oct\s+\d{1,2},?\s+2026)'
    hits = list(re.finditer(pat, t))
    print('  date hits:', len(hits))
    for m in hits[:14]:
        seg = clean(t[max(0, m.start()-600):m.start()+320])
        print('   >', seg[-300:])
