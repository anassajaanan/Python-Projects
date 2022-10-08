from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list+= [random.choice(symbols) for _ in range(nr_symbols)]
    password_list+=[random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = ""
    for char in password_list:
      password += char
    password_entry.delete(0,END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email": email,
            "password": password,
        }
    }

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror("Missing Fields", "One of the required field is empty or contains invalid data")
        password_entry.update()

    else:
        try:
            with open("data.json",mode="r") as data_file:
                data=json.load(data_file)
        except FileNotFoundError:
            with open("data.json",mode="w") as data_file:
                json.dump(new_data, data_file,indent=4)
        else:
            data.update(new_data)
            with open("data.json",mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
#==========================search===================================#
def search_password():
    website=website_entry.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            list_websites=[key for key in data]
            if website in list_websites:
                email=data[website]["email"]
                password=data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror("error", f"No details for {website} exist.")
    except FileNotFoundError:
        messagebox.showerror("error", "No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager | Made with ❤ by Anas Ajaanan(^_^) ")
window.config(padx=100,pady=50, bg="#40D6D5")


canvas=Canvas(window, width=800, height=650, highlightthickness=0, bg="#40D6D5")
my_image=PhotoImage(file="image.png")
canvas.create_image(400, 230, image=my_image)
canvas.grid(column=1,row=0)

#=====================labels============================
website_label=Label(text="Website :", font=("Helvitica", 20, "bold"), fg= "#2C3031", bg="#40D6D5")
website_label.place(x=60, y=450)
email_label=Label(text="Email/Username:", font=("Helvitica", 20, "bold"), fg= "#2C3031", bg="#40D6D5")
email_label.place(x=20, y=500)
password_label=Label(text="Password :", font=("Helvitica", 20, "bold"), fg= "#2C3031", bg="#40D6D5")
password_label.place(x=60,y=550)
#=====================entries==========================
website_entry=Entry( bd=0, bg="#F73C57", font=("Arial", 18, "bold"),width=22, fg="white")
website_entry.place(x=300,y=450)
website_entry.focus()
email_entry=Entry(bd=0 , bg="#F73C57", font=("arial", 18, "bold"),width=40, fg="white")
email_entry.place(x=300,y=500)
password_entry=Entry(bd=0 , bg="#F73C57", font=("Arial", 18, "bold"),width=22, fg="white")
password_entry.place(x=300,y=550)


#==================button=============================
generate_button=Button(text="Generate Password", bg="#FECD01", fg="black",bd=0,width=15,height=0,font=("Arial", 16, "bold"),padx=0,pady=0, command=generate_password)
generate_button.place(x=625, y=547)
add_button=Button(text="Add", bg="#FECD01", fg="black",bd=0,width=43,height=0,font=("Arial", 14, "bold"),padx=0,pady=0,command=save_password)
add_button.place(x=300, y=600)
search_button=Button(text="Search", bg="#FECD01", fg="black",bd=0,width=15,height=0,font=("Arial", 16, "bold"),padx=0,pady=0, command=search_password)
search_button.place(x=625  ,y=448)

# label=Label(text=" Made with ❤ by Anas Ajaanan ",bg="#40D6D5", fg="white",font=("Helvitica", 12, "bold") )
# label.place(x=0, y=675)





window.mainloop()

