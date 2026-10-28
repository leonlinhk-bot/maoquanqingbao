#!/usr/bin/env python3
"""抽取候选文章日期 + 正文前段。"""
import os, re, html

D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030/arts')


def txt(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S | re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


for name, label in [('a1', 'Artemis: RenRe CEO O\'Donnell ILS'), ('a2', 'Artemis: Aon CEO Case risk/capital'),
                    ('a3', 'Artemis: VIG Re Charles Bridge Re'), ('a4', 'Artemis: Morocco securitization'),
                    ('a5', 'Artemis: Lockton Re chairman Bermuda'),
                    ('b1', 'IBM: Aon debt USI'), ('b2', 'IBM: Arch primary'),
                    ('b3', 'IBM: Mining soft market'), ('b4', 'IBM: IUMI marine'),
                    ('c1', 'IA: Challenger/Daiichi'), ('c5', 'IA: Allianz Partners students'),
                    ('c6', 'IA: Igloo')]:
    p = f'{D}/{name}.html'
    if not os.path.exists(p):
        print(name, 'MISSING'); continue
    raw = open(p, encoding='utf-8', errors='replace').read()
    print('=' * 72)
    print(name, label)
    # 日期候选
    dates = re.findall(r'(?:datetime="|"datePublished"\s*:\s*"|>)(20\d\d-\d\d-\d\dT?[\d:+\-]*Z?)', raw)
    print('  dates:', list(dict.fromkeys(dates))[:6])
    for pat in (r'(\d{1,2}(?:st|nd|rd|th)? (?:January|February|March|April|May|June|July|August|September|October|November|December) 20\d\d)',
                r'((?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, 20\d\d)'):
        d2 = re.findall(pat, raw)
        if d2:
            print('  human dates:', list(dict.fromkeys(d2))[:4])
    # 正文
    body = ''
    m = re.search(r'<article[^>]*>(.*?)</article>', raw, re.S)
    if m:
        body = txt(m.group(1))
    if len(body) < 400:
        body = txt(raw)
    print('  BODY:', body[:1400])
