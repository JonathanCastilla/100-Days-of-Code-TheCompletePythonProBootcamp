"""
Module Name: food.py
Project Number: 19
Project Name: Snake Game
Description:
    This module defines the `Food` class, which represents the edible object 
    within the Snake Game. The `Food` class inherits from the `Turtle` class 
    to visually render food items as small circles that appear randomly 
    within the game area.

    When the snake's head collides with the food object, the `refresh()` 
    method is invoked to reposition the food to a new random location within 
    the game boundaries. This behavior simulates the continuous spawning of 
    food throughout the game.

    Key Features:
    - Random placement of the food item inside the playable area.
    - Compact graphical representation using a circle shape.
    - Rapid rendering speed for visual responsiveness.
    - Integration with the snake collision detection logic.

Author: Jonathan Eduardo Castilla Zamora
"""

# === Module Imports ===
from turtle import Turtle  # Provides graphical capabilities for food rendering
import random  # Used for generating random coordinates
from game_board import WIDTH, HEIGHT  # Imports game boundaries from game_board module

# === Constant ===
OFFSET_SCREEN = 20  # Defines a margin so that food never appears at the extreme edges


class Food(Turtle):
    """
    The `Food` class models the food element in the Snake Game. 
    It inherits from the `Turtle` class to draw and position 
    the food dynamically within the window.
    """

    def __init__(self):
        """
        Initializes the food object with a circular shape, small size,
        and random initial position within the game area.
        """
        super().__init__()  # Calls the parent Turtle class constructor
        self.shape("circle")  # Defines the food shape
        self.penup()  # Prevents unwanted lines when moving
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Makes the circle smaller (half size)
        self.color("white")  # Sets the food color
        self.speed('fastest')  # Maximizes rendering speed for quick updates
        self.refresh()  # Randomly positions the food at game start

    def refresh(self):
        """
        Repositions the food object at a new random location 
        within the game area, ensuring it stays inside the 
        visible window boundaries.
        """
        random_x = random.randint(-WIDTH // 2 + OFFSET_SCREEN, WIDTH // 2 - OFFSET_SCREEN)
        random_y = random.randint(-HEIGHT // 2 + OFFSET_SCREEN, HEIGHT // 2 - OFFSET_SCREEN)
        self.goto(x=random_x, y=random_y)  # Moves the food to the new coordinates
