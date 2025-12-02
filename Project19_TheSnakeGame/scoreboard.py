"""
Module Name: scoreboard.py
Project Number: 19
Project Name: Snake Game
Description:
    This module defines the `Scoreboard` class, which manages the display and
    updating of the player's score during gameplay, as well as the final
    “Game Over” message upon termination.

    It inherits from Python’s `Turtle` class to leverage its text rendering
    capabilities within the same graphical window used by the game. The
    scoreboard is positioned at the top center of the screen and dynamically
    updates in real time as the player progresses.

    Key Features:
    - Displays the player’s current score.
    - Automatically updates when the snake eats food.
    - Displays a “GAME OVER” message at the center of the screen.
    - Uses predefined font styles and alignment for consistent aesthetics.

Author: Jonathan Eduardo Castilla Zamora
"""

# === Module Imports ===
from turtle import Turtle
from game_board import HEIGHT  # Imports game board height for positioning the scoreboard

# === Screen Position and Style Constants ===
X_POS_SCOREBOARD = 0
Y_POS_SCOREBOARD = HEIGHT // 2 - 20  # Places scoreboard slightly below the top edge

ALIGNMENT = "center"  # Text alignment (centered horizontally)
FONT = ("Courier", 14, "bold")  # Font style for live score display
FONT_FOR_GAME_OVER = ("Courier", 18, "bold")  # Larger font for game over message


class Scoreboard(Turtle):
    """
    The `Scoreboard` class handles all score-related display operations.
    It inherits from the Turtle class, allowing text to be rendered
    directly on the game screen.
    """

    def __init__(self):
        """
        Initializes the scoreboard with zero score, hides the turtle cursor,
        and sets up its initial position and appearance.
        """
        super().__init__()  # Calls parent Turtle constructor
        self.penup()  # Prevents drawing lines when moving
        self.hideturtle()  # Hides the turtle shape for clean display
        self.goto(x=X_POS_SCOREBOARD, y=Y_POS_SCOREBOARD)  # Sets position near the top
        self.color("white")  # Text color
        self.score = 0  # Initial score
        self.high_score = 0 # Highest score
        self.update_score()  # Renders the initial score display

    def update_score(self):
        """
        Writes the current score on the screen at the scoreboard’s position.
        """
        self.clear()

        with open("data.txt", "r") as file:
            self.high_score = int(file.read())

        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):

        # Updating the high score obtained by player
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", "w") as file:
                file.write(str(self.high_score))

        self.score = 0 # Reset the current score
        self.update_score()

    def increase_score(self):
        """
        Clears the previous score, increments by one, and updates the display.
        Triggered each time the snake eats food.
        """
        self.clear()  # Removes previous score
        self.score += 1  # Increments score
        self.color("white")  # Ensures consistent color
        self.update_score()  # Displays new score

    def game_over(self):
        """
        Displays a centered 'GAME OVER' message when the player loses.
        """
        self.goto(x=0, y=0)  # Centers text in the middle of the screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_FOR_GAME_OVER)
