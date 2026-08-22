import re, html

def body_text(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    body = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(re.sub(r'\s+', ' ', body))
    return body

files = [
    ('.tmp/0821/iaa_hdi.html', 'HDI GLOBAL H1'),
    ('.tmp/0821/iaa_jp_credit.html', 'JAPANESE LIFE PRIVATE CREDIT'),
    ('.tmp/0821/iaa_sumitomo.html', 'SUMITOMO Q1'),
    ('.tmp/0821/ib_aia_broker.html', 'AIA BROKER ACCESS'),
    ('.tmp/0821/ib_allianz.html', 'ALLIANZ TRADE CHINA CEO'),
    ('.tmp/0821/ib_pingan.html', 'PING AN NBV TRAILS'),
]
for path, label in files:
    b = body_text(path)
    print('=' * 90)
    print(label)
    # find first meaningful paragraph after nav
    i = b.find('Subscribe')
    j = b.find('Related')
    seg = b[i+40:j] if i >= 0 and j > i else b[300:1800]
    seg = re.sub(r'^(.*?)Read in App', '', seg)
    print(seg[:1100])
    print()
