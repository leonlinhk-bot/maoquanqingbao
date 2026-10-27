#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 3 verified-increment items (InsuranceAsia News, 2026-10-27) into live-items.json."""
import json, datetime, os, sys

BASE = '/Users/leonliang/maoquanqingbao'
NOW = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()

items = [
{
 "id": "ian-moodys-apac-repricing-20261027",
 "clusterCount": 1,
 "verifyStatus": "pending",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-27T14:17:57+08:00",
 "originalUrl": "https://insuranceasianews.com/apac-insurers-ability-to-reprice-risks-will-help-preserve-profitability-moodys/",
 "sourceKey": "insuranceasianews",
 "sourceTier": "pro",
 "score": 74,
 "boards": ["market", "reg"],
 "themes": ["重新定价", "气候损失", "资本充足"],
 "title": {
   "sc": "穆迪：亚太险企靠重新定价守住盈利　天气损失占比上升是长期压力",
   "tc": "穆迪：亞太險企靠重新定價守住盈利　天氣損失佔比上升是長期壓力"
 },
 "summary": {
   "sc": "穆迪行业报告指，随保险渗透率逐步上升，亚太险企将吸收更大份额的天气相关损失，但凭重新定价能力仍可保住盈利。报告列监管资本框架、风险筛选、组合分散与先进分析四项为「扩承保而不损资本」的支撑。[EN原文]",
   "tc": "穆迪行業報告指，隨保險滲透率逐步上升，亞太險企將吸收更大份額的天氣相關損失，但憑重新定價能力仍可保住盈利。報告列監管資本框架、風險篩選、組合分散與先進分析四項為「擴承保而不損資本」的支撐。[EN原文]"
 },
 "why": {
   "sc": "这条给的是一个「涨价有依据」的框架：损失占比升、靠重新定价消化，等于告诉客户别把今年没加价当常态。谈续保时讲清定价周期，比事后解释加费更有说服力。",
   "tc": "這條給的是一個「漲價有依據」的框架：損失佔比升、靠重新定價消化，等於告訴客戶別把今年沒加價當常態。談續保時講清定價週期，比事後解釋加費更有說服力。"
 },
 "tags": {
   "sc": ["穆迪", "定价能力", "气候风险", "亚太承保"],
   "tc": ["穆迪", "定價能力", "氣候風險", "亞太承保"]
 },
 "actions": {
   "front": {"sc": "客户沟通：续保加费逻辑", "tc": "客戶溝通：續保加費邏輯"},
   "midback": {"sc": "研究：承保周期与资本", "tc": "研究：承保週期與資本"},
   "lead": {"sc": "团队简报：定价纪律", "tc": "團隊簡報：定價紀律"},
   "cross": {"sc": "跨境企业险定价", "tc": "跨境企業險定價"}
 },
 "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 2},
 "source": {"sc": "InsuranceAsia News 2026-10-27", "tc": "InsuranceAsia News 2026-10-27",
            "name": "insuranceasianews", "date": "2026-10-27", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "穆迪行业报告指，随渗透率上升，亚太险企将吸收更大份额的天气相关损失，但凭重新定价能力仍可守住盈利，并以监管资本框架、风险筛选、组合分散与先进分析支撑扩承保。",
   "tc": "穆迪行業報告指，隨滲透率上升，亞太險企將吸收更大份額的天氣相關損失，但憑重新定價能力仍可守住盈利，並以監管資本框架、風險篩選、組合分散與先進分析支撐擴承保。"
 }
},
{
 "id": "ian-blackrock-captives-third-party-capital-20261027",
 "clusterCount": 1,
 "verifyStatus": "pending",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-27T12:36:20+08:00",
 "originalUrl": "https://insuranceasianews.com/onshore-captives-third-party-capital-primed-for-rapid-growth-in-apac-blackrock/",
 "sourceKey": "insuranceasianews",
 "sourceTier": "pro",
 "score": 72,
 "boards": ["family", "market"],
 "themes": ["专属自保", "第三方资本", "监管资本"],
 "title": {
   "sc": "贝莱德：在岸专属自保与第三方资本　亚太将快速扩张",
   "tc": "貝萊德：在岸專屬自保與第三方資本　亞太將快速擴張"
 },
 "summary": {
   "sc": "贝莱德全球保险策略师 Mike Erickson 指，专属自保再保与第三方资本运用已是亚太险企「首要议题」，背景是区内监管资本制度持续演变。他主张险企整体看资产负债表、资产、负债与有限资本，多用再保释放产能给想增长的产品。[EN原文]",
   "tc": "貝萊德全球保險策略師 Mike Erickson 指，專屬自保再保與第三方資本運用已是亞太險企「首要議題」，背景是區內監管資本制度持續演變。他主張險企整體看資產負債表、資產、負債與有限資本，多用再保釋放產能給想增長的產品。[EN原文]"
 },
 "why": {
   "sc": "高客问「要不要设自保公司」时，别只从省保费答。这条给的资本视角更硬：自保是资本与再保结构安排，用于腾出承保产能。香港正在推专属自保，谈这个话题正当时。",
   "tc": "高客問「要不要設自保公司」時，別只從省保費答。這條給的資本視角更硬：自保是資本與再保結構安排，用於騰出承保產能。香港正在推專屬自保，談這個話題正當時。"
 },
 "tags": {
   "sc": ["专属自保", "第三方资本", "贝莱德", "家办"],
   "tc": ["專屬自保", "第三方資本", "貝萊德", "家辦"]
 },
 "actions": {
   "front": {"sc": "客户沟通：自保的资本逻辑", "tc": "客戶溝通：自保的資本邏輯"},
   "midback": {"sc": "研究：自保与再保结构", "tc": "研究：自保與再保結構"},
   "lead": {"sc": "团队简报：家办风险方案", "tc": "團隊簡報：家辦風險方案"},
   "cross": {"sc": "跨境家族资本安排", "tc": "跨境家族資本安排"}
 },
 "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 3},
 "source": {"sc": "InsuranceAsia News 2026-10-27", "tc": "InsuranceAsia News 2026-10-27",
            "name": "insuranceasianews", "date": "2026-10-27", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "贝莱德全球保险策略师指，专属自保再保与第三方资本运用已是亚太险企首要议题，因区内监管资本制度持续演变；主张多用再保释放产能给想增长的产品。",
   "tc": "貝萊德全球保險策略師指，專屬自保再保與第三方資本運用已是亞太險企首要議題，因區內監管資本制度持續演變；主張多用再保釋放產能給想增長的產品。"
 }
},
{
 "id": "ian-php2shell-cyber-ai-visibility-20261027",
 "clusterCount": 1,
 "verifyStatus": "pending",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-27T07:30:28+08:00",
 "originalUrl": "https://insuranceasianews.com/you-cant-fix-what-you-cant-see-cyber-insurers-warn-php2shell-website-shutdowns-highlight-ai-impact/",
 "sourceKey": "insuranceasianews",
 "sourceTier": "pro",
 "score": 70,
 "boards": ["tech", "market"],
 "themes": ["网络保险", "AI风险", "资产可视性"],
 "title": {
   "sc": "「看不见就修不了」　网络险业者：PHP2Shell 大规模关站是分水岭",
   "tc": "「看不見就修不了」　網絡險業者：PHP2Shell 大規模關站是分水嶺"
 },
 "summary": {
   "sc": "全球数以百万计网站因互联网底层程式码漏洞（PHP2Shell）被关闭，Cowbell、CyberCube 等网络险业者形容事件是分水岭，强调企业「看不见的资产」最难保：资产清点与可视性不足，风险就无从定价与修复，文章并把事件与 AI 影响相提并论。[EN原文]",
   "tc": "全球數以百萬計網站因互聯網底層程式碼漏洞（PHP2Shell）被關閉，Cowbell、CyberCube 等網絡險業者形容事件是分水嶺，強調企業「看不見的資產」最難保：資產清點與可視性不足，風險就無從定價與修復，文章並把事件與 AI 影響相提並論。[EN原文]"
 },
 "why": {
   "sc": "企业客户常以为买了网络险就全覆盖，实际承保前提是资产清单与可见性。这条能当作提问清单的起点：影子 IT、外包系统、网页资产有没有登记，答不上来就是缺口。",
   "tc": "企業客戶常以為買了網絡險就全覆蓋，實際承保前提是資產清單與可見性。這條能當作提問清單的起點：影子 IT、外包系統、網頁資產有沒有登記，答不上來就是缺口。"
 },
 "tags": {
   "sc": ["网络保险", "AI风险", "漏洞", "资产清点"],
   "tc": ["網絡保險", "AI風險", "漏洞", "資產清點"]
 },
 "actions": {
   "front": {"sc": "客户沟通：网络险承保前提", "tc": "客戶溝通：網絡險承保前提"},
   "midback": {"sc": "研究：AI 与网络险条款", "tc": "研究：AI 與網絡險條款"},
   "lead": {"sc": "团队培训：企业险提问清单", "tc": "團隊培訓：企業險提問清單"},
   "cross": {"sc": "跨境科技企业保障", "tc": "跨境科技企業保障"}
 },
 "rolesImpact": {"front": 2, "midback": 2, "lead": 3, "cross": 2},
 "source": {"sc": "InsuranceAsia News 2026-10-27", "tc": "InsuranceAsia News 2026-10-27",
            "name": "insuranceasianews", "date": "2026-10-27", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "全球数以百万计网站因底层程式码漏洞 PHP2Shell 被关闭，网络险业者形容为分水岭，强调「看不见的资产」最难保，资产清点与可视性是承保与修复的前提。",
   "tc": "全球數以百萬計網站因底層程式碼漏洞 PHP2Shell 被關閉，網絡險業者形容為分水嶺，強調「看不見的資產」最難保，資產清點與可視性是承保與修復的前提。"
 }
},
]

path = os.path.join(BASE, 'data/live-items.json')
d = json.load(open(path))
existing = {i['originalUrl'].rstrip('/') for i in d['items']} | {i['id'] for i in d['items']}
fresh = [it for it in items if it['originalUrl'].rstrip('/') not in existing and it['id'] not in existing]
print("to insert:", len(fresh), "skipped dupes:", len(items) - len(fresh))
if not fresh:
    sys.exit(0)

d['items'] = fresh + d['items']
d['meta']['itemCount'] = len(d['items'])
d['meta']['generatedAt'] = NOW
json.dump(d, open(path, 'w'), ensure_ascii=False, indent=1)
print("total now:", len(d['items']), "| generatedAt", NOW)

# last-check: all sources -> now
lc_path = os.path.join(BASE, 'data/last-check.json')
lc = json.load(open(lc_path))
lc['lastCheck'] = NOW
for k, v in lc['sources'].items():
    v['last'] = NOW
json.dump(lc, open(lc_path, 'w'), ensure_ascii=False, indent=2)
print("last-check updated:", lc['lastCheck'], "| sources:", len(lc['sources']))
