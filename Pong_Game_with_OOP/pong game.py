from turtle import Screen,Turtle
import time
from paddles import Paddle
from line import Line
from score_right import ScoreRight
from score_left import ScoreLeft
from ball import Ball

screen=Screen()
screen.bgcolor("black")
screen.screensize()
screen.setup(1.0, 1.0)
screen.tracer(0)
paddle = Paddle()
line=Line()
score_right=ScoreRight()
score_left=ScoreLeft()
ball=Ball()
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    screen.listen()
    screen.onkey(paddle.move_up_r, 'Up')
    screen.onkey(paddle.move_down_r, 'Down')
    screen.onkey(paddle.move_up_l, 'w')
    screen.onkey(paddle.move_down_l, 's')
    ball.move_ball()
    for i in range(len(paddle.list_right_squares)):
        if ball.distance(paddle.list_right_squares[i])<15:
            ball.setx(ball.xcor())
            ball.dx *= -1
            score_right.add_score_right()
    for i in range(len(paddle.list_left_squares)):
        if ball.distance(paddle.list_left_squares[i])<15:
            ball.setx(ball.xcor())
            ball.dx *= -1
            score_left.add_score_left()
    if ball.xcor()>780 :
        score_right.game_over_right()
        game_is_on=False
    if ball.xcor()<-780:
        score_left.game_over_left()
        game_is_on=False

screen.exitonclick()
