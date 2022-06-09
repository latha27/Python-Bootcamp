import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
player = Player()
score = Scoreboard()

screen.onkey(player.up, "Up")
# screen.onkey(player.right(), "Right")
# screen.onkey(player.left(), "Left")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move_cars()
    screen.update()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        score.increase_level()






