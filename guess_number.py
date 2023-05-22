#1 /usr/bin/env python3

import random
LIMIT = 10
def display_title():
    print("Guess the number!")
    print()
def play_game():
    num = random.randint(1, LIMIT)
    print("I'm thinking of a number between 1 and", LIMIT, "\n")
    count = 1
    while True:
        number = int(input("Your guess: "))
        if number < num:
            count += 1
            print("Too low")
        elif number > num:
            count += 1
            print("Too high")
        else:
            
            print("You guessed the number in", count, "tries")
            return
def main():
    display_title()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("Would you like to play another game? (y/n): ")
        print()
    print("Bye")

if __name__ == "__main__":
    main()
    
