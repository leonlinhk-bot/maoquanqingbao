import json, re, subprocess, os
D='.tmp/1008_0007'
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36'

def get(url, out):
    subprocess.run(['curl','-sL','-m','25','-A',UA,'-o',out,url], check=False)
    try:
        return open(out, encoding='utf-8', errors='ignore').read()
    except Exception:
        return ''

# --- ARTEMIS article list with dates ---
h=open(f'{D}/artemis.html',encoding='utf-8',errors='ignore').read()
print('=== ARTEMIS with dates ===')
# split by article
arts=re.split(r'(?=<article)', h)
for seg in arts:
    u=re.search(r'href="(https://www\.artemis\.bm/news/[a-z0-9\-]+/)"', seg)
    if not u: continue
    t=re.search(r'>([^<>]{15,160})</a>', seg)
    d=re.search(r'(\d{1,2}(?:st|nd|rd|th)?\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+2026|(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+2026)', seg)
    print((d.group(0) if d else '?'), '|', (t.group(1).strip() if t else '')[:75], '|', u.group(1))
