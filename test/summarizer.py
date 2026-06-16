import os
from openai import OpenAI

def summarize(text: str) -> str:
    # 1. 创建 client（连接 DeepSeek 服务器）
    client = OpenAI(
        api_key=os.environ["DEEPSEEK_API_KEY"],  # 从环境变量取密钥
        base_url="https://api.deepseek.com",      # 指向 DeepSeek 的地址
    )

    # 2. 发送消息，拿到回复
    response = client.chat.completions.create(
        model="deepseek-chat",
        max_tokens=1000,
        messages=[
            {"role": "system", "content": "你是总结助手，把用户输入总结成一句话。"},
            {"role": "user", "content": text},
        ],
    )

    # 3. 取出回复内容，返回
    return response.choices[0].message.content


if __name__ == "__main__":
    result = summarize("人工智能正在改变世界。")
    print(result)
