#!/usr/bin/env python3
import re, html

def extract(path, needle, span=3500):
    raw = open(path, encoding='utf-8', errors='ignore').read()
    # strip tags but keep text
    txt = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
    txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
    txt = re.sub(r'<[^>]+>', ' ', txt)
    txt = html.unescape(re.sub(r'\s+', ' ', txt))
    i = txt.rfind(needle)
    if i < 0:
        i = txt.find(needle)
    return txt[max(0, i-200):i+span]

print('===== HKMA 0821-3 (PBOC RMB Bills) =====')
print(extract('.tmp/0821b/hkma_0821_3.html', 'will issue Renminbi Bills', 2600))
print()
print('===== HKMA 0820-4 (Scam alert banks) =====')
print(extract('.tmp/0821b/hkma_0820_4.html', 'fraudulent websites', 2200))
