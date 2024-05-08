from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QTimer
from PySide2.QtGui import QImage, QPixmap, QIcon
from PySide2 import QtCore
from PySide2.QtCore import Slot

from Connector import Connector
from ui.AquaPilotUI import Ui_AquaPlayer

import cv2
import threading

class QMainWindow(QMainWindow): # 覆寫QMainWindow
    def __init__(self):
        super().__init__() # 呼叫父類別的建構函式
        self.setStyleSheet("background-color: #E0E0E0;") # 設定背景顏色
        self.setWindowIcon(QIcon("AquaPilotPC/img/logo3.png")) # 設定視窗icon
        self.connector = None # 初始化connector

    def add_connector(self, connector): # 新增connector
        self.connector = connector
        
    @Slot()
    def closeEvent(self, event): # 關閉視窗事件
        if self.connector is not None: # 如果connector不是None
            self.connector.send_exit_signal(self.connector.client_socket) # 發送退出socket訊息
            self.connector.stop() # 停止執行續
        print("關閉AquaPilot") # 顯示關閉事件
        QApplication.instance().quit() # 關閉視窗

class MyApp():
    def __init__(self):
        self.app = QApplication([]) # 創建應用程式
        self.window = QMainWindow() # 創建視窗

        self.ui = Ui_AquaPlayer() # 創建UI
        self.ui.setupUi(self.window) # 設定UI

        self.isCapturing = False # 初始化isCapturing為False
        self.connector = None # 初始化connector為None
        self.cap = None # 初始化cap為None
        
        # 連接button與函數
        self.ui.btnStrVideo0.clicked.connect(self.toggleCamera) 
        self.ui.btnConn.clicked.connect(self.connMod) 
        self.ui.btnClear.clicked.connect(self.clearFunc)
        self.ui.btnSend.clicked.connect(self.sendCommand)
        
        # 連接checkbox與函數
        self.ui.cbProbioticSprayer.stateChanged.connect(self.probioticSprayer)
        self.ui.cbAutoFeeder.stateChanged.connect(self.autoFeeder)

        # 初始化video0
        self.video0 = QTimer()
        self.video0.timeout.connect(self.updateFrame)

        self.ui.pteComm.setPlainText("-------------------------命令視窗-------------------------")
    
    def run(self): # 執行應用程式，於程式啟動時執行
        self.window.show()
        self.app.exec_()

    def updateSensorValue(self): # 更新感測器數值
        temp = self.connector.getTemp()
        hum = self.connector.getHum()
        self.ui.labTempValue.setText(str(temp)) 
        self.ui.labHumValue.setText(str(hum))

    def updateFrame(self): # 更新相機畫面
        ret, frame = self.cap.read()  
        if ret:
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape # 高、寬、通道數
            bytesPerLine = ch * w # 每行的字節數
            convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888) # 轉換成QImage格式
            quality = self.ui.cbxQuality.currentText() # 取得解析度

            if(quality == "1920*1080"):
                w = 1920
                h = 1080
            elif(quality == "1280*1024"):
                w = 1152
                h = 922
            elif(quality == "640*480"):
                w = 640
                h = 480
            elif(quality == "320*240"):
                w = 320
                h = 240
            
            p = convertToQtFormat.scaled(w, h, aspectRatioMode=QtCore.Qt.KeepAspectRatio) # 保持長寬比
            self.ui.labVideo0.setPixmap(QPixmap.fromImage(p)) # 顯示畫面
    
    def toggleCamera(self): # 開啟/關閉相機
        if(not self.cap == None):
            if self.isCapturing:
                self.video0.stop()
                self.isCapturing = False
                self.ui.labVideo0.setText("video0")
                self.ui.btnStrVideo0.setText("開始")
                self.ui.pteComm.appendPlainText("相機關閉")
            else:
                self.video0.start(20)
                self.isCapturing = True
                self.ui.btnStrVideo0.setText("關閉")
                self.ui.pteComm.appendPlainText("相機開啟")
                
                quality = self.ui.cbxQuality.currentText()
                
                if(quality == "1920*1080"):
                    self.ui.pteComm.appendPlainText("相機解析度設定1920*1080")
                elif(quality == "1280*1024"):
                    self.ui.pteComm.appendPlainText("相機解析度設定1280*1024")
                elif(quality == "640*480"):
                    self.ui.pteComm.appendPlainText("相機解析度設定640*480")
                elif(quality == "320*240"):
                    self.ui.pteComm.appendPlainText("相機解析度設定320*240")
        
    def connMod(self): # 連接模式
        port = 9999
        name = self.ui.txtName.text()
        ip = self.ui.txtIP.text()

        self.ui.labName.setText(str(name))
        self.ui.labIP.setText(str(ip))
        video0_url = 'http://' + str(ip) + ':8000/video'
        # print(video0_url)
        self.cap = cv2.VideoCapture(video0_url)

        # print(name, " ", ip)
        self.ui.pteComm.appendPlainText("連接養殖場伺服器...")
        try:
            self.connector = Connector(ip, port)
            self.window.add_connector(self.connector) # 將connector加入到window
            self.connector.start()
            self.ui.labStatus.setText("已連接")
            self.ui.pteComm.appendPlainText("成功連接伺服器")
            self.update_sensorvalue = QTimer()
            self.update_sensorvalue.timeout.connect(self.updateSensorValue)
            self.update_sensorvalue.start(1000)
        except ConnectionRefusedError:
            self.ui.pteComm.appendPlainText("無法連線，因為目標電腦拒絕連線")
        except OSError:
            self.ui.pteComm.appendPlainText("內容中所要求的位址不正確。")
        except Exception as e:
            self.ui.pteComm.appendPlainText(f"發生異常: {e}")
    
    def send_autoFeeder_command_to_connector(self, command): # 向Connector發送益生菌噴灑器命令
        if(command == 0):
            self.connector.send_AF_command(0)
        elif(command == 1):
            self.connector.send_AF_command(1)

    def autoFeeder(self): # 自動餵食器
        try:
            if self.ui.cbAutoFeeder.isChecked():
                self.ui.pteComm.appendPlainText("啟動自動餵食器")
                this_thread = threading.Thread(target=self.send_autoFeeder_command_to_connector, daemon = True, args=(1,))
                this_thread.start()
                
                # self.connector.send_AF_command(1)
                # print('啟動自動餵食器')
            else:
                self.ui.pteComm.appendPlainText("關閉自動餵食器")
                this_thread = threading.Thread(target=self.send_autoFeeder_command_to_connector, daemon = True, args=(0,))
                this_thread.start()
                # self.connector.send_AF_command(0)
                # print('關閉自動餵食器')
        except AttributeError:
            self.ui.pteComm.appendPlainText("尚未開啟連線")

    def send_probioticSprayer_command_to_connector(self, command): # 向Connector發送益生菌噴灑器命令
        if(command == 0):
            self.connector.send_PS_command(0)
        elif(command == 1):
            self.connector.send_PS_command(1)
        
    def probioticSprayer(self): # 益生菌噴灑器
        try:
            if self.ui.cbProbioticSprayer.isChecked():
                self.ui.pteComm.appendPlainText("啟動益生菌噴灑器")
                this_thread = threading.Thread(target=self.send_probioticSprayer_command_to_connector, daemon = True, args=(1,))
                this_thread.start()
                
                # self.send_probioticSprayer_command_to_connector(1)
                # print('啟動益生菌噴灑器')
            else:
                self.ui.pteComm.appendPlainText("關閉益生菌噴灑器")
                this_thread = threading.Thread(target=self.send_probioticSprayer_command_to_connector, daemon = True, args=(0,))
                this_thread.start()

                # self.send_probioticSprayer_command_to_connector(0)
                # print('關閉益生菌噴灑器')
        except AttributeError:
            self.ui.pteComm.appendPlainText("尚未開啟連線")
    
    def sendCommand(self): # 發送命令
        self.connector.send_command(self.ui.lineEditSend.text())
        printSendCommand = "向伺服器發送->" + self.ui.lineEditSend.text()
        self.ui.pteComm.appendPlainText(printSendCommand)        
        self.ui.lineEditSend.clear()

    def clearFunc(self): # 清除命令視窗
        self.ui.pteComm.clear()

if __name__ == "__main__":
    my_app = MyApp()
    my_app.run()