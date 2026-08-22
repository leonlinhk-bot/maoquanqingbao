import re, html

for f, label in [('.tmp/0821/hkma_0821_3.html', 'HKMA 0821-3 PBoC RMB bills'),
                 ('.tmp/0821/hkma_0820_4.html', 'HKMA 0820-4 scam alert')]:
    raw = open(f, encoding='utf-8', errors='ignore').read()
    print(f'===== {label} =====')
    # title
    m = re.search(r'<title>(.*?)</title>', raw, re.S)
    if m:
        print('TITLE:', html.unescape(m.group(1)).strip()[:150])
    # published time
    for p in [r'"datePublished"\s*:\s*"([^"]+)"', r'property="article:published_time"\s+content="([^"]+)"',
              r'(\d{1,2}\s+[A-Z][a-z]{2,8}\s+20\d{2})']:
        mm = re.search(p, raw)
        if mm:
            print('DATE:', mm.group(1))
            break
    # main body text
    body = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(re.sub(r'\s+', ' ', body))
    # find relevant slice
    i = body.find('21 August 2026')
    if i < 0:
        i = body.find('20 August 2026')
    if i < 0:
        i = body.find('2026')
    print('BODY:', body[max(0,i-100):i+1200])
    print()
