"""
=============================================================
 File: main.py
 Project no. 21: The Turtle Crossing Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora

 Description:
    This program implements a classic arcade-style "Turtle Crossing"
    game using Python's Turtle Graphics module.

    The player controls a turtle that must move upward across the
    road while avoiding horizontally moving cars. Cars increase in
    number and speed as the player clears levels, enhancing difficulty.

    Core functionalities:
    - Player movement via keyboard input (Up arrow key).
    - Car generation and continuous movement across the screen.
    - Collision detection between the player and cars.
    - Level management and game-over screen display.
    - Continuous gameplay loop until collision occurs.

    Object-oriented design:
    - `Gameboard` manages the screen and game state.
    - `Player` handles user-controlled movement and win-state logic.
    - `CarManager` creates and updates moving cars.
    - `Scoreboard` displays levels and game-over text.

=============================================================
"""

# --- Import game components and libraries ---
from car_manager import CarManager          # Class that manages moving cars
from scoreboard import Scoreboard           # Class for displaying score and level
from player import Player                   # Class representing the player turtle
from game_board import Gameboard, WIDTH, HEIGHT  # Gameboard and its dimensions
import time                                 # Used for refresh delay between frames
import random                               # (May be used for randomization in other modules)

# --- Dictionary to map input keys to movement functions ---
keywords_of_movement = {
    'player': {'up': 'Up'},  # Player moves with the Up Arrow key
}

# --- Object instantiation ---
gameboard = Gameboard()          # Creates game window and controls game state
player = Player()                # Initializes player turtle at starting position
scoreboard = Scoreboard()        # Displays current level
cars = []                        # List to store all CarManager objects

# --- Screen configuration ---
gameboard.screen.tracer(0)       # Disables auto-updating for smooth animation
gameboard.screen.listen()        # Activates keyboard listening

# --- Key binding for player movement ---
gameboard.screen.onkey(
    fun=player.up,
    key=keywords_of_movement['player']['up']
)

# --- Initial population of car objects ---
number_of_cars_within_a_loop = 40
for _ in range(number_of_cars_within_a_loop):
    cars.append(CarManager())    # Creates several cars with random attributes

# ============================================================
#                   Main Game Loop
# ============================================================

while not gameboard.is_game_over:

    gameboard.screen.update()    # Refreshes the screen frame
    time.sleep(0.1)              # Controls global game speed (frame rate)

    # --- Car movement + collision detection ---
    for i in range(len(cars)):

        # Check if player collides with the i-th car
        if player.is_collided(cars[i]):
            gameboard.is_game_over = True  # End game
            scoreboard.game_over()         # Display GAME OVER message

        cars[i].move()            # Move each car horizontally

    # --- Level completion check ---
    if player.ycor() >= player.finish_line_y_axis:
        # Player successfully crosses the road → increase difficulty
        player.move_to_starting_position()    # Reset player to starting line
        scoreboard.increase_level()           # Increment level number
        scoreboard.update()                   # Redraw scoreboard display

        number_of_cars_within_a_loop += 2     # Spawn even MORE cars next level

        # Add the new wave of cars
        for _ in range(number_of_cars_within_a_loop):
            cars.append(CarManager())

        # Increase speed of ALL cars currently on screen
        for i in range(len(cars)):
            cars[i].increase_speed()

# --- Close game on click after Game Over ---
gameboard.screen.exitonclick()
