import re, os, html
RAW = '/Users/leonliang/maoquanqingbao/data/_raw_1007_1808'
def rd(n):
    return open(os.path.join(RAW, n), encoding='utf-8', errors='ignore').read()

for f in ['ia_press.html','ia_circ.html','hkma_press.html','ibm_asia.html']:
    t = rd(f)
    print('#'*30, f, len(t))
    # print chunks around date-like strings
    hits = [m.start() for m in re.finditer(r'2026[-/年]\s?0?9|2026[-/年]\s?10|Oct(?:ober)? 2026|Sep(?:tember)? 2026', t)][:6]
    for h in hits:
        seg = t[max(0,h-500):h+300]
        seg = re.sub(r'\s+',' ', re.sub(r'<[^>]+>',' | ', seg))
        print('   ...', seg[-380:])
        print('   ---')
