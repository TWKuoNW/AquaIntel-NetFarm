from flask import Flask,request  #引入flask套件

app = Flask(__name__) #初始化flask服務

@app.route('/', methods=['POST']) #導向根目錄時跑下面函式，方法為"POST"
def home():
    if request.method == "GET": #當要求的方法為"GET"時，回傳網址中的"var1"變數
        return request.args['var1']

if __name__ == "__main__":
    app.run()  #將服務跑起來