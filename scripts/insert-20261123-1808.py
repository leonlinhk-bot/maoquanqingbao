import json
from datetime import datetime, timezone, timedelta

PATH = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(PATH, encoding='utf-8'))
items = d['items']
existing = {i['id'] for i in items} | {i.get('originalUrl', '') for i in items}

now = datetime.now(timezone(timedelta(hours=8))).replace(second=0, microsecond=0)

new = []

# ---------- 1. WTW 2027 Global Medical Trends — 香港 ----------
new.append({
 "id": "insuranceasia-wtw-medical-trend-2027-hk-20261123",
 "clusterCount": 1,
 "score": 76,
 "verifyStatus": "verified",
 "sourceTier": "pro",
 "sourceKey": "insuranceasia",
 "contentKind": "research",
 "title": {
  "sc": "WTW：香港医疗险净成本 2027 年预计升 8.6%　高于今年的 7.9%",
  "tc": "WTW：香港醫療險淨成本 2027 年預計升 8.6%　高於今年的 7.9%"
 },
 "summary": {
  "sc": "韋萊韜悅（WTW）11 月 23 日发布 2027 全球医疗趋势调查：香港净医疗险成本预计 2027 年升 8.6%，高于今年的 7.9%；毛费率则由 10% 升至 10.4%，本地通胀预测为 1.8%。亚太区净成本在五大区域中最高，今年 9.8%、2027 年预计 10.1%。香港主要推手为医护人手短缺、服务使用率与索偿频率上升，以及癌症长期治疗费用；报告指癌症亦是亚太区推高医疗险成本的首要慢性病。管理手段集中在扩大预防性筛查、加强慢病管理与健康福利投入。WTW 另提醒留意港人北上及大湾区就医用量上升，可能进一步带动本地医疗成本。",
  "tc": "韋萊韜悅（WTW）11 月 23 日發布 2027 全球醫療趨勢調查：香港淨醫療險成本預計 2027 年升 8.6%，高於今年的 7.9%；毛費率則由 10% 升至 10.4%，本地通脹預測為 1.8%。亞太區淨成本在五大區域中最高，今年 9.8%、2027 年預計 10.1%。香港主要推手為醫護人手短缺、服務使用率與索償頻率上升，以及癌症長期治療費用；報告指癌症亦是亞太區推高醫療險成本的首要慢性病。管理手段集中在擴大預防性篩查、加強慢病管理與健康福利投入。WTW 另提醒留意港人北上及大灣區就醫用量上升，可能進一步帶動本地醫療成本。"
 },
 "why": {
  "sc": "醫療險續保加價這幾年一直是前線最難解釋的一環：客戶問「為什麼又加」，若只答「公司調整」就等於把信任讓出去。這份調查給了一個可引用的第三方口徑——香港明年淨成本 8.6%、毛率 10.4%、通脹只有 1.8%，也就是說保費升幅與本地物價脫鈎，主要由醫療服務端的價格與用量推動。把它講清楚，加價溝通就從「爭取體諒」變成「共同面對一個已知的結構問題」，也順勢帶出自付額、病房級別、地區範圍這些可調節的設計。",
  "tc": "醫療險續保加價這幾年一直是前線最難解釋的一環：客戶問「為什麼又加」，若只答「公司調整」就等於把信任讓出去。這份調查給了一個可引用的第三方口徑——香港明年淨成本 8.6%、毛率 10.4%、通脹只有 1.8%，也就是說保費升幅與本地物價脫鈎，主要由醫療服務端的價格與用量推動。把它講清楚，加價溝通就從「爭取體諒」變成「共同面對一個已知的結構問題」，也順勢帶出自付額、病房級別、地區範圍這些可調節的設計。"
 },
 "actions": {
  "front": {"sc": "續保加價溝通先給結論：明年全港醫療險淨成本預計升 8.6%，你保單的加幅要放在這個背景下看", "tc": "續保加價溝通先給結論：明年全港醫療險淨成本預計升 8.6%，你保單的加幅要放在這個背景下看"},
  "midback": {"sc": "做一張「本地醫療通脹 vs 主要醫療險近年加幅」對照表，作為續保季節的標準話術底稿", "tc": "做一張「本地醫療通脹 vs 主要醫療險近年加幅」對照表，作為續保季節的標準話術底稿"},
  "lead": {"sc": "培訓切入：能把醫療通脹講清楚的人，才留得住長期醫療險客戶", "tc": "培訓切入：能把醫療通脹講清楚的人，才留得住長期醫療險客戶"},
  "cross": {"sc": "團體醫療（僱員福利）客戶可用香港 8.6% 與亞太 10.1% 的對比談明年福利預算", "tc": "團體醫療（僱員福利）客戶可用香港 8.6% 與亞太 10.1% 的對比談明年福利預算"}
 },
 "rolesImpact": {"front": 3, "midback": 2, "lead": 2, "cross": 3},
 "source": {"sc": "Insurance Asia（引 WTW 2027 全球醫療趨勢調查）", "lang": "en"},
 "boards": ["product", "market"],
 "themes": ["medical-inflation", "employee-benefits", "greater-bay-area"],
 "tags": {"sc": ["WTW", "医疗通胀", "医疗险", "大湾区", "雇员福利"], "tc": ["WTW", "醫療通脹", "醫療險", "大灣區", "僱員福利"]},
 "publishedAt": "2026-11-23T11:35:00+08:00",
 "originalUrl": "https://insuranceasia.com/insurance/news/hong-kong-medical-insurance-costs-climb-86-in-2027"
})

