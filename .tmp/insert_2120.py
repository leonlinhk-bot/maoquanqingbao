#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""21:08 cron: insert 2 backfilled NFRA items (missed by earlier runs), update meta."""
import json
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 22, 21, 20, 0, tzinfo=TZ).isoformat()

ITEMS = [
    {
        "id": "nfra-nonauto-governance-20260822",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "nfra",
        "title": {
            "sc": "金融监管总局印发《非车险综合治理行动方案》：分险种分阶段推进存量产品重新备案",
            "tc": "金融監管總局印發《非車險綜合治理行動方案》：分險種分階段推進存量產品重新備案"
        },
        "summary": {
            "sc": "金融监管总局近日印发《非车险综合治理行动方案》，治理非车险市场无序竞争：分险种、分阶段推进存量产品重新备案，加快产品清虚提质；强化中介与互联网平台保险业务管控，推动合规经营、有序竞争，方案共六部分。",
            "tc": "金融監管總局近日印發《非車險綜合治理行動方案》，治理非車險市場無序競爭：分險種、分階段推進存量產品重新備案，加快產品清虛提質；強化中介與互聯網平台保險業務管控，推動合規經營、有序競爭，方案共六部分。"
        },
        "why": {
            "sc": "内地财险产品端「清虚提质」提速，互联网平台搭售与非车险乱象整治直接影响跨境销售的合规口径；与香港中介监管（无牌销售、经纪转介查察）形成对照，提示渠道关注内地产品备案与销售合规趋势。",
            "tc": "內地財險產品端「清虛提質」提速，互聯網平台搭售與非車險亂象整治直接影響跨境銷售的合規口徑；與香港中介監管（無牌銷售、經紀轉介查察）形成對照，提示渠道關注內地產品備案與銷售合規趨勢。"
        },
        "actions": {
            "front": {},
            "midback": {
                "sc": "内地产品备案与合规趋势跟踪",
                "tc": "內地產品備案與合規趨勢跟蹤"
            },
            "lead": {},
            "cross": {
                "sc": "中介与互联网渠道合规口径",
                "tc": "中介與互聯網渠道合規口徑"
            }
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "source": {"sc": "法治日报（腾讯新闻转载）", "lang": "zh"},
        "boards": ["reg"],
        "themes": ["reg", "product"],
        "tags": {
            "sc": ["金融监管总局", "非车险", "产品备案", "综合治理", "互联网保险"],
            "tc": ["金融監管總局", "非車險", "產品備案", "綜合治理", "互聯網保險"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-22T07:54:00+08:00",
        "originalUrl": "https://news.qq.com/rain/a/20260822A02B8200",
        "ingestedAt": NOW,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "nfra-alm-measures-20260822",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "nfra",
        "title": {
            "sc": "金融监管总局发布《保险公司资产负债管理办法》：2027年起施行 暂不达标险企设3年过渡期",
            "tc": "金融監管總局發佈《保險公司資產負債管理辦法》：2027年起施行 暫不達標險企設3年過渡期"
        },
        "summary": {
            "sc": "金融监管总局8月21日发布《保险公司资产负债管理办法》：对财险、人身险公司分别设置资产负债监管指标，以利率风险对冲率替换久期缺口指标；自2027年1月1日施行，暂不达标险企设3年过渡期，核心是应对低利率环境。",
            "tc": "金融監管總局8月21日發佈《保險公司資產負債管理辦法》：對財險、人壽險公司分別設置資產負債監管指標，以利率風險對沖率替換久期缺口指標；自2027年1月1日施行，暫不達標險企設3年過渡期，核心是應對低利率環境。"
        },
        "why": {
            "sc": "内地资负管理新规落地，与香港保监局保费融资主题查察同向：低利率环境下监管从负债端定价转向资产端匹配管控；港险从业者可观察内地监管框架收紧节奏，对跨境配置与产品设计逻辑有参照意义。",
            "tc": "內地資負管理新規落地，與香港保監局保費融資主題查察同向：低利率環境下監管從負債端定價轉向資產端匹配管控；港險從業者可觀察內地監管框架收緊節奏，對跨境配置與產品設計邏輯有參照意義。"
        },
        "actions": {
            "front": {},
            "midback": {
                "sc": "内地监管框架收紧节奏跟踪",
                "tc": "內地監管框架收緊節奏跟蹤"
            },
            "lead": {},
            "cross": {
                "sc": "低利率环境资产负债匹配议题",
                "tc": "低利率環境資產負債匹配議題"
            }
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 1},
        "source": {"sc": "证券时报（东方财富转载）", "lang": "zh"},
        "boards": ["reg"],
        "themes": ["reg", "capital"],
        "tags": {
            "sc": ["金融监管总局", "资产负债管理", "保险公司", "过渡期", "低利率"],
            "tc": ["金融監管總局", "資產負債管理", "保險公司", "過渡期", "低利率"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-22T07:48:00+08:00",
        "originalUrl": "https://finance.eastmoney.com/a/202608223849824419.html",
        "ingestedAt": NOW,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]

path = 'data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
existing_ids = {it['id'] for it in d['items']}
existing_keys = {(it.get('sourceKey'), it.get('publishedAt', '')[:10]) for it in d['items']}

added = []
for it in ITEMS:
    if it['id'] in existing_ids:
        print("SKIP dup id:", it['id'])
        continue
    added.append(it)

d['items'] = added + d['items']
d['meta']['generatedAt'] = NOW
d['meta']['itemCount'] = len(d['items'])
d['meta']['windowNote'] = {
    "sc": f"本库{len(d['items'])}条。",
    "tc": f"本庫{len(d['items'])}條。"
}
d['meta']['asOf'] = "2026-08-22"

json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"added {len(added)} items; total now {len(d['items'])}")
for it in added:
    print(" +", it['id'])
