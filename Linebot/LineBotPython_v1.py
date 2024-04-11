import json
import requests
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import *

app = Flask(__name__)
@app.route("/", methods=['POST'])
def get_reply():
    try:
        # Channel access token
        api = LineBotApi('y5Qz/t831clWTAkbV48lHbnT2x0QkU7oP8i8yqcdK6CjF4aePyHkEq58z3OGLhiwg/U4uHSRrMANFRR7El9CwWTV/YauW6cCawB58pHEdEavlxs5Eplh35l8ho4EQG928vaNfcp9YJNVIczfDg4HhwdB04t89/1O/w1cDnyilFU=')
        # Channel secret
        handler = WebhookHandler('9489aa16c1ed0e9debda3b59a4f7ff0e')     
        body = request.get_data(as_text = True)
        json_data = json.loads(body)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        user_id = json_data['events'][0]["source"]['userId']
        text = json_data['events'][0]['message']['text']

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
                    "content": "你是一個能提供文蛤養殖知識的助理。"},
                {
                    "role": "user",
                    "content": text },
            ]
        }
        url = "https://api.openai.com/v1/chat/completions"
        res = requests.post(url, headers = headers, json = body)
        resDict = json.loads(res.text)

        for mes in resDict['choices']:
           response = mes['message']['content']
        
        api.push_message(user_id, TextSendMessage(text = response))
    except Exception as e:
        print(e)
    return 'OK'

if __name__ == "__main__":
    app.run()
    