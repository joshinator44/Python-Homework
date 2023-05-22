#! /usr/bin/env python3
import csv
import sys

FILENAME = "movie.csv"
def exit_program():
    print("Terminating program.")
    sys.exit()
def read_movies():
    movie_list = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            movie_list.append(row)
    return movie_list


def write_movies(movie_list):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(movie_list)
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
    if len(movie_list) == 0:
        print("There are no movies in the list.\n")
        return
    else:
        i = 1
        for row in movie_list:
            print(str(i) + ". " + row[0] + " (" + str(row[1]) + ")")
            i += 1
        print()
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
def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = (name, year)
    movie_list.append(movie)
    write_movies(movie_list)
    print(movie[0] + " was added.\n")

def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
            movie = movie_list.pop(number-1)
            write_movies(movie_list)
            print(movie[0] + " was deleted.\n")
    

if __name__ == "__main__":
    main()







    
