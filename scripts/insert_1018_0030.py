#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-18 00:xx 增量（补 10-17 18:08 / 21:08 两次未完成的采集）：
窗口 = lastCheck 2026-10-17T00:48 → 2026-10-18T00:3x。
新增：insuranceasia 1 + insurancebusinessmag 3 + insuranceasianews 1（补漏）+ ia 1（AIF/IAIS 补录）。
"""
import json, shutil, os
from datetime import datetime, timezone, timedelta

try:
    import zhconv
except Exception:
    zhconv = None
    print('WARN: zhconv missing')

P = '/Users/leonliang/maoquanqingbao'
HKT = timezone(timedelta(hours=8))
NOW = datetime.now(HKT).strftime('%Y-%m-%dT%H:%M:00+08:00')
STAMP = '1018-0030'


def t2(s):
    return zhconv.convert(s, 'zh-hant') if zhconv else s


def pair(s):
    return {'sc': s, 'tc': t2(s)}


def tlist(items):
    return {'sc': items, 'tc': [t2(x) for x in items]}


ITEMS = [
    # ---------- insuranceasia（media 66） ----------
    {
        "id": "insuranceasia-week-in-insurance-20261017",
        "publishedAt": "2026-10-17T05:00:00+08:00",
        "originalUrl": "https://insuranceasia.com/insurance/news/week-in-insurance-mox-launches-home-cover-igloo-enters-turkiye-fwd-invests-in-bolttech",
        "sourceKey": "insuranceasia", "sourceTier": "media", "score": 66, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["product", "market"],
        "themes": ["digital-insurance", "bancassurance", "home-insurance", "m-and-a", "cyber-risk", "legacy-planning"],
        "summary": pair("Insurance Asia 一周回顾：Mox Bank 推出全数码家居保险 Home Cushion（昆士兰保险香港承保，覆盖家居财物、楼宇结构与第三者责任，租客、自住业主与房东均适用，全程经手机应用投保）；Igloo 与 Sigortayeri 合作、经 Aktif Bank 旗下 N Kolay 应用进入土耳其，推出个人网络保险，为其首次走出亚太；富卫以 2,072 万美元（约 1.6261 亿港元）收购 bolttech insurance 25% 股权；永明亚洲调查显示 92% 菲律宾人拟把财富传给下一代，重点在教育与继承人准备；新加坡 52% 机构曾因勒索软件出现业务中断或收入损失，六成受害企业称攻击者使用 AI（全球为四成）。[EN原文]"),
        "why": pair("一周汇总把「银行 App 卖简单标准化产品」、跨境扩张、并购与传承需求串在一起。对前线而言，数字渠道的竞争已从储蓄险延伸到家居与网络险；而 AI 驱动攻击已是企业客户的现实风险，不只是技术话题。"),
        "source": {"sc": "Insurance Asia 2026-10-17 一周回顾（综合 Mox、Igloo、富卫、永明、Semperis）",
                   "tc": "Insurance Asia 2026-10-17 一週回顧（綜合 Mox、Igloo、富衛、永明、Semperis）",
                   "lang": "en", "name": "Insurance Asia", "date": "2026-10-17",
                   "note": "EN原文；RSS pubDate 2026-10-16 21:00 UTC＝香港时间 10-17 05:00"},
        "tags": tlist(["数字保险", "家居保险", "富卫", "永明", "网络攻击"]),
        "actions": {"front": pair("客户对话素材：家居与网络保障缺口"),
                    "midback": pair("产品与渠道动态跟踪"),
                    "lead": pair("团队简报：一周市场要点"),
                    "cross": pair("传承需求参考")},
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "title": pair("一周回顾：Mox 推全数码家居险、Igloo 进土耳其、富卫入股 bolttech"),
    },
    # ---------- insurancebusinessmag（media 62） ----------
    {
        "id": "ibm-atradius-apac-insolvencies-2027-20261017",
        "publishedAt": "2026-10-17T01:47:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/asiapacific-insolvencies-to-fall-5-in-2027-but-credit-risks-persist-593904.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["market"],
        "themes": ["trade-credit", "insolvency", "credit-risk", "apac", "macro-outlook"],
        "summary": pair("信用保险机构 Atradius 预测，亚太区企业破产数目 2027 年将下降 5%，但下跌主要来自财政脆弱企业退出市场，而非经营环境实质好转；存活企业仍面对高借贷成本、昂贵能源与融资收紧，付款违约与交易对手信用风险未减。该行同时把 2026 年全球破产预测上调至增长 5%（较 4 月预测高 2 个百分点），2027 年预计回落 4%。亚太改善主要来自澳洲与韩国，新西兰料大幅下降，日本维持高位，新加坡则预计在 2027 年反弹。[EN原文]"),
        "why": pair("「破产数目下降≠信用风险下降」这个区分，对做贸易信用险、保证险与企业应收帐款风险盘点的团队很实用；也提示 2027 年的宏观与承保假设不宜过早转乐观。"),
        "source": {"sc": "Insurance Business 2026-10-17 报道（引述 Atradius 预测）",
                   "tc": "Insurance Business 2026-10-17 報道（引述 Atradius 預測）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-17",
                   "note": "EN原文；含 2026 全球 +5%、2027 亚太 -5% 与主要市场分化"},
        "tags": tlist(["Atradius", "贸易信用保险", "企业破产", "亚太", "信用风险"]),
        "actions": {"front": {},
                    "midback": pair("贸易信用与保证险风险跟踪"),
                    "lead": pair("团队简报：信用风险展望"),
                    "cross": pair("企业客户应收帐款风险参考")},
        "rolesImpact": {"front": 0, "midback": 2, "lead": 1, "cross": 1},
        "title": pair("Atradius：亚太破产 2027 年料减 5%　惟信用风险未解"),
    },
    {
        "id": "ibm-lockton-hk-eb-hire-20261017",
        "publishedAt": "2026-10-17T01:43:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/benefits/lockton-hires-bupa-asia-executive-to-grow-hong-kong-employee-benefits-business-593903.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer", "product"],
        "themes": ["employee-benefits", "talent", "medical-inflation", "brokers", "hong-kong"],
        "summary": pair("Lockton 聘任原保柏（Bupa）亚洲业务拓展主管 Joe Leung 为香港业务拓展高级副总裁，加入其 people solutions 团队，负责扩展香港雇员福利业务、强化与保险人和中介的关系；她拥有逾 15 年保险、医疗与雇员福利经验，涉理赔管理、客户服务与顾问工作。报道指香港医疗成本 2026 年预计上升 9.9%（2025 年为 9.7%），低于亚太平均 14%，但仍令企业医疗保险计划与理赔成本受压。Lockton 近期亦在香港、马来西亚与印度增聘高管。[EN原文]"),
        "why": pair("医疗通胀下的雇员福利，是集团客户续保时最直接的痛点；国际经纪加码香港 EB 团队，意味着团险市场的人才与客户争夺会同步升温，也反映「福利＋风险」一体化顾问模式在扩张。"),
        "source": {"sc": "Insurance Business 2026-10-17 报道（Lockton 公布）",
                   "tc": "Insurance Business 2026-10-17 報道（Lockton 公布）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-17",
                   "note": "EN原文；含香港医疗通胀 9.9% 与亚太平均 14% 对比"},
        "tags": tlist(["Lockton", "雇员福利", "医疗通胀", "人才流动", "香港"]),
        "actions": {"front": pair("企业客户福利与医疗成本对话素材"),
                    "midback": pair("团险与雇员福利市场跟踪"),
                    "lead": pair("团队简报：经纪在港扩张"),
                    "cross": {}},
        "rolesImpact": {"front": 1, "midback": 2, "lead": 1, "cross": 0},
        "title": pair("Lockton 挖角保柏亚洲主管　扩大香港雇员福利业务"),
    },
    {
        "id": "ibm-allianz-singapore-hospital-cash-20261017",
        "publishedAt": "2026-10-17T01:37:00+08:00",
        "originalUrl": "https://www.insurancebusinessmag.com/asia/news/breaking-news/allianz-singapore-pitches-hospital-cash-cover-for-income-gap-as-shield-rules-tighten-593897.aspx",
        "sourceKey": "insurancebusinessmag", "sourceTier": "media", "score": 62, "verifyStatus": "verified",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["product", "reg"],
        "themes": ["health-insurance", "hospital-cash", "shield", "product-design", "singapore"],
        "summary": pair("安盛新加坡推广「Hospital Income Protect」住院现金计划，最高每日 300 新元、住院最长 750 日，深切治疗加倍至每日 600 新元（上限 90 日），出院后最多 30 日每日 300 新元休养金，另设最高 3,000 新元意外医疗及手术费用。背景是新加坡综合健保计划（Integrated Shield Plan）自 2026 年 4 月起，新附加保障不得覆盖最低垫底费，共同保险年度上限提高至 6,000 新元，投保人自付比例上升；当地约七成居民持有综合健保计划。安盛 10 月 15 日声明指，人手短缺、药价与科技开支上升正推高医院账单。[EN原文]"),
        "why": pair("监管收紧附加保障后，市场用「现金给付型」产品填补自付缺口，是产品设计回应监管变化的典型案例。香港客户同样面对医疗通胀与自付额上升，可作对谈与产品比较参照，但须说清楚住院现金不能替代医疗报销与收入保障。"),
        "source": {"sc": "Insurance Business 2026-10-17 报道（引述安盛新加坡 10-15 声明）",
                   "tc": "Insurance Business 2026-10-17 報道（引述安盛新加坡 10-15 聲明）",
                   "lang": "en", "name": "Insurance Business", "date": "2026-10-17",
                   "note": "EN原文；含 IP 附加保障新规与给付上限；保费未披露"},
        "tags": tlist(["安盛", "住院现金", "综合健保计划", "产品设计", "新加坡"]),
        "actions": {"front": pair("客户对谈素材：现金给付与医疗报销的分别"),
                    "midback": pair("健康险产品设计参考"),
                    "lead": pair("团队简报：监管改动下的产品回应"),
                    "cross": {}},
        "rolesImpact": {"front": 2, "midback": 2, "lead": 1, "cross": 0},
        "title": pair("安盛新加坡推住院现金计划　填补健保附加保障收紧后的自付缺口"),
    },
    # ---------- insuranceasianews（pro 70，补 10-16 18:08 时段漏采） ----------
    {
        "id": "ian-donaldson-brown-jared-sun-20261016",
        "publishedAt": "2026-10-16T17:25:00+08:00",
        "originalUrl": "https://insuranceasianews.com/kiwi-broker-donaldson-brown-promotes-jared-sun-to-head-of-financial-lines/",
        "sourceKey": "insuranceasianews", "sourceTier": "pro", "score": 70, "verifyStatus": "pending",
        "contentKind": "news", "clusterCount": 1,
        "boards": ["insurer"],
        "themes": ["appointments", "financial-lines", "new-zealand", "brokers"],
        "summary": pair("新西兰经纪 Donaldson Brown 晋升 Jared Sun 为金融及专业责任险（financial lines）主管，消息来自其 LinkedIn 公布；Sun 常驻奥克兰，在保险业有逾十年经验。原文属订阅内容，公开部分仅提供上述任命与背景要点，未披露具体业务目标。[EN原文]"),
        "why": pair("亚太中型经纪正加强金融线（董事责任、专业责任、网络）的专业能力，反映企业与高净值客户的金融风险需求上升；属人才与专业能力布局的观察点，待有更多公开信息再评估影响。"),
        "source": {"sc": "InsuranceAsia News 2026-10-16 报道（LinkedIn 公布）",
                   "tc": "InsuranceAsia News 2026-10-16 報道（LinkedIn 公布）",
                   "lang": "en", "name": "InsuranceAsia News", "date": "2026-10-16",
                   "note": "EN原文；付费墙，仅标题与导语可核；属 10-16 18:08 时段漏采补录"},
        "tags": tlist(["人事任命", "金融线保险", "新西兰", "经纪"]),
        "actions": {"front": {},
                    "midback": pair("亚太经纪人事与能力布局跟踪"),
                    "lead": {},
                    "cross": {}},
        "rolesImpact": {"front": 0, "midback": 1, "lead": 1, "cross": 0},
        "title": pair("新西兰经纪 Donaldson Brown 晋升 Jared Sun 掌金融线业务"),
    },
    # ---------- ia（official 88，AIF／IAIS 补录） ----------
    {
        "id": "ia-aif-2026-iais-hong-kong-20261015",
        "publishedAt": "2026-10-15",
        "originalUrl": "https://aif.ia.org.hk/",
        "sourceKey": "ia", "sourceTier": "official", "score": 88, "verifyStatus": "verified",
        "contentKind": "press", "clusterCount": 2,
        "boards": ["reg", "market"],
        "themes": ["aif", "iais", "supervision", "ai-governance", "natcat", "hong-kong"],
        "summary": pair("保监局年度旗舰活动「亚洲保险论坛 2026」将于 11 月 13 日下午 2 时至 4 时 30 分，在红磡香港嘉里酒店举行，主题为「多维布局 韧性致远」（The Resilience Blueprint amid Polycrisis），保监局于 10 月 15 日发布相关新闻稿。同周国际保险监督官协会（IAIS）2026 年年会亦在香港举行（11 月 12 至 13 日），议程包括 AI 对保险监管的影响、巨灾保障缺口与行业韧性，并由香港特区行政长官致开幕辞。[EN原文]"),
        "why": pair("IAIS 年会与亚洲保险论坛同周在港举行，是把全球监管议程带到香港的窗口：AI 治理、巨灾保障缺口、韧性建设都会是 11 月中的主线。对前线团队而言，这是与客户谈 AI 风险、保障缺口与跨境风险的时间锚点，也便于观察监管风向。"),
        "source": {"sc": "保险业监管局「亚洲保险论坛 2026」网站、IAIS 2026 年年会议程（保监局 2026-10-15 新闻稿）",
                   "tc": "保險業監管局「亞洲保險論壇 2026」網站、IAIS 2026 年年會議程（保監局 2026-10-15 新聞稿）",
                   "lang": "zh+en", "name": "保险业监管局", "date": "2026-10-15",
                   "note": "官方来源；IA 主站受 Cloudflare 拦截，经 aif.ia.org.hk 与 iais.org 核实日期、地点与议程；属补录"},
        "tags": tlist(["亚洲保险论坛", "IAIS", "保险监管", "人工智能治理", "巨灾保障缺口"]),
        "actions": {"front": pair("客户沟通时间锚点：11 月中监管议程"),
                    "midback": pair("监管议程与主题跟踪"),
                    "lead": pair("团队简报：IAIS 年会看点"),
                    "cross": pair("跨境风险管理参考")},
        "rolesImpact": {"front": 1, "midback": 1, "lead": 2, "cross": 1},
        "title": pair("亚洲保险论坛 2026 定于 11 月 13 日　IAIS 年会同周在港举行"),
    },
]


def main():
    path = os.path.join(P, 'data/live-items.json')
    shutil.copy(path, os.path.join(P, 'data', 'live-items.json.bak-%s' % STAMP))
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
        print('  +', it['publishedAt'], '|', it['sourceKey'], '|', it['title']['sc'][:56])

    lc_path = os.path.join(P, 'data/last-check.json')
    shutil.copy(lc_path, os.path.join(P, 'data', 'last-check.json.bak-%s' % STAMP))
    lc = json.load(open(lc_path, encoding='utf-8'))
    lc['lastCheck'] = NOW
    for k, v in lc.get('sources', {}).items():
        v['last'] = NOW
    json.dump(lc, open(lc_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('last-check updated:', len(lc.get('sources', {})), 'sources at', NOW)


if __name__ == '__main__':
    main()
