import turtle
import random

is_turtle = False
wu = turtle.Screen()
wu.setup(width=500, height=400)
user_bet = wu.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter the a color:")
color_list = ["red", "green", "black", "pink", "blue", "yellow", "brown"]
all_turtle = []
count_increase = 0
for color in color_list:
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=-100+count_increase)
    count_increase = count_increase + 30
    all_turtle.append(new_turtle)


if user_bet:
    is_turtle = True
while is_turtle:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            tu_color = turtle.pencolor()
            is_turtle = False
            if user_bet == tu_color:
                print("You've won")

            else:
                print(f"You've lose. The winning turtle is {tu_color}")

        move_turtle = random.randint(0, 10)
        turtle.forward(move_turtle)


wu.exitonclick()
