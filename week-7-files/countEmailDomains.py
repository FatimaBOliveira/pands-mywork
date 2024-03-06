# Count email Domains
# Program that checks the email domains of a csv file
# Author: Fatima Oliveira

import csv

FILENAME = "employees.csv"
domainCount = {}

with open(FILENAME, "r") as data:
    csv_reader = csv.reader(data, delimiter=",")
    firstline = True
    count = 0
    for line in csv_reader:
        if firstline:
            firstline = False
            continue
        email = line[8]
        start = email.find("@")
        domain = email[start+1:]
        #print(domain) # will print only the domains
        if domain not in domainCount:
            domainCount[domain] = 0
        else:
            domainCount[domain] += 1
for key, value in domainCount.items():
    print(key, "\t", value)