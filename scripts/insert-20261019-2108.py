# -*- coding: utf-8 -*-
"""2026-10-19 21:08 增量：Artemis 三条（Raphaela 巨灾损失 / E+S Rück 巴登巴登续保 / Q4 巨灾债券发起人）"""
import json

PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
NOW = '2026-10-19T21:15:00+08:00'

d = json.load(open(PATH, encoding='utf-8'))
items = d['items']
existing = {i.get('originalUrl', '').split('?')[0].rstrip('/') for i in items}

new_items = [
    {
        "id": "artemis-raphaela-euro-scs-loss-20261019",
        "publishedAt": "2026-10-19T15:30:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/late-august-euro-scs-and-hail-event-raphaela-estimated-near-eur-3-3bn-industry-loss-perils/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 73,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["catastrophe", "reinsurance", "climate", "pricing"],
        "title": {
            "sc": "PERILS：8 月西欧强对流「Raphaela」致保险业损失约 32.96 亿欧元",
            "tc": "PERILS：8 月西歐強對流「Raphaela」致保險業損失約 32.96 億歐元"
        },
        "summary": {
            "sc": "巨灾数据机构 PERILS 初步估计，8 月 26 至 28 日横扫法国、德国、瑞士及意大利的强对流与冰雹事件「Raphaela」，造成保险业损失约 32.96 亿欧元，来自财产险与车险。冰雹直径普遍 4 至 8 厘米，意大利北部录得最大 13 厘米；瑞士受灾带由日内瓦湖延伸至博登湖，被视为当地史上最大巨灾损失事件之一，事件无风暴相关死亡报告。",
            "tc": "巨災數據機構 PERILS 初步估計，8 月 26 至 28 日橫掃法國、德國、瑞士及意大利的強對流與冰雹事件「Raphaela」，造成保險業損失約 32.96 億歐元，來自財產險與車險。冰雹直徑普遍 4 至 8 厘米，意大利北部錄得最大 13 厘米；瑞士受災帶由日內瓦湖延伸至博登湖，被視為當地史上最大巨災損失事件之一，事件無風暴相關死亡報告。"
        },
        "why": {
            "sc": "欧洲冰雹损失连年走高，是再保定价与巨灾条款收紧的直接推手；向客户解释「为何高端家居/财产保障条款变严」时，可用具体损失量级作背景，而非泛泛讲气候风险。",
            "tc": "歐洲冰雹損失連年走高，是再保定價與巨災條款收緊的直接推手；向客户解釋「為何高端家居／財產保障條款變嚴」時，可用具體損失量級作背景，而非泛泛講氣候風險。"
        },
        "source": {
            "sc": "Artemis 2026-10-19（引 PERILS AG 初步估计）",
            "tc": "Artemis 2026-10-19（引 PERILS AG 初步估計）",
            "lang": "en",
            "name": "artemis",
            "date": "2026-10-19"
        },
        "tags": {
            "sc": ["巨灾", "冰雹", "欧洲", "再保险", "PERILS"],
            "tc": ["巨災", "冰雹", "歐洲", "再保險", "PERILS"]
        },
        "actions": {
            "front": {"sc": "客户沟通：财产保障条款收紧的行业背景", "tc": "客户溝通：財產保障條款收緊的行業背景"},
            "midback": {"sc": "核保与再保成本趋势跟踪", "tc": "核保與再保成本趨勢跟蹤"},
            "lead": {"sc": "团队简报：气候巨灾与费率", "tc": "團隊簡報：氣候巨災與費率"},
            "cross": {"sc": "高净值客户财产风险盘点素材", "tc": "高淨值客户財產風險盤點素材"}
        },
        "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "artemis-hannover-es-ruck-baden-baden-20261019",
        "publishedAt": "2026-10-19T15:00:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/hannover-res-es-ruck-sees-more-intense-catastrophe-risk-competition-ils-options-for-clients/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 71,
        "verifyStatus": "verified",
        "contentKind": "news",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["reinsurance", "pricing", "ils", "capacity"],
        "title": {
            "sc": "汉诺威再保险 E+S Rück：再保容量上升加剧竞争　以纪律承保守住价格",
            "tc": "漢諾威再保險 E+S Rück：再保容量上升加劇競爭　以紀律承保守住價格"
        },
        "summary": {
            "sc": "汉诺威再保险德国子公司 E+S Rück 在巴登巴登再保会议期间表示，德国再保需求仍强、整体环境稳定，但传统再保资本增加令价格与条款竞争明显加剧。行政总裁 Steinmann 指近年巨灾损失偏低不应掩盖自然巨灾、通胀、网络与地缘政治带来的不确定性，强调纪律承保与风险对价是保障再保长期可用性的前提，并把 ILS 定位为客户可选的补充工具。",
            "tc": "漢諾威再保險德國子公司 E+S Rück 在巴登巴登再保會議期間表示，德國再保需求仍強、整體環境穩定，但傳統再保資本增加令價格與條款競爭明顯加劇。行政總裁 Steinmann 指近年巨災損失偏低不應掩蓋自然巨災、通脹、網絡與地緣政治帶來的不確定性，強調紀律承保與風險對價是保障再保長期可用性的前提，並把 ILS 定位為客户可選的補充工具。"
        },
        "why": {
            "sc": "再保议价周期转向，是香港保单保证/分红结构与附加保障条款变化的上游信号；可用于理解未来一两年产品条款与费率取向，而不只是看单一公司加价。",
            "tc": "再保議價週期轉向，是香港保單保證／分紅結構與附加保障條款變化的上游信號；可用於理解未來一兩年產品條款與費率取向，而不只是看單一公司加價。"
        },
        "source": {
            "sc": "Artemis 2026-10-19（E+S Rück 巴登巴登续保展望）",
            "tc": "Artemis 2026-10-19（E+S Rück 巴登巴登續保展望）",
            "lang": "en",
            "name": "artemis",
            "date": "2026-10-19"
        },
        "tags": {
            "sc": ["再保险", "巴登巴登", "承保纪律", "ILS", "定价"],
            "tc": ["再保險", "巴登巴登", "承保紀律", "ILS", "定價"]
        },
        "actions": {
            "front": {"sc": "客户沟通：保单条款与费率变化的上游解释", "tc": "客户溝通：保單條款與費率變化的上游解釋"},
            "midback": {"sc": "再保续保与产品定价假设复核", "tc": "再保續保與產品定價假設覆核"},
            "lead": {"sc": "团队简报：再保周期与产品策略", "tc": "團隊簡報：再保週期與產品策略"},
            "cross": {"sc": "跨境风险转移方案素材", "tc": "跨境風險轉移方案素材"}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "ingestedAt": NOW
    },
    {
        "id": "artemis-catbond-q4-sponsors-20261019",
        "publishedAt": "2026-10-19T18:30:00+08:00",
        "originalUrl": "https://www.artemis.bm/news/lower-spread-environment-may-encourage-more-cat-bond-sponsors-in-q426-rostan-scor-ip/",
        "sourceKey": "artemis",
        "sourceTier": "pro",
        "score": 72,
        "verifyStatus": "verified",
        "contentKind": "report",
        "clusterCount": 1,
        "boards": ["market"],
        "themes": ["ils", "cat-bond", "market", "asset-management"],
        "title": {
            "sc": "SCOR：低息差环境或吸引更多发起人　Q4 巨灾债券发行有望破纪录",
            "tc": "SCOR：低息差環境或吸引更多發起人　Q4 巨災債券發行有望破紀錄"
        },
        "summary": {
            "sc": "SCOR Investment Partners ILS 策略主管 Rostan 回顾第三季指，美、日风季平静无重大登陆，一级巨灾债券市场夏季停发，前三季发行约 185 亿美元，略高于去年同期；计入二级市场后，Artemis 数据为 189 亿美元，创同期新高。他预期低息差环境将鼓励更多发起人在第四季入市，全年有望超越去年 250 亿美元的纪录。",
            "tc": "SCOR Investment Partners ILS 策略主管 Rostan 回顧第三季指，美、日風季平靜無重大登陸，一級巨災債券市場夏季停發，前三季發行約 185 億美元，略高於去年同期；計入二級市場後，Artemis 數據為 189 億美元，創同期新高。他預期低息差環境將鼓勵更多發起人在第四季入市，全年有望超越去年 250 億美元的紀錄。"
        },
        "why": {
            "sc": "ILS 是港府与保监局推动的新资产管理赛道（今年已有首单 sidecar 落地）；理解巨灾债券供需与息差走向，可用于与高净值客户谈另类资产的分散价值，而非只讲收益。",
            "tc": "ILS 是港府與保監局推動的新資產管理賽道（今年已有首單 sidecar 落地）；理解巨災債券供需與息差走向，可用於與高淨值客户談另類資產的分散價值，而非只講收益。"
        },
        "source": {
            "sc": "Artemis 2026-10-19（引 SCOR Investment Partners 第三季评论）",
            "tc": "Artemis 2026-10-19（引 SCOR Investment Partners 第三季評論）",
            "lang": "en",
            "name": "artemis",
            "date": "2026-10-19"
        },
        "tags": {
            "sc": ["巨灾债券", "ILS", "另类资产", "息差", "发行量"],
            "tc": ["巨災債券", "ILS", "另類資產", "息差", "發行量"]
        },
        "actions": {
            "front": {"sc": "客户沟通：另类资产的分散功能", "tc": "客户溝通：另類資產的分散功能"},
            "midback": {"sc": "产品尽职调查：ILS 配置可行性", "tc": "產品盡職調查：ILS 配置可行性"},
            "lead": {"sc": "团队简报：香港 ILS 生态进展", "tc": "團隊簡報：香港 ILS 生態進展"},
            "cross": {"sc": "家办客户资产配置素材", "tc": "家辦客户資產配置素材"}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 2},
        "ingestedAt": NOW
    }
]

added = 0
for it in new_items:
    key = it['originalUrl'].split('?')[0].rstrip('/')
    if key in existing:
        print('skip dup:', it['id'])
        continue
    items.insert(0, it)
    existing.add(key)
    added += 1

# 两条 pending 已核原文（标题+日期+署名页确认，正文付费）
upgraded = []
for it in items:
    if it.get('verifyStatus') == 'pending' and it.get('originalUrl', '').split('?')[0].rstrip('/') in {
        'https://insuranceasianews.com/japans-msad-considering-deal-for-malaysian-insurer-lpi-capital-bloomberg',
        'https://insuranceasianews.com/markel-hires-ray-lei-as-greater-china-product-proposition-lead'
    }:
        it['verifyStatus'] = 'verified'
        upgraded.append(it['id'])

items.sort(key=lambda x: x.get('publishedAt') or '', reverse=True)

meta = d['meta']
meta['generatedAt'] = NOW
meta['itemCount'] = len(items)
meta['windowNote'] = {"sc": f"本库{len(items)}条。", "tc": f"本庫{len(items)}條。"}

json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('added', added, 'total', len(items), 'upgraded', upgraded)
