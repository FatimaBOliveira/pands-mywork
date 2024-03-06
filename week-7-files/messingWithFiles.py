# Messing with files
# Author: Fatima Oliveira

FILENAME = "data.txt"

with open(FILENAME, "r") as f: # r is read mode
    #data = f.read()
    for data in f: # will do the same as above and it's more commum way to write.
        #print (data) # lines have an extra empty line between each other. If not needed, write as below with end=.
        #print (data, end="") # The end= part will be between the lines.
        print(data.strip()) # will work same as above code.

with open("data2.txt", "wt") as f: # if data2.txt doesn't exist, the line
    f.write("Hey now.\n") # any changes done, and if python runs, then data2.txt will be updates with changes, and previous will be deleted.
    f.write("Dark blue cat.\n")

with open("data2.txt", "a") as f: # "a" will add new lines below.
    f.write("Finally!\n")
    f.write("Weekend.\n")

with open("data2.txt", "w+") as f: # W will delete everything from previous entries. Will be treated as main.
    f.write("Again\n")
    f.write("Changes.\n")
    f.seek(0) # Needed for the entries above to show up when printed below
    data = f.read()
    print(data)

print("Done.")