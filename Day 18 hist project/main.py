import colorgram
import turtle as tur
import random


tur.colormode(255)
tim = tur.Turtle()
tim.speed("fastest")
tim.penup()
rgb_colors = []
colors = colorgram.extract("histspot.jpg",30)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
color_list = rgb_colors


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(rgb_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = tur.Screen()
screen.exitonclick()



