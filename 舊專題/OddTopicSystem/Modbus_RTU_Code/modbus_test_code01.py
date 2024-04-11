import serial
import time

ser = serial.Serial('COM3', baudrate=9600)
send = b'\x01\x04\x00\x01\x00\x02\x20\x0B'
list_send = ' '.join([format(byte, '02X') for byte in send]) # 發送命令轉字串
list_send = list_send.split() # 剖析成list
while(True):
    print("請求:")
    print(list_send)
    ser.write(send) # 發送
    #============================================
    length = list_send[4] + list_send[5] 
    length = int(length, 16)  
    length = length * 2 + 5
    getData = ser.read(length) # 接收回應
    #============================================
    list_data = ' '.join([format(byte, '02X') for byte in getData]) # 發送命令轉字串
    list_data = list_data.split() # 剖析成list
    print("回應:")
    print(list_data)
    print("============================================================")
    time.sleep(1)
    