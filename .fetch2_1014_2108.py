#!/usr/bin/env python3
"""Fetch supplementary article pages for fact confirmation."""
import os, re, html, zlib
import urllib.request

PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]
OUT = '/Users/leonliang/maoquanqingbao/data/_1014_2108'

URLS = {
    'art_karenclark': 'https://www.artemis.bm/news/ils-investors-need-to-speak-up-and-ask-for-alternative-model-views-karen-clark/',
    'iaasia_tataaia': 'https://insuranceasia.com/insurance/news/tata-aia-eases-wellness-targets-insurance-rewards',
    'iaasia_sunlife_ph': 'https://insuranceasia.com/insurance/news/philippine-legacy-planning-leaves-82-fearing-wealth-loss',
    'ian_iag_nrma': 'https://insuranceasianews.com/iag-offers-to-trade-nrma-western-australia-renewal-rights-for-raci-deal-approval/',
    'ian_picc_sidecar': 'https://insuranceasianews.com/picc-pc-raises-us12m-from-first-hong-kong-domiciled-sidecar/',
    'hkfi_media': 'https://www.hkfi.org.hk/media-release',
}


def get(url, timeout=30):
    try:
        r = op.open(url, timeout=timeout)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        return raw.decode('utf-8', 'replace')
    except Exception as e:
        return f'__ERR__ {type(e).__name__}: {str(e)[:110]}'


def text(h):
    h = re.sub(r'(?is)<(script|style|noscript).*?</\1>', ' ', h)
    return html.unescape(re.sub(r'\s+', ' ', re.sub('<[^>]+>', ' ', h))).strip()


for k, u in URLS.items():
    t = get(u)
    ok = not t.startswith('__ERR__')
    print(f'\n===== {k}  {"OK" if ok else t} =====')
    if not ok:
        continue
    open(f'{OUT}/{k}.html', 'w', encoding='utf-8').write(t)
    body = text(t)
    print(body[:1600])
