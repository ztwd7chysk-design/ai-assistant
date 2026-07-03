'''
Python 基础 06：函数
'''

#==== 1. 定义和调用 ====
def greet(name):
    '''向某人打招呼'''
    return f"你好，{name}"
print(greet("张三"))
print(greet("李四"))

#==== 2. 函数就是"打包好的逻辑" ====
#之前写过的分类逻辑，包成函数就能反复使用：
def get_category(text):
    if "开会" in text:
        return "任务"
    elif "想到" in text:
        return "想法"
    elif "记住" in text:
        return "备忘"
    else :
        return "其他"
    
print (get_category(input()))     


#==== 3.return 做两件事 =====
# (1) 结束函数  (2) 把结果还给调用者
def add(a,b):
    return a+b
result = add(3,5)
print(result)

# ===== 动手练习 =====
# 1. 写一个函数 is_even(n)，偶数返回 True，奇数返回 False
# 2. 写一个函数 classify(text)，接收文本，返回 {"category": "...", "text": "..."}


def is_even(n):
    if n % 2 == 0:
        return True
    else :
        return False
    
print(is_even(int(input())))

#第一个任务


def classify(text):
    if "开会" in text:
        return {
            "category":"任务",
            "text":text
        }
    elif "想到" in text:
        return {
            "category":"想法",
            "text":text
        }
print(classify(input()))