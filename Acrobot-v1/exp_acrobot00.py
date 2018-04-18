import numpy as np
import acrobot00 as ab

experiments = [
    np.random.rand(6) * 2 - 1
    for i in range(500)
]

ab.init(200,10)
ab.run(experiments)