import re, html, json

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

# --- InsuranceAsia insurance news page ---
raw = open('.tmp/iaasia-insurance.html', encoding='utf-8', errors='ignore').read()
print('IAASIA len', len(raw))
# links to articles: /insurance/... .html
arts = re.findall(r'<a[^>]+href="(/insurance/[^"#]+\.html)"[^>]*>(.*?)</a>', raw, flags=re.S)
seen = set(); out = []
for u, t in arts:
    t = strip_tags(t)
    if u in seen or not t: continue
    seen.add(u); out.append((u, t))
print('iaasia article links:', len(out))
for u, t in out[:45]:
    print(u, '|', t[:90])
