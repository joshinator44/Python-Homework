#!/usr/bin/env python3
import cards
import db
import locale as lc
from datetime import time, datetime


result = lc.setlocale(lc.LC_ALL, "en_US.UTF-8")
if result == "C":
    lc.setlocale(lc.LC_ALL, "en_US.UTF-8")
    


def display_title(start_time):
    print("BLACKJACK! ")
    print("Blackjack payout is 3:2 ")
    print("Enter 'x' for bet to exit")
    print("Start time:", start_time.strftime("%I:%M:%S %p"))
    print()


def get_starting_money():
    try:
        money = db.read_money()
    except FileNotFoundError:
        money = 0
        
    if money < 5:
        print("Data file missing, resetting starting amount to 1000.")
        db.write_money(100000)
        return 1000
        
    else:
        return money

def get_bet(money):
    while True:
        try:
            bet_amount = float(input("\nBet amount:      "))
        except ValueError:
            print("Invalid amount. Try again.")
            continue
        if bet_amount < 5:
             print("The minimum bet is 5.")
        elif bet_amount > 100000:
            print("The maximum bet is 1,00000.")
        elif bet_amount > money:
             print("You don't have enough money to make that bet.")
        else:
            return bet_amount
def display_cards(hand, title):
    print(title.upper())
    for card in hand:
        print(card[0], "of", card[1])
    print()


def play(deck, player_hand, money, bet_amount):
    while True:
        can_double_down = True
        if (money >= bet_amount * 2) and (len(player_hand) == 2):
            can_double_down = True
        if can_double_down:
            msg = "Hit, Stand, or Double Down? (h/s/d): "
        else:
            msg = "Hit or Stand? (h/s): "
        choice = input(msg)
        print()


        if choice.lower() == "h":
            cards.add_card(player_hand, cards.deal_card(deck))
            if cards.get_points(player_hand) > 21:
                break
            display_cards(player_hand, "YOUR CARDS: ")
        elif choice.lower() == "d":
            if (money <= bet_amount * 2) and (len(player_hand) == 2):
                print("Insufficent funds to do that")
                choice = input(msg)
                break
            else:
                cards.add_card(player_hand, cards.deal_card(deck))
                display_cards(player_hand, "YOUR CARDS: ")
                break
        elif choice.lower() == "s":
            break
        else:
            print("Not a valid choice, Try again")

    return player_hand, bet_amount
def buy_more_chips(money):
    while True:
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid amount. Try again.")
            continue

        if 0 < amount <= 10000:
            money += amount
            return money
        else:
            print("Invalid amount, must be from 0 to 10,000.")
            
            


def main():
    start_time = datetime.now()
    display_title(start_time)

    money = get_starting_money()
    print("Money:", lc.currency(money, grouping=True))
    

    while True:
        if money < 5:
            print("You are out of money.")
            buy_more = input("Would you like to buy more chips? (y/n)").lower()
            if buy_more == "y":
                money = buy_more_chips(money)
                print("Money:", lc.currency(money, grouping=True))
                db.write_money(money)
            else:
                break


   
        bet_amount = get_bet(money)
        if bet_amount == "x":
            break
        
        deck = cards.get_deck()
        cards.shuffle(deck)

        dealer_hand = cards.get_empty_hand()
        player_hand = cards.get_empty_hand()

        cards.add_card(player_hand, cards.deal_card(deck))
        cards.add_card(player_hand, cards.deal_card(deck))
        cards.add_card(dealer_hand, cards.deal_card(deck))

        display_cards(dealer_hand, "DEALER'S SHOW CARD:")
        display_cards(player_hand, "YOUR CARDS: ")

        player_hand, bet_amount = play(deck, player_hand, money, bet_amount)

        while cards.get_points(dealer_hand) < 17:
            cards.add_card(dealer_hand, cards.deal_card(deck))

        display_cards(dealer_hand, "DEALER'S CARDS: ")

        print("YOUR POINTS:       " + str(cards.get_points(player_hand)))

        print("DEALER'S POINTS:       " + str(cards.get_points(dealer_hand)))
        print()
        player_points = cards.get_points(player_hand)
        dealer_points = cards.get_points(dealer_hand)

        if player_points > 21:
            print("Sorry. You lose.")
            money -= bet_amount
        elif dealer_points > 21:
            print("Yay! Dealer busted. You Win!")
            money += bet_amount
    
        else:
            if player_points == 21 and len(player_hand) == 2:
                if dealer_points == 21 and len(dealer_hand) == 2:
                    print("Dang, dealer has blackjack too. You push")
                else:
                    print("Blackjack! You win!")
                    money += bet_amount * 1.5
                    money = round(money, 2)
            elif player_points > dealer_points:
                 print("Hooray! You win!")
                 money += bet_amount
            elif dealer_points > player_points:
                  print("Sorry, You lose.")
                  money -= bet_amount
            elif player_points == dealer_points:
                print("You push.")
            else:
                print("Sorry, I am not sure what happened.")

        print("Money:", lc.currency(money, grouping=True))
        print()

        db.write_money(money)

 


        again = input("Player again? (y/n): ")
        print()
        if again.lower() != "y":
            print("Come again soon!")
            break

        print()

        
    stop_time = datetime.now()
    display_end(start_time, stop_time)
    
def display_end(start_time, stop_time):
    elapse_time = stop_time - start_time
    minutes = elapse_time.seconds // 60
    seconds = elapse_time.seconds % 60

    hours = minutes // 60
    minutes = minutes % 60
    
    time_object = time(hours, minutes, seconds)

    print("Stop time:", stop_time.strftime("%I:%M:%S %p"))
    print("Elapsed time:", time_object)
    print("Cya!")

if __name__ == "__main__":
    main()

else:
    if result.lower() == "blackjack":
        print("You got blackjack!")
        money += round(bet_amount * 1.5)
    elif result.lower() == "win":
        print("You won!")
        money += bet_amount
    elif result.lower() == "push":
        print("You pushed.")
            
    elif result.lower() == "lose":
        print("You lost.")
        money -= bet_amount
