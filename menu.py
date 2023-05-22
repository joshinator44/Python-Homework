
class Recipe:
    ''' 1. Ingredients
        2. Measurements (how much of each specific ingredient to use)
        3. Directions! So what to do with the ingredients!    
    '''
    
    def __init__(self, i_name, i_ingredients, i_measurements, i_directions):

        self.name = i_name
        self.ingredients = i_ingredients
        self.measurements = i_measurements
        self.directions = i_directions

    def print(self):
        print("Ingredients: {} \n Measurements: {} \n {} ".format(self.ingredients, self.measurements, self.directions))


default_recipe = Recipe("Burger", ["Buns", "Patty", "Lettuce"], {"Buns":2, "Patty":1, "Lettuce": 1}, "Cook the burger")

dish_list = [default_recipe]

kill_word = "Quit"

add_word =  "Add"

remove_word = "Remove"

check_word = "Check"

recipe_index = dict()

def add():
    '''This will add a new dish
        1. We are probably going to need to add a new recipe to the Dish Dictionary...
        2. Get the user input for the NAME
        3. Get the user input for the list of ingredients...
        4. Get the user input for the measurements
        5. Get the user input for the directions.
        6. Create the new recipe using the definition we defined above, and then add it to the list of dishes/recipes that we are going to store for this menu app. 
        '''
    name = input("What is the recipe name: ") 

    ingredients = []
    
    while(True):

        ingredient_input = input("Please type in an ingredient. If you are done, type in 'Done': ")
        if ingredient_input == "Done":
            break 
        ingredients.append(ingredient_input)

    '''We need a data structure for the measurements.'''
    
    measurement = {}
    '''
    In English, the for loop would read like this: for each ingredient in the list of ingredients, do this for each ingredient.
    '''
    
    for ing in ingredients: 
        amount = input("How much of {} do we need?".format(ing))
        measurement[ing] = amount

    directions = input("What are the directions: ")
    
    ''' At this point in the function, we have all the information we need to create a recipe.'''

    new_recipe = Recipe(name, ingredients, measurement, directions)

    return new_recipe

def remove():
    '''This function will remove a dish from the menu'''


    remove_dish = input("Which dish would you like to remove: ")
    found_dish = False

    for dish in dish_list:
        if dish.name == remove_dish:
            found_dish = True
            '''We're going to need to do something to remove the dish! '''
            dish_list.remove(dish)
            print("This dish has been removed ")

        if found_dish:
            pass
        else:
            print("Dish does no exist")

        

                                                

    
def check():
    '''This function will check the menu for a dish, and give you the recipe'''
    '''What do we need to do for the check function? If the user wants to check a recipe, what should the program ask?
    Probably the name, since we'll the name to check to see if it's a valid recipe that's in our list. 
    '''
    dish_name = input("What is the name of the recipe you want to check?: ")

    found_dish = False
    
    for dish in dish_list:
        if dish.name == dish_name:
            '''The code will go here if the dish exists. We should print out all the information that the user needs now.'''

            found_dish = True
            
            print(dish.ingredients)
            print(dish.measurements)
            print(dish.directions)

    if found_dish:
        pass
    else:
        print("Dish does not exist in the list!")
            
    
    
if __name__ == "__main__":

    while True:

        user_input = input("User Commands: Add, Remove, Check, Quit. Enter your command: ")

        if user_input == add_word:

            print("Add...")

            new_recipe = add()
            
            dish_list.append(new_recipe)
            '''The .append that you see there is a member function (meaning it's part of the class definition) of a LIST. This is defined
                by Python, and you can read about in the Python documentation.'''

        elif user_input == remove_word:
            print("Remove...")

            remove()

        elif user_input == check_word:

            print("Check...")

            check()

        elif user_input == kill_word:
            
            break
        




