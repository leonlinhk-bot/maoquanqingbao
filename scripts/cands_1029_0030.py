#!/usr/bin/env python3
"""抽取候选文章 URL：Artemis 28 Oct / IBM 新出现 / InsuranceAsia 新出现"""
import os, re, html, json

D = os.path.expanduser('~/maoquanqingbao/.cache1029_0030')


def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()


out = {}

# Artemis: 抓 news 块，取标题+url+日期
t = open(f'{D}/artemis.raw', encoding='utf-8', errors='replace').read()
arts = []
for m in re.finditer(r'<a[^>]+href="(https://www\.artemis\.bm/news/[^"]+)"[^>]*>(.*?)</a>', t, re.S):
    url, tt = m.group(1), clean(m.group(2))
    tail = clean(t[m.end():m.end() + 500])
    dm = re.search(r'(\d{1,2})(?:st|nd|rd|th)? (January|February|March|April|May|June|July|August|September|October|November|December) (\d{4})', tail)
    if len(tt) > 25 and dm and 'artemis.bm/news/' in url:
        arts.append({'title': tt, 'url': url, 'date': ' '.join(dm.groups())})
seen = set()
arts2 = []
for a in arts:
    if a['url'] in seen:
        continue
    seen.add(a['url'])
    arts2.append(a)
out['artemis'] = arts2
print('--- ARTEMIS ---')
for a in arts2[:12]:
    print(' ', a['date'], '|', a['title'][:80])
    print('   ', a['url'])

# IBM: 从列表页抽取 breaking-news 链接
t = open(f'{D}/ibm_asia.raw', encoding='utf-8', errors='replace').read()
ibm = []
for m in re.finditer(r'href="(/asia/news/[a-z\-]+/[a-z0-9\-]+-59\d{4}\.aspx)"[^>]*>(.*?)</a>', t, re.S):
    url, tt = m.group(1), clean(m.group(2))
    if len(tt) > 20:
        ibm.append({'title': tt, 'url': 'https://www.insurancebusinessmag.com' + url})
seen = set(); ibm2 = []
for a in ibm:
    if a['url'] in seen:
        continue
    seen.add(a['url']); ibm2.append(a)
out['ibm'] = ibm2
print('\n--- IBM ---')
for a in ibm2[:12]:
    print(' ', a['title'][:85])
    print('   ', a['url'])

# InsuranceAsia: 列表页标题+URL（无日期，需进详情页）
t = open(f'{D}/insuranceasia.raw', encoding='utf-8', errors='replace').read()
ia = []
for m in re.finditer(r'href="(https://insuranceasia\.com/insurance/[^"]+)"[^>]*>(.*?)</a>', t, re.S):
    url, tt = m.group(1), clean(m.group(2))
    if len(tt) > 20:
        ia.append({'title': tt, 'url': url})
seen = set(); ia2 = []
for a in ia:
    if a['url'] in seen:
        continue
    seen.add(a['url']); ia2.append(a)
out['insuranceasia'] = ia2
print('\n--- INSURANCEASIA ---')
for a in ia2:
    print(' ', a['title'][:85])
    print('   ', a['url'])

json.dump(out, open(f'{D}/candidates.json', 'w'), ensure_ascii=False, indent=1)
print('\nsaved candidates.json')
