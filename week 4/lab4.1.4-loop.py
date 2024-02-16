# Loop
# Program that promotes the user to use -1 number
# Author: Fatima Oliveira

a = -1
b = int(input("enter a number: "))
print(a == b)
if not isinstance(a, int):
    print("please give me an int")
if a < b:
   print("a is lower than b")
elif a > b:
    print("a is not higher than b")
else:
   print("a is -1.")