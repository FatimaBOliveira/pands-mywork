# Flexible Arguments
# More messing with functions
# Author: Fatima Oliveira

# Unnamed args
def fun1(*args): # is not very comum to do this
    print(type(args))
    print(args)
    for val in args: # will print them in different lines
        print(val)

fun1("a", "b", "c")

# Keyword arguments
def fun2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for val in kwargs:
        print(val)

fun2(name="joe", age=21, gender="M")

# Sample code
def ave(*values):
    number_of_values = len(values)
    sum=0
    for value in values:
        sum += value

    average = sum/number_of_values
    return average, sum

av1, sum_of_numbers = ave(1,2,3,4,5,6) # av1 returns average and sum_of_numbers returns sum as above
print(f"{av1} and sum is {sum_of_numbers}") # av1 is average numbers of 1,2,3,4,5,6 and sum_of_numbers is the sum of same numbers.