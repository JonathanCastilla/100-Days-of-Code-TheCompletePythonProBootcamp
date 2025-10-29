"""
Project Number: 19
Project Name: Snake Game
Description:
    This program implements the classic "Snake" arcade game using Python’s Turtle Graphics library.

    The game consists of a moving snake that grows each time it eats food. The player controls the
    snake’s direction using keyboard keys (W, A, S, D). The game ends when the snake collides with
    the wall boundaries or with itself.

    The project is modular and organized into multiple classes:
        - `Snake`: Handles snake creation, movement, and growth.
        - `Food`: Manages food generation and repositioning.
        - `Scoreboard`: Displays and updates the player’s score and game-over message.
        - `GameBoard`: Manages the game screen, dimensions, and control flow.

    Key Features:
    - Continuous snake movement using time-based updates.
    - Collision detection with food, walls, and self-body segments.
    - Real-time score tracking and display.
    - Adjustable parameters for gameplay tuning (speed, screen size, wall offset).
    - Structured and object-oriented design promoting modularity.

Author: Jonathan Eduardo Castilla Zamora
"""

# === Module Imports ===
from snake import Snake
from scoreboard import Scoreboard
from game_board import GameBoard, WIDTH, HEIGHT
from food import Food
import time

# === Global Configuration Parameters ===
WALL_OFFSET = 10  # Distance from the border where collisions are detected
SNAKE_DISTANCE_TO_COLLIDE_WITH_ITSELF = WALL_OFFSET  # Minimum distance for snake to collide with itself

# Mapping of keyboard keys for player control
keywords_of_movement = {
    'right': 'd',
    'left': 'a',
    'up': 'w',
    'down': 's',
}

# === Object Instantiations ===
game_board = GameBoard()      # Initializes the game screen and its parameters
snake = Snake()               # Creates the snake object and its initial segments
food = Food()                 # Creates the food object placed at a random position
scoreboard = Scoreboard()     # Initializes the scoreboard to track player’s score

# === Screen Configuration ===
game_board.screen.tracer(0)   # Turns off automatic screen updates for smoother animation
game_board.screen.listen()    # Enables keyboard listening for player input

# === Key Bindings (Movement Controls) ===
game_board.screen.onkey(fun=snake.up, key=keywords_of_movement['up'])
game_board.screen.onkey(fun=snake.down, key=keywords_of_movement['down'])
game_board.screen.onkey(fun=snake.right, key=keywords_of_movement['right'])
game_board.screen.onkey(fun=snake.left, key=keywords_of_movement['left'])

# === Main Game Loop ===
while not game_board.is_game_over:
    game_board.screen.update()     # Manually refreshes screen for smoother animation
    time.sleep(0.1)                # Controls snake movement speed (delay between frames)
    snake.move_segments()          # Moves all snake segments forward in current direction

    # --- Detect Collision with Food ---
    if snake.head.distance(food) < snake.distance_to_eat:
        food.refresh()             # Repositions food at a new random location
        snake.extend()             # Adds a new segment to the snake’s tail
        scoreboard.increase_score()# Increases and updates the player’s score display

    # --- Detect Collision with Walls ---
    # Checks if snake head goes beyond screen boundaries
    if not (-(WIDTH // 2) + WALL_OFFSET < snake.head.xcor() < (WIDTH // 2) - WALL_OFFSET) or \
       not (-(HEIGHT // 2) + WALL_OFFSET < snake.head.ycor() < (HEIGHT // 2) - WALL_OFFSET):
        game_board.is_game_over = True
        scoreboard.game_over()     # Displays “Game Over” message

    # --- Detect Collision with Tail ---
    # If the head collides with any part of its own body:
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < SNAKE_DISTANCE_TO_COLLIDE_WITH_ITSELF:
            game_board.is_game_over = True
            scoreboard.game_over() # Ends the game and displays “Game Over” message

# === Exit Behavior ===
game_board.screen.exitonclick()  # Keeps window open until user clicks to close
