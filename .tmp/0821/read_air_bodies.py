import re, html

def body_text(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    body = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(re.sub(r'\s+', ' ', body))
    return body

for f, label in [('.tmp/0821/air_96629_etf.html', 'NFRA ETF RELAX'),
                 ('.tmp/0821/air_96628_health.html', 'CHINA HEALTH PLAN'),
                 ('.tmp/0821/air_96627_pingan.html', 'PING AN H1')]:
    b = body_text(f)
    # locate article start: after title line
    i = b.find('By ')
    print('=' * 90)
    print(label)
    print(b[i:i+1400])
    print()
