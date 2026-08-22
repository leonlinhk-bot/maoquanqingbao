import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

# AXA
raw = open('.tmp/2334/axa.html', encoding='utf-8', errors='ignore').read()
print('AXA len', len(raw))
for m in re.finditer(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+20\d{2}|\d{4}-\d{2}-\d{2})', raw):
    s = m.start()
    ctx = strip_tags(raw[max(0,s-500):s])
    print('AXA |', ctx[-80:], ' <<', m.group(1))
