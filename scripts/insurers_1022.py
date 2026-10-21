import re, html, json
from pathlib import Path
D = Path('/Users/leonliang/maoquanqingbao/data/_1022_0037')

for f in ['aia.html', 'pru.html', 'axa.html', 'sun.html', 'hkfi.html']:
    p = D / f
    txt = p.read_text(encoding='utf-8', errors='ignore')
    print(f'\n===== {f} ({len(txt)} chars) =====')
    # find anchors with text length > 15 and nearby date-like strings
    anchors = re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', txt, re.S)
    hits = 0
    for href, label in anchors:
        lab = html.unescape(re.sub(r'<[^>]+>', ' ', label))
        lab = re.sub(r'\s+', ' ', lab).strip()
        if len(lab) < 18:
            continue
        if re.search(r'(2026|2025)', lab) or any(k in lab for k in ['保險', '保险', '保單', '宣佈', '宣布', '推出', 'appoint', 'launch', 'announc']):
            print(f'  {lab[:110]}  ->  {href[:110]}')
            hits += 1
            if hits > 18:
                break
    # date tokens
    ds = re.findall(r'(20\d\d[-/年]\d{1,2}[-/月]\d{1,2})', txt)
    print('  date tokens:', ds[:12])
