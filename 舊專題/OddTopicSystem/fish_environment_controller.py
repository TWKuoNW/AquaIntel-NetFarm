class FishEnvironmentController:
    max_temperature = 28 #溫度 C
    min_temperature = 24 
    
    max_ph_value = 8.4 #酸鹼度 PH
    min_ph_value = 8.0 
    
    max_dissolved_oxygen = 8 #溶解氧 mg/L
    min_dissolved_oxygen = 6 
    
    max_salinity = 25 #鹽度 PPT
    min_salinity = 20 
    
    def get_environment_parameters(self):
        parameters = [
            self.max_temperature,
            self.min_temperature,
            self.max_ph_value,
            self.min_ph_value,
            self.max_dissolved_oxygen,
            self.min_dissolved_oxygen,
            self.max_salinity,
            self.min_salinity,
        ]
        return parameters

    
     


