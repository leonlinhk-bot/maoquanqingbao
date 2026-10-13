#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-14 03:00 (catch-up) increment into live-items.json.

窗口：2026-10-13T21:12（上轮）→ 2026-10-14T03:00（本轮）。
本轮为 launchd 登录补跑（last-check.json 的 lastCheck 属 10-13，非当日，故触发）。

本期新增 2 条：
  artemis 1（Verisk：飓风 Isaias 陆上财产保险损失初步估计 10 亿至 20 亿美元；
              与 Euler ILS 20–40 亿、Cotality 20–30 亿并列成三条行业损失口径）
  fsc 1（台湾金管会发布「金融业运用代理 AI 安全咨询文件」，30 日咨询期；
          安全治理／风险分级／安全控管三大面向 —— 属 10-13 发布、上轮漏收，本轮补回同日条目）

无新发布信源（本轮逐一复核）：
  IA 通函（最新 2026-10-02，lastUpdate 2026-10-02；press/circular 页 Cloudflare 拦截，
  经 web_extract 取回，表格无新增）、HKMA（新闻稿页最新 2026-10-13「Exchange Fund Bills
  Tender Results」，非保险实体、日常公告，已按 substance 跳过）、InsuranceAsia News
  （WP API 最新 2026-10-13 18:05，窗口外）、Insurance Business Asia（Atom feed lastBuild
  2026-10-13T03:02:34Z＝11:02 HKT，无更新）、InsuranceAsia.com（RSS 最新 16:36，站点
  「LATEST NEWS」相对时间为缓存值，不可信）、Asia Insurance Review（10-13 批次 97205–97223
  已入库）、SCMP（保险专题最新 10-07）、govhk（10-13 21:46/21:48 两条为海关走私与谋杀案，
  非保险）、NFRA（监管动态最新 2026-10-09）、MPFA（最新 05/10/2026）、HKFI（最新 16/9/2026）、
  AIA HK（最新 2026-10-09）、AXA HK（最新 2026-10-08）、Sun Life HK／Prudential HK／
  Manulife HK／FWD HK（页面 JS 渲染，日期锚点不可得，已用检索兜底，无窗口内新条目）。
已去重跳过：FWD 收购 bolttech 25%（10-12 已收）、日本 FSA 停售 Prudential/Gibraltar（10-11/10-13
  已收）、金管会放宽保险业投资健康福祉事业（10-06，经 IAA 10-13 已收）。
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

# ══ 1. Verisk：飓风 Isaias 陆上财产保险损失 10–20 亿美元 ══
ITEMS.append(mk(
    "artemis-verisk-hurricane-isaias-onshore-loss-20261014",
    "artemis", "pro", "news",
    "2026-10-14T00:14:55+08:00",
    "https://www.artemis.bm/news/verisk-estimates-hurricane-isaias-insured-onshore-property-losses-in-1bn-to-2bn-range/",
    "Verisk：飓风 Isaias 陆上财产保险损失初步估计 10 亿至 20 亿美元　为目前各口径中偏低者",
    "Artemis 于10月13日报道，巨灾风险建模机构 Verisk 就飓风 Isaias 发出初步行业保险损失估计，指风暴造成的陆上财产损失可能达20亿美元，区间为10亿至20亿美元。估算涵盖风灾与私营保险承担的暴雨潮（storm surge）损失——Isaias 于佛罗里达州狭长地带（Panhandle）登陆；Verisk 指风灾将占保险损失的绝大部分，标的包括陆上住宅、商业及工业物业的楼宇、内藏物与时间要素保障，以及汽车；并预期降水引发的水浸并非重要因素。最严重风灾位于登陆点以西，特别是佛州 Santa Rosa 县及 Escambia 县东北部，已见屋顶与结构受损。 Verisk 此口径为目前各估算中偏低者，仍处于市场预期的「低至中单位数十亿美元」区间：Euler ILS Partners 早前估计 20 亿至 40 亿美元，Cotality（前称 CoreLogic）估计 20 亿至 30 亿美元。 [EN原文]",
    "三条行业损失口径（Verisk 10–20 亿、Cotality 20–30 亿、Euler ILS 20–40 亿）同处「单位数十亿美元」量级，是判断本轮巨灾债券／ILS 是否触及触发门槛、以及再保端损失吸收节奏的直接参照。对香港市场的意义在于：本地正发展 ILS 与巨灾债券平台，此类第三方建模口径的差异与收敛过程，正是向机构与高净值客户解释「参数式触发 vs 实际损失」分野的鲜活案例。",
    "客户问巨灾债券触发与否时的损失口径参照",
    "巨灾损失估算的机构差异与收敛",
    "团队简报：ILS 触发机制与损失估计",
    "参数式与损失赔偿式的实务分野",
    (0, 2, 3, 2), ["market"],
    ["catastrophe", "ils", "cat-bonds", "industry-loss"],
    ["飓风Isaias", "Verisk", "巨灾损失", "巨灾债券", "参数式保险"],
    ("Artemis.bm 2026-10-13 报道", "Artemis.bm", "2026-10-13",
     "EN原文；含原文正文摘录"),
    "en", 70, "verified"))

