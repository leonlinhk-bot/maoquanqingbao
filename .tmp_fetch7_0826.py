#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html as htmllib, subprocess

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0.0.0 Safari/537.36")

def curl(url, timeout=35, extra=None):
    cmd = ["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA,
           "-H", "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "-H", "Accept-Language: zh-HK,zh;q=0.9,en;q=0.8",
           "-H", "sec-ch-ua: \"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
           "-H", "sec-ch-ua-mobile: ?0",
           "-H", "sec-ch-ua-platform: \"macOS\"",
           "-H", "Upgrade-Insecure-Requests: 1"]
    if extra:
        cmd += extra
    cmd.append(url)
    return subprocess.run(cmd, capture_output=True, text=True).stdout

def clean(txt):
    txt = re.sub(r'<script.*?</script>', ' ', txt, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = htmllib.unescape(txt)
    return re.sub(r'[ \t]+', ' ', txt)

print('===== 1. IA press releases (curl, full headers) =====')
for u in ['https://www.ia.org.hk/en/infocenter/press_releases.html',
          'https://www.ia.org.hk/tc/infocenter/press_releases.html']:
    txt = curl(u)
    print(f'--- {u} len={len(txt)}')
    if len(txt) > 1000:
        # print dated press items
        for m in re.finditer(r'<a[^>]+href="([^"]*press[^"]*)"[^>]*>([^<]{10,140})', txt):
            href, t = m.group(1), htmllib.unescape(m.group(2)).strip()
            print('  ', t[:90], '->', href[:120])
        print('  [first 400 chars]', clean(txt)[:400])
        break

print()
print('===== 2. IA circulars 2026 (curl) =====')
u = 'https://www.ia.org.hk/en/legislative_framework/circulars/reg_matters/circulars_on_regulatory_matters_2026.html'
txt = curl(u)
print(f'len={len(txt)}')
if len(txt) > 1000:
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>([^<]{10,140})', txt):
        href, t = m.group(1), htmllib.unescape(m.group(2)).strip()
        print('  ', t[:90], '->', href[:120])
    print('  [first 400 chars]', clean(txt)[:400])

print()
print('===== 3. NFRA 重要公告 (curl) =====')
u = ('https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=921&itemId=922'
     '&itemUrl=ItemListRightList.html&itemName=%E9%87%8D%E8%A6%81%E5%85%AC%E5%91%8A')
txt = curl(u)
print(f'len={len(txt)}')
print('  [first 800 chars]', clean(txt)[:800])

print()
print('===== 4. Manulife HK newsroom =====')
for u in ['https://www.manulife.com.hk/zh-hk/individual/about/newsroom.html',
          'https://www.manulife.com.hk/en/individual/about/newsroom.html']:
    txt = curl(u)
    print(f'--- {u} len={len(txt)}')
    if len(txt) > 2000:
        for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{12,120})', txt):
            href, t = m.group(1), htmllib.unescape(m.group(2)).strip()
            if '2026' in href or 'news' in href.lower() or 'press' in href.lower():
                print('  ', t[:80], '->', href[:110])
        break

print()
print('===== 5. Prudential HK newsroom =====')
u = 'https://www.prudential.com.hk/tc/about-us/newsroom/'
txt = curl(u)
print(f'len={len(txt)}')
if len(txt) > 2000:
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{12,120})', txt):
        href, t = m.group(1), htmllib.unescape(m.group(2)).strip()
        print('  ', t[:80], '->', href[:110])

print()
print('===== 6. AXA HK newsroom =====')
for u in ['https://www.axa.com.hk/zh/news-room/',
          'https://www.axa.com.hk/en/news-room/']:
    txt = curl(u)
    print(f'--- {u} len={len(txt)}')
    if len(txt) > 2000:
        for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{12,120})', txt):
            href, t = m.group(1), htmllib.unescape(m.group(2)).strip()
            if '2026' in href or 'news' in href.lower() or 'press' in href.lower():
                print('  ', t[:80], '->', href[:110])
        break

print()
print('===== 7. SunLife HK newsroom =====')
u = 'https://www.sunlife.com.hk/zh-hant/about-us/newsroom/news-releases/'
txt = curl(u)
print(f'len={len(txt)}')
if len(txt) > 2000:
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{12,120})', txt):
        href, t = m.group(1), htmllib.unescape(m.group(2)).strip()
        print('  ', t[:80], '->', href[:110])

print()
print('===== 8. SCMP insurance topic =====')
u = 'https://www.scmp.com/topics/insurance'
txt = curl(u)
print(f'len={len(txt)}')
if len(txt) > 2000:
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>\s*([^<]{15,120})', txt):
        href, t = m.group(1), htmllib.unescape(m.group(2)).strip()
        if '2026' in href or 'insurance' in href.lower():
            print('  ', t[:85], '->', href[:120])
