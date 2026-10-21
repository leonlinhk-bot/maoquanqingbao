import json, io
from datetime import datetime, timezone, timedelta

HKT = timezone(timedelta(hours=8))
NOW = datetime.now(HKT)
PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(PATH, encoding='utf-8'))
items = d['items']
existing = {i['id'] for i in items}

def it(**kw):
    return kw

new = []

new.append({
 "id": "scmp-offshore-trust-tax-guidance-20261021",
 "publishedAt": "2026-10-21T14:03:00+08:00",
 "originalUrl": "https://www.scmp.com/business/money/wealth/article/3371606/china-eases-uncertainty-over-offshore-trust-taxes-grace-period-ends",
 "sourceKey": "scmp",
 "sourceTier": "media",
 "score": 80,
 "verifyStatus": "verified",
 "contentKind": "news",
 "clusterCount": 1,
 "boards": ["family"],
 "themes": ["offshore-trust", "tax", "cross-border", "wealth"],
 "title": {
   "sc": "内地放宽离岸信托收益征税口径　90 天宽限期今日届满",
   "tc": "內地放寬離岸信託收益徵稅口徑　90 天寬限期今日屆滿"
 },
 "summary": {
   "sc": "内地税务机关在执行离岸信托收益新规时，开始接受「合理解释」，一名港上市内地企业高管称其申诉成功；国家税务总局本周以问答形式说明按国际惯例执行。为期 90 天的宽限期于 10 月 22 日届满，此前争议集中在香港上市架构与股权激励信托。",
   "tc": "內地稅務機關在執行離岸信託收益新規時，開始接受「合理解釋」，一名港上市內地企業高管稱其申訴成功；國家稅務總局本週以問答形式說明按國際慣例執行。為期 90 天的寬限期於 10 月 22 日屆滿，此前爭議集中在香港上市架構與股權激勵信託。"
 },
 "why": {
   "sc": "对做跨境高客的团队，这是「口径松动但未豁免」——谈单话术要从「省税」转为「合规申报＋合理解释留痕」，架构设计须预留税务意见与申报记录，否则宽限期后被动补税的风险仍在客户身上。",
   "tc": "對做跨境高客的團隊，這是「口徑鬆動但未豁免」——談單話術要從「省稅」轉為「合規申報＋合理解釋留痕」，架構設計須預留稅務意見與申報記錄，否則寬限期後被動補稅的風險仍在客戶身上。"
 },
 "source": {
   "sc": "South China Morning Post 2026-10-21（Themis Qi）",
   "tc": "South China Morning Post 2026-10-21（Themis Qi）",
   "lang": "en",
   "name": "scmp",
   "date": "2026-10-21"
 },
 "tags": {
   "sc": ["离岸信托", "税务合规", "跨境高客", "股权激励"],
   "tc": ["離岸信託", "稅務合規", "跨境高客", "股權激勵"]
 },
 "actions": {
   "front": {"sc": "客户沟通：口径放宽≠豁免，申报与解释要留痕", "tc": "客戶溝通：口徑放寬≠豁免，申報與解釋要留痕"},
   "midback": {"sc": "合规留痕：留存税务意见与申报往来文件", "tc": "合規留痕：留存稅務意見與申報往來文件"},
   "lead": {"sc": "团队简报：信托＋保单的税务衔接复盘", "tc": "團隊簡報：信託＋保單的稅務銜接復盤"},
   "cross": {"sc": "跨境架构：信托、保单与申报主体税基对齐", "tc": "跨境架構：信託、保單與申報主體稅基對齊"}
 },
 "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 3}
})

