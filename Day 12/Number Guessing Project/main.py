
import random

def greet():
    difficulty = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ").lower()
    return difficulty


def difficulty_chosen(difficulty):
    if difficulty == "easy":
        return  10
    elif difficulty == "hard":
        return 5
def guessing(life,number):
    while life > 0:
        print(f"You have {life} attempts remaining to guess the number{number}")
        guess =int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! the Answer is {number}")
            return
        elif guess < number:
            life -= 1
            print("Too low")
        elif guess > number:
            life -= 1
            print("Too high")
    print("Sorry you spent all the lives.\n Game Over")

#

def play_game():

    NUMBER = random.choice(range(1, 101))  # 1~100
    difficulty = greet()
    LIFE = difficulty_chosen(difficulty)
    guessing(LIFE, NUMBER)

while True:
    play_game()
    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! Goodbye ")
        break