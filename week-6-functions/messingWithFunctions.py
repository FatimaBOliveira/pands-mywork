# Messing with functions
# Defining and using functions
# Author: Fatima Oliveira

x, y, z = (1, 2, 3)
print(x, y, z)
#print(f"{x} {y} {z}") # will do the same as above
#print(x, y, z, sep="") # will print the values and will have "" in the middle of them
print(x, y, z, sep="", end="\n") # end= will print something in the end of showing the values 

def cube(number, power = 3): # can use topower instead of cube, will work the same
    #print(number)
    return (number ** power) # return (number ** 3), same as defined

cube(23)
cube(32)
ans = cube(23) # This and the print below are needed to get the return above
print(f"we got {ans}") 
ans2 = cube(32)
print(f"we got {ans2}")
#print(f"and 32 is {cube(32)}") # will do the same as above

num = 45
print(f"and {num} is {cube(num)}")
print(f"and {num} is {cube(num, 2)}") # the 2 will be now the power instead of 3 as mentioned above.