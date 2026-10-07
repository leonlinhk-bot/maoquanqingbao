p='data/live-items.json'
raw=open(p,encoding='utf-8').read()
i=raw.index('\n')
print(repr(raw[:120]))
print('second line:', repr(raw[i+1:i+40]))
print('size', len(raw))