new.append({
 "id": "ibm-singapore-haze-banks-investors-do-20261021",
 "publishedAt": "2026-10-21",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/catastrophe/singapore-signals-it-will-pursue-banks-and-investors-linked-to-indonesias-haze-fires-594247.aspx",
 "sourceKey": "insurancebusinessmag",
 "sourceTier": "pro",
 "score": 72,
 "verifyStatus": "verified",
 "contentKind": "news",
 "clusterCount": 1,
 "boards": ["product"],
 "themes": ["d-and-o", "environmental", "cross-border", "enforcement"],
 "title": {
   "sc": "新加坡拟追究印尼雾霾相关银行与投资者　上市公司 D&O 与环责险受检视",
   "tc": "新加坡擬追究印尼霧霾相關銀行與投資者　上市公司 D&O 與環責險受檢視"
 },
 "summary": {
   "sc": "新加坡当局表示正考虑以新法例及财务制裁，追究与印尼雾霾火点有关的在新上市公司、为其融资的银行与投资者；相关企业的董事责任、环境责任与供应链保障范围因此被重新检视，焦点在罚款与故意违法能否获赔。",
   "tc": "新加坡當局表示正考慮以新法例及財務制裁，追究與印尼霧霾火點有關的在新上市公司、為其融資的銀行與投資者；相關企業的董事責任、環境責任與供應鏈保障範圍因此被重新檢視，焦點在罰款與故意違法能否獲賠。"
 },
 "why": {
   "sc": "跨境客户的 D&O 与环责险能否赔，取决于「罚款/故意违法/漂绿」等除外条款与通知义务。这类跨境执法一出现，先核保单除外、再谈加保，比事后争论便宜得多。",
   "tc": "跨境客戶的 D&O 與環責險能否賠，取決於「罰款／故意違法／漂綠」等除外條款與通知義務。這類跨境執法一出現，先核保單除外、再談加保，比事後爭論便宜得多。"
 },
 "source": {
   "sc": "Insurance Business Asia 2026-10-21（Mav Rodriguez）",
   "tc": "Insurance Business Asia 2026-10-21（Mav Rodriguez）",
   "lang": "en",
   "name": "insurancebusinessmag",
   "date": "2026-10-21"
 },
 "tags": {
   "sc": ["D&O", "环境责任", "新加坡", "跨境执法"],
   "tc": ["D&O", "環境責任", "新加坡", "跨境執法"]
 },
 "actions": {
   "front": {"sc": "客户沟通：先问供应链与印尼敞口", "tc": "客戶溝通：先問供應鏈與印尼敞口"},
   "midback": {"sc": "核保资料：核对除外条款与通知义务", "tc": "核保資料：核對除外條款與通知義務"},
   "lead": {"sc": "团队简报：环责＋D&O 联动案例", "tc": "團隊簡報：環責＋D&O 聯動案例"},
   "cross": {"sc": "跨境架構：新马投资主体的董事责任", "tc": "跨境架構：新馬投資主體的董事責任"}
 },
 "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 2}
})

