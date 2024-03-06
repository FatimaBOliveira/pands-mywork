# Messing with the OS modules
# Author: Fatima Oliveira

import os

FILENAME = "messingWithFiles.py"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end="")
else:
    print(FILENAME, "Does not exist.")

# os.remove("data2.txt") # Will delete the file.