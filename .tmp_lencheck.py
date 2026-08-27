import re
src = open('.tmp_ingest_0826.py').read()
# crude: extract all "s_sc"/"s_tc" string literals from mk() calls
pairs = re.findall(r'mk\([^)]*?"sc":\s*"((?:[^"\\]|\\.)*)",\s*\n?\s*"tc":\s*"((?:[^"\\]|\\.)*)"', src)
for i, (s, t) in enumerate(pairs):
    if len(s) > 100 or len(t) > 100:
        print(f'item idx {i}: sc={len(s)} tc={len(t)}')
print('checked', len(pairs), 'summary pairs')
