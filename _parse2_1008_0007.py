import json, re, time
D='.tmp/1008_0007'
live=json.load(open('data/live-items.json'))
have={it.get('id') for it in live['items']}
have_url={it.get('originalUrl','') for it in live['items']}
have_sk={}
for it in live['items']:
    have_sk.setdefault(it.get('sourceKey'),[]).append(it.get('publishedAt',''))
print('total', len(live['items']))

# ---- insuranceasia html parse ----
try:
    h=open(f'{D}/iaasia.html',encoding='utf-8',errors='ignore').read()
    rows=re.findall(r'href="(https://insuranceasia\.com/[^"]+)"[^>]*>\s*([^<]{15,160})', h)
    seen=set(); out=[]
    for u,t in rows:
        if u in seen or '/insurance/' == u[-11:]: continue
        seen.add(u); out.append((t.strip()[:100], u))
    print('=== INSURANCEASIA links', len(out))
    for t,u in out[:35]:
        dup = 'DUP' if u in have_url else '   '
        print(dup, t, '|', u)
except Exception as e:
    print('iaasia err', e)

# ---- IBM dates ----
try:
    h=open(f'{D}/ibm.html',encoding='utf-8',errors='ignore').read()
    # look for date strings near article links
    for m in re.finditer(r'(\d{1,2} \w{3} 2026|\d{4}-\d{2}-\d{2})[^<]{0,200}?href="(/asia/news/[^"]+\.aspx)"', h):
        print('IBMDATE', m.group(1), m.group(2))
    print('--- ibm alt ---')
    for m in re.finditer(r'href="(/asia/news/[^"]+\.aspx)"[^>]*>([^<]{10,140})', h):
        print('IBMLINK', m.group(2)[:80], '|', m.group(1))
    # datetime attributes
    print('--- ibm datetime attrs ---')
    for m in list(re.finditer(r'datetime="([^"]+)"[^>]*>|<time[^>]*>([^<]+)</time>', h))[:30]:
        print('T', m.group(0)[:120])
except Exception as e:
    print('ibmerr', e)

# ---- Artemis article dates ----
try:
    h=open(f'{D}/artemis.html',encoding='utf-8',errors='ignore').read()
    for m in re.finditer(r'<article[^>]*>(.{0,1200}?)</article>', h, re.S):
        seg=m.group(1)
        u=re.search(r'href="(https://www\.artemis\.bm/news/[a-z0-9\-]+/)"', seg)
        t=re.search(r'<h[23][^>]*>\s*<a[^>]*>([^<]{10,160})', seg)
        d=re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+2026', seg)
        if u: print('ART', d.group(0) if d else '?', '|', (t.group(1) if t else '')[:80], '|', u.group(1))
except Exception as e:
    print('arterr', e)
