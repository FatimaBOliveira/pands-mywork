# Messing with real data and normalized random data.
# Author: Fatima Oliveira

import numpy as np
import matplotlib.pyplot as plt

numbers = np.array([5,10,50,100])
print(numbers)

rando = np.random.randint(numbers) # this will pick random numbers inside of the array of numbers
print(rando)

normalrando = np.random.normal(loc=50, scale = 10, size=10) # This will give 10 random numbers around the mean of 50, deviation of 10.
print(normalrando)


animals = ["Cat", "Dog", "Fish", "Horse"]

animalsrando = np.random.choice(animals, size=10) # will randomly pick 10 animals that can be one of the 4 above.
unique, counts = np.unique(animalsrando, return_counts=True) # will count the random numbers that we got above and will allow it to plot it as a pie, bar...
# we can now put this into a pie plot
plt.pie(counts, labels= unique)
plt.show()

plt.bar(unique, counts)
plt.show()