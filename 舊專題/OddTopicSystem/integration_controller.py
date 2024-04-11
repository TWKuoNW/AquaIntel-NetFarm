from sensor_data_fetcher import SensorDataFetch
from fish_environment_controller import FishEnvironmentController

sensor_fetcher = SensorDataFetch()
#print(sensor_fetcher.get_sensor_data())

fish_environment = FishEnvironmentController()
#print(fish_environment.get_environment_parameters())