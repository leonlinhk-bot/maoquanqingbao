#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-16 00:29 catch-up 增量：插入新条目 + 回写 meta + last-check。"""
import json, shutil, os
import zhconv

P = '/Users/leonliang/maoquanqingbao'
NOW = '2026-10-16T00:29:00+08:00'
STAMP = '1016-0029'

def t2(s):
    return zhconv.convert(s, 'zh-hant')

def pair(s):
    return {'sc': s, 'tc': t2(s)}

def tlist(items):
    return {'sc': items, 'tc': [t2(x) for x in items]}

ITEMS = [
 {
  "id": "rn-brit-re-james-winn-cuo-bermuda-20261016",
  "publishedAt": "2026-10-16T00:00:10+08:00",
  "originalUrl": "https://www.reinsurancene.ws/james-winn-appointed-cuo-and-head-of-office-brit-re-bermuda/",
  "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
  "contentKind": "news", "clusterCount": 1,
  "boards": ["insurer", "market"],
  "themes": ["appointments", "bermuda", "property-treaty", "leadership", "reinsurance"],
  "summary": pair("Brit Group Holdings 宣布委任现任伦敦物业条约险（Property Treaty）董事总经理 James Winn 为百慕达 Brit Re 首席核保官兼办公室主管，预计 2026 年底前调任，仍有待相关批准；Winn 在劳合社及百慕达市场拥有超过 35 年北美物业条约险经验。现任主管 Jonathan Stephenson 年底按计划交接，其任内把平台第三方保费做到逾 2.5 亿美元，并推出美国直接及临时（D&F）业务；另有两位助理副总裁将自伦敦调任，支援意外条约与 D&F 扩张。[EN原文]"),
  "why": pair("百慕达再保平台仍在扩编与补强核保梯队，反映离岸承保能力与人才持续向百慕达集中；香港若要争取专属自保与再保枢纽，须留意同类平台的竞争动作与人才流向。"),
  "source": {"sc": "Reinsurance News 2026-10-16 报道（Brit Group Holdings 公布）",
             "tc": "Reinsurance News 2026-10-16 報道（Brit Group Holdings 公布）",
             "lang": "en", "name": "Reinsurance News", "date": "2026-10-16",
             "note": "EN原文；含交接安排与平台规模口径"},
  "tags": tlist(["Brit", "百慕达", "再保险", "核保", "人事任命"]),
  "actions": {"front": {},
              "midback": pair("百慕达再保平台扩张动态跟踪"),
              "lead": pair("团队简报：离岸再保平台竞争"),
              "cross": {}},
  "rolesImpact": {"front": 0, "midback": 1, "lead": 2, "cross": 1},
  "title": pair("英资 Brit 委任 James Winn 掌百慕达 Brit Re　任首席核保官兼办公室主管"),
  "summaryShort": pair("Brit 委任 James Winn 为百慕达 Brit Re 首席核保官兼办公室主管，年底前调任，平台第三方保费已逾 2.5 亿美元。"),
 },
 {
  "id": "artemis-stand-landi-cfo-70m-series-c-20261015",
  "publishedAt": "2026-10-15T23:50:38+08:00",
  "originalUrl": "https://www.artemis.bm/news/stand-hires-former-nephila-exec-landi-as-cfo-raises-70-million-series-c/",
  "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
  "contentKind": "news", "clusterCount": 1,
  "boards": ["market", "tech"],
  "themes": ["insurtech", "ils", "catastrophe-risk", "funding", "climate-resilience"],
  "summary": pair("专注为巨灾暴露地区物业承保的持牌保险生产商 Stand，宣布聘用前 Nephila Capital 策略增长主管 Tony Landi 为首席财务官，负责财务、再保、资本市场与增长策略；公司同时完成 C 轮融资 7,000 万美元、估值约 10 亿美元，由 Saga Ventures 领投，Lowercarbon、Eclipse、Equal Ventures、Inspired Capital 等参与。Stand 承保物业规模由一年前 10 亿美元增至 100 亿美元，并以自研 Stand World Model 逐户模拟火灾、风灾等巨灾情景下的表现。[EN原文]"),
  "why": pair("「逐户物理建模＋ILS 资本」的定价模式正在挑战传统巨灾财产险，是气候韧性如何转化为保费优惠的样本；Nephila 人才流向科技保险平台，亦显示 ILS 与 insurtech 的人才融合。"),
  "source": {"sc": "Artemis.bm 2026-10-15 报道（Stand 公布 C 轮）",
             "tc": "Artemis.bm 2026-10-15 報道（Stand 公布 C 輪）",
             "lang": "en", "name": "Artemis.bm", "date": "2026-10-15",
             "note": "EN原文；含融资规模、估值与承保规模"},
  "tags": tlist(["Stand", "Nephila", "保险科技", "巨灾保险", "融资"]),
  "actions": {"front": {},
              "midback": pair("气候韧性定价模式跟踪"),
              "lead": pair("专题：物理建模与参数化承保"),
              "cross": pair("家办另类资产（ILS）参考")},
  "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 2},
  "title": pair("保险科企 Stand 聘前 Nephila 高层任 CFO　完成 7,000 万美元 C 轮、估值 10 亿美元"),
  "summaryShort": pair("Stand 聘前 Nephila 策略增长主管 Tony Landi 任 CFO，并完成 7,000 万美元 C 轮、估值约 10 亿美元，承保物业由 10 亿增至 100 亿美元。"),
 },
 {
  "id": "ian-marsh-greensill-credit-suisse-800m-settlement-20261015",
  "publishedAt": "2026-10-15T23:38:47+08:00",
  "originalUrl": "https://insuranceasianews.com/marsh-to-pay-largest-share-of-us800m-credit-suisse-greensill-settlement-ft/",
  "sourceKey": "insuranceasianews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
  "contentKind": "news", "clusterCount": 1,
  "boards": ["market"],
  "themes": ["professional-liability", "litigation", "greensill", "broker", "claims"],
  "summary": pair("InsuranceAsia News 引述《金融时报》报道，威达信（Marsh）将在瑞信（Credit Suisse）就 Greensill Capital 倒闭于澳洲提出的诉讼和解中承担最大份额，和解总额 8 亿美元；报道指该和解涉及多名被告，各方分摊细节未全面公开。该供应链金融集团倒闭引发连串专业责任与保单争议，此前已有 Tokio Marine 等承保人与瑞信达成和解。[EN原文；IAAN 正文需订阅]"),
  "why": pair("金融机构与中介的专业责任（PI）保单正在为供应链金融倒闭埋单，是责任险定价与尽职调查标准的重要案例，对香港经纪及金融机构客户的合规叙事有直接借鉴价值。"),
  "source": {"sc": "InsuranceAsia News 2026-10-15 报道（引述金融时报）",
             "tc": "InsuranceAsia News 2026-10-15 報道（引述金融時報）",
             "lang": "en", "name": "InsuranceAsia News", "date": "2026-10-15",
             "note": "EN原文；正文需订阅，导读仅依公开导语"},
  "tags": tlist(["威达信", "Greensill", "专业责任", "诉讼和解", "瑞信"]),
  "actions": {"front": {},
              "midback": pair("专业责任（PI）案例库"),
              "lead": pair("风险案例简报：供应链金融与中介责任"),
              "cross": pair("客户合规提示素材")},
  "rolesImpact": {"front": 0, "midback": 1, "lead": 2, "cross": 1},
  "title": pair("据报威达信在瑞信 Greensill 澳洲诉讼 8 亿美元和解中承担最大份额"),
  "summaryShort": pair("《金融时报》报道指，威达信将在瑞信就 Greensill 于澳洲提出的诉讼和解中承担最大份额，和解总额 8 亿美元。"),
 },
 {
  "id": "rn-marsh-ai-systemic-cyber-doyle-20261015",
  "publishedAt": "2026-10-15T23:30:28+08:00",
  "originalUrl": "https://www.reinsurancene.ws/marsh-leans-into-ai-growth-but-warns-of-systemic-cyber-exposure-ceo-doyle/",
  "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
  "contentKind": "speech", "clusterCount": 1,
  "boards": ["tech", "market"],
  "themes": ["ai-governance", "cyber-risk", "systemic-risk", "broker", "earnings"],
  "summary": pair("威达信（Marsh）总裁兼行政总裁 John Doyle 在第三季业绩电话会议表示，AI 已不是「未来因素」而是业务当下的驱动力，正重塑风险顾问、客户互动与内部工作流程；惟他警告无节制部署会放大网络曝险，为全球市场带来高度相关的系统性风险、甚至不可逆，强调开发者、企业与政府都要负责把关。Marsh 将主动协助客户管理 AI 相关责任并捕捉机遇，并已推出多项 AI 产品，用于风险、健康与人才数据。[EN原文]"),
  "why": pair("AI 治理与网络风险是监管同期议题（同日金管局公布「ART」框架）；此为国际经纪龙头对 AI 责任与系统性风险的公开口径，可直接用于企业客户的 AI 风险对话与自身 AI 赋能的合规叙事。"),
  "source": {"sc": "Reinsurance News 2026-10-15 报道（Marsh 第三季业绩会）",
             "tc": "Reinsurance News 2026-10-15 報道（Marsh 第三季業績會）",
             "lang": "en", "name": "Reinsurance News", "date": "2026-10-15",
             "note": "EN原文；含 CEO 原话与 AI 产品方向"},
  "tags": tlist(["威达信", "人工智能", "网络风险", "系统性风险", "保险经纪"]),
  "actions": {"front": {},
              "midback": pair("AI 责任与网络风险跟踪"),
              "lead": pair("团队简报：AI 责任与系统性网络风险"),
              "cross": pair("AI 治理对外引用素材")},
  "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 1},
  "title": pair("威达信 CEO Doyle：AI 已成业务即时驱动力　惟警告系统性网络风险须协同监管"),
  "summaryShort": pair("Marsh CEO Doyle 指 AI 已成业务即时驱动力，但无节制部署会放大网络曝险、带来系统性风险，行业须协同监管。"),
 },
 {
  "id": "rn-acic-aces-es-specialty-approval-20261015",
  "publishedAt": "2026-10-15T23:00:41+08:00",
  "originalUrl": "https://www.reinsurancene.ws/acics-aces-specialty-insurance-company-gets-approval-to-underwrite-es-insurance/",
  "sourceKey": "reinsurancenews", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
  "contentKind": "news", "clusterCount": 1,
  "boards": ["insurer", "market"],
  "themes": ["es-market", "catastrophe-property", "mga", "us-market", "capital"],
  "summary": pair("美国保险控股公司 American Coastal Insurance Corporation（ACIC）旗下新设子公司 ACES Specialty Insurance Company 已获亚利桑那州保险及金融机构部发出 Certificate of Authority，可承保超额及盈余（E&S）保险。ACIC 初期计划在佛罗里达、德州及南卡罗来纳州承接巨灾暴露的商业财产 E&S 业务，并预期 2026 年 12 月 1 日左右开业，仍须满足监管、评级机构及营运条件；ACIC 同时拥有内部 MGA Skyway Underwriters。[EN原文]"),
  "why": pair("风险由传统保险公司移往 E&S 渠道与 MGA 平台是结构性趋势；对香港发展专属自保、MGA 与巨灾财产承保能力的话题有对照价值。"),
  "source": {"sc": "Reinsurance News 2026-10-15 报道（ACIC 公布获牌）",
             "tc": "Reinsurance News 2026-10-15 報道（ACIC 公布獲牌）",
             "lang": "en", "name": "Reinsurance News", "date": "2026-10-15",
             "note": "EN原文；含牌照、开业时间与业务范围"},
  "tags": tlist(["E&S", "巨灾财产险", "亚利桑那", "美国保险市场", "MGA"]),
  "actions": {"front": {},
              "midback": pair("美国 E&S 渠道与 MGA 结构跟踪"),
              "lead": pair("市场结构简报：承保能力移向 E&S"),
              "cross": {}},
  "rolesImpact": {"front": 0, "midback": 1, "lead": 2, "cross": 1},
  "title": pair("ACIC 新设子公司 ACES 获亚利桑那州发牌　12 月起承保超额及盈余（E&S）商业财产险"),
  "summaryShort": pair("ACIC 旗下 ACES 获亚利桑那州发牌承保 E&S 业务，初期聚焦佛州、德州及南卡的巨灾商业财产险，预计 12 月起开业。"),
 },
 {
  "id": "artemis-marsh-ceo-casualty-sidecars-20261015",
  "publishedAt": "2026-10-15T22:47:51+08:00",
  "originalUrl": "https://www.artemis.bm/news/marsh-ceo-flags-client-interest-in-casualty-sidecars-notes-reinsurance-market-softening/",
  "sourceKey": "artemis", "sourceTier": "pro", "score": 70, "verifyStatus": "verified",
  "contentKind": "speech", "clusterCount": 1,
  "boards": ["market"],
  "themes": ["sidecar", "casualty-ils", "alternative-capital", "reinsurance-cycle", "liability"],
  "summary": pair("威达信行政总裁 John Doyle 在第三季业绩会指出，短尾再保条线持续偏软，主因传统再保与另类资本供应充裕、加上巨灾损失相对温和；客户正探索以第三方资本方案补充传统策略，包括为责任险组合设立 sidecar 载体，并预期竞争环境延续至 1 月 1 日续保周期。Marsh Re 上季收入跌 6% 至 3.74 亿美元；Doyle 承认公司在巨灾财产险及美国的比重略高，增长机会集中在临时再保、并购顾问与另类资本结构。[EN原文]"),
  "why": pair("香港上月才落地首宗保险侧挂（sidecar）安排（FSTB／PICC），国际经纪龙头此刻确认责任险 sidecar 需求成形，直接支持香港以 ILS 平台承接 casualty 风险的定位，也是向客户解释另类资本的现成材料。"),
  "source": {"sc": "Artemis.bm 2026-10-15 报道（Marsh 第三季业绩会）",
             "tc": "Artemis.bm 2026-10-15 報道（Marsh 第三季業績會）",
             "lang": "en", "name": "Artemis.bm", "date": "2026-10-15",
             "note": "EN原文；含 CEO 原话与续保周期看法"},
  "tags": tlist(["威达信", "侧挂", "另类资本", "责任险", "续保周期"]),
  "actions": {"front": {},
              "midback": pair("责任险 ILS／sidecar 动态跟踪"),
              "lead": pair("团队简报：香港侧挂安排的市场对照"),
              "cross": pair("客户另类资本解说素材")},
  "rolesImpact": {"front": 0, "midback": 2, "lead": 2, "cross": 2},
  "title": pair("威达信 CEO：客户探讨以侧挂（sidecar）等第三方资本方案　分担责任险组合风险"),
  "summaryShort": pair("Doyle 指短尾再保持续偏软，客户正探索为责任险组合设立 sidecar，相关竞争环境料延续至 1 月 1 日续保周期。"),
 },
 {
  "id": "ibm-marsh-q3-revenue-consulting-offset-20261015",
  "publishedAt": "2026-10-15T21:46:19+08:00",
  "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/marsh-revenue-rises-8-as-consulting-growth-offsets-reinsurance-decline-593667.aspx",
  "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
  "contentKind": "news", "clusterCount": 1,
  "boards": ["market"],
  "themes": ["broker", "earnings", "consulting", "asia-pacific", "reinsurance-cycle"],
  "summary": pair("威达信（Marsh）第三季收入增 8% 至 69 亿美元，基本收入增 5%，调整后每股盈利升 10% 至 2.03 美元；风险及保险服务收入 42 亿美元（基本增 3%），其中 Marsh Risk 收入 37 亿美元、基本增 5%，亚太区增 4%，美国及加拿大增 4%；再保业务收入跌 6% 至 3.74 亿美元。管理咨询（前 Oliver Wyman）收入增 14% 至 10 亿美元，People & Investments（前 Mercer）增 6%。首九个月收入增 7% 至 219 亿美元。[EN原文]"),
  "why": pair("亚太区经纪基本增长只有 4%、再保收入转负，反映区内定价下行与续保议价环境；可作为香港市场佣金收入与客户议价预期的先行指标。"),
  "source": {"sc": "Insurance Business 2026-10-15 报道（Marsh 第三季业绩）",
             "tc": "Insurance Business 2026-10-15 報道（Marsh 第三季業績）",
             "lang": "en", "name": "Insurance Business", "date": "2026-10-15",
             "note": "EN原文；含分部收入与亚太增长"},
  "tags": tlist(["威达信", "季度业绩", "保险经纪", "管理咨询", "再保险"]),
  "actions": {"front": {},
              "midback": pair("龙头经纪业绩与区域增长跟踪"),
              "lead": pair("续保季前市场气氛简报"),
              "cross": {}},
  "rolesImpact": {"front": 0, "midback": 1, "lead": 2, "cross": 1},
  "title": pair("威达信第三季收入增 8% 至 69 亿美元　管理咨询双位数增长抵销再保收入跌 6%"),
  "summaryShort": pair("Marsh 第三季收入增 8% 至 69 亿美元，Marsh Risk 亚太区基本增 4%，再保收入跌 6%，管理咨询增 14%。"),
 },
]


