import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

# PRU: check structure
raw = open('.tmp/2334/pru.html', encoding='utf-8', errors='ignore').read()
# find headings/article links
for m in re.finditer(r'<a[^>]+href="([^"]*(?:news|press)[^"]*)"[^>]*>(.*?)</a>', raw, re.S):
    t = strip_tags(m.group(2))
    if len(t) < 15: continue
    u = m.group(1)
    if 'prudential.com.hk' in u or u.startswith('/'):
        print('PRU |', u[:80], '|', t[:70])
