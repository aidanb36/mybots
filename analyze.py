import numpy
import matplotlib.pyplot as plt

backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')
backLegJointValues = numpy.load("data/backLegJointValues.npy")
frontLegJointValues = numpy.load("data/frontLegJointValues.npy")

# matplotlib.pyplot.plot(backLegSensorValues, linewidth = 4, label="Back Leg")
# matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")

plt.plot(backLegJointValues, linewidth=2, label='BackLeg')
plt.plot(frontLegJointValues, linewidth=2, label='FrontLeg')

plt.legend()
plt.show()
#add a gitignore file that contains the "data" folder