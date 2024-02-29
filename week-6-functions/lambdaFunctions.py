# Lambda Functions
# More messing with functions
# Author: Fatima Oliveira

'''
x = lambda arg1: arg1 ** 2
answer=x(4)
print(answer)
'''
bussinesstype = "standard"
#bussinesstype = "reduced"
vatcalc = lambda amount: amount * 0.23 # Standard

if bussinesstype == "reduced":
    vatcalc = lambda amount: amount * 0.135 # Reduced

cash = 10
print(vatcalc(cash))

# Sort a list
numbers = [2,33,55,1,4]
sortednumbers = sorted(numbers)
print(f"{numbers} sorted is {sortednumbers}")

# Sort a dictionary
data = [{"first": "Guido", "last": "Van Rossum", "YOB": 1956},
        {"first": "Grace", "last": "Hopper", "YOB": 1906},
        {"first": "Alan", "last": "Turing", "YOB": 1912}]
sorteddata = sorted(data, key=lambda x: x["YOB"]) # Doesn't matter writting x["YOB"] or x["last"], output is the same
for item in sorteddata:
    print(item)