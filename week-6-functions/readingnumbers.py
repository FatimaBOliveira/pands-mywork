# Reading Numbers
# Read in two numbers and multiple them
# Author: Fatima Oliveira

num1=False
while (num1 == False): #This is go on a loop if person keps typing a str instead of a int.
    try:
        num1 = int(input("Enter a number: ")) # int is essencial because if not used, it will treat the input as a str
    except ValueError: # in case of error due to str, the following message will appear
        print("No strings, please. ", end="") # The end="" will put both "No strings..." and "Enter a ..." together, otherwise in 2 lines.


num2 = False
while (num2 == False): 
    try:
        num2 = int(input("and another: ")) 
    except ValueError: 
        print("No strings, please. ", end="")

answer = num1 * num2

print(f"Answer is {answer}")

def readNum(): # This will do the same as both functions above in one 
    num = False
    while (num == False): # can also write (not num) instead of (num==Flase)
        try:
            num = int(input("Enter a number: ")) # Can also put the message inside readNum(note="..."") and in input only put note
        except ValueError: 
            print("No strings, please. ", end="")
    return num

num3 = readNum()
num4 = readNum() # can put message if also message while def readNum("...") and no message inside try, only note

answer2 = num3 * num4
print(f"Answer is {answer2}")