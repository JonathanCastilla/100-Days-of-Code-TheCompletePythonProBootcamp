"""
=============================================================
 File: game_board.py
 Project no. 21: The Turtle Crossing Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora
 Description:
     This module defines the Gameboard class, responsible for
     initializing and configuring the graphical window where the
     Turtle Crossing Game occurs. It sets screen dimensions, title,
     background color, and maintains the game’s running state.
=============================================================
"""

from turtle import Screen

# -------------------------------------------------------------
# Global Constants Defining the Display Configuration
# -------------------------------------------------------------
# The width of the game window in pixels.
WIDTH = 600

# The height of the game window in pixels.
HEIGHT = 600

# Background color of the screen. The default is white.
BG_COLOR = 'white'

# Title displayed on the window frame.
TITLE = 'Turtle Crossing Game'


class Gameboard():
    """
    The Gameboard class encapsulates the graphical interface where
    all game entities (player, cars, scoreboard, etc.) are rendered.
    It is responsible for window initialization and provides an
    attribute that indicates whether the game has ended.
    """

    def __init__(self):
        """
        Constructor that initializes the Turtle Graphics screen with
        predefined dimensions, background color, and window title. It
        also sets the game’s control flag 'is_game_over' to track the
        main loop termination.
        """

        # Create a new Turtle Screen instance, which serves as the main
        # drawing surface for the game.
        self.screen = Screen()

        # Configure the screen dimensions using the global width/height constants.
        self.screen.setup(width=WIDTH, height=HEIGHT)

        # Set the screen background color for visual clarity and contrast.
        self.screen.bgcolor(BG_COLOR)

        # Apply the title that appears in the window's top border.
        self.screen.title(TITLE)

        # Control flag indicating whether the game is finished.
        # It is monitored in the main loop.
        self.is_game_over = False
