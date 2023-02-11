from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=25, bg="white")

canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
img = PhotoImage(file="lock.png")
canvas.create_image(140, 140, image=img)
canvas.grid(row=0, column=1)

website = Label(text="Website:", bg="white")
website.grid(row=1, column=0)
website_input = Entry(width=67)
website_input.grid(row=1, column=1, columnspan=2)

email = Label(text="Email/Username:", bg="white")
email.grid(row=2, column=0)
email_input = Entry(width=67)
email_input.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", bg="white")
password.grid(row=3, column=0)
password_input = Entry(width=47)
password_input.grid(row=3, column=1)
generate_pwd = Button(text="Generate Password")
generate_pwd.grid(row=3, column=2)

add = Button(text="Add", width=57)
add.grid(row=4, column=1, columnspan=2)







window.mainloop()