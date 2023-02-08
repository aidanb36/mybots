import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
from cmath import pi
import random
import math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")


p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
backLegJointValues = numpy.zeros(1000)
frontLegJointValues = numpy.zeros(1000)
amplitudeBackLeg = -math.pi/4.0
frequencyBackLeg = 1/10.0
phaseOffsetBackLeg = 5

amplitudeFrontLeg = math.pi/4.0
frequencyFrontLeg = 1/20.0
phaseOffsetFrontLeg = 0

for i in range(1000):
    time.sleep(1 / 60)
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link2")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Link0")

    backLegPosition = math.sin(frequencyBackLeg * i + phaseOffsetBackLeg) * amplitudeBackLeg
    frontLegPosition = math.sin(frequencyFrontLeg * i + phaseOffsetFrontLeg) * amplitudeFrontLeg

    backLegJointValues[i] = backLegPosition
    frontLegJointValues[i] = frontLegPosition

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Link1_Link2",
        controlMode=p.POSITION_CONTROL,
        targetPosition= backLegPosition,
        maxForce=100)

    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName="Link0_Link1",
        controlMode=p.POSITION_CONTROL,
        targetPosition= frontLegPosition,
        maxForce=100)

p.disconnect()
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
numpy.save("data/backLegJointValues", backLegJointValues)
numpy.save("data/frontLegJointValues", frontLegJointValues)