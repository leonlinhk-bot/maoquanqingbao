# -*- coding: utf-8 -*-
import json
live = json.load(open('data/live-items.json', encoding='utf-8'))['items']
blob = json.dumps(live, ensure_ascii=False).lower()
cands = {
 'SCMP china bans online promos': ['online promos', '网络营销', '網絡營銷', '网络营销管理办法', 'private brokers'],
 'SCMP stocks insurers inflows': ['us$6 trillion', '6万亿美元', '險資', '险资', 'inflows from mainland'],
 'SCMP MPF offshore trusts': ['mpf accounts as offshore', '强积金', '強積金', 'offshore trusts'],
 'SCMP prudential manulife tech alliances': ['tech alliance', '技术合作', 'manulife seal'],
 'Sina 八部门网络营销 0930': ['八部门', '八部門', '金融产品网络营销', '金融產品網絡營銷'],
 'Sina 险资港股通ETF': ['港股通etf', 'qdii额度', 'qdii額度'],
 'Sina 交强险公告2025': ['交强险', '交強險'],
 'Sina 健康险2030': ['健康险改革', '健康保險', '2030年基本形成'],
 '第一财经 港险前三季': ['跨过香江', '跨過香江', '前三季度同比增长近千亿'],
 'IAN IRDAI reform push': ['irdai', 'irdai reform'],
 'IBM allianz names new CEOs partners direct': ['allianz partners', 'allianz direct'],
 'IBM insurance moves allianz aia life aon coface': ['aia life'],
}
for label, ks in cands.items():
    found = [k for k in ks if k in blob]
    print(('FOUND' if found else 'NOT  '), '|', label, '|', found)
