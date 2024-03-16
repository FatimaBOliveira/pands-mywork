# Messing with Histograms
# Author: Fatima Oliveira

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1) # this will make the hist representation always the same because seed is know
normdata = np.random.normal(size=100)
plt.hist(normdata)
plt.show()