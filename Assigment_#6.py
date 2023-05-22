#! /usr/bin/env python3

movies = [["Deadpool", "2016", "8.0"],
          ["Casino Royale", "2006", "8.6"],
          ["Star Wars: A New Hope", "1977", "8.6"]]

movie = ["Monsters, Inc", "2001", "8.1"]
movies.append(movie)
# The fist number is the row
# the second number is the column
print("Item in the movies position [0][0]: " + movies[0][0])
print("Item in the movies position [3][2]: " + movies[3][2])

print()
# Display all the elements in the movie list
# WE will need to use a nest for loop to do this

# The first loop goes through the row
for movie in movies:
    #The second loop goes through the columns
    for item in movie:
        print(item, end=" | ")
    print()
    
