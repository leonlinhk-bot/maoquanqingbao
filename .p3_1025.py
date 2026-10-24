import os, json, re
base = '/Users/leonliang/maoquanqingbao/data/_raw_1025_0044/'
for f in sorted(os.listdir(base)):
    p = base + f
    print('='*24, f, os.path.getsize(p))
    txt = open(p, encoding='utf-8', errors='replace').read()
    print(txt[:600].replace('\n', ' | '))
    print()
