#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日增量采集 2026-08-30(21:0x 补跑): 插入新条目到 live-items.json 最前, 更新 meta
窗口: 2026-08-29T09:06:33+08:00 (last-check) 之后; 补录 08-28 漏采的 IA 执法事件
信源覆盖: oncc(媒体)/tvb(媒体)/uhk(媒体); IA/HKMA/NFRA/保司新闻页 无 08-29~30 新公告
"""
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
NOW_STR = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

NEW_ITEMS = [
    {
        "id": "oncc-flmi-cheating-20260828",
        "clusterCount": 8,
        "score": 82,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "oncc",
        "title": {
            "sc": "保监局伙警方捣破FLMI资格试代考集团 拘15人 即日暂停认可涉案中心资格",
            "tc": "保監局夥警方搗破FLMI資格試代考集團 拘15人 即日暫停認可涉案中心資格"
        },
        "summary": {
            "sc": "保监局伙警方展开「雾泽」行动，瓦解由现职及前持牌保险从业员操控的FLMI资格考试作弊集团：观塘考场电脑预装遥距操控程式代答，考生额外缴付1.4万港元，共拘6男9女。保监局即日暂停认可涉案中心获取的FLMI资格，并将详细审核相关持牌人士。",
            "tc": "保監局夥警方展開「霧澤」行動，瓦解由現職及前持牌保險從業員操控的FLMI資格考試作弊集團：觀塘考場電腦預裝遙距操控程式代答，考生額外繳付1.4萬港元，共拘6男9女。保監局即日暫停認可涉案中心獲取的FLMI資格，並將詳細審核相關持牌人士。"
        },
        "why": {
            "sc": "中介人须以诚实方式取得学历资格，向保监局提供误导资料最高可罚5万港元；IA首次就资格试作弊联合警方执法并复核已获资格人士，直接影响持牌中介合规风险与培训生态。",
            "tc": "中介人須以誠實方式取得學歷資格，向保監局提供誤導資料最高可罰5萬港元；IA首次就資格試作弊聯合警方執法並覆核已獲資格人士，直接影響持牌中介合規風險與培訓生態。"
        },
        "actions": {
            "front": {"sc": "持牌中介自查资格来源与培训合规", "tc": "持牌中介自查資格來源與培訓合規"},
            "midback": {"sc": "IA执法与牌照复核动态跟踪", "tc": "IA執法與牌照覆核動態跟蹤"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "on.cc東網", "lang": "zh"},
        "boards": ["reg", "market"],
        "themes": ["fraud", "compliance"],
        "tags": {
            "sc": ["保监局", "FLMI", "资格考试", "执法", "持牌中介"],
            "tc": ["保監局", "FLMI", "資格考試", "執法", "持牌中介"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-28T14:30:00+08:00",
        "originalUrl": "https://hk.on.cc/hk/bkn/cnt/news/20260828/bkn-20260828143015880-0828_00822_001.html",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "tvb-hui-5yr-finance-20260830",
        "clusterCount": 4,
        "score": 78,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "tvb",
        "title": {
            "sc": "许正宇：首份五年规划金融三大方向 家族办公室增至3000间",
            "tc": "許正宇：首份五年規劃金融三大方向 家族辦公室增至3,000間"
        },
        "summary": {
            "sc": "许正宇指首份五年规划金融范畴聚焦三大方向：扩大融资、风险管理、资产管理等现有优势；放大金融红利结合其他产业；开拓大宗商品及黄金交易。家办数量已由1,600间增至3,000间，规划下月16日与施政报告同日公布，将为市场提供明确方向。",
            "tc": "許正宇指首份五年規劃金融範疇聚焦三大方向：擴大融資、風險管理、資產管理等現有優勢；放大金融紅利結合其他產業；開拓大宗商品及黃金交易。家辦數量已由1,600間增至3,000間，規劃下月16日與施政報告同日公佈，將為市場提供明確方向。"
        },
        "why": {
            "sc": "五年规划首次为金融业定指导性方向，家办数量倍增印证政策成效；大宗商品与黄金交易被列为新增长点，预示香港金融结构扩容，对保险资金运用与财富管理配置具风向标意义。",
            "tc": "五年規劃首次為金融業定指導性方向，家辦數量倍增印證政策成效；大宗商品與黃金交易被列為新增長點，預示香港金融結構擴容，對保險資金運用與財富管理配置具風向標意義。"
        },
        "actions": {
            "front": {},
            "midback": {},
            "lead": {"sc": "五年规划金融政策要点转内训材料", "tc": "五年規劃金融政策要點轉內訓材料"},
            "cross": {"sc": "家办与跨境财富政策跟踪", "tc": "家辦與跨境財富政策跟蹤"}
        },
        "rolesImpact": {"front": 0, "midback": 0, "lead": 1, "cross": 1},
        "source": {"sc": "TVB News", "lang": "zh"},
        "boards": ["family", "reg"],
        "themes": ["family-office", "reg"],
        "tags": {
            "sc": ["许正宇", "五年规划", "家族办公室", "大宗商品", "黄金交易"],
            "tc": ["許正宇", "五年規劃", "家族辦公室", "大宗商品", "黃金交易"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-30T11:44:00+08:00",
        "originalUrl": "https://news.tvb.com/tc/1192228-許正宇︰家族辦公室增至三千間五年規劃將為市場提供明確方向",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "uhk-pet-insurance-20260829",
        "clusterCount": 2,
        "score": 68,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "uhk",
        "title": {
            "sc": "消委会调查24个宠物保险计划：年费差近14倍 约七成限8岁前首次投保",
            "tc": "消委會調查24個寵物保險計劃：年費差近14倍 約七成限8歲前首次投保"
        },
        "summary": {
            "sc": "消委会6月调查7间公司24个宠物保险计划：年缴保费约1,000至14,000元，差距近14倍；23个计划承保猫狗，1个仅限龟鸟；约七成将首次投保年龄上限设为8岁。提醒细阅年度医疗保额、自负额、等候期及第三者责任保障。",
            "tc": "消委會6月調查7間公司24個寵物保險計劃：年繳保費約1,000至14,000元，差距近14倍；23個計劃承保貓狗，1個僅限龜鳥；約七成將首次投保年齡上限設為8歲。提醒細閱年度醫療保額、自負額、等候期及第三者責任保障。"
        },
        "why": {
            "sc": "宠物保险属新兴个人险种，保费与条款差异大，投保年龄限制是最大门槛；对前线IFA拓展家庭保障需求与客户教育有直接参考价值。",
            "tc": "寵物保險屬新興個人險種，保費與條款差異大，投保年齡限制是最大門檻；對前線IFA拓展家庭保障需求與客戶教育有直接參考價值。"
        },
        "actions": {
            "front": {"sc": "宠物保险客户教育与需求挖掘", "tc": "寵物保險客戶教育與需求挖掘"},
            "midback": {},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 0, "lead": 0, "cross": 0},
        "source": {"sc": "UHK 港生活", "lang": "zh"},
        "boards": ["product", "market"],
        "themes": ["product", "market"],
        "tags": {
            "sc": ["消委会", "宠物保险", "投保年龄", "医疗保额", "家庭保障"],
            "tc": ["消委會", "寵物保險", "投保年齡", "醫療保額", "家庭保障"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-29T12:19:04+08:00",
        "originalUrl": "https://hk.ulifestyle.com.hk/topic/detail/20102396/%E6%B6%88%E5%A7%94%E6%9C%83%E5%AF%B5%E7%89%A9%E4%BF%9D%E9%9A%AA-%E7%AC%AC%E4%B8%89%E8%80%85%E8%B2%AC%E4%BB%BB%E4%BF%9D%E9%9A%AA-%E5%B9%B4%E9%95%B7%E5%AF%B5%E7%89%A9%E9%A6%96%E6%AC%A1%E6%8A%95%E4%BF%9D-%E8%B2%93%E7%8B%97%E5%AF%B5%E7%89%A9%E4%BF%9D%E9%9A%AA-%E5%AF%B5%E7%89%A9%E4%BF%9D%E9%9A%AA%E8%87%AA%E8%B2%A0%E9%A1%8D",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]


def main():
    # 摘要字数校验 (50-100字)
    for it in NEW_ITEMS:
        n = len(it['summary']['sc'])
        if not (50 <= n <= 105):
            print(f"WARN 摘要字数 {n}: {it['id']}")
        else:
            print(f"OK 摘要 {n}字: {it['id']}")

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
