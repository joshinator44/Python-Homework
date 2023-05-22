#! /usr/bin/env python3
from dice import Die

class Game:
    def __init__(self):
        self.turn = 1
        self.score = 0
        self.scoreThisTurn = 0
        self.isTurnOver = False
        self.isGameOver = False
        self.die = Die()

def main():
    print("Game - Tester")
    game = Game()
    print("turn", game.turn)
    print("score",game.score)
    print("scoreThisTurn",game.scoreThisTurn)
    print("isTurnOver", game.isTurnOver)
    print("isGameOver", game.isGameOver)
    print("die", game.die)

if __name__ == "__main__":
    main()

