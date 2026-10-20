import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
rss = open(os.path.join(BASE, 'scmp.xml'), encoding='utf-8', errors='ignore').read()
print('=== SCMP items ===')
for m in re.finditer(r'<item[ >].*?</item>', rss, re.S):
    b = m.group(0)
    ti = re.search(r'<title[^>]*>(.*?)</title>', b, re.S)
    pd = re.search(r'<pubDate[^>]*>(.*?)</pubDate>', b, re.S)
    li = re.search(r'<link[^>]*>(.*?)</link>', b, re.S)
    t = html.unescape(re.sub(r'<[^>]+>', '', ti.group(1))) if ti else ''
    if re.search(r'insur|壽險|寿险|保險|保险|annuit|policy|MPF|強積金|reinsur', t, re.I):
        print((pd.group(1)[:25] if pd else '??'), '|', t[:100])
        print('   ', li.group(1)[:110] if li else '')

print('\n=== IBM asia page ===')
t = open(os.path.join(BASE, 'ibm_asia.html'), encoding='utf-8', errors='ignore').read()
t2 = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', t2, re.S):
    href, inner = m.group(1), m.group(2)
    s = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', inner))).strip()
    if len(s) > 40 and '/asia/news/' in href:
        print(s[:110], '||', href[:100])
