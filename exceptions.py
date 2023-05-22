#! /usr/bin/env python3
import sys
# Prompt for the filename
filename = input("Enter the OS filename: ")

OS = []

try:
    # Try to open the file
    with open("c: \\cimp8a\\" + filename) as file:
        for line in file:
            # Add the OS to the list
            line = line.replace("\n", "")
            OS.append(line)
except FileNotFoundError as e:
    # Display a file not found error
    print("FileNotFound:", e)
    sys.exit()
except OSError as e:
    # Display an error reading file message
    print("File found - error reading file")
    sys.exit()
except Exception as e:
    # Display a generic error message
    print("An unexpected error occured")
    sys.exit()



