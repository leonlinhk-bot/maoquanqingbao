#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-15 00:44 (launchd catch-up) increment into live-items.json.

窗口：2026-10-14T21:38（上轮 lastCheck）→ 2026-10-15T00:47（本轮，launchd 登录补跑：
last-check.json 属 10-14、非当日，触发补跑）。属夜间窄窗（约 3 小时）。

本期新增 2 条：
  artemis 1（Victory Capital：巨災債券配置靈活，可入固定收益或另類投資；
             14 Oct 21:00 HKT 发布，落在上轮窗口尾部但被漏收，本轮补回）
  insurancebusinessmag 1（加拿大央行：人口結構變化將令勞動人口收縮，2025 年人口僅增 0.5%）

信封内无新增（本轮逐一复核）：
  IA（新闻稿页／通函页 Cloudflare 拦截；经 web_extract 取回通函表，最新仍为 2026-05-13 批次/
      l 上轮记录 10-02，无新增）、HKMA（新闻稿页最新 2026-10-14，仅债券投标公告 +
      「Analytical Accounts of the Exchange Fund」等日常公告，非保险实体，按 substance 跳过；
      讲辞页最新 10-13、inSight 最新 10-12）、AIA HK（最新 2026-10-09）、Manulife HK（页面
      JS 渲染，jina 仅得保安提示，无法取日期）、Prudential HK（最新 10-04）、AXA HK（最新 10-08）、
      Sun Life HK（页面无日期锚点）、InsuranceAsia.com（RSS 最新 10-14 06:00，均在库）、
      InsuranceAsia News（WP API／feed 最新 10-14 17:52 McLarens 人事，按 substance 跳过）、
      SCMP（RSS 最新 10-14 21:00，均在库）、govhk（RSS 最新 10-14 21:00，无 10-15 条目、无保险相关）、
      NFRA（监管动态最新 10-14 18:02「丁向群会见澳门经财司司长」，礼节性会见，跳过）、
      FSTB（页面路径 404/JS 渲染，无新）、HKFI（页面 404，无法取数）。
已按 substance 去重跳过：PICC P&C 首宗香港侧挂车 ILS（已由财库局官方稿 + Artemis/IAN 多版覆盖）、
  AIA 终身年金（10-13 已收）、Jefferies AIA 新业务价值（已收）、皇岗口岸强制车保延伸（已收 3 版）、
  InsuranceAsia 10-13 早间批次（Vietnam 罚则／Sun Life 人事／Canara 印度业绩／Zurich-ShopeePay）
  —— 均为上轮已复核并以 substance 筛除的条目。
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

# ══ 1. Victory Capital：巨災債券的配置彈性 ══
ITEMS.append(mk(
    "artemis-victory-capital-cat-bonds-allocation-flexibility-20261014",
    "artemis", "pro", "news",
    "2026-10-14T21:00:42+08:00",
    "https://www.artemis.bm/news/cat-bonds-offer-flexibility-across-fixed-income-and-alternative-investment-allocations-victory-capital/",
    "Victory Capital：巨災債券配置具彈性　可歸入固定收益或另類投資　瑞士再保指數過去19年18年錄正回報",
    "Artemis 於10月14日報道，資產管理公司 Victory Capital 指出，巨災債券與傳統金融市場相關性低，且組合配置具高度彈性，既可歸入投資者的固定收益部分，也可放入另類投資策略。該行以瑞士再保全球巨災債券指數（2007–2025年）為代理指標：過去19年中有18年錄得正回報；三年度滾動回報介乎2.58%至16.07%，17個滾動期全部為正、且全部高於2%。該行強調巨災債券存在事件觸發的本金風險，未必適合所有投資者，主動管理可平衡地域曝險並捕捉結構性低效。[EN原文]",
    "這是 ILS 資產類別「機構化敘事」的最新一份素材：賣點已由「高收益」轉為「低相關性 + 配置彈性 + 長期正回報紀錄」。對香港的現實意義是，本港 ILS 生態（巨災債券、側掛車、未來受保護單元公司）能否持續發行，取決於本地及亞洲機構資金是否把巨災債券納入常規資產配置——資產管理公司開始在公開材料中做「配置框」論述，正是需求端成熟的先行信號。",
    "客戶問另類資產分散風險時的案例", "ILS 在組合中的定位（固定收益 vs 另類）",
    "團隊簡報：巨災債券的風險回報特徵", "家辦資產配置中的低相關性資產",
    (0, 2, 3, 2), ["market", "family"], ["ils", "cat-bonds", "asset-allocation", "diversification", "family-office"],
    ["Victory Capital", "巨災債券", "ILS", "資產配置", "瑞士再保指數"],
    ("Artemis.bm 2026-10-14 報道（Victory Capital 觀點）", "Artemis.bm", "2026-10-14",
     "EN原文；含瑞士再保全球巨災債券指數回報數據"),
    "en", 70, "verified"))

# ══ 2. 加拿大央行：人口結構變化令勞動人口收縮 ══
ITEMS.append(mk(
    "ibm-bank-of-canada-demographic-workforce-shrink-593491-20261014",
    "insurancebusinessmag", "media", "news",
    "2026-10-14T22:55:56+08:00",
    "https://www.insurancebusinessmag.com/asia/business-strategy/demographic-changes-to-shrink-canadas-workforce-bank-of-canada-593491.aspx",
    "加拿大央行：人口結構變化將令勞動人口收縮　2025年人口僅增0.5%（百餘年最慢）　醫療與退休需求上升",
    "Insurance Business 於10月14日報道，加拿大央行一份解說文件指出，人口老化加上移民減少，正令該國勞動人口收縮，並可能推高部分行業工資。加拿大2025年人口僅增長0.5%，為逾一世紀以來最慢，遠低於過去50年約1.2%的年均增速；生育率已低於更替水平逾50年，移民自2024年起持續削減（2026年臨時勞工目標23萬人）。央行指勞動力短缺或推高工資並傳導至通脹，同時年長人口醫療支出較高，帶動該行業需求。[EN原文]",
    "老齡化的宏觀傳導鏈很值得前線引用：出生率長期低於更替 + 移民收緊 → 勞動力缺口 → 工資與通脹壓力 → 公共財政與個人退休儲備雙重吃緊。把這條鏈條放到香港，即是「高才通」等人才政策、以及內地訪客定義調整所爭奪的，正是同一批可移動的年輕勞動力與高淨值人群；而退休收入缺口擴大，則直接支撐年金、醫療與長照類產品的需求敘事。",
    "客戶談退休儲備與人口老化時的國際參照", "退休收入缺口與年金需求",
    "團隊簡報：老齡化的宏觀傳導鏈", "人才流動與客戶結構變化",
    (0, 1, 2, 1), ["market"], ["demographics", "longevity", "retirement-gap", "macro"],
    ["加拿大央行", "人口老化", "勞動人口", "退休保障", "移民政策"],
    ("Insurance Business Asia 2026-10-14 報道（加拿大央行解說文件）", "Insurance Business Asia",
     "2026-10-14", "EN原文；含人口與移民數據要點"),
    "en", 60, "verified"))

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
