import re, json
D='.tmp/1008_0007'
live=json.load(open('data/live-items.json'))
have={it['id'] for it in live['items']}

# --- search live for possible dups ---
for k in ['corechoice','flexichoice','medical-freedom','smart-health','aia','sunlife','axa','manulife','pru']:
    hits=[it['id'] for it in live['items'] if k in it.get('id','').lower()]
    print(k, len(hits), hits[:6])
print()

# --- AIA page: find link+title+date near top ---
h=open(f'{D}/aia.html',encoding='utf-8',errors='ignore').read()
print('=== AIA news links ===')
seen=set()
for m in re.finditer(r'href="([^"]*(?:press-release|media-centre|news)[^"]*)"', h):
    u=m.group(1)
    if u in seen: continue
    seen.add(u)
    seg=h[m.start():m.start()+400]
    t=re.search(r'>([^<>]{12,160})<', seg)
    print('  ', u[:110], '|', (t.group(1).strip() if t else '')[:80])
    if len(seen)>25: break

print('=== AIA dates on page ===')
for m in list(re.finditer(r'(20\d\d[-/]\d\d[-/]\d\d|\d{1,2}\s+\w{3}\s+20\d\d|\w+ \d{1,2}, 20\d\d)', h))[:25]:
    print('  ', m.group(0))
