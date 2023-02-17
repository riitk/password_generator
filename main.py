import random
import pyperclip
from tkinter import *
from tkinter import messagebox
background_colour = "#A6E3E9"
LABEL_FONT = ("Arial", 10, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '+']

    letter_count = random.randint(8, 12)
    numbers_count = random.randint(3, 5)
    symbols_count = random.randint(3, 5)
    password = ''

    for i in range(1, letter_count+1):
        password = password+letters[random.randint(0, 51)]
    for k in range(1, numbers_count+1):
        password = password+numbers[random.randint(0, 9)]
    for l in range(1, symbols_count + 1):
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

    # is_filled = messagebox.showerror(title="Incomplete Details", message="Please Fill All Fields")
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Incomplete Details", message="Please Fill All Fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email} \nPassword: {password} \n Is it Ok to save ?")
        if is_ok:
            with open("data.txt", 'a') as file :
                file.writelines(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(pady=70, padx=70, background=background_colour)
window.title("Password Manager")
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

password_input = Entry(width=21, highlightthickness=0)
password_input.grid(column=1, row=3, columnspan=1)

# ---------------------------- Buttons ------------------------------- #

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
