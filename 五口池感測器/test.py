from pywinauto import Application
import time

path = r"C:\xampp\xampp-control.exe"
app = Application(backend='uia').start(path)
time.sleep(1)

# 印出應用程序窗口的控制項標識
app.print_control_identifiers()

# 選擇特定標題的窗口進行連接
app = app.connect(title="XAMPP Control Panel v3.3.0   [ Compiled: Apr 6th 2021 ]")
print(app.window())
