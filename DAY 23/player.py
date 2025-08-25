from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.pu()
        self.goto(STARTING_POSITION)
        self.go_to_start()
        self.setheading(90)


    def go_up(self):
        new_y = self.ycor()+ 20
        self.goto(self.xcor(),new_y)
        self.setheading(90)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)
        self.setheading(270)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False




