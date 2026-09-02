#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每日增量采集 2026-09-02 18:08 cron: 插入新条目到 live-items.json 最前, 更新 meta
窗口: 2026-09-01T21:10:00+08:00 (last-check) 之后
本轮新增(4): aia官方新闻稿(财富恒裕3) + InsuranceBusiness 3篇(MAS FSTI 4.0 / 国泰人寿GAIP / 穆迪ILS)
另含 13:36 部分批次已插入未提交的 4 条 (insuranceasia x3 + jefferies x1, 一并随本次提交上线)
信源覆盖: IA/HKMA/AIA新闻稿页/AIA官网/AXA/SunLife/Pru/Manulife/SCMP/FSTB/NFRA/InsuranceAsia RSS 已查, 窗口内无其他新公告
"""
import json, datetime

NOW = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8)))
NOW_STR = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

NEW_ITEMS = [
    {
        "id": "aia-wealth-plan3-20260902",
        "clusterCount": 1,
        "score": 80,
        "verifyStatus": "verified",
        "sourceTier": "insurer",
        "sourceKey": "aia",
        "title": {
            "sc": "友邦香港推「财富恒裕」人寿保险计划3：高净值终身分红寿险 最高逾6倍保障杠杆",
            "tc": "友邦香港推「財富恆裕」人壽保險計劃3：高淨值終身分紅壽險 最高逾6倍保障槓桿"
        },
        "summary": {
            "sc": "友邦香港及澳门9月2日推出专为高净值客户设计的终身分红寿险「财富恒裕3」：指定情况下保障最高可达保费6倍以上，设保单分拆选项，属香港按证公司「保单逆按计划」合资格寿险，可将保单转为终身退休收入；传承功能含市场首创「未来心愿安排」「健康障碍选项」及受益人灵活选项等。",
            "tc": "友邦香港及澳門9月2日推出專為高淨值客戶設計的終身分紅壽險「財富恆裕3」：指定情況下保障最高可達保費6倍以上，設保單分拆選項，屬香港按證公司「保單逆按計劃」合資格壽險，可將保單轉為終身退休收入；傳承功能含市場首創「未來心願安排」「健康障礙選項」及受益人靈活選項等。"
        },
        "why": {
            "sc": "高净值终身寿险加码保单分拆、逆按转换与预设传承指示等结构，直击高净值客户财富传承痛点，是友邦强化HNW产品线、应对长寿时代需求的重要落子，也是同类产品对标的基准。",
            "tc": "高淨值終身壽險加碼保單分拆、逆按轉換與預設傳承指示等結構，直擊高淨值客戶財富傳承痛點，是友邦強化HNW產品線、應對長壽時代需求的重要落子，也是同類產品對標的基準。"
        },
        "actions": {
            "front": {"sc": "高净值客户产品对位话术", "tc": "高淨值客戶產品對位話術"},
            "midback": {"sc": "传承功能条款拆解与竞品对比", "tc": "傳承功能條款拆解與競品對比"},
            "lead": {"sc": "HNW终身寿险产品动向跟踪", "tc": "HNW終身壽險產品動向跟蹤"},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "友邦保险 AIA（官方新闻稿）", "lang": "zh"},
        "boards": ["product", "family"],
        "themes": ["hnw", "par"],
        "tags": {
            "sc": ["友邦", "财富恒裕3", "高净值", "终身分红寿险", "保单逆按"],
            "tc": ["友邦", "財富恆裕3", "高淨值", "終身分紅壽險", "保單逆按"]
        },
        "contentKind": "press",
        "publishedAt": "2026-09-02T15:06:00+08:00",
        "originalUrl": "https://www.aia.com.hk/zh-hk/about-aia/about-us/media-centre/press-releases/2026/aia-press-release-20260902",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-mas-fsti4-ai-20260902",
        "clusterCount": 1,
        "score": 63,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusiness",
        "title": {
            "sc": "新加坡金管局3年注资2.2亿坡元推FSTI 4.0 设AI Pathfinder轨道对接官方审核AI工具 [EN原文]",
            "tc": "新加坡金管局3年注資2.2億坡元推FSTI 4.0 設AI Pathfinder軌道對接官方審核AI工具 [EN原文]"
        },
        "summary": {
            "sc": "新加坡金管局承诺3年投入2.2亿坡元推出金融科技与创新计划FSTI 4.0，设AI Pathfinder等六条轨道：前者经MAS主导的PathFin.ai平台，协助金融机构部署经官方审核的AI工具；另有人力轨道3年支援至少1000个金融科技实习。亚太保险科技市场2025年估约208亿美元，AI相关模式已成融资主流。",
            "tc": "新加坡金管局承諾3年投入2.2億坡元推出金融科技與創新計劃FSTI 4.0，設AI Pathfinder等六條軌道：前者經MAS主導的PathFin.ai平台，協助金融機構部署經官方審核的AI工具；另有人力軌道3年支援至少1000個金融科技實習。亞太保險科技市場2025年估約208億美元，AI相關模式已成融資主流。"
        },
        "why": {
            "sc": "区域监管将AI工具纳入官方审核与对接轨道，为保险公司采用AI提供合规捷径；对香港GenA.I.沙盒++及保险科技生态建设具直接参照意义。",
            "tc": "區域監管將AI工具納入官方審核與對接軌道，為保險公司採用AI提供合規捷徑；對香港GenA.I.沙盒++及保險科技生態建設具直接參照意義。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "AI工具合规采用路径跟踪", "tc": "AI工具合規採用路徑跟蹤"},
            "lead": {"sc": "区域AI监管动向参考", "tc": "區域AI監管動向參考"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Business 保险商业", "lang": "en"},
        "boards": ["tech"],
        "themes": ["insurtech", "ai"],
        "tags": {
            "sc": ["新加坡金管局", "MAS", "FSTI 4.0", "AI Pathfinder", "保险科技"],
            "tc": ["新加坡金管局", "MAS", "FSTI 4.0", "AI Pathfinder", "保險科技"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-02T09:28:16+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/mass-s220m-fintech-scheme-has-an-ai-onramp-insurers-should-know-about-588193.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-cathay-life-gaip-20260902",
        "clusterCount": 1,
        "score": 61,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusiness",
        "title": {
            "sc": "台湾国泰人寿加入GAIP成为主要伙伴 亚洲保障缺口逼近1万亿美元 [EN原文]",
            "tc": "台灣國泰人壽加入GAIP成為主要夥伴 亞洲保障缺口逼近1萬億美元 [EN原文]"
        },
        "summary": {
            "sc": "台湾最大寿险公司国泰人寿加入全球亚洲保险伙伴关系(GAIP)成为主要伙伴，将参与保障缺口、健康与退休保障及气候风险工作组。GAIP数据显示亚太保障缺口2022年达8860亿美元、较2017年增38%，瑞士再保险估2023年为9050亿美元、年均增5.8%，GAIP主席指缺口现已接近1万亿美元。",
            "tc": "台灣最大壽險公司國泰人壽加入全球亞洲保險夥伴關係(GAIP)成為主要夥伴，將參與保障缺口、健康與退休保障及氣候風險工作組。GAIP數據顯示亞太保障缺口2022年達8860億美元、較2017年增38%，瑞士再保險估2023年為9050億美元、年均增5.8%，GAIP主席指缺口現已接近1萬億美元。"
        },
        "why": {
            "sc": "亚洲保障缺口近万亿美元是港险跨境客群与亚洲业务叙事的核心数据；国泰人寿以台湾最大寿险身份加入GAIP，反映区域头部险企参与缺口治理的布局动向。",
            "tc": "亞洲保障缺口近萬億美元是港險跨境客群與亞洲業務敘事的核心數據；國泰人壽以台灣最大壽險身份加入GAIP，反映區域頭部險企參與缺口治理的佈局動向。"
        },
        "actions": {
            "front": {"sc": "保障缺口客户叙事数据点", "tc": "保障缺口客戶敘事數據點"},
            "midback": {"sc": "区域险企合作格局观察", "tc": "區域險企合作格局觀察"},
            "lead": {},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 0, "cross": 0},
        "source": {"sc": "Insurance Business 保险商业", "lang": "en"},
        "boards": ["market"],
        "themes": ["market", "health"],
        "tags": {
            "sc": ["国泰人寿", "GAIP", "保障缺口", "台湾", "亚洲保险"],
            "tc": ["國泰人壽", "GAIP", "保障缺口", "台灣", "亞洲保險"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-02T09:24:21+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/life-insurance/cathay-life-joins-gaip-as-asias-protection-gap-approaches-1-trillion-588192.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "ibm-moodys-ils-record-20260902",
        "clusterCount": 1,
        "score": 64,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "insurancebusiness",
        "title": {
            "sc": "穆迪：上半年保险连接证券未偿资本1445亿美元创纪录 巨灾债同比增17% [EN原文]",
            "tc": "穆迪：上半年保險連接證券未償資本1445億美元創紀錄 巨災債同比增17% [EN原文]"
        },
        "summary": {
            "sc": "穆迪数据显示，2026年上半年保险连接证券(ILS)未偿资本达1445亿美元创纪录：巨灾债约634亿美元、同比增17%且较2021年近翻倍，再保侧车约230亿美元、较2024年底增约50%；截至6月的12个月巨灾债发行249亿美元创同期新高。传统再保费率年内续跌16%，为1990年代末以来最大跌幅。",
            "tc": "穆迪數據顯示，2026年上半年保險連接證券(ILS)未償資本達1445億美元創紀錄：巨災債約634億美元、同比增17%且較2021年近翻倍，再保側車約230億美元、較2024年底增約50%；截至6月的12個月巨災債發行249億美元創同期新高。傳統再保費率年內續跌16%，為1990年代末以來最大跌幅。"
        },
        "why": {
            "sc": "ILS资本持续膨胀与传统再保价格加速下行并存，标志再保市场资本过剩格局加深，直接影响香港市场巨灾风险定价、再保安排与分出策略。",
            "tc": "ILS資本持續膨脹與傳統再保價格加速下行並存，標誌再保市場資本過剩格局加深，直接影響香港市場巨災風險定價、再保安排與分出策略。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "再保资本与定价趋势跟踪", "tc": "再保資本與定價趨勢跟蹤"},
            "lead": {"sc": "再保成本谈判与安排参考", "tc": "再保成本談判與安排參考"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "Insurance Business 保险商业", "lang": "en"},
        "boards": ["market"],
        "themes": ["reinsurance", "capital"],
        "tags": {
            "sc": ["穆迪", "ILS", "巨灾债", "再保险", "费率下行"],
            "tc": ["穆迪", "ILS", "巨災債", "再保險", "費率下行"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-02T10:20:21+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/moodys-sees-record-ils-capital-funding-riskier-hardertoplace-perils-588258.aspx",
        "ingestedAt": NOW_STR,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]


def main():
    # 摘要字数校验 (50-105字)
    for it in NEW_ITEMS:
        n = len(it['summary']['sc'])
        nt = len(it['summary']['tc'])
        flag = ''
        if not (50 <= n <= 105):
            flag += f' SC={n}'
        if not (50 <= nt <= 105):
            flag += f' TC={nt}'
        print(f"{'OK ' if not flag else 'WARN'} {n}/{nt}字: {it['id']}{flag}")

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
