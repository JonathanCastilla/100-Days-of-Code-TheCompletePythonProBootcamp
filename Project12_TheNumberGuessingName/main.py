'''
Project Number: 12
Project Name: The Number Guessing Game
Description:
    This program implements a simplified, text-based number guessing game.
    The computer generates a random integer between 1 and 100, and the player
    must attempt to guess it within a limited number of attempts. The difficulty
    level chosen by the player ('easy' or 'hard') determines the number of
    available attempts. The program provides interactive feedback on whether
    the guesses are too high or too low until the player succeeds or runs out
    of attempts. Upon completion, the player is prompted to decide whether
    to play again.
Author: Jonathan Eduardo Castilla Zamora
'''

from art import logo   # Importing ASCII art logo from an external file for better aesthetics
import random          # Importing Python's built-in library for generating random numbers

# Boolean control variable to allow repeated play until the user decides to stop
continue_playing = True

# Main program loop: executes the game repeatedly while the user chooses to continue
while continue_playing:
    print(logo)  # Displaying the logo/artwork at the start of each game session

    # Initial welcome message and explanation of the task
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # The program generates a random integer between 1 and 100, which becomes the target number
    number_to_guess = random.randint(1, 100)

    # The user selects a difficulty level, which determines the number of available attempts
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()

    # Input validation: ensures that only 'easy' or 'hard' are accepted
    while difficulty not in ['easy', 'hard']:
        difficulty = str(input("Choose a difficulty. Type correctly 'easy' or 'hard': ")).lower()

    # Assigning number of attempts according to difficulty level
    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    print(f"You have {str(attempts)} attempts remaining to guess the number.")

    # Secondary loop: runs as long as the player still has attempts left
    still_attempts = True
    while still_attempts:
        user_guess = input("Make a guess: ")

        # Validation: ensures the user inputs only numeric values (positive integers)
        while not user_guess.isnumeric():
            user_guess = input("Type correctly your guess. It must be a positive integer number: ")

        user_guess = int(user_guess)  # Converting input string into integer for comparison

        # Providing real-time feedback based on the guess
        if user_guess > number_to_guess:
            print("Your guess is too high.")
            print(f"You have {str(attempts)} attempts remaining to guess the number.")
        elif user_guess < number_to_guess:
            print("Your guess is too low.")
            print(f"You have {str(attempts)} attempts remaining to guess the number.")
        elif user_guess == number_to_guess:
            print(f"You got it! The number was: {number_to_guess}")
            break  # The loop terminates if the correct number is guessed

        # Decreasing the remaining attempts after each unsuccessful guess
        attempts -= 1

        # If the player runs out of attempts, the round ends
        if attempts == 0:
            print("You've run out of guesses.")
            still_attempts = False

    # After the game ends, the player decides whether to play again
    continue_playing = str(input("Would you like to play again? Type (y/n): ")).lower()

    # Input validation: ensures only 'y' or 'n' are accepted
    while continue_playing not in ['y', 'n']:
        continue_playing = str(input("Would you like to play again? Type correctly (y/n): ")).lower()

    # If the player chooses 'y', a new game session begins
    if continue_playing == 'y':
        continue_playing = True
        print("\n" * 100)  # Clears the screen by printing empty lines
    else:
        continue_playing = False
        print("Thank you for playing! Hope you enjoyed!")
