#!/usr/bin/env python3
# 增量插入 cron 2026-08-22 18:12 采集条目
import json
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=8))
NOW = datetime(2026, 8, 22, 18, 12, 0, tzinfo=TZ).isoformat()

new_item = {
    "id": "caixin-evergrande-life-license-20260822",
    "clusterCount": 1,
    "score": 76,
    "verifyStatus": "verified",
    "sourceTier": "pro",
    "sourceKey": "caixin",
    "title": {
        "sc": "财新：金融监管总局吊销恒大寿险牌照 涉违规运用保险资金与利益输送 [EN原文]",
        "tc": "財新：金融監管總局吊銷恆大壽險牌照 涉違規運用保險資金與利益輸送 [EN原文]"
    },
    "summary": {
        "sc": "国家金融监督管理总局以严重合规失当为由，吊销恒大寿险业务牌照，指其违规运用保险资金、向关联方输送利益。恒大寿险2015年入股中鑫大东方人寿（持50%股权）进入保险业，长期充当恒大集团融资工具；吊销决定发布在恒大创始人许家印被判终身监禁次日，标志该险企进入终局。",
        "tc": "國家金融監督管理總局以嚴重合規失當為由，吊銷恆大壽險業務牌照，指其違規運用保險資金、向關聯方輸送利益。恆大壽險2015年入股中鑫大東方人壽（持50%股權）進入保險業，長期充當恆大集團融資工具；吊銷決定發佈在恆大創始人許家印被判終身監禁次日，標誌該險企進入終局。"
    },
    "why": {
        "sc": "内地监管重拳样本：险企沦为集团融资工具被直接吊销牌照，与香港保监局对保费融资杠杆风险的主题查察形成对照，是渠道沟通内地客时可引用的监管趋严背景；提示留意内地保险业出清节奏与跨境资金合规议题。",
        "tc": "內地監管重拳樣本：險企淪為集團融資工具被直接吊銷牌照，與香港保監局對保費融資槓桿風險的主題查察形成對照，是渠道溝通內地客時可引用的監管趨嚴背景；提示留意內地保險業出清節奏與跨境資金合規議題。"
    },
    "actions": {
        "front": {},
        "midback": {},
        "lead": {
            "sc": "内地监管出清谈资",
            "tc": "內地監管出清談資"
        },
        "cross": {}
    },
    "rolesImpact": {
        "front": 0,
        "midback": 0,
        "lead": 1,
        "cross": 0
    },
    "source": {
        "sc": "Caixin Global 财新国际",
        "lang": "en"
    },
    "boards": ["reg"],
    "themes": ["regulatory", "compliance"],
    "tags": {
        "sc": ["恒大寿险", "牌照吊销", "金融监管总局", "资金运用"],
        "tc": ["恆大壽險", "牌照吊銷", "金融監管總局", "資金運用"]
    },
    "contentKind": "news",
    "publishedAt": "2026-08-22T02:35:00+08:00",
    "originalUrl": "https://www.caixinglobal.com/2026-08-22/china-revokes-evergrande-lifes-license-over-illegal-fund-use-102476710.html",
    "ingestedAt": NOW,
    "contentRole": {
        "sc": "本站导读",
        "tc": "本站導讀"
    },
    "featured": False,
    "evergreen": False
}

path = 'data/live-items.json'
d = json.load(open(path, encoding='utf-8'))

# 去重：同 id / 同 originalUrl（sourceKey 为信源名，可多条目共用）
existing_ids = {it['id'] for it in d['items']}
existing_urls = {it.get('originalUrl') for it in d['items']}
assert new_item['id'] not in existing_ids, 'duplicate id'
assert new_item['originalUrl'] not in existing_urls, 'duplicate url'

d['items'].insert(0, new_item)
d['meta']['generatedAt'] = NOW
d['meta']['itemCount'] = len(d['items'])
d['meta']['windowNote'] = {
    "sc": f"本库{len(d['items'])}条。",
    "tc": f"本庫{len(d['items'])}條。"
}
json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('inserted, total:', len(d['items']))
