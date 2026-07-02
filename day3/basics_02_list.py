'''
Python 基础02:列表
'''


#==== 1 .创建列表 ====
todos = ["学pyhton","试着完成一些项目","提交git","晚上健身"]
print(todos)
print(f"共{len(todos)}件事情")  #len()函数可以获得列表的长度
#我感觉有一点像数组，数组是C语言的概念，列表是python的概念
# 列表可以存储不同类型的数据，而数组只能存储同一类型的数据

#==== 2.索引：从0 开始 ====
print(todos[0])  #学python
print(todos[1])  #试着完成一些项目
print(todos[-1]) #晚上健身 负数索引从后往前，列表结构类似环
 
#==== 3.修改追加删除 ====

todos[1] = "和claude一起完成项目"
todos.append("晚上补至周四的任务")   #在末尾追加
todos.remove("提交git")   #删除指定元素
print(todos)

#==== 4.切片 ====
print(todos[0:2])  #左闭右开，索引0，1元素
print(todos[1:])   #索引1到末尾(从第二个元素到最后一个元素)



# ===== 动手练习 =====
# 1. 创建一个列表，包含你喜欢的 5 首歌
# 2. 打印第1首和最后1首
# 3. 追加一首新歌
# 4. 删除最不喜欢的那首
favourite_songs = ["我怀念的","phone kisses","can we kiss forever","call silence","i love you"]
print(favourite_songs[0],favourite_songs[-1])
favourite_songs.append("暮秋沉眠")
favourite_songs.remove("i love you")
print(f"我最喜欢的五首歌曲是:{favourite_songs}")
