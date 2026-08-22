#!/usr/bin/env python3
import re, html

def links(path, label, min_len=15):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    print(f'===== {label} ({len(raw)} bytes) =====')
    if 'Just a moment' in raw[:600]:
        print('  [Cloudflare]')
        return
    seen = set()
    n = 0
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, re.S):
        href = m.group(1)
        txt = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        txt = re.sub(r'\s+', ' ', txt)
        if len(txt) < min_len:
            continue
        key = (txt[:60], href[:100])
        if key in seen:
            continue
        seen.add(key)
        ctx = raw[max(0, m.start()-700):m.start()]
        dm = re.findall(r'(20\d{2}[-/.]\d{1,2}[-/.]\d{1,2})', ctx)
        dm2 = re.findall(r'(2026年\d{1,2}月\d{1,2}日)', ctx)
        d = dm[-1] if dm else (dm2[-1] if dm2 else '')
        print(f'  [{d}] {txt[:90]}')
        print(f'      {href[:140]}')
        n += 1
        if n >= 40:
            break

links('.tmp/0821/nfra_list.html', 'NFRA list')
print()
links('.tmp/0821/ia-jp.html', 'IA JP (295KB)')
