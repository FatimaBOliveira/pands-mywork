# Count 2
# Program that 
# Author: Fatima Oliveira

import os.path
FILENAME = "count2.txt"
if not os.path.isfile(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end="")
else:
    print (FILENAME, "File does not exist") #initialise file here

def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        # this file will be created when we write back.
        # no file assumes first time running 
        # ie 0 previous runs
        return 0

'''
def writeNumber(number):
    with open(FILENAME, "w") as f:
        # write takes a string so we need to convert
        f.write(str(number)) 

# main
num = readNumber()
num += 1
print ("we have run this program {} times".format(num))
writeNumber(num)
'''