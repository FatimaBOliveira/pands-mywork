# Messing wiht numpy
# Author: Fatima Oliveira

import numpy as np

list_of_numbers = [1,2,3,4,5, "asdfg"]
print(list_of_numbers)

numbers = np.array([1,2,3,4,5,6])
print(numbers)

numbers2 = np.array([1,2,3,4,5, "asdfg"]) # the "asdfg" will turn the other results as str as well, but the code above is treated as int because there's only numbers.
print(numbers2)

numbers = numbers + 3 # will add 3 to every element, can't do same with the list represented above
print(numbers)

numbers = numbers *[1,2,3,4,5,6] # will multiply each element by the number presented in this sequence.
print (numbers)

rando = np.random.randint(100,200,10) # This will give 10 random numbers between 100 and 200
print(rando)
# https://www.w3schools.com/python/numpy/numpy_random_normal.asp
normalrando = np.random.normal(loc=50, scale = 20, size=10) # This will give 10 random numbers around the mean of 50, deviation of 20.
print(normalrando)