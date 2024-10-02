import numpy as np
import time

x = np.arange(10000)
np.save('data', x)
time.sleep(600)