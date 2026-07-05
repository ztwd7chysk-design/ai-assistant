'''
JSON 格式练习
日期: 2026-07-01
'''

import json

# ======1. 字典 -> JSON 字符串 =======
person = {
    "name":"张三",
    "age": 18,
    "hobbies": ["看书","写代码"],
    "address": {
        "city": "厦门",
        "street": "思明区"
    }
}
json_str = json.dumps(person,ensure_ascii=False,indent=2)
print("python 字典 -> JSON 字符串")
print(json_str)
print(type(json_str))   # <class 'str'>


#======2. JSON 字符串 -> 字典 =======
