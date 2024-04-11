import mysql.connector
import keyboard
import time as t
from mysql.connector import Error
from datetime import datetime


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

# MySQL information
host = "localhost"
user = "root"
port = "3306"
password = "12345678"
database = "sensordata"

connection = create_connection(host, port, user, password, database)

# execute program
if connection:
    try:
        while(True):
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = {"time":time, "temperature":22, "humidity":60}
            write_to_mysql(connection, data)
            
            t.sleep(1)
            
            if keyboard.is_pressed('q'):
                break
                       
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
