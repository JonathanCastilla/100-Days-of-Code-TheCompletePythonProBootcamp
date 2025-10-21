"""
Project Number: 17
Project Name: The Damien Hirst’s Dots Painting Program
Description:
    This program generates a graphical composition inspired by Damien Hirst’s dot paintings.
    It employs the Turtle Graphics library to draw a grid of colorful dots whose colors
    are automatically extracted from a reference image using the Colorgram library.

    The program demonstrates modular and structured programming practices through the
    encapsulation of the painting logic into a dedicated function, and the use of
    extracted RGB color data for artistic replication. It leverages randomness to
    introduce color variability within the painting.

    Key Features:
    - Automatic color extraction from an input image using the Colorgram library.
    - Construction of a grid-based dot composition using the Turtle module.
    - Adjustable parameters for grid size, spacing, and dot dimensions.
    - Random color selection for visual variety within the defined palette.
    - Automatic window management and graceful termination upon user interaction.

    This implementation reflects computational art principles and demonstrates
    fundamental computer graphics programming using Python’s Turtle module.

Author: Jonathan Eduardo Castilla Zamora
"""

# Import required libraries
import colorgram          # Used for color extraction from the input image
from turtle import Turtle, Screen  # Turtle graphics for drawing the dot pattern
import random             # Randomization for color selection

def hirst_dot_painting(rows, columns, dot_colors, dots_size,
                       horizontal_space_between_dots, vertical_space_between_dots,
                       x_begin):
    """
    Draws a grid of colored dots inspired by Damien Hirst’s dot paintings.

    Parameters:
        rows (int): Number of rows in the grid.
        columns (int): Number of columns in the grid.
        dot_colors (list): List of RGB tuples representing available dot colors.
        dots_size (int): Diameter of each dot in pixels.
        horizontal_space_between_dots (int): Horizontal distance between consecutive dots.
        vertical_space_between_dots (int): Vertical distance between consecutive dot rows.
        x_begin (int): Initial x-coordinate from which the drawing begins.

    Description:
        The function uses a nested loop to construct the grid, positioning the
        turtle cursor in a systematic manner to maintain spacing consistency.
        For each grid position, a dot is drawn with a randomly chosen color
        from the extracted color palette.
    """
    turtle.pendown()
    for row in range(rows):
        for col in range(columns):
            turtle.dot(dots_size, random.choice(dot_colors))  # Draws a colored dot
            turtle.penup()
            turtle.forward(horizontal_space_between_dots)      # Moves horizontally
        turtle.setx(x_begin)                                  # Resets X position
        turtle.setheading(90)                                 # Turns upward
        turtle.forward(vertical_space_between_dots)           # Moves up to next row
        turtle.setheading(0)                                  # Resets orientation to the right


# --- Step 1: Color Extraction ---
# Extracts dominant colors from the input image while excluding near-white tones
number_of_colors = 20
colors = colorgram.extract(f='DamienHirstDotsPainting.jpg', number_of_colors=number_of_colors)

list_of_colors_in_painting = []
for color in colors:
    # Filters out light colors (near white) to maintain contrast
    if color.rgb.r < 245 and color.rgb.g < 245 and color.rgb.b < 245:
        list_of_colors_in_painting.append(tuple(color.rgb))

# print(list_of_colors_in_painting)  # Displays the extracted RGB color palette


# --- Step 2: Turtle Graphics Configuration ---
turtle = Turtle()
screen = Screen()

# Configure the screen properties
screen.colormode(255)             # Allows full RGB color mode
screen.setup(width=800, height=800)  # Defines window dimensions
screen.bgcolor('white')           # Sets background color
screen.title("The Hirst Painting") # Sets window title

turtle.penup()
x_begin = -220   # Initial X coordinate for painting start
y_begin = -220   # Initial Y coordinate
turtle.goto(x=x_begin, y=y_begin)  # Moves turtle to the initial position

# --- Step 3: Grid Parameters ---
rows = 10                      # Number of dot rows
cols = rows                    # Number of dot columns (square grid)
dots_size = 20                 # Diameter of each dot
horizontal_space = 50          # Horizontal spacing between dots
vertical_space = 50            # Vertical spacing between rows

# --- Step 4: Function Call to Generate Painting ---
hirst_dot_painting(
    rows=rows,
    columns=cols,
    dot_colors=list_of_colors_in_painting,
    dots_size=dots_size,
    horizontal_space_between_dots=horizontal_space,
    vertical_space_between_dots=vertical_space,
    x_begin=x_begin
)

# --- Step 5: Exit Mechanism ---
# Keeps the window open until user clicks to close it
screen.exitonclick()
