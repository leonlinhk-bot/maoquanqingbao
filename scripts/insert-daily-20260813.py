#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert daily collected items (2026-08-13 catch-up run) into live-items.json + update last-check.json."""
import json
from pathlib import Path
from datetime import datetime, timezone, timedelta

ROOT = Path(__file__).resolve().parent.parent
LIVE = ROOT / 'data/live-items.json'
LASTCHECK = ROOT / 'data/last-check.json'
HKT = timezone(timedelta(hours=8))
INGESTED = datetime.now(HKT).isoformat(timespec='seconds')


def item(id_, score, verify, tier, key, title_sc, title_tc, sum_sc, sum_tc,
         why_sc, why_tc, actions, roles, src_sc, lang, boards, themes,
         tags_sc, tags_tc, kind, published, url):
    return {
        "id": id_, "clusterCount": 1, "score": score, "verifyStatus": verify,
        "sourceTier": tier, "sourceKey": key,
        "title": {"sc": title_sc, "tc": title_tc},
        "summary": {"sc": sum_sc, "tc": sum_tc},
        "why": {"sc": why_sc, "tc": why_tc},
        "actions": actions, "rolesImpact": roles,
        "source": {"sc": src_sc, "lang": lang},
        "boards": boards, "themes": themes,
        "tags": {"sc": tags_sc, "tc": tags_tc},
        "contentKind": kind, "publishedAt": published, "originalUrl": url,
        "ingestedAt": INGESTED,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False, "evergreen": False,
    }


def L(sc, tc):
    return {"sc": sc, "tc": tc}


