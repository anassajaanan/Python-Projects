from turtle import Turtle
from random import choice
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("indianred3")
        self.penup()
        self.shapesize(2)
        x=choice([-1,1])
        y=choice([-1,1])
        self.dx=x
        self.dy=y
        self.speed=25
    def move_ball(self):
        self.setx(self.xcor()+(self.dx * self.speed))
        self.sety(self.ycor()+(self.dy * self.speed))
        if self.ycor()>395:
            self.sety(395)
            self.dy *= -1
        if self.ycor()<-385:
            self.sety(-385)
            self.dy *= -1

