#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-08-27 18:08 incremental items into live-items.json (front), update meta."""
import json
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=8))
now = datetime.now(TZ)
now_iso = now.strftime('%Y-%m-%dT%H:%M:%S+08:00')

NEW_ITEMS = [
    {
        "id": "ibm-nepal-glacier-travel-cover-20260827",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "尼泊尔洪水确认由冰川崩塌引发 旅游及探险险条款响应成焦点 [EN原文]",
            "tc": "尼泊爾洪水確認由冰川崩塌引發 旅遊及探險險條款響應成焦點 [EN原文]"
        },
        "summary": {
            "sc": "尼泊尔-西藏边境致命山洪已致近1500人失踪、至少700名外籍人士。专家分析卫星影像确认灾难由约5200米高处冰川崩塌引发而非地震，美国地质调查局澄清地震信号实为崩塌产生。事故成因将决定旅游及探险保单条款是否触发，非医疗撤离保障差异较大。",
            "tc": "尼泊爾-西藏邊境致命山洪已致近1500人失蹤、至少700名外籍人士。專家分析衛星影像確認災難由約5200米高處冰川崩塌引發而非地震，美國地質調查局澄清地震信號實為崩塌產生。事故成因將決定旅遊及探險保單條款是否觸發，非醫療撤離保障差異較大。"
        },
        "why": {
            "sc": "灾难成因判定直接影响旅游与探险险条款触发与理赔争议，港险同业可据此为高海拔探险客户检视保障缺口，对经纪行展业与核保具参考价值。",
            "tc": "災難成因判定直接影響旅遊與探險險條款觸發與理賠爭議，港險同業可據此為高海拔探險客戶檢視保障缺口，對經紀行展業與核保具參考價值。"
        },
        "actions": {
            "front": {},
            "midback": {
                "sc": "检视探险旅游险条款与保障缺口",
                "tc": "檢視探險旅遊險條款與保障缺口"
            },
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["product", "market"],
        "themes": ["natcat", "product"],
        "tags": {
            "sc": ["尼泊尔", "冰川崩塌", "旅游保险", "探险险"],
            "tc": ["尼泊爾", "冰川崩塌", "旅遊保險", "探險險"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-27T17:17:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/catastrophe/nepal-flood-was-triggered-by-a-glacier-not-an-earthquake--for-brokers-the-cause-is-the-question-587700.aspx",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "hkma-bank-scam-alert-20260827",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "verified",
        "sourceTier": "official",
        "sourceKey": "hkma",
        "title": {
            "sc": "金管局汇总三银行诈骗警示：汇立银行假冒App、华侨银行(香港)假网站、恒生钓鱼短信 [EN原文]",
            "tc": "金管局匯總三銀行詐騙警示：匯立銀行假冒App、華僑銀行(香港)假網站、恒生釣魚短信 [EN原文]"
        },
        "summary": {
            "sc": "金管局提醒公众留意三间银行警示：Fusion Bank（汇立银行）出现未经授权手机应用程式，华侨银行(香港)有假冒网站及网银登入画面，恒生银行有钓鱼即时讯息。金管局重申银行不会经短信或电邮附连结引导客户交易，亦不会索取密码等敏感资料。",
            "tc": "金管局提醒公眾留意三間銀行警示：Fusion Bank（匯立銀行）出現未經授權手機應用程式，華僑銀行(香港)有假冒網站及網銀登入畫面，恒生銀行有釣魚即時訊息。金管局重申銀行不會經短信或電郵附連結引導客戶交易，亦不會索取密碼等敏感資料。"
        },
        "why": {
            "sc": "假冒App、假网站与钓鱼短信瞄准零售银行客户，针对本港银行的网络诈骗手法持续翻新；保险缴费、转账环节的客户防诈教育可同步引用，前台可作提醒素材。",
            "tc": "假冒App、假網站與釣魚短信瞄準零售銀行客戶，針對本港銀行的網絡詐騙手法持續翻新；保險繳費、轉賬環節的客戶防詐教育可同步引用，前台可作提醒素材。"
        },
        "actions": {
            "front": {
                "sc": "客户防诈提醒素材",
                "tc": "客戶防詐提醒素材"
            },
            "midback": {},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "香港金融管理局 HKMA", "lang": "en"},
        "boards": ["market"],
        "themes": ["fraud", "cyber"],
        "tags": {
            "sc": ["金管局", "假冒App", "钓鱼", "防诈"],
            "tc": ["金管局", "假冒App", "釣魚", "防詐"]
        },
        "contentKind": "press",
        "publishedAt": "2026-08-27",
        "originalUrl": "https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/08/20260827-4/",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]

path = 'data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
existing_ids = {it['id'] for it in d['items']}
existing_urls = {it.get('originalUrl') for it in d['items']}

added = []
for it in NEW_ITEMS:
    if it['id'] in existing_ids:
        print(f"SKIP (dup id): {it['id']}")
        continue
    if it.get('originalUrl') in existing_urls:
        print(f"SKIP (dup url): {it['id']}")
        continue
    added.append(it)

if added:
    d['items'] = added + d['items']
    d['meta']['generatedAt'] = now_iso
    d['meta']['itemCount'] = len(d['items'])
    d['meta']['windowNote'] = {
        "sc": f"本库{len(d['items'])}条。",
        "tc": f"本庫{len(d['items'])}條。"
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"INSERTED {len(added)} items; total={len(d['items'])}")
    for it in added:
        print('  +', it['id'])
else:
    print("NOTHING INSERTED")
