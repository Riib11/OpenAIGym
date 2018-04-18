import numpy as np
import acrobot01 as ab

ab.init(STEPS=200, EPISODES=50, INC=0.2)
ab.run(np.array([-0.53262216,  0.61162884,  0.36063877,  0.77654563, -0.37914832,  0.95478668]))