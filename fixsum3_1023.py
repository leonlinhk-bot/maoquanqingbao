import json
PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(PATH, encoding='utf-8'))
for it in d['items']:
    if it['id'] == 'artemis-acorn-re-2026-2-450m-20261022':
        it['summary'] = {
          'sc': '汉诺威再本月推出第七只Acorn Re参数式美国地震巨灾债券，目标由2亿美元两度上调至4.5亿，为Oak Tree Assurance等提供保障，定价指引同步下调。',
          'tc': '漢諾威再本月推出第七隻Acorn Re參數式美國地震巨災債券，目標由2億美元兩度上調至4.5億，為Oak Tree Assurance等提供保障，定價指引同步下調。'}
        print(len(it['summary']['sc']), len(it['summary']['tc']))
json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
