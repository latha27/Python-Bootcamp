import turtle as t
import random
direction = [0, 90, 180, 270]
tim = t.Turtle()
t.colormode(255)
wn = t.Screen()
tim.pensize(5)
tim.speed("fastest")


def randomcolor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


for i in range(50):
    tim.color(randomcolor())
    tim.forward(30)
    tim.setheading(random.choice(direction))

wn.exitonclick()