# ---------- 2. Zurich × St. Gallen — AI Resilience Challenge ----------
new.append({
 "id": "ibm-zurich-ai-resilience-correlation-20261123",
 "clusterCount": 1,
 "score": 68,
 "verifyStatus": "verified",
 "sourceTier": "media",
 "sourceKey": "insurancebusinessmag",
 "contentKind": "research",
 "title": {
  "sc": "苏黎世×圣加仑大学：换 AI 供应商不等于分散风险　相关性风险更难察觉 [EN原文]",
  "tc": "蘇黎世×聖加侖大學：換 AI 供應商不等於分散風險　相關性風險更難察覺 [EN原文]"
 },
 "summary": {
  "sc": "蘇黎世保險集團與瑞士聖加侖大學 11 月 23 日發布《The AI Resilience Challenge》，基於 2026 年 7 至 9 月對 50 位專家的訪談，指 AI 損失沿兩條路徑擴散：一是較易理解的集中度風險（共用供應商、模型或基礎設施）；二是更難察覺的相關性風險——不同系統因共享訓練數據、架構或決策規則，在沒有共同故障點的情況下以相似方式失效，往往經由索償、投訴、監管行動或訴訟才浮現。結論是客戶即使更換或同時採用多套 AI 系統，底層風險仍可能與同業高度相關，商業險「分散即獨立」的傳統假設因此失效。研究建議企業把 AI 依賴圖譜延伸到直接供應商之外、明確 AI 決策問責、並測試關鍵活動在系統失效或需人工接管時能否持續。",
  "tc": "蘇黎世保險集團與瑞士聖加侖大學 11 月 23 日發布《The AI Resilience Challenge》，基於 2026 年 7 至 9 月對 50 位專家的訪談，指 AI 損失沿兩條路徑擴散：一是較易理解的集中度風險（共用供應商、模型或基礎設施）；二是更難察覺的相關性風險——不同系統因共享訓練數據、架構或決策規則，在沒有共同故障點的情況下以相似方式失效，往往經由索償、投訴、監管行動或訴訟才浮現。結論是客戶即使更換或同時採用多套 AI 系統，底層風險仍可能與同業高度相關，商業險「分散即獨立」的傳統假設因此失效。研究建議企業把 AI 依賴圖譜延伸到直接供應商之外、明確 AI 決策問責、並測試關鍵活動在系統失效或需人工接管時能否持續。"
 },
 "why": {
  "sc": "AI 風險過去在企業客戶口中常被簡化成「我們沒有用 OpenAI」或「我們有兩家供應商」，這份研究正是拆掉這個自我安慰：相關性風險來自共同的訓練數據與決策邏輯，換牌子換不掉。對前線的價值是入場券——用一句「換供應商不等於分散風險」就能把話題從產品比較拉到客戶的 AI 治理與保障缺口；對 ZUU 內部的 AI 培訓也一樣好用，因為它講的是組合風險，而不是單一工具風險。",
  "tc": "AI 風險過去在企業客戶口中常被簡化成「我們沒有用 OpenAI」或「我們有兩家供應商」，這份研究正是拆掉這個自我安慰：相關性風險來自共同的訓練數據與決策邏輯，換牌子換不掉。對前線的價值是入場券——用一句「換供應商不等於分散風險」就能把話題從產品比較拉到客戶的 AI 治理與保障缺口；對 ZUU 內部的 AI 培訓也一樣好用，因為它講的是組合風險，而不是單一工具風險。"
 },
 "actions": {
  "front": {"sc": "見企業客戶先問一句：你們的 AI 依賴有沒有延伸到供應商之外？再談保單缺口", "tc": "見企業客戶先問一句：你們的 AI 依賴有沒有延伸到供應商之外？再談保單缺口"},
  "midback": {"sc": "把「集中度風險 vs 相關性風險」做成一頁圖，放進企業客戶提案的 AI 章節", "tc": "把「集中度風險 vs 相關性風險」做成一頁圖，放進企業客戶提案的 AI 章節"},
  "lead": {"sc": "培訓素材：講「AI 是組合風險而非單一工具風險」最權威的公開研究之一", "tc": "培訓素材：講「AI 是組合風險而非單一工具風險」最權威的公開研究之一"},
  "cross": {"sc": "與律師、IT 審計方聯合服務時，可用它解釋為何要把 AI 條款寫進專業責任與網絡險", "tc": "與律師、IT 審計方聯合服務時，可用它解釋為何要把 AI 條款寫進專業責任與網絡險"}
 },
 "rolesImpact": {"front": 2, "midback": 3, "lead": 2, "cross": 3},
 "source": {"sc": "Insurance Business Asia（引蘇黎世保險集團與聖加侖大學研究）", "lang": "en"},
 "boards": ["tech"],
 "themes": ["ai-governance", "correlation-risk", "commercial-lines"],
 "tags": {"sc": ["苏黎世", "AI 风险", "相关性风险", "企业险", "治理"], "tc": ["蘇黎世", "AI 風險", "相關性風險", "企業險", "治理"]},
 "publishedAt": "2026-11-23T16:00:00+08:00",
 "originalUrl": "https://www.insurancebusinessmag.com/asia/news/technology/switching-ai-providers-does-not-make-clients-risks-independent-598365.aspx"
})

added = []
for it in new:
    if it['id'] in existing or it['originalUrl'] in existing:
        print('SKIP dup:', it['id'])
        continue
    added.append(it)

d['items'] = added + items
d['meta']['generatedAt'] = now.isoformat()
d['meta']['itemCount'] = len(d['items'])
if 'windowNote' in d['meta']:
    n = len(d['items'])
    d['meta']['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}

json.dump(d, open(PATH, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('added', len(added), 'total', len(d['items']))
for it in added:
    print(' +', it['publishedAt'], it['sourceKey'], it['title']['sc'][:50])
