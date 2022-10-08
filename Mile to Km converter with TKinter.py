from tkinter import *

window=Tk()
window.minsize(400,200)
window.title("Mile to Km Converter")
window.config(padx=100, pady=50, bg="lightslategray")

input=Entry(font=("Times New Roman",16,"bold"),bg="goldenrod")
input.grid(column=1, row=0)



label_miles=Label(text="Miles",font=("Times New Roman",16,"bold"), bg="goldenrod")

label_miles.grid(column=2, row=0)


label_is_equal=Label(text="is equal to>>>",font=("Times New Roman",16,"bold"), bg="lightslategray")
label_is_equal.grid(column=0, row=1)


label_km=Label(text="Km" ,font=("Times New Roman",16,"bold"), bg="crimson")
label_km.grid(column=2, row=1)

def calculate():
    mile_data=input.get()
    km_data='{:.0f}'.format(float(mile_data)*1.6, 2)
    result = Label(text=km_data, font=("Times New Roman",16,"bold"), bg="crimson")
    result.grid(column=1, row=1)





button=Button(text="Calculate" ,font=("Times New Roman",16,"bold"),bg="LightBlue", command=calculate)
button.grid(column=1, row=2)

# result=Label()
# result.config(text=c)
# result.grid(column=1, row=1)


window.mainloop()













window.mainloop()