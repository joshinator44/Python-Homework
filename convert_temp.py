#! /usr/bin/env python3

import temperature

def display_menu():
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print()

def convert_temp():
    option = int(input("Enter a menu option: "))
    print()
    if option == 1:
        f = int(input("Enter degrees Fahrenheit: "))
        c = round(temperature.to_celsius(f), 2)
        print("Degress Celsius:", c)
    elif option == 2:
        c = int(input("Enter degrees Celsius: "))
        f = round(temperature.to_farhenheit(c), 2)
        print("Degree Fahrenheit:", f)
    else:
        print("You must enter a valid menu number.")
def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another temperature? (y/n): ")
        print()

    print("Cya")

if __name__ == "__main__":
    main()
