import turtle
from turtle import Screen,Turtle
from random import randint,choice
list=[0,90,180,270]
turtle.colormode(255)
tim=Turtle()
tim.pensize(5)
tim.speed("fast")
for i in range(200):
    direction=choice(list)
    tim.color(randint(0,255),randint(0,255),randint(0,255))
    tim.forward(40)
    tim.right(direction)



my_screen=Screen()
my_screen.exitonclick()
