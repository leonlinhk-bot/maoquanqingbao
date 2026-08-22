import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/2334/ibmag.html', encoding='utf-8', errors='ignore').read()
print('ibmag len', len(raw))
# InsuranceBusiness structure: <a href="...article...">TITLE</a> with date in <time> or li
arts = re.findall(r'<a[^>]+href="(https://www\.insurancebusinessmag\.com/asia/news/[^"]+)"[^>]*>(.*?)</a>(.{0,500}?)', raw, re.S)
seen = set()
for u, t, after in arts:
    t = strip_tags(t)
    if not t or u in seen: continue
    seen.add(u)
    d = re.findall(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|\d{4}-\d{2}-\d{2})', after)
    ago = re.findall(r'(\d+\s+(?:hour|day|week|month|minute)s?\s+ago)', after)
    print(u.split('/')[-1][:60], '|', t[:60], '|', d[:1], ago[:1])
