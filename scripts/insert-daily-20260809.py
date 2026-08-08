#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-09) into live-items.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
INGESTED = "2026-08-09T18:08:00+08:00"

def item(id_, score, verify, tier, key, title_sc, title_tc, sum_sc, sum_tc,
         why_sc, why_tc, actions, roles, src_sc, lang, boards, themes,
         tags_sc, tags_tc, kind, published, url):
    return {
        "id": id_, "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": key,
        "title": {"sc": title_sc, "tc": title_tc},
        "summary": {"sc": sum_sc, "tc": sum_tc},
        "why": {"sc": why_sc, "tc": why_tc},
        "actions": actions, "rolesImpact": roles,
        "source": {"sc": src_sc, "lang": lang},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags_sc, "tc": tags_tc},
        "contentKind": kind, "publishedAt": published, "originalUrl": url,
        "ingestedAt": INGESTED,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False, "evergreen": False,
    }

new_items = [
    item(
        "ib-sk-ai-datacenter-20260808", 60, "verified", "media",
        "insurancebusinessmag:sk-ai-datacenter-20260808",
        "韩国拟建18.4GW AI数据中心 险企承保能力与定价承压",
        "韓國擬建18.4GW AI數據中心 險企承保能力與定價受壓",
        "韩国规划2035年前建成18.4GW AI数据中心容量、总投资逾千万亿韩元，三星火灾海上等险企正与外部专家制定承保指引；瑞再预计全球数据中心保费2030年将达242亿美元，火灾占损失成本42%而承保能力或不足，Aon已将数据中心计划容量提至50亿美元。[EN原文]",
        "韓國規劃2035年前建成18.4GW AI數據中心容量、總投資逾千萬億韓元，三星火災海上等險企正與外部專家制定承保指引；瑞再預計全球數據中心保費2030年將達242億美元，火災佔損失成本42%而承保能力或不足，Aon已將數據中心計劃容量提至50億美元。[EN原文]",
        "数据中心险成为亚太商险增长极，但承保经验缺乏+容量缺口将传导至经纪排分与客户融资结构，对香港商业险/再保险业务布局有直接参考意义。",
        "數據中心險成為亞太商險增長極，但承保經驗缺乏+容量缺口將傳導至經紀排分與客戶融資結構，對香港商業險/再保險業務佈局有直接參考意義。",
        {"front": {}, "midback": {}, "lead": {"sc": "数据中心容量缺口=排分与融资新变量", "tc": "數據中心容量缺口=排分與融資新變量"}, "cross": {}},
        {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "Insurance Business", "en", ["tech", "market"], ["datacenter", "underwriting"],
        ["AI数据中心", "承保能力", "韩国", "商险"],
        ["AI數據中心", "承保能力", "韓國", "商險"],
        "news", "2026-08-08T12:01:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/technology/south-korea-is-building-18-4-gw-of-ai-data-centre-capacity--its-insurers-dont-yet-know-how-to-price-585433.aspx",
    ),
    item(
        "ib-sk-nonclaim-clinics-20260808", 60, "verified", "media",
        "insurancebusinessmag:sk-nonclaim-clinics-20260808",
        "韩国「零理赔」诊所两年增25% 医责险核保数据盲区扩大",
        "韓國「零理賠」診所兩年增25% 醫責險核保數據盲區擴大",
        "韩国未申报医保理赔的医疗机构由2021年1810家增至2025年2272家（+25.5%），集中于首尔江南等美容医疗区；经纪与核保人难以再依赖理赔记录评估医责险风险，需转向索取手术量、治疗组合与医师资质等直接信息，外国患者市场扩大令该问题更突出。[EN原文]",
        "韓國未申報醫保理賠的醫療機構由2021年1810家增至2025年2272家（+25.5%），集中於首爾江南等美容醫療區；經紀與核保人難以再依賴理賠記錄評估醫責險風險，需轉向索取手術量、治療組合與醫師資質等直接信息，外國患者市場擴大令該問題更突出。[EN原文]",
        "理赔历史失效后的替代核保路径（直接索取诊所运营数据）对香港医疗/责任险中介有方法论参考价值，医责险数据盲区是亚太健康险共同痛点。",
        "理賠歷史失效後的替代核保路徑（直接索取診所營運數據）對香港醫療/責任險中介有方法論參考價值，醫責險數據盲區是亞太健康險共同痛點。",
        {"front": {}, "midback": {}, "lead": {"sc": "零理赔诊所=核保数据盲区新案例", "tc": "零理賠診所=核保數據盲區新案例"}, "cross": {}},
        {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "Insurance Business", "en", ["tech", "insurer"], ["underwriting", "health"],
        ["医责险", "核保", "韩国", "健康险"],
        ["醫責險", "核保", "韓國", "健康險"],
        "news", "2026-08-08T11:58:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/life-insurance/south-koreas-nonclaiming-clinics-raise-underwriting-questions-585432.aspx",
    ),
    item(
        "ib-dando-rates-20260808", 60, "verified", "media",
        "insurancebusinessmag:dando-rates-20260808",
        "D&O费率2025年跌6.8%后现「见底」迹象 续保策略转向扩保障",
        "D&O費率2025年跌6.8%後現「見底」跡象 續保策略轉向擴保障",
        "Howden数据显示全球D&O费率2025年平均下跌6.8%，末两季持平续保增多、市场现见底迹象；Aon与Marsh均录得美区D&O价格环比回升。仅11.5%客户调整限额，经纪窗口期或转向以竞争换更广理赔定义与Side A DIC限额，亚洲超额层费率连三季跌逾20%。[EN原文]",
        "Howden數據顯示全球D&O費率2025年平均下跌6.8%，末兩季持平續保增多、市場現見底跡象；Aon與Marsh均錄得美區D&O價格環比回升。僅11.5%客戶調整限額，經紀窗口期或轉向以競爭換更廣理賠定義與Side A DIC限額，亞洲超額層費率連三季跌逾20%。[EN原文]",
        "董责险费率周期拐点将至，「降价叙事」转向「扩保障叙事」，直接关系到经纪续保策略与客户沟通话术，对香港上市公司及跨境客户董责安排有参考价值。",
        "董責險費率週期拐點將至，「降價敘事」轉向「擴保障敘事」，直接關係到經紀續保策略與客戶溝通話術，對香港上市公司及跨境客戶董責安排有參考價值。",
        {"front": {}, "midback": {}, "lead": {"sc": "费率见底=续保谈扩保障的窗口", "tc": "費率見底=續保談擴保障的窗口"}, "cross": {}},
        {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "Insurance Business", "en", ["market", "reg"], ["dando", "pricing"],
        ["董责险", "费率", "续保", "市场趋势"],
        ["董責險", "費率", "續保", "市場趨勢"],
        "news", "2026-08-08T11:55:00+08:00",
        "https://www.insurancebusinessmag.com/asia/news/professional-liability/dando-rates-fall-6-8-but-show-signs-of-bottoming-out-585431.aspx",
    ),
]

data = json.loads(LIVE.read_text(encoding='utf-8'))
existing_keys = {it.get('sourceKey') for it in data['items']}
added = []
for it in new_items:
    if it['sourceKey'] in existing_keys:
        print(f"SKIP duplicate: {it['sourceKey']}")
        continue
    added.append(it)
    existing_keys.add(it['sourceKey'])

data['items'] = added + data['items']
data['meta']['generatedAt'] = INGESTED
data['meta']['itemCount'] = len(data['items'])
LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print(f"Inserted {len(added)} items. Total: {len(data['items'])}")
