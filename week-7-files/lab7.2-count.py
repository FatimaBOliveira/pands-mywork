# Count
# Program that will count how many times program was run.
# Author: Fatima Oliveira

FILENAME = "count.txt"
def readNumber():
   with open(FILENAME) as f:
     number = int(f.read())
     return number
# test it
num = readNumber()
print (num)

def writeNumber(number):
   with open(FILENAME, "w") as f: # write takes a string so we need to convert
     f.write(str(number))
# test it
writeNumber(9)

# main
num += 1
writeNumber(num) 
print (f"we have run this program {num} times")
#print ("we have run this program {} times".format(num)) # work same as above