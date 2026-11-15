#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一次性插入 2026-11-15 18:08 采集的条目
窗口：2026-11-13 21:08 → 2026-11-15 18:08（11-14 两次 cron 均未成功，含补录）
"""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIVE = os.path.join(BASE, "data", "live-items.json")
NOW = "2026-11-15T18:08:00+08:00"


def mk(**kw):
    return {
        "id": kw["id"],
        "clusterCount": 1,
        "score": kw["score"],
        "verifyStatus": kw.get("verifyStatus", "pending"),
        "sourceTier": kw["sourceTier"],
        "sourceKey": kw["sourceKey"],
        "title": {"sc": kw["t_sc"], "tc": kw["t_tc"]},
        "summary": {"sc": kw["s_sc"], "tc": kw["s_tc"]},
        "why": {"sc": kw["w_sc"], "tc": kw["w_tc"]},
        "actions": {
            "front": {"sc": kw["a_front"][0], "tc": kw["a_front"][1]} if kw.get("a_front") else {},
            "midback": {"sc": kw["a_mid"][0], "tc": kw["a_mid"][1]} if kw.get("a_mid") else {},
            "lead": {"sc": kw["a_lead"][0], "tc": kw["a_lead"][1]} if kw.get("a_lead") else {},
            "cross": {"sc": kw["a_cross"][0], "tc": kw["a_cross"][1]} if kw.get("a_cross") else {},
        },
        "rolesImpact": {
            "front": kw["r"][0], "midback": kw["r"][1],
            "lead": kw["r"][2], "cross": kw["r"][3],
        },
        "source": {"sc": kw["src"], "lang": kw["lang"]},
        "boards": kw["boards"],
        "themes": kw["themes"],
        "tags": {"sc": kw["tags_sc"], "tc": kw["tags_tc"]},
        "contentKind": kw["kind"],
        "publishedAt": kw["pub"],
        "originalUrl": kw["url"],
        "ingestedAt": NOW,
        "contentRole": {"sc": "本站导读", "tc": "本站導讀"},
        "featured": False,
        "evergreen": False,
        "summaryShort": {"sc": kw["s_sc"][:80], "tc": kw["s_tc"][:80]},
    }


ITEMS = []

# 1. 思派健康 300 万港元收购香港持牌经纪「正浩亚洲」90%（2026-11-14 报道）
ITEMS.append(mk(
    id="jrj-sipai-hk-broker-license-20261114",
    score=62, sourceTier="media", sourceKey="jrj", verifyStatus="verified",
    t_sc="思派健康约 300 万港元买下香港保险经纪牌照　拟做中企出海的跨境枢纽",
    t_tc="思派健康約 300 萬港元買下香港保險經紀牌照　擬做中企出海的跨境樞紐",
    s_sc="思派健康（00314.HK）以约 300 万港元收购 Star Intelligent 90% 股权，间接持有香港持牌保险经纪「正浩亚洲」90%，交易已于 10 月 16 日完成。正浩亚洲受保监局监管，专长贸易信用险、保证保险、政治风险及重大工程与能源项目再保险；思派称要把这张牌照做成跨境业务枢纽，为出海中企提供一站式风险与保险方案。",
    s_tc="思派健康（00314.HK）以約 300 萬港元收購 Star Intelligent 90% 股權，間接持有香港持牌保險經紀「正浩亞洲」90%，交易已於 10 月 16 日完成。正浩亞洲受保監局監管，專長貿易信用險、保證保險、政治風險及重大工程與能源項目再保險；思派稱要把這張牌照做成跨境業務樞紐，為出海中企提供一站式風險與保險方案。",
    w_sc="300 万港元买一张香港经纪牌照，说明香港持牌中介的「入场价」在内地产业资本眼里并不高，而它买的是跨境通道而不是本地客源。对本地经纪行的含义是：竞争不只来自同业，还来自内地健康险／医药险公司以「中企出海」为切口进场——抢的是团体与特殊风险，不是个人储蓄单。",
    w_tc="300 萬港元買一張香港經紀牌照，說明香港持牌中介的「入場價」在內地產業資本眼裡並不高，而它買的是跨境通道而不是本地客源。對本地經紀行的含義是：競爭不只來自同業，還來自內地健康險／醫藥險公司以「中企出海」為切口進場——搶的是團體與特殊風險，不是個人儲蓄單。",
    a_front=("客户若做跨境生意，贸易信用险、政治风险是切入团体与再保需求的话头", "客戶若做跨境生意，貿易信用險、政治風險是切入團體與再保需求的話頭"),
    a_mid=("留意内地产业资本进场后，经纪牌照估值与合作模式的定价变化", "留意內地產業資本進場後，經紀牌照估值與合作模式的定價變化"),
    a_lead=("香港牌照被当作「出海枢纽」，本地经纪可考虑做对接方而非硬拼价格", "香港牌照被當作「出海樞紐」，本地經紀可考慮做對接方而非硬拼價格"),
    a_cross=("中企出海风险包，是经纪与家办、律所联合获客的新品类", "中企出海風險包，是經紀與家辦、律所聯合獲客的新品類"),
    r=(1, 2, 2, 3),
    src="金融界", lang="zh",
    boards=["market"],
    themes=["broker", "mna", "cross-border"],
    tags_sc=["思派健康", "保险经纪牌照", "正浩亚洲", "中企出海", "跨境"],
    tags_tc=["思派健康", "保險經紀牌照", "正浩亞洲", "中企出海", "跨境"],
    kind="news", pub="2026-11-14T11:33:00+08:00",
    url="https://finance.jrj.com.cn/2026/11/14113359145880.shtml",
))

# 2. Insurance Asia 周报（11/9–11/13）：港费检讨、新加坡 ILP 要点表、商业险费率再跌 5%
ITEMS.append(mk(
    id="insuranceasia-week-in-insurance-20261114",
    score=68, sourceTier="media", sourceKey="insuranceasia", verifyStatus="verified",
    t_sc="Insurance Asia 周报：香港检讨保监局经费、新加坡统一投连险披露、全球商业险费率连跌九季 [EN原文]",
    t_tc="Insurance Asia 週報：香港檢討保監局經費、新加坡統一投連險披露、全球商業險費率連跌九季 [EN原文]",
    s_sc="Insurance Asia 11 月 9–13 日周报：香港保监局 11 月 4 日就年费与保费征费检讨展开公众咨询，长期业务年费非固定部分上限由 700 万港元升至 2,800 万港元；新加坡金管局将为投连险引入标准化产品要点表；台湾扩大医保覆盖，约 2,600 名癌症病人受惠；Marsh 指数显示全球商业险费率第三季再跌 5%，为连续第九季下滑。",
    s_tc="Insurance Asia 11 月 9–13 日週報：香港保監局 11 月 4 日就年費與保費徵費檢討展開公眾諮詢，長期業務年費非固定部分上限由 700 萬港元升至 2,800 萬港元；新加坡金管局將為投連險引入標準化產品要點表；台灣擴大醫保覆蓋，約 2,600 名癌症病人受惠；Marsh 指數顯示全球商業險費率第三季再跌 5%，為連續第九季下滑。",
    w_sc="三件事指向同一方向：监管在「向谁收钱、向客户披露什么」上收紧，而承保端仍在软市场——费率连跌九季。对香港市场的含义是，费用与披露成本上行、费率下行，中间的差额只能靠产品结构与高客服务补，纯价格竞争的空间越来越小。",
    w_tc="三件事指向同一方向：監管在「向誰收錢、向客戶披露什麼」上收緊，而承保端仍在軟市場——費率連跌九季。對香港市場的含義是，費用與披露成本上行、費率下行，中間的差額只能靠產品結構與高客服務補，純價格競爭的空間越來越小。",
    a_front=("跟客户谈投连险时，主动给「费用与风险一页纸」，比背产品书更有效", "跟客戶談投連險時，主動給「費用與風險一頁紙」，比背產品書更有效"),
    a_mid=("年费与征费检讨仍在咨询期，可整理成客户问答备查", "年費與徵費檢討仍在諮詢期，可整理成客戶問答備查"),
    a_lead=("软市场＋披露成本上升，团队考核宜向人均产能与续保质量倾斜", "軟市場＋披露成本上升，團隊考核宜向人均產能與續保質量傾斜"),
    a_cross=("商业险费率下行期，是企业客户重谈保障条件的窗口", "商業險費率下行期，是企業客戶重談保障條件的窗口"),
    r=(2, 2, 2, 2),
    src="Insurance Asia", lang="en",
    boards=["market", "reg"],
    themes=["pricing", "regulation", "apac"],
    tags_sc=["周报", "保费征费", "投连险披露", "商业险费率", "软市场"],
    tags_tc=["週報", "保費徵費", "投連險披露", "商業險費率", "軟市場"],
    kind="news", pub="2026-11-14T05:00:00+08:00",
    url="https://insuranceasia.com/insurance/news/week-in-insurance-hong-kong-reviews-insurer-fees-singapore-standardises-ilp-disclosures-commercial-rates-fall-5",
))

# 3. 宏利香港「宏富萬用壽險保險計劃」（2026-11-12，补录）
ITEMS.append(mk(
    id="manulife-hk-wealth-universal-life-20261112",
    score=76, sourceTier="insurer", sourceKey="manulife", verifyStatus="verified",
    t_sc="宏利香港推「宏富萬用壽險保險計劃」　终身保障＋灵活保费，瞄准财富规划需求",
    t_tc="宏利香港推「宏富萬用壽險保險計劃」　終身保障＋靈活保費，瞄準財富規劃需求",
    s_sc="宏利香港 11 月 12 日推出「宏富萬用壽險保險計劃」，属 A 类长期人寿保险计划，结合终身保障、保单价值增长潜力、具保证的保障措施与灵活保费安排；身故赔偿为保单户口价值或名义金额之较高者。宏利引述与 FT Longitude 的《财富新流向》研究：66% 香港富裕受访者正重新规划资产组合，48% 过去五年曾因人生阶段或家庭结构转变调整财富规划。",
    s_tc="宏利香港 11 月 12 日推出「宏富萬用壽險保險計劃」，屬 A 類長期人壽保險計劃，結合終身保障、保單價值增長潛力、具保證的保障措施與靈活保費安排；身故賠償為保單戶口價值或名義金額之較高者。宏利引述與 FT Longitude 的《財富新流向》研究：66% 香港富裕受訪者正重新規劃資產組合，48% 過去五年曾因人生階段或家庭結構轉變調整財富規劃。",
    w_sc="万用寿险在香港的定位一直是「高客的流动性工具」：保费灵活、现金价值可调，常与保费融资、传承架构搭配使用。保监局今年已就保费融资杠杆与零售化发出警示，这类产品在推的时候，前端话术的合规边界比产品条款本身更值得盯。",
    w_tc="萬用壽險在香港的定位一直是「高客的流動性工具」：保費靈活、現金價值可調，常與保費融資、傳承架構搭配使用。保監局今年已就保費融資槓桿與零售化發出警示，這類產品在推的時候，前端話術的合規邊界比產品條款本身更值得盯。",
    a_front=("谈万用寿险先讲「保费灵活＝可停可加」，别把它讲成高收益储蓄", "談萬用壽險先講「保費靈活＝可停可加」，別把它講成高收益儲蓄"),
    a_mid=("若客户提及保费融资，须按负担能力评估与杠杆披露要求留痕", "若客戶提及保費融資，須按負擔能力評估與槓桿披露要求留痕"),
    a_lead=("高客产品线更新要同步培训「非保证利益」的解释口径", "高客產品線更新要同步培訓「非保證利益」的解釋口徑"),
    a_cross=("万用寿险＋信托／保单分拆，是高客传承方案的标准组合", "萬用壽險＋信託／保單分拆，是高客傳承方案的標準組合"),
    r=(2, 3, 1, 2),
    src="宏利香港", lang="zh",
    boards=["product", "insurer"],
    themes=["product", "universal-life", "wealth-management"],
    tags_sc=["宏利香港", "万用寿险", "宏富", "高客", "保费融资"],
    tags_tc=["宏利香港", "萬用壽險", "宏富", "高客", "保費融資"],
    kind="press", pub="2026-11-12T00:00:00+08:00",
    url="https://manulife.com.hk/zh-hk/individual/about/newsroom/manulife-hk-launches-spectrum-universal-uife-insurance-plan.html",
))


def main():
    data = json.load(open(LIVE, encoding="utf-8"))
    items = data["items"]
    existing_ids = {i["id"] for i in items}
    existing_urls = {i.get("originalUrl") for i in items}

    added, skipped = [], []
    for it in ITEMS:
        if it["id"] in existing_ids:
            skipped.append((it["id"], "id dup"))
            continue
        if it["originalUrl"] in existing_urls:
            skipped.append((it["id"], "url dup"))
            continue
        added.append(it)

    if not added:
        print("no new items")
        return

    data["items"] = added + items
    n = len(data["items"])
    data["meta"]["itemCount"] = n
    data["meta"]["generatedAt"] = NOW
    data["meta"]["windowNote"] = {"sc": f"本库{n}条。", "tc": f"本庫{n}條。"}

    json.dump(data, open(LIVE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"inserted {len(added)} items -> total {n}")
    for it in added:
        print("  +", it["publishedAt"], it["sourceKey"], it["title"]["sc"][:60])
    for s in skipped:
        print("  skip", s)


if __name__ == "__main__":
    main()
