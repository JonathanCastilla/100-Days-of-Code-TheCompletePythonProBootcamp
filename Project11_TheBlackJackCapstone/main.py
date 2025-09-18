'''
Project Number: 11
Project Name: The Blackjack Capstone Project
Description:
    This program implements a simplified, text-based version of the Blackjack card game.
    The player competes against the computer (dealer) by drawing cards, aiming to achieve
    a score as close as possible to 21 without exceeding it. The program includes input
    validation, decision-making prompts for the player, and a basic decision strategy
    for the computer. Game outcomes such as win, lose, or draw are displayed interactively.
Author: Jonathan Eduardo Castilla Zamora
'''

# Importing required libraries
import random        # Provides functionality to randomly select cards
from art import logo # ASCII art logo for a visual introduction

# Representation of possible cards in Blackjack.
# The Ace is represented as 11, numbers 2-10 are included,
# and the face cards (Jack, Queen, King) are represented as 10.
cards = [11] + list(range(2, 11)) + [10, 10, 10]

# Display ASCII art logo for better user experience.
print(logo)

# Ask the user if they want to play the game. Input validation ensures proper responses.
continue_playing = str(input("Do you want to play a game of Blackjack? (y/n): ")).lower()
while continue_playing not in ["y", "n"]:
    continue_playing = str(input("Do you want to play a game of Blackjack? Type correctly (y/n): ")).lower()

# Convert user input into a Boolean for easier use in the main loop.
if continue_playing == "y":
    continue_playing = True
else:
    continue_playing = False

# Main game loop – runs as long as the player wishes to continue playing.
while continue_playing:

    # Both the player and the computer start with two cards.
    number_of_player_cards = 2
    number_of_computer_cards = number_of_player_cards

    # Boolean flag to track if the player decides to draw another card.
    getting_another_card = True

    # Generate initial hands by randomly choosing cards from the deck.
    player_cards = [random.choice(cards) for _ in range(number_of_player_cards)]
    player_score = sum(player_cards)

    computer_cards = [random.choice(cards) for _ in range(number_of_computer_cards)]
    computer_score = sum(computer_cards)

    # Player decision loop: allows the player to keep drawing cards until they stop or exceed 21.
    while getting_another_card:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer first card: {computer_cards[0]}")  # Dealer shows only the first card

        # Ask the player whether to draw another card or pass.
        getting_another_card = str(input("Type 'y' to get another card, 'n' to pass: ")).lower()

        # Input validation for decision
        while getting_another_card not in ["y", "n"]:
            getting_another_card = str(input("Type correctly 'y' to get another card or 'n' to pass: ")).lower()

        if getting_another_card == "y":
            # If player chooses to draw another card
            getting_another_card = True
            player_cards.append(random.choice(cards))  # Add a new card to player
            player_score = sum(player_cards)           # Update the score

            # Computer strategy: draws another card if score <= 16 (simplified dealer rule)
            if computer_score <= 16:
                computer_cards.append(random.choice(cards))
                computer_score = sum(computer_cards)

        else:
            # Player chooses to stop drawing cards.
            getting_another_card = False
            print(f"Your final hand: {player_cards}, final score: {player_score}")
            print(f"Computer final hand: {computer_cards}, final score: {computer_score}")

    # Outcome determination – compares player and computer scores with Blackjack rules.
    if player_score > 21 >= computer_score:
        print(f"You lose. :(")  # Player busts
    elif player_score <= 21 and (player_score > computer_score or computer_score > 21):
        print(f"You win. :)")   # Player closer to 21 or dealer busts
    elif player_score == computer_score:
        print(f"It's a draw. :0")  # Tie game
    elif 21 < computer_score <= player_score or 21 < player_score <= computer_score:
        print(f"Nobody wins. :(")  # Both bust
    else:
        print(f"You lose. :(")     # Dealer closer to 21

    # Ask the user whether they want to start a new game or exit.
    continue_playing = str(input("Do you want to play a game of Blackjack? (y/n): ")).lower()
    while continue_playing not in ["y", "n"]:
        continue_playing = str(input("Do you want to play a game of Blackjack? Type correctly (y/n): ")).lower()

    if continue_playing == "y":
        continue_playing = True
        print("\n" * 100)  # Clear the console by printing new lines
        print(logo)        # Display the logo again
    else:
        continue_playing = False
        print("Thank you for playing! Hope you enjoy!")
