# Types
# Testing 3 functions on a value: integer, floating-point number and string
# Author: Fatima

a = 89
print(int(a))
print(float(a))
print(str(a))

b = 3.3
print(int(b))
print(float(b))
print(str(b))

c = "egg"
#print(int(c))   Doesn't work
#print(float(c)) Doesn't work
print(str(c))

print ("variable {} is of the type: {} and value: {}".format("a", type(a), a))
print ("variable {} is of the type: {} and value: {}".format("b", type(b), b))
print ("variable {} is of the type: {} and value: {}".format("c", type(c), c))