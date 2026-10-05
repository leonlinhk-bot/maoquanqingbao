import re, html, os
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def txt(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

# IBM life sciences
d = open(CACHE+'a_ibm_lifesci', encoding='utf-8', errors='replace').read()
m = re.search(r'<h1[^>]*>(.*?)</h1>', d, re.S)
print('IBM H1:', txt(m.group(1))[:150] if m else '?')
paras = re.findall(r'<p[^>]*>(.*?)</p>', d, re.S)
out = [txt(p) for p in paras]
out = [p for p in out if len(p) > 60]
print('IBM BODY:', ' '.join(out[:5])[:1400])
print()
print('IBM preview/desc:', re.search(r'name="description" content="([^"]{20,400})"', d).group(1) if re.search(r'name="description" content="([^"]{20,400})"', d) else '-')
print()

# NFRA
n = open(CACHE+'nfra.html', encoding='utf-8', errors='replace').read()
print('NFRA size', len(n))
print('NFRA text:', txt(n)[:900])
print()

# Sun Life newsroom dates
s = open(CACHE+'sunlife.html', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'(2026[-/年]\d{1,2}[-/月]\d{1,2})', s):
    pass
dates = re.findall(r'(\d{4}[/-]\d{2}[/-]\d{2})', s)
print('SunLife date strings:', sorted(set(dates))[-12:])
