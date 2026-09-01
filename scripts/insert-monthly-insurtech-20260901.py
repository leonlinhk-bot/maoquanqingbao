#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每月AI与保险科技落地扫描 2026-09-01：插入 4 条新条目 + 回写 insurtech 信源 last-check。"""
import json, datetime

TZ = datetime.timezone(datetime.timedelta(hours=8))
now_iso = datetime.datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")

NEW_ITEMS = [
    {
        "id": "igloo-preseries-c-20260901",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "indotelko",
        "title": {
            "sc": "东南亚保险科技Igloo完成3600万美元Pre-C轮融资 法欧瑞泽与BNP Paribas Cardif领投",
            "tc": "東南亞保險科技Igloo完成3600萬美元Pre-C輪融資 法歐瑞澤與BNP Paribas Cardif領投"
        },
        "summary": {
            "sc": "区域保险科技平台Igloo宣布完成3600万美元Pre-Series C融资，由全球投资机构Eurazeo与保险公司BNP Paribas Cardif领投，Openspace旗下OSV+及La Maison跟投。距上一轮Series B+仅10个月，累计融资约1亿美元，估值较B+轮提升50%。Igloo聚焦东南亚低渗透保险市场，通过多分销渠道与多产品线平台推动普惠保险。",
            "tc": "區域保險科技平台Igloo宣布完成3600萬美元Pre-Series C融資，由全球投資機構Eurazeo與保險公司BNP Paribas Cardif領投，Openspace旗下OSV+及La Maison跟投。距上一輪Series B+僅10個月，累計融資約1億美元，估值較B+輪提升50%。Igloo聚焦東南亞低滲透保險市場，透過多分銷渠道與多產品線平台推動普惠保險。"
        },
        "why": {
            "sc": "东南亚保险科技融资回暖信号，显示财务投资方与保司资本联合押注区域保险数字化与普惠渗透，可作亚洲保险科技估值与融资节奏的参照。",
            "tc": "東南亞保險科技融資回暖信號，顯示財務投資方與保司資本聯合押注區域保險數位化與普惠滲透，可作亞洲保險科技估值與融資節奏的參照。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "区域保险科技融资动向追踪", "tc": "區域保險科技融資動向追蹤"},
            "lead": {"sc": "亚洲保险科技估值节奏参考", "tc": "亞洲保險科技估值節奏參考"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "IndoTelko", "lang": "en"},
        "boards": ["tech", "market"],
        "themes": ["insurtech", "funding", "regional"],
        "tags": {
            "sc": ["保险科技", "Igloo", "融资", "东南亚"],
            "tc": ["保險科技", "Igloo", "融資", "東南亞"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-01T03:49:00+08:00",
        "originalUrl": "https://www.indotelko.com/amp/read/1701779742/igloo-dapatkan-pendanaan-pra-seri-c-senilai-us-36-juta"
    },
    {
        "id": "chinalife-500-agents-20260828",
        "clusterCount": 1,
        "score": 66,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "peoplecn",
        "title": {
            "sc": "中国人寿打造超500个智能体 理赔时效降至0.36天 A股险企AI加速落地",
            "tc": "中國人壽打造超500個智能體 理賠時效降至0.36天 A股險企AI加速落地"
        },
        "summary": {
            "sc": "中国人寿在2026年中期业绩会披露，已打造超500个智能体，应用于销售服务、运营作业与风险管控；基于大模型对意外险、重疾险做责任辅助判定与信息分析，理赔时效降至0.36天；并为销售人员推出「AI私教」培训体系。同期中国平安AI坐席覆盖81%客服、新华保险理赔数字员工日均处理影像件超3万件，A股险企AI正从试点走向规模化落地。",
            "tc": "中國人壽在2026年中期業績會披露，已打造超500個智能體，應用於銷售服務、營運作業與風險管控；基於大模型對意外險、重疾險做責任輔助判定與信息分析，理賠時效降至0.36天；並為銷售人員推出「AI私教」培訓體系。同期中國平安AI坐席覆蓋81%客服、新華保險理賠數字員工日均處理影像件超3萬件，A股險企AI正從試點走向規模化落地。"
        },
        "why": {
            "sc": "头部寿险把智能体数量、Token消耗、理赔时效写进财报，标志AI从单点试点进入可量化经营指标，是内地寿险AI落地最直接的经营参考。",
            "tc": "頭部壽險把智能體數量、Token消耗、理賠時效寫進財報，標誌AI從單點試點進入可量化經營指標，是內地壽險AI落地最直接的經營參考。"
        },
        "actions": {
            "front": {"sc": "了解内地寿险AI理赔落地", "tc": "了解內地壽險AI理賠落地"},
            "midback": {"sc": "核保理赔AI流程对标", "tc": "核保理賠AI流程對標"},
            "lead": {"sc": "行业AI规模化趋势判断", "tc": "行業AI規模化趨勢判斷"},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "人民网", "lang": "zh"},
        "boards": ["insurer", "tech"],
        "themes": ["ai", "agentic-ai", "insurtech"],
        "tags": {
            "sc": ["中国人寿", "智能体", "AI理赔", "保险科技"],
            "tc": ["中國人壽", "智能體", "AI理賠", "保險科技"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-28T19:31:00+08:00",
        "originalUrl": "https://finance-app.people.cn/n1/2026/0828/c1004-40788240.html"
    },
    {
        "id": "kpmg-insurtech-h1-2026",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "verified",
        "sourceTier": "pro",
        "sourceKey": "kpmg",
        "title": {
            "sc": "KPMG：全球保险科技融资上半年降至37亿美元 交易量或创2016年来新低",
            "tc": "KPMG：全球保險科技融資上半年降至37億美元 交易量或創2016年來新低"
        },
        "summary": {
            "sc": "KPMG《Pulse of Fintech H1'26》显示，全球保险科技投资从2025年98亿美元四年高点回落至上半年37亿美元，仅124笔交易，若趋势延续将是2016年以来最低。最大交易为WTW收购Newfront，其后为Alan、Wefox、Corgi融资；亚太最大单为印度Turtlemint的4160万美元。报告指险企转向与全球科技公司合作AI，倒逼保险科技公司证明行业深度与专有数据。",
            "tc": "KPMG《Pulse of Fintech H1'26》顯示，全球保險科技投資從2025年98億美元四年高點回落至上半年37億美元，僅124筆交易，若趨勢延續將是2016年以來最低。最大交易為WTW收購Newfront，其後為Alan、Wefox、Corgi融資；亞太最大單為印度Turtlemint的4160萬美元。報告指險企轉向與全球科技公司合作AI，倒逼保險科技公司證明行業深度與專有數據。"
        },
        "why": {
            "sc": "保险科技融资收缩叠加险企「转投科技巨头」的结构性转向，说明行业竞争从「卖软件」走向「拼行业know-how与数据」，是判断亚洲保险科技估值与格局的关键数据。",
            "tc": "保險科技融資收縮疊加險企「轉投科技巨頭」的結構性轉向，說明行業競爭從「賣軟件」走向「拼行業know-how與數據」，是判斷亞洲保險科技估值與格局的關鍵數據。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "保险科技格局与融资研判", "tc": "保險科技格局與融資研判"},
            "lead": {"sc": "行业结构性转向参考", "tc": "行業結構性轉向參考"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 2, "cross": 0},
        "source": {"sc": "KPMG", "lang": "en"},
        "boards": ["tech", "market"],
        "themes": ["insurtech", "funding", "ai"],
        "tags": {
            "sc": ["保险科技", "融资", "KPMG", "全球"],
            "tc": ["保險科技", "融資", "KPMG", "全球"]
        },
        "contentKind": "stats",
        "publishedAt": "2026-08-28",
        "originalUrl": "https://assets.kpmg.com/content/dam/kpmgsites/xx/pdf/2026/08/pulse-of-fintech-h1-2026.pdf"
    },
    {
        "id": "indiafirst-agentforce-20260831",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "verified",
        "sourceTier": "media",
        "sourceKey": "cioandleader",
        "title": {
            "sc": "印度IndiaFirst Life选用Salesforce Agentforce 在承保/客服/理赔部署AI智能体",
            "tc": "印度IndiaFirst Life選用Salesforce Agentforce 在承保/客服/理賠部署AI智能體"
        },
        "summary": {
            "sc": "印度Bank of Baroda旗下寿险公司IndiaFirst Life宣布采用Salesforce Agentforce推进企业级AI转型，将可信AI智能体嵌入三大流程：新业务承保（审核KYC与财务/医疗文件、标记异常并给出核保建议）、客户服务（自动分类与情绪识别、生成合规回复）、理赔（核对文件、识别缺项、异常转人工）。项目建立在统一Salesforce平台上，覆盖从获客到理赔的全旅程。",
            "tc": "印度Bank of Baroda旗下壽險公司IndiaFirst Life宣布採用Salesforce Agentforce推進企業級AI轉型，將可信AI智能體嵌入三大流程：新業務承保（審核KYC與財務/醫療文件、標記異常並給出核保建議）、客戶服務（自動分類與情緒識別、生成合規回覆）、理賠（核對文件、識別缺項、異常轉人工）。項目建立在統一Salesforce平台上，覆蓋從獲客到理賠的全旅程。"
        },
        "why": {
            "sc": "寿险公司把代理式AI嵌入承保、客服、理赔三大核心环节，是亚洲寿险「AI智能体」落地的具体样本，可作核保理赔流程AI化的对标。",
            "tc": "壽險公司把代理式AI嵌入承保、客服、理賠三大核心環節，是亞洲壽險「AI智能體」落地的具體樣本，可作核保理賠流程AI化的對標。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "核保理赔AI流程对标", "tc": "核保理賠AI流程對標"},
            "lead": {"sc": "代理式AI落地趋势观察", "tc": "代理式AI落地趨勢觀察"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "source": {"sc": "CIO&Leader", "lang": "en"},
        "boards": ["insurer", "tech"],
        "themes": ["ai", "agentic-ai", "insurtech"],
        "tags": {
            "sc": ["Agentforce", "代理式AI", "印度", "核保理赔"],
            "tc": ["Agentforce", "代理式AI", "印度", "核保理賠"]
        },
        "contentKind": "news",
        "publishedAt": "2026-08-31",
        "originalUrl": "https://www.cioandleader.com/indiafirst-lifes-ai-driven-transformation-with-salesforce-agentforce/"
    }
]

# --- 1. live-items.json ---
path = "data/live-items.json"
data = json.load(open(path, encoding="utf-8"))
existing_ids = {it["id"] for it in data["items"]}
added = []
for it in NEW_ITEMS:
    if it["id"] in existing_ids:
        print("SKIP (dup id):", it["id"])
        continue
    data["items"].insert(0, it)
    added.append(it["id"])

data["meta"]["itemCount"] = len(data["items"])
data["meta"]["generatedAt"] = now_iso
data["meta"]["windowNote"] = {
    "sc": f"本库{len(data['items'])}条。",
    "tc": f"本庫{len(data['items'])}條。"
}
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"INSERTED {len(added)} items; total now {len(data['items'])}")
for a in added:
    print(" +", a)

# --- 2. last-check.json (仅更新 insurtech 信源检查时间) ---
lc_path = "data/last-check.json"
lc = json.load(open(lc_path, encoding="utf-8"))
lc["sources"]["insurtech"]["last"] = now_iso
json.dump(lc, open(lc_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"last-check.json insurtech.last -> {now_iso}")
