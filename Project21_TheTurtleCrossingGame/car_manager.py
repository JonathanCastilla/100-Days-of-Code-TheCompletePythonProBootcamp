"""
=============================================================
 File: car_manager.py
 Project no. 21: The Turtle Crossing Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora
 Description:
     This module defines the CarManager class, which is responsible
     for creating, positioning, and animating car objects across the
     game screen. Each car is represented as a Turtle instance with
     customized geometry, color, speed, and horizontal movement.
=============================================================
"""

from turtle import Turtle
from game_board import WIDTH, HEIGHT            # Imports screen dimensions from the game board
from player import STARTING_POSITION            # Import starting position to help calibrate spawning zones
import random

# Predefined palette of colors used to create visually diverse cars.
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

# Default movement speed for newly created cars.
STARTING_MOVE_DISTANCE = 5

# Increment added to a car’s movement speed each time the game level increases.
MOVE_INCREMENT = 10


class CarManager(Turtle):
    """
    Class responsible for handling the creation and movement of car objects
    that traverse the screen horizontally. Each car inherits from Turtle
    and behaves as an autonomous moving obstacle for the player.
    """
    def __init__(self):
        # Initialize the Turtle parent class.
        super().__init__()

        # Set the default color (will be overridden later by a random color).
        self.color('white')

        # Lift the pen to ensure cars do not draw lines while moving.
        self.penup()

        # -----------------------------
        # Randomized Car Spawn Location
        # -----------------------------
        # Generate a random Y-coordinate within the visible window space.
        # Cars are aligned in discrete vertical steps (20 px) to simulate lanes.
        # The STARTING_POSITION from the player is subtracted to ensure the spawn
        # does not conflict with the player's starting zone.
        self.y_init = random.randrange(
            - (HEIGHT // 2) - STARTING_POSITION[1] // 2 + 20,
            HEIGHT // 2 - 50,
            20
        )

        # Generate a random X-coordinate outside the right boundary of the screen.
        # Cars begin off-screen and travel leftward into the visible area.
        self.x_init = random.randrange(WIDTH // 2 + 20, WIDTH * 2, 30)

        # Move the new car to its randomly assigned starting position.
        self.goto(x=self.x_init, y=self.y_init)

        # Define the geometric representation of the car as a rectangle.
        self.shape('square')

        # Assign a random color from the predefined palette.
        self.color(random.choice(COLORS))

        # Initialize position tracking variables.
        # x_pos and y_pos store the next coordinates before moving the turtle.
        self.x_pos = 0
        self.y_pos = 0

        # Initialize horizontal movement value.
        # Cars travel leftwards by decreasing X coordinates.
        self.x_move = STARTING_MOVE_DISTANCE

        # Stretch the base square shape into a rectangular car shape.
        # stretch_wid = 1 → vertical compression
        # stretch_len = 2 → horizontal elongation
        self.shapesize(stretch_wid=1, stretch_len=2)

        # Track how many cars may be managed (not actively used here but kept for reference).
        self.number_of_cars = 6


    def move(self):
        """
        Updates the position of the car by translating it horizontally
        along the negative X-axis (left direction).
        """
        # Compute next X coordinate by subtracting movement speed.
        self.x_pos = self.xcor() - self.x_move

        # Y coordinate remains constant (cars only move horizontally).
        self.y_pos = self.ycor()

        # Move the Turtle object to its updated coordinates.
        self.goto(x=self.x_pos, y=self.y_pos)


    def increase_speed(self):
        """
        Increases the speed of the car by adding a predefined increment.
        This method is typically triggered when the player advances to the next level.
        """
        self.x_move += MOVE_INCREMENT
