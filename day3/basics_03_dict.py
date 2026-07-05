'''
Python 基础 03：字典
'''


#==== 1.创建字典：键值对 ====

person = {
    "name":"张三",
    "age":18,
    "city":"厦门"
}
#感觉有点像结构体
print (person)


#==== 2. 取值 ====

print(person["name"])
print(person.get("name"))  #推荐：get写法，key存在时，返回对应的值
print(person.get("height","身高"))  #key不存在时，返回默认值
#不变 = 能当 key，可变 = 不能当 key

#==== 3. 修改和新增 ====
person["age"] = 19
person["job"] = "学生"
print(person)


#==== 4. 字典就是 JSON 的 Python 形式 ====
# 你分类器要返回的就是这样一个字典：
result = {
    "category": "任务",
    "summary": "明天下午开会",
    "extracted": {
        "time": "明天下午3点",
        "people": ["张三"]
    }
}

print(result["category"])              # 任务
print(result["extracted"]["time"]) 


# ===== 动手练习 =====
# 1. 创建一个字典，存你自己的信息（名字、年龄、城市、爱好列表）
# 2. 用 .get() 取出 3 个不同的值
# 3. 新增一个键值对，比如"学习目标"


me = {
    "name":"yhy",
    "age":18,
    "city" : "厦门",
    "hobbies":["打篮球","看书"]
}

print(me.get("name"))
print(me.get("age"))
print(me.get("hobbies"))

me["goal"] = "成为一名优秀的程序员"
print(me.get("goal"))
print(me)
