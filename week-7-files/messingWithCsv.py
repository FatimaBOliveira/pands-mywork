# Messing with Csv
# Program that loads info from CSV files
# Author: Fatima Oliveira

import csv

FILENAME ="test.csv"

with open(FILENAME, "r") as test:
    csv_reader = csv.reader(test, delimiter=",")
    firstline = True
    for line in test:
        if firstline:
            firstline = False
            continue
        # print(line) # will print all the lines in csv file
        print(line[2]) # will print the occupation