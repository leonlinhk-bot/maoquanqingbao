import re, html

raw = open('.tmp/0821/hkma.html', encoding='utf-8', errors='ignore').read()
print('HKMA len', len(raw))
# HKMA press releases list page - look for article links with dates
seen = set()
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    href = m.group(1)
    txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
    if not txt or len(txt) < 12:
        continue
    if any(k in href.lower() for k in ['press-release', 'news', 'article', '2026', 'pr-']):
        key = (txt[:60], href[:80])
        if key in seen:
            continue
        seen.add(key)
        print(repr(txt[:90]), '->', href[:150])
