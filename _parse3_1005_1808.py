import json, re, html
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def cliptxt(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

print('=== Prudential HK newsroom ===')
p = open(CACHE+'prudential.html', encoding='utf-8', errors='replace').read()
hits = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', p, re.S)
for u, t in hits:
    t = cliptxt(t)
    if len(t) < 12: continue
    if any(k in u.lower() for k in ('news', 'press', 'media')) or any(k in t for k in ('2026', '2025')):
        print('  ', t[:110], '|', u)
print()

print('=== AXA HK newsroom ===')
x = open(CACHE+'axa.html', encoding='utf-8', errors='replace').read()
for u, t in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', x, re.S):
    t = cliptxt(t)
    if len(t) < 12: continue
    print('  ', t[:110], '|', u)
print()

print('=== Sun Life HK newsroom ===')
s = open(CACHE+'sunlife.html', encoding='utf-8', errors='replace').read()
for u, t in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', s, re.S):
    t = cliptxt(t)
    if len(t) < 15: continue
    print('  ', t[:115], '|', u)
