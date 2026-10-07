import re
D='.tmp/1008_0007'

def scan(fn, pats, label):
    try:
        h=open(f'{D}/{fn}',encoding='utf-8',errors='ignore').read()
    except Exception as e:
        print(fn,'ERR',e); return
    print('='*14, label, fn, len(h))
    seen=set()
    for pat in pats:
        for m in re.finditer(pat, h):
            s=' '.join(x.strip() for x in m.groups() if x)
            if not s or s in seen: continue
            seen.add(s)
            print('  ', s[:160])

# AIA press releases
scan('aia.html', [r'<h[23][^>]*>\s*<a[^>]*href="([^"]*)"[^>]*>([^<]{10,140})'], 'AIA')
scan('pru.html', [r'href="([^"]*(?:news|media|press)[^"]*)"[^>]*>\s*([^<]{10,140})'], 'PRU')
scan('axa.html', [r'<a[^>]*href="([^"]*)"[^>]*>\s*<[^>]*>?\s*([^<]{12,140})'], 'AXA')
scan('sun.html', [r'href="([^"]*(?:news|media|press)[^"]*)"[^>]*>\s*([^<]{10,140})'], 'SUN')
scan('hkfi_media.html', [r'href="([^"]*(?:media|release|news)[^"]*)"[^>]*>\s*<?[^>]*>?\s*([^<]{8,140})'], 'HKFI')
