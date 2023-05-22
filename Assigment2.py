#! /usr/bin/env python3

import random
# Get a random number between 1 and 9
randomNumber = random.randint(1, 9)
yourGuess = 0
count = 0

# Continue guessing until the guess is correct or the user types "Exit"
while yourGuess !=  randomNumber and yourGuess != "exit":
    yourGuess = input("Enter a guess between 1 to 9 or exit to end the game")

     # If the user type exit, and the application
    if yourGuess == "exit":
        break

    # Cast the user's guess to an int so it can be
    # used in the comparison below  
    yourGuess = int(yourGuess)

    count += 1

    if yourGuess < randomNumber:
        print("Too low")
    elif yourGuess > randomNumber:
        print("Too high")
    else:
        print("Right!")

        print("You took only", count, "tries!")
input() # Get the user's next guess
