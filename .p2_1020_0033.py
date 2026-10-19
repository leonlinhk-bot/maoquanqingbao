import re, os, json
from datetime import datetime
C = '.cache1020_0033'

def show(path, pats, label, limit=12):
    p = os.path.join(C, path)
    if not os.path.exists(p):
        print('##', label, 'MISSING'); return
    t = open(p, encoding='utf-8', errors='ignore').read()
    print('##', label, 'len', len(t))
    for pat in pats:
        hits = re.findall(pat, t, re.S)
        if hits:
            print('  pattern', pat[:40], 'hits', len(hits))
            for h in hits[:limit]:
                s = ' | '.join([re.sub(r'\s+', ' ', x)[:130] for x in h]) if isinstance(h, tuple) else re.sub(r'\s+',' ',h)[:150]
                print('   ', s)
            break

# HKMA press releases page: look for 2026 dates
show('hkma.html', [r'(\d{1,2} October 2026)', r'(2026-10-\d\d)'], 'HKMA')
# Iaasia
show('iaasia.html', [r'<a[^>]+href="([^"]*News/[^"]*)"[^>]*>\s*([^<]{15,140})</a>'], 'IAA')
# AIA
show('aia.html', [r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{15,160})</a>'], 'AIA', 25)
# SunLife
show('sunlife.html', [r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{15,160})</a>'], 'SunLife', 20)
# AXA
show('axa.html', [r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{15,160})</a>'], 'AXA', 20)
# Prudential
show('prudential.html', [r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{15,160})</a>'], 'Prudential', 20)
