# Quiz
# the with statement will automatically close the file when it is finished with it
# Author: Fatima Oliveira

'''
with open("test-a.txt") as f:
   data = f.read()
   print (data)
# the old way of doing this is
# f = open ("test1.txt")
# data = f.read()
# print(data)
# f.close()
'''

# a. Look at the program below, if the file test-a.txt does not exist. What will happen when the program runs?
    # Can't read file that doesn't exit, so it will tell that there's no such file or directory.
# b. Look at the program below, if the file test-b.txt does not exist, what will be outputted to the console when this program is run?
    # It will create a file wiht name test-b.txt and will output number: 7; 13
# c. What will the contents of the file test-b.txt be when this program is run?
    # It will contain the last line written "another line"
'''
# the with statement will automatically close the file when it is finished with it
with open("test-b.txt", "w") as f:
  data = f.write("test b\n") # returns the number of chars written
  print (data)
with open("test-b.txt", "w") as f2: # open file again
  data = f2.write("another line\n")
  print (data)
'''
# d. Look at the modified program below, what will the contents of the file be after this program is run.
    # Will create another file with name "test-d.txt", and will output both lines since 1 is w(write) and 2 is a(add).

# The with statement will automatically close the file when it is finished with it
with open("test-d.txt", "w") as f:
  data = f.write("test d\n") # returns the number of chars written
  print (data)
with open("test-d.txt", "a") as f2: # open file again
   data = f2.write("another line\n")
   print (data)