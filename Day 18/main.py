from random import *
from turtle import *

colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    random_col = (r, g, b)
    return random_col

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed","DeepSkyBlue","LightSeaGreen","wheat", "SlateGray","SeaGreen"]
directions = [0, 90, 180, 270]

jim = Turtle()
jim.shape("turtle")
jim.speed("fastest")
def random_color_jim():
    jim.color(choice(colours))


#how many angles in the  shape = i
#todo 360 / i = outside angle
# triangle = 360 /3 = 120 degree
# square = 360 / 4 = 90 degree
# pentagon = 360 /5 = 72 degree

def draw_shape(num_sides):
    for i in range(3,num_sides):
        for _ in range(i):
            jim.forward(100)
            jim.right(360/i)
        jim.color(choice(colours))

def random_walk():
    for _ in range(200):
        jim.setheading(choice(directions))
        jim.color(random_color())
        jim.pensize(choice(range(1,20)))
        jim.forward(20)

def sprio_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        jim.color(random_color())
        jim.circle(100)
        jim.setheading(jim.heading() + size_of_gap)


sprio_circle(10)
# draw_shape(choice(range(3,12)))

screen = Screen()
screen.exitonclick()


# import heroes
# print(heroes.gen())



