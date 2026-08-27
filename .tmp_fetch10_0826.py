#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, json, html as htmllib, subprocess, urllib.parse

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def curl(url, timeout=35):
    return subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                          capture_output=True, text=True).stdout

def clean(txt):
    txt = re.sub(r'<script.*?</script>', ' ', txt, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = htmllib.unescape(txt)
    return re.sub(r'\s+', ' ', txt).strip()

def bing_search(q, n=5):
    html = curl('https://www.bing.com/search?q=' + urllib.parse.quote(q) + '&count=15&setlang=en')
    out = []
    # b_algo blocks
    for block in re.findall(r'<li class="b_algo".*?</li>', html, re.S)[:n]:
        m = re.search(r'<h2[^>]*><a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
        if m:
            href = htmllib.unescape(m.group(1))
            title = clean(m.group(2))
            out.append((title[:90], href))
    return out

print('===== Bing HTML: resolve original URLs =====')
targets = [
    ('scmp-corruption', 'SCMP "As Beijing targets cross-border corruption, Hong Kong markets brace"'),
    ('taiping-h1', '中國太平 中期盈利 129億 升90% 新業務價值'),
    ('barclays-offshore', '巴克萊 內地離岸資產監管 進一步擴大 香港'),
    ('woo-fo', '吳光正 家族辦公室 出售 10億美元 私募股權'),
    ('sfi-impact', 'SFi 2026 影響力週 家族辦公室 系統性影響力投資'),
]
for tag, q in targets:
    print(f'--- {tag}: {q}')
    try:
        for title, href in bing_search(q):
            print('   ', title)
            print('      ', href[:160])
    except Exception as e:
        print('   ERR', e)

print()
print('===== IBM article passages =====')
for tag, u in [
    ('steadfast', 'https://www.insurancebusinessmag.com/asia/news/breaking-news/steadfast-lifts-profit-as-us-consortium-moves-to-take-it-private-587463.aspx'),
    ('sg-west-island', 'https://www.insurancebusinessmag.com/asia/news/construction/singapores-new-western-island-will-need-insurance-tools-that-do-not-yet-exist-587445.aspx'),
    ('sg-cfo', 'https://www.insurancebusinessmag.com/asia/news/professional-liability/singapores-cfo-confidence-crash-conceals-a-broker-opening-587444.aspx'),
    ('vn-credit', 'https://www.insurancebusinessmag.com/asia/news/breaking-news/vietnams-trade-boom-outpaces-its-credit-insurance-market-587443.aspx'),
]:
    try:
        html = curl(u)
        passages = re.findall(r'<div class="article__passage[^"]*"[^>]*>(.*?)</div>', html, re.S)
        txt = ' '.join(clean(p) for p in passages)
        print(f'--- {tag}: {txt[:600]}')
    except Exception as e:
        print(f'--- {tag} ERR {e}')

print()
print('===== insurtechinsights knowledge bank =====')
try:
    html = curl('https://www.insurtechinsights.com/knowledge-bank/')
    print('len:', len(html))
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{15,110})</a>', html):
        href, t = m.group(1), htmllib.unescape(m.group(2)).strip()
        print('  ', t[:85], '->', href[:130])
except Exception as e:
    print('ERR', e)

print()
print('===== IA RSS candidates =====')
for u in ['https://www.ia.org.hk/en/rss/press_releases.xml',
          'https://www.ia.org.hk/en/infocenter/rss.xml',
          'https://www.ia.org.hk/rss.xml']:
    r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "15", "-A", UA, u],
                       capture_output=True, text=True)
    print(f'  {u} -> HTTP {r.stdout}')
