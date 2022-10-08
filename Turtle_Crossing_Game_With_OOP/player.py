STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def player_move(self):
        self.forward(MOVE_DISTANCE)

    def cheak_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
    def restart_game(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


