# -*- coding: utf-8 -*-
import json, datetime, shutil

TZ = datetime.timezone(datetime.timedelta(hours=8))
NOW = datetime.datetime.now(TZ)
NOW_ISO = NOW.strftime('%Y-%m-%dT%H:%M:%S+08:00')

item = {
    "clusterCount": 1,
    "score": 68,
    "verifyStatus": "pending",
    "sourceTier": "media",
    "contentKind": "news",
    "actions": {
        "front": {
            "sc": "客户问及保德信时先厘清主体（美国保德信金融／日本保德信生命 vs 香港保诚 Prudential plc，两者无股权关系），不借同业负面事件作比较或销售话术",
            "tc": "客戶問及保德信時先釐清主體（美國保德信金融／日本保德信生命 vs 香港保誠 Prudential plc，兩者無股權關係），不借同業負面事件作比較或銷售話術",
        },
        "midback": {
            "sc": "把「员工私下收取客户资金、向客户借款、代客投资」列入销售行为红线自查清单，并检查佣金以外一切资金往来的留痕与举报渠道",
            "tc": "把「員工私下收取客戶資金、向客戶借款、代客投資」列入銷售行爲紅線自查清單，並檢查佣金以外一切資金往來的留痕與舉報渠道",
        },
        "lead": {
            "sc": "把海外监管处罚案例纳入新人合规课，说明「业务停止令」对业务连续性的实际冲击远大于罚款，而不只是罚款金额",
            "tc": "把海外監管處罰案例納入新人合規課，說明「業務停止令」對業務連續性的實際衝擊遠大於罰款，而不只是罰款金額",
        },
        "cross": {
            "sc": "涉及日本、美国寿险的客户咨询，以当地监管原文与公司公告为准，不引用二手摘要或无出处数字作依据",
            "tc": "涉及日本、美國壽險的客戶諮詢，以當地監管原文與公司公告爲準，不引用二手摘要或無出處數字作依據",
        },
    },
    "rolesImpact": {"front": 1, "midback": 2, "lead": 2, "cross": 1},
    "boards": ["reg", "insurer"],
    "themes": ["reg", "life", "japan", "conduct", "enforcement"],
    "tags": {
        "sc": ["日本保德信", "日本金融厅FSA", "部分业务停止令", "不当销售", "消费者赔偿", "Prudential Financial"],
        "tc": ["日本保德信", "日本金融廳FSA", "部分業務停止令", "不當銷售", "消費者賠償", "Prudential Financial"],
    },
    "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
    "featured": False,
    "evergreen": False,
    "ingestedAt": NOW_ISO,
    "id": "ian-prudential-life-japan-fsa-suspension-20261004",
    "sourceKey": "insuranceasianews",
    "publishedAt": "2026-10-04T14:25:00+08:00",
    "originalUrl": "https://insuranceasianews.com/japan-watchdog-moves-to-suspend-prudential-life-insurance-over-fraud-scandal/",
    "title": {
        "sc": "日本金融厅拟对保德信生命保险发出部分业务停止令：107名员工涉不当收取客户资金、历时34年、涉资约2,340万美元，停售期料逾三个月 [EN原文]",
        "tc": "日本金融廳擬對保德信生命保險發出部分業務停止令：107名員工涉不當收取客戶資金、歷時34年、涉資約2,340萬美元，停售期料逾三個月 [EN原文]",
    },
    "summary": {
        "sc": "InsuranceAsia News 10月4日报道：日本金融厅（FSA）拟对美国保德信金融集团（Prudential Financial）旗下日本保德信生命保险发出部分业务停止令，暂停其新保单取得与销售活动三个月以上。据报1991至2025年间共107名在职及离职员工以不当投资招揽、向客户借款等方式，令约500名客户合共损失约2,340万美元；该公司自2026年2月9日起已自愿停售新单，停售期料至今年11月5日。 [EN原文]",
        "tc": "InsuranceAsia News 10月4日報道：日本金融廳（FSA）擬對美國保德信金融集團（Prudential Financial）旗下日本保德信生命保險發出部分業務停止令，暫停其新保單取得與銷售活動三個月以上。據報1991至2025年間共107名在職及離職員工以不當投資招攬、向客戶借款等方式，令約500名客戶合共損失約2,340萬美元；該公司自2026年2月9日起已自願停售新單，停售期料至今年11月5日。 [EN原文]",
    },
    "why": {
        "sc": "这类「业务停止令＋消费者赔偿」的组合值得香港团队细看：一是说明不当销售的真实成本最终以停售、逐案赔偿与声誉折损的形式一次性还清，对业务连续性的杀伤大于罚款；二是涉事行为（向客户借款、私下收取资金、代客投资）本身即合规红线，可直接用作销售行为自查与新人培训的反面教材；三是提醒区分主体——美国保德信金融集团、日本保德信生命与香港保诚（Prudential plc）并无股权关系，客户问起时不要混为一谈。",
        "tc": "這類「業務停止令＋消費者賠償」的組合值得香港團隊細看：一是說明不當銷售的真實成本最終以停售、逐案賠償與聲譽折損的形式一次性還清，對業務連續性的殺傷大於罰款；二是涉事行爲（向客戶借款、私下收取資金、代客投資）本身即合規紅線，可直接用作銷售行爲自查與新人培訓的反面教材；三是提醒區分主體——美國保德信金融集團、日本保德信生命與香港保誠（Prudential plc）並無股權關係，客戶問起時不要混爲一談。",
    },
    "source": {
        "sc": "InsuranceAsia News 2026-10-04 14:25 [EN原文]",
        "tc": "InsuranceAsia News 2026-10-04 14:25 [EN原文]",
        "lang": "en",
    },
}

# --- 1. live-items.json ---
p = 'data/live-items.json'
shutil.copy(p, 'data/live-items.json.bak-1004-1808')
d = json.load(open(p, encoding='utf-8'))
ids = {it['id'] for it in d['items']}
assert item['id'] not in ids, 'duplicate id'
d['items'].insert(0, item)
n = len(d['items'])
d['meta']['itemCount'] = n
d['meta']['generatedAt'] = NOW_ISO
d['meta']['windowNote'] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('live-items.json updated: items =', n)

# --- 2. last-check.json ---
lp = 'data/last-check.json'
lc = json.load(open(lp, encoding='utf-8'))
lc['lastCheck'] = NOW_ISO
for k, v in lc.get('sources', {}).items():
    v['last'] = NOW_ISO
json.dump(lc, open(lp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('last-check.json updated:', NOW_ISO, '| sources:', len(lc.get('sources', {})))
