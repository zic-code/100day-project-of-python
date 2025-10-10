from turtle import Turtle
ALIGNMENT = "center"
FONT =("Courier", 24,"normal")
with open("data.txt") as file:
    contents = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = contents
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as file2:
                file2.write(str(self.highscore))
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

