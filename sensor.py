import numpy as np
import pyrosim.pyrosim as pyrosim
import robot

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(1000)



    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)


    def Save_Values(self):
        np.save('data/SensorValues.npy', self.values)
