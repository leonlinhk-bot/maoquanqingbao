import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/2334/pru.html', encoding='utf-8', errors='ignore').read()
# dump all hrefs with text, filter meaningful
seen = set()
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    t = strip_tags(m.group(2))
    if len(t) < 12 or m.group(1) in seen: continue
    seen.add(m.group(1))
    print('PRU |', m.group(1)[:85], '|', t[:70])
