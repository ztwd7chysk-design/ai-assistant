'''
Python 基础 05：for循环
'''

#==== 1.遍历列表  ====
tasks = ["学Python","写代码","整理笔记","提交Git"]

for task in tasks:
    print(f"待办:{task}")
    
#==== 2.代编号的遍历 ====
for i,task in enumerate(tasks):
    print(f"{i+1}.{task}")
    
#==== 3.遍历字典 ====
person = {
    "name" : "张三",
    "age" : 18,
    "city" : "厦门"
    }

for key,value in person.items():
    print(f"{key}:{value}")
    
print(person.items())

# ==== 4.在循环中用if ====
texts = [
    "明天下午三点开会",
    "突然想到一个好主意",
    "记住 nginx 配置路径"
]


for text in texts:
    if "开会" in text:
        category = "任务"
    elif "想到" in text:
        category = "想法"
    elif "记住" in text:
        category = "备忘"
    else:
        category = "其他"
    print(f"[{category}] {text}")
    
    
# ==== 动手练习 ====
# 1.创建一个包含 5 个数字的列表，用for循环打印每个数的平方
# 2.创建一个字典（名字：年龄），用for循环逐个打印“xxx今年x岁"



numbers = [input(),input(),input(),input(),input()]

for number in numbers:
    num = int(number)
    print(num*num)
    
    
#第一个问题


person = {
    "小明" : input(),
    "小王" : input()
}

for name,age in person.items():
    print(f"{name}的年龄是{age}")