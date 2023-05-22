#! /usr/bin/env python3


import requests



def show_title():
    print("My Recipes Program")
    print()

def show_menu():
    """
        This method displays the menu to screen"
    """
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all Meals for a Category")
    print("3 - Search Meal by Name")
    print("4 - Random Meal")
    print("5 - List all areas")
    print("6 - Search Meals by area")
    print("7 - Menu")
    print("0 - Exit the program\n\n")

def list_categories(categories):

    print("CATEGORIES")
    for i in range(len(categories)):
        category = categories[i]
        print(category.get_category())
    print()


def get_meals_by_category(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = requests.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            category = Meal(meal_data['idMeal'],
                            meal_data['strMeal'],
                            meal_data['strMealThumb'])
            meals.append(category)

    except (ValueError, KeyError, TypeError):
        print("JSON format error")
    return meals
def get_meals_by_information(category):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = requests.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            category = Meal(meal_data['idMeal'],
                            meal_data['strMeal'],
                            meal_data['strMealThumb'])
            meals.append(category)

    except (ValueError, KeyError, TypeError):
        print("JSON format error")
    return meals

def list_meals_by_category(category, meals):
    print(category.upper() + " MEALS")
    for i in range(len(meals)):
        meal = meals[i]
        print(meal.get_meal())
        print()

        
    

def search_meal_by_category(categories):
    lookup_category = input("Enter a Category: ")
    found = False

    for i in range(len(categories)):
        category = categories[i]
        if category.get_category().lower() == lookup_category.lower():
            found = True
            break

    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals_by_category(lookup_category, meals)
    else:
        print("Invalid Category, please try again")
def search_information_for_meal(categories):
    lookup_category = input("Enter a Meal: ")
    found = False

    for i in range(len(categories)):
        category = categories[i]
        if category.get_meals_by_information().lower() == lookup_category.lower():
            found = True
            break

    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals_by_category(lookup_category, meals)
    else:
        print("Invalid Category, please try again")

def main():
    show_title()
    show_menu()


    categories = requests.get_categories()
    while True:
        command = input("Command: ")
        if command == "1":
            list_categories(categories)
        elif command == "2":
            search_meal_by_category(categories)
        elif command == "3":

        else:
            print("Not a valid command. Please try again.\n")
            

if __name__ == "__main__":
    main()
