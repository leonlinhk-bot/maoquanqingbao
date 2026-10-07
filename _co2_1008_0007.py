import re, json
D='.tmp/1008_0007'

def titlerows(fn, pat):
    try:
        h=open(f'{D}/{fn}',encoding='utf-8',errors='ignore').read()
    except Exception as e:
        print(fn,'ERR',e); return
    print('='*12, fn, len(h))
    rows=re.findall(pat, h)
    seen=set()
    for r in rows[:40]:
        key=tuple(x[:90] for x in r)
        if key in seen: continue
        seen.add(key)
        print(' | '.join(x.strip()[:100] for x in r))

titlerows('scmp_rss.xml', r'<item>(.*?)</item>')
