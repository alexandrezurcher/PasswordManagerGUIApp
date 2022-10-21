from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list =[random.choice(letters) for x in range(nr_letters)]
    password_list +=[random.choice(symbols) for x in range(nr_symbols)]
    password_list +=[random.choice(numbers) for x in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = user_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please, dont leave empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPasswo"
                                                              f"rd: {password} \nDo you want to proceed and save it?")
        if is_ok:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Update old data with new data
                data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

username_label = Label(text="Email/username:")
username_label.grid(column=0,row=2)

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_entry = Entry(width=55)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

user_entry = Entry(width=55)
user_entry.grid(column=1,row=2,columnspan=2)
user_entry.insert(0, "a.mourazurcher@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password", width=17, command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add", width=47, command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky="W")

window.mainloop()