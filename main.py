from tkinter import *
from tkinter import messagebox as mbox
import random
import pyperclip
import json

# ---------------------------   SAVE PASSWORD --------------------------------
def save():
    website_data = website_input.get()
    email_data = email_input.get()
    password_data = password_input.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }
    if website_data == "" or email_data == "" or password_data == "":
        mbox.showerror(title="Error", message="Do not left empty!!!")
    else:
        is_ok = mbox.askokcancel(title="Check", message="Is it ok? Or do you want to change it?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)



# ---------------------------   PASSWORD GENERATOR  --------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
index = [1, 2, 3, 4, 5, 6, 7, 8, 9]

nr_letters = random.choice(index)
nr_symbols = random.choice(index)
nr_numbers = random.choice(index)

letter = ''
symbol = ''
number = ''
for x in range(nr_letters):
  letter += random.choice(letters)
for x in range(nr_symbols):
  symbol += random.choice(symbols)
for x in range(nr_numbers):
  number += random.choice(numbers)
result = letter + symbol + number
arr = []
for x in range(len(result)):
    arr.append(result[x])
random.shuffle(arr)
shuffled = ''
for x in arr:
    shuffled += x
def generate_password():
    pyperclip.copy(shuffled)
    password_input.insert(0, shuffled)

# ---------------------------   SEARCH FUNCTION  -----------------------------

def search_website():
    website = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            fetched_data = json.load(data_file)
    except FileNotFoundError:
        mbox.showerror(title="No Data", message="No data file found!!!")
    else:
        if website in fetched_data:
            mbox.showinfo(title=website, message=f"Email: ${fetched_data[website]['email']} \nPassword: ${fetched_data[website]['password']}")
        else:
            mbox.showerror(title=website, message="Website not found")

# ---------------------------   UI SETUP  ------------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=25, bg="white")

canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
img = PhotoImage(file="lock.png")
canvas.create_image(140, 140, image=img)
canvas.grid(row=0, column=1)

website = Label(text="Website:", bg="white")
website.grid(row=1, column=0)
website_input = Entry(width=47)
website_input.grid(row=1, column=1)
website_input.focus()

email = Label(text="Email/Username:", bg="white")
email.grid(row=2, column=0)
email_input = Entry(width=67)
email_input.grid(row=2, column=1, columnspan=2)

password = Label(text="Password:", bg="white")
password.grid(row=3, column=0)
password_input = Entry(width=47)
password_input.grid(row=3, column=1)
generate_pwd = Button(text="Generate Password", command=generate_password)
generate_pwd.grid(row=3, column=2)

add = Button(text="Add", width=57, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=15, command=search_website)
search.grid(row=1, column=2)

window.mainloop()