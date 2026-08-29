#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日增量采集 2026-08-29(08:53 补跑): 插入新条目到 live-items.json 最前, 更新 meta"""
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
NOW_STR = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

NEW_ITEMS = [
    {
        "id": "ibm-peakre-moodys-a3-20260829",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "穆迪上调鼎睿再保险评级至A3：认可其治理独立性于复星集团 [EN原文]",
            "tc": "穆迪上調鼎睿再保險評級至A3：認可其治理獨立性於復星集團 [EN原文]"
        },
        "summary": {
            "sc": "复星国际发布中期业绩：溢利17.2亿元增160.3%；旗下鼎睿再保险4月获穆迪由Baa1上调至A3，获认可治理与运营独立于母公司，KKR等成少数股东。A3评级影响再保合约在偿付能力框架下的资本认定。",
            "tc": "復星國際發佈中期業績：溢利17.2億元增160.3%；旗下鼎睿再保險4月獲穆迪由Baa1上調至A3，獲認可治理與運營獨立於母公司，KKR等成少數股東。A3評級影響再保合約在償付能力框架下的資本認定。"
        },
        "why": {
            "sc": "穆迪将再保人治理独立性量化为评级因子，A3与Baa1之差直接决定再保合约能否计入部分监管资本框架，对亚洲分出业务与再保对手方评估有实际影响。",
            "tc": "穆迪將再保人治理獨立性量化為評級因子，A3與Baa1之差直接決定再保合約能否計入部分監管資本框架，對亞洲分出業務與再保對手方評估有實際影響。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "再保对手方与评级动态跟踪", "tc": "再保對手方與評級動態跟蹤"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["market", "insurer"],
        "themes": ["reinsurance", "rating"],
        "tags": {
            "sc": ["穆迪", "鼎睿再保险", "复星国际", "评级上调"],
            "tc": ["穆迪", "鼎睿再保險", "復星國際", "評級上調"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-29T00:22:26+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/asia-reinsurer-sheds-parents-credit-shadow-in-moodys-upgrade-587893.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-agentic-ai-hk-20260828",
        "clusterCount": 1,
        "score": 72,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "代理式AI进入香港保险业：经纪中介尚未入局 合规责任框架待建 [EN原文]",
            "tc": "代理式AI進入香港保險業：經紀中介尚未入局 合規責任框架待建 [EN原文]"
        },
        "summary": {
            "sc": "首期GenA.I.沙盒++共30家金融机构36个用例入选，覆盖医疗理赔AI助手、多智能体欺诈检测及代理式支付，AXA、FWD、汇丰人寿、宏利等在列。文章指IAIS《AI监管应用文件》未新增义务，但中介须在AI自主理赔、反欺诈下自证合规。",
            "tc": "首期GenA.I.沙盒++共30家金融機構36個用例入選，覆蓋醫療理賠AI助手、多智能體欺詐檢測及代理式支付，AXA、FWD、匯豐人壽、宏利等在列。文章指IAIS《AI監管應用文件》未新增義務，但中介須在AI自主理賠、反欺詐下自證合規。"
        },
        "why": {
            "sc": "监管机构同步推进代理式AI测试与治理框架，经纪中介的操守义务将在测试结束后覆盖全市场，是港险渠道端AI合规的风向标。",
            "tc": "監管機構同步推進代理式AI測試與治理框架，經紀中介的操守義務將在測試結束後覆蓋全市場，是港險渠道端AI合規的風向標。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "AI治理与中介合规观察", "tc": "AI治理與中介合規觀察"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["tech", "reg"],
        "themes": ["ai", "reg"],
        "tags": {
            "sc": ["代理式AI", "GenA.I.沙盒++", "保险经纪", "AI治理"],
            "tc": ["代理式AI", "GenA.I.沙盒++", "保險經紀", "AI治理"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-28T23:47:22+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/agentic-ai-enters-hong-kong-insurance--and-brokers-arent-in-the-room-587889.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-tune-protect-q2-20260828",
        "clusterCount": 1,
        "score": 64,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusinessmag",
        "title": {
            "sc": "Tune Protect二季度扭亏为盈 航空旅行险走软 转投车险火险个人险 [EN原文]",
            "tc": "Tune Protect二季度扭虧為盈 航空旅行險走軟 轉投車險火險個人險 [EN原文]"
        },
        "summary": {
            "sc": "马来西亚数字险企Tune Protect二季度恢复盈利，航空关联旅行险量走软，承保能力转向车险、火险及个人险。文章指东南亚经纪主导的一般险分销遭数字原住民险企侵蚀；央行DITO数字保险牌照申请窗口至2026年底，市场结构竞争加剧。",
            "tc": "馬來西亞數字險企Tune Protect二季度恢復盈利，航空關聯旅行險量走軟，承保能力轉向車險、火險及個人險。文章指東南亞經紀主導的一般險分銷遭數字原住民險企侵蝕；央行DITO數字保險牌照申請窗口至2026年底，市場結構競爭加劇。"
        },
        "why": {
            "sc": "BNM数字保险牌照与数字险企转攻传统中间渠道，直接冲击东南亚经纪分销格局，对港险中介及区域扩张策略有对标价值。",
            "tc": "BNM數字保險牌照與數字險企轉攻傳統中間渠道，直接衝擊東南亞經紀分銷格局，對港險中介及區域擴張策略有對標價值。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "东南亚分销格局对标", "tc": "東南亞分銷格局對標"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business", "lang": "en"},
        "boards": ["market", "insurer"],
        "themes": ["channel", "market"],
        "tags": {
            "sc": ["Tune Protect", "马来西亚", "数字保险", "分销渠道"],
            "tc": ["Tune Protect", "馬來西亞", "數字保險", "分銷渠道"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-28T22:18:35+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/tune-protect-returns-to-quarterly-profit-as-airlinelinked-travel-volumes-soften-587874.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]

def main():
    path = 'data/live-items.json'
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    items = data['items']
    existing_ids = {it.get('id') for it in items}
    dup = [it['id'] for it in NEW_ITEMS if it['id'] in existing_ids]
    if dup:
        print('SKIP duplicates:', dup)
    fresh = [it for it in NEW_ITEMS if it['id'] not in existing_ids]
    titles = {(it.get('sourceKey'), it.get('title', {}).get('sc')) for it in items}
    fresh = [it for it in fresh if (it.get('sourceKey'), it.get('title', {}).get('sc')) not in titles]
    items[:0] = fresh
    data['items'] = items
    meta = data['meta']
    meta['itemCount'] = len(items)
    meta['generatedAt'] = NOW_STR
    meta['windowNote'] = {
        "sc": f"本库{len(items)}条。",
        "tc": f"本庫{len(items)}條。"
    }
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'新增 {len(fresh)} 条 -> 总条数 {len(items)}')
    for it in fresh:
        print(' +', it['id'])

if __name__ == '__main__':
    main()
