import numpy as np
import cartpole01 as cp

experiments = [
    np.random.rand(4) * 2 - 1
    for i in range(100)
]

# experiments = [[-0.44341505,  0.7920864,  -0.21603695,  0.72950489]]

cp.init(200,100)
cp.run(experiments)