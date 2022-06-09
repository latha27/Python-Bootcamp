import turtle as t
import random
wn = t.Screen()
t.colormode(255)
t.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


def draw_circle(size):
    for i in range(int(360 / size)):
        r = 50
        t.color(random_color())
        t.circle(r)
        t.left(10)


draw_circle(5)
wn.exitonclick()