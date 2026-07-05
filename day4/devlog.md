# 2026-07-03（周五）Day4 - 函数入门

## 完成
- 函数 def：定义、参数、return、调用 — basics_06_function.py
- 函数封装分类逻辑：get_category()、classify() 返回字典
- 奇数偶数判断：is_even(n) 用 % 取模运算
- 建立每日工作流：新建文件夹 → TODO.md → 学习 → devlog.md → Git 提交

## 关键理解
- return 做两件事：(1) 结束函数 (2) 把结果交还给调用者
- return vs print：print 只显示，return 可以存变量继续用
- 函数就是"打包好的逻辑"——之前写的 if 分类，包成函数就能反复调用
- % 是取模运算符，n % 2 == 0 判断偶数

## 遇到问题
- 文件名多了逗号（basics_06_function,.py）→ 重命名
- classify() 中误写 {text}（set）→ 应为 text（字符串）
- 又犯了 if/if 而非 if/elif 的问题

## 未完成（顺延至明天）
- basics_07_json.py（json.loads/dumps）
- basics_08_file.py（文件读写）
- basics_09_try.py（try/except）
- basics_10_import.py（import 与模块）
- 阅读并理解 classifier.py

## 明天
- 完成 Day4 剩余任务
- 综合练习：手动分类器
- 阅读 + 独立重写 classifier.py
