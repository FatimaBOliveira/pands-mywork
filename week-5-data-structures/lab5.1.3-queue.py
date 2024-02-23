# Queue
# Program that puts 10 random numbers into a queue, then select, print and show the remaining numbers that weren't pick up, 
#   that are still in queue.
# Author: Fatima Oliveira

import random
queue = []
numberOfNumbers=10
rangeTo=100

for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))
print (f"queue is {queue}")
while len(queue) != 0:
   currentNumber = queue.pop(0)
   print (f"current Number is {currentNumber} and the queue is {queue}")
print ("the queue is now empty")