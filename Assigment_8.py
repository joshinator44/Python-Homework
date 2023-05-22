#! /usr/bin/env python3
try:
    # Get a number from the user
    number = int(input("Enter an integer to square: "))
    print("Display the number squared: " + str(number * number))
except ValueError:
    
    print("You entered an invalid number")

