import re
D='.tmp/1008_0007'
for fn,label in [('sun.html','SUNLIFE'),('axa.html','AXA'),('hkfi_media.html','HKFI')]:
    try:
        h=open(f'{D}/{fn}',encoding='utf-8',errors='ignore').read()
    except Exception as e:
        print(fn,'ERR',e); continue
    print('='*14, label, len(h))
    seen=set()
    for m in re.finditer(r'href="([^"]*(?:news|media|press|release)[^"]*)"', h):
        u=m.group(1)
        if u in seen or len(u)<8: continue
        seen.add(u)
        seg=h[m.start():m.start()+500]
        t=re.search(r'>([^<>]{10,160})<', seg)
        d=re.search(r'(20\d\d[-/]\d\d[-/]\d\d|\d{1,2}\s+\w{3,9}\s+20\d\d|\w+ \d{1,2}, 20\d\d|\d{1,2}/\d{1,2}/20\d\d)', seg)
        print('  ', u[:95], '|', (t.group(1).strip() if t else '')[:70], '|', (d.group(1) if d else ''))
        if len(seen)>28: break
