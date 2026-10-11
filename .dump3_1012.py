import re, html, sys
D='.tmp/1012_0022'
def totext(s):
    s=re.sub(r'<script.*?</script>','',s,flags=re.S)
    s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' | ',s)
    s=html.unescape(s)
    s=re.sub(r'(\s*\|\s*)+',' | ',s)
    s=re.sub(r'[ \t]+',' ',s)
    return s
pats=r'(?:2026-10-1[012])|(?:Oct(?:ober)?\.?\s*1[012],?\s*2026)|(?:1[012]\s+Oct(?:ober)?\s+2026)|(?:2026\s*年\s*10\s*月\s*1[012]\s*日)|(?:10\s*月\s*1[012]\s*日)|(?:1[012]/10/2026)'
for f in sys.argv[1:]:
    try:
        t=open(f'{D}/{f}',encoding='utf-8',errors='ignore').read()
    except Exception as e:
        print(f,'ERR',e); continue
    x=totext(t)
    print('#'*25, f, 'len', len(x))
    hits=0
    for m in re.finditer(pats, x, re.I):
        a=max(0,m.start()-200); b=min(len(x), m.end()+200)
        seg=re.sub(r'(\s*\|\s*)+',' | ',x[a:b])
        seg=re.sub(r'\s+',' ',seg)
        print('  >', seg[:330]); hits+=1
        if hits>12: break
    if hits==0: print('   (no 10/11-12 Oct matches)')
