# Division
# Program that makes division between first number and second number
# Author: Fatima

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // given the int division
remainder = x%y    # % gives the remainder

print("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))