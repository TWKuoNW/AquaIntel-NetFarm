from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QTimer
from PySide2.QtGui import QImage, QPixmap, QIcon
from PySide2 import QtCore
from Connector import Connector

import cv2

class Stats:
    def __init__(self):
        self.ui = QUiLoader().load("AquaPilotPC/ui/AquaPlayerUI.ui")    
        self.isCapturing = False
        self.connector = None
        # self.cap = cv2.VideoCapture(0)
        
        self.ui.btnStrVideo0.clicked.connect(self.toggleCamera) 
        self.ui.btnConn.clicked.connect(self.connMod)
        self.ui.btnClear.clicked.connect(self.clearFunc)
        self.ui.btnSend.clicked.connect(self.sendCommand)
        
        self.ui.cbProbioticSprayer.stateChanged.connect(self.probioticSprayer)
        self.ui.cbAutoFeeder.stateChanged.connect(self.autoFeeder)

        self.video0 = QTimer(self.ui)
        self.video0.timeout.connect(self.updateFrame)

        self.ui.pteComm.setPlainText("-------------------------命令視窗-------------------------")

    def updateSensorValue(self):
        temp = self.connector.getTemp()  
        hum = self.connector.getHum()
        self.ui.labTempValue.setText(str(temp))
        self.ui.labHumValue.setText(str(hum))

    def updateFrame(self):
        ret, frame = self.cap.read()  
        if ret:
            rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgbImage.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
            
            quality = self.ui.cbxQuality.currentText()
            if(quality == "1920*1080"):
                w = 1920
                h = 1080
            elif(quality == "1280*1024"):
                w = 1280
                h = 1024
            elif(quality == "640*480"):
                w = 640
                h = 480
            elif(quality == "320*240"):
                w = 320
                h = 240
            
            p = convertToQtFormat.scaled(w, h, aspectRatioMode=QtCore.Qt.KeepAspectRatio)
            self.ui.labVideo0.setPixmap(QPixmap.fromImage(p))
    
    def toggleCamera(self):
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
        
    def connMod(self):
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
            self.connector.start()
            self.ui.labStatus.setText("已連接")
            self.ui.pteComm.appendPlainText("成功連接伺服器")
            self.update_sensorvalue = QTimer(self.ui)
            self.update_sensorvalue.timeout.connect(self.updateSensorValue)
            self.update_sensorvalue.start(1000)
        except ConnectionRefusedError:
            self.ui.pteComm.appendPlainText("無法連線，因為目標電腦拒絕連線")
        except OSError:
            self.ui.pteComm.appendPlainText("內容中所要求的位址不正確。")
        except Exception as e:
            self.ui.pteComm.appendPlainText(f"發生異常: {e}")
        
    def autoFeeder(self):
        try:
            if self.ui.cbAutoFeeder.isChecked():
                self.ui.pteComm.appendPlainText("啟動自動餵食器")
                self.connector.send_AF_command(1)
                # print('啟動自動餵食器')
            else:
                self.ui.pteComm.appendPlainText("關閉自動餵食器")
                self.connector.send_AF_command(0)
                # print('關閉自動餵食器')
        except AttributeError:
            self.ui.pteComm.appendPlainText("尚未開啟連線")

    def probioticSprayer(self):
        try:
            if self.ui.cbProbioticSprayer.isChecked():
                self.ui.pteComm.appendPlainText("啟動益生菌噴灑器")
                self.connector.send_PS_command(1)
                # print('啟動益生菌噴灑器')
            else:
                self.ui.pteComm.appendPlainText("關閉益生菌噴灑器")
                self.connector.send_PS_command(0)
                # print('關閉益生菌噴灑器')
        except AttributeError:
            self.ui.pteComm.appendPlainText("尚未開啟連線")
    
    def sendCommand(self):
        self.connector.send_command(self.ui.lineEditSend.text())
        printSendCommand = "向伺服器發送->" + self.ui.lineEditSend.text()
        self.ui.pteComm.appendPlainText(printSendCommand)        
        self.ui.lineEditSend.clear()

    def clearFunc(self):
        self.ui.pteComm.clear()

app = QApplication([])
app.setWindowIcon(QIcon("AquaPilotPC/img/logo3.png"))

stats = Stats()
stats.ui.show()
app.exec_()