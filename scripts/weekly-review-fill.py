#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""周末复核：补入机构研究(3条) + 更新 meta.generatedAt。"""
import json
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
LIVE = 'data/live-items.json'

data = json.load(open(LIVE, encoding='utf-8'))
items = data['items']
have_ids = {i['id'] for i in items}
have_urls = {i.get('originalUrl', '') for i in items}

new_items = [
    {
        "id": "swissre-sigma-2026-03-time-to-build",
        "clusterCount": 1,
        "score": 80,
        "verifyStatus": "verified",
        "sourceTier": "research",
        "sourceKey": "swissre",
        "title": {
            "sc": "瑞再 sigma 03/2026《Time to build》：AI数据中心与绿电到2030年或催生逾2000亿美元保费",
            "tc": "瑞再 sigma 03/2026《Time to build》：AI數據中心與綠電到2030年或催生逾2000億美元保費"
        },
        "summary": {
            "sc": "瑞再研究院最新 sigma 报告指全球进入资本开支超级周期，AI数据中心与可再生能源项目到2030年累计或产生逾2000亿美元保费，约当全球商业财产险保费的12%；但大型复杂互联项目更难承保，考验保司定价与风险建模能力。",
            "tc": "瑞再研究院最新 sigma 報告指全球進入資本開支超級周期，AI數據中心與可再生能源項目到2030年累計或產生逾2000億美元保費，約當全球商業財產險保費的12%；但大型複雜互聯項目更難承保，考驗保司定價與風險建模能力。"
        },
        "why": {
            "sc": "sigma 首次系统量化「AI基建→商业财险保费」的传导链，是理解科技投资周期如何重塑承保机会的官方口径；前线IFA给客户讲「AI时代保险业机会在哪」时有瑞再一手数据可引。",
            "tc": "sigma 首次系統量化「AI基建→商業財險保費」的傳導鏈，是理解科技投資週期如何重塑承保機會的官方口徑；前線IFA給客戶講「AI時代保險業機會在哪」時有瑞再一手數據可引。"
        },
        "actions": {
            "front": {"sc": "AI基建=承保新增长极", "tc": "AI基建=承保新增長極"},
            "midback": {},
            "lead": {"sc": "承保能力与风险建模的战略议题", "tc": "承保能力與風險建模的戰略議題"},
            "cross": {"sc": "全球承保前沿=跨境视角引用", "tc": "全球承保前沿=跨境視角引用"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 3, "cross": 3},
        "source": {"sc": "Swiss Re Institute sigma 03/2026 · 2026年9月", "lang": "en"},
        "boards": ["insurer"],
        "themes": ["reinsurance", "ai", "capital"],
        "tags": {"sc": ["瑞再", "sigma", "AI基建", "商业财险"], "tc": ["瑞再", "sigma", "AI基建", "商業財險"]},
        "contentKind": "research",
        "publishedAt": "2026-09-01",
        "originalUrl": "https://www.swissre.com/institute/research/sigma-research/sigma-2026-03-time-to-build.html"
    },
    {
        "id": "allianz-sector-atlas-2026",
        "clusterCount": 1,
        "score": 74,
        "verifyStatus": "verified",
        "sourceTier": "research",
        "sourceKey": "allianz",
        "title": {
            "sc": "安联研究《2026行业图谱》：三速经济下全球增速放缓至2.5%，AI投资撑起三成美国增长",
            "tc": "安聯研究《2026行業圖譜》：三速經濟下全球增速放緩至2.5%，AI投資撐起三成美國增長"
        },
        "summary": {
            "sc": "安联研究发布《Sector Atlas 2026》指全球经济增长2026年将放缓至+2.5%、2027年回升至+2.9%，AI投资单独贡献美国增长约三分之一；宏观承压但仍具韧性，是险资配置与寿险销售环境的重要背景。",
            "tc": "安聯研究發布《Sector Atlas 2026》指全球經濟增長2026年將放緩至+2.5%、2027年回升至+2.9%，AI投資單獨貢獻美國增長約三分之一；宏觀承壓但仍具韌性，是險資配置與壽險銷售環境的重要背景。"
        },
        "why": {
            "sc": "机构层面对2026下半年宏观的最新定调：增长降速但AI投资是核心引擎。对IFA理解客户资产配置情绪、把握「低增长环境下保险的防御价值」话题有直接参考。",
            "tc": "機構層面對2026下半年宏觀的最新定調：增長降速但AI投資是核心引擎。對IFA理解客戶資產配置情緒、把握「低增長環境下保險的防禦價值」話題有直接參考。"
        },
        "actions": {
            "front": {"sc": "低增长环境下保险的防御叙事", "tc": "低增長環境下保險的防禦敘事"},
            "midback": {},
            "lead": {},
            "cross": {"sc": "全球宏观=跨境配置背景", "tc": "全球宏觀=跨境配置背景"}
        },
        "rolesImpact": {"front": 2, "midback": 1, "lead": 2, "cross": 3},
        "source": {"sc": "Allianz Research · 2026年9月7日", "lang": "en"},
        "boards": ["market"],
        "themes": ["macro", "international"],
        "tags": {"sc": ["安联", "宏观", "行业图谱"], "tc": ["安聯", "宏觀", "行業圖譜"]},
        "contentKind": "research",
        "publishedAt": "2026-09-07",
        "originalUrl": "https://www.allianz.com/en/economic_research/insights/publications/specials_fmo/260907-sector-atlas-2026.html"
    },
    {
        "id": "allianz-ai-tech-debt-20260910",
        "clusterCount": 1,
        "score": 74,
        "verifyStatus": "verified",
        "sourceTier": "research",
        "sourceKey": "allianz",
        "title": {
            "sc": "安联研究：科技债「水面下的(AI)冰山」——AI资本开支信用风险补偿严重不足",
            "tc": "安聯研究：科技債「水面下的(AI)冰山」——AI資本開支信用風險補償嚴重不足"
        },
        "summary": {
            "sc": "安联研究指出，股权独享AI建设上行收益、信用端承担下行风险，但5年期科技债票息不足1%、10年期约2%，风险补偿严重不足；八大美国科技公司长期债务12个月内上升86%。对持有大量投资级信用敞口的险资构成警示。",
            "tc": "安聯研究指出，股權獨享AI建設上行收益、信用端承擔下行風險，但5年期科技債票息不足1%、10年期約2%，風險補償嚴重不足；八大美國科技公司長期債務12個月內上升86%。對持有大量投資級信用敞口的險資構成警示。"
        },
        "why": {
            "sc": "险资是投资级信用债的核心持有者，AI资本开支带来的信用集中度与息差收窄，直接影响保险公司资产端回报与久期管理；中后台与资管岗位理解这一风险传导链条有实际价值。",
            "tc": "險資是投資級信用債的核心持有者，AI資本開支帶來的信用集中度與息差收窄，直接影響保險公司資產端回報與久期管理；中後台與資管崗位理解這一風險傳導鏈條有實際價值。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "信用集中度=资产端风险点", "tc": "信用集中度=資產端風險點"},
            "lead": {},
            "cross": {"sc": "全球信用=跨境配置参考", "tc": "全球信用=跨境配置參考"}
        },
        "rolesImpact": {"front": 1, "midback": 3, "lead": 2, "cross": 2},
        "source": {"sc": "Allianz Research · 2026年9月10日", "lang": "en"},
        "boards": ["market"],
        "themes": ["macro", "ai", "capital"],
        "tags": {"sc": ["安联", "信用风险", "AI"], "tc": ["安聯", "信用風險", "AI"]},
        "contentKind": "research",
        "publishedAt": "2026-09-10",
        "originalUrl": "https://www.allianz.com/en/economic_research/insights/publications/specials_fmo/260910-AI-Capital-Markets.html"
    }
]

added = 0
for it in new_items:
    if it['id'] in have_ids or it['originalUrl'] in have_urls:
        print('跳过重复:', it['id'])
        continue
    items.append(it)
    added += 1

print('新增条目:', added)

# 更新 meta.generatedAt
data['meta']['generatedAt'] = datetime.now(CST).isoformat()
data['meta']['itemCount'] = len(items)
data['meta']['windowNote'] = {'sc': f'本库{len(items)}条。', 'tc': f'本庫{len(items)}條。'}

json.dump(data, open(LIVE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('总条数:', len(items))
