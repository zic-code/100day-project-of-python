import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = []
correct_score=0
is_game_on = True
data =pandas.read_csv("50_states.csv")

while is_game_on:
    answer_state = screen.textinput(title= f"{correct_score}/50 Guess the state", prompt = "What's another state's name")
    for state in data["state"]:
        states.append(state.lower())
    if answer_state.lower() in states:
        states.remove(answer_state)
        correct_score += 1
    else: print("Wrong!")

#1. Convert the guess to Title case


#2. Check if the guess is among the 50 states
#3. Write correct guesses onto the map.
#4. Use a loop to allow the use to keep guessing
#5. Record the correct guesses in a list.
#6 Keep track of the score

screen.exitonclick()