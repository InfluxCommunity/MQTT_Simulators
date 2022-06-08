


from random import  randint, uniform






construction_vehicle_counter = 1




class construction_vehicle():
    def __init__ (self, name) -> None:
        global construction_vehicle_counter
         
        self.construction_vehicle_ID = str(name)+ "_" + str(construction_vehicle_counter)
        construction_vehicle_counter+=1
        self.temperature = 0
        self.speed = 0
        self.vibration= 0

    def returnConstructionVehicleID(self):
        return self.construction_vehicle_ID

   
    def returnTemperature(self):
        self.temperature = round(uniform(20, 30), 2)
        return self.temperature

    def returnSpeed(self):
        # TODO dont randomise    
        self.speed = randint(0, 30)
        return self.speed
       

    def returnVibration(self):
        self.vibration = uniform(0, 2)
        return self.vibration
        
        
    
        





