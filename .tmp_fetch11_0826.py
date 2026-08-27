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

def ddg(q, n=6):
    html = curl('https://html.duckduckgo.com/html/?q=' + urllib.parse.quote(q))
    out = []
    for block in re.findall(r'<div class="result results_links.*?</div>\s*</div>', html, re.S)[:n]:
        m = re.search(r'<a[^>]+class="result__a"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', block, re.S)
        if m:
            href = m.group(1)
            if 'uddg=' in href:
                href = urllib.parse.unquote(href.split('uddg=')[1].split('&')[0])
            title = clean(m.group(2))
            sn = re.search(r'class="result__snippet"[^>]*>(.*?)</a>', block, re.S)
            snippet = clean(sn.group(1))[:120] if sn else ''
            out.append((title[:90], href[:160], snippet))
    return out

print('===== DuckDuckGo: resolve URLs =====')
targets = [
    ('scmp-corruption', 'scmp.com "Beijing targets cross-border corruption" Hong Kong markets'),
    ('taiping-h1', '中國太平 中期業績 2026 盈利 90% 00966'),
    ('barclays-offshore', '巴克萊 離岸資產 監管 擴大 香港 星島'),
    ('woo-fo', '吳光正 家族辦公室 私募股權 出售'),
    ('sfi-impact', 'SFi 影響力週 家族辦公室 調查 系統性影響力投資'),
    ('hkma-cross-boundary-annuity', 'HKMA 跨境 年金 發放 服務 香港年金公司'),
]
for tag, q in targets:
    print(f'--- {tag}: {q}')
    try:
        for title, href, sn in ddg(q):
            print('   ', title)
            print('      ', href)
            if sn:
                print('      sn:', sn)
    except Exception as e:
        print('   ERR', e)

print()
print('===== insurtechinsights article dates =====')
for tag, u in [
    ('coverme', 'https://www.insurtechinsights.com/manulife-launches-coverme-travel-insurance-app-inside-chatgpt/'),
    ('steadfast-buyout', 'https://www.insurtechinsights.com/5-5bn-buyout-kkr-backed-consortium-to-acquire-steadfast-group-with-amwins-and-dragoneer/'),
    ('riverstone-qbe', 'https://www.insurtechinsights.com/1-6bn-deal-riverstone-international-takes-on-qbe-legacy-reserves/'),
]:
    try:
        html = curl(u)
        dp = re.findall(r'"datePublished"\s*:\s*"([^"]+)"', html)
        dt = re.findall(r'datetime="([^"]+)"', html)
        title = re.search(r'<title>(.*?)</title>', html, re.S)
        m = re.search(r'<meta[^>]+name="description"[^>]+content="([^"]+)"', html)
        print(f'--- {tag} | title: {(title.group(1).strip()[:70] if title else "?")}')
        print('    datePublished:', dp[:1], '| datetime:', dt[:2])
        print('    desc:', (m.group(1)[:250] if m else '?'))
    except Exception as e:
        print(f'--- {tag} ERR {e}')
