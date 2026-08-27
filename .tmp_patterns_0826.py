import json, re, urllib.request, html as htmllib

d = json.load(open('data/live-items.json'))
items = d['items']

print('--- nfra URL patterns (last 6) ---')
n = 0
for it in reversed(items):
    if it.get('sourceKey') == 'nfra':
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['originalUrl'][:150])
        n += 1
        if n >= 6:
            break

print('--- manulife URL patterns (last 5) ---')
n = 0
for it in reversed(items):
    if it.get('sourceKey') == 'manulife':
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['originalUrl'][:150])
        n += 1
        if n >= 5:
            break

print('--- axa URL patterns (last 5) ---')
n = 0
for it in reversed(items):
    if it.get('sourceKey') == 'axa':
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['originalUrl'][:150])
        n += 1
        if n >= 5:
            break

print('--- sunlife URL patterns (last 5) ---')
n = 0
for it in reversed(items):
    if it.get('sourceKey') == 'sunlife':
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['originalUrl'][:150])
        n += 1
        if n >= 5:
            break

print('--- prudential URL patterns (last 5) ---')
n = 0
for it in reversed(items):
    if it.get('sourceKey') == 'prudential':
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['originalUrl'][:150])
        n += 1
        if n >= 5:
            break

print('--- ia URL patterns (last 6) ---')
n = 0
for it in reversed(items):
    if it.get('sourceKey') == 'ia':
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['originalUrl'][:150])
        n += 1
        if n >= 6:
            break

print('--- scmp URL patterns (last 4) ---')
n = 0
for it in reversed(items):
    if it.get('sourceKey') == 'scmp':
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['originalUrl'][:150])
        n += 1
        if n >= 4:
            break

print('--- insurtech-related ids (sourceKey contains tech/insur) ---')
for it in items:
    if 'insurtech' in it.get('sourceKey', '') or 'tech' in it.get('sourceKey', ''):
        print(' ', it['id'], '|', it.get('publishedAt'), '|', it['originalUrl'][:130])
