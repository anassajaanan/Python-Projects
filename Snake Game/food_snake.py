from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(-1)
        self.color("red")
        self.penup()
        self.shapesize(0.5,0.5)


    def generate(self):
        self.goto(randint(-280,280),randint(-280,280))


