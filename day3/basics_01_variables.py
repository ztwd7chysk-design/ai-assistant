'''
Python 基础 01:变量与数据类型
'''


#====1. 变量：给数据贴个标签=====
name = "yhy"         #字符串 str
age = 18             #整数 int
height = 178         #浮点数 float
is_student = True    #布尔值 bool

print(name,age,height, is_student)



#====2. type():查看数据类型=====
print(type(name))   #<class 'str'>
print(type(age))    #<class 'int'>
print(type(height)) #<class 'float'>
print(type(is_student)) #<class 'bool'>

#查看数据类型输出结果为<class 'xxx'>，其中xxx为数据类型名称

#====3.字符串操作 =====
greeting = "你好，" + name      #拼接
print(greeting)

print(f"我叫{name},今年{age}岁") #f-string格式化输出

#字符串方法
text = ' Hello World '
print(text.strip())    #去空格
print(text.lower())    #全小写
print(text.upper())    #全大写
print("World" in text) #判断是否包含-> True


# ===== 动手练习 =====
# 1. 创建 3 个变量：你的城市、你的爱好、今天的心情
# 2. 用 f-string 打印一句话，把这三个变量嵌进去
# 3. 用 type() 查看每个变量的类型


city = "厦门"
hobby = "打篮球"
mood = "not bad"

print(f"我现在在{city}，我喜欢{hobby}，我今天心情{mood}")
print(type(city),type(hobby),type(mood)) #应该全是string类型