import json
import requests

OPENAI_API_KEY = "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"  # 替換成你自己的Key

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}


body = {
    "model": "gpt-4",
    "messages": [
        {
            "role": "system",
            "content": "你是一個能提供 Python 程式指南的助理。"},
        {
            "role": "user",
            "content": "我如何在 python 中創建一個字典?"},
    ]
}


url = "https://api.openai.com/v1/chat/completions"

res = requests.post(url, headers=headers, json=body)
resDict = json.loads(res.text)

for mes in resDict['choices']:
    print(type(mes['message']['content']))