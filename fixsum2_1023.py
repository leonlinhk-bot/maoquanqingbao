import json
PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(PATH, encoding='utf-8'))
fix = {
 'scmp-hkma-yue-financial-innovation-20261022': {
   'sc': '金管局总裁余伟文在亚太金融论坛表示，真正的金融创新不是追逐新奇，而是把传统工具转化为高效方案、服务实体经济；他指大湾区要在2060年前碳中和，未来40年需近2万亿美元投资，香港以绿色债券引导资本。',
   'tc': '金管局總裁余偉文在亞太金融論壇表示，真正的金融創新不是追逐新奇，而是把傳統工具轉化為高效方案、服務實體經濟；他指大灣區要在2060年前碳中和，未來40年需近2萬億美元投資，香港以綠色債券引導資本。'},
 'artemis-acorn-re-2026-2-450m-20261022': {
   'sc': '汉诺威再本月推出第七只Acorn Re参数式美国地震巨灾债券，目标由2亿美元先上调75%至3.5亿，最新再提高至4.5亿美元，为Oak Tree Assurance及其他再保安排提供保障，定价指引同步下调。',
   'tc': '漢諾威再本月推出第七隻Acorn Re參數式美國地震巨災債券，目標由2億美元先上調75%至3.5億，最新再提高至4.5億美元，為Oak Tree Assurance及其他再保安排提供保障，定價指引同步下調。'},
}
for it in d['items']:
    if it['id'] in fix:
        it['summary'] = fix[it['id']]
        print(it['id'], len(it['summary']['sc']), len(it['summary']['tc']))
json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
