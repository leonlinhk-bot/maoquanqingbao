#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""每月AI与保险科技落地扫描 2026-10-01：插入 5 条新条目 + 回写 insurtech 信源 last-check。"""
import json, datetime

TZ = datetime.timezone(datetime.timedelta(hours=8))
now_iso = datetime.datetime.now(TZ).strftime("%Y-%m-%dT%H:%M:%S+08:00")

NEW_ITEMS = [
    {
        "id": "prudential-hk-ai-underwriter-20260909",
        "clusterCount": 1,
        "score": 78,
        "verifyStatus": "pending",
        "sourceTier": "insurer",
        "sourceKey": "prudential-hk",
        "title": {
            "sc": "保诚香港全面上线AI核保助手 联手阿里云在销售端实现即时预核保",
            "tc": "保誠香港全面上線AI核保助手 聯手阿里雲在銷售端實現即時預核保"
        },
        "summary": {
            "sc": "保诚香港9月9日全面上线AI Underwriter：与阿里云合作，理财顾问在销售端透过聊天机器人，基于客户财务、医疗、职业与住址画像即时取得初步核保指示（接受／除外／加费／补资料），无需等数天。方案基于阿里通义千问(Qwen)与RAG引擎，准确率超95%、幻觉率低于2%，三个月内完成部署；最终核保决定仍由核保人把关，后续将扩展至银保与经纪渠道。",
            "tc": "保誠香港9月9日全面上線AI Underwriter：與阿里雲合作，理財顧問在銷售端透過聊天機器人，基於客戶財務、醫療、職業與住址畫像即時取得初步核保指示（接受／除外／加費／補資料），無需等數天。方案基於阿里通義千問(Qwen)與RAG引擎，準確率超95%、幻覺率低於2%，三個月內完成部署；最終核保決定仍由核保人把關，後續將擴展至銀保與經紀渠道。"
        },
        "why": {
            "sc": "香港头部寿险把生成式AI推进到销售端即时预核保，是「AI辅助核保」从后台走向前线的标志性落地样本，可作核保流程AI化的对标。",
            "tc": "香港頭部壽險把生成式AI推進到銷售端即時預核保，是「AI輔助核保」從後台走向前線的標誌性落地樣本，可作核保流程AI化的對標。"
        },
        "actions": {
            "front": {"sc": "了解销售端AI预核保工具形态", "tc": "了解銷售端AI預核保工具形態"},
            "midback": {"sc": "核保流程AI化对标", "tc": "核保流程AI化對標"},
            "lead": {"sc": "行业AI落地节奏判断", "tc": "行業AI落地節奏判斷"},
            "cross": {}
        },
        "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 0},
        "source": {"sc": "保诚香港／阿里云", "lang": "zh+en"},
        "boards": ["insurer", "tech"],
        "themes": ["ai", "underwriting", "insurtech"],
        "tags": {
            "sc": ["保诚", "AI核保", "阿里云", "通义千问", "保险科技"],
            "tc": ["保誠", "AI核保", "阿里雲", "通義千問", "保險科技"]
        },
        "contentKind": "press",
        "publishedAt": "2026-09-09",
        "originalUrl": "https://www.alibabacloud.com/en/press-room/prudential-launches-brand-new-ai-underwriter?_p_lc=1",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "outmarket-ai-series-b-20260925",
        "clusterCount": 1,
        "score": 62,
        "verifyStatus": "pending",
        "sourceTier": "media",
        "sourceKey": "prnewswire",
        "title": {
            "sc": "AI保险作业平台Outmarket完成3450万美元B轮 距A轮仅四个月、估值约3.55亿美元",
            "tc": "AI保險作業平台Outmarket完成3450萬美元B輪 距A輪僅四個月、估值約3.55億美元"
        },
        "summary": {
            "sc": "美国AI保险平台Outmarket宣布完成3450万美元B轮融资，由SignalFire领投，Fika Ventures、Permanent Capital Ventures、TTV Capital、Dash Fund跟投；距上一轮1700万美元A轮仅四个月，估值约3.55亿美元，累计融资5650万美元。Outmarket用AI自动化经纪与代理的保单填写、文档审阅与推荐，聚焦商业险，已服务超300家代理机构、超25%全美百大经纪采用。",
            "tc": "美國AI保險平台Outmarket宣布完成3450萬美元B輪融資，由SignalFire領投，Fika Ventures、Permanent Capital Ventures、TTV Capital、Dash Fund跟投；距上一輪1700萬美元A輪僅四個月，估值約3.55億美元，累計融資5650萬美元。Outmarket用AI自動化經紀與代理的保單填寫、文檔審閱與推薦，聚焦商業險，已服務超300家代理機構、超25%全美百大經紀採用。"
        },
        "why": {
            "sc": "保险经纪AI作业层快速拿到大额融资，印证「AI嵌入代理分销基础设施」仍是保险科技最受资本认可的赛道。",
            "tc": "保險經紀AI作業層快速拿到大額融資，印證「AI嵌入代理分銷基礎設施」仍是保險科技最受資本認可的賽道。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "经纪AI工具动向追踪", "tc": "經紀AI工具動向追蹤"},
            "lead": {"sc": "保险科技融资节奏参考", "tc": "保險科技融資節奏參考"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 1, "lead": 2, "cross": 0},
        "source": {"sc": "PR Newswire / TechCrunch", "lang": "en"},
        "boards": ["tech", "market"],
        "themes": ["insurtech", "funding", "ai"],
        "tags": {
            "sc": ["保险科技", "融资", "Outmarket", "AI"],
            "tc": ["保險科技", "融資", "Outmarket", "AI"]
        },
        "contentKind": "news",
        "publishedAt": "2026-09-25",
        "originalUrl": "https://prnewswire.com/news-releases/outmarket-ai-raises-34-5m-series-b-to-solidify-position-as-the-1-ai-platform-for-insurance-302891583.html",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "duckcreek-agentic-fnol-20260928",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "sourceKey": "duck-creek",
        "title": {
            "sc": "Duck Creek发布Agentic FNOL：AI智能体编排首勘通知 实现实时理赔受理",
            "tc": "Duck Creek發布Agentic FNOL：AI智能體編排首勘通知 實現實時理賠受理"
        },
        "summary": {
            "sc": "保险核心系统商Duck Creek 9月28日发布Agentic First Notice of Loss（首勘通知），在其Agentic AI平台之上，以编排式AI智能体在数字、语音转文字、移动端等多渠道完成报案信息采集、校验、丰富与分流，并内置保单核验、早期欺诈与异常检测。方案与Google Cloud合作、基于Gemini模型，全程可追溯、可解释、可审计。Celent调研指22%险企计划2026年底前落地代理式AI。",
            "tc": "保險核心系統商Duck Creek 9月28日發布Agentic First Notice of Loss（首勘通知），在其Agentic AI平台之上，以編排式AI智能體在數字、語音轉文字、移動端等多渠道完成報案信息採集、校驗、豐富與分流，並內置保單核驗、早期欺詐與異常檢測。方案與Google Cloud合作、基於Gemini模型，全程可追溯、可解釋、可審計。Celent調研指22%險企計劃2026年底前落地代理式AI。"
        },
        "why": {
            "sc": "代理式AI进入理赔首勘环节，是「AI智能体替代碎片化人工受理」的典型产品化落地，可作理赔数字化方向参考。",
            "tc": "代理式AI進入理賠首勘環節，是「AI智能體替代碎片化人工受理」的典型產品化落地，可作理賠數位化方向參考。"
        },
        "actions": {
            "front": {"sc": "了解理赔AI受理工具", "tc": "了解理賠AI受理工具"},
            "midback": {"sc": "理赔流程AI化对标", "tc": "理賠流程AI化對標"},
            "lead": {"sc": "代理式AI趋势观察", "tc": "代理式AI趨勢觀察"},
            "cross": {}
        },
        "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 0},
        "source": {"sc": "Duck Creek", "lang": "en"},
        "boards": ["tech", "product"],
        "themes": ["agentic-ai", "claims", "insurtech"],
        "tags": {
            "sc": ["代理式AI", "理赔", "Duck Creek", "Gemini"],
            "tc": ["代理式AI", "理賠", "Duck Creek", "Gemini"]
        },
        "contentKind": "press",
        "publishedAt": "2026-09-28",
        "originalUrl": "https://newswire.ca/news-releases/duck-creek-launches-agentic-fnol-to-transform-claims-intake-with-intelligent-real-time-automation-864718970.html",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "sapiens-aip-platform-20260914",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "sourceKey": "sapiens",
        "title": {
            "sc": "Sapiens发布AI原生自主保险平台SapiensAIP 把代理式AI嵌入核心系统",
            "tc": "Sapiens發布AI原生自主保險平台SapiensAIP 把代理式AI嵌入核心系統"
        },
        "summary": {
            "sc": "保险科技商Sapiens 9月14日发布AI原生自主保险平台SapiensAIP：SaaS方案把代理式AI直接嵌入核心保单管理系统（PAS），覆盖承保、保单、计费、理赔与客户互动全流程。平台分体验、智能、基础三层，基础层基于其40余年行业本体论，让每个AI智能体具备保险推理上下文。首家客户为美国TPA Continental General，正评估其配置与迁移枢纽以加速业务上线。",
            "tc": "保險科技商Sapiens 9月14日發布AI原生自主保險平台SapiensAIP：SaaS方案把代理式AI直接嵌入核心保單管理系統（PAS），覆蓋承保、保單、計費、理賠與客戶互動全流程。平台分體驗、智能、基礎三層，基礎層基於其40餘年行業本體論，讓每個AI智能體具備保險推理上下文。首家客戶為美國TPA Continental General，正評估其配置與遷移樞紐以加速業務上線。"
        },
        "why": {
            "sc": "「AI原生核心系统」路线把代理式AI从外挂插件转为系统内建能力，是判断保险核心系统下一代形态的关键信号。",
            "tc": "「AI原生核心系統」路線把代理式AI從外掛插件轉為系統內建能力，是判斷保險核心系統下一代形態的關鍵信號。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "核心系统AI化方向参考", "tc": "核心系統AI化方向參考"},
            "lead": {"sc": "保险科技平台演进观察", "tc": "保險科技平台演進觀察"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 0},
        "source": {"sc": "Sapiens", "lang": "en"},
        "boards": ["tech"],
        "themes": ["agentic-ai", "insurtech", "platform"],
        "tags": {
            "sc": ["代理式AI", "核心系统", "Sapiens", "保险科技"],
            "tc": ["代理式AI", "核心系統", "Sapiens", "保險科技"]
        },
        "contentKind": "press",
        "publishedAt": "2026-09-14",
        "originalUrl": "https://sapiens.com/newsroom/sapiens-announces-its-ai-native-autonomous-insurance-platform-sapiensaip",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "axa-genai-sandbox-first-batch-20260902",
        "clusterCount": 1,
        "score": 76,
        "verifyStatus": "pending",
        "sourceTier": "insurer",
        "sourceKey": "axa-hk",
        "title": {
            "sc": "安盛香港入选GenA.I.沙盒++首批 以AI治理与网络韧性用例测试负责任AI",
            "tc": "安盛香港入選GenA.I.沙盒++首批 以AI治理與網絡韌性用例測試負責任AI"
        },
        "summary": {
            "sc": "安盛香港及澳门入选香港GenA.I.沙盒++首批参与者，将借助数码港AI超算中心，开发并测试聚焦「AI治理、网络韧性与风险缓释」的专项用例：强化企业风险缓释与AI治理，并提升客户与分销伙伴信任。行政总裁Sally Wan称此认可印证其科技领导力与负责任AI承诺；安盛亦为保监局AI促进计划首批核心参与保司。",
            "tc": "安盛香港及澳門入選香港GenA.I.沙盒++首批參與者，將借助數碼港AI超算中心，開發並測試聚焦「AI治理、網絡韌性與風險緩釋」的專項用例：強化企業風險緩釋與AI治理，並提升客戶與分銷夥伴信任。行政總裁Sally Wan稱此認可印證其科技領導力與負責任AI承諾；安盛亦為保監局AI促進計劃首批核心參與保司。"
        },
        "why": {
            "sc": "保司在监管沙盒中测试AI治理与网络韧性，标志保险业AI合规从「原则」走向「受控环境实测」，是港险AI监管落地的关键样本。",
            "tc": "保司在監管沙盒中測試AI治理與網絡韌性，標誌保險業AI合規從「原則」走向「受控環境實測」，是港險AI監管落地的關鍵樣本。"
        },
        "actions": {
            "front": {},
            "midback": {"sc": "关注沙盒AI治理用例标准", "tc": "關注沙盒AI治理用例標準"},
            "lead": {"sc": "保险AI合规框架研判", "tc": "保險AI合規框架研判"},
            "cross": {}
        },
        "rolesImpact": {"front": 0, "midback": 3, "lead": 3, "cross": 1},
        "source": {"sc": "安盛香港及澳门（AXA）", "lang": "zh+en"},
        "boards": ["reg", "tech"],
        "themes": ["ai-governance", "sandbox", "insurtech"],
        "tags": {
            "sc": ["安盛", "GenA.I.沙盒", "AI治理", "网络韧性", "保监局"],
            "tc": ["安盛", "GenA.I.沙盒", "AI治理", "網絡韌性", "保監局"]
        },
        "contentKind": "press",
        "publishedAt": "2026-09-02",
        "originalUrl": "https://insurtecheye.com/news/axa-selected-among-first-batch-for-gena-i-sandbox-pioneering-a-dedicated-risk-mi-bd8f936e",
        "ingestedAt": now_iso,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
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
    "sc": f"本库{len(data['items'])}条。含10月1日月度AI与保险科技扫描+{len(added)}条。",
    "tc": f"本庫{len(data['items'])}條。含10月1日月度AI與保險科技掃描+{len(added)}條。"
}
json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"INSERTED {len(added)} items; total now {len(data['items'])}")
for a in added:
    print(" +", a)

# --- 2. last-check.json (更新 insurtech 信源检查时间 + 全局 lastCheck) ---
lc_path = "data/last-check.json"
lc = json.load(open(lc_path, encoding="utf-8"))
lc["sources"]["insurtech"]["last"] = now_iso
lc["lastCheck"] = now_iso
json.dump(lc, open(lc_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"last-check.json insurtech.last -> {now_iso}")
