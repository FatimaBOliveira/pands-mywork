# Test While
# Program that reads while
# Author: Fatima Oliveira

# Counter controlled loops
count = 0
while (count < 10): # will count from first number
    print("count is ", count)
    count = count + 1 #if this is not enter, it will go on infinite loop

print("at the end count is ", count)

count = 10
while (count >=0): # will do countdown
    print("countdown ", count)
    count -= 1
print("blast off")

# Sentinal controlled loops

val = input("type something (q to quit): ")
while val != "q":
    print("hi mom")
    val = input("q to quit: ")
print("all done")