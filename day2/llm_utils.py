"""
大模型调用工具模块
封装 API 调用，方便项目复用
日期:2026-06-30
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# 加载环境变量
load_dotenv()

# 初始化客户端（只执行一次）
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def first_call_llm(prompt, system_prompt="你是一个有用的助手", temperature=0.7, max_tokens=500):
    """
    通用的大模型调用函数
    
    参数:
        prompt (str): 用户输入的提示词
        system_prompt (str): 系统提示词，定义 AI 的角色
        temperature (float): 0.0~1.5,越高越随机
        max_tokens (int): 最大返回长度
    
    返回:
        str: AI 的文本回复
    """
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[错误] API 调用失败: {e}"