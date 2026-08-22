import re

raw = open('.tmp/iarss.xml', encoding='utf-8', errors='replace').read()
print('len:', len(raw))
print(raw[:1500])
