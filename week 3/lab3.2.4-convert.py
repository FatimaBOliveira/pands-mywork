# Convert
# Convert dollars in cents
# Author: Fatima

# input amout in dollars: -5.99 (floated amount)
# amount showed in cents: 599

dollar = 5.99
amount = float(-dollar)

print("Please enter an amount: " + str(amount))

# https://codereview.stackexchange.com/questions/121074/safely-convert-dollars-to-cents

cents = dollar * 100
print (cents)