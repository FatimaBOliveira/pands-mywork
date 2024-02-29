# Scope
# More messing with functions
# Author: Fatima Oliveira

# Don't use global variables

x = 999

#def fun(): NOT TO DO
#    print(x) NOT TO DO because x is defined outsite
#fun()

def fun(num):
    print(num)
fun(x)

def fun2(x2): # don't use same x outside and inside function because it's treated as different
    print(f"in fun2 x {x2}")
    global x # not to do, global values shouldn't be inside black box
    x = 21 # Not to do, will give 2 different values
    print(f"in funs2 c {x2}")

fun2(x)
print(f"after fun2 x is {x}")