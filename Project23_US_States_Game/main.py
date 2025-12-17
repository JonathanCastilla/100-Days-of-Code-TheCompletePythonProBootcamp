"""
=============================================================
 File: main.py
 Project no. 23: The U.S. States Game
 Author: Jonathan Eduardo Castilla Zamora

 Description:
     This script serves as the main execution file for the
     U.S. States guessing game. It coordinates data loading,
     user interaction, and game flow by integrating the Map
     class with a CSV dataset containing state coordinates.
=============================================================
"""

# === IMPORT REQUIRED MODULES ===
from map import Map                 # Custom class managing the map and game logic
import pandas as pd                 # Library for data manipulation and CSV handling


# === LOAD DATASET ===
# Reads the CSV file containing state names and their x, y coordinates
data = pd.read_csv('50_states.csv')


# === INITIALIZE GAME MAP ===
# Creates an instance of the Map class, which also initializes the screen
game_map = Map()


# === DEBUG / VALIDATION OUTPUT ===
# Prints the x-coordinate of Ohio to verify that the dataset is loaded correctly
print(data[data['state'] == 'Ohio']['x'].values[0])


# === INITIAL USER PROMPT ===
# Displays the first input dialog asking the user to guess a state name
game_map.answer_state = game_map.prompt_user_input(
    title_text=game_map.beginning_title,
    prompt_text=game_map.prompt
)

# Checks whether the initial answer is correct, incorrect, or an exit command
game_map.check_answer_state(data)


# === MAIN GAME LOOP ===
# Continues running until the game_over flag becomes True
while not game_map.game_over:

    # Prompts the user with updated progress information
    game_map.answer_state = game_map.prompt_user_input(
        title_text=game_map.playing_title,
        prompt_text=game_map.prompt
    )

    # Validates the user's answer against the dataset
    game_map.check_answer_state(data)

    # Checks whether the user has successfully guessed all 50 states
    game_map.check_user_wins()
