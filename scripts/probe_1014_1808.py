#!/usr/bin/env python3
import urllib.request, zlib, sys
PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]
urls = [
 'https://www.bing.com/news/search?q=%E4%BF%9D%E9%9A%AA&format=RSS',
 'https://www.bing.com/search?q=hong+kong+insurance&format=rss',
 'https://duckduckgo.com/html/?q=hong+kong+insurance+news',
 'https://news.google.com/rss/search?q=hong+kong+insurance&hl=en-US&gl=US&ceid=US:en',
 'https://www.hk01.com/feed',
 'https://www.etnet.com.hk/www/tc/news/home_editor_choice.php',
 'https://www.aastocks.com/tc/stocks/news/aafn-news',
 'https://www.hkfi.org.hk/zh/media-release',
 'https://www.ia.org.hk/en/infocenter/press_releases.html',
]
for u in urls:
    try:
        r = op.open(u, timeout=20)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        print(f'OK {len(raw):>8} {r.status} {u}')
        open('data/_1014/probe_' + str(abs(hash(u)) % 100000) + '.raw', 'wb').write(raw)
    except Exception as e:
        print(f'ERR {type(e).__name__}: {str(e)[:70]} {u}')
