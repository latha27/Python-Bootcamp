from turtle import Turtle, Screen
from paddle_create import PaddleCreate
from ball import Ball
from scoreboard import Scoreboard
import time

wu = Screen()
ball = Ball()
score = Scoreboard()

wu.setup(width=800, height=600)
wu.bgcolor("black")
wu.title("Pong")
wu.tracer(0)

r_paddle = PaddleCreate((350, 0))
l_paddle = PaddleCreate((-350, 0))

wu.listen()
wu.onkey(r_paddle.up, "Up")
wu.onkey(r_paddle.down, "Down")
wu.onkey(l_paddle.up, "w")
wu.onkey(l_paddle.down, "s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    wu.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()




wu.exitonclick()
