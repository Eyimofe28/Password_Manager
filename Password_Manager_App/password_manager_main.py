from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
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
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "Email": email,
        "Password": password
    }}

    if website and email and password:
        if messagebox.askokcancel(title=website, message=f"Email: {email}\n"
                                                         f"Password: {password}\n\n"
                                                         f"Are you satisfied with this info you've entered?"):
            # with open("data.txt", mode='r') as file:
            #     file.write(f"\n{website} | {email} | {password}")
            try:
                with open("data.json", mode="r") as file:
                    # Reading old data from a JSON file.
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
                    successful_save()
            else:
                if website in data:
                    if messagebox.askokcancel(message=f"You are about to replace the password for this site: {website}."
                                              f"\nWould you still like to proceed?", title='Warning ⚠️'):
                        # Appending new data to old data.
                        data.update(new_data)
                        with open('data.json', mode='w') as file:
                            # Replacing old data with new data in JSON file.
                            json.dump(data, file, indent=4)
                        successful_save()
                else:
                    data.update(new_data)
                    with open('data.json', mode='w') as file:
                        json.dump(data, file, indent=4)
                    successful_save()
    else:
        messagebox.showerror(message="Please make sure not to leave any entry field empty.", title="Oops")


def successful_save():
    messagebox.showinfo(message='Info saved :)', title='Success!')
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Sorry, no data file found.")
    else:
        website = website_entry.get().title()
        if website:
            if website in data:
                email = data[website]["Email"]
                password = data[website]["Password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(message="No details for this website found.", title="Oh No :(")
        else:
            messagebox.showerror(message="Please make sure the website entry box isn't empty and try again.")


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

website_entry = Entry(width=24)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text='Search', bg='#1A3636', fg='white', activebackground='blue', command=find_password)
search_button.grid(row=1, column=2, sticky='w')

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=10)

email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2)

email_entry.insert(END, string="default email")

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
