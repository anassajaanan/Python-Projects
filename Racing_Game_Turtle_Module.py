from turtle import Turtle,Screen
from random import randint


tim1=Turtle()
screen=Screen()
screen.setup(500,400)
user_guess=screen.textinput("Make your bet", " Wich turtle will win ? Enter A color ")

tim1.shape("turtle")
tim1.color("red")
tim1.penup()
tim1.setposition(-240,-100)


tim2=Turtle()
tim2.shape("turtle")
tim2.color("blue")
tim2.penup()
tim2.goto(-240,-60)

tim3=Turtle()
tim3.shape("turtle")
tim3.color("pink")
tim3.penup()
tim3.goto(-240,-20)

tim4=Turtle()
tim4.shape("turtle")
tim4.color("yellow")
tim4.penup()
tim4.goto(-240,20)

tim5=Turtle()
tim5.shape("turtle")
tim5.color("green")
tim5.penup()
tim5.goto(-240,60)
list_turtles=[tim1,tim2,tim3,tim4,tim5]
is_race_on=True
while is_race_on :
    for turtle in list_turtles:
        if turtle.xcor()>230:
            winner_turtle=turtle.pencolor()
            if winner_turtle==user_guess:
                print("You wone!!")
                print(f"the winner is the turtle {winner_turtle}")
                is_race_on=False
            else:
                print("you lost!!!")
                print(f"the winner is the turtle {winner_turtle}")
                is_race_on=False
        turtle.forward(randint(0,10))





screen.exitonclick()







