'''
Author: Jade Aidoghie
Creation Date: 8/21/2023
'''

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, font
import random


def read_names_from_file(filename):
    ''' Function to read names from a file '''
    with open(filename, 'r') as file:
        return [line.strip().lower().capitalize() for line in file]

# Read first and last names from files
first_names = read_names_from_file('./first-names.txt')  
last_names = read_names_from_file('./last-names.txt')  


def generate_names(count, name_type):
    ''' Function to generate random names '''
    names = []
    for _ in range(count):
        first = random.choice(first_names)
        last = random.choice(last_names)
        if name_type == 1:  # First Name
            names.append(first)
        elif name_type == 2:  # Last Name
            names.append(last)
        else:  # Both
            names.append(f"{first} {last}")
    return names


def on_generate_clicked():
    ''' Function to handle the generation button click '''
    if name_type_var.get() == 0:
        output_text.config(fg='red')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.INSERT, "Select a Field")
    else:
        output_text.config(fg='black')
        output_text.delete(1.0, tk.END)  # Clear the existing text
        count = int(number_of_names.get())
        name_type = name_type_var.get()
        names = generate_names(count, name_type)
        output_text.insert(tk.INSERT, '\n'.join(names))  # Display names


def on_reset_clicked():
    ''' Function to reset the application to its initial state '''
    name_type_var.set(0)  # Clear radio button selection
    number_of_names.set(1)  # Reset dropdown to 1
    output_text.delete(1.0, tk.END)  # Clear the output area


def clear_error_message():
    ''' Function to clear the error message when a radio button is clicked '''
    if output_text.get(1.0, tk.END).strip() == "Select a Field":
        output_text.delete(1.0, tk.END)
        output_text.config(fg='black')


# Set up the main window
root = tk.Tk()
root.title("Random Name Generator")
root.configure(bg="#87AE73")

# Create and configure a style
style = ttk.Style()
style.configure("TRadiobutton", background="#87AE73", foreground="white", focuscolor=style.configure(".")["background"])

# Define font for the title
title_font = font.Font(size=14, weight='bold')

# Add title label with larger font
title_label = tk.Label(root, text="Random Name Generator", bg="#87AE73", fg="white", font=title_font)
title_label.pack(pady=10)

# Add label and dropdown for number of names
names_label = tk.Label(root, text="How many examples would you like to generate?", bg="#87AE73", fg="white")
names_label.pack(pady=10)

number_of_names = ttk.Combobox(root, values=[1, 5, 10, 15, 20, 25, 30])
number_of_names.set(1)
number_of_names.pack(pady=5)

# Add radio buttons for name type
name_type_var = tk.IntVar(value=0)
first_radio = ttk.Radiobutton(root, text="First Name", variable=name_type_var, value=1, style="TRadiobutton", command=clear_error_message)
last_radio = ttk.Radiobutton(root, text="Last Name", variable=name_type_var, value=2, style="TRadiobutton", command=clear_error_message)
both_radio = ttk.Radiobutton(root, text="Both", variable=name_type_var, value=3, style="TRadiobutton", command=clear_error_message)
first_radio.pack()
last_radio.pack()
both_radio.pack()

# Add generate button
generate_button = tk.Button(root, text="Generate", command=on_generate_clicked, bg="#A67B5B", fg="white")
generate_button.pack(pady=10)

# Add reset button
reset_button = tk.Button(root, text="Reset", command=on_reset_clicked, bg="#A67B5B", fg="white")
reset_button.pack(pady=10)

# Add a text area to display the generated names
output_text = scrolledtext.ScrolledText(root, height=10)
output_text.pack(pady=10)

root.mainloop()
