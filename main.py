from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip

"""----------Generate Random Password--------"""
def generate_password():
    random_letter = string.ascii_letters + string.digits + "!@#$%^&*()"
    random_password = [random.choice(random_letter) for _ in range(10)]
    password = "".join(random_password)
    Entry_password.insert(0, password)
    pyperclip.copy(password)



"""-----------------Save data To txt---------"""
def save_data():
    website = Entry_website.get()
    email = Entry_email.get()
    password = Entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="There must be not an empty field")
    else:
        pop_up_confirm = messagebox.askokcancel(title=website, message=f"email : {email}\n "
                                                f"password : {password}\n Are you okay to save?")
        if pop_up_confirm:
            with open("data.txt", 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

                Entry_website.delete(0, END)
                Entry_password.delete(0, END)

"""---------------UI Setup-----------------"""

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)


# Label
Website_label = Label(text="Website:")
Website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
Password_label = Label(text="password")
Password_label.grid(column=0, row=3)


# Entry
Entry_website = Entry(width=52)
Entry_website.grid(column=1, row=1, columnspan=2)
Entry_email = Entry(width=52)
Entry_email.grid(column=1, row=2, columnspan=2)
Entry_email.insert(0, "haikaljr1245@gmail.com")
Entry_password = Entry(width=33)
Entry_password.grid(column=1, row=3)


# Button
add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

window.mainloop()