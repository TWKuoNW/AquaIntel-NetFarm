import json
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import *

class LinebotCommunicator:
    app = Flask(__name__) # 創建一個 Flask 應用
    @app.route("/", methods=['POST']) # 創建一個路徑的 POST 請求處理器
    def get_reply():
        try:
            # 初始化 LineBotApi 和 WebhookHandler
            api = LineBotApi('y5Qz/t831clWTAkbV48lHbnT2x0QkU7oP8i8yqcdK6CjF4aePyHkEq58z3OGLhiwg/U4uHSRrMANFRR7El9CwWTV/YauW6cCawB58pHEdEavlxs5Eplh35l8ho4EQG928vaNfcp9YJNVIczfDg4HhwdB04t89/1O/w1cDnyilFU=') #本篇暫時不會用到，但後續會用到
            handler = WebhookHandler('9489aa16c1ed0e9debda3b59a4f7ff0e')
            body = request.get_data(as_text=True) # 獲取 POST 請求的資料
            json_data = json.loads(body) # 解析成 JSON 格式
            signature = request.headers['X-Line-Signature'] # 取得 Line-Signature 頭部
            handler.handle(body, signature) # 使用 WebhookHandler 處理請求
            user_id = json_data['events'][0]["source"]['userId']
            text = json_data['events'][0]['message']['text']
            print(user_id, text)
            
            api.push_message(user_id, TextSendMessage(text="測試"))
            api.push_message(user_id, StickerSendMessage(package_id=1070, sticker_id=17842))
        except Exception as e:
            print(e)
        
        return 'OK'

    if __name__ == "__main__":
        app.run()
    