import re, html
D='.tmp/1012_0022'
def txt(s):
    s=re.sub(r'<script.*?</script>','',s,flags=re.S)
    s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>','|',s)
    s=html.unescape(s)
    s=re.sub(r'\|+','|',s)
    s=re.sub(r'[ \t]+',' ',s)
    return s

import sys
files=sys.argv[1:] or ['hkma.html']
for f in files:
    t=open(f'{D}/{f}',encoding='utf-8',errors='ignore').read()
    x=txt(t)
    print('#'*30, f)
    # print segments containing date patterns
    pats=[r'2026-\d\d-\d\d', r'\d{1,2}\s+(?:Oct|Sep|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Nov|Dec)\w*\s+2026', r'2026年\d{1,2}月\d{1,2}日', r'\d{1,2}/\d{1,2}/2026']
    seen=set()
    for p in pats:
        for m in re.finditer(p, x):
            a=max(0,m.start()-160); b=min(len(x), m.end()+160)
            seg=re.sub(r'\|',' | ',x[a:b])
            key=re.sub(r'\s+',' ',seg)[:120]
            if key in seen: continue
            seen.add(key)
            print('  >', re.sub(r'\s+',' ',seg)[:300])
