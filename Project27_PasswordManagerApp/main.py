"""
=============================================================
 File: main.py
 Project no. 27: The Password Manager Application
 Author: Jonathan Eduardo Castilla Zamora

 Description:
    This module implements a Graphical User Interface (GUI)
    application designed as a localized credential vault.
    Built upon the `tkinter` framework, the system features
    stochastic password generation, Operating System (OS)
    clipboard integration via the `pyperclip` library, and
    persistent data storage utilizing structured JSON
    serialization. It enforces basic input validation, employs
    modal dialogues to ensure data integrity prior to local
    commit, and includes a query mechanism to retrieve existing
    cryptographic records.
=============================================================
"""

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ----------------------- GEOMETRIC CONSTANTS -------------------------- #
# Spatial configuration parameters establishing the foundational canvas dimensions.
WIDTH = 200
HEIGHT = 200
PADDING = 50

# Dictionaries standardizing the dimensional widths of interactive UI widgets
# to maintain a cohesive graphical matrix.
WIDTH_ENTRIES = {
    "website": 26,
    "username": 45,
    "password": 26
}

WIDTH_BUTTONS = {
    "password": 15,
    "add": 38,
    "search": 15
}


# ----------------------- CRYPTOGRAPHIC MECHANISMS ----------------------- #
def generate_password():
    """
    Executes a pseudo-random generation algorithm to synthesize a robust
    alphanumeric and symbolic credential string. The resultant sequence
    is programmatically injected into the password entry field and
    simultaneously copied to the host operating system's clipboard
    for immediate deployment.
    """
    # Define the discrete character sets
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Utilize list comprehensions to extract randomized sub-samples from each set
    password_letters = [random.choice(letters) for _ in range(random.randint(4, 6))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(4, 6))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(4, 6))]

    # Concatenate the discrete lists into a singular array
    password_list = password_letters + password_symbols + password_numbers

    # Introduce entropy by shuffling the consolidated array in place
    random.shuffle(password_list)

    # Coerce the array into a contiguous scalar string
    password = "".join(password_list)

    # Mutate the UI and OS clipboard state
    entry_password.delete(0, END)  # Purge existing field data prior to insertion
    entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- DATA PERSISTENCE -------------------------- #
def save_data():
    """
    Retrieves scalar inputs from the graphical interface, validates their
    completeness, and commits the credentials to a local structured JSON
    database (`data.json`) upon explicit user confirmation via a modal dialogue.
    """
    # Acquire string values from the active entry fields
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    # Construct the nested dictionary payload for JSON serialization
    new_data = {
        website: {
            'email': username,
            'password': password
        }
    }

    # Input Validation: Prevent the commitment of null or incomplete records
    if website == "" or username == "" or password == "":
        messagebox.showerror(title="Validation Error", message="Please ensure all credential fields are filled in.")
    else:
        # Deploy a modal dialogue to explicitly verify the data packet before I/O execution
        correct_data = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {username} \nPassword: {password}\n\nIs it okay to save?"
        )

        # Execute File I/O operations strictly if user consent is explicitly granted
        if correct_data:
            try:
                # Attempt to open and deserialize the existing JSON structure
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                # If the file does not exist, initialize a new JSON file with the current payload
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                # If the file exists, mutate the loaded dictionary with the new payload
                data.update(new_data)
                # Serialize the updated dictionary back to the JSON file
                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)  # Corrected parameter: 'data' instead of 'new_data'
            finally:
                # Purge the entry fields to secure the interface for subsequent inputs
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- DATA RETRIEVAL -------------------------- #
def find_password():
    """
    Executes a localized query against the JSON database utilizing the
    provided website string as a primary key. Renders a modal dialogue
    displaying the corresponding credentials or an error notification
    if the entity is absent.
    """
    # Acquire the primary key (website) from the active entry field
    website = entry_website.get()

    try:
        # Attempt to open and deserialize the existing JSON structure
        with open('data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message="No localized database file (data.json) was found.")
    else:
        # Evaluate if the primary key exists within the loaded dictionary
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title='Error', message=f"No credential records for '{website}' currently exist.")


# ---------------------------- UI ARCHITECTURE ---------------------------- #
# 1. GUI Initialization: Constructing the Root Window
# Instantiate the primary application window and establish architectural padding.
window = Tk()
window.title("Password Manager")
window.minsize(width=WIDTH, height=HEIGHT)
window.config(padx=PADDING, pady=PADDING)

# 2. Canvas Construction
# Instantiate a Canvas widget to manage and render the primary graphical overlay (logo).
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
logo = PhotoImage(file='logo.png')
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=logo)
canvas.grid(row=0, column=1)

# 3. Typography: Instantiating Static Semantic Labels
lb_website = Label(window, text="Website:", fg="black")
lb_website.grid(row=1, column=0)

lb_username = Label(window, text="Email/Username:", fg="black")
lb_username.grid(row=2, column=0)

lb_password = Label(window, text="Password:", fg="black")
lb_password.grid(row=3, column=0)

# 4. Data Acquisition: Defining the Input Matrices (Entries)
entry_website = Entry(window, width=WIDTH_ENTRIES["website"])
entry_website.grid(row=1, column=1)
# Programmatically force keyboard focus to the first entry field upon initialization
entry_website.focus()

entry_username = Entry(window, width=WIDTH_ENTRIES["username"])
entry_username.grid(row=2, column=1, columnspan=2)
# Populate a default temporal value for rapid user execution
entry_username.insert(0, "username@gmail.com")

entry_password = Entry(window, width=WIDTH_ENTRIES["password"])
entry_password.grid(row=3, column=1)

# 5. Control Mechanisms: Actuation Buttons
search_button = Button(window, text='Search', width=WIDTH_BUTTONS["search"], command=find_password)
search_button.grid(row=1, column=2)

password_button = Button(window, text="Generate Password", width=WIDTH_BUTTONS["password"], command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(window, text="Add", width=WIDTH_BUTTONS["add"], command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

# 6. Main Execution Loop
# Invoke the continuous event-listening sequence to maintain the application instance.
window.mainloop()