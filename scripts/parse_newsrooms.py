#!/usr/bin/env python3
"""Parse downloaded newsroom HTML files: extract anchors with nearby dates."""
import re, html, sys, os, glob
from datetime import datetime

def clean(s):
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

def parse_file(path):
    raw = open(path, encoding='utf-8', errors='replace').read()
    # strip scripts/styles
    raw = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    raw = re.sub(r'<style.*?</style>', ' ', raw, flags=re.S)
    # find blocks: anchor with href + nearby date text
    pat = re.compile(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', re.S)
    out = []
    for m in pat.finditer(raw):
        href, inner = m.group(1), clean(m.group(2))
        if not inner or len(inner) < 12:
            continue
        if any(x in href.lower() for x in ('.css', '.js', '.png', '.jpg', '.ico', 'javascript', '#', 'mailto')):
            continue
        # date near anchor: look at 600 chars before
        start = max(0, m.start() - 500)
        ctx = raw[start:m.start()]
        dates = re.findall(r'(20\d\d)[-/年.](\d{1,2})[-/月.](\d{1,2})', ctx)
        dstr = ''
        if dates:
            y, mo, d = dates[-1]
            dstr = f'{y}-{int(mo):02d}-{int(d):02d}'
        out.append((dstr, inner[:120], href[:130]))
    return out

if __name__ == '__main__':
    files = sys.argv[1:] or sorted(glob.glob('/tmp/probe_*.html'))
    for f in files:
        print(f'\n===== {os.path.basename(f)} =====')
        try:
            rows = parse_file(f)
        except Exception as e:
            print('parse error:', e)
            continue
        print('anchors:', len(rows))
        for d, t, h in rows[:25]:
            print(f'- [{d}] {t} | {h}')
