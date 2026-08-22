#!/usr/bin/env python3
import re, html

def body_text(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    body = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(re.sub(r'\s+', ' ', body))
    return body

targets = [
    ('.tmp/0821/air_96629_etf.html', 'NFRA ETF RELAX', 'The National Financial Regulatory Administration'),
    ('.tmp/0821/air_96628_health.html', 'CHINA HEALTH PLAN', 'China has unveiled a five-year plan'),
    ('.tmp/0821/air_96627_pingan.html', 'PING AN H1', 'net profit attributable to shareholders'),
    ('.tmp/0821/air_96605_reins.html', 'REINS CAPITAL', 'Reinsurance'),
    ('.tmp/0821/air_96602_mas.html', 'MAS ASSET MGMT', 'MAS'),
    ('.tmp/0821/air_96590_hnwi.html', 'HNWI INSURANCE DEMAND', 'HNWI'),
]
for f, label, needle in targets:
    b = body_text(f)
    i = b.find(needle)
    print('=' * 90)
    print(label)
    print(b[i:i+1100] if i >= 0 else b[300:1300])
    print()
