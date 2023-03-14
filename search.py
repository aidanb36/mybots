import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

# for x in range(5):
# 	os.system("python generate.py")
# 	os.system("python simulate.py")
# hc = HILL_CLIMBER()
# hc.Evolve()
# hc.Show_Best()
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()