new_items = [
    # 1. SCMP: HSBC insurance division reshuffle after Moncreiffe exit (Aug 12 19:53)
    item(
        "scmp-hsbc-insurance-reshuffle-20260812", 68, "verified", "media",
        "scmp:hsbc-insurance-reshuffle-20260812",
        "汇丰重组保险部门：全球保险业务CEO离任 曾翠琼、张凯即任联席CEO",
        "滙豐重組保險部門：全球保險業務CEO離任 曾翠瓊、張凱即任聯席CEO",
        "据汇丰内部备忘录，全球保险业务行政总裁Edward Moncreiffe离职「寻求外部机会」，即日起由汇丰人寿香港行政总裁曾翠琼与国际财富及卓越理财亚洲主管张凯出任保险业务联席CEO，两人继续兼任原职。备忘录由国际财富及卓越理财CEO Barry O'Byrne及亚洲、中东联席CEO共同签发，强调保险是服务富裕至超高净值客户的领先财富管理关键。Moncreiffe于2024年出任现职，在汇丰任职逾二十年。[EN原文]",
        "據滙豐內部備忘錄，全球保險業務行政總裁Edward Moncreiffe離職「尋求外部機會」，即日起由滙豐人壽香港行政總裁曾翠瓊與國際財富及卓越理財亞洲主管張凱出任保險業務聯席CEO，兩人繼續兼任原職。備忘錄由國際財富及卓越理財CEO Barry O'Byrne及亞洲、中東聯席CEO共同簽發，強調保險是服務富裕至超高淨值客戶的領先財富管理關鍵。",
        "汇丰保险高管更替并拆分联席架构，直接影响其香港银保渠道策略与保险分销格局，是观察外资银行保险业务走向的重要信号。",
        "滙豐保險高管更替並拆分聯席架構，直接影響其香港銀保渠道策略與保險分銷格局，是觀察外資銀行保險業務走向的重要信號。",
        {"front": L("银保渠道人事变动=合作沟通要点", "銀保渠道人事變動=合作溝通要點"), "midback": {}, "lead": {}, "cross": L("汇丰重组影响港险分销格局", "滙豐重組影響港險分銷格局")},
        {"front": 2, "midback": 2, "lead": 2, "cross": 2},
        "SCMP 南华早报", "en",
        ["insurer", "market"], ["people", "distribution"],
        ["汇丰", "保险业务", "人事变动", "联席CEO", "银保"], ["滙豐", "保險業務", "人事變動", "聯席CEO", "銀保"],
        "news", "2026-08-12T19:53:30+08:00",
        "https://www.scmp.com/business/banking-finance/article/3363806/hsbc-reshuffles-insurance-division-after-ceos-surprise-departure-internal-memo",
    ),
    # 2. InsuranceAsia News: PICC appoints Tan Jiong as chairman (Aug 12)
    item(
        "picc-tan-jiong-chairman-20260812", 66, "pending", "media",
        "insuranceasia:picc-tan-jiong-chairman-20260812",
        "中国人保委任谭炯为执行董事兼董事长 待股东会及金融监管总局核准",
        "中國人保委任譚炯為執行董事兼董事長 待股東會及金融監管總局核准",
        "中国人民保险集团公告，董事会通过提名谭炯为执行董事兼董事长。谭炯现年60岁，曾任国家开发银行副董事长、行长，早年长期任职中行、工行并曾任贵州省副省长；任期待股东会审议及国家金融监管总局核准任职资格后生效，人保将于8月28日召开临时股东会。前任董事长丁向群已于5月履新金融监管总局党委书记、局长，人保帅印空缺近两月后补齐。[EN原文]",
        "中國人民保險集團公告，董事會通過提名譚炯為執行董事兼董事長。譚炯現年60歲，曾任國家開發銀行副董事長、行長，早年長期任職中行、工行並曾任貴州省副省長；任期待股東會審議及國家金融監管總局核准任職資格後生效，人保將於8月28日召開臨時股東會。前任董事長丁向群已於5月履新金融監管總局黨委書記、局長。",
        "人保作为国内保险龙头的人事落定，标志保险业「一把手」换届完成，其战略延续性对内地保险市场及在港上市中资险企估值具有参照意义。",
        "人保作為國內保險龍頭的人事落定，標誌保險業「一把手」換屆完成，其戰略延續性對內地保險市場及在港上市中資險企估值具有參照意義。",
        {"front": {}, "midback": {}, "lead": L("央企险企掌门更替=行业风向", "央企險企掌門更替=行業風向"), "cross": {}},
        {"front": 1, "midback": 2, "lead": 2, "cross": 1},
        "InsuranceAsia News", "en",
        ["insurer"], ["people", "china"],
        ["中国人保", "谭炯", "董事长", "丁向群", "金融监管总局"], ["中國人保", "譚炯", "董事長", "丁向群", "金融監管總局"],
        "news", "2026-08-12T15:13:19+08:00",
        "https://insuranceasianews.com/picc-appoints-veteran-banker-tan-jiong-as-chairman/",
    ),
    # 3. InsuranceAsia News: Typhoon Dolphin US$178m losses, Ping An payouts (Aug 12)
    item(
        "typhoon-dolphin-178m-20260812", 65, "pending", "media",
        "insuranceasia:typhoon-dolphin-178m-20260812",
        "台风「白海豚」五地接报案近10万件 估损12亿元 平安预估赔付超9600万美元",
        "颱風「白海豚」五地接報案近10萬件 估損12億元 平安預估賠付超9600萬美元",
        "InsuranceAsia News引述监管数据：台风「白海豚」登陆后，浙江、上海、江苏、江西、宁波五地保险机构累计接报案近10万件，估损12亿元人民币（约1.78亿美元），其中平安预估赔付超9600万美元。此前金融监管总局披露，针对近期强降雨、台风等灾害，22省份保险业累计已赔付76亿元、赔付进度57%。[EN原文]",
        "InsuranceAsia News引述監管數據：颱風「白海豚」登陸後，浙江、上海、江蘇、江西、寧波五地保險機構累計接報案近10萬件，估損12億元人民幣（約1.78億美元），其中平安預估賠付超9600萬美元。此前金融監管總局披露，針對近期強降雨、颱風等災害，22省份保險業累計已賠付76億元、賠付進度57%。",
        "从监管总额到头部险企个案赔付的量化，为巨灾建模与再保定价提供最新参照，亦可用于客户理赔预期沟通。",
        "從監管總額到頭部險企個案賠付的量化，為巨災建模與再保定價提供最新參照，亦可用於客戶理賠預期溝通。",
        {"front": {}, "midback": L("巨灾赔付数据=再保与定价参照", "巨災賠付數據=再保與定價參照"), "lead": {}, "cross": {}},
        {"front": 1, "midback": 2, "lead": 1, "cross": 1},
        "InsuranceAsia News", "en",
        ["insurer", "market"], ["natcat", "claims"],
        ["台风白海豚", "平安", "理赔", "巨灾", "估损"], ["颱風白海豚", "平安", "理賠", "巨災", "估損"],
        "news", "2026-08-12T14:23:38+08:00",
        "https://insuranceasianews.com/typhoon-dolphin-losses-hit-us178m-as-beijing-battles-heavy-rain-floods/",
    ),
    # 4. SCMP: HK property recovery vs widening offshore tax net (Aug 12 07:51)
    item(
        "scmp-hk-property-tax-net-20260812", 66, "verified", "media",
        "scmp:hk-property-tax-net-20260812",
        "内地拓宽境外征税网 香港楼市复苏面临新风险 保险放缓亦拖累写字楼需求",
        "內地拓寬境外徵稅網 香港樓市復甦面臨新風險 保險放緩亦拖累寫字樓需求",
        "南华早报分析：若内地对境外财富的监管整治由保险收益延伸至物业，香港楼市复苏将受新考验。瑞银估算对香港住宅投资收入征20%税，将使净租金回报率由约2.2%降至1.8%，与内地一线城市水平大致拉平；港险业务放缓亦将拖累写字楼需求——保险公司截至2025年10月占用约6%的香港甲级写字楼存量（世邦魏理仕数据）。[EN原文]",
        "南華早報分析：若內地對境外財富的監管整治由保險收益延伸至物業，香港樓市復甦將受新考驗。瑞銀估算對香港住宅投資收入徵20%稅，將使淨租金回報率由約2.2%降至1.8%，與內地一線城市水平大致拉平；港險業務放緩亦將拖累寫字樓需求——保險公司截至2025年10月佔用約6%的香港甲級寫字樓存量（世邦魏理仕數據）。",
        "把港险征税议题延伸至楼市与写字楼市场的传导分析，是高净值客户沟通「香港资产配置」时稀缺的跨资产视角。",
        "把港險徵稅議題延伸至樓市與寫字樓市場的傳導分析，是高淨值客戶溝通「香港資產配置」時稀缺的跨資產視角。",
        {"front": L("征税传导=跨资产客户沟通", "徵稅傳導=跨資產客戶溝通"), "midback": {}, "lead": {}, "cross": L("税务整治影响在港资产配置", "稅務整治影響在港資產配置")},
        {"front": 2, "midback": 1, "lead": 1, "cross": 3},
        "SCMP 南华早报", "en",
        ["market"], ["taxation", "cross-border"],
        ["港险征税", "香港楼市", "租金回报率", "写字楼", "境外征税"], ["港險徵稅", "香港樓市", "租金回報率", "寫字樓", "境外徵稅"],
        "news", "2026-08-12T07:51:55+08:00",
        "https://www.scmp.com/business/article/3363634/hong-kong-property-recovery-faces-new-risk-china-widens-offshore-tax-net",
    ),
    # 5. 广西金融监管局: crackdown on unauthorized use of broker/agent wording (Aug 12)
    item(
        "gx-broker-name-compliance-20260812", 62, "verified", "media",
        "toutiao:gx-broker-name-compliance-20260812",
        "广西金融监管局：严查违规使用「保险代理」「保险经纪」字样经营主体",
        "廣西金融監管局：嚴查違規使用「保險代理」「保險經紀」字樣經營主體",
        "广西金融监管局8月12日公告：保险代理、保险经纪属金融特许经营业务，企业名称或经营范围含「保险代理」「保险经纪」等字样的经营主体，实际从事相关业务的须依法取得金融监管总局及派出机构许可；未取得许可的须尽快变更名称及经营范围、删除相关字样，逾期不改将由金融、市场监管部门依法从严处理。",
        "廣西金融監管局8月12日公告：保險代理、保險經紀屬金融特許經營業務，企業名稱或經營範圍含「保險代理」「保險經紀」等字樣的經營主體，實際從事相關業務的須依法取得金融監管總局及派出機構許可；未取得許可的須盡快變更名稱及經營範圍、刪除相關字樣，逾期不改將由金融、市場監管部門依法從嚴處理。",
        "内地对保险中介字样的特许经营整治趋严，对涉足内地获客或转介的港险渠道有合规提示意义，避免踩入无牌经营红线。",
        "內地對保險中介字樣的特許經營整治趨嚴，對涉足內地獲客或轉介的港險渠道有合規提示意義，避免踩入無牌經營紅線。",
        {"front": L("中介字样整治=渠道合规提示", "中介字樣整治=渠道合規提示"), "midback": {}, "lead": {}, "cross": {}},
        {"front": 2, "midback": 2, "lead": 1, "cross": 1},
        "金融界·保险晚餐（广西金融监管局公告）", "zh",
        ["compliance"], ["channel", "compliance"],
        ["保险代理", "保险经纪", "特许经营", "广西金融监管局", "无牌经营"], ["保險代理", "保險經紀", "特許經營", "廣西金融監管局", "無牌經營"],
        "circular", "2026-08-12T00:00:00+08:00",
        "http://m.toutiao.com/group/7673136546282832399/",
    ),
]

# ---- insert into live-items.json ----
data = json.loads(LIVE.read_text(encoding='utf-8'))
existing_keys = {it.get('sourceKey') for it in data['items']}
added = []
for it in new_items:
    if it['sourceKey'] in existing_keys:
        print(f"SKIP duplicate: {it['sourceKey']}")
        continue
    added.append(it)
    existing_keys.add(it['sourceKey'])

data['items'] = added + data['items']
data['meta']['generatedAt'] = INGESTED
data['meta']['itemCount'] = len(data['items'])
LIVE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print(f"Inserted {len(added)} items. Total: {len(data['items'])}")

# ---- update last-check.json (checkpoint mechanism) ----
now = datetime.now(HKT).isoformat(timespec='seconds')
lc = json.loads(LASTCHECK.read_text(encoding='utf-8'))
lc['lastCheck'] = now
for key, src in lc['sources'].items():
    src['last'] = now
LASTCHECK.write_text(json.dumps(lc, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
print("last-check.json updated ->", now)
