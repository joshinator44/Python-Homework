#! /usr/bin/env python3
import csv
import sys

FILENAME = "movies.csv"
def exit_program():
    print("Terminating program.")
    sys.exit()
def read_movies():
    try:
        movies = []
        with open(FILENAME) as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        print("Could not find " + FILENAME + " file.")
        exit_program()
    except Exception as e:
        print(typ(e), e)
        exit_program()


def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    except Exception as e:
        print(type(e), e)
        exit_program()
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list = List all movies")
    print("add = Add a movie")
    print("del = Delete a movie")
    print("exit = Exit program")
    print()

def list_movies(movie_list):
    i = 1
    for movie in movie_list:
        print(str(i) + ". " + movie[0], "(" + movie[1] + ")")
        i += 1
    print
def add(movie_list):
    name = input("Movie: ")
    try:
        year = int(input("Year: "))
        movie = (name, year)
        movies.appnd(movie)
        write_movies(movie_list)
        print(movie[0] + " was added.\n")
            
    except ValueError:
            print("Invalid entry for year, please try again.")

def delete(movie_list):
    while True:
        try:
            number = int(input("Enter number or 0 to exit: "))
            if number == 0:
                break
            elif number < 1 or number > len(movie_list):
                print("There is no movie with that number, please try again.\n")
                continue
            else:
                movie = movie_list.pop(number-1)
                write_movies(movie_list)
                print(movie + " was deleted.\n")
    
        except ValueError:
            print("Invalid movie number. Please try again.")
            continue
def main():
    movie_list = read_movies()
    
    display_menu()
    while True:
        command  = input("Command: ")
        if command.lower() == "list":
            list_movies(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        
        else:
            print("Not a valid command. Please try agian. \n")
    print("Bye!")

if __name__ == "__main__":
    main()







    
