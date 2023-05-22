

class character:
    health = 100
    strength = 5
    bag = []
    
    
class player(character):

    equipped_items = []
    current_weight = 0
    max_weight = 10
    name = ""

    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        item_strength = 0
        for item in self.equipped_items:
            if type(item) == weapon:
                item_strength += item.strength
        enemy.health -= self.strength + item_strength          
            
    def pickup_item(self, item):
        if (self.current_weight >= self.max_weight):
            print("Player cannot pick up this item!")
        else:
            self.bag.append(item)
            self.current_weight += item.weight
        
    def equip_item(self, item):
        self.equipped_items.append(item)

    def check_bag(self):
        '''This function will just check the name of every item in your bag'''
        for item in self.bag:
            print(item.name)
        
class item:
    weight = 1
    name = ""

    def __init__(self, name):
        self.name = name

class weapon(item):
    strength = 1

class armor(item):
    defense = 1





def word_match(word, match):
    new_word = word.replace(" ", " ")
    if new_word.upper() == match.upper():
        
        return True
    else:
        return False

random_drop_list = [
    weapon("Sword"),
    weapon("Bow"),
    weapon("Axe")
    ]



if __name__ == "__main__":
    
    while True:
        
        name = input("What is your character name? ")
        player1 = player(name)
        
        for item in random_drop_list:
            print(item.name)
            
        weapon_choice = input("Choose your weapon: ")

        for item in random_drop_list:
            if word_match(item.name, item.name):
                player1.equip_item(item)
                print("{} equipped {}".format(player1.name, item.name))
                    
            


