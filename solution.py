import numpy as np
import pyrosim.pyrosim as pyrosim
import os
import random

length = 1
width = 1
height = 1

x = 0
y = 0
z = 1 / 2
class SOLUTION:

    def __init__(self):

        self.weights = np.random.rand(3,2)
        self.weights = self.weights*2-1

    def Evaluate(self, guiOrDirect):

        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + guiOrDirect)
        fitness = open("fitness.txt", "r")
        self.fitness = float(fitness.read())
        fitness.close()

    def Mutate(self):
        randomRow = random.randint(0, len(self.weights)-1)
        randomColumn = random.randint(0, len(self.weights[0])-1)
        self.weights[randomRow, randomColumn] = random.random()*2-1

    def Create_World(self):

        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x - 5, y + 5, z], size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-.5, 0, -.5], size=[length, width, height])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5, 0, -.5], size=[length, width, height])
        pyrosim.End()

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        # Sensor Neurons
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

        # Motor Neurons
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(
                    sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

        pyrosim.End()