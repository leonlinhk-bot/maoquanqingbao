#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch source pages with browser UA into /tmp/src/ for parsing."""
import os, sys, urllib.request, ssl, time

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
os.makedirs('/tmp/src', exist_ok=True)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = {
    'ia_press': 'https://www.ia.org.hk/en/infocenter/press_releases/press_releases.html',
    'ia_speeches': 'https://www.ia.org.hk/en/infocenter/speeches_articles.html',
    'aia': 'https://www.aia.com.hk/en/about-aia/about-us/media-centre/press-releases',
    'manulife': 'https://www.manulife.com.hk/en/individual/about/newsroom.html',
    'prudential': 'https://www.prudential.com.hk/en/about-us/newsroom/',
    'axa': 'https://www.axa.com.hk/en/news-room',
    'sunlife': 'https://www.sunlife.com.hk/en/about-us/newsroom/news-releases/',
    'scmp': 'https://www.scmp.com/topics/insurance',
    'nfra': 'https://www.nfra.gov.cn/cn/view/pages/ItemList.html?itemPId=922&itemId=933',
    'fstb': 'https://www.fstb.gov.hk/en/',
}

for name, url in urls.items():
    out = f'/tmp/src/{name}.html'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept-Language': 'en,zh;q=0.8'})
        with urllib.request.urlopen(req, timeout=30, context=ctx) as r:
            raw = r.read()
        # try utf-8, fall back to gb18030 for Chinese gov sites
        for enc in ('utf-8', 'gb18030'):
            try:
                txt = raw.decode(enc)
                break
            except UnicodeDecodeError:
                continue
        open(out, 'w', encoding='utf-8').write(txt)
        print(f'{name}: {len(txt)} chars OK')
    except Exception as e:
        print(f'{name}: ERROR {e}')
    time.sleep(1)
