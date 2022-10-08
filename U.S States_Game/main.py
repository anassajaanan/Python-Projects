import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S states game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


states=pandas.read_csv("50_states.csv")
state_names=states["state"].to_list()
state_x=states["x"].to_list()
state_y=states["y"].to_list()

correct_answers=0
guessed_answers=[]
while correct_answers<50:

    gues = screen.textinput(f"{correct_answers}/50 States Correct", "add a new state ").title()
    if gues=="Exit":
        states_to_learn = [name for name in state_names if name not in guessed_answers]
        learn_states = pandas.DataFrame(states_to_learn, columns=["state"])
        learn_states.to_csv("states_to_learn.csv")
        break

    if gues in state_names:

        new_state=turtle.Turtle()
        new_state.penup()
        new_state.hideturtle()
        index=state_names.index(gues)
        new_x=state_x[index]
        new_y=state_y[index]
        new_state.goto(new_x, new_y)
        new_state.write(gues, False , "center" ,("Arial", 10, "normal"))
        guessed_answers.append(gues)
        correct_answers += 1

