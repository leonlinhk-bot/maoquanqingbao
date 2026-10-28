import os, re, html, json
D = '.cache1028_1010'

def clean(s):
    s = re.sub(r'<[^>]+>', '', s or '')
    return re.sub(r'\s+', ' ', html.unescape(s)).strip()

# ---- govhk zh: inspect one item
t = open(f'{D}/govhk_zh.raw', encoding='utf-8', errors='replace').read()
items = re.findall(r'<item[ >].*?</item>', t, re.S)
print('govhk_zh items', len(items))
print('--- sample item ---')
print(items[0][:700])
print('--- titles via CDATA ---')
KW = ['保险', '保險', '保監', '金融', '財經', '強積金', '年金', '退休', '證監', '金管局', '家族辦公室', '資產管理', '跨境', '人民幣', '銀髮', '跨境通']
rows = []
for it in items:
    m = re.search(r'<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>', it, re.S)
    title = clean(m.group(1)) if m else ''
    lm = re.search(r'<link>(.*?)</link>', it, re.S)
    link = clean(lm.group(1)) if lm else ''
    dm = re.search(r'<pubDate>(.*?)</pubDate>', it, re.S)
    d = clean(dm.group(1)) if dm else ''
    rows.append((title, link, d))
hit = [r for r in rows if any(k in r[0] for k in KW)]
print('kw hits', len(hit))
for r in hit[:25]:
    print(' ', r[2][:25], '|', r[0][:70], '|', r[1])
print()
print('--- newest 12 govhk zh titles ---')
for r in rows[:12]:
    print(' ', r[2][:25], '|', r[0][:75])
