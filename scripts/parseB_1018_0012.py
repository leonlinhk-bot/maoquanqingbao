#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os, html

C = '/Users/leonliang/maoquanqingbao/.cache1018_0012'

def strip(s):
    s = re.sub(r'<script.*?</script>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<style.*?</style>', ' ', s, flags=re.S|re.I)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()

MON = {m:i+1 for i,m in enumerate(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])}

def scan(fn, pats, label):
    print('='*20, label, fn)
    raw = open(os.path.join(C, fn), encoding='utf-8', errors='ignore').read()
    # find anchor blocks containing a date-ish string
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', raw, flags=re.S|re.I):
        href, inner = m.group(1), strip(m.group(2))
        if not inner or len(inner) < 12:
            continue
        ctx = raw[m.start():m.start()+900]
        ctxs = strip(ctx)
        if any(p in ctxs for p in pats):
            print('  %s\n     %s\n     ctx: %s' % (inner[:150], href[:160], ctxs[:180]))
            print('  ---')

scan('ia_press.html', ['2026', 'Oct', 'Oct 2026'], 'IA PRESS')
scan('ia_circ.html', ['2026', 'Oct'], 'IA CIRCULAR')
scan('hkma.html', ['2026', 'Oct'], 'HKMA')
scan('hkfi.html', ['2026', 'Oct'], 'HKFI')
scan('govhk.xml', ['2026-10-1', '2026-10-17', '2026-10-18'], 'GOVHK RSS')
