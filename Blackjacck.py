#!/usr/bin/env python3
import cards
import db


def display_title():
    print("BLACKJACK: ")
    print("Blackjack payout is 3:2 ")
    print("Enter 'x' for bet to exit \n")
    print()


def get_starting_money():
    try:
        money = db.read_money()
    except FileNotFoundError:
        money = 0
        
    if money < 5:
        print("You were out of money")
        print("We gave you 100 so you could play.")
        db.write_money(100)
        return 100
    else:
        return money

def get_bet(money):

        if user_bet == "x":
            return user_bet
        user_bet = flout(user_bet)
        if user_bet < 5:
            print("The minimum bet is 5.")
        elif user_bet > 1000:
            print("The maximum bet is 1,000.")
        elif user_bet > money:
            print("You don't have enough money to make that bet.")
        else:
            return user_bet
def display_cards(hand, title):
    print(title.upper())
    for card in hand:
        print(card[0], "of", card[1])
    print()


def play(deck, player_hand):
    while True:
        choice = input("Hit or Stand? (h/s): ")
        print()


        if choice.lower() == "h":
            cards.add_card(player_hand, cards.deal_card(deck))
            if cards.get_points(player_hand) > 21:
                break
            display_cards(player_hand, "YOUR CARDS: ")
        if choice.lower() == "s":
            break
        else:
            print("Not a valid choice, Try again")

    return player_hand
def buy_more_chips(money):
    while True:
        amount = float(input("Amount: "))

        if 0 < amount <= 10000:
            money += amount
            return money
        else:
            print("Invalid amount, must be from 0 to 10,000.")
            
            


def main():
    display_title()

    money = get_starting_money()
    print("Money:", money)
    

    while True:
        if money < 5:
            print("You are out of money.")
            buy_more = input("Would you like to buy more chips? (y/n)").lower()
            if buy_more == "y":
                money = buy_more_chips(money)
                print("Money", money)
                db.write_money(money)
            else:
                break


   
        user_bet = get_bet(money)
        if user_bet == "x":
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

        player_hand = play(deck, player_hand)

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
            money -= user_bet
        elif dealer_points > 21:
            print("Yay! Dealer busted. You Win!")
            money += user_bet
    
        else:
            if player_points == 21 and len(player_hand) == 2:
                if dealer_points == 21 and len(dealer_hand) == 2:
                    print("Dang, dealer has blackjack too. You push")
                else:
                    print("Blackjack! You win!")
                    money += user_bet * 1.5
                    money = round(money, 2)
            elif player_points > dealer_points:
                 print("Hooray! You win!")
                 money += user_bet
            elif dealer_points > player_points:
                  print("Sorry, You lose.")
                  money -= user_bet
            elif player_points == dealer_points:
                print("You push.")
            else:
                print("Sorry, I am not sure what happened.")

        print("Money", money)
        print()

        db.write_money(money)

 


        again = input("Player again? (y/n): ")
        print()
        if again.lower() != "y":
            print("Come again soon!")
            break

        print()

        
    
    print("Bye! ")
    
if __name__ == "__main__":
    main()
else:
    if result.lower() == "blackjack":
        print("You got blackjack!")
        money += round(user_bet * 1.5)
    elif result.lower() == "win":
        print("You won!")
        money += user_bet
    elif result.lower() == "push":
        print("You pushed.")
            
    elif result.lower() == "lose":
        print("You lost.")
        money -= user_bet
