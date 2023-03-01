import pybullet

import constants as c

import pybullet as p
import time as t
import pybullet_data
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
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

            t.sleep(c.SLEEP_INCREMENT)

        # Destructor
        def __del__():
            p.disconnect()