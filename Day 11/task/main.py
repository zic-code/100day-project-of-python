import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
games = ["blackjack"]
def game_start(money=100):
    game_select =input(f"You have ${money} now. which game do you want to play?").lower()
    if game_select == "blackjack":
        bet = int(input("how much you want to bet in this game? $"))
        if bet > money:
            print("You can not bet more than what you have")
            game_start(money)
        else:
            blackjack(money,bet)
def draw_card():
    return random.choice(cards)

def calculate_total(hand):
    total = sum(hand)
    while total > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        total = sum(hand)
    return total

def blackjack(money,bet):
    print(logo)
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower() == "y":
        
        player_hand=[draw_card(),draw_card()]
        computer_hand=[draw_card(),draw_card()]
        player_total = calculate_total(player_hand)
        computer_total = calculate_total(computer_hand)
        print(f" Your hands have {player_hand}  your total = {player_total}")
        if player_total == 21:
            print(f"Congratulation You got blackJack!")
            money += bet *1.5
            print(f"Now you have ${money}left ")
            return blackjack(money,bet)
        print(f" Dealer has [{computer_hand[0]}, ?]")

        while input("Hit or Stand?").lower() == "hit":
            player_hand.append(draw_card())
            player_total = calculate_total(player_hand)
            print(f" Your hands have {player_hand}  your total = {player_total}")
            if player_total > 21:
                print("you busted")
                money -= bet
                print("You lose")
                money -= bet
                print(f"Now you have ${money}left ")
                if money > bet:
                    blackjack(money, bet)
                else:
                    if money <= 0:
                        print("You have no money left. Game over")
                        return print("Goodbye")
                    else:
                        print("You don't have enough money")
                        game_start(money)

        while computer_total < 16:
            computer_total = calculate_total(computer_hand)
            computer_hand.append(draw_card())
            if computer_total > 21:
                print(f" dealer has {computer_hand} dealers total = {computer_total}")
                print("Dealer busted")
                money += bet
                print(f"Now you have ${money}left ")
                return blackjack(money,bet)
        print(f" dealer has {computer_hand} dealers total = {computer_total}")


        if player_total == computer_total:
            print("Draw")
            print(f"Now you have ${money}left ")
        if player_total > computer_total:
            print("You Won")
            money += bet
            print(f"Now you have ${money}left ")
        elif player_total < computer_total:
            print("You lose")
            money -= bet
            print(f"Now you have ${money}left ")
            if money > bet:
                blackjack(money,bet)
            else:
                if money <= 0:
                    print("You have no money left. Game over")
                    return print("Goodbye")
                else:
                    print("You don't have enough money")
                    game_start(money)
    game_start(money)
    return None


game_start(money=100)