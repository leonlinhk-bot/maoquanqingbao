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

for tag, u in [
    ('steadfast', 'https://www.insurancebusinessmag.com/asia/news/breaking-news/steadfast-lifts-profit-as-us-consortium-moves-to-take-it-private-587463.aspx'),
    ('sg-west-island', 'https://www.insurancebusinessmag.com/asia/news/construction/singapores-new-western-island-will-need-insurance-tools-that-do-not-yet-exist-587445.aspx'),
    ('vn-credit', 'https://www.insurancebusinessmag.com/asia/news/breaking-news/vietnams-trade-boom-outpaces-its-credit-insurance-market-587443.aspx'),
]:
    html = curl(u)
    # JSON-LD articleBody
    body = ''
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            d = json.loads(m.group(1))
            if isinstance(d, list):
                d = d[0] if d else {}
            if 'articleBody' in d:
                body = d['articleBody']
                break
        except Exception:
            pass
    if not body:
        # paragraphs
        m = re.search(r'<div class="article-detail__left__content">(.*?)</div>\s*</div>', html, re.S)
        if m:
            body = clean(m.group(1))
    print(f'--- {tag} | body: {body[:700]}')
    print()
