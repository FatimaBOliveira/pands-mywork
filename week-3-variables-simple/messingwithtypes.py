# Messing with types
# Practising some variable types
# Author: Fatima

answer_is = "winter season"
result = 12

print (f"We're in {answer_is}")
print ("We're in " + answer_is )

print (f"The answer is {result}")
#print ("The result is " + result) this won't work for numbers, so you need to use the form below
print ("the answer is " + str(result))

print (f"Type of answer is {type(answer_is)}")
print (f"Type of answer is {type(result)}")
print (f"Typhe of answer is {type(type(answer_is))}")