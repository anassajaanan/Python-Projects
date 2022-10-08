from tkinter import *
import customtkinter
import math
import pygame
from tkinter import ttk



# ---------------------------- CONSTANTS ------------------------------- #

WORK_MIN = 45
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repition=0
counter=1
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label.config(text="" )
    check_mark_label.config(text="" )
    canvas.itemconfig(time_text, text="00:00")
    global repition
    repition=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repition
    repition+=1
    if repition % 2 != 0:
        time_count_down(WORK_MIN * 60)
        label.config(text="Work Session🎓")
    elif repition % 2 ==0 and repition % 8!=0:
        global counter
        time_count_down(SHORT_BREAK_MIN * 60)
        check_mark_label.config(text="✓" * counter, fg="#13913F")
        label.config(text="Short Break👏🏻")
        counter+=1
    else:
        time_count_down(LONG_BREAK_MIN * 60)
        check_mark_label.config(text="✓" * 4,fg="#EB1D36" )
        label.config(text="Long Break😇")
        repition=0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def time_count_down(time):
    global timer
    num_min=math.floor(time/60)
    num_sec=math.floor(time%60)
    if num_min>9:
        if num_sec>9:
            canvas.itemconfig(time_text, text= f"{num_min}:{num_sec}")
        else:
            canvas.itemconfig(time_text, text=f"{num_min}:0{num_sec}")
    else:
        if num_sec > 9:
            canvas.itemconfig(time_text, text=f"0{num_min}:{num_sec}")
        else:
            canvas.itemconfig(time_text, text=f"0{num_min}:0{num_sec}")
    if time>0:
        timer=window.after(1000, time_count_down, time-1)
    if time==0:
        pygame.mixer.music.load("music.wav")
        pygame.mixer.music.play(loops=0)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro Timer")
window.config(padx=100,pady=50, bg="#F5EDDC")

canvas=Canvas(width=978, height=548, highlightthickness=0)
my_image=PhotoImage(file="Pomodoro_timer.png")
canvas.create_image(489, 274, image=my_image)
time_text=canvas.create_text(520, 250,text="00:00", font=("calibri", 45, "bold"), fill="#F6E3C5")
canvas.grid(column=1,row=1)

pygame.mixer.init()

b1=ttk.Button(master=window, text="Start", command=start_timer)
b1.grid(column=0,row=2)
b1.invoke()

customtkinter.set_appearance_mode("System")
start_button=customtkinter.CTkButton(master=window, text="Start", fg_color="#EB1D36",hover_color="#13913F", text_font=("calibri", 30, "bold"), command=start_timer)
start_button.grid(column=0,row=2)
reset_button=customtkinter.CTkButton(master=window, text="Reset", fg_color="#EB1D36",hover_color="#13913F", text_font=("calibri", 30, "bold"), command=reset)
reset_button.grid(column=2,row=2)


label = Label(text="", font=("Times New Roman", 65, "bold"), fg="#13913F",bg="#F5EDDC")
label.grid(column=1, row=0)
check_mark_label=Label(text="", font=("Arial", 45, "bold"), fg="#13913F",bg="#F5EDDC")
check_mark_label.grid(column=1,row=2)




window.mainloop()