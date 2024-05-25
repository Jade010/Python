'''
Name Generator Application
Author: Jade Aidoghie
Date: 3/3/24

This is an updated and modernized version of an older project I worked on. It includes updated aesthetics using customtkiner
as well as more features for filtering names. A text file is used for last names while a cleaned dataset is used for first 
names so the can be filtered by gender.

'''


import customtkinter as ctk
import random
import pandas as pd


def read_names_from_file(filename):
    ''' Function to read names from a file '''
    with open(filename, 'r') as file:
        return [line.strip().lower().capitalize() for line in file]

def read_names_with_gender(filename):
    ''' Function to read names and gender from CSV file '''
    df = pd.read_csv(filename)
    female_names = df[df['Gender'] == 'F']['Name'].str.capitalize().tolist()
    male_names = df[df['Gender'] == 'M']['Name'].str.capitalize().tolist()
    return female_names, male_names

# Reading first and last names from files
first_names_female, first_names_male = read_names_with_gender('./cleaned_names.csv')  
last_names = read_names_from_file('./last-names.txt')  


def generate_names(count, name_type, gender, first_letter_first, first_letter_last):
    ''' Function to generate random names '''
    if name_type == 3:  # Both names
        filtered_first_names_female = [name for name in first_names_female if first_letter_first == "Default" or name.startswith(first_letter_first)]
        filtered_first_names_male = [name for name in first_names_male if first_letter_first == "Default" or name.startswith(first_letter_first)]
        filtered_last_names = [name for name in last_names if first_letter_last == "Default" or name.startswith(first_letter_last)]
    else:  # First Name or Last Name
        filtered_first_names_female = [name for name in first_names_female if first_letter_first == "Default" or name.startswith(first_letter_first)]
        filtered_first_names_male = [name for name in first_names_male if first_letter_first == "Default" or name.startswith(first_letter_first)]
        filtered_last_names = [name for name in last_names if first_letter_first == "Default" or name.startswith(first_letter_first)]

    names = []
    for _ in range(count):
        if gender == "Female":
            first = random.choice(filtered_first_names_female)
        elif gender == "Male":
            first = random.choice(filtered_first_names_male)
        else:
            first = random.choice(filtered_first_names_female + filtered_first_names_male)
        last = random.choice(filtered_last_names)
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
        output_text.configure(fg_color=("gray75", "gray25"))
        output_text.delete("1.0", ctk.END)
        output_text.insert(ctk.INSERT, "Select a Field")
    else:
        output_text.configure(fg_color=("white", "gray15"))
        output_text.delete("1.0", ctk.END)  # Clearing the existing text
        count = int(number_of_names.get())
        name_type = name_type_var.get()
        gender = gender_var.get()
        if name_type == 3:  # Both
            first_letter_first = first_letter_first_var.get()
            first_letter_last = first_letter_last_var.get()
        else:
            first_letter_first = first_letter_var.get()
            first_letter_last = "Default"
        names = generate_names(count, name_type, gender, first_letter_first, first_letter_last)
        output_text.insert(ctk.INSERT, '\n'.join(names))  # Displaying names


def on_reset_clicked():
    ''' Function to reset the application to its initial state '''
    name_type_var.set(3)  # Reset type selection to Both
    number_of_names.set("1")  # Reset dropdown to 1
    gender_var.set("Both")  # Reset gender selection to Both
    first_letter_var.set("Default")  # Reset first letter selection to Default
    first_letter_first_var.set("Default")  # Reset first letter first name selection to Default
    first_letter_last_var.set("Default")  # Reset first letter last name selection to Default
    show_both_letters()  # Show both letters dropdowns for default state
    output_text.delete("1.0", ctk.END)  # Clear the output area


def show_both_letters():
    ''' Function to show the two dropdowns for both first and last name letters '''
    first_letter_frame.pack_forget()
    first_letter_both_frame.pack(pady=10, after=gender_frame)

def show_single_letter():
    ''' Function to show the single dropdown for first or last name letter '''
    first_letter_both_frame.pack_forget()
    first_letter_frame.pack(pady=10, after=gender_frame)


def on_name_type_changed():
    ''' Function to handle the name type radio button change '''
    if name_type_var.get() == 3:  # Both
        show_both_letters()
    else:
        show_single_letter()


# Setting up the main window
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

root = ctk.CTk()
root.title("Random Name Generator")
root.geometry("500x600")

# Defining font for the title
title_font = ctk.CTkFont(size=20, weight="bold")

