"""
=============================================================
 File: main.py
 Project no. 25: The Mile to Kilometers Converter Project
 Author: Jonathan Eduardo Castilla Zamora

 Description:
    This module implements a Graphical User Interface (GUI)
    application designed to perform deterministic unit
    conversions from miles to kilometers. Utilizing the Python
    standard `tkinter` library, it constructs an event-driven
    interface that captures scalar input, applies the standard
    international conversion coefficient, and dynamically
    updates the display with the computed metric equivalent.
=============================================================
"""

from tkinter import *

def miles_to_kilometers(miles: float) -> float:
    """
    Computes the metric equivalent of a distance given in miles.

    Parameters:
        miles (float): The scalar distance expressed in miles.

    Returns:
        float: The corresponding distance in kilometers,
               quantized to three decimal places.
    """
    # 1.60934 represents the exact standard conversion factor
    return round(miles * 1.60934, 3)


# 1. GUI Initialization: Constructing the root window
# Instantiate the primary application window and establish its foundational parameters.
window = Tk()
window.title('Mile to Kilometers')
window.minsize(width=400, height=50)
# Apply internal padding to establish spatial margins around the operational widgets
window.config(padx=25, pady=25)


# 2. Interface Typography: Instantiating and mapping Label widgets
# Define static labels to provide contextual semantics for the interface.
lb1 = Label(text='Miles', font=('Arial', 11))
lb1.grid(row=0, column=2)

lb2 = Label(text='is equal to', font=('Arial', 11))
lb2.grid(row=1, column=0)

lb3 = Label(text='Km', font=('Arial', 11))
lb3.grid(row=1, column=2)

# Instantiate a dynamic label allocated for displaying the computed output.
lb_result = Label(text='0', font=('Arial', 11))
lb_result.grid(row=1, column=1)


# 3. Data Acquisition: Instantiating the Entry widget
# Construct an input field to systematically capture the user's numerical data.
miles = Entry(width=15, justify='center', font=('Arial', 11))
miles.grid(row=0, column=1)


# 4. Event Handling and Execution: Defining the Button widget
def calculate_km():
    """
    Callback function triggered by the button actuation.
    Retrieves the string input, coerces it to a floating-point
    variable, computes the conversion, and mutates the state
    of the output label.
    """
    kilometers = miles_to_kilometers(float(miles.get()))
    # Reconfigure the label's text attribute to reflect the new state
    lb_result.config(text=kilometers)
    lb_result.grid(row=1, column=1)

# Bind the execution callback to a graphical button component.
calculate = Button(text='Calculate', command=calculate_km)
calculate.grid(row=2, column=1)


# 5. Main Execution Loop
# Invoke the continuous event-listening loop, suspending script termination
# until the application window is explicitly destroyed by the user.
window.mainloop()