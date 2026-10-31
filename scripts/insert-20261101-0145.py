# -*- coding: utf-8 -*-
"""Insert 4 curated items for 2026-11-01 01:38 run (window: 2026-10-31T12:20 -> now)."""
import json, datetime

LIVE = "/Users/leonliang/maoquanqingbao/data/live-items.json"
NOW = "2026-11-01T01:45:00+08:00"

items = [
 {
  "id": "ian-full-capacity-korea-re-backstop-20261031",
  "publishedAt": "2026-10-31T08:00:00+08:00",
  "originalUrl": "https://www.insuranceasianews.com/looking-beyond-market-cycles/",
  "sourceKey": "insuranceasianews",
  "sourceTier": "media",
  "score": 70,
  "contentKind": "news",
  "boards": ["market", "reg"],
  "themes": ["再保险", "另类资本", "韩国市场"],
  "title": {
   "sc": "IAN周报：韩国拟立法设国家再保险backstop　BlackRock指自保再保与第三方资本成亚太「首要议题」",
   "tc": "IAN週報：韓國擬立法設國家再保險backstop　BlackRock指自保再保與第三方資本成亞太「首要議題」"
  },
  "summary": {
   "sc": "《Full Capacity》10月31日周报要点：韩国拟为风暴、洪水、地震保险引入国家再保险安排，由国家与保险公司签订再保协议、财政部充当最后再保险人（修法草案）；BlackRock 金融机构组保险策略师称，自保再保（captive reinsurance）与第三方资本运用是亚太险企「首要议题」；迪拜 MGA elseco 在新加坡设劳合社 coverholder 先做意外及健康险，并从平安产险取得通航运力；印度分销改革咨询意见期延至周六，已收逾650份意见。[EN原文]",
   "tc": "《Full Capacity》10月31日週報要點：韓國擬為風暴、洪水、地震保險引入國家再保險安排，由國家與保險公司簽訂再保協議、財政部充當最後再保險人（修法草案）；BlackRock 金融機構組保險策略師稱，自保再保（captive reinsurance）與第三方資本運用是亞太險企「首要議題」；迪拜 MGA elseco 在新加坡設勞合社 coverholder 先做意外及健康險，並從平安產險取得通航運力；印度分銷改革諮詢意見期延至週六，已收逾650份意見。[EN原文]"
  },
  "why": {
   "sc": "看点不是韩国本身，而是「政府当最后再保人」这条路径正在亚太扩散——巨灾风险从商业再保回流财政，会改变再保议价结构。客户抱怨再保推高保费时，这是可引用的区域对照；BlackRock 提的 captive／第三方资本，也解释了为何当前再保定价偏软。",
   "tc": "看點不是韓國本身，而是「政府當最後再保人」這條路徑正在亞太擴散——巨災風險從商業再保回流財政，會改變再保議價結構。客戶抱怨再保推高保費時，這是可引用的區域對照；BlackRock 提的 captive／第三方資本，也解釋了為何當前再保定價偏軟。"
  },
  "tags": {
   "sc": ["韩国", "国家再保险", "自保再保", "第三方资本", "印度分销改革"],
   "tc": ["韓國", "國家再保險", "自保再保", "第三方資本", "印度分銷改革"]
  },
  "actions": {
   "front": {"sc": "客户沟通：再保成本上升的区域背景", "tc": "客戶溝通：再保成本上升的區域背景"},
   "midback": {"sc": "产品跟踪：captive 与第三方资本对定价影响", "tc": "產品跟蹤：captive 與第三方資本對定價影響"},
   "lead": {"sc": "团队简报：亚太再保格局一周要点", "tc": "團隊簡報：亞太再保格局一週要點"},
   "cross": {"sc": "跨境客户：东南亚监管与承保能力变化", "tc": "跨境客戶：東南亞監管與承保能力變化"}
  },
  "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 2},
  "source": {
   "sc": "InsuranceAsia News（Full Capacity 周报）2026-10-31",
   "tc": "InsuranceAsia News（Full Capacity 週報）2026-10-31",
   "name": "insuranceasianews", "date": "2026-10-31", "lang": "en"
  },
  "lang": "en",
  "verifyStatus": "verified",
  "clusterCount": 1,
  "ingestedAt": NOW
 },
 {
  "id": "iaasia-weekly-cat-loss-hk-indonesia-20261031",
  "publishedAt": "2026-10-31T05:00:00+08:00",
  "originalUrl": "https://insuranceasia.com/insurance/news/week-in-insurance-catastrophe-losses-hit-242b-hong-kong-life-premiums-surge-indonesia-tightens-capital-rules",
  "sourceKey": "insuranceasia",
  "sourceTier": "media",
  "score": 64,
  "contentKind": "news",
  "boards": ["market"],
  "themes": ["巨灾损失", "寿险保费", "资本监管"],
  "title": {
   "sc": "Insurance Asia周报：全球巨灾损失2,420亿美元　香港寿险保费续升、印尼收紧资本规则",
   "tc": "Insurance Asia週報：全球巨災損失2,420億美元　香港壽險保費續升、印尼收緊資本規則"
  },
  "summary": {
   "sc": "Insurance Asia 10月31日本周综述三条主线：一、全球巨灾损失累计约2,420亿美元，其中首九个月保险损失约920亿美元；二、香港寿险保费延续升势；三、印尼进一步收紧保险资本规则。原文为要闻汇编，各项数据的细项与出处见库内对应条目，本条目仅作索引。[EN原文]",
   "tc": "Insurance Asia 10月31日本週綜述三條主線：一、全球巨災損失累計約2,420億美元，其中首九個月保險損失約920億美元；二、香港壽險保費延續升勢；三、印尼進一步收緊保險資本規則。原文為要聞彙編，各項數據的細項與出處見庫內對應條目，本條目僅作索引。[EN原文]"
  },
  "why": {
   "sc": "一周三件事放一起看才成立：巨灾损失走高、香港保费仍升、东南亚监管收资本——「风险涨价、需求不减、监管变严」同时发生，是本周市场叙事的骨架。细项请点原文或库内单条，别只引摘要数字。",
   "tc": "一週三件事放一起看才成立：巨災損失走高、香港保費仍升、東南亞監管收資本——「風險漲價、需求不減、監管變嚴」同時發生，是本週市場敘事的骨架。細項請點原文或庫內單條，別只引摘要數字。"
  },
  "tags": {
   "sc": ["周报", "巨灾损失", "香港寿险", "印尼", "资本监管"],
   "tc": ["週報", "巨災損失", "香港壽險", "印尼", "資本監管"]
  },
  "actions": {
   "front": {"sc": "客户沟通：市场三条主线的周度归纳", "tc": "客戶溝通：市場三條主線的週度歸納"},
   "midback": {"sc": "数据跟踪：巨灾损失与再保定价", "tc": "數據跟蹤：巨災損失與再保定價"},
   "lead": {"sc": "团队简报：本周市场叙事骨架", "tc": "團隊簡報：本週市場敘事骨架"},
   "cross": {"sc": "跨境客户：印尼资本新规影响", "tc": "跨境客戶：印尼資本新規影響"}
  },
  "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 2},
  "source": {
   "sc": "Insurance Asia 2026-10-31",
   "tc": "Insurance Asia 2026-10-31",
   "name": "insuranceasia", "date": "2026-10-31", "lang": "en"
  },
  "lang": "en",
  "verifyStatus": "pending",
  "clusterCount": 1,
  "ingestedAt": NOW
 },
 {
  "id": "ibm-hcmc-social-insurance-compliance-20261031",
  "publishedAt": "2026-10-31T00:35:00+08:00",
  "originalUrl": "https://www.insurancebusinessmag.com/asia/news/auto-motor/ho-chi-minh-city-moves-to-close-the-compliance-gap-in-its-transport-sector-595687.aspx",
  "sourceKey": "insurancebusinessmag",
  "sourceTier": "media",
  "score": 62,
  "contentKind": "news",
  "boards": ["reg", "market"],
  "themes": ["社保合规", "强制性保险", "越南市场"],
  "title": {
   "sc": "胡志明市拟排查6,787家运输企业社保合规　欠缴近13.6万亿越南盾、逃缴最高罚18-20%",
   "tc": "胡志明市擬排查6,787家運輸企業社保合規　欠繳近13.6萬億越南盾、逃繳最高罰18-20%"
  },
  "summary": {
   "sc": "胡志明市社保机构建议对全市6,787家持牌运输企业系统排查，核查是否为司机及车辆服务人员缴纳强制性社保、医保与失业保险，覆盖32.4万辆许可车辆；并点名以合作合同、服务合同掩盖雇佣关系以规避缴费的做法。截至9月30日三项保险欠缴近13.6万亿越南盾，占全年收入目标8.4%，涉15.8万家单位。2026年9月10日生效的第283/2026号法令把迟缴与故意逃缴分开罚则：少报缴费基数或经提醒仍不缴，按逃缴额18%-20%罚款、上限7,500万越南盾，累犯可移送刑事。[EN原文]",
   "tc": "胡志明市社保機構建議對全市6,787家持牌運輸企業系統排查，核查是否為司機及車輛服務人員繳納強制性社保、醫保與失業保險，覆蓋32.4萬輛許可車輛；並點名以合作合同、服務合同掩蓋僱傭關係以規避繳費的做法。截至9月30日三項保險欠繳近13.6萬億越南盾，佔全年收入目標8.4%，涉15.8萬家單位。2026年9月10日生效的第283/2026號法令把遲繳與故意逃繳分開罰則：少報繳費基數或經提醒仍不繳，按逃繳額18%-20%罰款、上限7,500萬越南盾，累犯可移送刑事。[EN原文]"
  },
  "why": {
   "sc": "东南亚市场的共同剧本：强制险种先立规、再靠「排查＋罚则」落地。越南把社保迟缴与逃缴分档、还设了百分比罚款上限，是可预判执法力度的模板；做跨境客户或大湾区制造业客户的，可据此提醒雇主责任与员工福利的合规缺口。",
   "tc": "東南亞市場的共同劇本：強制險種先立規、再靠「排查＋罰則」落地。越南把社保遲繳與逃繳分檔、還設了百分比罰款上限，是可預判執法力度的模板；做跨境客戶或大灣區製造業客戶的，可據此提醒僱主責任與員工福利的合規缺口。"
  },
  "tags": {
   "sc": ["越南", "社保合规", "强制性保险", "雇主责任", "罚则"],
   "tc": ["越南", "社保合規", "強制性保險", "僱主責任", "罰則"]
  },
  "actions": {
   "front": {"sc": "客户沟通：跨境雇主的合规缺口", "tc": "客戶溝通：跨境僱主的合規缺口"},
   "midback": {"sc": "产品跟踪：员工福利与雇主责任衔接", "tc": "產品跟蹤：員工福利與僱主責任銜接"},
   "lead": {"sc": "团队简报：东南亚强制险执法趋势", "tc": "團隊簡報：東南亞強制險執法趨勢"},
   "cross": {"sc": "跨境客户：越南厂区用工与保险安排", "tc": "跨境客戶：越南廠區用工與保險安排"}
  },
  "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 3},
  "source": {
   "sc": "Insurance Business Asia 2026-10-31",
   "tc": "Insurance Business Asia 2026-10-31",
   "name": "insurancebusinessmag", "date": "2026-10-31", "lang": "en"
  },
  "lang": "en",
  "verifyStatus": "verified",
  "clusterCount": 1,
  "ingestedAt": NOW
 },
 {
  "id": "ian-willis-tilney-departs-20261031",
  "publishedAt": "2026-10-31T15:07:00+08:00",
  "originalUrl": "https://www.insuranceasianews.com/willis-asia-natural-resources-head-nicki-tilney-departs/",
  "sourceKey": "insuranceasianews",
  "sourceTier": "media",
  "score": 60,
  "contentKind": "news",
  "boards": ["market"],
  "themes": ["人事变动", "经纪市场", "自然资源险"],
  "title": {
   "sc": "Willis亚太自然资源险负责人Nicky Tilney离任　任职四年后返英",
   "tc": "Willis亞太自然資源險負責人Nicky Tilney離任　任職四年後返英"
  },
  "summary": {
   "sc": "据 LinkedIn 10月31日更新，Willis 亚太区自然资源业务负责人 Nicky Tilney 在任职四年后离任，将返回英国，下一站未公布。该条位于付费墙后，可核事实仅「离任＋返英」两项。自然资源险覆盖能源、矿业与基建类大型商业风险，区域负责人更替通常伴随经纪业务份额与团队流动。[EN原文]",
   "tc": "據 LinkedIn 10月31日更新，Willis 亞太區自然資源業務負責人 Nicky Tilney 在任職四年後離任，將返回英國，下一站未公布。該條位於付費牆後，可核事實僅「離任＋返英」兩項。自然資源險覆蓋能源、礦業與基建類大型商業風險，區域負責人更替通常伴隨經紀業務份額與團隊流動。[EN原文]"
  },
  "why": {
   "sc": "单看是人事，但自然资源险是亚太少数费率仍在硬的板块，负责人离任往往先体现在团队跟随与存量客户重投。做大型商业险转介的，值得记一笔、等后续团队去向。",
   "tc": "單看是人事，但自然資源險是亞太少數費率仍在硬的板塊，負責人離任往往先體現在團隊跟隨與存量客戶重投。做大型商業險轉介的，值得記一筆、等後續團隊去向。"
  },
  "tags": {
   "sc": ["Willis", "人事变动", "自然资源险", "经纪"],
   "tc": ["Willis", "人事變動", "自然資源險", "經紀"]
  },
  "actions": {
   "front": {"sc": "", "tc": ""},
   "midback": {"sc": "渠道跟踪：经纪团队流动", "tc": "渠道跟蹤：經紀團隊流動"},
   "lead": {"sc": "团队简报：商业险渠道人事", "tc": "團隊簡報：商業險渠道人事"},
   "cross": {"sc": "", "tc": ""}
  },
  "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 0},
  "source": {
   "sc": "InsuranceAsia News 2026-10-31",
   "tc": "InsuranceAsia News 2026-10-31",
   "name": "insuranceasianews", "date": "2026-10-31", "lang": "en"
  },
  "lang": "en",
  "verifyStatus": "verified",
  "clusterCount": 1,
  "ingestedAt": NOW
 },
]

d = json.load(open(LIVE, encoding="utf-8"))
old = d["items"]
have = {i.get("id") for i in old}
urls = {i.get("originalUrl") for i in old}
add = [i for i in items if i["id"] not in have and i["originalUrl"] not in urls]
print("to add:", len(add), [i["id"] for i in add])
d["items"] = add + old
n = len(d["items"])
d.setdefault("meta", {})
d["meta"]["itemCount"] = n
d["meta"]["generatedAt"] = "2026-11-01T01:45:00+08:00"
wn = d["meta"].get("windowNote")
if isinstance(wn, dict):
    wn["sc"] = f"本库{n}条。"
    wn["tc"] = f"本庫{n}條。"
json.dump(d, open(LIVE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("total now:", n)
