#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 2026-10-12 00:2x increment into live-items.json.

窗口：2026-10-11T21:14（21:08 轮）→ 2026-10-12T00:22。10月11日为周日、10月12日凌晨，
香港监管（IA 通函页被 Cloudflare 拦、搜索结果最新仍为 2026-05-13 通函；IA 新闻稿无新发）、
HKMA（最新 2026-10-09）、NFRA（最新 2026-10-09）、HKFI、保司官网均无新发布。
本期新增 4 条：
 - insuranceasianews（10-11 14:07）：日本金融厅对 Prudential Life / Gibraltar Life 发出部分业务停止令，
   母企同收业务改善命令（前两轮漏采，本期补上；监管重磅）
 - insuranceasianews（10-11 12:58）：澳洲竞争审裁处暂缓 IAG-RAC Insurance 覆核，待 ACCC 公共利益裁定（前两轮漏采）
 - manulife（10-08，10-12 生效）：宏利委任 Sinéad O'Connor 为集团首席精算师（补漏，集团层面人事）
 - insurtech（10-08）：丹麦 TODAY 完成 280 万欧元种子轮，为保险/财务顾问打造合规 AI 销售作业系统（补漏）
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
    """Accept str or (sc, tc) tuple; return traditional-Chinese string."""
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

# ══ 1. 日本金融厅：对 Prudential Life 及 Gibraltar Life 发出部分业务停止令（3个月），母企同收改善命令 ══
ITEMS.append(mk(
    "ian-japan-fsa-prudential-life-gibraltar-suspension-order-20261011",
    "insuranceasianews", "media", "news",
    "2026-10-11T14:07:00+08:00",
    "https://insuranceasianews.com/japans-fsa-suspends-prudential-life-gibraltar-life-operations-for-3-months-over-employee-fraud/",
    "日本金融廳下令Prudential Life及Gibraltar Life部分停業3個月　母公司同收業務改善命令（員工不當收款逾61億日圓）",
    "日本金融廳（FSA）對美國保德信金融集團（Prudential Financial）旗下Prudential Life Insurance及Gibraltar Life Insurance發出部分業務停止令，自2026年10月13日起至2027年1月底，兩間壽險公司不得簽訂新保險合約或銷售保險產品，以便重建管理及監督體系；FSA同時向兩者的母公司Prudential Holdings of Japan發出業務改善命令，要求強化企業管治。這是FSA自2019年對日本郵政保險採取行動以來，首次對壽險公司發出停業令。事件源於Prudential Life今年1月披露逾100名現職及前員工不當向客戶收取共約31億日圓，時任社長其後辭任；10月8日發表的第三方調查報告指受害人自報損失總額超過61億日圓，並把原因歸咎於過度強調銷售業績的企業文化。公司表示將檢討高度依賴銷售佣金報酬的制度，引入最低保證薪金；社長（Hiromitsu Tokumaru）及兩名高管自願退還3個月月薪的30%。 [EN原文]",
    "佣金與業績驅動的銷售文化最終招致監管停業令，是「以客戶為中心」由口號變成監管要求的標誌性個案。兩個實務要點：①品牌要分清——出事的Prudential Life／Gibraltar Life屬美國保德信金融集團，與在香港經營的保誠（Prudential plc）是不同集團，向客戶與團隊解說時切勿混淆；②可作風險披露與銷售操守討論的真實教材（佣金結構、最低保證薪金、佣金回吐等控制手段）。",
    "與團隊分享：佣金驅動銷售文化如何觸發監管重罰",
    "高客風險披露溝通素材：保險公司操守與品牌辨識",
    "晨會提示：分清「美國保德信」與「保誠香港」，避免誤傳",
    "區域監管執法比較（日本FSA vs 香港保監局行為監管）",
    (1, 2, 3, 1), ["reg", "insurer"], ["reg", "conduct", "asia", "life"],
    ["日本金融厅", "Prudential Life", "Gibraltar Life", "业务停止令", "销售文化"],
    ("InsuranceAsia News 2026-10-11 报道（引日本时报／时事社）",
     "InsuranceAsia News 2026-10-11 報道（引日本時報／時事社）", "InsuranceAsia News", "2026-10-11",
     "EN原文；FSA 命令 2026-10-13 起生效至 2027 年 1 月底"),
    "en", 72, "verified"))

