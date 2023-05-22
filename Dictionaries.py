'''This program will take any number of user inputs, and it will keep track of every character that the user types in. The program will have a 'quit' word so that it doesn't run infinetly'''


kill_word = "Quit"

dictionary = dict()


if __name__ == "__main__":

    while(True):
        word = input()

        if word == kill_word:
            break

        for character in word:


            if character in dictionary.keys():
                dictionary[character] += 1

            else:
                dictionary[character] = 1
    print(dictionary)
  
