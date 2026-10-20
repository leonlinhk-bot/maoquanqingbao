import re, os, html, sys
BASE = '/Users/leonliang/maoquanqingbao/.cache1020_1808'
FILES = ['air97221.html', 'air97220.html', 'air97259.html', 'air97257.html',
         'iaasia_sunlife.html', 'ian_cyclone.html', 'ian_howden.html',
         'ia_indonesia.html', 'ia_taiwan.html', 'ia_hdfc.html']


def clean(fn):
    t = open(os.path.join(BASE, fn), encoding='utf-8', errors='ignore').read()
    t = re.sub(r'<script.*?</script>', ' ', t, flags=re.S | re.I)
    t = re.sub(r'<style.*?</style>', ' ', t, flags=re.S | re.I)
    # meta dates
    metas = re.findall(r'<meta[^>]+(?:property|name)="(article:published_time|published_time|pubdate|date|og:title)"[^>]+content="([^"]*)"', t, re.I)
    body = re.sub(r'<[^>]+>', '\n', t)
    lines = [re.sub(r'\s+', ' ', html.unescape(x)).strip() for x in body.split('\n')]
    lines = [x for x in lines if x]
    return metas, lines


for fn in FILES:
    metas, lines = clean(fn)
    print('=' * 90)
    print('##', fn)
    print('META:', metas[:6])
    # print first meaningful 45 lines after title-ish content
    txt = [l for l in lines if len(l) > 40]
    print('TITLE:', txt[0][:150] if txt else '')
    print('--- first paragraphs ---')
    shown = 0
    for l in txt[1:60]:
        if len(l) > 60:
            print('  ', l[:400])
            shown += 1
        if shown >= 12:
            break
