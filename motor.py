import numpy
import pyrosim.pyrosim as pyrosim
import pybullet as p
import constants as c


class MOTOR:
    def Set_Values(self, robot, desiredAngle):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot,
                                    jointName=self.jointName,
                                    controlMode=p.POSITION_CONTROL,
                                    targetPosition=desiredAngle,
                                    maxForce=c.MAX_FORCE)

    def __init__(self, jointName):
        self.jointName = jointName

        # Initialize variables for sin curve of motor values
        self.offset = 0
        self.frequency = 0
        self.amplitude = 0
        self.motorValues = numpy.zeros(c.SIMULATION_STEPS)