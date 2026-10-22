# -*- coding: utf-8 -*-
"""2026-10-22 18:12 每日增量入库：11 条（窗口 2026-10-22 01:51 → 2026-10-22 18:12 HKT）"""
import json
from datetime import datetime

PATH = 'data/live-items.json'
NOW = datetime.now().astimezone().replace(microsecond=0).isoformat()

d = json.load(open(PATH, encoding='utf-8'))
items = d['items']
existing = {it['originalUrl'].split('?')[0].rstrip('/') for it in items}

new_items = [
{
 "id": "govhk-ce-financial-street-forum-20261022",
 "publishedAt": "2026-10-22T18:00:00+08:00",
 "originalUrl": "https://www.info.gov.hk/gia/general/202610/22/P2026102200260.htm",
 "sourceKey": "govhk", "sourceTier": "official", "score": 88,
 "verifyStatus": "verified", "contentKind": "speech", "clusterCount": 1,
 "boards": ["market", "family"], "themes": ["wealth-management", "risk-management-centre", "specialty-insurance", "five-year-plan"],
 "title": {"sc": "特首金融街论坛致辞：香港跃居全球最大跨境财富管理中心　发力亚洲风险管理中心",
           "tc": "特首金融街論壇致辭：香港躍居全球最大跨境財富管理中心　發力亞洲風險管理中心"},
 "summary": {"sc": "李家超在 2026 金融街论坛年会闭幕式视像致辞称，香港今年跃居全球最大跨境财富管理中心，并正构建亚洲顶尖风险管理中心，推动为黄金、绿色燃料等新兴产业提供专项保险；同时巩固全球最大离岸人民币枢纽，扩大点心债市场、推动人民币柜台纳入港股通。",
             "tc": "李家超在 2026 金融街論壇年會閉幕式視像致辭稱，香港今年躍居全球最大跨境財富管理中心，並正構建亞洲頂尖風險管理中心，推動為黃金、綠色燃料等新興產業提供專項保險；同時鞏固全球最大離岸人民幣樞紐，擴大點心債市場、推動人民幣櫃台納入港股通。"},
 "why": {"sc": "官方最高层对香港金融定位的最新表述：财富管理与风险管理两条主线并列，等于为「保险＋家办」的组合叙事背书。做高客的团队可直接引用「全球最大跨境财富管理中心」与「专项保险（黄金、绿色燃料）」两个提法，但要提醒客户这是政策方向而非产品承诺。",
         "tc": "官方最高層對香港金融定位的最新表述：財富管理與風險管理兩條主線並列，等於為「保險＋家辦」的組合敘事背書。做高客的團隊可直接引用「全球最大跨境財富管理中心」與「專項保險（黃金、綠色燃料）」兩個提法，但要提醒客戶這是政策方向而非產品承諾。"},
 "source": {"sc": "香港特区政府新闻公报 2026-10-22 18:00（行政长官致辞全文）", "tc": "香港特區政府新聞公報 2026-10-22 18:00（行政長官致辭全文）", "lang": "zh", "name": "govhk", "date": "2026-10-22"},
 "tags": {"sc": ["施政方向", "跨境财富管理", "风险管理中心", "专项保险", "离岸人民币"],
          "tc": ["施政方向", "跨境財富管理", "風險管理中心", "專項保險", "離岸人民幣"]},
 "actions": {"front": {"sc": "客户沟通：香港财富管理中心定位的政策依据", "tc": "客戶溝通：香港財富管理中心定位的政策依據"},
             "midback": {"sc": "方案研究：专项保险（黄金、绿色燃料）与客户产业的对接", "tc": "方案研究：專項保險（黃金、綠色燃料）與客戶產業的對接"},
             "lead": {"sc": "团队简报：五年规划对接十五五的金融要点", "tc": "團隊簡報：五年規劃對接十五五的金融要點"},
             "cross": {"sc": "高客叙事：财富管理＋风险管理双主线", "tc": "高客敘事：財富管理＋風險管理雙主線"}},
 "rolesImpact": {"front": 2, "midback": 1, "lead": 2, "cross": 2},
 "ingestedAt": NOW
},
{
 "id": "scmp-china-tax-workforce-offshore-trust-20261022",
 "publishedAt": "2026-10-22T17:51:00+08:00",
 "originalUrl": "https://www.scmp.com/business/china-business/article/3371791/china-expands-tax-workforce-tougher-enforcement-moves-spotlight",
 "sourceKey": "scmp", "sourceTier": "media", "score": 80,
 "verifyStatus": "verified", "contentKind": "news", "clusterCount": 1,
 "boards": ["family", "reg"], "themes": ["tax", "offshore-trust", "hnw", "enforcement"],
 "title": {"sc": "内地税务系统扩编 2.4 万人　离岸信托收益申报限期今日届满",
           "tc": "內地稅務系統擴編 2.4 萬人　離岸信託收益申報限期今日屆滿"},
 "summary": {"sc": "内地 2027 年公务员招录计划含 24,013 个税务职位，占全部名额逾 67%（上年逾 65%），多数在国家税务总局地方分支。国家税务总局本周明确离岸信托收益须申报缴纳个税，10 月 22 日前结清免收滞纳金；上半年至少 80 家上市公司被要求补缴企业所得税及滞纳金。",
             "tc": "內地 2027 年公務員招錄計劃含 24,013 個稅務職位，佔全部名額逾 67%（上年逾 65%），多數在國家稅務總局地方分支。國家稅務總局本週明確離岸信託收益須申報繳納個稅，10 月 22 日前結清免收滯納金；上半年至少 80 家上市公司被要求補繳企業所得稅及滯納金。"},
 "why": {"sc": "离岸信托征税从「个案」走向「有编制、有期限」的执行阶段——扩编 2.4 万税务人员是长期变量，不是一次性动作。受访英国律师预期高净值家族信托争议会增加。对做跨境高客的团队，这是重做「税务尽调＋披露」叙事的信号：客户的问题会从「要不要报」变成「怎么补、怎么举证」。",
         "tc": "離岸信託徵稅從「個案」走向「有編制、有期限」的執行階段——擴編 2.4 萬稅務人員是長期變量，不是一次性動作。受訪英國律師預期高淨值家族信託爭議會增加。對做跨境高客的團隊，這是重做「稅務盡調＋披露」敘事的信號：客戶的問題會從「要不要報」變成「怎麼補、怎麼舉證」。"},
 "source": {"sc": "South China Morning Post 2026-10-22（Zhu Wenqian，北京）", "tc": "South China Morning Post 2026-10-22（Zhu Wenqian，北京）", "lang": "en", "name": "scmp", "date": "2026-10-22"},
 "tags": {"sc": ["离岸信托", "个人所得税", "税务执法", "高净值", "跨境合规"],
          "tc": ["離岸信託", "個人所得稅", "稅務執法", "高淨值", "跨境合規"]},
 "actions": {"front": {"sc": "客户沟通：申报义务一直在，宽限期只是缓冲", "tc": "客戶溝通：申報義務一直在，寬限期只是緩衝"},
             "midback": {"sc": "合规留痕：信托架构的税务意见与申报记录", "tc": "合規留痕：信託架構的稅務意見與申報記錄"},
             "lead": {"sc": "团队简报：内地税务执法趋势与客户问答", "tc": "團隊簡報：內地稅務執法趨勢與客戶問答"},
             "cross": {"sc": "跨境架构：信托、保单与申报主体的税基对齐", "tc": "跨境架構：信託、保單與申報主體的稅基對齊"}},
 "rolesImpact": {"front": 2, "midback": 2, "lead": 2, "cross": 3},
 "ingestedAt": NOW
},
{
 "id": "govhk-legco-q11-cross-border-medical-ads-20261021",
 "publishedAt": "2026-10-21T15:00:00+08:00",
 "originalUrl": "https://www.info.gov.hk/gia/general/202610/21/P2026102100267.htm",
 "sourceKey": "govhk", "sourceTier": "official", "score": 82,
 "verifyStatus": "verified", "contentKind": "news", "clusterCount": 1,
 "boards": ["reg", "product"], "themes": ["cross-border-medical", "advertising", "gba", "consumer-protection"],
 "title": {"sc": "立法会十一题：跨境医疗广告监管　境外机构不受本地专业守则约束",
           "tc": "立法會十一題：跨境醫療廣告監管　境外機構不受本地專業守則約束"},
 "summary": {"sc": "医务卫生局书面答复：本港注册医护受专业守则规限、原则上不得以广告招徕，但境外机构不受同一约束，形成宣传规范差异；《不良广告（医药）条例》只针对特定疾病与疗效声称。卫生署已与内地部委建立联络通报机制，消委会与澳门及内地逾 30 个省市签有跨境投诉转介备忘录。",
             "tc": "醫務衞生局書面答覆：本港註冊醫護受專業守則規限、原則上不得以廣告招徠，但境外機構不受同一約束，形成宣傳規範差異；《不良廣告（醫藥）條例》只針對特定疾病與療效聲稱。衞生署已與內地部委建立聯絡通報機制，消委會與澳門及內地逾 30 個省市簽有跨境投訴轉介備忘錄。"},
 "why": {"sc": "对做内地客医疗险、重疾险的团队：客户的就医信息越来越多来自境外机构投放的广告，而广告规范与医疗责任分属两套体系。可据此向客户讲清「保单不是医疗服务提供者」，并给出跨境求诊的风险提示与投诉转介渠道——这是不涉产品比较、却能建立专业信任的谈资。",
         "tc": "對做內地客醫療險、重疾險的團隊：客戶的就醫資訊越來越多來自境外機構投放的廣告，而廣告規範與醫療責任分屬兩套體系。可據此向客戶講清「保單不是醫療服務提供者」，並給出跨境求診的風險提示與投訴轉介渠道——這是不涉產品比較、卻能建立專業信任的談資。"},
 "source": {"sc": "香港特区政府新闻公报 2026-10-21 15:00（立法会十一题书面答复）", "tc": "香港特區政府新聞公報 2026-10-21 15:00（立法會十一題書面答覆）", "lang": "zh", "name": "govhk", "date": "2026-10-21"},
 "tags": {"sc": ["跨境医疗", "广告监管", "大湾区", "医疗险", "消费者权益"],
          "tc": ["跨境醫療", "廣告監管", "大灣區", "醫療險", "消費者權益"]},
 "actions": {"front": {"sc": "客户沟通：保单不等于医疗服务提供者", "tc": "客戶溝通：保單不等於醫療服務提供者"},
             "midback": {"sc": "理赔提示：跨境就医的单据与病历留存", "tc": "理賠提示：跨境就醫的單據與病歷留存"},
             "lead": {"sc": "团队简报：跨境医疗宣传规范差异", "tc": "團隊簡報：跨境醫療宣傳規範差異"},
             "cross": {"sc": "大湾区医疗融合下的服务衔接", "tc": "大灣區醫療融合下的服務銜接"}},
 "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 2},
 "ingestedAt": NOW
},
{
 "id": "iaasia-japan-agency-recommendation-rules-20261022",
 "publishedAt": "2026-10-22T17:08:00+08:00",
 "originalUrl": "https://insuranceasia.com/videos/japan-forces-insurance-agencies-justify-recommendations",
 "sourceKey": "insuranceasia", "sourceTier": "pro", "score": 74,
 "verifyStatus": "verified", "contentKind": "news", "clusterCount": 1,
 "boards": ["reg", "product"], "themes": ["conduct", "recommendation", "japan", "multi-tie"],
 "title": {"sc": "日本新规：多保代理须举证推荐理由　2028 年 3 月生效",
           "tc": "日本新規：多保代理須舉證推薦理由　2028 年 3 月生效"},
 "summary": {"sc": "日本新销售规则 2028 年 3 月 1 日生效，代理多家保险公司的机构须强化产品比较，并以客户需求而非与保司的关系解释推荐理由；车险须按保障与保费选择，寿险与医疗险须对应客户保障需要、预算与长期财务优先次序。2026 年 6 月另把独立经纪最低保证金由 2,000 万日元降至 1,000 万日元。",
             "tc": "日本新銷售規則 2028 年 3 月 1 日生效，代理多家保險公司的機構須強化產品比較，並以客戶需求而非與保司的關係解釋推薦理由；車險須按保障與保費選擇，壽險與醫療險須對應客戶保障需要、預算與長期財務優先次序。2026 年 6 月另把獨立經紀最低保證金由 2,000 萬日元降至 1,000 萬日元。"},
 "why": {"sc": "亚洲监管正在把「为什么推荐这款」从行业惯例变成可举证的合规义务。香港虽未照搬，但公平待客与合适性要求方向一致。团队现在就该把需求分析、产品比较、替代方案说明做成可回溯的记录——等到客户或监管来问，临时补是补不出来的。",
         "tc": "亞洲監管正在把「為什麼推薦這款」從行業慣例變成可舉證的合規義務。香港雖未照搬，但公平待客與合適性要求方向一致。團隊現在就該把需求分析、產品比較、替代方案說明做成可回溯的記錄——等到客戶或監管來問，臨時補是補不出來的。"},
 "source": {"sc": "InsuranceAsia 2026-10-22（引 Mordor Intelligence 分析师评论）", "tc": "InsuranceAsia 2026-10-22（引 Mordor Intelligence 分析師評論）", "lang": "en", "name": "insuranceasia", "date": "2026-10-22"},
 "tags": {"sc": ["销售行为", "推荐理由", "日本", "多保代理", "合适性"],
          "tc": ["銷售行為", "推薦理由", "日本", "多保代理", "合適性"]},
 "actions": {"front": {"sc": "客户沟通：把推荐理由讲清楚，本身就是专业度", "tc": "客戶溝通：把推薦理由講清楚，本身就是專業度"},
             "midback": {"sc": "流程改造：需求分析与产品比较留痕模板", "tc": "流程改造：需求分析與產品比較留痕模板"},
             "lead": {"sc": "团队培训：多保代理的举证式销售", "tc": "團隊培訓：多保代理的舉證式銷售"},
             "cross": {"sc": "—", "tc": "—"}},
 "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 0},
 "ingestedAt": NOW
},
{
 "id": "ibm-cfc-sme-cyber-disconnect-20261022",
 "publishedAt": "2026-10-22",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/cyber/smes-rank-cyber-their-top-risk-but-misread-the-threats-cfc-594508.aspx",
 "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 70,
 "verifyStatus": "verified", "contentKind": "stats", "clusterCount": 1,
 "boards": ["product", "tech"], "themes": ["cyber", "sme", "coverage-gap", "education"],
 "title": {"sc": "CFC：中小企视网络为最大风险　却 74% 不知保单涵盖人为失误",
           "tc": "CFC：中小企視網絡為最大風險　卻 74% 不知保單涵蓋人為失誤"},
 "summary": {"sc": "CFC 首份全球中小企（营收 2,500 万美元以下）网络风险研究：近半把网络攻击与数据外泄列为最大商业风险，近三成过去三年曾遭遇；但仅 30% 视钓鱼与社交工程为主要威胁、28% 认为人为失误重要。CFC 自身理赔中勒索软件占成本 64%、人为失误涉 75% 个案；74% 受访者不知网络保险涵盖人为失误。",
             "tc": "CFC 首份全球中小企（營收 2,500 萬美元以下）網絡風險研究：近半把網絡攻擊與數據外泄列為最大商業風險，近三成過去三年曾遭遇；但僅 30% 視釣魚與社交工程為主要威脅、28% 認為人為失誤重要。CFC 自身理賠中勒索軟件佔成本 64%、人為失誤涉 75% 個案；74% 受訪者不知網絡保險涵蓋人為失誤。"},
 "why": {"sc": "「知道自己有风险」与「知道自己买了什么」是两件事——这正是中小企业网络险的成交障碍，也是经纪的切入点。对做 SME 客户的团队，与其讲威胁，不如讲保单到底赔什么：人为失误、事件响应、法律与监管支援，这三项是 61%–74% 客户不知道的。",
         "tc": "「知道自己有風險」與「知道自己買了什麼」是兩件事——這正是中小企網絡險的成交障礙，也是經紀的切入點。對做 SME 客戶的團隊，與其講威脅，不如講保單到底賠什麼：人為失誤、事件響應、法律與監管支援，這三項是 61%–74% 客戶不知道的。"},
 "source": {"sc": "Insurance Business Asia 2026-10-22（引 CFC《The Cyber Insurance Disconnect》）", "tc": "Insurance Business Asia 2026-10-22（引 CFC《The Cyber Insurance Disconnect》）", "lang": "en", "name": "insurancebusinessmag", "date": "2026-10-22"},
 "tags": {"sc": ["网络保险", "中小企", "保障缺口", "人为失误", "客户教育"],
          "tc": ["網絡保險", "中小企", "保障缺口", "人為失誤", "客戶教育"]},
 "actions": {"front": {"sc": "客户沟通：先讲赔什么，再讲威胁有多大", "tc": "客戶溝通：先講賠什麼，再講威脅有多大"},
             "midback": {"sc": "条款检视：人为失误、事件响应、法律支援三项", "tc": "條款檢視：人為失誤、事件響應、法律支援三項"},
             "lead": {"sc": "团队简报：SME 网络险的成交障碍", "tc": "團隊簡報：SME 網絡險的成交障礙"},
             "cross": {"sc": "—", "tc": "—"}},
 "rolesImpact": {"front": 3, "midback": 2, "lead": 1, "cross": 0},
 "ingestedAt": NOW
},
{
 "id": "ibm-tysers-singapore-ceo-marine-20261022",
 "publishedAt": "2026-10-22",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/tysers-confirms-singapore-ceo-to-lead-asiapacific-insurance-expansion-594444.aspx",
 "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 68,
 "verifyStatus": "verified", "contentKind": "news", "clusterCount": 1,
 "boards": ["market", "insurer"], "themes": ["marine", "brokerage", "apac", "market-data"],
 "title": {"sc": "Tysers 星洲 CEO 获 MAS 批准　亚太水险保费 426 亿美元、亚太占 30.8%",
           "tc": "Tysers 星洲 CEO 獲 MAS 批准　亞太水險保費 426 億美元、亞太佔 30.8%"},
 "summary": {"sc": "新加坡金管局批准 William Furness-Smith 出任 Tysers 新加坡行政总裁，统筹亚太扩张。文中引 IUMI 数字：2025 年全球水险保费升 5.5% 至 426 亿美元，亚太占 30.8%；亚洲占全球货运险保费 36.4%，新加坡货运险保费增 13%，亚洲货运赔付率略低于 70%、自 2020 年起呈上行。",
             "tc": "新加坡金管局批准 William Furness-Smith 出任 Tysers 新加坡行政總裁，統籌亞太擴張。文中引 IUMI 數字：2025 年全球水險保費升 5.5% 至 426 億美元，亞太佔 30.8%；亞洲佔全球貨運險保費 36.4%，新加坡貨運險保費增 13%，亞洲貨運賠付率略低於 70%、自 2020 年起呈上行。"},
 "why": {"sc": "两个方向相反的信号：保费在增长，价格却在软化，赔付率还在往上走。做贸易、物流类企业客户的团队，续保时不能只谈降价——赔付率上行意味着核保会收紧除外责任与申报要求，提前帮客户把货运申报流程做扎实，比争 5% 折扣更有价值。",
         "tc": "兩個方向相反的信號：保費在增長，價格卻在軟化，賠付率還在往上走。做貿易、物流類企業客戶的團隊，續保時不能只談降價——賠付率上行意味著核保會收緊除外責任與申報要求，提前幫客戶把貨運申報流程做扎實，比爭 5% 折扣更有價值。"},
 "source": {"sc": "Insurance Business Asia 2026-10-22（引 IUMI 统计与市场评估）", "tc": "Insurance Business Asia 2026-10-22（引 IUMI 統計與市場評估）", "lang": "en", "name": "insurancebusinessmag", "date": "2026-10-22"},
 "tags": {"sc": ["水险", "货运险", "亚太市场", "赔付率", "经纪扩张"],
          "tc": ["水險", "貨運險", "亞太市場", "賠付率", "經紀擴張"]},
 "actions": {"front": {"sc": "客户沟通：保费增长与价格软化同时发生", "tc": "客戶溝通：保費增長與價格軟化同時發生"},
             "midback": {"sc": "续保准备：货运申报与除外责任核对", "tc": "續保準備：貨運申報與除外責任核對"},
             "lead": {"sc": "团队简报：水险区域格局", "tc": "團隊簡報：水險區域格局"},
             "cross": {"sc": "—", "tc": "—"}},
 "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 0},
 "ingestedAt": NOW
},
{
 "id": "rn-sompo-indonesia-syariah-entity-20261022",
 "publishedAt": "2026-10-22T14:00:00+08:00",
 "originalUrl": "https://www.reinsurancene.ws/sompo-indonesia-establishes-dedicated-general-syariah-insurance-company/",
 "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 66,
 "verifyStatus": "verified", "contentKind": "news", "clusterCount": 1,
 "boards": ["insurer", "market"], "themes": ["syariah", "indonesia", "entity-setup", "ojk"],
 "title": {"sc": "印尼 Sompo 设专门伊斯兰一般保险公司　按 OJK 规定独立运营",
           "tc": "印尼 Sompo 設專門伊斯蘭一般保險公司　按 OJK 規定獨立運營"},
 "summary": {"sc": "Sompo Insurance Indonesia 宣布 PT Sompo Insurance Sharia（Sompo Syariah）正式开业，成为独立的一般伊斯兰保险公司；此前自 2017 年起以伊斯兰业务形式经营。新公司按金融服务管理局（OJK）规定设立，由 Ratna Indrayani 出任行政总裁，集团称可分拆治理、产品定制与教育推广。",
             "tc": "Sompo Insurance Indonesia 宣布 PT Sompo Insurance Sharia（Sompo Syariah）正式開業，成為獨立的一般伊斯蘭保險公司；此前自 2017 年起以伊斯蘭業務形式經營。新公司按金融服務管理局（OJK）規定設立，由 Ratna Indrayani 出任行政總裁，集團稱可分拆治理、產品定制與教育推廣。"},
 "why": {"sc": "东南亚市场正在把伊斯兰保险从「窗口业务」拆成独立法人，说明当地监管要求与客群规模都已到位。对香港团队的直接启发有限，但对服务东南亚华商或穆斯林客群的跨境客户，这是可引用的市场成熟度信号。",
         "tc": "東南亞市場正在把伊斯蘭保險從「窗口業務」拆成獨立法人，說明當地監管要求與客群規模都已到位。對香港團隊的直接啟發有限，但對服務東南亞華商或穆斯林客群的跨境客戶，這是可引用的市場成熟度信號。"},
 "source": {"sc": "Reinsurance News 2026-10-22（引 Sompo 公告）", "tc": "Reinsurance News 2026-10-22（引 Sompo 公告）", "lang": "en", "name": "reinsurancenews", "date": "2026-10-22"},
 "tags": {"sc": ["伊斯兰保险", "印尼", "OJK", "市场准入", "区域扩张"],
          "tc": ["伊斯蘭保險", "印尼", "OJK", "市場准入", "區域擴張"]},
 "actions": {"front": {"sc": "客户沟通：东南亚市场的伊斯兰保险供给", "tc": "客戶溝通：東南亞市場的伊斯蘭保險供給"},
             "midback": {"sc": "—", "tc": "—"},
             "lead": {"sc": "团队简报：印尼市场结构变化", "tc": "團隊簡報：印尼市場結構變化"},
             "cross": {"sc": "跨境客群的产品适配提示", "tc": "跨境客群的產品適配提示"}},
 "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 1},
 "ingestedAt": NOW
},
{
 "id": "rn-tal-daiichi-challenger-takeover-20261022",
 "publishedAt": "2026-10-22T13:30:00+08:00",
 "originalUrl": "https://www.reinsurancene.ws/tal-dai-ichi-life-australia-proposes-acquisition-of-remaining-challenger-shares/",
 "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 68,
 "verifyStatus": "verified", "contentKind": "news", "clusterCount": 1,
 "boards": ["insurer", "market"], "themes": ["m-and-a", "australia", "annuity", "japan"],
 "title": {"sc": "第一生命旗下 TAL 提购澳洲 Challenger 余下 79.5%　每股 11.80 澳元",
           "tc": "第一生命旗下 TAL 提購澳洲 Challenger 餘下 79.5%　每股 11.80 澳元"},
 "summary": {"sc": "日本第一生命集团旗下 TAL Dai-ichi Life Australia 向 Challenger 董事会提出非约束性建议，拟以每股 11.80 澳元、按协议安排收购其尚未持有的 79.5% 普通股。2025 年 4 月 MS&AD 已把所持 15.1%（约 1.04 亿股、800 亿日元）售予 TAL。交易仍须尽调、最终条款与监管批准。",
             "tc": "日本第一生命集團旗下 TAL Dai-ichi Life Australia 向 Challenger 董事會提出非約束性建議，擬以每股 11.80 澳元、按協議安排收購其尚未持有的 79.5% 普通股。2025 年 4 月 MS&AD 已把所持 15.1%（約 1.04 億股、800 億日元）售予 TAL。交易仍須盡調、最終條款與監管批准。"},
 "why": {"sc": "日本寿险资本继续向海外年金与退休资产延伸，澳洲是主战场。对香港的镜像意义在于：外资集团对「长期负债＋资产管理」的整合更有兴趣，而非纯保障业务——这会影响未来几年香港市场上储蓄型产品的供给与定价逻辑。",
         "tc": "日本壽險資本繼續向海外年金與退休資產延伸，澳洲是主戰場。對香港的鏡像意義在於：外資集團對「長期負債＋資產管理」的整合更有興趣，而非純保障業務——這會影響未來幾年香港市場上儲蓄型產品的供給與定價邏輯。"},
 "source": {"sc": "Reinsurance News 2026-10-22（引 TAL Dai-ichi 建议文件）", "tc": "Reinsurance News 2026-10-22（引 TAL Dai-ichi 建議文件）", "lang": "en", "name": "reinsurancenews", "date": "2026-10-22"},
 "tags": {"sc": ["并购", "澳洲", "年金", "第一生命", "行业整合"],
          "tc": ["併購", "澳洲", "年金", "第一生命", "行業整合"]},
 "actions": {"front": {"sc": "客户沟通：外资集团偏好长期负债型资产", "tc": "客戶溝通：外資集團偏好長期負債型資產"},
             "midback": {"sc": "—", "tc": "—"},
             "lead": {"sc": "团队简报：亚太寿险并购脉络", "tc": "團隊簡報：亞太壽險併購脈絡"},
             "cross": {"sc": "储蓄型产品供给的长期变量", "tc": "儲蓄型產品供給的長期變量"}},
 "rolesImpact": {"front": 1, "midback": 0, "lead": 1, "cross": 1},
 "ingestedAt": NOW
},
{
 "id": "artemis-mexico-world-bank-cat-ddo-20261022",
 "publishedAt": "2026-10-22",
 "originalUrl": "https://www.artemis.bm/news/mexico-gets-its-first-world-bank-cat-ddo-to-complement-cat-bonds-and-parametric-insurance/",
 "sourceKey": "artemis", "sourceTier": "pro", "score": 66,
 "verifyStatus": "verified", "contentKind": "news", "clusterCount": 1,
 "boards": ["market"], "themes": ["sovereign-risk", "catastrophe", "world-bank", "protection-gap"],
 "title": {"sc": "墨西哥首获世行 5 亿美元 Cat DDO　与巨灾债券、参数式保险互补",
           "tc": "墨西哥首獲世行 5 億美元 Cat DDO　與巨災債券、參數式保險互補"},
 "summary": {"sc": "世界银行批准 5 亿美元融资，墨西哥首次取得「灾难延迟提款选择权」（Cat DDO）：政府宣布进入紧急状态后即可提款，期限三年、可延长，用于应对自然灾害、气候变化与公共卫生紧急事件，并与墨西哥 2024 年两笔 IBRD 巨灾债券及参数式保险形成互补。",
             "tc": "世界銀行批准 5 億美元融資，墨西哥首次取得「災難延遲提款選擇權」（Cat DDO）：政府宣布進入緊急狀態後即可提款，期限三年、可延長，用於應對自然災害、氣候變化與公共衛生緊急事件，並與墨西哥 2024 年兩筆 IBRD 巨災債券及參數式保險形成互補。"},
 "why": {"sc": "主权层的风险融资工具越铺越完整：先有巨灾债券，再加信用额度，最后才是保险。香港近年推动巨灾保险与 ILS（含首宗侧挂车证券），这条「债券＋额度＋保险」的组合思路，可作为向企业客户解释风险分层与自留额的材料。",
         "tc": "主權層的風險融資工具越鋪越完整：先有巨災債券，再加信用額度，最後才是保險。香港近年推動巨災保險與 ILS（含首宗側掛車證券），這條「債券＋額度＋保險」的組合思路，可作為向企業客戶解釋風險分層與自留額的材料。"},
 "source": {"sc": "Artemis 2026-10-22（引世界银行公告）", "tc": "Artemis 2026-10-22（引世界銀行公告）", "lang": "en", "name": "artemis", "date": "2026-10-22"},
 "tags": {"sc": ["巨灾风险融资", "世界银行", "参数式保险", "主权风险", "保障缺口"],
          "tc": ["巨災風險融資", "世界銀行", "參數式保險", "主權風險", "保障缺口"]},
 "actions": {"front": {"sc": "客户沟通：风险分层的三种资金来源", "tc": "客戶溝通：風險分層的三種資金來源"},
             "midback": {"sc": "自留额设计：额度＋保险的组合", "tc": "自留額設計：額度＋保險的組合"},
             "lead": {"sc": "团队简报：主权风险融资工具演进", "tc": "團隊簡報：主權風險融資工具演進"},
             "cross": {"sc": "—", "tc": "—"}},
 "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 0},
 "ingestedAt": NOW
},
{
 "id": "ian-uk-pi-tt-club-thomas-miller-20261022",
 "publishedAt": "2026-10-22T17:50:00+08:00",
 "originalUrl": "https://insuranceasianews.com/defining-moment-as-uk-pi-club-tt-club-complete-thomas-miller-acquisition/",
 "sourceKey": "insuranceasianews", "sourceTier": "media", "score": 64,
 "verifyStatus": "pending", "contentKind": "news", "clusterCount": 1,
 "boards": ["insurer", "market"], "themes": ["marine", "pi-club", "m-and-a", "mutual"],
 "title": {"sc": "UK P&I Club 与 TT Club 完成联合收购 Thomas Miller",
           "tc": "UK P&I Club 與 TT Club 完成聯合收購 Thomas Miller"},
 "summary": {"sc": "英国船东互保协会 UK P&I Club 与 TT Club 宣布完成对 Thomas Miller Holdings 集团的联合收购，报道称之为组建新集团的重要里程碑。该交易把两家互保协会的管理公司纳入同一架构，涉及货运、船舶责任与专业责任等领域。（原文有付费墙，仅据首段。）",
             "tc": "英國船東互保協會 UK P&I Club 與 TT Club 宣布完成對 Thomas Miller Holdings 集團的聯合收購，報道稱之為組建新集團的重要里程碑。該交易把兩家互保協會的管理公司納入同一架構，涉及貨運、船舶責任與專業責任等領域。（原文有付費牆，僅據首段。）"},
 "why": {"sc": "互保协会的管理公司与承保实体长期分离，这次合并把治理与资本放在一起，是 P&I 体系的结构性变化。对香港做航运、贸易客户的团队，值得跟进合并后出单主体、会费与理赔授权是否变化——这些细节会直接影响客户的续保体验。",
         "tc": "互保協會的管理公司與承保實體長期分離，這次合併把治理與資本放在一起，是 P&I 體系的結構性變化。對香港做航運、貿易客戶的團隊，值得跟進合併後出單主體、會費與理賠授權是否變化——這些細節會直接影響客戶的續保體驗。"},
 "source": {"sc": "InsuranceAsia News 2026-10-22（Andrew Mullen）", "tc": "InsuranceAsia News 2026-10-22（Andrew Mullen）", "lang": "en", "name": "insuranceasianews", "date": "2026-10-22"},
 "tags": {"sc": ["船东互保", "并购", "水险", "治理结构", "英国"],
          "tc": ["船東互保", "併購", "水險", "治理結構", "英國"]},
 "actions": {"front": {"sc": "客户沟通：合作方架构变动提示", "tc": "客戶溝通：合作方架構變動提示"},
             "midback": {"sc": "出单与理赔：主体与授权是否变化", "tc": "出單與理賠：主體與授權是否變化"},
             "lead": {"sc": "团队简报：P&I 体系整合", "tc": "團隊簡報：P&I 體系整合"},
             "cross": {"sc": "—", "tc": "—"}},
 "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 0},
 "ingestedAt": NOW
},
{
 "id": "ian-ai-exclusions-pushback-20261022",
 "publishedAt": "2026-10-22T07:30:00+08:00",
 "originalUrl": "https://insuranceasianews.com/dont-carve-it-out-insurers-push-back-on-blanket-ai-exclusions-as-adoption-surges/",
 "sourceKey": "insuranceasianews", "sourceTier": "media", "score": 68,
 "verifyStatus": "pending", "contentKind": "news", "clusterCount": 1,
 "boards": ["tech", "product"], "themes": ["ai", "exclusions", "coverage-gap", "underwriting"],
 "title": {"sc": "保险业者反对「一刀切」AI 除外条款　警告保障缺口扩大",
           "tc": "保險業者反對「一刀切」AI 除外條款　警告保障缺口擴大"},
 "summary": {"sc": "报道指随着 AI 嵌入企业日常营运，保险公司正抵制在保单中加入笼统的 AI 除外条款，警告全面剔除会制造保障缺口。业者主张按实际风险分层处理，而非整体排除。（原文有付费墙，仅据首段与摘要。）",
             "tc": "報道指隨著 AI 嵌入企業日常營運，保險公司正抵制在保單中加入籠統的 AI 除外條款，警告全面剔除會製造保障缺口。業者主張按實際風險分層處理，而非整體排除。（原文有付費牆，僅據首段與摘要。）"},
 "why": {"sc": "AI 相关的除外与承保口径正在形成，方向是「分层」而非「全剔」。对做科技、专业责任客户的团队，现在正是逐条核对保单里 AI 相关措辞的窗口期——等核保口径固化后再争取，空间会小很多。",
         "tc": "AI 相關的除外與承保口徑正在形成，方向是「分層」而非「全剔」。對做科技、專業責任客戶的團隊，現在正是逐條核對保單裡 AI 相關措辭的窗口期——等核保口徑固化後再爭取，空間會小很多。"},
 "source": {"sc": "InsuranceAsia News 2026-10-22", "tc": "InsuranceAsia News 2026-10-22", "lang": "en", "name": "insuranceasianews", "date": "2026-10-22"},
 "tags": {"sc": ["人工智能", "除外条款", "专业责任", "核保口径", "保障缺口"],
          "tc": ["人工智能", "除外條款", "專業責任", "核保口徑", "保障缺口"]},
 "actions": {"front": {"sc": "客户沟通：AI 相关风险是否在保", "tc": "客戶溝通：AI 相關風險是否在保"},
             "midback": {"sc": "条款检视：AI 措辞逐条核对", "tc": "條款檢視：AI 措辭逐條核對"},
             "lead": {"sc": "团队简报：AI 承保口径趋势", "tc": "團隊簡報：AI 承保口徑趨勢"},
             "cross": {"sc": "跨境科技客户的条款差异", "tc": "跨境科技客戶的條款差異"}},
 "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 1},
 "ingestedAt": NOW
},
]

added = []
for it in new_items:
    key = it['originalUrl'].split('?')[0].rstrip('/')
    if key in existing:
        print('skip dup:', it['id'])
        continue
    items.insert(0, it)
    existing.add(key)
    added.append(it['id'])

items.sort(key=lambda x: x.get('publishedAt') or '', reverse=True)

meta = d['meta']
meta['generatedAt'] = NOW
meta['itemCount'] = len(items)
meta['windowNote'] = {"sc": f"本库{len(items)}条。", "tc": f"本庫{len(items)}條。"}

json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('added', len(added), 'total', len(items))
for a in added:
    print('  +', a)
