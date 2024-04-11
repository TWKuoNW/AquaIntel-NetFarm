import requests
import time
import keyboard
from bs4 import BeautifulSoup

list = ["酸鹼度", "溶解氧", "鹽度", "濁度", "氨氮" ,"電導率" ,"資料更新時間"]
url = "http://210.61.164.188:8080/tv"

while(True):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.find_all("text", class_ = [ "st6 st7 st8" , "st9 st7 st10" ])
    j = 0
    for i in data:
        print(list[j] + ":\t" + i.get_text(strip = True))
        j = j + 1

    time.sleep(5)
    print()
    if keyboard.is_pressed('q'):
        break
    