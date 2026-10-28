#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-28 增量条目 into live-items.json (7 条，均已核原文)."""
import json, datetime, os, sys

BASE = '/Users/leonliang/maoquanqingbao'
NOW = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()

items = [
{
 "id": "ia-hk-q2-premium-boom-jefferies-20261028",
 "clusterCount": 1,
 "verifyStatus": "verified",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-28T05:30:00+08:00",
 "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-insurers-see-premium-boom-without-new-policy-growth",
 "sourceKey": "insuranceasia",
 "sourceTier": "media",
 "score": 72,
 "boards": ["market", "insurer"],
 "themes": ["保费增长", "分销渠道", "经纪占比"],
 "title": {
   "sc": "Jefferies：香港次季寿险保费升89%　新单件数反跌6%",
   "tc": "Jefferies：香港次季壽險保費升89%　新單件數反跌6%"
 },
 "summary": {
   "sc": "Jefferies 10月27日报告：香港寿险次季保费同比升89%，代理+40%、银行+102%、经纪+119%，但全市场新单件数跌6%、单均保费升101%。汇丰银行渠道升179%、宏利银行渠道升236%；经纪已是宏利与富卫最大渠道。[EN原文]",
   "tc": "Jefferies 10月27日報告：香港壽險次季保費同比升89%，代理+40%、銀行+102%、經紀+119%，但全市場新單件數跌6%、單均保費升101%。匯豐銀行渠道升179%、宏利銀行渠道升236%；經紀已是宏利與富衛最大渠道。[EN原文]"
 },
 "why": {
   "sc": "这条点明「客户不买多，但买大」：件数跌、单均保费翻倍，成交靠大单不靠单量。谈客时力气应放在保额与结构，而不是追件数；经纪渠道跑赢代理与银行，也说明专业中介份额在扩大。",
   "tc": "這條點明「客戶不買多，但買大」：件數跌、單均保費翻倍，成交靠大單不靠單量。談客時力氣應放在保額與結構，而不是追件數；經紀渠道跑贏代理與銀行，也說明專業中介份額在擴大。"
 },
 "tags": {"sc": ["香港市场", "保费结构", "分销渠道", "Jefferies"],
          "tc": ["香港市場", "保費結構", "分銷渠道", "Jefferies"]},
 "actions": {
   "front": {"sc": "客户沟通：保额与结构优先", "tc": "客戶溝通：保額與結構優先"},
   "midback": {"sc": "研究：渠道结构变化", "tc": "研究：渠道結構變化"},
   "lead": {"sc": "团队简报：渠道产能", "tc": "團隊簡報：渠道產能"},
   "cross": {"sc": "跨境客户资产搬家", "tc": "跨境客戶資產搬家"}
 },
 "rolesImpact": {"front": 3, "midback": 3, "lead": 2, "cross": 2},
 "source": {"sc": "Insurance Asia 2026-10-28", "tc": "Insurance Asia 2026-10-28",
            "name": "insuranceasia", "date": "2026-10-28", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "Jefferies 报告指香港寿险次季保费同比升89%，代理、银行、经纪三渠道齐升，但新单件数跌6%，单均保费升101%，反映增长来自单笔规模而非件数。",
   "tc": "Jefferies 報告指香港壽險次季保費同比升89%，代理、銀行、經紀三渠道齊升，但新單件數跌6%，單均保費升101%，反映增長來自單筆規模而非件數。"
 }
},
{
 "id": "ia-hk-insurance-hub-ai-terms-20261028",
 "clusterCount": 1,
 "verifyStatus": "verified",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-28T05:45:00+08:00",
 "originalUrl": "https://insuranceasia.com/insurance/news/insurance-information-platform-deploys-ai-decode-complex-policy-terms",
 "sourceKey": "insuranceasia",
 "sourceTier": "media",
 "score": 70,
 "boards": ["tech", "product"],
 "themes": ["AI解读", "条款透明", "消费者教育"],
 "title": {
   "sc": "香港保险资讯平台用 AI 拆解保单条款　专攻不保事项与理赔条件",
   "tc": "香港保險資訊平台用 AI 拆解保單條款　專攻不保事項與理賠條件"
 },
 "summary": {
   "sc": "香港保险资讯平台 HK Insurance Hub 推出 AI 内容优化，用大数据与生成式 AI 把冗长条款重组为易懂解释，覆盖自愿医保（VHIS）、寿险、重疾与一般保险，重点挑出消费者易忽略的不保事项、理赔条件与保障上限。[EN原文]",
   "tc": "香港保險資訊平台 HK Insurance Hub 推出 AI 內容優化，用大數據與生成式 AI 把冗長條款重組為易懂解釋，覆蓋自願醫保（VHIS）、壽險、重疾與一般保險，重點挑出消費者易忽略的不保事項、理賠條件與保障上限。[EN原文]"
 },
 "why": {
   "sc": "客户看不懂条款，是「买错」与「理赔落差」的源头。平台把不保事项单独挑出来讲，等于替前线做了预教育：谈单前请客户先看这类解释，再逐条对回自己那张保单，比事后解释争议省力得多。",
   "tc": "客戶看不懂條款，是「買錯」與「理賠落差」的源頭。平台把不保事項單獨挑出來講，等於替前線做了預教育：談單前請客戶先看這類解釋，再逐條對回自己那張保單，比事後解釋爭議省力得多。"
 },
 "tags": {"sc": ["AI应用", "保单条款", "消费者教育", "VHIS"],
          "tc": ["AI應用", "保單條款", "消費者教育", "VHIS"]},
 "actions": {
   "front": {"sc": "客户沟通：条款预教育", "tc": "客戶溝通：條款預教育"},
   "midback": {"sc": "研究：AI 条款解释工具", "tc": "研究：AI 條款解釋工具"},
   "lead": {"sc": "团队培训：不保事项清单", "tc": "團隊培訓：不保事項清單"},
   "cross": {"sc": "跨境客户跨境保单解读", "tc": "跨境客戶跨境保單解讀"}
 },
 "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 1},
 "source": {"sc": "Insurance Asia 2026-10-28", "tc": "Insurance Asia 2026-10-28",
            "name": "insuranceasia", "date": "2026-10-28", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "香港保险资讯平台 HK Insurance Hub 以大数据和生成式 AI 重组保单条款，覆盖 VHIS、寿险、重疾与一般保险，重点提示不保事项、理赔条件与保障上限。",
   "tc": "香港保險資訊平台 HK Insurance Hub 以大數據和生成式 AI 重組保單條款，覆蓋 VHIS、壽險、重疾與一般保險，重點提示不保事項、理賠條件與保障上限。"
 }
},
{
 "id": "ibm-korea-fsc-blocks-ai-jv-20261028",
 "clusterCount": 1,
 "verifyStatus": "verified",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-28T00:56:00+08:00",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/south-korean-regulator-blocks-insurance-bodys-ai-venture-595139.aspx",
 "sourceKey": "ibm",
 "sourceTier": "media",
 "score": 70,
 "boards": ["reg", "tech"],
 "themes": ["AI治理", "监管边界", "机构投资"],
 "title": {
   "sc": "韩国金委会否决保险研修院投资 AI 合资公司　以「业务范围」划红线",
   "tc": "韓國金委會否決保險研修院投資 AI 合資公司　以「業務範圍」劃紅線"
 },
 "summary": {
   "sc": "韩国金融委员会（FSC）10月2日经监管民愿平台答复：依《保险业法》第178条第3款，保险研修院业务限于培训与教育，无论设子公司或合资入股，投资营利性 AI 公司均超业务范围，项目不得推进。此前6月FSC已定金融业AI决策须由人负责。[EN原文]",
   "tc": "韓國金融委員會（FSC）10月2日經監管民願平台答覆：依《保險業法》第178條第3款，保險研修院業務限於培訓與教育，無論設子公司或合資入股，投資營利性 AI 公司均超業務範圍，項目不得推進。此前6月FSC已定金融業AI決策須由人負責。[EN原文]"
 },
 "why": {
   "sc": "监管对「机构能不能投 AI」给出硬边界：非营利的行业机构不能用合资公司做 AI。判断「保险机构＋科技公司」的合作结构时，先看主体资质与业务范围，别先谈技术能力——顺序错了，方案再漂亮也过不了。",
   "tc": "監管對「機構能不能投 AI」給出硬邊界：非營利的行業機構不能用合資公司做 AI。判斷「保險機構＋科技公司」的合作結構時，先看主體資質與業務範圍，別先談技術能力——順序錯了，方案再漂亮也過不了。"
 },
 "tags": {"sc": ["韩国监管", "AI治理", "业务范围", "合资"],
          "tc": ["韓國監管", "AI治理", "業務範圍", "合資"]},
 "actions": {
   "front": {"sc": "客户沟通：AI 合作的资质前提", "tc": "客戶溝通：AI 合作的資質前提"},
   "midback": {"sc": "研究：AI 治理与问责", "tc": "研究：AI 治理與問責"},
   "lead": {"sc": "团队简报：监管对AI的态度", "tc": "團隊簡報：監管對AI的態度"},
   "cross": {"sc": "跨境科技合作结构", "tc": "跨境科技合作結構"}
 },
 "rolesImpact": {"front": 1, "midback": 3, "lead": 2, "cross": 2},
 "source": {"sc": "Insurance Business Asia 2026-10-28", "tc": "Insurance Business Asia 2026-10-28",
            "name": "ibm", "date": "2026-10-28", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "韩国金融委员会裁定保险研修院入股营利性 AI 合资公司超出《保险业法》业务范围，项目不得推进，是监管首次以业务界限叫停保险机构 AI 投资。",
   "tc": "韓國金融委員會裁定保險研修院入股營利性 AI 合資公司超出《保險業法》業務範圍，項目不得推進，是監管首次以業務界限叫停保險機構 AI 投資。"
 }
},
{
 "id": "ibm-india-commission-caps-20261027",
 "clusterCount": 1,
 "verifyStatus": "verified",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-27T23:59:00+08:00",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/indian-brokers-face-6070-revenue-hit-under-proposed-commission-caps-595134.aspx",
 "sourceKey": "ibm",
 "sourceTier": "media",
 "score": 72,
 "boards": ["reg", "market"],
 "themes": ["佣金监管", "分销成本", "中介生存"],
 "title": {
   "sc": "印度拟恢复佣金上限　中介收入或降六至七成，咨询期延至10月31日",
   "tc": "印度擬恢復佣金上限　中介收入或降六至七成，諮詢期延至10月31日"
 },
 "summary": {
   "sc": "印度 IRDAI 9月23日发布《重新校准保险分销经济学》咨询文件，拟恢复2023年取消的硬性佣金上限：寿险首年中介5%-20%、代理6.25%-25%，健康险新单约15%、续保5%，车险强制三者险零佣金。已收650多份意见，截止延至10月31日。[EN原文]",
   "tc": "印度 IRDAI 9月23日發布《重新校準保險分銷經濟學》諮詢文件，擬恢復2023年取消的硬性佣金上限：壽險首年中介5%-20%、代理6.25%-25%，健康險新單約15%、續保5%，車險強制三者險零佣金。已收650多份意見，截止延至10月31日。[EN原文]"
 },
 "why": {
   "sc": "这是「分销经济学」被重新定价的样板：印度用数据指佣金增速远超保费——2022-23 至 2024-25 寿险企业代理给付升125%、保费仅升28%。香港虽未动佣金，但客户与监管都在问「这笔钱花在哪」，提前把价值主张讲清楚，比事后辩护有用。",
   "tc": "這是「分銷經濟學」被重新定價的樣板：印度用數據指佣金增速遠超保費——2022-23 至 2024-25 壽險企業代理給付升125%、保費僅升28%。香港雖未動佣金，但客戶與監管都在問「這筆錢花在哪」，提前把價值主張講清楚，比事後辯護有用。"
 },
 "tags": {"sc": ["印度监管", "佣金上限", "中介经济学", "IRDAI"],
          "tc": ["印度監管", "佣金上限", "中介經濟學", "IRDAI"]},
 "actions": {
   "front": {"sc": "客户沟通：顾问价值怎么讲", "tc": "客戶溝通：顧問價值怎麼講"},
   "midback": {"sc": "研究：分销成本与监管", "tc": "研究：分銷成本與監管"},
   "lead": {"sc": "团队简报：中介生存模式", "tc": "團隊簡報：中介生存模式"},
   "cross": {"sc": "跨境同业监管比较", "tc": "跨境同業監管比較"}
 },
 "rolesImpact": {"front": 2, "midback": 3, "lead": 3, "cross": 1},
 "source": {"sc": "Insurance Business Asia 2026-10-27", "tc": "Insurance Business Asia 2026-10-27",
            "name": "ibm", "date": "2026-10-27", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "印度 IRDAI 拟恢复硬性佣金上限，中介收入或降六至七成；官方数据显示分销成本增速远超保费，2022-23 至 2024-25 寿险企业代理给付升125%、保费仅升28%。",
   "tc": "印度 IRDAI 擬恢復硬性佣金上限，中介收入或降六至七成；官方數據顯示分銷成本增速遠超保費，2022-23 至 2024-25 壽險企業代理給付升125%、保費僅升28%。"
 }
},
{
 "id": "rn-eu-climate-resilience-insurance-alliance-20261028",
 "clusterCount": 1,
 "verifyStatus": "verified",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-28T01:00:00+08:00",
 "originalUrl": "https://www.reinsurancene.ws/eu-unveils-climate-resilience-framework-with-re-insurance-protection-gap-in-focus/",
 "sourceKey": "reinsurancenews",
 "sourceTier": "pro",
 "score": 70,
 "boards": ["market", "reg"],
 "themes": ["气候韧性", "保障缺口", "巨灾债券"],
 "title": {
   "sc": "欧盟推气候韧性框架　设气候保险联盟补天灾保障缺口",
   "tc": "歐盟推氣候韌性框架　設氣候保險聯盟補天災保障缺口"
 },
 "summary": {
   "sc": "欧盟委员会提出气候韧性框架及《气候韧性法》，估算每年需700亿欧元适应投资，并设「气候保险联盟」收窄天灾保障缺口：欧盟历史上约25%天灾损失有保险。联盟将着力提高投保率、奖励防灾、评估再保与巨灾债券容量，2027年底前交首批措施。[EN原文]",
   "tc": "歐盟委員會提出氣候韌性框架及《氣候韌性法》，估算每年需700億歐元適應投資，並設「氣候保險聯盟」收窄天災保障缺口：歐盟歷史上約25%天災損失有保險。聯盟將著力提高投保率、獎勵防災、評估再保與巨災債券容量，2027年底前交首批措施。[EN原文]"
 },
 "why": {
   "sc": "官方把「保障缺口」写进法律框架，等于承认单靠商业保险补不上天灾。跟高客谈巨灾与气候风险时，这条给的是政策趋势而非产品话术：先讲缺口有多大，再回头看自有保障够不够。",
   "tc": "官方把「保障缺口」寫進法律框架，等於承認單靠商業保險補不上天災。跟高客談巨災與氣候風險時，這條給的是政策趨勢而非產品話術：先講缺口有多大，再回頭看自有保障夠不夠。"
 },
 "tags": {"sc": ["欧盟", "气候风险", "保障缺口", "巨灾债券"],
          "tc": ["歐盟", "氣候風險", "保障缺口", "巨災債券"]},
 "actions": {
   "front": {"sc": "客户沟通：巨灾缺口有多大", "tc": "客戶溝通：巨災缺口有多大"},
   "midback": {"sc": "研究：气候政策与再保容量", "tc": "研究：氣候政策與再保容量"},
   "lead": {"sc": "团队简报：气候风险叙事", "tc": "團隊簡報：氣候風險敘事"},
   "cross": {"sc": "跨境资产巨灾暴露", "tc": "跨境資產巨災暴露"}
 },
 "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 2},
 "source": {"sc": "Reinsurance News 2026-10-27", "tc": "Reinsurance News 2026-10-27",
            "name": "reinsurancenews", "date": "2026-10-27", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "欧盟委员会提出气候韧性框架与《气候韧性法》，估算每年需700亿欧元适应投资，并设气候保险联盟补缺口——欧盟仅约25%天灾损失有保险，首批措施2027年底交。",
   "tc": "歐盟委員會提出氣候韌性框架與《氣候韌性法》，估算每年需700億歐元適應投資，並設氣候保險聯盟補缺口——歐盟僅約25%天災損失有保險，首批措施2027年底交。"
 }
},
{
 "id": "scmp-former-csrc-official-bribery-sentence-20261027",
 "clusterCount": 1,
 "verifyStatus": "verified",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-27T21:35:00+08:00",
 "originalUrl": "https://www.scmp.com/business/banking-finance/article/3372339/china-hands-former-regulator-suspended-death-sentence-over-us65m-bribery-charge",
 "sourceKey": "scmp",
 "sourceTier": "media",
 "score": 62,
 "boards": ["reg"],
 "themes": ["廉政风险", "监管治理", "金融反腐"],
 "title": {
   "sc": "受贿约6,500万美元　前中证监官员王惠民被判死缓",
   "tc": "受賄約6,500萬美元　前中證監官員王惠民被判死緩"
 },
 "summary": {
   "sc": "前中国证监会高级官员王惠民10月27日在成都被判受贿罪成，判处死刑、缓期两年执行。报道指涉案贿款约6,500万美元，是北京金融领域反腐行动的又一要案；判决未披露更多案情细节。[EN原文]",
   "tc": "前中國證監會高級官員王惠民10月27日在成都被判受賄罪成，判處死刑、緩期兩年執行。報道指涉案賄款約6,500萬美元，是北京金融領域反腐行動的又一要案；判決未披露更多案情細節。[EN原文]"
 },
 "why": {
   "sc": "金融监管系统的人事与廉政风险，会传导到审批节奏与合规预期。做跨境或涉内地业务时，这条提醒的是「执行监管的人同样被约束」，别把监管口径当成个人关系可以解决的事。",
   "tc": "金融監管系統的人事與廉政風險，會傳導到審批節奏與合規預期。做跨境或涉內地業務時，這條提醒的是「執行監管的人同樣被約束」，別把監管口徑當成個人關係可以解決的事。"
 },
 "tags": {"sc": ["反腐", "证监会", "监管治理", "内地"],
          "tc": ["反腐", "證監會", "監管治理", "內地"]},
 "actions": {
   "front": {"sc": "客户沟通：合规预期管理", "tc": "客戶溝通：合規預期管理"},
   "midback": {"sc": "研究：监管治理风险", "tc": "研究：監管治理風險"},
   "lead": {"sc": "团队简报：内地合规环境", "tc": "團隊簡報：內地合規環境"},
   "cross": {"sc": "跨境业务合规边界", "tc": "跨境業務合規邊界"}
 },
 "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 2},
 "source": {"sc": "South China Morning Post 2026-10-27", "tc": "South China Morning Post 2026-10-27",
            "name": "scmp", "date": "2026-10-27", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "前中国证监会高级官员王惠民因受贿约6,500万美元被判死刑、缓期两年执行，为内地金融领域反腐行动的又一要案。",
   "tc": "前中國證監會高級官員王惠民因受賄約6,500萬美元被判死刑、緩期兩年執行，為內地金融領域反腐行動的又一要案。"
 }
},
{
 "id": "ibm-korea-staged-crash-fraud-20261028",
 "clusterCount": 1,
 "verifyStatus": "verified",
 "contentKind": "news",
 "ingestedAt": NOW,
 "publishedAt": "2026-10-28T01:32:00+08:00",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/auto-motor/staged-car-crashes-drain-south-korean-motor-books-as-fraud-hits-record-595145.aspx",
 "sourceKey": "ibm",
 "sourceTier": "media",
 "score": 68,
 "boards": ["market"],
 "themes": ["保险欺诈", "车险理赔", "成本传导"],
 "title": {
   "sc": "韩国假车祸骗保成组织化产业　四个月查2,045宗、911人被查",
   "tc": "韓國假車禍騙保成組織化產業　四個月查2,045宗、911人被查"
 },
 "summary": {
   "sc": "韩国警察厅国家侦查本部6至9月四个月行动，查获2,045宗故意制造交通事故骗保案、锁定911名嫌疑人（12人拘留），确认损失75.2亿韩元（约540万美元）。报道指去年韩国保险业整体欺诈损失估计达9万亿韩元。[EN原文]",
   "tc": "韓國警察廳國家偵查本部6至9月四個月行動，查獲2,045宗故意製造交通事故騙保案、鎖定911名嫌疑人（12人拘留），確認損失75.2億韓元（約540萬美元）。報道指去年韓國保險業整體欺詐損失估計達9萬億韓元。[EN原文]"
 },
 "why": {
   "sc": "骗保推高的是所有投保人的成本。理赔端的「变道碰撞」套路提醒我们：帮客户备理赔材料时要强调现场取证与行车纪录，别让客户被组织化骗保网络当成工具，也别忘了这直接推高明年车险定价。",
   "tc": "騙保推高的是所有投保人的成本。理賠端的「變道碰撞」套路提醒我們：幫客戶備理賠材料時要強調現場取證與行車紀錄，別讓客戶被組織化騙保網絡當成工具，也別忘了這直接推高明年車險定價。"
 },
 "tags": {"sc": ["保险欺诈", "车险", "韩国", "理赔"],
          "tc": ["保險欺詐", "車險", "韓國", "理賠"]},
 "actions": {
   "front": {"sc": "客户沟通：理赔现场取证", "tc": "客戶溝通：理賠現場取證"},
   "midback": {"sc": "研究：欺诈成本与定价", "tc": "研究：欺詐成本與定價"},
   "lead": {"sc": "团队培训：理赔防诈要点", "tc": "團隊培訓：理賠防詐要點"},
   "cross": {"sc": "跨境车队风险管理", "tc": "跨境車隊風險管理"}
 },
 "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 1},
 "source": {"sc": "Insurance Business Asia 2026-10-28", "tc": "Insurance Business Asia 2026-10-28",
            "name": "ibm", "date": "2026-10-28", "lang": "en"},
 "lang": "en",
 "summaryShort": {
   "sc": "韩国警方四个月查获2,045宗故意制造车祸骗保案、锁定911名嫌疑人，确认损失约540万美元；去年韩国保险业欺诈损失估计达9万亿韩元。",
   "tc": "韓國警方四個月查獲2,045宗故意製造車禍騙保案、鎖定911名嫌疑人，確認損失約540萬美元；去年韓國保險業欺詐損失估計達9萬億韓元。"
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

lc_path = os.path.join(BASE, 'data/last-check.json')
lc = json.load(open(lc_path))
lc['lastCheck'] = NOW
for k, v in lc['sources'].items():
    v['last'] = NOW
json.dump(lc, open(lc_path, 'w'), ensure_ascii=False, indent=2)
print("last-check updated:", lc['lastCheck'], "| sources:", len(lc['sources']))
