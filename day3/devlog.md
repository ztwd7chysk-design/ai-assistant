# 2026-07-02（周三）Day3 - Python 基础速成

## 完成
- 变量与数据类型（str, int, float, bool）— basics_01_variables.py
- 列表：创建、索引、len() — basics_02_list.py
- 字典：键值对、get()、嵌套取值、key 规则（不可变类型）— basics_03_dict.py
- if/elif/else 条件判断：比较运算符、逻辑运算符（and/or/not）、in 关键词 — basics_04_if.py
- for 循环：遍历列表、enumerate 编号、遍历字典（.items()/.values()）、循环中嵌套 if — basics_05_for.py
- JSON 基础操作：json.loads/dumps 练习 — json_practice.py

## 关键理解
- 列表 vs C 数组：列表可存不同类型，数组只能同类型
- 字典 vs C 结构体：字典字段运行时可变，结构体编译时固定
- 不可变类型才能当 key：str/int/tuple 可以，list/dict 不行
- enumerate() 是自动编号器，本质是每次返回 (序号, 元素)
- .items() 把字典拆成 (key, value) 元组对，for 循环解包取值
- input() 永远返回字符串，要数学运算需 int() 或 float() 转换

## 遇到问题
- if/if/if 和 if/elif/elif 的区别：用 if 不会互斥，可能触发多个分支；用 elif 只会命中一个
- 遍历字典时 for x in dict 拿到的是 key，要取值用 .values()，俩都要用 .items()

## 未完成（顺延至明天）
- basics_06_function.py（函数 def）
- 阅读并理解 classifier.py

## 明天（Day4）
- 完成函数 def 学习
- 阅读 classifier.py，逐行理解
- 独立重写分类器核心逻辑
- 如时间允许，进入 Day4 原计划任务
