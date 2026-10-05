import json, re, html
CACHE = '/Users/leonliang/maoquanqingbao/data/_cache1005_1808/'

def cliptxt(s):
    s = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

print('=== Artemis news ===')
a = open(CACHE+'artemis.html', encoding='utf-8', errors='replace').read()
# artemis lists with dates
for m in re.finditer(r'<a[^>]+href="(https://www\.artemis\.bm/news/[^"]+)"[^>]*>(.*?)</a>', a, re.S):
    t = cliptxt(m.group(2))
    if len(t) < 15: continue
    print('  ', t[:120], '|', m.group(1))
print()

print('=== InsuranceBusinessMag asia breaking news ===')
i = open(CACHE+'ibm.html', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<a[^>]+href="([^"]*/news/[^"]+)"[^>]*>(.*?)</a>', i, re.S):
    t = cliptxt(m.group(2))
    if len(t) < 20: continue
    print('  ', t[:120], '|', m.group(1))
print()

print('=== govhk general_zh RSS (recent 25) ===')
g = open(CACHE+'govhk_zh.xml', encoding='utf-8', errors='replace').read()
items = re.findall(r'<item>(.*?)</item>', g, re.S)
for b in items[:25]:
    t = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', b, re.S)
    d = re.search(r'<pubDate>(.*?)</pubDate>', b, re.S)
    l = re.search(r'<link>(.*?)</link>', b, re.S)
    print('  ', (d.group(1) if d else '?').strip(), '|', cliptxt(t.group(1) if t else '')[:100])
    print('      ', (l.group(1) if l else '').strip())
print()

print('=== NFRA index ===')
n = open(CACHE+'nfra.html', encoding='utf-8', errors='replace').read()
print(' len', len(n))
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*title="([^"]{10,120})"', n):
    print('  ', cliptxt(m.group(2))[:110], '|', m.group(1))
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', n, re.S):
    t = cliptxt(m.group(2))
    if len(t) > 12:
        print('  T:', t[:110], '|', m.group(1)[:120])