# Adding title label with larger font
title_label = ctk.CTkLabel(root, text="Random Name Generator", font=title_font)
title_label.pack(pady=20)

# Adding radio buttons for name type
name_type_var = ctk.IntVar(value=3)
radio_frame = ctk.CTkFrame(root, height=50)
radio_frame.pack(pady=10)
type_label = ctk.CTkLabel(radio_frame, text="Type:")
type_label.pack(side="left", padx=5)
first_radio = ctk.CTkRadioButton(radio_frame, text="First Name", variable=name_type_var, value=1, command=on_name_type_changed)
last_radio = ctk.CTkRadioButton(radio_frame, text="Last Name", variable=name_type_var, value=2, command=on_name_type_changed)
both_radio = ctk.CTkRadioButton(radio_frame, text="Both", variable=name_type_var, value=3, command=on_name_type_changed)
first_radio.pack(side="left", padx=5)
last_radio.pack(side="left", padx=5)
both_radio.pack(side="left", padx=5)

# Adding radio buttons for gender
gender_var = ctk.StringVar(value="Both")
gender_frame = ctk.CTkFrame(root, height=50)
gender_frame.pack(pady=10)
gender_label = ctk.CTkLabel(gender_frame, text="Gender:")
gender_label.pack(side="left", padx=5)
gender_female_radio = ctk.CTkRadioButton(gender_frame, text="Feminine", variable=gender_var, value="Female")
gender_male_radio = ctk.CTkRadioButton(gender_frame, text="Masculine", variable=gender_var, value="Male")
gender_both_radio = ctk.CTkRadioButton(gender_frame, text="Both", variable=gender_var, value="Both")
gender_female_radio.pack(side="left", padx=5)
gender_male_radio.pack(side="left", padx=5)
gender_both_radio.pack(side="left", padx=5)

# Adding filter for first letter (single)
first_letter_var = ctk.StringVar(value="Default")
first_letter_frame = ctk.CTkFrame(root, height=50)
first_letter_label = ctk.CTkLabel(first_letter_frame, text="First Letter:")
first_letter_label.pack(side="left", padx=5)
first_letter_combobox = ctk.CTkComboBox(first_letter_frame, values=["Default"] + [chr(i) for i in range(65, 91)], variable=first_letter_var)
first_letter_combobox.pack(side="left", padx=5)

# Adding filters for first letters (both)
first_letter_both_frame = ctk.CTkFrame(root, height=100)
first_letter_first_var = ctk.StringVar(value="Default")
first_letter_last_var = ctk.StringVar(value="Default")
first_letter_first_label = ctk.CTkLabel(first_letter_both_frame, text="First Letter First Name:")
first_letter_first_label.pack(side="top", anchor="w", padx=5)
first_letter_first_combobox = ctk.CTkComboBox(first_letter_both_frame, values=["Default"] + [chr(i) for i in range(65, 91)], variable=first_letter_first_var)
first_letter_first_combobox.pack(side="top", padx=5, pady=5)
first_letter_last_label = ctk.CTkLabel(first_letter_both_frame, text="First Letter Last Name:")
first_letter_last_label.pack(side="top", anchor="w", padx=5)
first_letter_last_combobox = ctk.CTkComboBox(first_letter_both_frame, values=["Default"] + [chr(i) for i in range(65, 91)], variable=first_letter_last_var)
first_letter_last_combobox.pack(side="top", padx=5, pady=5)

# Initially show both letters dropdowns for the default state (both names)
first_letter_both_frame.pack(pady=10, after=gender_frame)

# Add label and dropdown for number of names
names_frame = ctk.CTkFrame(root, height=50)
names_frame.pack(pady=10)
names_label = ctk.CTkLabel(names_frame, text="Samples:")
names_label.pack(side="left", padx=5)
number_of_names = ctk.CTkComboBox(names_frame, values=["1", "5", "10", "15", "20", "25", "30"])
number_of_names.set("1")
number_of_names.pack(side="left", padx=5)

# Adding buttons
button_frame = ctk.CTkFrame(root, height=50)
button_frame.pack(pady=10)
generate_button = ctk.CTkButton(button_frame, text="Generate", command=on_generate_clicked)
generate_button.pack(side="left", padx=5)
reset_button = ctk.CTkButton(button_frame, text="Reset", command=on_reset_clicked)
reset_button.pack(side="left", padx=5)

# Adding a text area to display the generated names
output_text = ctk.CTkTextbox(root, height=100)
output_text.pack(pady=10, padx=20, fill=ctk.BOTH, expand=True)

root.mainloop()