import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
x = 0
y = 0
z = 0.5
length = 1
width = 1
height = 1
for x in range(5):
    for y in range(5):
        z=0
        length = 1
        width = 1
        height = 1
        for z in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x, y, z+.5] , size=[length, width, height])
            length = .9*length
            width = .9*width
            height = .9*height
pyrosim.End()


