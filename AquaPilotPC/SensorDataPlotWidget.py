from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from ui.SensorDataPlotUI import Ui_Form

import sys
import paramiko

class PlotSensorData(QThread):
    task_done = Signal()
    def run(self):
        try:
            file_path = "D:\智慧養殖專題\AquaIntel-NetFarm\AquaPilotPC\sensor_data.txt"
            time_list = []
            air_temperature_list = []
            air_humidity_list = []
            water_temperature_list = []
            water_DO_list = []

            with open(file_path, "r") as file:
                for line in file:
                    line = line.strip().split(", ")
                    
                    time_list.append(line[0])
                    air_temperature_list.append(line[1].split(" ")[1].split("C")[0])
                    air_humidity_list.append(line[2].split(" ")[1].split("%")[0])
                    water_temperature_list.append(line[3].split(" ")[1].split("C")[0])
                    water_DO_list.append(line[4].split(" ")[1].split("mg/L")[0])
                    

            self.plot_widget = self.args[0]
            self.plot_widget.plot(time_list, air_temperature_list)

            self.task_done.emit()

        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def set_args(self, *args):
        self.args = args

class TransferSensorData(QThread):
    task_done = Signal()
    def run(self):
        remote_path = '/home/pi/AquaPilotFarm/sensor_data.txt'  # Raspberry Pi 上的文件路徑
        local_path = 'D:/智慧養殖專題/AquaIntel-NetFarm/AquaPilotPC/sensor_data.txt'  # PC保存文件的路徑
        hostname = '100.81.241.109'  # Pi的IP地址
        port = 22  # SSH 預設 port
        username = 'pi'  # Pi 的使用者名稱
        password = '123456'  # Pi 的密碼

        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=password)
        
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(remote_path, local_path)
        sftp.close()
        transport.close()
        print('File transferred successfully.')
        self.task_done.emit()

class MyMplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MyMplCanvas, self).__init__(fig)

        self.plot()

    def plot(self, x_list = [], y_list = []):
        self.axes.clear()  # 清除原有的圖形
        self.axes.plot(x_list, y_list)

        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Air Temperature (°C)')

        self.axes.set_xticks([])
        self.axes.set_yticks([])

        self.draw()

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("感測器數據繪圖")

        # 將繪圖物件加入到視窗中
        self.plot_widget = MyMplCanvas()
        self.ui.verticalLayout_2.insertWidget(0, self.plot_widget)
        
        # 連接按鈕的點擊事件
        self.ui.pushButton.clicked.connect(self.on_push_button_clicked)
        self.ui.btnUpdate.clicked.connect(self.on_btnUpdate_clicked)
        
        # 創建傳輸資料的執行續
        self.transfer_sensor_data = TransferSensorData()
        self.transfer_sensor_data.task_done.connect(self.on_transfer_sensor_data_done) # 連接傳輸資料完成的訊號

        # 創建繪圖的執行續
        self.plot_sensor_data = PlotSensorData()
        self.plot_sensor_data.task_done.connect(self.on_plot_sensor_data_done)


    def on_btnUpdate_clicked(self):
        self.ui.btnUpdate.setText('更新中...')
        self.plot_sensor_data.set_args(self.plot_widget)
        self.plot_sensor_data.start()

    def on_plot_sensor_data_done(self):
        self.ui.btnUpdate.setText('更新完成!')

    def on_push_button_clicked(self):
        self.ui.pushButton.setText('傳輸中請稍後...')
        self.transfer_sensor_data.start() # 啟動傳輸資料的執行續

    def on_transfer_sensor_data_done(self):
        self.ui.pushButton.setText("傳輸完成!")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    sys.exit(app.exec_())