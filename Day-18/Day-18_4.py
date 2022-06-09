from turtle import Turtle,Screen
from random import choice
tim = Turtle()
colors = ["green", "brown", "red", "blue", "black", "pink", "orange"]


def sides(num_side):
    angle = 360 / num_side

    for i in range(num_side):
        tim.forward(100)
        tim.right(angle)


for num in range(3, 11):
    sides(num)
    colours = choice(colors)
    print(colours)
    tim.color(colours)
























screen= Screen()
screen.exitonclick()