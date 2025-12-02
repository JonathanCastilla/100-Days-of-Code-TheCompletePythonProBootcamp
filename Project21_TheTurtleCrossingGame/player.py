"""
=============================================================
 File: player.py
 Project no. 21: The Turtle Crossing Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora
 Description:
     This module defines the Player class, which represents the
     controllable turtle character in the Turtle Crossing Game. The
     player moves vertically toward a designated finish line while
     avoiding collisions with moving cars.
=============================================================
"""

from turtle import Turtle
import math

# -------------------------------------------------------------
# Global Configuration Constants
# -------------------------------------------------------------

# Initial position of the player when the game starts or resets.
STARTING_POSITION = (0, -200)

# Vertical distance (in pixels) the player moves with each 'Up' key press.
MOVE_DISTANCE = 10

# Y-coordinate representing the finish line — when the player reaches
# this value, a level is completed.
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    The Player class extends the Turtle class to model the frog-like
    character controlled by the user. Its responsibilities include:
        - Handling movement
        - Resetting position upon level completion
        - Detecting collisions with cars
    """

    def __init__(self):
        """
        Constructor that initializes the player's appearance, starting
        position, orientation, and collision parameters.
        """
        super().__init__()

        # Set the turtle's visual properties.
        self.shape('turtle')
        self.color('black')

        # Lift the pen to prevent drawing lines while moving.
        self.penup()

        # Ensure the turtle is facing upward (toward the finish line).
        self.setheading(90)

        # Move the player to the predefined initial position.
        self.move_to_starting_position()

        # Set the finish line Y-coordinate used by the main game logic.
        self.finish_line_y_axis = FINISH_LINE_Y

        # Boolean indicating whether the player has reached the finish line.
        self.in_finish_line = False

        # Minimum distance at which a collision with a car is registered.
        self.collision_threshold = 20

    # -------------------------------------------------------------
    # Movement and State Functions
    # -------------------------------------------------------------

    def move_to_starting_position(self):
        """
        Repositions the player back at the starting location. This
        occurs when a new level begins after reaching the finish line.
        """
        self.goto(STARTING_POSITION)

    def is_collided(self, obstacle):
        """
        Determines whether the player has collided with a car.

        Parameters:
            obstacle (Turtle): The car or object whose distance is checked.

        Returns:
            bool: True if the distance between the player and the obstacle
                  is less than or equal to the collision threshold.
        """

        # Compute the Euclidean distance between player and obstacle.
        distance = self.distance(obstacle.pos())

        # Check collision based on the threshold.
        if distance <= self.collision_threshold:
            return True
        else:
            return False

    def up(self):
        """
        Moves the player upward by a fixed distance. This action is tied
        to the 'Up' key in the main script via the screen's event system.
        """
        self.forward(MOVE_DISTANCE)
