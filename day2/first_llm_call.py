"""
第一个大模型 API 调用
日期:2026-06-30
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env 文件中的 API Key
load_dotenv()

# 初始化 DeepSeek 客户端（DeepSeek 兼容 OpenAI 库）
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),#身份证号
    base_url="https://api.deepseek.com"
)

# 发送第一条消息
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "用三句话介绍人工智能的历史"}
    ],
    max_tokens=20,#输出会被截断，这是用于控制成本
    temperature=0.0
)

# 打印 AI 的回复
print(response.choices[0].message.content)

from llm_utils import first_call_llm

# 使用封装好的函数调用大模型
result = first_call_llm("用一句话概括人工智能的历史", temperature=0.0)
print(result)

# 测试带重试的封装
result = first_call_llm("你好，请简单介绍你自己")
print(result)