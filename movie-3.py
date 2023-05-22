#! /usr/bin/env python3

FILENAME = "movies.txt"
def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replae("\n", "")
            movies.append(line)
        return movies
def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(movie + "\n")
            
    

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list = List all movies")
    print("add = Add a movie")
    print("del = Delete a movie")
    print("exit = Exit program")
    print()

def list_movies(movies):
    
    for i in range(len(movies)):
        movie = movies[i]
        print(str(i + 1) + ", " + movie)
    print()
def main():
    display_menu()
    movies = read_movies()
    while True:
        command  = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add(movies)
        elif command.lower() == "del":
            delete(movies)
        elif command.lower() == "exit":
            break
        
        else:
            print("Not a valid command. Please try agian. \n")
    print("Bye!")
def add_movie(movie_list):
    movie = input("Movie: ")
    movie_list.append(movie)
    write_movies(movies)
    print(movie + " was added. \n")

def delete(movies):
    number = int(input("Number: "))
    if number < 1 or number > len(movies):
        print("Invalid movie number.\n")
    else:
        movie = movies.pop(number - 1)
        write_movies(movies)
        print(movie + " was deleted.\n")
    

if __name__ == "__main__":
    main()
