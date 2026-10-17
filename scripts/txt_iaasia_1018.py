import re, html
raw = open('/Users/leonliang/maoquanqingbao/.cache1018_0012/iaasia.html', encoding='utf-8', errors='ignore').read()
t = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S | re.I)
t = re.sub(r'<[^>]+>', ' ', t)
t = html.unescape(t)
t = re.sub(r'\s+', ' ', t)
print(t[:3000])
