import random
import pyperclip
from tkinter import *
from tkinter import messagebox
import json

background_colour = "#A6E3E9"
LABEL_FONT = ("Arial", 10, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

    letter_count = random.randint(8, 12)
    numbers_count = random.randint(3, 5)
    symbols_count = random.randint(3, 5)
    password = ''

    for i in range(1, letter_count + 1):
        password = password + letters[random.randint(0, 51)]
    for k in range(1, numbers_count + 1):
        password = password + numbers[random.randint(0, 9)]
    for m in range(1, symbols_count + 1):
        password = password + symbols[random.randint(0, 9)]

    password_list = list(password.strip(" "))

    random.shuffle(password_list)
    final_password = ''.join(password_list)
    password_input.insert(0, final_password)
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # is_filled = messagebox.showerror(title="Incomplete Details", message="Please Fill All Fields")
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Incomplete Details", message="Please Fill All Fields")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"Email: {email} \nPassword: {password} \nIs it Ok to save ?")
        if is_ok:
            try:
                with open("data.json", 'r') as file:
                    try:
                        data = json.load(file)
                        data.update(new_data)
                    except:
                        with open("data.json", 'w') as w_file:
                            json.dump(new_data, w_file, indent=4)
                    else:
                        with open("data.json", 'w') as w_file:
                            json.dump(data, w_file, indent=4)
            except FileNotFoundError:
                with open("data.json", 'w') as file:
                    json.dump(new_data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- Searching ------------------------------- #


def search():
    search_word = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if search_word in data:
            messagebox.showinfo(title=search_word, message=f"Email : {data[search_word]['email']}\nPassword : "
                                                           f"{data[search_word]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No Entry for {search_word} Found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(pady=60, padx=30, background=background_colour)
window.title("Password Manager")
window.minsize(550, 400)
window.resizable(0, 0)
logo = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=200, highlightthickness=0, background=background_colour)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# ---------------------------- Labels ------------------------------- #

website_label = Label(text="Website:", font=LABEL_FONT, background=background_colour)
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", font=LABEL_FONT, background=background_colour)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=LABEL_FONT, background=background_colour)
password_label.grid(column=0, row=3)

# ---------------------------- Inputs ------------------------------- #

website_input = Entry(width=39, highlightthickness=0)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=39, highlightthickness=0)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "@gmail.com")

password_input = Entry(width=39, highlightthickness=0)
password_input.grid(column=1, row=3, columnspan=2)

# ---------------------------- Buttons ------------------------------- #

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password, width=15)
# generate_password_button.grid(column=2, row=3)
generate_password_button.place(x=400, y= 243)

add_button = Button(text="Add", highlightthickness=0, width=33, command=save)
# add_button.grid(column=1, row=4, columnspan=2)
add_button.place(x=115, y=285)

search_button = Button(text="Search", highlightthickness=0, width=15, command=search)
# search_button.grid(column=2, row=1)
search_button.place(x=400, y=198)

window.mainloop()
