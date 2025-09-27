"""
Project Number: 13
Project Name: The Higher Lower Game
Description:
    This program implements a text-based comparison game where the player 
    is presented with two public figures (Option A and Option B), each 
    described by their profession and country of origin. The objective is 
    to guess which of the two has a higher number of followers. The data 
    is randomly selected from a predefined dataset. For each correct 
    answer, the player's score increases, and a new comparison is shown. 
    The game ends when the player provides an incorrect answer, after 
    which they are prompted to decide whether to start a new game or exit.
Author: Jonathan Eduardo Castilla Zamora
"""

from art import logo, vs  # Import ASCII art for display
from game_data import data  # Import the dataset containing public figures
from random import randint  # Import function for random index selection

# Flag to manage whether a new game session should be started
start_a_new_game = True

# Outer loop to handle restarting the entire game
while start_a_new_game:
    user_score = 0  # Initialize the player's score at the start of each game
    continue_playing = True  # Flag to control the current game session

    # Inner loop for a single continuous play session
    while continue_playing:
        print(logo)  # Display the game logo at the beginning of each round

        # Randomly select two unique individuals from the dataset
        random_choice_for_a = randint(0, len(data) - 1)
        random_choice_for_b = randint(0, len(data) - 1)

        # Ensure that A and B are not the same entry
        while random_choice_for_a == random_choice_for_b:
            random_choice_for_a = randint(0, len(data) - 1)

        # Display data for the first comparison option
        print(
            f"Compare A: {data[random_choice_for_a]['name']}, "
            f"a {data[random_choice_for_a]['description']}, "
            f"from {data[random_choice_for_a]['country']}."
        )

        print(vs)  # Display the "vs" ASCII art for visual separation

        # Display data for the second comparison option
        print(
            f"Compare B: {data[random_choice_for_b]['name']}, "
            f"a {data[random_choice_for_b]['description']}, "
            f"from {data[random_choice_for_b]['country']}."
        )

        # Prompt the user for input and ensure valid response
        user_answer = str(input("Who has more followers? Type 'A' or 'B': ")).upper()
        while user_answer not in ['A', 'B']:
            user_answer = str(input("Who has more followers? Type correctly 'A' or 'B': ")).upper()

        # Determine which option (A or B) has the higher follower count
        if data[random_choice_for_a]['follower_count'] > data[random_choice_for_b]['follower_count']:
            correct_answer = 'A'
        else:
            correct_answer = 'B'

        # Compare user input with the correct answer
        if user_answer == correct_answer:
            user_score += 1  # Increment score for correct guess
            print("\n" * 100)  # Simulate screen clearing by printing blank lines
            print(f"Congratulations! You got it! Current score: {user_score}")
        else:
            # End the current session due to incorrect guess
            print(f"Sorry, that's not the right answer. Final score: {user_score}")
            continue_playing = False

            # Prompt the user to decide whether to start a new game
            start_a_new_game = str(input("Would you like to start a new game? Type 'y' or 'n': ")).lower()
            while start_a_new_game not in ["y", "n"]:
                start_a_new_game = str(input("Would you like to start a new game? Type correctly 'y' or 'n': ")).lower()

            if start_a_new_game == "y":
                start_a_new_game = True
                print("\n" * 100)  # Clear the screen before restarting
            else:
                start_a_new_game = False
                print("Hope you enjoyed! :)")
