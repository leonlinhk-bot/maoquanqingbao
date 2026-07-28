# 猫圈儿港险情报站 · Agent & API 接入

## 三条路径

### 1. JSON Feed（推荐）
- 精选：https://hkmaoquanqingbao.com/feed/featured.json
- 全量索引：https://hkmaoquanqingbao.com/feed/all.json

无需 API Key，匿名只读。按需缓存，建议≥60s 间隔。

### 2. RSS
- https://hkmaoquanqingbao.com/feed/featured.xml

推荐读取频率≥30 分钟。收到 429 按 Retry-After 退避。

### 3. Web
- https://hkmaoquanqingbao.com

每日打开「今日脉搏 / 全部动态 / 角色日报」，顶部角色切片视图。

## 示例问法

给 AI Agent 用的中文自然语言（安装本站 Skill 后）：

- 过去 24 小时港险监管与产品最重要的 5 件事？
- 只给我中后台合规视角，忽略促销。
- 佣金分摊与转介费相关规则时间线。
- 把本周精选同步成 Markdown 清单。

## 数据契约

### featured.json 条目字段

| 字段 | 类型 | 说明 |
|------|------|------|
| id | string | 唯一条目标识 |
| title | string | 中文标题 |
| summary | string | 摘要（120-200 字） |
| why | string | 推荐理由 |
| sourceLabel | string | 信源名称 |
| sourceTier | string | official / insurer / pro / media |
| tags | string[] | 标签 |
| themes | string[] | 12 主题码之一 |
| publishedAt | ISO 8601 | 发布时间 |
| effectiveAt | ISO 8601 | 生效日期（可选） |
| score | number | 60-99 质量分 |
| originalUrl | string | 权威原文链接 |
| canonicalUrl | string | 本站阅读页链接 |
| verifyStatus | string | verified / pending |
| rolesImpact | object | {front, midback, lead, cross} 影响强度 0-3 |

## 使用与免责

- 摘要与动作卡由人工/AI 二次整理，数字与政策引用前必须打开原文 URL 复核。
- 对外发布请保留来源与 canonical；本站导读不构成销售建议、投资建议或法律意见。
- 公开可读 ≠ 可忽略版权与频率合同；禁止批量绕过限流的爬取。
- 不承诺 SLA，请自备缓存与降级。角色切片仅改变排序与动作卡，不改变事实本身。
