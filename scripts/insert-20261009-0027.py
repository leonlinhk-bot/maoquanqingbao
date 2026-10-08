#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-09 00:2x increment into live-items.json.

窗口：2026-10-08T23:15（上次检查）→ 2026-10-09T00:27。
本期新增 1 条：Artemis — USAA Residential Re 2026-2 巨災債券（$225m 目標）。
其余 13 个信源在此窗口内无新内容（IA 通函/新闻、HKMA、govhk、AIA/宏利/保誠/AXA/永明
官网、InsuranceAsia / InsuranceAsia News / Insurance Business Asia / SCMP、NFRA 均确认无更新）。
"""
import json
from datetime import datetime, timezone, timedelta

NOW = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%dT%H:%M:%S+08:00')
CR = {"sc": "本站导读", "tc": "本站導讀"}


def mk(id_, sourceKey, tier, kind, pub, url, t, s, w, a_f, a_m, a_l, a_c, ri, boards, themes,
       tags, src, lang, score, verify='pending'):
    return {
        "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": sourceKey, "contentKind": kind,
        "actions": {
            "front": {"sc": a_f[0], "tc": a_f[1]},
            "midback": {"sc": a_m[0], "tc": a_m[1]},
            "lead": {"sc": a_l[0], "tc": a_l[1]},
            "cross": {"sc": a_c[0], "tc": a_c[1]},
        },
        "rolesImpact": {"front": ri[0], "midback": ri[1], "lead": ri[2], "cross": ri[3]},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags, "tc": tags},
        "contentRole": CR, "featured": False, "evergreen": False, "ingestedAt": NOW,
        "id": id_, "publishedAt": pub, "originalUrl": url,
        "title": {"sc": t[0], "tc": t[1]},
        "summary": {"sc": s[0], "tc": s[1]},
        "why": {"sc": w[0], "tc": w[1]},
        "source": {"sc": src[0], "tc": src[1], "lang": lang, "name": src[2],
                   "date": src[3], "note": None},
    }


ITEMS = []

# ══ 1. Artemis：USAA 重返巨災債券市場 目標2.25億美元 Residential Re 2026-2 ══
ITEMS.append(mk(
 "artemis-usaa-residential-re-2026-2-225m-20261008", "artemis", "pro", "news",
 "2026-10-08T23:30:00+08:00",
 "https://www.artemis.bm/news/usaa-returns-with-225m-target-residential-re-2026-2-multi-peril-catastrophe-bond/",
 ("Artemis：USAA 重返巨災債券市場 目標2.25億美元 Residential Re 2026-2（風季後144A市場重開）",
  "Artemis：USAA 重返巨災債券市場 目標2.25億美元 Residential Re 2026-2（風季後144A市場重開）"),
 ("Artemis 10月8日報道：美國軍人互助保險公司 USAA 重返巨災債券市場，透過特殊目的保險公司 Residential Reinsurance 2026 Limited 發行 Series 2026-2，初步目標2.25億美元或以上再保險保障，為 Artemis 追蹤的第48宗 USAA 巨災債券。本次發行分三檔票據，全部以賠償（indemnity）觸發、按每次事故（per-occurrence）提供四年期保障，保障期由2026年12月1日至2030年11月30日，涵蓋美國熱帶氣旋、地震（含火災後續）、強烈雷暴、冬季風暴、山火、火山爆發、隕石撞擊及其他風險（包括汽車及租客保單的水浸損失）。Class 2 檔初步規模5,000萬美元，附著點24.5億美元、耗盡點34.5億美元，初始附著概率8.24%、預期損失6.04%，指導價8.5%至9.25%；Class 3 檔同為5,000萬美元，附著點34.5億美元、耗盡點46億美元，附著概率4.4%、預期損失3.34%，指導價5%至5.5%。報道指此舉標誌風季淡靜後144A廣泛銀團發行市場重開，而倍數（multiple）已隨財產巨災再保價格軟化而下移；USAA 今年4月曾發行歷來最大的8.25億美元 Residential Re 2026-1。 [EN原文]",
  "Artemis 10月8日報道：美國軍人互助保險公司 USAA 重返巨災債券市場，透過特殊目的保險公司 Residential Reinsurance 2026 Limited 發行 Series 2026-2，初步目標2.25億美元或以上再保險保障，為 Artemis 追蹤的第48宗 USAA 巨災債券。本次發行分三檔票據，全部以賠償（indemnity）觸發、按每次事故（per-occurrence）提供四年期保障，保障期由2026年12月1日至2030年11月30日，涵蓋美國熱帶氣旋、地震（含火災後續）、強烈雷暴、冬季風暴、山火、火山爆發、隕石撞擊及其他風險（包括汽車及租客保單的水浸損失）。Class 2 檔初步規模5,000萬美元，附著點24.5億美元、耗盡點34.5億美元，初始附著概率8.24%、預期損失6.04%，指導價8.5%至9.25%；Class 3 檔同為5,000萬美元，附著點34.5億美元、耗盡點46億美元，附著概率4.4%、預期損失3.34%，指導價5%至5.5%。報道指此舉標誌風季淡靜後144A廣泛銀團發行市場重開，而倍數（multiple）已隨財產巨災再保價格軟化而下移；USAA 今年4月曾發行歷來最大的8.25億美元 Residential Re 2026-1。 [EN原文]"),
 ("風季後首宗大型144A巨災債券是觀察第四季再保定價與 ILS 資金胃納的先行指標；發行倍數下移與指導價水平，反映財產巨災風險定價持續正常化，對亞洲（含香港）分出人的再保成本預期有參考意義。",
  "風季後首宗大型144A巨災債券是觀察第四季再保定價與 ILS 資金胃納的先行指標；發行倍數下移與指導價水平，反映財產巨災風險定價持續正常化，對亞洲（含香港）分出人的再保成本預期有參考意義。"),
 ("引用資本市場工具條款時只作架構說明，不涉及任何投資建議",
  "引用資本市場工具條款時只作架構說明，不涉及任何投資建議"),
 ("納入ILS與巨災債券發行監察", "納入ILS與巨災債券發行監察"),
 ("用於說明風季後再保定價與ILS資金流向", "用於說明風季後再保定價與ILS資金流向"),
 ("香港ILS政策方向與國際發行節奏的對照參考", "香港ILS政策方向與國際發行節奏的對照參考"),
 (1, 2, 2, 2), ["market", "ils"], ["ils", "catastrophe-bond", "pricing", "reinsurance"],
 ["USAA", "巨災債券", "Residential Re", "144A"],
 ("Artemis 2026-10-08 報道", "Artemis 2026-10-08 報道", "Artemis", "2026-10-08"), "en", 71, "verified"))


path = '/Users/leonliang/maoquanqingbao/data/live-items.json'
d = json.load(open(path, encoding='utf-8'))
ids = {it['id'] for it in d['items']}
urls = {(it.get('originalUrl') or '').rstrip('/') for it in d['items']}
added = []
for it in ITEMS:
    if it['id'] in ids:
        print('SKIP dup id:', it['id'])
        continue
    if it['originalUrl'].rstrip('/') in urls:
        print('SKIP dup url:', it['id'])
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
