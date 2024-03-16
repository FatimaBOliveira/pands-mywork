# Function
# Program to show y=x^2
# Author: Fatima Oliveira

import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself
plt.plot(xpoints, ypoints)
plt.show()