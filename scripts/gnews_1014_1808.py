#!/usr/bin/env python3
"""Google News RSS sweep via local proxy; filter to items published after last check."""
import re, html, zlib, json, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
CUT = datetime(2026, 10, 14, 2, 11, tzinfo=HKT)
PROXY = 'http://127.0.0.1:17891'
op = urllib.request.build_opener(urllib.request.ProxyHandler({'http': PROXY, 'https': PROXY}))
op.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36')]


def get(url):
    try:
        r = op.open(url, timeout=30)
        raw = r.read()
        if r.headers.get('Content-Encoding') == 'gzip':
            raw = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
        return raw.decode('utf-8', 'replace')
    except Exception as e:
        return f'__ERR__ {type(e).__name__}: {str(e)[:110]}'


def strip(t):
    t = re.sub(r'<!\[CDATA\[(.*?)\]\]>', r'\1', t or '', flags=re.S)
    return html.unescape(re.sub(r'<[^>]+>', ' ', t)).strip()


QUERIES = {
    'hk_regulator': '保監局 OR 保險業監管局 OR "Insurance Authority"',
    'hk_insurance': '香港 保險 業 監管',
    'hk_insurers': '友邦 OR 保誠 OR 宏利 OR 安盛 OR 永明 香港',
    'family_office': '香港 家族辦公室',
    'hk_ils': '香港 巨災債券 OR 保險相連證券',
    'insurtech': '香港 保險科技 OR 人工智能 保險',
    'mpf': '強積金 積金局',
    'cross_border': '跨境 保險 大灣區',
}
for k, q in QUERIES.items():
    url = 'https://news.google.com/rss/search?q=' + urllib.parse.quote(q) + '&hl=zh-HK&gl=HK&ceid=HK:zh-Hant'
    raw = get(url)
    if raw.startswith('__ERR__'):
        print(f'\n### {k}: {raw}')
        continue
    rows = []
    for blk in re.findall(r'<item\b.*?</item>', raw, re.S):
        def g(t):
            m = re.search(rf'<{t}[^>]*>(.*?)</{t}>', blk, re.S)
            return m.group(1) if m else ''
        try:
            dt = datetime.strptime(strip(g('pubDate')), '%a, %d %b %Y %H:%M:%S %Z').replace(tzinfo=timezone.utc).astimezone(HKT)
        except Exception:
            continue
        if dt > CUT:
            rows.append((dt, strip(g('title')), strip(g('link')), strip(g('source'))))
    print(f'\n### {k}: {len(rows)} new')
    for dt, t, l, s in sorted(rows):
        print(f'- {dt:%m-%d %H:%M} | {t[:100]} | {s}')
