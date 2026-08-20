# -*- coding: utf-8 -*-
"""同步 index.html / README.md 的 Ling-3.0-flash 今晚 23:00 限免截止信息"""
import io

BASE = r"C:\Users\liuph216\WorkBuddy\automation-2026-06-08-11-21-56"
edits = []


def patch(path, pairs):
    p = BASE + "\\" + path
    with io.open(p, "r", encoding="utf-8") as f:
        s = f.read()
    for label, old, new in pairs:
        n = s.count(old)
        if n != 1:
            edits.append(("%s / %s" % (path, label), "FAIL count=%d" % n))
            continue
        s = s.replace(old, new, 1)
        edits.append(("%s / %s" % (path, label), "OK"))
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(s)
    return s.count("\ufffd")


# ---------------- index.html ----------------
idx_old_h3 = ('<h3>🔥 免费榜换王：Kimi K3 以 98 分首次登顶全部免费模型第一'
              '（经 Ollama Cloud 免费层可直接调用）· GLM-5.2 退居第二 · '
              'DeepSeek V4-Flash 0731 开源进第 4 · 腾讯 Hy3 限免仅剩 2 天</h3>')
idx_new_h3 = ('<h3>🔥 免费榜换王：Kimi K3 以 98 分首次登顶全部免费模型第一'
              '（经 Ollama Cloud 免费层可直接调用）· GLM-5.2 退居第二 · '
              'DeepSeek V4-Flash 0731 开源进第 4 · ⏰ 蚂蚁百灵 Ling-3.0-flash 限免今晚 23:00 截止 · '
              '腾讯 Hy3 限免仅剩 2 天</h3>')

idx_old_p = ('freellm.net 实测目录 424+ 免费大模型 / 30 家供应商。</p>')
idx_new_p = ('freellm.net 实测目录 424+ 免费大模型 / 30 家供应商。'
             '⏰ <b>今日最紧急窗口：蚂蚁百灵 Ling-3.0-flash（124B 总参 / 5.1B 激活、34 项评测 15 个第一、'
             'SWE-Bench Pro 56.6% 参测第一、综合均分与 DeepSeek-V4-Flash 并列第一）的 OpenRouter 与官方平台'
             '限时免费今晚 23:00（北京时间）准点关闭，期满后正式开源权重</b>。</p>')

n1 = patch("index.html", [("历史条目标题", idx_old_h3, idx_new_h3),
                          ("历史条目摘要", idx_old_p, idx_new_p)])

# ---------------- README.md ----------------
rm_old = ('场外腾讯 Hy3（91分）经 WorkBuddy/CodeBuddy 限免<b>仅剩 2 天（截止 8/5）</b>。')
rm_new = ('场外腾讯 Hy3（91分）经 WorkBuddy/CodeBuddy 限免<b>仅剩 2 天（截止 8/5）</b>。'
          '⏰ **今日最紧急窗口**：蚂蚁百灵 **Ling-3.0-flash**（7/24 发布、124B 总参 / 5.1B 激活、'
          '原生 256K 可扩 1M、34 个评测维度 15 个第一 19 个第二、综合均分与 DeepSeek-V4-Flash 并列第一、'
          'SWE-Bench Pro 56.6% 参测第一）在 OpenRouter 与百灵官方平台的**限时免费今晚 23:00（北京时间）准点关闭，'
          '免费期结束后正式开源权重**——想评测的今天务必跑完。')

rm_old2 = ('⚠️ **风险提醒**：Ollama 免费额度数值未公开、Hy3 限免 8/5 截止、')
rm_new2 = ('⚠️ **风险提醒**：⏰ Ling-3.0-flash 限免今晚 23:00 截止、Ollama 免费额度数值未公开、Hy3 限免 8/5 截止、')

n2 = patch("README.md", [("今日摘要", rm_old, rm_new),
                         ("风险提醒", rm_old2, rm_new2)])

for k, v in edits:
    print("%-28s %s" % (k, v))
print("FFFD index.html:", n1, "| README.md:", n2)
