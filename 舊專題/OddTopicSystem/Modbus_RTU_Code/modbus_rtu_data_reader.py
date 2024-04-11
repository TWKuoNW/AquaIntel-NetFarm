import serial
import time
import threading
import keyboard

def modbusCRC(msg : str) -> int: # CRC calculator
    crc = 0xFFFF
    for n in range(len(msg)):
        crc ^= msg[n]
        for i in range(8):
            if(crc & 1):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

def main():
    ser = serial.Serial('COM3', baudrate=9600)
    while(boolean):   
        origin_send = b'\x01\x04\x00\x01\x00\x02' # request 
        
        list_send = ' '.join([format(byte, '02X') for byte in origin_send]) # command to string
        list_send = list_send.split() # parse to list
        
        str_send = ""
        
        for i in range(len(list_send)):
            str_send = str_send + list_send[i]
        bytes_send = bytes.fromhex(str_send)

        crc = modbusCRC(bytes_send)
        ba = crc.to_bytes(2, byteorder='little')
        str_send = str_send + str('{:02X}'.format(ba[0]))
        str_send = str_send + str('{:02X}'.format(ba[1]))
        bytes_send = str_send.encode()
        
        # ================= calc length ================= 
        outputLenHex = list_send[4] + list_send[5] 
        outputLenDex = int(outputLenHex, 16)  
        outputLen = outputLenDex * 2 + 5
        bytes_send = bytes.fromhex(bytes_send.decode('utf-8'))
        
        ser.write(bytes_send) # send command
        getData = ser.read(outputLen) # read response
        # ================= calc length ================= 
        
        data = ' '.join([format(byte, '02X') for byte in getData]) # response to string
        data = data.split() # parse list
        
        # ============= Conversion and translate =============
        value1 = data[3] + data[4]
        value2 = data[5] + data[6]
        temperature = int(value1, 16) # to DEX
        humidity = int(value2, 16) 

        print("溫度:",temperature / 10 ," 濕度:", humidity / 10)
        # ============= Conversion and translate =============
        time.sleep(1)

main_thread = threading.Thread(target = main)  # define thread
main_thread.start()
boolean = True

while(boolean):
    if keyboard.is_pressed('q'):
        print("Exiting the program.")
        boolean = False


