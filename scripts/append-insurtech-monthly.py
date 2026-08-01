#!/usr/bin/env python3
"""Append monthly AI & InsurTech scan items to live-items.json"""
import json
import sys
from datetime import datetime

NEW_ITEMS = [
    {
        "id": "pcpd-ai-sandbox-jul06",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "pending",
        "sourceTier": "official",
        "sourceKey": "pcpd-dpo",
        "title": {
            "sc": "香港私隐公署与数字办联合推出「保障个人资料AI沙盒」",
            "tc": "香港私隱公署與數字辦聯合推出「保障個人資料AI沙盒」"
        },
        "summary": {
            "sc": "2026年7月6日，个人资料私隐专员公署(PCPD)与数字政策办公室(DPO)联合推出「保障个人资料AI沙盒」，旨在积极对接国家十五五规划「发展与安全并重」方针，为AI技术在港应用提供个人资料保障测试环境。保险业作为高度依赖个人数据的行业，此沙盒为AI核保、理赔等场景提供合规路径。[EN原文]",
            "tc": "私隱公署與數字辦聯合推出「保障個人資料AI沙盒」，為AI在保險核保理賠等場景提供個人資料保障合規測試環境。[EN原文]"
        },
        "why": {
            "sc": "AI+隐私合规=保险科技落地的关键门槛，沙盒提供可控测试环境",
            "tc": "AI+私隱合規=保險科技落地的關鍵門檻，沙盒提供可控測試環境"
        },
        "actions": {
            "front": {},
            "midback": {
                "sc": "关注沙盒具体标准，评估AI核保理赔工具的合规路径",
                "tc": "關注沙盒具體標準，評估AI核保理賠工具的合規路徑"
            },
            "lead": {
                "sc": "AI隐私合规需纳入保险科技投资决策框架",
                "tc": "AI私隱合規需納入保險科技投資決策框架"
            },
            "cross": {}
        },
        "rolesImpact": {
            "front": 1,
            "midback": 3,
            "lead": 3,
            "cross": 0
        },
        "source": {
            "sc": "香港政府资讯中心",
            "lang": "zh+en"
        },
        "boards": ["reg", "tech"],
        "themes": ["AI", "privacy", "sandbox"],
        "tags": {
            "sc": ["AI沙盒", "个人资料保障", "PCPD", "DPO", "保险科技"],
            "tc": ["AI沙盒", "個人資料保障", "PCPD", "DPO", "保險科技"]
        },
        "contentKind": "press",
        "publishedAt": "2026-07-06T00:00:00+08:00",
        "originalUrl": "https://www.info.gov.hk/gia/general/202607/06/P2026070300679.htm",
        "ingestedAt": "2026-08-01T12:00:00+08:00",
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "genai-sandbox-plus-jul17",
        "clusterCount": 1,
        "score": 88,
        "verifyStatus": "pending",
        "sourceTier": "official",
        "sourceKey": "hkma-sfc-ia-mpfa",
        "title": {
            "sc": "GenA.I.沙盒++正式扩展至保险等多元金融领域",
            "tc": "GenA.I.沙盒++正式擴展至保險等多元金融領域"
        },
        "summary": {
            "sc": "2026年7月中旬，金管局联合证监会、保监局、积金局及数码港宣布推出「生成式人工智能沙盒++」，在2024年首版基础上将覆盖范围从银行业扩展至证券、资管、保险、强积金及储值支付工具。聚焦风险管理、反诈骗和客户体验三大场景，持续推进「以AI对抗AI」策略。参与机构可获得监管指引、技术支援及数码港超算中心GPU资源。[EN原文]",
            "tc": "金管局聯同證監會、保監局、積金局及數碼港推出GenA.I.沙盒++，覆蓋保險等多元金融領域，聚焦風險管理、反詐騙和客戶體驗。[EN原文]"
        },
        "why": {
            "sc": "GenA.I.沙盒扩展至保险=监管正式为保险业GenAI应用打开合规通道",
            "tc": "GenA.I.沙盒擴展至保險=監管正式為保險業GenAI應用打開合規通道"
        },
        "actions": {
            "front": {
                "sc": "关注沙盒中保险相关用例，评估GenAI在客户服务的合规应用",
                "tc": "關注沙盒中保險相關用例，評估GenAI在客戶服務的合規應用"
            },
            "midback": {
                "sc": "GenAI在反欺诈和风险管理场景的沙盒测试=优先级高",
                "tc": "GenAI在反欺詐和風險管理場景的沙盒測試=優先級高"
            },
            "lead": {
                "sc": "保险业GenAI合规框架渐清晰，应尽早评估内部用例",
                "tc": "保險業GenAI合規框架漸清晰，應盡早評估內部用例"
            },
            "cross": {}
        },
        "rolesImpact": {
            "front": 2,
            "midback": 4,
            "lead": 4,
            "cross": 1
        },
        "source": {
            "sc": "金管局/保监局/证监会联合发布",
            "lang": "zh+en"
        },
        "boards": ["reg", "tech"],
        "themes": ["GenAI", "sandbox", "insurtech"],
        "tags": {
            "sc": ["GenAI沙盒", "保监局", "金管局", "数码港", "保险科技"],
            "tc": ["GenAI沙盒", "保監局", "金管局", "數碼港", "保險科技"]
        },
        "contentKind": "press",
        "publishedAt": "2026-07-17T00:00:00+08:00",
        "originalUrl": "https://m.tech.china.com/redian/2026/0717/072026_1919989.html",
        "ingestedAt": "2026-08-01T12:00:00+08:00",
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "insurtech-funding-q1-2026",
        "clusterCount": 1,
        "score": 72,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "sourceKey": "fintechly",
        "title": {
            "sc": "全球InsurTech融资回暖：Q1融资16.3亿美元，资金流向AI基础设施",
            "tc": "全球InsurTech融資回暖：Q1融資16.3億美元，資金流向AI基礎設施"
        },
        "summary": {
            "sc": "Fintechly 2026年7月报道：全球InsurTech融资在Q1 2026达16.3亿美元，为2022年底以来最强背靠背季度之一。AI-focused InsurTechs捕获大部分资金，但最强投资逻辑转向「保险公司可嵌入的基础设施」而非「颠覆性玩法」。传统保险公司成为主要买家。[EN原文]",
            "tc": "全球InsurTech Q1融資16.3億美元，AI-focused InsurTechs捕獲大部分資金，投資邏輯從顛覆轉向基礎設施。[EN原文]"
        },
        "why": {
            "sc": "InsurTech融资回暖+AI基础设施转向=保险科技进入务实落地期",
            "tc": "InsurTech融資回暖+AI基礎設施轉向=保險科技進入務實落地期"
        },
        "actions": {
            "front": {},
            "midback": {
                "sc": "关注AI基础设施类InsurTech解决方案的采购评估",
                "tc": "關注AI基礎設施類InsurTech解決方案的採購評估"
            },
            "lead": {
                "sc": "融资回暖信号=保险科技投资窗口正在打开",
                "tc": "融資回暖信號=保險科技投資窗口正在打開"
            },
            "cross": {}
        },
        "rolesImpact": {
            "front": 0,
            "midback": 2,
            "lead": 3,
            "cross": 0
        },
        "source": {
            "sc": "Fintechly",
            "lang": "zh+en"
        },
        "boards": ["market", "tech"],
        "themes": ["insurtech", "funding", "AI"],
        "tags": {
            "sc": ["InsurTech", "融资", "AI基础设施", "Q1 2026"],
            "tc": ["InsurTech", "融資", "AI基礎設施", "Q1 2026"]
        },
        "contentKind": "news",
        "publishedAt": "2026-07-14T06:38:00+08:00",
        "originalUrl": "https://fintechly.com/capital/insurtech-funding-is-back-the-money-is-buying-infrastructure-not-disruption/",
        "ingestedAt": "2026-08-01T12:00:00+08:00",
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "agentic-ai-insurance-jul14",
        "clusterCount": 1,
        "score": 70,
        "verifyStatus": "pending",
        "sourceTier": "pro",
        "sourceKey": "arxiv",
        "title": {
            "sc": "学术前沿：Agentic AI时代的保险承保、定价与端到端自动化框架",
            "tc": "學術前沿：Agentic AI時代的保險承保、定價與端到端自動化框架"
        },
        "summary": {
            "sc": "arXiv 2026年7月论文《AI-Native Insurance for Agentic AI》提出Agentic AI时代保险新范式：保险覆盖对象从被动数字资产转向能推理、调用工具、改变外部状态的操作型AI代理。论文开发了针对网络攻击、自主决策失误、模型漂移、依赖中断、专业疏忽、监管违规及网络物理伤害等新风险的原生AI承保与定价框架。[EN原文]",
            "tc": "arXiv論文探討Agentic AI時代保險新範式，開發針對自主AI代理失誤、模型漂移等新風險的原生AI承保定價框架。[EN原文]"
        },
        "why": {
            "sc": "Agentic AI保险是前沿领域，预示保险产品形态的下一阶段演化",
            "tc": "Agentic AI保險是前沿領域，預示保險產品形態的下一階段演化"
        },
        "actions": {
            "front": {},
            "midback": {
                "sc": "了解Agentic AI风险分类，为未来产品开发储备知识",
                "tc": "了解Agentic AI風險分類，為未來產品開發儲備知識"
            },
            "lead": {
                "sc": "Agentic AI保险=保险产品创新的前沿方向",
                "tc": "Agentic AI保險=保險產品創新的前沿方向"
            },
            "cross": {}
        },
        "rolesImpact": {
            "front": 0,
            "midback": 2,
            "lead": 2,
            "cross": 0
        },
        "source": {
            "sc": "arXiv",
            "lang": "zh+en"
        },
        "boards": ["tech"],
        "themes": ["agentic-ai", "underwriting", "research"],
        "tags": {
            "sc": ["Agentic AI", "保险科技", "承保框架", "学术论文"],
            "tc": ["Agentic AI", "保險科技", "承保框架", "學術論文"]
        },
        "contentKind": "news",
        "publishedAt": "2026-07-14T08:00:00+08:00",
        "originalUrl": "https://arxiv.org/pdf/2607.13230",
        "ingestedAt": "2026-08-01T12:00:00+08:00",
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    },
    {
        "id": "cyber-mapping-circular-jul29",
        "clusterCount": 1,
        "score": 85,
        "verifyStatus": "pending",
        "sourceTier": "official",
        "sourceKey": "hkma-sfc-ia-mpfa",
        "title": {
            "sc": "金管局证监保监积金局联合发布跨行业网络安全测绘通函",
            "tc": "金管局證監保監積金局聯合發布跨行業網絡安全測繪通函"
        },
        "summary": {
            "sc": "2026年7月29日，金管局、证监会、保监局及积金局联合发布跨行业网络安全测绘通函，要求所有认可机构、持牌法团、授权保险公司及强积金核准受托人参与。此举旨在系统性评估全金融行业网络安全态势，为后续网络韧性监管提供数据基础。[EN原文]",
            "tc": "四大監管機構聯合發布跨行業網絡安全測繪通函，要求所有認可機構及授權保險公司參與，系統評估全行業網絡安全態勢。[EN原文]"
        },
        "why": {
            "sc": "跨行业网络安全测绘=保险业网络安全监管从机构自律走向行业协同",
            "tc": "跨行業網絡安全測繪=保險業網絡安全監管從機構自律走向行業協同"
        },
        "actions": {
            "front": {},
            "midback": {
                "sc": "IT安全团队需配合网络安全测绘自查与数据提交",
                "tc": "IT安全團隊需配合網絡安全測繪自查與數據提交"
            },
            "lead": {
                "sc": "网络安全合规投入在保险科技预算中的优先级应提高",
                "tc": "網絡安全合規投入在保險科技預算中的優先級應提高"
            },
            "cross": {}
        },
        "rolesImpact": {
            "front": 0,
            "midback": 4,
            "lead": 3,
            "cross": 0
        },
        "source": {
            "sc": "证监会联合通函",
            "lang": "zh+en"
        },
        "boards": ["reg", "tech"],
        "themes": ["cybersecurity", "IA", "HKMA"],
        "tags": {
            "sc": ["网络安全", "联合通函", "保监局", "金管局", "证监会"],
            "tc": ["網絡安全", "聯合通函", "保監局", "金管局", "證監會"]
        },
        "contentKind": "circular",
        "publishedAt": "2026-07-29T09:04:00+08:00",
        "originalUrl": "https://apps.sfc.hk/edistributionWeb/gateway/EN/circular/intermediaries/supervision/doc?refNo=26EC45",
        "ingestedAt": "2026-08-01T12:00:00+08:00",
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False
    }
]

# Read existing data
with open('data/live-items.json', 'r') as f:
    data = json.load(f)

# Append new items
data['items'].extend(NEW_ITEMS)

# Update meta
new_count = len(data['items'])
data['meta']['itemCount'] = new_count
data['meta']['generatedAt'] = '2026-08-01T12:00:00+08:00'
data['meta']['windowNote'] = {
    "sc": f"本库{new_count}条。含8月1日月度AI与保险科技扫描+5条。",
    "tc": f"本庫{new_count}條。含8月1日月度AI與保險科技掃描+5條。"
}

# Write back
with open('data/live-items.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Update last-check.json for insurtech source
with open('data/last-check.json', 'r') as f:
    check_data = json.load(f)

check_data['sources']['insurtech']['last'] = '2026-08-01T12:00:00+08:00'
check_data['lastCheck'] = '2026-08-01T12:00:00+08:00'

with open('data/last-check.json', 'w') as f:
    json.dump(check_data, f, ensure_ascii=False, indent=2)

print(f"Done. Items: {len(data['items'])}. Added {len(NEW_ITEMS)} new items.")
for item in NEW_ITEMS:
    print(f"  + {item['id']}")
