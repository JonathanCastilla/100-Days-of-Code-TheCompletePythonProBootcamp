"""
=============================================================
 File: scoreboard.py
 Project: Pong Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora
 Description:
     This module defines the `Scoreboard` class responsible for
     managing, displaying, and updating the score of both players
     during the Pong game.

     It also handles the detection of a winning condition and
     displays a victory message when a player reaches the
     predefined score limit.

     The class inherits from the `Turtle` object in order to use
     its text rendering and positioning capabilities within the
     game window.
=============================================================
"""

# -------------------------------------------------------------
# Imports
# -------------------------------------------------------------
from turtle import Turtle

# -------------------------------------------------------------
# Constants
# -------------------------------------------------------------
FONT = ("Courier", 52, "bold")                     # Font style for the live score display
FONT_FOR_WIN_MESSAGE = ("Courier", 24, "bold")     # Font style for the victory message
SCORE_TO_WIN = 5                                   # Number of points required to win the game

# -------------------------------------------------------------
# Scoreboard Class Definition
# -------------------------------------------------------------
class Scoreboard(Turtle):
    """
    The Scoreboard class handles the visual representation of the
    players' scores and determines the winning player once the
    target score is reached.
    """

    def __init__(self):
        """
        Initializes the scoreboard object:
          - Hides the turtle cursor
          - Sets the text color and font
          - Initializes both players' scores and winner state
        """
        super().__init__()
        self.hideturtle()             # Hides the turtle icon (no visible cursor)
        self.color("white")           # Sets text color to white for contrast
        self.penup()                  # Prevents drawing lines during movement
        self.left_paddle_score = 0    # Initializes left player score
        self.right_paddle_score = 0   # Initializes right player score
        self.winner = None            # Placeholder for the winning player

    # ---------------------------------------------------------
    # Score Display Update
    # ---------------------------------------------------------
    def update(self):
        """
        Updates the displayed score for both players.
        The function clears previous scores and redraws the
        updated values at fixed positions on the screen.
        """
        self.clear()                  # Clear previous score text

        # Display left player's score
        self.goto(-100, 200)          # Position on top-left
        self.write(self.left_paddle_score, align="center", font=FONT)

        # Display right player's score
        self.goto(100, 200)           # Position on top-right
        self.write(self.right_paddle_score, align="center", font=FONT)

    # ---------------------------------------------------------
    # Winner Detection
    # ---------------------------------------------------------
    def check_winner(self):
        """
        Checks if either player has reached the winning score.
        Returns True if the game should end, otherwise False.
        """
        if self.right_paddle_score >= SCORE_TO_WIN or self.left_paddle_score >= SCORE_TO_WIN:
            # Determine which player won
            if self.right_paddle_score > self.left_paddle_score:
                self.winner = "Right"
            else:
                self.winner = "Left"

            # Print final message on screen
            self.print_win_message()
            return True
        else:
            return False

    # ---------------------------------------------------------
    # Victory Message Display
    # ---------------------------------------------------------
    def print_win_message(self):
        """
        Displays a message declaring the winner of the match.
        """
        self.goto(0, 0)  # Center the message on the screen
        self.write(f"'{self.winner} player' wins!", align="center", font=FONT_FOR_WIN_MESSAGE)
