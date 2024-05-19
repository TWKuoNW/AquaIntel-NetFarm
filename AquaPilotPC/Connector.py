import socket
import threading
import time

class Connector(threading.Thread): # 建立一個連接器的class
    def __init__(self, host, port):  # 初始化Thread的設定，接收兩個參數(ip, port)
        super().__init__() # 調用父類別(Thread)的建構函式
        self.host = host 
        self.port = port 
        # 創建一個socket物件，其中 socket.AF_INET 代表使用 IPv4 地址族；SOCK_STREAM 則代表使用 TCP 傳輸，若想使用 UDP 則宣告成 SOCK_DGRAM。
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.settimeout(10) # 判定十秒為超時連線
        self.client_socket.connect((host, port)) # 連接伺服器
        self._stop_event = threading.Event() # 創建一個事件，用於執行續的同步
        self.temp = 0.0 # 初始化溫度參數
        self.hum = 0.0 # 初始化濕度參數
        self.water_temp = 0.0 # 初始化水溫參數
        self.DO = 0.0 # 初始化溶氧參數

    def run(self): # 執行續啟動後會啟動該function
        while(not self.stopped()):  # 不斷循環直到檢查到_stop_event被設定
            try:
                data = self.client_socket.recv(1024).decode("utf-8") # 從socket接收數據
                if(data != ""): # 資料不等於空
                    first_digit = data.split(' ')[0]
                    # data = data.strip().split(' ') # 將收到的data解析，strip()去除尾部的換行，.split(' ')分割資料
                    if(first_digit == '01'): # 判斷第一個字元是否為01，若是則執行以下
                        # print(f"收到溫濕度資料: {data}")
                        self.temp = data.split(' ')[1] # 將溫度資料存入self.temp
                        self.hum = data.split(' ')[2] # 將濕度資料存入self.hum
                    elif(first_digit == '02'):
                        self.water_temp = data.split(' ')[1] # 將溫度資料存入self.temp
                        self.DO = data.split(' ')[2] # 將濕度資料存入self.hum
                        
                    elif(first_digit == '03'):
                        pass
                    """
                    self.temp = float(data[0])
                    self.hum = float(data[1])
                    """

                elif(data == "EXIT"):
                    print("收到退出信號......")
                    self.send_exit_signal(self.client_socket) # 發送退出socket訊息
                    self.stop() # 停止執行續
                    print("退出執行續")
            except socket.error as e: # 發生錯誤執行以下
                print(f"Socket error: {e}") # 列印錯誤訊息
                self.send_exit_signal(self.client_socket) # 發送退出socket訊息
                self.client_socket.close() # 關閉socket
                self.stop() # 停止執行續
            time.sleep(1)

        self.client_socket.close() # 循環結束，關閉socket連線
        print("連線關閉。")

    def getTemp(self):
        return self.temp
    
    def getHum(self):
        return self.hum
    
    def getWaterTemp(self):
        return self.water_temp
    
    def getDO(self):    
        return self.DO
        
    def stop(self):
        self._stop_event.set() # 建立_stop_event標示為True，用於通知執行續的停止

    def stopped(self): # 這個function會回傳boolean型態，若有設置停止就會回傳True，反之為False
        return self._stop_event.is_set() # 檢查_stop_event標誌，如果設置了就返回True

    def send_exit_signal(self, socket): # 用於發送退出通知
        exit_signal = "EXIT" 
        socket.sendall(exit_signal.encode('utf-8'))
    
    def send_PS_command(self, command):
        if(command == 0):
            # print("close")
            command = "ps0"
            self.client_socket.sendall(command.encode('utf-8'))
        elif(command == 1):
            # print("open")
            command = "ps1"
            self.client_socket.sendall(command.encode('utf-8'))
        else:
            pass 

    def send_AF_command(self, command):
        if(command == 0):
            # print("close")
            command = "af0"
            self.client_socket.sendall(command.encode('utf-8'))
        elif(command == 1):
            # print("open")
            command = "af1"
            self.client_socket.sendall(command.encode('utf-8'))
        else:
            pass

    def send_command(self, command):
        self.client_socket.sendall(command.encode('utf-8'))

# 使用示例
if __name__ == "__main__":
    host = "192.168.0.100"
    port = 9999
    connector = Connector(host, port)
    connector.start()

    time.sleep(5)
    connector.stop()