# ══ 2. 澳洲竞争审裁处暂缓 IAG-RAC Insurance 覆核，待 ACCC 公共利益裁定 ══
ITEMS.append(mk(
    "ian-australia-tribunal-halts-iag-raci-review-public-benefit-20261011",
    "insuranceasianews", "media", "news",
    "2026-10-11T12:58:00+08:00",
    "https://insuranceasianews.com/australias-competition-tribunal-halts-iag-raci-appeal-pending-accc-public-benefit-ruling/",
    "澳洲競爭審裁處暫緩IAG收購RAC Insurance覆核申請　待ACCC完成「公共利益」裁定後恢復",
    "InsuranceAsia News 10月11日報道：澳洲競爭審裁處（Australian Competition Tribunal）暫緩審理IAG及賣方母公司RACWA就ACCC否決收購RAC Insurance（涉約13.5億澳元）提出的覆核申請，原因是兩方將另行向ACCC提交「公共利益」（public benefit）申請，一旦提交，審裁處程序必須暫停至ACCC作出裁定。報道指兩方計劃在周三（10月14日）前提交申請，ACCC有50個營業日作出決定（申請人估計約2027年2月初有結果），之後審裁處的時鐘才重新起算；審裁處已把買賣雙方的覆核合併審理，並預留2027年3月底至4月中的12天聆訊。ACCC於9月23日裁定該收購會實質減少西澳汽車保險及家居財物保險的競爭，不得付諸實行；若交易最終獲批，IAG將以RAC品牌在西澳承保車險及家居保險。 [EN原文]",
    "併購審批的兩條賽道（競爭評估＋公共利益評估）與時間表，是理解競爭法如何「先問競爭損害、再問整體效益」的現成範例。香港近年整合動作（專屬自保、跨境合作、險企股權變動）增加，這類個案可作與企業客、管理層討論監管審批路徑與過渡期安排的參照。",
    "與企業客／管理層談併購審批路徑時的國際參照",
    "市場整合趨勢觀察：區域保險併購節奏",
    "團隊分享：競爭法與保險市場結構的關係",
    "與香港市場整合（自保、股權變動）個案的對照",
    (1, 1, 2, 1), ["market"], ["m-a", "competition", "australia"],
    ["IAG", "RAC Insurance", "ACCC", "竞争审裁处", "并购审批"],
    ("InsuranceAsia News 2026-10-11 报道", "InsuranceAsia News 2026-10-11 報道",
     "InsuranceAsia News", "2026-10-11", "EN原文；10-14 前提交公共利益申请"),
    "en", 64, "verified"))

