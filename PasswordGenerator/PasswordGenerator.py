import tkinter as tk  # GUI
import secrets        # Will be harder to predict than random library
import string         # Need predefined character sets
import pyperclip      # Need to copy text directly to clipboard

# ------------------
# Functions Section
# ------------------

def generate_password(length=12):
    "Function to create a password with a default length of 12."

    # Allowed characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Infinite loop until a good password is created
    while True:
        # Picking a secure character X length amount of times and combining into string
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        # Making sure at least one lowercase and one uppercase letter, one number, and one symbol
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password 

def generate():
    "Function that is triggered when the 'generate' button is clicked."
    password = generate_password() # Calling previous function
    password_var.set(password) # Updating UI  with generated password and refresh entry box
    status_var.set("")

def copy():
    "Function that is triggered when 'copy' button is clicked."

    # If password exists (not empty) then copy password to clipboard and update UI
    if password_var.get():
        pyperclip.copy(password_var.get())
        status_var.set("Copied")

# -------------
# Main Section
#--------------


root = tk.Tk()                    # Initializing main app window
root.title("Password Generator")  # Window title
root.geometry("350x200")          # Fixing window size (w x h)
root.resizable(False, False)      # No resizing since it is such a small app

# Color palette
SAGE = "#A3B18A"
LIGHT_BROWN = "#D2B48C"
DARK_TEXT = "#2F3E2F"

root.configure(bg=SAGE) # Window background

# Title on main window
title = tk.Label(root, text="Password Generator", bg=SAGE, fg=DARK_TEXT, font=("Segoe UI", 14, "bold"))
title.pack(pady=(15, 10)) # Vertical spacing

# Password display
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var,
                          font=("Consolas", 12),
                          justify="center",
                          bd=0,
                          bg="white",
                          fg=DARK_TEXT,
                          width=25)
password_entry.pack(pady=5, ipady=6)

# Buttons frame
btn_frame = tk.Frame(root, bg=SAGE)
btn_frame.pack(pady=10)

# Generate button
generate_btn = tk.Button(btn_frame, text="Generate",
                         bg=LIGHT_BROWN, fg=DARK_TEXT,
                         activebackground="#C4A484",
                         bd=0, padx=10, pady=5,
                         command=generate)
generate_btn.grid(row=0, column=0, padx=5)

# Copy Button
copy_btn = tk.Button(btn_frame, text="Copy",
                     bg=LIGHT_BROWN, fg=DARK_TEXT,
                     activebackground="#C4A484",
                     bd=0, padx=10, pady=5,
                     command=copy)
copy_btn.grid(row=0, column=1, padx=5)

# Status message
status_var = tk.StringVar()
status_label = tk.Label(root, textvariable=status_var,
                        bg=SAGE, fg=DARK_TEXT,
                        font=("Segoe UI", 9))
status_label.pack()

root.mainloop()