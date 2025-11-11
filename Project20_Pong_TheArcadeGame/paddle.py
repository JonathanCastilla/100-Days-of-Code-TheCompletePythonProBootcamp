"""
=============================================================
 File: paddle.py
 Project: Pong Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora
 Description:
     This module defines the `Paddle` class, representing one of
     the two paddles controlled by the players in the Pong game.

     Each paddle is modeled as a movable rectangular object that
     can travel vertically within the boundaries of the screen.
     The class employs a non-blocking timer loop to continuously
     update paddle position, simulating smooth movement while
     maintaining responsiveness to user input.

     The implementation highlights object-oriented principles,
     event-driven programming, and animation control using the
     `turtle` module and its screen event system.
=============================================================
"""

# -------------------------------------------------------------
# Imports
# -------------------------------------------------------------
from turtle import Turtle
from game_board import HEIGHT

# -------------------------------------------------------------
# Constants
# -------------------------------------------------------------
MOVEMENT_STEP = 20                 # Step size (in pixels) for each movement update
MOVEMENT_ANGLES = {                # Dictionary mapping direction labels to angular degrees
    'up': 90,
    'down': 270,
}
PADDLE_LIMIT_Y = HEIGHT // 2 - 25  # Vertical boundary to prevent paddle from moving off-screen
REFRESH_TIME = 30                  # Timer interval (in milliseconds) between movement updates

# -------------------------------------------------------------
# Paddle Class Definition
# -------------------------------------------------------------
class Paddle(Turtle):
    """
    The `Paddle` class encapsulates the visual and behavioral
    logic of a Pong paddle. It inherits from `turtle.Turtle`,
    allowing graphical manipulation and collision detection.

    Each paddle:
      - Moves vertically according to player input.
      - Is constrained within the top and bottom screen limits.
      - Employs timed callbacks (`ontimer`) for smooth, continuous motion.
    """

    def __init__(self, start_pos, screen):
        """
        Initializes the paddle object with a starting position and
        an associated screen for managing timed updates.

        Parameters:
            start_pos (tuple): (x, y) coordinates of the paddle's starting position.
            screen (turtle.Screen): The main screen instance used for animation control.
        """
        super().__init__()
        self.starting_position = start_pos
        self.step_for_forward_movement = MOVEMENT_STEP
        self.penup()                           # Avoids drawing trail lines
        self.goto(self.starting_position)      # Moves paddle to initial position
        self.shapesize(stretch_wid=5, stretch_len=1)  # Defines paddle proportions
        self.shape("square")                   # Default paddle shape
        self.color("white")                    # Paddle color for visibility

        # Motion control attributes
        self.direction = None                  # Current direction ('up' or 'down')
        self.screen = screen                   # Reference to main screen for scheduling
        self.is_moving = False                 # State flag to indicate active motion

    # ---------------------------------------------------------
    # Input Handling — Movement Control
    # ---------------------------------------------------------
    def toggle_up(self):
        """
        Activates continuous upward motion. If the paddle is not
        already moving, begins motion using recursive timed calls.
        """
        self.direction = 'up'
        if not self.is_moving:
            self.is_moving = True
            self.move_continuously()

    def toggle_down(self):
        """
        Activates continuous downward motion. If the paddle is not
        already moving, begins motion using recursive timed calls.
        """
        self.direction = 'down'
        if not self.is_moving:
            self.is_moving = True
            self.move_continuously()

    # ---------------------------------------------------------
    # Continuous Paddle Movement
    # ---------------------------------------------------------
    def move_continuously(self):
        """
        Executes continuous paddle motion in the selected direction
        while respecting the upper and lower boundary limits.

        The function re-calls itself via the `ontimer` event to
        maintain fluid movement without freezing the game loop.
        """
        # Movement when direction is upward
        if self.direction == 'up':
            if self.ycor() < PADDLE_LIMIT_Y:
                self.goto(self.xcor(), self.ycor() + MOVEMENT_STEP)
            else:
                self.is_moving = False  # Stop when top boundary is reached

        # Movement when direction is downward
        elif self.direction == 'down':
            if self.ycor() > -PADDLE_LIMIT_Y:
                self.goto(self.xcor(), self.ycor() - MOVEMENT_STEP)
            else:
                self.is_moving = False  # Stop when bottom boundary is reached

        # Schedule next movement frame if still active
        if self.is_moving:
            self.screen.ontimer(self.move_continuously, REFRESH_TIME)

    # ---------------------------------------------------------
    # Stop Paddle Movement
    # ---------------------------------------------------------
    def stop(self):
        """
        Halts paddle motion and clears its direction state.
        Can be called to interrupt movement under custom events.
        """
        self.is_moving = False
        self.direction = None
