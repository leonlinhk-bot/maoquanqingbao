import json

PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(PATH, encoding='utf-8'))

fix = {
 'ibm-osaka-broker-vendor-cyber-20261022': {
   'sc': '日本大阪IwaiCosmo披露，外包服务商系统被入侵，七个账户出现虚假买卖指令、五个账户实际成交，公司已冲销交易，并泄漏4975名客户资料。争点是供应商网络被攻破时，网络责任落在哪一方。',
   'tc': '日本大阪IwaiCosmo披露，外包服務商系統被入侵，七個賬戶出現虛假買賣指令、五個賬戶實際成交，公司已沖銷交易，並洩漏4975名客戶資料。爭點是供應商網絡被攻破時，網絡責任落在哪一方。'},
 'ibm-pvi-vietnam-reinsurance-expansion-20261022': {
   'sc': '越南最大非寿险公司PVI Insurance 10月20日在曼谷与泰京银行签合作备忘录，并与Muang Thai商讨合作；公司同时寻求在中亚、南高加索与中东承接再保业务，聚焦工业与能源大型项目。',
   'tc': '越南最大非壽險公司PVI Insurance 10月20日在曼谷與泰京銀行簽合作備忘錄，並與Muang Thai商討合作；公司同時尋求在中亞、南高加索與中東承接再保業務，聚焦工業與能源大型項目。'},
 'iaasia-global-market-19-8t-2035-20261022': {
   'sc': 'Maximise Market Research估算，全球保险市场由2025年9.5万亿美元增至2035年19.8万亿，年复合增长7.6%；亚太区增量保费最高，动力来自渗透率提升、经济增长与监管变化。',
   'tc': 'Maximise Market Research估算，全球保險市場由2025年9.5萬億美元增至2035年19.8萬億，年複合增長7.6%；亞太區增量保費最高，動力來自滲透率提升、經濟增長與監管變化。'},
}

for it in d['items']:
    if it['id'] in fix:
        it['summary'] = fix[it['id']]
        print(it['id'], len(it['summary']['sc']), len(it['summary']['tc']))

json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 全库新条目长度复核
bad = []
for it in d['items'][:11]:
    for k in ('sc', 'tc'):
        n = len(it['summary'][k])
        if not (50 <= n <= 100):
            bad.append((it['id'], k, n))
print('out-of-range:', bad)
print('total', len(d['items']))
