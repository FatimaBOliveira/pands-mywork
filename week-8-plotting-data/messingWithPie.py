# Messing with Pie Charts
# Author: Fatima Oliveira

import numpy as np
import matplotlib.pyplot as plt

fruit = np.array(["apples", "orange", "bananas"])
numbers = np.array([3, 6, 12])

plt.pie(numbers, labels = fruit)
plt.legend()
plt.show()