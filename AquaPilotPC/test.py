file_path = "D:\智慧養殖專題\AquaIntel-NetFarm\AquaPilotPC\sensor_data.txt"

try:
    time_list = []
    air_temperature_list = []
    air_humidity_list = []
    water_temperature_list = []
    water_DO_list = []

    with open(file_path, "r") as file:
        # 逐行读取文件内容
        for line in file:
            line = line.strip().split(", ")
            
            time_list.append(line[0])
            air_temperature_list.append(line[1].split(" ")[1].split("C")[0])
            air_humidity_list.append(line[2].split(" ")[1].split("%")[0])
            water_temperature_list.append(line[3].split(" ")[1].split("C")[0])
            water_DO_list.append(line[4].split(" ")[1].split("mg/L")[0])
            #print(line)
        
        print(f"Time: {air_temperature_list}")
        
        """
        print(f"Air Temperature: {air_temperature_list}")
        print(f"Air Humidity: {air_humidity_list}")
        print(f"Water Temperature: {water_temperature_list}")
        """
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
