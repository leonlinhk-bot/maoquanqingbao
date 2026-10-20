import re, os, html
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
FILES = ['rn_nms.html', 'rn_moodys.html', 'rn_gal.html', 'art_ambest.html', 'ian_cyber.html']

for fn in FILES:
    t = open(os.path.join(BASE, fn), encoding='utf-8', errors='ignore').read()
    pubs = re.findall(r'(?:property|name)="(?:article:published_time|published_time)"[^>]+content="([^"]+)"', t)
    t2 = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
    t2 = re.sub(r'<style.*?</style>', ' ', t2, flags=re.S | re.I)
    # main article paragraphs
    paras = re.findall(r'<p[^>]*>(.*?)</p>', t2, re.S)
    clean = []
    for p in paras:
        s = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', p))).strip()
        if len(s) > 70:
            clean.append(s)
    print('=' * 88)
    print('##', fn, 'PUB:', pubs[:2])
    for s in clean[:7]:
        print('  -', s[:600])
