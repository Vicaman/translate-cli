# translate.py
import os
import argparse
from openai import OpenAI
def translate(text: str, target_lang: str = "英文") -> str:
    # 1. 创建 client
    client = OpenAI(
        api_key=os.environ["DEEPSEEK_API_KEY"],
        base_url="https://api.deepseek.com"
    )
    # 2. 调用翻译接口
    response = client.chat.completions.create(
        model="deepseek-chat",
        max_tokens=1000,
    messages=[
    {"role": "system", "content": f"你是翻译助手，把用户输入翻译成{target_lang}，只输出翻译结果，不要解释。"},
    {"role": "user", "content": text},  # 用传进来的参数，不要写死
]    )
    # 3.获取翻译结果
    return response.choices[0].message.content


def main():
    
    # 1. 创建解析器
    
    parser = argparse.ArgumentParser(description="命令行翻译工具")
    parser.add_argument("-i", "--input", help="输入文件路径")
    parser.add_argument("-o", "--output", help="输出文件路径")
    
    # 2. 声明 text 位置参数（不加 --，所以是位置参数）
    
    parser.add_argument("text", nargs="?", default="", help="要翻译的文本")
    
    # 3. 声明 --to 可选参数（加 --，有默认值）
    
    parser.add_argument("--to", default="英文", help="目标语言")       # ← 填参数名和默认值

    # 4. 解析
    
    args = parser.parse_args()

    # 5. 读取输入内容
   
    if args.input:
        # 从文件读取
        with open(args.input, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        # 直接从命令行输入
        content = args.text
    
    # 6. 调用翻译
    result = translate(content, args.to)

      # 7. 输出：有 -o 写文件，没有就打印
    if  args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"已保存到 {args.output}")
    else:
        print(result)

if __name__ == "__main__":                    # ← 补上入口
    main()
