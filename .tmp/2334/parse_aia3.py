import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/2334/aia.html', encoding='utf-8', errors='ignore').read()
# find all date-like strings with surrounding context in the 2026 section
idx = raw.find('press-releases/2026')
# Find first press release link block and print 2000 chars around it
m = re.search(r'<a[^>]+href="([^"]*press-releases/2026/[^"]+)"[^>]*>(.*?)</a>', raw, re.S)
start = m.start()
print(strip_tags(raw[start-1500:start+500])[:1500])
