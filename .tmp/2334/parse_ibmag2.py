import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/2334/ibmag.html', encoding='utf-8', errors='ignore').read()
# all hrefs
hrefs = re.findall(r'href="([^"]+)"', raw)
from collections import Counter
print(Counter(h.split('/')[3] if len(h.split('/'))>3 else h for h in hrefs if 'insurancebusinessmag' in h).most_common(8))
news = [h for h in hrefs if '/asia/news/' in h and h not in ['https://www.insurancebusinessmag.com/asia/news/breaking-news/']]
seen = set()
for h in news:
    if h in seen: continue
    seen.add(h)
print('unique news urls:', len(seen))
for h in list(seen)[:40]:
    print(h)
