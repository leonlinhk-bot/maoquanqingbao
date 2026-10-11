import re, html, sys
D='.tmp/1012_0022'
def txt(s):
    s=re.sub(r'<script.*?</script>','',s,flags=re.S)
    s=re.sub(r'<style.*?</style>','',s,flags=re.S)
    s=re.sub(r'<[^>]+>',' ',s)
    return re.sub(r'\s+',' ',html.unescape(s))

for f in ['hkma.html','artemis.html','ibm.html','nfra.html','prudential.html','axa.html','sunlife.html','aia.html']:
    try:
        t=open(f'{D}/{f}',encoding='utf-8',errors='ignore').read()
    except Exception as e:
        print(f,'ERR',e); continue
    print('#'*25, f, 'len', len(t))
    # find date-like strings with nearby anchor text
    for m in re.finditer(r'<(?:a|li|h\d|div|span)[^>]*>([^<]{0,180})</(?:a|li|h\d|div|span)>', t):
        seg=html.unescape(m.group(1)).strip()
        if re.search(r'(Oct|October|月)\s*(1[012]|1[0-9])|2026-10-1[0-2]|10\s*月\s*1[0-2]', seg) and len(seg)>12:
            print('  ', seg[:170])
