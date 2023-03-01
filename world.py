import pybullet as p

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")  # loads floor
        p.loadSDF("world.sdf")
