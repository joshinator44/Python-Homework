class Category:
    def __init__(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category
class Meal:
    def __init__(self, meal_id, meal, meal_thumb):
        self.__meal_id = meal_id
        self.__meal = meal
        self.__meal_thumb = meal_thumb
        
    def get_meal_id(self):
        return self.__meal_id 
    
    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id
        
    def get_meal(self):
        return self.__meal
    
    def set_meal(self, meal):
        self.__meal = meal
        
    def get_meal_thumb(self):
        return self.__meal_thumb
    
    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb
