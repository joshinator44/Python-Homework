#1 usr/bin/env python3

import sys
import os
# prompt for the fil name
filename = input("Enter the OS filename: ")

OS = []

try:
    #open the file
    with open(filename) as file:
        try:
            if os.stat(filename).st_size == 0:
                raise ValueError("The file is empty")
            for line in file:
                # add the os from the file to the list
                line = line.replace("\n", "")
                OS.append(line)

        except Exception as e:
            # display a generic error message
            print(type(e), e)
            sys.exit()
        finally:
            file.close()

except FileNotFoundError as e:
    # display a fgeneric error messahe
    print("Could not find the file " + filename)
    sys.exit

