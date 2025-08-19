from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):

        self.segments =[]
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.pu()
            new_segment.goto(position)
            self.segments.append(new_segment)