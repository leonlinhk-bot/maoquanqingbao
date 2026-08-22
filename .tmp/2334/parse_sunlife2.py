import re, html

def strip_tags(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return html.unescape(re.sub(r'\s+', ' ', s)).strip()

raw = open('.tmp/2334/sunlife.html', encoding='utf-8', errors='ignore').read()
# print context around first news release link
m = re.search(r'news-releases/2026/sun-life-mpf-nearly-20', raw)
if m:
    print(strip_tags(raw[m.start()-1000:m.start()+400])[:1200])
