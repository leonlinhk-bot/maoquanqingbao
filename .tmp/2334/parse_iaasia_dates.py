import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/iaasia-insurance.html', encoding='utf-8', errors='ignore').read()
# find "ago" or date markers near article titles
for m in re.finditer(r'<a[^>]+href="(https://insuranceasia\.com/insurance/(?:news|in-focus|exclusive|insights|features)/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    u, t = m.group(1), strip_tags(m.group(2))
    if not t: continue
    ctx = raw[m.end():m.end()+500]
    ago = re.findall(r'(\d+\s+(?:hour|day|week|month|minute)s?\s+ago|\d{4}-\d{2}-\d{2}|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4})', ctx)
    print(u.split('/')[-1][:55], '|', t[:55], '|', ago[:2])