# ══ 2. 台湾金管会：金融业运用代理 AI 安全咨询文件 ══
ITEMS.append(mk(
    "fsc-taiwan-financial-agentic-ai-safety-consultation-20261013",
    "fsc", "official", "circular",
    "2026-10-13",
    "https://www.fsc.gov.tw/ch/home.jsp?id=96&parentpath=0,2&mcustomize=news_view.jsp&dataserno=202610130003&dtable=News",
    "台湾金管会发布「金融业运用代理 AI 安全咨询文件」　三大面向展开 30 日咨询",
    "台湾金融监督管理委员会（金管会）于2026年10月13日发布「金融业运用代理AI安全咨询文件」，就金融业导入代理式AI（Agentic AI）的安全治理、风险分级与安全控管三大面向征询意见，咨询期30日。金管会指出，代理AI相较聊天式AI具备规划步骤、呼叫工具、跨系统存取资料以推进任务的能力；导入得当可提升营运效率，但缺乏管理可能引致目标偏离、工具误用或越权、敏感资料外泄，以及多步流程错误连锁扩大。文件提出三轴风险分级（资料敏感度、动作影响、能力边界／可扩散性），采「就高不就低」原则并纳入生命周期管理；安全控管面则把代理AI视为具行动能力的非人类身分与工作负载，参照零信任原则（不预设信任、持续验证、最小权限、可追溯），就身分、执行环境、网络、应用与工作负载、资料、行为控制及可视性提出基本与进阶要求。文件明言不取代现行法令、监理规范与委外管理，属政策研议与后续指引的前置基础。",
    "这是区域内首份专门针对「代理式 AI」的金融业安全治理咨询文件，把AI风险从「模型输出」推进到「AI自行调用工具与越权动作」，与香港保监局 GenA.I. 沙盒++、以及本号关注的IFA前线AI应用直接同构。三项设计——以「应用场景」为管理单位、三轴风险分级、把AI当非人类身分纳入零信任——可作为团队内部AI工具（客户跟进、核保预审、内容生成）授权与权限设计的对照清单，亦是向客户说明「AI辅助≠AI决策」的现成外部依据。",
    "团队AI工具授权与权限设计的对照清单",
    "代理式AI风险分级与KYAI（认识你的AI）框架",
    "团队分享：AI安全治理三大面向",
    "AI治理跨境对照（台／港）",
    (2, 2, 3, 2), ["reg", "tech"],
    ["ai-governance", "insurtech", "regulation", "conduct"],
    ["金管会", "代理AI", "AI治理", "零信任", "咨询文件"],
    ("金融监督管理委员会（台湾）2026-10-13 新闻稿", "金管会", "2026-10-13",
     "官方新闻稿；附件为咨询文件 PDF（2026-10-13 14:38 上载，publishedAt 标 date-only）"),
    "zh", 88, "verified"))

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
lc.setdefault('sources', {})['fsc'] = {
    "url": "https://www.fsc.gov.tw/ch/home.jsp?id=96&parentpath=0,2",
    "last": NOW,
}
for k, v in lc.get('sources', {}).items():
    v['last'] = NOW
json.dump(lc, open(lp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check.json updated:', NOW, '| sources:', len(lc.get('sources', {})))

for it in added:
    print('  +', it['id'], '|', it['publishedAt'], '|', it['sourceKey'], '|', it['sourceTier'],
          '|', it['verifyStatus'])
