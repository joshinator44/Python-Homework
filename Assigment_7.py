#! /usr/bin/env python3

# Open a file - write mode (overwrite)
file = open("hello.txt", "w")

# Writing to the file
file.write("Hello World\n")
file.write("From Joshua")

# Close the file
file.close()

print("This will read and the print the entire file")
with open("hello.txt") as file:
    text = file.read()
    print(text)

print()

# Read the entire file and print 1 line at a time
print("This will read the entire file "
      "and then print 1 line at a time")
with open("hello.txt") as file:
    for line in file:
        print(line, end="")

print("\n")

# Read the entire file as a list
print("This will read file as a list "
      "and then print 1 list item at a time")
with open("hello.txt") as file:
    listItems = file.readline()
    for item in listItems:
        print(item, end="")

print("\n")

# Read and print the file 1 line at a time
print("This will read and print the file "
      "1 line at a time")
with open("hello.txt") as file:
    line = file.readline()
    print(line, end="")
    line = file.readline()
    print(line)
        
