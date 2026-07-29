# 邮件发送指南

## 方法一：Python 脚本（最稳）

```bash
# 1. 获取 Gmail App Password（一次性）
# 打开 https://myaccount.google.com/apppasswords
# → 「选择应用」选「邮件」
# → 「选择设备」选「Mac」
# → 复制 16 位密码（格式: xxxx xxxx xxxx xxxx）

# 2. 设置环境变量（每次开终端时）
export GMAIL_APP_PASSWORD="你的16位密码"

# 3. 发送周报
cd ~/maoquanqingbao
python3 scripts/send-digest.py --period weekly --to weigangmaoquan@gmail.com

# 4. 发送日报（可选）
python3 scripts/send-digest.py --period daily --to weigangmaoquan@gmail.com
```

## 方法二：手动 mailto（快）

在数据下载页点击「打开 Gmail 写信」→ 自动填充标题和正文 → 手动粘贴摘要内容。

## 方法三：Cron 定时发送（后续）

配置完 App Password 后：
```bash
# 每周六 10:00 发送周报到你的 Gmail
cronjob create --name "情报站周报" \
  --schedule "0 10 * * 6" \
  --prompt "在 ~/maoquanqingbao 执行 python3 scripts/send-digest.py --period weekly --to weigangmaoquan@gmail.com"
```

## 注意事项

- App Password 不要提交到 Git（已在 .gitignore 中排除 .env）
- Gmail 每日有发送上限（普通账号 ~500 封/天，足够用）
- 首次发送可能被 Gmail 标记为「可疑邮件」，在收件箱点「这不是垃圾邮件」即可
