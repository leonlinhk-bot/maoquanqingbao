# 猫圈儿 · 使用度 Worker

微观行为聚合：搜索词 / 条目打开 / 视图切换 / 角色选择 / 海报下载。

## 一次性部署

```bash
cd /Users/leonliang/maoquanqingbao/workers/usage

# 1. 登录（浏览器 OAuth，比 API token 省事）
npx wrangler login

# 2. 建 KV
npx wrangler kv namespace create USAGE_KV
# 把返回的 id 填进 wrangler.toml 的 id =

# 3. 部署
npx wrangler deploy
# 记下 workers.dev 域名，例如 https://hkii-usage.<subdomain>.workers.dev
```

## 接到主站

1. 打开 `index.html`，把 `window.HKII_USAGE_ENDPOINT` 改成 Worker URL（无尾斜杠）
2. 可选：把 `window.HKII_CF_BEACON` 填成 Cloudflare Web Analytics token
3. `bash scripts/publish.sh`

自定义路由（可选，需橙云）：在 Cloudflare 给 `hkmaoquanqingbao.com` 加 Worker 路由 `api.hkmaoquanqingbao.com/*`，前端 endpoint 改成 `https://api.hkmaoquanqingbao.com`。

## 前端事件

| t | v | 触发 |
|---|---|------|
| search | 搜索词 | 确认搜索（Enter / compositionend / 点热搜） |
| open | itemId | 打开详情抽屉 |
| view | viewId | 切换导航（今日脉搏/全部动态…） |
| role | roleId | 切换四角色 |
| poster | dark/light | 下载海报 |
| fav | — | 收藏 |
| export | — | 导出 MD |

## 读数

```bash
# 热搜
curl -s 'https://hkii-usage.xxx.workers.dev/hot?n=20&days=14' | jq

# 7 日汇总
curl -s 'https://hkii-usage.xxx.workers.dev/stats?days=7' | jq
```

## 隐私

- 不采 PII、不采 cookie、不采指纹
- 搜索词过滤拼音中间态
- IP 仅做内存 rate limit，不落 KV
- CORS 锁生产域名
