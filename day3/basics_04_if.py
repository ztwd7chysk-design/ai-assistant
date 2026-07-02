'''
Python 基础 04:条件判断
'''

#==== 1.基本if ====
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
    
    
#==== 2.用in判断是否包含 ====
text = input()
 
if "开会" in text:
    print("这是任务")
elif "想到" in text:
    print("这是想法")
elif "记住" in text:
    print("这是备忘")
else:
    print("其他")
    
#==== 3.组合条件 ====
has_time = True
has_action = True

if has_time and has_action:
    print("这应该是个任务")
elif has_time or has_action:
    print("这可能是个任务")
else:
    print("这可能是想法或者备忘")
    
    
# ===== 动手练习 =====
# 1. 写一个判断天气的程序：
#    - 如果温度 > 35，打印"太热了"
#    - 如果温度 20-35，打印"舒适"
#    - 如果温度 < 20，打印"有点冷"
# 2. 判断一段文本属于哪个分类（用 in 关键词）


temperature = int(input())

if temperature > 35 :
    print("太热了")
elif temperature >= 20:
    print("很舒适")
else:
    print("有点冷")
    
#这是第一个练习


text = input()

if "math" in text:
    print("这段话和数学相关")
elif "chinese" in  text:
    print("这段话和语文相关")
elif "english" in text:
    print("这段话和英语相关")
else:
    print("其他")
    
#这是第二个练习