# Guess 3
# Program that helps chosing a number between a random number
# Author: Fatima Oliveira

#https://www.w3schools.com/python/python_for_loops.asp


guess = int(input("Please guess the number:"))
for numberToGuess in range(0,100):

    while guess != numberToGuess:
        print (f"Wrong, the number is {numberToGuess}")
        guess = int(input("Please guess again: "))
    if guess == numberToGuess:
        print ("Well done! Yes the number was ", numberToGuess)
        break
    
# https://www.w3schools.com/python/python_while_loops.asp