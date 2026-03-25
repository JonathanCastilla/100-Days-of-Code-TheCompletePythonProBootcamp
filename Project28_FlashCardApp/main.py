"""
=============================================================
 File: main.py
 Project no. 28: The Flashcard Application
 Author: Jonathan Eduardo Castilla Zamora

 Description:
    This module implements a Graphical User Interface (GUI)
    application designed to facilitate cognitive retention and
    language acquisition via spatial repetition. Built upon the
    `tkinter` framework and utilizing `pandas` for tabular data
    manipulation, the system presents bilingual flashcards.
    It incorporates non-blocking temporal callbacks to flip
    cards automatically and dynamically mutates a localized
    dataset to track the user's learning progress by filtering
    out acquired vocabulary.
=============================================================
"""

from tkinter import *
import pandas as pd
from random import choice

# ----------------------- ARCHITECTURAL CONSTANTS -------------------------- #
# Spatial configuration parameters establishing foundational canvas dimensions.
WIDTH = {
    'window': 800,
    'card front': 800,
    'card back': 600,
}

HEIGHT = {
    'window': 525,
    'card front': 525,
    'card back': 600,
}

PADDING = {
    'x': 50,
    'y': 50
}

# Typographic matrices to maintain a cohesive visual hierarchy.
FONTS = {
    'language': ('Arial', 40, 'italic'),
    'word': ('Arial', 60, 'bold'),
}

# Cartesian coordinates for dynamic text rendering on the canvas.
lb_coordinates = {
    'language': (400, 150),
    'word': (400, 263),
}

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------- DATA INGESTION PIPELINE -------------------------- #
# Initialize global state variables
to_learn = []
selected_word = {}

try:
    # Attempt to ingest the mutated dataset containing unlearned vocabulary
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    # Fallback: Ingest the primary dataset if no historical progress exists
    original_data = pd.read_csv('data/french_words.csv') # Corrected from pd.DataFrame()
    to_learn = original_data.to_dict(orient='records')
else:
    # Coerce the DataFrame into a list of standardized dictionary records
    to_learn = data.to_dict(orient='records')


# ----------------------- STATE & TEMPORAL MANAGEMENT ---------------------- #
def next_card():
    """
    Selects a stochastic data pair from the unlearned vocabulary matrix,
    updates the graphical canvas to display the target language (French),
    and initiates a non-blocking temporal callback to reveal the translation.
    """
    global selected_word, flip_timer

    # Interrupt any pre-existing asynchronous flip sequences to prevent overlapping events
    window.after_cancel(flip_timer)

    # Extract a random entity reference directly from the active list
    selected_word = choice(to_learn)

    # Mutate the Canvas text objects to reflect the newly acquired state
    canvas.itemconfigure(lb_language, text='French', fill='black')
    canvas.itemconfigure(lb_word, text=selected_word['French'], fill='black')
    canvas.itemconfigure(card_background, image=card_front_image)

    # Schedule the subsequent state mutation (card flip) asynchronously after 3000 milliseconds
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """
    Executes the visual inversion of the flashcard, mutating the canvas
    background asset and typography to reveal the native translation (English).
    """
    canvas.itemconfigure(lb_language, text='English', fill='white')
    canvas.itemconfigure(lb_word, text=selected_word['English'], fill='white')
    canvas.itemconfigure(card_background, image=card_back_image)

def is_known():
    """
    Acts as an affirmative callback sequence. Purges the currently evaluated
    vocabulary item from the active memory matrix and serializes the updated
    dataset to disk to ensure progressive learning continuity.
    """
    # Purge the acquired entity from the active matrix
    to_learn.remove(selected_word)

    # Serialize the mutated dataset back into persistent CSV format
    pd.DataFrame(to_learn).to_csv('data/words_to_learn.csv', index=False)

    # Advance the discrete state machine to the subsequent entity
    next_card()

# ---------------------------- UI ARCHITECTURE ---------------------------- #
# 1. GUI Initialization: Constructing the Root Window
window = Tk()
window.title("Flash Card App")
window.configure(background=BACKGROUND_COLOR, padx=PADDING['x'], pady=PADDING['y'])
window.minsize(width=WIDTH['window'], height=HEIGHT['window'])

# Initialize a foundational temporal variable to anchor subsequent cancellations
flip_timer = window.after(3000, func=flip_card)

# 2. Canvas Construction
# Instantiate a Canvas widget to manage overlapping graphical assets and typographic layers.
canvas = Canvas(window, width=WIDTH['card front'], height=HEIGHT['card front'], background=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file='images/card_front.png')
card_back_image = PhotoImage(file='images/card_back.png')

card_background = canvas.create_image(WIDTH['card front'] / 2, HEIGHT['card front'] / 2, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

lb_language = canvas.create_text(lb_coordinates['language'][0], lb_coordinates['language'][1], text='Title', font=FONTS['language'])
lb_word = canvas.create_text(lb_coordinates['word'][0], lb_coordinates['word'][1], text='Word', font=FONTS['word'])

# 3. Control Mechanisms: Actuation Buttons
wrong_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Initialize the primary execution pipeline by calling the first data pair
next_card()

# 4. Main Execution Loop
window.mainloop()