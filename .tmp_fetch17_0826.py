#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json, html as htmllib, subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def curl(url, timeout=30):
    return subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                          capture_output=True, text=True).stdout

def clean(txt):
    txt = re.sub(r'<script.*?</script>', ' ', txt, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = htmllib.unescape(txt)
    return re.sub(r'\s+', ' ', txt).strip()

d = json.load(open('data/live-items.json'))
items = d['items']
ids = {it['id'] for it in items}
urls = {it.get('originalUrl') for it in items}

print('--- dupe checks ---')
for probe in ['steadfast', 'kkr', 'coverme', 'manulife-ai', 'spillover', 'eastmoney',
              'shouhui', '手回', 'hsbc', 'self-declaration', 'west-island', 'westisland',
              'copay', 'co-pay', 'india-life', 'penetration', 'acb']:
    hits = [i for i in ids if probe in i]
    if hits:
        print(f'  {probe}: {hits}')

print()
print('--- HSBC HK EastMoney article ---')
try:
    html = curl('https://finance.eastmoney.com/a/202608263854423949.html')
    title = re.search(r'<title>(.*?)</title>', html, re.S)
    print('title:', clean(title.group(1))[:100] if title else '?')
    m = re.search(r'<div class="txtinfos"[^>]*>(.*?)</div>', html, re.S)
    if m:
        print('meta:', clean(m.group(1))[:200])
    body = re.findall(r'<p[^>]*>(.*?)</p>', html, re.S)
    txt = ' '.join(clean(p) for p in body)
    print('body:', txt[:900])
except Exception as e:
    print('ERR', e)

print()
print('--- Shouhui article ---')
try:
    html = curl('https://finance.eastmoney.com/a/202608263854433255.html')
    title = re.search(r'<title>(.*?)</title>', html, re.S)
    print('title:', clean(title.group(1))[:100] if title else '?')
    body = re.findall(r'<p[^>]*>(.*?)</p>', html, re.S)
    txt = ' '.join(clean(p) for p in body)
    print('body:', txt[:900])
except Exception as e:
    print('ERR', e)
