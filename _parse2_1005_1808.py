import json, re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def cliptxt(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

print('=== InsuranceAsiaNews WP API (json) ===')
d = json.load(open(CACHE+'ian.json'))
for p in d:
    print('  ', p.get('date'), '|', cliptxt(p.get('title',{}).get('rendered',''))[:105])
    print('      ', p.get('link'))

print()
print('=== HKMA press releases ===')
h = open(CACHE+'hkma_press.html', encoding='utf-8', errors='replace').read()
rows = re.findall(r'<a[^>]+href="([^"]*press-release[^"]*)"[^>]*>(.*?)</a>', h, re.S)
seen = set()
for u, t in rows:
    t = cliptxt(t)
    if not t or t in seen: continue
    seen.add(t)
    print('  ', t[:110], '|', u if u.startswith('http') else 'https://www.hkma.gov.hk'+u)
    if len(seen) > 14: break

print()
print('=== AIA press (html) ===')
a = open(CACHE+'aia.html', encoding='utf-8', errors='replace').read()
print('  len', len(a))
for m in re.finditer(r'"title"\s*:\s*"([^"]{10,140})"', a)  :
    print('   T:', m.group(1)[:120])
for m in re.finditer(r'href="(/zh-hk/about-aia/about-us/media-centre/press-releases/[^"]+)"', a):
    print('   U:', m.group(1))

print()
print('=== Prudential newsroom ===')
p = open(CACHE+'prudential.html', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'href="([^"]*newsroom[^"]*)"[^>]*>\s*([^<]{8,140})', p):
    print('  ', cliptxt(m.group(2))[:110], '|', m.group(1))

print()
print('=== AXA newsroom ===')
x = open(CACHE+'axa.html', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'href="([^"]*news[^"]*)"[^>]*>\s*([^<]{8,140})', x):
    print('  ', cliptxt(m.group(2))[:110], '|', m.group(1))

print()
print('=== Sun Life newsroom ===')
s = open(CACHE+'sunlife.html', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'href="([^"]*news[^"]*)"[^>]*>\s*([^<]{8,140})', s):
    print('  ', cliptxt(m.group(2))[:110], '|', m.group(1))
