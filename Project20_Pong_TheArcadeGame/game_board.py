"""
# ==========================
# File: game_board.py
# Author: Jonathan Eduardo Castilla Zamora
# Description: Defines the main game window (screen) for the Pong game,
#              including its dimensions, title, and background color.
# ==========================
"""

from turtle import Screen

# --- Game Window Configuration ---
WIDTH = 800  # Width of the game screen in pixels
HEIGHT = 600  # Height of the game screen in pixels
TITLE = 'PONG: The Arcade Game'  # Title displayed on the game window


class GameBoard():
    """
    GameBoard sets up the main game window using the Turtle graphics library.
    It configures the screen size, background color, title, and includes
    a flag to check whether the game is over.
    """

    def __init__(self):
        # Create a Screen object
        self.screen = Screen()

        # Configure screen dimensions
        self.screen.setup(WIDTH, HEIGHT)

        # Set the background color
        self.screen.bgcolor("black")

        # Set the window title
        self.screen.title(TITLE)

        # Game state flag
        self.is_game_over = False
