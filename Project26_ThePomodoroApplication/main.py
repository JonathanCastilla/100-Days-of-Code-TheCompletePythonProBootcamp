"""
=============================================================
 File: main.py
 Project no. 26: The Pomodoro Application
 Author: Jonathan Eduardo Castilla Zamora

 Description:
    This module implements a Graphical User Interface (GUI)
    application that facilitates the Pomodoro time-management
    methodology. Built upon the `tkinter` framework, the system
    utilizes a discrete state machine and non-blocking recursive
    callbacks to alternate between focused work intervals and
    rest periods. It features dynamic visual feedback, tracking
    completed cycles via symbolic checkmarks and semantic color
    shifts to optimize user productivity and cognitive pacing.
=============================================================
"""

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
# Lexicon of hexadecimal color codes and typographic parameters
# utilized to maintain a cohesive visual hierarchy.
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

# Temporal Configuration (defined natively in minutes)
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Operational Temporal Variables
WORK_SEC = WORK_MIN * 60
SHORT_BREAK_SEC = SHORT_BREAK_MIN * 60
LONG_BREAK_SEC = LONG_BREAK_MIN * 60

# Spatial and Typographic Constraints for UI Components
WIDTH = 200
HEIGHT = 224
PADDING = 50
FONT = (FONT_NAME, 24, "bold")
CHECKMARK_FONT = ("Arial", 12)
TITLE_FONT = ("Times New Roman", 20, "bold")
BUTTON_FONT = ("Times New Roman", 10, "bold")

# -------------------------- STATE VARIABLES --------------------------- #
# Global variables required to maintain execution context across asynchronous callbacks.
LB_CHECKMARK_TEXT = ''
repetitions = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Interrupts the active asynchronous countdown sequence and restores
    the application to its initial state. Resets iteration counters,
    clears visual tracking indicators, and normalizes typography.
    """
    global repetitions
    global LB_CHECKMARK_TEXT

    # 1. Halt the active non-blocking tkinter loop
    window.after_cancel(timer)

    # 2. Reinitialize state variables
    repetitions = 0
    LB_CHECKMARK_TEXT = ''

    # 3. Restore default graphical configurations
    lb_title.configure(text="Timer", font=TITLE_FONT, fg=GREEN, bg=YELLOW)
    lb_checkmark.configure(text="", font=CHECKMARK_FONT, fg=GREEN, bg=YELLOW)
    canvas.itemconfigure(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """
    Advances the discrete state machine governing the Pomodoro cycles.
    Evaluates the current repetition count via modulo arithmetic to
    dictate and initiate the subsequent temporal phase (Work, Short Break,
    or Long Break), simultaneously updating the semantic UI elements.
    """
    global repetitions
    repetitions += 1

    # Evaluate phase transitions based on iterative modulo logic
    if repetitions % 2 == 0:
        # Every 8th cycle corresponds to a prolonged cognitive rest period
        if repetitions == 8:
            lb_title.configure(text="Break! 😴💤", font=TITLE_FONT, fg=RED, bg=YELLOW)
            count_down(LONG_BREAK_SEC)
        # Standard even cycles correspond to brief rest periods
        else:
            lb_title.configure(text="Break! 😴💤", font=TITLE_FONT, fg=PINK, bg=YELLOW)
            count_down(SHORT_BREAK_SEC)

    # Odd cycles invariably correspond to focused work intervals
    elif repetitions % 2 == 1:
        lb_title.configure(text="Work! 😊🛠", font=TITLE_FONT, fg=GREEN, bg=YELLOW)
        count_down(WORK_SEC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count: int):
    """
    Executes a recursive, non-blocking temporal countdown utilizing
    the tkinter event loop.

    Parameters:
        count (int): The residual temporal duration in seconds.
    """
    # Compute the discrete minute and second components via integer division and modulo
    count_min = count // 60
    count_sec = count % 60

    # Type coercion and zero-padding to maintain standard digital chronometer syntax (MM:SS)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    # Mutate the Canvas text object to reflect the current temporal state
    canvas.itemconfigure(timer_text, text=f"{count_min}:{count_sec}")

    # Recursive spatial evaluation
    if count > 0:
        global timer
        # Schedule the subsequent decrement to execute asynchronously after 1000 milliseconds
        timer = window.after(1000, count_down, count - 1)
    else:
        # Upon interval exhaustion, auto-advance the state machine
        start_timer()

        # Append a completion discrete token (checkmark) after every completed work interval
        if repetitions % 4 == 1:
            global LB_CHECKMARK_TEXT
            LB_CHECKMARK_TEXT += '✅'
            lb_checkmark.configure(text=LB_CHECKMARK_TEXT, font=CHECKMARK_FONT, fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
# 1. GUI Initialization: Constructing the Root Window
# Instantiate the primary application window and establish architectural padding.
window = Tk()
window.title('Pomodoro')
window.configure(padx=PADDING, pady=PADDING, bg=YELLOW)

# 2. Canvas Construction
# Instantiate a Canvas widget to manage complex graphical overlays (image and text).
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(WIDTH / 2, HEIGHT / 2, image=tomato_image)
timer_text = canvas.create_text(WIDTH / 2, HEIGHT / 2, fill="white", text="00:00", font=FONT)
canvas.grid(row=2, column=2)

# 3. Typography and Feedback Labels
# -- TITLE LABEL: Provides semantic context for the current operational phase.
lb_title = Label(window, text="Timer", font=TITLE_FONT, fg=GREEN, bg=YELLOW)
lb_title.grid(row=1, column=2)

# -- CHECKMARK LABEL: Visually tracks completed Pomodoro cycles.
lb_checkmark = Label(window, font=CHECKMARK_FONT, fg=GREEN, bg=YELLOW)
lb_checkmark.grid(row=4, column=2)

# 4. Control Mechanisms: Actuation Buttons
# Bind execution callbacks to interactive graphical components.
start_button = Button(window, text="Start", font=BUTTON_FONT, fg=YELLOW, bg=GREEN, highlightthickness=0,
                      command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(window, text="Reset", font=BUTTON_FONT, fg=YELLOW, bg=GREEN, highlightthickness=0,
                      command=reset_timer)
reset_button.grid(row=3, column=3)

# 5. Main Execution Loop
# Invoke the continuous event-listening sequence to maintain the application instance.
window.mainloop()