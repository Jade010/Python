'''
Author: Jade Aidoghie
Creation Date: 12/15/2023
Description: This is a GUI based password generator. This will allow you to generate a password 
between 8-15 characters long that has at least one Uppercase letter, lowercase letter, and number. 
Once you generate a password you can copy it with a click of a button.
'''


import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip


def generate_password(length):
  ''' Function to generate a password of a given length. '''
    if length < 8 or length > 15:
        messagebox.showerror("Invalid Length", "Password length must be between 8 and 15 characters.")
        return ""
    
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(random.choice(characters) for i in range(length))
        if (any(c.islower() for c in password) and any(c.isupper() for c in password) 
            and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password)):
            break
    return password

def on_generate_clicked():
  ''' Function to handle the event when the "Generate Password" button is clicked. '''
    try:
        length = int(length_entry.get())
        password = generate_password(length)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def on_copy_clicked():
  ''' Function to handle the event when the "Copy to Clipboard" button is clicked. '''
    password = password_entry.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

# GUI Setup
root = tk.Tk()
root.title("Strong Password Generator")
root.configure(bg='#87AE73')  

tk.Label(root, text="Password Length:", bg='#87AE73', fg='white').pack(padx=10, pady=5)
length_entry = tk.Entry(root)
length_entry.pack(padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Password", bg='#A67B5B', fg='white', command=on_generate_clicked)
generate_button.pack(padx=10, pady=5)

password_entry = tk.Entry(root, width=30)
password_entry.pack(padx=10, pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", bg='#A67B5B', fg='white', command=on_copy_clicked)
copy_button.pack(padx=10, pady=5)

root.mainloop()
