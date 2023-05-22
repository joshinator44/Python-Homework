#1 /usr/bin/env python3
"""

This module contains function for converting
temperature between degrees Fahrenheit
and degrees Celius
"""
def to_celsius(fahrenheit):
    """
    This converts degrees Fahrenheit to Celsius
    :param fahrenheit: This is the degrees Fahrenheit to convert
    :return: The converted Celsius value
    """
    celsius = (fahrenheit - 32) * 5/9

    return celsius
def to_farhenheit(celsius):
    """
    This converts degrees Celsius to Fahrenheit
    :param celsiu: This is the degrees Celsius to convert
    :return: The converted Fahrenheit value
    """
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

# the main() function is used to test the conversion function
# this code isn't run if this isn't the main module
def main():
    for temp in range(0, 212, 40):
        print(temp, "Fahrenheit =", round(to_celsius(temp)), "Celsius")

    for temp in range(0, 100, 20):
        print(temp, "Celsius = ", round(to_farhenheit(temp)), "Fahrenheit")

# if this module is the main module, call the main()
# function to test the conversion functions

if __name__ == "__main__":
    main()
    

    
