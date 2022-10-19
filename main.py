from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    file = open("./data.txt", "a")
    file.write(f"{website_entry.get()} | {user_entry.get()} | {password_entry.get()}\n")
    website_entry.delete(0, END)
    password_entry.delete(0, END)
    file.close()
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


generate_password_button = Button(text="Generate Password",width=17)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add", width=47, command=save)
add_button.grid(column=1,row=4,columnspan=2,sticky="W")

window.mainloop()