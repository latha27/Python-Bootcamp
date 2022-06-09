from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import snake
import time

wu = Screen()
wu.setup(width=600, height=600)
wu.bgcolor("black")
wu.title("My Snake Game")
wu.tracer(0)

snake = snake.Snake()
food = Food()
score = ScoreBoard()


wu.listen()
wu.onkey(snake.up, "Up")
wu.onkey(snake.down, "Down")
wu.onkey(snake.left, "Left")
wu.onkey(snake.right, "Right")


is_game_on = True
while is_game_on:
    wu.update()
    time.sleep(0.2)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        is_game_on = False
        score.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

wu.exitonclick()