new.append({
 "id": "rn-generali-org-restructure-20261021",
 "publishedAt": "2026-10-21",
 "originalUrl": "https://www.reinsurancene.ws/generali-unveils-new-organisational-structure/",
 "sourceKey": "reinsurancenews",
 "sourceTier": "pro",
 "score": 70,
 "verifyStatus": "verified",
 "contentKind": "news",
 "clusterCount": 1,
 "boards": ["insurer"],
 "themes": ["org-change", "asia", "strategy"],
 "title": {
   "sc": "忠意集团 11 月起重组架构　2027 年亚洲区由 Roberto Leonardi 领军",
   "tc": "忠意集團 11 月起重組架構　2027 年亞洲區由 Roberto Leonardi 領軍"
 },
 "summary": {
   "sc": "忠意董事会通过「Lifetime Partner 27」收尾阶段的组织调整：11 月 2 日起取消总经理一职，职能并入副 CEO Terzariol；2027 年 1 月起保险市场分五个大区，亚洲区由 Roberto Leonardi 负责，并新设集团保险与业务表现、Redion 援助与雇员福利平台。",
   "tc": "忠意董事會通過「Lifetime Partner 27」收尾階段的組織調整：11 月 2 日起取消總經理一職，職能併入副 CEO Terzariol；2027 年 1 月起保險市場分五個大區，亞洲區由 Roberto Leonardi 負責，並新設集團保險與業務表現、Redion 援助與僱員福利平台。"
 },
 "why": {
   "sc": "集团重组先动汇报线，再动产品与再保安排。与忠意香港有业务往来的经纪，值得提前摸清亚洲区新决策口径与再保、雇员福利两条线的接口，避免续保期问错人。",
   "tc": "集團重組先動匯報線，再動產品與再保安排。與忠意香港有業務往來的經紀，值得提前摸清亞洲區新決策口徑與再保、僱員福利兩條線的接口，避免續保期問錯人。"
 },
 "source": {
   "sc": "Reinsurance News 2026-10-21（Saumya Jain）",
   "tc": "Reinsurance News 2026-10-21（Saumya Jain）",
   "lang": "en",
   "name": "reinsurancenews",
   "date": "2026-10-21"
 },
 "tags": {
   "sc": ["忠意", "组织架构", "亚洲区", "集团战略"],
   "tc": ["忠意", "組織架構", "亞洲區", "集團戰略"]
 },
 "actions": {
   "front": {"sc": "客户沟通：集团评级与偿付能力未变", "tc": "客戶溝通：集團評級與償付能力未變"},
   "midback": {"sc": "供应商尽调：更新联系人矩阵", "tc": "供應商盡調：更新聯繫人矩陣"},
   "lead": {"sc": "团队简报：亚洲区新汇报线", "tc": "團隊簡報：亞洲區新匯報線"},
   "cross": {"sc": "跨境架构：集团内再保与自保接口", "tc": "跨境架構：集團內再保與自保接口"}
 },
 "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 1}
})

new.append({
 "id": "rn-hci-tokenised-reinsurance-isaias-20261021",
 "publishedAt": "2026-10-21",
 "originalUrl": "https://www.reinsurancene.ws/hcis-reinsurance-tower-and-token-affected-after-claims-from-hurricane-isaias-hit/",
 "sourceKey": "reinsurancenews",
 "sourceTier": "pro",
 "score": 72,
 "verifyStatus": "verified",
 "contentKind": "news",
 "clusterCount": 1,
 "boards": ["tech"],
 "themes": ["ils", "tokenisation", "cat-risk", "claims"],
 "title": {
   "sc": "HCI：飓风 Isaias 理赔触及第三层再保　代币化再保 Token B 同受影响",
   "tc": "HCI：颶風 Isaias 理賠觸及第三層再保　代幣化再保 Token B 同受影響"
 },
 "summary": {
   "sc": "美国坦帕 HCI 确认三层再保中仅第三层（佛州北部，自留 1,500 万美元）被 Isaias 理赔触及，其代币化再保 Token B 虽受影响但仍保持盈利。该飓风 10 月 9 日以二级登陆佛州，各模型估行业保险损失 25 亿至 45 亿美元。",
   "tc": "美國坦帕 HCI 確認三層再保中僅第三層（佛州北部，自留 1,500 萬美元）被 Isaias 理賠觸及，其代幣化再保 Token B 雖受影響但仍保持盈利。該颶風 10 月 9 日以二級登陸佛州，各模型估行業保險損失 25 億至 45 億美元。"
 },
 "why": {
   "sc": "代币化再保首次被真实巨灾理赔检验：链上分润不能脱离再保条款，触发点、自留与流动性仍按传统结构走。想用 ILS 概念做高客另类配置的团队，这是现成且中性的风险教育案例。",
   "tc": "代幣化再保首次被真實巨災理賠檢驗：鏈上分潤不能脫離再保條款，觸發點、自留與流動性仍按傳統結構走。想用 ILS 概念做高客另類配置的團隊，這是現成且中性的風險教育案例。"
 },
 "source": {
   "sc": "Reinsurance News 2026-10-21（Saumya Jain）",
   "tc": "Reinsurance News 2026-10-21（Saumya Jain）",
   "lang": "en",
   "name": "reinsurancenews",
   "date": "2026-10-21"
 },
 "tags": {
   "sc": ["ILS", "代币化", "巨灾风险", "理赔"],
   "tc": ["ILS", "代幣化", "巨災風險", "理賠"]
 },
 "actions": {
   "front": {"sc": "客户沟通：另类配置须讲触发机制", "tc": "客戶溝通：另類配置須講觸發機制"},
   "midback": {"sc": "产品审查：条款与流动性披露", "tc": "產品審查：條款與流動性披露"},
   "lead": {"sc": "团队简报：代币化再保实况", "tc": "團隊簡報：代幣化再保實況"},
   "cross": {"sc": "跨境架构：ILS 持仓的合规申报", "tc": "跨境架構：ILS 持倉的合規申報"}
 },
 "rolesImpact": {"front": 1, "midback": 1, "lead": 1, "cross": 1}
})

