import numpy as np
import time

x = np.arange(10000)
np.save('data/1', x)
np.save('data/2', x)
np.save('data/3', x)
time.sleep(600)