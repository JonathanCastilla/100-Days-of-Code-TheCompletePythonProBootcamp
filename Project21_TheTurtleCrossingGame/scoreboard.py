"""
=============================================================
 File: scoreboard.py
 Project no. 21: The Turtle Crossing Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora
 Description:
     This module defines the Scoreboard class, which is responsible
     for displaying the current level and the 'Game Over' message
     on the game screen. The scoreboard updates each time the
     player reaches the finish line.
=============================================================
"""

from turtle import Turtle
from game_board import WIDTH, HEIGHT

# -------------------------------------------------------------
# Configuration Constants
# -------------------------------------------------------------

# Font style for scoreboard text (Courier, size 14, bold).
FONT = ("Courier", 14, "bold")

# Coordinates for drawing the level text on the screen.
X_POS_SCOREBOARD = - (WIDTH // 2) + 20
Y_POS_SCOREBOARD = HEIGHT // 2 - 40

# Coordinates for displaying the "GAME OVER" message.
X_POS_GAME_OVER = 0
Y_POS_GAME_OVER = 0


class Scoreboard(Turtle):
    """
    The Scoreboard class extends Turtle to display real-time text
    information on the screen. It manages:
        - The current game level
        - Updating display text after major game events
        - Rendering a centered 'Game Over' message
    """

    def __init__(self):
        """
        Initializes the scoreboard at the top-left corner of the screen
        and prints the initial level.
        """
        super().__init__()

        # Hide the turtle icon so only the text is visible.
        self.hideturtle()

        # Prevent drawing lines when positioning the scoreboard.
        self.penup()

        # Use black text to ensure visibility on the white background.
        self.color("black")

        # Game starts at level 0.
        self.level = 0

        # Move the turtle to the designated scoreboard position.
        self.goto(x=X_POS_SCOREBOARD, y=Y_POS_SCOREBOARD)

        # Print initial level.
        self.write(f"Level: {self.level}", align="left", font=FONT)

    # -------------------------------------------------------------
    # Score and UI Update Methods
    # -------------------------------------------------------------

    def increase_level(self):
        """
        Increments the level counter. The updated value is printed
        on-screen by calling update().
        """
        self.level += 1

    def update(self):
        """
        Clears previous text and rewrites the updated level.
        Called each time the player completes a level.
        """
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        """
        Displays the 'GAME OVER' message centered on the screen.
        Called when the player collides with a car.
        """
        self.goto(X_POS_GAME_OVER, Y_POS_GAME_OVER)
        self.write("GAME OVER", align="center", font=FONT)
