"""
=============================================================
 File: main.py
 Project: Pong Game (Python Turtle Graphics)
 Author: Jonathan Eduardo Castilla Zamora
 Description:
     This script serves as the main entry point for the Pong Game.
     It integrates all components of the game: the game board,
     paddles, ball, and scoreboard. The logic includes player
     controls, ball movement, collision detection, scoring, and
     game termination conditions.

     The implementation relies on the 'turtle' graphics library,
     with modular design separating each element into distinct
     classes for maintainability and clarity.
=============================================================
"""

# -------------------------------------------------------------
# Import modules and custom classes
# -------------------------------------------------------------
from game_board import GameBoard, WIDTH, HEIGHT   # Game window setup and constants
from paddle import Paddle                         # Paddle (player-controlled object)
from ball import Ball                             # Ball movement and collisions
from scoreboard import Scoreboard                 # Score management and winner detection
import time                                       # Time control for frame delay and animation pacing

# -------------------------------------------------------------
# Constants
# -------------------------------------------------------------
STARTING_POSITIONS_LEFT_PADDLE = (-350, 0)        # Initial position of left paddle
STARTING_POSITIONS_RIGHT_PADDLE = (350, 0)        # Initial position of right paddle
DISTANCE_FOR_COLLISION = 40                       # Distance threshold for ball-paddle collision

# -------------------------------------------------------------
# Game Initialization
# -------------------------------------------------------------
game_board = GameBoard()                          # Create the game board (screen setup)
screen = game_board.screen                        # Access the main screen for control bindings
left_paddle = Paddle(STARTING_POSITIONS_LEFT_PADDLE, screen)   # Instantiate left paddle
right_paddle = Paddle(STARTING_POSITIONS_RIGHT_PADDLE, screen) # Instantiate right paddle
ball = Ball()                                     # Instantiate the ball
scoreboard = Scoreboard()                         # Instantiate the scoreboard

# -------------------------------------------------------------
# Keyboard Control Mapping
# -------------------------------------------------------------
keywords_of_movement = {
    'right_paddle': {'up': 'Up', 'down': 'Down'}, # Right paddle controlled by arrow keys
    'left_paddle': {'up': 'w', 'down': 's'}       # Left paddle controlled by W/S keys
}

# -------------------------------------------------------------
# Screen Configuration and Key Bindings
# -------------------------------------------------------------
game_board.screen.tracer(0)   # Disables auto-refresh for smooth animation (manual control)
game_board.screen.listen()    # Activates key event listening

# Bind each key to a toggle function (continuous movement logic in Paddle class)
game_board.screen.onkey(fun=right_paddle.toggle_up, key=keywords_of_movement['right_paddle']['up'])
game_board.screen.onkey(fun=right_paddle.toggle_down, key=keywords_of_movement['right_paddle']['down'])
game_board.screen.onkey(fun=left_paddle.toggle_up, key=keywords_of_movement['left_paddle']['up'])
game_board.screen.onkey(fun=left_paddle.toggle_down, key=keywords_of_movement['left_paddle']['down'])

# -------------------------------------------------------------
# Main Game Loop
# -------------------------------------------------------------
while not game_board.is_game_over:
    # --- Screen and Score Updates ---
    game_board.screen.update()   # Refresh screen frame manually
    scoreboard.update()          # Refresh scoreboard display
    time.sleep(0.05)             # Delay between frames for smoother movement

    # --- Ball Movement ---
    ball.move()                  # Update ball position on each frame

    # ---------------------------------------------------------
    # Collision Detection: Ball with Top/Bottom Walls
    # ---------------------------------------------------------
    if abs(ball.ycor()) >= HEIGHT // 2:
        ball.bounce_y_axis()     # Reverse vertical direction upon collision

    # ---------------------------------------------------------
    # Collision Detection: Ball with Paddles
    # ---------------------------------------------------------
    # Right paddle collision condition
    right_collision = (
        ball.distance(right_paddle) < DISTANCE_FOR_COLLISION and
        ball.xcor() > STARTING_POSITIONS_RIGHT_PADDLE[0] - 30
    )

    # Left paddle collision condition
    left_collision = (
        ball.distance(left_paddle) < DISTANCE_FOR_COLLISION and
        ball.xcor() < STARTING_POSITIONS_LEFT_PADDLE[0] + 30
    )

    # Bounce ball horizontally if it touches any paddle
    if right_collision or left_collision:
        ball.bounce_x_axis()

    # ---------------------------------------------------------
    # Scoring and Ball Reset Logic
    # ---------------------------------------------------------
    if abs(ball.xcor()) > WIDTH // 2:
        ball.increase_speed()  # Increment speed after each score event

        # Determine which player scores
        if ball.xcor() < 0:
            scoreboard.right_paddle_score += 1   # Right player scores
        else:
            scoreboard.left_paddle_score += 1    # Left player scores

        scoreboard.update()       # Refresh displayed score
        ball.reset_position()     # Recenter the ball and reverse its direction

    # ---------------------------------------------------------
    # Check for Winning Condition
    # ---------------------------------------------------------
    game_board.is_game_over = scoreboard.check_winner()  # Ends loop if a player reaches max score

# -------------------------------------------------------------
# Exit Condition
# -------------------------------------------------------------
game_board.screen.exitonclick()  # Keeps window open until user clicks
