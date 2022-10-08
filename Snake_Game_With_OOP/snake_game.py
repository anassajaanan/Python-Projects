import time
from turtle import Screen
from snake import Snake
from food_snake import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game | Made with ❤ by Anas Ajaanan(^_^) ")
screen.tracer(0)

snack=Snake()
my_food=Food()
score=ScoreBoard()

screen.listen()
screen.onkey(snack.up, 'Up')
screen.onkey(snack.down, 'Down')
screen.onkey(snack.left, 'Left')
screen.onkey(snack.right, 'Right')


game_is_on=True
my_food.generate()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()
    if snack.head.distance(my_food)<15:
        my_food.generate()
        score.generat_score()
        snack.extand()
    if snack.head.xcor()>285 or snack.head.xcor()<-285 or snack.head.ycor()>285 or snack.head.ycor()<-285:
        snack.reset_snack()
        score.reset_score()
    if snack.collision_tail():
        snack.reset_snack()
        score.reset_score()



























screen.exitonclick()