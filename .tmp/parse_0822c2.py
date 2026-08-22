import re, html

def strip_tags(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

for fn in ['hkma-press.html', 'fstb-press.html']:
    p = 'data/_raw/t0822c/' + fn
    raw = open(p, encoding='utf-8', errors='ignore').read()
    print('=' * 25, fn, '=' * 25)
    # find press release titles: often <a> with date nearby, or in specific containers
    # look for lines containing 2026/08 or Aug 2026 or 8月
    for m in re.finditer(r'(20\d\d[-/年]\s?\d{1,2}[-/月]\s?\d{1,2}[日号]?|2026[-/]\d{2}[-/]\d{2})', raw):
        start = max(0, m.start() - 200)
        seg = raw[start:m.end() + 200]
        # strip tags
        seg = strip_tags(seg)
        if seg:
            print('  ...', seg[:180].replace('\n', ' '))
