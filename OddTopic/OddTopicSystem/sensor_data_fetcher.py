import requests
import time
from bs4 import BeautifulSoup

class SensorDataFetch:
    mark_list = ["酸鹼度" , "溶解氧", "鹽度" , "濁度" , "氨氮"  , "電導率" , "資料更新時間"]
    sensor_data = []
    def get_sensor_data(self):
        url = "http://210.61.164.188:8080/tv"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find_all("text", class_ = [ "st6 st7 st8" , "st9 st7 st10" ])
        for i in data:
            self.sensor_data.append(i.get_text(strip = True))
        return self.sensor_data
    
    def toString(self):
        url = "http://210.61.164.188:8080/tv"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.find_all("text", class_ = [ "st6 st7 st8" , "st9 st7 st10" ])
        j = 0
        for i in data:
            print(self.mark_list[j] + ":\t" + i.get_text(strip = True))
            j = j + 1

while(True):
    sensor_fetcher = SensorDataFetch()
    # sensor_fetcher.get_sensor_data()
    sensor_fetcher.toString()
    time.sleep(5)

    


    
    
