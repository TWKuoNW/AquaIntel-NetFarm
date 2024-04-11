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
    ba = crc.to_bytes(2, byteorder='little')
    return ba

def main():
    ser = serial.Serial('COM3', baudrate=9600) # define COM PORT and baudrate
    while(boolean):   
        origin_send = ["01","04","00","01","00","02"] # request command
        bytes_send = bytes([int(x, 16) for x in origin_send]) # list to bytes

        crc = modbusCRC(bytes_send) # CRC calculator function
        origin_send.append(str('{:02X}'.format(crc[0]))) # append crc LO 
        origin_send.append(str('{:02X}'.format(crc[1]))) # append crc HI     
        
        # ==================== calc length ==================== 
        length = origin_send[4] + origin_send[5] 
        length = int(length , 16)  
        length = length * 2 + 5
        
        bytes_send = bytes([int(x, 16) for x in origin_send])
        # ==================== calc length ==================== 

        ser.write(bytes_send) # send command
        data = ser.read(length) # read response
        
        # ============= Conversion and translate =============
        data = [format(x, '02x') for x in data]
        value1 = data[3] + data[4]
        value2 = data[5] + data[6]
        temperature = int(value1, 16) # HEX to DEX
        humidity = int(value2, 16) 

        print("溫度:",temperature / 10 ," 濕度:", humidity / 10)
        # ============= Conversion and translate =============
        time.sleep(1)

main_thread = threading.Thread(target = main)  # define thread
main_thread.start() # thread start
boolean = True

while(boolean):
    if keyboard.is_pressed('q'):
        print("Exiting the program.")
        boolean = False