#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Supplement insert for 2026-10-14 21:08 run.

窗口：2026-10-14T02:11 → 2026-10-14T21:08。补入 18:08 脚本遗漏、但落在窗口内的条目：
  1. Artemis：ILS 投资者应要求纳入另类模型视图（Karen Clark，10-14 02:15 HKT）
  2. Insurance Asia：Tata AIA 印度重启 Vitality 健康奖励（10-14 05:30 HKT）
  3. Insurance Asia：Sun Life Asia 菲律宾传承调查「Passing the Torch」（10-14 05:15 HKT）
  4. InsuranceAsia News：IAG 以 NRMA 西澳续保权换取 RACI 交易获批（10-14 09:08 HKT）

已排除（同事件/无实质）：PICC 侧挂车（已由财库局官方稿覆盖）、McLarens 区域理算师任命（人事）。
IA 新闻稿页与 RSS 仍被 Cloudflare 拦截（主机不可达），监管通函最新为 2026-10-02 → 窗口内无新增。
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


def mk(id_, sourceKey, tier, kind, pub, url, t, s, w, a_f, a_m, a_l, a_c, ri, boards, themes,
       tags, src, lang, score, verify='pending'):
    return {
        "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": sourceKey, "contentKind": kind,
        "actions": {
            "front": {"sc": a_f, "tc": T(a_f)},
            "midback": {"sc": a_m, "tc": T(a_m)},
            "lead": {"sc": a_l, "tc": T(a_l)},
            "cross": {"sc": a_c, "tc": T(a_c)},
        },
        "rolesImpact": {"front": ri[0], "midback": ri[1], "lead": ri[2], "cross": ri[3]},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags, "tc": [T(x) for x in tags]},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": t, "tc": T(t)},
        "summary": {"sc": s, "tc": T(s)},
        "why": {"sc": w, "tc": T(w)},
        "source": {"sc": src[0], "tc": T(src[0]), "lang": lang, "name": src[1],
                   "date": src[2], "note": src[3] if len(src) > 3 else None},
    }


ITEMS = []

# ══ 1. Karen Clark：ILS 投資者應要求另類模型視圖 ══
ITEMS.append(mk(
    "artemis-ils-investors-alternative-model-views-karen-clark-20261014",
    "artemis", "pro", "news",
    "2026-10-14T02:15:19+08:00",
    "https://www.artemis.bm/news/ils-investors-need-to-speak-up-and-ask-for-alternative-model-views-karen-clark/",
    "Karen Clark：ILS 投資者應主動要求納入另類模型視圖　勿長期沿用「舊模型」",
    "Artemis 於10月14日報道，巨災風險模型公司 Karen Clark & Company 行政總裁兼聯合創辦人 Karen Clark 在 ILS Bermuda Convergence 2026 會議上呼籲，保險相連證券（ILS）社群及投資者應主動要求交易文件納入另類模型視圖。她指出，隨着新一代模型、人工智能及新數據源被廣泛採用，業界值得讓更多模型進入發行文件與 ILS 交易分析流程；現實情況是，美國不少主險公司內部定價、核保、再保與曝險管理均用她的模型，但到了巨災債券或 ILS 交易卻被迫沿用經紀與交易管理人慣用的既有模型，因為「投資者不會接受」。她直言：投資者需要發聲，表明自己重視另類視圖與第二代模型。[EN原文]",
    "巨災模型是 ILS 定價的核心爭議點：模型選擇直接改變觸發概率與預期損失，也決定投資者的估值共識。當發行文件長期鎖定少數既有模型，風險定價的透明度與可比性就受限，模型風險（model risk）反而被掩蓋。對香港發展 ILS 市場的參照是：制度除了處理發行與稅務，還須在披露與模型多樣性上留出空間，否則本地發行在國際投資者眼中會缺少可比性與可信度。",
    "客戶問巨災風險定價依據時的背景", "模型風險與定價可比性",
    "團隊簡報：ILS 模型選擇的爭議", "香港 ILS 披露制度的模型要求",
    (0, 2, 3, 2), ["market"], ["ils", "catastrophe", "risk-modelling", "model-risk", "alternative-capital"],
    ["Karen Clark", "巨災模型", "ILS", "模型風險", "投資者視圖"],
    ("Artemis.bm 2026-10-14 報道（ILS Bermuda Convergence 2026）", "Artemis.bm", "2026-10-14",
     "EN原文；含會議發言引述"),
    "en", 70, "verified"))