new.append({
 "id": "artemis-usaa-residential-re-2026-2-upsize-20261021",
 "publishedAt": "2026-10-21",
 "originalUrl": "https://www.artemis.bm/news/usaa-lifts-residential-re-2026-2-cat-bond-target-to-350m-as-price-guidance-drops/",
 "sourceKey": "artemis",
 "sourceTier": "pro",
 "score": 70,
 "verifyStatus": "verified",
 "contentKind": "news",
 "clusterCount": 1,
 "boards": ["market"],
 "themes": ["cat-bond", "pricing", "capacity"],
 "title": {
   "sc": "USAA 巨灾债券目标上调 56% 至 3.5 亿美元　三档价格指引同步下调",
   "tc": "USAA 巨災債券目標上調 56% 至 3.5 億美元　三檔價格指引同步下調"
 },
 "summary": {
   "sc": "USAA 的 Residential Re 2026-2 发行目标由 2.25 亿上调 56% 至 3.5 亿美元，三档票据价格指引同步下调，提供 2026 年 12 月至 2030 年 11 月的四年期一次事故型多灾因再保；大西洋飓风季至今无重大损失，巨灾债基金现金充裕。",
   "tc": "USAA 的 Residential Re 2026-2 發行目標由 2.25 億上調 56% 至 3.5 億美元，三檔票據價格指引同步下調，提供 2026 年 12 月至 2030 年 11 月的四年期一次事故型多災因再保；大西洋颶風季至今無重大損失，巨災債基金現金充裕。"
 },
 "why": {
   "sc": "一级市场「扩容＋降价」是资本过剩最直接的读数。这股定价压力会经 1 月再保续约传导到港险公司的再保成本与产品定价——客户问「保费会否回落」，可用它作硬证据，而不是猜。",
   "tc": "一級市場「擴容＋降價」是資本過剩最直接的讀數。這股定價壓力會經 1 月再保續約傳導到港險公司的再保成本與產品定價——客戶問「保費會否回落」，可用它作硬證據，而不是猜。"
 },
 "source": {
   "sc": "Artemis 2026-10-21（Steve Evans）",
   "tc": "Artemis 2026-10-21（Steve Evans）",
   "lang": "en",
   "name": "artemis",
   "date": "2026-10-21"
 },
 "tags": {
   "sc": ["巨灾债券", "再保定价", "承保能力", "美国"],
   "tc": ["巨災債券", "再保定價", "承保能力", "美國"]
 },
 "actions": {
   "front": {"sc": "客户沟通：再保成本下行的证据", "tc": "客戶溝通：再保成本下行的證據"},
   "midback": {"sc": "核保资料：续保定价参考", "tc": "核保資料：續保定價參考"},
   "lead": {"sc": "团队简报：1 月续保前瞻", "tc": "團隊簡報：1 月續保前瞻"},
   "cross": {"sc": "跨境架构：另类资本配置视角", "tc": "跨境架構：另類資本配置視角"}
 },
 "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 1}
})

