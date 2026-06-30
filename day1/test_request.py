'''
测试 requests 库
功能:调用公开api,获取猫咪冷知识
日期:2026-06-30
'''
import requests

#1.发送请求
url = "https://catfact.ninja/fact"
response = requests.get(url)

#2.查看状态码（200表示成功)
print(f"状态码:{response.status_code}")

#3.解析返回的json

data = response.json()
print(f"猫咪冷知识：{data['fact']}")


#4.查看完整响应（调试用，可以注释掉）
#print(f"完整响应：{data}")