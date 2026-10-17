import re, html, os
raw = open('/Users/leonliang/maoquanqingbao/.cache1018_0012/scmp.html', encoding='utf-8', errors='ignore').read()
# find article links with dates in the page JSON/HTML
seen = set()
cnt = 0
for m in re.finditer(r'"datePublished":"([^"]+)"[^{}]{0,800}?"headline":"([^"]{10,200})"', raw):
    date, head = m.group(1), m.group(2)
    if date < '2026-10-16':
        continue
    if head in seen:
        continue
    seen.add(head)
    print(date, '|', html.unescape(head)[:120])
    cnt += 1
print('found', cnt)
# fallback: article links
if cnt == 0:
    for m in re.finditer(r'<a[^>]+href="(/[^"]*article/[^"]+)"[^>]*>(.*?)</a>', raw, flags=re.S):
        t = re.sub(r'<[^>]+>', ' ', m.group(2))
        t = re.sub(r'\s+', ' ', html.unescape(t)).strip()
        if len(t) > 20 and t not in seen:
            seen.add(t)
            print(m.group(1)[:100], '|', t[:110])
            cnt += 1
            if cnt > 40:
                break
