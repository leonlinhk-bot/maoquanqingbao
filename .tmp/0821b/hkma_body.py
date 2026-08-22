#!/usr/bin/env python3
import re, html

raw = open('.tmp/0821b/hkma_0821_3.html', encoding='utf-8', errors='ignore').read()
# find main body: after 'Annexes' or after the tender notice paragraph
txt = re.sub(r'<script.*?</script>', ' ', raw, flags=re.S)
txt = re.sub(r'<style.*?</style>', ' ', txt, flags=re.S)
txt = re.sub(r'<[^>]+>', ' ', txt)
txt = html.unescape(re.sub(r'\s+', ' ', txt))
# find last occurrence of 'Renminbi Bills' heading area - the main body
i = txt.rfind('The People\'s Bank of China will issue')
if i < 0:
    i = txt.rfind('Renminbi Bills through')
print(txt[i:i+1600])
