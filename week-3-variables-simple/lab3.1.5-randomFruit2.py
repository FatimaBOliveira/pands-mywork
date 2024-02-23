# Random fruit
# This program prints random fruits
# Author: Fatima

import random

fruits = ("Apple", "Orange", "Banana", "Pear")

# We want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits [index]
print("A random fruit: {}".format(fruit))