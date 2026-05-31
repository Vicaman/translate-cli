# translate-cli

命令行翻译工具，基于 DeepSeek API。

## 安装

```bash
pip install openai
```

## 配置

设置 DeepSeek API Key：

```bash
# Linux / macOS
export DEEPSEEK_API_KEY=sk-your-key-here

# Windows PowerShell
$env:DEEPSEEK_API_KEY="sk-your-key-here"
```

## 使用

```bash
# 直接翻译
python translate.py "hello world" --to 中文
python translate.py "你好世界" --to 英文

# 文件翻译
python translate.py -i input.txt -o output.txt --to 日文
```
