import json
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import *

app = Flask(__name__)
@app.route("/", methods=['POST'])
def get_reply():
    try:
        api = LineBotApi('y5Qz/t831clWTAkbV48lHbnT2x0QkU7oP8i8yqcdK6CjF4aePyHkEq58z3OGLhiwg/U4uHSRrMANFRR7El9CwWTV/YauW6cCawB58pHEdEavlxs5Eplh35l8ho4EQG928vaNfcp9YJNVIczfDg4HhwdB04t89/1O/w1cDnyilFU=') #本篇暫時不會用到，但後續會用到
        handler = WebhookHandler('9489aa16c1ed0e9debda3b59a4f7ff0e')
        body = request.get_data(as_text=True)
        json_data = json.loads(body)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        user_id = json_data['events'][0]["source"]['userId']
        text = json_data['events'][0]['message']['text']
        print(user_id, text)
        
        api.push_message(user_id, TextSendMessage(text="曹家森你好"))
        api.push_message(user_id, StickerSendMessage(package_id=1070, sticker_id=17842))
    except Exception as e:
        print(e)
	
    return 'OK'

if __name__ == "__main__":
    app.run()
    