new.append({
 "id": "rn-chubb-9m26-pc-underwriting-record-20261021",
 "publishedAt": "2026-10-21",
 "originalUrl": "https://www.reinsurancene.ws/chubb-posts-record-5-79bn-pc-underwriting-income-for-first-9m-26/",
 "sourceKey": "reinsurancenews",
 "sourceTier": "pro",
 "score": 70,
 "verifyStatus": "verified",
 "contentKind": "news",
 "clusterCount": 1,
 "boards": ["insurer"],
 "themes": ["earnings", "p-and-c", "combined-ratio"],
 "title": {
   "sc": "安达首九月产险承保利润 57.9 亿美元创新高　Q3 综合成本率升至 84.1%",
   "tc": "安達首九月產險承保利潤 57.9 億美元創新高　Q3 綜合成本率升至 84.1%"
 },
 "summary": {
   "sc": "安达 2026 年首九月产险承保利润 57.9 亿美元、同比增 33.7%，综合成本率 84%，毛保费 528.6 亿美元增 4.8%。单季 Q3 承保利润跌 8.8% 至 20.6 亿美元，综合成本率由 81.8% 升至 84.1%，税前巨灾损失 7.05 亿美元（上年 2.85 亿）。",
   "tc": "安達 2026 年首九月產險承保利潤 57.9 億美元、同比增 33.7%，綜合成本率 84%，毛保費 528.6 億美元增 4.8%。單季 Q3 承保利潤跌 8.8% 至 20.6 億美元，綜合成本率由 81.8% 升至 84.1%，稅前巨災損失 7.05 億美元（上年 2.85 億）。"
 },
 "why": {
   "sc": "累计承保利润创高、单季成本率却明显转差，说明「费率下行＋巨灾损失正常化」的剪刀差正在形成。向客户解释加保、自留或转嫁安排时，同业成本率与巨灾损失是最好用的硬数据。",
   "tc": "累計承保利潤創高、單季成本率卻明顯轉差，說明「費率下行＋巨災損失正常化」的剪刀差正在形成。向客戶解釋加保、自留或轉嫁安排時，同業成本率與巨災損失是最好用的硬數據。"
 },
 "source": {
   "sc": "Reinsurance News 2026-10-21（Kane Wells）",
   "tc": "Reinsurance News 2026-10-21（Kane Wells）",
   "lang": "en",
   "name": "reinsurancenews",
   "date": "2026-10-21"
 },
 "tags": {
   "sc": ["安达", "承保利润", "综合成本率", "巨灾损失"],
   "tc": ["安達", "承保利潤", "綜合成本率", "巨災損失"]
 },
 "actions": {
   "front": {"sc": "客户沟通：用成本率解释加保必要性", "tc": "客戶溝通：用成本率解釋加保必要性"},
   "midback": {"sc": "核保资料：同业成本率对标", "tc": "核保資料：同業成本率對標"},
   "lead": {"sc": "团队简报：费率与损失剪刀差", "tc": "團隊簡報：費率與損失剪刀差"},
   "cross": {"sc": "跨境架构：跨国客户自留层级调整", "tc": "跨境架構：跨國客戶自留層級調整"}
 },
 "rolesImpact": {"front": 2, "midback": 1, "lead": 1, "cross": 1}
})

added = []
for n in new:
    if n['id'] in existing:
        print('SKIP dup', n['id'])
        continue
    n['ingestedAt'] = NOW.isoformat(timespec='seconds')
    added.append(n)

items[:0] = added
d['meta']['generatedAt'] = NOW.isoformat(timespec='seconds')
d['meta']['itemCount'] = len(items)
d['meta']['windowNote'] = {
  'sc': f"本库{len(items)}条。",
  'tc': f"本庫{len(items)}條。"
}
json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('added', len(added), 'total', len(items))
for a in added:
    print(' +', a['id'])
