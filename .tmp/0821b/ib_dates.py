#!/usr/bin/env python3
import re, html, glob, os

def body_text(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    body = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(re.sub(r'\s+', ' ', body))
    return body

for f in ['.tmp/0821/ib_aia_broker.html', '.tmp/0821/ib_allianz.html', '.tmp/0821/ib_pingan.html',
          '.tmp/0821/ib_hk_postcode.html', '.tmp/0821/ib_oona.html', '.tmp/0821/ib_rebuild.html',
          '.tmp/0821/ib_gallagher.html', '.tmp/0821/ib_586726.html', '.tmp/0821/ib_586773.html']:
    if not os.path.exists(f):
        continue
    b = body_text(f)
    m = re.search(r'By [A-Za-z .\u2019-]+ (Aug|Sep|Oct) \d{1,2}, 20\d{2}', b)
    m2 = re.search(r'(Aug|Sep|Oct) \d{1,2}, 20\d{2}', b)
    title = ''
    t = re.search(r'<title>(.*?)</title>', open(f, encoding='utf-8', errors='ignore').read(), re.S)
    if t:
        title = html.unescape(t.group(1)).strip()[:100]
    print('=' * 80)
    print(os.path.basename(f), '| DATE:', (m.group(0) if m else (m2.group(0) if m2 else '?')))
    print('TITLE:', title)
    # body snippet around the headline
    i = b.find('Share')
    print('BODY:', b[i:i+500].strip()[:450] if i > 0 else b[300:750])
