#!/usr/bin/env python3
import re, html

def body_text(path):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    body = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    body = html.unescape(re.sub(r'\s+', ' ', body))
    return body

def find_main(b, markers):
    # search for marker positions, pick the last occurrence region (main content usually after nav)
    pos = -1
    for m in markers:
        p = b.rfind(m)
        if p > pos:
            pos = p
    return pos

for f, label, markers in [
    ('.tmp/0821b/hkma_0821_3.html', 'HKMA 0821-3 PBOC RMB BILLS', ['The People\'s Bank of China will issue', 'Press Releases']),
    ('.tmp/0821b/hkma_0820_4.html', 'HKMA 0820-4 SCAM ALERT', ['Scam alert related to banks', 'banks'])]:
    b = body_text(f)
    print('=' * 90)
    print(label)
    # find last occurrence of title-ish text
    i = b.rfind(markers[0])
    if i < 0:
        i = b.find(markers[0])
    seg = b[i:i+1500]
    print(seg)
    print()
