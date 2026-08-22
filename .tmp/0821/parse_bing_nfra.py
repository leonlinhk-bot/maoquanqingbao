import re, html

raw = open('.tmp/0821/bing_nfra.html', encoding='utf-8', errors='ignore').read()
print('=== bing_nfra results ===')
for m in re.finditer(r'<li class="b_algo".*?</li>', raw, re.S):
    blk = m.group(0)
    a = re.search(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', blk, re.S)
    if not a:
        continue
    href = a.group(1)
    title = html.unescape(re.sub(r'<[^>]+>', '', a.group(2))).strip()
    snip = re.search(r'<p[^>]*>(.*?)</p>', blk, re.S)
    s = html.unescape(re.sub(r'<[^>]+>', '', snip.group(1))).strip() if snip else ''
    print(f'- {title[:90]}')
    print(f'  {href[:120]}')
    print(f'  {s[:150]}')