# ══ 3. 宏利委任 Sinéad O'Connor 为集团首席精算师（10月12日生效）══
ITEMS.append(mk(
    "manulife-chief-actuary-sinead-oconnor-appointment-20261012",
    "manulife", "insurer", "press",
    "2026-10-08",
    "https://www.prnewswire.com/apac/news-releases/manulife-appoints-sinead-oconnor-as-chief-actuary-joining-executive-leadership-team-302902577.html",
    "宏利委任Sinéad O'Connor為集團首席精算師　10月12日生效並加入執行領導團隊",
    "宏利金融（Manulife，多倫多）10月8日宣布，委任Sinéad O'Connor為集團首席精算師（Chief Actuary），2026年10月12日生效，直接向總裁兼行政總裁Phil Witherington匯報，並加入集團執行領導團隊。O'Connor於2007年加入宏利，此前為集團有效業務管理（Inforce Management）環球主管，歷任副首席精算師、團體精算主管、美國IFRS首席精算師，並曾在年金、長期護理及財務部門擔任領導職務。 [EN原文]",
    "精算職能是長期產品定價、分紅假設與資本效率的源頭；在IFRS 17／風險為本資本制度（RBC）與CSM關注度上升的背景下，集團層面精算換帥是可留意的公司財務策略訊號。對前線而言，有助理解「產品假設由誰定、怎樣定」，日後客戶問及分紅與保證回報的可持續性時，能把討論拉回公司償付能力與投資策略而非單一數字。",
    "團隊知識補強：精算與分紅假設由誰把關",
    "與高客談長期回報可持續性時的背景理解",
    "留意集團精算人事與後續產品定價取向",
    "與RBC／IFRS 17 資本議題的連動觀察",
    (1, 3, 2, 1), ["insurer"], ["people", "insurer", "group"],
    ["宏利", "首席精算师", "人事任命", "精算", "资本效率"],
    ("Manulife 新聞稿（PR Newswire，2026-10-08）", "Manulife 新聞稿（PR Newswire，2026-10-08）",
     "Manulife / PR Newswire", "2026-10-08", "EN原文；10-12 生效"),
    "en", 76, "verified"))

# ══ 4. 丹麦 TODAY 完成 280 万欧元种子轮：保险／财务顾问的合规 AI 销售作业系统 ══
ITEMS.append(mk(
    "insurtech-today-ai-advisor-os-seed-2-8m-eur-20261008",
    "insurtech", "pro", "news",
    "2026-10-08",
    "https://tech.eu/2026/10/08/today-lands-eur28m-to-scale-its-ai-platform-for-financial-advisors",
    "丹麥TODAY完成280萬歐元種子輪　為保險及財務顧問打造「合規AI銷售作業系統」（DACH區逾3,500名顧問使用）",
    "哥本哈根及柏林的TODAY（UseToday ApS）完成280萬歐元種子輪，由德國High-Tech Gründerfonds（HTGF）與英國InsurTech Gateway共同領投，SeedX、Lucid Capital及天使投資者（包括前HDI行政總裁Herbert Rogenhofer、Tech11創辦人Pierre Dubosq）參與；此前已於一年前完成100萬歐元預種輪。其AI銷售作業系統覆蓋顧問會前、會中、會後：即時轉錄客戶會面（匿名化、不儲存音檔）、按顧問自有範本自動生成符合IDD要求的文件、於通話中提供異議處理與下一步建議提示、並可透過對話檢索歷史紀錄；另有AI模擬訓練（可設定DISC性格的模擬客戶），完成後可取得IDD持續教育學分。公司稱DACH區已有逾3,500名保險／分銷／獨立經紀顧問使用，平均每週節省5小時行政時間、收入最多提升10%，本輪資金將用於拓展德奧瑞（DACH）市場的前後台全流程自動化。 [EN原文]",
    "直接對應「IFA AI賦能」主線：把會議轉錄、合規文件（IDD相當於持牌人建議紀錄與培訓要求）與演練教練三合一，是可對標落地的工具形態。可用於設計團隊AI工作流的取捨討論——哪些交給AI（紀錄、範本、演練），哪些必須由持牌人簽署負責，以及AI模擬客戶訓練如何嵌入新人培育。",
    "團隊AI工作流設計參考：紀錄、文件、演練三合一",
    "新人培育：AI模擬客戶演練與持續教育學分",
    "合規邊界討論：AI生成文件的責任歸屬",
    "對標工具選型：顧問端 AI 產品形態",
    (3, 2, 3, 2), ["tech"], ["insurtech", "ai", "advisor-productivity", "distribution"],
    ["insurtech", "AI销售系统", "顾问生产力", "IDD合规", "种子轮"],
    ("Tech.eu 2026-10-08 报道", "Tech.eu 2026-10-08 報道", "Tech.eu", "2026-10-08",
     "EN原文；前轮未采集，本期补漏"),
    "en", 70, "verified"))


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
