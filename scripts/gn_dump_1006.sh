#!/bin/bash
cd /Users/leonliang/maoquanqingbao
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124.0 Safari/537.36"
# try resolving a google news rss article link
URL=$(python3 - <<'PY'
import re
t=open('data/_raw_1006_2343/gn_hk_fo.xml',encoding='utf-8',errors='ignore').read()
ents=re.findall(r'<item[\s>].*?</item>', t, re.S)
for e in ents[:6]:
    ti=re.search(r'<title>(.*?)</title>', e, re.S)
    ln=re.search(r'<link>(.*?)</link>', e, re.S)
    print(ti.group(1)[:60], '|||', ln.group(1))
PY
)
echo "$URL"
