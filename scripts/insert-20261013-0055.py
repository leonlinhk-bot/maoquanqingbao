#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-13 00:5x increment into live-items.json.

窗口：2026-10-12T18:22（18:08 轮）→ 2026-10-13T00:55（21:08 轮延迟补跑）。
本期新增 5 条：
  artemis 2（ILS Bermuda 百慕达 ILS 枢纽、飓风 Simon 未触墨西哥参数式巨灾债券）
  scmp 1（港交所 CEO：扩展指数／衍生品／人民币计价产品）
  insuranceasia 1（补漏 10-12 05:45：安盛新加坡旅游保障额度）
  insurancebusinessmag 1（H&M 网络攻击指控、ASOS 外泄凸显第三方平台暴露）
无新发布信源：IA（通函最新 2026-10-02；新闻稿页 Cloudflare 拦截，经搜索核对无新）、
  HKMA（最新 2026-10-08）、AIA（最新 10-09）、Manulife/AXA/SunLife/Prudential HK（新闻室无新）、
  insuranceasianews（最新 10-12 15:18，已于 18:08 轮收录）、govhk（10 条新但均非保险相关）、
  NFRA（最新 10-09）、HKFI（最新 2026-09-16）、FSTB。
"""
import json
from datetime import datetime, timezone, timedelta

try:
    import zhconv
    def T(s):
        return zhconv.convert(s, 'zh-hant')
except Exception:  # pragma: no cover
    def T(s):
        return s

NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
CR = {"sc": "本站导读", "tc": "本站導讀"}


def TC(x):
    s = x[0] if isinstance(x, (tuple, list)) else x
    return T(s)


def mk(id_, sourceKey, tier, kind, pub, url, t, s, w, a_f, a_m, a_l, a_c, ri, boards, themes,
       tags, src, lang, score, verify='pending'):
    return {
        "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": sourceKey, "contentKind": kind,
        "actions": {
            "front": {"sc": a_f[0] if isinstance(a_f, (tuple, list)) else a_f, "tc": TC(a_f)},
            "midback": {"sc": a_m[0] if isinstance(a_m, (tuple, list)) else a_m, "tc": TC(a_m)},
            "lead": {"sc": a_l[0] if isinstance(a_l, (tuple, list)) else a_l, "tc": TC(a_l)},
            "cross": {"sc": a_c[0] if isinstance(a_c, (tuple, list)) else a_c, "tc": TC(a_c)},
        },
        "rolesImpact": {"front": ri[0], "midback": ri[1], "lead": ri[2], "cross": ri[3]},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags, "tc": [T(x) for x in tags]},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": t, "tc": T(t)},
        "summary": {"sc": s, "tc": T(s)},
        "why": {"sc": w, "tc": T(w)},
        "source": {"sc": src[0], "tc": T(src[0]), "lang": lang, "name": src[2],
                   "date": src[3], "note": src[4] if len(src) > 4 else None},
    }


ITEMS = []

# ══ 1. ILS Bermuda：百慕达续居全球 ILS 枢纽 ══
ITEMS.append(mk(
    "artemis-bermuda-ils-market-development-ils-bermuda-20261012",
    "artemis", "pro", "news",
    "2026-10-12T21:00:33+08:00",
    "https://www.artemis.bm/news/bermuda-advances-insurance-linked-securities-market-development-as-sector-expands-ils-bermuda/",
    "ILS Bermuda：全球ILS市場持續擴張　百慕達續居巨災債券與另類風險轉移的設立、監管及上市樞紐",
    "Artemis 於10月12日報道，行業組織 ILS Bermuda 指出，保險相連證券（ILS）作為再保險資本的基礎來源，持續在產品、地區與風險類型上擴張；百慕達憑藉成熟再保險市場、專業服務供應商、比例相稱（proportionate）的監管框架及資本市場基建，在巨災債券、特殊目的保險人（SPI）、抵押再保險及側車（sidecar）等結構的設立、監管、管理與上市方面維持領先地位，並能支持新興形式的風險轉移。ILS Bermuda 亦指市場已明顯擴展至美國颶風以外的新興風險類型；該組織為業界年度大會 Convergence 的主辦方，會議於本周舉行。 [EN原文]",
    "香港正推動巨災債券／ILS 生態與專屬自保，並在五年規劃及《施政報告》下強化風險管理中心定位；百慕達是國際 ILS 的基準市場，其「可預期監管框架＋專業服務生態＋上市基建」是直接對照面。理解對手為何留住發行人與投資者，可用於內部政策討論與向企業客解釋 captive 與 ILS 工具的分工，而非只講單一產品。",
    "與企業客談風險轉移工具時的區域對照",
    "ILS／巨災債券基礎知識補強",
    "團隊分享：ILS 生態與香港風險管理中心定位",
    "香港巨災債券與專屬自保政策的國際參照",
    (1, 2, 3, 2), ["market", "reg"], ["ils", "catastrophe-bond", "captive", "risk-hub"],
    ["ILS", "百慕达", "巨灾债券", "专属自保", "风险枢纽"],
    ("Artemis.bm 2026-10-12 报道", "Artemis.bm 2026-10-12 報道",
     "Artemis.bm", "2026-10-12", "EN原文；Convergence 年会本周举行"),
    "en", 70, "verified"))

# ══ 2. 飓风 Simon 未触及墨西哥参数式巨灾债券触发区 ══
ITEMS.append(mk(
    "artemis-hurricane-simon-mexico-catbond-trigger-zones-loconte-20261012",
    "artemis", "pro", "news",
    "2026-10-12T19:37:58+08:00",
    "https://www.artemis.bm/news/hurricane-simon-track-remained-outside-of-mexico-cat-bond-parametric-trigger-zones-loconte/",
    "Artemis：颶風Simon路徑西移　似未進入墨西哥1.75億美元參數式巨災債券觸發框　料賠付不會到來",
    "Artemis 於10月12日報道，引述資產管理公司 Azimut Switzerland 的 ILS 投資專員 Isacco Loconte 分析，指四級颶風 Simon 路徑西移後，似一直停留於國際復興開發銀行（IBRD）「CAR Mexico 2024（Pacific）」1.75億美元參數式巨災債券的參數觸發框（parametric trigger boxes）之外。雖然 Simon 的最低中心氣壓曾降至足以觸發賠付的水平（前提是路徑須進入參數框），屬「非常接近」的一次，但以美國國家颶風中心（NHC）初步路徑數據插值計算，Simon 似未接近至觸發該債券，初步顯示不會有賠付。 [EN原文]",
    "承接周末該債券「觸發與否」的懸念，本條為事件初步定調（料無賠付）。對前線的實用價值：一是更新與客戶／團隊談參數式（parametric）與賠償式（indemnity）風險轉移時可用的完整案例；二是再次說明參數產品的基差風險（basis risk）——風暴強度足夠，但路徑差之毫釐便不觸發，客戶對參數式保障範圍與定價的預期需要校準。",
    "客戶談天災／參數式保障時的案例更新",
    "追蹤 ILS 基金與巨災債券觸發對表現的影響",
    "團隊分享：參數式觸發機制與基差風險",
    "香港發展 ILS 市場的國際案例參照",
    (1, 2, 2, 2), ["market"], ["ils", "catastrophe-bond", "parametric", "natural-catastrophe"],
    ["飓风Simon", "墨西哥", "巨灾债券", "参数式", "ILS"],
    ("Artemis.bm 2026-10-12 报道", "Artemis.bm 2026-10-12 報道",
     "Artemis.bm", "2026-10-12", "EN原文；IBRD CAR Mexico 2024 (Pacific) 1.75 亿美元"),
    "en", 70, "verified"))

# ══ 3. 港交所 CEO：扩展指数、衍生品与人民币计价产品 ══
ITEMS.append(mk(
    "scmp-hkex-ceo-indices-derivatives-yuan-20261012",
    "scmp", "media", "news",
    "2026-10-12T19:07:25+08:00",
    "https://www.scmp.com/business/markets/article/3370617/hong-kong-expand-indices-derivatives-and-yuan-denominated-products-hkex-ceo",
    "港交所CEO：將擴展指數、衍生品及人民幣計價產品　涵蓋人民幣黃金期貨與人民幣計價股票交易",
    "《南華早報》10月12日報道，香港交易所（HKEX）行政總裁於周一發表的網誌表示，將推出進一步措施以提升市場流動性、吸引更多國際投資者，並擴大人民幣的應用，具體包括人民幣計價的黃金期貨及人民幣計價股票交易。相關計劃承接《施政報告》及香港五年規劃下鞏固國際金融中心地位的重點方向。 [EN原文]",
    "香港資本市場深化（人民幣計價產品、衍生品擴容）是保險資金與高客資產配置的底層基建變化：一是產品供給增加，持有人民幣資產或以人民幣為負債幣種的客戶，對沖與收益工具選擇更闊；二是壽險長期負債的資產端與本地市場深度直接相關，屬與高客及家族辦公室談資產配置時的宏觀背景，可與香港保險資金運用及 RBC 討論相連。",
    "高客資產配置話題：香港市場深度提升",
    "留意人民幣計價工具供給的變化",
    "團隊分享：金融基建與客戶配置邏輯",
    "與保險資金運用及 RBC 的關聯討論",
    (1, 1, 2, 2), ["market", "family"], ["hong-kong", "capital-markets", "rmb", "family-office"],
    ["港交所", "人民币", "衍生品", "金融市场", "资产配置"],
    ("南华早报（SCMP） 2026-10-12 报道", "南華早報（SCMP） 2026-10-12 報道",
     "South China Morning Post", "2026-10-12", "EN原文；HKEX 行政总裁网志"),
    "en", 62, "verified"))

# ══ 4. 安盛新加坡旅游保障（10-12 补漏） ══
ITEMS.append(mk(
    "iaasia-allianz-travel-protect-delay-cover-20261012",
    "insuranceasia", "pro", "news",
    "2026-10-12T05:45:00+08:00",
    "https://insuranceasia.com/insurance/news/allianz-travel-insurance-covers-delays-2310",
    "安盛新加坡推旅遊保障　航班延誤賠付上限2,310美元、海外醫療保障最高154萬美元",
    "Insurance Asia 10月12日報道，安盛（Allianz）新加坡指旅遊中斷情況在2025年初改善後再度趨頻，成因包括旅遊需求強勁、空域限制、天氣波動、燃油成本上升及航班網絡互相牽連；延誤可引致錯過轉機、延長停留、額外住宿及行李問題。其 Allianz Travel Protect 產品提供最高2,310美元（3,000新加坡元）的旅程延誤保障、最高154萬美元（200萬新加坡元）海外醫療費用保障，以及行李遺失或延誤保障，並在符合條件下為旅程意外延長提供自動保障延伸。 [EN原文]",
    "旅遊保障的延誤門檻與醫療上限，是前線最常被客戶追問、也最容易被忽略的細節。本條提供一個具體市場對標（延誤上限、海外醫療上限、行李保障、自動延長），可用於向客戶說明「同樣叫旅遊保險，延誤與醫療額度差異可以很大」，並呼應本地大灣區短途旅遊保障產品的市場節奏。",
    "與客戶核對旅遊保障額度時的對標參考",
    "產品比較：延誤／醫療／行李三項上限",
    "團隊分享：旅遊保險理賠門檻與客戶預期管理",
    "大灣區短途旅遊保障趨勢對照",
    (2, 2, 1, 1), ["product", "insurer"], ["travel", "product", "claims", "apac"],
    ["安盛", "旅游保险", "航班延误", "海外医疗", "新加坡"],
    ("Insurance Asia 2026-10-12 报道", "Insurance Asia 2026-10-12 報道",
     "Insurance Asia", "2026-10-12", "EN原文；延误上限 S$3,000（约 US$2,310）"),
    "en", 70, "verified"))

# ══ 5. H&M 网络攻击指控；零售网络风险蔓延 ══
ITEMS.append(mk(
    "ibm-handm-cyber-retail-risk-20261012",
    "insurancebusinessmag", "media", "news",
    "2026-10-12",
    "https://www.insurancebusinessmag.com/asia/news/cyber/handm-investigates-hacking-claims-as-retail-cyber-risks-spread-593136.aspx",
    "H&M調查黑客入侵指控　零售業網絡風險蔓延　ASOS外洩凸顯第三方平台與憑證被盜暴露",
    "Insurance Business Asia 10月12日報道，H&M正調查可能遭受網絡攻擊的指控，涉事黑客疑與英國時裝零售商 ASOS 近期外洩事件相關；H&M 稱未發現其數據環境被入侵的迹象，其斯德哥爾摩股價周一跌約1.4%。ASOS 於10月6日確認攻擊者透過社交工程冒充可信聯絡人取得員工登入憑證，並藉此存取存放於第三方平台的客戶姓名及聯絡資料（付款卡資料與帳戶密碼未受影響），網站與應用程式維持運作；ASOS 明確引用其網絡保險（含業務持續保障），但稱量化影響仍尚早。報道並指 M&S 在2025年網絡攻擊後獲約1億英鎊保險賠付，涉3.24億英鎊銷售損失。 [EN原文]",
    "用零售業單一案例把「網絡保險賠什麼」講清楚：資料外洩（鑑證、通知、法律及監管應對成本）與營運中斷（業務中斷損失）屬兩條不同理賠路徑，而企業投保時最常忽略的是第三方平台依賴與憑證被盜的暴露。適合作為與企業客、管理層討論網絡風險自留與轉移的現成案例，並提示核保問卷中「第三方／雲端依賴」一項的實質意義。",
    "與企業客談網絡風險自留與轉移的案例",
    "核保問卷：第三方與雲端依賴的問法",
    "團隊分享：資料外洩 vs 業務中斷的理賠差異",
    "網絡風險與保險保障缺口的公開案例庫",
    (1, 2, 2, 2), ["tech", "market"], ["cyber", "claims", "enterprise", "risk"],
    ["网络保险", "H&M", "ASOS", "数据外泄", "业务中断"],
    ("Insurance Business Asia 2026-10-12 报道", "Insurance Business Asia 2026-10-12 報道",
     "Insurance Business Asia", "2026-10-12", "EN原文；日期为报道日（原文只标日期）"),
    "en", 60, "verified"))

# ═══ 写入 ═══
path = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
ids = {it.get('id') for it in d['items']}
urls = {(it.get('originalUrl') or '').rstrip('/') for it in d['items']}
added = []
for it in reversed(ITEMS):
    if it['id'] in ids or it['originalUrl'].rstrip('/') in urls:
        print('SKIP dup:', it['id'])
        continue
    d['items'] = [it] + d['items']
    ids.add(it['id'])
    urls.add(it['originalUrl'].rstrip('/'))
    added.append(it)

n = len(d['items'])
d['meta']['generatedAt'] = NOW
d['meta']['itemCount'] = n
d['meta']['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'added {len(added)} items, total {n}, generatedAt {NOW}')

lp = '/Users/leonliang/maoquanqingbao/data/last-check.json'
lc = json.load(open(lp, encoding='utf-8'))
lc['lastCheck'] = NOW
for k, v in lc.get('sources', {}).items():
    v['last'] = NOW
json.dump(lc, open(lp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check.json updated:', NOW, '| sources:', len(lc.get('sources', {})))

for it in added:
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'], '|', it['verifyStatus'])
