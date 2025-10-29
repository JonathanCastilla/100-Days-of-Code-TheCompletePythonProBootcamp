# ==============================================
# game_board.py
# ==============================================
# This module defines the GameBoard class, which is responsible
# for initializing and managing the game window (or board)
# using Python’s built-in turtle graphics system.
# ==============================================

from turtle import Screen

# --------------------------------------------------------------
# Global constants defining the dimensions of the game window
# --------------------------------------------------------------
WIDTH = 600     # Width of the game window in pixels
HEIGHT = 600    # Height of the game window in pixels


class GameBoard:
    """
    The GameBoard class initializes the main game window using
    the turtle graphics Screen object. It sets up the board’s
    dimensions, background color, and title, and keeps track
    of whether the game is over.
    """
    def __init__(self):
        # Create a screen instance to serve as the game display
        self.screen = Screen()

        # Set up the screen size using predefined constants
        self.screen.setup(width=WIDTH, height=HEIGHT)

        # Set background color to black for contrast with snake and food
        self.screen.bgcolor("black")

        # Set the title displayed on the window bar
        self.screen.title("Snake Game")

        # Flag used to indicate whether the game is over
        self.is_game_over = False
