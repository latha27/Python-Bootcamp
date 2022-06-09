from turtle import Turtle,Screen
import random
direction = [0, 90, 180, 270]
tim = Turtle()
colors = ["green", "brown", "red", "blue", "black", "pink", "orange"]
wn = Screen()
tim.pensize(5)
tim.speed("fastest")

for i in range(50):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))

wn.exitonclick()