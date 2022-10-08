import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car=CarManager()



screen.listen()
screen.onkey(player.player_move, 'Up')
score=Scoreboard()



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.add_cars()
    car.move_care()
    for i in range(len(car.list_cars)):
        if player.distance(car.list_cars[i])<=20:
            score.game_over()
            game_is_on = False
    if player.cheak_line():
        player.restart_game()
        car.reset_cars()
        score.score+=1
        car.speed()
        score.new_score()













screen.exitonclick()
