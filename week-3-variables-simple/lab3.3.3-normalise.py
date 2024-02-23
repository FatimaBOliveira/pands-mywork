# Normalise
# Program that reads in a string and strips
# Author: Fatima


# any leading or trailing spaces.
# It also converts all the letters to lower case.


rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

# and the normalised one
print(f"That String normalised is :{normalisedString}")

# It then outputs the lengths of the original string
print(f"we reduced the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")