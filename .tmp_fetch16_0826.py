#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, html as htmllib, subprocess

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126"

def curl(url, timeout=25):
    return subprocess.run(["curl", "-sL", "--compressed", "--max-time", str(timeout), "-A", UA, url],
                          capture_output=True, text=True).stdout

feeds = [
    ('hkbt', 'https://www.hkbt.com.hk/feed/'),
    ('oncc-finance', 'https://hk.on.cc/rss/finance.xml'),
    ('oncc-realtime', 'https://hk.on.cc/rss/realtime.xml'),
    ('stheadline-fin', 'https://www.stheadline.com/rss/realtime-finance.xml'),
    ('hket', 'https://www.hket.com/rss/'),
    ('hkej', 'https://www1.hkej.com/rss/index.xml'),
    ('hkcd', 'http://www.hkcd.com/rss/hkcd_rss.xml'),
]
for tag, u in feeds:
    txt = curl(u)
    print(f'===== {tag}: {u} len={len(txt)}')
    if len(txt) < 200:
        print('   (empty/blocked)')
        continue
    items = re.findall(r'<item>(.*?)</item>', txt, re.S)
    print(f'   items: {len(items)}')
    for it in items[:10]:
        t = re.search(r'<title>(.*?)</title>', it, re.S)
        l = re.search(r'<link>(.*?)</link>', it, re.S)
        p = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
        title = htmllib.unescape(t.group(1)).strip() if t else '?'
        link = htmllib.unescape(l.group(1)).strip() if l else '?'
        mark = ''
        if any(k in title for k in ['太平', '家辦', '家办', '家族', '巴克', '離岸', '离岸', '保險', '保险', 'SFi', '影響力']):
            mark = ' <<<'
        print(f'   [{p.group(1).strip() if p else "?"}] {title[:80]}{mark}')
        print(f'       {link[:140]}')
