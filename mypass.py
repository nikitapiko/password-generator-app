from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import time

default_username = "nikita.pikulenko@gmail.com"
# ------------------ PASSWORD GENERATOR ------------ #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for char in range(randint(2, 4))]
    password_numbers = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    # print(password_list)

    shuffle(password_list)

    password = "".join(password_list)

    count = 3
    countdown(count)
    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ------------------ SAVE PASSWORD ----------------- #
def countdown(count):

    countdown_label.config(text=count)
    if count > 0:
        window.after(1000, countdown, count - 1)
    if count == 0:
        countdown_label.config(text="Password generated")
        d

def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) and len(username) and len(password) != 0:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail/username: {username} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(title=website, message="Saved.")
    else:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")


# ------------------ UI SETUP ---------------------- #
# window
window = Tk()
# window.minsize(height=400, width=400)
window.title("Password Manager")
window.config(padx=50, pady=50)

# image - canvas
logo_img = PhotoImage(width=200, height=200, file="logo.png")
canvas = Canvas()
canvas.create_image(145, 120, image=logo_img)

# labels

website_label = Label(text="Website/App:")
username_label = Label(text="E-Mail/Username:")
password_label = Label(text="Password:")

countdown_label = Label()
countdown_label.grid(column=1, row=5, columnspan=2)
# entries
website_entry = Entry()
website_entry.get()
website_entry.focus()

username_entry = Entry()
username_entry.insert(0, default_username)

# password field
password_entry = Entry()
# password_field.focus()

# buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", command=save_data)

# grids
canvas.grid(column=1, row=0)


website_label.grid(column=0, row=1)
website_entry.config(width=36)
website_entry.grid(column=1, columnspan=2, row=1)


username_label.grid(column=0, row=2)
username_entry.config(width=36)
username_entry.grid(column=1, columnspan=2, row=2)


password_label.grid(column=0, row=3)
password_entry.config(width=18)
password_entry.grid(column=1, row=3)


generate_password_button.grid(column=2, row=3, columnspan=1, sticky="w")

# generate_password_button.config(width=10)



add_button.grid(column=1, row=4, columnspan=2)
add_button.config(width=34)


# i should write the mainframe for my next code
# just the pseudocode
# - the application for chess
# - analyzing photos of chess boards and replicating the positions on a virtual one using AI


window.mainloop()

