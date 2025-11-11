"""
=============================================================
 File: ball.py
 Project: Pong Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora
 Description:
     This module defines the `Ball` class, responsible for the
     creation, motion, and physical interactions of the ball in
     the Pong game.

     It includes functions for movement, bouncing off the walls
     and paddles, resetting position after scoring events, and
     gradually increasing the speed to enhance difficulty as the
     match progresses.
=============================================================
"""

# -------------------------------------------------------------
# Imports
# -------------------------------------------------------------
from turtle import Turtle
from game_board import WIDTH, HEIGHT

# -------------------------------------------------------------
# Constants
# -------------------------------------------------------------
STARTING_POSITION = (0, 0)                     # Initial position of the ball at game start or after scoring
SECOND_POSITION = (WIDTH // 2, HEIGHT // 2)    # Optional position (not used but kept for reference)
STEP_MOVEMENT_FORWARD = 25                     # Default forward step (unused but conceptually for calibration)
EXTRA_SPEED = 2                                # Incremental speed value after each score event

# -------------------------------------------------------------
# Ball Class Definition
# -------------------------------------------------------------
class Ball(Turtle):
    """
    The Ball class manages the movement and collision mechanics of
    the Pong ball. It inherits from `turtle.Turtle` to utilize
    graphical movement and rendering functions.
    """

    def __init__(self):
        """
        Initializes the ball's attributes and visual representation:
          - Sets shape and color
          - Configures starting position and motion vectors
          - Initializes movement deltas for both X and Y axes
        """
        super().__init__()
        self.shape('circle')                   # Defines ball shape
        self.color('white')                    # Ball color
        self.penup()                           # Avoids drawing a line while moving
        self.starting_position = STARTING_POSITION
        self.collision = False                 # Boolean flag for future collision tracking
        self.x_pos = 0                         # Current x position (updated during motion)
        self.y_pos = 0                         # Current y position (updated during motion)
        self.x_move = 10                       # Step increment along the X axis
        self.y_move = 10                       # Step increment along the Y axis

    # ---------------------------------------------------------
    # Ball Motion
    # ---------------------------------------------------------
    def move(self):
        """
        Moves the ball continuously by updating its position based
        on the current movement vectors (`x_move`, `y_move`).
        """
        self.x_pos = self.xcor() + self.x_move
        self.y_pos = self.ycor() + self.y_move
        self.goto(self.x_pos, self.y_pos)

    # ---------------------------------------------------------
    # Bounce Mechanics — Y Axis
    # ---------------------------------------------------------
    def bounce_y_axis(self):
        """
        Inverts the vertical movement component (`y_move`) to
        simulate a bounce when the ball collides with the top or
        bottom boundary of the game window.
        """
        self.y_move *= -1

    # ---------------------------------------------------------
    # Bounce Mechanics — X Axis
    # ---------------------------------------------------------
    def bounce_x_axis(self):
        """
        Inverts the horizontal movement component (`x_move`) to
        simulate a bounce when the ball collides with a paddle.
        """
        self.x_move *= -1

    # ---------------------------------------------------------
    # Ball Reset After Scoring
    # ---------------------------------------------------------
    def reset_position(self):
        """
        Resets the ball's position to the center of the screen
        and reverses its horizontal direction to restart play.
        """
        self.goto(STARTING_POSITION)
        self.bounce_x_axis()

    # ---------------------------------------------------------
    # Dynamic Speed Adjustment
    # ---------------------------------------------------------
    def increase_speed(self):
        """
        Gradually increases the ball’s speed after each point is
        scored to raise the game’s difficulty level.

        The direction is preserved while the step increments are
        modified in magnitude.
        """
        if self.x_move > 0 and self.y_move > 0:
            self.x_move += EXTRA_SPEED
            self.y_move += EXTRA_SPEED
        else:
            self.x_move -= EXTRA_SPEED
            self.y_move -= EXTRA_SPEED
