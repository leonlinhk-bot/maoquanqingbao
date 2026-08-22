import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

MONTHS = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

for name, fn in [('PRU', '.tmp/2334/pru.html'), ('SUNLIFE', '.tmp/2334/sunlife.html'), ('AXA', '.tmp/2334/axa.html')]:
    raw = open(fn, encoding='utf-8', errors='ignore').read()
    print(f'===== {name} len {len(raw)}')
    # grab all date-like strings with 500 chars before
    for m in re.finditer(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+20\d{2})', raw):
        s = m.start()
        ctx = strip_tags(raw[max(0,s-600):s])
        print('...', ctx[-90:], ' <<DATE>> ', m.group(1))
