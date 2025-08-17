import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

available_options = [rock,paper,scissors]
cpu_choice = random.choice(available_options)
print(" Welcome to the Rock,Paper,Scissors game! ")
players_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors\n"))

if len(available_options)-1 < players_choice:
    print("Invalid Number, You lose")
else:
    players_choose = available_options[players_choice]
    print(f"You choose: {players_choose}\n Computer choose:{cpu_choice}")
    if players_choose == rock:
        if cpu_choice == rock:
            print("Draw")
        elif cpu_choice == paper:
            print("You lose")
        elif cpu_choice == scissors:
            print("You Won ")
    elif players_choose == paper:
        if cpu_choice == rock:
            print("You Won")
        elif cpu_choice == paper:
            print("Draw")
        elif cpu_choice == scissors:
            print("You lose")
    elif players_choose == scissors:
        if cpu_choice == rock:
            print("You lose")
        elif cpu_choice == paper:
            print("You Won")
        elif cpu_choice == scissors:
            print("Draw")

# import random
#
#
# rock_art = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
#
# paper_art = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
#
# scissors_art = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
#
#
# options = ["rock", "paper", "scissors"]
# art_map = {
#     "rock": rock_art,
#     "paper": paper_art,
#     "scissors": scissors_art
# }
#
#
# win_map = {
#     "rock": "scissors",
#     "paper": "rock",
#     "scissors": "paper"
# }
#
#
# print("Welcome to the Rock, Paper, Scissors game!")
# players_choice_index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
#
# if players_choice_index not in [0, 1, 2]:
#     print("Invalid Number, You lose!")
# else:
#     player = options[players_choice_index]
#     cpu = random.choice(options)
#
#     print(f"\nYou chose:\n{art_map[player]}")
#     print(f"\nComputer chose:\n{art_map[cpu]}")
#
#     if player == cpu:
#         print("It's a Draw!")
#     elif win_map[player] == cpu:
#         print("You Win!")
#     else:
#         print("You Lose!")
#
