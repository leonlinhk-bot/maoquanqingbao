import re, sys, os
D = 'data/_raw_1010_0110'
for f in ['hkma', 'hkfi', 'axa', 'fstb_other', 'nfra_news', 'aia', 'prudential', 'sunlife', 'manulife', 'nfra', 'ia_press', 'hkma_rss']:
    p = os.path.join(D, f + '.out')
    if not os.path.exists(p):
        print('##### MISSING', f); continue
    h = open(p, encoding='utf-8', errors='replace').read()
    print('#####', f, 'len', len(h))
    ms = [m.start() for m in re.finditer(r'2026-10|/2026/10/|202610|2026年10', h)][:2]
    if not ms:
        ms = [m.start() for m in re.finditer(r'2026', h)][:2]
    for s in ms:
        print('   ...', re.sub(r'\s+', ' ', h[max(0, s - 400):s + 400])[:800])
        print('   ---')