def main():
    path = os.path.join(P, 'data/live-items.json')
    shutil.copy(path, os.path.join(P, 'data', f'live-items.json.bak-{STAMP}'))
    d = json.load(open(path, encoding='utf-8'))
    have = {it.get('id') for it in d['items']}
    urls = {it.get('originalUrl') for it in d['items']}
    new = []
    for it in ITEMS:
        if it['id'] in have:
            print('SKIP dup id:', it['id']); continue
        if it['originalUrl'] in urls:
            print('SKIP dup url:', it['id']); continue
        it.setdefault('featured', False)
        it.setdefault('evergreen', False)
        it.setdefault('contentRole', {"sc": "本站导读", "tc": "本站導讀"})
        it['ingestedAt'] = NOW
        new.append(it)
    new.sort(key=lambda x: x['publishedAt'], reverse=True)
    d['items'] = new + d['items']
    meta = d['meta']
    meta['generatedAt'] = NOW
    meta['itemCount'] = len(d['items'])
    meta['windowNote'] = {"sc": "本库%d条。" % len(d['items']), "tc": "本庫%d條。" % len(d['items'])}
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('inserted:', len(new), 'total:', len(d['items']))
    for it in new:
        print('  +', it['publishedAt'], '|', it['sourceKey'], '|', it['title']['sc'][:50])

    lc_path = os.path.join(P, 'data/last-check.json')
    shutil.copy(lc_path, os.path.join(P, 'data', f'last-check.json.bak-{STAMP}'))
    lc = json.load(open(lc_path, encoding='utf-8'))
    lc['lastCheck'] = NOW
    for k, v in lc.get('sources', {}).items():
        v['last'] = NOW
    json.dump(lc, open(lc_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('last-check updated:', len(lc.get('sources', {})), 'sources')


if __name__ == '__main__':
    main()
