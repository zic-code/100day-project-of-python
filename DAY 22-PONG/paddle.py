from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()

        self.color("white")
        self.shape("square")
        self.shapesize(5.0, 1.0, 1)
        self.pu()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
