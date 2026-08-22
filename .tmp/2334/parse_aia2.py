import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/2334/aia.html', encoding='utf-8', errors='ignore').read()
# AIA newsroom cards: find div blocks containing press-release links + dates nearby
# Print raw text around the first 5 press release links
count = 0
for m in re.finditer(r'<a[^>]+href="([^"]*press-releases/2026/[^"]+)"[^>]*>(.*?)</a>', raw, re.S):
    if count >= 12: break
    u, t = m.group(1), strip_tags(m.group(2))
    ctx = raw[m.start()-800:m.start()]
    # dates often appear in the card: DD MMM YYYY
    d = re.findall(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+20\d{2})', ctx)
    print('AIA |', t[:70], '|', d[-2:] if d else 'NODATE')
    count += 1
