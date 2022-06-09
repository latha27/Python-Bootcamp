import turtle
import random
tim = turtle.Turtle()
wn = turtle.Screen()


def forward_tu():
    tim.forward(5)


def backward_tu():
    tim.backward(5)


def counter_clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clock_wise():
    new_heading = tim.heading - 10
    tim.setheading(new_heading)


def clear_tu():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


wn.onkey(forward_tu, "w")
wn.onkey(backward_tu, "s")
wn.onkey(counter_clock, "a")
wn.onkey(clock_wise, "d")
wn.onkey(clear_tu, "c")
wn.listen()
wn.exitonclick()