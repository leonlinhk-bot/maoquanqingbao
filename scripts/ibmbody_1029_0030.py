#!/usr/bin/env python3
"""IBM 正文抽取（跳过导航）"""
import os, re, html

D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030/arts')


def txt(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


for name in ('b1', 'b2', 'b3', 'b4'):
    raw = open(f'{D}/{name}.html', encoding='utf-8', errors='replace').read()
    print('=' * 72)
    print(name)
    # 找 article body 容器
    best = ''
    for pat in [r'<div[^>]+class="[^"]*article__?body[^"]*"[^>]*>(.*?)</div>\s*</div>',
                r'<div[^>]+class="[^"]*article-content[^"]*"[^>]*>(.*?)</div>\s*</div>',
                r'<article[^>]*>(.*?)</article>']:
        m = re.search(pat, raw, re.S | re.I)
        if m:
            t = txt(m.group(1))
            if len(t) > len(best):
                best = t
    if len(best) < 500:
        # 兜底：从标题第二次出现处切
        idx = raw.find('</h1>')
        if idx > 0:
            best = txt(raw[idx:idx + 20000])
    print(best[:2000])
