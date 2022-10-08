from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.heading()
        self.pensize(5)
        self.color("white")
        self.speed(-1)
        self.goto(0,440)
        self.setheading(270)
        for i in range(19):
            self.forward(15)
            self.penup()
            self.forward(30)
            self.pendown()
        self.hideturtle()
