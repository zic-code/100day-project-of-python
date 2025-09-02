import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
answered_states = []
correct_score=0
is_game_on = True
data =pandas.read_csv("50_states.csv")
states = data.state.to_list()

while is_game_on:
    answer_state = screen.textinput(title= f"{correct_score}/50 Guess the state", prompt = "What's another state's name").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in answered_states]
        # missing_states = []
        # for state in states:
        #     if state not in answered_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        is_game_on = False
    if len(answered_states) == 50:
        is_game_on = False
    if answer_state in states:
        if answer_state in answered_states:
            print("You answered that states!")
        else:
            state_data = data[data.state == answer_state]
            row = state_data.iloc[0]
            t = turtle.Turtle()
            t.hideturtle()
            t.pu()
            t.goto(int(row.x),int(row.y))
            t.write(state_data.state.item())
            correct_score += 1
        answered_states.append(answer_state)


#1. Convert the guess to Title case


#2. Check if the guess is among the 50 states
#3. Write correct guesses onto the map.
#4. Use a loop to allow the use to keep guessing
#5. Record the correct guesses in a list.
#6 Keep track of the score

screen.exitonclick()