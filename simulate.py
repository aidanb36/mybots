import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(100)
frontLegSensorValues = numpy.zeros(100)

for i in range(100):
    time.sleep(1 / 60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link0")

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Link1_Link2",
        controlMode=p.POSITION_CONTROL,
        targetPosition=0.0,
        maxForce=500)

p.disconnect()
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
