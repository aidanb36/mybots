import pybullet

import constants as c
import pybullet_data
import pybullet as p
import time as t
import pybullet_data
from world import WORLD
from robot import ROBOT

class SIMULATION:
    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # gets custom pybullet shapes for easier use

        p.setGravity(0, 0, c.GRAVITY)  # set gravity

        self.world = WORLD()
        self.robot = ROBOT()

    def Run(self):
        for i in range(c.SIMULATION_STEPS):
            p.stepSimulation()
            ROBOT.Sense(self.robot)
            ROBOT.Think(self.robot)
            ROBOT.Act(self.robot)
            if self.directOrGUI == "DIRECT":
                t.sleep(c.timeStepDirect)

            if self.directOrGUI == "GUI":
                t.sleep(c.timeStepGUI)
            # t.sleep(c.SLEEP_INCREMENT)

    def Get_Fitness(self):

        self.robot.Get_Fitness()
    # Destructor
    def __del__(self):
        p.disconnect()