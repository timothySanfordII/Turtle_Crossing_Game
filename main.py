import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_counter = 1
game_is_on = True
collision = False

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(player.move, "Up")
    car_manager.create_car()
    car_manager.move_cars()
    collision = car_manager.collision_detect(player)
    if collision:
        scoreboard.game_over()
        game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()