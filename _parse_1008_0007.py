import json, re, os, time
D='.tmp/1008_0007'
CUT=time.mktime(time.strptime('2026-10-07 18:13','%Y-%m-%d %H:%M'))

def show(title, rows):
    print('='*20, title, f'({len(rows)})')
    for r in rows[:25]:
        print(' | '.join(str(x) for x in r))

# --- insuranceasianews WP JSON ---
try:
    d=json.load(open(f'{D}/ianews.json'))
    rows=[]
    for p in d:
        rows.append((p.get('date','')[:16], re.sub('<[^>]+>','',p.get('title',{}).get('rendered',''))[:90], p.get('link','')))
    rows.sort(reverse=True)
    show('IANEWS (top dated)', rows)
except Exception as e:
    print('ianews err', e)

# --- govhk RSS ---
try:
    x=open(f'{D}/fstb.xml',encoding='utf-8',errors='ignore').read()
    items=re.findall(r'<item>(.*?)</item>', x, re.S)
    rows=[]
    for it in items:
        t=re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
        l=re.search(r'<link>(.*?)</link>', it, re.S)
        p=re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        rows.append((p.group(1).strip() if p else '', (t.group(1).strip() if t else '')[:90], (l.group(1).strip() if l else '')))
    show('GOVHK RSS', rows)
except Exception as e:
    print('govhk err', e)

# --- HKMA html ---
try:
    h=open(f'{D}/hkma.html',encoding='utf-8',errors='ignore').read()
    # find date + title pairs
    rows=re.findall(r'(\d{1,2} \w{3} 2026)[^<]*</[^>]+>\s*(?:<[^>]+>\s*)*<a[^>]*href="([^"]+)"[^>]*>\s*([^<]{5,140})', h)
    show('HKMA raw', rows)
    # alt: look for 'press-release' links
    rows2=re.findall(r'href="([^"]*press-release[^"]*)"[^>]*>\s*([^<]{8,140})', h)
    show('HKMA press links', rows2)
except Exception as e:
    print('hkma err', e)

# --- IBM ---
try:
    h=open(f'{D}/ibm.html',encoding='utf-8',errors='ignore').read()
    rows=re.findall(r'href="(/asia/news/[^"]+)"[^>]*>\s*([^<]{10,160})', h)
    seen=set(); out=[]
    for u,t in rows:
        if u in seen: continue
        seen.add(u); out.append((t.strip()[:110], u))
    show('IBM links', out)
except Exception as e:
    print('ibm err', e)

# --- ARTEMIS ---
try:
    h=open(f'{D}/artemis.html',encoding='utf-8',errors='ignore').read()
    rows=re.findall(r'href="(https://www\.artemis\.bm/news/[^"]+)"[^>]*>\s*([^<]{12,150})', h)
    seen=set(); out=[]
    for u,t in rows:
        if u in seen: continue
        seen.add(u); out.append((t.strip()[:110], u))
    show('ARTEMIS', out)
except Exception as e:
    print('artemis err', e)

# --- NFRA ---
try:
    h=open(f'{D}/nfra.html',encoding='utf-8',errors='ignore').read()
    rows=re.findall(r'href="([^"]*ItemDetail[^"]*)"[^>]*>\s*([^<]{6,120})', h)
    seen=set(); out=[]
    for u,t in rows:
        if u in seen: continue
        seen.add(u); out.append((t.strip()[:110], u))
    show('NFRA', out)
except Exception as e:
    print('nfra err', e)

# --- SCMP ---
try:
    h=open(f'{D}/scmp.html',encoding='utf-8',errors='ignore').read()
    rows=re.findall(r'href="(/news/[^"]+)"[^>]*>([^<]{15,150})', h)
    seen=set(); out=[]
    for u,t in rows:
        if u in seen: continue
        seen.add(u); out.append((t.strip()[:110], u))
    show('SCMP', out[:40])
except Exception as e:
    print('scmp err', e)
