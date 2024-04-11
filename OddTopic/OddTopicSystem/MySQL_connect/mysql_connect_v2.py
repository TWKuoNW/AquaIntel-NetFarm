import mysql.connector
import keyboard
import time as t
from mysql.connector import Error
from datetime import datetime
import serial
import threading
import keyboard

def create_connection(host, port, user, password, database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            port = port,
            user = user,
            password = password,
            database = database
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def write_to_mysql(connection, data):
    try:
        cursor = connection.cursor()
        insert_command = "INSERT INTO data (time, temperature, humidity) VALUES ( %s, %s, %s)"
        cursor.execute(insert_command, (data['time'], data['temperature'], data['humidity']))
        connection.commit()
        print("inserted successfully")

    except Error as e:
        print(f"Error: {e}")

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
    # MySQL information
    host = "localhost"
    user = "root"
    port = "3306"
    password = "12345678"
    database = "sensordata"
    connection = create_connection(host, port, user, password, database)
    ser = serial.Serial('COM4', baudrate=9600) # define COM PORT and baudrate

    # execute program
    if connection:
        try:
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

                temperature = temperature / 10
                humidity = humidity / 10

                print("溫度:", temperature, " 濕度:", humidity)
                # ============= Conversion and translate =============

                time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                data = {"time":time, "temperature":temperature, "humidity":humidity}
                write_to_mysql(connection, data)
                t.sleep(1)
                        
            # search data table
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM data")
            result = cursor.fetchall()
            
            # print result
            for row in result:
                print(row)

        except Error as e:
            print(f"Error: {e}")

        finally:
            #  connection close
            cursor.close()
            connection.close()
            print("Connection to MySQL database closed")    

main_thread = threading.Thread(target = main)  # define thread
main_thread.start() # thread start
boolean = True

while(boolean):
    if keyboard.is_pressed('q'):
        print("Exiting the program.")
        boolean = False