# ══ 2. Tata AIA 印度重啟 Vitality ══
ITEMS.append(mk(
    "iaasia-tata-aia-vitality-relaunch-india-20261014",
    "insuranceasia", "media", "news",
    "2026-10-14T05:30:00+08:00",
    "https://insuranceasia.com/insurance/news/tata-aia-eases-wellness-targets-insurance-rewards",
    "Tata AIA 在印度重啟 Vitality 健康獎勵計劃　每日步數門檻由7,500降至5,000　可換保費折扣",
    "Insurance Asia 於10月14日報道，Tata AIA Life Insurance 在印度重新推出 Vitality 健康獎勵計劃：每日賺取獎勵的步數門檻由7,500步下調至5,000步，並擴大保障權益，以鼓勵客戶建立健康習慣。該計劃2022年首次在印度推出，結合健康追蹤、健康獎勵與保費折扣，今次重推更強調長壽（longevity），並已加入 Health Connect 整合以追蹤心率與活動量。Tata AIA 表示，計劃依據的研究顯示持續健康習慣或可令預期壽命延長最多五年，惟個人結果或有差異。[EN原文]",
    "「互動式保單」（interactive insurance）的關鍵設計變數是門檻高低：門檻過高則參與率低、獎勵形同虛設，過低則失去行為誘因。Tata AIA 由7,500步降至5,000步，本質是以降低摩擦換取參與規模，這對本地健康險與危疾產品的增值服務設計具參考價值——健康獎勵要能落地，門檻須對應真實人群的日常行為分佈。",
    "客戶談健康獎勵與保費折扣時的案例", "互動式保單的門檻設計",
    "團隊分享：健康獎勵計劃落地要點", "健康管理服務與產品附加值",
    (1, 2, 2, 2), ["product", "tech"], ["health", "wellness", "interactive-insurance", "product-design", "india"],
    ["Tata AIA", "Vitality", "健康獎勵", "保費折扣", "互動式保單"],
    ("Insurance Asia 2026-10-14 報道", "Insurance Asia", "2026-10-14", "EN原文；含正文要點"),
    "en", 66, "verified"))

# ══ 3. Sun Life Asia 菲律賓傳承調查 ══
ITEMS.append(mk(
    "iaasia-sun-life-asia-passing-the-torch-philippines-20261014",
    "insuranceasia", "media", "news",
    "2026-10-14T05:15:00+08:00",
    "https://insuranceasia.com/insurance/news/philippine-legacy-planning-leaves-82-fearing-wealth-loss",
    "Sun Life Asia 調查：92% 菲律賓人計劃傳承財富　教育機會成首要傳承項（56%）　82% 憂財富流失",
    "Insurance Asia 於10月14日報道，Sun Life Asia 發布報告《Passing the Torch: When Legacy Means More Than Money》，顯示更多菲律賓人以結構化方式規劃傳承：92% 受訪者打算把金融資產或財富留給下一代；傳承優先次序中，教育機會以56%居首，金融財富與家族傳統各佔45%；在計劃轉移資產的受訪者中，61%希望財富以長期增長方式投資。報道並指82%受訪者擔心財富流失，50%認為「受益人安排是否妥當」是最大關注點。[EN原文]",
    "傳承規劃的實務缺口不在「想不想傳」，而在「受益人與工具是否備妥」：82%憂慮財富流失、半數聚焦受益人安排，說明客戶真正需要的是提名、保單受益人指定、信託與遺囑之間的協同，而非單一產品。教育優先於金錢的排序，亦提示傳承方案要處理跨代價值傳遞——這正是保險在指定受益人與現金流安排上的結構性優勢。",
    "客戶談傳承時的受益人安排提醒", "保單受益人指定與傳承工具協同",
    "團隊分享：傳承規劃的客戶關注點", "家族財富跨代轉移方案",
    (2, 3, 3, 3), ["family", "market"], ["legacy", "wealth-transfer", "beneficiary", "family-office", "asean"],
    ["Sun Life Asia", "傳承規劃", "受益人安排", "教育傳承", "菲律賓"],
    ("Insurance Asia 2026-10-14 報道（Sun Life Asia 報告）", "Insurance Asia", "2026-10-14",
     "EN原文；含報告數據要點"),
    "en", 68, "verified"))

# ══ 4. IAG 以西澳 NRMA 續保權換 RACI 交易獲批 ══
ITEMS.append(mk(
    "ian-iag-nrma-wa-renewal-rights-raci-acquisition-20261014",
    "insuranceasianews", "pro", "news",
    "2026-10-14T09:08:43+08:00",
    "https://insuranceasianews.com/iag-offers-to-trade-nrma-western-australia-renewal-rights-for-raci-deal-approval/",
    "IAG 提出轉讓西澳 NRMA 家居及汽車保單續保權　換取 RACI 收購獲批　另承諾十年投入1,400萬美元社區抗逆",
    "InsuranceAsia News 於10月14日報道，澳洲保險集團 IAG 向競爭監管機構提交公共利益申請，提出把西澳（Western Australia）NRMA Insurance 現行家居及汽車保單的續保權轉讓予另一保險人，並附帶其他讓步，以爭取 RAC Insurance（RACI）收購案獲批；IAG 同時提出處理西澳北部 RACI 家居保險的可得性問題，並承諾未來十年投入1,400萬美元於社區抗逆能力。[EN原文]",
    "這是「併購讓步換取監管批准」的典型案例：監管機構關切的不只是市場份額，還包括區域保障可得性與消費者選擇。對區域保險市場的啟示是，交易審批已把「保障覆蓋的可及性」納入考量，這與香港及大灣區討論市場集中度、消費者保障時的分析框架一致，值得在區域市場週報中追蹤其最終裁決與條件設計。",
    "客戶問市場整合對保單影響時的背景", "併購審批中的消費者保障考量",
    "團隊分享：區域保險併購的監管條件", "市場集中度與保障可得性分析",
    (0, 2, 2, 3), ["market", "reg"], ["m&a", "competition", "home-insurance", "consumer-protection", "australia"],
    ["IAG", "RACI", "NRMA", "續保權", "併購審批"],
    ("InsuranceAsia News 2026-10-14 報道", "InsuranceAsia News", "2026-10-14",
     "EN原文；訂閱內容，事實來自官網導語"),
    "en", 70, "pending"))

# ═══ 寫入 ═══
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
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'],
          '|', it['verifyStatus'])
