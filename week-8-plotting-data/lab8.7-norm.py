# Normalise salaries
# Author: Fatima Oliveira

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100
np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
ages = np.random.randint(low=21, high=65, size=numberOfEntries)
sns.lineplot(x=ages,y=salaries) # https://www.kaggle.com/code/berkayalan/seaborn-a-complete-data-visualization-guide
plt.title("random plot")
plt.xlabel("ages")
plt.ylabel("salaries")
plt.legend()
plt.show()