import re, html, json

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/iaasia-insurance.html', encoding='utf-8', errors='ignore').read()
# find article blocks: look for <a href=...>title</a> followed by dates
# try to find date-like strings near hrefs
arts = re.findall(r'<a[^>]+href="(https://insuranceasia\.com/insurance/(?:news|in-focus|exclusive|insights|features)/[^"]+)"[^>]*>(.*?)</a>(.{0,600}?)(?=<a|$)', raw, flags=re.S)
print('blocks:', len(arts))
for u, t, after in arts:
    t = strip_tags(t)
    dates = re.findall(r'(\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{4}|\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})', after)
    print(u.split('/')[-1][:60], '|', t[:60], '|', dates[:2])
