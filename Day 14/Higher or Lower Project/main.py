# display Art:
from art import logo, vs
from game_data import data
from random import choice


def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_disc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_disc}, from{account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Takes a user's guess and the follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return user_guess =="a"
    else:
        return user_guess == "b"



print(logo)
score = 0
game_should_continue =True
account_b = choice(data)

while game_should_continue:
    #Generate a random account form the game data
    account_a = account_b
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Clear the screen
    print("\n"*20)
    print(logo)

    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Give user feedback on their guess.

    # score keeping.
    if is_correct:
        score += 1
        print(f"You're right! Current score is {score}.")

    else:
        print(f"Sorry, that's wrong. Current score is {score}.")
        game_should_continue= False
#Make the game repeatable.

#making account at positionB become next account at position A.


