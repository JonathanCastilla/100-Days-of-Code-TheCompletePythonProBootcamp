'''
No. project: 7
Name project: Hangman Game
Description: This program implements a text-based version of the classic Hangman game.
             A random word is selected from a predefined word list, and the player
             must guess letters within a limited number of lives. Each incorrect guess
             reduces the available lives and progresses the hangman ASCII art.
             The game ends when the player either guesses the full word (win)
            o r runs out of lives (loss).
Author: Jonathan Eduardo Castilla Zamora
'''


# Importing required libraries and external modules
import random  # Provides functions to generate random choices
from hangman_words import word_list  # Imports the predefined list of words for the game
from hangman_art import stages, logo  # Imports ASCII art for hangman stages and the game logo

# Initialize the number of lives (equal to the number of stages minus one)
lives = len(stages) - 1

# Display the logo of the game
print(logo)

# Randomly select a word from the imported word list
chosen_word = random.choice(word_list)
# (Optional) For debugging purposes, the following line can be uncommented to display the chosen word
# print(chosen_word)

# Create a placeholder string with underscores representing each letter of the chosen word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Initialize game state variables
game_over = False  # Boolean flag to control the game loop
correct_letters = []  # Stores correctly guessed letters

# Main game loop, continues until the game is won or lost
while not game_over:
    # Display the number of lives remaining
    print("****************************" + str(lives) + "/6 LIVES LEFT****************************")

    # Prompt the player to guess a letter, converting input to lowercase
    guess = input("Guess a letter: ").lower()

    # Initialize the string that will display the current state of the guessed word
    display = ""

    # Iterate over each letter in the chosen word
    for letter in chosen_word:
        if letter == guess:
            # If the guessed letter matches, reveal it and record it as correct
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            # If the letter has already been correctly guessed earlier, reveal it again
            display += letter
        elif letter in display:
            # (Redundant condition, since display is being built here) 
            print("You have already guessed that letter: " + letter)
        else:
            # If the letter has not yet been guessed, keep it hidden as "_"
            display += "_"

    # Display the current progress of the word
    print("Word to guess: " + display)

    # If the guessed letter is not in the chosen word, reduce a life
    if guess not in chosen_word:
        lives -= 1
        print("Sorry, you guessed letter '" + guess + "', that is not in the word. You lose a life.")

        # Check if the player has lost all lives
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print("The correct word was: " + chosen_word)

    # If the word has been completely guessed (no underscores remain), declare a win
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Display the current stage of the hangman according to remaining lives
    print(stages[lives])
