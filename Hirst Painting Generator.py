import turtle
from turtle import Turtle,Screen
from random import choice

list_colors=[(239, 234, 226), (220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61), (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47), (152, 207, 217), (8, 93, 113), (184, 185, 208), (74, 72, 37)]
turtle.colormode(255)
tim=Turtle()
tim.speed("fastest")
my_scrren=Screen()
my_scrren.screensize(800,400)
color=choice(list_colors)
tim.hideturtle()
tim.penup()
tim.goto(-300, -250)
tim.showturtle()
height=-250
for n in range(10):
    for i in range(10):
        color = choice(list_colors)
        tim.forward(60)
        tim.dot(30,color)
    height+=60
    tim.goto(-300,height)
tim.hideturtle()

my_scrren.exitonclick()
