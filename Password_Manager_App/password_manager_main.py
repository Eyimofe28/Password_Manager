from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    generated_password = "".join(password_list)
    pyperclip.copy(generated_password)
    password_entry.delete(0, END)
    password_entry.insert(END, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if website and email and password:
        if messagebox.askokcancel(title=website, message=f"Email: {email}\n"
                                                         f"Password: {password}\n\n"
                                                         f"Are you satisfied with this info you've entered?"):
            with open("data.txt", mode='a') as file:
                file.write(f"\n{website} | {email} | {password}")

            messagebox.showinfo(message='Info saved🤩', title='Success!')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showerror(message="Please make sure not to leave any entry field empty.", title="Oops")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.resizable(width=False, height=False)
window.config(padx=50, pady=30, bg='#91DDCF')

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=15)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = Entry(width=42)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=10)

email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2)

email_entry.insert(END, string="eyimofeajagunna@gmail.com")

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

password_button = Button(text='Generate Password', fg='white', bg='#32cd32', command=generate_password)
password_button.grid(row=3, column=2, sticky='w')

add_button = Button(text='Save Info!', width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

note = Label(text="Note: Generated passwords are automatically saved to your clipboard! ✨")
note.grid(row=5, column=0, columnspan=12, pady=15)

window.mainloop()
