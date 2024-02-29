# Quiz
# Author: Fatima Oliveira

# function yo takes one parameter 
def yo(a): 
    return a * 2 
# here we are calling the function yo 
# and are passing in an argument, 3 
yo(3) 

#1. Look at the program above: 
#   a. What will be printed out when this program is run?  
  #   Nothing will be printed because there's no print function in this program.
#   b. What would you have to add to the program to get it to print out what the calling the function yo(3) returns? 
  #   print(yo(3)) or as below


def yo(a, multiply=2): 
    return a * multiply
yo(3)
number = yo(3)
abc = 3
print(f"The answer of this quiz is {number}")
print(f"The answer of this quiz is {yo(abc, 3)}")