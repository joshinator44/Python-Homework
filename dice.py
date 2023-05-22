#! usr/bin/env python3
import random

class Die:
    def __init__(self):
        self.__value = 1

    def value(self):
        return self.__value
    def roll(self):
        self.__value = random.randrange(1, 7)

class Dice:
    def __init__(self):
        self.__list = []

    def list(self):
        dice_tuple = tuple(self.__list)
        return dice_tuple
    def addDie(self,die):
        self.__list.append(die)

    def rollALL(self):
        for die in self.__list:
            die.roll()
def main():
    print("Die - Tester")
    die = Die()
    print(die.value())
    die.roll()
    print(die.value())

    print("Dice - Tester")
    dice = Dice()
    print(len(dice.list()))
    dice.addDie(die)
    print(len(dice.list()))
    print(dice)
##     for die in dice:
##          print(die.value())
if __name__ == "__main__":
    main()
