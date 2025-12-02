"""
Module Name: snake.py
Project Number: 19
Project Name: Snake Game
Description:
    This module defines the `Snake` class, which implements the fundamental logic
    for creating, rendering, and moving the snake entity in the Snake Game.

    The snake is modeled as a collection of square-shaped segments (Turtle objects)
    that follow each other’s movement. The player can control the direction of the
    snake using keyboard inputs (W, A, S, D) corresponding to the four cardinal directions.

    Each movement step advances the head forward, while the remaining body segments
    follow the path of the preceding one, maintaining continuity in the snake’s form.
    Collision detection logic is implemented in the main game loop to manage
    interactions with food, walls, and the snake’s own body.

    Key Features:
    - Modular generation of snake body segments.
    - Continuous movement achieved by segment position shifting.
    - Extension of the snake body upon food consumption.
    - Prevention of immediate reversal to avoid self-collision.
    - Consistent step-based and angle-controlled movement for realism.

Author: Jonathan Eduardo Castilla Zamora
"""

# === Module Imports ===
from turtle import Turtle  # Used for graphical representation of the snake

# === Constants ===
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake's body segments
MOVEMENT_STEP = 20  # Step size in pixels for each movement
MOVEMENT_ANGLES = {  # Dictionary mapping directions to angles in degrees
    'right': 0,
    'left': 180,
    'up': 90,
    'down': 270,
}
DISTANCE_TO_FOOD = 25  # Distance threshold for detecting collision with food


class Snake:
    """
    The `Snake` class encapsulates the creation, rendering, and
    dynamic movement behavior of the snake in the game.
    """

    def __init__(self):
        """
        Initializes the Snake instance by generating the initial body segments,
        setting movement parameters, and defining the head and eating threshold.
        """
        self.starting_positions = STARTING_POSITIONS
        self.a_snake_segment = None
        self.snake_segments = []  # List that stores all body segments
        self.generate()  # Generates the initial three segments

        self.step_for_forward_movement = MOVEMENT_STEP
        self.head = self.snake_segments[0]  # The first segment acts as the snake's head

        self.distance_to_eat = DISTANCE_TO_FOOD  # Distance threshold for food detection

    def generate(self):
        """
        Generates the initial snake body by creating and positioning
        individual square-shaped segments using predefined coordinates.
        """
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a single segment (square) at the specified position.

        Args:
            position (tuple): The (x, y) coordinates for the new segment.
        """
        self.a_snake_segment = Turtle()
        self.a_snake_segment.shape('square')  # Defines segment shape
        self.a_snake_segment.color('white')  # Defines color
        self.a_snake_segment.penup()  # Prevents unwanted line drawing
        self.a_snake_segment.goto(position)  # Places the segment at the given coordinates
        self.snake_segments.append(self.a_snake_segment)

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.generate()
        self.head = self.snake_segments[0]

    def extend(self):
        """
        Extends the snake’s body by adding a new segment
        at the position of the last segment (tail).
        """
        self.add_segment(self.snake_segments[-1].position())

    def move_segments(self):
        """
        Moves all snake segments forward in a cohesive manner:
        - Each segment takes the position of the one before it.
        - The head advances forward in its current heading direction.
        """
        # Move each segment to the position of the previous one (backward iteration)
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x_position = self.snake_segments[segment - 1].xcor()
            new_y_position = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x_position, new_y_position)

        # Move the head forward by a fixed step
        self.head.forward(self.step_for_forward_movement)

    # === Directional Movement Methods ===

    def right(self):
        """Turns the snake's head to the right (0°), preventing reversal into itself."""
        if self.head.heading() != MOVEMENT_ANGLES['left']:
            self.head.setheading(MOVEMENT_ANGLES['right'])

    def left(self):
        """Turns the snake's head to the left (180°), preventing reversal into itself."""
        if self.head.heading() != MOVEMENT_ANGLES['right']:
            self.head.setheading(MOVEMENT_ANGLES['left'])

    def up(self):
        """Turns the snake's head upward (90°), preventing reversal into itself."""
        if self.head.heading() != MOVEMENT_ANGLES['down']:
            self.head.setheading(MOVEMENT_ANGLES['up'])

    def down(self):
        """Turns the snake's head downward (270°), preventing reversal into itself."""
        if self.head.heading() != MOVEMENT_ANGLES['up']:
            self.head.setheading(MOVEMENT_ANGLES['down'])
