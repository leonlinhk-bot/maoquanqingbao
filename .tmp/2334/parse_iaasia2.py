import re, html, json

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/iaasia-insurance.html', encoding='utf-8', errors='ignore').read()
# find all hrefs
hrefs = re.findall(r'href="([^"]+)"', raw)
print('total hrefs:', len(hrefs))
from collections import Counter
c = Counter(h.split('/')[1] if h.startswith('/') else h.split('/')[0] for h in hrefs)
print(c.most_common(15))
# unique article-like urls
arts = [h for h in hrefs if any(x in h for x in ['/insurance/', 'article', 'story'])]
seen = set(); out = []
for h in arts:
    if h in seen: continue
    seen.add(h); out.append(h)
for h in out[:50]:
    print(h)
