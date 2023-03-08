import numpy
import math

# Environment
SIMULATION_STEPS = 400
# GRAVITY = -15
GRAVITY = -9.8
SLEEP_INCREMENT = 1 / 60

# Joints

MAX_FORCE = 50

# Movements
BACK_AMPLITUDE = math.pi / 4.0
BACK_FREQUENCY = 10
BACK_PHASE_OFFSET = 0
FRONT_AMPLITUDE = math.pi / 4.0
FRONT_FREQUENCY = 20
FRONT_PHASE_OFFSET = numpy.pi
SIN_DIVISOR = (SIMULATION_STEPS / 20 * math.pi)
numberOfGenerations = 10
gravity_x = 0
gravity_y = 0
gravity_z = -9.8
motorMaxForce = 25
timeStepDirect = 0
timeStepGUI = 1/60
simulationSize = 1000
